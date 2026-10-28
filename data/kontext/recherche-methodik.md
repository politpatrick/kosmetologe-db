---
id: kontext:recherche-methodik
typ: kontext
titel: Recherche-Methodik und Sicherheitskennzeichnung
einsatz: [text, beratung, skill]
prioritaet: hoch
kurz: Evidenzstufen (stark/moderat/schwach/keine), Aussage-Sicherheit ([Sicher]/[Wahrscheinlich]/[Vermutung]) und Regeln für die Wirkstoff-Recherche.
tags: [methodik, evidenz]
verwandt: [kontext:fachliche-grundsaetze, quelle:pubmed, quelle:sccs]
quellen:
  - id: quelle:kosmetologe-projekt
    fundstelle: abgeleitet aus Rechercheberichten 2026-10-20 bis 2026-10-28
status: entwurf
aktualisiert: 2026-10-28
---
Aus der Arbeitsweise des Projekts abgeleitet; die ursprüngliche Projektvorgabe lag beim Import nicht vor und sollte ergänzt werden.

## Evidenzstufen (Feld `evidenz` bei Wirkstoffen)
- **stark** – mehrere RCTs oder systematische Übersicht mit konsistentem Ergebnis
- **moderat** – einzelne kleinere RCTs, Split-Face-Studien
- **schwach** – In-vitro, Tiermodell, Fallberichte, Mechanistik
- **keine** / **nicht-bewertet** – Lehrbuchangabe ohne Studienlage; Lehrbücher sind keine Primärevidenz

## Aussage-Sicherheit (im Text)
- **[Sicher]** – am Originaldokument geprüft
- **[Wahrscheinlich]** – aus Abstract oder Zusammenfassung, Volltext/Primärquelle nicht geprüft
- **[Vermutung]** – Sekundärquelle, Entwurfsstatus oder eigene Einordnung

## Impact (Feld `impact`)
hoch / mittel / niedrig / offen – nach Evidenz, Marktrelevanz, Neuigkeitswert und Sicherheitsrelevanz (SCCS/Verordnung). Pflege in `maintenance/impact-liste.md`.

## Recherche-Regeln
- PubMed nach Eintragsdatum, Fenster 7 Tage (bei dünner Lage bis 14 Tage), Duplikate über PMID/DOI abgleichen.
- Regulatorik nur aus Primärquellen (EUR-Lex, SCCS) als [Sicher]; Branchenportale höchstens [Vermutung].
- Herstellernahe Studien und Interessenkonflikte ausdrücklich nennen.
- Verworfene Treffer kurz begründen (Onkologie, Chirurgie, Tier ohne Hautbezug …).
- Ergebnisse als Bericht unter `berichte/recherche/YYYY-MM-DD.md`, Änderungen an Einträgen im Abschnitt „Änderungslog“.
