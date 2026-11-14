# Output capture and delivery

Run commands and emit text directly unless a row of this table applies. Then
use the bundled checker; with `--publish-full` it saves the complete output where a display limit would cut it.

| Situation | Call |
| --- | --- |
| A command's output may exceed the tool's display limit | Capture |
| Composed text must fit a known output limit | Size check |
| Complete text would not fit, or the role's delivery contract permits or asks for a file | Publish |

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

## The three calls

**Capture.** Choose it before the first execution, because output lost to a
display limit cannot be recovered from a command that must not run twice.

```text
<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" [--max-output-tokens <limit>] [--publish-full --project-root "<workspace>"] [--timeout-seconds <seconds>] --run -- <command> <arguments>
```

- Put checker options before `--run`. The checker runs the argv without a
  shell, so it expands no wildcards or pipes; start a Python child as
  `<verified-python> -X utf8 <script>`. Keep quoted paths as single arguments
  and launcher tokens such as `py -3` separate.
- `<limit>` is the smallest applicable declared output limit or an explicit
  override. Omit it when none is known; a guessed budget produces a false fit.
- Where writing is permitted, add `--publish-full --project-root` whenever the
  output may exceed the limit or the command must not run twice; a limit alone
  discards output that does not fit. Pass the limit, `--publish-full` or both.
- With a limit, fitting output returns inline and, with `--publish-full`,
  larger output is saved from the same execution. Without a limit,
  `--publish-full` always saves and returns metadata only.
- Stdin gives EOF and there is no default deadline. Add `--timeout-seconds`
  when the host cannot bound the wait.
- Machine data still goes through code before display. Run a repeatable
  producer inside the evaluating script, which the checker can capture; for a
  command with an effect, capture first and evaluate the saved file.

**Size check** for the complete composed text, labels and combined results
included, against the smallest applicable known limit:

```text
<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<text>" --max-output-tokens <limit>
```

Without a limit, emit the complete text directly. The check compares UTF-8
bytes with `floor(limit * 4 / 5)`; text held in memory can be compared the same
way without saving. It is a conservative proxy, not a token count, and does
not see host framing.

**Publish** complete unchanged text as a file and send its absolute path:

```text
<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<text>" --publish-full --project-root "<workspace>"
```

Published files live in `.scoville/temp`, where the checker adds a `.gitignore`
when none exists. They are temporary, stay out of commits and are never
overwritten. Publishing without a limit makes no fit claim. Tell the recipient
to process machine data in code and read required prose in full before work
that depends on the file.

A role that may not write files does not capture to files: it narrows the command to the facts it needs or asks the
assigning agent for the input.

## Read the result

| Result | Meaning and next step |
| --- | --- |
| `exit=<n> stdout_bytes=<n> stderr_bytes=<n>`, then `stdout:\n`, stdout, `\nstderr:\n` and stderr | Complete capture. `exit` is the child's status and the checker exits with it (a signal as `128 + signal`). The two streams are grouped, not interleaved in time. |
| JSON `"status": "complete_file"` from a capture | The complete output is in `full_file`, in the same layout; parse it by the header's byte counts, without decoding invalid bytes. Evaluate it there before dependent work. `output_complete: false` only says the inline copy was omitted. |
| `output_complete=false exit=<n>` without a file | The output was not delivered and stays unread. Narrow the command, or rerun with `--publish-full` when the command is safe to repeat. |
| Exit 125 with JSON `"status": "capture_failed"` on stderr | The checker could not complete the capture. Follow `instruction`. `error` names the cause, `full_file` holds what was saved (as `.bin`), `capture_complete` says whether that is the whole output, `process_id` names a process whose termination is unconfirmed. After `publication_failed`, `reason` gives the filesystem error and `capture_error` an earlier capture failure. |
| Exit 125 with a line `output_complete=false error=<cause> exit=<n>` | The same failure without a saved copy: the output is lost or incomplete, and `exit` is no result after `timeout` or `interrupted`. Do not guess an encoding. Rerun only a command that is safe to repeat. |
| `exit=125` or `"exit_code": 125` without `capture_failed` or `error=` | The child itself exited 125; the capture is complete. |
| JSON `"status": "fits_conservative_budget"` | Emit the text. |
| JSON `"status": "compact_required"` | Follow `instruction`: shorten wording and drop irrelevant material while keeping every required fact and safeguard; publish the complete text if it still cannot fit. Cutting text off is never the fix, because the reader cannot tell what is missing. |
| JSON `"status": "complete_file"` from a publish | Send `full_file` as described under Publish. |
| JSON `"status": "publication_failed"` | Follow `instruction`; `full_file`, when present, is a complete recovery copy. |

Exit 0 does not make missing, unread or undecodable output usable: work that
needs that output waits until it is recovered, while independent work goes on.
Replacement characters that the source does not contain mean the text was
damaged on the way and count like invalid UTF-8. A command that is still
running has no result yet: keep its handle and collect every chunk and the
final exit status.


## Claude Code output limits

Claude Code limits Bash output in characters (`BASH_MAX_OUTPUT_LENGTH`,
overridden by the setting `bashOutputMaxChars`), with different ceilings for
success and failure and with host framing on top. Check the effective
settings; that value is not a `--max-output-tokens` limit and supports no
claim of an inline fit. Without a known token limit and with write permission,
capture with `--publish-full` and no limit, then read the saved file rather
than the host's preview. See
[Claude Code output limits](https://code.claude.com/docs/en/tools-reference#output-limits).


