# CLAUDE.md – Arbeiten mit der Kosmetologe-DB

Diese Datei lädt Claude Code automatisch, wenn im Repo gearbeitet wird.

## Was ist das?
Eine dateibasierte Wissensdatenbank zur Kosmetologie. Jeder Eintrag ist eine Markdown-Datei
mit YAML-Frontmatter unter `data/<ordner>/<slug>.md`. IDs haben die Form `typ:slug`
(z. B. `wirkstoff:niacinamid`) und verknüpfen Einträge untereinander.

| Typ | Ordner | Inhalt |
|---|---|---|
| wirkstoff | data/wirkstoffe | Inhaltsstoffe mit INCI, Funktion, Eignung, Regulierung |
| haut | data/haut | Hauttypen, Hautzustände, Effloreszenzen, Erkrankungen |
| behandlung | data/behandlungen | Kosmetische Behandlungen mit Indikation/Kontraindikation |
| formulierung | data/formulierungen | Produktsysteme (Emulsionen, Gele, Tensidsysteme …) |
| recht | data/recht | EU-/DE-Normen mit Stand und Prüftermin |
| begriff | data/begriffe | Glossar |
| quelle | data/quellen | Quellenregister (nur bibliografische Daten) |
| kontext | data/kontext | Projektkontext: Tonalität, Design, Code-Konventionen, Leitplanken |

Außerhalb von `data/` (nicht im Index):
- `berichte/recherche/` – datierte Rechercheberichte (PubMed, SCCS, EUR-Lex)
- `maintenance/impact-liste.md` – Priorisierung der Wirkstoffe nach Evidenz und Impact

## Lesen (schnellster Weg)
1. `dist/llms.txt` – kompakte Liste aller Einträge mit Kurzbeschreibung.
2. `dist/index.json` – vollständige Metadaten inkl. Rückverweisen (`verweise_von`).
3. Einzelne Datei unter `pfad` lesen, wenn Details gebraucht werden.
4. Suche: `python scripts/kdb.py search <begriff>`.

Vor Design-, Code- oder Textaufgaben immer die `kontext:`-Einträge mit passendem `einsatz` lesen,
`kontext:fachliche-grundsaetze` und `kontext:recherche-methodik` gelten immer.

## Schreiben – Regeln
- Neue Einträge nach Schema `schema/entry.schema.json` + Pflichtfelder aus `schema/types.json`.
- Dateiname = Slug der ID. Kleinbuchstaben, Bindestriche, Umlaute ausschreiben (ae/oe/ue/ss).
- Nur eigene Formulierungen. **Nie** Textpassagen aus urheberrechtlich geschützten Quellen
  übernehmen (Repo ist öffentlich). Fundstellen zitieren: `quellen: [{id, fundstelle}]`.
- Neue oder geänderte Fachaussagen: `status: entwurf`. Auf `geprueft` erst nach Abgleich mit
  einer Quelle setzen und `geprueft_am` eintragen.
- `aktualisiert` bei jeder inhaltlichen Änderung auf das heutige Datum setzen.
- Danach immer:
  ```bash
  python scripts/kdb.py validate && python scripts/kdb.py build
  ```
  und `dist/` mit committen. CI bricht ab, wenn `dist/` veraltet ist.
- Größere Änderungen in `CHANGELOG.md` notieren.

## Private Quellen
Die Fachbücher liegen nur lokal unter `privat/` (per .gitignore ausgeschlossen):
- `privat/originale/*.pdf` – Originale; daneben `*.txt` als durchsuchbarer Textauszug mit
  Markern `<!-- PDF-Seite n -->`. Pfad im Quelleneintrag: `lokal_privat`.
- `privat/*.md` – Zusammenfassungen (Feld `lokal_zusammenfassung`); das Springer-Lexikon ist dort im Original.

Regeln:
- Zum Prüfen und Erweitern gilt das **Original**; die Zusammenfassung nur zur Orientierung.
- Fundstellen nennen **gedruckte** Seiten: gedruckte Seite = PDF-Seite − `seitenversatz` des Quelleneintrags.
- Lesen ja, zitieren oder einchecken nie. Nur eigene Formulierungen ins Repo.
- `privat/` existiert nur auf dem Mac des Nutzers; fehlt es, Prüfungen gegen Bücher überspringen und im PR vermerken.

## Pflege
Wiederkehrende Aufgaben stehen in `maintenance/prompts/` und laufen als geplante Aufgaben.
Ablauf jeder Pflegeaufgabe: Branch `pflege/<datum>-<aufgabe>` → Änderungen → validate/build → Pull Request.
