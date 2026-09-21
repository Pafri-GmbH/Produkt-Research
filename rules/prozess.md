# Prozess – Idee → Voranalyse → Tiefenanalyse → Briefing

## Stufen und Skills

| Stufe | Skill | Eingabe | Ausgabe | Gate |
|---|---|---|---|---|
| 0 Ideen | `/ideen <Thema> [n]` | Suchfeld, Anzahl | `ideas/<slug>.md` je Idee, `ideas/_laeufe/<datum>-<thema>.md` | Freigabe durch Pafri je Idee |
| 1 Voranalyse | `/voranalyse <slug>` | freigegebene Idee | `pipeline/<slug>/00-idee.md` + `01-voranalyse.md` | Gate 1 |
| – Entscheidungen | `/entscheidungen [slug]` | Klicks aus dem Dashboard (Freigabe, Go, Stop, Beobachten, Nacharbeit) | Gate/Status im Repo, danach die nächste Stufe | – |
| 2 Tiefenanalyse | `/deep-dive <slug>` | Voranalyse mit Go | `pipeline/<slug>/02-deep-dive.md` | Gate 2 |
| 3 Briefing | `/briefing <slug>` | Deep-Dive mit Go | `pipeline/<slug>/03-briefing.md` | Gate 3 → NG-Nummer |

Nach Gate 3 (Go): Ordner `pipeline/<slug>/` nach `products/NG00xx/` verschieben, `ng_nummer` im Frontmatter setzen.

## Status-Werte (Frontmatter `status`)

| Status | Gesetzt von | Bedeutung |
|---|---|---|
| `importiert` | Import | Aus Miro-Longlist übernommen, noch nicht durch `/ideen` geprüft |
| `idee` | `/ideen` | Neu recherchiert, wartet auf Freigabe |
| `freigegeben` | Pafri | Freigabe für Voranalyse erteilt |
| `voranalyse` | `/voranalyse` | Voranalyse geschrieben, wartet an Gate 1 |
| `deep-dive` | `/deep-dive` | Tiefenanalyse geschrieben, wartet an Gate 2 |
| `briefing` | `/briefing` | Briefing geschrieben, wartet an Gate 3 |
| `produkt` | Pafri (Gate 3 Go) | NG-Nummer vergeben, in `products/` |
| `beobachten` | Pafri | Zurückgestellt, wird bei passendem Anlass wieder aufgenommen |
| `abgelehnt` | Pafri | Stop an einem Gate oder bei der Freigabe |

Jeder Statuswechsel trägt `status_datum` (ISO-Datum) und bei Stop/Beobachten ein Feld `stop_grund`.

## Gate-Entscheidung

Nur Pafri entscheidet. Der Skill schreibt seine Empfehlung, wartet und startet nie von sich aus die nächste Stufe.

Zwei gleichwertige Wege für die Entscheidung:
1. **Chat**: Pafri antwortet auf den Gate-Block; der Skill der Stufe setzt Gate/Status (Schritt „Nach Pafris Entscheidung“).
2. **Dashboard**: Pafri klickt im Steckbrief auf Freigeben, Go, Stop, Beobachten oder Nacharbeit. Der Klick liegt als Dokument in der Artifact-Datenbank (Collection `entscheidungen`, siehe unten) und gilt als Pafris Entscheidung. `/entscheidungen` holt ihn ab, setzt Gate/Status und führt die nächste Stufe im selben Lauf aus.

- **Freigabe** (Stufe 0 → 1): `status: freigegeben`. Commit `gate(<slug>): freigabe voranalyse`.
- **Go**: Skill setzt `gate_<n>: go`, `status` bleibt bis zum Start der nächsten Stufe unverändert. Commit `gate(<slug>): go <nächste-stufe>`.
- **Stop**: `status: abgelehnt`, `stop_grund` ausfüllen. Commit `gate(<slug>): stop`.
- **Beobachten**: `status: beobachten`, `stop_grund` ausfüllen. Commit `gate(<slug>): beobachten`.
- **Nacharbeit**: Pafri nennt die Lücke, Skill überarbeitet dieselbe Datei, kein Statuswechsel. Commit `feat(<slug>): nacharbeit <stufe>`.

### Warteschlange `entscheidungen/<slug>` (Artifact-Datenbank)

Ein Dokument je Slug, Dokument-ID = Slug, letzte Entscheidung gewinnt. Das Repo bleibt Quelle der Wahrheit; die Datenbank ist nur der Briefkasten zwischen Dashboard und Session.

```json
{
  "slug": "pflanzenschere",
  "aktion": "freigabe | go | stop | beobachten | nacharbeit",
  "gate": 0,
  "naechste_stufe": "Voranalyse | Deep-Dive | Briefing | NG-Nummer | null",
  "erwarteter_status": "importiert",
  "kommentar": "",
  "erstellt": "2026-09-21T09:12:00Z",
  "status": "offen | verarbeitet | abgebrochen",
  "verarbeitet": null, "commit": null, "hinweis": null
}
```

`gate` 0 = Freigabe, 1–3 = Gate. `kommentar` ist Pflicht bei Stop, Beobachten (wird `stop_grund`) und Nacharbeit (Auftrag). `erwarteter_status` ist der Status zum Klickzeitpunkt; weicht er vom Repo ab, setzt `/entscheidungen` das Dokument auf `abgebrochen` mit `hinweis` und führt nichts aus.

## Gate-Block (Pflicht am Ende jedes Skills)

```
---
## Gate <n>: <Stufe> – <slug>
**Empfehlung:** Go | Stop | Beobachten
**Begründung (3 Sätze max):** …
**Offene Punkte / Datenlücken:** …
**Nächster Schritt bei Go:** /<nächster-skill> <slug>
**Deine Entscheidung (Go / Stop / Beobachten / Nacharbeit):** _wartet_
---
```

Bei `/ideen` ersetzt die Freigabeliste den Gate-Block: eine Zeile je Idee mit Slug, Kurzbeschreibung, Vor-Score, Empfehlung. Pafri markiert die Freigaben.

## Commits

Ein Lauf oder eine Stufe = ein Commit. Danach immer `python scripts/dashboard.py`, `DASHBOARD.md` und `dashboard.html` mitcommitten und `dashboard.html` als Artifact unter https://claude.ai/artifact/2rvyEyRe1p9ietKExeRiiT neu veröffentlichen.

```
feat(ideen): lauf 2026-09-18 giesszubehoer
feat(<slug>): voranalyse
feat(<slug>): deep-dive
feat(<slug>): briefing
feat(<slug>): nacharbeit voranalyse
gate(<slug>): freigabe voranalyse
gate(<slug>): go deep-dive
gate(<slug>): stop
chore: …
```

Beim Veröffentlichen von `dashboard.html` als Artifact nie den Parameter `capabilities` übergeben: Das Dashboard ist einmalig mit `{db: {}}` veröffentlicht worden, jede weitere Veröffentlichung ohne den Parameter behält das bei. Wer `capabilities` neu setzt oder leert, schaltet die Buttons ab.

## Zahlen und Quellen

- Jede Zahl trägt `(Quelle, Abrufdatum)` oder ist als Schätzung markiert: `~` oder „Schätzung aus …".
- BSR, Absatz und Suchvolumen sind ohne Helium 10 immer Schätzungen. Beschriftung: `~450 St./Monat (Schätzung aus BSR ~1.300 Garten, 2026-09-16)`.
- Amazon.de per WebFetch blockiert → Alternativen in `rules/quellen.md`, Einschränkung im Lauf-Protokoll vermerken.
