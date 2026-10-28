# Change Workflow

Locate and change the canonical owner with the least exploration and smallest
coherent diff that can deliver the requested behavior.

## Contents

- Locate proportionately
- Implement for the outcome
- Handle dependencies and boundaries
- Review implementation

## Locate proportionately

1. In version-controlled projects, inspect state before editing and preserve
   unrelated changes.
2. Start with requested exact paths; otherwise select candidate files before
   searching contents. For broad or unknown scope, use bounded path or metadata
   discovery and set an output budget before reading contents.
3. Read only the owner and relevant callers, contracts, tests or configuration
   needed for named open questions. Read known small files directly without a
   directory inventory.

Keep browser profiles, generated artifacts and raw traces outside ordinary
searches unless named or implicated by evidence. Use bounded queries or targeted
lookups instead of complete recursive lists when they identify candidates. Require
neither a complete size inventory nor a fixed byte limit.

Recover incomplete required reads under the shared writing rules before
continuing. A line limit cannot bound a large JSONL event; filter an explicitly
needed large source locally while retaining every required fact.

For a contained change, stop when the owner, affected behavior, and focused
check are clear. Inspect affected consumers and serialization, persistence,
publication, authorization or process boundaries when the change can alter their
contract or introduce a material failure. Expand only when evidence names another
path; do not run a broad repository inventory as insurance.

Evidence that the same cause affects another input, state, or consumer within
the changed contract also justifies inspecting that variant. Similar symptoms
or nearby code alone do not justify expansion.

## Implement for the outcome

Use the direct processing needed by the actual input structure. Additional
traversals, recursive search and intermediate state need a concrete purpose in
the requested behavior. Neither recursion nor multiple passes are inherently
wrong; do not merge clear passes into a more complex algorithm merely to count
fewer passes.

When runtime, memory, I/O cost or cache behavior may materially change, read
[cost and cache decisions](cost-and-cache.md) before deciding or judging that work.

- Put behavior in its canonical owner. Reuse an existing pathway when it
  achieves the requested result, permits the explicitly intended changes, and
  preserves every requirement that applies regardless of the pathway. These
  include shared authorization, protection of other data, and required
  persistence. A prerequisite serving only another operation's purpose does not
  become required through reuse. If it blocks this operation, adjust the
  existing pathway or separate its operation-specific behavior using the
  smallest maintainable change. Keep applicable guarantees at their responsible
  boundaries; dropping such a prerequisite does not waive them.
- In existing code, follow project rules and surrounding naming, idioms, error
  handling, comments, annotations, test style, and established module
  boundaries unless they conflict with the requested outcome, safety, or a
  binding contract. Name code for behavior, not novelty or history.
- Start with a behavior-complete implementation. Add safeguards under SKILL.md's
  Failure consequences rule.
  Avoid speculative helpers, guards, flags, layers, compatibility paths, and
  nearby cleanup.
- Implementation choices are not new requirements. Before adding safeguards
  for states introduced by the design, consider removing those states while
  preserving the original requirements and established guarantees.
- Fix the evidenced root cause. Do not special-case a test or symptom.
- Prefer existing dependencies and supported extension points.
- Remove temporary diagnostics, placeholders, dead branches, and restatement
  comments before completion. Remove guards or workarounds from earlier attempts
  whose justification no longer holds after the root-cause fix. When a change
  replaces a model, path, format, detection route or guard, remove the replaced
  one in the same change unless a named current consumer still needs it; remove
  unused contract methods with their implementations. Comment only on
  constraints code cannot express.

Encapsulate an existing responsibility or state boundary even with one caller
when it makes ownership and independent change clearer. Extract helpers for
real concepts or reuse. Add reusable frameworks, extension points and
configurable variants only for a concrete current need. Do not split code merely
to meet a size metric or spread unchanged coupling across more files. A narrow
fix does not authorize a broad refactor. Existing projects keep their
organization; SKILL.md routes wholly new projects to ecosystem guidance.

Do not restyle or reformat untouched code. Every changed hunk must support the
outcome or a named risk.
Preserve encoding and line endings outside the edited lines, including in mixed-
ending files. A whitespace warning does not authorize whole-file normalization
or a Git configuration change. Inspect the affected diff and fix only introduced
defects; leave unrelated existing formatting alone.

## Handle dependencies and boundaries

Apply the rules in SKILL.md's Scope, integrity, and authority section at every affected boundary. Keep validation,
authorization, persistence and publication in their canonical layers.

Keep dependency direction visible. Add no cycle or shortcut into another
module's internals. Keep public surfaces small, integration details in adapters,
and domain rules out of generic infrastructure helpers. Give mutable state a
clear owner, and separate I/O from deterministic domain logic only at a real
test or maintenance boundary. Whoever creates a resource owns or names its
cleanup. Add retry, cancellation, or timeout machinery only when required by the
request, an existing contract, or a credible failure consequence under the safeguard rule in SKILL.md's Failure consequences section. A failed attempt alone does not justify adding retries.

For agent-facing helpers, scripts and prompts, keep required inputs few, provide
an invocation the agent can use directly, and make successful output usable by
its intended consumer without repair. Errors identify the cause and a concrete
next action, including expected formats or allowed values where relevant.

Respect existing manifests, lockfiles, generators, and build entry points.
Keep touched dependency versions traceable, and use syntax and APIs supported by
the target runtime. Change a generator or hand-written source, not its output.
Before installing a newly needed direct package, verify its exact identity and
intended source against official project documentation; reuse already verified
evidence. A local runtime version alone does not choose the target version.
Consolidate proven duplication in its canonical owner when the shared behavior
has the same contract.

Trace relevant untrusted inputs to the operation they could affect and use a safe
interface at that concrete boundary. Rely on properties already guaranteed by
the caller, type or boundary validation while the value and trust conditions
remain unchanged; do not revalidate them internally. A type annotation alone
does not validate external data. Assess the actual possible consequence.

For a changed symbol or public behavior, locate directly affected callers,
registrations, and test doubles. Cover each independently affected contract
variant; one representative real consumer is sufficient when inspection finds
only one variant. Do not inventory unrelated callers or neighboring modules.
Where the contract requires durable state, trace storage before completion is
acknowledged. Persist what the actual workflow needs. Continuing from saved
output does not by itself require persisted execution states or recovery
commands. State or async execution alone does not require persistence.
For destructive behavior, verify scope and reversibility before the action,
not after it.

## Review implementation

When reviewing the resulting implementation, including your final scoped diff,
read [implementation review](implementation-review.md). Independent review remains
subject to the task's authority and cadence; this reference adds no review phase.
