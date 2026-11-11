# Planning and Decisions

Use planning to coordinate dependent outcomes, preserve continuation state or
record material choices in the project's existing owner.

## Contents

- Use one planning owner
- Define behavior-complete work
- Record material decisions
- Resolve decision ambiguity
- Hand off and resume

## Use one planning owner

The authoritative project plan is the durable owner; any required runtime plan
is a disposable mirror. Without a project plan, use the existing runtime owner.
A small contained change needs no new records unless the project requires them.

## Define behavior-complete work

Keep one behavior-complete lifecycle item active at a time, with an observable,
independently resumable outcome. Its implementation and verification belong
together; commands, review and documentation remain subordinate steps/evidence.
Split only for distinct resumable outcomes and acceptance boundaries, including
when dependencies, owners or rollout timing require them.

Acceptance names necessary outcome conditions and required results. Keep methods
in steps unless independently required for acceptance. Scoville Plan owns native
field and granularity rules.

Continue to the next authorized in-scope item when its dependencies are met; a
checkpoint is not a new task that needs a new go-ahead.

Keep current results, remaining work, binding constraints and material decisions.
In native Plans, Steps own actions; Instructions add
conditions absent from Steps. Record accepted results and required review
completion during closure, without archiving review text or reconstructing
history. Use the existing owner's maintenance route for requested cleanup.

## Record material decisions

For an assigned review of native Plan or Decision fields, use Scoville Plan only when
already independently available and applicable; otherwise use the repository's
existing field owner. For Scoville Plan, read its read-only route
and applicable field rules; otherwise read the existing owner's applicable field
rules, since Code's engineering criteria do not define those fields. Stay
within the assigned source boundary: a field review reads, and leaves
maintenance, selectors, tests and record writes to their owner.

Apply SKILL.md's material-choice criteria. Preserve each decision, its source
and status in the existing plan, ADR, decision log, authorized commit or
pull-request mechanism; without one, use a handoff only when future work depends
on it. Keep authorization distinct from observation.
When `scoville-plan` is already independently available and applicable, it owns
canonical Plan, Work Item, and Decision mutation; this reference supplies only
Code's implementation analysis. Otherwise keep using the repository's existing
owner; nothing here requires finding or imitating that Skill.

## Resolve decision ambiguity

Follow SKILL.md's choice and permission rules. In unattended work, choose within
the explicitly authorized decision space. Record an unresolved material choice
as a proposal, hold only the work that depends on it and continue the
independent authorized work.

## Hand off and resume

When Scoville Handoff is active for an explicit transfer, it owns the
continuation prompt and its required contents. The summary below does not
restrict that prompt.

For existing project records, or a requested handoff when Scoville Handoff is
inactive, retain the requested outcome, binding constraints, current state,
decisive evidence, next concrete step, and any material decision not already
recorded canonically.

On resume, treat the handoff as a snapshot rather than current truth: re-read
applicable instructions, inspect repository and plan state, and reconcile any
mismatch before continuing. Reuse completed work whose evidence still matches
the current tree.
