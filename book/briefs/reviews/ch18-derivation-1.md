# Chapter 18 (part 1) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch18/ch18.tex, s18-1.tex, s18-2.tex, s18-3.tex, /home/user/dmdd-solid/book/tex/appD/D-43.tex, D-44.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch18/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch18 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch18/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch18/derivation-1.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch18/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently (sympy or a small script) and state the verdict. Cached data: figscripts/ch18, figscripts/ch10 si_elf_binned.npz, ch05 npz. PRIORITY: the impact-ionization kernel eq:18.1-ii, θ_ii, the LO double-count conditions, the backward equation and energy identity, the seed split (2.997 vs 2.712); D.43 moments and decomposition; D.44 renewal theory and the 0911.1532 misprints; the Fano decomposition 0.092+0.291−0.269 = 0.114 at E_g = 1.160 eV; the step-model overcount 5.9× and the TV thresholds (4.37, 12.95 eV), photon vs DM ≤ 0.062; the two Si parameter sets (18.1 vs 18.2/18.3) and their effect; b_N 0.345 vs 0.352.
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
