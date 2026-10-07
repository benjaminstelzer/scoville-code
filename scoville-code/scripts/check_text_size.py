#!/usr/bin/env python3
"""Check planned text against the declared complete tool-output limit without emitting it."""
import argparse
import json
import os
from pathlib import Path
import tempfile
import sys


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


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', type=Path, required=True,
                        help='UTF-8 file containing the complete planned output, including any combined results')
    parser.add_argument('--max-output-tokens', type=int,
                        help='actual smallest applicable command/outer tool-output limit, from the tool declaration or explicit override')
    parser.add_argument('--publish-full', action='store_true',
                        help="publish complete unchanged text when required content cannot fit or the active role's transfer contract independently requires file delivery")
    parser.add_argument('--project-root', type=Path,
                        help='existing absolute workspace, required only with --publish-full')
    args = parser.parse_args()
    if args.max_output_tokens is None and not args.publish_full:
        parser.error('--max-output-tokens is required for a size check: --file <text> --max-output-tokens <limit>; for independently required file delivery without a content limit: --file <text> --publish-full --project-root <existing-absolute-workspace>')
    if args.max_output_tokens is not None and args.max_output_tokens < 1:
        parser.error('--max-output-tokens must be positive; use the actual declared limit, not a guessed or increased value')
    if args.publish_full and (not args.project_root or not args.project_root.is_absolute() or not args.project_root.is_dir()):
        parser.error('--publish-full requires --project-root <existing-absolute-workspace>')
    if args.project_root and not args.publish_full:
        parser.error('--project-root requires --publish-full; omit it for a read-only size check')
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
