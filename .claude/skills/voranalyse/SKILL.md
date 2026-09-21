---
name: voranalyse
description: Stufe 1 – Voranalyse nach Pafris 22-Punkte-Checkliste für eine freigegebene Idee. Aufruf /voranalyse <slug>. Schreibt pipeline/<slug>/00-idee.md und 01-voranalyse.md, vergibt Einzelscores, endet mit Gate-1-Block.
---

# /voranalyse <slug>

## Vorbereitung
1. `DASHBOARD.md`, `rules/prozess.md`, `rules/schema.md`, `rules/voranalyse.md`, `rules/scoring.md`, `rules/kalkulation.md`, `rules/quellen.md` lesen. Danach `templates/01-voranalyse.md` (Gerüst) und `vorlagen/beispiel-voranalyse-bewaesserungskugeln.md` (Detailtiefe, Tonfall) lesen.
2. `ideas/<slug>.md` lesen. Status muss `freigegeben` (oder `importiert`/`idee` mit ausdrücklicher Anweisung von Pafri) sein, sonst abbrechen und nachfragen.

## Recherche
3. Referenz-ASIN festlegen (Hauptkonkurrent mit bestem Ranking). Amazon.de blockiert → `rules/quellen.md`.
4. Alle 22 Prüfpunkte in Originalreihenfolge bearbeiten, danach Block 4 (Nr. 23–30: Keywords, Top-Listings, Markteintritt, Kalkulation, Differenzierung, IP, Compliance/Logistik, Risiken). Spalte „Erklärung" unverändert aus `rules/voranalyse.md`. Kein Punkt leer: Befund mit Quelle/Datum, Schätzung markiert oder `[fehlt]`. Zahlen nach `rules/kalkulation.md` kennzeichnen.
5. Nr. 22 Alibaba nur lesend. Kalkulation (Nr. 26) mit einer Variante und Pauschalen; EK ohne Angebot nach 30-%-Regel.

## Schreiben
6. `pipeline/<slug>/00-idee.md` = Kopie von `ideas/<slug>.md`.
7. `pipeline/<slug>/01-voranalyse.md` = Kopie von `templates/01-voranalyse.md`, vollständig befüllt, kein Abschnitt entfernt. Frontmatter inkl. Kennzahlen (`rules/schema.md`); `score` darf nicht leer sein.
8. Fazit in fünf Zeilen + sechs Teilnoten mit je einem Begründungssatz + `score_gesamt` (0–100), Zone, Lane nach `rules/scoring.md`. K.O. → `ko_verstoss` füllen, `score: D`, `ko: ja: K…`.
9. Status in `ideas/<slug>.md` und `00-idee.md`: `status: voranalyse`, `status_datum`, `scores` (sechs Keys), `score_gesamt`, `score` (Lane aus Gesamtscore).
10. `python scripts/dashboard.py`. Commit `feat(<slug>): voranalyse`.

## Abschluss
11. Gate-1-Block aus `rules/prozess.md` (Zeile „Ergebnis" mit Score, Zone, DB1, Break-even-ACOS). Empfehlung strikt nach Zone (Go ≥ 70, Review 50–69, Reject < 50); bei Review die 1–2 kippenden Kriterien nennen; Red Flags → Stop. Im Chat nur Zusammenfassung (max. 10 Zeilen) + Gate-Block. Warten. Nie `/deep-dive` selbst starten.
12. Nach Pafris Entscheidung (im Chat oder per Dashboard-Button, abgeholt durch `/entscheidungen`): `gate_1` setzen, bei Stop/Beobachten Status + `stop_grund`, Dashboard, Commit `gate(<slug>): go deep-dive` bzw. `stop` / `beobachten`.
