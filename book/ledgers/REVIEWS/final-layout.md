# Final layout pass: overfull boxes (2026-11-07)

Build: `cd tex && latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-fix main.tex`
(the outdir started as a copy of build-release).

Before: 54 overfull hboxes > 5 pt (largest s21-5 83 pt, s17-4 73 pt, D-28 72 pt, s8-6 55 pt; 20 at 18.7 pt
from the Ch7 running head).
After: 0 overfull > 5 pt (150 smaller ones remain, all <= 5 pt), 0 errors, 0 undefined citations or
references; latexmk settled. 1842 pages. Copied to `releases/book-full.pdf`.

No text, number, equation content or label was changed. TOC entries are unchanged.

## Global (preamble.tex)
- `\setcounter{biburl{num,uc,lc}penalty}{9000}`: long DOIs may break. Fixed bibliography overflows in
  Ch5 (24.5 pt), Ch8 (13.1 pt), App. D (13.1 pt).
- `\setlength{\emergencystretch}{1.5em}`: TeX's third pass, used only by paragraphs that would otherwise
  be overfull. Fixed paragraphs in s2-3, s3-6, s4-2, s15-4, D-18, D-27 (the "lines 83--1" entry), D-28 l.87.

## Running heads
- ch07/ch07.tex: `\chaptermark{Magnets, superconductors, Dirac materials, defects}` after `\chapter`
  (short head; the chapter title and TOC entry are unchanged). Fixed the 18.7/19.2 pt series (pp. 360-398).
- appD/D-5.tex, appD/D-40.tex: short section running head through a local `\sectionmark` override
  around `\section`, restored right after (heads: "Hohenberg--Kohn theorems and Kohn--Sham construction",
  "Absorption by current and spin current"). Fixed 5.6 pt and 2 x 45.8 pt.

## Displays and tables
| File | Was | Fix |
|---|---|---|
| ch02/s2-2.tex (WE 2.x hydrogen) | 16.4 pt | `split` at second `=` |
| ch02/s2-5.tex (WE oscillator) | 16.6 pt | `split` at second `=` |
| ch03/s3-5.tex (WE Z alpha) | 16.2 pt | `equation*` -> `gather*`, Si and Ge on two lines |
| ch04/s4-9.tex eq:4.9-kernels | 8.5 pt | `\qquad` -> `\quad` before p = k - k' |
| ch08/s8-6.tex eq:8.6-electronic | 23.5 pt | `gathered`, two relations on two lines |
| ch08/s8-6.tex eq:8.6-dyson | 55.2 pt | S^+ bracket broken onto a second aligned line |
| ch11/s11-7.tex (WE daily) | 17.3 pt | `multline*` after the second component |
| ch11/s11-9.tex nuisances | 28.9 pt | parenthetical (lambda_4) continued on a second row |
| ch17/s17-4.tex eq:17.4-Mmig | 73.2 pt | `split`, second line `\times v_kappa ...` |
| ch17/s17-5.tex tab:17-speeds | 42.4 pt | constants column p{0.40} -> p{0.29}\linewidth |
| ch21/s21-5.tex eq:21.5-recast | 83.1 pt | case conditions set as two-line `tabular` |
| ch21/s21-7.tex eq:21.7-pb210 | 8.6 pt | `split` at the final `=` |
| appD/D-3.tex eq:D.3-markov | 9.0 pt | `split` |
| appD/D-16.tex eq:D.16-frozen | 49.5 pt | `split` inside the bracket |
| appD/D-22.tex eq:D.22-eps | 14.4 pt | `split`; `\left[ \right]` -> `\biggl[ \biggr]` |
| appD/D-28.tex S^bin/C^cross | 72.2 pt | `equation*` -> `gather*` |
| appD/D-28.tex kick amplitude | 53.5 pt | `multline*` |
| appD/D-46.tex eq:D.46-defect | 5.1 pt | `split` at second `\le` |

## Inline formulas (`\allowbreak`)
- ch08/s8-6.tex l.67 (29.0 pt): before the electronic overlap.
- appD/D-11.tex l.104 (28.7 pt): after `[v_C(0)/V]`.
- appD/D-28.tex l.46 (15.7 pt): after `\Delta E_j` in the TRK element.

None left unfixed.
