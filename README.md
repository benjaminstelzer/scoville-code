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
  builds that kind of thing. It doesn't add a second implementation beside
  the one that works.
- It starts from the simplest approach that solves the request. A safeguard,
  an abstraction or a test needs a real case in this application - a local
  script is not hardened like a payment service.
- It names the test that proves the request and reports it by name. A bug is
  confirmed before it is fixed and then covered by a passing test. Behavior
  whose failure would charge a wrong amount, grant access, lose data or open
  a security hole also gets a test that is seen failing first. "All tests
  pass" doesn't count when the relevant test wasn't among them.
- The report keeps what was observed apart from what remains unverified.
- Your architecture and project rules come first.
- Where the host can start a separate agent, a change to code behavior is
  read once by an agent that hasn't seen the author's reasoning.
- A review goes through the same points in someone else's change and names
  the place, the problem and what to use instead.

## What it costs

Reading the relevant code and checking behavior takes tokens and time. The
independent reading of a change adds one agent run.

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

In a brand-new project, Code falls back on its
[project conventions](scoville-code/references/project-conventions.md) for
anything your instructions leave open. Existing projects keep their
organization.

## Install

Works in Codex and Claude Code. It needs a shell for the project's checks and
Python 3.11+ for its bundled helper.

Use `gpt-6.2-sol` or Claude Opus 5.5 at medium reasoning effort or higher. Below
that, steps get skipped more often.

Ask your agent host:

```text
Install this Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-code/tree/main/scoville-code
Preserve personal settings and unrelated Skills. Report the installed location
and whether the host discovers the Skill.
```

The host needs write access to its Skills directory. The
[Codex](https://learn.chatgpt.com/docs/build-skills) and
[Claude Code](https://code.claude.com/docs/en/skills) Skills guides say where
that is. This Skill works on its own. The other Scoville Skills are in the
[Scoville Suite](https://github.com/benjaminstelzer/scoville-suite).

## Configuration

You can edit the bundled [conventions](scoville-code/references/project-conventions.md),
but the next update may overwrite them. To keep your own:

1. Create a Markdown file outside the Skill installation.
2. Reference it from your global or project
`AGENTS.md` (Codex) or `CLAUDE.md` (Claude Code), for example:

```markdown
### Greenfield project conventions

For the initial organization of a wholly new project, first follow this
project's explicit requirements, then read `docs/project-conventions.md`
for my additional folder and filename conventions. Use Scoville Code's
defaults only for choices neither source settles. Do not apply this
fallback to additions or refactors in an existing project.
```

Relative paths resolve from the file that references them. The agent reads
the referenced file and tells you if it can't find it.

## Background

Code grew from engineering work in large, evolving projects. Early versions
could turn a small change into a ritual: extra safeguards, repeated checks and
elaborate proof that added little to the result. The useful shift was toward
the actual problem, a maintainable solution and tests that protect real
behavior.

Against no Skill, on 18 real changes that each hid a defect, Claude Opus 5.5
found 16 with Code and 10 without. That comes from one or two runs with an
earlier revision of the rules - a direction, not an effect size.

The [full instructions](https://github.com/benjaminstelzer/scoville-code/blob/main/scoville-code/SKILL.md) are what the agent reads.
The [development notes](https://github.com/benjaminstelzer/scoville-suite/blob/main/members/scoville-code/development/README.md)
have the test tables and the sources.

## License

MIT. See [LICENSE](LICENSE).
