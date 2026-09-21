#!/usr/bin/env python3
"""Erzeugt DASHBOARD.md und dashboard.html aus dem Frontmatter in ideas/, pipeline/ und products/.

Aufruf: python scripts/dashboard.py
Keine Abhängigkeiten außer der Standardbibliothek (kein PyYAML nötig).
"""
from __future__ import annotations

import json
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
REPO_URL = "https://github.com/Pafri-GmbH/Produkt-Research/blob/main/"
STAGE_FILES = ["03-briefing.md", "02-deep-dive.md", "01-voranalyse.md"]


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


def parse_body(text: str) -> dict:
    """Liest die Pflichtabschnitte des Steckbriefs für dashboard.html (Kurzbeschreibung, SWOT, KPIs, Offene Punkte)."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    body = text[m.end():] if m else text
    secs: dict[str, list[str]] = {}
    cur = None
    for line in body.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip()
            secs[cur] = []
        elif cur is not None:
            secs[cur].append(line)

    def sec(prefix: str) -> list[str]:
        for k, v in secs.items():
            if k.lower().startswith(prefix):
                return v
        return []

    def cells(row: str) -> list[str]:
        return [c.strip() for c in row.strip().strip("|").split("|")]

    def is_sep(row: str) -> bool:
        return set(row.replace("|", "").strip()) <= set("-: ")

    def items(cell: str) -> list[str]:
        return [x.strip() for x in re.split(r"<br\s*/?>", cell) if x.strip()]

    kurz = " ".join(l.strip() for l in sec("kurzbeschreibung") if l.strip()).strip()

    swot = {"s": [], "w": [], "o": [], "t": []}
    rows = [r for r in sec("swot") if r.strip().startswith("|") and not is_sep(r)]
    data_rows = [r for r in rows if not any(h in r for h in ("Stärken", "Staerken", "Chancen"))]
    if len(data_rows) >= 1:
        c = cells(data_rows[0]) + ["", ""]
        swot["s"], swot["w"] = items(c[0]), items(c[1])
    if len(data_rows) >= 2:
        c = cells(data_rows[1]) + ["", ""]
        swot["o"], swot["t"] = items(c[0]), items(c[1])

    kpis = []
    for r in sec("kpis"):
        if r.strip().startswith("|") and not is_sep(r):
            c = cells(r)
            if c and c[0] not in ("Kennzahl",):
                kpis.append([c[0], c[1] if len(c) > 1 else ""])

    offen = [l.strip()[2:].strip() for l in sec("offene punkte") if l.strip().startswith("- ")]
    return {"kurz": kurz, "swot": swot, "kpis": kpis, "offen": offen}


def parse_gate_block(text: str) -> dict | None:
    """Liest den Gate-Block (rules/prozess.md) aus einer Stufen-Datei: Empfehlung, Begründung, offene Punkte, nächster Schritt, Entscheidung."""
    m = re.search(r"^## Gate (\d):[^\n]*\n(.*?)(?:^---\s*$|\Z)", text, re.S | re.M)
    if not m:
        return None
    block = {"gate": int(m.group(1)), "empfehlung": "", "begruendung": "", "offen": "", "naechster": "", "entscheidung": ""}
    keys = {
        "empfehlung": "empfehlung", "begründung": "begruendung", "begruendung": "begruendung",
        "offene punkte": "offen", "nächster schritt": "naechster", "naechster schritt": "naechster",
        "deine entscheidung": "entscheidung",
    }
    cur = None
    for line in m.group(2).splitlines():
        fm = re.match(r"^\*\*(.+?)\*\*\s*:?\s*(.*)$", line.strip())
        if fm:
            label = fm.group(1).lower()
            cur = next((v for k, v in keys.items() if label.startswith(k)), None)
            if cur:
                block[cur] = fm.group(2).strip()
            continue
        if cur and line.strip():
            block[cur] = (block[cur] + " " + line.strip()).strip()
    block["empfehlung"] = block["empfehlung"].strip(" _*")
    return block


def parse_stage(folder: Path) -> dict | None:
    """Jüngste Stufen-Datei in pipeline/<slug>/ bzw. products/NG00xx/: Datei, Fazit, Gate-Block."""
    for name in STAGE_FILES:
        path = folder / name
        if path.exists():
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            return {
                "datei": str(path.relative_to(ROOT)),
                "stufe": fm.get("stufe") or name[3:-3],
                "datum": fm.get("datum"),
                "fazit": fm.get("fazit"),
                "gate_block": parse_gate_block(text),
            }
    return None


def load_entries() -> list[dict]:
    entries: dict[str, dict] = {}
    # Reihenfolge: ideas zuerst, pipeline/products überschreiben (haben Vorrang).
    for path in sorted((ROOT / "ideas").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm.get("slug"):
            fm["_pfad"] = str(path.relative_to(ROOT))
            fm["_body"] = parse_body(text)
            entries[fm["slug"]] = fm
    for base in ("pipeline", "products"):
        for path in sorted((ROOT / base).glob("*/00-idee.md")):
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if fm.get("slug"):
                fm["_pfad"] = str(path.parent.relative_to(ROOT))
                fm["_body"] = parse_body(text)
                fm["_stufe"] = parse_stage(path.parent)
                entries[fm["slug"]] = fm
    return list(entries.values())


def load_runs() -> list[dict]:
    runs = []
    for r in sorted((ROOT / "ideas" / "_laeufe").glob("*.md")):
        runs.append(parse_frontmatter(r.read_text(encoding="utf-8")))
    return runs


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
    runs = load_runs()
    lines += ["## Läufe", ""]
    if runs:
        lines += ["| Lauf | Thema | Ziel | Gefunden | Dedupe | Einschränkungen |", "|---|---|---|---|---|---|"]
        for fm in runs:
            lines.append(f"| {fmt(fm.get('lauf'))} | {fmt(fm.get('thema'))} | {fmt(fm.get('ziel_anzahl'))} | {fmt(fm.get('gefunden'))} | {fmt(fm.get('dedupe_verworfen'))} | {fmt(fm.get('quellen_eingeschraenkt'))} |")
    else:
        lines.append("Noch keine Läufe.")
    lines.append("")
    return "\n".join(lines)


def build_html(entries: list[dict], runs: list[dict]) -> str:
    """Füllt scripts/dashboard_template.html mit den Daten (JSON im <script id="data">)."""
    def num(v):
        return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None

    rows = []
    for e in entries:
        s = e.get("vk_spanne_eur")
        vk_min = vk_max = None
        if isinstance(s, list) and len(s) == 2:
            vk_min, vk_max = num(s[0]), num(s[1])
        scores = e.get("scores") if isinstance(e.get("scores"), dict) else {}
        body = e.get("_body", {})
        rows.append({
            "slug": e.get("slug"),
            "titel": e.get("titel") or e.get("slug"),
            "status": e.get("status"),
            "status_datum": e.get("status_datum"),
            "quelle": e.get("quelle"),
            "lauf": e.get("lauf"),
            "kategorie": e.get("kategorie"),
            "vk_min": vk_min,
            "vk_max": vk_max,
            "score": e.get("score") if e.get("score") in ("A", "B", "C", "D") else None,
            "score_gesamt": num(e.get("score_gesamt")),
            "scores": {k: num(scores.get(k)) for k in ("marge", "markt", "usp", "risiko")},
            "ko_verstoss": [str(x) for x in e.get("ko_verstoss") or [] if x is not None],
            "pipeline_status_miro": e.get("pipeline_status_miro"),
            "gate_1": e.get("gate_1"),
            "gate_2": e.get("gate_2"),
            "gate_3": e.get("gate_3"),
            "ng_nummer": e.get("ng_nummer"),
            "stop_grund": e.get("stop_grund"),
            "pfad": e.get("_pfad"),
            "kurz": body.get("kurz", ""),
            "swot": body.get("swot", {}),
            "kpis": body.get("kpis", []),
            "offen": body.get("offen", []),
            "github_url": REPO_URL + (e.get("_pfad") or ""),
            "stufe": e.get("_stufe"),
        })
    run_rows = [{
        "lauf": r.get("lauf"), "thema": r.get("thema"), "ziel_anzahl": r.get("ziel_anzahl"),
        "gefunden": r.get("gefunden"), "dedupe_verworfen": r.get("dedupe_verworfen"),
        "quellen_eingeschraenkt": r.get("quellen_eingeschraenkt"),
    } for r in runs]
    data = {"stand": date.today().isoformat(), "next_ng": next_ng(entries), "repo_url": REPO_URL, "entries": rows, "runs": run_rows}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    template = (ROOT / "scripts" / "dashboard_template.html").read_text(encoding="utf-8")
    return template.replace("__DATA__", payload)


def main() -> int:
    entries = load_entries()
    runs = load_runs()
    (ROOT / "DASHBOARD.md").write_text(build(entries), encoding="utf-8")
    (ROOT / "dashboard.html").write_text(build_html(entries, runs), encoding="utf-8")
    print(f"DASHBOARD.md und dashboard.html geschrieben: {len(entries)} Einträge")
    return 0


if __name__ == "__main__":
    sys.exit(main())
