---
format_version: 1
id: ADR-0002
status: accepted
created: 2026-08-31
accepted: 2026-08-31
scope: skills/maintainability
supersedes: ADR-0001
---

# Checkstyle-Wert von 2.000 Zeilen verwenden

## Decision

Scoville Code verwendet für handgeschriebene Quelldateien grundsätzlich eine
Obergrenze von 2.000 physischen Zeilen. Strengere Projektregeln gehen weiterhin
vor. Die bestehenden Ausnahmen und Schutzregeln gegen Metrik-Gaming sowie
ungefragte Bestandsrefactorings bleiben erhalten.

## Problem

Die zuvor ausgewählte Obergrenze von 1.000 Zeilen entspricht nicht mehr der
aktuellen Nutzerentscheidung. Gewünscht ist der konfigurierbare Standardwert von
2.000 Zeilen aus Checkstyle FileLength.

## Drivers

- Der Nutzer hat 2.000 Zeilen ausdrücklich ausgewählt.
- Checkstyle dokumentiert 2.000 als Standardwert seiner konfigurierbaren
  FileLength-Prüfung.
- Die Dateigröße bleibt ein Wartbarkeitssignal. Kohäsion, Projektvorrang und
  konkrete Ausnahmen entscheiden weiterhin über eine sinnvolle Aufteilung.
- Ein einzelner Werkzeugwert wird nicht als universeller Industriestandard
  dargestellt.

## Considered alternatives

- Die bisherige Grenze von 1.000 Zeilen beibehalten. Das widerspricht der neuen
  Nutzerentscheidung.
- Jede Projektgrenze durch 2.000 ersetzen. Das würde strengere verbindliche
  Projektkonventionen übergehen.
- Die Größenregel vollständig entfernen. Das würde den zuvor bestätigten
  Wartbarkeitsfehlmodus wieder ungeregelt lassen.

## Consequences

Handgeschriebene Dateien zwischen 1.001 und 2.000 Zeilen benötigen allein wegen
der Scoville-Vorgabe keine Ausnahme mehr. Eine klare fachliche Teilung kann
trotzdem früher sinnvoll sein. Bestehende Dateien über 2.000 Zeilen werden nicht
automatisch refaktoriert. Historische Plan- und Entscheidungsunterlagen behalten
den damals gültigen Wert von 1.000 Zeilen.

## Confirmation

Die aktive Change-Referenz und aktuelle Dokumentation müssen 2.000 an den für
die Regel relevanten Stellen nennen. Grenzfälle müssen oberhalb von 2.000
liegen. Paket-, JSON-, Link- und Synchronisierungsprüfungen müssen bestehen.
Fable prüft den fertigen Skill anschließend lesend.

## Revisit when

Der Nutzer wählt einen anderen Wert, ein verbindliches Projektlimit geht vor
oder reale Einsätze zeigen, dass die Grenze die gewünschte Wartbarkeitswirkung
nicht erreicht.
