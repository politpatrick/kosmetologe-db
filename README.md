# Kosmetologe-DB

Offene, für Menschen und Claude lesbare Wissensdatenbank zur Kosmetologie:
Wirkstoffe (INCI), Hauttypen und -zustände, kosmetische Behandlungen, Formulierungen,
EU-/DE-Kosmetikrecht, Glossar und Projektkontext.

> Keine medizinische Beratung. Einträge mit Status `entwurf` sind noch nicht fachlich geprüft.

## Aufbau
```
data/        Einträge als Markdown + YAML-Frontmatter (ein Ordner je Typ)
schema/      JSON-Schema und Pflichtfelder je Typ
dist/        generiert: index.json (vollständig), llms.txt (kompakt für LLMs)
scripts/     kdb.py – validate | build | check-build | search | due | stats
skills/      Claude-Skill „kosmetologe-wissen“
maintenance/ Prompts und Backlog für geplante Pflegeaufgaben
```

## Nutzung
```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/kdb.py search retinol
.venv/bin/python scripts/kdb.py validate && .venv/bin/python scripts/kdb.py build
```

### In Claude
- **Claude Code:** Repo klonen – `CLAUDE.md` wird automatisch geladen.
- **Skill:** Ordner `skills/kosmetologe-wissen` als Skill installieren (oder als ZIP in claude.ai hochladen).
- **Projekt/Chat:** `dist/llms.txt` als Wissensdatei hinzufügen oder per Raw-URL abrufen lassen.
- **Design/Code:** `kontext:`-Einträge mit `einsatz: design|code` enthalten die Vorgaben.

## Quellen und Urheberrecht
Das Repo enthält nur eigene Formulierungen und bibliografische Angaben. Volltexte der
Fachbücher werden nicht veröffentlicht. Rechtsnormen sind amtliche Werke (§ 5 UrhG).
