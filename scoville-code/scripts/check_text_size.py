#!/usr/bin/env python3
"""Check text size, capture a command or publish complete text."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import tempfile
import sys
import subprocess
import signal
import threading
import time


class PublicationError(OSError):
    def __init__(self, cause, recovery_file):
        super().__init__(str(cause))
        self.recovery_file = str(recovery_file)
        self.reason = f'{type(cause).__name__}:{getattr(cause, "errno", None)}'


class CaptureInterrupted(Exception):
    pass


class TextParser(argparse.ArgumentParser):
    output_budget = None
    capture_mode = False

    def exit(self, status=0, message=None):
        super().exit(125 if status and self.capture_mode else status, message)

    def error(self, message):
        if self.output_budget is None:
            super().error(message)
        # Never cut a diagnostic to make it fit. Exit status remains authoritative.
        diagnostic = ('error: ' + message + '\n').encode('utf-8')
        if len(diagnostic) <= self.output_budget:
            sys.stderr.buffer.write(diagnostic)
        self.exit(2)


def publish_full(root, data, suffix='.txt'):
    root = root.resolve()
    directory = (root / '.scoville' / 'temp').resolve()
    if not directory.is_relative_to(root):
        raise ValueError(f'.scoville/temp resolved to "{directory}" and must stay inside --project-root "{root}"; use a direct contained temporary directory')
    directory.mkdir(parents=True, exist_ok=True)
    # A content-derived name keeps one immutable file per text.
    target = directory / (hashlib.sha256(data).hexdigest() + suffix)
    temporary = None
    complete = False
    try:
        with tempfile.NamedTemporaryFile(dir=directory, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
        complete = True
        # Ignore creation must not lose the sole complete capture on failure.
        try:
            marker = os.open(directory / '.gitignore', os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_BINARY', 0))
        except FileExistsError:
            pass
        else:
            with os.fdopen(marker, 'wb') as stream:
                stream.write(b'*\n')
        try:
            os.link(temporary, target)
        except FileExistsError:
            if target.is_symlink() or not target.is_file() or target.read_bytes() != data:
                raise ValueError(f'the hash-named target "{target}" is not the same regular file; do not overwrite it')
        temporary.unlink()
    except (OSError, ValueError) as error:
        if complete:
            raise PublicationError(error, temporary) from error
        if temporary is not None:
            temporary.unlink()
        raise
    return str(target)


def collect_output(process, timeout):
    """Drain incrementally so a surviving pipe owner cannot hide captured bytes."""
    chunks = [[], []]
    failures = []
    lock = threading.Lock()

    def drain(stream, index):
        try:
            while data := stream.read1(65536):
                with lock:
                    chunks[index].append(data)
        except OSError:
            with lock:
                failures.append('capture_read_failed')
        finally:
            stream.close()

    readers = [threading.Thread(target=drain, args=(stream, index), daemon=True)
               for index, stream in enumerate((process.stdout, process.stderr))]
    for reader in readers:
        reader.start()
    deadline = None if timeout is None else time.monotonic() + timeout

    def remaining(end):
        return None if end is None else max(0, end - time.monotonic())

    failure = None
    def interrupted(signum, frame):
        raise CaptureInterrupted(signum)

    handled = (signal.SIGINT, signal.SIGTERM) + ((signal.SIGHUP,) if os.name != 'nt' else ())
    previous = {value: signal.signal(value, interrupted) for value in handled}
    try:
        process.wait(timeout=remaining(deadline))
        for reader in readers:
            reader.join(remaining(deadline))
        if any(reader.is_alive() for reader in readers):
            raise subprocess.TimeoutExpired(process.args, timeout)
    except (subprocess.TimeoutExpired, CaptureInterrupted, KeyboardInterrupt) as error:
        failure = 'timeout' if isinstance(error, subprocess.TimeoutExpired) else 'interrupted'
        for value in handled:
            signal.signal(value, signal.SIG_IGN)
        cleanup_failure = failure + '_cleanup_incomplete'
        try:
            if os.name == 'nt':
                killed = subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
                if killed.returncode:
                    failure = cleanup_failure
            else:
                os.killpg(process.pid, signal.SIGKILL)
        except (OSError, subprocess.TimeoutExpired):
            failure = cleanup_failure
        cleanup_deadline = time.monotonic() + 5
        if process.poll() is None:
            try:
                process.kill()
                process.wait(timeout=remaining(cleanup_deadline))
            except (OSError, subprocess.TimeoutExpired):
                failure = cleanup_failure
        for reader in readers:
            reader.join(remaining(cleanup_deadline))
        if any(reader.is_alive() for reader in readers):
            failure = cleanup_failure
        # A blocked reader owns its stream until EOF. Closing it here can wait
        # on the Windows buffered-reader lock and defeat the deadline.
    finally:
        for value, handler in previous.items():
            signal.signal(value, handler)
    with lock:
        return b''.join(chunks[0]), b''.join(chunks[1]), failure or (failures[0] if failures else None)


def capture_command(args):
    budget = args.max_output_tokens * 4 // 5 if args.max_output_tokens is not None else None
    command = args.run[1:] if args.run[:1] == ['--'] else args.run
    known_exit = None
    capture_complete = False
    failure_kind = None
    rendered = None
    process = None

    def fits(data):
        return budget is None or len(data) <= budget

    def error(message):
        for text in (f'output_complete=false error={message} exit={known_exit}\n',
                     f'output_complete=false error=capture exit={known_exit}\n'):
            encoded = text.encode('utf-8')
            if fits(encoded):
                sys.stderr.buffer.write(encoded)
                break
        return 125

    # Reject budgets unable to carry even a status before starting a command.
    minimum = b'output_complete=false exit=-2147483648\n'
    if args.publish_full:
        directory = (args.project_root.resolve() / '.scoville/temp').resolve()
        if not directory.is_relative_to(args.project_root.resolve()):
            return error('.scoville/temp escapes --project-root')
        minimum = (json.dumps({'status': 'capture_failed', 'error': 'publication_failed',
            'capture_error': 'timeout_cleanup_incomplete',
            'capture_complete': False, 'output_complete': False, 'process_id': 2147483647,
            'exit_code': -2147483648, 'reason': 'PermissionError:123456789',
            'instruction': 'Read full_file; correct publication conditions without rerunning the producer.',
            'full_file': str(directory / ('0' * 64 + '.txt'))},
            ensure_ascii=True) + '\n').encode('ascii')
    if not fits(minimum):
        return error('budget cannot fit complete status metadata')
    if not command:
        return error('--run requires a complete command argument list')
    if Path(command[0]).suffix.lower() == '.py':
        return error(
            'PYTHON_INTERPRETER_REQUIRED child_started=false: '
            'insert the verified Python executable and -X utf8 before the script; '
            'keep all existing arguments'
        )
    if args.publish_full:
        try:
            directory.mkdir(parents=True, exist_ok=True)
        except OSError as failure:
            return error(f'--publish-full preparation failed at "{directory}": {failure}')
    try:
        process = subprocess.Popen(command, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            start_new_session=os.name != 'nt')
        stdout, stderr, failure_kind = collect_output(process, args.timeout_seconds)
        capture_complete = failure_kind is None
        known_exit = process.returncode
        header = (f'exit={known_exit} stdout_bytes={len(stdout)} '
                  f'stderr_bytes={len(stderr)}\n').encode('ascii')
        rendered = header + b'stdout:\n' + stdout + b'\nstderr:\n' + stderr
        try:
            stdout.decode('utf-8', errors='strict')
            stderr.decode('utf-8', errors='strict')
        except UnicodeError:
            failure_kind = failure_kind or 'invalid_utf8'
        if failure_kind:
            if args.publish_full:
                metadata = {'status': 'capture_failed', 'error': failure_kind,
                    'capture_complete': failure_kind == 'invalid_utf8', 'output_complete': False,
                    'exit_code': known_exit,
                    'full_file': publish_full(args.project_root, rendered, '.bin')}
                if failure_kind == 'invalid_utf8':
                    metadata['instruction'] = ('Original bytes and child exit retained; UTF-8 interpretation is open. '
                        'Stop text-dependent work. Use only producer-established encoding; no replacement or producer retry.')
                if failure_kind.endswith('_cleanup_incomplete'):
                    metadata['process_id'] = process.pid
                output = (json.dumps(metadata,
                    ensure_ascii=True) + '\n').encode('ascii')
                if not fits(output):
                    return error('budget cannot fit complete failure metadata')
                sys.stderr.buffer.write(output)
                return 125
            return error(f'{failure_kind} process_id={process.pid}' if failure_kind == 'timeout_cleanup_incomplete' else failure_kind)
        if budget is not None and fits(rendered):
            output = rendered
        elif args.publish_full:
            metadata = {'status': 'complete_file', 'output_complete': False,
                'exit_code': known_exit, 'full_file': publish_full(args.project_root, rendered)}
            if budget is None:
                metadata['capture_complete'] = True
            output = (json.dumps(metadata, ensure_ascii=True) + '\n').encode('ascii')
        else:
            output = (f'output_complete=false exit={known_exit} stdout_bytes={len(stdout)} '
                      f'stderr_bytes={len(stderr)}\n').encode('ascii')
            if not fits(output):
                output = f'output_complete=false exit={known_exit}\n'.encode('ascii')
        if not fits(output):
            return error('budget cannot fit complete status metadata')
        sys.stdout.buffer.write(output)
        # Retain the original signal in metadata and use its conventional shell status.
        return 128 - known_exit if known_exit < 0 else known_exit
    except (OSError, ValueError) as failure:
        if rendered is None or not args.publish_full:
            return error(str(failure))
        recovery_file = getattr(failure, 'recovery_file', None)
        metadata = {'status': 'capture_failed', 'error': 'publication_failed',
            'reason': getattr(failure, 'reason', f'{type(failure).__name__}:{getattr(failure, "errno", None)}'),
            'capture_complete': capture_complete,
            'instruction': ('Read full_file; correct publication conditions without rerunning the producer.' if recovery_file else
                            'No saved copy exists. Correct storage conditions; do not rerun the producer without authority.'),
            'output_complete': False, 'exit_code': known_exit,
            'full_file': recovery_file}
        if failure_kind:
            metadata['capture_error'] = failure_kind
            if failure_kind.endswith('_cleanup_incomplete'):
                metadata['process_id'] = process.pid
        output = (json.dumps(metadata, ensure_ascii=True) + '\n').encode('ascii')
        if not fits(output):
            return error('budget cannot fit publication recovery metadata')
        sys.stderr.buffer.write(output)
        return 125


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    parser = TextParser(description=__doc__, allow_abbrev=False)
    options = sys.argv[:sys.argv.index('--run') + 1] if '--run' in sys.argv else sys.argv
    parser.capture_mode = '--run' in options
    if '--run' in options:
        for index, arg in enumerate(options):
            value = (options[index + 1] if arg == '--max-output-tokens' and index + 1 < len(options)
                     else arg.partition('=')[2] if arg.startswith('--max-output-tokens=') else None)
            if value is not None:
                try:
                    parser.output_budget = max(0, int(value) * 4 // 5)
                except ValueError:
                    pass
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--file', type=Path,
                        help='UTF-8 planned output for size check or publication')
    source.add_argument('--run', action='store_true',
                        help='capture the complete native command argv after --, without a shell or automatic retry; put checker options before --run')
    parser.add_argument('--max-output-tokens', type=int,
                        help='actual smallest applicable command/outer tool-output limit, from the tool declaration or explicit override')
    parser.add_argument('--publish-full', action='store_true',
                        help="with --run, save complete output if it cannot fit or no limit is supplied; with --file, explicitly publish complete unchanged text")
    parser.add_argument('--project-root', type=Path,
                        help='existing absolute workspace, required only with --publish-full')
    parser.add_argument('--timeout-seconds', type=float,
                        help='optional positive finite deadline for --run; timeout terminates its process family, preserves available output and never retries')
    # An optional argparse REMAINDER does not consume the -- separator. Split
    # the native argv explicitly so child options never become checker options.
    args = parser.parse_args(options[1:])
    args.run = sys.argv[sys.argv.index('--run') + 1:] if args.run else None
    if args.run is not None and (args.run[:1] != ['--'] or len(args.run) < 2):
        parser.error('--run requires -- followed by a complete command argument list; supply --max-output-tokens <positive-limit> or --publish-full --project-root <existing-absolute-workspace> before --run')
    if args.max_output_tokens is None and not args.publish_full:
        parser.error('--max-output-tokens is required for a size check: --file <text> --max-output-tokens <limit>; for independently required file delivery without a content limit: --file <text> --publish-full --project-root <existing-absolute-workspace>')
    if args.max_output_tokens is not None and args.max_output_tokens < 1:
        parser.error('--max-output-tokens must be positive; use the actual declared limit, not a guessed or increased value')
    if args.publish_full and (not args.project_root or not args.project_root.is_absolute() or not args.project_root.is_dir()):
        parser.error('--publish-full requires --project-root <existing-absolute-workspace>')
    if args.project_root and not args.publish_full:
        parser.error('--project-root requires --publish-full; omit it for a read-only size check')
    if args.timeout_seconds is not None and (args.run is None or not math.isfinite(args.timeout_seconds) or args.timeout_seconds <= 0):
        parser.error('--timeout-seconds requires --run and a positive finite number of seconds')
    if args.run is not None:
        return capture_command(args)
    try:
        data = args.file.read_bytes()
        data.decode('utf-8')
    except (OSError, UnicodeError) as error:
        parser.error(f'--file "{args.file}" must be a readable UTF-8 file; provide the complete UTF-8 planned output: {error}')
    # UTF-8 bytes are a conservative size proxy, not a model-specific token count.
    result = {'utf8_bytes': len(data)}
    if args.max_output_tokens is not None:
        target = args.max_output_tokens * 4 // 5
        fits = len(data) <= target
        result.update({
            'status': 'fits_conservative_budget' if fits else 'compact_required',
            'tool_output_limit_tokens': args.max_output_tokens,
            'recommended_max_utf8_bytes': target,
            'measurement': 'conservative UTF-8 byte budget, not an exact token count',
        })
    if args.max_output_tokens is not None and not fits:
        result['instruction'] = (
            f'The declared tool-output limit is {args.max_output_tokens} tokens. '
            f'This text exceeds the conservative budget of {target} UTF-8 bytes; this is not a measured token overflow. '
            f'Compact the planned text to at most {target} UTF-8 bytes before output. '
            'Remove only irrelevant information. Preserve every required fact and safeguard. '
            'Never truncate text or automatically increase the limit. '
            'If essential text cannot fit, use --publish-full --project-root <workspace> '
            'and send the returned absolute path instead of a partial result.'
        )
    if args.publish_full:
        try:
            result['full_file'] = publish_full(args.project_root, data)
        except PublicationError as error:
            print(json.dumps({'status': 'publication_failed', 'reason': error.reason,
                              'message': str(error), 'full_file': error.recovery_file,
                              'instruction': 'Read full_file; correct publication conditions without changing the original source.'}, ensure_ascii=True), file=sys.stderr)
            return 2
        except (OSError, ValueError) as error:
            parser.error(f'complete-file publication failed: {error}')
        result['status'] = 'complete_file'
        result['instruction'] = 'Send this absolute path. It contains the complete unchanged text. At its permitted stage, the receiver applies the shared reading rule: machine data in code, required prose in full, before dependent work.'
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
