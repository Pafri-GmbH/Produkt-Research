---
name: deep-dive
description: Stufe 2 – Tiefenanalyse nach Pafris xlsx-Vorlage mit 4–6 Wettbewerbern, Rezensions-Mining und Wunschprodukt. Aufruf /deep-dive <slug>. Schreibt pipeline/<slug>/02-deep-dive.md, endet mit Gate-2-Block.
---

# /deep-dive <slug>

## Vorbereitung
1. `DASHBOARD.md`, `rules/prozess.md`, `rules/schema.md`, `rules/deep-dive.md`, `rules/scoring.md`, `rules/kalkulation.md`, `rules/quellen.md` lesen. Danach `templates/02-deep-dive.md` (Gerüst) und `vorlagen/beispiel-tiefenanalyse-bewaesserungskugeln.md` (Detailtiefe) lesen.
2. `pipeline/<slug>/00-idee.md` und `01-voranalyse.md` lesen. `gate_1` muss `go` sein, sonst abbrechen und nachfragen.

## Recherche
3. 4–6 Wettbewerber wählen: Referenz-ASIN der Voranalyse, Marktführer, 1–2 Private-Label, 1 Niedrigpreis. ASINs im Frontmatter `wettbewerber`.
4. Alle Abschnitte 0 und A–O aus `rules/deep-dive.md` füllen, je Wettbewerber eine Spalte. Absatz/Umsatz als Schätzung aus BSR markieren. Leere Zellen `[fehlt]`, nie raten. Zahlen aus der Voranalyse übernehmen, Änderungen im Executive Summary ausweisen.
5. Abschnitt D: je Wettbewerber bis zu 7 kritische Rezensionen mit Datum. D2 (Rezensions-Mining) über alle Wettbewerber clustern, D3 (Produktanforderungen aus Kundensicht) daraus ableiten.
6. Abschnitt L Einkauf: Alibaba/1688 lesend, Preisspanne, MOQ, Lead Time. Kein Kontakt. Sourcing-Anforderungen für Briefing Teil B notieren.
7. Abschnitt K Wunschprodukt je Start-Variante (max. 2) vollständig ausfüllen; M Detailkalkulation je Variante mit Sensitivität nach `rules/kalkulation.md`; N Compliance; O Launch-Skizze.

## Schreiben
8. `pipeline/<slug>/02-deep-dive.md` = Kopie von `templates/02-deep-dive.md`, vollständig befüllt. Frontmatter inkl. Kennzahlen (`rules/schema.md`), `unsicherheit_1/2` gefüllt.
9. Sechs Teilnoten mit belegten Zahlen aktualisieren (Δ zur Voranalyse ausweisen), `score_gesamt`, Zone, Lane, Status `deep-dive` in `ideas/<slug>.md` und `00-idee.md`.
10. `python scripts/dashboard.py`. Commit `feat(<slug>): deep-dive`.

## Abschluss
11. Gate-2-Block (Zeile „Ergebnis" mit Score, DB1, Break-even-ACOS vs. CPC, Kapitalbedarf). Empfehlung Go nur nach `rules/scoring.md` Abschnitt 5 (Zone Go, DB1 ≥ 35 %, Break-even-ACOS über CPC-Niveau, kein Risiko „hoch" ohne Gegenmaßnahme); sonst Nacharbeit mit Nennung der fehlenden Zahl oder Stop. Im Chat nur Zusammenfassung (max. 10 Zeilen) + Gate-Block. Warten. Nie `/briefing` selbst starten.
12. Nach Entscheidung (im Chat oder per Dashboard-Button, abgeholt durch `/entscheidungen`): `gate_2`, ggf. Status + `stop_grund`, Dashboard, Commit `gate(<slug>): …`.
