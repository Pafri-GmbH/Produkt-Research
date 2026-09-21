# Kalkulation, Zahlenkennzeichnung, Ton

Gemeinsame Regeln für `/voranalyse` und `/deep-dive`. Quelle: Pafris Detaildokument (`vorlagen/detaildokument-analysen.md`, Abschnitt 0). Ergänzt `rules/prozess.md` (Zahlen und Quellen) und `rules/quellen.md`.

## 1. Kalkulationslogik (einheitlich in beiden Stufen)

```
Netto-VK        = Brutto-VK / 1,19
Verkaufsgebühr  = Brutto-VK × 15 %                       (Amazon-Kategorie Garten)
FBA-Versand     = laut Größenklasse (Kleines Paket / Standard / Groß), Gebührentabelle DE
Landed Cost     = EK + Fracht + Zoll + Einfuhrnebenkosten (je Stück)
DB1 (€)         = Netto-VK − Landed Cost − Verkaufsgebühr − FBA-Versand
DB1 (%)         = DB1 (€) / Netto-VK
DB2 (€)         = DB1 (€) − Lagerkosten − EPR/Verpackung − Retourenpauschale − Ads-Anteil
Break-even-ACOS = DB1 (€) / Brutto-VK                    (Ziel ≥ 35 %; Referenz NG0001: 43,7 %)
Kapitalbedarf   = MOQ × Landed Cost + Erstausstattung (Fotos, Verpackungsdesign, Samples)
```

- **EK ohne Angebot:** 30-%-Regel (EK ≈ 30 % vom Brutto-VK), immer als Schätzung markiert. Liegt ein Alibaba-Richtpreis vor, hat er Vorrang (Quelle, Datum, MOQ nennen).
- **Fracht und Zoll ohne Angebot:** Pauschale je Stück aus Seefracht-Richtwerten China–DE und TARIC-Zollsatz, als Schätzung markiert.
- **CPC-Niveau:** ohne Helium 10 als Schätzung aus dem Nischenvergleich (`~0,60–0,90 €`), Grundlage nennen.
- Voranalyse: eine Variante, Pauschalen. Deep-Dive: je Variante, alle Kostenblöcke, Sensitivität (EK ± 15 %, CPC ± 30 %, VK −10 % / Ziel / +10 %).

## 2. Kennzeichnung von Zahlen (Pflicht)

| Art | Schreibweise |
|---|---|
| Beobachtet | `Wert (Quelle, YYYY-MM-DD)` |
| Geschätzt | `~Wert (Schätzung: Grundlage)` – gilt immer für BSR, Absatz, Suchvolumen, CPC, EK ohne Angebot |
| Nicht ermittelbar | `[fehlt]` – der Prüfpunkt bleibt in der Datei stehen, wird nie gelöscht |

Werte mit Einheit schreiben (`24,90 €`, `41 %`, `~450 St./Monat`), Dezimaltrennzeichen Komma.

## 3. Ton und Umfang

- Deutsch, knapp, jede Aussage mit Zahl oder Grund. Keine „könnte funktionieren"-Formulierungen.
- Die Datei enthält die Details, der Chat nur die Zusammenfassung (max. 10 Zeilen) plus Gate-Block.
- Alle Prüfpunkte der Vorlage bleiben stehen, nichts weglassen, nichts umsortieren.
- Zahlen aus der Voranalyse werden im Deep-Dive übernommen und nur mit Begründung geändert; Änderungen im Executive Summary ausweisen.
