# Implementation review

Apply [Code review quality](code-review.md) before acceptance. Use Validation for
unresolved runtime-cost or cache-correctness claims in scope.

Judge against the requested result, continuing guarantees and authorized scope.
Apply SKILL.md's Failure consequences rule to missing and added protection.
For unnecessary machinery, identify its unsupported purpose and concrete added
work, state or maintenance burden; recommend the simplest sound correction.
Optional improvements do not block acceptance or authorize implementation;
include them only when useful to a relevant decision.
After a module split, exercise affected consumers and its import, autoload,
registration or startup path before claiming the behavior remains reachable.

For each actionable finding, give the exact location, evidenced mechanism,
observable impact, simplest sound correction and validation limit. Prioritize
safety, data loss and correctness. Report unrelated pre-existing issues only
when they affect the next action.
