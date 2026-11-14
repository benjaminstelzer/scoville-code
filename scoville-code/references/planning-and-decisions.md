# Planning and Decisions

Use the project's existing plan and decision records; a runtime plan only
mirrors them. A small contained change needs no new record unless the project
requires one.

## Work items

Keep one behavior-complete item active at a time: an observable, separately
resumable outcome with its implementation and verification. Commands, review
and documentation are its steps. Split only where outcomes are accepted and
resumed separately. Acceptance names the results that must hold; a method
belongs in the steps unless it is itself required. Continue with the next
authorized item whose dependencies are met; a checkpoint needs no new
go-ahead.

In native Plans, Steps own actions; Instructions add
conditions absent from Steps. At closure record accepted results and review
completion, not review text or history.

## Decisions and field reviews

Record each material decision with its source and status in the existing
plan, ADR, decision log, authorized commit or pull request; a small contained
change adds no new ADR or plan for it unless the project requires one. Without
such a record, use a handoff only when future work depends on it. In unattended work, choose within
the decision space the user authorized, record an open material choice as a
proposal, hold only the work that depends on it and continue the rest.
`scoville-plan` owns Plan, Work Item and Decision changes only when it is
already independently available and applicable; otherwise the repository's
existing record owner does.

For an assigned review of native Plan or Decision fields, read the existing
field owner's rules; with Scoville Plan already available and applicable,
those are its read-only route and field rules. Code's engineering
criteria do not define those fields. The review reads; maintenance, selectors,
tests and record writes stay with their owner.

## Hand off and resume

Scoville Handoff, when active for an explicit transfer, owns the
continuation prompt and its contents.

Otherwise a requested handoff or project record retains the requested
outcome, binding constraints, current state, decisive evidence, the next
concrete step and any material decision not yet recorded. On resume, treat a
handoff as a snapshot: re-read the applicable instructions, inspect repository
and plan state, reconcile any mismatch and reuse completed work whose evidence
still matches the current tree.
