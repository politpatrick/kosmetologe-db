---
name: kosmetologe-wissen
description: Fachwissen zu Kosmetologie aus der Kosmetologe-DB (GitHub) nutzen – Wirkstoffe/INCI, Hauttypen und -zustände, kosmetische Behandlungen, Formulierungen, EU/DE-Kosmetikrecht sowie Projektkontext für Design, Code und Texte. Verwenden bei Fragen zu Hautpflege, Inhaltsstoffen, Behandlungsplänen, Produkttexten, Kosmetik-Apps oder -Designs, oder wenn der Nutzer „Kosmetologe“ erwähnt.
---

# Kosmetologe-Wissen

Die Wissensbasis liegt im GitHub-Repo **kosmetologe-db**. Inhalte niemals aus dem Gedächtnis
erfinden, wenn die DB einen Eintrag hat – die DB ist die Referenz.

## 1. Daten beschaffen
Reihenfolge, erste verfügbare Variante nutzen:
1. Lokaler Klon (falls vorhanden): `dist/llms.txt` und `dist/index.json` im Repo lesen.
2. Remote: `https://raw.githubusercontent.com/<OWNER>/kosmetologe-db/main/dist/llms.txt`
   und für Details `…/main/<pfad>` abrufen.

## 2. Relevante Einträge finden
- In `llms.txt` nach Titel/ID/Kurztext suchen; in `index.json` über `tags`, `verwandt`,
  `verweise_von`, `indikation`, `geeignet_fuer` navigieren.
- Immer `kontext:fachliche-grundsaetze` beachten.
- Für Design-/Code-/Textaufgaben zusätzlich alle `kontext:`-Einträge mit passendem `einsatz` laden.

## 3. Antworten
- Aussagen mit Eintrags-ID belegen, z. B. „(wirkstoff:retinol)“.
- Einträge mit `status: entwurf` als „noch nicht fachlich geprüft“ kennzeichnen.
- Recht: Stand und `pruefen_bis` nennen; liegt `pruefen_bis` in der Vergangenheit, auf mögliche
  Änderungen hinweisen.
- Bei `aerztlich_abklaeren`-Merkmalen klar an Ärztin/Arzt verweisen – keine Diagnosen.

## 4. Lücken melden
Fehlt Wissen in der DB, am Ende der Antwort kurz vorschlagen, welcher Eintrag
(Typ, ID, Kurztext) ergänzt werden sollte. Im Repo selbst nur nach den Regeln in `CLAUDE.md` schreiben.
