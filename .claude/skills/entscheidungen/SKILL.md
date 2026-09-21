---
name: entscheidungen
description: Übersicht aller offenen Entscheidungen für Pafri – wartende Gates, Freigaben, entschiedene aber nicht gestartete Stufen, ungeprüfte Importe, Beobachten-Liste. Aufruf /entscheidungen [<slug>]. Nimmt anschließend Pafris Entscheidungen entgegen und setzt sie um.
---

# /entscheidungen [<slug>]

Reine Entscheidungsübersicht. Startet keine Stufe, schreibt nichts, bis Pafri entscheidet.

## Vorbereitung
1. `rules/prozess.md` lesen (Status-Werte, Gate-Regeln, Commit-Format).
2. `python scripts/entscheidungen.py --md` ausführen. Das Skript liest ausschließlich das Frontmatter in `ideas/`, `pipeline/`, `products/` und die Gate-Blöcke der aktuellen Stufen-Dateien.

## Ausgabe
3. Die fünf Abschnitte des Skripts unverändert ausgeben (Gates · Freigaben · Entschieden-nicht-gestartet · Importiert-ungeprüft · Beobachten). Bei sehr langen Tabellen (Abschnitt 4) nur Lane A vollständig, B und C als Zählung mit Hinweis auf `DASHBOARD.md`.
4. Bei offenen Gates je Slug zusätzlich den vollständigen Gate-Block aus der Stufen-Datei zitieren (Empfehlung, Begründung, offene Punkte).
5. Mit `<slug>`: nur diesen Eintrag zeigen, mit Gate-Block und Kurzbeschreibung aus dem Steckbrief.
6. Abschluss mit der Antwortsyntax:

```
Deine Entscheidungen (eine Zeile je Slug):
  go <slug>                 Gate passieren, nächste Stufe freigeben
  stop <slug> <grund>       ablehnen
  beobachten <slug> <grund> zurückstellen
  nacharbeit <slug> <lücke> gleiche Stufe überarbeiten
  freigabe <slug>           Idee (idee/importiert) für /voranalyse freigeben
  aufnehmen <slug>          Beobachten → freigegeben
```

## Umsetzung nach Pafris Antwort
7. Je Entscheidung Frontmatter setzen (`rules/prozess.md`, `rules/schema.md`):
   - `go` → `gate_<n>: go`, Status unverändert.
   - `stop` → `status: abgelehnt`, `status_datum`, `stop_grund`.
   - `beobachten` → `status: beobachten`, `status_datum`, `stop_grund`.
   - `freigabe` / `aufnehmen` → `status: freigegeben`, `status_datum`, `stop_grund: null`.
   - `nacharbeit` → kein Statuswechsel, Lücke an den zuständigen Skill übergeben (nicht selbst starten).
   Änderungen immer in `ideas/<slug>.md` **und**, falls vorhanden, `pipeline/<slug>/00-idee.md`.
8. `python scripts/dashboard.py`, `dashboard.html` als Artifact unter https://claude.ai/artifact/2rvyEyRe1p9ietKExeRiiT neu veröffentlichen.
9. Ein Commit je Entscheidung: `gate(<slug>): go deep-dive` · `gate(<slug>): stop` · `gate(<slug>): beobachten` · `gate(<slug>): freigabe`.
10. Danach die nächsten Schritte auflisten (`/voranalyse <slug>` usw.) und warten. Nie eigenmächtig die nächste Stufe starten.
