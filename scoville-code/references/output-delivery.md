# Output capture and delivery

Apply the [shell-command guards](shell-commands.md).

File reading follows the shared writing rule; choose its method yourself.
For other commands, capture potentially large output, including diagnostics, before display.
For a permitted command use:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --max-output-tokens <limit> --run -- <command> <arguments>`.
Start Python text producers with `<verified-python> -X utf8`. To capture one, use
`--run -- <verified-python> -X utf8 "<helper.py>" <all documented arguments>`;
the outer Python runs only the checker. The helper runs argv without a shell,
captures both streams completely, validates UTF-8 and measures rendered status
and labels too. Grouped streams do not prove chronological order. It preserves
the child's exit status; signals use `128 + signal` and report the original
status. Helper failures use 125 and stop dependent work.

Choose capture before execution:

| Command or role | Capture route |
| --- | --- |
| Effects or nonreproducible output | Configure UTF-8 and choose allowed `--publish-full --project-root "<workspace>"` before the first `--run`. |
| Safely repeatable read-only query | One rerun with that option is allowed only when the current role and phase permit writing this temporary capture file. |
| Saving is not permitted | Narrow only while retaining every required fact, or report the missing input. |
| Reviewer reading sources | Read completely; do not save source captures. The manager supplies large inputs. |

With `--run`, complete output that fits is returned directly, even with
`--publish-full`; larger output is saved from that same execution. Invalid
UTF-8 fails with 125 without saving. Replacement characters introduced relative
to the source also stop dependent work.

Prepare large text for delivery:

1. Finish the complete rendered output, including labels and combined results.
2. Without an applicable declared or explicitly selected limit, emit complete
   UTF-8 directly; invent no budget or numeric check.
3. With a limit, use the smallest applicable limit. In memory, compare UTF-8
   bytes with `floor(limit_in_tokens * 4 / 5)` without saving. For an existing
   or permissibly prepared file use:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<text>" --max-output-tokens <limit>`.
   Keep each quoted path one argument and launcher tokens such as `py -3` separate.
   The checker measures the complete emitted text, not opaque host framing or
   exact provider token counts.

4. If exceeded, compact wording and remove irrelevant material while preserving
   required facts and safeguards.
5. If it still cannot fit, publish complete unchanged text with
   `--publish-full --project-root "<workspace>"`. Send the absolute path and an
   instruction to read the entire file before dependent work. Published files
   are never overwritten.

These artifacts are temporary: never stage or commit them. Use another agent's
artifact as evidence only when explicitly supplied.

If the active role's transfer contract independently permits file delivery,
publish without a size check when no content limit applies; omit
`--max-output-tokens` and make no fit claim.

