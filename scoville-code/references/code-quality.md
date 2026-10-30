# Code quality

Complete rules already supplied or read from this build satisfy references to
code-quality.md. Retain them; do not reread unchanged copies.

Apply these criteria when choosing or recommending an implementation and before
acceptance or reporting no findings. Inspect relevant code paths for simplicity,
algorithmic cost, maintainability and clarity against the requested result,
continuing guarantees and authorized scope. An audit uses its assigned scope;
new code or a change includes executable logic and callers, data flows or
dependencies whose behavior, input sizes or guarantees can change, including
configuration. For pure text or formatting changes, check content and unintended
effects; examine unchanged algorithms only for a behavioral reason.

Choose the simplest sound solution at the responsible owner for the project's
maintenance and development intent. Without established intent, the author
derives expected lifespan and evolution from the request and asks only when
uncertainty materially changes the design; a read-only reviewer reports it as
an open decision. Encapsulate real responsibilities and state boundaries, even
with one caller when independent change becomes clearer. Keep dependencies free
of cycles and shortcuts into another module's internals. Avoid duplicated policy,
recurring workarounds, speculative variants, arbitrary splits and hidden coupling.
Owners, contracts and data flow must be understandable without chat history.
Unnecessary behavior, state or layers with a concrete work or maintenance cost
can be defects; a different style, fewer lines or a hypothetical extension need
is not one.

Missing protection is a defect only for a requirement or a credible reachable
failure in supported use or through a concrete attack path; a prior incident is
unnecessary. Added protection needs the same basis and a named gap in existing
behavior. Fault injection supports protection only when it models such a path.
Reject an attribution whose preconditions cannot occur on the claimed path.
Prefer removing unnecessary risky state or narrowing an unsupported claim to
adding machinery. An existing visible exception or failed command suffices when
it causes no material harm and preserves the contract; visibility alone cannot
undo damage or satisfy a broken guarantee. Risk identifies what to examine, not
a preset amount of hardening.

Trace relevant loops, collection scans and recursion in code: establish reachable
inputs, bounds, what grows and what repeats. Check avoidable quadratic,
exponential or comparable work and prefer equivalent lookup, pass or reuse when
it removes meaningful cost without disproportionate complexity. Nested syntax
alone proves nothing; disjoint traversals, fixed bounds or required output can
justify the work. Reject failure attributions excluded by actual bounds. This
static check requires no benchmark or extra test run and does not request
general performance or cache tuning.

For material runtime, memory or I/O tradeoffs, establish expected or explicitly
assumed input sizes and affected call paths. An asymptotic improvement alone does
not justify extra complexity or memory; compare direct computation or reuse
before proposing a cache. Use an existing cache through its canonical access
path only when its contract fits: keys, context or tenant separation, lifetime
and invalidation. Add a cache only for a concrete benefit justifying its state,
memory and validity rules. Resolve a material cost or behavior choice with the
user; a read-only reviewer reports it without making the choice.

Preserve required guarantees and diagnostics. Authors resolve material findings
within their authority before acceptance; read-only reviewers report them without
editing. Name missing necessary sources as evidence gaps. Optional improvements
are not defects, do not block acceptance or authorize implementation, and appear
only where the role's result contract permits them and they help a relevant
decision. Report actionable findings or concrete evidence limits in the existing
result fields, without a per-aspect checklist, minimum finding count or additional
review phase. Roles retain their own permissions and output schemas.
