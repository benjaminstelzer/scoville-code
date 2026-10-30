# Shared writing rules

Apply these rules to plans, decisions, instructions, agent messages, handoffs,
reviews and reports. Preserve required schemas and delivery contracts. For
reusable instructions and outputs another agent will act on, apply
[agent instruction design](instruction-design.md) through their producing rule or
template. Load that reference when authoring or revising the producing Skill,
rule or template; recipients use their supplied task and the writing rules below.

## Read and load by content

Before requesting or reading machine reports, logs or structured state, read
[machine-data.md](machine-data.md). This includes direct native tool results,
files, failures and embedded structured strings, independently of shell use.
Evaluate the complete relevant data in code; display checked results and
necessary prose diagnostics, never raw records or state.

Read required instructions, original assignments, native finals, binding Plan
or Decision text and needed source passages completely. Choose a permitted
method that delivers them in full. A partial or truncated result leaves the
missing text unread; recover it before dependent work or report the blocker.
Use existing completeness signals without verification reads of complete text.

Read only the scope the next decision needs. Reuse retained identities and
complete results instead of repeating inventories; broaden for a concrete
uncertainty. Fully loaded shared rules of the same build remain loaded across
Skills. Reload after changed rules/builds, explicit reload, or a concrete reason
the retained text is missing, incomplete or uncertain. Load newly needed
specialized references normally.

Before shell commands, read [shell-commands.md](shell-commands.md). Before
limited result transfer, potentially large output, complete-file delivery or
a nonrepeatable effect, read [output-delivery.md](output-delivery.md).
When saving composed or transferred text, use literal-safe UTF-8 writes or
patches without interpolating content into executable code. Finish saving
before dependent commands; preparation failure stops them.

## Evidence-based conclusions

In exchanges with users and agents, defend supported factual or technical
conclusions with decisive evidence and check counterevidence at its source.
Explain why an objection fails or name the correction when facts, requirements,
assumptions or inference prove wrong, incomplete or superseded. State remaining
uncertainty or disagreement. Confidence, repetition, authority and agreement
are not evidence; user preferences and authorized decisions still govern scope.

## Write for the recipient

Give the scope, results, distinct failures, blockers, limits and next permitted
action needed to understand or verify the result. Group equivalent results and
identical failures with their affected scope; preserve differing causes and
acceptance consequences. Omit routine chronology, raw logs, passing-check
output, unchanged inventories and bookkeeping unless required or decisive.
Cite existing detailed evidence instead of duplicating it or creating another
report solely for omitted detail. Choose prose, labelled fields, lists, tables
or diagrams for clarity; use unambiguous terms and actions.

Treat an uncertain recipient as fresh. Supply the facts, constraints and
authority needed for the next correct action without hidden history. Where the
contract allows, replace accessible source text with its exact path, section
and reading instruction. Still state everything needed before that read and
everything a transfer or evidence contract requires directly. Quote wording
when decisive or required; a TL;DR cannot replace necessary explanation.

Preserve required facts, exact user wording, schemas, statuses, control messages,
identities, permissions, stops, quiescence and complete-delivery contracts.
Explicit edits and required secret redaction retain their own authority.

Use the current request's language and format; forward quoted user-facing text
unchanged. During longer work, an agent answering the user directly gives brief
material findings and next actions. Its final report stands alone and states
whether the whole task is complete, required checks and actual results, and
specific missing inputs or decisions. Continue authorized work.

These rules grant no command, write or other permission and change no task
risk, required model, role or authority. Questions and assessments authorize no
changes. A role that cannot run commands or save files returns complete text
through its permitted result channel; the caller applies the delivery route
before limited display. Report a concrete transport limit if that channel
cannot carry the required content.
