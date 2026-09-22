---
name: ideenlauf
description: Stufe 0 als kompletter Marktlücken-Lauf – 10–15 neue nicegarden-Produktideen mit Muss-/Soll-/Ausschluss-Prüfung, Note A–D, Amazon.de-Belegen (Preise, Bewertungen, BSR) und mindestens zwei Quellen je Idee. Aufruf /ideenlauf [<Suchfeld>] [Anzahl]. Erweitert /ideen um das feste Kriterienraster, die Batch-Abfrage über /amazon und den vierteiligen Ergebnisbericht im Chat.
---

# /ideenlauf [<Suchfeld>] [Anzahl, Standard 12]

Vorlage: Pafris Scout-Auftrag vom 2026-09-22 („Produktscout für nicegarden“). Ohne Suchfeld gilt das ganze Sortimentsfeld Garten · Balkon · Pflanzen · Innenraumbegrünung, Edelstahl/Premium-Design, VK 15–40 €. `/ideen` bleibt der leichte Lauf für ein einzelnes Thema; `/ideenlauf` ist der breite Lauf mit Notenvergabe und Bericht. Beide schreiben dieselben Dateien und enden mit der Freigabeliste – nie selbst `/voranalyse` starten.

## 0. Vorbereitung
1. `DASHBOARD.md`, `rules/prozess.md`, `rules/schema.md`, `rules/produktkriterien.md`, `rules/scoring.md`, `rules/quellen.md`, `.claude/skills/amazon/SKILL.md` lesen.
2. Bestand für Dedupe laden: alle Slugs und Titel aus `ideas/`, `pipeline/`, `products/`; Bestandsprodukte (NG-Nummern) sind ausgeschlossen.
3. Amazon-Erreichbarkeit prüfen: `node scripts/amazon.mjs autocomplete "pflanzen edelstahl"`. Exit 2/3 → Fallback-Quellen (`rules/quellen.md` Nr. 2–5) und `quellen_eingeschraenkt` im Protokoll.

## 1. Kriterienraster (fest, aus dem Auftrag)

**Muss (K.O. → Note D):** VK auf Amazon.de realistisch 15–40 € · passt zu Edelstahl/Premium-Design in Garten, Pflanzen, Balkon oder Innenraum · kein IP-Risiko (geschütztes Design, Markennähe, Patent) · keine Elektronik, kein Lebensmittelkontakt, kein Spielzeug · nicht schon im Sortiment (Gießkanne, Bewässerungskugel, weitere NG-Nummern).

**Soll (zählen, 0–6):** ganzjährige Nachfrage oder planbarer Peak (Q4-Geschenk = Plus) · FBA „Kleines Paket“ · ≤ 2 Materialien · Top-Listings mit Schwächen (< 4,3★, Plastik, generische Bilder) · Differenzierung über Material, Design oder Set · geschenktauglich.

**Ausschluss-Signale (→ Note D):** Preisband < 12 € dominiert · > 3 Listings mit > 5.000 Bewertungen ohne Lücke · Großmarke mit eigenem Design zum Premium-Preis (Gardena, Fiskars, Emsa, WMF, blomus …).

**Note:** A = alle Muss, ≥ 4 Soll, klare Lücke → Voranalyse dringend · B = alle Muss, 2–3 Soll, Lücke plausibel · C = Muss erfüllt, wenig Soll oder starker Wettbewerb → parken · D = Muss verletzt oder Ausschluss-Signal (Grund nennen). Die Note ist die Lane in `score:` (`rules/scoring.md` Abschnitt 4).

## 2. Kandidaten sammeln (Ziel: 20–25 Kandidaten für 10–15 Ideen)
- Brainstorm entlang der vier Kategorien (Bewässerung · Pflege & Werkzeug · Anzucht & Ranken · Gefäße & Deko) und der Zielgruppen (Balkon, Zimmerpflanzen, Naturgarten, Geschenk).
- Keine Varianten derselben Kategorie als getrennte Ideen (Untersetzer/Tablett, Futtersäule/Knödelhalter → eine Idee plus Hinweis oder D-Zeile mit Grund).
- Bestand abgleichen: gleicher Produkttyp in anderer Größe → Dedupe (Abschnitt 5).

## 3. Belege ziehen (Reihenfolge fest)
1. **Amazon.de Batch** – `scripts/amazon_batch.sh <ausgabeordner> "<keyword 1>" "<keyword 2>" …` ruft `suche` seriell auf (nie parallel, Amazon-Kadenz). Ein Keyword je Kandidat, Seite 1 reicht. Danach `autocomplete` für jedes Hauptkeyword (Nachfrage-Signal, Synonyme).
2. **Produktseiten** – je A/B-Kandidat 2–3 ASINs (Marktführer, Edelstahl-Referenz, schwächstes Top-Listing): `scripts/amazon_batch.sh <ordner> --produkt B0… B0…` liefert BSR, Gewicht, „erhältlich seit“, Rezensionen. BSR → Absatz nach `rules/quellen.md`, immer `~` und mit Hinweis auf Nebensaison, wenn der Abruf außerhalb des Peaks liegt.
3. **Zweitquellen** (WebSearch, mindestens drei Gruppen abdecken): Premium-/Designmarken (blomus, Esschert, Burgon & Ball/Sophie Conran, Bujnie, Manufactum, thegardenshop.de, bloomling.de) · Trend/Design (spoga+gafa, Plantura/KANN Gartentrends, Etsy Garden Gifts, Pinterest, TikTok #balkongarten) · Test-/Vergleichsportale (vergleich.org, testbericht.de, garten.schule) nur als Nachfrage-Indikator · Vorlauf amazon.co.uk/.com. idealo/geizhals sind im Cloud-Egress meist gesperrt → vermerken.
4. Jede Zahl mit `(Quelle, YYYY-MM-DD)`; EK ohne Alibaba als „~x € (Faustregel 20 % VK, Alibaba gesperrt)“; IP-Prüfung (DPMA/EUIPO) als offenen Punkt führen, wenn Egress gesperrt.

## 4. Bewerten
Je Kandidat in dieser Reihenfolge: Muss → Ausschluss-Signale → Soll zählen → Note. Belege für die Note in einem Satz („6/6 Soll, Top-Listings 3,8–4,3★, kein Listing > 5.000 Bew.“). Bei A zusätzlich die Lücke in einem Satz benennen; wenn die Lücke nur über Design und nicht über Qualität geht (Bestandslistings ≥ 4,5★), höchstens B.

## 5. Dedupe
Gleicher Slug, Synonym, gleicher Produkttyp in anderer Größe → nicht neu anlegen. Bestehende Datei um Abschnitt `## Ergänzung aus Lauf <datum> (Dedupe: <Kandidat>)` mit den neuen Amazon-Zahlen ergänzen und im Protokoll unter „Dedupe“ führen. Verwandte, aber andere Produkttypen (Tränke ≠ Futtersäule, Band ≠ Kragen) dürfen neu angelegt werden – Querverweis in „Warum nicegarden“.

## 6. Schreiben
1. Je Idee `ideas/<slug>.md` nach `templates/ideensteckbrief.md` mit `status: idee`, `quelle: ideen-lauf`, `lauf: <datum>-<thema-slug>`, `score: <A–D>`. Zusätzlich zwischen „Markt-Ersteindruck“ und „SWOT“: bei A/B `## Marktlücke, Differenzierung, Risiken` (5–8 Sätze, ≥ 2 URLs, davon eine Amazon.de-Listing-URL), bei D `## Ausschluss-Signal (Lane D)` (Grund mit Zahlen). D-Ideen werden angelegt, damit die Ablehnung dokumentiert ist; `status` bleibt `idee`, nur Pafri lehnt ab.
2. Zahlen aus den `/amazon`-Ausgaben 1:1 (Preis, Sterne, Bewertungen, BSR, „X Mal gekauft“); Referenz-ASINs mit `https://www.amazon.de/dp/<ASIN>`.
3. `ideas/_laeufe/<datum>-<thema-slug>.md` nach `templates/lauf-protokoll.md`, ergänzt um „Auftrag“ (Kriterienraster), „Top 3“ und die Ergebnistabelle mit Note je Idee.
4. `python scripts/dashboard.py`, dann `dashboard.html` unter https://claude.ai/artifact/2rvyEyRe1p9ietKExeRiiT neu veröffentlichen (gleiche URL, nie `capabilities` übergeben).
5. Ein Commit: `feat(ideen): lauf <datum> <thema-slug>`, Push auf den Arbeitsbranch.

## 7. Bericht im Chat (vierteilig, deutsch, Markdown)
1. Tabelle aller Ideen: Produktidee | Note | Preisband min/Median/max | relevante Listings (Seite 1 / gesamt) | Bewertungen Top 3 (Anzahl · Sterne) | erfüllte Soll (x/6) | Ausschluss-Signal ja/nein. Darunter die Dedupe-Zeilen.
2. Je A/B-Idee 5–8 Sätze: Lücke, Differenzierung nicegarden, größte Risiken, ≥ 2 Quell-URLs.
3. Je D-Idee ein Satz mit Grund.
4. Top 3 in Reihenfolge mit Begründung, Liste aller genutzten Quellen, Hinweis auf Freigabeliste im Protokoll und Einschränkungen (gesperrte Quellen, Nebensaison-BSR).

## 8. Abschluss
Freigabeliste im Protokoll (`- [ ] <slug> – Note – Empfehlung`) ersetzt den Gate-Block. Warten auf Pafri (Chat oder Dashboard-Klick via `/entscheidungen`). Bei Freigabe: `status: freigegeben`, `status_datum`, Dashboard, Commit `gate(<slug>): freigabe voranalyse`.

## Erfahrungswerte aus dem Lauf 2026-09-22
- 23 Suchseiten + 12 Autocomplete + 18 Produktseiten seriell dauern ~35 Minuten; Batches im Hintergrund starten und währenddessen die Zweitquellen ziehen.
- Produktseiten liefern „erhältlich seit“ und Gewicht nur bei einem Teil der ASINs – als `[fehlt]` führen, nicht schätzen.
- Typische D-Gründe im Edelstahl-Umfeld: Preisband < 12 € (Regenmesser, Knödelhalter, Blumenfrosch, Gießaufsatz), Markendominanz (Unkrautstecher, Zwiebelpflanzer), Lebensmittelkontakt (Kräutertrockner).
- Saisonprodukte (Vogelfütterung, Bienentränke, Balkonhalter) im September mit BSR 7.000–70.000 bewerten → Absatzschätzung konservativ, Peak-BSR als offenen Punkt notieren.
