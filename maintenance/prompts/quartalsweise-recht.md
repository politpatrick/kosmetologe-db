# Quartalsweise: Rechtsstand abgleichen

1. `git checkout main && git pull`.
2. Für jeden `recht:`-Eintrag die amtliche Quelle (`url`) aufrufen und `stand` vergleichen.
   Für die EU-Kosmetikverordnung: neue Änderungsverordnungen seit dem letzten `geprueft_am`
   ermitteln (EUR-Lex, „konsolidierte Fassungen“).
3. Betroffene Wirkstoffe (Feld `regulierung`) anpassen: Grenzwerte, Übergangsfristen.
4. `stand`, `geprueft_am`, `aktualisiert` aktualisieren; `pruefen_bis` = heute + 3 Monate.
5. Lokale Spiegelung law-data-germany prüfen, falls vorhanden.
6. validate + build, Branch `pflege/<YYYY-MM-DD>-recht`, PR mit Änderungsübersicht und Links.
