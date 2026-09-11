# Deferred acceptance: Astra instruction fixes

2026-09-11: the user authorized the reviewed changes and explicitly deferred
acceptance to conserve tokens, intending to observe behavior. Source edits do
not establish behavioral acceptance. No test suite, model probe or post-change
independent review has run. Local installation and publication were subsequently authorized on 2026-09-11.
They do not close acceptance; observations must identify which package actually ran.

## F04: editorial migration labels

Only purely editorial work is excluded from the migration label trigger. Real
migration policy and all other High triggers remain unchanged.

Pending cases:
- A wording-only prompt update called a migration is classified by actual effects.
- A destructive data migration remains High when reviewed or run as a dry run.
- A persisted-contract change is not classified as ordinary text editing.
- Explicit release/migration checks remain required. Measure classification and
  actual testing separately; risk alone already does not widen test scope.

## Other owners

Each repository owns its acceptance record, with all cases still pending:
- [F01 WordPress](https://github.com/benjaminstelzer/wordpress-backend-ui-skill/blob/main/development/acceptance-astra.md)
- [F02 Plan](https://github.com/benjaminstelzer/scoville-plan/blob/main/development/acceptance-astra.md)
- [F05 Claude and Astra](https://github.com/benjaminstelzer/ask-claude-and-astra-for-codex/blob/main/development/acceptance-astra.md)
- [F05 Claude and SOL](https://github.com/benjaminstelzer/ask-claude-and-sol-for-codex/blob/main/development/acceptance-astra.md)
- [F09a Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm/blob/main/development/acceptance-astra.md)

## Unimplemented conditional candidates

- F03 Plan drafting: first observe a sufficiently specified natural-language
  request. Clarify only an actual ambiguity/failure; never invent requirements
  or change the initial active Plan and todo/current item lifecycle.
- F08 Code/UI/Scribe opt-out: probe both before loading and after prior authorized
  use. Continue an authorized edit without the excluded Skill; explicit no-edit
  still forbids edits. Omit changes if the existing local opt-out contract works.
- F07 review length: existing roles already allow detailed answers over 6000
  characters. Probe short, explicitly detailed and genuinely truncated results
  before changing anything. No multipart protocol is authorized by this record.
- F09b Brainstorm read batching/LEDGER and F10 Design coverage bookkeeping stay
  unchanged pending demonstrated need. Preserve explicit read limits, separate
  provenance and detection of a missing middle even with an intact footer.

## Resume acceptance

Start only when the user requests it. Identify actual host, model/effort and loaded
package paths/hashes; installed copies may differ from these source repositories.
For comparisons, retain the pre-change Git baseline and candidate working tree,
use identical tasks/tools and keep expected outcomes outside the executor input.
Inspect existing relevant tests before choosing commands. Structural tests and
manual observations prove only their own scope. Record observed behavior and
remaining gaps here or in the owning record, never infer a pass from silence.
No automatic recurring task or broad model benchmark is requested.
