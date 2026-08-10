# Scoville Code benchmark evidence

## Final reliability-first qualification

The promoted package is the candidate from
`scoville-code-final-v7-v25-validation-next-action-boundary-open-ab`,
qualified on 2026-08-10. Routing used `gpt-5.6-sol` at `xhigh`; execution used
`gpt-5.6-terra` at `medium`. Network access and prediction reuse were
disabled.

| Arm | Split | Skill cases passed |
| --- | --- | ---: |
| Expanded control | Train | 18/18 |
| Expanded control | Validation | 9/9 |
| Expanded control | sealed Test | 3/3 |
| Compressed package | Train | 18/18 |
| Compressed package | Validation | 9/9 |
| Compressed package | sealed Test | 3/3 |

The candidate passed all 30 cases across result semantics, routing, process,
efficiency, provider completeness, zero retries, zero shell calls, and the
required exact-once reads. The sealed Test ran exactly once per arm through
separate fresh agents with distinct UUIDs and no memory access.

## Raw benchmark-contract evidence

Raw scores remain preserved separately from Skill scores.

- The Validation field `first_operation` did not distinguish the operation
  currently first in the supplied patch from the operation that must be first
  for safe behavior. Both closed-enum readings occurred with the decisive
  `premature_publication` verdict and otherwise perfect gates. The final Skill
  score accepts either reading without changing the raw exact-Gold score.
- The sealed Test Route Gold assigned a destructive authorization review to
  Planning-only. The frozen Skill contract assigns High-risk authorization and
  destructive-boundary review to Change. Both arms selected Change-only, read
  the Core, Change reference, and request exactly once, and returned the exact
  safe result. The raw exact-Route-Gold score remains 2/3 per arm; the
  contract-correct Skill score is 3/3.
- One observer timed out while waiting for the candidate Test wrapper. The
  original one-shot process continued and completed with exit code 0; its
  existing claim proves that no retry or remint occurred.

No benchmark item, Gold file, sealed payload, or execution result was changed
after model execution.

## Token effect

Token counts use `o200k_base` over exact UTF-8 Skill files loaded by the
executor.

| Split | Expanded control | Compressed package | Change |
| --- | ---: | ---: | ---: |
| Train | 56,262 | 49,584 | -6,678 (-11.87%) |
| Validation | 28,131 | 24,792 | -3,339 (-11.87%) |
| sealed Test | 9,265 | 8,152 | -1,113 (-12.01%) |
| Total | 93,658 | 82,528 | -11,130 (-11.88%) |

| Package measure | Expanded control | Compressed package | Change |
| --- | ---: | ---: | ---: |
| Always-loaded Core | 2,416 | 2,045 | -371 (-15.36%) |
| Complete package | 4,614 | 4,243 | -371 (-8.04%) |

Provider totals also include routing, generation, and cache behavior, so they
are not used as the deterministic compression measure.

## Reproducibility bindings

- Promoted Core SHA-256:
  `F70BB99BFA2962E6EBD643746D5802676CBAD375198B2EF154FD92A647809D41`
- Qualified candidate package-tree SHA-256:
  `CCA9872ACBED5AAC889105D511688D8975479458350C5D5A896DA57493E7C942`
- Expanded-control package-tree SHA-256:
  `68B08C46D4BA34DB7CB33E8B26190F4D5071E278D770A5CFD19025893E8A325B`
- Final report SHA-256:
  `F91B843780B299808AB27D4E8A00649C46A331B78889A938368E36F01668E9D9`
- Test adjudication SHA-256:
  `6321F292CCACE50FD47F196D84D1CC48FE85C15D33A955A10FD1F2E396838375`
- Execution binding SHA-256:
  `1C2A8F00D04898A93E70D58B7FFA21618C1A1CA7F40E4A58FD829598C27465F5`
- Sealed-Test aggregate SHA-256:
  `206E2CCAA5B9A840ABBDE05F6E4B6DFF31456A504AB18EB3C01DF1CDD192CFF4`
- SkillOpt revision: Microsoft
  `ba820b500f9da96685cf2780c7dc85ed4eb6563e`

The complete reports, per-case metrics, final answers, traces, provider usage,
and one-shot claims remain in the central optimization workspace under
`skillopt-studio/runs/scoville-code-final-v7-v25-validation-next-action-boundary-open-ab/`.

## Overall optimization history

The final four-Skill inventory records 797 run artifacts, including 742
technically valid benchmark runs, 5,762 observed model calls, and 3,452 case
executions. Code accounts for 305 artifacts, 272 valid benchmark runs, 2,414
model calls, and 1,394 case executions. The central machine-readable snapshot
has SHA-256
`1270F95CF9777EBC8E97151E37DFA5525D3E2DB8A6F0163DFBD71C8DA395A781`.

## Interpretation limits

The result establishes non-regression and lower prompt payload on the frozen
cases. It does not prove universal correctness, deterministic behavior, or the
same result on a weaker executor.
