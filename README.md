# Scoville Code Anti-AI-Slop

Sharpens the output. Turns down the slop.

We have all seen it:

- Your agent reports "✅ All tests pass" but never ran them.
- You asked for a bugfix and got 400 lines of extra test setup around a
  one-line change.
- A second helper function appears even though the project already has one that
  does the same job three files away.
- The automated checks pass, the change is merged, and the system is a little
  harder to understand than before.

That is AI slop: motion without progress toward what you actually asked for.
Scoville is an Agent Skill—a reusable instruction file for coding agents. It
keeps the agent focused on the result you can see and use. Correct code, sensible
structure, and useful checks still matter, but they support the requested
change instead of replacing it. A one-line fix should not arrive wrapped in a
seven-section plan. It has, historically.

It prevents two opposite failures. The first is unproven work: the agent says a
change works without checking. The second is process theater: the agent produces
plans, tests, refactors, and documentation but not the requested behavior.
Scoville follows your instructions and the project's existing workflow first;
its own rules fill only the gaps.

## Why "Scoville"?

The original Scoville test measured how far chili extract could be diluted
before trained tasters could no longer detect the heat. AI slop works the same
way in reverse: real engineering gets diluted with extra setup, filler tests,
and unproven claims until no actual progress is detectable. This skill
measures, and limits, that dilution. It is the one Scoville scale where you want
the heat.

## Install

Works with any coding agent that supports the Agent Skills format: a `SKILL.md`
instruction file with its name and description at the top. Compatible agents
include Claude Code and Codex.

Usually, let your coding agent install the skill. Send it this prompt:

```text
Install this Agent Skill from GitHub and make it available for my coding work:
https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/tree/main/scoville-code-anti-ai-slop
```

Add "for all my projects" or "only for this project" when the installation
scope matters. The agent should choose its supported skills directory,
install the skill directory under the unchanged name
`scoville-code-anti-ai-slop`, and refresh its skill list.

If your agent cannot install skills itself, copy the repository's
`scoville-code-anti-ai-slop/` directory so the final path is:

```text
<skills-dir>/scoville-code-anti-ai-slop/SKILL.md
```

For Claude Code, `<skills-dir>` is `~/.claude/skills/` for all projects or
`.claude/skills/` inside a repository for that project only. For other agents,
consult their documentation; paths differ per agent.

**Verify it works.** Skills load when a relevant task calls for them, so try a
small task: *"Use Scoville to rename one variable that is used only inside a
single function and does not change what the program does."* Unless your
project has stricter rules, the agent should make only that change. It should
run at most one existing quick check and stop—no plan, new test, or full test
suite for a harmless rename.

**What it costs.** Skill discovery exposes only the name and description. After
activation, the core loads first and selects planning, change workflow, and
validation guidance only when the task needs them. Provider token usage also
depends on the host and conversation.

## What it enforces

- **Deliver the result you asked for.** The agent spends its effort on the
  requested behavior. Plans, tests, documentation, and refactors are used when
  they help deliver that behavior or prevent a specific problem. The checklist
  is not the feature.
- **Prove results before claiming them.** The agent runs the smallest useful
  checks and reports only what they actually show. A failed check counts as a
  real problem unless evidence shows that it was already there or comes from
  the tooling or setup. When the tooling fails, the agent may run the project's
  documented setup once or try one genuinely different check; it does not shop
  around for a friendlier test environment. If a function or public interface
  changes, at least one real use of it is checked. Once the behavior is proven,
  testing stops. After two failed fixes for the same problem, the agent changes
  its approach instead of applying patch number three with renewed optimism.
- **Match the process to the job.** The agent can answer or review without
  editing. It can explore an idea without calling the prototype finished.
  Ordinary changes receive focused checks; releases and serious risks receive
  broader ones. A one-line rename does not become a launch rehearsal. These
  modes guide the agent internally rather than appearing as ceremony in its
  answer.
- **Do not make unsafe behavior look safe.** A helper called `safe_delete` must
  actually be safe. A timeout must not return old or empty data as though it
  were fresh. Distinct errors must not be reduced to one yes-or-no value when
  callers need the reason. Work is not reported as saved or published before
  the underlying operation has completed, and a new shortcut must not bypass
  the project's existing safety checks. Existing untidiness is reported rather
  than pulled into the task unless the current change makes it worse or cannot
  work correctly without fixing it.
- **Use the project's existing records.** Important decisions belong in the
  plan, architecture record, or pull request the project already uses. The
  agent does not create a second planning diary to document the first one. A
  handoff records only what another agent needs to continue correctly.
- **Ask when the answer changes the outcome.** The agent first completes work
  that does not depend on the question. It asks before choosing different
  product behavior, accepting irreversible loss, weakening a protection,
  adding external cost, or expanding the scope. When nobody is present to
  answer, it takes the smallest reversible option and reports the assumption.
- **Fit the tools already in use.** Scoville defines what must be established,
  not a universal list of commands. In a version-controlled project, the agent
  finishes by inspecting the complete relevant change and repository state.
  Without version control, it reads before overwriting and preserves everything
  outside the requested edit.

The full rules live in
[SKILL.md](scoville-code-anti-ai-slop/SKILL.md).

## Use with the Scoville family

Code works independently. When companion Skills are installed, combine them
only for the concerns they own.

Use [Scoville UI Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop)
when an engineering task also changes interface hierarchy, layout, interaction
presentation, responsive behavior, or rendered UI evidence. Use
[Scoville Scribe Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop)
when it changes reader-facing wording. Use
[Scoville Plan](https://github.com/benjaminstelzer/scoville-plan) when the
engineering work spans dependent outcomes or must survive interruption or
handoff. Plan owns durable direction and Work Item lifecycle; Code keeps the
implementation scoped and proven; UI preserves the product's design language
and interface quality; Scribe preserves meaning, terminology, and factual
wording.

## Design

Scoville keeps authorization, ownership, risk selection, review scope, and
truthful reporting in the core. It conditionally loads three focused guides:

- [references/planning-and-decisions.md](scoville-code-anti-ai-slop/references/planning-and-decisions.md)
  covers project plans, decisions, durable handoffs, and genuine decision
  ambiguity.
- [references/change-workflow.md](scoville-code-anti-ai-slop/references/change-workflow.md)
  covers exploration, implementation, structural risk, and concrete patch or
  ownership review.
- [references/validation.md](scoville-code-anti-ai-slop/references/validation.md)
  covers check selection, repeated failures, evidence review, and completion
  claims.

The skill does not replace your instructions, architecture documents, automated
checks, security policy, release workflow, or human review. For each decision,
it first follows the current request, then requirements of the agent system,
then the project's rules and established practices. It uses its own defaults
only when those sources leave the decision open. This lets Scoville fill gaps
instead of fighting the project. A project rule can replace a Scoville default,
but it can never justify invented test results or a weaker safety check.

Earlier versions maintained their own working-plan file, decision log, and
completion templates. In practice, agents began treating the production of
plans, tests, and tidy process as success—even when the requested change was
still missing. The anti-slop skill had started producing slop of its own, which
was at least on topic.

The current version therefore creates no records of its own. If the project
already has a plan, that is the plan. An agent system that requires its own plan
view may keep a temporary copy, but it must not become a competing record.
Decisions that change the result, scope, ownership, public behavior, data or
security, reversibility, or the limits of testing go into the project's existing
plan, architecture record, commit, or pull request.

## Sources and inspirations

The skill draws from the following sources:

- [OpenAI coding-agent best practices](https://developers.openai.com/codex/learn/best-practices): goal/context/constraints/done-when prompts, planning before complex work, tight permissions, focused checks, and diff review.
- [Cursor Thermo-Nuclear Code Quality Review Skill](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md): simplifying tangled code, questioning unnecessary wrappers, keeping one clear owner for each behavior, and reviewing the complete change rather than isolated lines.
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/): attacks hidden in prompts, leaked private information, unsafe dependencies, mishandled model output, and agents receiving more authority than they need.
- [OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and [LLM06 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/): treat untrusted text as data, grant only necessary access, and require human approval for high-risk actions.
- [Andrej Karpathy on vibe coding](https://x.com/karpathy/status/1886192184808149383): natural-language software construction is powerful, but production engineering still needs scope, review, testing, taste, and ownership.
- [Simon Willison's distinction between vibe coding and reviewed, tested,
  understood AI-assisted coding](https://simonwillison.net/2025/Mar/19/vibe-coding/):
  Scoville is for the latter.
- Martin Fowler on [internal quality](https://martinfowler.com/articles/is-quality-worth-cost.html) and [technical debt](https://martinfowler.com/bliki/TechnicalDebt.html): maintainability is a delivery property, not polish.
- Recent research on AI/vibe-coding quality: [Vibe Coding in Practice](https://arxiv.org/abs/2510.00328), [VibeContract](https://arxiv.org/abs/2603.15691), and [Is Vibe Coding Safe?](https://arxiv.org/abs/2512.03262).

## Repository contents

The directory you install, `scoville-code-anti-ai-slop/`, contains the core
instruction file, three focused references, and a small metadata file that
helps agents display the skill. The repository's README, changelog, and license
stay outside that directory. The skill installs no scripts, libraries, or
other software and contains no rules tied to a particular programming language
or framework.

## Status

The installable directory passes the canonical Agent Skill validator, focused
Sol Medium routing probes, family-composition probes, and local host-neutrality
checks. These runs validate the routing behavior in Codex CLI; the Skill text
itself remains host-neutral, while empirical behavior in other hosts depends on
their Agent Skills implementation.

## License

MIT - see [LICENSE](LICENSE).
