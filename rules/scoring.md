# Scoring-Modell

Abgeleitet aus zwei Quellen von Pafri (Stand 2026-09-16):
1. Notion „Template – Produktanalyse-Bewertung" (Company Brain → Wiki & SOPs), 4 Kriterien je 1–10, Empfehlungslogik nach Gesamt-Score.
2. Miro „Nicegarden Scout Longlist" (April 2026): Lanes A–D mit SWOT je Karte.

Ein eigenes Scoring-Dokument als Datei existiert nicht in Drive. Die Abschnitte „Gewichte", „K.O.-Regeln" und „Zuordnung A–D" sind Vorschläge und als **[neu]** markiert. Schema ändern nur nach Rücksprache mit Pafri.

## 1. Kriterien und Anker (Notion, 1:1)

### Marge Score (1–10)
- **9–10**: > 50 % Marge, klar profitabel auch mit Werbekosten
- **7–8**: 35–50 % Marge, gesund
- **5–6**: 20–35 % Marge, knapp
- **1–4**: < 20 % Marge, Vorsicht

### Markt Score (1–10)
- **9–10**: Wachsendes Segment, klare Nachfrage, niedrige Sättigung
- **7–8**: Stabiler Markt mit Potenzial
- **5–6**: Reifer Markt, kompetitiv
- **1–4**: Schrumpfender oder übersättigter Markt

### USP Score (1–10)
- **9–10**: Klares Differenzierungsmerkmal, schwer zu kopieren
- **7–8**: Mehrere Vorteile gegenüber Wettbewerb
- **5–6**: Leichte Vorteile, vergleichbar
- **1–4**: Me-too-Produkt

### Risiko Score (1–10, 10 = wenig Risiko)
- **9–10**: Stabile Lieferkette, keine regulatorischen Risiken, erprobte Kategorie
- **7–8**: Geringe Risiken, gut handhabbar
- **5–6**: Mittlere Risiken (z. B. Saisonalität, Lieferanten-Abhängigkeit)
- **1–4**: Hohe Risiken (rechtlich, Lieferkette, IP)

## 2. Empfehlungslogik (Notion, 1:1)

- **Gesamt-Score ≥ 7,5**: 🟢 Klares Go
- **Gesamt-Score 5,5–7,4**: 🟡 Bedingt – weitere Bedingungen prüfen
- **Gesamt-Score < 5,5**: 🔴 Stop oder ⏸️ Mehr Recherche

## 3. Gewichte [neu]

Notion rechnet den Gesamt-Score als Formel, die Gewichtung ist im Template nicht dokumentiert. Bis Pafri etwas anderes festlegt: **ungewichteter Mittelwert** der vier Scores (entspricht dem Yoga-Block-Beispiel in Notion: 8/7/8/7 → 7,5).

```
score_gesamt = (marge + markt + usp + risiko) / 4, eine Nachkommastelle
```

## 4. Zuordnung Gesamt-Score → Lane A–D [neu]

Miro nutzt A–D, Notion nutzt Zahlen. Vorschlag zur Verbindung:

| Lane | Bedeutung (Miro) | Gesamt-Score | Ampel |
|---|---|---|---|
| A | Empfohlen | ≥ 7,5 | 🟢 |
| B | Prüfen | 6,5–7,4 | 🟡 |
| C | Beobachten | 5,5–6,4 | 🟡 |
| D | Ablehnen | < 5,5 oder K.O. | 🔴 |

Importierte Miro-Karten behalten ihre Lane als `score`, `score_gesamt` bleibt `null`, bis `/voranalyse` die vier Einzelscores vergibt.

## 5. K.O.-Regeln [neu]

Abgeleitet aus den Prüfpunkten 4–8 der Voranalyse-Checkliste und den Ablehnungsgründen der Miro-Lane D. Ein K.O. setzt `score: D`, egal wie hoch die Einzelscores sind. Der Skill listet den Verstoß in `ko_verstoss`.

| Nr. | Regel | Quelle |
|---|---|---|
| K1 | Elektroprodukt (Prüf-, Zertifizierungs-, Registrierungspflicht) | Voranalyse Nr. 5 |
| K2 | Chemisches Produkt oder Lebensmittel mit erhöhten Prüfanforderungen (inkl. Düngemittelrecht) | Voranalyse Nr. 4, Miro „Rasendünger" |
| K3 | Erotik-/Erwachsenenprodukt (Werbebeschränkung) | Voranalyse Nr. 6 |
| K4 | Größenabhängige Retouren (Kleidung, Handschuhe, Schuhe) | Voranalyse Nr. 7, Miro „Gartenhandschuhe" |
| K5 | Versandgewicht > 2 kg oder Übergrößenzuschlag bei FBA ohne Premium-Preisspielraum | Voranalyse Nr. 1–2, Miro „Schlauchwagen", „Rankgitter" |
| K6 | Zielpreis auf Amazon.de dauerhaft < 10 € | Voranalyse Nr. 10 |
| K7 | Kein Markenfit: nicht Garten/Pflanzenpflege, nicht als Edelstahl/Premium positionierbar | CLAUDE.md, Miro „Windlicht", „Kräuterschneider" |

## 6. Schwellen für Weiterleitung [neu]

- `/ideen` vergibt nur eine Lane (A–D) als Vor-Score mit Begründung, keine Einzelscores.
- `/voranalyse` vergibt die vier Einzelscores und berechnet `score_gesamt`. Empfehlung Go nur bei ≥ 6,5 und ohne K.O.
- `/deep-dive` aktualisiert die Scores mit belegten Zahlen. Empfehlung Go nur bei ≥ 7,5 und ohne K.O.
- `/briefing` ändert keine Scores mehr.
