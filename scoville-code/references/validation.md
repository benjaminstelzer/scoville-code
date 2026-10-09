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

For relevant unresolved runtime or memory costs, use realistic input sizes or
a focused measurement that can decide between the alternatives. No universal
benchmark suite is required. When cache use changes, check freshness,
invalidation and context separation as applicable to that change.

- **Explore:** Use the cheapest decisive observation. Add no regression, stress,
  repetition, or matrix work unless the hypothesis requires it.
- **Develop:** Prefer an existing focused test, typecheck, lint, build, or direct
  execution. Add a test only when it protects observable regression-prone
  behavior or a material invariant in the project's existing harness.
- **Defect:** Reproduce the reported failure when practical, then prove the same
  case passes after the fix.

Use a broad release, readiness, platform or migration gate only when the task
makes that completion decision or a binding project rule requires it. Otherwise
exercise each changed behavior and concrete material failure with the narrowest
decisive check. Risk alone does not expand the task.

When a change alters a symbol used elsewhere, exercise each independently
affected contract variant; one affected use is sufficient when inspection finds
only one variant. Tests that mirror implementation without protecting behavior
are not proof.
For every behavior test, derive expected results from the requested behavior
or an independent contract, not solely from the implementation being checked.
An independently implemented actual consumer can establish boundary expectations.
A constant copied by both sides or the producer's own round trip does not
establish compatibility.
Controlled deterministic checks remain sufficient for behavior that does not
claim such a boundary.

Test required outcomes and behavior. Check source material only to protect a
technical contract that exists independently of the test and that an actual
program, build or host interface depends on, such as a parsed format, required
package or import structure, or agreement between version declarations that
consumers read. Compare changing values with their owner or each other instead
of pinning their current values. Prose read as instructions, documentation or
diagnostics is not such a contract; test its effect through behavior. Exact
comparisons remain appropriate for complete unchanged data transfer and
generated artifacts checked against their current canonical owner. For
diagnostics, check failure status, the identified input or condition, required
corrective information and the corrected invocation, not sentence wording.
Assert exact prose only when the user explicitly requires that text. Preserve
the required outcome when replacing a wording assertion with a behavior check.

A stub, mock, or hand-built fixture can support only the behavior actually
exercised. If a claim depends on a dependency's behavior or a producer-consumer
interaction replaced by the test, exercise that boundary with the actual
component or narrow the claim and leave the required behavior unverified.
Unmet required acceptance remains open. Controlled fixtures remain valid when
the behavior under test actually runs. Required evidence does not expand
existing permissions.

For a stateful behavior claim, trace the actual call through its factory and
configuration to the same stored state you observe. A passing isolated instance
or separate snapshot does not prove the application's binding. Include separate
processes when they participate in that behavior, without inventing unrelated
integration work.

For an added or changed safeguard against a material failure, verify that valid
use still succeeds and the claimed protection holds where the effect occurs.
A prior check alone is insufficient when its result can become stale; for
example, a checked path can change before deletion. For negative-path evidence,
establish this sequence:

```text
Required preconditions completed → target operation reached and caused failure
  → relevant aftermath observed against the contract
```

Rejection at an earlier check does not prove protection at the claimed boundary.
An existing unambiguous return, state, or call observation can supply this
evidence; do not require universal counters, logging, production instrumentation,
or a fault-injection framework.

## Handle failures

Evaluate each check's own exit status and diagnostic. A later successful command
must not hide an earlier failure. Run checks separately or stop the command group
on failure. In PowerShell, inspect `$LASTEXITCODE` immediately after a native
command; `$ErrorActionPreference` alone does not make native failures terminating.

Classify a failed check before reacting. Treat it as caused by the change unless
specific evidence shows it is pre-existing or environmental; fix what the
change caused. Apply the integrity rule in SKILL.md's Scope, integrity, and authority section when changing assertions or
validators: distinguish an explicitly replaced contract from an unmet one.

For infrastructure failure, use the project's documented setup when relevant.
Continue with another check only when a named open acceptance question, a
relevant change in conditions, or a binding project requirement justifies it.
Choose a check that can answer that question. Stop when no authorized next
check can add decisive evidence, and report the required behavior as unverified.
An unresolved requirement alone does not justify repeated ineffective probing.

Retain the first complete diagnostic. On repeated output, report the stable
failure signature and meaningful delta rather than printing the same large log
again.

## Stop repetition

Reuse completed work, reviewed unchanged content and complete passing results
while their requirements, inputs and relevant conditions, such as files,
dependencies, runtime, configuration and environment, remain unchanged. A new
Step, role, assignment, review or release phase alone does not justify repeating
them; a required independent review of content no reviewer has assessed is not
a repetition. Repeat only the affected work for a relevant change, a
still-unanswered question or a binding protocol; name the new result or evidence
it can add. Concurrency, stochastic or flaky claims may require repeated
observations tied to the actual claim.

| Correction state | Next action |
| --- | --- |
| New evidence or changed conditions support the failed strategy | Retry only when they change or substantiate the causal explanation. Different reproductions, new failure output or passing checks alone do not. |
| Unsupported diagnosis, or two unsuccessful corrections of the same failure or evidenced cause | Return to owner, contract and evidence before another patch. A symptom-specific patch is not a new approach. New evidence for a bounded cause may justify a focused correction. |
| No supported next approach | Stop that repair path, report blocker and continue independent work. |
| Decisive evidence passes | Record the concise result once and continue or complete the requested work. |

Do not weaken acceptance or bypass host attempt limits.

Add checks, independent reviews or
bookkeeping only for a separate changed behavior, an unresolved material risk
or a binding requirement. Group required reviews at the completed boundary of
their scope unless their protocol requires an earlier review. Keep only results
and open limits needed for further development plus independently required
records; do not store review texts, raw test logs or a complete check history by
default. An earlier aggregate pass becomes stale when related production code
or tests change afterward; rerun the smallest aggregate check covering the final
tree or narrow the completion claim.

Do not fix unrelated suite failures unless they block the requested outcome or
the user expands scope.

## Inspect the final change

Inspect the final scoped diff and repository state. Confirm that the outcome
resides in its canonical owner, each hunk serves the request or a named risk,
and required guarantees and acceptance remain intact. For generated output,
inspect the source owner and affected consumer output. Reuse reviewed unchanged
content and evidence; revisit only affected content. Tie completion to the final
tree; passing checks already run on it need no rerun while their inputs and
conditions are unchanged. Report material unverified behavior.

## Report the evidence

Report each decisive command or observation and its actual result. Distinguish a
clean compile, source review, unit test, rendered interaction, live-system check,
and deployment; one does not imply another. If a check was skipped, failed, or
could not run, say so and narrow the claim. Never cite stale evidence as proof of
the final change.

Prefer decisive status, failures and observations to unnecessary counts. Compute
a count only when it affects acceptance or a decision. In PowerShell, make collections explicit,
for example `@($report.checks.PSObject.Properties).Count`; do not report per-element
`.Count` values as one total.
