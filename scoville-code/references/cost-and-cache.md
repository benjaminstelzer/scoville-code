# Cost and cache decisions

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
