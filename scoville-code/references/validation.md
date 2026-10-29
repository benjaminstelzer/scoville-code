# Validation and Completion Evidence

Use the cheapest decisive evidence for changed behavior, required guarantees
and credible failure consequences. A pass proves only what the check exercised.

## Contents

- Select proportional checks
- Handle failures
- Stop repetition
- Inspect the final change
- Report the evidence

## Select proportional checks

Validation is sufficient when independent changed behaviors and material risks
have decisive evidence and another check would not plausibly change the result.

For relevant unresolved runtime or memory costs, use realistic input sizes or
a focused measurement that can decide between the alternatives. No universal
benchmark suite is required. When cache use changes, check freshness,
invalidation and context separation as applicable to that change.

- **Explore:** Use the cheapest decisive observation for the hypothesis.
- **Develop:** Prefer an existing focused test, typecheck, lint, build, or direct
  execution. Add a test only when it protects observable regression-prone
  behavior or a material invariant in the project's existing harness.
- **Defect:** Before correcting, establish a violation of the requested behavior
  or an independent contract; a test mismatch, audit finding or review finding
  alone is not proof. Reproduce it, or trace it through normal supported use or
  a reachable attack path when reproduction is impractical; then verify the same
  case after correction.

Use broad release, readiness, platform or migration gates only for that requested
decision or a binding project rule. Evidence requirements do not expand permissions.

When a change alters a symbol used elsewhere, exercise each independently
affected contract variant; one affected use is sufficient when inspection finds
only one variant.
Derive expectations from requested behavior or an independent contract. Review
affected existing assertions on that basis: preserve independent guarantees,
including locks, rollback, no-write behavior and fresh-process readback when
required; revise assertions that merely pin implementation. Allow equivalent
implementations and authorized behavior changes. Use independently justified
bounds unless exact counts are contractual.

Before judging, confirm the relevant preconditions, actual measured path and
a measurement that distinguishes the claimed result from the failure being
checked. For a claimed state change, observe a starting state different from
the expected result. Reuse existing observations; add a negative probe only
when they leave this open. A broken, skipped or non-discriminating check cannot
prove success.

Use an actual independent consumer to establish compatibility across a claimed
boundary; copied constants or a producer's own round trip cannot establish it.
Controlled deterministic checks suffice for claims within the behavior they run.

Select evidence by subject:

| Subject | Meaningful evidence | Avoid |
| --- | --- | --- |
| Parsed format, package/import structure or consumer-read version declarations | Protect the actual program/build/host contract; compare changing values with their owner or each other. | Pinning incidental source text or today's values. |
| Instruction/documentation prose | For wording-only edits, compare clarity, consistency and preserved meaning with the baseline. For changed required behavior or claimed effectiveness, test the affected outcome under the applicable evaluation contract. | Exact wording assertions unless that wording is binding. |
| Diagnostics | Failure status, identified input/condition, corrective information and corrected invocation. | Sentence matching. |
| Complete unchanged transfer or independently required artifact integrity | Exact content comparisons where that contract requires them. | Replacing exactness with an insufficient approximation. |
| Ordinary generated/copied outputs | Successful current creation and expected outputs. | Content/hash comparisons without task, binding contract or concrete defect requiring them. |

Keep the required outcome when replacing wording assertions with behavior checks.

A stub, mock or fixture proves only exercised behavior. If it replaces a
dependency or interaction the claim relies on, exercise the actual boundary or
narrow the claim; unmet required acceptance stays open.

For stateful claims, trace the actual factory/configuration/call path to the
observed stored state, including participating processes. An isolated instance
or separate snapshot does not prove application binding.

For changed protection, verify valid use and the guarantee where the effect
occurs, accounting for state that can change after a prior check. Fault injection
must model a credible path under SKILL.md's Failure consequences rule. Negative
evidence must establish:

```text
Required preconditions completed → target operation reached and caused failure
  → relevant aftermath observed against the contract
```

Earlier rejection does not prove protection at the target boundary. Existing
unambiguous return, state or call observations suffice; add no instrumentation
framework merely to create evidence.

## Handle failures

Evaluate each check's own exit status and diagnostic under the shared
[shell rules](shell-commands.md); a later success must not hide a failure.

Diagnose failed checks against the contract and relevant baseline. Correct
change-caused failures; keep unresolved causes explicit. Apply SKILL.md's
integrity rule to assertions and validators, distinguishing replaced contracts
from unmet ones. If requirements conflict or the goal is infeasible, explain
the evidence and stop that path instead of presenting a substitute as success.

For infrastructure failure, use the project's documented setup when relevant.

Retain the first complete diagnostic. Report the stable failure and meaningful
delta on repetition under the shared [data evaluation](machine-data.md) and
[output capture](output-delivery.md) rules.

## Stop repetition

Reuse reviewed content and complete passing results while requirements, inputs,
files, dependencies, runtime, configuration and environment remain relevantly
unchanged. A new Step, role or phase alone does not require reruns. A required
independent review of unreviewed content remains necessary and reuses valid
results. Repeat observations only when the actual concurrency, stochastic or
flaky claim needs them.

| Correction state | Next action |
| --- | --- |
| Correction failed | Reassess the cause against owner, contract and evidence. Continue only with a supported next diagnosis or an approach substantiated by changed evidence or conditions; another symptom patch or additional output alone is insufficient. |
| No supported next approach | Stop that repair path, report blocker and continue independent work. |
| Decisive evidence passes | Record the concise result once and continue or complete the requested work. |

Do not weaken acceptance or bypass host attempt limits.

Before more checks, reviews or records, use available evidence and identify the
open question, changed condition or binding requirement. If no authorized check
can decide it, stop probing and report the required behavior as unverified.

Group required reviews at completed scope unless their protocol requires an
earlier review. Keep results, open limits and independently required records;
update superseded statuses in maintained summaries. Preserve required earlier
evidence with its version and limits. Plan and Decision records own their updates.

An earlier aggregate pass becomes stale when related production code
or tests change afterward; rerun the smallest aggregate check covering the final
tree or narrow the completion claim.

Do not fix unrelated suite failures unless they block the requested outcome or
the user expands scope.

## Inspect the final change

Inspect the final scoped diff and repository state for canonical ownership,
authorized scope and preserved acceptance. For generated output, inspect its
source and affected consumer output. Apply the required Code review quality
route; reuse unchanged reviewed content. Tie completion evidence to the final
tree and report material unverified behavior.

## Report the evidence

Report actual checks and results, material failures and limits. Distinguish
source inspection, compilation, unit tests, rendered interaction, live-system
checks and deployment; one does not prove another. Skipped, failed, unavailable
or stale evidence cannot support a pass. Count only when it affects acceptance
or a decision, checking the whole relevant collection.
