# Produktbriefing – Schema

Quellen: „Produktbriefing Quick Check - Blumengießkanne" (NG0001, Google Doc `1pG_0GzwZAn5rUzh4PpJwtcO6Ie6wHAmFk88fEmhMzdk`) und „Produktbriefing Quick-Check- Vorlage" (Doc `12E59pEdKTZW20VZlMONl-JVsXpSQJ5nM6VXUGXFd_B4`, inhaltlich das Beispiel Gartenabfallsack). Ein Briefing zu NG0002 (Bewässerungskugeln) existiert weder in Drive noch in Notion (Notion-Projektseite NG0002 ist leer, Stand 2026-09-16). Die Struktur folgt daher dem NG0001-Briefing 1:1; NG0002 dient nur als Referenz für den Ablauf danach (Golden Sample, Labortests, Prüfplan, Verpackung, Margenkalkulator).

Ausgabe: `pipeline/<slug>/03-briefing.md`. Zwei Teile: **Teil A (deutsch)** ist die Entscheidungsvorlage für Pafri, **Teil B (englisch)** die Spezifikation, die Pafri an Sourcing/Hersteller weitergibt. Teil B [neu] übersetzt und erweitert die Vorlagenfelder um das, was eine Herstelleranfrage braucht.

## Teil A – Entscheidung (deutsch)

Reihenfolge und Feldnamen der Vorlage:

1. **Titel**: „Produktbriefing <Produktname>"
2. **Beispiel ASIN**: ASIN + Link
3. **Bild**: Link zum Referenzbild (kein Upload)
4. **Material**: Wunschmaterial, zulässige Alternativen, Ausschlüsse (Beispiel NG0001: „Vorzugsweise Edelstahl - rostfrei; alternatives Material denkbar wenn ähnliche Qualität")
5. **Max. Versandkarton Abmaße** (NG0001) bzw. **Größe (Produkteinheit)** (Vorlage)
6. **Farbe**: Pflichtfarben, optionale Farben
7. **Varianten**: Größe/Volumen/Set, Bandbreite
8. **Verpackung**: Art, Branding, offene Frage nach Standardverpackung
9. **zusätzliche Eigenschaften**: Bulletliste (Funktion, Robustheit, Design, Griff, Zubehör)
10. **Ziel-EK**: € je Stück
11. **Ziel MOQ**: Stück
12. **voraussichtliche Jahresmenge**: Stück
13. **Weitere Punkte zur Klärung** (Originalliste):
    - erforderliche Prüfungen? zu erwartende Prüfkosten
    - Kennzeichnungspflichten
    - Konformität EU Markt
    - Größe, Anzahl Artikel und Maße eines Masterkartons
    - Gewicht je Artikel
    - Verpackungsgröße (je Artikel, Einzelartikel und Set)

### A.14 Entscheidungsgrundlage [neu]

Kurzblock, damit Pafri am Gate 3 nicht in den Deep-Dive zurück muss:
- Ziel-VK auf Amazon.de und Zielmarge (Formel: VK − Amazon-Gebühren ~15 % − FBA − PPC ~10 % − EK − Fracht/Zoll; alle Annahmen benennen)
- Erwarteter Absatz/Monat (Schätzung, Quelle)
- Top-3 USPs aus Deep-Dive Abschnitt G
- Top-3 Risiken aus Deep-Dive Abschnitt I
- Scores und `score_gesamt` (unverändert aus Deep-Dive)
- Vorschlag NG-Nummer (nächste freie, siehe `DASHBOARD.md`)

## Teil B – Product Specification for Sourcing (English) [neu]

Alle Angaben aus Teil A und Deep-Dive Abschnitt K, auf Englisch, so formuliert, dass Pafri den Block unverändert in eine Herstelleranfrage kopieren kann. Slogan-Regel: „Designed in Germany", never „Made in Germany".

1. **Product name / working title**
2. **Reference product**: ASIN, link, what to match and what to change
3. **Material & finish**: grade (e.g. stainless steel 304 / 430), thickness, surface, coating, rust-free requirement, excluded materials
4. **Dimensions & capacity**: product unit, tolerances, max. shipping carton
5. **Weight**: target product weight, max. shipping weight
6. **Colours / variants**: mandatory, optional, quantity split
7. **Functional requirements**: bullet list (from A.9), each testable
8. **Components & accessories**: handle material, nozzle, inserts, included extras
9. **Packaging**: type, branding (logo files supplied by Pafri), inlay, unit + master carton, labelling (EAN, made-in origin label as legally required)
10. **Compliance & testing**: required certificates for EU market (e.g. REACH, LFGB where food/plant-water contact, packaging ordinance/LUCID), test reports requested from supplier, tests Pafri will commission
11. **Quality requirements**: acceptable defect rate, golden sample process, pre-shipment inspection
12. **Commercial**: target unit price (EXW/FOB), MOQ, expected annual quantity, sample request, lead time, payment terms as question
13. **Questions to supplier**: list (from A.13 translated + supplier-specific)

## Abschluss

Gate-Block aus `rules/prozess.md`. Bei Go: Pafri vergibt die NG-Nummer, Skill trägt `ng_nummer` ein und verschiebt den Ordner nach `products/NG00xx/`.

## Hinweise

- Keine Preise erfinden: Ziel-EK aus Alibaba-Spannen des Deep-Dive (Abschnitt L) ableiten, Richtwert der Voranalyse: EK ≈ 20 % vom VK des Vergleichsprodukts.
- Kein Versand, keine Anfrage. Das Briefing ist die Übergabe an Pafri (Regel 9).
