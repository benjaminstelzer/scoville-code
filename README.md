# Scoville Code

Passing tests are useful. Passing tests for the wrong behavior, rather less so.
Scoville Code keeps implementation, debugging and review tied to the result you
asked for: find the cause, work with the existing architecture and check what
actually changed.

Scoville measures chili heat. Code aims for sharper reasoning before a small
fix acquires its own framework.

## How it works

- Establish the requested result and find the code responsible for it.
- Fix the cause within the project's architecture and your authorized scope.
- Check the affected behavior and relevant performance costs.
- Reassess failed fixes, report remaining limits and stop when further checks
  would no longer change the decision.

## What it enforces

- **Work that serves the request.** Refactors, safeguards and tests need a
  concrete purpose. The agent asks about material choices and settles routine
  details from the project.
- **Your conventions.** Existing architecture and project rules take precedence.
  New projects start with a small structure organized by responsibility.
- **Evidence that fits the change.** Check the behavior, preserve guarantees and
  distinguish observed results from what remains unverified.

Keep personal conventions outside the installed Skill so updates preserve them.
See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions)
and [full instructions](https://github.com/benjaminstelzer/scoville-code/blob/main/scoville-code/SKILL.md).

## What it costs

- Reading relevant code and checking behavior takes tokens and time. The extra work is aimed at avoiding fixes that merely look finished.

## How it was developed

The cases come from real engineering tasks: wrong-cause fixes, missed outcomes
and checks repeated without new information. They shaped the focus on useful
evidence. Selected comparisons do not establish a general performance gain.

## Compatibility

Developed for Codex and Claude Code with reference access and a shell for the project's own checks. Fable, Astra, SOL or Opus (5.0+) are recommended. Luna 6 with High reasoning has passing results in selected practical Code tasks in Codex, but some practical checks and one abstract instruction-recall check did not pass. These checks do not establish reliable use across Code tasks or on other model routes or hosts.

## Install

This Skill works independently. Other Scoville Skills are optional.

### Install this Skill

Ask your agent host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-code/tree/main/scoville-code
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```

The host needs permission to write to its Skills directory. The
[Codex Skills guide](https://learn.chatgpt.com/docs/build-skills) and the
[Claude Code Skills guide](https://code.claude.com/docs/en/skills)
list the locations for each host.

### Install the complete Scoville suite

The complete suite is in the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

## Configuration

### Your own conventions

You can edit the bundled [conventions](scoville-code/references/project-conventions.md),
but the next Skill update may overwrite them. To keep your conventions:

1. Create a Markdown file outside the Skill installation.
2. Reference it explicitly from your global or project
`AGENTS.md` (Codex) or `CLAUDE.md` (Claude Code). For example, add this to
the file at the project root:

```markdown
### Greenfield project conventions

For the initial organization of a wholly new project, first follow this
project's explicit requirements, then read `docs/project-conventions.md`
for my additional folder and filename conventions. Use Scoville Code's
defaults only for choices neither source settles. Do not apply this
fallback to additions or refactors in an existing project.
```

3. Resolve relative paths from the referencing `AGENTS.md` or `CLAUDE.md`.
   A personal file shared across projects can use an absolute path.

The agent reads the referenced file and tells you if it can't find it.

Project-specific instructions and framework requirements still apply.

## How to use

```text
Use Scoville Code to analyze this codebase for correctness, ownership and missing validation. Report prioritized findings.
```

```text
Use Scoville Code to fix the failing checkout total when a coupon and free shipping combine. Find the cause, change the responsible code and verify the corrected case.
```

```text
Use Scoville Code to add CSV export to the orders page. Follow the existing structure and verify the exported fields and values against a representative local test order.
```

### Starting a new project

In a brand-new project, Scoville Code falls back on
[`references/project-conventions.md`](scoville-code/references/project-conventions.md)
for anything the project instructions leave open. Those defaults follow the
language and framework, with a small `src/`, `tests/`, `docs/` and `scripts/`
layout where it fits. Directories are only added when they're needed, and
tests can sit next to the code if the framework expects that. Existing
projects keep their organization, even during refactors or when modules are
added.

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

## Family

- [Code](https://github.com/benjaminstelzer/scoville-code) covers engineering scope, implementation, risk and validation.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) keeps Plans, Work Items, Decisions and their status in the repository.
- [UI](https://github.com/benjaminstelzer/scoville-ui) covers UI implementation, information structure, accessibility and rendered checks, with an optional WordPress adapter.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) passes active work to another agent or session.
- [Project Context Cleanup](https://github.com/benjaminstelzer/scoville-suite) keeps requested project rules and index text concise without losing required context.

## License

MIT. See [LICENSE](LICENSE).
