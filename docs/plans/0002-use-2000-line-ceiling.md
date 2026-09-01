---
format_version: 1
id: PLAN-0002
status: completed
created: 2026-08-31
updated: 2026-09-01
---

# Dateigrenze auf 2.000 Zeilen anheben

## Goal

Die aktuelle Scoville-Code-Regel, ihre Evaluationsdefinitionen und die
öffentliche Dokumentation verwenden den vom Nutzer ausgewählten
Checkstyle-Wert von 2.000 Zeilen. Das kanonische Paket und die lokalen Codex-
und Claude-Kopien stimmen überein. Fable prüft danach den fertigen Skill.

## Non-goals

- Keine Änderung der übrigen Wartbarkeitsregeln oder ihrer Ausnahmen.
- Keine Umschreibung historischer abgeschlossener Planinhalte.
- Kein SkillOpt-Lauf, Benchmark, Commit, Push oder GitHub-Release ohne eigenen
  Auftrag.
- Keine Änderung an Fluid Base oder anderen Scoville-Skills.

## Work items

### W-001 Neue Dateigrenze vollständig übernehmen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0002]
Outcome: Der aktive Scoville-Code-Skill verwendet 2.000 Zeilen mit unveränderten Prioritäten und Ausnahmen und liegt geprüft in allen lokalen Paketkopien vor.
Acceptance: Aktive Regel und aktuelle Dokumentation verwenden 2.000. Grenzfälle oberhalb der Grenze bleiben entscheidungsscharf. Historische Unterlagen bleiben als Historie erhalten. Skill-, JSON-, Link-, Plan-, Diff- und Paketsynchronisierungsprüfungen bestehen. Fable prüft das fertige Paket und bestätigte Fehler sind behoben. Nicht ausgeführte SkillOpt- oder Verhaltenstests werden benannt.
Steps:
1. Aktive Regel, Fälle und aktuelle Dokumentation auf 2.000 Zeilen angleichen.
2. Kanonisches Paket sowie Codex- und Claude-Kopie prüfen und synchronisieren.
3. Fable den fertigen Skill und die geänderten Fälle lesend prüfen lassen.
4. Bestätigte Fehler korrigieren und die betroffenen Prüfungen wiederholen.
5. Nachweise eintragen und Plan abschließen.
Evidence: [Active package contains one 2000-line declaration and no active 1000-line wording, Evaluation JSON parsed with 10 unique cases and the explicit oversized-file fixtures 24000 2400 and 2300 all exceed the 2000-line ceiling, Skill validation passed for canonical Codex and Claude packages, All 5 package files match across canonical Codex and Claude roots, Local Markdown link inspection passed across 13 files, Fable read-only review found the active rule and cases consistent, Fable evidence-wording finding corrected in ADR-0002, Change reference contains no line longer than 100 characters, SkillOpt and model-behavior tests were not run]
