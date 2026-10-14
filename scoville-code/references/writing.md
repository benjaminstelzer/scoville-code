# Shared writing rules

Apply these rules to plans, decisions, instructions, agent messages, handoffs,
reviews and reports. Preserve the required output schemas and delivery contracts.

Fully read shared writing and shell rules of the same build count as loaded
across Suite Skills, including routes that name their writing reference. Reload
after an explicit reload, changed rules or build, or missing, incomplete or
uncertain retained text. Load newly needed specialized references normally.

When saving composed or transferred text, use a literal-safe UTF-8 file-write
or patch operation. Do not interpolate the content into executable code. Finish saving
before any dependent command. A preparation failure stops that command.

Never truncate text, including command and combined tool output. Do not blame
a specific tool or host for missing output unless evidence shows it. A
shortened later query does not prove that the original capture was truncated.
Recover the complete content first under the applicable reading or output rule.

## File reading

Read every required file completely before dependent work. Choose a permitted
method yourself. If a read is incomplete or fails, obtain the missing content.
If this is impossible, name the unread input and stop dependent work.

For machine reports, use permitted commands to parse the complete data and run
the required checks. Show only the checked collection and fields, decisive
values, results and all deviations within that scope. For collection checks,
show the processed and expected counts, not every passing path. Parsing alone
proves no result; read required text passages for their meaning. Parse errors,
missing required fields, wrong types or unsupported formats in the checked
scope prevent a pass. Do not replace a complete check with sampling. Roles
without command permission use the complete reading method above. Instructions,
original assignments, native finals and binding Plan or Decision text still
require complete reading; parsing does not replace it.

For operations other than file reading, read [shell rules and their conditional delivery route](shell-commands.md)
before shell commands, complete-file preparation or output that may exceed an
applicable limit.

If your role cannot run commands or write files, compact your answer without
losing required content and return the complete text through its permitted
result channel. The caller must capture the complete result and apply the
[size check or complete-file route](output-delivery.md)
before displaying it through a limited tool output. If a known cap on that
result channel itself prevents complete delivery, report the concrete transport
limitation.

Write for the actual recipient. Messages to agents, such as assignments,
steering, questions, results, reviews and handoffs, use short labelled fields,
not conversational prose. So does the visible commentary of an agent that does
not answer the user directly. Send only facts needed
for the next correct decision or action: result, decisive evidence, concrete
defect or blocker, unresolved limit and necessary next permitted action.
Omit narration, recaps, unchanged settings, history and known procedures unless
the recipient needs them or a contract requires them. Use unambiguous labels
and actions; no unexplained abbreviations or invented protocol tokens.

Treat an uncertain recipient as fresh; assume no hidden history. Supply every
fact and constraint needed for the next correct decision or action. For source
text the recipient can access and is permitted to read, give its exact path and
section with an explicit reading instruction instead of repeating it. State
other required facts directly. Quote only wording needed as decisive evidence
or required text from a source the recipient cannot read.
Preserve required schemas, statuses, exact control
messages and exact user wording, identities, permissions, stops, quiescence and
complete-delivery contracts unchanged. Keep required facts when rewriting or
transferring content.

Write text for the user in the language and format their current request asks
for; forward quoted user-facing text unchanged. A final user report states whether the
whole requested task is complete, required checks and actual results, and specific
missing inputs or decisions. Continue authorized work. An agent answering the
user directly gives brief material findings and next actions during longer work.
Make the final user report
understandable on its own.

These rules grant no permissions and change no task risk, required model, role
or authority; role instructions own any delivery exception. Questions and
assessments authorize no changes.

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
