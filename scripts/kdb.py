#!/usr/bin/env python3
"""Kosmetologe-DB: validieren, Index bauen, suchen, Prüfbedarf melden.

Aufruf:
  python scripts/kdb.py validate          # Schema, IDs, Querverweise prüfen
  python scripts/kdb.py build             # dist/index.json + dist/llms.txt erzeugen
  python scripts/kdb.py check-build       # Fehler, wenn dist/ nicht aktuell ist (CI)
  python scripts/kdb.py search <begriff>  # Volltextsuche über Titel, Aliase, Tags, Text
  python scripts/kdb.py due [--tage N]    # Einträge, deren Prüfung fällig ist
  python scripts/kdb.py stats             # Bestand je Typ und Status
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DIST = ROOT / "dist"
SCHEMA = json.loads((ROOT / "schema/entry.schema.json").read_text(encoding="utf-8"))
TYPES = json.loads((ROOT / "schema/types.json").read_text(encoding="utf-8"))
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
ID_REF = re.compile(r"\b(?:wirkstoff|haut|behandlung|formulierung|recht|begriff|quelle|kontext):[a-z0-9-]+\b")
# Ab diesem Alter gilt ein geprüfter Eintrag als prüfbedürftig
REVIEW_DAYS = 365


def load_entries():
    entries = []
    for path in sorted(DATA.rglob("*.md")):
        if path.name.startswith("_"):
            continue
        raw = path.read_text(encoding="utf-8")
        m = FRONTMATTER.match(raw)
        if not m:
            entries.append({"_path": path, "_error": "kein YAML-Frontmatter"})
            continue
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as exc:
            entries.append({"_path": path, "_error": f"YAML-Fehler: {exc}".replace("\n", " ")})
            continue
        # YAML liefert Datumswerte als date; Schema erwartet Strings
        for k, v in list(meta.items()):
            if isinstance(v, dt.date):
                meta[k] = v.isoformat()
        meta["_path"] = path
        meta["_body"] = m.group(2).strip()
        entries.append(meta)
    return entries


def validate(entries):
    errors = []
    validator = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
    ids = {}
    for e in entries:
        rel = e["_path"].relative_to(ROOT)
        if "_error" in e:
            errors.append(f"{rel}: {e['_error']}")
            continue
        meta = {k: v for k, v in e.items() if not k.startswith("_")}
        for err in validator.iter_errors(meta):
            loc = "/".join(map(str, err.path)) or "(root)"
            errors.append(f"{rel}: {loc}: {err.message}")
        typ, eid = e.get("typ"), e.get("id", "")
        if typ in TYPES:
            if e["_path"].parent.name != TYPES[typ]["ordner"]:
                errors.append(f"{rel}: Typ '{typ}' gehört nach data/{TYPES[typ]['ordner']}/")
            for feld in TYPES[typ]["pflicht"]:
                if feld not in e:
                    errors.append(f"{rel}: Pflichtfeld '{feld}' fehlt für Typ '{typ}'")
        if eid and not eid.startswith(f"{typ}:"):
            errors.append(f"{rel}: ID '{eid}' passt nicht zum Typ '{typ}'")
        if eid and e["_path"].stem != eid.split(":", 1)[1]:
            errors.append(f"{rel}: Dateiname muss '{eid.split(':', 1)[1]}.md' lauten")
        if eid in ids:
            errors.append(f"{rel}: doppelte ID '{eid}' (auch in {ids[eid]})")
        ids[eid] = rel
    # Querverweise in Frontmatter und Text auflösen
    for e in entries:
        if "_error" in e:
            continue
        rel = e["_path"].relative_to(ROOT)
        refs = set(ID_REF.findall(yaml.safe_dump({k: v for k, v in e.items() if not k.startswith("_") and k != "id"})))
        refs |= set(ID_REF.findall(e["_body"]))
        for ref in sorted(refs - ids.keys()):
            errors.append(f"{rel}: unbekannter Verweis '{ref}'")
    return errors


def build_index(entries):
    items = []
    for e in sorted(entries, key=lambda x: x.get("id", "")):
        meta = {k: v for k, v in e.items() if not k.startswith("_")}
        meta["pfad"] = str(e["_path"].relative_to(ROOT))
        items.append(meta)
    # Rückverweise, damit Claude auch eingehende Kanten sieht
    back = {}
    for it in items:
        for ref in set(ID_REF.findall(json.dumps({k: v for k, v in it.items() if k != "id"}, ensure_ascii=False))):
            back.setdefault(ref, []).append(it["id"])
    for it in items:
        it["verweise_von"] = sorted(set(back.get(it["id"], [])))
    index = {"schema_version": 1, "anzahl": len(items), "eintraege": items}
    lines = [
        "# Kosmetologe-DB – Kompaktindex für LLMs",
        "",
        "> Wissensdatenbank zu Kosmetologie: Wirkstoffe, Haut, Behandlungen, Formulierungen, Recht, Begriffe, Quellen und Projektkontext.",
        "> Volltext eines Eintrags: Datei unter `pfad` lesen. Maschinenlesbar: dist/index.json.",
        "",
    ]
    for typ in TYPES:
        group = [it for it in items if it.get("typ") == typ]
        if not group:
            continue
        lines.append(f"## {typ} ({len(group)})")
        for it in group:
            kurz = f" – {it['kurz']}" if it.get("kurz") else ""
            flag = "" if it.get("status") == "geprueft" else f" [{it.get('status')}]"
            lines.append(f"- `{it['id']}` [{it['titel']}]({it['pfad']}){kurz}{flag}")
        lines.append("")
    return (
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        "\n".join(lines),
    )


def due(entries, tage):
    today = dt.date.today()
    horizon = today + dt.timedelta(days=tage)
    out = []
    for e in entries:
        if "_error" in e or e.get("status") == "veraltet":
            continue
        reason = None
        if e.get("pruefen_bis") and dt.date.fromisoformat(e["pruefen_bis"]) <= horizon:
            reason = f"pruefen_bis {e['pruefen_bis']}"
        elif e.get("status") == "entwurf":
            reason = "Entwurf, noch nicht geprüft"
        elif e.get("geprueft_am") and (today - dt.date.fromisoformat(e["geprueft_am"])).days > REVIEW_DAYS:
            reason = f"zuletzt geprüft {e['geprueft_am']}"
        if reason:
            out.append((e["id"], str(e["_path"].relative_to(ROOT)), reason))
    return out


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    cmd, args = argv[0], argv[1:]
    entries = load_entries()
    if cmd == "validate":
        errors = validate(entries)
        for err in errors:
            print(f"FEHLER {err}")
        print(f"{len(entries)} Einträge, {len(errors)} Fehler")
        return 1 if errors else 0
    if cmd in ("build", "check-build"):
        index_json, llms = build_index(entries)
        targets = {DIST / "index.json": index_json, DIST / "llms.txt": llms}
        if cmd == "check-build":
            stale = [p.name for p, c in targets.items() if not p.exists() or p.read_text(encoding="utf-8") != c]
            if stale:
                print(f"dist/ veraltet ({', '.join(stale)}): bitte 'python scripts/kdb.py build' ausführen")
                return 1
            print("dist/ ist aktuell")
            return 0
        DIST.mkdir(exist_ok=True)
        for p, c in targets.items():
            p.write_text(c, encoding="utf-8")
        print(f"Index mit {len(entries)} Einträgen geschrieben")
        return 0
    if cmd == "search":
        needle = " ".join(args).lower()
        for e in entries:
            hay = " ".join([e.get("id", ""), e.get("titel", ""), " ".join(e.get("aliase", [])),
                            " ".join(e.get("tags", [])), e.get("kurz", ""), e.get("_body", "")]).lower()
            if needle in hay:
                print(f"{e['id']}\t{e['_path'].relative_to(ROOT)}\t{e.get('kurz', '')}")
        return 0
    if cmd == "due":
        tage = int(args[1]) if len(args) > 1 and args[0] == "--tage" else 30
        for eid, path, reason in due(entries, tage):
            print(f"{eid}\t{path}\t{reason}")
        return 0
    if cmd == "stats":
        counts = {}
        for e in entries:
            key = (e.get("typ", "?"), e.get("status", "?"))
            counts[key] = counts.get(key, 0) + 1
        for (typ, status), n in sorted(counts.items()):
            print(f"{typ:<14}{status:<10}{n}")
        print(f"gesamt        {len(entries)}")
        return 0
    print(f"Unbekannter Befehl: {cmd}\n{__doc__}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
