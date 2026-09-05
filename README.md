# Scoville Code Anti-AI-Slop

The result is the point. The process earns its place by making that result
safer, clearer, or easier to verify.

It usually looks harmless:

- The agent reports "All tests pass." No tests ran. The suite has passed as
  prose.
- A failing test is declared "pre-existing" after one glance at its name. No
  baseline, comparison, or other evidence appears.
- Lint and typecheck pass, so the changed behavior is reported as verified. The
  behavior itself was not consulted.
- A failing assertion or safety guard is weakened until CI turns green.
  Consensus has been reached. Correctness was not invited.

That is coding slop: evidence is narrated instead of observed. The report says
fixed. The behavior remains unknown, or the check that caught the bug no longer
does.

Scoville Code is a goal-first Agent Skill for planning, changing, testing,
reviewing, and removing code or engineering artifacts. It keeps canonical
ownership, scope, risk boundaries, validation, and honest evidence visible. It
can answer or diagnose without editing, and it does not turn every rename into
a release rehearsal merely because a checklist was feeling ambitious.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution. In coding, the
heat is the requested behavior after plans, wrappers, tests, and confident
status prose have all tried to become the feature.

## How to use

Name Scoville Code for codebase work where scope, ownership, risk, or evidence
matters:

```text
Use Scoville Code to implement rate limiting in the existing API owner. Keep the diff scoped, preserve public behavior outside the stated limit, and run the repository's relevant checks.
```

```text
Use Scoville Code to diagnose why this migration sometimes leaves consumers on the old schema. Identify the supported root cause and evidence. Do not change files.
```

```text
Use Scoville Code to review this patch for correctness, hidden failure paths, ownership drift, and missing validation. Report prioritized findings only.
```

Explicit `$scoville-code-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/tree/main/scoville-code-anti-ai-slop
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

```text
Install the complete Scoville Skill suite for all my projects. Fetch and install every exact package directory below:

https://github.com/benjaminstelzer/scoville-brainstorm/tree/main/scoville-brainstorm
https://github.com/benjaminstelzer/scoville-research/tree/main/scoville-research
https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/tree/main/scoville-code-anti-ai-slop
https://github.com/benjaminstelzer/scoville-design-anti-ai-slop/tree/main/scoville-design-anti-ai-slop
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
https://github.com/benjaminstelzer/scoville-plan/tree/main/scoville-plan
https://github.com/benjaminstelzer/scoville-handoff/tree/main/scoville-handoff

Preserve existing customizations and ask before overwriting conflicting files. Report every installed location and whether the host discovers each Skill.
```

## What it enforces

- **Outcome over ceremony.** Plans, tests, docs, and refactors support the
  requested behavior. Producing them is not completion by itself.
- **Canonical ownership.** The change fits the project's existing architecture,
  records, terminology, and workflow instead of creating a second owner.
- **Proportionate risk.** Small reversible work stays small. Destructive,
  public-facing, security, data, or release work receives stronger gates.
- **Evidence before claims.** Checks prove only what they observed. A failed
  tool is not silently promoted to a passing product.
- **Root-cause correction.** The agent changes approach after repeated failure
  instead of applying patch number three with renewed optimism.
- **Navigable code structure.** Hand-written source files use a default ceiling
  of 2,000 physical lines with project priority and concrete exceptions. Domain
  ownership, module boundaries, dependency direction, generated sources, and
  resource cleanup remain explicit without forcing one architecture.
- **Material questions only.** It asks when a missing choice changes behavior,
  authority, cost, reversibility, or scope, not for details the code settles.
- **Complete handoff.** The final report names changed behavior, relevant
  validation, unresolved failures, and repository state without pretending.

The complete contract is in
[SKILL.md](scoville-code-anti-ai-slop/SKILL.md).

## How it works

The Core selects an internal mode from Advise, Explore, Develop, or Harden, then
loads only the planning, change-workflow, or validation guidance the operation
needs. Project instructions and established owners outrank Skill defaults. The
Skill creates no private plan or decision log and installs no executable
software. The repository remains the source of truth, which saves everyone
from auditing the audit trail's audit trail.

For repository structure and development tools, see
[maintenance notes](docs/maintenance.md).

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores
  materially different mechanisms before selection.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web,
  GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns
  engineering scope, implementation, risk, and validation.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns
  visual definition, art direction, design systems, critique, and repair.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns
  framework-aligned implementation, interface mechanics, accessibility, and
  rendered evidence, with a standalone design fallback.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns
  wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans,
  Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active
  work to another agent or session.

## Status

The maintainability candidate and v1.0.17 control each passed 8/8 open Train
cases and 3/4 open Validation cases in three runs. Every failure concerned the
same narrow security fix. A conservative SkillOpt proposal also scored 3/4 and
was rejected. The four-case Holdout remains sealed.

Earlier 30/30 results belong to the historically qualified Code package.
Neither those scores nor instruction-size comparisons qualify the current
maintainability extension. See [benchmark evidence](docs/benchmark-evidence.md)
for the candidates, failures, and retained history.

## Sources

- [OpenAI coding-agent best practices](https://developers.openai.com/codex/learn/best-practices)
  for explicit outcomes, constraints, permissions, and focused verification.
- [Cursor Thermo-Nuclear Code Quality Review](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md)
  for ownership, simplification, and complete-change review.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
  for prompt injection, unsafe output, information disclosure, and excessive
  agency.
- Martin Fowler on [internal quality](https://martinfowler.com/articles/is-quality-worth-cost.html)
  and [technical debt](https://martinfowler.com/bliki/TechnicalDebt.html).
- Simon Willison on
  [vibe coding versus reviewed AI-assisted engineering](https://simonwillison.net/2025/Mar/19/vibe-coding/).
- [Google Engineering Practices](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
  for design, complexity, tests, naming, consistency, and review context.
- [DORA code maintainability](https://dora.dev/capabilities/code-maintainability/)
  for source discoverability, dependency traceability, and reproducible builds.
- Configurable file-size checks in [ESLint](https://eslint.org/docs/latest/rules/max-lines)
  and [Checkstyle](https://checkstyle.org/checks/sizes/filelength.html), whose
  different defaults are not treated as one universal standard.

## License

MIT. See [LICENSE](LICENSE).
