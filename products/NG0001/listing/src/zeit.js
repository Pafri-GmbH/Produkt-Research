// Zeitleiste für Videoszenen: alle Animationen laufen über die Web Animations API, sind pausiert
// und werden von window.__seek(sekunden) gesetzt. So rendert scripts/listing_render.mjs jeden Frame exakt.
const ANIM = [];
const WEICH = "cubic-bezier(.16,.84,.28,1)";

function anim(sel, keyframes, { t, d = 0.6, ease = WEICH, fill = "both" }) {
  const els = typeof sel === "string" ? document.querySelectorAll(sel) : [sel];
  els.forEach((el) => {
    const a = el.animate(keyframes, { delay: t * 1000, duration: d * 1000, easing: ease, fill });
    a.pause();
    ANIM.push(a);
  });
}

const ARTEN = {
  fade: [{ opacity: 0 }, { opacity: 1 }],
  hoch: [{ opacity: 0, transform: "translateY(46px)" }, { opacity: 1, transform: "none" }],
  links: [{ opacity: 0, transform: "translateX(-60px)" }, { opacity: 1, transform: "none" }],
  rechts: [{ opacity: 0, transform: "translateX(60px)" }, { opacity: 1, transform: "none" }],
  pop: [{ opacity: 0, transform: "scale(.72)" }, { opacity: 1, transform: "scale(1.04)", offset: 0.7 }, { opacity: 1, transform: "scale(1)" }],
  wischX: [{ clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0 0 0)" }],
  wischY: [{ clipPath: "inset(0 0 100% 0)" }, { clipPath: "inset(0 0 0 0)" }],
};

// Element erscheint zum Zeitpunkt t; mit staffel werden mehrere Treffer nacheinander eingeblendet
function rein(sel, t, art = "hoch", d = 0.6, staffel = 0) {
  document.querySelectorAll(sel).forEach((el, i) => anim(el, ARTEN[art], { t: t + i * staffel, d }));
}

// Szene: blendet ab `von` über die vorherige, verschwindet, sobald die nächste deckt
function szene(sel, von, bis, blende = 0.5) {
  const el = document.querySelector(sel);
  if (von > 0) anim(el, ARTEN.fade, { t: von, d: blende, ease: "ease-in-out" });
  if (bis != null) anim(el, [{ visibility: "visible" }, { visibility: "hidden" }], { t: bis + blende, d: 0.001, fill: "forwards", ease: "steps(1, end)" });
}

window.__seek = (sek) => {
  for (const a of ANIM) a.currentTime = sek * 1000;
  return new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
};
