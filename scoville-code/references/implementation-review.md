# Implementation review

## Review implementation

For changes that may materially affect runtime, memory, I/O cost or caches,
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
