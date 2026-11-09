# Chapter 15 (part 2) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch15/ch15.tex, s15-3.tex, s15-4.tex, s15-summary.tex, /home/user/dmdd-solid/book/tex/appD/D-40.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch15/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch15 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch15/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch15/derivation-2.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch15/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently and state the verdict. Cached data: figscripts/ch15 (all .log files), ch10, ch05 npz. PRIORITY: the thin-film sheet-screening factor [(ε_a+ε_b)/(q_∥d)]² (eq:15.3-sheet; 540 in WE 15.3); the dirty-film loss = ε₀ωρ_el and the ×24; the Lindhard function at ω+iγ_rel giving twice the Drude tail (vs Mermin); the Mattis–Bardeen dirty-limit ratio; the impurity- and phonon-assisted absorption derivations (D.40: Nambu amplitude collapse, case-I coherence factor, Allen and Hochberg–Lin–Zurek recovered); Limit Check 15.4a (11.4Δ); the summary nuisance table against the sections. The spin-current pair-breaking ALP claim is being checked separately (ledgers/REVIEWS/ch15/spincurrent-check.md); do not duplicate it, but report anything you notice.
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
