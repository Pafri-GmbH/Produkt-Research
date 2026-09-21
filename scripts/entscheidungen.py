#!/usr/bin/env python3
"""Listet alle offenen Entscheidungen für Pafri aus dem Frontmatter in ideas/, pipeline/ und products/.

Aufruf: python scripts/entscheidungen.py [--md]
Ohne Option: Klartext für die Konsole. Mit --md: Markdown-Tabellen (für den Skill /entscheidungen).
Nutzt den Parser aus scripts/dashboard.py, keine weiteren Abhängigkeiten.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dashboard import ROOT, LANE_ORDER, fmt, load_entries, vk  # noqa: E402

GATE_STAGE = {"voranalyse": (1, "01-voranalyse.md", "/deep-dive"),
              "deep-dive": (2, "02-deep-dive.md", "/briefing"),
              "briefing": (3, "03-briefing.md", "NG-Nummer vergeben")}


def gate_block(e: dict) -> dict:
    """Liest Empfehlung und offene Punkte aus dem Gate-Block der aktuellen Stufen-Datei."""
    st = e.get("status")
    if st not in GATE_STAGE:
        return {}
    _, fname, _ = GATE_STAGE[st]
    path = ROOT / e["_pfad"] / fname
    if not path.exists():
        return {"empfehlung": "[Datei fehlt]", "offen": ""}
    text = path.read_text(encoding="utf-8")
    emp = re.findall(r"\*\*Empfehlung:\*\*\s*(.+)", text)
    off = re.findall(r"\*\*Offene Punkte / Datenlücken:\*\*\s*(.+)", text)
    return {"empfehlung": emp[-1].strip() if emp else "[fehlt]",
            "offen": off[-1].strip() if off else "–"}


def collect(entries: list[dict]) -> dict:
    gates = [e for e in entries if e.get("status") in GATE_STAGE and not e.get(f"gate_{GATE_STAGE[e['status']][0]}")]
    go_nicht_gestartet = [e for e in entries if e.get("status") in GATE_STAGE and e.get(f"gate_{GATE_STAGE[e['status']][0]}") == "go"]
    freigabe = [e for e in entries if e.get("status") == "idee"]
    freigegeben = [e for e in entries if e.get("status") == "freigegeben"]
    importiert = [e for e in entries if e.get("status") == "importiert"]
    beobachten = [e for e in entries if e.get("status") == "beobachten"]
    lane = lambda x: (LANE_ORDER.get(str(x.get("score")), 9), x["slug"])
    return {
        "gates": sorted(gates, key=lambda x: (-GATE_STAGE[x["status"]][0], x["slug"])),
        "go_nicht_gestartet": sorted(go_nicht_gestartet, key=lambda x: x["slug"]),
        "freigabe": sorted(freigabe, key=lane),
        "freigegeben": sorted(freigegeben, key=lambda x: x["slug"]),
        "importiert": sorted(importiert, key=lane),
        "beobachten": sorted(beobachten, key=lambda x: x["slug"]),
    }


def build_md(entries: list[dict]) -> str:
    c = collect(entries)
    L = [f"# Offene Entscheidungen – Stand {date.today().isoformat()}", ""]
    n_akt = len(c["gates"]) + len(c["freigabe"])
    L.append(f"Aktiv wartend: **{n_akt}** (Gates {len(c['gates'])}, Freigaben {len(c['freigabe'])}) · "
             f"Go ohne Start: {len(c['go_nicht_gestartet'])} · Freigegeben ohne Voranalyse: {len(c['freigegeben'])} · "
             f"Importiert (ungeprüft): {len(c['importiert'])} · Beobachten: {len(c['beobachten'])}")
    L.append("")

    L += ["## 1. Gates – Entscheidung Go / Stop / Beobachten / Nacharbeit", ""]
    if c["gates"]:
        L += ["| Gate | Slug | Titel | Gesamt | Empfehlung | Offene Punkte | Bei Go | Datei |", "|---|---|---|---|---|---|---|---|"]
        for e in c["gates"]:
            n, fname, nxt = GATE_STAGE[e["status"]]
            g = gate_block(e)
            L.append(f"| {n} | {e['slug']} | {fmt(e.get('titel'))} | {fmt(e.get('score_gesamt'))} | {g.get('empfehlung','–')} | {g.get('offen','–')} | `{nxt} {e['slug']}` | `{e['_pfad']}/{fname}` |")
    else:
        L.append("Keine offenen Gates.")
    L.append("")

    L += ["## 2. Freigabe für Voranalyse – neue Ideen aus `/ideen`", ""]
    if c["freigabe"]:
        L += ["| Lane | Slug | Titel | Kategorie | VK | Lauf | Datei |", "|---|---|---|---|---|---|---|"]
        for e in c["freigabe"]:
            L.append(f"| {fmt(e.get('score'))} | {e['slug']} | {fmt(e.get('titel'))} | {fmt(e.get('kategorie'))} | {vk(e)} | {fmt(e.get('lauf'))} | `{e['_pfad']}` |")
    else:
        L.append("Keine Ideen warten auf Freigabe.")
    L.append("")

    L += ["## 3. Entschieden, aber nicht gestartet", ""]
    rows = []
    for e in c["go_nicht_gestartet"]:
        n, _, nxt = GATE_STAGE[e["status"]]
        rows.append(f"| {e['slug']} | Gate {n} = go | `{nxt} {e['slug']}` |")
    for e in c["freigegeben"]:
        rows.append(f"| {e['slug']} | freigegeben | `/voranalyse {e['slug']}` |")
    if rows:
        L += ["| Slug | Stand | Nächster Schritt |", "|---|---|---|"] + rows
    else:
        L.append("Nichts offen.")
    L.append("")

    L += ["## 4. Importiert, noch nicht geprüft (Miro-Longlist)", ""]
    if c["importiert"]:
        L.append("Freigabe direkt möglich (`freigabe <slug>`) oder Prüfung im nächsten `/ideen`-Lauf.")
        L.append("")
        L += ["| Lane | Slug | Titel | Kategorie | VK | Miro-Stand |", "|---|---|---|---|---|---|"]
        for e in c["importiert"]:
            L.append(f"| {fmt(e.get('score'))} | {e['slug']} | {fmt(e.get('titel'))} | {fmt(e.get('kategorie'))} | {vk(e)} | {fmt(e.get('pipeline_status_miro'))} |")
    else:
        L.append("Keine.")
    L.append("")

    L += ["## 5. Beobachten – wieder aufnehmen oder ablehnen?", ""]
    if c["beobachten"]:
        L += ["| Slug | Titel | Seit | Grund |", "|---|---|---|---|"]
        for e in c["beobachten"]:
            L.append(f"| {e['slug']} | {fmt(e.get('titel'))} | {fmt(e.get('status_datum'))} | {fmt(e.get('stop_grund'))} |")
    else:
        L.append("Keine.")
    L.append("")
    return "\n".join(L)


def build_txt(entries: list[dict]) -> str:
    md = build_md(entries)
    out = []
    for line in md.splitlines():
        if line.startswith("|") and set(line.replace("|", "").strip()) <= set("-: "):
            continue
        line = line.replace("**", "").replace("`", "")
        out.append(re.sub(r"\s*\|\s*", "  ", line.strip("| ")) if line.startswith("|") else line)
    return "\n".join(out)


if __name__ == "__main__":
    entries = load_entries()
    print(build_md(entries) if "--md" in sys.argv else build_txt(entries))
