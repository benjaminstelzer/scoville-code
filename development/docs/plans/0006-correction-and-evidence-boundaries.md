---
format_version: 1
id: PLAN-0006
status: completed
created: 2026-09-10
updated: 2026-09-10
---

# Clarify correction scope and evidence boundaries

## Goal

Make three existing Scoville Code requirements more explicit: inspect directly
related failure variants, distinguish mocked behavior from integration evidence,
and reconsider a repeatedly unsuccessful correction mechanism even when the
existing checks pass. Preserve proportionate validation and narrow ownership.

The implementation specification and development-case expectations are in
[correction-and-evidence-boundaries.md](../correction-and-evidence-boundaries.md).
That document records the plan's self-review and owns no execution state.

## Non-goals

- No mandatory test count, exhaustive input matrix, universal integration test,
  new test framework, model-specific rule, or independent-review requirement.
- No change to Skill routing, risk classification, file-size rules, permission
  boundaries, or the user's and repository's existing workflows.
- No Gemini Worker, private project product, installed Skill, release, or historical
  benchmark changes in this plan. Publication and installation are separate scope.
- No claim of improved model reliability from wording inspection or case definitions.

## Work items

### W-001 Clarify and verify bounded correction and evidence requirements

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: The existing Change and Validation references cover the three identified ambiguities without introducing unrelated work or weakening completion evidence.
Acceptance: F1-F3 in the linked specification are implemented at their named owners. C01-C14 have explicit behavior-based expectations with descriptive IDs in the existing development case format and pass a documented semantic self-review. Existing cases remain intact. Skill frontmatter validation, evaluation JSON parsing and unique IDs, local links, native Plan validation, and diff checks pass. The complete candidate diff preserves routing, permissions, existing stop rules, and proportional scope. Evidence distinguishes static inspection from any separately executed model evaluation; no new behavioral qualification is claimed from static checks.
Steps:
1. Re-read the current source and repository state against the recorded baseline; reconcile intervening changes before editing and preserve existing work.
2. Clarify the evidence-based inspection boundary in Change and extend the affected-boundary and repetition paragraphs in Validation using F1-F3; retain the existing root-cause bullet and keep SKILL.md and the remaining reference unchanged.
3. Add C01-C14 to the existing development evaluation-case owner with observable expected and forbidden behavior; preserve historical cases and sealed evidence.
4. Inspect each rule against positive and negative cases and the existing scope and stop clauses; correct ambiguity or duplicated instructions before final checks.
5. Run the named structural checks and inspect the entire candidate diff; record exactly which claims those checks support and leave model reliability unverified without actual evaluation.
Evidence: [2026-09-10 F1-F3 implemented and fourteen new cases reviewed; docs/correction-boundary-verification.md, 24 unique case definitions; ten historical cases preserved; entrypoint and Planning unchanged, Native profile and repository layout passed; YAML and compatibility checked separately from the legacy validator limitation, No new model qualification; later publication request is separate scope]
