# Wöchentlich: Wirkstoff-Recherche

Arbeite im lokalen Klon der kosmetologe-db (CLAUDE.md und `data/kontext/recherche-methodik.md` beachten).

1. `git checkout main && git pull`. Den jüngsten Bericht in `berichte/recherche/` lesen (Duplikatabgleich über PMID/DOI).
2. **Sicherheit und Regulatorik:** SCCS-Opinions-Seite und EUR-Lex auf neue Gutachten bzw. Änderungen der
   VO (EG) 1223/2009 seit dem letzten Bericht prüfen. Nur Primärquellen als [Sicher].
3. **Neue Studien:** PubMed nach Eintragsdatum, letzte 7 Tage (bei dünner Lage 14 Tage), Fokus auf topische
   Kosmetikwirkstoffe und Hautanwendung. Zuerst Stoffe mit Impact „hoch“ aus `maintenance/impact-liste.md`.
4. Für jeden relevanten Fund: Evidenzstufe und Sicherheitskennzeichnung vergeben, Herstellernähe nennen.
   Betroffene Einträge in `data/wirkstoffe/` um einen Abschnitt „Änderungslog“ ergänzen (Datum, Fund, PMID/DOI).
   Neue Wirkstoffe nur bei Impact hoch anlegen. Impact-Liste anpassen, wenn sich eine Bewertung ändert.
5. Bericht `berichte/recherche/YYYY-MM-DD.md` mit den Abschnitten: 1) Sicherheit und Regulatorik,
   2) Neue Funde, 3) Geänderte oder neue Dateien, 4) Unsicherheiten und Werkzeuge.
6. validate + build, Branch `pflege/<YYYY-MM-DD>-recherche`, PR mit Kurzfassung der wichtigsten Befunde.
