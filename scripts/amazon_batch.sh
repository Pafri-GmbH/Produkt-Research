#!/usr/bin/env bash
# Serielle Amazon.de-Abfragen für /ideenlauf und /ideen.
#
#   scripts/amazon_batch.sh <ausgabeordner> "<keyword>" ["<keyword>" …]          Suchseite 1 je Keyword
#   scripts/amazon_batch.sh <ausgabeordner> --autocomplete "<prefix>" [...]     Autocomplete je Prefix
#   scripts/amazon_batch.sh <ausgabeordner> --produkt <ASIN> [<ASIN> …]         Produktseite je ASIN
#
# Ruft scripts/amazon.mjs nacheinander auf (nie parallel, Amazon-Kadenz) und legt je Aufruf
# eine Textdatei im Ausgabeordner ab; die letzte Zeile jeder Datei ist "EXIT=<code>".
# Exit-Codes von amazon.mjs: 0 ok · 1 Bedienfehler · 2 Captcha/Sperre · 3 Egress gesperrt.
# Am Ende wird <ausgabeordner>/DONE geschrieben. Für lange Batches: nohup … & und auf DONE warten.
set -u
cd "$(dirname "$0")/.."

out="${1:?Ausgabeordner fehlt}"; shift
mkdir -p "$out"
rm -f "$out/DONE"

mode="suche"
case "${1:-}" in
  --autocomplete) mode="autocomplete"; shift ;;
  --produkt)      mode="produkt"; shift ;;
esac

for arg in "$@"; do
  key="$(echo "$arg" | tr ' /' '__' | tr -cd '[:alnum:]_äöüÄÖÜß-')"
  f="$out/${mode}_${key}.txt"
  timeout 170 node scripts/amazon.mjs "$mode" "$arg" > "$f" 2>&1
  code=$?
  echo "EXIT=$code" >> "$f"
  echo "$mode $arg → $f (EXIT=$code)"
  if [ "$code" -eq 2 ] || [ "$code" -eq 3 ]; then
    echo "amazon.mjs meldet Exit $code (Captcha/Egress) – Batch abgebrochen, Fallback-Quellen nutzen." >&2
    echo "ABBRUCH=$code" > "$out/DONE"
    exit "$code"
  fi
done
echo OK > "$out/DONE"
