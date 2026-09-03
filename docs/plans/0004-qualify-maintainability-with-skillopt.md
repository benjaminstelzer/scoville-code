---
format_version: 1
id: PLAN-0004
status: completed
created: 2026-09-01
updated: 2026-09-03
---

# Qualify the maintainability rules with SkillOpt

## Goal

The current Scoville Code candidate is evaluated in the local SkillOpt Studio
isolation against the last published control package. A frozen 8/4/4 benchmark
measures the new maintainability decisions and existing routing boundaries. The
qualification ends with a hash-bound promotion decision and a one-time holdout
only for eligible arms.

## Non-goals

- No commit, push, GitHub release, or update to public tags.
- No installation of a generated candidate in Codex or Claude.
- No automatic adoption of a SkillOpt proposal based on a total score or lower
  token count.
- No repetition, rewriting, or reminting of a consumed holdout.
- No change to other Scoville Skills or their benchmarks.

## Work items

### W-001 Freeze packages and executable benchmark

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0003]
Outcome: The control and candidate are isolated in SkillOpt Studio with a validated 16-case benchmark and complete hash bindings.
Acceptance: The control package comes from the latest published tag. The candidate matches the current five-file package. Train, Validation, and Test contain 8, 4, and 4 unique cases. Prediction and scoring are separate. The new configuration uses the current Studio revision with Sol xhigh as optimizer and Terra medium as target model. Preflight reports ready.
Steps:
1. Resolve the current Studio contract and the latest published control package.
2. Copy both complete packages into separate read-only snapshots.
3. Make the ten existing cases executable and add six counterexamples.
4. Hash the benchmark and packages and bind them to a new configuration.
5. Run static benchmark validation and token-free preflight.
Evidence: [GitHub Release and local tag v1.0.17 resolve to commit dff5c4101f4a93ade848dacc17366eb9d566f113, Control package tree SHA256 is c499559a0478414973bcaefa1b6ef00500f5df32b705aea2c23bd96e710f6988, Candidate package tree SHA256 is 1a5d6608c06c627b130256ab9483e677c41524b1e2f62d29df8da6d0098bacbf, Benchmark validation passed with 8 Train 4 Validation 4 Test and 16 unique IDs, Prediction inspection found no scorer object or expected string leakage, Benchmark lock binds 14 files and Test seal binds 4 items, Control and candidate preflights reported ready on SkillOpt ba820b500f9da96685cf2780c7dc85ed4eb6563e, Both preflights confirmed Terra medium Sol xhigh global Skill isolation and disabled network, Both preflights reported test_payload_opened false]

### W-002 Run open A/B qualification

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0003]
Outcome: The control and candidate have comparable open behavioral evidence and a reasoned decision about a possible optimization run.
Acceptance: A Validation smoke passes. Both arms run on Train and Validation. Validation is executed with three independent run IDs per arm. Every run records agent_ok, hard, behavior_hard, efficiency_hard, failed invariants, commands, and provider tokens. A confirmed Skill failure triggers at most one conservative training run. A proposal remains unpromoted without all open gates passing.
Steps:
1. Run one Validation case per arm as a wiring check.
2. Run Train and Validation for the control and candidate with fresh run IDs.
3. Repeat Validation independently three times per arm and compare stability.
4. Classify failures as Skill, benchmark, or infrastructure failures.
5. Only after a confirmed Skill failure, run one conservative training step and repeat the open A/B evaluation.
Evidence: [Initial V1 smokes were retained with agent_ok false after an invalid Studio refresh token, Studio authentication was refreshed once and the Sol xhigh optimizer smoke passed, V1 through V5 preserve all observed benchmark and infrastructure failures as separate run evidence, V4 and byte-identical V5 Train predictions passed 8 of 8 hard gates for both arms, V6 preflight reported ready with 8 Train 4 Validation 4 sealed Test and test_payload_opened false, Six independent V6 Validation runs completed with agent_ok true, Control and candidate each passed 3 of 4 in all three Validation repetitions, Every Validation failure was maint-narrow-security-fix on expected_json_subset only, Both arms applied and tested the narrow security fix but omitted the scoped oversized-file concern, One conservative SkillOpt step completed with 22 calls and 1124603 tokens, SkillOpt rejected its 10690-character proposal after Selection remained 3 of 4, Best origin remained initial_skill with zero accepted edits, Normalized best Skill bytes match the input candidate exactly]

### W-003 Complete the promotion decision and holdout

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0003]
Outcome: The eligible candidate and control have one-time holdout evidence, or the holdout remains demonstrably sealed because the open gates did not pass.
Acceptance: Only openly qualified arms are each run once with valid_unseen. Test bytes and gold remain unopened before the gate decision. Raw results and possible benchmark adjudication remain separate. The exact candidate hash is documented as rejected from qualification or eligible for promotion. Static Skill, Plan, JSON, link, diff, and package-synchronization checks are then reported with their limits.
Steps:
1. Check open gates and hash bindings for holdout eligibility.
2. Run the control and eligible candidate once each with valid_unseen.
3. Classify raw failures without retry, reminting, or gold changes.
4. Document the qualification decision and evidence limits in the repository.
5. Run final local checks and complete the Plan.
Evidence: [No arm passed every open hard gate and Holdout eligibility was denied, V6 run inspection found zero valid_unseen executions, V6 Test seal remains sealed with 4 items and SHA256 3afcdc76e922d69a18119e43c448fa94f5edc10be56a5348c275fbf23c3e78e4, Machine-readable evidence records outcome not_qualified and zero accepted edits, Benchmark evidence documents the stable failure and withheld Holdout, Canonical snapshot Codex and Claude packages match across all 5 files, Skill validation passed for canonical Codex and Claude packages, Evaluation and qualification JSON parsed with expected counts and outcomes, Local Markdown link inspection passed across 16 files, Plan profile validation passed with 4 plans 6 work items and 3 decisions, Git diff check passed with only a line-ending warning]
