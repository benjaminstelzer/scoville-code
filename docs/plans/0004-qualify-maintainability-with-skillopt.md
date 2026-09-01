---
format_version: 1
id: PLAN-0004
status: completed
created: 2026-09-01
updated: 2026-09-01
---

# Wartbarkeitsregeln mit SkillOpt qualifizieren

## Goal

Der aktuelle Scoville-Code-Kandidat wird unter der lokalen SkillOpt-Studio-
Isolation gegen das letzte veröffentlichte Kontrollpaket geprüft. Ein
eingefrorener 8/4/4-Benchmark misst die neuen Wartbarkeitsentscheidungen und
bestehende Routing-Grenzen. Die Qualifikation endet mit einer hashgebundenen
Promotionsentscheidung und einem einmaligen Holdout nur für berechtigte Arme.

## Non-goals

- Kein Commit, Push, GitHub-Release oder Update öffentlicher Tags.
- Keine Installation eines generierten Kandidaten in Codex oder Claude.
- Keine automatische Übernahme eines SkillOpt-Vorschlags aufgrund eines
  Gesamtwerts oder geringerer Tokenzahl.
- Keine Wiederholung, Umschreibung oder Neuprägung eines verbrauchten
  Holdouts.
- Keine Änderung anderer Scoville-Skills oder ihrer Benchmarks.

## Work items

### W-001 Pakete und ausführbaren Benchmark einfrieren

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0003]
Outcome: Kontrolle und Kandidat liegen mit einem validierten 16-Fälle-Benchmark und vollständigen Hashbindungen isoliert im SkillOpt Studio vor.
Acceptance: Das Kontrollpaket stammt aus dem letzten veröffentlichten Tag. Der Kandidat entspricht dem aktuellen Fünf-Dateien-Paket. Train Validation und Test enthalten 8 4 und 4 eindeutige Fälle. Prediction und Scoring sind getrennt. Die neue Konfiguration verwendet die aktuelle Studio-Revision sowie Sol xhigh als Optimierer und Terra medium als Zielmodell. Preflight meldet ready.
Steps:
1. Aktuellen Studio-Vertrag und das letzte veröffentlichte Kontrollpaket auflösen.
2. Beide vollständigen Pakete in getrennte schreibgeschützte Snapshots kopieren.
3. Zehn bestehende Fälle ausführbar machen und sechs Gegenproben ergänzen.
4. Benchmark und Pakete hashen und mit einer neuen Konfiguration binden.
5. Statische Benchmark-Prüfung und tokenfreien Preflight ausführen.
Evidence: [GitHub Release and local tag v1.0.17 resolve to commit dff5c4101f4a93ade848dacc17366eb9d566f113, Control package tree SHA256 is c499559a0478414973bcaefa1b6ef00500f5df32b705aea2c23bd96e710f6988, Candidate package tree SHA256 is 1a5d6608c06c627b130256ab9483e677c41524b1e2f62d29df8da6d0098bacbf, Benchmark validation passed with 8 Train 4 Validation 4 Test and 16 unique IDs, Prediction inspection found no scorer object or expected string leakage, Benchmark lock binds 14 files and Test seal binds 4 items, Control and candidate preflights reported ready on SkillOpt ba820b500f9da96685cf2780c7dc85ed4eb6563e, Both preflights confirmed Terra medium Sol xhigh global Skill isolation and disabled network, Both preflights reported test_payload_opened false]

### W-002 Offene A/B-Qualifikation ausführen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0003]
Outcome: Kontrolle und Kandidat besitzen vergleichbare offene Verhaltensnachweise und eine begründete Entscheidung über einen möglichen Optimierungslauf.
Acceptance: Ein Validation-Smoke besteht. Beide Arme laufen auf Train und Validation. Validation wird mit drei unabhängigen Run-IDs pro Arm ausgeführt. Jeder Lauf dokumentiert agent_ok hard behavior_hard efficiency_hard fehlgeschlagene Invarianten Befehle und Provider-Tokens. Ein bestätigter Skill-Fehler löst höchstens einen konservativen Trainingslauf aus. Ein Vorschlag bleibt ohne vollständige offene Gates unpromotet.
Steps:
1. Einen einzelnen Validation-Fall pro Arm als Verkabelungsprüfung ausführen.
2. Train und Validation für Kontrolle und Kandidat mit frischen Run-IDs ausführen.
3. Validation je Arm dreimal unabhängig wiederholen und Stabilität vergleichen.
4. Fehler als Skill Benchmark oder Infrastruktur klassifizieren.
5. Nur bei bestätigtem Skill-Fehler einen konservativen Trainingslauf und erneute offene A/B-Prüfung ausführen.
Evidence: [Initial V1 smokes were retained with agent_ok false after an invalid Studio refresh token, Studio authentication was refreshed once and the Sol xhigh optimizer smoke passed, V1 through V5 preserve all observed benchmark and infrastructure failures as separate run evidence, V4 and byte-identical V5 Train predictions passed 8 of 8 hard gates for both arms, V6 preflight reported ready with 8 Train 4 Validation 4 sealed Test and test_payload_opened false, Six independent V6 Validation runs completed with agent_ok true, Control and candidate each passed 3 of 4 in all three Validation repetitions, Every Validation failure was maint-narrow-security-fix on expected_json_subset only, Both arms applied and tested the narrow security fix but omitted the scoped oversized-file concern, One conservative SkillOpt step completed with 22 calls and 1124603 tokens, SkillOpt rejected its 10690-character proposal after Selection remained 3 of 4, Best origin remained initial_skill with zero accepted edits, Normalized best Skill bytes match the input candidate exactly]

### W-003 Promotionsentscheidung und Holdout abschließen

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: [ADR-0003]
Outcome: Der berechtigte Kandidat und die Kontrolle besitzen einmalige Holdout-Evidenz oder der Holdout bleibt wegen nicht bestandener offener Gates nachweislich versiegelt.
Acceptance: Nur offen qualifizierte Arme werden je einmal mit valid_unseen ausgeführt. Testbytes und Gold bleiben vor der Gate-Entscheidung ungeöffnet. Rohergebnis und mögliche Benchmark-Adjudikation bleiben getrennt. Der exakte Kandidaten-Hash wird als qualifiziert abgelehnt oder promotionsfähig dokumentiert. Statische Skill- Plan- JSON- Link- Diff- und Paketsynchronisierungsprüfungen werden danach mit ihren Grenzen berichtet.
Steps:
1. Offene Gates und Hashbindungen als Holdout-Berechtigung prüfen.
2. Kontrolle und berechtigten Kandidaten je einmal mit valid_unseen ausführen.
3. Rohe Fehler ohne Retry Reminting oder Gold-Änderung klassifizieren.
4. Qualifikationsentscheidung und Nachweisgrenzen im Repository dokumentieren.
5. Finale lokale Prüfungen ausführen und den Plan abschließen.
Evidence: [No arm passed every open hard gate and Holdout eligibility was denied, V6 run inspection found zero valid_unseen executions, V6 Test seal remains sealed with 4 items and SHA256 3afcdc76e922d69a18119e43c448fa94f5edc10be56a5348c275fbf23c3e78e4, Machine-readable evidence records outcome not_qualified and zero accepted edits, Benchmark evidence documents the stable failure and withheld Holdout, Canonical snapshot Codex and Claude packages match across all 5 files, Skill validation passed for canonical Codex and Claude packages, Evaluation and qualification JSON parsed with expected counts and outcomes, Local Markdown link inspection passed across 16 files, Plan profile validation passed with 4 plans 6 work items and 3 decisions, Git diff check passed with only a line-ending warning]
