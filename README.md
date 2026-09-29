# Scoville Code

A coding agent can produce passing tests while missing the behavior you asked
for. Scoville Code connects the requested result, the existing implementation
and the evidence that a change works.

Use it to write, debug, review or remove code. It has the agent find the
actual cause, work within the project's architecture and check the affected
behavior, with as much effort as the task deserves.

The heat, in this case, is the behavior you asked for and the evidence that it
works. Scoville Code keeps both clear through implementation and testing.

## How it works

- Before editing, pin down the outcome, the responsible code, the risks and
  the check that will settle whether it works.
- Read the relevant code, its callers and tests. Look further when the
  evidence calls for it.
- Fix the cause, within the existing architecture and the scope you asked for.
- Check runtime and memory costs before and after the change. Prefer simpler
  algorithms and avoiding repeated work. Use suitable existing caches correctly
  and explain the tradeoff before asking you to approve a new one.
- Check the changed behavior and report what the evidence actually proves.
- When something fails, investigate it without weakening guarantees. Change
  an outdated assertion only when a change to the expected behavior has been
  approved. After two failed fixes for the same cause, step back and reassess.
- Look at the complete change, report what's still open, and stop checking
  once more evidence wouldn't change the decision.

## What it enforces

- **The requested result.** Plans, tests and refactors serve the outcome. The
  task is only done when the behavior itself works.
- **Project conventions.** Changes follow the project's architecture, records,
  terminology and workflow.
- **Proportionate checks.** Checks target concrete ways things could fail.
  Broader security, migration or release checks happen when the task or the
  project's rules call for them.
- **Supported claims.** Reports keep observed results, failed checks and
  unverified behavior apart.
- **Root-cause correction.** If fixes keep failing, the approach gets
  reassessed.
- **Navigable code.** Changes follow existing conventions and module
  boundaries. New projects start with a small layout organized by
  responsibility. Source files are limited to 2,000 lines by default, with
  room for justified exceptions.
- **Necessary questions.** The agent asks when a choice affects behavior,
  authority, cost, reversibility or scope. Ordinary details it settles from
  the project itself.
- **Your conventions.** Project instructions come first. The defaults only
  apply to a brand-new project. To keep your own conventions across updates,
  store them outside the installed Skill and reference them from `AGENTS.md`
  (Codex) or `CLAUDE.md` (Claude Code).
  See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions).
- **Useful completion reports.** The final report states what behavior
  changed, how it was checked, which failures remain and the relevant
  repository state.

The full instructions are in [SKILL.md](https://github.com/benjaminstelzer/scoville-code/blob/main/scoville-code/SKILL.md).

## What it costs

- Reading the code and running checks costs more tokens and time than
  patching right away.

## How it was developed

- The cases come from real engineering tasks and their histories: fixes aimed
  at the wrong cause, missed outcomes and checks that ran again and again.
- Targeted simulations and SkillOpt fed into the revisions of the
  instructions, and tests made sure the required behavior survived them.

## Compatibility

Use a frontier model from the Fable, Astra, SOL or Opus families, version 5.0
or newer. Luna was also used in testing.

The host has to be able to read the Skill's references and run the project's
own build, test and check commands in a shell. Version control is optional,
and the Skill ships no scripts. It was developed for Codex and Claude Code.
Other hosts haven't been tested.

It works on its own. The other Scoville Skills are optional.

This Skill works independently. Other Scoville Skills are optional.

## Install

### Install this Skill

This package works on its own. Ask your agent host:

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

### Your own conventions

You can edit the bundled reference, but the next Skill update may overwrite
it. For conventions you want to keep, maintain a Markdown file outside the
Skill installation and reference it explicitly from your global or project
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

Then create the file with your conventions. Relative paths are resolved from
the `AGENTS.md` or `CLAUDE.md` that references them, and a personal file
shared across projects can use an absolute path. The agent reads the
referenced file and tells you if it can't find it.

Project-specific instructions and framework requirements still apply.

The name comes from the Scoville scale, which originally measured chili heat through dilution.

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

## License

MIT. See [LICENSE](LICENSE).
