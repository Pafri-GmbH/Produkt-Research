"""Freisteller der Gießkanne aus MAIN (NG0001).

Eingabe:  data/raw/listing/NG0001/original/MAIN.png (3000x3000, Produkt vor Verpackung auf Weiß)
Ausgabe:  data/raw/listing/NG0001/assets/kanne.png  (RGBA, eng beschnitten)
          data/raw/listing/NG0001/assets/kanne.json (Bounding-Box im Original)

Das Produkt liegt im Original teils vor der Verpackung (Auslauf-Spitze, oberer Rand)
und auf einem weichen Bodenschatten. Deshalb drei Verfahren:
  - gegen reines Weiß: Schwellwert + Flood-Fill von außen
  - vor der Verpackung: Geometrie (Auslauf = zwei Geraden + Kappe, Rand = Ellipsenbogen)
  - am Boden: äußerste scharfe Kante je Strahl (Schatten ist weich, Kante hart)
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np
from scipy.ndimage import median_filter
from scipy.optimize import least_squares

ROOT = Path(__file__).resolve().parents[4]
RAW = ROOT / "data/raw/listing/NG0001"
WHITE = 247          # ab hier gilt ein Pixel als Hintergrund-Weiß
Y_CUT = 1390         # oberhalb davon liegt die Verpackung hinter dem Produkt
X_BOX_RIGHT = 1935   # rechts davon ist auch oben reines Weiß


def main() -> None:
    im = cv2.imread(str(RAW / "original/MAIN.png"))
    h, w = im.shape[:2]
    mn = im.min(axis=2)
    gray = cv2.GaussianBlur(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY), (0, 0), 1.2).astype(np.float32)

    # 1) Hintergrund per Flood-Fill (Rand, Dreieck Auslauf/Korpus, Grifföffnung)
    white = np.where(mn >= WHITE, 255, 0).astype(np.uint8)
    ff = white.copy()
    mask = np.zeros((h + 2, w + 2), np.uint8)
    for seed in [(5, 5), (w - 5, 5), (5, h - 5), (w - 5, h - 5), (900, 1800), (2480, 1850)]:
        if ff[seed[1], seed[0]] == 255:
            cv2.floodFill(ff, mask, seed, 128)
    fg = (ff != 128)

    # 2) Auslauf: Kanten aus Zeilen unterhalb der Verpackung, nach oben verlängert
    ys = np.arange(Y_CUT + 40, 2050, 10)
    left, right = [], []
    for y in ys:
        xs = np.where(mn[y, :1200] < WHITE)[0]
        left.append(xs[0])
        gaps = np.where(np.diff(xs) > 60)[0]          # Lücke bis zum Korpus
        right.append(xs[gaps[0]] if len(gaps) else xs[-1])
    kl, dl = np.polyfit(ys, left, 1)
    kr, dr = np.polyfit(ys, right, 1)
    xl = lambda y: kl * y + dl
    xr = lambda y: kr * y + dr
    cap = [(58, 1166), (61, 1162), (70, 1160), (100, 1159), (130, 1162), (160, 1167),
           (185, 1173), (203, 1179), (212, 1184)]
    spout = np.array(
        [(xl(Y_CUT + 20), Y_CUT + 20), (xl(1167), 1167)] + cap + [(xr(1190), 1190), (xr(Y_CUT + 20), Y_CUT + 20)],
        np.float32,
    )

    # 3) Oberer Rand: Ellipsenbogen, robust an Kantenpunkte angepasst
    px, py = [], []
    gy = np.abs(np.diff(gray, axis=0))
    for x in range(1400, 2270, 4):
        if x >= X_BOX_RIGHT:
            col = np.where(mn[1100:1400, x] < WHITE)[0]
            if len(col):
                px.append(x); py.append(1100 + col[0])
        else:
            col = gy[1140:1260, x]
            idx = np.where(col > 5.0)[0]
            if len(idx):
                px.append(x); py.append(1140 + idx[0] + 0.5)
    px, py = np.array(px, float), np.array(py, float)

    def rim(p, x):
        cx, a, cy, b, tilt = p
        t = np.clip(1 - ((x - cx) / a) ** 2, 0, None)
        return cy - b * np.sqrt(t) + tilt * (x - cx)

    fit = least_squares(lambda p: rim(p, px) - py, [1787, 520, 1300, 135, 0.0], loss="soft_l1", f_scale=2.0)
    p = fit.x
    # Korpus-Seitenkante links (Gerade aus Zeilen darunter)
    ys2 = np.arange(Y_CUT + 40, 1900, 10)
    bl = []
    for y in ys2:
        xs = np.where(mn[y, 1100:1500] < WHITE)[0]
        bl.append(1100 + xs[0])
    kb, db = np.polyfit(ys2, bl, 1)

    upper = np.zeros((h, w), np.uint8)
    cv2.fillPoly(upper, [np.round(spout * 16).astype(np.int32)], 255, lineType=cv2.LINE_AA, shift=4)
    # linke Ecke des Rands: dort verdeckt die Kartonkante die Kontur, Punkte aus der Vergrößerung abgelesen
    corner = np.array([(1293, 1245), (1297, 1234), (1303, 1225), (1312, 1216), (1330, 1208), (1350, 1203),
                       (1375, 1198), (1400, 1193), (1420, 1188.5)], float)
    xs_r = np.arange(1293, X_BOX_RIGHT + 1)
    ys_r = rim(p, xs_r.astype(float))
    left_part = xs_r <= 1420
    ys_r[left_part] = np.interp(xs_r[left_part], corner[:, 0], corner[:, 1])
    blend = (xs_r > 1420) & (xs_r <= 1480)                       # weicher Übergang zum Ellipsenbogen
    t = (xs_r[blend] - 1420) / 60.0
    ys_r[blend] = (1 - t) * (corner[-1, 1] + (ys_r[blend] - rim(p, 1420.0))) + t * ys_r[blend]
    body = [(kb * (Y_CUT + 20) + db, Y_CUT + 20)]
    for x, y in zip(xs_r, ys_r):
        if x >= kb * y + db:                 # rechts der Seitenkante
            body.append((x, y))
    body += [(X_BOX_RIGHT, Y_CUT + 20)]
    cv2.fillPoly(upper, [np.round(np.array(body, np.float32) * 16).astype(np.int32)], 255, lineType=cv2.LINE_AA, shift=4)

    alpha = np.where(fg, 255, 0).astype(np.uint8)
    zone = np.zeros((h, w), bool)
    zone[:Y_CUT, :X_BOX_RIGHT] = True
    alpha[zone] = upper[zone]
    # Übergangsstreifen: Geometrie und Schwellwert überlappen 20 px, dort Vereinigung
    alpha[Y_CUT:Y_CUT + 20, :X_BOX_RIGHT] = np.maximum(alpha[Y_CUT:Y_CUT + 20, :X_BOX_RIGHT], upper[Y_CUT:Y_CUT + 20, :X_BOX_RIGHT])

    # 4) Boden: Der Schatten ist neutralgrau und weich, die Bodenkante der Kanne hat einen warmen Saum.
    #    Je Strahl ab Zentrum: äußerster Punkt mit R-B > 8, danach Ausreißer verwerfen und glätten.
    blur = cv2.GaussianBlur(im, (0, 0), 1.5).astype(np.float32)
    warm = blur[..., 2] - blur[..., 0]
    c = np.array([1760.0, 2300.0])
    angles = np.deg2rad(np.arange(8, 172.01, 0.5))
    rs = np.arange(900, 150, -0.5)
    radii = []
    for a in angles:
        d = np.array([np.cos(a), np.sin(a)])
        pts = c[None, :] + rs[:, None] * d[None, :]
        ok = (pts[:, 0] >= 0) & (pts[:, 0] < w - 1) & (pts[:, 1] >= 0) & (pts[:, 1] < h - 1)
        prof = cv2.remap(warm, pts[ok, 0].astype(np.float32)[None], pts[ok, 1].astype(np.float32)[None], cv2.INTER_LINEAR)[0]
        hit = np.where(prof > 8.0)[0]
        radii.append(rs[ok][hit[0]] if len(hit) else np.nan)
    radii = np.array(radii)
    idx = np.arange(len(radii))
    good = ~np.isnan(radii)
    filled = np.interp(idx, idx[good], radii[good])
    med = median_filter(filled, size=41, mode="nearest")
    good &= np.abs(filled - med) < 10
    radii = np.interp(idx, idx[good], filled[good])
    radii = cv2.GaussianBlur(radii.astype(np.float32)[None], (0, 0), 3)[0] + 1.0
    poly = np.stack([c[0] + radii * np.cos(angles), c[1] + radii * np.sin(angles)], axis=1)
    base = np.zeros((h, w), np.uint8)
    closed = np.vstack([poly, [poly[-1, 0], c[1] - 50], [poly[0, 0], c[1] - 50]])
    cv2.fillPoly(base, [np.round(closed * 16).astype(np.int32)], 255, lineType=cv2.LINE_AA, shift=4)
    y_base = 2440
    zb = np.zeros((h, w), bool)
    zb[y_base:, 1050:2460] = True
    alpha[zb] = np.minimum(alpha[zb], base[zb])
    alpha[2505:, :1050] = 0
    alpha[2505:, 2460:] = 0

    # 5) Kante: 1 px einziehen, leicht weichzeichnen (kein weißer Saum auf farbigem Grund)
    alpha = cv2.erode(alpha, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
    alpha = cv2.GaussianBlur(alpha, (0, 0), 0.8)

    ysn, xsn = np.where(alpha > 8)
    x0, x1, y0, y1 = xsn.min(), xsn.max() + 1, ysn.min(), ysn.max() + 1
    pad = 6
    x0, y0, x1, y1 = max(x0 - pad, 0), max(y0 - pad, 0), min(x1 + pad, w), min(y1 + pad, h)
    rgba = np.dstack([im, alpha])[y0:y1, x0:x1]
    out = RAW / "assets"
    out.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out / "kanne.png"), rgba)
    (out / "kanne.json").write_text(json.dumps({"bbox": [int(x0), int(y0), int(x1), int(y1)], "rim_fit": [float(v) for v in p]}))
    print("kanne.png", rgba.shape, "bbox", (x0, y0, x1, y1), "rim", np.round(p, 2), "fit cost", round(float(fit.cost), 1))


if __name__ == "__main__":
    sys.exit(main())
