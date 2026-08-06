# Changelog

## 2026-08-06: Standalone authoritative-plan terminology

### Changed

- Generalized plan-composition guidance and evaluation fixtures so the Skill
  works with any authoritative project plan without implying a dependency
  on a particular planning product.

### Validation

- The canonical Skill validator and evaluation JSON parser pass; standalone
  fixtures cover both authoritative-plan and no-plan operation.

## 2026-08-06: ReasonKeep composition and compact validation evidence

### Changed

- Mapped independently resumable outcomes to ReasonKeep Work Items while
  keeping implementation, review, testing, and documentation steps inside the
  same behavior-complete item.
- Required repeated large diagnostics to be reduced to their stable failure
  signature and meaningful delta after the first complete capture.
- Made aggregate evidence stale when later code, tests, or harness changes
  affect the completion claim; the affected aggregate check must be rerun or
  the claim must be narrowed.

### Validation

- Evaluation fixtures cover a small ReasonKeep change, a structural multi-item
  change, repeated Testing Library DOM output, and a test added after the last
  aggregate suite.

## 2026-08-06: Acceptance-path coverage before validation stops

### Changed

- Required decisive evidence to cover every explicit acceptance behavior and
  each concrete coupling that can make a required path behave differently
  before validation stops.
- Clarified that a passing check for one interface, input path, or state
  transition cannot prove a behaviorally distinct path or handoff.
- Preserved the existing ban on unrelated broad suites and combinatorial test
  matrices.

### Validation

- The installable directory passed the canonical Agent Skill validator.
- A history review confirmed that the July validation-economy changes remain
  intact while acceptance-path coverage is restored before the stop decision.

## 2026-08-03: Skill-only distribution and documentation alignment

### Changed

- Scoville Code is distributed through the installable Agent Skill directory,
  with one installation path and one runtime instruction owner.
- Aligned the README structure and installation language with the other
  Scoville skills while retaining Code as the family reference.
- Kept the documentation history focused on the supported skill distribution.

### Validation

- The installable directory passed the canonical Agent Skill validator.
- Repository-wide searches confirmed that documentation and installation
  guidance use the supported skill directory.

## 2026-08-03: Rename to Scoville Code Anti-AI-Slop

### Changed

- Renamed the repository and installable skill from
  `scoville-anti-ai-coding-slop` to `scoville-code-anti-ai-slop` so the Code,
  Scribe, and UI skills use the same family naming scheme.
- Updated the skill name and heading, display metadata, installation URL,
  documented paths, current repository links, and family cross-references.
  Historical changelog entries retain the names that were current when those
  changes shipped.

### Migration

- Replace existing installations under `scoville-anti-ai-coding-slop/` with a
  folder named `scoville-code-anti-ai-slop/`. Do not keep both names installed.
- GitHub redirects the previous repository URL, but skill discovery still
  requires the installation directory and `SKILL.md` frontmatter name to match.

## 2026-08-02: README factual and clarity corrections

### Changed

- Corrected the documented frontmatter size from 64 words to 62.
- Replaced the opaque `No artifact economy` label with a direct description of
  the rule against parallel process artifacts.
- Linked Simon Willison's primary source for the distinction between vibe coding
  and reviewed, tested, understood AI-assisted coding.

## 2026-07-26: Installable skill separated from repository documentation

### Changed

- Moved `SKILL.md` and `agents/openai.yaml` into the
  `scoville-anti-ai-coding-slop/` directory. The installable directory now
  contains only runtime skill files, while README, changelog, and license remain
  at the repository root.
- Updated installation instructions and the rules link to target the named
  skill directory. Its parent directory continues to match the frontmatter
  name.

## 2026-07-26: Runtime-neutral operations, interactive asking, validation floor

### Added

- Modes, risk flags, and the framing questions are internal selectors and must
  never appear in output as a preamble, heading, or checklist. Without this the
  skill invites its own ceremony: an agent that has been handed a rubric tends
  to perform it visibly, which is the Goodhart failure the goal-first rewrite
  set out to remove.
- A validation floor against silent regressions: when a change alters the
  behavior or signature of a symbol used elsewhere, at least one check must
  exercise one of those uses. The surrounding rules all push toward stopping
  early, and nothing previously stopped a focused check on the owner from
  passing while its callers broke. The rule is scoped to behavior and signature
  so that a purely local rename still needs nothing beyond one existing check.
- An infrastructure failure now permits the project's documented setup step
  once before the single substitute check. A missing dependency in a fresh
  environment is routine and cheap to fix; treating it as a reason to report
  unverified was an escape hatch, not restraint.
- A rule for projects without version control: every edit is irreversible, so
  read a file before overwriting it and preserve content the request does not
  touch. This case was previously unhandled, and it is the case with the least
  margin for error.
- Worked examples for all five integrity-floor failures. The goal-first rewrite
  removed the SC1-SC10 examples and left the file almost entirely abstract;
  examples are what makes an abstract rule recognizable in real code.

### Changed

- Asking now scales with the setting. Work that does not depend on the answer
  happens first; then the agent asks once and specifically, before the
  dependent work. When the user is present, one question beats a wrong guess;
  when running unattended, the agent does not block but names the assumption it
  took. The previous single rule was tuned for unattended batches and made
  interactive agents guess at material product ambiguity.
- The final inspection is stated as an outcome, not a command line. It requires
  one inspection of the complete scoped change and the working-tree state using
  whatever the runtime provides, and applies only when the project is under
  version control. Prescribing `git diff --check`, the scoped diff, and
  `git status --short` in one command put runtime specifics into a principles
  document and sent agents looking for Git in directories that have none. The
  concrete Git form moved to the README.
- `Advisory` and `Review` merged into one `Advise` mode; they differed in label
  only. Four modes remain: Advise, Explore, Develop, Harden.
- `Workflow inheritance` became `Precedence` and moved to the top, where the
  ordering it defines actually applies. Its first tier now names system and
  safety instructions explicitly, which the section header previously carried
  only in the intro paragraph.
- The integrity failures became their own top-level section instead of a tail
  of `Risk flags`. They are absolute, not risk-selected safeguards.
- The prompt-injection rule moved from `Locate proportionately` to
  `Version control and safety`, next to the other rules it belongs with.
- The frontmatter description now names triggering situations instead of
  values, and states what the skill is not needed for.
- Removed three internal duplicates: the prohibition on competing plans and
  logs stated three times, the precedence rule stated twice, and the
  test-only/refactor-only/documentation-only rule stated twice.

### Note

- `SKILL.md` grew from 1,866 to 1,953 words of rules. The deduplication and
  tighter phrasing did not offset the added examples and rules, and the README
  word count was corrected from its stale "roughly 1,700".

## 2026-07-22: Compaction-safe handoff record

### Changed

- The handoff record now carries the requested outcome's binding constraints
  and any unrecorded material decision that affects future work. This closes
  the loss of scope prohibitions across compaction and resolves the literal
  conflict between the four-field cap and the Material decisions clause.
- Restored the resume rule lost in the goal-first rewrite: a resuming agent
  treats the record as a snapshot, re-reads the applicable instructions,
  inspects current version-control state, and reconciles any mismatch before
  continuing.

## 2026-07-22: Code style follows the surrounding code

### Added

- Implementation rule: write code that reads like the surrounding code — match
  its naming, idioms, error handling, and comment and annotation density; name
  things for their behavior, not their history or novelty (e.g. no new_,
  improved_, or _v2 names); never restyle or reformat code the change does not
  otherwise touch.
- Comment rule: write a comment only for a constraint the code cannot express,
  never to narrate the change or address the reviewer.
- New tests follow the project's existing test style and harness.
- Speculative guards join the speculative-scaffolding list, covering
  defensive clutter the project does not practice.

### Changed

- Unrelated pre-existing findings are reported only when they could change the
  user's next action. This closes a report-padding loophole where listing
  trivial pre-existing smells could substitute for progress.

## 2026-07-21: Restore validation stop semantics

### Changed

- Limit an infrastructure failure to one different substitute check; if that
  cannot demonstrate the behavior, stop and report it as unverified instead of
  probing additional runners, environments, or dependency paths.
- Make decisive evidence terminal for the behavior unless a separate changed
  behavior, named risk, or higher-priority requirement remains unverified.
- Require one coherent final Git inspection after validation. A new validation
  and inspection round opens only when that inspection exposes a concrete
  defect that is then fixed.

## 2026-07-20: Goal-first rewrite

### Changed

- Rebuilt the skill around one governing principle: after safety and explicit
  constraints, optimize for the requested observable outcome. Correctness,
  structure, and validation constrain delivery; they are no longer substitute
  deliverables. This addresses the observed Goodhart failure where agents
  optimized for tests, plans, and defensible process instead of product
  progress.
- Replaced size classification (Trivial/Tiny/Standard) with five modes:
  Advisory, Review, Explore, Develop, and Harden. Structural and High risk
  flags remain independent, and touching a central file, public API, or
  existing test suite alone never escalates Develop to Harden.
- Made validation decision-relevant: checks continue only while additional
  evidence could plausibly change the implementation or completion decision.
- A failed check is now presumed substantive and caused by the change unless
  specific evidence shows it is pre-existing or environmental.
- Two consecutive failed attempts against the same failing check stop patching
  and require re-reading the owner contract and changing or narrowing the
  approach.
- Explore code kept beyond the experiment becomes Develop work and must meet
  Develop validation before completion is claimed.
- When the runtime requires its own plan while an authoritative project plan
  exists, the runtime plan is a disposable mirror; the project plan remains
  the only canonical state.
- Handoffs across interruption, handoff, or compaction record only four
  fields: requested outcome, current state, decisive evidence so far, and next
  concrete step.
- Material decisions form a boundary, not a gate: they are recorded in the
  project's existing plan, ADR, decision-log, commit, or pull-request
  mechanism, and ordinary implementation details are decided locally.

### Removed

- The automatic working-plan file (`PLAN.md` fallback) and the
  `docs/engineering-decisions.md` fallback log. Scoville no longer creates any
  artifact of its own.
- The SC1-SC10 numbering. The hard integrity failures survive as a named list
  (misleading wrappers, silent fallbacks, lossy projections, publication
  before durable work, duplicate owners); maintainability smells became
  review signals instead of automatic blockers.
- README benchmark results and the small-model validation claim: they measured
  the previous rule set and must be re-run against the goal-first version
  before any efficiency claim returns.

## 2026-07-18: Benchmark results in the README

### Added

- Benchmark section with the 45-run delivery comparison: paired median deltas
  against a native arm, the tested LOC-Bench instances, and a short protocol
  summary.
- The introduction states the measured token savings of roughly 25 to 30
  percent at identical task quality.

## 2026-07-18: Consistent and unambiguous vocabulary

### Changed

- One term per concept: the single proving check is now always the "decisive
  check" (previously also "decisive validation", "focused validation", and
  "primary decisive check"), the persisted plan artifact is always the
  "working-plan file" (previously also "working-state file"), Trivial and Tiny
  checks are both "focused checks", the owner is always the "canonical owner",
  and the current unit of work is the "active work item".
- Resolved the elliptical precedence sentence: overrides apply concern by
  concern, and they never override higher-priority instructions, safety,
  integrity, or truthful evidence.
- Removed an ambiguous pronoun chain from the subagent planning clause and
  spelled out the work-in-progress limit.
- README trigger-test wording follows the Trivial check rename.

### Note

- The `SKILL.md` hash changes again; pinned benchmark arms must re-pin. Re-run
  the small-model comprehension gate before relying on the README's validation
  claim for this wording.

## 2026-07-18: Runtime and user precedence at decision points

### Changed

- Planning resolves in order: user instructions, the planning mechanism the
  runtime provides in the current context, the project's designated mechanism,
  and only then the ephemeral fallback. The fallback never runs beside another
  active planning mechanism, and the working file exists only when the plan
  must survive compaction or handoff and no available mechanism already
  preserves it.
- Subagents that cannot reach their caller's planning mechanism plan
  ephemerally and return plan-relevant state in their result; persistence
  belongs to the caller.
- Workflow inheritance names runtime-supplied rules and invoked skills as an
  explicit tier between user instructions and repository conventions.
- Rereading an unchanged file is allowed when the runtime's editing tool
  requires its own read before an edit.
- Tiny work skips a written plan unless the user or runtime requires one.
- Creating `docs/engineering-decisions.md` defers to user or runtime approval
  requirements for new files.

### Note

- The `SKILL.md` hash changes with this release; pinned benchmark arms must
  re-pin their commit and hash.

## 2026-07-16: Validation-loop termination

### Changed

- Require a specifically named Structural or High flag before adding broader
  validation that is not already required by the repository or user.
- Make one passing decisive check terminal for its work item and proceed
  directly to one final diff and version-control status inspection.
- Make that final Git inspection operationally atomic: one command bundles
  `git diff --check`, the scoped diff, and `git status --short`; separate
  pre/post inspection commands are forbidden.
- Prohibit unchanged failed-command reruns, repeated confirmation checks, and
  additional similar tests after decisive evidence.
- Classify failed checks from their output. Infrastructure failures permit at
  most one different, narrower substitute check and remain explicitly
  unverified.
- Prevent missing dependencies or import failures from automatically escalating
  into builds, installations, code generation, or renewed repository
  exploration.

### Validation intent

- Preserve Scoville's owner, structure, safety, and evidence requirements while
  removing redundant validation and post-proof exploration.
- Treat token and runtime reductions as directional goals; correctness,
  required repository tests, and truthful residual-risk reporting remain hard
  gates.

## 2026-07-16: Bounded executable repository discovery

### Changed

- Treat runtime-supplied repository directives as already loaded and avoid
  rediscovering directive or conventional workflow files without concrete
  evidence that another exact directive applies.
- Use exact task paths directly, resolve logical owners with one targeted
  filename or symbol search, and expand discovery only when inspected evidence
  leaves a material owner, boundary, or validation question unresolved.
- Stop localization after source and its directly relevant test confirm the
  canonical owner. Do not verify an opened path with another filename search or
  reread it unchanged before editing.

### Validated

- Optimized the standalone skill with SkillOpt against executable Terra/medium
  engineering tasks. The selected frozen candidate passed development,
  validation, and held-out splits at 3/3 each.
- The original control passed the held-out behavior, canonical-owner,
  changed-file, and focused-test checks in all three cases, but reached 0/3 on
  the complete hard gate because it still performed unnecessary broad or
  post-owner exploration. The selected wording removed those failures without
  relaxing behavior, ownership, or validation requirements.
- Limited the claim to the fixed nine-case executable suite and one model/run
  configuration; it does not establish general latency, token, or product-value
  improvements.

## 2026-07-15: GPT-5.6 Luna / Low optimization and validation

### Validated

- Optimization-gated the standalone skill against GPT-5.6 Luna at low reasoning
  in an isolated Codex environment. The unchanged skill identified all required
  Scoville concerns in 10/10 single-concern cases and 10/10 compound cases with
  two or three interacting concerns.
- Kept the production-proven skill rules unchanged because the complete Luna
  test suites passed without requiring model-specific wording or branches.
- Documented the evidence boundary: these suites test pre-edit instruction
  comprehension, not executable patch quality on real repositories.

## 2026-07-13: Adaptive, risk-proportionate workflow

### Changed

- Made Scoville inherit user and repository workflows concern by concern, with
  compact fallback rules only where the project is silent.
- Separated change size from structural and high-risk classification so small
  edits stay lightweight without weakening safety, ownership, boundary,
  atomicity, or validation requirements.
- Reframed execution around behavior-complete work items, real stop conditions,
  focused evidence, final-diff review, and explicit residual risk.
- Aligned the README with the current engineering gate and replaced the
  agent-specific manual installation matrix with one agent-install prompt plus
  a short manual fallback.
- Simplified the skill with an agent-neutral trigger, direct wording, concrete
  SC1-SC5 examples, clearer gate timing, and project-owned decision records
  while retaining the full safety and risk gates.
- Added a user-overridable working-plan fallback for likely compaction or
  handoff and one shared decision-and-rationale record when projects provide no
  mechanism.
- Defined a distinct fallback file when `PLAN.md` belongs to unrelated work and
  restored append-only supersession for semantic decision history.
- Reworked the README with concrete failure examples, installation verification,
  context-cost guidance, an accurate repository inventory, and the MIT license
  link.
- Refined the README prose, replaced em-dash punctuation, and corrected the
  classification, context-cost, and fallback-record details.

**Commits:** [`596b76b`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/596b76bfa3856dfe226b5b8d5bb61e0f84c86ca4),
[`7706e9d`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/7706e9d6d854dbd59c3ed11a4f59015db4ddd6eb),
[`01b4269`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/01b42691c7e743ea685b00af293d2f0970d472e0),
[`551f790`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/551f7900577644422dcb65e9ef038d3426769113),
[`c4a96ad`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/c4a96adcfea83c949ba71b9a7c8f18894cc279d2),
[`8818ce8`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/8818ce806caed79bb84a723ea3c0b901ecbbe727),
[`53c1c26`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/53c1c265c49c2d5bbdd28cb8a43603129e969fe9)

## 2026-07-10: Structural execution and review gate

### Changed

- Renamed the Codex-facing UI entry to **Scoville Engineering Gate** and updated
  its prompt to emphasize canonical ownership, structural checks, and real
  validation evidence.
- Expanded the skill from a code-change loop into explicit Change, Review,
  Advisory, and Non-engineering modes for engineering artifacts as well as code.
- Established the `SC1`-`SC10` structural failure model, covering misleading
  wrappers, silent fallbacks, lossy boundaries, state-before-durable ordering,
  duplicate pathways, responsibility growth, speculative abstraction, mode
  creep, implementation-mirroring tests, and incomplete scaffolding.
- Added explicit owner, boundary, atomicity, dependency, failure-proof,
  completion, and residual-risk gates.

**Commits:** [`98251ac`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/98251ac576ef7a7da3c49e7342ec641bcade0f4c),
[`2c465cf`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/2c465cf06f3926c7406bd2cee71e4dd61487421c)

## 2026-07-08: Leaner structural workflow

### Changed

- Condensed the expanded quality gate into a smaller eight-step workflow while
  preserving owner-first changes, structural review, real validation output,
  anti-oscillation behavior, and reportable risk.
- Clarified that engineering artifacts with behavioral or contract impact use
  the same gate, while pure questions apply only the relevant safety rules.

**Commit:** [`fc0730f`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/fc0730f6d26cefab2d514d6ef652e991545bfd86)

## 2026-07-07: Structural quality beyond green tests

### Added

- Introduced explicit structural failure modes and pre- and post-edit structure
  review for code-judo opportunities, file-size signals, atomicity, lossy
  boundaries, misleading wrappers, and failure-mode tests.
- Added holistic branch-diff review and stronger completion checks so passing
  tests alone could not approve structurally harmful changes.

### Documentation

- Expanded the README to explain Scoville's structural-quality focus.

**Commits:** [`703f97b`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/703f97bfdce236d5e96c8066d5df0d3ca8b43608),
[`f71d38d`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/f71d38d28c75a87ff919745cf9e723f2f09f482c)

## 2026-07-03: Execution-focused quality gate

### Changed

- Reworked the original checklist into an execution-first workflow with task
  classification, planning, source-of-truth discovery, milestone progress,
  evidence-backed validation, handoff context, and anti-oscillation rules.
- Iterated that workflow into a fixed classify, plan, locate owner, edit,
  validate, self-check, and report loop with concrete banned patterns.
- Strengthened edit and validation rules with read-before-edit, conflict
  detection, surgical changes, dependency approval, fail-first defect proof,
  narrow-to-broad checks, and repository-owned version-control policy.

**Commits:** [`4f2028e`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/4f2028ec5fc4759d7cb6644e301992aa3aed5dc9),
[`24148db`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/24148dbdf2e4bc8e311436d256853427fc7f7478),
[`ddb8d91`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/ddb8d91d2b645ea784a1346e89df56be95bfccbf)

## 2026-07-01: Repository metadata correction

### Fixed

- Corrected the copyright holder name in the MIT license.

**Commit:** [`702ede7`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/702ede704e0fe7b899fe007d43680968c85332b0)

## 2026-06-29: Initial skill

### Added

- Published the first README and anti-AI-slop quality-gate definition.
- Added the MIT license and Codex UI metadata.
- Added the Scoville tagline, installation guidance for compatible agents, and
  a curated source and inspiration list.

**Commits:** [`d8d9a1c`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/d8d9a1cd6e85ca8cd9b484061125cf193052744c),
[`2915ef7`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/2915ef7eb0418041d856820ab4ef3cfc523223f6),
[`1583888`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/1583888119028d58e78e233bef68c198a6148748),
[`2045e8c`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/2045e8c7700768ad82ca1ace08598c2b713965da),
[`b1614b6`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/b1614b65076186e107ea571c1fc713aa67310a28),
[`750630b`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/750630b5abc05278590910f8a1ec98e281d78c2a),
[`c133db9`](https://github.com/benjaminstelzer/scoville-anti-ai-coding-slop/commit/c133db9f8d9b5dcfbfb6fb53b79bff02fea15a54)
