# Detaildokument – Voranalyse (Stufe 1) und Tiefenanalyse (Stufe 2)

Repo: `pafri-brain` · Prozess: `/ideen` → Gate 0 → **`/voranalyse`** → Gate 1 → **`/deep-dive`** → Gate 2 → `/briefing` → Gate 3
Scope (Stand Sep 2026): Amazon.de, Websuche statt Helium 10, Markdown im Repo, Stop/Go an jedem Gate.

Dieses Dokument beschreibt beide Analysen so, dass Claude Code sie reproduzierbar ausführt. Die zugehörigen Mustervorlagen liegen in `templates/01-voranalyse.md` und `templates/02-deep-dive.md`; die Kennzahlen beider Dateien werden von `scripts/dashboard.py` in `DASHBOARD.md` gezogen (Abschnitt 4).

Ablage im Repo:

| Datei | Zweck |
|---|---|
| `rules/voranalyse.md` | Abschnitt 1 dieses Dokuments (Prüfpunkte, Regeln) |
| `rules/deep-dive.md` | Abschnitt 2 dieses Dokuments (Wettbewerber-Schema, Regeln) |
| `templates/01-voranalyse.md` | Mustervorlage Stufe 1 – wird 1:1 nach `pipeline/<slug>/01-voranalyse.md` kopiert und befüllt |
| `templates/02-deep-dive.md` | Mustervorlage Stufe 2 – wird 1:1 nach `pipeline/<slug>/02-deep-dive.md` kopiert und befüllt |
| `scripts/dashboard.py` | erweitert um den Block „Analysen-Kennzahlen" |

Wenn Pafris Original-Vorlagen (22-Punkte-Checkliste, 4-Wettbewerber-Excel) in `vorlagen/` liegen, gilt: deren Prüfpunkte und Felder werden in die Abschnitte unten **eingehängt**, nicht ersetzt. Die Reihenfolge der Originale bleibt erhalten; Punkte, die hier zusätzlich stehen, werden als `[neu]` markiert.

---

## 0. Gemeinsame Regeln für beide Analysen

**Datenquellen (Websuche, kein Helium 10)**
- Amazon.de: Suchergebnisseiten, Top-Listings (Titel, Preis, Sterne, Anzahl Bewertungen, Varianten, Bildqualität, A+), Bestseller-Listen, Suchvorschläge (Autocomplete). Wenn WebFetch auf Amazon blockiert: Suchmaschinen-Snippets, idealo/geizhals, Händlerseiten, Wettbewerber-Shops.
- Marken/IP: DPMA- und EUIPO-Register (Marken), Google Patents / DPMAregister (Design, Gebrauchsmuster).
- Compliance: Produktsicherheitsverordnung (GPSR), Verpackungsgesetz/LUCID, PPWR-Übergangsfristen.
- Kosten: Amazon-FBA-Gebührentabelle DE (Versand nach Größenklasse, Verkaufsgebühr 15 % in Garten), Frachtrichtwerte Seefracht China–DE, Zollsätze (TARIC).

**Kennzeichnung von Zahlen (Pflicht)**
- Beobachtet: `Wert (Quelle, abgerufen JJJJ-MM-TT)`
- Geschätzt: `~Wert (Schätzung: Grundlage)` – gilt immer für BSR, Absatz, Suchvolumen, CPC, EK.
- Nicht ermittelbar: `[offen – Daten fehlen]` – der Prüfpunkt bleibt in der Datei stehen, wird nie gelöscht.

**Kalkulationslogik (einheitlich in beiden Stufen)**
```
Netto-VK        = Brutto-VK / 1,19
Verkaufsgebühr  = Brutto-VK × 15 %
FBA-Versand     = laut Größenklasse (Kleines Paket / Standard / Groß)
Landed Cost     = EK + Fracht + Zoll + Einfuhrnebenkosten (je Stück)
DB1 (€)         = Netto-VK − Landed Cost − Verkaufsgebühr − FBA-Versand
DB1 (%)         = DB1 (€) / Netto-VK
DB2 (€)         = DB1 (€) − Lagerkosten − EPR/Verpackung − Retourenpauschale − Ads-Anteil
Break-even-ACOS = DB1 (€) / Brutto-VK          (Ziel: ≥ 35 %; NG0001-Referenz: 43,7 %)
Kapitalbedarf   = MOQ × Landed Cost + Erstausstattung (Fotos, Verpackungsdesign, Samples)
```
EK ohne Angebot: 30-%-Regel (EK ≈ 30 % vom Brutto-VK), immer als Schätzung markiert.

**Ton und Umfang**
- Deutsch, knapp, jede Aussage mit Zahl oder Grund. Keine „könnte funktionieren"-Formulierungen.
- Die Datei enthält die Details, der Chat nur das Gate (max. 10 Zeilen + Gate-Block).

---

## 1. Voranalyse (Stufe 1) – Kurzcheck mit Score

### 1.1 Zweck
In 1–2 Stunden Rechenzeit klären, ob eine freigegebene Idee eine Tiefenanalyse rechtfertigt. Ergebnis ist ein Score 0–100 mit Zone (Go / Review / Reject) und ein Fünf-Zeilen-Fazit. Die Voranalyse beantwortet vier Fragen: Gibt es Nachfrage? Ist der Wettbewerb angreifbar? Rechnet sich das im VK-Korridor 15–40 €? Gibt es ein K.O.?

### 1.2 Input und Voraussetzungen
- `ideas/<slug>.md` mit `status: freigegeben` (Gate 0 durch Pafri)
- `rules/produktkriterien.md`, `rules/scoring.md`, `rules/schema.md`
- Beim Start: `git mv ideas/<slug>.md pipeline/<slug>/00-idee.md`, Frontmatter `status: voranalyse`, `stufe: 1`

### 1.3 Prüfpunkte in Originalreihenfolge

**Block A – Produkt und Zielkunde**
1. Produktbeschreibung: Typ, Größe/Fassungsvermögen, Material, Ausführung (ein Absatz)
2. Zielkunde und Nutzungssituation: wer, wofür, welches Problem wird gelöst
3. Markenfit nicegarden: Edelstahl/Premium-Design, Garten/Balkon/Innenraum; Cross-Selling zu NG0001/NG0002

**Block B – Markt und Nachfrage**
4. Hauptkeyword und 3–5 Nebenkeywords (aus Amazon-Suchvorschlägen und Listing-Titeln)
5. Nachfrage-Signal: Anzahl Ergebnisse, Bestseller-Präsenz, „Über X Mal gekauft im letzten Monat"-Angaben der Top-Listings (Amazon.de zeigt das bei vielen Produkten), Google-Trends-Verlauf DE
6. Saisonalität: ganzjährig / Frühjahr–Sommer / Q4-Geschenk – mit Begründung
7. Grobe Marktgröße Amazon.de als Bandbreite (~Schätzung: Top-10-Absatz × Ø Preis)

**Block C – Wettbewerb**
8. Top 5–10 Listings in Tabelle: Marke, Preis, Sterne, Bewertungen, Material, Variantenanzahl, Bildqualität (1–3), sichtbare Schwäche
9. Wettbewerbsstruktur: Anteil chinesischer Direktanbieter, große Marken (Gardena, Fiskars, Emsa …), Private-Label-Dichte
10. Die zwei angreifbarsten Listings mit Begründung (Bewertung < 4,3, Plastik, generische Bilder, Preislücke, fehlende Varianten)
11. Markteintritts-Realismus: wie viele Bewertungen braucht ein neues Listing für Seite 1 (Bandbreite), realistischer Zeithorizont, geschätztes CPC-Niveau (~Schätzung aus Nischenvergleich)

**Block D – Grobe Kalkulation**
12. VK-Korridor (aus Top-Listings) und Ziel-VK nicegarden (Premium-Position begründen)
13. EK-Annahme (30-%-Regel oder Alibaba-Richtpreis), Fracht/Zoll pauschal, FBA-Größenklasse aus typischen Maßen
14. DB1 in € und %, Break-even-ACOS – Vergleich mit geschätztem CPC-Niveau
15. Erster Kapitalbedarf-Check: typische MOQ × Landed Cost

**Block E – Differenzierung und Risiken**
16. 3–5 Differenzierungshypothesen, jede aus einer beobachteten Wettbewerber-Schwäche abgeleitet
17. IP-Schnellcheck: DPMA/EUIPO nach Marken, Google Patents nach Design – Ergebnis „unauffällig / prüfen / hoch"
18. Material und Compliance-Vorprüfung: Anzahl Materialien (max. 2), GPSR-Kennzeichnung, Lebensmittelkontakt/Elektronik ausgeschlossen?
19. Logistik: Maße, Gewicht, Bruchrisiko, FBA-Klasse „Kleines Paket" erreichbar?
20. Weitere Risiken: Saisonalität, chinesische Direktanbieter, Kategorie-Beschränkungen

**Block F – Bewertung**
21. Score nach `rules/scoring.md`: sechs Kriterien, Teilnote 0–10 mit je einem Begründungssatz, K.O.-Regeln, Gesamtscore, Zone
22. Fazit in fünf Zeilen + offene Fragen für die Tiefenanalyse

### 1.4 Scoring (Kurzfassung aus `rules/scoring.md`)

| # | Kriterium | Gewicht | schwach 0–3 | mittel 4–6 | stark 7–10 |
|---|---|---|---|---|---|
| 1 | Marge & DB-Potenzial | 25 % | DB1 < 25 % | 25–35 % | > 35 %, Break-even-ACOS mit Puffer zum CPC-Niveau |
| 2 | Nachfrage | 20 % | schwaches Signal, fallend | stabil, mittel | stark, wachsend, ganzjährig |
| 3 | Wettbewerb (invers) | 20 % | Top 10 dominiert, > 1.000 Bewertungen durchgängig | gemischt | mehrere angreifbare Listings |
| 4 | Logistik & FBA-Fit | 10 % | sperrig/zerbrechlich | Standard | klein, leicht, robust, Kleines Paket |
| 5 | Markenfit & Synergien | 10 % | kein Garten-Bezug | Garten-nah, Insel | Kernsortiment + Cross-Selling |
| 6 | Risikoprofil (invers) | 15 % | konkretes IP-/Compliance-Risiko | prüfbar, lösbar | unauffällig |

Score = Σ (Teilnote × Gewicht) × 10. **K.O.:** Teilnote ≤ 2 bei Kriterium 1 oder 6 → Reject. Zonen: **Go ≥ 70 · Review 50–69 · Reject < 50.** Kalibrierung: NG0001/NG0002 sollten ~70–80 erreichen.

### 1.5 Output
- Datei `pipeline/<slug>/01-voranalyse.md` nach `templates/01-voranalyse.md` – alle 22 Prüfpunkte, nichts weglassen
- Frontmatter der Analyse-Datei trägt die Dashboard-Felder (Abschnitt 4)
- `00-idee.md`: `score`, `naechster_schritt: Gate 1`, `aktualisiert`
- `python scripts/dashboard.py`, Commit `feat(<slug>): voranalyse`

### 1.6 Gate 1
Gate-Block aus `rules/prozess.md`. Empfehlung strikt nach Zone. Bei Review: die 1–2 Kriterien nennen, die das Bild kippen würden. Bei Red Flags (K.O., dominanter IP-Inhaber, Break-even-ACOS unter CPC-Niveau) Stop empfehlen, auch wenn der Score rechnerisch über 50 liegt.

---

## 2. Tiefenanalyse (Stufe 2) – Entscheidungsbasis vor dem Briefing

### 2.1 Zweck
Aus einem Go-Kandidaten eine belastbare Entscheidungsgrundlage machen: Wettbewerb bis auf Rezensions-Ebene verstehen, Produktanforderungen aus Kundensicht ableiten, Kalkulation je Variante mit Sensitivität rechnen, Sourcing- und Compliance-Anforderungen so weit vorbereiten, dass das Briefing (Teil B, englisch) daraus geschrieben werden kann. Ergebnis: Go / No-Go mit den zwei größten Unsicherheiten.

### 2.2 Input und Voraussetzungen
- `pipeline/<slug>/01-voranalyse.md` vorhanden, Gate 1 = Go (`naechster_schritt: /deep-dive`)
- `rules/deep-dive.md`, `rules/produktkriterien.md`, `00-idee.md`, `01-voranalyse.md` lesen
- Frontmatter `00-idee.md`: `status: deep-dive`, `stufe: 2`
- Zahlen aus der Voranalyse werden übernommen und nur mit Begründung geändert (Änderung in Abschnitt 1 der Datei ausweisen)

### 2.3 Abschnitte in Originalreihenfolge

**1. Executive Summary** – Empfehlung in einem Satz + fünf Kernzahlen (Ziel-VK, Landed Cost, DB1 %, Break-even-ACOS, Kapitalbedarf Charge 1) + Abweichungen zur Voranalyse.

**2. Produktspezifikation** – Varianten (Größen/Farben, Empfehlung: Start mit max. 2), Material und Oberfläche (Edelstahl-Güte 304/430, Finish), Maße und Gewicht je Variante, Verpackung (Retail-Box, Innenpolster, FBA-Größenklasse, EPR-Materialfraktionen), Zubehör/Set-Inhalt.

**3. Wettbewerber-Deep-Dive (4-Wettbewerber-Schema)** – Auswahl: drei Top-Listings nach Bewertungsanzahl + ein Premium-/Design-Anbieter. Je Wettbewerber dieselben Felder:
Marke/Listing · ASIN (falls sichtbar) · Preis und Preishistorie (idealo) · Sterne · Bewertungen · geschätzter Monatsabsatz (~) · Varianten · Material · Maße/Gewicht · Bildanzahl und -qualität · A+/Video · Titel-Keywords · Verkäufertyp (Amazon, FBA-Händler, China-Direkt) · Stärken (3) · Schwächen (3).

**4. Rezensions-Mining → Produktanforderungen** – Je Wettbewerber: wiederkehrende Kritikpunkte aus 1–3-Sterne-Rezensionen und Lobpunkte aus 5-Sterne-Rezensionen (öffentlich lesbar, mit Häufigkeitsangabe „x von y gelesenen"). Daraus die Tabelle **„Produktanforderungen aus Kundensicht"**: Anforderung · Herkunft (welche Kritik) · Priorität Muss/Soll · Konsequenz für Spezifikation. Das ist die wichtigste Eingabe fürs Briefing.

**5. Positionierung & Differenzierung** – Preis-/Qualitäts-Karte (Wettbewerber und nicegarden-Zielposition), drei USPs mit Beleg aus Abschnitt 3–4, Listing-Ansatz (Titelstruktur, Bilder-Konzept, A+-Story), Ziel-VK mit Herleitung.

**6. Keywords** – Cluster aus Amazon-Autocomplete und Listing-Titeln: Haupt-Cluster, Long-Tail, Anwendungs- und Geschenk-Cluster. Ohne Volumen (kein Helium 10) – Volumen wird nach dem Briefing manuell ergänzt, Platzhalterspalte bleibt stehen.

**7. Marktgröße** – Bandbreite mit Herleitung (Top-10-Absatz ~ × Ø Preis), realistischer Marktanteil nach 6 und 12 Monaten, Absatzziel je Monat.

**8. Detailkalkulation je Variante** – EK (Richtpreis mit Quelle oder 30-%-Regel), Fracht und Zoll, Einfuhrnebenkosten, Landed Cost, Verkaufsgebühr, FBA-Versand, Lagerkosten, EPR/Verpackung, Retourenpauschale → DB1 und DB2 in € und %, Break-even-ACOS, Ziel-TACoS, Kapitalbedarf Charge 1.

**9. Sourcing-Anforderungen** – Lieferantentyp, MOQ-Erwartung, Sample-Prozess, Lead Time, Qualitätskriterien (NG0001-Learning: Rostbeständigkeit ist Muss, Prüfmethode benennen), Fragen an den Lieferanten. Vorbereitung für Briefing Teil B.

**10. Compliance** – GPSR (verantwortliche Person, Kennzeichnung), Verpackungsgesetz/LUCID, PPWR-Anforderungen an Verpackung, Materialdeklaration, Kategorie-Freigaben Amazon; PL/CZ nur als Hinweis (Scope Amazon.de).

**11. Launch-Skizze** – Ranking-Strategie (Learnings NG0001: Coupon-Push, TACoS-Steuerung, Ziel-BSR), Ads-Startbudget als Bandbreite, Zeitplan Sample → Order → Launch.

**12. Risiken & Mitigation** – Top 5 mit Eintrittswahrscheinlichkeit (niedrig/mittel/hoch), Auswirkung, konkreter Gegenmaßnahme.

**13. Sensitivitätsanalyse** – EK ± 15 %, CPC ± 30 %, VK-Szenarien (−10 % / Ziel / +10 %) → Wirkung auf DB1 % und Break-even-ACOS in einer Tabelle.

**14. Empfehlung** – Go für Briefing / Nachbessern / Stop mit Begründung; die zwei größten Unsicherheiten und wie sie geschlossen werden (z. B. Sample, H10-Export).

### 2.4 Output
- `pipeline/<slug>/02-deep-dive.md` nach `templates/02-deep-dive.md`, alle 14 Abschnitte
- Frontmatter mit Dashboard-Feldern (Abschnitt 4)
- `00-idee.md`: `naechster_schritt: Gate 2`, `aktualisiert`
- `python scripts/dashboard.py`, Commit `feat(<slug>): deep-dive`

### 2.5 Gate 2
Gate-Block aus `rules/prozess.md`. Go nur, wenn DB1 ≥ 35 % im Ziel-Szenario und Break-even-ACOS über dem geschätzten CPC-Niveau liegt und kein Risiko mit „hoch" ohne Gegenmaßnahme bleibt. Sonst Nachbessern (mit Nennung, welche Zahl fehlt) oder Stop.

---

## 3. Abgrenzung der beiden Analysen

| | Voranalyse | Tiefenanalyse |
|---|---|---|
| Frage | Lohnt sich der Aufwand? | Machen wir es – und wie genau? |
| Tiefe Wettbewerb | Top 5–10 als Tabelle, zwei angreifbare | 4 Wettbewerber vollständig + Rezensionen |
| Kalkulation | eine Variante, Pauschalen | je Variante, alle Kostenblöcke, Sensitivität |
| Kundensicht | Hypothesen aus sichtbaren Schwächen | belegte Anforderungen aus Rezensionen |
| Sourcing/Compliance | Vorprüfung ja/nein | Anforderungsliste fürs Briefing |
| Ergebnis | Score 0–100, Zone | Go/No-Go, zwei Unsicherheiten |
| Aufwand Claude Code | 15–30 Suchen | 40–80 Suchen, Rezensionen lesen |
| Gate | 1 – Go/Review/Stop | 2 – Go/Nachbessern/Stop |

---

## 4. Darstellung im Dashboard

`scripts/dashboard.py` liest zusätzlich das Frontmatter von `01-voranalyse.md` und `02-deep-dive.md` je Pipeline-Ordner und erzeugt den Block **„Analysen-Kennzahlen"**. Die Felder müssen flach im Frontmatter der Analyse-Datei stehen; das Template gibt sie vor.

**Frontmatter `01-voranalyse.md` (Dashboard-relevant)**

```yaml
slug:
stufe: 1
erstellt:
quellen_stand:
score:              # 0–100
zone:               # go / review / reject
vk_ziel:            # € brutto
ek_annahme:         # € je Stück, ~
db1_prozent:        # DB1 in % vom Netto-VK
break_even_acos:    # %
kapitalbedarf:      # € Charge 1, ~
ko:                 # nein / ja: <Kriterium>
empfehlung:         # Go / Review / Stop
```

**Frontmatter `02-deep-dive.md` (Dashboard-relevant)**

```yaml
slug:
stufe: 2
erstellt:
quellen_stand:
vk_ziel:
landed_cost:
db1_prozent:
db2_prozent:
break_even_acos:
moq:
kapitalbedarf:
varianten:          # Anzahl Start-Varianten
risiko_hoch:        # Anzahl Risiken mit „hoch"
empfehlung:         # Go / Nachbessern / Stop
unsicherheit_1:
unsicherheit_2:
```

**Mustervorlage des Dashboard-Blocks (Ausgabe in `DASHBOARD.md`)**

```
## Analysen-Kennzahlen

| Slug | Stufe | Score | Zone | VK-Ziel | DB1 % | BE-ACOS | Kapital Ch. 1 | Empfehlung | Stand |
|---|---|---|---|---|---|---|---|---|---|
| edelstahl-pflanzenspruehe-500ml | 2 | 74 | go | 24,90 € | 41 % | 39 % | ~6.800 € | Go | 2026-09-21 |
| giesskanne-3l-outdoor | 1 | 58 | review | 34,90 € | 31 % | 27 % | ~9.500 € | Review | 2026-09-19 |

Stufe 2 überschreibt VK/DB1/BE-ACOS/Kapital aus Stufe 1; Score und Zone bleiben aus Stufe 1.
Offen (Unsicherheiten aus Deep-Dive):
- edelstahl-pflanzenspruehe-500ml: Pumpmechanik Qualität (Sample) · CPC-Niveau (H10-Export)
```

Regeln:
- Die Kurzansicht zeigt nur diese Spalten. Wer mehr will, öffnet die Datei – der Pfad steht in der Tabelle „In Arbeit".
- Leere Felder erscheinen leer, nie mit Platzhaltertext. Ein leeres `score` in Stufe 1 ist ein Fehler.
- Werte werden mit Einheit geschrieben (`24,90 €`, `41 %`), damit die Tabelle ohne Nachbearbeitung lesbar ist.
- Der Block erscheint nur, wenn mindestens eine Analyse-Datei existiert.
