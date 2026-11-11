# Code quality

A complete copy of these rules from this build already in your context,
including one embedded in your assignment, is this reference; do not reread it.

Apply these criteria when choosing or recommending an implementation and before
accepting a change or reporting no findings. Judge simplicity, algorithmic
cost, maintainability and clarity against the requested result, the guarantees
that must keep holding and the authorized scope. An audit uses its assigned
scope. New code or a change includes the executable logic and the callers, data
flows, dependencies and configuration whose behavior, input sizes or guarantees
it can alter. For pure text or formatting changes, check content and unintended
effects, and examine unchanged algorithms only for a behavioral reason.

## Simplest sound solution

Choose the simplest sound solution at the responsible owner for the project's
maintenance and development intent. Without established intent, the author
derives expected lifespan and evolution from the request and asks only when the
uncertainty materially changes the design; a read-only reviewer reports it as
an open decision. Encapsulate real responsibilities and state boundaries, even
with one caller when that makes independent change clearer. Keep dependencies
free of cycles and of shortcuts into another module's internals. Avoid
duplicated policy, recurring workarounds, speculative variants, arbitrary
splits and hidden coupling. Owners, contracts and data flow must be
understandable without chat history. Unnecessary behavior, state or layers
with a concrete work or maintenance cost can be defects; a different style,
fewer lines or a hypothetical extension need is not one.

## When protection is needed

Missing protection is a defect only against a requirement or a credible failure
reachable in supported use or through a concrete attack path; no prior incident
is needed. Added protection needs the same basis and a named gap in existing
behavior. Prefer removing unnecessary risky state or narrowing an unsupported
claim to adding machinery. An existing visible exception or failed command is
enough when it causes no material harm and keeps the contract; visibility alone
cannot undo damage or satisfy a broken guarantee. Fault injection supports
protection only when it models such a path, and an attribution whose
preconditions cannot occur on the claimed path is rejected. Risk tells you what
to examine, not how much hardening to add.

Illustration:

| Situation | Protection |
| --- | --- |
| An internal function receives a list its only caller has just validated | None: the precondition cannot fail on this path. |
| An export overwrites the user's file and can fail halfway | Needed: write a temporary file and rename it, because a partial overwrite loses data that a visible error cannot bring back. |
| A CLI crashes with a clear traceback on a malformed config file | The visible failure suffices: nothing is damaged and the user can correct the file. |
| An HTTP handler builds a file path from a request parameter | Needed: a concrete attack path reaches files outside the intended directory. |

## Algorithmic cost

Trace relevant loops, collection scans and recursion in the code: reachable
inputs, bounds, what grows and what repeats. Look for avoidable quadratic,
exponential or comparable work, and prefer an equivalent lookup, single pass or
reuse when it removes meaningful cost without disproportionate complexity.
Nested syntax alone proves nothing; disjoint traversals, fixed bounds or
required output can justify the work, and a failure attribution that the
actual bounds exclude is rejected. This is a static check: it needs no
benchmark or extra test run and is not a request for general performance or
cache tuning.

For material runtime, memory or I/O tradeoffs, establish expected or explicitly
assumed input sizes and the affected call paths. An asymptotic improvement
alone does not justify extra complexity or memory; compare direct computation
or reuse before proposing a cache. Use an existing cache through its canonical
access path only when its contract fits: keys, context or tenant separation,
lifetime and invalidation. Add a cache only for a concrete benefit that
justifies its state, memory and validity rules. Resolve a material cost or
behavior choice with the user; a read-only reviewer reports it without making
the choice.

## Findings

Preserve required guarantees and diagnostics. Authors resolve material findings
within their authority before acceptance; read-only reviewers report them
without editing. Name missing necessary sources as evidence gaps. Optional
improvements are not defects: they neither block acceptance nor authorize
implementation, and they appear only where the role's result contract permits
them and they help a relevant decision. Report actionable findings or concrete
evidence limits in the existing result fields; no per-aspect checklist, minimum
finding count or additional review phase is expected. Roles keep their own
permissions and output schemas.
