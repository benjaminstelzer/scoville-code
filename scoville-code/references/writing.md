# Shared writing rules

Apply these rules to plans, decisions, instructions, agent messages, handoffs,
reviews and reports. Preserve the required output schemas and delivery contracts.

When composing reusable instructions or an output for another agent to act on,
read [agent instruction design](instruction-design.md). Apply it at the producing
rule or template; the receiving agent needs its task, not the authoring workflow.

Before reading or displaying an input, distinguish its content:

| Input | Required handling |
| --- | --- |
| Machine reports, logs and structured state | Evaluate the full relevant scope in code. Display checked results and necessary prose diagnostics, never raw records, payloads or stored state. |
| Instructions, original assignments, native finals, binding Plan or Decision text, and needed source text | Read the required text completely. |

This applies to direct tool results, saved captures and failures. A filename,
capture or size check changes delivery, not what may be displayed.

Fully read shared writing and shell rules of the same build count as loaded
across Suite Skills. Do not reread retained shared rules merely because another
Skill route names the same writing or shell reference. Reload them after an
explicit reload, changed rules or build, or missing, incomplete or uncertain
retained text. Treat retained text as uncertain only for a concrete reason,
not general caution. Load newly needed specialized references normally.

When saving composed or transferred text, use a literal-safe UTF-8 file-write
or patch operation. Do not interpolate the content into executable code. Finish saving
before any dependent command. A preparation failure stops that command.

Preserve required content without truncation. Do not blame
a specific tool or host for missing output unless evidence shows it. A
shortened later query does not prove that the original capture was truncated.
Recover the complete content first under the applicable reading or output rule.

## Evidence-based conclusions

Apply this rule in exchanges with users and agents. When challenged, defend
supported factual or technical conclusions with decisive evidence and explain
why the counterargument does not refute it. Check contrary evidence against its
sources. Revise only when evidence shows that the decisive facts, requirements,
assumptions or inference were wrong, incomplete or superseded; name the
correction. Confidence, repetition, authority and agreement are not evidence.
State uncertainty and preserve unresolved disagreement; do not defend claims
whose support no longer holds. Respect the user's preferences and authorized
decisions without treating them as proof of a factual claim.

## File reading

Choose a permitted method yourself that can deliver each required text completely;
size or metadata may inform that choice when a read may be large. A truncated
or partial result does not complete the required reads. Use existing completion
and truncation signals; do not add verification reads to an already complete read. Recover
missing required content before dependent work; if impossible, name it and stop
that work.

The relevant scope is what the next decision needs; narrowing to it is not
sampling. Reuse retained identities, notifications and complete results instead
of repeating whole inventories. If a tool returns directly without a route to
evaluate its result in code before display, narrow the request with its supported
filters instead. Broaden only to resolve a concrete uncertainty. Preserve every
required fact and obtain complete required results.

For machine reports, when commands are permitted, use this order:

1. Parse the complete checked scope in code. Establish needed fields and types
   from all relevant records and the producer's contract. Schema discovery
   displays field names, types and collection sizes, never records or values.
   Display a control value only when its meaning is established and it is
   needed to decide or explain a check. Stored payloads are not control values.
2. Extract required text passages and read them completely for their meaning.
   Required passages include prose whose wording matters, such as diagnostics,
   messages and schema descriptions. Objects, arrays and serialized structured
   state remain report data, including inside string fields; inspect and
   compare them in code rather than displaying them as text passages.
   Parse a string as embedded data only when its established format requires
   it. Catch parser failures before display; report location and reason, not
   echoed input or state.
   Before writing filters or assertions, take the actual values from the data
   and their meaning from the schema, producer or binding contract; do not
   guess literals. Different wording with the same established meaning is no
   defect unless exact values are binding. Unknown or contradictory meanings
   stay unresolved and establish neither success nor permission. Run the
   required checks over the complete checked scope. Parsing alone proves no
   result.
3. Before executing a command that displays machine data, check its output
   expressions and emitted values against steps 1 and 2 and the limits below.
   Compare structured values, including states before and after a change, in code.
   Build a compact result from the checks; selecting or serializing report
   subtrees or whole state strings is not a compact result. Display only checked
   collection and field names, decisive values, results and every relevant
   deviation. Include the identity or property, decisive expected and actual
   values, and complete necessary diagnostic text that explain each deviation,
   as applicable. Group identical diagnostics with counts and affected scope;
   keep differing conditions distinct. For collection checks, include processed and expected counts,
   not every passing entry. Correct an overbroad output expression before
   execution; do not print this self-check.

Parse errors, missing required fields, wrong types or unsupported formats in
the checked scope prevent a pass. Do not replace a complete check with sampling.
Without command permission, obtain the needed machine-data evaluation from a
permitted caller or report the missing capability. Read required prose fully.
This grants no command or write permission.

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

Write for the actual recipient. Use labelled fields for structured assignments
or results when they make scope, evidence and the next action easier to find.
Choose concise prose, lists, tables or diagrams to fit the information.
Messages and reports include only what is
needed to understand or verify the result and take the next correct action:
relevant scope, results, distinct failures, blockers, gaps or limits, and a
necessary next permitted action. Group equivalent passing results and identical failures with their
affected scope; keep differing causes or acceptance consequences distinct.
Omit narration, chronology, test or coordination history, recaps, raw logs, raw
output of passing checks, inventories, unchanged settings, known procedures
and statements about actions not taken, unless they change how the result is
read or the next action, or a contract requires them. Cite the exact path of
existing detailed evidence where needed instead of repeating it; do not create
another report to hold omitted text. Explicitly requested formats, binding
schemas, exact quotes and required complete evidence still apply.
Use unambiguous labels
and actions; no unexplained abbreviations or invented protocol tokens.

Treat an uncertain recipient as fresh; assume no hidden history. Supply every
fact and constraint needed for the next correct decision or action. When the
output contract allows a source pointer, give its exact path and section with
a reading instruction instead of duplicating accessible source text. State
directly every fact needed before that read and every fact a transfer or evidence
contract requires in the output. Quote wording only when decisive or required.
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

Write instructions and explanations for their actual recipient; target current
frontier models for AI-consumed text. Supply the context needed without hidden
history, use plain wording and one term per meaning, and preserve literal paths,
commands, field names and technical syntax. Length alone proves neither
effectiveness nor performance.

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
