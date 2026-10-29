# Cost and cache decisions

For material runtime, memory or I/O tradeoffs, establish expected or explicitly
assumed input sizes and affected call paths. Use the required Code review
quality check for algorithmic cost; compare direct computation or reuse before
proposing a cache. An asymptotic improvement alone does not justify extra
complexity or memory.

Use an existing cache only when its contract fits, through its canonical access
path and with correct keys, context or tenant separation, lifetime and
invalidation. Add a cache only for a concrete benefit that justifies its state,
memory and validity rules. Apply SKILL.md's Resolve material choices section when
its behavioral or cost tradeoff needs a user decision.
