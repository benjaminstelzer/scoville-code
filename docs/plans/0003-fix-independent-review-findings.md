---
format_version: 1
id: PLAN-0003
status: completed
created: 2026-09-01
updated: 2026-09-01
---

# Befunde der unabhängigen Prüfung beheben

## Goal

Die drei bestätigten Präzisionsfehler aus den unabhängigen Prüfungen sind im
aktuellen Scoville-Code-Skill und seinen Nachweisen behoben. Das kanonische
Paket sowie die lokalen Codex- und Claude-Kopien stimmen überein. Fable und ein
frischer SOL-Agent prüfen den fertigen Stand anschließend unabhängig.

## Non-goals

- Keine Erweiterung um optionale Evaluationsfälle ohne bestätigten Defekt.
- Keine weitere Änderung der Wartbarkeitsregeln oder der 2.000-Zeilen-Grenze.
- Kein SkillOpt-Lauf, Benchmark, Commit, Push oder GitHub-Release.
- Keine Änderung an Fluid Base oder anderen Scoville-Skills.

## Work items

### W-001 Bestätigte Prüfungsbefunde korrigieren und erneut prüfen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0002]
Outcome: Die Evidenz beschreibt die zehn Fälle korrekt. Die Ausnahmen sind erkennbar beispielhaft und der Runtime-Fall belegt einen tatsächlichen fehlenden Startpfad.
Acceptance: Alle drei bestätigten Befunde sind mit kleinen bedeutungserhaltenden Änderungen behoben. Skill-, JSON-, Link-, Plan-, Diff- und Paketsynchronisierungsprüfungen bestehen. Fable und ein frischer SOL-Agent prüfen denselben fertigen Stand unabhängig. Bestätigte Restfehler werden behoben. Nicht ausgeführte SkillOpt- oder Verhaltenstests werden benannt.
Steps:
1. Evidenzsatz, Ausnahmenformulierung und Runtime-Registrierungsfall präzisieren.
2. Kanonisches Paket sowie Codex- und Claude-Kopie prüfen und synchronisieren.
3. Statische Prüfungen und die gezielten Grenzfallprüfungen ausführen.
4. Fable und einen frischen SOL-Agenten denselben fertigen Stand prüfen lassen.
5. Bestätigte Restfehler korrigieren, Nachweise eintragen und Plan abschließen.
Evidence: [Three specified review findings corrected, Evaluation JSON parsed with 10 unique cases and numeric fixtures 24000 2400 2300 all exceed 2000, Skill validation passed for canonical Codex and Claude packages, All 5 package files match across canonical Codex and Claude roots, Local Markdown link inspection passed across 14 files, Plan profile validation passed with 3 plans 3 work items and 2 decisions, Git diff check passed with only a line-ending warning, Edited prose passed the requested punctuation checks, Initial independent recheck found one evidence-scope defect and one stale update date, Both residual findings were corrected, Final Fable follow-up reported no required findings, Final SOL follow-up reported no required findings, SkillOpt and model-behavior tests were not run]
