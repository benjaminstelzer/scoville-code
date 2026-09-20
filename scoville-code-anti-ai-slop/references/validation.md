# Validation and Completion Evidence

Choose the cheapest evidence that could disprove a claim about the changed
behavior or expose a named failure risk. A passing check proves only what it exercised.

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

When a change alters a symbol used elsewhere, exercise each independently
affected contract variant; one affected use is sufficient when inspection finds
only one variant. Tests that mirror implementation without protecting behavior
are not proof.
For an affected boundary contract, derive expectations from the agreed contract
or an independently implemented actual consumer. A constant copied by both
sides or the producer's own round trip does not establish compatibility.
Controlled deterministic checks remain sufficient for behavior that does not
claim such a boundary.

A stub, mock, or hand-built fixture can support only the behavior actually
exercised. If a claim depends on a dependency's behavior or a producer-consumer
interaction replaced by the test, exercise that boundary with the actual
component or narrow the claim and leave the required behavior unverified.
Unmet required acceptance remains open. Controlled fixtures remain valid when
the behavior under test actually runs. Required evidence does not expand
existing permissions.

For a negative-path claim, establish that required preconditions completed,
the intended target operation was reached and caused the failure, and relevant
aftermath matches the contract. An existing unambiguous return, state, or call
observation can supply this evidence; do not require universal counters,
logging, production instrumentation, or a fault-injection framework.

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
flaky-test, or project protocol requires repetition. If two consecutive correction
attempts fail to fix the same check, or verified findings after both attempts show
the same causal mechanism still violates the affected contract, stop patching
and re-read the owner, contract, and evidence. Then change the approach or narrow
the change without weakening required acceptance. Different reproductions or
passing existing checks do not reset this trigger. Similar symptoms alone do not
establish a shared cause.

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
