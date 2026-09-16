---
name: ideen
description: Stufe 0 – Recherche-Lauf für neue nicegarden-Produktideen auf Amazon.de. Aufruf /ideen <Thema> [Anzahl]. Legt ideas/<slug>.md an, schreibt Lauf-Protokoll und endet mit Freigabeliste für Pafri.
---

# /ideen <Thema> [Anzahl, Standard 10]

## Vorbereitung
1. `DASHBOARD.md`, `rules/prozess.md`, `rules/schema.md`, `rules/produktkriterien.md`, `rules/scoring.md`, `rules/quellen.md` lesen.
2. Bestand für Dedupe laden: alle Slugs und Titel aus `ideas/`, `pipeline/`, `products/`.

## Recherche
3. Suchraster aus dem Thema ableiten: 8–15 Keywords (deutsch), Amazon-Kategorien, Synonyme.
4. Quellen in der Reihenfolge aus `rules/quellen.md`. Amazon.de blockiert → Alternativen, Einschränkung notieren.
5. Je Kandidat: Preisspanne, 3 Top-Anbieter mit ~Bewertungen, Saisonalität, Versandgewicht, grobe Alibaba-Spanne. Jede Zahl mit Quelle/Datum oder `~`.
6. K.O.-Regeln (`rules/scoring.md` Abschnitt 5) prüfen. K.O. → Lane D, trotzdem anlegen, damit die Ablehnung dokumentiert ist.
7. Vor-Score als Lane A–D vergeben (keine Einzelscores).

## Dedupe
8. Gleicher Slug, Synonym, gleicher Produkttyp in anderer Größe → nicht neu anlegen. Bestehende Datei um neue Erkenntnisse ergänzen und im Protokoll unter „Dedupe" führen.

## Schreiben
9. Je Idee `ideas/<slug>.md` nach `templates/ideensteckbrief.md`, `status: idee`, `quelle: ideen-lauf`, `lauf: <datum>-<thema-slug>`.
10. `ideas/_laeufe/<datum>-<thema-slug>.md` nach `templates/lauf-protokoll.md`.
11. `python scripts/dashboard.py`.
12. Commit: `feat(ideen): lauf <datum> <thema-slug>`.

## Abschluss
13. Freigabeliste ausgeben (ersetzt den Gate-Block): eine Zeile je Idee `- [ ] <slug> – Lane – ein Satz`. Dann warten. Nie `/voranalyse` selbst starten.
14. Bei Freigabe durch Pafri: `status: freigegeben`, `status_datum`, Dashboard, Commit `gate(<slug>): freigegeben`.
