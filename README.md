# Scoville Code

A coding agent can finish the wrong thing quite thoroughly. The tests are green,
the report sounds certain, but the behavior you asked for is still missing.

Scoville Code is the engineering foundation of the suite. It connects the
requested result, the existing implementation and the evidence that the change
works. The agent must understand the cause and respect the project's architecture,
not simply produce a plausible patch. Use it to develop, diagnose, review or
remove code without turning every small change into a full audit.

## How it works

- Establish the observable outcome, responsible code, introduced risks and cheapest decisive check before substantial editing.
- Read the owner and relevant callers, contracts and tests. Expand only when the evidence points elsewhere.
- Fix the cause in the existing implementation. Avoid parallel paths, speculative abstractions and unrelated cleanup.
- Test the changed behavior. A successful build or mocked integration proves only what it exercised.
- Investigate failed checks without weakening required guarantees. Change obsolete assertions only when an explicitly authorized contract change requires it. After two unsuccessful corrections of the same cause, reassess the approach.
- Inspect the complete change and report observed results and remaining gaps. Stop checking when further evidence would not change the decision.

## What it enforces

- **Outcome over ceremony.** Plans, tests, docs, and refactors support the
  requested behavior. Producing them is not completion by itself.
- **Canonical ownership.** The change fits the project's existing architecture,
  records, terminology, and workflow instead of creating a second owner.
- **Proportionate risk.** Small reversible work stays small. Checks follow
  concrete failure risks. Broader security, migration or release gates apply
  when the requested outcome or project rules require them.
- **Evidence before claims.** Checks prove only what they observed. A failed
  tool is not silently promoted to a passing product.
- **Root-cause correction.** The agent changes approach after repeated failure
  instead of repeating the same unsuccessful fix.
- **Navigable code structure.** Existing work follows project conventions and
  surrounding module boundaries. Greenfield work starts with the smallest
  coherent responsibility-based layout. A 2,000-line default ceiling remains
  a backstop with concrete exceptions, never an architecture target.
- **Material questions only.** It asks when a missing choice changes behavior,
  authority, cost, reversibility, or scope, not for details the code settles.
- **Defaults for a wholly new project.** Project instructions come first.
  Only complete greenfield work uses the stack-specific conventions in the
  Skill's `references/project-conventions.md`. Keep personal overrides outside
  the installed Skill and reference them explicitly from `AGENTS.md` so Skill
  updates do not replace them. Existing projects keep their organization.
  The [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions)
  explains paths, precedence and update behavior with a copyable example.
- **Complete handoff.** The final report names changed behavior, relevant
  validation, unresolved failures, and relevant repository state.

- The complete contract is in [SKILL.md](https://github.com/benjaminstelzer/scoville-code/blob/main/scoville-code/SKILL.md).

## What it costs

- Source inspection and checks use more tokens and time than an immediate patch.

## How it was developed

- Developed through real engineering tasks and analysis of their complete histories.
- Turned wrong-cause fixes, missed outcomes and repeated checks into instruction changes and regression cases.
- Combined targeted simulations with optimization workflows, including SkillOpt.
- Retained shorter instructions only when required behavior survived the tests.

## Compatibility

Use a frontier LLM from the Fable, Astra, SOL or Opus families, version 5.0 or
newer. This is the minimum model requirement, not a claim that every model in
those families has been tested.

The host must read the Skill's references and run the project's own build, test
and check commands in a shell. Version control is optional. The Skill bundles
no scripts and requires no network access. It was developed for Codex and
Claude Code. Other hosts are untested.

This Skill works on its own. Other Scoville Skills are optional and handle
only their own concerns when available and applicable.

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

Project instructions come first. Scoville Code uses its organization fallback
only when you start a wholly new project, and only for choices your instructions
have not already settled. Adding a module to an existing project is not a fresh
start. Neither is a refactor or a missing naming rule.

The defaults live in
[`references/project-conventions.md`](scoville-code/references/project-conventions.md)
inside the installed Skill. They follow the selected language and framework:
Python modules, Angular components and PSR-4 classes have different naming
rules for a reason. Where the ecosystem leaves the choice open, the fallback
uses a small `src/`, `tests/`, `docs/` and `scripts/` layout. Directories appear
when they have a purpose, not as an empty scaffold. Tests can live beside the
code when the framework expects that.

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

Create the referenced file with your actual preferences. Relative paths resolve
from the directory containing the referring `AGENTS.md`. A shared personal file
can instead use an explicit absolute path available on that machine. The Skill
does not search your computer for convention files. If the required file cannot
be read, the agent reports that input gap before making dependent choices.

Your file is maintained separately from the installed Skill, so replacing the
Skill does not replace it. Project-specific instructions still take precedence
over generic personal defaults unless you explicitly choose otherwise. Required
framework paths and loading rules remain binding. Naming preferences do not
grant new permissions or extend the fallback to existing projects.

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
