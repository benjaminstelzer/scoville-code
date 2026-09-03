---
format_version: 1
id: PLAN-0001
status: completed
created: 2026-08-31
updated: 2026-09-03
---

# Maintainable file and module structure in Scoville Code

## Goal

Scoville Code should contain concrete, verifiable rules for maintainable code.
The request specifies no more than 1,000 lines per file, with justified
exceptions; meaningful directories for adapters, plugins, and import functions;
and logically named files. Other relevant gaps will be filled while existing
rules remain in their current locations. An additional user request requires a
comparison with professional, language-independent development practices.
Fable reviews the expanded Plan before the Skill, its tests, documentation, or
installed copies are changed.

The implementation covers the canonical repository
`Z:\Projekts\AI\scoville-code-anti-ai-slop` and then the existing local
Scoville Code copies for Codex and Claude. Publication is not part of this task.

**Verified baseline, 2026-08-31**

- The Code repository has no preceding changes at `dff5c41`.
- Core and the installed Codex core are byte-identical. The Skill already has
  rules for canonical ownership, scope, risk, error handling, and proportional
  tests. Concrete size and structure rules are missing.
- `references/change-workflow.md` requires existing naming conventions and
  small, coherent changes, but defines neither file sizes nor directory
  boundaries, function scope, or dependency direction.
- Fluid Base was read only. The project path named in its `AGENTS.md` is
  `C:\Users\benja\Desktop\DIVI5 Plugin`. That checkout and
  `Z:\Projekts\AI\divi-5-fluid-base` are at `46ee6e9b`. The unversioned Desktop
  directories `research/` and `workspace/` remain untouched.

**What Fluid Base actually demonstrates**

The examples come from `src/divi-5-fluid-base/`, the naming convention in
`docs/plugin-specific/file-naming-convention.md`, and the Developer Guide.

| Observation | Evidence | Transferable principle |
| --- | --- | --- |
| Generic admin framework separated from the product | `includes/dynamitec-admin-framework/` and `assets/js/dynamitec-admin-framework/` versus `assets/js/admin/` | Framework and product-specific adapters have separate responsibilities and directories. |
| Different platform editions separated | `includes/traits/edition/divi4/`, `includes/traits/edition/divi5/`, `divi5fb-trait-edition-adapters.php` | Edition and integration details remain behind one clear, shared call boundary. |
| Configuration, schema, and specifications are discoverable | `includes/config/`, `includes/schema/`, `includes/overrides/` | Files and directories follow their actual responsibility. |
| Files have domain-specific names | `divi5fb-trait-frontend-css-cache.php`, `divi5fb-trait-override-sync-jobs.php`, `dynadm-scroll-state.js` | Names identify the task and domain instead of using numbered file fragments. |
| Import/export is a concrete functional area | `includes/traits/divi5fb-trait-import-export.php` | The example is a separate file, not a separate import directory. Language import statements are not meant. |
| Generated content can be large | `divi5fb-config-setup-reset-presets.php`, 28,697 lines, names its generator | Edit source data and the generator; do not split generated output merely to satisfy a line count. |
| A sound base structure does not guarantee small files | 17 of 115 examined PHP/JS/CSS files exceed 1,000 lines, excluding vendor and minified files | Line count is a review signal, not proof of an error or of a useful concrete split. |

The second large data file, `divi5fb-config-divi-default-baselines.php`, has
14,099 lines and provenance metadata. The readable runtime code
`assets/js/divi5fb-runtime.js` has 4,066 lines. This inventory is not a
refactoring request and not a judgment that each of these files should be
split. Product prefixes, PHP traits, and specific directory names do not become
universal Scoville standards.

**Intended rule scope**

| Area | Already present | Addition or clarification |
| --- | --- | --- |
| File size | No concrete limit | Hand-written source files should generally have no more than 1,000 physical lines in normal project formatting. This is not a target, and the limit must not be gamed by removing comments or compressing code. Split earlier when a meaningful domain boundary exists. |
| Exceptions and legacy code | Small changes, no unsolicited restructuring | Generated, minified, and externally managed files are not to be split according to this limit. For a coherent hand-written file over 1,000 lines, explain why a concrete split would increase coupling, break invariants, or conflict with a necessary format. Do not turn a narrowly scoped legacy fix into an unsolicited large split. |
| Directories | Respect the existing architecture | Put actual adapter, plugin, and data-import subsystems in their own clearly named directories or existing equivalent project areas. Do not move an existing small, coherent single-file capability merely to satisfy a schematic directory structure. Do not create empty future directories. |
| Meaning of import | Not addressed | Data imports and integrations are structural boundaries. Language `import`, `use`, or `require` statements remain with the consuming module according to existing language and tool conventions. There is no directory requirement for each import statement. |
| Names and responsibilities | Adopt naming conventions | Give each file or module one comprehensible domain responsibility. Reuse existing precise names. Avoid vague catch-all files, numbered fragments, and artificial one-function files. |
| Functions and control flow | Only general coherence | Limit functions to one understandable task and reduce hidden side effects and deep nesting. Extract small helpers only for recognizable concepts or reused logic. Do not impose another universal line quota per function. |
| Dependencies and interfaces | Canonical owner, no parallel paths | Keep dependency direction visible, avoid new cycles, and do not reach into another module's internal files. Keep public module surfaces small. Integration details belong in adapters; domain rules do not belong in generic framework helpers. Do not automatically add a new layered architecture. |
| State and side effects | Preserve relevant state semantics | Give mutable state a clear owner and avoid hidden global coupling. Separate I/O and infrastructure from predictable domain logic where this creates real test or maintenance boundaries. Do not universally require dependency-injection containers. |
| Contracts and configuration | Preserve meaning at boundaries | Make new units and schemas explicit at actual boundaries. Do not maintain domain rules, configuration, or constants requiring justification in multiple divergent places. Do not duplicate existing general boundary rules. |
| Resources | Do not swallow errors or report false success | Any code that creates handles, listeners, timers, or connections needs a clear owner for cleanup. Add retry, cancellation, and timeout mechanisms only when required by the task, an existing contract, or a concrete failure trace. |
| Duplication and abstraction | Speculative helpers and layers already prohibited | Consolidate demonstrated duplication of domain logic in the canonical owner. Do not abstract before a second real consumer or a demonstrated shared invariant exists. |
| Generated sources and runtime | Prefer existing tools | Separate hand-written sources from vendor code, generated output, and build artifacts. Change the generator rather than its output. Language syntax and library APIs must match the declared target version. |
| Traceable dependencies and builds | Only partly concrete | Respect existing manifests, lockfiles, and build entry points. Keep versions of touched dependencies traceable. Do not automatically introduce a package manager or CI platform. |
| Tests and documentation | Proportional, observed checks | After splitting a file or module, test real callers, import/autoload paths, and startup paths. Do not duplicate general testing, linting, and documentation rules. |

The rules remain subordinate to explicit requests, runtime requirements, and
binding project conventions. They neither expand change authority nor
automatically widen the scope of a bug fix. Structural changes continue to be
assessed under the existing risk model.

**Comparison with professional practices, checked 2026-08-31**

The following comparison is a synthesis of the named primary sources, not a
claim that every company uses the same process or architecture. The tools named
there are not installed here.

- Google reviews design, functionality, complexity, tests, names, and necessary
  documentation, among other things. Personal style preferences should be
  separated from binding requirements. This supports concrete review criteria
  instead of more blanket numeric quotas. The sections Complexity through
  Context in [What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
  were read.
- Google's [Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html)
  calls for small, coherent changes with their associated tests and separates
  extensive refactoring from functional changes. The line counts discussed
  there concern change size, not source-file size. What is Small, Separate Out
  Refactorings, and Keep related test code in the same CL were read.
- DORA describes discoverability, reuse, and changeable dependencies as
  maintainability characteristics. Dependency provenance and exact versions,
  as well as reproducible builds, are concrete additions for this Plan. The
  criteria and implementation section of
  [Code maintainability](https://dora.dev/capabilities/code-maintainability/)
  were read.
- Automated builds and fast tests continuously provide feedback on changes.
  For Scoville, this means using existing project-wide checks and honestly
  reporting failures, not receiving new permission to merge or deploy. The
  implementation and common pitfalls in
  [DORA Continuous integration](https://dora.dev/capabilities/continuous-integration/)
  were read.
- The [ESLint documentation for max-lines](https://eslint.org/docs/latest/rules/max-lines)
  explicitly does not claim a universally suitable file size. Its configurable
  rule defaults to 300 lines, whereas
  [Checkstyle FileLength](https://checkstyle.org/checks/sizes/filelength.html)
  uses 2,000. The rationale and options or properties were read. The 1,000-line
  limit is therefore the user/Scoville requirement with justified exceptions,
  not a claimed industry standard.
- DORA evaluates loose coupling by whether changes and tests can be made
  independently, not merely by the use of a particular technology. The
  introduction and architecture tradeoff in
  [Loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/)
  were read. Applied to this Skill, directory boundaries must reflect real
  module boundaries. A microservice, layered, or feature-first structure is not
  prescribed for every project.
- [NIST SSDF](https://csrc.nist.gov/projects/ssdf) integrates security into the
  development process and requires a risk-oriented, applicable selection rather
  than a checklist applied blindly. Overview, SSDF Practices, and SSDF Use were
  read. The [publication overview](https://csrc.nist.gov/Projects/ssdf/publications)
  lists version 1.1 as final and 1.2 as a draft. This Plan does not treat a draft
  as a binding standard. Existing Code rules for security and failure evidence
  remain in effect.

**Implementation in a professional development environment**

As a synthesis, three kinds of rules can be distinguished:

| Rule type | Examples | Treatment in the Skill |
| --- | --- | --- |
| Binding project contract | Target versions, public interfaces, security and data rules, fixed formats | Satisfy existing requirements and test affected contracts. Do not break them for a style rule. |
| Automatable project convention | Formatter, linter, type checking, build, tests, configured size limits | Use existing tools. Name results precisely. Do not add a new universal tool stack. |
| Review judgment requiring justification | Domain coherence, useful file splits, necessary abstraction, exceptions to the 1,000-line limit | Examine concrete effects and the alternative. Do not infer quality from a filename or metric alone. |

The corresponding workflow consists of agreed project rules, a small coherent
change, appropriate local checks, domain review, and the already configured
automated integration checks. Extensive restructuring is visibly separated
from the actual bug or feature change. The Skill follows existing ownership and
approval boundaries. It does not require a new external reviewer for every
small change.

**Fable comparison before implementation**

Fable 5 was consulted twice with high reasoning in a persistent, read-only
session. The backend did not report a concrete resolved model name. The review
took 139 seconds and the prioritized follow-up 68 seconds. Both responses are
advice, not approval or behavioral testing.

The Plan review called the Plan implementation-ready without requiring another
user decision. The following findings are accepted:

- A stricter configured project limit takes precedence over the Scoville limit.
- Exception reasons are examples, not a closed list.
- Contract, test, and documentation rules are not stated twice.
- Retry, cancellation, and timeout rules apply only for an existing task,
  contract, or concrete failure pattern.
- Additions are folded into the existing sections. The current priority of
  security and integrity over maintainability remains unchanged.
- Demonstrated domain duplication is covered without encouraging speculative
  abstraction.
- The five evaluation definitions cover a large generated file, metric gaming,
  a narrow legacy fix, data import versus language import, and real
  caller/startup paths after a split.

Fable's own guideline recommendation names the same areas as must-haves.
Qualitative function splitting, manifests/lockfiles, new units/schemas, and
retry/cancellation rules are useful only conditionally. Function line counts,
directory templates, DI containers, microservices, comment density, coverage
quotas, concrete tool defaults, mandatory reviewers, and CI platforms are not
set universally. The Change reference receives approximately 25 to 35 new
lines. The number 1,000 appears exactly once in the actual rule.

**Planned file distribution**

- The concrete guidance goes into the reference loaded before changes and
  reviews, `scoville-code-anti-ai-slop/references/change-workflow.md`. No new
  reference system or additional loading requirement is needed.
- The new guidance is limited to approximately 25 to 35 lines and folded into
  existing sections. Review priority remains unchanged.
- `SKILL.md` is expected to remain unchanged. Only an actually necessary link
  may be added, without changing activation or risk rules.
- `tests/evaluation-cases.json` receives five scenarios: a large generated
  file, metric gaming, a narrow legacy fix, data import versus language import,
  and real caller/startup paths after a split. They are documented as
  definitions, not as model tests that have already passed.
- README and changelog describe the additions and distinguish historical
  benchmark results from the changed package. Old measurements are neither
  reassigned nor overwritten.
- Local Codex and Claude copies are synchronized only after the Fable comparison
  and validation of the canonical result. Independent local changes must first
  be checked and preserved.

**Questions for Fable before implementation**

1. Does the 1,000-line rule remain effective without causing pointless file
   splitting or unsolicited refactoring?
2. Is the directory rule appropriate to the user request and the Fluid Base
   structure actually inspected, without generalizing its specific technology?
3. Which proposed additions close real gaps, and which are redundant,
   misleading, or too broad?
4. Are important, generally applicable maintainability rules or meaningful edge
   cases for the evaluation definitions missing?
5. Is the existing Change reference sufficient as the sole detail owner, and do
   activation, project precedence, scope, and evidence boundaries remain intact?
6. Does the source comparison accurately represent professional practices and
   cleanly separate evidenced principles, concrete tool defaults, and the
   explicitly requested 1,000-line rule?

## Non-goals

- No changes, splitting, or publication of Fluid Base.
- No changes to other Scoville Skills or global system prompts.
- No prescribed programming language, framework layering, or fixed filename
  structure for all projects.
- No automatic refactoring based only on a line count, and no introduction of a
  new linter, build, or test framework.
- No commit, push, GitHub release, or tag cleanup without a separate request.
- No claimed behavioral test or new benchmark based only on static checks, case
  descriptions, or Fable's Plan review.

## Work items

### W-001 Add maintainability rules after the reviewed Plan

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0001]
Outcome: Scoville Code contains the compared rules for file size, structure, naming, and supplementary maintainability boundaries in the canonical package and the verified local copies.
Acceptance: The source comparison separates professional principles from tool defaults and the user's limit. Fable's read-only review of the expanded Plan precedes every Skill change. Confirmed findings are incorporated into the Plan. The rules preserve project precedence, meaningful exceptions, and narrow change boundaries. Skill validation, JSON validation, link checking, complete diff inspection, and byte comparison of the local package copies pass. Fluid Base remains unchanged. Behavioral tests that were not run are identified.
Steps:
1. Ask Fable to review the Plan against the named Code and Fluid Base sources and assess the relevant findings.
2. Refine the not-yet-started Work Item and, if necessary, the documented Decision according to the reviewed Plan.
3. Add only the maintainability gaps confirmed after the Fable comparison to the Change reference, five evaluation definitions, and associated documentation.
4. Validate the canonical package and synchronize the existing local Scoville Code copies without losing independent changes.
5. Document evidence, remaining limits, and Plan completion.
Evidence: [Fable plan review and prioritized guideline follow-up completed before Skill edits, Seven public primary-source pages inspected for professional-practice comparison, Fluid Base source and structure inspected read-only at 46ee6e9b, Skill validation passed for canonical Codex and Claude packages, Evaluation JSON parsed with 10 unique case definitions, Local Markdown link inspection passed across 11 files, Complete scoped diff inspected and Fluid Base tracked source remained unchanged, Canonical Codex and Claude packages match across all 5 files, No new model-behavior benchmark was run]
