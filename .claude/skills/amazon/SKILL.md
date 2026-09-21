---
name: amazon
description: Amazon.de-Daten für Ideen, Voranalyse und Deep-Dive – Suchseiten, Produktseiten (BSR, Preis, Sterne, Bewertungen, erhältlich seit), Rezensionen, Bestseller-Listen und Autocomplete per Playwright. Aufruf /amazon <befehl> … oder direkt node scripts/amazon.mjs. Rohdaten nach data/raw/amazon/, Werte mit Quelle „Amazon.de, <Datum>".
---

# /amazon <befehl> …

Liest amazon.de mit einem eigenen Chromium (Playwright) und gibt die Werte fertig zitiert für die Stufen-Dateien aus. Ersetzt in `rules/quellen.md` Quelle Nr. 1 („Amazon.de direkt"). Snippets (Nr. 2) bleiben Fallback.

## Befehle

| Aufruf | Liefert | Für |
|---|---|---|
| `node scripts/amazon.mjs suche "<keyword>" [--seiten N] [--node <id>]` | je Karte ASIN, Titel, Preis, Listenpreis, Sterne, Bewertungen, Badges (Amazon's Choice, Bestseller), gesponsert, „X Mal gekauft"; Preisband, Median, Bewertungsspanne | Ideen Nr. 5; Voranalyse Nr. 10, 12, 15, 24; Deep-Dive Wettbewerberwahl |
| `node scripts/amazon.mjs produkt <ASIN> [<ASIN> …]` | Preis, Sterne, Bewertungen, **BSR Haupt-/Unterkategorie**, erhältlich seit, Verkäufer/FBA, Varianten, Bilderzahl, A+, Maße/Gewicht, „X Mal gekauft", Kategoriepfad, Bullets, bis zu 10 Rezensionen der Produktseite | Voranalyse Nr. 1, 2, 9–16, 19, 20; Deep-Dive Abschnitt A–C |
| `node scripts/amazon.mjs rezensionen <ASIN> [--kritisch] [--max N]` | Datum, Sterne, Titel, Text (gekürzt), Variante, verifiziert | Deep-Dive Abschnitt D (bis zu 7 kritische je Wettbewerber), D2 Mining |
| `node scripts/amazon.mjs bestseller <node-id> [--seiten 2]` | Rang, ASIN, Titel, Preis, Sterne, Bewertungen | Voranalyse Nr. 9, 12, 18; Ideen |
| `node scripts/amazon.mjs autocomplete "<prefix>"` | Amazon-Suchvorschläge | Voranalyse Nr. 23 Keywords; Ideen Suchraster |

Optionen: `--json` (Rohobjekt), `--frisch` (Tages-Cache ignorieren), `--cdp http://localhost:9222` (lokalen Chrome mit offenem Amazon-Tab nutzen), `--sichtbar` (Browser sichtbar, nur lokal). `--selbsttest` prüft die Parser ohne Netz.

Exit-Codes: `0` ok · `1` Bedienfehler · `2` Captcha/Sperre · `3` Egress gesperrt (Allowlist fehlt) · `4` Playwright fehlt.

## Regeln
1. Vor dem ersten Aufruf einer Analyse `rules/quellen.md` lesen. Reihenfolge je Analyse: `autocomplete` → `suche` Seite 1–2 je Hauptkeyword → `produkt` für Referenz-ASIN und Top-Listings → `rezensionen --kritisch --max 7` je Wettbewerber (Deep-Dive) → `bestseller` für den Kategorie-Node.
2. Jeder Aufruf schreibt `data/raw/amazon/<YYYY-MM-DD>/<befehl>-<key>.json` (gitignored) und liest am selben Tag aus dieser Datei. Nicht mehr Seiten abrufen als die Analyse braucht; seriell, nie parallel.
3. Werte 1:1 übernehmen und mit `(Amazon.de, <Datum>)` zitieren – die Markdown-Ausgabe hat das Format schon. Nicht gefundene Felder sind `[fehlt]`. Absatz/Umsatz nie aus dem Skript, sondern als `~Wert (Schätzung aus BSR …)` nach `rules/quellen.md`.
4. Exit 2 oder 3 → sofort auf Quellen 2–5 aus `rules/quellen.md` wechseln, nichts raten, und im Lauf-Protokoll bzw. im Kopfblock der Stufen-Datei vermerken: `quellen_eingeschraenkt: [amazon.de Captcha]` oder `[amazon.de Egress gesperrt]`.
5. Nur lesen: kein Login, kein Warenkorb, keine Massenläufe über das Analyseziel hinaus. Rezensionen ohne Rezensentennamen speichern.

## Einrichtung

**Cloud-Session (claude.ai/code):** Umgebung bearbeiten → Network access **Custom** → „Also include default list of common package managers" anhaken → Allowed domains:
```
www.amazon.de
*.amazon.de
*.media-amazon.com
*.ssl-images-amazon.com
completion.amazon.de
```
Optional für Quellen Nr. 3/4/6: `www.idealo.de`, `*.alibaba.com`, `www.ebay.de`, `www.otto.de`. Wirkt ab der nächsten Session. Playwright und Chromium sind im Cloud-Image vorhanden.

**Lokal (Desktop-App/CLI):** `npm i -g playwright && npx playwright install chromium`. Mit eigenem Browser statt headless: Chrome mit `--remote-debugging-port=9222` starten und `--cdp http://localhost:9222` anhängen – dann laufen die Abrufe über die eigene IP und Cookies, ohne Allowlist und praktisch ohne Captcha.

## Bekannte Grenzen
- Keyword-Suche liefert maximal 7 Seiten; mit `--node` (Kategorie) mehr.
- Rezensionsseiten (`/product-reviews/`) verlangen teils Login; dann fällt das Skript auf die bis zu 10 Rezensionen der Produktseite zurück und kennzeichnet das in der Ausgabe.
- Preise und Lieferhinweise hängen vom Standort-Cookie der Session ab (Cloud-VM ohne DE-Adresse); Preis in EUR ist trotzdem der Listingpreis.
- Rechenzentrums-IPs erhalten häufiger ein Captcha. Das Skript wiederholt einmal nach 10 s, dann Exit 2.
- Amazon ändert das DOM; brechen Felder auf `null` weg, Selektoren in `scripts/amazon.mjs` (Blöcke `EXTRACT_*`) nachziehen und `--selbsttest` erweitern.
- Automatisierter Abruf ist von Amazons Nutzungsbedingungen nicht gedeckt; das Skript bleibt deshalb bei Lesezugriff in Browser-Kadenz und ohne Konto.
