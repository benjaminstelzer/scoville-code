# Astra acceptance and session audit, 12 September 2026

The reviewed September 11 changes passed the limited text probes below. Full
host routing acceptance remains open. The session audit found avoidable work,
but does not establish that Astra or Skill size caused the account quota spike.

Subsequent approved fixes and tool-capable fixture results are recorded in
[skill-fix-acceptance-2026-09-12.md](skill-fix-acceptance-2026-09-12.md).
The historical test and audit boundaries below remain unchanged.

## Test results

Existing suites, run once with Python 3.14:

- Scoville Plan: 50/50 tests passed.
- Ask Claude and Astra: 24/24 tests passed.
- Ask Claude and SOL: 21/21 tests passed.

Command in each owning repository:
`python -B -m unittest discover -s development/tests -v`.
These test profile structure and adapter behavior, not Desktop orchestration.
Existing Code (24), Plan (27) and Brainstorm (8) case definitions also parsed
as valid JSON; parsing is not execution of those cases.

Fifteen fresh text probes used Codex CLI `0.154.0-alpha.6.2`, requested model
`gpt-6-astra`, effort `low`. Each process received only its named Skill core,
necessary supplied reference and fixture text. Host Skill discovery, plugins,
apps, memories, browser and shell execution were disabled. No conversation was
resumed. Package content was copied from the installed Codex package and hashed.
This is controlled instruction application, not native discovery or tool-use proof.
Model/effort are command-selected; independent backend model attestation is absent.

| Cases | Observed result | Remaining boundary |
| --- | --- | --- |
| F04: editorial migration, destructive dry-run review, consumed JSON type change, explicit linkcheck | Normal, High and Structural distinguished; explicit check retained | No actual migration or check execution |
| F01: visible PHP/Core settings source, unknown renderer, excluded metabox | Source resolved without question; one relevant question with independent button assessment; metabox excluded | No actual source reads, browser or runtime validation |
| F02: initial status, repeated status, dependent implementation, explicit Decision handling | Both proposals visible; status asks for no decision; dependent/explicit handling asks | Repeat uses supplied prior-state context, not a resumed session; no lifecycle writes |
| F09a: audit the Skill, inspect a known correct setting | Audit stays an audit; known fix uses ordinary-task reasoning | No real generators, reads, capacity handling or YES workflow |
| F05: ordinary self-assessment with either consultation Skill available | No consultation initiated | No tools available; authorized creation, follow-up, partial provider failure and transport remain untested |

No target-rule violation was observed in these narrow cases. This does not close
the complete acceptance cases in the owning records. F03, F07, F08, F09b and F10
remain unqualified. The separate UI W-002 records were not resumed or changed.

One earlier Medium smoke run completed before the user's Low correction. It is
invalid: Windows CLI policy rejected its `Get-Content`, so no Skill read occurred.
The failure was not bypassed. Text injection was the one alternative check; it
cannot substitute for that missing read. The smoke used 26,301 input and 281
output tokens. The 15 Low probes used 242,433 input tokens (81,664 cached), 3,237
output tokens and 172 seconds in aggregate. No before/after Skill comparison ran.

All six installed `SKILL.md` files matched repository source. Full package
differences were limited to Brainstorm YAML line endings and private `config.json`
files in the two consultation packages. No configuration values were published.

| Package | Tested source commit | Installed SKILL.md SHA-256 |
| --- | --- | --- |
| Code | e39f8d9413d73310921c8677f83f61fdb394c06c | 6b0ce702307e79f8e71fcccdad887a149e8c1e8ef6863fe5d6027e8c40416473 |
| Plan | 298a8d37976bd6cda027cc70bc9be6fecfd385eb | d534f0ccdb7e31b38a5dc9ccc1fba3319207808ca5f08ef04828b96cf9f2ba2d |
| WordPress | 5471c1c81fca012abc1c818e0324d86c99567c29 | e13f0739de4dd1d8fe8afb5dc81336c11e656673c842967bc8921863615becef |
| Brainstorm | c3b62c7ea64bcffe09526aead7e3c3d999168ea8 | ccd6d1ecca8d802c29d16af6ed0c896df8840564f481d60a7d56f9d5def2d697 |
| Claude/Astra | 3fad73fe017747d6d455db17ef8d45adffa82c4a | d017e72312f7b464f564293c49255db9d1fec1964e6cf47f16585e5feef83f20 |
| Claude/SOL | d7c252eb561376409cc9c8b038f9c4808edb3e30 | 067f442f26b8191b3542e14460822dbb843c78fca899d05869607af6435a7eba |

## Session coverage and private project consumption

Read-only inventory and machine triage covered 698 local Codex sessions with
events between 2026-09-05 09:04 UTC and 2026-09-12 09:04 UTC: 644 archived and
54 unarchived. This includes 129 `vscode`, 22 `exec`, and 547 other/nested source
records; it is not 698 independent user tasks. Detailed inspection targeted
user corrections, repeated calls and high-usage sessions, not every turn.
Currently active sessions are only represented through this cutoff.

private project attribution uses a recorded working directory containing `private project`.
Usage sums unique `token_usage_record.response_id` values, requires the record's
thread ID to match its owning session, and filters by event timestamp. It does
not sum cumulative `token_count` snapshots. Reasoning is part of output and is
not added again. Other-provider worker usage outside these records is absent.

| Local private project usage | Aug 29–Sep 5 | Sep 5–Sep 12 |
| --- | ---: | ---: |
| Sessions with recorded usage | 61 | 231 |
| Model responses | 9,401 | 21,630 |
| Input tokens, including cache | 1,293,971,752 | 2,936,190,903 |
| Cached input tokens | 1,255,879,040 | 2,865,242,880 |
| Uncached input tokens | 38,092,712 | 70,948,023 |
| Output tokens | 4,720,945 | 9,596,365 |
| Mean input per response | 137,642 | 135,746 |

The recent period contains 2.30 times as many responses, while mean input per
response is slightly lower. 97.58% of recent input is cached. Recorded activity
in the earlier window starts September 2; active days, work volume, model mix
and completion output are not matched. These are therefore descriptive totals,
not a controlled weekly efficiency or model comparison. Cache accounting is not
account quota accounting; no euro cost or percentage of wasted quota is inferred.

One long private project session, `01a074c6-2024-7a23-a799-9c2ac9314daa`, accounts for
36.85% of recent private project input: 7,244 responses, 6,758 recorded outer tool calls
and 64 compactions. Nested shell commands are not counted as separate outer calls.
This concentration makes repeated interaction in long contexts a priority for
investigation; the whole session is not classified as waste.

## Located findings

The local source references below are original transcripts, not exported copies.

1. **Unbounded search generated avoidable output.** In “Prüfe private project
   Gemini-Verbrauch”, a content search covered `.local`, including browser data.
   The tool reported 27,370,019 original tokens and over 108 MB omitted; only a
   truncated result reached the caller. Those original tokens are NOT claimed
   as billed or model-consumed. The agent then narrowed the scope. This is a
   concrete execution failure against Code's proportionate-location rule, not
   evidence that the Skill needs a longer general warning. Source: session
   `01a085fb-adcf-7102-af19-244d92b80d3a`, lines 26–40.

2. **Empty polling repeatedly re-entered the model.** In “Hängende Session hier
   fortsetzen”, terminal session 99932 was polled at five-second effective
   intervals and returned no output repeatedly (lines 18713–18734). In session
   `01a08655-b9be-7432-a9c9-7d89e54528b1`, 123 of 259 outer calls contained
   polling; the identical 60-second wait occurred 88 times. Lines 977–1031 show
   ten consecutive timeout results. Waiting itself was necessary; the frequency
   and model re-entry are the optimization target. Host wakeup/update limits
   must remain respected. Do not treat every repeated wait as a Skill defect.

3. **Instruction availability and instruction application diverged.** In “Setze
   Phase 2 vollständig um”, the agent acknowledged using a plugin-specific
   switch instead of the DynAdm owner and overstating earlier UI assessments
   (line 3975). After acknowledging incomplete post-compaction restoration
   (3985), it read several reference files together; the output was again
   truncated (4003–4006). This supports a failure in applying/recovering the
   rules. It does not prove a host lost a loaded Skill. Source:
   `01a090fa-e3b8-7300-a5bf-b001d79b7675`.

4. **The former UI contract caused excessive check frequency.** The user
   identified “Every subsequent layout edit repeats…” as causing screenshots
   after small edits. “UI-Skill Prüfungen bündeln” changed that contract on
   September 11. Current source explicitly batches implementation and
   correction edits. Preserve that fix and test it; do not add another
   after-every-edit gate. Source: `01a0926f-b4ea-7913-89b9-4e47c5403666`, lines
   9–41. The WordPress companion's final-evidence requirements must be composed
   with the same batch boundary, not interpreted as a second full test pass.

5. **Transfer was followed by a repeated UI matrix.** “W-227 Priorisierte UI
   auf XMTEST abnehmen” ran final live editor checks, then the user explicitly
   stopped routine retesting after transfer. The assistant preserved that
   instruction. This was a scope/cadence correction; the earlier Work Item also
   requested installed acceptance, so the earlier checks are not retroactively
   unauthorized. Source: `01a08c0b-b92e-7631-8fbf-668e0c6a76eb`, lines 661–714.

6. **A historical stop was applied to a different workflow.** After W-209,
   the agent stopped the Codex chain using an old Gemini-chain stop. It admitted
   this might be too broad when asked “Warum stopp?”. The transcript supports
   an authority-scope ambiguity, not permission to erase old stops automatically.
   Source: `01a08c6d-98b6-71c2-b293-7caa55012522`, lines 715–727.

Counterevidence matters: the Phase 2 Scribe question at lines 248–253 did not
establish missing activation; the prior trace names Scribe/interface-text.
The private project typography investigation at `01a074c6…`, lines 42608–42611, found that
two suspected heading colors matched Core. Do not turn every user concern,
missing announcement or visual difference into a routing failure.

## Optimization direction

Prioritize fewer avoidable model/tool cycles and correct first implementation,
then reduce payload. The results do not support separate Astra Skill copies,
blanket token targets, removing required evidence, or adding repeated checklists.

| Priority | Owner | Concrete next change or test |
| --- | --- | --- |
| 1 | Code / execution harness | Before content search, identify candidate files. Exclude browser profiles, generated artifacts and raw traces unless they are the named source. Size each read to its output budget; recover only the missing range. Test a `.local` fixture containing large irrelevant data. |
| 1 | UI / WordPress / host context | Verify owner selection before styling writes and retain the selected owner plus pending checks across compaction. Reuse available instructions; reload only genuinely missing or changed portions. Test the DynAdm-switch failure and a truncated recovery read. |
| 1 | Worker / host orchestration | Use event waits and the longest host-permitted useful wait, with cursors. Do not interleave empty polls with speculative reads or repeated status narration. Test unchanged worker state and early user interruption. |
| 2 | UI / WordPress | Exercise the existing batch rule with several edits, one end-of-batch check, then one correction batch. Preserve final source/geometry/visual evidence without duplicate composed checks. |
| 2 | Code / Plan | Carry forward passed evidence while its relevant inputs remain unchanged. Recheck affected behavior after a real change, failure, environment difference or explicit request; transfer alone is not a second full acceptance suite. |
| 2 | Plan / handoff | Preserve the scope and subject of historical stops; reconcile a new authorized workflow before imposing an old stop on it. Test new Codex work versus a Gemini-specific stop. |

These are bounded follow-up recommendations, not implemented Skill changes.
Do not mechanically shorten the entire family or infer savings before a matched
behavioral test. A host-capable Astra Low run remains necessary for actual
activation, scoped reads, compaction recovery, edits and consultation lifecycle.
No Skill instructions, installations, private project code, release state or native Work Item lifecycle
were changed by this audit.

## Local evidence locations

Original transcripts remain under `C:/Users/benja/.codex/archived_sessions/`
or `C:/Users/benja/.codex/sessions/2026/09/11/`; their filename suffix is the
session UUID above. All line numbers refer to the original JSONL, one record
per line. Usage comes from read-only `state_5.sqlite` inventory plus those
transcripts. Generated raw probes, extracted messages and intermediate
statistics are disposable and are not published evidence.

- [Broad private project search](C:/Users/benja/.codex/archived_sessions/rollout-2026-09-09T13-44-18-01a085fb-adcf-7102-af19-244d92b80d3a.jsonl:26)
- [Empty terminal polling](C:/Users/benja/.codex/archived_sessions/rollout-2026-09-06T05-32-16-01a074c6-2024-7a23-a799-9c2ac9314daa.jsonl:18713)
- [Repeated coordinator waits](C:/Users/benja/.codex/archived_sessions/rollout-2026-09-09T15-22-40-01a08655-b9be-7432-a9c9-7d89e54528b1.jsonl:977)
- [UI ownership and recovery](C:/Users/benja/.codex/sessions/2026/09/11/rollout-2026-09-11T16-59-16-01a090fa-e3b8-7300-a5bf-b001d79b7675.jsonl:3975)
- [Transfer test scope](C:/Users/benja/.codex/archived_sessions/rollout-2026-09-10T17-59-33-01a08c0b-b92e-7631-8fbf-668e0c6a76eb.jsonl:686)
