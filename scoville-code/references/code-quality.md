# Code quality

A complete copy of these rules from this build already in your context,
including one embedded in your assignment, is this reference; do not reread it.

Authors choosing an implementation and reviewers judging it apply the same
criteria to the authorized scope: the changed logic and the callers, data
flows, dependencies and configuration it can alter. A pure text or formatting
change needs no algorithm review.

## Simplest sound solution

Choose the simplest sound solution at the source that owns the behavior, for
the project's maintenance and development intent. Defects: a second
implementation of logic the project already has; a workaround repeated where
its shared cause could be fixed; a variant, layer, state or abstraction for a
need nobody has stated; code only understandable from the chat history. Not
defects: a different style, a shorter possible version, a missing
hypothetical extension, or a real responsibility or state boundary
encapsulated for one caller.

## When protection is needed

Missing protection is a defect only against a requirement or a failure
reachable in supported use or through a concrete attack path; no prior
incident is needed. Added protection needs the same basis and a named gap in
existing behavior. A visible exception or failed command is enough when it
causes no material harm; visibility cannot undo damage. Prefer removing risky
state or narrowing an unsupported claim to adding machinery. Reject a failure
attribution whose preconditions or input bounds cannot occur on the claimed
path.

Illustration:

| Situation | Protection |
| --- | --- |
| An internal function receives a list its only caller has just validated | None: the precondition cannot fail on this path. |
| An export overwrites the user's file and can fail halfway | Needed: write a temporary file and rename it, because a partial overwrite loses data that a visible error cannot bring back. |
| A CLI crashes with a clear traceback on a malformed config file | The visible failure suffices: nothing is damaged and the user can correct the file. |
| An HTTP handler builds a file path from a request parameter | Needed: a concrete attack path reaches files outside the intended directory. |

## Algorithmic cost

Read the loops, collection scans and recursion the change touches: which
inputs reach them, what grows, what repeats. Replace avoidable quadratic or
exponential work with a lookup, single pass or reuse when that removes
meaningful cost without disproportionate complexity; fixed bounds or disjoint
traversals justify nested loops. No benchmark or general performance tuning
is asked.

Add a cache only for a concrete benefit that justifies its state, memory and
validity rules, after comparing direct computation or reuse. Use an existing
cache through its own access path, and only when its keys, tenant or context
separation, lifetime and invalidation fit.

## Reviewing a change

Read the whole change, then look beyond it: most maintainability defects show
only against the rest of the codebase. Go through the change with these
questions. Judge from the code; run no benchmark or profiler for this. A
finding names the place, the problem and the existing function, path or
interface to use instead.

| Look at | Ask | Defect when |
| --- | --- | --- |
| Each function, class and constant table the change adds | Does the codebase already have this? Search by what it does, not by its name. | An existing function or table does the same job. |
| Each new or changed call path | Is there now a second way to do the same thing? | A copied pipeline, a fallback to the old path, a flag nobody asked for, or callers left on a replaced path. |
| Each use of another module | Does it go through that module's public interface, from the right layer? | It reads private names, the storage file or table or internal data structures; a business rule sits in a handler or template; new module-level mutable state. |
| Each loop | Does its body walk a collection or do input/output per item while the outer collection can be large? | Yes, and a set, dict, single pass or batch call would do. |
| Each validation, guard, retry, fallback and special case | Which real input or failure reaches it in this application? | None can; it repeats what the caller guarantees; it swallows an error or returns a default. |
| Structure the change adds | Does the request need it? | A base class, registry, option or layer with one use; recursion or deep nesting where one pass would do. |
| Each test | Would it fail if the behavior it covers broke, and did it run? For new or corrected behavior: does it fail without the change? | It repeats the implementation or only asserts that a mock was called; the behavior that matters is untested; the relevant test is skipped or not collected. |
| What is left over | Is anything dead? | Commented-out or unreachable code, unused parameters, debug output; configuration, documentation or tests of a removed feature. |
| The next reader | Can a person follow it without the chat history, and find it later? | Names that hide what a thing does, a function with several jobs, a new setting or module missing where the project documents them. |

Not defects: a different style; a nested loop over two fixed small
collections; a guard on a value that really comes from outside at that point;
a helper that resembles an existing one but means something else in the
domain; a real responsibility encapsulated for one caller.

## Findings

Authors resolve material findings within their authority before acceptance;
a material design, cost or behavior choice goes to the user. Read-only
reviewers report findings, open decisions and missing sources without editing
or choosing. Optional improvements are not defects: they neither block
acceptance nor authorize implementation. Report findings in the role's
existing result fields, each defect as its own finding: a maintainability
defect stays in the report when a more severe finding exists, and two defects
in one function are two findings. The review table is how you look, not a
form to fill in: no entry per question, no minimum finding count and no extra
review phase.
