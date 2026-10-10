# Shared writing rules

Apply these rules to plans, decisions, instructions, agent messages, handoffs,
reviews and reports. Preserve the required output schemas and delivery contracts.

When saving composed or transferred text, use a literal-safe UTF-8 file-write
or patch operation. Do not interpolate the content into executable code. Finish and verify saved
content before any dependent command. A preparation failure stops that command. Existing write permissions
still apply.

Never truncate text, including command and combined tool output. The checker
measures the complete emitted text, not opaque host framing or exact provider
token counts.

Attribute truncation only to the layer supported by the evidence. A shortened
later query does not prove that the original capture was truncated. If the
model-visible output or effective host cap is unknown, leave the host cause
unconfirmed and use the existing complete-output recovery.

## Large reads

Without an applicable limit, read complete UTF-8 directly; invent no budget.
With an applicable limit:

1. Use the smallest declared or explicitly selected limit of the command and
   every enclosing tool output. Read separately unless the complete combined output,
   including labels and metadata, is measured and fits; combined reads share
   that budget.
2. If the file may exceed that limit, use the verified Python interpreter and
   bundled reader:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<document>" --max-output-tokens <limit> --part 1`.
   It validates the complete UTF-8 file and budgets labels too.
   Python runs the full checker path `<skill-directory>/scripts/check_text_size.py`
   after `-X utf8`. The checker reads every document only through `--file`, including
   SKILL.md files and references of any Skill, assignments, and `.py` files read as
   text. Keep the verified launcher, checker path and quoting unchanged. Copy the
   last correct complete command: change only `--part` for the reported next part;
   for another document change only `--file` and reset `--part` to 1.
3. For multipart output, follow `part=N bytes=start:end/total next=M` with
   `--part M` through `last`,
   where end equals total. Read every unchanged part in order before dependent
   work. Use one limit for the whole sequence. If an applicable limit changes,
   restart at part 1 with the new smallest limit; never raise a binding limit
   to keep the old sequence.

Reader parts are already bounded. Execute the supplied reader command unchanged;
do not wrap it in `--run`, add `--publish-full`, or save its output.

A reader error leaves the read incomplete, even if its diagnostic cannot fit.
Correct a visible cause and restart at part 1. Do not repeat an unchanged failed
call or raise a binding limit. Otherwise report the unread document and stop
dependent work.
Do not alter or copy the input, truncate it or recover omitted text after an
oversized read.

To check a supplied expected SHA-256, use the same checker with
`--file "<artifact>" --sha256 --max-output-tokens <limit>` and compare its
`sha256` with the supplied value. A mismatch or error stops dependent work.
Then read the same unchanged file from `--part 1` through `last` with the same
limit. Hash verification is not reading; ordinary sources need no extra hash check.

Without suitable Python 3.11+, use
the manual fallback listed in [Runtime helpers](../SKILL.md#runtime-helpers). A missing helper
or helper error does not enable it.
If commands are forbidden, use the host's permitted UTF-8 reader in ordered
ranges within its limits. This replaces no required helper operation. Name any
required unread input and stop the work depending on it.

## Shell commands

Before running shell commands, follow [shell command rules](shell-commands.md).

Capture potentially large command output, including diagnostics, before display.
For a permitted command use:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --max-output-tokens <limit> --run -- <command> <arguments>`.
Start Python text producers with `<verified-python> -X utf8`. To capture one, use
`--run -- <verified-python> -X utf8 "<helper.py>" <all documented arguments>`;
the outer Python runs only the checker. The helper runs argv without a shell,
captures both streams completely, validates UTF-8 and measures rendered status
and labels too. Grouped streams do not prove chronological order. It preserves
the child's exit status; signals use `128 + signal` and report the original
status. Helper failures use 125 and stop dependent work. So does withheld required
content marked `output_complete=false`, even with exit 0.

Choose capture before execution:

| Command or role | Capture route |
| --- | --- |
| Effects or nonreproducible output | Configure UTF-8 and choose allowed `--publish-full --project-root "<workspace>"` before the first `--run`. Never repeat effects to save output. |
| Safely repeatable read-only query | One rerun with that option is allowed only when the current role and phase permit writing this temporary capture file. |
| Saving is not permitted | Narrow only while retaining every required fact, or report the missing input. |
| Reviewer reading sources | Use the bounded reader; do not save source captures. The manager supplies large inputs. |

Publication saves complete UTF-8 from that execution. Invalid UTF-8 fails with
125 without saving.

Preserve command status and complete UTF-8 bytes before display. Capture or
decoding failure, or replacement characters introduced relative to the source,
stop dependent work.

Prepare large text for delivery:

1. Finish the complete rendered output, including labels and combined results.
2. Without an applicable declared or explicitly selected limit, emit complete
   UTF-8 directly; invent no budget or numeric check.
3. With a limit, use the smallest applicable limit. In memory, compare UTF-8
   bytes with `floor(limit_in_tokens * 4 / 5)` without saving. For an existing
   or permissibly prepared file use:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<text>" --max-output-tokens <limit>`.
   Keep each quoted path one argument and launcher tokens such as `py -3` separate.

4. If exceeded, compact wording and remove irrelevant material while preserving
   required facts and safeguards.
5. If it still cannot fit, publish complete unchanged text with
   `--publish-full --project-root "<workspace>"`. Send the absolute path, SHA-256
   and an instruction to verify the hash and read the entire file under the
   reader rule before dependent work. Hash verification alone is not reading.

These artifacts are temporary: never stage or commit them. Use another agent's
artifact as evidence only when explicitly supplied.

If the active role's transfer contract independently permits file delivery,
publish without a size check when no content limit applies; omit
`--max-output-tokens` and make no fit claim.

If your role cannot run commands or write files, compact your answer without
losing required content and return the complete text through its permitted
result channel. The caller must capture the complete result and apply the size
check or complete-file route before displaying it through a limited tool output.
These rules grant no additional command or write permission. Role instructions
own any necessary delivery exception. If a known cap on that result channel itself
prevents complete delivery, report the concrete transport limitation.

Write for the actual recipient. All internal agent communication, including
assignments, steering, questions, results, reviews and handoffs, uses minimal
clearly labelled fields, not conversational status prose. Send only facts needed
for the next correct decision or action: result, decisive evidence, concrete
defect or blocker, unresolved limit and necessary next permitted action.
Omit narration, recaps, unchanged settings, history and known procedures unless
the recipient needs them or a contract requires them. Use unambiguous labels
and actions; no unexplained abbreviations or invented protocol tokens.

Treat an uncertain recipient as fresh. Supply every required fact and constraint
directly or through exact accessible sources with an explicit reading instruction;
assume no hidden history. Preserve required schemas, statuses, exact control
messages and user relay text, identities, permissions, stops, quiescence and
complete-delivery contracts unchanged. Keep required facts when rewriting or
transferring content.

Human-addressed text, including unchanged user relay bodies, follows the direct
user question and its delivery contract. A final user report states whether the
whole requested task is complete, required checks and actual results, and specific
missing inputs or decisions. Continue authorized work. During longer work, give
the user brief material findings and next actions. Make the final user report
understandable on its own.
Writing rules change no task risk, required model, role or authority. Questions
and assessments authorize no changes.

Skill, reference, Plan, Decision and builder-fixed instruction text and
human-addressed explanations use the shortest wording that even simpler models,
such as Luna, Haiku or Gemini, understand on first reading: complete sentences
with a verb or imperative, one term per meaning and plain words before jargon.
Composed internal fields need not be complete sentences but keep one term per
meaning.
Avoid slash chains in prose; preserve literal paths, commands, field names and
technical syntax. Length alone proves neither effectiveness nor performance.

Keep each rule at its responsible source. Remove repetition and low-value
maintenance detail while preserving required context and safeguards. Retain
records only when needed for development or an independently binding requirement.
Record that required reviews occurred; do not archive their text, reconstruct a
complete history, duplicate Steps as prose or document solely for bookkeeping.
A TL;DR cannot replace necessary explanation. Use paragraphs, lists or compact
diagrams when they clarify decisions; preserve useful diagrams.

For adviser work, apply these rules to generated framing and answers. Do not
stylistically rewrite literal user questions, quotations, technical data or
hidden expectation keys. Explicitly requested edits and required secret redaction
retain their own authority.
