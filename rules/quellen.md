# Recherche-Quellen und Einschränkungen

## Reihenfolge
1. **Amazon.de direkt über `/amazon`** (`node scripts/amazon.mjs`: `suche`, `produkt` mit BSR, `rezensionen`, `bestseller`, `autocomplete`; Regeln in `.claude/skills/amazon/SKILL.md`). Schlägt das Skript fehl (Exit 2 Captcha, Exit 3 Egress gesperrt) → Punkt 2–5, Einschränkung im Lauf-Protokoll bzw. Kopfblock der Stufen-Datei unter `quellen_eingeschraenkt` vermerken.
2. **Suchmaschinen-Snippets** (WebSearch) mit `site:amazon.de <Keyword>`: Titel, Preis, Bewertungsanzahl, teils BSR.
3. **Preisvergleiche und Händler**: idealo, Google Shopping, OBI, Hornbach, Dehner, Bauhaus, Manufactum, Etsy (nur für Trend/Preis).
4. **Wettbewerber-Shops** (Netrox, Relaxdays, Gardena, Lechuza, Blumat u. a.) für Spezifikationen und Preise.
5. **Trend**: Google Trends (Keyword-Saisonalität), Pinterest/TikTok nur qualitativ.
6. **Sourcing**: Alibaba/1688 nur lesend (Preisspanne, MOQ, Anbieterzahl, Lead Time).
7. **Nachfrage-Signale ohne Helium 10**: Anzahl Suchergebnisse, „Über X Mal gekauft im letzten Monat" bei Top-Listings, Bestseller-Präsenz, Amazon-Autocomplete für Keywords, Google Trends DE.
8. **Marken / IP**: DPMA- und EUIPO-Register (Marken), Google Patents und DPMAregister (Design, Gebrauchsmuster).
9. **Compliance**: Produktsicherheitsverordnung (GPSR), Verpackungsgesetz/LUCID, PPWR-Übergangsfristen.
10. **Kosten**: Amazon-FBA-Gebührentabelle DE (Versand nach Größenklasse, Verkaufsgebühr 15 % Garten), Seefracht-Richtwerte China–DE, Zollsätze (TARIC). Rechenweg in `rules/kalkulation.md`.

## Nicht verfügbar
Helium 10, Junglescout, Keepa. Alle BSR-, Absatz-, Umsatz- und Suchvolumenangaben sind Schätzungen und werden so beschriftet.

## Schätzregel BSR → Absatz (nur Anhaltspunkt, Kategorie Garten Amazon.de)
Grobe Faustwerte aus Pafris Voranalyse Bewässerungskugeln (BSR ~3.000 Garten ≈ 200 St./Monat, Dez 2025) und Tiefenanalyse (BSR 445 ≈ 700 St./Monat, BSR 858 ≈ 500 St./Monat). Immer als `~` und „Schätzung aus BSR" markieren, nie als Messwert.

## Zitierformat
`Wert (Quelle, YYYY-MM-DD)` oder `~Wert (Schätzung aus …, YYYY-MM-DD)`. Links im Abschnitt „Quellen" der Datei.
