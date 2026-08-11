# Scoville Code Anti-AI-Slop

Keeps the requested engineering result visible through the process around it.

Scoville Code is a goal-first Agent Skill for planning, changing, testing,
reviewing, and removing code or engineering artifacts. It preserves canonical
ownership, scope, risk boundaries, validation, and honest evidence. It can
answer or diagnose without editing, and it does not turn every rename into a
release rehearsal.

## Why "Scoville"?

The family is named for useful signal that survives dilution. In coding, the
heat is the requested behavior after plans, wrappers, tests, and confident
status prose have all tried to become the feature.

## How to use

Name Scoville Code for codebase work where scope, ownership, risk, or evidence
matters:

```text
Use Scoville Code to implement rate limiting in the existing API owner. Keep the diff scoped, preserve public behavior outside the stated limit, and run the repository's relevant checks.
```

```text
Use Scoville Code to diagnose why this migration sometimes leaves consumers on the old schema. Identify the supported root cause and evidence; do not change files.
```

```text
Use Scoville Code to review this patch for correctness, hidden failure paths, ownership drift, and missing validation. Report prioritized findings only.
```

Explicit `$scoville-code-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

## Install

Use an Agent Skills-compatible host and Terra 5.6 Medium or a comparably
capable executor such as Opus 4.8. Ask the agent to install:

```text
Install this Agent Skill and refresh the available Skill list:
https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/tree/main/scoville-code-anti-ai-slop
Keep the installed directory name scoville-code-anti-ai-slop. Use Terra 5.6 Medium or a comparably capable executor such as Opus 4.8.
```

The final path must end in
`<skills-dir>/scoville-code-anti-ai-slop/SKILL.md`. For Claude Code, use
`~/.claude/skills/` globally or `.claude/skills/` inside one project. Other
hosts use their supported Skills directory.

**What it costs.** The strengthened 2,045-token Core is 16.59% larger than
`v1.0.6`; workflow references load only when needed. That extra context buys
tighter scope, risk handling, validation, and honest evidence. Use it where
correctness and maintainability matter; skip it for a disposable vibe-coding
experiment when token use matters more. See
[benchmark evidence](docs/benchmark-evidence.md).

## What it enforces

- **Outcome over ceremony.** Plans, tests, docs, and refactors support the
  requested behavior; producing them is not completion by itself.
- **Canonical ownership.** The change fits the project's existing architecture,
  records, terminology, and workflow instead of creating a second owner.
- **Proportionate risk.** Small reversible work stays small; destructive,
  public, security, data, or release work receives stronger gates.
- **Evidence before claims.** Checks prove only what they observed. A failed
  tool is not silently promoted to a passing product.
- **Root-cause correction.** The agent changes approach after repeated failure
  instead of applying patch number three with renewed optimism.
- **Material questions only.** It asks when a missing choice changes behavior,
  authority, cost, reversibility, or scope, not for details the code settles.
- **Complete handoff.** The final report names changed behavior, relevant
  validation, unresolved failures, and repository state without pretending.

The complete contract is in
[SKILL.md](scoville-code-anti-ai-slop/SKILL.md).

## How it works

The Core selects an internal mode—Advise, Explore, Develop, or Harden—then
loads only the planning, change-workflow, or validation guidance the operation
needs. Project instructions and established owners outrank Skill defaults. The
Skill creates no private plan or decision log and installs no executable
software; the repository remains the source of truth, which saves everyone
from auditing the audit trail's audit trail.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores
  materially different mechanisms before selection.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns
  engineering scope, implementation, risk, and validation.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns
  interface hierarchy, framework fit, accessibility, and rendered evidence.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns
  wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans,
  Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active
  work to another agent or session.

## Status

A reliability-first extension of
[Microsoft SkillOpt](https://github.com/microsoft/SkillOpt) tested the six
Scoville Skills across **1,201 optimization and evaluation runs**. Scoville
Code passed **30/30 final cases**. Its Core is **16.59% larger than v1.0.6**
because reliability coverage expanded; SkillOpt compressed the strengthened
version. See [benchmark evidence](docs/benchmark-evidence.md).
The [family run ledger](docs/optimization-history.md) shows the complete count.

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

## License

MIT - see [LICENSE](LICENSE).
