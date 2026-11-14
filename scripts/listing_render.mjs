#!/usr/bin/env node
// Rendert Listing-Grafiken und Produktvideos aus HTML-Seiten (Playwright + ffmpeg).
//
//   node scripts/listing_render.mjs still <seite.html> <aus.png> [--size 3000x3000]
//   node scripts/listing_render.mjs frame <seite.html> <aus.png> --t 12.5 [--size 1920x1080]
//   node scripts/listing_render.mjs video <seite.html> <aus.mp4> --dauer 30 [--fps 30] [--size 1920x1080] [--jobs 4]
//
// <seite.html> relativ zum Repo-Root. Die Seite wird über einen lokalen Server aus dem Repo-Root
// geladen (Assets per absolutem Pfad, z. B. /data/raw/listing/NG0001/assets/kanne.png).
// Für frame/video muss die Seite window.__seek(sekunden) bereitstellen (siehe products/NG0001/listing/src/zeit.js):
// alle Animationen sind pausiert und werden je Frame auf den Zeitpunkt gesetzt – das Ergebnis ist reproduzierbar.

import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const MIME = {
  ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".mjs": "text/javascript",
  ".json": "application/json", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml", ".woff2": "font/woff2", ".woff": "font/woff",
};

async function ladePlaywright() {
  try {
    return await import("playwright");
  } catch {
    return createRequire(import.meta.url)("playwright");
  }
}

function args(argv) {
  const pos = [];
  const opt = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith("--")) opt[argv[i].slice(2)] = argv[++i];
    else pos.push(argv[i]);
  }
  return { pos, opt };
}

function server() {
  const srv = http.createServer((req, res) => {
    const rel = decodeURIComponent(new URL(req.url, "http://x").pathname);
    const file = path.join(ROOT, rel);
    if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
      res.writeHead(404).end("nicht gefunden: " + rel);
      return;
    }
    res.writeHead(200, { "content-type": MIME[path.extname(file).toLowerCase()] || "application/octet-stream" });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise((ok) => srv.listen(0, "127.0.0.1", () => ok(srv)));
}

async function oeffne(browser, url, w, h) {
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  const fehler = [];
  page.on("requestfailed", (r) => fehler.push(`Laden fehlgeschlagen: ${r.url()}`));
  page.on("response", (r) => { if (r.status() >= 400) fehler.push(`HTTP ${r.status()}: ${r.url()}`); });
  page.on("pageerror", (e) => fehler.push(`Skriptfehler: ${e.message}`));
  await page.goto(url, { waitUntil: "load" });
  await page.evaluate(async () => {
    await document.fonts.ready;
    await Promise.all([...document.images].map((i) => (i.complete ? i.decode().catch(() => {}) : new Promise((r) => { i.onload = i.onerror = r; }))));
    if (window.__bereit) await window.__bereit;
  });
  if (fehler.length) throw new Error(fehler.join("\n"));
  return page;
}

async function main() {
  const { pos, opt } = args(process.argv.slice(2));
  const [modus, seite, aus] = pos;
  if (!["still", "frame", "video"].includes(modus) || !seite || !aus) {
    console.error("Aufruf: listing_render.mjs still|frame|video <seite.html> <ausgabe> [--size BxH] [--t s] [--dauer s] [--fps n] [--jobs n]");
    process.exit(2);
  }
  const [w, h] = (opt.size || (modus === "still" ? "3000x3000" : "1920x1080")).split("x").map(Number);
  const { chromium } = await ladePlaywright();
  const srv = await server();
  const url = `http://127.0.0.1:${srv.address().port}/${seite.replace(/^\/+/, "")}`;
  const browser = await chromium.launch();
  fs.mkdirSync(path.dirname(path.resolve(aus)), { recursive: true });
  try {
    if (modus === "still") {
      const page = await oeffne(browser, url, w, h);
      await page.screenshot({ path: aus, type: "png" });
    } else if (modus === "frame") {
      const page = await oeffne(browser, url, w, h);
      await page.evaluate((t) => window.__seek(t), Number(opt.t || 0));
      await page.screenshot({ path: aus, type: "png" });
    } else {
      const fps = Number(opt.fps || 30);
      const dauer = Number(opt.dauer);
      if (!dauer) throw new Error("--dauer fehlt");
      const n = Math.round(dauer * fps);
      const jobs = Math.max(1, Number(opt.jobs || 4));
      const pages = await Promise.all(Array.from({ length: jobs }, () => oeffne(browser, url, w, h)));
      const ff = spawn("ffmpeg", [
        "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-c:v", "png", "-i", "-",
        "-vf", "scale=in_range=full:out_range=tv:out_color_matrix=bt709,format=yuv420p",
        "-c:v", "libx264", "-preset", "slow", "-crf", String(opt.crf || 16), "-profile:v", "high", "-level", "4.1",
        "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
        "-r", String(fps), "-movflags", "+faststart", aus,
      ], { stdio: ["pipe", "inherit", "inherit"] });
      const fertig = new Promise((ok, nok) => ff.on("close", (c) => (c === 0 ? ok() : nok(new Error("ffmpeg Exit " + c)))));
      const t0 = Date.now();
      for (let i = 0; i < n; i += jobs) {
        const bilder = await Promise.all(pages.map(async (page, k) => {
          const f = i + k;
          if (f >= n) return null;
          await page.evaluate((t) => window.__seek(t), f / fps);
          return page.screenshot({ type: "png" });
        }));
        for (const b of bilder) if (b && !ff.stdin.write(b)) await new Promise((r) => ff.stdin.once("drain", r));
        if (i % (fps * 5) < jobs) console.error(`  ${Math.min(i + jobs, n)}/${n} Frames, ${((Date.now() - t0) / 1000).toFixed(0)} s`);
      }
      ff.stdin.end();
      await fertig;
    }
    console.error("geschrieben:", aus);
  } finally {
    await browser.close();
    srv.close();
  }
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
