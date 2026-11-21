# Scoville Code

Passing tests are useful. Passing tests for the wrong behavior, rather less so.
Scoville Code keeps implementation, debugging and review tied to the result you
asked for: find the cause, work with the existing architecture and check what
actually changed.

Scoville measures chili heat. Code aims for sharper reasoning before a small
fix acquires its own framework.

## How it works

- Before writing, the agent looks for what the project already has: the
  function that does the job, the module it belongs in and the way the project
  builds that kind of thing.
- It starts from the simplest approach that solves the request and holds its
  code to it.
- While writing, it keeps one path, uses other modules through their public
  interfaces, keeps each fact in one place and reads its own loops for work
  that repeats per item. That is a reading check, not a benchmark.
- It names the test that proves the request and reports it by name. For a
  bug fix, or new behavior whose failure would charge a wrong amount, grant
  access, lose data or open a security hole, it sees that test fail first. A refactoring keeps the existing tests green
  before and after; a change without runtime behavior gets the fitting source
  or build check, not a test.
- It ends by reading its diff against these rules and reports the test that
  proves the request.
- Where the host can start a separate agent, a change to code behavior is
  then read once by an agent that has not seen the author's reasoning. The
  author declines findings that only ask for more protection. Under a
  workflow that already reviews each change independently, that review takes
  its place.
- A review goes through the same points in someone else's change and names
  the place, the problem and, where one exists, the function, path or
  interface to use instead.

## What it enforces

- **Code the next reader can extend.** No second implementation of logic the
  project already has, no parallel path beside the one that works, no reaching
  into another module's internals and nothing left behind.
- **Effort in proportion.** A safeguard, an abstraction or a test needs a real
  case in this application. A local script is not hardened like a payment
  service, and a small request stays a small diff.
- **Tests that prove something.** The test checks the requested result and
  actually runs; for a bug fix or costly behavior it is seen failing first. "All tests pass" does not count when the relevant test was
  not among them.
- **Your conventions.** Existing architecture and project rules take precedence.
  New projects start with a small structure organized by responsibility.
- **Honest evidence.** The report keeps what was observed apart from what
  remains unverified. The agent asks about material choices and explains
  conflicting requirements instead of substituting a different result.

Keep personal conventions outside the installed Skill so updates preserve them.
See the [customization guide](https://github.com/benjaminstelzer/scoville-code#your-own-conventions)
and [full instructions](https://github.com/benjaminstelzer/scoville-code/blob/main/scoville-code/SKILL.md).

## What it costs

- Reading relevant code and checking behavior takes tokens and time. The extra work is aimed at avoiding fixes that merely look finished.
- The independent reading of a change to code behavior adds one agent run. In my measurements a review took two to four minutes.

## How it was developed

Code grew from engineering work in large, evolving projects. Early versions
could turn a small change into a ritual: extra safeguards, repeated checks and
elaborate proof that added little to the result. The useful shift was toward
the actual problem, a maintainable solution and tests that protect real behavior.

Ideas are tried in focused tests, then checked against complete workflows in
real projects. Missed requirements, unnecessary complexity and wasted work feed
into the next revision. The revised rules go through the same cycle again.

### What the tests showed

Two tests, each with the Skill against no Skill: a review of 18 real changes
that each hold a defect fixed later, and a new web application built from
five consecutive requests. The state of November 2026:

**Claude Opus 5.5, medium reasoning effort**

| Test | Measure | With the Skill | Without |
| --- | --- | --- | --- |
| Review | Defects found (of 18) | **16**\* | 10 |
| Review | Misplaced module boundaries found (of 3) | **3**\* | 0 |
| Review | Time per review | **143 s**\* | 145 s |
| New application | Hidden acceptance checks | all passed | all passed |
| New application | Versions with quadratic work | **none** | 1 of 2 |
| New application | Mechanisms nobody asked for | **2 to 4**\* | 14 to 18 |
| New application | Places with repeated work | **0 to 2**\* | 2 to 9 |
| New application | Hidden errors | **0 to 1**\* | 4 to 6 |

**gpt-6.2-sol, medium reasoning effort**

| Test | Measure | With the Skill | Without |
| --- | --- | --- | --- |
| Review | Defects found (of 18) | **12**\* | 10 |
| Review | Misplaced module boundaries found (of 3) | **2**\* | 0 |
| Review | Time per review | 260 s\* | **178 s** |
| New application | Hidden acceptance checks | all passed | all passed |
| New application | Versions with quadratic work | none | none |
| New application | Mechanisms nobody asked for | **4 to 8** | 5 to 9 |
| New application | Places with repeated work | **0** | 3 |
| New application | Hidden errors | **0** | 0 to 1 |

The better result of each row is bold. \* An older run, measured with an
earlier revision of the rules.

With the current rules neither model builds locks, synchronisation between
windows, paging or caches the requests did not ask for, and a failed write or
file read is reported to the user.

The limits: one or two runs per cell show a direction, not an effect size.
The rules grew from the same two projects the review cases come from. The
Sol counts with the Skill were made by other readers than the counts without
it, so that pair is a rough comparison.

## Compatibility

Developed for Codex and Claude Code with reference access and a shell
for project checks. Size checks require Python 3.11+ and the bundled checker.
Tested with `gpt-6.1-sol` and Claude Opus 5.5; these models at medium reasoning effort are the minimum,
because lower effort skips steps more often.

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
- [Skillwriter](https://github.com/benjaminstelzer/scoville-skillwriter) writes, simplifies and reviews Skills and reusable agent prompts.

## License

MIT. See [LICENSE](LICENSE).
