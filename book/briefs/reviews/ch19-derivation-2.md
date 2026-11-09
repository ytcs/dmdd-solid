# Chapter 19 (part 2) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch19/ch19.tex, s19-4.tex, s19-5.tex, s19-6.tex, s19-summary.tex, /home/user/dmdd-solid/book/tex/appD/D-45.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch19/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch19 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch19/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch19/derivation-2.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch19/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently and state the verdict. Cached data: figscripts/ch19 (all .log files), ch10, ch05 npz. PRIORITY: the displacement-count solver (0.70 vs NRT 0.8) and its MC; the stored-energy bounds 0.055/0.064 and their four conditions; the p_surv bounds vs the research returns; Ge E_d model-conditionality; the balance law eq:19.5-balance and D.45 (configurational E_st, ΔZPE, W_bias by Ramo); the heat ratio 1.407 and the 3.5 % release; the calibration identity; the exact bound and widening; the two-bias inversion; 𝔯_coll 1.154 vs 1.144 and the f_ion range; the 19.6a defecton diffusion closed form (T ≥ 0.28 band widths; low-T coefficient 2× Pushkarov) and the 19.6b Frenkel–Kontorova correction −a²/72d²; the summary and nuisance table against the final sections.
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
