# Validation and Completion Evidence

SKILL.md covers the checks of an ordinary change. Read the section for your
situation.

## A check still fails after a correction

| Correction state | Next action |
| --- | --- |
| Correction failed | Reassess the cause against the responsible source, the contract and the evidence. Continue only with a diagnosis the evidence supports or an approach that changed evidence or conditions justify; another symptom patch or more output is not progress. |
| No supported next approach | End that repair path, report the blocker and continue independent work. |
| Decisive evidence passes | Record the result once and continue. |

However many corrections failed, acceptance stays as required and the host's
attempt limits apply. Keep the first complete diagnostic; when a failure
repeats, report the stable failure and what changed. If no authorized check
can decide a question, stop probing and report the behavior as unverified.
Leave unrelated failing tests alone unless they block the requested outcome.

## Before another check, review or record

Name the open question, changed condition or binding requirement the new
check would settle; without one, the evidence you have is enough. Reuse
reviewed content and passing results while requirements, files, dependencies,
runtime and configuration are unchanged; a new step, role or phase alone
requires no rerun. A required independent review of unreviewed content still
takes place, at completed scope unless its protocol asks earlier. After edits
to related code or tests an earlier aggregate pass is stale: rerun the
smallest check covering the final tree or narrow the claim.
When a result changes, replace the outdated status in the summary you
maintain instead of appending a new one.

## What decides a claim

A skipped, broken or failed check proves nothing, and neither does one that
cannot tell the claimed result from the failure.

| Claim | Decides it | Does not decide it |
| --- | --- | --- |
| A state changed, such as a restore or migration | A starting state that differed from the expected result, on the path the product takes | A field that was already empty, counted as restored |
| Stored state works in the application | The actual factory, configuration and call path to the observed store, including participating processes | An isolated instance or separate snapshot |
| Compatible with another component | That component's contract or the real consumer | Constants copied into the test; the producer's own round trip |
| A protection rejects the failure | Preconditions completed, target operation reached and failed, aftermath observed | An earlier rejection: a database fault that stops the state read before the cache read under test |
| Bounded internal work | A justified bound, validly measured; lock, rollback and no-write assertions stay | An exact count of today's reads or queries, or incidental source text, unless contractual |
| Instruction, documentation or error text | Meaning against the baseline; a behavior test where required behavior changed; for an error its status, named input and correction | Exact wording, unless the wording is binding |
| Generated or copied output | Successful current creation and the expected outputs; exact comparison only where an unchanged transfer is the contract | Content or hash comparison without a task, contract or concrete defect requiring it |

Fault injection must model a credible path under [Code quality](code-quality.md).
An existing unambiguous return, state or call observation suffices; add no
instrumentation to create evidence. Report a count only when it affects
acceptance or a decision.
