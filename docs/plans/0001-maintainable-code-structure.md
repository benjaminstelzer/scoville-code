---
format_version: 1
id: PLAN-0001
status: completed
created: 2026-08-31
updated: 2026-08-31
---

# Wartbare Datei- und Modulstruktur in Scoville Code

## Goal

Scoville Code soll konkrete, überprüfbare Regeln für wartbaren Code enthalten.
Der Auftrag nennt höchstens 1.000 Zeilen pro Datei mit begründeten Ausnahmen,
sinnvolle Verzeichnisse für Adapter, Plugins und Import-Funktionen sowie logisch
benannte Dateien. Weitere relevante Lücken werden ergänzt, bereits vorhandene
Regeln bleiben an ihrem bisherigen Ort. Ein zusätzlicher Nutzerauftrag verlangt
den Abgleich mit professionellen sprachunabhängigen Entwicklungspraktiken.
Fable prüft den damit ergänzten Plan, bevor der
Skill, seine Tests, Dokumentation oder installierten Kopien geändert werden.

Die Umsetzung betrifft das kanonische Repository
`Z:\Projekts\AI\scoville-code-anti-ai-slop` und anschließend die vorhandenen
lokalen Scoville-Code-Kopien für Codex und Claude. Eine Veröffentlichung ist
nicht Teil dieses Auftrags.

**Geprüfter Ausgangspunkt, 2026-08-31**

- Das Code-Repository steht ohne vorgelagerte Änderungen auf `dff5c41`.
- Core und installierter Codex-Core sind bytegleich. Der Skill hat bereits
  Regeln für kanonische Zuständigkeit, Umfang, Risiko, Fehlerbehandlung und
  angemessene Tests. Konkrete Größen- und Strukturregeln fehlen.
- `references/change-workflow.md` fordert bestehende Namenskonventionen und
  kleine kohärente Änderungen, definiert aber weder Dateigrößen noch
  Verzeichnisgrenzen, Funktionszuschnitt oder Abhängigkeitsrichtung.
- Fluid Base wurde ausschließlich gelesen. Der in seinem `AGENTS.md` genannte
  Projektpfad ist `C:\Users\benja\Desktop\DIVI5 Plugin`. Dieser Checkout und
  `Z:\Projekts\AI\divi-5-fluid-base` stehen auf `46ee6e9b`. Die unversionierten
  Desktop-Verzeichnisse `research/` und `workspace/` bleiben unangetastet.

**Was Fluid Base tatsächlich zeigt**

Die Beispiele stammen aus `src/divi-5-fluid-base/`, der Namenskonvention in
`docs/plugin-specific/file-naming-convention.md` und dem Developer Guide.

| Beobachtung | Beleg | Übertragbares Prinzip |
| --- | --- | --- |
| Generisches Admin-Framework getrennt vom Produkt | `includes/dynamitec-admin-framework/` und `assets/js/dynamitec-admin-framework/` gegenüber `assets/js/admin/` | Framework und produktspezifische Adapter haben getrennte Zuständigkeiten und Verzeichnisse. |
| Unterschiedliche Plattformeditionen getrennt | `includes/traits/edition/divi4/`, `includes/traits/edition/divi5/`, `divi5fb-trait-edition-adapters.php` | Editions- und Integrationsdetails bleiben hinter einer klaren gemeinsamen Aufrufgrenze. |
| Konfiguration, Schema und Spezifikationen auffindbar | `includes/config/`, `includes/schema/`, `includes/overrides/` | Dateien und Verzeichnisse folgen ihrer tatsächlichen Verantwortung. |
| Dateien tragen fachliche Namen | `divi5fb-trait-frontend-css-cache.php`, `divi5fb-trait-override-sync-jobs.php`, `dynadm-scroll-state.js` | Namen benennen Aufgabe und fachlichen Bereich statt nummerierter Dateiteile. |
| Import/Export ist ein konkreter Funktionsbereich | `includes/traits/divi5fb-trait-import-export.php` | Das Beispiel ist eine eigene Datei, kein eigenes Import-Verzeichnis. Sprachliche Import-Anweisungen sind nicht gemeint. |
| Generierte Inhalte können groß sein | `divi5fb-config-setup-reset-presets.php`, 28.697 Zeilen, nennt seinen Generator | Quelldaten und Generator bearbeiten, erzeugte Ergebnisse nicht zum Erfüllen einer Zeilenzahl aufteilen. |
| Eine gute Grundstruktur garantiert keine kleinen Dateien | 17 von 115 untersuchten PHP-/JS-/CSS-Dateien über 1.000 Zeilen, ohne Vendor und minifizierte Dateien | Zeilenzahl ist ein Prüfsignal, kein Beleg für Fehler oder eine sinnvolle konkrete Aufteilung. |

Die zweite große Datendatei `divi5fb-config-divi-default-baselines.php` hat
14.099 Zeilen und Herkunftsmetadaten. Der lesbare Runtime-Code
`assets/js/divi5fb-runtime.js` hat 4.066 Zeilen. Diese Bestandsaufnahme ist kein
Refactoring-Auftrag und kein Urteil, dass jede dieser Dateien geteilt werden
sollte. Produktpräfixe, PHP-Traits und konkrete Ordnernamen werden nicht zum
universellen Scoville-Standard erklärt.

**Vorgesehener Regelumfang**

| Bereich | Bereits vorhanden | Ergänzung oder Präzisierung |
| --- | --- | --- |
| Dateigröße | Keine konkrete Grenze | Handgeschriebene Quelldateien grundsätzlich höchstens 1.000 physische Zeilen in normaler Projektformatierung. Kein Zielwert und kein Schönrechnen durch Entfernen von Kommentaren oder Zusammenpressen. Sinnvolle fachliche Teilung früher vornehmen. |
| Ausnahmen und Bestand | Kleine Änderungen, kein ungefragter Umbau | Generierte, minifizierte und fremdverwaltete Dateien sind nicht nach der Grenze zu zerlegen. Bei einer kohärenten handgeschriebenen Datei über 1.000 Zeilen begründen, warum eine konkrete Teilung Kopplung erhöht, Invarianten zerreißt oder mit einem notwendigen Format kollidiert. Bei eng begrenzten Bestandskorrekturen keine ungefragte Großaufteilung. |
| Verzeichnisse | Bestehende Architektur respektieren | Tatsächlich implementierte Adapter-, Plugin- und Datenimport-Subsysteme in eigene aussagekräftige Verzeichnisse oder vorhandene gleichwertige Projektbereiche legen. Bestehende kleine kohärente Ein-Datei-Funktionen nicht nur für eine schematische Ordnerstruktur verschieben. Keine leeren Zukunftsordner. |
| Import-Begriff | Nicht behandelt | Datenimporte und Integrationen sind Strukturgrenzen. Sprachliche `import`, `use` oder `require`-Anweisungen bleiben nach der bestehenden Sprach- und Toolkonvention beim konsumierenden Modul. Keine Ordnerpflicht pro Import-Anweisung. |
| Namen und Zuständigkeiten | Namenskonventionen übernehmen | Ein nachvollziehbarer fachlicher Verantwortungsbereich pro Datei oder Modul. Bestehende präzise Namen übernehmen. Keine unspezifischen Sammeldateien, nummerierten Fragmente oder künstlichen Ein-Funktions-Dateien. |
| Funktionen und Kontrollfluss | Nur allgemeine Kohärenz | Funktionen auf eine verständliche Aufgabe begrenzen, versteckte Nebenwirkungen und tiefe Verschachtelung reduzieren. Kleine Hilfsfunktionen nur für erkennbare Begriffe oder wiederverwendete Logik. Keine universelle zusätzliche Zeilenquote pro Funktion. |
| Abhängigkeiten und Schnittstellen | Kanonischer Owner, keine Parallelpfade | Abhängigkeitsrichtung sichtbar halten, neue Zyklen und Zugriffe auf fremde interne Dateien vermeiden. Kleine öffentliche Moduloberflächen. Integrationsdetails gehören in Adapter, fachliche Regeln nicht in generische Framework-Helfer. Keine automatische neue Layer-Architektur. |
| Zustand und Seiteneffekte | Erhalt relevanter Zustandssemantik | Veränderlichen Zustand einem klaren Owner geben, versteckte globale Kopplung vermeiden. Ein-/Ausgabe und Infrastruktur von berechenbarer Fachlogik trennen, soweit dadurch echte Test- oder Wartungsgrenzen entstehen. Keine allgemeine Pflicht zu DI-Containern. |
| Verträge und Konfiguration | Bedeutung an Grenzen erhalten | Neue Einheiten und Schemas an tatsächlichen Grenzen explizit machen. Fachliche Regeln, Konfiguration und begründungsbedürftige Konstanten nicht mehrfach auseinanderlaufend pflegen. Bestehende allgemeine Grenzregeln nicht duplizieren. |
| Ressourcen | Fehler nicht verschlucken, kein falscher Erfolg | Wer Handles, Listener, Timer oder Verbindungen anlegt, braucht einen klaren Owner für die Freigabe. Retry-, Abbruch- und Timeout-Mechanismen nur ergänzen, wenn Auftrag, bestehender Vertrag oder konkrete Fehlerspur sie verlangt. |
| Duplikation und Abstraktion | Spekulative Helfer und Schichten bereits verboten | Belegte Duplikation fachlicher Logik im kanonischen Owner zusammenführen. Keine Abstraktion vor einem zweiten realen Nutzer oder einer belegten gemeinsamen Invariante. |
| Generierte Quellen und Runtime | Bestehende Werkzeuge bevorzugen | Handgeschriebene Quellen von Vendor, generierten Ergebnissen und Build-Artefakten trennen. Generator statt Ausgabe ändern. Sprachsyntax und Bibliotheks-APIs müssen zur deklarierten Zielversion passen. |
| Nachvollziehbare Abhängigkeiten und Builds | Nur teilweise konkret | Vorhandene Manifeste, Lockfiles und Build-Einstiegspunkte respektieren. Versionen berührter Abhängigkeiten nachvollziehbar halten. Keine automatische Einführung eines Paketmanagers oder einer CI-Plattform. |
| Tests und Dokumentation | Proportionale, beobachtete Prüfungen | Nach Datei- oder Modulaufteilung reale Aufrufer, Import-/Autoload- und Startpfade prüfen. Allgemeine Test-, Lint- und Dokumentationsregeln nicht duplizieren. |

Die Regeln bleiben nachrangig zu expliziten Aufträgen, Runtime-Anforderungen und
verbindlichen Projektkonventionen. Sie erweitern weder Änderungsbefugnisse noch
automatisch die Reichweite einer Fehlerkorrektur. Strukturelle Änderungen werden
weiterhin nach dem bestehenden Risikomodell beurteilt.

**Abgleich mit professionellen Praktiken, geprüft am 2026-08-31**

Der folgende Abgleich ist eine Synthese der genannten Primärquellen, keine
Behauptung, dass alle Unternehmen denselben Prozess oder dieselbe Architektur
verwenden. Die dort genannten Werkzeuge werden hier nicht installiert.

- Google prüft unter anderem Entwurf, Funktion, Komplexität, Tests, Namen und
  notwendige Dokumentation. Persönliche Stilpräferenzen sind von verbindlichen
  Vorgaben zu trennen. Das stützt konkrete Review-Kriterien statt zusätzlicher
  pauschaler Zahlenquoten. Gelesen wurden die Abschnitte Complexity bis Context
  in [What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html).
- Googles [Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html)
  fordert zusammenhängende kleine Änderungen mit zugehörigen Tests und trennt
  umfangreiche Refactorings von fachlichen Änderungen. Die dort diskutierten
  Zeilenzahlen betreffen Änderungsumfänge, nicht die Größe einer Quelldatei.
  Gelesen wurden What is Small, Separate Out Refactorings und Keep related test
  code in the same CL.
- DORA beschreibt Auffindbarkeit, Wiederverwendung und änderbare Abhängigkeiten
  als Wartbarkeitsmerkmale. Herkunft und genaue Versionen von Abhängigkeiten
  sowie reproduzierbare Builds sind konkrete Ergänzungen für diesen Plan.
  Gelesen wurden die Kriterien und der Implementierungsabschnitt von
  [Code maintainability](https://dora.dev/capabilities/code-maintainability/).
- Automatisierte Builds und schnelle Tests liefern laufend Rückmeldung zu
  Änderungen. Für Scoville folgt daraus die Nutzung vorhandener projektweiter
  Checks und ein ehrlicher Umgang mit fehlschlagenden Prüfungen, keine neue
  Berechtigung zum Merge oder Deployment. Gelesen wurden Implementierung und
  typische Fehler in [DORA Continuous integration](https://dora.dev/capabilities/continuous-integration/).
- Eine universelle geeignete Dateigröße wird von der
  [ESLint-Dokumentation zu max-lines](https://eslint.org/docs/latest/rules/max-lines)
  ausdrücklich nicht behauptet. Die konfigurierbare Regel hat standardmäßig
  300 Zeilen, [Checkstyle FileLength](https://checkstyle.org/checks/sizes/filelength.html)
  dagegen 2.000. Gelesen wurden Begründung und Optionen beziehungsweise
  Properties. Die 1.000-Zeilen-Grenze ist daher die Nutzer-/Scoville-Vorgabe mit
  begründeten Ausnahmen, kein angeblich belegter Industriestandard.
- DORA beurteilt lose Kopplung daran, ob Änderungen und Tests unabhängig
  möglich sind, nicht am bloßen Einsatz einer bestimmten Technologie.
  Gelesen wurden Einleitung und Architekturabwägung in
  [Loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/).
  Übertragung auf diesen Skill: Verzeichnisgrenzen müssen echte Modulgrenzen
  abbilden. Eine Microservice-, Layer- oder Feature-first-Struktur wird nicht
  für alle Projekte vorgeschrieben.
- [NIST SSDF](https://csrc.nist.gov/projects/ssdf) integriert Sicherheit in den
  Entwicklungsprozess und verlangt eine risikoorientierte, anwendbare Auswahl
  statt einer blind abzuarbeitenden Checkliste. Gelesen wurden Overview,
  SSDF Practices und SSDF Use. Die
  [Publikationsübersicht](https://csrc.nist.gov/Projects/ssdf/publications)
  führt Version 1.1 als final und 1.2 als Entwurf. Für diesen Plan wird kein
  Entwurf als verbindlicher Standard behandelt. Die vorhandenen Code-Regeln zu
  Sicherheit und Fehlernachweisen bleiben bestehen.

**Umsetzung in einer professionellen Entwicklungsumgebung**

Als Synthese lassen sich drei Arten von Regeln unterscheiden:

| Regelart | Beispiele | Umgang im Skill |
| --- | --- | --- |
| Verbindlicher Projektvertrag | Zielversionen, öffentliche Schnittstellen, Sicherheits- und Datenregeln, festgelegte Formate | Bestehende Vorgaben erfüllen und betroffene Verträge prüfen. Nicht für eine Stilregel brechen. |
| Automatisierbare Projektkonvention | Formatter, Linter, Typprüfung, Build, Tests, konfigurierte Größenlimits | Vorhandene Werkzeuge nutzen. Ergebnisse genau benennen. Kein neuer universeller Tool-Stack. |
| Begründungspflichtiges Review-Urteil | Fachliche Kohärenz, sinnvolle Dateiaufteilung, notwendige Abstraktion, Ausnahmen von der 1.000-Zeilen-Grenze | Konkrete Auswirkungen und die Alternative prüfen. Nicht allein aus Dateinamen oder einer Metrik auf Qualität schließen. |

Ein entsprechender Ablauf besteht aus vereinbarten Projektregeln, einer kleinen
zusammenhängenden Änderung, passenden lokalen Prüfungen, fachlichem Review und
den bereits eingerichteten automatisierten Integrationsprüfungen. Umfangreiche
Umstrukturierungen werden sichtbar vom eigentlichen Fehler- oder Feature-Fix
getrennt. Der Skill folgt den vorhandenen Zuständigkeiten und Freigaben. Ein
externer Reviewer wird nicht für jede kleine Änderung neu vorgeschrieben.

**Fable-Abgleich vor der Umsetzung**

Fable 5 wurde mit hoher Denkleistung in einer persistenten, lesenden Sitzung
zweimal befragt. Das Backend meldete keinen konkreten aufgelösten Modellnamen.
Die Prüfung dauerte 139 Sekunden, die priorisierte Folgefrage 68 Sekunden.
Beide Antworten sind Beratung und weder Freigabe noch Verhaltenstest.

Die Planprüfung bezeichnete den Plan als umsetzungsreif ohne notwendige weitere
Nutzerentscheidung. Übernommen werden:

- Ein strengeres konfiguriertes Projektlimit geht der Scoville-Grenze vor.
- Ausnahmegründe sind Beispiele, keine geschlossene Liste.
- Vertrags-, Test- und Dokumentationsregeln werden nicht doppelt formuliert.
- Retry-, Abbruch- und Timeout-Regeln greifen nur bei bestehendem Auftrag,
  Vertrag oder konkretem Fehlerbild.
- Die Ergänzungen werden in vorhandene Abschnitte eingefaltet. Die bisherige
  Priorität von Sicherheit und Integrität vor Wartbarkeit bleibt unverändert.
- Belegte fachliche Duplikation wird berücksichtigt, ohne spekulative
  Abstraktion zu fördern.
- Die fünf Evaluationsdefinitionen behandeln generierte Großdatei,
  Metrik-Gaming, enge Bestandskorrektur, Datenimport versus Sprachimport und
  reale Aufrufer-/Startpfade nach einer Aufteilung.

Fables eigene Richtlinienempfehlung nennt dieselben Bereiche als Must-have.
Nur bedingt sinnvoll sind qualitative Funktionsaufteilung, Manifeste/Lockfiles,
neue Einheiten/Schemas und Retry-/Abbruchregeln. Nicht universell festgelegt
werden Funktionszeilen, Ordnerschablonen, DI-Container, Microservices,
Kommentardichte, Coverage-Quoten, konkrete Tool-Defaults, Pflicht-Reviewer oder
CI-Plattformen. Die Change-Referenz erhält ungefähr 25 bis 35 neue Zeilen. Die
Zahl 1.000 erscheint in der eigentlichen Regel genau einmal.

**Geplante Dateiverteilung**

- Die konkrete Anleitung kommt in die bereits vor Änderungen und Reviews
  geladene Referenz `scoville-code-anti-ai-slop/references/change-workflow.md`.
  Ein neues Referenzsystem oder eine zusätzliche Ladepflicht ist nicht nötig.
- Die neue Anleitung wird auf ungefähr 25 bis 35 Zeilen begrenzt und in die
  bestehenden Abschnitte eingefaltet. Die Review-Priorität bleibt unverändert.
- `SKILL.md` bleibt voraussichtlich unverändert. Nur eine tatsächlich nötige
  Verknüpfung darf ergänzt werden, ohne Aktivierungs- oder Risikoregeln zu ändern.
- `tests/evaluation-cases.json` erhält fünf Szenarien: eine generierte
  Großdatei, Metrik-Gaming, eine enge Bestandskorrektur, Datenimport versus
  Sprachimport sowie reale Aufrufer-/Startpfade nach einer Aufteilung. Sie
  werden als Definitionen, nicht als bereits
  bestandene Modelltests dokumentiert.
- README und Changelog beschreiben die Ergänzungen und grenzen historische
  Benchmark-Ergebnisse vom geänderten Paket ab. Alte Messungen werden weder
  neu zugerechnet noch überschrieben.
- Lokale Codex-/Claude-Kopien werden erst nach Fable-Abgleich und Prüfung des
  kanonischen Ergebnisses angeglichen. Unabhängige lokale Änderungen sind vorher
  zu prüfen und zu erhalten.

**Fragen an Fable vor der Umsetzung**

1. Bleibt die 1.000-Zeilen-Regel wirksam, ohne sinnlose Dateiteilung oder
   ungefragte Refactorings auszulösen?
2. Ist die Verzeichnisregel dem Nutzerwunsch und der tatsächlich gelesenen
   Fluid-Base-Struktur angemessen, ohne deren konkrete Technik zu verallgemeinern?
3. Welche der vorgeschlagenen Ergänzungen schließen echte Lücken, welche sind
   redundant, missverständlich oder zu pauschal?
4. Fehlen wichtige, allgemein anwendbare Wartbarkeitsregeln oder aussagekräftige
   Grenzfälle für die Evaluationsdefinitionen?
5. Reicht die vorhandene Change-Referenz als einziger Detail-Owner, und bleiben
   Aktivierung, Projektvorrang, Umfang sowie Nachweisgrenzen intakt?
6. Gibt der Quellenabgleich professionelle Praktiken zutreffend wieder und
   trennt er belegte Prinzipien, konkrete Werkzeug-Defaults und die ausdrücklich
   gewünschte 1.000-Zeilen-Regel sauber?

## Non-goals

- Keine Änderungen, Aufteilung oder Veröffentlichung von Fluid Base.
- Keine Änderungen an anderen Scoville-Skills oder globalen Systemprompts.
- Keine vorgeschriebene Programmiersprache, Framework-Schichtung oder feste
  Dateinamenstruktur für alle Projekte.
- Keine automatischen Refactorings nur aufgrund einer Zeilenzahl und keine
  Einführung eines neuen Linter-, Build- oder Test-Frameworks.
- Kein Commit, Push, GitHub-Release oder Tag-Cleanup ohne eigenen Auftrag.
- Kein behaupteter Verhaltenstest oder neuer Benchmark allein aus statischen
  Prüfungen, Fallbeschreibungen oder Fables Planprüfung.

## Work items

### W-001 Wartbarkeitsregeln nach geprüftem Plan ergänzen

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0001]
Outcome: Scoville Code enthält die abgeglichenen Regeln zu Dateigröße, Struktur, Benennung und ergänzenden Wartbarkeitsgrenzen im kanonischen Paket und den geprüften lokalen Kopien.
Acceptance: Der Quellenabgleich trennt professionelle Prinzipien von Werkzeug-Defaults und der Nutzergrenze. Fables lesende Prüfung des ergänzten Plans liegt vor jeder Skill-Änderung vor. Bestätigte Hinweise sind im Plan berücksichtigt. Die Regeln erhalten Projektvorrang, sinnvolle Ausnahmen und enge Änderungsgrenzen. Skill-Validierung, JSON-Prüfung, Linkprüfung, vollständige Diff-Sichtung und Bytevergleich der lokalen Paketkopien sind erfolgreich. Fluid Base bleibt unverändert. Nicht durchgeführte Verhaltenstests sind benannt.
Steps:
1. Den Plan mit den benannten Code- und Fluid-Base-Quellen von Fable prüfen lassen und relevante Befunde bewerten.
2. Den noch nicht begonnenen Work Item und gegebenenfalls die dokumentierte Entscheidung entsprechend dem abgeglichenen Plan präzisieren.
3. Nur die nach dem Fable-Abgleich bestätigten Wartbarkeitslücken in Change-Referenz, fünf Evaluationsdefinitionen und zugehöriger Dokumentation ergänzen.
4. Das kanonische Paket prüfen und die vorhandenen lokalen Scoville-Code-Kopien ohne Verlust unabhängiger Änderungen angleichen.
5. Nachweise, verbleibende Grenzen und Planabschluss dokumentieren.
Evidence: [Fable plan review and prioritized guideline follow-up completed before Skill edits, Seven public primary-source pages inspected for professional-practice comparison, Fluid Base source and structure inspected read-only at 46ee6e9b, Skill validation passed for canonical Codex and Claude packages, Evaluation JSON parsed with 10 unique case definitions, Local Markdown link inspection passed across 11 files, Complete scoped diff inspected and Fluid Base tracked source remained unchanged, Canonical Codex and Claude packages match across all 5 files, No new model-behavior benchmark was run]
