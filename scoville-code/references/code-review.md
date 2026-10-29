# Code review quality

Complete rules already supplied or read from this build satisfy references to
code-review.md. Retain them; do not reread unchanged copies.

Before approving or reporting no findings, inspect the relevant code paths for
simplicity, algorithmic cost, maintainability and clarity. For an audit, use the
assigned scope. For a change, include changed executable logic and callers, data
flows or dependencies whose behavior, input sizes or guarantees can change
through the diff, including configuration.
For pure text or formatting changes, check content and unintended effects;
do not examine unchanged algorithms without a behavioral reason.

Choose the simplest sound solution at the responsible owner for the project's
maintenance and development intent. Check encapsulation, dependency direction,
duplicated policy and recurring workarounds. Owners, contracts and data flow
must be understandable without chat history. Unnecessary behavior, state or
layers with a concrete work or maintenance cost can be defects; a different
style, fewer lines or a hypothetical extension need is not one.

Trace relevant loops, collection scans and recursion in code: establish reachable
inputs, bounds, what grows and what repeats. Check avoidable quadratic,
exponential or comparable work and prefer equivalent lookup, pass or reuse when
it removes meaningful cost without disproportionate complexity. Nested syntax
alone proves nothing; disjoint traversals, fixed bounds or required output can
justify the work. Reject failure attributions excluded by actual bounds. This
static check requires no benchmark or extra test run and does not request
general performance or cache tuning.

Preserve required guarantees and diagnostics. Resolve material findings before
approval; name missing necessary sources as evidence gaps. Report actionable
findings or concrete evidence limits in the existing result fields, without
a per-aspect checklist, minimum finding count or additional review phase.
