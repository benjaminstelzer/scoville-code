---
format_version: 1
id: ADR-0003
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: skills/evaluation
---

# Qualify the maintainability rules with SkillOpt

## Decision

The current maintainability rules are qualified with a frozen A/B comparison in
the local SkillOpt Studio. The last released package serves as the control and
the current five-file state as the candidate. The benchmark uses 16 cases with
8 Train, 4 Validation, and 4 sealed Holdout cases. An optimization proposal may
be adopted only after all open hard gates and the one-time Holdout pass.

## Problem

The static checks and independent reviews establish wording and package
synchronization. They do not establish that a target model reliably applies the
new rules in boundary cases or preserves existing routing and validation
decisions.

## Drivers

- The user selected the described SkillOpt test plan for implementation.
- The new rules contain priorities, exceptions, and negative boundaries that a
  text comparison alone cannot prove.
- Control and candidate must receive the same tasks under the same isolated
  model configuration.
- Holdout content must not influence open iteration or optimization.
- Hard behavioral rules take precedence over token or call reductions.

## Considered alternatives

- Check only the ten declarative JSON cases statically. This does not establish
  model execution.
- Start a SkillOpt training run immediately. This would mix diagnosis and
  change.
- Run only the current candidate without a control. This could not distinguish
  existing failures cleanly from newly introduced regressions.
- Repeat or rewrite the Holdout after a failure. This would remove the
  independent promotion boundary.

## Consequences

Qualification requires frozen packages, separate open and sealed cases, and
multiple independent Validation runs. A generated candidate initially remains
a proposal. A real Skill failure can trigger a conservative training run.
Benchmark or infrastructure failures remain as raw evidence and do not justify
retrospective Gold changes.

## Confirmation

A manifest must bind package and benchmark hashes, model roles, the SkillOpt
revision, and split sizes. Preflight, open A/B runs, and three independent
Validation runs per arm must report their hard gates. Only then is the sealed
Holdout run once per arm through `valid_unseen`. Only the exact candidate hash
that was checked may be considered eligible for promotion.

## Revisit when

The local Studio contract, target models, SkillOpt revision, or maintainability
rules change. A new qualification cycle requires new run IDs and a new untouched
Holdout.
