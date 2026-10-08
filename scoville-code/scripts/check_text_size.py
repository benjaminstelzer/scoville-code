#!/usr/bin/env python3
"""Check text, read bounded UTF-8 parts, capture a command or publish complete text."""
import argparse
import json
import os
from pathlib import Path
import tempfile
import sys
import subprocess


def read_part(data, number, budget):
    """Return one complete, labelled UTF-8 portion within the output budget."""
    start = 0
    current = 1
    while True:
        def label(end):
            continuation = 'last' if end == len(data) else f'next={current + 1}'
            return f'part={current} bytes={start}:{end}/{len(data)} {continuation}\n'.encode('ascii')

        # The shorter final label can fit even when a nonfinal candidate cannot.
        if len(label(len(data))) + len(data) - start <= budget:
            end = len(data)
        else:
            low, high = start, min(len(data) - 1, start + budget)
            while low < high:
                middle = (low + high + 1) // 2
                if len(label(middle)) + middle - start <= budget:
                    low = middle
                else:
                    high = middle - 1
            end = low
        # Never split a UTF-8 character. Prefer a complete line when possible.
        while end < len(data) and end > start and data[end] & 0xc0 == 0x80:
            end -= 1
        if end < len(data):
            newline = data.rfind(b'\n', start, end)
            if newline >= start:
                end = newline + 1
        if len(label(end)) + end - start > budget or (end == start and start < len(data)):
            raise ValueError('output budget cannot fit the part label and next UTF-8 character')
        if current == number:
            return label(end) + data[start:end]
        if end == len(data):
            raise ValueError(f'--part exceeds the final part {current}')
        start, current = end, current + 1


class TextParser(argparse.ArgumentParser):
    part_budget = None
    capture_mode = False

    def exit(self, status=0, message=None):
        super().exit(125 if status and self.capture_mode else status, message)

    def error(self, message):
        if self.part_budget is None:
            super().error(message)
        # Never cut a diagnostic to make it fit. Exit status remains authoritative.
        diagnostic = ('error: ' + message + '\n').encode('utf-8')
        if len(diagnostic) <= self.part_budget:
            sys.stderr.buffer.write(diagnostic)
        self.exit(2)


def publish_full(root, data):
    import hashlib
    root = root.resolve()
    directory = (root / '.scoville' / 'temp').resolve()
    if not directory.is_relative_to(root):
        raise ValueError(f'.scoville/temp resolved to "{directory}" and must stay inside --project-root "{root}"; use a direct contained temporary directory')
    directory.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(data).hexdigest()
    target = directory / (digest + '.txt')
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=directory, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
        try:
            os.link(temporary, target)
        except FileExistsError:
            if target.is_symlink() or not target.is_file() or target.read_bytes() != data:
                raise ValueError(f'the hash-named target "{target}" is not the same regular file; do not overwrite it')
    finally:
        if temporary is not None:
            temporary.unlink()
    return str(target), digest


def capture_command(args):
    budget = args.max_output_tokens * 4 // 5
    command = args.run[1:] if args.run[:1] == ['--'] else args.run
    known_exit = None

    def error(message):
        for text in (f'output_complete=false error={message} exit={known_exit}\n',
                     f'output_complete=false error=capture exit={known_exit}\n'):
            encoded = text.encode('utf-8')
            if len(encoded) <= budget:
                sys.stderr.buffer.write(encoded)
                break
        return 125

    # Reject budgets unable to carry even a status before starting a command.
    minimum = b'output_complete=false exit=-2147483648\n'
    if args.publish_full:
        directory = (args.project_root.resolve() / '.scoville/temp').resolve()
        if not directory.is_relative_to(args.project_root.resolve()):
            return error('.scoville/temp escapes --project-root')
        minimum = (json.dumps({'status': 'complete_file', 'output_complete': False,
            'exit_code': -2147483648, 'full_file': str(directory / ('0' * 64 + '.txt')),
            'sha256': '0' * 64}, ensure_ascii=True) + '\n').encode('ascii')
    if len(minimum) > budget:
        return error('budget cannot fit complete status metadata')
    if not command:
        return error('--run requires a complete command argument list')
    if args.publish_full:
        try:
            directory.mkdir(parents=True, exist_ok=True)
        except OSError as failure:
            return error(f'--publish-full preparation failed at "{directory}": {failure}')
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        known_exit = result.returncode
        result.stdout.decode('utf-8', errors='strict')
        result.stderr.decode('utf-8', errors='strict')
        header = (f'exit={known_exit} stdout_bytes={len(result.stdout)} '
                  f'stderr_bytes={len(result.stderr)}\n').encode('ascii')
        rendered = header + b'stdout:\n' + result.stdout + b'\nstderr:\n' + result.stderr
        if args.publish_full:
            path, digest = publish_full(args.project_root, rendered)
            output = (json.dumps({'status': 'complete_file', 'output_complete': False,
                'exit_code': known_exit, 'full_file': path, 'sha256': digest}, ensure_ascii=True) + '\n').encode('ascii')
        elif len(rendered) <= budget:
            output = rendered
        else:
            output = (f'output_complete=false exit={known_exit} stdout_bytes={len(result.stdout)} '
                      f'stderr_bytes={len(result.stderr)}\n').encode('ascii')
            if len(output) > budget:
                output = f'output_complete=false exit={known_exit}\n'.encode('ascii')
        if len(output) > budget:
            return error('budget cannot fit complete status metadata')
        sys.stdout.buffer.write(output)
        # Retain the original signal in metadata and use its conventional shell status.
        return 128 - known_exit if known_exit < 0 else known_exit
    except (OSError, ValueError) as failure:
        return error(str(failure))


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    parser = TextParser(description=__doc__, allow_abbrev=False)
    options = sys.argv[:sys.argv.index('--run') + 1] if '--run' in sys.argv else sys.argv
    parser.capture_mode = '--run' in options
    if '--run' in options or '--part' in options or any(arg.startswith('--part=') for arg in options):
        for index, arg in enumerate(options):
            value = (options[index + 1] if arg == '--max-output-tokens' and index + 1 < len(options)
                     else arg.partition('=')[2] if arg.startswith('--max-output-tokens=') else None)
            if value is not None:
                try:
                    parser.part_budget = max(0, int(value) * 4 // 5)
                except ValueError:
                    pass
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--file', type=Path,
                        help='UTF-8 file containing the complete planned output, including any combined results')
    source.add_argument('--run', action='store_true',
                        help='capture the complete native command argv after --, without a shell or automatic retry; put checker options before --run')
    parser.add_argument('--max-output-tokens', type=int,
                        help='actual smallest applicable command/outer tool-output limit, from the tool declaration or explicit override')
    parser.add_argument('--publish-full', action='store_true',
                        help="publish complete unchanged text when required content cannot fit or the active role's transfer contract independently requires file delivery")
    parser.add_argument('--project-root', type=Path,
                        help='existing absolute workspace, required only with --publish-full')
    parser.add_argument('--part', type=int,
                        help='read this one-based unchanged UTF-8 portion within the declared output budget')
    # An optional argparse REMAINDER does not consume the -- separator. Split
    # the native argv explicitly so child options never become checker options.
    args = parser.parse_args(options[1:])
    args.run = sys.argv[sys.argv.index('--run') + 1:] if args.run else None
    if args.part is not None and (args.part < 1 or args.publish_full or args.project_root or args.run is not None):
        parser.error('--part must be positive and cannot be combined with --publish-full, --project-root or --run')
    if args.run is not None and (args.max_output_tokens is None or args.run[:1] != ['--'] or len(args.run) < 2):
        parser.error('--run requires --max-output-tokens <positive-limit> and -- followed by a complete command argument list')
    if args.max_output_tokens is None and not args.publish_full:
        parser.error('--max-output-tokens is required for a size check: --file <text> --max-output-tokens <limit>; for independently required file delivery without a content limit: --file <text> --publish-full --project-root <existing-absolute-workspace>')
    if args.max_output_tokens is not None and args.max_output_tokens < 1:
        parser.error('--max-output-tokens must be positive; use the actual declared limit, not a guessed or increased value')
    if args.publish_full and (not args.project_root or not args.project_root.is_absolute() or not args.project_root.is_dir()):
        parser.error('--publish-full requires --project-root <existing-absolute-workspace>')
    if args.project_root and not args.publish_full:
        parser.error('--project-root requires --publish-full; omit it for a read-only size check')
    if args.run is not None:
        return capture_command(args)
    try:
        data = args.file.read_bytes()
        data.decode('utf-8')
    except (OSError, UnicodeError) as error:
        parser.error(f'--file "{args.file}" must be a readable UTF-8 file; provide the complete UTF-8 planned output: {error}')
    if args.part is not None:
        try:
            output = read_part(data, args.part, args.max_output_tokens * 4 // 5)
        except ValueError as error:
            parser.error(str(error))
        sys.stdout.buffer.write(output)
        return 0
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
            'and send the returned absolute path and SHA-256 instead of a partial result.'
        )
    if args.publish_full:
        try:
            result['full_file'], result['sha256'] = publish_full(args.project_root, data)
        except (OSError, ValueError) as error:
            parser.error(f'complete-file publication failed: {error}')
        result['status'] = 'complete_file'
        result['instruction'] = 'Send this absolute path and SHA-256. It contains the complete unchanged text; the receiver must verify the SHA-256 and read the entire file at its permitted stage before dependent work.'
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
