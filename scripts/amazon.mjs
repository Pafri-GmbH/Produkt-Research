#!/usr/bin/env node
// scripts/amazon.mjs – Amazon.de-Daten für Ideen, Voranalyse und Deep-Dive.
//
// Aufruf:  node scripts/amazon.mjs <befehl> [argumente] [optionen]
//
// Befehle
//   suche "<keyword>" [--seiten N] [--node <id>]   Suchergebnisseite(n): Karten mit ASIN, Preis, Sterne, Bewertungen, Badges
//   produkt <ASIN> [<ASIN> ...]                     Produktseite: Preis, Sterne, Bewertungen, BSR, erhältlich seit, Verkäufer, Varianten
//   rezensionen <ASIN> [--kritisch] [--max N]       Rezensionen (Standard: alle Sterne, neueste zuerst)
//   bestseller <node-id> [--seiten N]               Bestseller-Liste einer Kategorie (Garten)
//   autocomplete "<prefix>"                         Amazon-Suchvorschläge
//   --selbsttest                                    Parser-Test ohne Netz
//
// Optionen
//   --json      Rohobjekt statt Markdown ausgeben
//   --frisch    Tages-Cache in data/raw/amazon/<datum>/ ignorieren
//   --cdp <url> Bestehenden lokalen Chrome nutzen (z. B. http://localhost:9222), statt headless zu starten
//   --sichtbar  Browser sichtbar starten (nur lokal sinnvoll)
//
// Exit-Codes: 0 ok · 1 Bedienfehler · 2 Amazon Captcha/Sperre · 3 Egress gesperrt (Allowlist) · 4 Playwright fehlt
//
// Regeln: nur lesen, kein Login, serielle Abrufe mit Pausen. Werte tragen die Quelle „Amazon.de, <Datum>".
// Absatz aus BSR wird hier nicht geschätzt – das macht die Analyse nach rules/quellen.md.

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, "..");
const RAW_DIR = path.join(REPO, "data", "raw", "amazon");
const BASE = "https://www.amazon.de";
const MARKETPLACE_DE = "A1PA6795UKMFR9";
const UA =
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36";
const MAX_SEITEN_SUCHE = 7;

const EXIT = { OK: 0, BEDIENUNG: 1, CAPTCHA: 2, EGRESS: 3, PLAYWRIGHT: 4 };

// ---------------------------------------------------------------------------
// Hilfsfunktionen (reine Funktionen, auch im Selbsttest genutzt)
// ---------------------------------------------------------------------------

export function heute() {
  return new Date().toISOString().slice(0, 10);
}

export function parseZahlDE(text) {
  // "1.234,56 €" → 1234.56 · "12.345" → 12345 · "4,3 von 5" → 4.3
  if (text == null) return null;
  const m = String(text).replace(/ /g, " ").match(/-?\d{1,3}(?:\.\d{3})*(?:,\d+)?|-?\d+(?:,\d+)?/);
  if (!m) return null;
  return Number(m[0].replace(/\./g, "").replace(",", "."));
}

export function parseSterne(text) {
  // "4,3 von 5 Sternen" → 4.3
  if (!text) return null;
  const m = String(text).match(/(\d(?:[.,]\d)?)\s*(?:von|out of)\s*5/i);
  return m ? Number(m[1].replace(",", ".")) : null;
}

export function parseBewertungen(text) {
  // "1.234 Bewertungen" / "(1.234)" / "1.234 Sternebewertungen" → 1234
  if (!text) return null;
  const m = String(text).replace(/ /g, " ").match(/(\d{1,3}(?:\.\d{3})+|\d+)\s*(?:Bewertung|Sternebewertung|global|\)|$)/i);
  return m ? Number(m[1].replace(/\./g, "")) : null;
}

export function parseBSR(text) {
  // "Nr. 1.234 in Garten (Siehe Top 100 in Garten) Nr. 12 in Gießkannen" → [{rang:1234,kategorie:"Garten"},{rang:12,kategorie:"Gießkannen"}]
  if (!text) return [];
  const t = String(text).replace(/ /g, " ").replace(/\s+/g, " ");
  const out = [];
  const re = /Nr\.\s*([\d.]+)\s+in\s+([^()\n]+?)(?=\s*\(|\s+Nr\.|\s*$)/g;
  let m;
  while ((m = re.exec(t))) {
    out.push({ rang: Number(m[1].replace(/\./g, "")), kategorie: m[2].trim() });
  }
  return out;
}

export function parseErgebnisseCa(text) {
  // "1-48 von mehr als 1.000 Ergebnissen" / "1-16 von 237 Ergebnissen" → { ca: 1000, mehr_als: true }
  if (!text) return null;
  const t = String(text).replace(/ /g, " ");
  const m = t.match(/von\s+(mehr als\s+|über\s+)?([\d.]+)\s+Ergebnis/i);
  if (!m) return null;
  return { ca: Number(m[2].replace(/\./g, "")), mehr_als: Boolean(m[1]) };
}

export function parseDatumDE(text) {
  // "Rezension aus Deutschland vom 12. März 2026" → "2026-03-12"
  if (!text) return null;
  const monate = {
    januar: 1, februar: 2, märz: 3, maerz: 3, april: 4, mai: 5, juni: 6, juli: 7,
    august: 8, september: 9, oktober: 10, november: 11, dezember: 12,
  };
  const m = String(text).match(/(\d{1,2})\.\s*([A-Za-zäöüÄÖÜ]+)\s+(\d{4})/);
  if (!m) return null;
  const mon = monate[m[2].toLowerCase()];
  if (!mon) return null;
  return `${m[3]}-${String(mon).padStart(2, "0")}-${String(m[1]).padStart(2, "0")}`;
}

export function istCaptcha(html, titel) {
  const t = `${titel || ""}`.toLowerCase();
  const h = `${html || ""}`;
  return (
    t.includes("robot check") ||
    t.includes("bot check") ||
    /validateCaptcha/.test(h) ||
    /Geben Sie die angezeigten Zeichen/i.test(h) ||
    /Enter the characters you see below/i.test(h)
  );
}

export function zitat(wert, datum, einheit = "") {
  if (wert == null || wert === "") return "[fehlt]";
  return `${wert}${einheit} (Amazon.de, ${datum})`;
}

function schlaf(ms) {
  return new Promise((r) => setTimeout(r, ms));
}
function pause() {
  return schlaf(3000 + Math.floor(Math.random() * 3000));
}

function kuerzen(s, n) {
  if (!s) return s;
  const t = String(s).replace(/\s+/g, " ").trim();
  return t.length > n ? t.slice(0, n - 1) + "…" : t;
}

// ---------------------------------------------------------------------------
// Argumente
// ---------------------------------------------------------------------------

function parseArgs(argv) {
  const opts = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith("--")) {
      const key = a.slice(2);
      const next = argv[i + 1];
      if (["seiten", "node", "max", "cdp"].includes(key)) {
        opts[key] = next;
        i++;
      } else {
        opts[key] = true;
      }
    } else {
      opts._.push(a);
    }
  }
  return opts;
}

function usage() {
  const src = fs.readFileSync(fileURLToPath(import.meta.url), "utf8");
  const kopf = src.split("\n").slice(1).filter((l) => l.startsWith("//")).map((l) => l.replace(/^\/\/ ?/, ""));
  return kopf.join("\n").trim();
}

// ---------------------------------------------------------------------------
// Cache
// ---------------------------------------------------------------------------

function cacheDatei(befehl, key) {
  const safe = String(key).toLowerCase().replace(/[^a-z0-9äöüß]+/gi, "-").replace(/^-|-$/g, "").slice(0, 80);
  return path.join(RAW_DIR, heute(), `${befehl}-${safe}.json`);
}
function cacheLesen(datei, frisch) {
  if (frisch || !fs.existsSync(datei)) return null;
  try {
    return JSON.parse(fs.readFileSync(datei, "utf8"));
  } catch {
    return null;
  }
}
function cacheSchreiben(datei, obj) {
  fs.mkdirSync(path.dirname(datei), { recursive: true });
  fs.writeFileSync(datei, JSON.stringify(obj, null, 2));
}

// ---------------------------------------------------------------------------
// Browser
// ---------------------------------------------------------------------------

async function ladePlaywright() {
  try {
    return await import("playwright");
  } catch {
    try {
      const req = createRequire(import.meta.url);
      return req("/opt/node22/lib/node_modules/playwright");
    } catch {
      return null;
    }
  }
}

async function browserStarten(opts) {
  const pw = await ladePlaywright();
  if (!pw) {
    console.error("Playwright fehlt. Lokal: npm i -g playwright && npx playwright install chromium");
    process.exit(EXIT.PLAYWRIGHT);
  }
  if (opts.cdp) {
    // Bestehender lokaler Chrome: chrome --remote-debugging-port=9222
    const browser = await pw.chromium.connectOverCDP(opts.cdp);
    const context = browser.contexts()[0] || (await browser.newContext());
    const page = await context.newPage();
    return { browser, context, page, schliessen: async () => { await page.close().catch(() => {}); } };
  }
  const profil = path.join(RAW_DIR, ".profile");
  fs.mkdirSync(profil, { recursive: true });
  const launch = {
    headless: !opts.sichtbar,
    locale: "de-DE",
    userAgent: UA,
    extraHTTPHeaders: { "Accept-Language": "de-DE,de;q=0.9" },
    viewport: { width: 1366, height: 900 },
    args: ["--no-sandbox", "--disable-blink-features=AutomationControlled"],
  };
  if (!process.env.PLAYWRIGHT_BROWSERS_PATH && fs.existsSync("/opt/pw-browsers/chromium")) {
    launch.executablePath = "/opt/pw-browsers/chromium";
  }
  const context = await pw.chromium.launchPersistentContext(profil, launch);
  const page = context.pages()[0] || (await context.newPage());
  return { browser: null, context, page, schliessen: async () => { await context.close().catch(() => {}); } };
}

async function seiteLaden(page, url, versuch = 0) {
  let resp;
  try {
    resp = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  } catch (e) {
    const msg = String(e && e.message);
    if (/ERR_TUNNEL_CONNECTION_FAILED|ERR_PROXY|403|ERR_NAME_NOT_RESOLVED|ERR_CONNECTION/.test(msg)) {
      console.error(`amazon.de Egress gesperrt – Allowlist prüfen (${url})`);
      process.exit(EXIT.EGRESS);
    }
    throw e;
  }
  await page.waitForLoadState("networkidle", { timeout: 15000 }).catch(() => {});
  // Cookie-Consent einmalig
  const consent = page.locator("#sp-cc-accept");
  if (await consent.count()) {
    await consent.first().click({ timeout: 3000 }).catch(() => {});
    await schlaf(500);
  }
  const titel = await page.title().catch(() => "");
  const html = await page.content().catch(() => "");
  if (istCaptcha(html, titel) || (resp && resp.status() === 503)) {
    if (versuch === 0) {
      console.error("amazon.de zeigt Captcha – warte 10 s und versuche einmal erneut …");
      await schlaf(10000);
      return seiteLaden(page, url, 1);
    }
    console.error(`amazon.de Captcha/Sperre (${url})`);
    process.exit(EXIT.CAPTCHA);
  }
  return resp;
}

// ---------------------------------------------------------------------------
// Extraktion (läuft im Browser-Kontext, daher reines DOM-JS ohne Imports)
// ---------------------------------------------------------------------------

const EXTRACT_SUCHE = () => {
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, " ").trim() : null);
  const cards = [...document.querySelectorAll('[data-component-type="s-search-result"]')];
  const items = cards.map((el) => {
    const asin = el.getAttribute("data-asin") || null;
    const h2 = el.querySelector("h2");
    const link = el.querySelector("h2 a, a.a-link-normal.s-no-outline");
    const badges = [...el.querySelectorAll(".a-badge-text, [data-a-badge-type] .a-badge-label-inner")].map(txt).filter(Boolean);
    const alle = txt(el) || "";
    const bought = alle.match(/([\d.]+\s*(?:Tsd\.|\+)?\+?)\s*Mal (?:im|in den) letzten Monat gekauft/i);
    const review = el.querySelector('[aria-label$="Bewertungen"], [aria-label$="Bewertung"], a[href*="customerReviews"] span.s-underline-text, span.s-underline-text');
    return {
      asin,
      position: Number(el.getAttribute("data-index")) || null,
      titel: txt(h2),
      url: link && link.href ? link.href.split("/ref=")[0] : null,
      bild: (el.querySelector("img.s-image") || {}).src || null,
      preis_roh: txt(el.querySelector(".a-price:not([data-a-strike]) .a-offscreen")),
      listenpreis_roh: txt(el.querySelector(".a-price[data-a-strike] .a-offscreen")),
      sterne_roh: txt(el.querySelector(".a-icon-alt")) || (el.querySelector('[aria-label*="von 5"]') || {}).getAttribute?.("aria-label") || null,
      bewertungen_roh: review ? (review.getAttribute("aria-label") || txt(review)) : null,
      badges,
      gesponsert: /Gesponsert|Sponsored/.test(alle) || Boolean(el.querySelector(".puis-sponsored-label-text, [data-component-type='sp-sponsored-result']")),
      gekauft_letzter_monat: bought ? bought[0] : null,
      lieferung: txt(el.querySelector('[data-cy="delivery-recipe"]')),
    };
  });
  const next = document.querySelector("a.s-pagination-next:not(.s-pagination-disabled)");
  const cur = document.querySelector(".s-pagination-selected");
  const info = document.querySelector('[data-component-type="s-result-info-bar"]');
  return {
    seite: cur ? Number(cur.textContent.trim()) : 1,
    naechste_seite: next ? next.href : null,
    ergebnisse_roh: info ? info.textContent.replace(/\s+/g, " ").trim() : null,
    items,
  };
};

const EXTRACT_PRODUKT = () => {
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, " ").trim() : null);
  const q = (s) => document.querySelector(s);
  const details = {};
  document.querySelectorAll("#productDetails_detailBullets_sections1 tr, #productDetails_techSpec_section_1 tr, #productDetails_techSpec_section_2 tr").forEach((tr) => {
    const k = txt(tr.querySelector("th"));
    const v = txt(tr.querySelector("td"));
    if (k && v) details[k] = v;
  });
  document.querySelectorAll("#detailBullets_feature_div li, #detailBulletsWrapper_feature_div li").forEach((li) => {
    const t = txt(li);
    const m = t && t.match(/^(.+?)\s*[:‏:]\s*‎?\s*(.+)$/);
    if (m) details[m[1].replace(/[‎‏]/g, "").trim()] = m[2].replace(/[‎‏]/g, "").trim();
  });
  const bsrKey = Object.keys(details).find((k) => /Bestseller-Rang|Best Sellers Rank/i.test(k));
  const seitKey = Object.keys(details).find((k) => /Im Angebot von Amazon\.de seit|Date First Available/i.test(k));
  const gewichtKey = Object.keys(details).find((k) => /Artikelgewicht|Gewicht|Item Weight/i.test(k));
  const masseKey = Object.keys(details).find((k) => /Produktabmessungen|Abmessungen|Product Dimensions/i.test(k));
  const merchant = txt(q("#merchant-info")) || txt(q("#tabular-buybox")) || "";
  const bought = (txt(q("#social-proofing-faceout-title-tk_bought")) || "");
  const twister = [...document.querySelectorAll("#twister .a-row, #twister_feature_div .a-row, #variation_color_name, #variation_size_name")];
  const varianten = [...document.querySelectorAll("#twister li[data-defaultasin], #twister li[id^='color_name_'], #twister li[id^='size_name_'], #twister select option")].length;
  const reviews = [...document.querySelectorAll('#cm-cr-dp-review-list [data-hook="review"], [data-hook="review"]')].slice(0, 10).map((r) => ({
    datum_roh: txt(r.querySelector('[data-hook="review-date"]')),
    sterne_roh: txt(r.querySelector('[data-hook="review-star-rating"], [data-hook="cmps-review-star-rating"]')),
    titel: txt(r.querySelector('[data-hook="review-title"] span:not(.a-icon-alt):last-child, [data-hook="review-title"]')),
    text: txt(r.querySelector('[data-hook="review-body"]')),
    variante: txt(r.querySelector('[data-hook="format-strip"]')),
    verifiziert: Boolean(r.querySelector('[data-hook="avp-badge"]')),
  }));
  return {
    titel: txt(q("#productTitle")),
    marke: txt(q("#bylineInfo")),
    preis_roh: txt(q("#corePrice_feature_div .a-price:not([data-a-strike]) .a-offscreen")) || txt(q("#corePriceDisplay_desktop_feature_div .a-price:not([data-a-strike]) .a-offscreen")) || txt(q(".a-price:not([data-a-strike]) .a-offscreen")),
    listenpreis_roh: txt(q("#corePriceDisplay_desktop_feature_div .basisPrice .a-offscreen")) || txt(q(".a-price[data-a-strike] .a-offscreen")),
    sterne_roh: (q("#acrPopover") || {}).getAttribute?.("title") || txt(q("#acrPopover .a-icon-alt")),
    bewertungen_roh: txt(q("#acrCustomerReviewText")),
    bsr_roh: bsrKey ? details[bsrKey] : txt(q("#SalesRank")),
    erhaeltlich_seit: seitKey ? details[seitKey] : null,
    gewicht: gewichtKey ? details[gewichtKey] : null,
    masse: masseKey ? details[masseKey] : null,
    verkaeufer: merchant || null,
    fba: /Versand durch Amazon|Verkauf durch Amazon|Amazon\.de/.test(merchant) || null,
    varianten_anzahl: varianten || (twister.length ? twister.length : 0),
    bilder_anzahl: document.querySelectorAll("#altImages li.imageThumbnail, #altImages li.item").length || null,
    aplus: Boolean(q("#aplus, #aplus_feature_div")),
    bullets: [...document.querySelectorAll("#feature-bullets li span.a-list-item")].map(txt).filter(Boolean).slice(0, 8),
    gekauft_letzter_monat: bought || null,
    kategorie_pfad: [...document.querySelectorAll("#wayfinding-breadcrumbs_feature_div a")].map(txt).filter(Boolean),
    rezensionen_dp: reviews,
    details,
  };
};

const EXTRACT_REZENSIONEN = () => {
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, " ").trim() : null);
  const list = [...document.querySelectorAll('[data-hook="review"]')].map((r) => ({
    datum_roh: txt(r.querySelector('[data-hook="review-date"]')),
    sterne_roh: txt(r.querySelector('[data-hook="review-star-rating"], [data-hook="cmps-review-star-rating"]')),
    titel: txt(r.querySelector('[data-hook="review-title"] span:not(.a-icon-alt):last-child, [data-hook="review-title"]')),
    text: txt(r.querySelector('[data-hook="review-body"]')),
    variante: txt(r.querySelector('[data-hook="format-strip"]')),
    verifiziert: Boolean(r.querySelector('[data-hook="avp-badge"]')),
  }));
  const next = document.querySelector("li.a-last a");
  const login = /ap\/signin/.test(location.href) || Boolean(document.querySelector("#ap_email, form[name='signIn']"));
  return { rezensionen: list, naechste_seite: next ? next.href : null, login_noetig: login };
};

const EXTRACT_BESTSELLER = () => {
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, " ").trim() : null);
  const items = [...document.querySelectorAll("#gridItemRoot, div[id^='p13n-asin-index-']")].map((el) => {
    const rank = txt(el.querySelector(".zg-bdg-text"));
    const a = el.querySelector("a.a-link-normal[href*='/dp/']");
    const m = a && a.href.match(/\/dp\/([A-Z0-9]{10})/);
    return {
      rang: rank ? Number(rank.replace("#", "")) : null,
      asin: m ? m[1] : null,
      titel: txt(el.querySelector("._cDEzb_p13n-sc-css-line-clamp-3_g3dy1, ._cDEzb_p13n-sc-css-line-clamp-4_2q2cc, .p13n-sc-truncate-desktop-type2, .p13n-sc-truncated")),
      preis_roh: txt(el.querySelector("._cDEzb_p13n-sc-price_3mJ9Z, .p13n-sc-price, .a-color-price")),
      sterne_roh: txt(el.querySelector(".a-icon-alt")),
      bewertungen_roh: txt(el.querySelector(".a-size-small[aria-hidden], a[title] span.a-size-small")),
      url: a ? a.href.split("/ref=")[0] : null,
    };
  });
  const next = document.querySelector("li.a-last a");
  return { items, naechste_seite: next ? next.href : null };
};

// ---------------------------------------------------------------------------
// Normalisierung + Markdown
// ---------------------------------------------------------------------------

export function normSuchKarte(k) {
  return {
    asin: k.asin,
    position: k.position,
    titel: k.titel,
    url: k.url,
    bild: k.bild,
    preis: parseZahlDE(k.preis_roh),
    listenpreis: parseZahlDE(k.listenpreis_roh),
    sterne: parseSterne(k.sterne_roh),
    bewertungen: parseBewertungen(k.bewertungen_roh),
    badges: k.badges || [],
    amazons_choice: (k.badges || []).some((b) => /Amazon's Choice|Amazon’s Choice|Tipp/i.test(b)),
    bestseller: (k.badges || []).some((b) => /Bestseller/i.test(b)),
    gesponsert: Boolean(k.gesponsert),
    gekauft_letzter_monat: k.gekauft_letzter_monat,
    lieferung: k.lieferung,
  };
}

export function normProdukt(asin, p) {
  const bsr = parseBSR(p.bsr_roh);
  return {
    asin,
    url: `${BASE}/dp/${asin}`,
    titel: p.titel,
    marke: p.marke ? p.marke.replace(/^(Marke:|Besuche den|Besuchen Sie den)\s*/i, "").replace(/-Store$/i, "").trim() : null,
    preis: parseZahlDE(p.preis_roh),
    listenpreis: parseZahlDE(p.listenpreis_roh),
    sterne: parseSterne(p.sterne_roh),
    bewertungen: parseBewertungen(p.bewertungen_roh),
    bsr_haupt: bsr[0] || null,
    bsr_unter: bsr.slice(1),
    bsr_roh: p.bsr_roh || null,
    erhaeltlich_seit: p.erhaeltlich_seit,
    verkaeufer: p.verkaeufer,
    fba: p.fba,
    varianten_anzahl: p.varianten_anzahl,
    bilder_anzahl: p.bilder_anzahl,
    aplus: p.aplus,
    gewicht: p.gewicht,
    masse: p.masse,
    gekauft_letzter_monat: p.gekauft_letzter_monat,
    kategorie_pfad: p.kategorie_pfad,
    bullets: p.bullets,
    rezensionen_dp: (p.rezensionen_dp || []).map(normRezension),
  };
}

export function normRezension(r) {
  return {
    datum: parseDatumDE(r.datum_roh),
    sterne: parseSterne(r.sterne_roh),
    titel: r.titel,
    text: kuerzen(r.text, 600),
    variante: r.variante,
    verifiziert: Boolean(r.verifiziert),
  };
}

function euro(v) {
  return v == null ? "[fehlt]" : `${v.toFixed(2).replace(".", ",")} €`;
}
function z(v) {
  return v == null || v === "" ? "[fehlt]" : String(v);
}

function mdSuche(res, datum) {
  const l = [];
  l.push(`**Amazon.de Suche „${res.keyword}"** – Seite(n) ${res.seiten.map((s) => s.seite).join(", ")}, ${z(res.ergebnisse_roh)} (Amazon.de, ${datum})`);
  l.push("");
  l.push("| # | Marke / Titel (gekürzt) | ASIN | Preis | Sterne | Bewert. | Badges | Gesp. | Gekauft/Monat | abgerufen |");
  l.push("|---|---|---|---|---|---|---|---|---|---|");
  let i = 0;
  for (const s of res.seiten) {
    for (const k of s.items) {
      i++;
      l.push(`| ${i} | ${kuerzen(k.titel, 70)} | ${z(k.asin)} | ${euro(k.preis)} | ${z(k.sterne)} | ${z(k.bewertungen)} | ${k.badges.join(", ") || "–"} | ${k.gesponsert ? "ja" : "–"} | ${z(k.gekauft_letzter_monat)} | ${datum} |`);
    }
  }
  const org = res.seiten.flatMap((s) => s.items).filter((k) => !k.gesponsert && k.preis != null);
  if (org.length) {
    const preise = org.map((k) => k.preis).sort((a, b) => a - b);
    const bew = org.map((k) => k.bewertungen).filter((v) => v != null).sort((a, b) => a - b);
    l.push("");
    l.push(`Organisch ${org.length} Listings · Preisband ${euro(preise[0])} – ${euro(preise[preise.length - 1])} · Median ${euro(preise[Math.floor(preise.length / 2)])} · Bewertungen ${bew.length ? `${bew[0]} – ${bew[bew.length - 1]}, Median ${bew[Math.floor(bew.length / 2)]}` : "[fehlt]"} · gesponsert ${res.seiten.flatMap((s) => s.items).filter((k) => k.gesponsert).length} (Amazon.de, ${datum})`);
  }
  l.push("");
  l.push(`Rohdaten: ${path.relative(REPO, res._datei)}`);
  return l.join("\n");
}

function mdProdukt(p, datum) {
  const l = [];
  l.push(`**${z(p.titel)}** – ${p.url}`);
  l.push("");
  l.push("| Feld | Wert |");
  l.push("|---|---|");
  l.push(`| ASIN | ${p.asin} |`);
  l.push(`| Marke | ${zitat(p.marke, datum)} |`);
  l.push(`| Aktueller Preis | ${p.preis == null ? "[fehlt]" : zitat(euro(p.preis), datum)} |`);
  l.push(`| Listenpreis | ${p.listenpreis == null ? "–" : zitat(euro(p.listenpreis), datum)} |`);
  l.push(`| Bewertungsschnitt | ${zitat(p.sterne, datum)} |`);
  l.push(`| Anzahl Bewertungen | ${zitat(p.bewertungen, datum)} |`);
  l.push(`| BSR Hauptkategorie | ${p.bsr_haupt ? zitat(`Nr. ${p.bsr_haupt.rang} in ${p.bsr_haupt.kategorie}`, datum) : "[fehlt]"} |`);
  l.push(`| BSR Unterkategorie | ${p.bsr_unter.length ? zitat(p.bsr_unter.map((b) => `Nr. ${b.rang} in ${b.kategorie}`).join("; "), datum) : "[fehlt]"} |`);
  l.push(`| Erhältlich seit | ${zitat(p.erhaeltlich_seit, datum)} |`);
  l.push(`| Verkäufer / FBA | ${zitat(p.verkaeufer, datum)}${p.fba ? " · FBA" : ""} |`);
  l.push(`| Varianten | ${zitat(p.varianten_anzahl, datum)} |`);
  l.push(`| Bilder | ${zitat(p.bilder_anzahl, datum)} · A+ ${p.aplus ? "ja" : "nein"} |`);
  l.push(`| Maße / Gewicht | ${z(p.masse)} / ${z(p.gewicht)} |`);
  l.push(`| Gekauft letzter Monat | ${zitat(p.gekauft_letzter_monat, datum)} |`);
  l.push(`| Kategorie | ${(p.kategorie_pfad || []).join(" › ") || "[fehlt]"} |`);
  if (p.bullets && p.bullets.length) {
    l.push("");
    l.push("Bullets: " + p.bullets.map((b) => kuerzen(b, 120)).join(" · "));
  }
  if (p.rezensionen_dp && p.rezensionen_dp.length) {
    l.push("");
    l.push(`Rezensionen auf der Produktseite (${p.rezensionen_dp.length}):`);
    for (const r of p.rezensionen_dp) l.push(`- ${z(r.datum)} · ${z(r.sterne)}★ · ${kuerzen(r.titel, 60)} – ${kuerzen(r.text, 200)}`);
  }
  return l.join("\n");
}

function mdRezensionen(res, datum) {
  const l = [];
  l.push(`**Rezensionen ${res.asin}** (${res.filter}, ${res.rezensionen.length} gelesen${res.quelle === "dp" ? ", nur Produktseite – Rezensionsseiten erfordern Login" : ""}; Amazon.de, ${datum})`);
  l.push("");
  l.push("| Datum | Sterne | Titel | Text (gekürzt) | Variante | Verifiziert |");
  l.push("|---|---|---|---|---|---|");
  for (const r of res.rezensionen) {
    l.push(`| ${z(r.datum)} | ${z(r.sterne)} | ${kuerzen(r.titel, 60)} | ${kuerzen(r.text, 220)} | ${z(r.variante)} | ${r.verifiziert ? "ja" : "–"} |`);
  }
  return l.join("\n");
}

function mdBestseller(res, datum) {
  const l = [];
  l.push(`**Bestseller Node ${res.node}** (${res.items.length} Einträge; Amazon.de, ${datum}) – ${res.url}`);
  l.push("");
  l.push("| Rang | ASIN | Titel (gekürzt) | Preis | Sterne | Bewert. |");
  l.push("|---|---|---|---|---|---|");
  for (const k of res.items) l.push(`| ${z(k.rang)} | ${z(k.asin)} | ${kuerzen(k.titel, 70)} | ${euro(k.preis)} | ${z(k.sterne)} | ${z(k.bewertungen)} |`);
  return l.join("\n");
}

function mdAutocomplete(res, datum) {
  return [`**Amazon-Autocomplete „${res.prefix}"** (Amazon.de, ${datum})`, "", ...res.vorschlaege.map((v) => `- ${v}`)].join("\n");
}

// ---------------------------------------------------------------------------
// Befehle
// ---------------------------------------------------------------------------

async function cmdSuche(opts) {
  const keyword = opts._[1];
  if (!keyword) return fehler("suche: Keyword fehlt");
  const seitenMax = Math.min(Number(opts.seiten || 1), MAX_SEITEN_SUCHE);
  const datei = cacheDatei("suche", `${keyword}${opts.node ? "-n" + opts.node : ""}-s${seitenMax}`);
  let res = cacheLesen(datei, opts.frisch);
  if (!res) {
    const b = await browserStarten(opts);
    try {
      res = { keyword, node: opts.node || null, datum: heute(), ergebnisse_roh: null, seiten: [] };
      let url = `${BASE}/s?k=${encodeURIComponent(keyword)}${opts.node ? `&rh=n%3A${opts.node}` : ""}`;
      const gesehen = new Set();
      for (let s = 1; s <= seitenMax && url; s++) {
        if (s > 1) await pause();
        await seiteLaden(b.page, url);
        const roh = await b.page.evaluate(EXTRACT_SUCHE);
        const items = roh.items.map(normSuchKarte).filter((k) => k.asin);
        const asins = items.map((k) => k.asin).join(",");
        if (!items.length && s === 1) {
          console.error("Keine Suchkarten gefunden – Seite prüfen (Interstitial/Captcha?).");
          process.exit(EXIT.CAPTCHA);
        }
        if (gesehen.has(asins)) break; // Amazon liefert Seite 1 bei Überlauf
        gesehen.add(asins);
        if (!res.ergebnisse_roh) res.ergebnisse_roh = roh.ergebnisse_roh;
        res.seiten.push({ seite: roh.seite || s, url, items });
        url = roh.naechste_seite;
      }
      res.ergebnisse_ca = parseErgebnisseCa(res.ergebnisse_roh);
    } finally {
      await b.schliessen();
    }
    cacheSchreiben(datei, res);
  }
  res._datei = datei;
  ausgabe(opts, res, () => mdSuche(res, res.datum));
}

async function cmdProdukt(opts) {
  const asins = opts._.slice(1).map((a) => a.toUpperCase()).filter((a) => /^[A-Z0-9]{10}$/.test(a));
  if (!asins.length) return fehler("produkt: mindestens eine gültige ASIN (10 Zeichen) angeben");
  const out = [];
  let b = null;
  try {
    for (let i = 0; i < asins.length; i++) {
      const asin = asins[i];
      const datei = cacheDatei("produkt", asin);
      let p = cacheLesen(datei, opts.frisch);
      if (!p) {
        if (!b) b = await browserStarten(opts);
        else await pause();
        await seiteLaden(b.page, `${BASE}/dp/${asin}`);
        const roh = await b.page.evaluate(EXTRACT_PRODUKT);
        p = normProdukt(asin, roh);
        p.datum = heute();
        cacheSchreiben(datei, p);
      }
      out.push(p);
    }
  } finally {
    if (b) await b.schliessen();
  }
  ausgabe(opts, out.length === 1 ? out[0] : out, () => out.map((p) => mdProdukt(p, p.datum)).join("\n\n---\n\n"));
}

async function cmdRezensionen(opts) {
  const asin = (opts._[1] || "").toUpperCase();
  if (!/^[A-Z0-9]{10}$/.test(asin)) return fehler("rezensionen: gültige ASIN angeben");
  const max = Number(opts.max || 20);
  const filter = opts.kritisch ? "critical" : "all_stars";
  const datei = cacheDatei("rezensionen", `${asin}-${filter}-${max}`);
  let res = cacheLesen(datei, opts.frisch);
  if (!res) {
    const b = await browserStarten(opts);
    try {
      res = { asin, filter: opts.kritisch ? "kritisch (1–3 Sterne)" : "alle Sterne", datum: heute(), quelle: "product-reviews", rezensionen: [] };
      let url = `${BASE}/product-reviews/${asin}?filterByStar=${filter}&sortBy=recent&reviewerType=all_reviews&pageNumber=1`;
      let seite = 0;
      while (url && res.rezensionen.length < max && seite < 10) {
        seite++;
        if (seite > 1) await pause();
        await seiteLaden(b.page, url);
        const roh = await b.page.evaluate(EXTRACT_REZENSIONEN);
        if (roh.login_noetig || (!roh.rezensionen.length && seite === 1)) {
          // Fallback: Rezensionsblock der Produktseite
          await pause();
          await seiteLaden(b.page, `${BASE}/dp/${asin}`);
          const dp = await b.page.evaluate(EXTRACT_PRODUKT);
          res.quelle = "dp";
          res.rezensionen = (dp.rezensionen_dp || []).map(normRezension);
          if (opts.kritisch) res.rezensionen = res.rezensionen.filter((r) => r.sterne != null && r.sterne <= 3);
          break;
        }
        res.rezensionen.push(...roh.rezensionen.map(normRezension));
        url = roh.naechste_seite;
      }
      res.rezensionen = res.rezensionen.slice(0, max);
    } finally {
      await b.schliessen();
    }
    cacheSchreiben(datei, res);
  }
  ausgabe(opts, res, () => mdRezensionen(res, res.datum));
}

async function cmdBestseller(opts) {
  const node = opts._[1];
  if (!node || !/^\d+$/.test(node)) return fehler("bestseller: numerische Node-ID angeben (z. B. 10925031)");
  const seitenMax = Math.min(Number(opts.seiten || 1), 2);
  const datei = cacheDatei("bestseller", `${node}-s${seitenMax}`);
  let res = cacheLesen(datei, opts.frisch);
  if (!res) {
    const b = await browserStarten(opts);
    try {
      const url0 = `${BASE}/gp/bestsellers/garden/${node}`;
      res = { node, url: url0, datum: heute(), items: [] };
      let url = url0;
      for (let s = 1; s <= seitenMax && url; s++) {
        if (s > 1) await pause();
        await seiteLaden(b.page, url);
        // Lazy-Loading: bis zum Seitenende scrollen
        for (let y = 0; y < 6; y++) {
          await b.page.mouse.wheel(0, 1500).catch(() => {});
          await schlaf(400);
        }
        const roh = await b.page.evaluate(EXTRACT_BESTSELLER);
        res.items.push(
          ...roh.items.filter((k) => k.asin).map((k) => ({
            rang: k.rang, asin: k.asin, titel: k.titel, url: k.url,
            preis: parseZahlDE(k.preis_roh), sterne: parseSterne(k.sterne_roh), bewertungen: parseBewertungen(k.bewertungen_roh),
          }))
        );
        url = roh.naechste_seite;
      }
    } finally {
      await b.schliessen();
    }
    cacheSchreiben(datei, res);
  }
  ausgabe(opts, res, () => mdBestseller(res, res.datum));
}

async function cmdAutocomplete(opts) {
  const prefix = opts._[1];
  if (!prefix) return fehler("autocomplete: Prefix fehlt");
  const datei = cacheDatei("autocomplete", prefix);
  let res = cacheLesen(datei, opts.frisch);
  if (!res) {
    const b = await browserStarten(opts);
    try {
      await seiteLaden(b.page, `${BASE}/`);
      const url = `https://completion.amazon.de/api/2017/suggestions?mid=${MARKETPLACE_DE}&alias=aps&lop=de_DE&prefix=${encodeURIComponent(prefix)}&limit=11`;
      const json = await b.page.evaluate(async (u) => {
        const r = await fetch(u, { credentials: "include" });
        if (!r.ok) return { fehler: r.status };
        return r.json();
      }, url);
      if (json && json.fehler) {
        console.error(`Autocomplete-API antwortet ${json.fehler}`);
        process.exit(EXIT.CAPTCHA);
      }
      res = { prefix, datum: heute(), vorschlaege: (json.suggestions || []).map((s) => s.value).filter(Boolean) };
    } finally {
      await b.schliessen();
    }
    cacheSchreiben(datei, res);
  }
  ausgabe(opts, res, () => mdAutocomplete(res, res.datum));
}

function ausgabe(opts, obj, md) {
  if (opts.json) {
    const clone = JSON.parse(JSON.stringify(obj, (k, v) => (k === "_datei" ? undefined : v)));
    process.stdout.write(JSON.stringify(clone, null, 2) + "\n");
  } else {
    process.stdout.write(md() + "\n");
  }
}

function fehler(msg) {
  console.error(msg);
  console.error("");
  console.error(usage());
  process.exit(EXIT.BEDIENUNG);
}

// ---------------------------------------------------------------------------
// Selbsttest (ohne Netz): Parser gegen feste Proben
// ---------------------------------------------------------------------------

function selbsttest() {
  const faelle = [
    ["parseZahlDE 1.234,56 €", parseZahlDE("1.234,56 €"), 1234.56],
    ["parseZahlDE 12,99 €", parseZahlDE("12,99 €"), 12.99],
    ["parseZahlDE null", parseZahlDE(null), null],
    ["parseSterne", parseSterne("4,3 von 5 Sternen"), 4.3],
    ["parseSterne en", parseSterne("4.5 out of 5 stars"), 4.5],
    ["parseBewertungen 1.234", parseBewertungen("1.234 Bewertungen"), 1234],
    ["parseBewertungen klammer", parseBewertungen("(632)"), 632],
    ["parseBewertungen Sternebew.", parseBewertungen("2.510 Sternebewertungen"), 2510],
    ["parseBSR haupt", parseBSR("Nr. 1.234 in Garten (Siehe Top 100 in Garten) Nr. 12 in Gießkannen")[0], { rang: 1234, kategorie: "Garten" }],
    ["parseBSR unter", parseBSR("Nr. 1.234 in Garten (Siehe Top 100 in Garten) Nr. 12 in Gießkannen")[1], { rang: 12, kategorie: "Gießkannen" }],
    ["parseBSR leer", parseBSR(null), []],
    ["parseErgebnisseCa mehr als", parseErgebnisseCa("1-48 von mehr als 1.000 Ergebnissen für „gießkanne“"), { ca: 1000, mehr_als: true }],
    ["parseErgebnisseCa exakt", parseErgebnisseCa("1-16 von 237 Ergebnissen"), { ca: 237, mehr_als: false }],
    ["parseDatumDE", parseDatumDE("Rezension aus Deutschland vom 12. März 2026"), "2026-03-12"],
    ["parseDatumDE 3. Mai", parseDatumDE("Bewertet in Deutschland am 3. Mai 2025"), "2025-05-03"],
    ["istCaptcha ja", istCaptcha('<form action="/errors/validateCaptcha">', "Amazon.de"), true],
    ["istCaptcha nein", istCaptcha("<div>ok</div>", "Amazon.de: Gießkanne"), false],
    ["zitat", zitat(12.99, "2026-09-21", " €"), "12.99 € (Amazon.de, 2026-09-21)"],
    ["zitat fehlt", zitat(null, "2026-09-21"), "[fehlt]"],
    [
      "normSuchKarte",
      normSuchKarte({ asin: "B0002RL4NS", preis_roh: "29,95 €", sterne_roh: "4,6 von 5 Sternen", bewertungen_roh: "1.052", badges: ["Bestseller"], gesponsert: false }).bestseller,
      true,
    ],
    [
      "normProdukt bsr",
      normProdukt("B0002RL4NS", { bsr_roh: "Nr. 2.345 in Garten (Siehe Top 100 in Garten) Nr. 3 in Gießkannen", marke: "Besuche den blomus-Store", preis_roh: "29,95 €" }).bsr_haupt.rang,
      2345,
    ],
    ["normProdukt marke", normProdukt("B0002RL4NS", { marke: "Marke: blomus" }).marke, "blomus"],
  ];
  let ok = 0;
  for (const [name, ist, soll] of faelle) {
    const passt = JSON.stringify(ist) === JSON.stringify(soll);
    if (passt) ok++;
    console.log(`${passt ? "✓" : "✗"} ${name}${passt ? "" : `  ist=${JSON.stringify(ist)} soll=${JSON.stringify(soll)}`}`);
  }
  console.log(`${ok}/${faelle.length} Parser-Tests bestanden`);
  process.exit(ok === faelle.length ? 0 : 1);
}

// ---------------------------------------------------------------------------
// main
// ---------------------------------------------------------------------------

const istHauptmodul = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (istHauptmodul) {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.selbsttest) selbsttest();
  else if (opts.help || !opts._[0]) {
    console.log(usage());
    process.exit(opts.help ? 0 : EXIT.BEDIENUNG);
  } else {
    const befehle = { suche: cmdSuche, produkt: cmdProdukt, rezensionen: cmdRezensionen, bestseller: cmdBestseller, autocomplete: cmdAutocomplete };
    const fn = befehle[opts._[0]];
    if (!fn) fehler(`Unbekannter Befehl: ${opts._[0]}`);
    else fn(opts).catch((e) => {
      console.error(`Fehler: ${e && e.message ? e.message : e}`);
      process.exit(1);
    });
  }
}
