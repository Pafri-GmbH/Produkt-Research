# Produktvideo Gießkanne (NG0001) – Storyboard

Stand: 2026-11-14 · 16:9, 1920×1080, 30 fps, 30,0 s, ohne Ton · Datei `NG0001_Produktvideo_16x9.mp4` · Quelle `src/video.html`

Jede Szene blendet 0,5 s über die vorherige. Erster Frame zeigt Produkt und Logo, die Endkarte steht ab 27,6 s bis zum letzten Frame.

| Zeit | Szene | Bildquelle | Text im Bild |
|---|---|---|---|
| 0,0–3,6 s | Einstieg: Produkt vor Flieder-Kreis, langsamer Zoom | Freisteller aus MAIN | MEHR FREUDE AM GIESSEN · Die Edelstahl-Gießkanne mit Holzgriff – 1 Liter |
| 3,6–8,2 s | Gießen auf Basilikum, langsamer Zoom zur Auslauf-Spitze | Foto aus PT06 | EINFACH & GENAU GIESSEN · Extra langer Auslauf · Präziser Ausguss · Leicht zu befüllen |
| 8,2–13,2 s | Drei Lupen: Gravur, Auslauf, Griff | Freisteller aus MAIN | MODERNES DESIGN TRIFFT QUALITÄT · Langlebig – Präzise – Wertig · Hochwertiger Edelstahl · Präziser Ausguss · Stabiler Holzgriff · Robust & rostfrei |
| 13,2–17,6 s | Maßlinien nacheinander | Freisteller aus MAIN, Werte aus PT03 | KOMPAKTES DESIGN – GROSSES VOLUMEN · Leicht und perfekt ausbalanciert · 9,5 cm · 13 cm · 11 cm · 15,8 cm · 1 L |
| 17,6–22,4 s | Wohnzimmer-Foto + vier Ortsbilder | Fotos aus PT04 | INDOOR & OUTDOOR GEEIGNET · Überall vielseitig einsetzbar · Wohnzimmer · Garten · Balkon · Küche · Bad |
| 22,4–26,2 s | Verpackung + Produkt auf Grün | MAIN ohne Badge | STILVOLL VERPACKT · Eine schöne Geschenkidee für Pflanzenliebhaber · Hochwertige Verpackung · Edles Design |
| 26,2–30,0 s | Endkarte mit Logo | Logo-SVG | MEHR FREUDE AM GIESSEN · Designed in Germany |

Alle Texte stammen aus den vorhandenen Listingbildern und dem Doc „Amazon Listing Blumengießkanne". Kein Preis, keine URL, keine Vergleichsaussage.

## Neu rendern

Rohdaten liegen unter `data/raw/listing/NG0001/` (gitignored): `original/` (7 Bilder aus Drive), `assets/` (Logo-SVG als `logo1_schwarz.svg`), `fonts/` (`npm pack @fontsource/red-hat-display`, entpackt). Benötigt: Python mit `pillow`, `opencv-python-headless`, `scipy`; Node mit Playwright; `ffmpeg`.

```bash
python3 products/NG0001/listing/src/prep_cutout.py
```
```bash
python3 products/NG0001/listing/src/prep_scene.py
```
```bash
python3 products/NG0001/listing/src/prep_crops.py
```
```bash
node scripts/listing_render.mjs still products/NG0001/listing/src/main_a.html data/raw/listing/NG0001/out/MAIN_A.png
```
```bash
node scripts/listing_render.mjs still products/NG0001/listing/src/pt04.html data/raw/listing/NG0001/out/PT04.png
```
```bash
node scripts/listing_render.mjs frame products/NG0001/listing/src/video.html data/raw/listing/NG0001/frames/vorschau.png --t 2.5
```
```bash
node scripts/listing_render.mjs video products/NG0001/listing/src/video.html data/raw/listing/NG0001/out/NG0001_Produktvideo_16x9.mp4 --dauer 30
```
```bash
python3 products/NG0001/listing/src/export.py
```

Texte und Zeiten ändern: in `src/video.html` (Szenen `#s1`–`#s7`, Zeitleiste im Skript am Ende). Das Rendern des Videos dauert etwa 4 Minuten.
