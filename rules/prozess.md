# Prozess – Idee → Voranalyse → Tiefenanalyse → Briefing

## Stufen und Skills

| Stufe | Skill | Eingabe | Ausgabe | Gate |
|---|---|---|---|---|
| 0 Ideen | `/ideen <Thema> [n]` | Suchfeld, Anzahl | `ideas/<slug>.md` je Idee, `ideas/_laeufe/<datum>-<thema>.md` | Freigabe durch Pafri je Idee |
| 1 Voranalyse | `/voranalyse <slug>` | freigegebene Idee | `pipeline/<slug>/00-idee.md` + `01-voranalyse.md` | Gate 1 |
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

Nur Pafri entscheidet. Der Skill schreibt seine Empfehlung, wartet und startet nie die nächste Stufe.

- **Go**: Skill setzt `gate_<n>: go`, `status` bleibt bis zum Start der nächsten Stufe unverändert. Commit `gate(<slug>): go <nächste-stufe>`.
- **Stop**: `status: abgelehnt`, `stop_grund` ausfüllen. Commit `gate(<slug>): stop`.
- **Beobachten**: `status: beobachten`, `stop_grund` ausfüllen. Commit `gate(<slug>): beobachten`.
- **Nacharbeit**: Pafri nennt die Lücke, Skill überarbeitet dieselbe Datei, kein Statuswechsel.

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
gate(<slug>): go deep-dive
gate(<slug>): stop
chore: …
```

## Zahlen und Quellen

- Jede Zahl trägt `(Quelle, Abrufdatum)` oder ist als Schätzung markiert: `~` oder „Schätzung aus …".
- BSR, Absatz und Suchvolumen sind ohne Helium 10 immer Schätzungen. Beschriftung: `~450 St./Monat (Schätzung aus BSR ~1.300 Garten, 2026-09-16)`.
- Amazon.de per WebFetch blockiert → Alternativen in `rules/quellen.md`, Einschränkung im Lauf-Protokoll vermerken.
