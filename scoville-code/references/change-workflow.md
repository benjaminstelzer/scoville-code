# Change Workflow

Locate and change the canonical owner with the least exploration and smallest
coherent diff that can deliver the requested behavior.

## Contents

- Locate proportionately
- Implement for the outcome
- Handle dependencies and boundaries
- Review implementation

## Locate proportionately

When the project is version-controlled, inspect its state before editing and
preserve unrelated changes. Start with exact paths named by the request;
otherwise identify candidate files before searching their contents. Keep browser
profiles, generated artifacts and raw traces outside ordinary source searches;
include them when named or implicated by evidence. When the possible scope is
broad or unknown, use bounded path or metadata discovery to select candidates
and set an output budget before reading contents. Do not emit a complete
recursive file list when a bounded path query or targeted lookup can identify
candidates. Read only the owner and relevant callers, contracts, tests or
configuration needed to answer named open questions. Do not automatically
continue truncated output; recover only the missing relevant range or field. A
line limit alone does not bound a large JSONL event, so filter an explicitly
needed large source locally before returning the relevant fields. Read a known
small file directly without first inventorying its directory. Do not require a
complete size inventory or a fixed byte limit.

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

When a change could materially affect runtime, memory use or I/O cost,
consider expected or explicitly assumed input sizes and affected call paths.
Look for nested traversals, repeated linear searches or I/O, branching recursion
and repeated computation of the same subproblem. Compare
simpler algorithms, suitable data structures and avoiding duplicate work before
proposing a cache. Bounded O(n²) can be appropriate; asymptotic improvement
alone does not justify extra complexity or memory.

Use an existing cache only when its contract fits, through its canonical access
path and with correct keys, context or tenant separation, lifetime and
invalidation. Add a cache only for a concrete benefit that justifies its state,
memory and validity rules. Apply SKILL.md's Resolve material choices section when
its behavioral or cost tradeoff needs a user decision.

- Put behavior in its canonical owner and reuse the canonical pathway.
- In existing code, follow project rules and surrounding naming, idioms, error
  handling, comments, annotations, test style, and established module
  boundaries unless they conflict with the requested outcome, safety, or a
  binding contract. Name code for behavior, not novelty or history.
- Implement the smallest maintainable, behavior-complete result. For new
  functionality, start with the simplest end-to-end implementation that delivers
  the outcome and lets failures surface. Additional checks or error handling
  must meet the safeguard rule in SKILL.md's Failure consequences section; an existence check before an operation
  that already fails clearly or a catch that only rethrows adds no protection.
  Avoid speculative helpers, guards, flags, layers, compatibility paths, and
  nearby cleanup.
- Implementation choices are not new requirements. Before adding safeguards
  for states introduced by the design, consider removing those states while
  preserving the original requirements and established guarantees.
- Fix the evidenced root cause. Do not special-case a test or symptom.
- Prefer existing dependencies and supported extension points.
- Remove temporary diagnostics, placeholders, dead branches, and restatement
  comments before completion. Remove guards or workarounds from earlier attempts
  whose justification no longer holds after the root-cause fix; preserve those
  still required. Comment only on constraints code cannot express.

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

For changes meeting the cost-check trigger in "Implement for the outcome",
check the resulting code for repeated work or a cheaper suitable alternative.
Use Validation for relevant unresolved cost questions and cache-correctness
evidence.

Judge the change against the requested behavior, established guarantees and
authorized scope. A review with no findings is complete; finding a different
possible implementation is not evidence of a defect.

Prioritize concrete safety, data-loss and correctness consequences. Apply
the safeguard rule in SKILL.md's Failure consequences section to both added and missing protection. For an unnecessary
mechanism, identify its lack of a required purpose, its added work, state,
supported variants or maintenance burden, and the smallest removal. This is a
scope or maintainability finding, not an invitation to add hardening. For missing
protection, name the credible state, violated requirement or material consequence,
and why existing failure behavior is insufficient.

A conceivable edge case or style preference alone is not a finding. Optional
improvements do not block acceptance or become implementation work without
authorization; omit them unless they inform a relevant decision. Investigate
dependency cycles, hidden state or unclear ownership through their actual impact.
After a module split, exercise affected consumers and its import, autoload,
registration or startup path before claiming the behavior remains reachable.

For each actionable finding, state the exact location, mechanism, observable
impact, smallest correction, and validation limit. Confirm the evidence supports
the diagnosed cause. Do not turn personal style preferences or unrelated
pre-existing issues into blockers.
