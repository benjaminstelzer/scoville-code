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
check are clear. For Structural or High risk, inspect directly affected
consumers and relevant serialization, persistence, publication, authorization,
or process boundaries. Expand only when evidence names another path; do not run
a broad repository inventory as insurance.

Evidence that the same cause affects another input, state, or consumer within
the changed contract also justifies inspecting that variant. Similar symptoms
or nearby code alone do not justify expansion.

## Implement for the outcome

- Put behavior in its canonical owner and reuse the canonical pathway.
- In existing code, follow project rules and surrounding naming, idioms, error
  handling, comments, annotations, test style, and established module
  boundaries unless they conflict with the requested outcome, safety, or a
  binding contract. Name code for behavior, not novelty or history.
- Implement the smallest maintainable, behavior-complete result. Avoid
  speculative helpers, guards, flags, layers, compatibility paths, and nearby
  cleanup.
- Fix the evidenced root cause. Do not special-case a test or symptom.
- Prefer existing dependencies and supported extension points.
- Remove temporary diagnostics, placeholders, dead branches, and restatement
  comments before completion. Comment only on constraints code cannot express.

Apply these Scoville defaults for navigable code:
- Project conventions and stricter configured limits override the defaults
  below.
- Follow the core's complete-greenfield gate before reading
  [project-conventions.md](project-conventions.md). Existing projects keep their
  organization even when a new module or an unspecified naming detail appears.
- For greenfield work without relevant project conventions, start with the
  smallest coherent layout. Keep one nameable domain responsibility per file
  or module, and split when a second responsibility or a real I/O, integration,
  or state boundary would make navigation or independent change clearer. Use
  purpose-revealing names; create no speculative layers or empty structure.
- Keep hand-written source files at no more than 2,000 physical lines in normal
  formatting, and split earlier at real responsibility boundaries. This is a
  ceiling, not a target. Never meet it through compression, lost comments, or
  numbered fragments.
- Do not split generated, minified, vendored, or tool-owned files. Larger
  coherent hand-written files need a concrete reason. For example, a split
  could worsen coupling, break an invariant, or conflict with a required
  format. A narrow fix does not authorize a broad refactor.
- Give implemented adapter, plugin, and data-import subsystems descriptive
  directories or an established equivalent area. Language `import`, `use`, or
  `require` statements follow project conventions and require no directory.
  Create no empty future-facing structure.
- Avoid catch-alls, metric-only fragments, and artificial one-function files.
- Keep functions focused on one understandable task, with side effects visible
  to callers. Extract helpers for real concepts or reuse, not a size metric.

Do not restyle or reformat untouched code. Every changed hunk must support the
outcome or a named risk.
Preserve encoding and line endings outside the edited lines, including in mixed-
ending files. A whitespace warning does not authorize whole-file normalization
or a Git configuration change. Inspect the affected diff and fix only introduced
defects; leave unrelated existing formatting alone.

## Handle dependencies and boundaries

Apply the core's integrity rules at every affected boundary. Keep validation,
authorization, persistence and publication in their canonical layers.

Keep dependency direction visible. Add no cycle or shortcut into another
module's internals. Keep public surfaces small, integration details in adapters,
and domain rules out of generic infrastructure helpers. Give mutable state a
clear owner, and separate I/O from deterministic domain logic only at a real
test or maintenance boundary. Whoever creates a resource owns or names its
cleanup. Add retry, cancellation, or timeout machinery only when required by the
request, an existing contract, or an observed failure.

Respect existing manifests, lockfiles, generators, and build entry points.
Keep touched dependency versions traceable, and use syntax and APIs supported by
the target runtime. Change a generator or hand-written source, not its output.
Consolidate proven duplication in its canonical owner, but create no abstraction
before a second real consumer or shared invariant exists.

For a changed symbol or public behavior, locate directly affected callers,
registrations, and test doubles. Cover each independently affected contract
variant; one representative real consumer is sufficient when inspection finds
only one variant. Do not inventory unrelated callers or neighboring modules.
For stateful or async work, trace when data becomes durable and when completion
is acknowledged. For destructive behavior, verify scope and reversibility
before the action, not after it.

## Review implementation

Prioritize findings in this order: safety or data loss; premature publication;
lossy boundaries; duplicate owners or bypasses; misleading or silent failure;
then maintainability problems and missing meaningful coverage.

For maintainability, reject line-count gaming, vague catch-all ownership, new
dependency cycles, hidden global state, or separation that only spreads the
same coupling across more files. After a real split, require evidence from
affected consumers and import, autoload, registration, or startup paths. Treat
an unexplained exception as a finding, not authority for out-of-scope cleanup.

For each actionable finding, state the exact location, mechanism, observable
impact, smallest correction, and validation limit. Confirm the evidence supports
the diagnosed cause. Do not turn personal style preferences or unrelated
pre-existing issues into blockers.
