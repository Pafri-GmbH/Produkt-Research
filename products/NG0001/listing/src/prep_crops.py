"""Foto-Ausschnitte und Deko aus den Original-Listingbildern (NG0001) für PT04-neu und das Video.

Koordinaten beziehen sich auf die 3000x3000-Originale. Ausgabe: data/raw/listing/NG0001/assets/.
"""
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[4]
RAW = ROOT / "data/raw/listing/NG0001"
A = RAW / "assets"
Q = [cv2.IMWRITE_JPEG_QUALITY, 94]


def main() -> None:
    A.mkdir(parents=True, exist_ok=True)
    pt01 = cv2.imread(str(RAW / "original/PT01.png"))
    pt04 = cv2.imread(str(RAW / "original/PT04.jpg"))
    pt06 = cv2.imread(str(RAW / "original/PT06.jpg"))

    # 16:9-Fotoflächen (ohne Kopfzeile, ohne Logo unten rechts). Die fliederfarbene Infobox
    # der Originale liegt im Ausschnitt und wird im Video von einer neuen Box überdeckt:
    #   PT06: Box x 85-1400, y 900-1705   -> im Ausschnitt y minus 810
    #   PT01: Box x 1990-2915, y 900-1550 -> im Ausschnitt y minus 810
    cv2.imwrite(str(A / "foto_giessen.jpg"), pt06[810:2497, 0:3000], Q)
    cv2.imwrite(str(A / "foto_garten.jpg"), pt01[810:2497, 0:3000], Q)

    # Wohnzimmer-Foto (sauberer Rechteck-Ausschnitt innerhalb des großen Kreises von PT04)
    cv2.imwrite(str(A / "foto_wohnzimmer.jpg"), pt04[0:1740, 1640:3000], Q)

    # Runde Ortsbilder aus PT04: Quadrat innerhalb des gestrichelten Rings
    for name, (cx, cy) in {"garten": (1020, 300), "balkon": (895, 830), "kueche": (980, 1365), "bad": (1260, 1820)}.items():
        r = 188
        cv2.imwrite(str(A / f"ort_{name}.jpg"), pt04[cy - r:cy + r, cx - r:cx + r], Q)

    # Monstera-Blatt (Deko) als Alpha-Maske: liegt in PT04 unten links frei auf Beige
    reg = pt04[1630:2000, 70:410].astype(np.float32)
    bg = np.median(reg[:12].reshape(-1, 3), axis=0)
    dist = np.linalg.norm(reg - bg[None, None], axis=2)
    alpha = np.clip(dist / np.percentile(dist, 99), 0, 1)
    alpha[alpha < 0.12] = 0
    alpha = cv2.GaussianBlur((alpha * 255).astype(np.uint8), (0, 0), 0.7)
    rgba = np.dstack([np.full(alpha.shape + (3,), 255, np.uint8), alpha])
    ys, xs = np.where(alpha > 10)
    cv2.imwrite(str(A / "blatt.png"), rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1])
    print("ok", sorted(p.name for p in A.glob("*")))


if __name__ == "__main__":
    main()
