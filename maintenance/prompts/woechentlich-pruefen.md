# Wöchentlich: Qualitätsprüfung

Arbeite im lokalen Klon der kosmetologe-db (CLAUDE.md beachten).

1. `git checkout main && git pull`.
2. `python scripts/kdb.py validate` und `python scripts/kdb.py check-build`. Fehler beheben.
3. `python scripts/kdb.py due --tage 30` ausführen. Für bis zu **5** fällige Einträge
   (Recht zuerst, dann älteste Entwürfe):
   - Aussagen gegen die genannte Quelle prüfen (private Volltexte unter `lokal_privat` lesen,
     Rechtstexte über amtliche URL). Nichts wörtlich übernehmen.
   - Korrekt → `status: geprueft`, `geprueft_am`/`aktualisiert` = heute.
   - Falsch/unsicher → korrigieren oder Unsicherheit im Text vermerken, Status `entwurf` lassen.
4. Kaputte oder fehlende Querverweise (`verwandt`) ergänzen, wo sie offensichtlich sind.
5. `python scripts/kdb.py build`, Branch `pflege/<YYYY-MM-DD>-pruefen`, commit, push,
   Pull Request mit Liste der geprüften Einträge und offener Fragen.
6. Gibt es nichts zu tun: nichts committen, nur kurz berichten.
