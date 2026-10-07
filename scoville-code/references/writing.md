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
smallest applicable limit. Apply this before the first file read that emits
potentially large text, including an assignment received by file path. Checking
the size does not emit the file. For a read, use the checker's size and
recommended_max_utf8_bytes, not its compaction or publication instruction. Read
the unchanged text in ordered, character-safe portions within that byte budget,
including output labels. Do not alter or copy the input, first request an
oversized full read, or recover omitted text after truncation.

Native Codex Ask advisers and Workflow children may discover the interpreter and
run the named text-size checker before reading potentially large text, including
when the interpreter and checker are outside the workspace. For necessary
oversized-answer or handoff delivery only, they may also run complete-file
publication commands and prepare temporary complete artifacts under the project's
`.scoville/temp`. Among these roles, reviewers must not
execute tests or change project files beyond these delivery artifacts. This
exception permits no other project writes and does not override host tool
restrictions or Workflow ownership and takeover gates.

Capture potentially large command output in full without displaying it. Before
emitting large text, check the complete planned output, including combined
results and labels. Invoke the verified Python interpreter with the following
arguments, preserving each quoted path as one argument. Keep a launcher such as
`py -3` as two unquoted tokens. Quote an executable path; in PowerShell, prefix
that quoted path with `&`:
`<verified-python> "<skill-directory>/scripts/check_text_size.py" --file "<text>" --max-output-tokens <limit>`,
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
