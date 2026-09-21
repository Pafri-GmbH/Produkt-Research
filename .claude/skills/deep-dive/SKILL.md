---
name: deep-dive
description: Stufe 2 – Tiefenanalyse nach Pafris xlsx-Vorlage mit 4–6 Wettbewerbern, Rezensions-Mining und Wunschprodukt. Aufruf /deep-dive <slug>. Schreibt pipeline/<slug>/02-deep-dive.md, endet mit Gate-2-Block.
---

# /deep-dive <slug>

## Vorbereitung
1. `DASHBOARD.md`, `rules/prozess.md`, `rules/schema.md`, `rules/deep-dive.md`, `rules/scoring.md`, `rules/quellen.md` lesen.
2. `pipeline/<slug>/00-idee.md` und `01-voranalyse.md` lesen. `gate_1` muss `go` sein, sonst abbrechen und nachfragen.

## Recherche
3. 4–6 Wettbewerber wählen: Referenz-ASIN der Voranalyse, Marktführer, 1–2 Private-Label, 1 Niedrigpreis. ASINs im Frontmatter `wettbewerber`.
4. Alle Abschnitte A–L aus `rules/deep-dive.md` je Wettbewerber füllen. Absatz/Umsatz als Schätzung aus BSR markieren. Leere Zellen `[fehlt]`, nie raten.
5. Abschnitt D: je Wettbewerber bis zu 7 kritische Rezensionen mit Datum. Abschnitt D2 (Rezensions-Mining) über alle Wettbewerber clustern.
6. Abschnitt L Einkauf: Alibaba/1688 lesend, Preisspanne + MOQ. Kein Kontakt.
7. Abschnitt K Wunschprodukt vollständig ausfüllen; das ist die Grundlage für das Briefing.

## Schreiben
8. `pipeline/<slug>/02-deep-dive.md` mit Frontmatter (`stufe: deep-dive`, `datum`, `wettbewerber`, `fazit`).
9. Scores aktualisieren (belegte Zahlen), `score_gesamt`, Status `deep-dive` in `ideas/<slug>.md` und `00-idee.md`.
10. `python scripts/dashboard.py`. Commit `feat(<slug>): deep-dive`.

## Abschluss
11. Gate-2-Block. Empfehlung Go nur bei `score_gesamt ≥ 7,5` und ohne K.O. Warten. Nie `/briefing` selbst starten.
12. Nach Entscheidung (im Chat oder per Dashboard-Button, abgeholt durch `/entscheidungen`): `gate_2`, ggf. Status + `stop_grund`, Dashboard, Commit `gate(<slug>): …`.
