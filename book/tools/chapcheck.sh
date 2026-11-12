#!/usr/bin/env bash
# Compile one chapter or appendix alone, with its true number, and report errors and broken references.
# Usage: tools/chapcheck.sh ch10 [OUTDIR]     (also appA, appC, appD, appE, appF; OUTDIR defaults to /tmp/chapcheck-<name>)
# Labels of the rest of the book come from tex/xref/all.tex, written by the last full build (./build.sh), so a
# reference is reported as undefined only when its label exists nowhere. Citations are not resolved (no biber run).
# A label deleted since the last full build is still in all.tex: grep tex/ for a label before deleting it.
set -u
here="$(cd "$(dirname "$0")/.." && pwd)"
name="$1"; out="${2:-/tmp/chapcheck-$name}"; mkdir -p "$out"
case "$name" in
  ch*) n=$((10#${name#ch})); setup="\\mainmatter\\setcounter{chapter}{$((n-1))}";;
  appA) setup="\\appendix\\crefalias{chapter}{appendix}";;
  appC) setup="\\appendix\\crefalias{chapter}{appendix}\\setcounter{chapter}{2}";;
  appD) setup="\\appendix\\crefalias{chapter}{appendix}\\setcounter{chapter}{3}";;
  appE) setup="\\appendix\\crefalias{chapter}{appendix}\\setcounter{chapter}{4}";;
  appF) setup="\\appendix\\crefalias{chapter}{appendix}\\setcounter{chapter}{5}";;
  *) echo "unknown unit $name"; exit 2;;
esac
cat > "$here/tex/check-$name.tex" <<TEX
\\documentclass[11pt,twoside,openright]{book}
\\newcommand{\\xreffile}{xref/all.tex}
\\input{preamble}
\\volume{}{0}{}
\\begin{document}
$setup
\\input{$name/$name}
\\end{document}
TEX
cd "$here/tex"
for i in 1 2; do pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" "check-$name.tex" > "$out/run$i.txt" 2>&1; rc=$?; done
rm -f "check-$name.tex"
log="$out/check-$name.log"
echo "exit code: $rc; pages: $(grep -o 'Output written on .*' "$log" | grep -o '[0-9]* pages')"
grep -n '^!' -A6 "$log" | head -40
echo "undefined references: $(grep -c 'Reference .* undefined' "$log")"
grep 'Reference .* undefined' "$log" | sed 's/ on page.*//' | sort | uniq -c | head -40
echo "multiply defined labels: $(grep -c 'multiply defined' "$log")"
grep 'multiply defined' "$log" | head
echo "overfull hboxes > 5pt: $(grep -E 'Overfull \\hbox \(([5-9]|[0-9]{2,})\.' "$log" | wc -l)"
