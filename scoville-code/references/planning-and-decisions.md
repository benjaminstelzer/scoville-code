# Planning and Decisions

Use planning only when it helps coordinate real dependent outcomes, preserves
state across interruption, or records a material choice. Process is never a
substitute deliverable.

## Contents

- Use one planning owner
- Define behavior-complete work
- Record material decisions
- Resolve decision ambiguity
- Hand off and resume

## Use one planning owner

An authoritative project plan is the sole durable planning state. A runtime that
requires its own plan holds a disposable mirror of the same work. Use a runtime
plan alone only when no project plan exists. Do not create a plan file, decision
log, validation ceremony, or second source of truth merely because a code task
exists.

Use the available planning mechanism only for multiple dependent work items,
material sequencing, or work that must survive handoff or compaction. For a
small contained change, implement and validate directly unless a binding project
workflow requires a tracked item.

## Define behavior-complete work

Keep one behavior-complete lifecycle item active at a time. Its outcome should
be independently resumable and observable. Implementation and its verification
for one observable behavior belong to the same behavior Work Item; test
commands, review, and documentation remain subordinate steps or evidence.

Split work only into independently resumable outcomes with distinct acceptance
boundaries. Separate dependencies, owners, or rollout timing justify a split
only when they create such independent outcomes. Keep acceptance and evidence
with the item that owns the behavior.

Continue to the next authorized in-scope item when its dependencies are met; do
not treat every checkpoint as a new task.

## Record material decisions

Use the core's material-choice criteria.

Record a material decision in the project's existing plan, ADR, decision log,
authorized commit, or pull-request mechanism. When none exists, preserve it in a
handoff only if future work depends on it. Do not invent a durable record system.
When `scoville-plan` is already independently available and applicable, it owns
canonical Plan, Work Item, and Decision mutation; this reference supplies only
Code's implementation analysis. This mention does not require loading or
searching for that Skill. Without independent availability, keep using the
repository's existing owner and do not require or simulate Scoville Plan.

## Resolve decision ambiguity

For ordinary details, choose the smallest reversible option that preserves the
outcome. For an unresolved material choice, follow the core's question rule.

Do independent work first, then ask one specific question before dependent work.
In unattended work, assumptions may resolve only harmless details or choices
inside an explicitly authorized decision space. If dependent work needs an
unresolved material choice, record the proposal and stop that dependent work;
continue only independent authorized work.

## Hand off and resume

A durable handoff contains only the requested outcome, binding constraints,
current state, decisive evidence, next concrete step, and any material decision
not already recorded canonically.

On resume, treat the handoff as a snapshot rather than current truth: re-read
applicable instructions, inspect repository and plan state, and reconcile any
mismatch before continuing. Do not repeat completed work whose evidence still
matches the current tree.
