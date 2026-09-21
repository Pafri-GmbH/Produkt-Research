# CLAUDE.md – Produktrecherche nicegarden

Du unterstützt Pafri GmbH bei der Produktrecherche für die Marke **nicegarden** (Premium-Garten- und Pflanzenpflegeprodukte aus Edelstahl, Amazon.de FBA). Dieses Repo ist die Quelle der Wahrheit für den Prozess **Idee → Voranalyse → Tiefenanalyse → Produktbriefing**. Der Nutzer heißt intern **Pafri**.

## Sprache und Ton
- Deutsch. Englisch nur im Spezifikationsteil des Briefings (Teil B).
- Knapp, strukturiert, direkt. Keine Präambeln, keine Wiederholung des Gesagten.
- Slogan „Designed in Germany" – nie „Made in Germany".

## Prozess in Kurzform
`/ideen` → Freigabe durch Pafri → `/voranalyse <slug>` → Gate 1 → `/deep-dive <slug>` → Gate 2 → `/briefing <slug>` → Gate 3 → NG-Nummer.
Freigabe und Gate-Entscheidungen kommen per Chat **oder** per Button im Dashboard; Dashboard-Klicks holt `/entscheidungen` ab und führt die nächste Stufe aus.
Details, Status-Werte, Gate-Block und Warteschlange: `rules/prozess.md`.

## Betriebsregeln
1. **Stop/Go an jedem Gate.** Jeder Skill endet mit dem Gate-Block aus `rules/prozess.md` und wartet auf Pafris Entscheidung. Nie eigenmächtig die nächste Stufe starten. Eine Entscheidung im Chat und ein Klick im Dashboard (abgeholt durch `/entscheidungen`) sind gleichwertig; nur nach einer davon läuft die nächste Stufe.
2. **Zahlen haben eine Quelle.** Jede Zahl trägt Quelle und Abrufdatum oder ist als Schätzung markiert (`~`, „Schätzung aus …"). Es gibt keine Helium-10-Daten – BSR, Absatz und Suchvolumen sind immer Schätzungen und werden so beschriftet.
3. **Markt = Amazon.de.** Andere Marktplätze nur auf ausdrückliche Anfrage.
4. **Vorlagen 1:1.** `rules/scoring.md`, `rules/voranalyse.md`, `rules/deep-dive.md`, `rules/briefing.md` sind aus Pafris Vorlagen abgeleitet. Schema nicht ändern, ohne zu fragen.
5. **Status nur über Frontmatter.** Statuswechsel setzt der jeweilige Skill (`rules/schema.md`); danach immer `python scripts/dashboard.py`. Das erzeugt `DASHBOARD.md` und `dashboard.html`; `dashboard.html` anschließend als Artifact unter https://claude.ai/artifact/2rvyEyRe1p9ietKExeRiiT neu veröffentlichen (gleiche URL, nie ein neues Artifact anlegen, nie den Parameter `capabilities` übergeben – sonst verlieren die Dashboard-Buttons ihre Datenbank).
6. **Dedupe.** Vor jeder neuen Idee `ideas/`, `pipeline/` und `products/` prüfen – Slug, Synonyme, gleicher Produkttyp in anderer Größe.
7. **Ein Lauf oder eine Stufe = ein Commit.** Format: `feat(ideen): lauf 2026-09-18 giesszubehoer` · `feat(<slug>): voranalyse` · `gate(<slug>): go deep-dive`.
8. **Websuche.** Amazon.de-Seiten per WebFetch können blockiert sein. Dann: Suchmaschinen-Snippets, Wettbewerber-Shops, Preisvergleiche, Händlerseiten. Einschränkung im Lauf-Protokoll vermerken, nie stillschweigend raten.
9. **Nichts außerhalb des Repos.** Keine Mails, keine Bestellungen, keine Lieferantenkontakte – das Briefing ist die Übergabe an Pafri.

## Repo-Struktur
```
CLAUDE.md               diese Datei
START-PROMPT.md         Einrichtung und erster Lauf
DASHBOARD.md            generierte Übersicht (scripts/dashboard.py)
dashboard.html          generiertes interaktives Dashboard, veröffentlicht als Artifact (zentrales Tool, Buttons schreiben in die Artifact-DB)
rules/                  Prozess, Schema, Produktkriterien, Recherche-Quellen, Stufen-Schemata (aus Vorlagen)
templates/              Ideensteckbrief, Lauf-Protokoll
vorlagen/               Pafris Original-Vorlagen (docx/xlsx/md) – nur lesen
ideas/<slug>.md         Stufe 0: eine Datei je Idee
ideas/_laeufe/          Protokoll je Recherche-Lauf
pipeline/<slug>/        Stufe 1–3: 00-idee.md, 01-voranalyse.md, 02-deep-dive.md, 03-briefing.md (Review im Dashboard liest fazit + Gate-Block)
products/NG00xx/        nach Gate 3 (Go): Ordner aus pipeline/ hierher verschoben
data/raw/               Rohdaten, ignoriert (z. B. Miro-Export)
scripts/                dashboard.py, dashboard_template.html
.claude/skills/         ideen, voranalyse, deep-dive, briefing, entscheidungen
```

## Beim Start jeder Session
1. `DASHBOARD.md` lesen (interaktiv: https://claude.ai/artifact/2rvyEyRe1p9ietKExeRiiT).
2. Die `rules/`-Datei der angefragten Stufe lesen.
3. Bei `/voranalyse`, `/deep-dive`, `/briefing`: alle vorherigen Stufen-Dateien der Idee lesen.
4. Erst dann arbeiten.
