---
format_version: 1
id: PLAN-0002
status: completed
created: 2026-09-19
updated: 2026-09-19
---

# Scoville Code: verlässliche Vertragsprüfungen und begrenztes Einlesen

## Goal

Vier gezielte Präzisierungen aus `C:/Users/benja/Desktop/scoville-audit.md` umsetzen und mit begrenzten ausführbaren Fällen prüfen. Der Skill soll große Inhaltsmengen vor dem Einlesen eingrenzen, unabhängige Vertragserwartungen nutzen, den tatsächlich geprüften Fehlerpfad nachweisen und betroffene Verbrauchervarianten erfassen. Bestehende ausreichende Regeln erhalten; keinen Nutzen behaupten, den die Prüfung nicht zeigt.

- Ausführungsowner ist dieses Repository. Das native Planprofil liegt in `development/`; die folgenden Dateipfade sind relativ zum Repository-Root. Geplante Reihenfolge: W-001, W-002, W-003, W-004. Alle Punkte sind noch unbegonnen. Der Nutzer hat den Plan angefordert, noch keine Umsetzung gestartet; bei späterem Umsetzungsauftrag PLAN-0002 mit W-001 aktivieren.
- Scoville Code ausschließlich als zu bearbeitenden Gegenstand lesen, nicht als eigene Arbeitsanweisung. Scoville Plan besitzt die Planpflege. Hauptdatei `scoville-code-anti-ai-slop/SKILL.md` unverändert lassen; Änderungen gehören in die zwei vorhandenen Referenzen. Englische Skilltexte beibehalten.
- Startbasis: `references/change-workflow.md` enthält bereits Kandidatenauswahl, Ausgabebudget und begrenzte Recovery; `references/validation.md` verbietet bereits implementierungsspiegelnde Tests und unbewiesene Mock-Grenzen. `development/tests/evaluation-cases.json` enthält 24 beschreibende Fälle, keinen ausführbaren Verhaltensrunner. `development/skill-fix-acceptance-2026-09-12.md` dokumentiert einen früheren tatsächlichen Vergleich zum begrenzten Lesen; kein neuer Astra-Review-Auftrag folgt aus dem abgeschlossenen PLAN-0001.
- Vor jeder Änderung Ausgangsdateien und Fälle lokal einfrieren. Baseline gegen Kandidat mit identischen Fixtures, Aufgabe, Modell-/Efforteinstellungen und Werkzeugrechten in getrennten frischen Ausführungskontexten vergleichen. Erst die benötigten Referenzen ändern; je W-Item ein Fehlerfall samt Gegenfall in einem Szenario. Maximal ein Baseline-/Kandidatenpaar pro W-Item, insgesamt acht Agentenläufe; keine automatischen Wiederholungen, Zusatzmodelle oder breite Benchmark-Suite. Vorhandenen zugänglichen Tool-/Agentenrunner verwenden; keinen Dienst oder Evaluationsrahmen neu entwickeln. Fehlt er, Verhaltensabnahme offen lassen und den konkreten fehlenden Ausführungsweg melden.
- Jeder Prüflauf darf nur sein isoliertes Fixture ändern. Keine Desktop-Projekte oder echten Installationen zugänglich machen. Sollkriterien bleiben beim Prüfer; der Agent erhält Aufgabe und Quellen, nicht die erwartete Diagnose. Toolaufrufe, tatsächlich ausgeführte Checks, Änderungen und zurückgegebene Inhaltsmengen lokal auswerten; nur knappe Ergebnisse in den Arbeitskontext übernehmen. Selbstbeschreibungen des Agenten sind kein Ausführungsnachweis.
- Fixtures und Rohtraces unter `Z:/Projekts/AI/temp/YYYY-MM-DD-scoville-code-fix/`; kleine wiederverwendbare Eingaben/Fallbeschreibungen dürfen in `development/tests/` bleiben. Vor Läufen per vorhandenem Runner ein begrenztes Aufruf-/Ausgabebudget setzen; mindestens Einzelantworten begrenzen und bei wiederholtem unnötigem Nachladen abbrechen. Wenn der Runner Gesamtverbrauch nicht begrenzen kann, keine garantierte Tokenobergrenze behaupten. Keine großen Rohtraces in den Kontext laden.
- Abnahme unterscheidet Wirksamkeit und Regelklarheit: Kandidat muss alle Sollkriterien ohne Scope-Ausweitung erfüllen. Fehlerhafte Kandidaten nicht als abgeschlossen markieren. Bei identischem korrektem Baseline-/Kandidatenverhalten keinen Nutzen erfinden; nur eine nachweislich beseitigte konkrete Textlücke rechtfertigt die Präzisierung. Ohne solche Lücke Änderung verwerfen und das belegte Nichtändern als Ergebnis festhalten. Keine endlose Optimierung; weitere Versuche benötigen einen benannten Befund und gesonderten Auftrag.
- Abschließend nur betroffene vorhandene Fälle semantisch gegen den finalen Text prüfen, JSON parsen und scoped Diff lesen. Nach einer späteren Änderung an bereits geprüfter Semantik deren Nachweis als veraltet kennzeichnen; keine ungeprüfte Gesamtfreigabe. Ausgeführte Befunde kurz in Evidence festhalten, Rohantworten nicht dauerhaft übernehmen. Native Strukturprüfung: `python C:/Users/benja/.codex/skills/scoville-plan/scripts/validate_profile.py --root development --format json`.

## Non-goals

- Keine Produktfixes, erneuten Audits oder breiten Tests in private project/Fluidbase; keine Änderungen an Scoville Plan, UI oder anderen Skills.
- Keine Installation, Veröffentlichung, Versions-/Releasepflege, Commits oder Pushes. Der Plan endet bei geprüftem kanonischem Skillquelltext und seinen Fällen; Verteilung bleibt ein gesonderter Auftrag.
- Keine neue Infrastruktur, Pflichtbrowserchecks, pauschalen Komplettsuiten, festen globalen MB-Grenzen, generischen Retries/Fallbacks oder zusätzlichen Planprozesse. Kein kontoweites Limitversprechen und keine allgemeine Einsparungsquote aus Einzelfällen.

## Work items

### W-001 Große Inhaltsmengen vor dem Einlesen eingrenzen

Status: done
Depends on: []
Blocked by: []
Decisions: []
Outcome: Die bestehende Suchregel verhindert blindes rekursives Inhaltsladen und wahllose Fortsetzung abgeschnittener Ausgaben, ohne kleine gezielte Reads mit Inventuren zu belasten.
Acceptance: Im gepaarten ausführbaren Fall wird die relevante kleine Konfiguration richtig geändert; irrelevante Dateiinhalte werden nicht ausgegeben. Eine ausdrücklich benötigte große einzeilige JSONL-Datei wird lokal nach dem benötigten Feld gefiltert. Kein vollständiges rekursives Listing, kein Rohdump und kein seitenweises Leeren aller Truncations. Gegenfall: exakte kleine Datei wird ohne Verzeichnisinventur gelesen. Tatsächliche Werkzeugaufrufe und kumulierte ausgegebene Inhaltsmenge sind ausgewertet; keine Gleichsetzung mit Wochenquota.
Steps:
1. Lies den Code-Abschnitt von `development/skill-fix-acceptance-2026-09-12.md` sowie `scoville-code-anti-ai-slop/references/change-workflow.md` unter Locate proportionately. Friere die Ausgangsfassung ein; übernimm die vorhandene Scope-/Recovery-Logik, statt sie nochmals einzuführen.
2. Ergänze einen Fall samt Gegenfall in `development/tests/evaluation-cases.json`: kleine benannte Konfiguration, 500 irrelevante Dateien, eine lokal generierte 2-MiB-JSONL-Einzelzeile mit genau einem angefragten Ergebnisfeld. Erzeuge diese Daten ausschließlich im Task-Temp; Aufgabe ist eine konkrete Konfigurationsänderung plus Ausgabe dieses Felds, ohne Hinweise auf die Falle. Der separate Gegenfall nennt nur die kleine Datei. Beide Kontexte erhalten dieselben Inhalte.
3. Präzisiere ausschließlich den bestehenden Locate-proportionately-Absatz in `scoville-code-anti-ai-slop/references/change-workflow.md`: bei unbekanntem breitem Umfang zuerst begrenzte Metadaten/Pfadauswahl; vor Inhaltslesen Auswahl und Ausgabebudget eingrenzen; weitere Reads nur für benannte offene Fragen; keine automatische Truncation-Fortsetzung. Bekannte kleine Dateien direkt lesen und ausdrücklich benötigte große Quellen lokal filtern. Keine vollständige Größeninventur und kein starres MB-Limit verlangen.
4. Führe das eine Baseline-/Kandidatenpaar nach dem gemeinsamen Protokoll aus. Prüfe Dateiergebnis und Read-Traces, nicht nur die Abschlussantwort; erfasse den Unterschied zwischen erzeugter Toolausgabe und tatsächlich sichtbarer begrenzter Ausgabe, soweit verfügbar.
Evidence: [Initial Astra Low pair exposed complete recursive path listings in both variants; wording was tightened and Acceptance remained open, Authorized rerun passed: candidate bounded paths to 30 and JSONL output to 13 chars while baseline emitted all paths; both edits and checks passed]

### W-002 Erwartungen an unabhängigen Grenzverträgen prüfen

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: []
Outcome: Ein Test, der denselben falschen Datenvertrag wie der Producer kopiert, gilt nicht als Kompatibilitätsnachweis; lokale deterministische Beweise bleiben ausreichend.
Acceptance: Kandidat erkennt im ausführbaren Fixture die Abweichung eines erzeugten Attributpfads vom unabhängigen Consumervertrag, korrigiert Producer und fehlerhafte Testerwartung und führt einen Test mit tatsächlichem Consumer aus. Consumervertrag bleibt unverändert. Der bestehende reine Transformationstest bleibt ohne Browser, Netzwerk oder Framework akzeptiert. Baseline/Kandidat nach gemeinsamem Protokoll verglichen; keine Übernahme des Fehlers in den Consumer.
Steps:
1. Lies `scoville-code-anti-ai-slop/references/validation.md` unter Select proportional checks sowie die vorhandenen Fälle `fixture-producer-consumer-boundary` und `controlled-fixture-pure-transform` in `development/tests/evaluation-cases.json`.
2. Ergänze dort einen ausführbaren Fall: Producer und bisheriger Test nutzen `title.font.font.size`, während die unabhängige lokale Consumerspezifikation und der tatsächliche Consumer `title.font.size` unterstützen. Liefere einen vorhandenen grünen Producer-Test und einen engen Consumer-Aufruf; Aufgabe ist die fehlerhafte Übergabe zu beheben. Ein unabhängiger korrekter reiner String-Transformationsfall dient als Gegenfall. Keine echten Divi-Dateien kopieren.
3. Präzisiere den vorhandenen Satz zu implementierungsspiegelnden Tests in `scoville-code-anti-ai-slop/references/validation.md`: Erwartungen bei betroffenen Grenzverträgen aus vereinbartem Vertrag oder unabhängigem tatsächlichem Verbraucher ableiten; gemeinsam kopierte Konstante oder eigener Roundtrip genügt dafür nicht. Erhalte die Ausnahme für echte kontrollierte deterministische Checks und den begrenzten Claim bei unprüfbarer Integration.
4. Führe das eine Baseline-/Kandidatenpaar aus; prüfe tatsächliche Änderungen und Consumer-Testresultat. Prüfe zugleich, dass kein globales Recherche-, Browser- oder Integrationserfordernis im Skilltext entstanden ist.
Evidence: [Astra Low pair changed only producer.py and its mirrored test; the actual consumer contract stayed byte-identical and all three focused tests passed, Baseline and candidate behavior matched; retained wording closes the observed independent-expectation gap without claiming run improvement]

### W-003 Nachweisen, dass die Fehlerinjektion den Zielpfad trifft

Status: done
Depends on: [W-002]
Blocked by: []
Decisions: []
Outcome: Negativtests belegen ihre Vorbedingungen und den benannten Fehlerpunkt, statt einen früheren Abbruch als Beweis für einen späteren Pfad zu akzeptieren.
Acceptance: Im ausführbaren Fixture wird der State-Read erfolgreich durchlaufen und erst der Cache-Read gezielt zum Scheitern gebracht; separat bleibt der State-Fehler geprüft. Jeweils erfolgt kein Provideraufruf. Der Agent akzeptiert nicht einfach beide Fehlercodes im Cache-Read-Test. Im Gegenfall bleibt ein bereits eindeutiger Negativtest ohne neue Zähler oder Produktionsinstrumentierung gültig. Tatsächliche Tests und Nachwirkungen sind beobachtet.
Steps:
1. Lies den Fixture-/Mock-Absatz in `scoville-code-anti-ai-slop/references/validation.md` und halte das private project-Muster fest: globale DB-Störung trifft State-Read vor Cache-Read; ein gelockerter Codevergleich würde die fehlende Abdeckung verstecken.
2. Ergänze den Fall in `development/tests/evaluation-cases.json` und ein kleines isoliertes ausführbares Fixture mit State-Read, Cache-Read und gezähltem Provideraufruf. Liefere den irreführenden ursprünglichen Test und als zu prüfenden Vorschlag die Akzeptanz beider Codes. Ergänze einen bereits eindeutig zielgenauen Fehlerfall als Gegenfall; keine Datenbank und kein Netz nötig.
3. Ergänze den bestehenden Fixture-/Mock-Absatz in `scoville-code-anti-ai-slop/references/validation.md` um tatsächlich erreichte Vorbedingungen, getroffene Zieloperation und relevante Nachwirkung. Bestehende eindeutige Rückgaben dürfen als Nachweis genügen; keine universelle Zähler-, Logging- oder Fault-Injection-Pflicht hinzufügen.
4. Führe das eine Baseline-/Kandidatenpaar aus und prüfe die beiden Fehlerpfade sowie unveränderte Scope-Grenzen. Prüfe, dass die neue Formulierung die in W-002 abgenommene unabhängige Vertragserwartung nicht abschwächt.
Evidence: [Astra Low pair isolated state and cache failures and asserted exact paths with no provider call; all three tests passed, Production code and the already unambiguous control stayed unchanged; no universal instrumentation was added]

### W-004 Unabhängig betroffene Verbrauchervarianten erfassen

Status: done
Depends on: [W-003]
Blocked by: []
Decisions: []
Outcome: Vertragsänderungen berücksichtigen direkt betroffene reale Varianten und Test-Doubles, ohne alle Aufrufer oder benachbarte Module pauschal prüfen zu müssen.
Acceptance: Im ausführbaren Fixture werden zwei unabhängig betroffene registrierte Verbrauchervarianten und ein alter Test-Double gefunden und korrekt angepasst; beide Varianten werden gezielt ausgeführt. Ein unbeteiligter Nachbar bleibt unangetastet. Gegenfall: interner Rewrite mit unverändertem Vertrag erzeugt keine umfassende Verbraucherinventur. Die finalen Referenzen widersprechen sich nicht; Fall-JSON ist gültig, Planstruktur ist gültig und alle nicht beobachteten Verhaltensnachweise bleiben offen.
Steps:
1. Lies in `scoville-code-anti-ai-slop/references/change-workflow.md` den Absatz For a changed symbol or public behavior und in `references/validation.md` den Satz exercise at least one affected use. Prüfe beide gemeinsam auf die Verwechslung zwischen Mindestbeispiel und vollständiger betroffener Variantenabdeckung.
2. Ergänze in `development/tests/evaluation-cases.json` ein ausführbares Mini-Repository mit einer explizit angeforderten Vertragsänderung, zwei über eine kleine Registry auffindbaren verschiedenen Verbrauchervarianten, einem veralteten Test-Double und einem unbeteiligten Nachbar. Ergänze als Gegenfall einen internen Rewrite ohne Vertragsänderung. Auftrag nennt das gewünschte Verhalten, nicht die Zahl versteckter Varianten.
3. Ersetze die betroffene Verbraucherformulierung in `scoville-code-anti-ai-slop/references/change-workflow.md`: direkt betroffene Aufrufer, Registrierungen und Test-Doubles lokalisieren; unabhängig betroffene Vertragsvarianten berücksichtigen; ein repräsentativer Verbraucher genügt bei nur einer Variante. Stimme den vorhandenen Satz in `scoville-code-anti-ai-slop/references/validation.md` knapp darauf ab, ohne eine zweite ausführliche Regelkopie anzulegen.
4. Führe das eine Baseline-/Kandidatenpaar aus. Prüfe anschließend die zwei final geänderten Referenzen vollständig auf Duplikate, Scope-Ausweitung und gegenseitige Widersprüche; parse `development/tests/evaluation-cases.json` mit Python und vergleiche gezielt die bestehenden Fälle `contained-change-without-exposed-variant`, `fixture-producer-consumer-boundary` und `controlled-fixture-pure-transform` mit dem finalen Text.
5. Halte ausschließlich beobachtete Abnahmen und verbliebene Grenzen in den Evidence-Feldern dieses Plans fest, prüfe scoped Diff und native Struktur. Entferne ausschließlich verifizierte eigene Task-Temp-Artefakte, nachdem notwendige knappe Ergebnisse übernommen wurden. Keine Installation oder Veröffentlichung anschließen.
Evidence: [Astra Low pair updated both registered consumers and the test double; four focused tests passed and registry plus unrelated neighbor stayed byte-identical, Full references showed no duplicate or contradictory rule; three named legacy cases matched final text and evaluation JSON parsed, Evaluator rerun passed W-001 observations and 3 W-002 plus 3 W-003 plus 4 W-004 tests]
