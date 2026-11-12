#!/usr/bin/env bash
# Build the three volumes. Usage: ./build.sh [OUTDIR]   (default: build/)
# Each pass builds vol1, vol2 and vol3 with latexmk and then refreshes the cross-volume labels (tex/xref/);
# passes repeat until those labels stop changing. PDFs are left in OUTDIR; copy them to releases/ for a release.
set -u
here="$(cd "$(dirname "$0")" && pwd)"
out="$(mkdir -p "${1:-$here/build}" && cd "${1:-$here/build}" && pwd)"
python3 "$here/tools/split_B1.py" || exit 1
cd "$here/tex"
mkdir -p xref
for v in vol1 vol2 vol3; do [ -f "xref/$v.tex" ] || echo "% empty until the first build" > "xref/$v.tex"; done
status=0
for pass in 1 2 3 4; do
  for v in vol1 vol2 vol3; do
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir="$out" "$v.tex" > "$out/$v.latexmk.log" 2>&1 \
      || { echo "$v: latexmk failed (pass $pass), see $out/$v.log"; status=1; }
  done
  [ $status -eq 0 ] || break
  python3 "$here/tools/xref.py" "$out"; x=$?
  [ $x -eq 3 ] || break
done
for v in vol1 vol2 vol3; do
  [ -f "$out/$v.pdf" ] && printf '%s: %s pages, %s undefined references, %s undefined citations\n' "$v" \
    "$(pdfinfo "$out/$v.pdf" | awk '/^Pages/{print $2}')" \
    "$(grep -c 'Reference .* undefined' "$out/$v.log")" "$(grep -c 'Citation .* undefined' "$out/$v.log")"
done
python3 "$here/tools/floatsplit.py" "$out" || true
exit $status
