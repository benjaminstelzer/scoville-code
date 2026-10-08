# Shared writing rules

Apply these rules to plans, decisions, instructions, agent messages, handoffs,
reviews and reports. Preserve the required output schemas and delivery contracts.

When saving composed or transferred text, use a literal-safe UTF-8 file-write
or patch operation. Do not interpolate the content into shell commands or
`python -c` code. Finish and verify the saved content before any dependent
command. A preparation failure stops that command. Existing write permissions
still apply.

Never truncate text, including command and combined tool output. Apply only
declared or explicitly selected output limits. If none applies to this result
channel, do not invent a limit or require a numeric size check. A known inner
or outer limit still applies; check the complete combined output against the
smallest applicable limit. Measure all content your commands and orchestration
script emit into one outer tool result, including forwarded metadata, labels,
separators and combined results. Several inner calls or `text()` calls in one
outer call share that result's budget. The checker measures this content; it
does not measure opaque host-added framing or guarantee provider-specific token
counts. Before the first potentially large file read, use
the bundled checker with:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<file-to-read>" --max-output-tokens <limit> --part 1`.
It validates the complete UTF-8 file and includes its label in the budget:
`part=N bytes=start:end/total next=M` names the next `--part M`;
`last` replaces `next=M` only when end equals total. Read through `last`.
Read every unchanged part before dependent work. Use separate outer tool calls
unless their complete combined output has been measured and fits. An error leaves
the read incomplete, even when a tiny budget cannot fit a diagnostic. With no
limit, read complete UTF-8 directly. Without Python, use
the manual fallback listed in [Runtime helpers](../SKILL.md#runtime-helpers). A missing helper
or helper error does not enable it. Do not alter or copy the input, request an oversized full read, or recover
omitted text after truncation.

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

Capture potentially large command output before displaying it, including
diagnostics. With Python, use the existing checker for a permitted native command:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --max-output-tokens <limit> --run -- <command> <arguments>`.
Start Python text producers with `-X utf8`. The helper runs argv without a shell,
captures complete stdout and stderr, validates UTF-8 and measures the whole
rendered output including status and labels. Grouped streams do not establish
their chronological order. It preserves the child's exit status; signal exits
use `128 + signal` with the original status in the output. Its own failures use
125 and stop dependent work. `output_complete=false` means required content was
withheld, even if the command returned 0. Never treat that as a complete read.
For needed output from a safely repeatable read-only query, a role allowed to save it may rerun the query
once with `--publish-full --project-root "<workspace>"` before `--run`, then read
the complete file with `--part`. Read-only roles narrow the query only when every
required fact remains included, or report the missing input.
For effects or nonreproducible required output, choose an allowed
`--publish-full --project-root "<workspace>"` before `--run` on the first call.
It saves valid UTF-8 output from that same execution. Invalid UTF-8 stops with 125
and is not saved; configure the producer for UTF-8 first. Never rerun such a command
merely to add saving. This grants no new command or write rights. Reviewers must
not capture sources to a file for their own reading; the manager supplies needed
large inputs. For other shell output, preserve its own status and complete UTF-8
bytes before display. PowerShell `Out-String` formats objects and POSIX command
substitution removes trailing newlines. Neither preserves arbitrary raw output.
A capture failure, decoding error or replacement character introduced relative
to the source stops dependent work.
Before emitting large text, check the complete planned output, including combined
results and labels. For captured output in memory, count its complete rendered
UTF-8 bytes directly against `floor(limit_in_tokens * 4 / 5)`, without writing a
file. With an existing or permissibly prepared UTF-8 file, invoke the verified
Python interpreter with the following
arguments, preserving each quoted path as one argument. Keep a launcher such as
`py -3` as two unquoted tokens. Quote an executable path; in PowerShell, prefix
that quoted path with `&`:
`<verified-python> -X utf8 "<skill-directory>/scripts/check_text_size.py" --file "<text>" --max-output-tokens <limit>`,
using the smallest applicable declared or explicitly overridden output limit.
If the conservative budget is exceeded, compact wording and remove only
irrelevant material while preserving required facts and safeguards. If it still
cannot fit, use `--publish-full --project-root "<workspace>"` to publish the complete
unchanged text. Published files are temporary delivery artifacts. Use another
agent's artifact as evidence only when explicitly supplied, and never stage or
commit these artifacts. Send the published file's absolute path and SHA-256 and instruct the recipient
to verify the hash and read the entire file before dependent work. Decode files
and emit text explicitly as UTF-8. If portions are needed, keep their order,
split at character boundaries, and check each complete rendered output including
labels and combined results. Hash verification alone is not reading.

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

Preserve the result, scope, prerequisites, decisions, permissions, boundaries
and acceptance criteria. Supply needed facts directly or through exact,
accessible sources with an explicit reading instruction. Never assume hidden
conversation history. Keep current state, dependencies, binding constraints,
decision reasons, evidence limits and next actions when needed to assess or
continue correctly.

Say whether the entire requested task is complete. Report the required checks
and their actual results. Name any specific missing inputs or decisions.
Continue authorized work. Apart from the explicit delivery-artifact exception,
a question or assessment alone authorizes no change, and writing rules change
no task risk, required model, role or authority.

Use the shortest wording Luna can understand on first reading. Write complete
sentences with a verb or imperative. Use one term per meaning and plain words
before jargon. Avoid slash chains in prose; preserve literal paths, commands,
field names and other technical syntax.

Keep each rule at its responsible source. Remove repetition and low-value
maintenance detail, not required context or safeguards. Keep records only when
needed for further development or an independently binding requirement. Reviews
serve development; do not archive their text. A concise record that a required
review occurred is sufficient. Do not reconstruct a complete project history,
duplicate Steps as prose, or create documentation solely to prove bookkeeping.
A TL;DR cannot replace necessary explanation. Use paragraphs, lists or
a compact diagram when they clarify the decision; preserve useful diagrams.

For longer work, briefly report meaningful findings and next actions. Make the
final result, actual checks and remaining limits understandable on their own.
Length alone proves neither effectiveness nor performance.

For adviser work, these rules govern generated framing and answers. Do not
stylistically rewrite literal user questions, quotations, technical data or
hidden expectation keys. Explicitly requested content edits and required secret
redaction retain their own authority.
