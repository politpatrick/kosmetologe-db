# Changelog

## 2026-10-28 – Wöchentliche Prüfung
- `recht:vo-2024-996` am Amtsblatt-Text geprüft: Anhang VI und 4-MBC ergänzt, Grenzwerte und Übergangsfristen tabelliert
- `recht:eu-kosmetikverordnung` gegen konsolidierte Fassung 18.05.2026 geprüft, URL aktualisiert, Art. 19/20 präzisiert
- `begriff:hlb-wert`, `formulierung:emulsion-ow` geprüft (Fundstellen korrigiert); `formulierung:emulsion-wo` teilgeprüft, Beleg für Magnesiumsulfat offen

## 2026-10-28 – Recherchierte Wirkstoffdateien
- 59 Wirkstoffdateien aus dem claude.ai-Projekt übernommen: 36 neue Einträge, 23 bestehende mit dem Projekttext zusammengeführt (54 → 90 Einträge)
- Dateiverweise (`foo.md`) in Eintrags-IDs umgewandelt; Rechts- und Quellenbezüge automatisch verknüpft

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
