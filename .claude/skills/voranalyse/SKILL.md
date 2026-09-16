---
name: voranalyse
description: Stufe 1 – Voranalyse nach Pafris 22-Punkte-Checkliste für eine freigegebene Idee. Aufruf /voranalyse <slug>. Schreibt pipeline/<slug>/00-idee.md und 01-voranalyse.md, vergibt Einzelscores, endet mit Gate-1-Block.
---

# /voranalyse <slug>

## Vorbereitung
1. `DASHBOARD.md`, `rules/prozess.md`, `rules/schema.md`, `rules/voranalyse.md`, `rules/scoring.md`, `rules/quellen.md` lesen.
2. `ideas/<slug>.md` lesen. Status muss `freigegeben` (oder `importiert`/`idee` mit ausdrücklicher Anweisung von Pafri) sein, sonst abbrechen und nachfragen.

## Recherche
3. Referenz-ASIN festlegen (Hauptkonkurrent mit bestem Ranking). Amazon.de blockiert → `rules/quellen.md`.
4. Alle 22 Prüfpunkte in Originalreihenfolge bearbeiten. Spalte „Erklärung" unverändert aus `rules/voranalyse.md`. Kein Punkt leer: Befund mit Quelle/Datum, Schätzung markiert oder `[fehlt]`.
5. Nr. 22 Alibaba nur lesend.

## Schreiben
6. `pipeline/<slug>/00-idee.md` = Kopie von `ideas/<slug>.md`.
7. `pipeline/<slug>/01-voranalyse.md` nach `rules/voranalyse.md` mit Frontmatter (`stufe: voranalyse`, `datum`, `referenz_asin`, `hauptkategorie`, `fazit`).
8. Fazit + vier Einzelscores + `score_gesamt` nach `rules/scoring.md`. K.O. → `ko_verstoss` füllen, `score: D`.
9. Status in `ideas/<slug>.md` und `00-idee.md`: `status: voranalyse`, `status_datum`, `scores`, `score_gesamt`, `score` (Lane aus Gesamt-Score).
10. `python scripts/dashboard.py`. Commit `feat(<slug>): voranalyse`.

## Abschluss
11. Gate-1-Block aus `rules/prozess.md`. Empfehlung Go nur bei `score_gesamt ≥ 6,5` und ohne K.O. Warten. Nie `/deep-dive` selbst starten.
12. Nach Pafris Entscheidung: `gate_1` setzen, bei Stop/Beobachten Status + `stop_grund`, Dashboard, Commit `gate(<slug>): go deep-dive` bzw. `stop` / `beobachten`.
