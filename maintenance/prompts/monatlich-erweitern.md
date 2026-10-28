# Monatlich: Datenbank erweitern

Arbeite im lokalen Klon der kosmetologe-db (CLAUDE.md beachten).

1. `git checkout main && git pull`, `python scripts/kdb.py stats`.
2. Lücken bestimmen: Verweise im Text ohne eigenen Eintrag, Stoffe/Begriffe aus den
   Kapitelgliederungen der Quellen (`data/quellen/*`, `lokal_privat`), die noch fehlen,
   Wünsche aus `maintenance/backlog.md`, Abschnitt B der `maintenance/impact-liste.md`
   (Stoffe ohne eigenen Eintrag) und die private Arbeitsliste `privat/Literatur-Wirkstoffliste.md`
   (Funktion, Quelle und Fundstelle je Stoff – nur als Ausgangspunkt, nicht abschreiben).
3. **8–12** neue Einträge anlegen, ausgewogen über Typen; je Eintrag eigene Formulierung,
   Quellenangabe mit Fundstelle, `evidenz` (Lehrbuch allein = `nicht-bewertet`), `status: entwurf`, sinnvolle `verwandt`-Links in beide Richtungen.
4. Erledigte Backlog-Punkte abhaken.
5. validate + build, Branch `pflege/<YYYY-MM-DD>-erweitern`, PR mit Liste der neuen IDs.
