"""Verpackung ohne Badge + Schatten-Ebenen aus MAIN (NG0001).

Braucht assets/kanne.png (prep_cutout.py). Schreibt nach data/raw/listing/NG0001/assets/:
  main_b_rgb.png      MAIN ohne Badge, sonst unverändert (3000x3000, weißer Grund)
  kanne_schatten.png  Kanne + eigener Bodenschatten, transparent (für farbige Flächen)
  karton_szene.png    Verpackung + Kanne + Schatten, transparent
  *.json              Lage der Ausschnitte im 3000er-Original
"""
import json
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[4]
RAW = ROOT / "data/raw/listing/NG0001"
A = RAW / "assets"


def remove_badge(im: np.ndarray) -> np.ndarray:
    """Badge sitzt auf der linken Kartonseite (glattes Papier): Fläche aus den Zeilen darüber/darunter
    interpolieren, Papierkorn aus einem sauberen Streifen zurücklegen."""
    out = im.astype(np.float32)
    cx, cy, ax, ay = 333, 725, 208, 298
    x0, x1, y0, y1 = cx - ax - 12, cx + ax + 12, cy - ay - 12, cy + ay + 12
    top = out[y0 - 26:y0 - 4, x0:x1].mean(axis=0)          # (w,3)
    bot = out[y1 + 4:y1 + 26, x0:x1].mean(axis=0)
    top = cv2.GaussianBlur(top[None], (0, 0), 6)[0]
    bot = cv2.GaussianBlur(bot[None], (0, 0), 6)[0]
    t = np.linspace(0, 1, y1 - y0)[:, None, None]
    fill = (1 - t) * top[None] + t * bot[None]
    # Papierkorn: sauberer Streifen oberhalb, hochfrequenter Anteil, gespiegelt gekachelt
    patch = out[300:420, x0:x1]
    grain = patch - cv2.GaussianBlur(patch, (0, 0), 4)
    tiles = [grain if i % 2 == 0 else grain[::-1] for i in range((y1 - y0) // grain.shape[0] + 1)]
    grain = np.vstack(tiles)[: y1 - y0]
    fill = fill + grain
    yy, xx = np.mgrid[y0:y1, x0:x1]
    d = np.sqrt(((xx - cx) / ax) ** 2 + ((yy - cy) / ay) ** 2)
    m = np.clip((1.0 - d) / 0.035, 0, 1)[..., None]          # weiche Kante
    out[y0:y1, x0:x1] = m * fill + (1 - m) * out[y0:y1, x0:x1]
    return np.clip(out, 0, 255).astype(np.uint8)


def main() -> None:
    im = cv2.imread(str(RAW / "original/MAIN.png"))
    h, w = im.shape[:2]
    mb = remove_badge(im)
    cv2.imwrite(str(A / "main_b_rgb.png"), mb)

    # Produkt-Alpha auf volle Fläche legen
    kanne = cv2.imread(str(A / "kanne.png"), cv2.IMREAD_UNCHANGED)
    kx0, ky0, kx1, ky1 = json.loads((A / "kanne.json").read_text())["bbox"]
    a_prod = np.zeros((h, w), np.float32)
    a_prod[ky0:ky1, kx0:kx1] = kanne[..., 3] / 255.0

    # Karton-Silhouette: Schwellwert gegen Weiß, begrenzt durch Kanten-Polygon (unten liegt Schatten)
    mn = mb.min(axis=2)
    poly = np.array([(112, 190), (1935, 190), (1935, 1193), (1375, 1203), (940, 1216), (555, 1229),
                     (250, 1206), (112, 1193)], np.int32)
    clip = np.zeros((h, w), np.uint8)
    cv2.fillPoly(clip, [poly], 255, lineType=cv2.LINE_AA)
    box = ((mn < 247).astype(np.uint8) * 255)
    box = cv2.morphologyEx(box, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41)))
    box = cv2.bitwise_and(box, clip)
    box = cv2.GaussianBlur(cv2.erode(box, np.ones((3, 3), np.uint8)), (0, 0), 0.8)
    a_box = box.astype(np.float32) / 255.0

    # Schatten: außerhalb der Objekte ist alles Nicht-Weiße neutraler Schatten -> Schwarz mit Alpha
    gray = cv2.cvtColor(mb, cv2.COLOR_BGR2GRAY).astype(np.float32)
    a_sh = np.clip((252.0 - gray) / 252.0, 0, 1)
    obj = ((np.maximum(a_prod, a_box) > 0.02).astype(np.uint8)) * 255
    obj = cv2.dilate(obj, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    sh8 = (a_sh * 255).astype(np.uint8)
    small = cv2.resize(sh8, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    msmall = cv2.resize(obj, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_NEAREST)
    filled = cv2.inpaint(small, msmall, 6, cv2.INPAINT_TELEA)      # Schatten unter die Objektkanten fortsetzen
    filled = cv2.resize(filled, (w, h), interpolation=cv2.INTER_LINEAR)
    sh8 = np.where(obj > 0, filled, sh8)
    a_sh = cv2.GaussianBlur(sh8, (0, 0), 2.0).astype(np.float32) / 255.0
    a_sh[a_sh < 0.012] = 0
    # Kartonschatten läuft im Original links aus dem Bild: zum Rand hin ausblenden statt hart abschneiden
    ramp = np.clip(np.arange(w, dtype=np.float32) / 140.0, 0, 1)
    a_sh *= np.minimum(ramp, ramp[::-1])[None, :]

    def export(name, layers, zone=None):
        """layers: Liste (rgb float, alpha) von unten nach oben -> ein RGBA mit geradem Alpha."""
        acc_rgb = np.zeros((h, w, 3), np.float32)
        acc_a = np.zeros((h, w), np.float32)
        for rgb, a in layers:
            a = a if zone is None else a * zone
            acc_rgb = rgb * a[..., None] + acc_rgb * (1 - a[..., None])
            acc_a = a + acc_a * (1 - a)
        rgb = acc_rgb / np.maximum(acc_a[..., None], 1e-4)
        rgba = np.dstack([np.clip(rgb, 0, 255), acc_a * 255]).astype(np.uint8)
        ys, xs = np.where(rgba[..., 3] > 3)
        x0, x1, y0, y1 = max(xs.min() - 8, 0), min(xs.max() + 9, w), max(ys.min() - 8, 0), min(ys.max() + 9, h)
        cv2.imwrite(str(A / f"{name}.png"), rgba[y0:y1, x0:x1])
        (A / f"{name}.json").write_text(json.dumps({"bbox": [int(x0), int(y0), int(x1), int(y1)]}))
        print(name, rgba[y0:y1, x0:x1].shape, "bbox", (x0, y0, x1, y1))

    black = np.zeros((h, w, 3), np.float32)
    f = mb.astype(np.float32)
    # Kanne mit eigenem Bodenschatten (nur Bodenzone, nicht der Kartonschatten an der Spitze)
    zone = np.zeros((h, w), np.float32)
    zone[2380:, :] = 1.0
    zone = cv2.GaussianBlur(zone, (0, 0), 25)
    export("kanne_schatten", [(black, a_sh * zone), (f, a_prod)])
    export("karton_szene", [(black, a_sh), (f, a_box), (f, a_prod)])


if __name__ == "__main__":
    main()
