# Agent instruction design

Write reusable instructions and agent-facing prompts for current frontier
models of OpenAI and Anthropic unless the request or project names other target
models. Give them what they lack and constrain only what must not vary. Mark
provider-specific advice. These writing rules grant no task permissions.

- **Outcome and done:** State the goal, context the recipient cannot infer,
  real constraints and what counts as done. Omit explanations of general
  knowledge; retain contracts, project conventions and concise guidance against
  known model failure patterns. Preserve intended
  scope, facts, permissions, required behavior and acceptance criteria.
- **Reasons:** Give the reason for a non-obvious rule when it helps apply it.
- **Freedom matches fragility:** Use goals and heuristics where several
  approaches work. Prescribe exact commands, schemas or order only where a
  deviation breaks something; prefer an existing helper for deterministic work.
- **Plain emphasis:** Write "Use X when Y", not "CRITICAL: you MUST". Strong
  emphasis can make the recipient over-apply a rule.
- **Real stops:** Name the concrete decisions or actions requiring user approval
  and their conditions. Honor approval already given; vague caution causes
  premature stops.
- **Useful guidance:** Omit default behavior such as "think carefully". A check
  should name a concrete acceptance criterion, invariant or validator.
- **One owner:** Keep each rule once at its responsible source. State precedence
  where instructions can collide, including the user's request over Skill
  defaults. First clarify, merge or remove the rule causing the problem. Add a
  counterrule only for an independently necessary boundary.
- **Positive and specific:** State the wanted behavior and its condition. Name
  concrete patterns to avoid when necessary; add an example for real ambiguity.
- **Stable wording:** Use one term per meaning. Describe current behavior, not
  removed rules, previous versions or expiring dates.
- **Facts:** State what must be factual and where invented content is allowed.
  Keep literal user text, fixed schemas, field names and helper contracts intact.
- **Structure:** Use numbered steps for required order, a table for a simple
  choice and a Mermaid flow for complex branches, loops, stops or role handoffs.
  Let the diagram replace duplicate sequence prose while retaining every rule,
  permission, stop and exception in the diagram or accompanying text.

For Mermaid flowcharts use `flowchart TD`, descriptive node IDs, quoted labels
and labelled question exits. Give each node one action or question and use the
same terms as the text. Split flows above about 20 nodes by phase when clearer.
Preserve useful existing diagrams.

Supply the context needed without hidden history. Where the recipient can read
a required source, give its exact path and reading condition rather than
duplicating it. An output schema governs shape; do not add fields merely to
apply this guidance. Detailed Skill-authoring workflow and validation belong
to Scoville Skillwriter and the host's Skill Creator.
