# Listing-Update Gießkanne (NG0001) – Bild-Audit

Stand: 2026-11-14 · Quelle: Drive-Ordner „Listingbilder - Gießkanne - NG0001" (`1tdOfoxY_0pA-juvGuqDUqzpGGha00cOM`), 7 Bilder, abgerufen 2026-11-14 · Texte: Doc „Amazon Listing Blumengießkanne" (`14yw9uYB50JSI-PGSM6URC9VTj3DzmMbQIMZtoB9I2qs`) · CI: „NICEGARDEN Brand CI 03:25.png"

Ergebnis in Drive: Unterordner [Update 2026-11](https://drive.google.com/drive/folders/1y5vSEN5R_u_DWU6Yj7V1x5kex0e6U9A4). Originale unverändert.

## Befund und Maßnahme je Bild

| Bild | Inhalt | Befund | Maßnahme |
|---|---|---|---|
| MAIN | Produkt + Verpackung + Badge „Deutsches Start-up" mit Flagge | Badge/Text und Verpackung widersprechen den Hauptbild-Regeln (reines Weiß, nur das Produkt, kein Text/Badge). Flagge legt deutsche Herkunft nahe; Marke sagt „Designed in Germany". Datei ist PNG mit Endung `.jpg` (6,5 MB). | **MAIN_A** neu: nur Produkt auf Weiß. **MAIN_B** als Alternative: wie bisher, Badge entfernt. |
| PT01 | Garten-Szene, „Besonders einfaches & genaues Giessen" | Inhalt in Ordnung. Datei ist PNG mit Endung `.jpg` (9,3 MB). | Nur Neuexport als JPEG (1,9 MB). |
| PT02 | Indoor & Outdoor, 4 Szenen | In Ordnung. | Keine. |
| PT03 | Maße, 1 L | In Ordnung. Datei ist PNG mit Endung `.jpg` (6,1 MB). Dezimalpunkt statt Komma („9.5 cm"). | Nur Neuexport als JPEG (1,4 MB). |
| PT04 | „Immer griffbereit", 5 Orte | Kein Produkt im Bild; Aussage doppelt PT02. Bullet 4 (Geschenk/Verpackung) hat kein eigenes Bild. | **PT04** neu: „Eine schöne Geschenkidee" mit Verpackung + Produkt. |
| PT05 | Detail-Features | In Ordnung. | Keine. |
| PT06 | Marke, Gießen auf Basilikum | In Ordnung. Unterzeile „Zeitloses Design aus Deutschland". | Keine (siehe Empfehlungen). |

### Korrektur gegenüber dem Plan
Im Plan stand für PT01 „lila Himmel, sichtbare Farbstufen". Das war ein Fehler der verkleinerten Vorschau bei der Sichtung. Das Original in 3000×3000 hat einen normalen Himmel und keine Farbstufen. PT01 wurde deshalb nicht neu gebaut, nur als JPEG exportiert.

## Neue Dateien

| Datei | Format | Größe | Hinweis |
|---|---|---|---|
| `MAIN_A.jpg` | 3000×3000, JPEG, sRGB | 0,56 MB | Ecken und Randstreifen gemessen 255/255/255; Produktbreite 90 % der Bildkante. Bodenschatten aus dem Original übernommen. |
| `MAIN_B.jpg` | 3000×3000 | 0,97 MB | Original-MAIN, nur Badge retuschiert. Verpackung bleibt im Bild → Restrisiko bei den Hauptbild-Regeln bleibt. |
| `PT04.jpg` | 3000×3000 | 0,84 MB | Texte: „Eine schöne Geschenkidee" · „Hochwertig & stilvoll verpackt" · Hochwertige Verpackung · Edles Design · Ideal zum Verschenken (aus Bullet 4). |
| `PT01.jpg`, `PT03.jpg` | 3000×3000 | 1,93 / 1,41 MB | Inhalt unverändert. |
| `NG0001_Produktvideo_16x9.mp4` | 1920×1080, 30 fps, H.264, 30,0 s, ohne Ton | 9,0 MB | Aufbau siehe `storyboard.md`. |
| `Video_Vorschaubild.jpg` | 1920×1080 | 0,21 MB | Frame bei 2,5 s. |
| `Kontaktbogen.jpg` | 3600×2120 | 0,96 MB | Bisher / Neu nebeneinander. |

PT02, PT05, PT06 wurden nicht neu abgelegt – die Originale im Hauptordner gelten weiter.

## Empfehlungen (nicht umgesetzt, Entscheidung Pafri)
1. **Hauptbild:** MAIN_A einsetzen. MAIN_B nur, wenn die Verpackung im Hauptbild wichtiger ist als die Regelkonformität.
2. **PT06 Unterzeile:** „Zeitloses Design aus Deutschland" → „Designed in Germany" (Marken-Slogan). Das Video nutzt bereits „Designed in Germany".
3. **PT03:** Dezimalkomma („9,5 cm", „15,8 cm", „11,2 cm"). Das Video nutzt Kommas.
4. **Maße prüfen:** Das Listing-Doc nennt „T × B × H – 11 × 13,5 × 27 cm", PT03 zeigt Höhe 13 cm, Boden 11 cm, Auslauf 15,8 cm. Die 27 cm passen nicht zur Höhe (eher Gesamtlänge mit Auslauf). Vor dem nächsten Textupdate am Produkt nachmessen.
5. **Reihenfolge (Vorschlag):** MAIN_A → PT01 → PT05 → PT03 → PT02 → PT04 neu → PT06.

## Einschränkungen
- Kein Filmmaterial vorhanden: Das Video ist aus den Standbildern animiert (Zooms, Einblendungen), kein gefilmter Gieß-Clip.
- Keine neuen Produktaussagen: alle Texte stammen aus den vorhandenen Bildern und dem Listing-Doc.
- Amazon-Vorgaben nicht live gegen Seller Central / Amazon Ads geprüft: `advertising.amazon.com` ist in dieser Cloud-Umgebung nicht freigegeben. Zugrunde gelegt: Sponsored Brands Video 6–45 s, 16:9, 1920×1080, MP4/MOV, ≤ 500 MB, keine schwarzen Balken, kein Text unten rechts; Listing-Video MP4/MOV (Drittquellen, abgerufen 2026-11-14: [perpetua.io](https://perpetua.io/sponsored-brands-video/), [goatconsulting.com](https://goatconsulting.com/merchandising/complete-guide-to-amazon-video-requirements-2024), [sell.amazon.com](https://sell.amazon.com/blog/amazon-product-video)). Ob eine Tonspur Pflicht ist, war nicht belegbar; falls der Upload eine verlangt:
  ```bash
  ffmpeg -i NG0001_Produktvideo_16x9.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo -shortest -c:v copy -c:a aac -b:a 128k NG0001_Produktvideo_16x9_stumm.mp4
  ```
- Das Video (9,0 MB) ließ sich nicht per Connector nach Drive laden (Limit ca. 3 MB je Datei). Es wurde im Chat übergeben und muss von Hand in den Drive-Ordner gelegt werden.
- Kein Upload zu Amazon, keine Mails.

## Schrift und Farben
Red Hat Display (npm `@fontsource/red-hat-display`, OFL) · Grün `#31511E` · Flieder `#CCC5F1` · Beige `#EFEDE9` · Logo aus Drive „Logo 03/25" (`nicegarden_logo1_schwarz_transparent.svg`).
