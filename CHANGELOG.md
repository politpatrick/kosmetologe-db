# Changelog

## 2026-10-28 – Import aus dem claude.ai-Projekt
- Rechtsauswertungen Anhang II (Arzneistoffe), III (Duftstoff-Allergene), VI (UV-Filter); VO (EU) 2024/996
- 18 recherchierte Wirkstoffe aus der Impact-Liste (Abschnitt A); Felder `evidenz` und `impact`
- Rechercheberichte unter `berichte/recherche/`, Impact-Liste unter `maintenance/`
- `kontext:recherche-methodik` (Evidenzstufen, [Sicher]/[Wahrscheinlich]/[Vermutung])
- Quellen korrigiert: Dermatologie-Leitfaden = Herrmann/Trinkkeller 2020, Tadros 2023; neu PubMed, SCCS, Projekt
- `kdb.py` meldet YAML-Fehler je Datei statt abzubrechen

## 2026-10-28 – Aufbau
- Schema (8 Typen), Validierungs- und Index-Skript `scripts/kdb.py`
- Erstbefüllung: 28 Einträge (Wirkstoffe, Haut, Behandlungen, Formulierungen, Recht, Begriffe, Quellen, Kontext)
- Claude-Integration: CLAUDE.md, Skill `kosmetologe-wissen`, `dist/llms.txt`, `dist/index.json`
- Pflegeprozess: Prompts für wöchentliche Prüfung, monatliche Erweiterung, quartalsweisen Rechtsabgleich
