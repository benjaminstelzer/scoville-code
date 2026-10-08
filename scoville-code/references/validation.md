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
example, a checked path can change before deletion. For a negative-path claim,
establish that required preconditions completed, the intended target operation
was reached and caused the failure, and relevant aftermath matches the contract.
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

Rerun a command only when relevant inputs or conditions changed, a named open
acceptance question can be answered by that run, or a binding project protocol
requires it. Name the expected evidence. Unchanged repetition without new
information is not justified. Concurrency, stochastic or flaky behavior can
require repeated observations when tied to the actual claim.

Do not repeat a failed correction strategy unless new evidence or changed
conditions support the next attempt. If the same cause persists or the diagnosis
is unsupported, return to the owner, contract and evidence before patching again.
A new symptom-specific patch is not a new approach. Without a supported next
approach, stop that repair path, report the blocker and continue independent
work. Do not weaken acceptance or bypass host attempt limits. New evidence that
identifies a bounded cause can justify a focused correction.

After two unsuccessful corrections of the same failure or evidenced cause,
reassess the owner, contract and evidence before another patch. Different
reproductions, new failure output or passing existing checks do not reset this
checkpoint. New output supports a next attempt only when it changes or
substantiates the causal explanation.

After decisive evidence passes, record the concise result once and
continue the requested development or complete the task. Add no checks,
independent reviews or bookkeeping unless a separate changed behavior,
unresolved material risk or binding requirement remains. Group required
reviews at the completed boundary of their scope, not after each edit or
tool result, unless their protocol requires an earlier review.
Reviews serve assessment and correction during development. Do not permanently
store their texts, raw test logs or a complete check history by default. Keep
only results and open limits needed for further development, plus independently
required records.
An earlier aggregate pass becomes stale when related production code or tests
change afterward; rerun the smallest aggregate check covering the final tree or
narrow the completion claim.

Do not fix unrelated suite failures unless they block the requested outcome or
the user expands scope.

## Inspect the final change

Inspect the final scoped diff and repository state. Confirm that the outcome
resides in its canonical owner, each hunk serves the request or a named risk,
and required guarantees and acceptance remain intact. For generated output,
inspect the source owner and affected consumer output. Reuse reviewed unchanged
content and evidence; revisit affected content after a correction. Tie completion
to the final tree and report material unverified behavior.

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
