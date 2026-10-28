# Implementation review

## Review implementation

[Code review quality](code-review.md) is a required acceptance condition.
The rules below do not weaken it.

Separately, use Validation for relevant unresolved cost questions and
cache-correctness evidence when those concerns are in scope. They do not replace
the required static review of loops and recursion.

Judge the change against the requested result, explicitly intended changes,
guarantees that still apply, and authorized scope. Do not demand a prerequisite
merely because a reused pathway enforces it; identify what required result or
continuing guarantee would fail without it. A review with no findings is
complete; finding a different possible implementation is not evidence of a defect.

Apply [Evidence-based conclusions](writing.md#evidence-based-conclusions) to
disputed findings.

Prioritize concrete safety, data-loss and correctness consequences. Apply the
safeguard rule in SKILL.md's Failure consequences section to both added and
missing protection. For an unnecessary mechanism, identify its lack of a
required purpose, its added work, state, supported variants or maintenance
burden, and the smallest removal. This is a scope or maintainability finding,
not an invitation to add hardening. For missing protection, name the credible
failure under the safeguard rule in SKILL.md's Failure consequences section, the
violated requirement and why existing failure behavior is insufficient. Name the
cheapest correction first: narrowing an unsupported claim, using existing
visible failure, or removing the state that causes the risk. Request a new
mechanism only when none of these meets the requirement.

A conceivable edge case or style preference alone is not a finding. Optional
improvements do not block acceptance or become implementation work without
authorization; omit them unless they inform a relevant decision. Investigate
dependency cycles, hidden state or unclear ownership through their actual impact.
After a module split, exercise affected consumers and its import, autoload,
registration or startup path before claiming the behavior remains reachable.

When composing an agent-facing review, apply the shared
[instruction design](instruction-design.md) rules. For each actionable finding,
state the exact location, mechanism, observable impact, smallest correction,
and validation limit. Confirm the evidence supports
the diagnosed cause. Do not turn personal style preferences or unrelated
pre-existing issues into blockers.
