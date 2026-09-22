---
stufe: voranalyse
slug: vogelfuttersaeule-edelstahl
datum: 2026-09-22
bearbeiter: claude
quellen_stand: 2026-09-22
quellen_eingeschraenkt: [amazon.de Captcha (AWS-WAF, *.awswaf.com vom Proxy gesperrt), alibaba.com Egress gesperrt, shop.dobar.de Egress gesperrt]
referenz_asin: B0B21K47D4
hauptkategorie: Garten › Vogelfutter & Zubehör › Futterstationen für Wildvögel
fazit: Nicht weiter verfolgen in dieser Form – Nachfrage und angreifbare Edelstahl-Listings vorhanden, aber DB1 ~20 % und Break-even-ACOS ~17 % nach 30-%-Regel (Standardpaket, 30 € VK); nur ein belegter EK ≤ 6 € dreht die Rechnung.
score: 54
zone: review
vk_ziel: 29,90 €
ek_annahme: ~8,97 €
db1_prozent: ~20 %
break_even_acos: ~17 %
kapitalbedarf: ~6.900 €
ko: nein
empfehlung: Stop
---

# Voranalyse – Vogelfuttersäule Edelstahl (vogelfuttersaeule-edelstahl)

> Alle Prüfpunkte bleiben stehen. Beobachtet: `Wert (Quelle, YYYY-MM-DD)` · Schätzung: `~Wert (Schätzung: Grundlage)` · nicht ermittelbar: `[fehlt]`. Regeln: `rules/voranalyse.md`, `rules/kalkulation.md`, `rules/scoring.md`.

> **Quellen-Einschränkung dieses Laufs (2026-09-22):** `node scripts/amazon.mjs` brach mit Exit 2 ab (AWS-WAF-Prüfung, `*.awswaf.com` vom Egress-Proxy mit 403 abgewiesen). WebFetch auf Amazon.de lieferte nur den Seitenkopf (Titel, Maße), keine Preise/BSR. Alibaba und shop.dobar.de: Egress gesperrt. Amazon-Werte (Preis, Sterne, Bewertungen, BSR) stammen aus dem `/amazon`-Abruf des Ideen-Laufs vom selben Tag (`ideas/_laeufe/2026-09-22-marktluecken-edelstahl.md`, zitiert als „Amazon.de, 2026-09-22"); alles Weitere aus Suchmaschinen- und Händler-Snippets. Autocomplete (Nr. 23) und Produktseiten-Rezensionen konnten nicht abgerufen werden.

## Kopf

| Feld | Inhalt |
|---|---|
| Datum der Erfassung | 2026-09-22 |
| Produktbezeichnung / Hauptkeyword | Vogelfuttersäule Edelstahl (Vogelfutterspender Edelstahl / Futtersäule Edelstahl / Futtersilo) |
| ASIN Referenzprodukt / Hauptkonkurrent | B0B21K47D4 (Relaxdays Vogelfutterhaus Edelstahl, bestes Ranking im Edelstahl-Segment: BSR 7.341 Garten / Nr. 46 Futterstationen, Amazon.de, 2026-09-22) · https://www.amazon.de/dp/B0B21K47D4 – Hinweis: Relaxdays ist ein Futterhaus mit Erdspieß (16 × 17,5 × 17 cm, Amazon.de-Seitenkopf, 2026-09-22), keine Säule. Säulen-Referenz: B009WNGW8U (Haushalt International, 778 Bew.) |
| Hauptkategorie auf Amazon | Garten › Vogelfutter & Zubehör › Futterstationen für Wildvögel (Relaxdays Nr. 46 in Futterstationen, Amazon.de, 2026-09-22) |

## Checkliste (Originalreihenfolge)

OK: ✅ unkritisch · ⚠️ Einschränkung · ❌ kritisch. Spalte „Erklärung" ist der Originaltext aus `rules/voranalyse.md`.

### Block 1: Produkt

| Nr. | Merkmal | Erklärung (Original) | OK | Ergebnis / Bemerkung |
|---|---|---|---|---|
| 1 | Größe / Abmaße des Produktes | Produkte mit großen Abmaßen sind kostspieliger im Fulfillment & Import | ⚠️ | Esschert FB393 Edelstahl-Silo 14,1 × 14,1 × 27,1 cm (bloomling/vogelfutter24-Snippet, 2026-09-22); Relaxdays 16 × 17,5 × 17 cm (Amazon.de, 2026-09-22); Wettbewerber-Säulen 26–52 cm (wildtier liebe 35/52 cm, Snippets, 2026-09-22). Verpackt ~16 × 16 × 30 cm (Schätzung: Produktmaße + Karton) → Höhe > 12 cm, **„Kleines Paket" (max. 35 × 25 × 12 cm) nicht erreichbar**, FBA-Standardpaket. |
| 2 | Gewicht des Produktes | Schwere Produkte > 2kg sind kostspieliger im Fulfillment & Import | ✅ | Esschert FB393 (Edelstahl + PC) 0,31 kg (Snippet, 2026-09-22). Mit Glassilo ~0,5–0,6 kg netto, ~0,7–0,8 kg versandfertig (Schätzung: Borosilikatrohr Ø 8 cm × 20 cm + Einlage). Weit unter 2 kg. |
| 3 | Komplexität / Beschaffenheit | Besteht das Produkt aus vielen Einzelteilen? Ist es sehr filigran? Überlege dir, ob das Produkt aufgrund der Beschaffenheit anfällig für Probleme sein könnte. | ⚠️ | 5–6 Teile: Dach, Silo, Boden/Futterschale, 2–4 Sitzstangen, Aufhängung. Kritisch sind Bodenverschluss und Silo: dobar 10089 „Boden über waghalsigen Klemmmechanismus", „nach kurzer Zeit aufgeplatzt" (Produktseite B007JTD46W, Amazon.de, 2026-09-22); MIXXIDEA „rostet am Deckel und an den Futterlöchern" (Amazon.de-Rezensionssnippet, 2026-09-22). Glassilo = Bruchrisiko in Transport und Nutzung. |
| 4 | Chemisches Produkt / Lebensmittel | Bei chemischen Produkten (insb. mit Hautkontakt) & Lebensmitteln bestehen erhöhte Prüfanforderungen, die häufig weitere Investments erforderlich machen | ✅ | Nein. Futterbehälter für Wildvögel, kein Lebensmittelkontakt im Sinne LFGB (Heimtierfutter-Kontakt ohne Prüfpflicht, Schätzung). Futter wird nicht mitverkauft. |
| 5 | Elektroprodukt | Bei Elektroprodukten geht der Markteinstieg grundsätzlich mit erhöhten Prüf-, Zertifizierungs- und Registrierungsanforderungen einher. | ✅ | Nein (keine Kamera-/Solarvariante vorgesehen). |
| 6 | Erotik-Produkt / Produkte für Erwachsene | Erotikprodukte unterliegen einer Werbebeschränkung, so dass sich hier Nachteile für den Markteinstieg ergeben. Es können keine Werbeanzeigen geschaltet werden. | ✅ | Nein. |
| 7 | Produkt mit hoher Retourenquote | Produkte mit hoher Retourenquote erzeugen hohe Zusatzkosten. Beispiele sind: Kleidung, Schuhe, Schutzanzüge, Handschuhe | ⚠️ | Keine Größenabhängigkeit. Retourenrisiko aus Transportbruch (Glassilo) und „Vögel nehmen es nicht an"; Retourenquote [fehlt], ~3–5 % (Schätzung: Garten-Hartware). |
| 8 | Markt mit ausgeprägtem Design Fokus (Geschmack) | Produkte, bei denen die Geschmacksfrage im absoluten Vordergrund steht, können sehr problematisch sein. Wenn das von dir realisierte Design nicht den Geschmack der Kunden trifft, kann das ganze sehr unprofitabel werden. Beispiele sind: Schmuck, Deko-Objekte & Accessoires, Kleidung | ⚠️ | Funktion (Futter trocken, Reinigung, Wetterfestigkeit) steht vorn; Design differenziert im Premium-Segment (dobar „Premium-Pickbar" Echtglas ab 50,99 €, testbericht.de-Snippet, 2026-09-22). Silber/Edelstahl ist neutral – geringes Geschmacksrisiko. |

### Block 2: Markt

| Nr. | Merkmal | Erklärung (Original) | OK | Ergebnis / Bemerkung |
|---|---|---|---|---|
| 9 | Bestseller Rang (Ersteindruck der Verkaufszahlen) | Prüfe, ob das gefundene Produkt aktuell ein gutes Ranking besitzt. Nutze die BSR-Tabelle oder Junglescout Sales Estimator um eine Einschätzung über die aktuellen Verkaufszahlen vorzunehmen. | ⚠️ | Relaxdays B0B21K47D4 BSR 7.341 Garten; Haushalt International B009WNGW8U BSR 21.949; dobar B007JTD46W BSR 20.663 (alle Amazon.de, 2026-09-22) → ~100 / ~30 / ~30 St./Monat im September (Schätzung aus BSR nach `rules/quellen.md`, Nebensaison). Q4 ~×3–5 (Schätzung: Saisonmuster Winterfütterung). |
| 10 | Preis & Preisbereich überprüfen | Für welchen Preis wird das Referenzprodukt angeboten? In welchem Preisbereich fällt der Großteil der Nachfrage ab? Die Preisstellung sollte > 10€ sein, damit der Einstieg sich wirklich lohnt. Verwende Helium10, um dir hierzu den besten Überblick zu verschaffen. | ✅ | Referenz 24,09 €. Suche „vogelfutterspender edelstahl": 8,02–80,20 €, Median 22,94 €, 46 organische Listings (Amazon.de, 2026-09-22). Edelstahl-Säulen 18,53–27,53 € (ebd.); wildtier liebe 23,90–27,90 € (moebel.de/reavet-Snippets, 2026-09-22); Esschert FB393 19,99 € Fachhandel (bloomling, 2026-09-22). Nachfrageschwerpunkt ~18–28 € (Schätzung aus Bewertungsverteilung). > 10 € erfüllt. |
| 11 | Umsatzvolumen, Absatz im vorderen Feld | Entsprechen Umsatz, Absatz & Gewinn der aktuellen Marktteilnehmer den eigenen Erwartungen? Ist das Umsatzvolumen insgesamt hoch genug? Verwende Helium10, um dir hierzu den besten Überblick zu verschaffen. | ⚠️ | Edelstahl-Top-3 ~160 St./Monat × ~22 € ≈ ~3.500 €/Monat im September (Schätzung aus BSR); Jahr ~2.000–3.000 St. ≈ ~50.000–65.000 € für die Top-3 (Schätzung: Q4 ×3–5, Sommer ×0,5). Gesamtmarkt Wildvogelfutter DE 145 Mio. € 2024 (pet-online 10/2025, Snippet, 2026-09-22) – Futterstellen-Anteil [fehlt]. |
| 12 | Markttiefe | Ist eine geringe oder ausgeprägte Tiefe vorhanden? Erzielen mindestens 2-3 Anbieter annehmbare Verkaufszahlen? Verwende Helium10, um dir hierzu den besten Überblick zu verschaffen. | ✅ | Ausgeprägte Tiefe: 381 Ergebnisse, 46 organische Listings Seite 1 (Amazon.de, 2026-09-22); ≥ 6 Anbieter mit ≥ 400 Bewertungen im Umfeld (MIXXIDEA 2.234 / 1.178, PROVIDE 1.971, Dehner 1.371, HI 778, dobar 487; Amazon.de, 2026-09-22). |
| 13 | Saisonalität / Trendverlauf | Eine Saisonalität liegt vor, wenn sich das Produkt nur in bestimmten Zeiträumen besonders gut verkauft. Nutze Keepa oder Helium10, um dir die Verkaufshistorien der Mitbewerber im vorderen Feld ganz genau anzusehen. Zusätzlich kannst du die Hauptkeywords mit Google Trends untersuchen. | ⚠️ | Deutliche Saison Oktober–Februar: Futterstelle „im September oder Oktober einrichten" (umweltberatung.at, NABU-Snippets, 2026-09-22); Saisonstart Spätherbst (pet-online 10/2025). Ganzjahresfütterung wächst (NABU). Google Trends 5 Jahre [fehlt] (nicht abrufbar). Einkauf muss bis ~August stehen. |
| 14 | Nachfrage konstant? | Helium10 und der Sales Estimator zeigen dir immer nur eine Momentaufnahme des Marktes. Prüfe also, ob das Produkt sich bereits über einen längeren Zeitraum gut verkauft hat. Hierzu kannst du Keepa oder Helium10 nutzen und dir die Historie ansehen. | ✅ | Langlebige Nachfrage: dobar B007… und HI B009… seit ~2012/13 gelistet (Schätzung aus ASIN-Präfix) und weiter im Ranking; Wildvogelfütterung ist jährlich wiederkehrend. Keepa-Historie [fehlt]. |
| 15 | Anzahl der Bewertungen | Haben die Seller im vorderen Feld bereits ausschließlich sehr viele Bewertungen gesammelt? Falls Ja: Gibt es weitere Anbieter, die auch mit weniger Bewertungen annehmbare Verkaufszahlen erreichen? | ✅ | Nein, gemischt: Relaxdays erreicht mit 98 Bew. den besten BSR (7.341) im Edelstahl-Segment; MeLiTec B0D7MPMWQ4 23 Bew. auf Seite 1 (Amazon.de, 2026-09-22). Max. 2.234 Bew. im Umfeld, kein Listing > 5.000. |

### Block 3: Wettbewerb und Positionierung

| Nr. | Merkmal | Erklärung (Original) | OK | Ergebnis / Bemerkung |
|---|---|---|---|---|
| 16 | Old Niche Sellers im vorderen Feld? | Angebote, die bereits sehr lange auf Amazon aktiv sind haben sich häufig sehr stark im Ranking gefestigt und sich insgesamt stark positioniert. Erzielen in dem Markt ausschließlich Anbieter annehmbare Verkaufszahlen, die das Produkt bereits sehr lange auf Amazon verkaufen? Sieh dir hierzu das Datum des Verkaufsstarts und die Historie an. | ⚠️ | Gemischt: dobar B007JTD46W und HI B009WNGW8U ~2012/13, Dehner/Esschert als Alt-Marken; aber Relaxdays B0B21K47D4 ~2022 mit bestem BSR, MeLiTec B0D7MPMWQ4 ~2024 (Schätzung aus ASIN-Präfix, „erhältlich seit" [fehlt]). Neue Listings kommen rein. |
| 17 | Markttendenz Funktional vs. Emotional | Nimm hier eine Einschätzung darüber vor, ob das Produkt eher emotionaler oder funktionaler Natur ist. Natürlich gibt es nicht nur diese beiden „Extreme", allerdings ermöglicht die Eingrenzung weitere Interpretationen über das Kaufverhalten der Kunden und darüber, welche Faktoren bei der Kaufentscheidung im Vordergrund stehen. Emotional: Stöbern, Bereitschaft höhere Preise zu zahlen, starkes Marketing möglich. Funktional: schnelle Kaufentscheidung, Preis steht bei Kaufentscheidung häufig im Vordergrund, begrenzte o. keine emotionale Bindung zum Produkt | ⚠️ | Überwiegend funktional (Preisanker 18–23 €, Vergleich über Füllmenge/Futteröffnungen), mit emotionaler Komponente (Vögel beobachten, Naturschutz, Geschenk Q4). Premium über 30 € nur mit Designmarke (PROVIDE 39,96 €, dobar Echtglas 50,99 €). |
| 18 | Markendominanz / Markentreue | Ist ersichtlich, dass die Nachfrage in der Nische nur auf bekannte oder stark etablierte Markenprodukte abfällt? Gibt es neben etablierten Marken weitere Private Label Produkte, die ebenfalls annehmbare Verkaufszahlen erreichen? Dominieren Markenprodukte den Löwenanteil der Nachfrage? | ⚠️ | Keine Einzeldominanz, aber dichtes Feld aus Fachmarken (dobar, Dehner, CJ Wildlife, Vivara, wildtier liebe, Esschert) und Private Label (Relaxdays, HI, MIXXIDEA, MeLiTec). Private Label verkauft annehmbar (Relaxdays BSR 7.341). |
| 19 | Vermarktung & Optimierung der Wettbewerber | Ersteindruck: Wie wurde die Vermarktung bei den Topsellern im vorderen Feld umgesetzt? Sind die Produktbilder professionell? Gibt es bereits starke USPs? Wurden Produktbeschreibung und Bulletpoints verkaufspsychologisch gut umgesetzt? Schätze ein, ob du die direkten Mitbewerber schlagen und das ganze deutlich besser machen kannst. | ⚠️ | Titel keyword-lastig („Vogelfutterspender zum Aufhängen, mit Erdspieß…", Relaxdays; „Vogel-Futterstation, Futtersäule, Wildvögel Futtersilo I Ganzjährige Vogelfütterung", wildtier liebe; Amazon.de-Titel, 2026-09-22). wildtier liebe mit Ratgeber-Beigabe als USP. Bilder/A+ [fehlt] (Produktseiten nicht lesbar). Händler-Listing HI ohne Markenauftritt. |
| 20 | Möglichkeiten für Verbesserungen, Optimierungen & USPs? | Ersteindruck: Was sagen die Kunden über die bestehenden Produkte? Gibt es Optimierungsmöglichkeiten, anhand welcher du das Produkt deutlich aufwerten kannst? Kannst du ein deutlich besseres Angebot positionieren und einen klaren Nutzenvorteil / ein klares Alleinstellungsmerkmal realisieren, welches du gezielt kommunizieren kannst? | ✅ | Kundenkritik: Klemmboden löst sich, Silo platzt (dobar, 3,8★); Rost an Deckel/Futterlöchern (MIXXIDEA); Acryl/PC altert. Hebel: Vollmetall 304 inkl. Sitzstangen, Bajonett-Boden werkzeuglos zerlegbar (Reinigung alle 2–3 Wochen empfohlen, Vivara-Snippet, 2026-09-22), Glassilo. Aber: dobar besetzt „Echtglas-Premium" bereits (50,99 €). |
| 21 | Brand Building | Ersteindruck: Lässt sich eine Marke um das Produkt oder den Produktbereich bauen? Dies wäre langfristig für die Vermarktung von Vorteil. | ⚠️ | Wildvogel-Linie mit `vogeltraenke-vogelbad` (Longlist) und `meisenknoedelhalter-edelstahl` (Lane D) denkbar – aber außerhalb Pflanzenpflege, eigene Zielgruppe (Vogelfreunde, Tierbedarf) mit wenig Cross-Selling zu NG0001/NG0002. |
| 22 | Alibaba Check / EK | Grobe Alibaba Recherche, wie sehen die EKs aus etc. / Grober Richtwert EK ca. 20% vom VK Vergleichsprodukt | ⚠️ | Alibaba per WebFetch gesperrt. Showroom-Snippet „Stainless Steel Bird Feeder": 2.000+ Produkte, MOQ 1–100 Stück (alibaba.com-Snippet, 2026-09-22), Preise für Säulen [fehlt] (nur Kolibri-Tränken ~2,70 $). Richtwert 20 % vom VK 24,09 € = ~4,80 €. Plausibilität: Esschert FB393 19,99 € Endpreis → Fabrik-EK ~3–5 € (Schätzung: Handelsspannen Fachhandel/Großhandel). Kalkulationsbasis nach Regel: 30 % vom Ziel-VK = ~8,97 €. |

### Block 4: Ergänzungen [neu]

**23. Keywords**

| Typ | Keyword | Quelle |
|---|---|---|
| Haupt | vogelfutterspender edelstahl | Amazon-Suchseite (Ideen-Lauf `/amazon suche`, Amazon.de, 2026-09-22); Autocomplete [fehlt] (WAF) |
| Neben | futtersäule edelstahl | Amazon-Suchseite mit Node 4380814031 (Suchmaschinen-Index, 2026-09-22); Listing-Titel wildtier liebe, B004S1TORW |
| Neben | vogelfutterstation edelstahl / zum aufhängen | Listing-Titel HI B009WNGW8U, Relaxdays B0B21K47D4 (Amazon.de, 2026-09-22) |
| Neben | futtersilo vögel | Listing-Titel wildtier liebe B0CGV7BYBN, Esschert „Vogelfuttersilo" (Snippets, 2026-09-22) |
| Neben | futtersäule wildvögel ganzjährig | Listing-Titel wildtier liebe (Snippet, 2026-09-22) |

**24. Top-Listings** (5–10; Ergänzung zu Nr. 9–12 und 16–19)

| # | Marke / Titel (gekürzt) | ASIN | Preis | Sterne | Bewert. | Material | Varianten | Bilder (1–3) | Sichtbare Schwäche | abgerufen |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Relaxdays Vogelfutterhaus Edelstahl mit Erdspieß | B0B21K47D4 | 24,09 € | 4,2 | 98 | Edelstahl | [fehlt] | [fehlt] | Futterhaus statt Säule, Relaxdays-Massenlisting | 2026-09-22 |
| 2 | Haushalt International Edelstahl Vogelfutterstation | B009WNGW8U | 21,79 € | 4,3 | 778 | Edelstahl + Kunststoffsilo | [fehlt] | [fehlt] | Händlerlisting ohne Marke, altes Listing (~2013) | 2026-09-22 |
| 3 | dobar 10089 Futtersäule Edelstahlschlaufe | B007JTD46W | 18,53 € | 3,8 | 487 | Acryl + Metall | [fehlt] | [fehlt] | Klemmboden, Silo platzt (Rezensionen) | 2026-09-22 |
| 4 | MIXXIDEA Futterspender Edelstahl | B09MFCS2C1 | 24,08 € | 4,3 | 1.178 | Edelstahl | [fehlt] | [fehlt] | Rost an Deckel/Futterlöchern (Rezensions-Snippet MIXXIDEA) | 2026-09-22 |
| 5 | MeLiTec Edelstahl Vogelfutterhaus | B0D7MPMWQ4 | 26,38 € | 4,4 | 23 | Edelstahl | [fehlt] | [fehlt] | Neu (~2024), kaum Bewertungen | 2026-09-22 |
| 6 | MIXXIDEA Metallrohr-Futterspender 6 Öffnungen | B08CDCM5KQ (Titel-Übereinstimmung, Snippet) | 20,64 € | 4,4 | 2.234 | Metall lackiert + PC | Farben (Grün, Kupfer) | [fehlt] | Lackiertes Metall, kein Edelstahl | 2026-09-22 |
| 7 | PROVIDE Futterstation | [fehlt] | 39,96 € | 4,7 | 1.971 | [fehlt] | [fehlt] | [fehlt] | Preisanker oben, Station statt Säule | 2026-09-22 |
| 8 | Dehner Triple Futtersäule | [fehlt] | 22,94 € | 4,3 | 1.371 | Metall schwarz + Kunststoff | 3 Säulen | [fehlt] | Kein Edelstahl | 2026-09-22 |
| 9 | wildtier liebe Futtersäule 35/52 cm Edelstahl | B0CGV7439P / B0CGV7BYBN | 23,90–27,90 € (moebel.de/reavet-Snippets) | [fehlt] | [fehlt] | Edelstahl + Kunststoffsilo | 26/35/38/52 cm, Silber/Schwarz | [fehlt] | Kunststoffsilo, Direktmarke mit Ratgeber | 2026-09-22 |
| 10 | Esschert Design FB393 Vogelfuttersilo (Fachhandel, Amazon [fehlt]) | – | 19,99 € (bloomling) | [fehlt] | [fehlt] | Edelstahl + PC, 310 g | – | [fehlt] | PC-Silo, Designmarke unter 20 € | 2026-09-22 |

Wettbewerbsstruktur: China-Direkt 2 von 10 (MIXXIDEA ×2, MeLiTec wahrscheinlich) · Große Marken: Dehner, dobar, wildtier liebe, Esschert, CJ Wildlife, Vivara · Private Label: Relaxdays, Haushalt International, PROVIDE · Preisband beobachtet: 18,53 – 39,96 € (Säulen/Stationen), Suche gesamt 8,02–80,20 €.
Die zwei angreifbarsten Listings: 1. dobar 10089 (B007JTD46W) – warum: 3,8★, Klemmboden und platzendes Silo als wiederkehrende Kritik, Acrylsilo · 2. Haushalt International (B009WNGW8U) – warum: 778 Bew. bei 4,3★ ohne Markenauftritt, Kunststoffsilo, Listing-Generation 2013.

**25. Markteintritts-Realismus**
- Bewertungen für Seite 1 (Bandbreite): ~20–2.200 (Amazon.de, 2026-09-22: MeLiTec 23 bis MIXXIDEA 2.234); für die Edelstahl-Top-5 ~100–800 (Schätzung)
- Zeithorizont: ~9–12 Monate bis stabile Seite 1 (Schätzung: Launch muss vor Oktober live sein, sonst ein Jahr Warten; erste Saison für Bewertungsaufbau)
- CPC-Niveau: ~0,50–0,80 € (Schätzung: Nischenvergleich Garten/Tierbedarf, Q4-Konkurrenz durch Fachmarken). Bei ~10 % Conversion entspricht das einem nötigen ACOS von ~17–27 % bei 29,90 €.

**26. Grobe Kalkulation** (`rules/kalkulation.md`, eine Variante, Pauschalen)

VK-Korridor Wettbewerb: 18,53 – 27,53 € (Edelstahl-Säulen, Amazon.de, 2026-09-22), Premium-Ausreißer 39,96–50,99 € · Ziel-VK nicegarden: 29,90 € (Begründung Premium-Position: über Relaxdays 24,09 € und MeLiTec 26,38 € mit Vollmetall + Glassilo, deutlich unter PROVIDE 39,96 € und dobar Echtglas 50,99 €)

| Position | Wert | Grundlage |
|---|---|---|
| Brutto-VK | 29,90 € | Ziel-VK |
| Netto-VK (/1,19) | 25,13 € | |
| EK je Stück | ~8,97 € | 30-%-Regel (kein Alibaba-Angebot, Egress gesperrt) |
| Fracht + Zoll + Nebenkosten je Stück | ~1,75 € | Pauschale: Seefracht ~1,10 € (Schätzung: Karton ~16 × 16 × 30 cm = 7,7 l, ~140 €/m³), Zoll ~0,25 € (Schätzung: 2,7 % auf 7326 90 98, Einreihung ungeprüft), Einfuhrnebenkosten ~0,40 € |
| Landed Cost | ~10,72 € | |
| Verkaufsgebühr 15 % | 4,49 € | Kategorie Garten |
| FBA-Größenklasse | Standardpaket (Höhe ~30 cm > 12 cm) | Maße (Nr. 1–2) |
| FBA-Versand | ~4,80 € | Schätzung: 1-kg-Pakete DE 3,99–5,99 € (automationsmanufaktur/pandotax-Snippets, 2026-09-22) + 1,5 % Treibstoffzuschlag seit 17.04.2026; Rate Card 07/2026 nicht lesbar |
| **DB1** | ~5,12 € = ~20 % | Sensitivität: EK ~6,00 € → DB1 ~8,18 € = ~33 %; EK ~4,50 € → ~9,72 € = ~39 %; VK 34,90 € bei 30-%-Regel → ~7,03 € = ~24 % |
| **Break-even-ACOS** | ~17 % | vs. CPC-Niveau (Nr. 25, nötiger ACOS ~17–27 %): **unterschritten**. Bei EK ~6,00 € ~27 % (knapp), bei EK ~4,50 € ~33 % (ok) |
| Kapitalbedarf-Check | ~500 Stück × 10,72 € = ~5.360 € + Erstausstattung ~1.500 € (Fotos, Verpackung, Glas-Bruchtest-Samples) = ~6.900 € | typische MOQ 500 (Schätzung; Alibaba-Snippet MOQ 1–100 gilt für Handelsware); Saisonware: gesamte Charge bis September einlagern |

**27. Differenzierungshypothesen** (3–5, je aus einer beobachteten Schwäche; Ergänzung zu Nr. 20)

| # | Hypothese | Abgeleitet aus |
|---|---|---|
| 1 | Bajonett-Boden aus Edelstahl statt Klemmung, werkzeuglos zerlegbar, spülmaschinenfest | dobar 10089: „Boden über waghalsigen Klemmmechanismus", „aufgeplatzt" (3,8★); Reinigung alle 2–3 Wochen empfohlen (Vivara) |
| 2 | Silo aus Borosilikatglas statt Acryl/PC (vergilbt nicht, kratzfest), bruchsicher verpackt | Acryl-/PC-Silos bei dobar, HI, Esschert, wildtier liebe; UV-Alterung als Thema in Ratgebern |
| 3 | Vollständig 304-Edelstahl inkl. Sitzstangen und Aufhängung – Rostfrei-Versprechen | MIXXIDEA: „rostet am Deckel und an den Futterlöchern" |
| 4 | Pflegeset/Ratgeber-Karte „Ganzjahresfütterung" + Geschenkverpackung für Q4 | wildtier liebe nutzt Ratgeber als USP; Geschenkanlass Q4, Futterstelle ab September einrichten |
| 5 | Linie „Wildvogel" mit Vogeltränke Edelstahl (Longlist) als Bundle | Miro-Longlist `vogeltraenke-vogelbad`; keine Edelstahl-Linie auf Amazon.de erkennbar |

**28. IP-Schnellcheck**
DPMA/EUIPO Marken: Register nicht abgefragt (Egress) → [fehlt]; Wettbewerbermarken (dobar, Dehner, wildtier liebe, Esschert, MIXXIDEA) betreffen Namen, nicht Gattung · Google Patents / DPMAregister Design: kein Treffer zu eingetragenem Design/Gebrauchsmuster für Futtersäule mit Bajonettboden in Snippets (2026-09-22); Bajonettverschluss bei Futtersäulen bereits am Markt (anyprint3d BirdieBistro, Snippet, 2026-09-22) → Allgemeingut, kein Alleinstellungsschutz · Ergebnis: **prüfen** (Registerabfrage nachholen, Grundform Rohr + Dach gilt als Allgemeingut)

**29. Material, Compliance, Logistik**
Materialien (max. 2): Edelstahl 304 (Dach, Boden, Stangen, Aufhängung) + Borosilikatglas (Silo) – 2 Materialien; Dichtung/Ringe [fehlt] · GPSR-Kennzeichnung: Hersteller-/Importeurangabe, Chargen-ID, Warnhinweis Glas (Standard) · Verpackungsgesetz/LUCID: Registrierung besteht für NG0001/NG0002, Karton + Einlage anmelden · Elektronik/Lebensmittelkontakt/Spielzeug: nein/nein/nein
Maße: ~14 × 14 × 27 cm netto, ~16 × 16 × 30 cm verpackt (Schätzung, Nr. 1) · Gewicht: ~0,5–0,6 kg netto, ~0,7–0,8 kg versandfertig (Schätzung) · Bruchrisiko: **mittel–hoch** (Glassilo; Alternative PC senkt Risiko, verliert USP) · „Kleines Paket" erreichbar: nein (Höhe > 12 cm)

**30. Weitere Risiken**
Saisonalität: hoch – Absatz konzentriert auf Oktober–Februar, Einkauf bis August, Restbestand überwintert bei Q4-Lagergebühr 52,20 €/m³ (Snippet, 2026-09-22) · China-Direkt: mittel – MIXXIDEA/MeLiTec im Edelstahl-Segment, Esschert Designmarke bei 19,99 € als Preisdeckel · Kategorie-Beschränkungen Amazon: keine bekannt (Garten, ungated) · Sonstiges: Markenfit nur Garten-nah (Wildvogel statt Pflanzenpflege); Glasbruch-Retouren; Preisanker 18–24 € begrenzt Ziel-VK.

## Fazit

**Fazit:** Nicht weiter verfolgen in dieser Form – nur mit belegtem EK ≤ 6 € neu bewerten:
1. Nachfrage ist real und wiederkehrend: Relaxdays erreicht mit 98 Bewertungen BSR 7.341 schon in der Nebensaison, Q4 ×3–5, Marktumfeld mit ≥ 6 Anbietern > 400 Bewertungen.
2. Wettbewerb ist qualitativ angreifbar (dobar 3,8★ Klemmboden, MIXXIDEA Rost, Acryl-/PC-Silos), aber dicht besetzt mit Fachmarken und Preisankern bei 18–24 €.
3. Die Kalkulation trägt nicht: Standardpaket (~4,80 € FBA) plus 30-%-EK ergeben bei 29,90 € nur ~20 % DB1 und ~17 % Break-even-ACOS – unter dem nötigen ACOS von ~17–27 % (Red Flag).
4. Markenfit ist nur Garten-nah (Wildvogel), kaum Cross-Selling zu Gießkanne und Bewässerungskugeln; Saisonlager bindet ~6.900 € bis Q4.
5. Die Rechnung dreht nur ein Alibaba-Angebot ≤ 6 € (DB1 ~33 %) bzw. ≤ 4,50 € (DB1 ~39 %) – Esschert FB393 für 19,99 € Endpreis macht das plausibel, belegt ist es nicht.

### Score (`rules/scoring.md`)

| # | Kriterium | Gewicht | Teilnote 0–10 | Begründung (ein Satz mit Zahl oder Grund) |
|---|---|---|---|---|
| 1 | Marge & DB-Potenzial | 25 % | 3 | DB1 ~20 % und Break-even-ACOS ~17 % nach 30-%-Regel bei Standardpaket-FBA ~4,80 €; erst bei EK ≤ 6 € über 30 %. |
| 2 | Nachfrage | 20 % | 6 | BSR 7.341 (Relaxdays) in der Nebensaison und Q4-Peak, aber stark saisonal Oktober–Februar. |
| 3 | Wettbewerb (invers) | 20 % | 6 | Top-Edelstahl-Listings 3,8–4,4★ mit 23–1.178 Bewertungen angreifbar, Umfeld aber dicht mit Fachmarken und Preisankern 18–24 €. |
| 4 | Logistik & FBA-Fit | 10 % | 6 | ~0,7–0,8 kg versandfertig, aber ~30 cm hoch (Standardpaket statt Kleines Paket) und Glassilo mit Bruchrisiko. |
| 5 | Markenfit & Synergien | 10 % | 6 | Edelstahl und Garten/Balkon passen, aber Wildvogel statt Pflanzenpflege, kein direktes Bundle mit NG0001/NG0002. |
| 6 | Risikoprofil (invers) | 15 % | 7 | Kein IP- oder Compliance-Treffer, Risiken sind Saisonlager und Glasbruch – lösbar. |

K.O.-Prüfung (`rules/scoring.md` Abschnitt 3): nein – K0 nicht erreicht (Marge 3 > 2), K1–K7 unauffällig (mechanisch, < 2 kg, VK > 10 €, Garten-Bezug)
Red Flag (`rules/scoring.md` Abschnitt 3): **ja** – Break-even-ACOS ~17 % unter dem geschätzten CPC-Niveau (nötiger ACOS ~17–27 %)
**Gesamtscore: 54 / 100 → Zone: Review → Lane: C** · Empfehlung wegen Red Flag: Stop

Kippende Kriterien: Marge (3). Belegt ein Alibaba-Angebot EK ≤ 6 € inkl. Glassilo, steigt Marge auf 5–6 → Gesamtscore ~59–62, Zone Review, Lane C–B, Break-even-ACOS ~27 % (knapp im CPC-Band, Red Flag entfällt). Mit EK ≤ 4,50 € (Marge 7) und Nachfrage 7 (belegter Q4-BSR < 3.000) → ~66.

### Offene Fragen für die Tiefenanalyse
- Alibaba-Angebot Edelstahl-Futtersäule 304 mit Borosilikatsilo: Preis, MOQ, Bruchtest, Lead Time (Egress gesperrt) – entscheidet über Stop oder Neubewertung.
- FBA-Größenklasse und Gebühr exakt nach Rate Card 07/2026 (PDF nicht lesbar) – ggf. flachere Verpackung (Silo separat) für günstigere Klasse.
- Q4-BSR der Top-5 (Keepa fehlt) – Amazon-Abruf im Oktober/November wiederholen.
- Google Trends „vogelfutterspender" / „futtersäule" 5 Jahre DE.
- DPMA/EUIPO-Registerabfrage.
- Glas vs. PC: Bruchquote, Kunden-Präferenz (dobar Echtglas-Rezensionen).

## Quellen
- https://www.amazon.de/s?k=vogelfutterspender+edelstahl (Ideen-Lauf `/amazon suche`, 2026-09-22)
- https://www.amazon.de/dp/B0B21K47D4 · https://www.amazon.de/dp/B007JTD46W · https://www.amazon.de/dp/B009WNGW8U (Ideen-Lauf `/amazon produkt` 2026-09-22; WebFetch Seitenkopf 2026-09-22)
- https://www.amazon.de/dp/B09MFCS2C1 · https://www.amazon.de/dp/B0D7MPMWQ4 (2026-09-22)
- https://www.amazon.de/Vogelfutterspender-Anschl%C3%BCsse-transparent-Stahlaufh%C3%A4nger-wetterfest/dp/B08CDCM5KQ (Snippet, 2026-09-22)
- https://www.amazon.de/wildtier-liebe-Vogelfutters%C3%A4ule-Edelstahl-Silber/dp/B0CGV7439P · https://www.amazon.de/wildtier-liebe-Vogelfutterspender-Vogel-Futterstation-Vogelfutter-S%C3%A4ule/dp/B0CGV7BYBN (Snippets, 2026-09-22)
- https://reavet.de/Futtersaeule-fuer-Samen-Koerner-Kerne-52cm-versch-Farben · https://www.kaufland.de/product/486963786/ (Snippets, 2026-09-22)
- https://www.bloomling.de/esschert-design/edelstahlvogelfuttersilo · https://www.vogelfutter24.de/onlineshop/futterspender-systeme/futterautomaten-fuer-koerner/5902/fb393-edelstahlvogelfuttersilo (Esschert FB393, 2026-09-22)
- https://shop.dobar.de/produkt/vogelfuttersaeule-premium-pickbar-aus-echtglas/ · https://www.testbericht.de/vogelhaus/futtersilo (Snippets, 2026-09-22)
- https://www.gruenteam-versand.de/premium-futtersaeule-888 (CJ Wildlife, Snippet, 2026-09-22)
- https://www.vivara.de/futtersaeulen-reinigen (Snippet, 2026-09-22)
- https://www.anyprint3d.de/de/vogelfutterspender-birdiebistro.html (Bajonettverschluss, Snippet, 2026-09-22)
- https://www.alibaba.com/showroom/stainless-steel-bird-feeder.html (Snippet, 2026-09-22)
- https://www.petonline.de/daten/pet/2025/10-2025/gartenvoegel-im-fokus.html (Wildvogelfutter 145 Mio. €, 2026-09-22)
- https://www.umweltberatung.at/winterfuetterung-fuer-voegel · https://www.nabu.de/tiere-und-pflanzen/voegel/helfen/vogelfuetterung/index.html (Saison, 2026-09-22)
- https://automationsmanufaktur.de/blog/amazon-fba-gebuehren-2026 · https://pandotax.de/ecommerce/amazon-gebuehrensenkung-2026/ (FBA 2026, Snippets, 2026-09-22)
- https://m.media-amazon.com/images/G/02/sell/images/260630-FBA-Rate-Card-DE1.pdf (abgerufen, Text nicht extrahierbar, 2026-09-22)

---
## Gate 1: Voranalyse – vogelfuttersaeule-edelstahl
**Ergebnis:** Score 54 / 100, Zone Review, DB1 ~20 % (Schätzung, EK nach 30-%-Regel), Break-even-ACOS ~17 %
**Empfehlung:** Stop
**Begründung (3 Sätze max):** Nachfrage und angreifbare Edelstahl-Listings sind vorhanden, aber Standardpaket-FBA und 30-%-EK drücken DB1 auf ~20 % und den Break-even-ACOS auf ~17 % – unter dem nötigen ACOS von ~17–27 % (Red Flag). Dazu kommen Saisonlager (~6.900 € bis Q4) und nur Garten-naher Markenfit ohne Bundle zu NG0001/NG0002. Kippen kann das nur ein belegter EK ≤ 6 € (DB1 ~33 %); bis dahin wäre Beobachten die Alternative zum Stop.
**Offene Punkte / Datenlücken:** Alibaba-Angebot (EK, MOQ); FBA-Gebühr exakt nach Rate Card 07/2026; Q4-BSR; Google Trends; DPMA/EUIPO.
**Nächster Schritt bei Go:** /deep-dive vogelfuttersaeule-edelstahl
**Deine Entscheidung (Go / Stop / Beobachten / Nacharbeit):** _wartet_
---
