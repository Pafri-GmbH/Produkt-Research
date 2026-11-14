"""Endformate für den Upload (NG0001): PNG-Render -> JPEG (sRGB, Qualität 92, 4:4:4) und Prüfwerte.

Erwartet in data/raw/listing/NG0001/out/: MAIN_A.png, PT04.png (scripts/listing_render.mjs still …)
und frames/vorschau.png (… frame … --t 2.5). Schreibt nach data/raw/listing/NG0001/upload/.
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageCms

ROOT = Path(__file__).resolve().parents[4]
RAW = ROOT / "data/raw/listing/NG0001"
UP = RAW / "upload"
SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()


def jpeg(src: Path, name: str) -> Path:
    im = Image.open(src).convert("RGB")
    dst = UP / name
    im.save(dst, "JPEG", quality=92, subsampling=0, optimize=True, icc_profile=SRGB)
    print(f"{name:28s} {im.size[0]}x{im.size[1]}  {dst.stat().st_size / 1e6:.2f} MB")
    return dst


def main() -> None:
    UP.mkdir(parents=True, exist_ok=True)
    a = jpeg(RAW / "out/MAIN_A.png", "MAIN_A.jpg")
    jpeg(RAW / "assets/main_b_rgb.png", "MAIN_B.jpg")
    jpeg(RAW / "out/PT04.png", "PT04.jpg")
    # unverändert, nur als echtes JPEG (Originale sind PNG-Daten mit Endung .jpg, 6–9 MB)
    jpeg(RAW / "original/PT01.png", "PT01.jpg")
    jpeg(RAW / "original/PT03.png", "PT03.jpg")
    jpeg(RAW / "frames/vorschau.png", "Video_Vorschaubild.jpg")

    # Prüfung Hauptbild A: Ecken reinweiß, Produkt füllt >= 85 % der längeren Kante
    px = np.asarray(Image.open(a).convert("RGB"))
    ecken = [tuple(int(v) for v in px[y, x]) for y, x in [(0, 0), (0, -1), (-1, 0), (-1, -1)]]
    alpha = np.asarray(Image.open(RAW / "assets/kanne.png"))[..., 3]
    breite = alpha.shape[1] * 2705 / 2902 / 3000          # Skalierung aus main_a.html
    rand = np.concatenate([px[:40].reshape(-1, 3), px[-40:].reshape(-1, 3), px[:, :40].reshape(-1, 3), px[:, -40:].reshape(-1, 3)])
    print("MAIN_A Ecken:", ecken, "| Randstreifen min:", int(rand.min()), f"| Produktbreite: {breite:.1%} der Bildkante")


if __name__ == "__main__":
    main()
