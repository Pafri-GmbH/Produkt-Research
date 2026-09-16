# Tiefenanalyse (Deep-Dive) – Schema

Quelle: „Vorlage tiefgehende Analyse.xlsx" (Drive-ID `11x1qY0VdQbHE8v1NzXMQ1i_eHtkXv1VQ`, Tabelle1 „Tiefgehende Analyse"). Ausgefüllte Beispiele: „Bewässerungskugeln - tiefgehende Analyse.xlsx" (18.12.2025, 4 Mitbewerber), „Grillplatte tiefgehende Analyse.xlsx" (6 Mitbewerber), „Eiskübel tiefgehende Analyse.xlsx" (6 Mitbewerber). Die Zeilen sind 1:1 die Zeilen der Vorlage in Originalreihenfolge. Das Bewässerungskugeln-Beispiel hat gegenüber der Rohvorlage Zeilen ergänzt (ASIN, Artikelbezeichnung, Marke, Anzahl Kugeln, Preisbereich (1 Jahr), BSR Haupt-/Unterkategorie, Varianten, Notizen). Diese sind als **[Beispiel 2025]** markiert und werden übernommen, weil sie Pafris aktuelle Praxis sind.

Ausgabe: `pipeline/<slug>/02-deep-dive.md`. Die Vorlage ist eine Matrix: Zeilen = Merkmale, Spalten = Mitbewerber 1–5 (Vorlage) bzw. 1–6 (Praxis). Im Markdown: eine Tabelle je Abschnitt, Spalte 1 = Merkmal, dann eine Spalte je Mitbewerber. Mindestens 4, höchstens 6 Mitbewerber.

## Kopf

| Feld | |
|---|---|
| Produkt / Nische | |
| Bearbeiter | claude |
| Datum | ISO |
| Herstelleranfrage | „nicht eingeleitet" (Regel 9: keine Kontakte). Pafri setzt „wird eingeleitet". |

## A. Angebotsdetails / Marktdaten (je Mitbewerber)

1. Produktbild (Link)
2. ASIN [Beispiel 2025]
3. Artikelbezeichnung [Beispiel 2025]
4. Marke [Beispiel 2025] (Vorlage: „Hersteller")
5. Herkunft Seller
6. Abwicklung Vertrieb (FBA / MFN)
7. Aktueller Preis
8. Anzahl / Setumfang im Angebot [Beispiel 2025, dort „Anzahl Kugeln"]
9. Preisbereich (1 Jahr)
10. Häufigste Preisstellung
11. Erhältlich seit
12. BSR Hauptkategorie
13. Hauptkategorie
14. BSR Unterkategorie [Beispiel 2025]
15. Unterkategorie [Beispiel 2025]
16. Verkäufe im Monat (Schätzung, markieren)
17. Umsatz im Monat (Schätzung, markieren)
18. Varianten [Beispiel 2025]
19. Verkaufshistorie
20. Anzahl der Bewertungen
21. Bewertungsschnitt
22. Zielgruppe / Käuferschaft
23. Notizen [Beispiel 2025]

## B. Produkteigenschaften & Merkmale des Marktes (je Mitbewerber)

1. Größe Produkteinheit
2. Gewicht (Versand)
3. Abmaße (Versand)
4. Materialien
5. Farbe
6. Variantenvielfalt
7. Anzahl der Varianten
8. Anzahl / Setumfang
9. Qualitätsmerkmale / Siegel
10. Verpackungsart
11. Kennzeichnungspflichten
12. Prüfungen
13. Schutzrechte
14. Besonderheiten / USP

## C. Vermarktung & Optimierung (je Mitbewerber)

1. Anzahl Produktbilder
2. Qualität des Titelbildes (x/10)
3. Qualität der Produktbilder (x/10)
4. Qualität der Verkaufstexte (x/10)
5. Erweiterte Beschreibung geschaltet (A+: x/10 bzw. nein)

## D. Kritische Kundenmeinungen (je Mitbewerber)

Rezension 1 bis Rezension 7, danach **Zusammenfassung** je Mitbewerber (Vorlage: eine Zeile „Zusammenfassung").

## D2. Rezensions-Mining [neu]

Ergänzt Abschnitt D um eine Auswertung über alle Mitbewerber hinweg, weil der Prozess ohne Helium 10 stärker auf Rezensionen als Datenquelle angewiesen ist.

| Thema (Cluster) | Nennungen (≈) | Mitbewerber betroffen | Beispielzitat | Ableitung für unser Produkt |
|---|---|---|---|---|

Cluster-Vorgabe: Funktion, Material/Haltbarkeit, Verpackung/Lieferung, Handhabung/Reinigung, Optik, Preis-Leistung. Nur Rezensionen mit Datum und Quelle. Positive Wiederholer („was Kunden lieben") als eigene Zeile.

## E. Schwächen des Mitbewerbers (je Mitbewerber, Punkt 1–5)

## F. Stärken des Mitbewerbers (je Mitbewerber, Punkt 1–7)

## G. MEINE OPTIMIERUNGSANSÄTZE & USPs (Punkt 1–7, eine Spalte)

## H. Validierung der Erkenntnisse: Chancen für den Markteinstieg (Punkt 1–5)

## I. Validierung der Erkenntnisse: Risiken für den Markteinstieg (Punkt 1–5)

## J. Schlussfolgerungen / Bewertung (Ja / Nein / Eventuell)

1. Passt das Produkt zu Nicegarden? [Beispiel 2025] (Vorlage: „Lässt sich eine Marke um das Produkt bauen?")
2. Ist eine gezielte Kundenansprache möglich?
3. Kann ich die Vermarktung deutlich besser machen?
4. Kann ich das Produkt / das Angebot verbessern?
5. Kann ich die Verpackung verbessern?

## K. Produktmerkmale & Informationen / Mein Wunschprodukt

1. Gewicht (Versand)
2. Abmaße (Versand)
3. Materialien
4. Besondere Eigenschaften (mehrere Zeilen möglich)
5. Farbe / Farbvarianten
6. Variantenvielfalt
7. Anzahl der Varianten
8. Qualitätsmerkmale / Siegel
9. Verpackungsart
10. Kennzeichnungspflichten
11. erforderliche Prüfungen
12. Target-Verkaufspreis
13. Erwartungen (Absatz/Monat)
14. Mindestbestellmenge

## L. Einkauf [Beispiel 2025]

| Link | EK | Mindestbestellmenge | Notizen |
|---|---|---|---|

Nur lesend recherchierte Alibaba-/1688-Angebote (Preisspanne, MOQ). Spalte „Notizen" enthält bei Claude nie „kontaktiert" (Regel 9).

## Fazit und Scores

Aktualisierte Einzelscores (Marge, Markt, USP, Risiko) mit belegten Zahlen nach `rules/scoring.md`, `score_gesamt`, danach der Gate-Block aus `rules/prozess.md`.

## Hinweise zur Bearbeitung

- Absatz/Umsatz je Mitbewerber sind Schätzungen aus BSR (`~`, Quelle, Datum). Keine Helium-10-Werte erfinden.
- Amazon.de blockiert → `rules/quellen.md`. Fehlende Zellen `[fehlt]`.
- Abschnitt K (Wunschprodukt) ist die Brücke zum Briefing: jede Zeile wird in `03-briefing.md` Teil B wiederverwendet.
