# Output capture and delivery

Apply [shell-command rules](shell-commands.md) for commands and
[machine-data.md](machine-data.md) for machine output. This route governs
transport; a capture or size pass does not permit raw-data display.
File readers choose their permitted method and read required prose completely.

## Runtime helpers

Use the bundled helpers for their operations. Read their invocation instructions,
not their source, unless diagnosing a failure.

| Condition | Required route |
| --- | --- |
| Suitable Python 3.11+ is available | Use the bundled helper; do not load manual references. |
| No suitable Python 3.11+ | Read only the matching optional reference below. |
| Missing script, missing dependency or helper error | Stop the affected operation; this never enables the manual route. |

| Helper | Optional no-Python reference |
| --- | --- |
| `scripts/check_text_size.py` | [check_text_size](fallbacks/check_text_size-fallback.md) |

## Capture before execution

For potentially large command output, including diagnostics, use:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --max-output-tokens <limit> --run -- <command> <arguments>`.

The checker executes argv without a shell, captures both streams completely,
validates UTF-8 and measures rendered status and labels. Grouped streams do not
prove chronological order. It preserves child exit status; signals use
`128 + signal` and report the original status. Checker failures use 125 and
stop dependent work. Start Python producers with `-X utf8`, including after
`--run --`; the outer Python runs only the checker.

Run machine-data producers inside evaluating code that retains the complete
result or opens its `full_file` before emitting checked output. The checker
can capture that evaluator. For effects or nonreproducible output, preserve
the producer's identity, complete stdout, stderr and exit status in permitted
temporary files before evaluation; evaluator failure must not require rerunning it.

| Operation or role | Required capture choice |
| --- | --- |
| Effect or nonreproducible output | Configure UTF-8 and allowed `--publish-full --project-root "<workspace>"` before the first `--run`. |
| Safely repeatable read-only query | One rerun with that option is allowed only if the role and phase permit the temporary write. |
| Saving forbidden | Narrow while preserving all required facts, or report the missing input. |
| Reviewer reading sources | Read completely without saving source captures; the assigning agent supplies large inputs. |

With `--run`, fitting output is returned directly even with `--publish-full`;
larger output is saved from that execution. Direct machine output still needs
evaluation before display. Invalid UTF-8 fails with 125 without saving.
Replacement characters introduced relative to the source also stop dependent work.

A saved command capture contains `exit=<n> stdout_bytes=<n> stderr_bytes=<n>`,
then `stdout:\n`, stdout, `\nstderr:\n` and stderr. Parse using the byte counts
and UTF-8. JSON `"status": "complete_file"` with `full_file` identifies complete
saved output; `"output_complete": false` describes its omitted inline portion.
Open `full_file` and process the contents before dependent work. Without this
route, missing output or `output_complete=false` leaves required content unread.
A running command requires its handle, all chunks and final exit status.

## Prepare complete text

1. Finish the entire rendered output, including labels and combined results.
2. Without a declared or explicitly selected limit, emit complete UTF-8 directly;
   invent no budget or numeric check.
3. With a limit, use the smallest applicable one. In memory compare UTF-8 bytes
   with `floor(limit_in_tokens * 4 / 5)` without saving. For an existing or
   permissibly prepared file use:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<text>" --max-output-tokens <limit>`.
   Keep quoted paths as single arguments and launcher tokens such as `py -3`
   separate. This measures complete emitted text, not opaque host framing or
   exact provider token counts.
4. If exceeded, compact wording and remove irrelevant material while preserving
   required facts and safeguards; never truncate.
5. If necessary text still cannot fit, publish complete unchanged text with
   `--publish-full --project-root "<workspace>"`. Send the absolute path and
   instruct the recipient to process machine data in code and required prose
   in full before dependent work. Published files are never overwritten.

If the role's transfer contract independently permits file delivery, publish
without a size check when no limit applies; omit `--max-output-tokens` and make
no fit claim. These artifacts are temporary: never stage or commit them. Use
another agent's artifact as evidence only when explicitly supplied.

