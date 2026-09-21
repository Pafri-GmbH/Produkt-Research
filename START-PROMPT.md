# Start mit Claude Code

## Einmalige Einrichtung (manuell, 10 Minuten)
1. GitHub: neues privates Repository `Produkt-Research`, ohne README.
2. Terminal: `git clone <repo-url> && cd Produkt-Research`
3. Inhalt dieses Startpakets in den Ordner kopieren (inkl. versteckter `.claude/` und `.gitignore`).
4. Deine Vorlagen nach `vorlagen/` legen – siehe `vorlagen/README.md`.
5. Optional: Miro-Longlist als CSV/Text nach `data/raw/miro-longlist.csv` (oder `.md`).
6. `git add -A && git commit -m "chore: startpaket"` – dann `claude` starten.
7. Amazon-Zugriff für `/amazon` (Voranalyse, Deep-Dive): In der Cloud-Session auf claude.ai/code die Umgebung bearbeiten → Network access **Custom** → „Also include default list of common package managers" anhaken → Allowed domains `www.amazon.de`, `*.amazon.de`, `*.media-amazon.com`, `*.ssl-images-amazon.com`, `completion.amazon.de` (optional `www.idealo.de`, `*.alibaba.com`, `www.ebay.de`, `www.otto.de`). Lokal stattdessen `npm i -g playwright && npx playwright install chromium`; Details in `.claude/skills/amazon/SKILL.md`.

## Prompt 1 – Einrichtung (in Claude Code einfügen)

```
Lies CLAUDE.md, rules/prozess.md und rules/schema.md.

Schritt 1 – Vorlagen übernehmen
In vorlagen/ liegen meine Templates: Scoring-Modell, Voranalyse, Tiefenanalyse, Briefing-Beispiel NG0002. Lies sie (docx mit python-docx, xlsx mit openpyxl, falls nötig installieren). Leite daraus ab:
- rules/scoring.md   – Kriterien, Gewichte, Anker, K.O.-Regeln, Schwellen
- rules/voranalyse.md – alle Prüfpunkte der Vorlage in der Originalreihenfolge
- rules/deep-dive.md  – Wettbewerber-Schema und alle Abschnitte der Vorlage
- rules/briefing.md   – Struktur des NG0002-Briefings als Vorlage, Teil A deutsch (Entscheidung), Teil B englisch (Spezifikation für Sourcing)
Schema 1:1, nichts weglassen, nichts hinzufügen. Zeig mir vor dem Schreiben je Datei die Abschnittsliste in einer Zeile pro Abschnitt. Wo eine Vorlage etwas nicht abdeckt, das der Prozess braucht (z. B. Rezensions-Mining im Deep-Dive, Sourcing-Spezifikation im Briefing), schlag einen Zusatzabschnitt vor und markiere ihn als [neu].

Schritt 2 – Longlist importieren
Falls data/raw/miro-longlist.* existiert: jede Zeile als ideas/<slug>.md nach templates/ideensteckbrief.md anlegen, status: importiert, quelle: miro-longlist, vorhandene Bewertungen (A/B/C/D, SWOT, KPIs) übernehmen. Fehlendes als [fehlt] markieren.

Schritt 3 – Dashboard
python scripts/dashboard.py ausführen, DASHBOARD.md zeigen.

Schritt 4 – Stopp
Commit „chore: vorlagen und import". Dann warten – ich starte den ersten Lauf selbst mit /ideen.
```

## Prompt 2 – erster Recherche-Lauf

```
/ideen Gießzubehör und Pflanzenpflege Innenraum 15
```

Danach läuft der Prozess über die Skills: `/voranalyse <slug>`, `/deep-dive <slug>`, `/briefing <slug>`. Jeder Skill endet mit einem Gate-Block und wartet auf dein Go/Stop.

## Bedienung über das Dashboard

Im Dashboard (https://claude.ai/artifact/2rvyEyRe1p9ietKExeRiiT) öffnest du eine Idee, liest unter „Review“ Fazit und Gate-Empfehlung und klickst **Freigeben**, **Go**, **Stop**, **Beobachten** oder **Nacharbeit**. Der Klick landet in der Warteschlange. In einer Claude-Session genügt dann:

```
/entscheidungen
```

Claude holt alle Klicks ab, setzt Status und Gate im Repo, führt die nächste Stufe aus (Voranalyse, Deep-Dive, Briefing oder NG-Nummer) und veröffentlicht das Dashboard neu. Chat-Entscheidungen funktionieren weiterhin genauso.
