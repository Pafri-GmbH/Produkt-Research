---
stufe: deep-dive
slug: pflanzenetiketten-metall
datum: 2026-11-14
bearbeiter: claude
quellen_stand: 2026-11-14
quellen_eingeschraenkt: [amazon.de Rezensionsseiten erfordern Login (nur Produktseiten-Rezensionen gelesen), amazon.de Captcha bis Freigabe token.awswaf.com (2026-11-13), alibaba.com Abruf nicht freigegeben (nur Suchmaschinen-Snippets), Keepa/Preisverlauf nicht verfügbar, Google Trends nicht abgerufen, DPMA/EUIPO/DPMAregister Design nicht abgefragt]
wettbewerber: [B00814L088, B07V4297ZC, B0G23L9HR4, B0FMQVGDX2, B0GZPBF5Z6, B08F5HMWG1]
fazit: Stop – auch mit Alibaba-Richtpreis (~0,30 €/Stecker) nur DB1 ~26 % und Break-even-ACOS ~22 % im CPC-Band; Stift-USP ist inzwischen Standard, Segment ~220 St./Monat; Go erst bei belegtem EK ≤ ~4,80 € je 20er-Set.
vk_ziel: 24,90 €
landed_cost: ~7,88 €
db1_prozent: ~26 %
db2_prozent: ~9 %
break_even_acos: ~22 %
moq: ~500 Sets
kapitalbedarf: ~5.400 €
varianten: 1
risiko_hoch: 3
empfehlung: Stop
unsicherheit_1: EK für 0,5-mm-Edelstahl-304-Stecker, vernietet, mit Stift und Box (Basis nur Alibaba-Snippets 0,14–0,35 €/Stk, keine Dicke angegeben) – schließen durch RFQ von Pafri bei 3 Lieferanten mit Zielpreis ≤ 4,80 € je 20er-Set
unsicherheit_2: Absatz/Saisonfaktor (BSR-Schätzung aus Nebensaison Okt/Nov, kein Keepa/H10, kein Google Trends) – schließen durch H10-/Keepa-Export der 6 Wettbewerber über 12 Monate
---

# Tiefenanalyse – Pflanzenetiketten Metall (pflanzenetiketten-metall)

> Alle Abschnitte bleiben stehen. Zahlen aus der Voranalyse werden übernommen; Änderungen in Abschnitt 0 ausweisen. Kennzeichnung nach `rules/kalkulation.md`. Schema: `rules/deep-dive.md` (Abschnitte A–L 1:1 aus Pafris xlsx-Vorlage, Ergänzungen [neu]).

> **Quellen dieses Laufs (2026-11-13/14):** Amazon.de über `scripts/amazon.mjs`: 8 Produktseiten (6 Wettbewerber + GardenMate Mini/Hook), 2 Suchen Seite 1, Autocomplete. Lieferort 10115 Berlin. Am 2026-11-13 zunächst Captcha (Exit 2), weil der AWS-WAF-Host der Umgebung fehlte; nach Freigabe von `…token.awswaf.com` ok. Rezensionsseiten verlangen Login → je Wettbewerber nur die bis zu 10 Rezensionen der Produktseite; kritische Rezensionen daher wenige, ergänzt um Varianten desselben Parents (GardenMate Mini/Hook). Alibaba nur über Suchmaschinen-Snippets (Abruf der Seite nicht freigegeben). Absatz = Schätzung aus BSR nach `rules/quellen.md` (Potenzkurve durch BSR 445 ≈ 700 und BSR 3.000 ≈ 200 St./Monat). Abrufzeitpunkt November = Nebensaison.

## 0. Executive Summary [neu]

**Empfehlung:** Stop – der Alibaba-Richtpreis bestätigt die Red Flag der Voranalyse statt sie aufzulösen (DB1 ~26 %, Break-even-ACOS ~22 % im CPC-Band ~16–28 %), und die geplante Differenzierung „Stift im Set“ ist seit Sommer 2026 Marktstandard (Bamworld, drei Edelstahl-304-Neulinge).

| Kernzahl | Wert | Δ zur Voranalyse |
|---|---|---|
| Ziel-VK | 24,90 € (20 Stecker) | unverändert |
| Landed Cost | ~7,88 € (EK ~6,80 € aus Alibaba-Snippets statt 30-%-Regel ~7,47 €) | −0,69 € (Voranalyse ~8,57 €) |
| DB1 % | ~26 % (5,41 €) | +3 Pp (Voranalyse ~23 %) |
| Break-even-ACOS | ~22 % | +3 Pp (Voranalyse ~19 %), weiter unter CPC-Obergrenze ~28 % |
| Kapitalbedarf Charge 1 | ~5.400 € (500 Sets × 7,88 € + 1.500 €) | −400 € (Voranalyse ~5.800 €) |

Weitere Änderungen ggü. Voranalyse: BSR GardenMate 12.386 → 18.876 (Nebensaison, ~80 → ~60 St./Monat, Schätzung aus BSR); Metall-Segment ~165 → ~220 St./Monat (Schätzung aus BSR, neu: Bamworld B0FMQVGDX2 ~40, U/B ~40); Preis STARTOSTAR 25,80 € → 20,43 €; Teilnote Wettbewerb 5 → 4, Marge 3 → 4; Score 50 → 50.

## Kopf

| Feld | |
|---|---|
| Produkt / Nische | Pflanzenschilder / Pflanzenstecker Metall zum Beschriften (Edelstahl 304), Garten › Pflanzenschilder |
| Bearbeiter | claude |
| Datum | 2026-11-14 |
| Herstelleranfrage | nicht eingeleitet |

Auswahl Mitbewerber (6): M1 Referenz-ASIN der Voranalyse und Marktführer Metall (GardenMate Large) · M2 meiste Bewertungen und niedrigster Stückpreis Metall (STARTOSTAR, 0,68 €/Stk) · M3 Private Label China (KINGLAKE) · M4 Private Label, jüngster Aufsteiger mit Stift im Set (Bamworld) · M5 direktes Material-Pendant Edelstahl 304 mit Stift (EfforPrac) · M6 Premium-/Design-Anbieter Schiefer (Hoberg).

## A. Angebotsdetails / Marktdaten

| Merkmal | M1 GardenMate | M2 STARTOSTAR | M3 KINGLAKE | M4 Bamworld | M5 EfforPrac | M6 Hoberg |
|---|---|---|---|---|---|---|
| Produktbild (Link) | https://www.amazon.de/dp/B00814L088 | https://www.amazon.de/dp/B07V4297ZC | https://www.amazon.de/dp/B0G23L9HR4 | https://www.amazon.de/dp/B0FMQVGDX2 | https://www.amazon.de/dp/B0GZPBF5Z6 | https://www.amazon.de/dp/B08F5HMWG1 |
| ASIN | B00814L088 | B07V4297ZC | B0G23L9HR4 | B0FMQVGDX2 | B0GZPBF5Z6 | B08F5HMWG1 |
| Artikelbezeichnung | 25x Pflanzenschilder Typ Large aus Metall, 30 cm, Feld 9 × 3 cm | Metall Pflanzenstecker … 30er Set | 27 cm Pflanzenschilder Metall, 25 Stück, Silber | Pflanzenschilder Metall 30 Stück mit Stift | 10 Stück Pflanzenmarker aus 304 Edelstahl mit Marker | Schiefer-Pflanzschilder 10er Set, Erdspieße Stahl, 9 × 7 cm |
| Marke | GardenMate (AllMates GmbH) | STARTOSTAR | KINGLAKE (JH Gardening) | Bamworld | EfforPrac | Hoberg |
| Herkunft Seller | Deutschland (AllMates GmbH; Herkunftsland laut Produktdaten USA) (Amazon.de, 2026-11-13) | China (Verkäufer „Dragonfly mall“, Listing-Hinweis „aus dem Ausland verkauft“) (Amazon.de, 2026-11-13) | China (JH Gardening, Herkunft China) (Amazon.de, 2026-11-13) | China (Herkunft China) (Amazon.de, 2026-11-14) | China (ElegantPick, Herkunft China) (Amazon.de, 2026-11-13) | Deutschland (DS e-Sales GmbH) (Amazon.de, 2026-11-13) |
| Abwicklung Vertrieb (FBA / MFN) | FBA | FBA | FBA | FBA | MFN (Versender = Verkäufer ElegantPick) | FBA |
| Aktueller Preis | 27,70 € (Amazon.de, 2026-11-13) | 20,43 € (Listenpreis 25,10 €) (Amazon.de, 2026-11-13) | 21,09 € (Amazon.de, 2026-11-13) | 22,20 € (Amazon.de, 2026-11-14) | 15,05 € (Amazon.de, 2026-11-13) | 26,64 € (Amazon.de, 2026-11-13) |
| Anzahl / Setumfang im Angebot | 25 Stk. (1,11 €/Stk.) | 30 Stk. (0,68 €/Stk.) | 25 Stk. (0,84 €/Stk.) | 30 Stk. + Stift (0,74 €/Stk.) | 10 Stk. + Stift (1,51 €/Stk.) | 10 Stk. (2,66 €/Stk.) |
| Preisbereich (1 Jahr) | [fehlt] (Keepa nicht verfügbar); beobachtet 28,02 € (2026-10-19) → 27,70 € (2026-11-13) | [fehlt]; 25,80 € (2026-10-19) → 20,43 € (2026-11-13); Rezension 2022: 50er-Pack 39,99 € → deutlich höher | [fehlt]; 21,33 € → 21,09 € | [fehlt]; 22,20 € (2026-11-14) | [fehlt]; 15,22 € → 15,05 € | [fehlt]; 26,94 € → 26,64 €; Parallel-ASIN B0868ZQ4Z3 30,40 € |
| Häufigste Preisstellung | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |
| Erhältlich seit | [fehlt]; ~2012–2014 (Schätzung: ASIN-Präfix B008, älteste Rezension 2014-09-23) | [fehlt]; ~2019 (Schätzung: ASIN-Präfix B07V) | [fehlt]; ~2025 (Schätzung: ASIN-Präfix B0G2; Bewertungen vom Vorgänger-Parent übernommen, Rezension 2024-04-13) | [fehlt]; ~2025 (Schätzung: ASIN-Präfix B0FM, älteste Rezension 2026-06-09) | [fehlt]; ~2026 (Schätzung: ASIN-Präfix B0GZ, 0 Bewertungen) | [fehlt]; ~2020 (Schätzung: ASIN-Präfix B08F) |
| BSR Hauptkategorie | Nr. 18.876 Garten (Amazon.de, 2026-11-13) | Nr. 45.098 Garten (Amazon.de, 2026-11-13) | Nr. 47.361 Garten (Amazon.de, 2026-11-13) | Nr. 35.390 Garten (Amazon.de, 2026-11-14) | Nr. 142.218 Garten (Amazon.de, 2026-11-13) | Nr. 31.474 Garten (Amazon.de, 2026-11-13) |
| Hauptkategorie | Garten | Garten | Garten | Garten | Garten | Garten |
| BSR Unterkategorie | Nr. 24 | Nr. 91 | Nr. 95 | Nr. 68 | Nr. 313 | Nr. 57 |
| Unterkategorie | Pflanzenschilder | Pflanzenschilder | Pflanzenschilder | Pflanzenschilder | Pflanzenschilder | Pflanzenschilder |
| Verkäufe im Monat (~Schätzung aus BSR) | ~60 St. für Parent mit 4 Typen (Large/Mini/Hook/Banner teilen BSR 18.876) (Schätzung aus BSR, 2026-11-13) | ~34 St. (Schätzung aus BSR, 2026-11-13) | ~33 St. für Parent 27/14 cm (Schätzung aus BSR, 2026-11-13) | ~40 St. (Schätzung aus BSR, 2026-11-14) | ~16 St. (Schätzung aus BSR, 2026-11-13) | ~43 St. (Schätzung aus BSR, 2026-11-13) |
| Umsatz im Monat (~Schätzung) | ~1.470 € (Schätzung: ~60 × Ø ~24,50 € über 4 Typen) | ~690 € (Schätzung: ~34 × 20,43 €) | ~690 € (Schätzung: ~33 × 21,09 €) | ~880 € (Schätzung: ~40 × 22,20 €) | ~240 € (Schätzung: ~16 × 15,05 €) | ~1.140 € (Schätzung: ~43 × 26,64 €) |
| Varianten | 4 (Typ Large, Mini, Hook, Banner) | 6 | 4 (27 cm / 14 cm, Farben) | [fehlt] | [fehlt] | 9 (Formen) |
| Verkaufshistorie | Rezensionen 2014–2026 durchgehend, stabil; BSR 12.386 (2026-10-19) → 18.876 (2026-11-13), saisonaler Rückgang | Rezensionen 2022–2026; Preisspitzen 2022 (Rezension 2022-07-28) | Rezensionen gehäuft März–September 2026 | alle gelesenen Rezensionen Juni–Oktober 2026 → junges, wachsendes Listing | keine Bewertungen; Absatz gering | Rezensionen 2024–2026, Häufung April–August |
| Anzahl der Bewertungen | 1.407 (Amazon.de, 2026-11-13) | 1.980 (Amazon.de, 2026-11-13) | 212 (Amazon.de, 2026-11-13) | 70 (Amazon.de, 2026-11-14) | 0 / [fehlt] (Amazon.de, 2026-11-13) | 929 (Amazon.de, 2026-11-13) |
| Bewertungsschnitt | 4,4 | 4,5 | 4,6 | 4,8 | [fehlt] | 4,7 |
| Zielgruppe / Käuferschaft | Hobbygärtner mit Staudenbeet, Rosen, Hochbeet; Sammler („mittlerweile 50 Stück“, Rezension 2014-09-23) | preisbewusste Gärtner, Großmengen (30/50er) | Hobbygärtner, Geschenk („perfekte Geschenk für Gärtner“, Bullet) | Kräuter-/Hochbeet-Gärtner, Einsteiger (Stift im Set) | Gemüse-/Kräuterbeet, Edelstahl-Käufer | Kräutergarten, Schaugärten, Optik-Käufer („Bibelgarten“, Rezension 2026-08-31) |
| Notizen | Füße verzinkter Stahl, Feld Zinkblech – kein Edelstahl; Stift ausdrücklich nicht enthalten (Bullet) | Listing räumt Rost bei abgeschabter Beschichtung ein (Bullet) | Blech 0,2 mm (Rezension 2026-07-26) | Stift im Set, Gestänge laut Rezensionen stabil | Edelstahl 304 + Stift, 333 g; Amazon-Kunden kaufen trotz Preis 15 € kaum | Schiefer + 40-cm-Stahlspieß, Kreide/Stift im Set |
| abgerufen | 2026-11-13 | 2026-11-13 | 2026-11-13 | 2026-11-14 | 2026-11-13 | 2026-11-13 |

## B. Produkteigenschaften & Merkmale des Marktes

| Merkmal | M1 GardenMate | M2 STARTOSTAR | M3 KINGLAKE | M4 Bamworld | M5 EfforPrac | M6 Hoberg |
|---|---|---|---|---|---|---|
| Größe Produkteinheit | Höhe ~30 cm, Feld 9 × 3 cm (Bullet) | Höhe 26,9 cm, Feld 8,9 × 3 cm, leicht geneigt (Bullet) | Höhe 27 cm (Titel), Feld [fehlt] | [fehlt] | [fehlt] | Tafel 9 × 7 × 0,5 cm, Spieß 40 cm (Bullet) |
| Gewicht (Versand) | 1,54 Pfund ≈ 0,70 kg (Amazon.de, 2026-11-13) | [fehlt] | [fehlt] | [fehlt] | 333 g (Amazon.de, 2026-11-13) | [fehlt] |
| Abmaße (Versand) | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |
| Materialien | Füße verzinkter Stahl, Feld Zinkblech (Bullet) | verzinktes Eisen, lackiert/pulverbeschichtet (Bullet) | Eisen (Bullet), Blech 0,2 mm (Rezension 2026-07-26) | „rostfreies Metall“ ohne Güte (Bullet) | Edelstahl 304 (Titel) | Schiefer + Stahl (Bullet) |
| Farbe | Silber | Schwarz, Silber u. a. (6 Varianten) | Silber, Kupferoptik | Silber | Silber | Naturschiefer |
| Variantenvielfalt | Form (4 Typen) | Farbe/Menge | Höhe/Farbe | [fehlt] | [fehlt] | Form (oval, rund, eckig …) |
| Anzahl der Varianten | 4 | 6 | 4 | [fehlt] | [fehlt] | 9 |
| Anzahl / Setumfang | 25 | 30 | 25 | 30 + Stift | 10 + Stift | 10 + Kreide/Stift |
| Qualitätsmerkmale / Siegel | „Markenqualität aus dem Hause GardenMate“; keine Siegel | keine | keine | keine | keine | keine |
| Verpackungsart | [fehlt] | [fehlt] | [fehlt]; Lieferung unbeschädigt (Rezension 2025-03-30) | [fehlt] | [fehlt] | Einzelkarton für Schiefer, „liebevoll durchdacht verpackt“ (Rezensionen 2026-04-11, 2026-05-26) |
| Kennzeichnungspflichten | GPSR-Angaben [fehlt] (nicht im Listing sichtbar) | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |
| Prüfungen | keine angegeben | keine | keine | keine | keine | keine |
| Schutzrechte | Wortmarke GARDENMATE (AllMates GmbH, Anmeldung 2016-04-28, „metal plant markers“; trademark.justia.com, 2026-10-19); Design [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |
| Besonderheiten / USP | Systemdesign (kombinierbar Large/Mini/XL), Markenbekanntheit | geneigtes Feld, Stückpreis | Doppelbein, Kupferoptik | Stift im Set, Beschriftung mit Wasser abwischbar | Edelstahl 304 + Stift | Naturmaterial, Geschenk-Optik |

## C. Vermarktung & Optimierung

Bewertung x/10 als Schätzung aus Bilderzahl, Bullet-Qualität und A+-Vorhandensein (Bilder selbst nicht visuell geprüft).

| Merkmal | M1 GardenMate | M2 STARTOSTAR | M3 KINGLAKE | M4 Bamworld | M5 EfforPrac | M6 Hoberg |
|---|---|---|---|---|---|---|
| Anzahl Produktbilder | 7 (Amazon.de, 2026-11-13) | 6 | 7 | 6 (Amazon.de, 2026-11-14) | 7 | 7 |
| Qualität des Titelbildes (x/10) | ~6 (Schätzung) | ~6 (Schätzung) | ~7 (Schätzung) | ~7 (Schätzung) | ~5 (Schätzung) | ~8 (Schätzung) |
| Qualität der Produktbilder (x/10) | ~6 (Schätzung) | ~5 (Schätzung) | ~7 (Schätzung) | ~6 (Schätzung) | ~5 (Schätzung) | ~8 (Schätzung) |
| Qualität der Verkaufstexte (x/10) | 5 – Bullets kurz, „Markenqualität“ ohne Beleg, kein Edelstahl | 4 – maschinelle Übersetzung, Hinweis „rostet leicht“ | 6 – strukturierte Bullets 【】, Geschenk-Winkel | 6 – klare Nutzenbullets, Keyword „Hochbeet Zubehör“ | 4 – Übersetzungsfehler („Diese Schilder für LASSEN sich…“) | 7 – Maße, Material, Funktion klar |
| Erweiterte Beschreibung (A+ x/10 / nein) | ja, [fehlt] Note | ja, [fehlt] | ja, [fehlt] | ja, [fehlt] | ja, [fehlt] | ja, [fehlt] |
| Titel-Keywords [neu] | pflanzenschilder, metall, wetterfest, pflanzenstecker zum beschriften, hochbeet, gewächshaus | metall pflanzenstecker, steckschilder, pflanzetiketten, wetterfest | pflanzenschilder, pflanzenstecker metall, wetterfest, kräuterstecker | pflanzenschilder metall, mit stift, wetterfest, kräutergarten, hochbeet zubehör | pflanzenmarker 304 edelstahl, wetterfest, mit marker | schiefer-pflanzschilder, witterungsbeständig, kräuter |
| Video [neu] | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |

## D. Kritische Kundenmeinungen

Je Mitbewerber die kritischen (1–3★) und kritisch formulierten 4★-Rezensionen der Produktseite; Rezensionsseiten erfordern Login. M1 ergänzt um GardenMate Mini (B00814TLBG) und Hook (B00EC9NOJ4), gleicher Parent und gleiche Bauart. Gelesen gesamt: 59 Rezensionen (Produktseiten), davon 17 kritisch.

| Rezension | M1 GardenMate | M2 STARTOSTAR | M3 KINGLAKE | M4 Bamworld | M5 EfforPrac | M6 Hoberg |
|---|---|---|---|---|---|---|
| Rezension 1 | 2021-07-12 · 3★ Large: „Blech … extrem dünn und auch nicht sonderlich gut gestanzt. An einer Seite ist immer scharfer Grat“ | 2022-07-28 · 4★: „Preisentwicklung mehr als fragwürdig … 50 Stück Schwarz kostete am 13.06.22 noch 39,99 €“ | 2026-07-26 · 4★: „das Kupferblech ist aber nur 0,2 mm dünn“ | 2026-10-19 · 4★: „Leider hält der Stift zum Beschriften nicht sehr lange bei Regen“ | [fehlt] (0 Rezensionen) | 2024-10-01 · 4★: „keinen guten Stand im Beet … Da drehen sie sich ständig“ |
| Rezension 2 | 2025-09-23 · 1★ Mini: „billiges dünnes Blech dass sich beim Anschauen schon verbiegt. Verletzungsgefahr durch Grat an den Kanten“ | 2026-02-11 · 5★ (Kritik im Text): „les écritures ne tiennent pas dans le temps“ | [fehlt] (keine weitere kritische Rezension auf der Produktseite) | 2026-07-29 · 5★ (Vorbehalt): „mal schauen, ob sich evtl. Rost ansetzt und ob die Schrift zumindest ein…“ | [fehlt] | 2026-06-06 · 5★ (Kritik im Text): „La craie fournie avec s'efface à l'eau“ |
| Rezension 3 | 2014-08-16 · 3★ Hook: „Nach stärkeren Winden und Unwetter muss man die Bleche immer wieder zusammensuchen, da sie sehr dünn und sehr leicht sind“ | Listing selbst (Bullet): „es rostet leicht, wenn die Beschichtung abgeschabt wird“ | [fehlt] | 2026-06-09 · 5★: „nicht den mitgelieferten Stift, sondern einen wasserfesten Edding … verwendet“ | [fehlt] | [fehlt] |
| Rezension 4 | 2023-11-29 · 4★ Hook: „Dicke von 0,22mm … sehr dünn und leicht verbiegbar“ | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |
| Rezension 5 | 2023-05-30 · 3★ Mini: „hatte mir die Schilder etwas starrer / stärkeres Blech vorgestellt“ | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |
| Rezension 6 | 2025-12-31 · 5★ Large (Kritik im Text): „Leider habe ich noch keinen Stift gefunden der nicht verblasst“ | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |
| Rezension 7 | 2018-05-22 · 5★ Hook: „die Stäbe ein bisschen fragil...verbiegen also schnell“; 2024-08-28 · 4★ Large: „sehen auch leider nicht ganz so schick aus wie Schilder aus Holz“; 2026-08-30 · 4★ Large: „Fallen leider etwas zu klein aus“; 2024-11-03 · 1★ Large: nie geliefert (NL) | [fehlt] | [fehlt] | [fehlt] | [fehlt] | [fehlt] |
| Zusammenfassung | Dünnes Zinkblech (0,22 mm), Grat an Stanzkanten, Schilder lösen sich (Hook), Stift fehlt; Systemdesign wird gelobt | kaum Kritik auf Seite 1; Preissprünge, Beschichtung kann rosten, Schrift hält nicht | Blechstärke 0,2 mm einziger Kritikpunkt | beigelegter Stift hält bei Regen nicht; Rost-Skepsis | keine Daten | Schiefer dreht sich, Kreide wischt ab; ansonsten sehr positiv |

## D2. Rezensions-Mining [neu]

Basis: 59 gelesene Produktseiten-Rezensionen (7 ASINs inkl. GardenMate Mini/Hook, 2026-11-13/14) plus Voranalyse-Lesung 2026-10-19 (KINGLAKE Schiefer B06XYZ3FKB).

| Thema (Cluster) | Nennungen (≈ x von y gelesenen) | Mitbewerber betroffen | Beispielzitat (Datum) | Ableitung für unser Produkt |
|---|---|---|---|---|
| Funktion | 4 von 59 (Schilder lösen sich, drehen sich, Stäbe ungleich lang/dünn) | M1 (Hook), M6, U/B B09MF4F32K | „Bleche immer wieder zusammensuchen“ (2014-08-16); „drehen sie sich ständig“ (2024-10-01) | Schild fest vernietet; Doppelbein gegen Verdrehen |
| Material / Haltbarkeit | 7 von 59 (dünnes Blech, verbiegt, Grat, Rostzweifel) | M1, M3, M4, M2 (Listing) | „Verletzungsgefahr durch Grat an den Kanten“ (2025-09-23); „nur 0,2 mm dünn“ (2026-07-26) | 0,5 mm Edelstahl 304, entgratet/gerollte Kante, Salzsprühtest |
| Verpackung / Lieferung | 2 von 59 (nie geliefert; Bruch bei anderem Anbieter) | M1, M3 (Verweis) | „unbeschädigt angekommen (ganz im Gegensatz zu … anderen Anbieter)“ (2025-03-30) | Retail-Box mit Einlage, Stäbe gebündelt |
| Handhabung / Reinigung | 5 von 59 (Stift verblasst / hält nicht bei Regen, Kreide wischt ab) | M1, M2, M4, M6 | „noch keinen Stift gefunden der nicht verblasst“ (2025-12-31); „Stift … hält nicht sehr lange bei Regen“ (2026-10-19) | Stift allein reicht nicht – Stiftqualität (Lack/UV) ist der Hebel; Alternative Gravur-Service |
| Optik | 2 von 59 (weniger schick als Holz; zu klein) | M1 | „nicht ganz so schick aus wie Schilder aus Holz“ (2024-08-28) | Größeres Feld (10 × 3,5 cm), gebürstetes Finish, Schwarz-Variante |
| Preis-Leistung | 2 von 59 (Preissprünge, „überteuert“) | M1 (Mini), M2 | „Absolut überteuert, billiges dünnes Blech“ (2025-09-23) | Premium-Preis nur mit sichtbar dickerem Material rechtfertigbar |
| Was Kunden lieben (5 Sterne) | ~35 von 59 (wetterfest, langlebig, gut lesbar, edle Optik, groß genug) | alle | „Stehen … seit Sommer, Herbst und Winter draußen und sehen noch immer aus wie Neu“ (2025-12-31); „sehen sehr edel aus“ (2026-06-15) | Langlebigkeit und Lesbarkeit sind die Kaufgründe – Bilder müssen Winterfestigkeit zeigen |

## D3. Produktanforderungen aus Kundensicht [neu]

Wichtigste Eingabe für das Briefing (Teil B).

| # | Anforderung | Herkunft (welche Kritik / welches Lob) | Muss / Soll | Konsequenz für Spezifikation |
|---|---|---|---|---|
| 1 | Schild verbiegt nicht bei Handhabung | „dünnes Blech … verbiegt“ (M1 Mini 2025-09-23), 0,2–0,22 mm (M1 Hook, M3) | Muss | Schild Edelstahl 304, Stärke ≥ 0,5 mm (Toleranz ± 0,03 mm) |
| 2 | Keine scharfen Kanten | Grat (M1 Large 2021-07-12, Mini 2025-09-23) | Muss | Kanten entgratet oder gerollt, Ecken R ≥ 2 mm; GPSR-relevant |
| 3 | Schild bleibt am Stab | „Bleche … zusammensuchen“ (M1 Hook 2014-08-16) | Muss | Schild mit Stab vernietet oder punktgeschweißt, Zugtest ≥ 50 N |
| 4 | Kein Rost über ≥ 2 Winter | „rosten in ein paar Jahren“ (U/B, Voranalyse), M2-Listing „rostet leicht“ | Muss | Stab und Schild Edelstahl 304 (1.4301), passiviert; Salzsprühtest ISO 9227 NSS ≥ 48 h ohne Rotrost |
| 5 | Beschriftung hält Regen/UV | Stift verblasst (M1 2025-12-31), Bamworld-Stift hält nicht (M4 2026-10-19) | Muss | Lackmalstift auf Wasserbasis (pigmentiert, UV-stabil), kein Gefahrgut; Bewitterungstest Sample 4 Wochen außen |
| 6 | Steht stabil, dreht nicht | „drehen sie sich ständig“ (M6 2024-10-01) | Soll | Doppelbein oder Flachstab, Länge 30 cm, Einstecktiefe ≥ 12 cm |
| 7 | Gut lesbar, groß genug | „zu klein“ (M1 2026-08-30), Lob für Größe (M2, M3) | Soll | Feld ~10 × 3,5 cm (größer als GardenMate 9 × 3 cm) |
| 8 | Edle Optik | „edel“, „schick“ (M3 2026-09-26, M4 2026-06-15) | Soll | gebürstet (No. 4) bzw. matt-schwarz pulverbeschichtet als Variante |

## E. Schwächen des Mitbewerbers (Punkt 1–5)

| # | M1 GardenMate | M2 STARTOSTAR | M3 KINGLAKE | M4 Bamworld | M5 EfforPrac | M6 Hoberg |
|---|---|---|---|---|---|---|
| 1 | Zinkblech 0,22 mm statt Edelstahl | verzinktes Eisen, rostet bei Beschichtungsschaden (Listing) | Eisenblech 0,2 mm | Stift hält Regen nicht | keine Bewertungen, BSR 142.218 | Schiefer dreht sich im Beet |
| 2 | Grat an Stanzkanten | Preissprünge (2022) | China-Direkt, Bullets übersetzt | Material ohne Güteangabe | MFN, kein Prime | Kreide wischt ab |
| 3 | kein Stift im Set | Übersetzungsqualität der Bullets | Feldmaß nicht im Titel | junges Listing (70 Bew.) | Übersetzungsfehler in Bullets | 2,66 €/Stk., nur 10 Stk. |
| 4 | Hook: Schild lose | BSR 45.098 trotz 1.980 Bewertungen | BSR 47.361 | Herkunft China, Marke ohne Gartenprofil | 10 Stk. für 15,05 € (1,51 €/Stk.) | bruchgefährdet (Schiefer, Voranalyse B06XYZ3FKB) |
| 5 | Herkunftsangabe „USA“ irritiert, Bullets generisch | Optik einfach | – | – | – | Gewicht/Versand [fehlt] |

## F. Stärken des Mitbewerbers (Punkt 1–7)

| # | M1 GardenMate | M2 STARTOSTAR | M3 KINGLAKE | M4 Bamworld | M5 EfforPrac | M6 Hoberg |
|---|---|---|---|---|---|---|
| 1 | 1.407 Bewertungen, 4,4★ | 1.980 Bewertungen, 4,5★ | 4,6★ | 4,8★ | Edelstahl 304 im Titel | 929 Bewertungen, 4,7★ |
| 2 | seit ~2014 etabliert, Marke | niedrigster Stückpreis Metall (0,68 €) | Doppelbein, stabil | Stift im Set | Stift im Set | Premium-Optik, Geschenkfähigkeit |
| 3 | Systemdesign 4 Typen, kombinierbar | geneigtes Feld, gute Lesbarkeit | 2 Höhen, Kupferoptik | schnelles Wachstum (~40 St./Monat nach ~6 Monaten) | – | 9 Formvarianten |
| 4 | bester BSR im Metall-Segment | 6 Farb-/Mengenvarianten | Geschenk-Positionierung | „Hochbeet Zubehör“ im Titel | – | sorgfältige Verpackung |
| 5 | FBA, deutscher Seller | FBA | FBA | FBA | – | FBA, deutscher Seller |
| 6 | 7 Bilder + A+ | A+ | 7 Bilder + A+ | A+ | 7 Bilder + A+ | 7 Bilder + A+ |
| 7 | winterfest belegt (Rezension 2025-12-31) | „halten ewig“ (Rezension 2023-11-28) | „hält nach Jahren“ (Rezension 2024-04-13) | „sehr stabiles Gestänge“ (Rezension 2026-07-29) | – | „überdauern problemlos auch Frost“ (Rezension 2026-08-20) |

## G. Meine Optimierungsansätze & USPs (Punkt 1–7)

| # | Ansatz / USP | Beleg (Abschnitt D–F) |
|---|---|---|
| 1 | 0,5 mm Edelstahl 304, „verbiegt nicht, rostet nicht“ als Hauptbotschaft, Dicke im Titel | D2 Material 7 von 59; E M1/M3 Nr. 1 |
| 2 | Entgratete, gerundete Kanten | D M1 Rezension 1–2 |
| 3 | Schild fest vernietet | D M1 Rezension 3 (Hook) |
| 4 | Hochwertiger UV-stabiler Lackstift statt Billig-Marker (Stift allein ist kein USP mehr: M4, M5, B0H336FKWY, B0GN7SQ5NF liefern Stift) | D M4 Rezension 1, M1 Rezension 6 |
| 5 | Größeres Feld 10 × 3,5 cm | D M1 Rezension 7 („zu klein“) |
| 6 | Matt-Schwarz als zweite Variante (Autocomplete „pflanzenschilder schwarz“, Metall-Schwarz nur bei STARTOSTAR) | Autocomplete 2026-11-13; B M2 |
| 7 | Markenbox mit Pflanz-Kalender-Karte, Bundle-fähig mit Anzucht-Set | D2 Verpackung; Voranalyse Nr. 21 |

**Positionierung [neu]:** Preis-/Qualitäts-Karte

| Anbieter | Preis | Qualität (1–5) | Position |
|---|---|---|---|
| M1 GardenMate | 27,70 € / 25 (1,11 €/Stk.) | 3 | Marke, Mittelklasse-Material, oberer Preis |
| M2 STARTOSTAR | 20,43 € / 30 (0,68 €/Stk.) | 3 | Preisführer Metall |
| M3 KINGLAKE | 21,09 € / 25 (0,84 €/Stk.) | 3 | China-PL, Mitte |
| M4 Bamworld | 22,20 € / 30 (0,74 €/Stk.) | 3–4 | China-PL mit Stift, Aufsteiger |
| M5 EfforPrac | 15,05 € / 10 (1,51 €/Stk.) | 4 (Material) | Edelstahl 304, kleines Set, kein Absatz |
| M6 Hoberg | 26,64 € / 10 (2,66 €/Stk.) | 4 | Premium-Naturmaterial |
| **nicegarden (Ziel)** | 24,90 € / 20 (1,25 €/Stk.) | 5 | Premium-Edelstahl, dickstes Material |

Listing-Ansatz: Titelstruktur: „nicegarden Pflanzenschilder Edelstahl 304 – 20 Stück, 0,5 mm, 30 cm, mit wetterfestem Lackstift – Pflanzenstecker zum Beschriften für Hochbeet, Kräuter, Gemüse“ · Bilder-Konzept: 1 Set freigestellt mit Stift und Box · 2 Dickenvergleich 0,5 mm vs. 0,2 mm (Biegetest) · 3 Kante/Niete Makro · 4 Beet im Winter/Frost · 5 Maße · 6 Beschriftungsanleitung · 7 Lifestyle Hochbeet · A+-Story: „Einmal kaufen, nie wieder suchen“ – Material, Winterfestigkeit, Designed in Germany, Cross-Sell NG0001/NG0002 · Ziel-VK: 24,90 € – Herleitung: 1,25 €/Stk. liegt 13 % über GardenMate (1,11 €) und unter Edelstahl-Neulingen (1,51–2,48 €/Stk.), Preisschwelle unter 25 €.

**Keywords [neu]** (Cluster aus Autocomplete und Listing-Titeln, ohne Volumen)

| Cluster | Keywords | Volumen (H10, später) |
|---|---|---|
| Haupt | pflanzenschilder metall · pflanzenschilder edelstahl · pflanzenstecker metall | |
| Long-Tail | pflanzenschilder zum beschriften wetterfest · pflanzenschilder schwarz · pflanzenschilder metall mit stift · pflanzenetiketten edelstahl | |
| Anwendung | kräuterschilder · hochbeet zubehör · pflanzenschilder für draußen · rosen schilder | |
| Geschenk | geschenk für gärtner · gartengeschenk edelstahl | |

## H. Validierung: Chancen für den Markteinstieg (Punkt 1–5)

1. Material-Lücke: kein etabliertes Metall-Listing nutzt Edelstahl; GardenMate (Zinkblech 0,22 mm) führt mit nur ~60 St./Monat für 4 Typen (Schätzung aus BSR, 2026-11-13).
2. Wiederkehrende Kritik (dünn, Grat, lose) ist mit Spezifikation lösbar und gut bebilderbar (Biegetest).
3. Junge Listings wachsen schnell: Bamworld erreicht mit 70 Bewertungen ~40 St./Monat (Schätzung aus BSR 35.390) – Markteintritt ohne hohe Bewertungshürde möglich.
4. Logistik ideal: ~0,7 kg, flach, bruchsicher, Kleines Paket.
5. Bundle-Potenzial mit Anzucht-Set/Hochbeet-Zubehör und Cross-Selling im nicegarden-Store.

**Marktgröße [neu]:** ~4.700–14.000 € / Monat (Herleitung: Metall-Top-6 M1–M5 + U/B ~220 St./Monat × Ø ~21 € = ~4.700 € in der Nebensaison November; Peak März–Juni ×2–3 = ~9.500–14.000 €, Schätzung aus BSR) · Marktanteil Ziel M6: ~10 % · M12: ~15 % · Absatzziel: ~40 St./Monat Jahresschnitt (Peak ~80, Winter ~20; Schätzung)

## I. Validierung: Risiken für den Markteinstieg (Punkt 1–5)

| # | Risiko | Wahrscheinlichkeit (niedrig / mittel / hoch) | Auswirkung | Gegenmaßnahme [neu] |
|---|---|---|---|---|
| 1 | Marge trägt nicht: EK für 0,5-mm-304-Ausführung liegt über ~4,80 € je Set | hoch | DB1 < 35 %, Break-even-ACOS im CPC-Band → Ads unwirtschaftlich | RFQ durch Pafri bei 3 Lieferanten mit Zielpreis ≤ 4,80 €; ohne Beleg kein Order |
| 2 | Preisdruck China-Direkt (Edelstahl-10er ab 15,05 €, Metall 0,68 €/Stk., Kunststoff 100 Stk. 5,54 €) | hoch | VK 24,90 € nicht haltbar, VK −10 % → DB1 ~20 % | Material sichtbar machen (Dicke im Titel, Biegetest-Bild), Bundle statt Einzelpreiswettbewerb |
| 3 | Saisonalität und Zeitplan: Peak März–Juni, Chinesisches Neujahr 2027 (Anfang Februar) verzögert Produktion | hoch | Launch nach Saisonstart → ein Jahr Lagerkosten | Order bis Mitte Dezember 2026 oder Launch auf Frühjahr 2028 schieben; Luftfracht-Teilmenge prüfen |
| 4 | USP-Erosion: Stift im Set ist Standard; Edelstahl-304-Neulinge kopieren schnell | mittel | Differenzierung reduziert sich auf Materialstärke | Dicke, Niete und Stiftqualität kombiniert kommunizieren; optional Gravur-Service |
| 5 | Lackstift als Gefahrgut (lösungsmittelbasiert) blockiert FBA-Einlagerung | mittel | Hazmat-Prüfung, Verzögerung | wasserbasierten Pigmentmarker spezifizieren, SDS vom Lieferanten anfordern lassen |

## J. Schlussfolgerungen / Bewertung (Ja / Nein / Eventuell)

| Frage | Antwort | Begründung |
|---|---|---|
| 1. Passt das Produkt zu Nicegarden? | Ja | Edelstahl, Garten/Anzucht, Premium-Positionierung möglich |
| 2. Ist eine gezielte Kundenansprache möglich? | Eventuell | Hochbeet-/Kräutergärtner erreichbar, aber Kaufentscheidung überwiegend nach Stückpreis (Voranalyse Nr. 17) |
| 3. Kann ich die Vermarktung deutlich besser machen? | Ja | Texte M1/M2/M5 4–5/10; keiner kommuniziert Materialstärke oder Kante |
| 4. Kann ich das Produkt / das Angebot verbessern? | Ja | 0,5 mm Edelstahl, Niete, Kante, Stiftqualität – D3 Nr. 1–5 |
| 5. Kann ich die Verpackung verbessern? | Ja | Wettbewerber ohne erkennbare Markenbox (Ausnahme Hoberg) |

## K. Produktmerkmale & Informationen / Mein Wunschprodukt

| Merkmal | Variante 1 | Variante 2 |
|---|---|---|
| Gewicht (Versand) | ~0,70 kg (Schätzung: 20 × ~30 g + Box ~80 g) | ~0,72 kg (Schätzung: + Pulverlack) |
| Abmaße (Versand) | ~33 × 12 × 4 cm (Schätzung: Stablänge 30 cm + Box) | ~33 × 12 × 4 cm |
| Materialien (Edelstahl-Güte 304 / 430, Finish) | Edelstahl 304 (1.4301), Schild 0,5 mm, Stab Ø 3 mm Doppelbein, gebürstet, passiviert | wie V1, matt-schwarz pulverbeschichtet |
| Besondere Eigenschaften | Schild vernietet; Kanten entgratet/gerundet; Feld 10 × 3,5 cm; Höhe 30 cm; Lackstift weiß, wasserbasiert, UV-stabil | wie V1, Lackstift weiß (Kontrast auf Schwarz) |
| Farbe / Farbvarianten | Silber (gebürstet) | Matt-Schwarz |
| Variantenvielfalt | Farbe | Farbe |
| Anzahl der Varianten | 1 | 1 |
| Qualitätsmerkmale / Siegel | Materialzertifikat 304 (Mill Certificate), Salzsprühtest ≥ 48 h NSS | dazu Haftung Pulverlack (Gitterschnitt ISO 2409) |
| Verpackungsart (Retail-Box, Polster, FBA-Klasse, EPR-Fraktionen) | Faltschachtel Kraft, Stäbe mit Papierband gebündelt, keine Kunststoffe; Kleines Paket; EPR: Papier/Pappe | wie V1 |
| Kennzeichnungspflichten | GPSR: Hersteller/Importeur, Anschrift, Artikel-/Chargennr., Warnhinweis „spitze Enden – nicht für Kinder“; Stift: SDS, ggf. CLP | wie V1 |
| erforderliche Prüfungen | Salzsprühtest, Biegeprüfung Schild, Zugtest Niete ≥ 50 N, Bewitterung Stift 4 Wochen | dazu Gitterschnitt |
| Target-Verkaufspreis | 24,90 € | 24,90 € |
| Erwartungen (Absatz/Monat) | ~40 St. Jahresschnitt (Peak ~80) (Schätzung, H) | ~15 St. (Schätzung: Nische „schwarz“) |
| Mindestbestellmenge | ~500 Sets (Schätzung, L) | ~300 Sets (Schätzung) |

Empfehlung Start-Varianten (max. 2): nur Variante 1 (Silber). Variante 2 erst nach Abverkauf Charge 1, weil das Segment (~220 St./Monat) zwei Varianten mit getrennter MOQ nicht trägt und V2 die Marge um weitere ~1 Pp senkt.

## L. Einkauf

| Link | EK | Mindestbestellmenge | Lead Time | Notizen |
|---|---|---|---|---|
| https://www.alibaba.com/showroom/for-metal-plant-labels.html („Waterproof Heavy Duty Metal Plant Labels Stainless Steel …“) | 0,14–0,35 € je Stecker (Suchmaschinen-Snippet, 2026-11-14) | 2 Stück (Snippet) | [fehlt] | Dicke/Güte nicht angegeben; vermutlich 0,2–0,3 mm |
| https://www.alibaba.com/showroom/metal-plant-labels.html („Insert Stainless Steel Label Garden … Reusable Plant Label“) | 0,85 US$ je Stecker (Snippet, 2026-11-14) | 300 Stück | [fehlt] | Edelstahl, Dicke [fehlt] |
| https://www.alibaba.com/showroom/metal-plant-labels.html („Copper Plants Outdoor Gardening Plant Herb Markers …“) | 0,17–0,20 US$ (Snippet, 2026-11-14) | 30 Stück | [fehlt] | Kupferoptik, kein Edelstahl |
| https://www.alibaba.com/showroom/cheap-plant-stakes.html (Slate Garden Markers with Stainless Steel Stakes) | 0,42–0,66 € je Stück (Snippet, 2026-11-14) | 2 bzw. 1.000 Stück | [fehlt] | Schiefer + Edelstahlspieß, Vergleich Premium |
| Alibaba-Kategorie „garden stake label“ | [fehlt] | [fehlt] | [fehlt] | 804 Produkte (Snippet, 2026-10-19, Voranalyse) |

Nur lesend (Alibaba/1688; Seite selbst nicht abrufbar, nur Suchmaschinen-Snippets). Herstelleranfrage: nicht eingeleitet.

EK-Ansatz Variante 1 (Schätzung): 20 Stecker × ~0,30 € (obere Hälfte des Bands 0,14–0,35 €, weil 0,5 mm statt Standard ~0,2 mm) = ~6,00 € + Lackstift ~0,25 € + Faltschachtel bedruckt ~0,45 € + Konfektionierung ~0,10 € = **~6,80 € je Set** (Schätzung aus Alibaba-Snippets, 2026-11-14). Plausibilität: 30-%-Regel ~7,47 €; Materialwert Edelstahl ~0,6 kg × ~2,5–3 US$/kg ≈ 1,40–1,70 € (Schätzung).

**Sourcing-Anforderungen [neu]** (Vorbereitung Briefing Teil B): Lieferantentyp: Metallwaren-Hersteller (Stanzen + Drahtbiegen + Nieten) mit Garten-Export, kein Händler · MOQ-Erwartung: 300–500 Sets bei eigener Box · Sample-Prozess: 3 Lieferanten, je 2 Sets Standard + Spezifikation (0,5 mm, vernietet), Dickenmessung Mikrometer, Biegetest, Salzsprühtest extern oder Salzwasser-Lagerung 7 Tage · Lead Time: ~25–35 Tage Produktion + ~35–45 Tage Seefracht (Schätzung) · Qualitätskriterien (inkl. Rostbeständigkeit + Prüfmethode): 304 per Mill Certificate und Magnettest/XRF-Stichprobe, Salzsprühtest ISO 9227 NSS ≥ 48 h ohne Rotrost (NG0001-Learning: Rostbeständigkeit ist Muss), Kanten gratfrei (Handtest mit Stoff), Niete Zugtest ≥ 50 N · Fragen an den Lieferanten: Preis je Set bei 300/500/1.000; Blechstärke und Güte schriftlich; Niete oder Punktschweißung; wasserbasierter Lackmarker mit SDS verfügbar; Box-Druck MOQ; Produktionszeit vor/nach Chinesischem Neujahr 2027.

## M. Detailkalkulation je Variante [neu]

`rules/kalkulation.md`

| Position | Variante 1 | Variante 2 | Grundlage |
|---|---|---|---|
| Brutto-VK | 24,90 € | 24,90 € | Ziel-VK (G) |
| Netto-VK (/1,19) | 20,92 € | 20,92 € | |
| EK je Stück | ~6,80 € | ~7,05 € | Richtpreis Alibaba-Snippets (L), V2 + ~0,25 € Pulverlack (Schätzung) |
| Fracht + Zoll + Nebenkosten | ~1,08 € | ~1,09 € | Seefracht ~0,60 € (Schätzung: ~0,7 kg flach), Zoll 2,7 % auf EK ~0,18 € (TARIC 7326 90 98, Schätzung, nicht geprüft), Einfuhrnebenkosten ~0,30 € |
| **Landed Cost** | ~7,88 € | ~8,14 € | |
| Verkaufsgebühr 15 % | 3,73 € | 3,73 € | |
| FBA-Versand | ~3,90 € | ~3,90 € | Kleines Paket, ~0,7 kg; Gebührentabelle DE 2026 3,38–4,54 € (aus `pipeline/edelstahl-pflanzsprueher/01-voranalyse.md`, Stand 2026-09-21) |
| **DB1 €** | ~5,41 € | ~5,15 € | |
| **DB1 %** (vom Netto-VK) | ~26 % | ~25 % | |
| Lagerkosten je Stück | ~0,15 € | ~0,15 € | Schätzung: ~0,0016 m³ × ~26 €/m³/Monat × ~2 Monate Ø ≈ 0,08 € + Q4-Zuschlag und Langzeitlager-Puffer (Saisonware) |
| EPR / Verpackung | ~0,05 € | ~0,05 € | Schätzung: ~80 g Pappe, LUCID-Systembeteiligung |
| Retourenpauschale | ~0,25 € | ~0,25 € | Schätzung: ~4 % Retourenquote × ~6 € (Bearbeitung + Abschreibung) |
| Ads-Anteil (Ziel-TACoS) | ~2,99 € | ~2,99 € | Ziel-TACoS 12 % × 24,90 € (Schätzung, Dauerbetrieb nach Launch) |
| **DB2 €** | ~1,97 € | ~1,71 € | |
| **DB2 %** | ~9 % | ~8 % | |
| **Break-even-ACOS** | ~22 % | ~21 % | DB1 € / Brutto-VK; CPC-Niveau ~0,40–0,70 € ≙ ACOS ~16–28 % (Schätzung, Voranalyse Nr. 25) |
| MOQ | ~500 Sets | ~300 Sets | Schätzung (L) |
| **Kapitalbedarf Charge 1** | ~5.400 € | ~2.400 € (nur bei Zweitcharge) | 500 × 7,88 € + Erstausstattung ~1.500 € (Fotos, Box-Design, Samples) |

**Sensitivität** (Variante 1; V2 jeweils ~1 Pp darunter)

| Szenario | DB1 % | Break-even-ACOS |
|---|---|---|
| Basis | ~26 % | ~22 % |
| EK +15 % (7,82 €) | ~21 % | ~18 % |
| EK −15 % (5,78 €) | ~31 % | ~26 % |
| CPC +30 % (Wirkung auf Ads-Anteil / DB2) | ~26 % (DB2 ~5 %, Ads ~3,89 €) | ~22 % – Schwelle über CPC-Band verfehlt deutlicher (~36 % ACOS-Äquivalent oben) |
| CPC −30 % | ~26 % (DB2 ~14 %, Ads ~2,09 €) | ~22 % – liegt dann knapp über dem CPC-Band (~11–20 %) |
| VK −10 % (22,41 €) | ~20 % | ~16 % |
| VK +10 % (27,39 €) | ~31 % | ~26 % |
| Zusatz: VK 29,90 € | ~35 % | ~30 % |
| Zusatz: EK 4,80 € (Go-Schwelle) | ~36 % | ~30 % |
| Zusatz: 40er-Set 34,90 € (EK ~12,90 €, FBA ~4,54 €) | ~16 % | ~14 % |

Lesart: Go-Schwellen (DB1 ≥ 35 %, Break-even-ACOS über CPC-Band) erreicht V1 nur mit EK ≤ ~4,80 € (−29 % zur Basis) oder VK ≥ ~29,90 € (1,50 €/Stk., +35 % über GardenMate je Stück, ohne Absatzbeleg im Edelstahl-Segment: M5 ~16 St./Monat). Größere Sets verschlechtern die Marge, weil der EK linear mitwächst.

## N. Compliance [neu]

| Thema | Anforderung | Status |
|---|---|---|
| GPSR (verantwortliche Person, Kennzeichnung) | Pafri GmbH als Importeur/verantwortliche Person mit Anschrift auf Box und im Listing; Artikel-/Chargennr.; Warnhinweis spitze Stäbe/Kanten; Risikoanalyse (Kanten, Kinder) | offen – im Briefing festlegen |
| Verpackungsgesetz / LUCID | Systembeteiligung Pappe; nicegarden-Registrierung vorhanden (Voranalyse Nr. 29) | vorhanden, Mengen melden |
| PPWR (Verpackung) | Verordnung (EU) 2025/40, anwendbar ab 12.08.2026: Verpackung minimieren, Monomaterial Pappe, ohne Kunststoff (Kenntnisstand, nicht neu abgerufen) | durch Kraftbox erfüllbar |
| Materialdeklaration | „Edelstahl 304 (1.4301)“ nur mit Mill Certificate; Stift: SDS, Gefahrgut-Einstufung (wasserbasiert → i. d. R. kein Gefahrgut, prüfen); CLP-Kennzeichnung falls lösemittelhaltig | offen – Lieferantenfrage (L) |
| Amazon Kategorie-Freigabe | Garten › Pflanzenschilder, keine Freigabe nötig (Voranalyse Nr. 30); Stift ggf. Hazmat-Prüfung mit SDS | offen für Stift |

## O. Launch-Skizze [neu]

Ranking-Strategie (Learnings NG0001: Coupon-Push, TACoS-Steuerung, Ziel-BSR): Launch Ende Februar/Anfang März mit 20-%-Coupon und Vine (bis 30 Einheiten), Exact-Match auf „pflanzenschilder metall/edelstahl“, Ziel-BSR < 15.000 Garten (≈ Top 20 Pflanzenschilder) im April; ab Monat 3 TACoS ≤ 12 % · Ads-Startbudget: ~200–500 € / Monat (Schätzung: CPC ~0,40–0,70 € × ~15–25 Klicks/Tag) · Zeitplan: Sample → Order → Launch (Wochen): RFQ + Samples 3–4 Wochen → Order + Produktion 4–5 Wochen (Chinesisches Neujahr 2027 Anfang Februar) → Seefracht 6 Wochen → FBA-Einlagerung 1–2 Wochen = ~15–17 Wochen; ab Gate 2 (Mitte November 2026) Launch frühestens Anfang März 2027 und nur, wenn die Order bis Mitte Dezember 2026 steht.

## Fazit und Scores

**Fazit:** Stop – Begründung: Der Alibaba-Richtpreis (~0,30 €/Stecker für die 0,5-mm-Ausführung, Schätzung aus Snippets) hebt DB1 nur von ~23 % auf ~26 %, der Break-even-ACOS (~22 %) bleibt im CPC-Band ~16–28 %, die Red Flag aus der Voranalyse bleibt bestehen. Das Segment ist klein (~220 St./Monat, Schätzung aus BSR) und das geplante Differenzierungsmerkmal „Stift im Set“ haben Bamworld und drei Edelstahl-304-Neulinge seit 2026 bereits. Selbst bei Go-EK (≤ 4,80 €) und ~40 St./Monat läge der DB1 bei ~300 €/Monat – als Einzelprodukt zu wenig, als Bundle-Beilage zu Anzucht-Set/Hochbeet denkbar.

| # | Kriterium | Gewicht | Teilnote 0–10 | Δ Voranalyse | Begründung (belegte Zahl) |
|---|---|---|---|---|---|
| 1 | Marge & DB-Potenzial | 25 % | 4 | +1 | DB1 ~26 % mit Alibaba-Richtpreis (statt ~23 %), Break-even-ACOS ~22 % ohne Puffer zum CPC-Band. |
| 2 | Nachfrage | 20 % | 4 | 0 | Metall-Segment ~220 St./Monat in der Nebensaison (Schätzung aus BSR, 2026-11-13/14), saisonal März–Juni, seit 2014 stabil. |
| 3 | Wettbewerb (invers) | 20 % | 4 | −1 | Stift-USP von Bamworld (70 Bew., ~40 St./Monat) und 3 Edelstahl-304-Neulingen besetzt; GardenMate Mini 4,1★ bleibt angreifbar. |
| 4 | Logistik & FBA-Fit | 10 % | 8 | 0 | ~0,7 kg, ~33 × 12 × 4 cm, bruchsicher, Kleines Paket. |
| 5 | Markenfit & Synergien | 10 % | 7 | 0 | Edelstahl und Anzucht/Hochbeet passen, Bundle mit Anzucht-Set möglich, kein direktes Cross-Selling zu NG0001/NG0002. |
| 6 | Risikoprofil (invers) | 15 % | 6 | 0 | Kein IP-Hindernis sichtbar (GARDENMATE nur Wortmarke), DPMA/Design-Register weiter nicht abgefragt; Stift-Gefahrgut prüfbar. |

K.O.-Prüfung: nein (Marge 4, Risiko 6 > K0-Schwelle 2)
Red Flag: ja – Break-even-ACOS ~22 % innerhalb des geschätzten CPC-Bands (~16–28 % ACOS-Äquivalent) → Stop trotz Score ≥ 50.
**Gesamtscore: 50 / 100 (4×0,25 + 4×0,20 + 4×0,20 + 8×0,10 + 7×0,10 + 6×0,15 = 5,0) → Zone: Review → Lane: C**

Go-Kriterien `rules/scoring.md` Abschnitt 5: Zone Go ✗ (50) · DB1 ≥ 35 % ✗ (~26 %) · Break-even-ACOS über CPC-Niveau ✗ (~22 % vs. bis ~28 %) · Risiko „hoch“ mit Gegenmaßnahme ✓ (3 × hoch, je mit Gegenmaßnahme).

Die zwei größten Unsicherheiten und wie sie geschlossen werden:
1. EK der 0,5-mm-Edelstahl-304-Ausführung, vernietet, mit Stift und Box (Basis nur Snippets ohne Dickenangabe) – schließen durch RFQ von Pafri bei 3 Lieferanten mit Zielpreis ≤ 4,80 € je 20er-Set; erst ein belegter Preis darunter dreht Marge und Red Flag.
2. Absatz und Saisonfaktor (BSR aus Okt./Nov., kein Keepa/H10, kein Google Trends) – schließen durch H10-/Keepa-Export der 6 Wettbewerber über 12 Monate und Google Trends „pflanzenschilder“ 5 Jahre.

## Quellen
- Amazon.de Produktseiten via `scripts/amazon.mjs`: https://www.amazon.de/dp/B00814L088, /dp/B07V4297ZC, /dp/B0G23L9HR4, /dp/B09MF4F32K, /dp/B0GZPBF5Z6, /dp/B08F5HMWG1 (2026-11-13); /dp/B0FMQVGDX2, /dp/B0H336FKWY, /dp/B00814TLBG, /dp/B00EC9NOJ4 (2026-11-14). Rohdaten `data/raw/amazon/2026-11-13/`, `data/raw/amazon/2026-11-14/`
- Amazon.de Suche „pflanzenschilder edelstahl“ und „pflanzenschilder metall“, Seite 1, Lieferort 10115 (2026-11-14)
- Amazon.de Autocomplete „pflanzenschilder“ (2026-11-13)
- Alibaba (Suchmaschinen-Snippets, Seiten nicht abrufbar): https://www.alibaba.com/showroom/for-metal-plant-labels.html, https://www.alibaba.com/showroom/metal-plant-labels.html, https://www.alibaba.com/showroom/cheap-plant-stakes.html (2026-11-14)
- Einzelhandel-Referenz Edelstahl 304, 25er-Pack 28,99 US$: https://bravextools.com/products/metal-plant-labels-25-pack-black (Snippet, 2026-11-14)
- https://trademark.justia.com/owners/allmates-gmbh-co-kg-5354946 (2026-10-19, aus Voranalyse)
- FBA-Gebühren DE 2026: übernommen aus `pipeline/edelstahl-pflanzsprueher/01-voranalyse.md` (Stand 2026-09-21)
- Voranalyse `pipeline/pflanzenetiketten-metall/01-voranalyse.md` (2026-10-19)

---
## Gate 2: Tiefenanalyse – pflanzenetiketten-metall
**Ergebnis:** Score 50 / 100 (Zone Review), DB1 ~26 %, Break-even-ACOS ~22 % vs. CPC ~0,40–0,70 € (≙ ~16–28 % ACOS), Kapitalbedarf ~5.400 €
**Empfehlung:** Stop
**Begründung (3 Sätze max):** Mit Alibaba-Richtpreis statt 30-%-Regel steigt DB1 nur auf ~26 %, der Break-even-ACOS bleibt mit ~22 % im CPC-Band – die Red Flag der Voranalyse bleibt. Das Metall-Segment ist klein (~220 St./Monat, Schätzung aus BSR) und „Stift im Set“ ist seit 2026 Marktstandard (Bamworld, Edelstahl-304-Neulinge). Bild kippt nur mit belegtem EK ≤ ~4,80 € je 20er-Set; dann eher als Bundle-Beilage (Anzucht-Set) denn als Einzelprodukt.
**Offene Punkte / Datenlücken:** belegter EK/MOQ für 0,5-mm-304-Ausführung (nur RFQ durch Pafri); Keepa/H10-Verlauf und Google Trends; DPMA/EUIPO/Design-Register; kritische Rezensionen jenseits der Produktseite (Login nötig).
**Nächster Schritt bei Go:** /briefing pflanzenetiketten-metall
**Deine Entscheidung (Go / Stop / Beobachten / Nacharbeit):** _wartet_
---
