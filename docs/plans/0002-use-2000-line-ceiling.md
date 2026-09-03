---
format_version: 1
id: PLAN-0002
status: completed
created: 2026-08-31
updated: 2026-09-03
---

# Raise the file ceiling to 2,000 lines

## Goal

The current Scoville Code rule, its evaluation definitions, and the public
documentation use the user-selected Checkstyle value of 2,000 lines. The
canonical package and the local Codex and Claude copies match. Fable then
reviews the completed Skill.

## Non-goals

- No change to the other maintainability rules or their exceptions.
- No rewriting of historical completed Plan content.
- No SkillOpt run, benchmark, commit, push, or GitHub release without a separate
  request.
- No change to Fluid Base or other Scoville Skills.

## Work items

### W-001 Adopt the new file ceiling completely

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0002]
Outcome: The active Scoville Code Skill uses 2,000 lines with unchanged priorities and exceptions and is available in every local package copy after validation.
Acceptance: The active rule and current documentation use 2,000. Edge cases above the ceiling remain decision-sharp. Historical records remain as history. Skill, JSON, link, Plan, diff, and package-synchronization checks pass. Fable reviews the completed package, and confirmed errors are corrected. SkillOpt or behavioral tests that were not run are identified.
Steps:
1. Align the active rule, cases, and current documentation with 2,000 lines.
2. Validate and synchronize the canonical package and the Codex and Claude copies.
3. Ask Fable to review the completed Skill and the changed cases in read-only mode.
4. Correct confirmed errors and repeat the affected checks.
5. Record evidence and complete the Plan.
Evidence: [Active package contains one 2000-line declaration and no active 1000-line wording, Evaluation JSON parsed with 10 unique cases and the explicit oversized-file fixtures 24000 2400 and 2300 all exceed the 2000-line ceiling, Skill validation passed for canonical Codex and Claude packages, All 5 package files match across canonical Codex and Claude roots, Local Markdown link inspection passed across 13 files, Fable read-only review found the active rule and cases consistent, Fable evidence-wording finding corrected in ADR-0002, Change reference contains no line longer than 100 characters, SkillOpt and model-behavior tests were not run]
