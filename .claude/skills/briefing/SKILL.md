---
name: briefing
description: Stufe 3 – Produktbriefing nach NG0001-Struktur, Teil A deutsch (Entscheidung), Teil B englisch (Sourcing-Spezifikation). Aufruf /briefing <slug>. Schreibt pipeline/<slug>/03-briefing.md, endet mit Gate-3-Block; bei Go Verschiebung nach products/NG00xx/.
---

# /briefing <slug>

## Vorbereitung
1. `DASHBOARD.md`, `rules/prozess.md`, `rules/schema.md`, `rules/briefing.md`, `rules/scoring.md` lesen.
2. `pipeline/<slug>/00-idee.md`, `01-voranalyse.md`, `02-deep-dive.md` lesen. `gate_2` muss `go` sein, sonst abbrechen und nachfragen.

## Schreiben
3. Teil A (deutsch) exakt in der Feldreihenfolge aus `rules/briefing.md`, Werte aus Deep-Dive Abschnitt K und L. Ziel-EK aus Alibaba-Spanne ableiten und Herleitung nennen. A.14 Entscheidungsgrundlage mit Margenrechnung und allen Annahmen.
4. Teil B (English) nach `rules/briefing.md`, jede Anforderung testbar formuliert. „Designed in Germany", nie „Made in Germany".
5. `pipeline/<slug>/03-briefing.md` mit Frontmatter (`stufe: briefing`, `datum`, `ziel_ek_eur`, `ziel_vk_eur`, `moq`, `fazit`). Scores unverändert.
6. Status `briefing` in `ideas/<slug>.md` und `00-idee.md`. `python scripts/dashboard.py`. Commit `feat(<slug>): briefing`.

## Abschluss
7. Gate-3-Block mit Vorschlag der nächsten freien NG-Nummer (aus `DASHBOARD.md`). Warten. Keine Mails, keine Anfragen, keine Bestellungen.
8. Bei Go durch Pafri: `ng_nummer` eintragen, `status: produkt`, `gate_3: go`, Ordner `git mv pipeline/<slug> products/NG00xx`, `ideas/<slug>.md` aktualisieren, Dashboard, Commit `gate(<slug>): go NG00xx`.
9. Bei Stop/Beobachten: Status + `stop_grund`, Ordner bleibt in `pipeline/`, Dashboard, Commit `gate(<slug>): …`.
