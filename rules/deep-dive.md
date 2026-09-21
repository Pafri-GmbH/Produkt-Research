# Tiefenanalyse (Deep-Dive) – Schema

Quelle: „Vorlage tiefgehende Analyse.xlsx" (Drive-ID `11x1qY0VdQbHE8v1NzXMQ1i_eHtkXv1VQ`, Tabelle1 „Tiefgehende Analyse"). Ausgefüllte Beispiele: „Bewässerungskugeln - tiefgehende Analyse.xlsx" (18.12.2025, 4 Mitbewerber), „Grillplatte tiefgehende Analyse.xlsx" (6 Mitbewerber), „Eiskübel tiefgehende Analyse.xlsx" (6 Mitbewerber). Die Zeilen sind 1:1 die Zeilen der Vorlage in Originalreihenfolge. Das Bewässerungskugeln-Beispiel hat gegenüber der Rohvorlage Zeilen ergänzt (ASIN, Artikelbezeichnung, Marke, Anzahl Kugeln, Preisbereich (1 Jahr), BSR Haupt-/Unterkategorie, Varianten, Notizen). Diese sind als **[Beispiel 2025]** markiert und werden übernommen, weil sie Pafris aktuelle Praxis sind.

Ausgabe: `pipeline/<slug>/02-deep-dive.md`, **Mustervorlage `templates/02-deep-dive.md` 1:1 kopieren und befüllen**. Abschnitte A–L sind die Vorlage; die mit [neu] markierten Abschnitte und Zeilen stammen aus Pafris Detaildokument (`vorlagen/detaildokument-analysen.md`, Abschnitt 2) und aus dem Rezensions-Mining. Zweck: aus einem Go-Kandidaten eine belastbare Entscheidungsgrundlage machen, aus der das Briefing (Teil B) geschrieben werden kann. Aufwand: 40–80 Suchen, Rezensionen lesen.

Die Vorlage ist eine Matrix: Zeilen = Merkmale, Spalten = Mitbewerber 1–5 (Vorlage) bzw. 1–6 (Praxis). Im Markdown: eine Tabelle je Abschnitt, Spalte 1 = Merkmal, dann eine Spalte je Mitbewerber. Mindestens 4, höchstens 6 Mitbewerber.

## 0. Executive Summary [neu]

Empfehlung in einem Satz, fünf Kernzahlen (Ziel-VK, Landed Cost, DB1 %, Break-even-ACOS, Kapitalbedarf Charge 1) mit Abweichung zur Voranalyse.

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

Cluster-Vorgabe: Funktion, Material/Haltbarkeit, Verpackung/Lieferung, Handhabung/Reinigung, Optik, Preis-Leistung. Nur Rezensionen mit Datum und Quelle, Häufigkeit als „x von y gelesenen". Positive Wiederholer („was Kunden lieben") als eigene Zeile.

## D3. Produktanforderungen aus Kundensicht [neu]

Tabelle Anforderung · Herkunft (welche Kritik / welches Lob) · Priorität Muss/Soll · Konsequenz für Spezifikation. Wichtigste Eingabe für das Briefing Teil B.

## E. Schwächen des Mitbewerbers (je Mitbewerber, Punkt 1–5)

## F. Stärken des Mitbewerbers (je Mitbewerber, Punkt 1–7)

## G. MEINE OPTIMIERUNGSANSÄTZE & USPs (Punkt 1–7, eine Spalte)

Jeder Ansatz mit Beleg aus D–F. Ergänzt [neu]: Preis-/Qualitäts-Karte (Mitbewerber und nicegarden-Zielposition), Listing-Ansatz (Titelstruktur, Bilder-Konzept, A+-Story), Ziel-VK mit Herleitung, Keyword-Cluster (Haupt, Long-Tail, Anwendung, Geschenk; Volumen-Spalte bleibt leer, wird nach dem Briefing manuell ergänzt).

## H. Validierung der Erkenntnisse: Chancen für den Markteinstieg (Punkt 1–5)

Ergänzt [neu]: Marktgröße als Bandbreite (Top-10-Absatz × Ø Preis), realistischer Marktanteil nach 6 und 12 Monaten, Absatzziel je Monat.

## I. Validierung der Erkenntnisse: Risiken für den Markteinstieg (Punkt 1–5)

Je Risiko [neu]: Eintrittswahrscheinlichkeit (niedrig / mittel / hoch), Auswirkung, konkrete Gegenmaßnahme. Anzahl „hoch" landet als `risiko_hoch` im Frontmatter.

## J. Schlussfolgerungen / Bewertung (Ja / Nein / Eventuell)

1. Passt das Produkt zu Nicegarden? [Beispiel 2025] (Vorlage: „Lässt sich eine Marke um das Produkt bauen?")
2. Ist eine gezielte Kundenansprache möglich?
3. Kann ich die Vermarktung deutlich besser machen?
4. Kann ich das Produkt / das Angebot verbessern?
5. Kann ich die Verpackung verbessern?

## K. Produktmerkmale & Informationen / Mein Wunschprodukt

Je Start-Variante eine Spalte (Empfehlung: max. 2). Materialien mit Edelstahl-Güte (304/430) und Finish; Verpackung mit FBA-Größenklasse und EPR-Materialfraktionen.

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

Nur lesend recherchierte Alibaba-/1688-Angebote (Preisspanne, MOQ, Lead Time). Spalte „Notizen" enthält bei Claude nie „kontaktiert" (Regel 9). Ergänzt [neu]: Sourcing-Anforderungen als Vorbereitung für Briefing Teil B (Lieferantentyp, MOQ-Erwartung, Sample-Prozess, Lead Time, Qualitätskriterien mit Rostbeständigkeit und Prüfmethode, Fragen an den Lieferanten).

## M. Detailkalkulation je Variante [neu]

Nach `rules/kalkulation.md`: EK, Fracht/Zoll/Nebenkosten, Landed Cost, Verkaufsgebühr, FBA-Versand, Lagerkosten, EPR/Verpackung, Retourenpauschale, Ads-Anteil → DB1 und DB2 in € und %, Break-even-ACOS, MOQ, Kapitalbedarf Charge 1. Dazu die Sensitivität (EK ± 15 %, CPC ± 30 %, VK −10 % / Ziel / +10 %) auf DB1 % und Break-even-ACOS.

## N. Compliance [neu]

GPSR (verantwortliche Person, Kennzeichnung), Verpackungsgesetz/LUCID, PPWR-Anforderungen an die Verpackung, Materialdeklaration, Amazon-Kategorie-Freigabe. Andere Marktplätze nur als Hinweis (Scope Amazon.de).

## O. Launch-Skizze [neu]

Ranking-Strategie (Learnings NG0001: Coupon-Push, TACoS-Steuerung, Ziel-BSR), Ads-Startbudget als Bandbreite, Zeitplan Sample → Order → Launch.

## Fazit und Scores

Empfehlung Go / Nacharbeit / Stop mit Begründung, aktualisierte Teilnoten (sechs Kriterien, Δ zur Voranalyse, belegte Zahlen) nach `rules/scoring.md`, `score_gesamt`, Zone, Lane, die zwei größten Unsicherheiten und wie sie geschlossen werden (Sample, H10-Export). Danach der Gate-Block aus `rules/prozess.md`; Zeile „Ergebnis" nennt Score, DB1, Break-even-ACOS vs. CPC und Kapitalbedarf. Go nur nach den Schwellen in `rules/scoring.md` Abschnitt 5.

Frontmatter der Datei trägt die Kennzahlen für das Dashboard (`rules/schema.md`): `vk_ziel`, `landed_cost`, `db1_prozent`, `db2_prozent`, `break_even_acos`, `moq`, `kapitalbedarf`, `varianten`, `risiko_hoch`, `empfehlung`, `unsicherheit_1`, `unsicherheit_2`. Stufe 2 überschreibt im Dashboard VK, DB1, BE-ACOS und Kapital aus Stufe 1; Score und Zone bleiben aus Stufe 1, bis der Deep-Dive sie aktualisiert.

## Hinweise zur Bearbeitung

- Absatz/Umsatz je Mitbewerber sind Schätzungen aus BSR (`~`, Quelle, Datum). Keine Helium-10-Werte erfinden.
- Amazon.de blockiert → `rules/quellen.md`. Fehlende Zellen `[fehlt]`.
- Abschnitt K (Wunschprodukt) und D3 (Produktanforderungen) sind die Brücke zum Briefing: jede Zeile wird in `03-briefing.md` Teil B wiederverwendet.
- Zahlen aus der Voranalyse übernehmen, nur mit Begründung ändern; Änderungen im Executive Summary ausweisen.
