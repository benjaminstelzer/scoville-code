---
format_version: 1
id: PLAN-0001
status: completed
created: 2026-09-12
updated: 2026-09-12
---

# Skill compliance and work efficiency

## Goal

Improve instruction application and reduce avoidable search, recovery and verification cycles using the September 12 session audit. Obtain Astra's explicit approval of this implementation plan before changing Skill behavior; revise and resubmit actionable objections until approved. Use Astra Low for behavioral tests. Preserve required evidence and report measured work separately from account quota or causal savings.

## Non-goals

No private project product changes, public releases, commits, global Codex configuration changes, separate Astra Skill variants, blanket shortening, new orchestration framework or relaxed acceptance gates. Do not change already adequate worker or UI rules solely because historical sessions violated them. Local installation covers only changed Skill files in existing Codex and Claude installations; preserve personal configuration.

## Work items

### W-001 Bound discovery and recovery output

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Code's existing location workflow selects candidate source files before broad content reads and recovers only missing relevant output after truncation.
Acceptance: Astra Low fixture runs exercise a named source amid irrelevant browser data and a truncated reference read; observe scoped reads and complete relevant recovery without rescanning the payload. Explicitly named generated or trace sources remain readable. Compare baseline and changed instructions using identical fixtures and requested settings.
Steps:
1. Secure Astra approval of the complete plan and freeze relevant source baselines and fixtures in the task temp directory.
2. Replace the existing location paragraph with concise operational search and read boundaries; preserve justified expansion and explicit-source exceptions.
3. Run bounded baseline and changed behavioral checks and inspect the required actual read and recovery traces; text-only answers do not satisfy this gate.
Evidence: [Astra approved consultation 02; skill-fix-review-2026-09-12.md, Paired actual read and edit traces passed; skill-fix-acceptance-2026-09-12.md Code section]

### W-002 Compose one UI verification batch

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: WordPress validation shares the current UI batch boundary and evidence without triggering checks after each small edit; canonical framework ownership remains explicit before custom styling.
Acceptance: Astra Low tool-capable fixture cases record verification scheduling and evidence handling for several related edits followed by one source-measure-visual sequence and one correction batch; a missing framework primitive is handled through its canonical owner. Instrumented fixture events prove scheduling only; browser rendering remains deferred. Checks retain distinct evidence types. Inspect current UI owner rules and change them only if a concrete ambiguity remains; record adequate unchanged rules as regressions.
Steps:
1. Reconcile the WordPress core and validation reference subsequent-edit wording with current UI batching and evidence reuse.
2. Test ownership and batch behavior with baseline and changed composed instructions using identical fixture inputs.
Evidence: [Paired executed scheduling and owner fixtures passed; skill-fix-acceptance-2026-09-12.md WordPress section]

### W-003 Restore necessary Plan context without redundant reloads

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Plan distinguishes available unchanged instructions from missing context and live mutable records; historical restrictions retain their actual subject and scope.
Acceptance: Astra Low tool-capable cases cover available references, missing relevant contents despite an unchanged hash, changed live Plan state, and a Gemini-specific stop alongside authorized Codex work. A sequential fixture exposes an observed change from reference A to B at the same path and requires reloading B before the dependent action while reusing available unchanged references. Missing instructions and live records are read; unrelated history is not reloaded. An applicable stop still blocks dependent action and ambiguity does not create authority.
Steps:
1. Replace the per-operation Skill-reference hash prescription with availability and change-aware reuse: retain a known source identity and reload on observed edits, version changes or a stale-source signal; inspect the relevant source when freshness is uncertain. Preserve exact-byte guards for mutable Plan writes.
2. Add subject-scoped restriction handling only where the existing Plan contract lacks it.
3. Run paired fixture checks and the existing Plan structural test suite once after changes.
Evidence: [Paired three-turn actual read traces passed; skill-fix-acceptance-2026-09-12.md Plan section, Existing Plan suite passed 50 tests]

### W-004 Qualify and activate the bounded fixes

Status: done
Depends on: [W-001, W-002, W-003]
Blocked by: []
Decisions: []
Outcome: The approved fixes are validated and synchronized into existing local installations with an honest acceptance summary and retained review result.
Acceptance: W-001 through W-003 have their required tool-executed fixture evidence before installation. A missing runner or required trace leaves the owning item incomplete and blocks W-004 installation and completion; text probes are supplemental only. Changed packages pass applicable syntax and existing tests; inspect diffs and compare installed changed files byte-for-byte. Report any compatibility-field validator limitation separately. Record matched behavioral outcomes and available usage without inferring quota savings or improvement from unchanged behavior. Native discovery, real compaction, browser rendering and interruption remain separately unqualified.
Steps:
1. Finish W-001 through W-003 and run one bounded unchanged-worker wait regression without starting real workers or external jobs.
2. Use isolated tool-capable fixtures; on unavailable or denied required tools preserve incomplete status and block installation. Changing this gate requires an explicit user-approved scope change before installation.
3. Resolve observed regressions before installation; preserve a concise result and review metadata in this development owner and remove disposable evidence only through permitted cleanup.
4. Synchronize changed files into existing Codex and Claude packages while preserving unrelated files and local configuration.
Evidence: [Ten installed readbacks match five tested source files; skill-fix-acceptance-2026-09-12.md Local activation, Cleanup denied by automatic policy; temporary evidence remains]
