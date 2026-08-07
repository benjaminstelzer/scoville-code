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
otherwise use a targeted filename or symbol search. Read the owning file and the
callers, contracts, tests, or configuration needed to confirm its behavior.

For a contained change, stop when the owner, affected behavior, and focused
check are clear. For Structural or High risk, inspect directly affected
consumers and relevant serialization, persistence, publication, authorization,
or process boundaries. Expand only when evidence names another path; do not run
a broad repository inventory as insurance.

For Explore work, test the hypothesis with the cheapest decisive observation.
Do not add production scaffolding. If experimental code remains, reclassify it
as Develop work and validate it accordingly.

## Implement for the outcome

- Put behavior in its canonical owner and reuse the canonical pathway.
- Match surrounding naming, idioms, error handling, comments, and annotations.
  Name code for behavior, not novelty or history.
- Implement the smallest maintainable, behavior-complete result. Avoid
  speculative helpers, guards, flags, layers, compatibility paths, and nearby
  cleanup.
- Fix the evidenced root cause. Do not special-case a test or symptom.
- Make durable work precede progress, publication, acknowledgement, or success.
- Prefer existing dependencies and supported extension points.
- Remove temporary diagnostics, placeholders, dead branches, and restatement
  comments before completion. Comment only on constraints code cannot express.

Do not restyle or reformat untouched code. Every changed hunk must support the
outcome or a named risk.

## Handle dependencies and boundaries

Preserve failure meaning and all semantics consumers need when data crosses a
boundary. Do not collapse distinct statuses or error reasons for local
convenience. Keep validation, authorization, persistence, and publication in
their canonical layers.

For a changed symbol or public behavior, inspect at least one real consumer. For
stateful or async work, trace when data becomes durable and when completion is
acknowledged. For destructive behavior, verify scope and reversibility before
the action, not after it.

## Review implementation

Prioritize findings in this order: safety or data loss; premature publication;
lossy boundaries; duplicate owners or bypasses; misleading or silent failure;
then maintainability problems and missing meaningful coverage.

For each actionable finding, state the exact location, mechanism, observable
impact, smallest correction, and validation limit. Confirm the evidence supports
the diagnosed cause. Do not turn personal style preferences or unrelated
pre-existing issues into blockers.
