# Validation and Completion Evidence

Choose the cheapest evidence that could disprove the changed behavior or a
named risk. A passing check proves only what it exercised.

## Contents

- Select proportional checks
- Handle failures
- Stop repetition
- Inspect the final change
- Report the evidence

## Select proportional checks

Validation is sufficient when every independent changed behavior and material
risk has decisive evidence and another check would not plausibly change the
implementation or completion decision.

- **Explore:** Use the cheapest decisive observation. Add no regression, stress,
  repetition, or matrix work unless the hypothesis requires it.
- **Develop:** Prefer an existing focused test, typecheck, lint, build, or direct
  execution. Add a test only when it protects observable regression-prone
  behavior or a material invariant in the project's existing harness.
- **Defect:** Reproduce the reported failure when practical, then prove the same
  case passes after the fix.
- **Structural or High:** Exercise the concrete material failure mode. Add
  broader checks only for the affected boundary or named risk.
- **Harden:** Run project-owned release, platform, migration, security, or broad
  suites once at the meaningful completion boundary.

Choose evidence scope as an exclusive decision:

1. Use a broad release, readiness, platform, or migration gate only when the
   current task makes that completion decision or a binding project rule
   requires it.
2. Otherwise prove each specific changed behavior and affected boundary with
   the narrowest decisive check.
3. Risk selects the failure mode to exercise; it never widens scope by itself.

When a change alters a symbol used elsewhere, exercise at least one affected
use. Tests that mirror implementation without protecting behavior are not proof.

## Handle failures

Classify a failed check before reacting. Treat it as caused by the change unless
specific evidence shows it is pre-existing or environmental; fix what the
change caused. Never weaken or delete a failing test or guard to obtain green
output.

For infrastructure failure, run the project's documented setup once if needed,
then try at most one different check that still exercises the behavior. If
neither does, stop and report the behavior as unverified instead of probing more
runners, environments, or dependencies.

Retain the first complete diagnostic. On repeated output, report the stable
failure signature and meaningful delta rather than printing the same large log
again.

## Stop repetition

Do not rerun an unchanged command unless a named concurrency, stochastic,
flaky-test, or project protocol requires repetition. If two consecutive attempts
fail to fix the same check, stop patching, re-read the owner's contract and
evidence, then change the approach or narrow the change.

After decisive evidence passes, run no broader or similar check for that behavior
unless a separate changed behavior, named risk, or binding requirement remains.
An earlier aggregate pass becomes stale when related production code or tests
change afterward; rerun the smallest aggregate check covering the final tree or
narrow the completion claim.

Do not fix unrelated suite failures unless they block the requested outcome or
the user expands scope.

## Inspect the final change

Before completion:

1. confirm the observable outcome resides in the canonical owner;
2. inspect every changed file and the complete scoped change;
3. confirm every hunk supports the outcome or a named risk;
4. confirm no integrity-floor failure was introduced; and
5. state material unverified behavior or residual risk.

For version-controlled work, use one final inspection of the complete scoped
diff and working-tree state. Do not follow it with another test, diff, or status
command unless it reveals a concrete defect. After fixing that defect, validate
only the affected behavior and inspect once more.

## Report the evidence

Report each decisive command or observation and its actual result. Distinguish a
clean compile, source review, unit test, rendered interaction, live-system check,
and deployment; one does not imply another. If a check was skipped, failed, or
could not run, say so and narrow the claim. Never cite stale evidence as proof of
the final change.
