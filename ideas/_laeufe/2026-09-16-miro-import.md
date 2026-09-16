---
lauf: 2026-09-16-miro-import
datum: 2026-09-16
thema: Import Miro-Longlist „Nicegarden Scout Longlist" (Stand April 2026)
ziel_anzahl: 38
gefunden: 38
dedupe_verworfen: 0
quellen_eingeschraenkt: [kein Recherche-Lauf, nur Import; Miro-Karten enthalten nur VK-Spanne und SWOT]
---

# Lauf 2026-09-16 – Import Miro-Longlist

## Quelle
Miro-Board „Nicegarden Scout Longlist", https://miro.com/app/board/uXjVHmZbxI8=/ , Kanban „Scout Longlist nach Score", 38 Karten, ausgelesen 2026-09-16 über die Miro-Anbindung und als `data/raw/miro-longlist.csv` (ignoriert) gesichert. Import mit `python scripts/import_miro.py --skip bewaesserungskugeln-glas`.

## Zuordnung
| Miro | Repo |
|---|---|
| Lane A Empfohlen / B Pruefen / C Beobachten | `score: A/B/C`, `status: importiert` |
| Lane D Ablehnen | `score: D`, `status: abgelehnt`, `stop_grund` = Miro-Schwächen |
| Priority „Launch aktiv" (Bewaesserungskugeln Glas) | `products/NG0002/00-idee.md`, `status: produkt` |
| Priority „Voranalyse fertig" (Edelstahl-Pflanzsprüher) | `status: importiert`, `pipeline_status_miro: Voranalyse fertig`; Voranalyse-Dokument in Drive nicht gefunden → `[fehlt]` |
| Tags | `kategorie` (Bewässerung · Pflege & Werkzeug · Anzucht & Ranken · Gefäße & Deko) |
| Beschreibung „VK x-y EUR | STAERKEN | SCHWAECHEN | CHANCEN | RISIKEN" | `vk_spanne_eur`, SWOT-Tabelle |

## Ergebnis
| Lane | Anzahl | Status |
|---|---|---|
| A | 12 (davon 1 Produkt NG0002) | 11 importiert |
| B | 16 | importiert |
| C | 7 | importiert |
| D | 3 | abgelehnt |

Zusätzlich angelegt (nicht aus Miro):
- `products/NG0001/00-idee.md` – Edelstahl-Gießkanne, Bestandsprodukt (quelle: pafri)
- `ideas/eiskuebel-edelstahl.md`, `ideas/grillplatte-edelstahl.md` – Drive-Tiefenanalysen Nov 2025 ohne Miro-Karte, `status: beobachten` (quelle: drive)

## Dedupe
Keine Dubletten innerhalb der Longlist. Hinweise für spätere Läufe: „Pflanzstäbe / Rankstäbe", „Rankhilfen / Pflanzgitter", „Rankgitter Balkon" und „Moosstab Premium" sind verwandte Produkttypen (Rank-/Stützhilfen); „Sukkulenten-Töpfe Set", „Terracotta-Übertöpfe Set" und „Pflanzgefäß Edelstahl groß" sind Gefäße in verschiedenen Größen. Bei `/ideen` nicht erneut anlegen, sondern bestehende Dateien ergänzen.

## Einschränkungen
- Kein Recherche-Lauf: Kurzbeschreibung, Referenz-ASINs, Top-Anbieter, KPIs außer VK-Spanne fehlen und sind als `[fehlt]` markiert.
- VK-Spannen sind Pafris Schätzungen vom April 2026, keine aktuellen Amazon.de-Preise.
- Umlaute wurden aus dem ASCII-Export rekonstruiert (Pflanzspruecher → Pflanzsprüher usw.).

## Freigabeliste für Pafri
Kein Freigabeschritt: Import setzt nur `status: importiert`. Freigabe für `/voranalyse` erfolgt je Idee auf Zuruf oder über den ersten `/ideen`-Lauf.
