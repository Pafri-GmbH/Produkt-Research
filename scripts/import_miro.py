#!/usr/bin/env python3
"""Importiert data/raw/miro-longlist.csv als ideas/<slug>.md nach templates/ideensteckbrief.md.

CSV-Spalten (Export des Miro-Kanban „Scout Longlist nach Score"):
Title, Status, Description, Priority, Tags
Description-Format: "VK x-y EUR | STAERKEN … | SCHWAECHEN … | CHANCEN … | RISIKEN …"

Aufruf: python scripts/import_miro.py [--lauf 2026-09-16-miro-import] [--datum 2026-09-16]
Bestehende Dateien werden nicht überschrieben (Dedupe), sondern gemeldet.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANE = {"A Empfohlen": "A", "B Pruefen": "B", "C Beobachten": "C", "D Ablehnen": "D"}
KAT = {
    "Bewaesserung": "Bewässerung",
    "Pflege & Werkzeug": "Pflege & Werkzeug",
    "Anzucht & Ranken": "Anzucht & Ranken",
    "Gefaesse & Deko": "Gefäße & Deko",
}
UMLAUT_FIX = {  # Miro-Export ist ASCII; Titel für Anzeige zurückschreiben
    "Pflanzspruecher": "Pflanzsprüher", "Kraeuter": "Kräuter", "Toepfe": "Töpfe",
    "Staebe": "Stäbe", "staebe": "stäbe", "Bewaesserung": "Bewässerung",
    "Uebertoepfe": "Übertöpfe", "Duengestaebchen": "Düngestäbchen",
    "Vogeltraenke": "Vogeltränke", "Kuechen": "Küchen", "Kueche": "Küche",
    "Pflanzgefaess": "Pflanzgefäß", "Schuerze": "Schürze", "Rasenduenger": "Rasendünger",
    "Pflanzenstaender": "Pflanzenständer", "Giessstab": "Gießstab",
}


def slugify(title: str) -> str:
    s = title.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def pretty(title: str) -> str:
    for a, b in UMLAUT_FIX.items():
        title = title.replace(a, b)
    return title


def parse_desc(desc: str) -> dict:
    out = {"neu": False, "vk": None, "staerken": "", "schwaechen": "", "chancen": "", "risiken": ""}
    parts = [p.strip() for p in desc.split("|")]
    for p in parts:
        if p == "NEU":
            out["neu"] = True
        elif p.startswith("VK "):
            m = re.match(r"VK (\d+)-(\d+) EUR", p)
            if m:
                out["vk"] = [int(m.group(1)), int(m.group(2))]
        elif p.startswith("STAERKEN "):
            out["staerken"] = p[len("STAERKEN "):]
        elif p.startswith("SCHWAECHEN "):
            out["schwaechen"] = p[len("SCHWAECHEN "):]
        elif p.startswith("CHANCEN "):
            out["chancen"] = p[len("CHANCEN "):]
        elif p.startswith("RISIKEN "):
            out["risiken"] = p[len("RISIKEN "):]
    return out


def bullets(text: str) -> str:
    items = [t.strip() for t in text.split(",") if t.strip()]
    return "<br>".join(items) if items else "[fehlt]"


def render(row: dict, lauf: str, datum: str) -> tuple[str, str]:
    title = pretty(row["Title"].strip())
    slug = slugify(title)
    d = parse_desc(row["Description"])
    lane = LANE.get(row["Status"].strip(), "[fehlt]")
    kat = KAT.get(row["Tags"].strip(), row["Tags"].strip() or "[fehlt]")
    prio = row["Priority"].strip() or "Longlist"
    vk = f"[{d['vk'][0]}, {d['vk'][1]}]" if d["vk"] else "null"
    vk_txt = f"{d['vk'][0]}–{d['vk'][1]} € (Miro-Longlist, Stand April 2026, Schätzung)" if d["vk"] else "[fehlt]"
    neu = " (in Miro als NEU markiert)" if d["neu"] else ""
    ko = "[]"
    stop = "null"
    status = "importiert"
    if lane == "D":
        status = "abgelehnt"
        stop = f'"Miro-Lane D Ablehnen (April 2026): {d["schwaechen"]}"'
    fm = f"""---
slug: {slug}
titel: {title}
status: {status}
status_datum: {datum}
quelle: miro-longlist
lauf: {lauf}
kategorie: {kat}
vk_spanne_eur: {vk}
score: {lane}
score_gesamt: null
scores:
  marge: null
  markt: null
  usp: null
  risiko: null
ko_verstoss: {ko}
pipeline_status_miro: {prio}
gate_1: null
gate_2: null
gate_3: null
ng_nummer: null
stop_grund: {stop}
---
"""
    body = f"""
# {title}

## Kurzbeschreibung
[fehlt] – Miro-Karte enthält nur SWOT und VK-Spanne{neu}. Kurzbeschreibung wird bei `/voranalyse` oder im nächsten `/ideen`-Lauf ergänzt.

## Warum nicegarden
Kategorie laut Miro: **{kat}**. Markenfit-Begründung: [fehlt] (Anhaltspunkte in Stärken/Chancen unten).

## Markt-Ersteindruck
- Preisspanne Amazon.de: {vk_txt}
- Top-Anbieter (3): [fehlt]
- Saisonalität: [fehlt]
- Ersteinschätzung Lane: **{lane}** (Miro-Lane „{row['Status'].strip()}", April 2026). Pipeline-Status Miro: {prio}.

## SWOT
| Stärken | Schwächen |
|---|---|
| {bullets(d['staerken'])} | {bullets(d['schwaechen'])} |

| Chancen | Risiken |
|---|---|
| {bullets(d['chancen'])} | {bullets(d['risiken'])} |

## KPIs (Schätzungen, markiert)
| Kennzahl | Wert | Quelle / Schätzung |
|---|---|---|
| VK-Korridor | {vk_txt} | Miro-Longlist |
| ~Absatz Top-3 / Monat | [fehlt] | |
| ~EK Alibaba | [fehlt] | |
| Versandgewicht | [fehlt] | |

## Referenz-ASINs
- [fehlt]

## Quellen
- Miro-Board „Nicegarden Scout Longlist", https://miro.com/app/board/uXjVHmZbxI8=/ (Stand April 2026, importiert {datum})

## Offene Punkte
- Kurzbeschreibung, Referenz-ASINs, Top-Anbieter und KPIs fehlen (Import ohne Recherche).
"""
    return slug, fm + body


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=str(ROOT / "data/raw/miro-longlist.csv"))
    ap.add_argument("--lauf", default="2026-09-16-miro-import")
    ap.add_argument("--datum", default="2026-09-16")
    ap.add_argument("--skip", nargs="*", default=[], help="Slugs, die nicht angelegt werden (z. B. bereits Produkt)")
    a = ap.parse_args()

    created, skipped = [], []
    with open(a.csv, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            slug, text = render(row, a.lauf, a.datum)
            if slug in a.skip:
                skipped.append((slug, "skip-liste"))
                continue
            target = ROOT / "ideas" / f"{slug}.md"
            if target.exists():
                skipped.append((slug, "existiert"))
                continue
            target.write_text(text, encoding="utf-8")
            created.append(slug)
    print(f"angelegt: {len(created)}")
    for s in created:
        print("  +", s)
    if skipped:
        print(f"übersprungen: {len(skipped)}")
        for s, why in skipped:
            print("  -", s, f"({why})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
