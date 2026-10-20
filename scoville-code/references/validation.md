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
- **Defect:** Before correcting, establish a violation of the requested behavior
  or an independent contract; a test mismatch alone is not proof. Reproduce when
  practical, then verify the same case after correction.

Use a broad release, readiness, platform or migration gate only when the task
makes that completion decision or a binding project rule requires it. Otherwise
exercise each changed behavior and concrete material failure with the narrowest
decisive check. Risk alone does not expand the task.

When a change alters a symbol used elsewhere, exercise each independently
affected contract variant; one affected use is sufficient when inspection finds
only one variant.
Derive test expectations from requested behavior or an independent contract,
not solely from current implementation. Review existing assertions affected
by the task on the same basis; revise expectations that merely pin the current
implementation. Allow equivalent implementations and
authorized behavior changes while preserving required guarantees. For internal
work, use independently justified bounds unless the contract requires an exact
count.

Before judging, confirm the relevant preconditions, actual measured path and
a measurement that distinguishes the claimed result from the failure being
checked. For a claimed state change, observe a starting state different from
the expected result. Reuse existing observations; add a negative probe only
when they leave this open. A broken, skipped or non-discriminating check cannot
prove success.

An independently implemented actual consumer can establish boundary expectations.
A constant copied by both sides or the producer's own round trip does not
establish compatibility.
Controlled deterministic checks remain sufficient for behavior that does not
claim such a boundary.

Select evidence by subject:

| Subject | Meaningful evidence | Avoid |
| --- | --- | --- |
| Parsed format, package/import structure or consumer-read version declarations | Protect the actual program/build/host contract; compare changing values with their owner or each other. | Pinning incidental source text or today's values. |
| Instruction/documentation prose | Verify its effect through behavior. | Exact wording assertions unless the user requires that wording. |
| Diagnostics | Failure status, identified input/condition, corrective information and corrected invocation. | Sentence matching. |
| Complete unchanged transfer or independently required artifact integrity | Exact content comparisons where that contract requires them. | Replacing exactness with an insufficient approximation. |
| Ordinary generated/copied outputs | Successful current creation and expected outputs. | Content/hash comparisons without task, binding contract or concrete defect requiring them. |

Keep the required outcome when replacing wording assertions with behavior checks.

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

Retain the first complete diagnostic. On repeated output, report the stable
failure signature and meaningful delta rather than printing the same large log
again.

## Stop repetition

Reuse completed work, reviewed content and complete passing results while their
requirements, inputs, files, dependencies, runtime, configuration and environment
remain relevantly unchanged. A new Step, role, assignment, review or release phase alone
does not justify repetition. A required independent review of previously
unreviewed content is not repetition; it reuses still-valid results instead of
rerunning their checks. Concurrency, stochastic or flaky claims may require
repeated observations tied to the actual claim.

| Correction state | Next action |
| --- | --- |
| New evidence or changed conditions support the failed strategy | Retry only when they change or substantiate the causal explanation. Different reproductions, new failure output or passing checks alone do not. |
| Unsupported diagnosis, or two unsuccessful corrections of the same failure or evidenced cause | Return to owner, contract and evidence before another patch. A symptom-specific patch is not a new approach. New evidence for a bounded cause may justify a focused correction. |
| No supported next approach | Stop that repair path, report blocker and continue independent work. |
| Decisive evidence passes | Record the concise result once and continue or complete the requested work. |

Do not weaken acceptance or bypass host attempt limits.

Before adding a check, review or record:

1. Use available evidence first. Add work only for a named open question about
   changed behavior, a material risk or changed conditions, or when the user,
   a binding requirement or a protocol requires it.
2. Choose the cheapest check that can decide the question. If no authorized
   check can add decisive evidence, stop probing that question and report the
   required behavior as unverified. An unresolved requirement alone does not
   justify repeated ineffective probing.

Group required reviews at their completed scope unless their protocol requires
an earlier review. Keep only results and open limits needed for further work
plus independently required records; no review texts, raw logs or full history
by default. When updating a current result summary you maintain, search it for
each item changed by the new result and replace every superseded status.
Retain required earlier evidence with its version and measurement limits.
Plan and Decision records keep their own update rules.

An earlier aggregate pass becomes stale when related production code
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

Report what was checked and its actual result; include detail only where it
affects acceptance or the next decision. Distinguish a
clean compile, source review, unit test, rendered interaction, live-system check,
and deployment; one does not imply another. If a check was skipped, failed, or
could not run, say so and narrow the claim. Never cite stale evidence as proof of
the final change.

Prefer decisive status, failures and observations to unnecessary counts. Compute
a count only when it affects acceptance or a decision; verify the collection
total rather than reporting per-element counts.
