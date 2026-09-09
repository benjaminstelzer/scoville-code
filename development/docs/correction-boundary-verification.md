# Correction-boundary verification

Verified on 2026-09-10 for PLAN-0006. The Change reference clarifies the
evidence-based inspection boundary. Validation now distinguishes substituted
behavior from actual integration evidence and recognizes repeated causal
failures across different checks. SKILL.md and the Planning reference are
unchanged.

## Semantic self-review

All fourteen new case definitions were inspected against the final instructions:

- C01/C02: another variant is included through a demonstrated causal path.
- C03/C04/C13: current sufficient evidence, unrelated legacy code and contained
  internal changes do not create extra test or consumer-inspection duties.
- C05/C07: mocks or prepared labels cannot prove the replaced behavior.
- C06: controlled inputs remain valid for directly exercised pure behavior.
- C08: missing permission leaves the specific required acceptance open.
- C09: different checks do not reset two verified failures of the same mechanism.
- C10/C11: unrelated defects and a single failed correction do not meet that trigger.
- C12: diagnosis grants no extra correction attempt or fallback.
- C14: implementation review plus evidence assessment uses Change and Validation
  under the existing routing. No Planning requirement is added.

JSON parsing, required case fields and unique IDs passed for 24 cases. All ten
pre-existing case objects match HEAD. Case definitions and this self-review do
not establish model behavior or new qualification.

## Structural checks and limits

- Native Plan validator: valid, zero errors and warnings.
- Repository layout: passed.
- YAML, package name, description and compatibility: passed. The compatibility
  field is 249 characters and agrees with the README and instruction requirements.
- The legacy Skill Creator quick validator rejected the pre-existing supported
  `compatibility` key. The key was retained. Explicit YAML and required-field
  checks provide the documented fallback; the legacy validator was not changed.
- Local links and the complete scoped diff were inspected. No routing,
  permission, file-size, historical benchmark or sealed-case contract changed.

No new provider evaluation was run. Fable's prior compact review concerned the
plan, not execution of the resulting Skill. Publication and installation are
handled separately under the user's later request.
