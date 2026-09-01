---
format_version: 1
id: ADR-0001
status: superseded
created: 2026-08-31
accepted: 2026-08-31
scope: skills/maintainability
superseded_by: ADR-0002
---

# Wartbare Datei- und Modulstruktur als Code-Standard ergänzen

## Decision

Scoville Code erhält sprachunabhängige Wartbarkeitsregeln in der vorhandenen
Change-Referenz. Handgeschriebene Quelldateien haben grundsätzlich höchstens
1.000 physische Zeilen. Strengere Projektregeln gehen vor, kohärente Ausnahmen
werden begründet. Ergänzt werden fachliche Datei- und Verzeichnisgrenzen,
Abhängigkeitsrichtung, Generator-/Runtime-Grenzen, Zustands- und
Ressourcenbesitz sowie Duplikation ohne spekulative Abstraktion.

## Problem

Der aktuelle Skill schützt Umfang, Zuständigkeit, Grenzsemantik und Nachweise,
formuliert aber keine konkrete Dateiobergrenze und zu wenig handlungsnahe
Regeln für Datei-, Verzeichnis- und Modulstruktur. Dadurch können große
Sammeldateien, flacher Subsystem-Wildwuchs oder rein metrische Aufteilungen die
vorhandenen allgemeinen Regeln passieren.

## Drivers

- Die Nutzerentscheidung verlangt die 1.000-Zeilen-Grenze mit einer Ausnahme,
  wenn keine sinnvolle Teilung möglich ist.
- Adapter, Plugins und Datenimport-Funktionen sollen auffindbare fachliche
  Bereiche erhalten. Sprachliche Import-Anweisungen sind davon verschieden.
- Fluid Base zeigt nützliche Verantwortungsgrenzen, aber auch große generierte
  und handgeschriebene Dateien. Seine konkrete PHP-/Trait-Struktur ist keine
  universelle Vorlage.
- Professionelle Primärquellen stützen Kohäsion, kleine überprüfbare Änderungen,
  nachvollziehbare Abhängigkeiten und reproduzierbare Prüfungen. Sie belegen
  keinen universellen Dateigrenzwert.
- Fables Planprüfung und eigene Empfehlung verlangen dieselbe Kalibrierung und
  warnen vor Doppelregeln sowie einer langen Lehrbuch-Checkliste.

## Considered alternatives

- Keine konkrete Grenze ergänzen. Das lässt den ausdrücklich genannten
  Fehlmodus ungelöst.
- Jede Datei über 1.000 Zeilen zwingend teilen. Das beschädigt generierte,
  fremdverwaltete oder fachlich untrennbare Inhalte und erweitert kleine Fixes.
- Eine neue allgemeine Architektur-Referenz oder feste Layer-Struktur einführen.
  Das erhöht Lade- und Pflegekosten und übergeht Projektkonventionen.
- Nur eine Tool-Regel empfehlen. Tool-Defaults unterscheiden sich und besitzen
  ohne Projektkonfiguration keine Autorität.

## Consequences

Neue oder substanziell bearbeitete handgeschriebene Dateien werden früher an
fachlichen Grenzen geteilt. Überschreitungen brauchen eine konkrete Begründung,
lösen aber kein automatisches Bestandsrefactoring aus. Projektregeln,
Zielversionen und Runtime-Verträge bleiben vorrangig. Die Change-Referenz wird
größer, deshalb bleibt die Ergänzung auf entscheidungsrelevante Regeln und Fälle
begrenzt. Historische Benchmarks belegen das geänderte Paket nicht.

## Confirmation

Die Referenz nennt Grenze, Vorrang, Ausnahmen und verbotene Metrik-Tricks. Fünf
Evaluationsdefinitionen decken die benannten Grenzfälle ab. Paketvalidierung,
JSON-Prüfung, Linkprüfung, Diff-Sichtung und Bytevergleich der lokalen Kopien
bestätigen nur Struktur und Synchronisierung. Ein Verhaltenstest muss getrennt
als solcher durchgeführt und berichtet werden.

## Revisit when

Reale Projekte zeigen wiederholt, dass die Grenze sinnvolle Änderungen
verhindert, Ausnahmen beliebig werden, die zusätzliche Referenz die
Entscheidungsqualität verschlechtert oder ein projektnatives Maß die Aufgabe
nachweislich besser löst.
