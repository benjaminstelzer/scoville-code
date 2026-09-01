---
format_version: 1
id: ADR-0003
status: accepted
created: 2026-09-01
accepted: 2026-09-01
scope: skills/evaluation
---

# Wartbarkeitsregeln mit SkillOpt qualifizieren

## Decision

Die aktuellen Wartbarkeitsregeln werden mit einem eingefrorenen A/B-Vergleich
im lokalen SkillOpt Studio qualifiziert. Das letzte veröffentlichte Paket dient
als Kontrolle und der aktuelle Fünf-Dateien-Stand als Kandidat. Der Benchmark
verwendet 16 Fälle mit 8 Train-, 4 Validation- und 4 versiegelten
Holdout-Fällen. Ein Optimierungsvorschlag darf nur nach vollständigem Bestehen
der offenen harten Gates und des einmaligen Holdouts übernommen werden.

## Problem

Die statischen Prüfungen und unabhängigen Reviews belegen die Formulierung und
Paketsynchronisierung. Sie belegen nicht, dass ein Zielmodell die neuen Regeln
bei Grenzfällen zuverlässig anwendet oder bestehende Routing- und
Validierungsentscheidungen beibehält.

## Drivers

- Der Nutzer hat den beschriebenen SkillOpt-Testplan zur Umsetzung ausgewählt.
- Die neuen Regeln enthalten Prioritäten, Ausnahmen und negative Grenzen, die
  ein reiner Textvergleich nicht beweist.
- Kontrolle und Kandidat müssen dieselben Aufgaben unter derselben isolierten
  Modellkonfiguration erhalten.
- Holdout-Inhalte dürfen offene Iteration oder Optimierung nicht beeinflussen.
- Harte Verhaltensregeln gehen vor Token- oder Aufrufreduktionen.

## Considered alternatives

- Nur die zehn deklarativen JSON-Fälle statisch prüfen. Das belegt keine
  Modellausführung.
- Sofort einen SkillOpt-Trainingslauf starten. Das würde Diagnose und
  Veränderung vermischen.
- Nur den aktuellen Kandidaten ohne Kontrolle ausführen. Das könnte bestehende
  Fehler und neu eingeführte Regressionen nicht sauber unterscheiden.
- Den Holdout nach einem Fehlschlag wiederholen oder umschreiben. Das würde die
  unabhängige Promotionsgrenze aufheben.

## Consequences

Die Qualifikation benötigt eingefrorene Pakete, getrennte offene und versiegelte
Fälle sowie mehrere unabhängige Validation-Läufe. Ein generierter Kandidat
bleibt zunächst ein Vorschlag. Ein realer Skill-Fehler kann einen konservativen
Trainingslauf auslösen. Benchmark- oder Infrastrukturfehler bleiben als rohe
Evidenz erhalten und rechtfertigen keine nachträgliche Gold-Anpassung.

## Confirmation

Ein Manifest muss Paket- und Benchmark-Hashes, Modellrollen, SkillOpt-Revision
und Splitgrößen binden. Preflight, offene A/B-Läufe und drei unabhängige
Validation-Läufe pro Arm müssen ihre harten Gates ausweisen. Der versiegelte
Holdout wird erst danach je Arm einmal über `valid_unseen` ausgeführt. Nur der
exakt geprüfte Kandidaten-Hash darf als promotionsfähig gelten.

## Revisit when

Der lokale Studio-Vertrag, die Zielmodelle, die SkillOpt-Revision oder die
Wartbarkeitsregeln ändern sich. Ein neuer Qualifikationszyklus benötigt neue
Run-IDs und einen neuen unangetasteten Holdout.
