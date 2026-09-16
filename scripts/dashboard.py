#!/usr/bin/env python3
"""Erzeugt DASHBOARD.md aus dem Frontmatter in ideas/, pipeline/ und products/.

Aufruf: python scripts/dashboard.py
Keine Abhängigkeiten außer der Standardbibliothek (kein PyYAML nötig).
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS_ORDER = [
    "produkt", "briefing", "deep-dive", "voranalyse", "freigegeben",
    "idee", "importiert", "beobachten", "abgelehnt",
]
STAGE_LABEL = {
    "produkt": "Produkt (NG)",
    "briefing": "Gate 3 wartet",
    "deep-dive": "Gate 2 wartet",
    "voranalyse": "Gate 1 wartet",
    "freigegeben": "Freigegeben → /voranalyse",
    "idee": "Wartet auf Freigabe",
    "importiert": "Importiert (Miro)",
    "beobachten": "Beobachten",
    "abgelehnt": "Abgelehnt",
}
LANE_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3}


def parse_frontmatter(text: str) -> dict:
    """Minimaler YAML-Parser für flache Keys, Listen in [] und ein Level Einrückung."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    data: dict = {}
    current_parent = None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.split(" #", 1)[0].rstrip()
        if ":" not in line:
            continue
        key, _, val = line.strip().partition(":")
        val = val.strip()
        if indent == 0:
            if val == "":
                data[key] = {}
                current_parent = key
            else:
                data[key] = _coerce(val)
                current_parent = None
        elif current_parent is not None:
            data[current_parent][key] = _coerce(val)
    return data


def _coerce(val: str):
    if val in ("null", "~", ""):
        return None
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        return [_coerce(v.strip()) for v in inner.split(",")] if inner else []
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        return val[1:-1]
    try:
        return int(val)
    except ValueError:
        pass
    try:
        return float(val)
    except ValueError:
        return val


def load_entries() -> list[dict]:
    entries: dict[str, dict] = {}
    # Reihenfolge: ideas zuerst, pipeline/products überschreiben (haben Vorrang).
    for path in sorted((ROOT / "ideas").glob("*.md")):
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm.get("slug"):
            fm["_pfad"] = str(path.relative_to(ROOT))
            entries[fm["slug"]] = fm
    for base in ("pipeline", "products"):
        for path in sorted((ROOT / base).glob("*/00-idee.md")):
            fm = parse_frontmatter(path.read_text(encoding="utf-8"))
            if fm.get("slug"):
                fm["_pfad"] = str(path.parent.relative_to(ROOT))
                entries[fm["slug"]] = fm
    return list(entries.values())


def fmt(v) -> str:
    if v is None:
        return "–"
    if isinstance(v, list):
        return ", ".join(str(x) for x in v) if v else "–"
    if isinstance(v, float):
        return f"{v:.1f}".replace(".", ",")
    return str(v)


def vk(e: dict) -> str:
    s = e.get("vk_spanne_eur")
    if isinstance(s, list) and len(s) == 2 and all(isinstance(x, (int, float)) for x in s):
        return f"{s[0]}–{s[1]} €"
    return "–"


def next_ng(entries: list[dict]) -> str:
    nums = []
    for e in entries:
        ng = e.get("ng_nummer")
        if isinstance(ng, str) and ng.startswith("NG"):
            try:
                nums.append(int(ng[2:]))
            except ValueError:
                pass
    return f"NG{(max(nums) + 1 if nums else 1):04d}"


def build(entries: list[dict]) -> str:
    today = date.today().isoformat()
    lines = [f"# Dashboard nicegarden Produktrecherche", "",
             f"Stand: {today} · generiert von `scripts/dashboard.py` · {len(entries)} Einträge · nächste freie NG-Nummer: **{next_ng(entries)}**", ""]

    # Zusammenfassung
    lines += ["## Status-Übersicht", "", "| Status | Anzahl | Bedeutung |", "|---|---|---|"]
    for st in STATUS_ORDER:
        n = sum(1 for e in entries if e.get("status") == st)
        if n:
            lines.append(f"| `{st}` | {n} | {STAGE_LABEL.get(st, '')} |")
    unknown = [e for e in entries if e.get("status") not in STATUS_ORDER]
    if unknown:
        lines.append(f"| (unbekannt) | {len(unknown)} | {', '.join(e['slug'] for e in unknown)} |")
    lines.append("")

    # Offene Entscheidungen
    waiting = [e for e in entries if e.get("status") in ("idee", "voranalyse", "deep-dive", "briefing")]
    lines += ["## Wartet auf Pafri", ""]
    if waiting:
        lines += ["| Slug | Stufe | Score | Gesamt | Pfad |", "|---|---|---|---|---|"]
        for e in sorted(waiting, key=lambda x: STATUS_ORDER.index(x.get("status"))):
            lines.append(f"| {e['slug']} | {STAGE_LABEL[e['status']]} | {fmt(e.get('score'))} | {fmt(e.get('score_gesamt'))} | `{e['_pfad']}` |")
    else:
        lines.append("Keine offenen Gates.")
    lines.append("")

    # Produkte
    prods = [e for e in entries if e.get("status") == "produkt"]
    lines += ["## Produkte", ""]
    if prods:
        lines += ["| NG | Slug | Titel | Pfad |", "|---|---|---|---|"]
        for e in sorted(prods, key=lambda x: str(x.get("ng_nummer"))):
            lines.append(f"| {fmt(e.get('ng_nummer'))} | {e['slug']} | {fmt(e.get('titel'))} | `{e['_pfad']}` |")
    else:
        lines.append("Noch keine.")
    lines.append("")

    # Pipeline
    pipe = [e for e in entries if e.get("status") in ("freigegeben", "voranalyse", "deep-dive", "briefing")]
    lines += ["## Pipeline (Stufe 1–3)", ""]
    if pipe:
        lines += ["| Slug | Status | Gate 1 | Gate 2 | Gate 3 | Gesamt | Pfad |", "|---|---|---|---|---|---|---|"]
        for e in sorted(pipe, key=lambda x: STATUS_ORDER.index(x.get("status"))):
            lines.append(f"| {e['slug']} | `{e['status']}` | {fmt(e.get('gate_1'))} | {fmt(e.get('gate_2'))} | {fmt(e.get('gate_3'))} | {fmt(e.get('score_gesamt'))} | `{e['_pfad']}` |")
    else:
        lines.append("Leer.")
    lines.append("")

    # Ideen nach Lane
    ideas = [e for e in entries if e.get("status") in ("importiert", "idee", "beobachten")]
    lines += ["## Ideen (Stufe 0) nach Lane", ""]
    if ideas:
        lines += ["| Lane | Slug | Titel | Kategorie | VK | Status | Quelle | Lauf |", "|---|---|---|---|---|---|---|---|"]
        for e in sorted(ideas, key=lambda x: (LANE_ORDER.get(str(x.get("score")), 9), x["slug"])):
            lines.append(f"| {fmt(e.get('score'))} | {e['slug']} | {fmt(e.get('titel'))} | {fmt(e.get('kategorie'))} | {vk(e)} | `{e['status']}` | {fmt(e.get('quelle'))} | {fmt(e.get('lauf'))} |")
    else:
        lines.append("Leer.")
    lines.append("")

    # Abgelehnt
    rej = [e for e in entries if e.get("status") == "abgelehnt"]
    lines += ["## Abgelehnt", ""]
    if rej:
        lines += ["| Slug | Titel | Grund |", "|---|---|---|"]
        for e in sorted(rej, key=lambda x: x["slug"]):
            lines.append(f"| {e['slug']} | {fmt(e.get('titel'))} | {fmt(e.get('stop_grund'))} |")
    else:
        lines.append("Keine.")
    lines.append("")

    # Läufe
    runs = sorted((ROOT / "ideas" / "_laeufe").glob("*.md"))
    lines += ["## Läufe", ""]
    if runs:
        lines += ["| Lauf | Thema | Ziel | Gefunden | Dedupe | Einschränkungen |", "|---|---|---|---|---|---|"]
        for r in runs:
            fm = parse_frontmatter(r.read_text(encoding="utf-8"))
            lines.append(f"| {fmt(fm.get('lauf'))} | {fmt(fm.get('thema'))} | {fmt(fm.get('ziel_anzahl'))} | {fmt(fm.get('gefunden'))} | {fmt(fm.get('dedupe_verworfen'))} | {fmt(fm.get('quellen_eingeschraenkt'))} |")
    else:
        lines.append("Noch keine Läufe.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    entries = load_entries()
    out = ROOT / "DASHBOARD.md"
    out.write_text(build(entries), encoding="utf-8")
    print(f"DASHBOARD.md geschrieben: {len(entries)} Einträge")
    return 0


if __name__ == "__main__":
    sys.exit(main())
