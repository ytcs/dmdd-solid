# Chapter 18 (part 2) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch18/ch18.tex, s18-4.tex, s18-5.tex, s18-summary.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch18/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch18 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch18/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch18/derivation-2.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch18/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently and state the verdict. Cached data: figscripts/ch18 (all .log files), ch10, ch05 npz. PRIORITY: the A_AB = 5.674 calibration and Table 18.1 (Si F 0.114, 2.5σ; Ge −5 %, GaAs −6 %); the Klein-relation derivation, the 36–39 % uniform-population overstatement and the 0.65–84 window; the linear-law fit; the validated-range table; eq:18.5-Eg (captured electron raises non-pair energy by E_g); binomial thinning; the 0.56 % loss explaining 0.114 vs 0.119; the heat-based Fano F(1−E_x^b/E_g)²; unsplit excitons and r_𝓔 = 0.56 µm at 4 V/cm; the rate-equation solution; the summary and nuisance table against the final sections (the summary was drafted before 18.2–18.4 were final).
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
