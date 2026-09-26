# Scoville Code

A coding agent can produce passing tests while missing the behavior you asked
for. Scoville Code connects the requested result, the existing implementation
and the evidence that a change works.

Use it to develop, diagnose, review or remove code. It directs the agent to find
the cause, respect the project's architecture and check the affected behavior
with effort proportionate to the task.

## How it works

- Identify the outcome, responsible code, risks and decisive check before editing.
- Read relevant code, callers and tests. Expand the investigation when evidence requires it.
- Fix the cause within the existing architecture and requested scope.
- Check the changed behavior and report what the evidence actually proves.
- Investigate failures without weakening guarantees. Revise obsolete assertions only for an authorized contract change. Reassess after two failed corrections of the same cause.
- Inspect the complete change, report remaining gaps and stop checking when further evidence would not change the decision.

## What it enforces

- **The requested result.** Plans, tests and refactors support the outcome;
  completion requires the behavior itself.
- **Existing ownership.** Changes follow the project's architecture, records,
  terminology and workflow.
- **Proportionate checks.** Verification addresses concrete failure risks.
  Broader security, migration or release checks follow the task and project rules.
- **Supported claims.** Reports distinguish observed results, failed checks
  and unverified behavior.
- **Root-cause correction.** Repeated failure triggers a reassessment of the approach.
- **Navigable code.** Existing conventions and module boundaries guide changes.
  New projects start with a small layout organized by responsibility. The
  2,000-line default ceiling permits justified exceptions.
- **Necessary questions.** Ask when a choice changes behavior, authority, cost,
  reversibility or scope. Resolve ordinary details from the project.
- **Your conventions.** Project instructions take priority. Defaults apply only
  to a wholly new project. Keep personal conventions outside the installed
  Skill and reference them from `AGENTS.md` to preserve them across updates.
  See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions).
- **Useful completion reports.** State changed behavior, validation, unresolved
  failures and relevant repository state.

The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-code/blob/main/scoville-code/SKILL.md).

## What it costs

- Source inspection and checks use more tokens and time than an immediate patch.

## How it was developed

- Real engineering tasks and their histories supplied cases involving wrong-cause fixes, missed outcomes and repeated checks.
- Targeted simulations and SkillOpt informed instruction revisions, with tests checking that required behavior survived.

## Compatibility

Use a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0 or
newer. This is the minimum model requirement, not a claim that every model in
those families has been tested.

The host must read the Skill's references and run the project's own build, test
and check commands in a shell. Version control is optional. The Skill bundles
no scripts and requires no network access. It was developed for Codex and
Claude Code. Other hosts are untested.

This Skill works independently. Other Scoville Skills are optional.

## Install

### Install this Skill

This standalone package works independently. Ask your compatible agent host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-code/tree/main/scoville-code
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```

The host needs permission to write to its Skills directory. See the
[Codex Skills guide](https://learn.chatgpt.com/docs/build-skills) or the
[Claude Code Skills guide](https://code.claude.com/docs/en/skills)
for host-specific locations.

### Install the complete Scoville suite

Get the complete suite from the
[Scoville Suite monorepo](https://github.com/benjaminstelzer/scoville-suite).
Install its released Skill packages, not development templates.

## How to use

```text
Use Scoville Code to analyze this codebase for correctness, ownership and missing validation. Report prioritized findings.
```

```text
Analyze this codebase for defects and hidden failure paths. Support findings with code evidence and keep the analysis read-only.
```

### Starting a new project

For a wholly new project, Scoville Code uses
[`references/project-conventions.md`](scoville-code/references/project-conventions.md)
for choices the project instructions leave open. Its defaults follow the
language and framework, with a small `src/`, `tests/`, `docs/` and `scripts/`
layout where appropriate. Directories are added when needed; tests may sit
beside code when the framework expects it. Existing projects retain their
organization, including during refactors or module additions.

### Your own conventions

You can edit the bundled reference, but a Skill update can replace that edit.
For conventions you want to keep across updates, maintain a Markdown file
outside the Skill installation and explicitly reference it in your global or
project `AGENTS.md`. For example, with an `AGENTS.md` at the project root:

```markdown
### Greenfield project conventions

For the initial organization of a wholly new project, first follow this
project's explicit requirements, then read `docs/project-conventions.md`
for my additional folder and filename conventions. Use Scoville Code's
defaults only for choices neither source settles. Do not apply this
fallback to additions or refactors in an existing project.
```

Create the file with your conventions. Relative paths resolve from the
referring `AGENTS.md`; a shared personal file can use an absolute path.
The agent reads the explicitly referenced file and reports it if unavailable.

Keeping conventions outside the installed Skill preserves them across updates.
Project-specific instructions and framework requirements still apply.

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

- [Code](https://github.com/benjaminstelzer/scoville-code) owns engineering scope, implementation, risk, and validation.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans, Work Items, Decisions, and lifecycle state.
- [UI](https://github.com/benjaminstelzer/scoville-ui) owns UI implementation, information structure, accessibility and rendered evidence, with a conditional WordPress adapter.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active work to another agent or session.

## License

MIT. See [LICENSE](LICENSE).
