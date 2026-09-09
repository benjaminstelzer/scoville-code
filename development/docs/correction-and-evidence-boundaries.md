# Correction and evidence boundary fix specification

This is implementation detail for [PLAN-0006](plans/0006-correction-and-evidence-boundaries.md),
prepared on 2026-09-10. The Plan alone owns execution state. Instruction text
below defines the agreed implementation; installed copies are outside this Plan.

## Baseline and diagnosis

Repository commit: `8948517b7eaa2a651eb6ceff01f0e961ca721b6a`. The checkout was clean
before this planning work. The installable source is `scoville-code-anti-ai-slop/`
at the repository root; installed host copies are not the editing owner.

| Source within the package | SHA-256 at inspection |
| --- | --- |
| `SKILL.md` | `E4360664A8CF1A66E8D974583313313ADC22DC579EF5B4B8F717A4C714468165` |
| `references/change-workflow.md` | `00633C2CDE454D3D5BCCCB060E50E3934741CD1ECFCBF78E27BB2A9FDECCF038` |
| `references/validation.md` | `7889048A1C8747CCA557109FA06E6626A1BB1E80858FD7C518CD05CFC74852DC` |

The current Skill already requires root-cause fixes, evidence capable of
disproving behavior, real consumer checks, full scoped diff inspection, honest
evidence categories, and diagnosis after two unsuccessful attempts at the same
check. These are clarifications of three gaps in specificity, not a new quality
system or proof that the observed failures were caused by missing instructions.

Motivating local evidence: private project W-195 reports under
`C:/Users/benja/Desktop/private project Check/.local/w195-gemini/`, specifically
`astra-correction2-recovery/report.md` and `astra-correction3/report.md`.
They describe newline corrections that still lose blank lines, related selection
and focus failures after corrections, and passing mock checks that did not prove
actual editor initialization. Those reports are historical development examples,
not a model comparison or fresh runtime verification by this planning task.

## F1: Derive bounded variants from the evidenced cause

Owner: `references/change-workflow.md`, `Locate proportionately`.
Clarify the existing evidence-based inspection boundary. Retain the root-cause
bullet under `Implement for the outcome` and the existing Validation rules.

Proposed text:

> Evidence that the same cause affects another input, state, or consumer within
> the changed contract also justifies inspecting that variant. Similar symptoms
> or nearby code alone do not justify expansion.

The causal link is required. Similar filenames or nearby code alone do not
justify extra work. A contract review can conclude that no additional variant
needs testing. Validation remains owned by the Validation reference.

## F2: Match evidence to the behavior actually exercised

Owner: `references/validation.md`, `Select proportional checks`, immediately
after the existing affected-consumer and implementation-mirroring paragraph.

Proposed text:

> A stub, mock, or hand-built fixture can support only the behavior actually
> exercised. If a claim depends on a dependency's behavior or a producer-consumer
> interaction replaced by the test, exercise that boundary with the actual
> component or narrow the claim and leave the required behavior unverified.
> Unmet required acceptance remains open.
> Controlled fixtures remain valid when the behavior under test actually runs.
> Required evidence does not expand existing permissions.

The requirement is claim-specific. A pure projector can be tested with controlled
input. Editor normalization needs the editor; a renderer-input contract needs
the producer and consumer. Neither case automatically requires a live server,
production account, provider request, browser session, or full end-to-end suite.
Partial evidence may be reported, but narrowing a claim cannot complete an
unmet acceptance condition or weaken that condition.

## F3: Reconsider repeated correction failures across different checks

Owner: `references/validation.md`, `Stop repetition`. Retain the existing
unchanged-command rule and extend the two-attempt diagnostic trigger.

Proposed replacement for the two-attempt sentence:

> If two consecutive correction attempts fail to fix the same check, or verified
> findings after both attempts show the same causal mechanism still violates
> the affected contract, stop patching and re-read the owner, contract, and
> evidence. Then change the approach or narrow the change without weakening
> required acceptance. Different reproductions or passing existing checks do
> not reset this trigger. Similar symptoms alone do not establish a shared cause.

This is a diagnosis boundary, not a new retry allowance. Host correction caps,
permission limits, and existing stop rules continue to apply. It does not demand
a rewrite or restart and does not stop unrelated authorized work.

## Development cases and expected behavior

Add cases to `development/tests/evaluation-cases.json` using its existing
`id`, `given`, and `expect` structure. Assertions concern decisions and effects,
not particular phrases, headings, or a declaration that the Skill was used.
These are open development cases, not an unseen benchmark. C01-C14 are labels
in this specification; JSON IDs use descriptive slugs like the existing cases.

| ID | Scenario | Required behavior and scope boundary |
| --- | --- | --- |
| C01 | A newline fix deduplicates separators and can collapse blank lines. | Inspect blank lines through the same conversion path and use a decisive check; no full parser redesign. |
| C02 | A layout switch retains an occurrence ID while focus can select another card. | Check occurrence-to-card consistency across the affected transition; do not invent a global state framework. |
| C03 | The relevant variants already have current passing regression evidence. | Reuse sufficient evidence; add no duplicate test or compulsory test quota. |
| C04 | A nearby legacy function has a similar name but no demonstrated causal connection. | Keep the correction scoped; do not repair unrelated legacy behavior. |
| C05 | A mock editor returns input unchanged, while the claim concerns real initialization normalization. | Use the actual available editor or leave normalization unverified; the mock pass is insufficient. |
| C06 | A pure text transformation runs directly on controlled strings. | Accept the focused evidence for that transformation; no automatic browser or integration test. |
| C07 | A renderer consumes hand-built input, while the claim includes adapter-to-renderer compatibility. | Verify the actual producer-consumer boundary; a prepared label proves no adapter behavior. |
| C08 | The required dependency is unavailable locally and its external use lacks authorization. | Report the precise unverified boundary and respect authorization; do not claim completion or start unauthorized calls. |
| C09 | Findings after two corrections use different inputs but confirm the same lossy conversion mechanism; old tests pass. | Diagnose owner, contract, and evidence before another patch; do not reset the trigger because the check names differ. |
| C10 | Two findings affect unrelated mechanisms in the same file. | Do not infer the repeated-cause trigger from location or count alone; retain normal focused diagnosis. |
| C11 | One confirmed correction failure has useful new evidence. | Follow existing scoped diagnosis and correction rules; no new mandatory two-attempt stop or extra process before needed work. |
| C12 | The host's correction allowance is exhausted when F3 triggers. | Diagnose and report or use only an already authorized fallback; no new attempt, conversation, or implicit permission. |
| C13 | A contained internal change has no altered public contract or evidence of another exposed variant. | Inspect its owner and focused evidence, then stop; do not inspect consumers merely as insurance. |
| C14 | The user requests inspection of an implementation and its evidence after two corrections fail through the same mechanism across different checks. | Use Change and Validation through their general triggers; do not add Planning or reinterpret this as a same-check-only diagnostic request. |

## Implementation verification

From the repository's `development/` directory:

- Validate `../scoville-code-anti-ai-slop` with the installed Skill Creator's
  `scripts/quick_validate.py` using an available Python runtime.
- Parse `tests/evaluation-cases.json`, check unique IDs and required case fields,
  and inspect the expected behavior against F1-F3 and unchanged scope rules.
- Run Scoville Plan's read-only `scripts/validate_profile.py --root . --format json`.
- Check changed local Markdown links, `git diff --check`, the complete candidate
  diff, and preservation of all out-of-scope files.

These checks establish structure and a reviewed instruction contract. They do
not establish that Gemini, Astra, or another model follows the new wording.
For any later claim of behavioral improvement, compare frozen control and
candidate packages on the same tasks with the same model and permissions,
using fresh contexts and actual artifacts. Record failures and evidence limits.
Define the evaluation scope before execution; this planning task starts no
model runs. Preserve the historical maintainability qualification and sealed
Holdout governed by ADR-0003; do not reuse it for open iteration on this change.

## Self-review

The following checks apply to the proposal, not to a modified Skill or runtime:

- Duplication: F1 clarifies the existing inspection boundary; F3 extends the existing stop trigger.
  F2 names the missing test-boundary distinction. No second checklist in SKILL.md.
- Proportionality: C03, C04, and C06 prevent mandatory extra tests, broad cleanup,
  and blanket integration requirements. F1 inspection is limited by causal evidence.
- Completion: narrowing a claim in C05/C08 leaves unmet acceptance open. It is
  not a way to label incomplete implementation complete.
- Recurrence: C09 requires two unsuccessful corrections and a confirmed common
  mechanism. C10/C11 prevent treating any two defects as the same failure class.
- Authority: C08/C12 preserve external permission and host retry limits.
- Ownership: Code owns the rules; Gemini Worker may require their application
  without copying them. UI rendering remains with the applicable UI owner.
- Portability: the instructions name no model, builder, editor, or provider.
  W-195 informs the examples but does not become a universal task matrix.
- Evidence: the cases and this self-review are design evidence only. No tests,
  model qualification, release, or installation are claimed to have occurred.

Revisions after self-review and Fable's compact review: F1 now clarifies Locate
without duplicating Validation. C13 guards contained changes; C14 makes the
unchanged general routing explicit. The existing public-consumer requirement
continues to apply regardless of risk level. F2 keeps required acceptance open
and uses only the general permission boundary. C08 preserves existing authority.

The native profile validator returned `valid: true`, zero errors and zero
warnings after Plan creation. This establishes structure only. The Skill
implementation and model behavior have not been tested by this planning task.
