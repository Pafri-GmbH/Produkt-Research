# Schema – Frontmatter und Dateien

Alle Dateien in `ideas/`, `pipeline/` und `products/` sind Markdown mit YAML-Frontmatter. `scripts/dashboard.py` liest ausschließlich das Frontmatter.

## Slug

- Kleinbuchstaben, ASCII, Bindestriche: `bewaesserungskugeln-glas`, `pflanzenschere`.
- Umlaute: ä→ae, ö→oe, ü→ue, ß→ss.
- Produkttyp zuerst, Material/Variante danach: `pflanzgefaess-edelstahl-gross`.
- Dedupe vor jedem Anlegen: gleicher Slug, Synonym oder gleicher Produkttyp in anderer Größe → bestehende Datei ergänzen statt neue anlegen.

## Ideensteckbrief `ideas/<slug>.md` und `pipeline/<slug>/00-idee.md`

```yaml
---
slug: pflanzenschere
titel: Pflanzenschere
status: importiert            # siehe rules/prozess.md
status_datum: 2026-09-16
quelle: miro-longlist         # miro-longlist | ideen-lauf | pafri | drive
lauf: 2026-09-16-miro-import  # Dateiname in ideas/_laeufe/ ohne .md
kategorie: Pflege & Werkzeug  # Bewässerung | Pflege & Werkzeug | Anzucht & Ranken | Gefäße & Deko
vk_spanne_eur: [12, 25]       # Zielpreis auf Amazon.de, [min, max]
score: A                      # A | B | C | D  (rules/scoring.md)
score_gesamt: null            # 1–10, gewichteter Wert aus rules/scoring.md, null bis /voranalyse
scores:                       # Einzelscores 1–10, null wenn nicht bewertet
  marge: null
  markt: null
  usp: null
  risiko: null
ko_verstoss: []               # Liste der K.O.-Regeln aus rules/scoring.md, leer = keine
pipeline_status_miro: Longlist # nur bei quelle: miro-longlist
gate_1: null                  # go | stop | beobachten | null
gate_2: null
gate_3: null
ng_nummer: null               # NG0003 …
stop_grund: null
---
```

Pflichtabschnitte im Body (Reihenfolge fest, siehe `templates/ideensteckbrief.md`):
Kurzbeschreibung · Warum nicegarden · Markt-Ersteindruck · SWOT · KPIs · Referenz-ASINs · Quellen · Offene Punkte.

Fehlende Angaben werden als `[fehlt]` markiert, nie geraten.

## Stufen-Dateien in `pipeline/<slug>/`

| Datei | Frontmatter-Zusätze |
|---|---|
| `00-idee.md` | Kopie des Ideensteckbriefs zum Zeitpunkt der Freigabe |
| `01-voranalyse.md` | `stufe: voranalyse`, `datum`, `bearbeiter: claude`, `referenz_asin`, `hauptkategorie`, `fazit` |
| `02-deep-dive.md` | `stufe: deep-dive`, `datum`, `wettbewerber: [ASIN, …]`, `fazit` |
| `03-briefing.md` | `stufe: briefing`, `datum`, `ziel_ek_eur`, `ziel_vk_eur`, `moq`, `fazit` |

Der Statuswechsel erfolgt immer in `ideas/<slug>.md` (bleibt Quelle der Wahrheit für Status) **und** in `pipeline/<slug>/00-idee.md`. `scripts/dashboard.py` bevorzugt `pipeline/`/`products/`, wenn dort eine `00-idee.md` liegt.

## Lauf-Protokoll `ideas/_laeufe/<datum>-<thema>.md`

```yaml
---
lauf: 2026-09-18-giesszubehoer
datum: 2026-09-18
thema: Gießzubehör und Pflanzenpflege Innenraum
ziel_anzahl: 15
gefunden: 15
dedupe_verworfen: 3
quellen_eingeschraenkt: [amazon.de WebFetch blockiert]
---
```

Body nach `templates/lauf-protokoll.md`.

## Produkte `products/NG00xx/`

Ordner heißt nach NG-Nummer. Enthält die vier Stufen-Dateien aus `pipeline/<slug>/`. Frontmatter in `00-idee.md`: `status: produkt`, `ng_nummer: NG00xx`.
