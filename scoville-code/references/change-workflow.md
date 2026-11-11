# Change Workflow

Apply [Code quality](code-quality.md) when choosing the implementation and
reviewing its result. This route owns the author's work, not separate criteria.

## Contents

- Locate proportionately
- Implement for the outcome
- Handle dependencies and boundaries
- Review implementation

## Locate proportionately

Inspect version-control state before editing and preserve unrelated work. Start
with requested paths; otherwise discover candidate paths before searching
contents. Read the owner and relevant callers, contracts, tests and configuration
to resolve named uncertainties. Read known small files directly.

Keep browser profiles, generated artifacts and raw traces out of ordinary
searches unless they are named or implicated, and query large sources with
targeted, bounded searches. Expand when evidence identifies another affected
input, consumer or boundary, not merely for nearby code or similar symptoms.
Exploration is finished when ownership, affected behavior and the decisive
checks are clear.

## Implement for the outcome

- Fix the evidenced cause at its canonical owner. Resolve recurring workarounds
  at their common owner when they share a contract; one special case does not
  justify a framework.
- Reuse a suitable existing path while preserving SKILL.md's boundary guarantees.
  Separate prerequisites belonging only to another operation when they block
  the requested behavior; reuse alone does not make those prerequisites required.
- Follow explicit project conventions, surrounding code idioms and established
  module boundaries. Prefer existing dependencies and supported extension points.
  Start behavior-complete; apply Code quality to added safeguards.
- Remove temporary diagnostics, placeholders, dead branches and superseded
  workarounds. Remove a replaced path and unused contract methods with their
  implementations unless a named current consumer still requires them.

Recommend broader structural changes with their benefit and cost;
implement them only within authorized scope.

Each hunk serves the outcome or a named risk. Preserve unrelated formatting,
encoding and line endings; a whitespace warning justifies neither normalizing
whole files, which would bury the real change in the diff, nor changing Git
configuration.

## Handle dependencies and boundaries

Keep guarantees in their canonical layers and mutable state with a clear owner.
Whoever creates a resource owns or names its cleanup. Add retry, cancellation
or timeout machinery under Code quality's protection criterion.

For agent-facing helpers, scripts and prompts, keep required inputs few, provide
an invocation the agent can use directly, and make successful output usable by
its intended consumer without repair. Errors identify the cause and a concrete
next action, including expected formats or allowed values where relevant.

Respect manifests, lockfiles, generators and build entry points. Change the
source owner rather than generated output. Keep dependency versions traceable
and use APIs and syntax supported by the project's target runtime.
Before installing a newly needed direct package, verify its exact identity and
intended source against official project documentation; reuse already verified
evidence. A local runtime version alone does not choose the target version.

Trace relevant untrusted inputs to the operation they could affect and use a safe
interface at that concrete boundary. Rely on properties already guaranteed by
the caller, type or boundary validation while the value and trust conditions
remain unchanged, without validating them again internally. A type annotation
alone does not validate external data. Assess the actual possible consequence.

For a changed symbol or public behavior, locate directly affected callers,
registrations, and test doubles. Cover each independently affected contract
variant; one representative real consumer is sufficient when inspection finds
only one variant; unrelated callers and neighboring modules need no inventory.
For destructive behavior, verify scope and reversibility before the action.

## Review implementation

When reviewing the resulting implementation, including your final scoped diff,
apply [Code quality](code-quality.md) and Validation. Whether an independent
review also takes place follows the task's authority and cadence.
