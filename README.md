# Scoville Code Anti-AI-Slop

A coding agent can finish the wrong thing quite thoroughly. The tests are green,
the report sounds certain, but the behavior you asked for is still missing.

Scoville Code keeps the requested outcome at the centre of engineering work.
It asks the agent to find the code that owns the problem, make a proportionate
change and check the behavior affected by it. A failing check needs a cause.
Calling it pre-existing, or weakening the assertion until it passes, does not
resolve it.

Use it for implementation, diagnosis, review and removal of code or engineering
artifacts. It can investigate without editing. Small changes should stay small,
while migrations, security boundaries and irreversible work need closer checks.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution.
In Code, that means keeping the requested behavior in view as the task grows in detail.

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

## Compatibility

Any Agent Skills host that can read references/ and run the project's own build, test and check commands in a shell. Version control optional. No bundled scripts, no network access required. Developed for Codex and Claude Code; other hosts untested.

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

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

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
  instead of repeating the same unsuccessful fix.
- **Navigable code structure.** Hand-written source files use a default ceiling
  of 2,000 physical lines with project priority and concrete exceptions. Domain
  ownership, module boundaries, dependency direction, generated sources, and
  resource cleanup remain explicit without forcing one architecture.
- **Material questions only.** It asks when a missing choice changes behavior,
  authority, cost, reversibility, or scope, not for details the code settles.
- **Complete handoff.** The final report names changed behavior, relevant
  validation, unresolved failures, and relevant repository state.

The complete contract is in
[SKILL.md](scoville-code-anti-ai-slop/SKILL.md).

## How it works

The Core selects an internal mode from Advise, Explore, Develop, or Harden, then
loads only the planning, change-workflow, or validation guidance the operation
needs. Project instructions and established owners outrank Skill defaults. The
Skill creates no private plan or decision log and installs no executable
software. The repository remains the source of truth.

## How it was developed

Code has grown through real engineering work. I read complete task histories
to find where an agent loses the requested outcome, works around the wrong
cause or keeps checking something it has already established. Repeated searches
and oversized tool output matter for the same reason: they consume context
without necessarily helping to fix the problem.

Those observations become instruction changes and regression cases. I also use
SkillOpt to explore shorter instructions. The
[development history](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/blob/b3509d8e6fc5f485e1b3274b600de7f717aea396/CHANGELOG.md)
includes an adopted compression and a later proposal I rejected because it
still missed a required concern. Shorter is useful when the required behavior
survives.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores materially different mechanisms before selection.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web, GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns engineering scope, implementation, risk, and validation.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns visual definition, art direction, design systems, critique, and repair.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns framework-aligned implementation, interface mechanics, accessibility, and rendered evidence, with a standalone design fallback.
- [WordPress UI Backend](https://github.com/benjaminstelzer/scoville-wordpress-ui-backend-anti-ai-slop) owns plugin-owned WordPress admin interfaces, platform components, spacing, accessibility and internationalization.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans, Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active work to another agent or session.
- [Workflow Codex](https://github.com/benjaminstelzer/scoville-suite) coordinates explicit Plan execution through native Codex project tasks.

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

