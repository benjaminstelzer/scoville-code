# Shared writing rules

Apply these rules to plans, decisions, instructions, agent messages, handoffs,
reviews and reports. Preserve the required output schemas and delivery contracts.

When saving composed or transferred text, use a literal-safe UTF-8 file-write
or patch operation. Do not interpolate the content into shell commands or
`python -c` code. Finish and verify the saved content before any dependent
command. A preparation failure stops that command. Existing write permissions
still apply.

Never truncate text, including command and combined tool output. The checker
measures the complete emitted text, not opaque host framing or exact provider
token counts.

Attribute truncation only to the layer supported by the evidence. A shortened
later query does not prove that the original capture was truncated. If the
model-visible output or effective host cap is unknown, leave the host cause
unconfirmed and use the existing complete-output recovery.

Without an applicable limit, read complete UTF-8 directly; invent no budget.
With an applicable limit:

1. Use the smallest declared or explicitly selected limit for the read and
   enclosing output. Read separately unless the complete combined output,
   including labels and metadata, is measured and fits; combined reads share
   that budget.
2. If the file may exceed that limit, use the verified Python interpreter and
   bundled reader:
   `<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<document>" --max-output-tokens <limit> --part 1`.
   It validates the complete UTF-8 file and budgets labels too.
3. For multipart output, follow `part=N bytes=start:end/total next=M` with
   `--part M` through `last`,
   where end equals total. Read every unchanged part in order before dependent
   work. Keep the budget unchanged; otherwise restart at part 1.

A reader error leaves the read incomplete, even if its diagnostic cannot fit.
Do not alter or copy the input, truncate it or recover omitted text after an
oversized read.

The reader program is `scripts/check_text_size.py`; pass its document only as
`--file`. Only named `.py` files may be Python program files. SKILL.md, references
and assignments are documents, never programs.

Without suitable Python 3.11+, use
the manual fallback listed in [Runtime helpers](../SKILL.md#runtime-helpers). A missing helper
or helper error does not enable it.
If commands are forbidden, use the host's permitted UTF-8 reader in ordered
ranges within its limits. This replaces no required helper operation. Name any
required unread input and stop the work depending on it.

Native Codex Ask advisers and Workflow children may discover the interpreter and
run the named checker for bounded UTF-8 reads, command capture, size checks and
oversized-result delivery, including
when the interpreter and checker are outside the workspace. For necessary
oversized-answer or handoff delivery only, they may also run complete-file
publication commands and prepare temporary complete artifacts under the project's
`.scoville/temp`. Among these roles, reviewers must not
execute tests or change project files beyond these delivery artifacts. This
exception permits no other project writes and does not override host tool
restrictions or Workflow ownership and takeover gates.

Capture potentially large command output, including diagnostics, before display.
For a permitted command use:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --max-output-tokens <limit> --run -- <command> <arguments>`.
Start Python text producers with `-X utf8`. The helper runs argv without a shell,
captures both streams completely, validates UTF-8 and measures rendered status
and labels too. Grouped streams do not prove chronological order. It preserves
the child's exit status; signals use `128 + signal` and report the original
status. Helper failures use 125 and stop dependent work. So does withheld required
content marked `output_complete=false`, even with exit 0.

For effects or nonreproducible output, choose an allowed
`--publish-full --project-root "<workspace>"` before `--run` on the first call.
This saves complete UTF-8 output from that execution; invalid UTF-8 fails with
125 without saving. Configure UTF-8 first; never repeat effects merely to save
their output. A safely repeatable read-only query may be rerun once with that
option when the role may save it. Otherwise narrow the query only if all required
facts remain included, or report the missing input. Reviewers never capture
sources to files for their own reading; the manager supplies large inputs.

For other shell output, preserve status and complete UTF-8 bytes before display.
PowerShell `Out-String` formats objects; POSIX command substitution strips trailing
newlines. Neither preserves arbitrary raw output. Capture or decoding failure,
or replacement characters introduced relative to the source, stop dependent work.

Before emitting large text through a channel with a declared or explicitly
selected output limit, measure the complete rendered output, including
labels and combined results. Without an applicable limit, emit the complete
UTF-8 text directly; no numeric size check is due and no budget may be invented.
In memory, compare its UTF-8 byte count with
`floor(limit_in_tokens * 4 / 5)` without saving. For an existing or permissibly
prepared file use:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<text>" --max-output-tokens <limit>`,
Keep each quoted path one argument. Keep launcher tokens such as `py -3` separate;
quote an executable path and prefix it with `&` in PowerShell. Use the smallest
applicable declared or explicitly overridden limit. If exceeded, compact wording
and remove irrelevant material while preserving required facts and safeguards.
If it still cannot fit, publish the complete unchanged text with
`--publish-full --project-root "<workspace>"`. Send its absolute path and SHA-256,
instructing the recipient to verify the hash and read the entire file through
the reader rule above before dependent work. Hash verification alone is not
reading. These artifacts are temporary: never stage or commit them, and use
another agent's artifact as evidence only when explicitly supplied.

If the active role's transfer contract independently permits file delivery,
publish without a size check when no content limit applies; omit
`--max-output-tokens` and make no fit claim.

If your role cannot run commands or write files, compact your answer without
losing required content and return the complete text through its permitted
result channel. The caller must capture the complete result and apply the size
check or complete-file route before displaying it through a limited tool output.
Apart from the delivery-artifact exception above, these rules grant no additional
command or write permission. If a known cap on that result channel itself
prevents complete delivery, report the concrete transport limitation.

Preserve results, scope, prerequisites, decisions, permissions, boundaries and
acceptance criteria. Supply needed facts directly or through exact accessible
sources with an explicit reading instruction; assume no hidden history. Include
state, dependencies, binding constraints, decision reasons, evidence limits and
next actions needed for assessment or continuation.

Report whether the whole requested task is complete, required checks and actual
results, and specific missing inputs or decisions. Continue authorized work.
During longer work, briefly report meaningful findings and next actions. Make
the final result, checks and remaining limits understandable on their own.
Writing rules change no task risk, required model, role or authority. Apart from
the explicit delivery-artifact exception, questions and assessments authorize
no changes.

Use the shortest wording Luna understands on first reading: complete sentences
with a verb or imperative, one term per meaning and plain words before jargon.
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
