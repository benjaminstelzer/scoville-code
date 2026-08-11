# Scoville optimization history

As of 2026-08-11, the six Scoville Skills retain the following development
history:

| Skill | Optimization and evaluation runs | Benchmark case executions |
| --- | ---: | ---: |
| Scoville Brainstorm | 182 | 584 |
| Scoville Code | 305 | 1,394 |
| Scoville UI | 131 | 513 |
| Scoville Scribe | 181 | 753 |
| Scoville Plan | 180 | 792 |
| Scoville Handoff | 222 | 620 |
| **Family total** | **1,201** | **4,656** |

Runs are retained optimization or evaluation records, not only final passing
rows. Diagnostic attempts, rejected candidates, infrastructure stops, and
benchmark-contract investigations remain counted because they were part of
reaching the released Skills. Case executions are target-model benchmark rows;
activation, optimizer-only, installed-host, and live-integration calls may be
tracked separately in each Skill's detailed evidence.

The Code, UI, Scribe, and Plan counts come from the frozen four-Skill aggregate
snapshot with SHA-256
`1270F95CF9777EBC8E97151E37DFA5525D3E2DB8A6F0163DFBD71C8DA395A781`.
Handoff and Brainstorm retain their later per-run ledgers in their respective
repositories. Each Skill's benchmark report defines its scoring, qualification,
token measures, and limits.

