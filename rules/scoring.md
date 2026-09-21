# Scoring-Modell

Stand 2026-09-21. Gilt für `/voranalyse` (Erstvergabe) und `/deep-dive` (Aktualisierung mit belegten Zahlen). Abgeleitet aus Pafris Detaildokument „Voranalyse und Tiefenanalyse" (`vorlagen/detaildokument-analysen.md`, Abschnitt 1.4). Das ältere Notion-Modell (4 Kriterien 1–10, `vorlagen/scoring-notion.md`) ist damit abgelöst; seine Anker für Marge, Markt, USP und Risiko sind unten in die sechs Kriterien eingeflossen. Schema ändern nur nach Rücksprache mit Pafri.

## 1. Sechs Kriterien, Teilnote 0–10, gewichtet

| # | Kriterium | Frontmatter-Key | Gewicht | schwach 0–3 | mittel 4–6 | stark 7–10 |
|---|---|---|---|---|---|---|
| 1 | Marge & DB-Potenzial | `marge` | 25 % | DB1 < 25 % | DB1 25–35 % | DB1 > 35 %, Break-even-ACOS mit Puffer zum CPC-Niveau |
| 2 | Nachfrage | `nachfrage` | 20 % | schwaches Signal, fallend | stabil, mittel | stark, wachsend, ganzjährig |
| 3 | Wettbewerb (invers) | `wettbewerb` | 20 % | Top 10 dominiert, > 1.000 Bewertungen durchgängig | gemischt | mehrere angreifbare Listings |
| 4 | Logistik & FBA-Fit | `logistik` | 10 % | sperrig / zerbrechlich / > 2 kg | Standard | klein, leicht, robust, „Kleines Paket" |
| 5 | Markenfit & Synergien | `markenfit` | 10 % | kein Garten-Bezug | Garten-nah, Insel | Kernsortiment + Cross-Selling zu NG0001/NG0002 |
| 6 | Risikoprofil (invers) | `risiko` | 15 % | konkretes IP-/Compliance-Risiko | prüfbar, lösbar | unauffällig |

Jede Teilnote trägt genau einen Begründungssatz mit Zahl oder Grund. DB1, Break-even-ACOS und CPC-Niveau kommen aus `rules/kalkulation.md`.

## 2. Gesamtscore und Zonen

```
score_gesamt = Σ (Teilnote × Gewicht) × 10        → 0–100, ganzzahlig gerundet
```

| Zone | `score_gesamt` | Bedeutung |
|---|---|---|
| **Go** | ≥ 70 | Empfehlung Go |
| **Review** | 50–69 | Bedingt: die 1–2 Kriterien nennen, die das Bild kippen würden |
| **Reject** | < 50 | Empfehlung Stop |

Kalibrierung: NG0001 (Edelstahl-Gießkanne) und NG0002 (Bewässerungskugeln) sollten rückgerechnet ~70–80 erreichen.

## 3. K.O.-Regeln

Ein K.O. setzt `score: D` und Zone Reject, unabhängig vom Gesamtscore. Der Skill listet den Verstoß in `ko_verstoss`.

| Nr. | Regel | Quelle |
|---|---|---|
| K0 | Teilnote ≤ 2 bei Kriterium 1 (Marge) oder 6 (Risiko) | Detaildokument 1.4 |
| K1 | Elektroprodukt (Prüf-, Zertifizierungs-, Registrierungspflicht) | Voranalyse Nr. 5 |
| K2 | Chemisches Produkt oder Lebensmittel mit erhöhten Prüfanforderungen (inkl. Düngemittelrecht) | Voranalyse Nr. 4, Miro „Rasendünger" |
| K3 | Erotik-/Erwachsenenprodukt (Werbebeschränkung) | Voranalyse Nr. 6 |
| K4 | Größenabhängige Retouren (Kleidung, Handschuhe, Schuhe) | Voranalyse Nr. 7, Miro „Gartenhandschuhe" |
| K5 | Versandgewicht > 2 kg oder Übergrößenzuschlag bei FBA ohne Premium-Preisspielraum | Voranalyse Nr. 1–2, Miro „Schlauchwagen", „Rankgitter" |
| K6 | Zielpreis auf Amazon.de dauerhaft < 10 € | Voranalyse Nr. 10 |
| K7 | Kein Markenfit: nicht Garten/Pflanzenpflege, nicht als Edelstahl/Premium positionierbar | `rules/produktkriterien.md` |

Red Flags, die auch bei Score ≥ 50 zur Stop-Empfehlung führen: dominanter IP-Inhaber in der Nische, Break-even-ACOS unter dem geschätzten CPC-Niveau.

## 4. Zuordnung Gesamtscore → Lane A–D

Miro und `/ideen` arbeiten mit Lanes, das Dashboard zeigt sie. Ab `/voranalyse` wird die Lane aus dem Score abgeleitet:

| Lane | Bedeutung (Miro) | `score_gesamt` | Zone |
|---|---|---|---|
| A | Empfohlen | ≥ 70 | Go |
| B | Prüfen | 60–69 | Review |
| C | Beobachten | 50–59 | Review |
| D | Ablehnen | < 50 oder K.O. | Reject |

Importierte Miro-Karten behalten ihre Lane als `score`, `score_gesamt` bleibt `null`, bis `/voranalyse` die sechs Teilnoten vergibt.

## 5. Schwellen je Stufe

- `/ideen` vergibt nur eine Lane (A–D) als Vor-Score mit Begründung, keine Teilnoten.
- `/voranalyse` vergibt die sechs Teilnoten, `score_gesamt`, Zone, Lane. Empfehlung strikt nach Zone; Red Flags (Abschnitt 3) schlagen die Zone.
- `/deep-dive` aktualisiert die Teilnoten mit belegten Zahlen. Empfehlung Go nur, wenn zusätzlich DB1 ≥ 35 % im Ziel-Szenario, Break-even-ACOS über dem geschätzten CPC-Niveau und kein Risiko „hoch" ohne Gegenmaßnahme bleibt. Sonst Nacharbeit (mit Nennung der fehlenden Zahl) oder Stop.
- `/briefing` ändert keine Scores mehr.
