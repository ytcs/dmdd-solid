# Chapter 20 (part 2) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch20/ch20.tex, s20-4.tex, s20-5.tex, s20-summary.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch20/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch20 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch20/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch20/derivation-2.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch20/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently and state the verdict. Cached data: figscripts/ch20 (all .log files), ch10, ch05 npz. PRIORITY: the quasiparticle yield 2Δ/E below 4Δ (kinematic proof), the Kaplan cascade and its MC, the 0.590/0.600 values and the Guruswamy comparison; 20.5's collection kernels, the 𝔯_coll sign formula and the band (0.935–0.998; 1.04–1.09 from the second-film threshold) — recompute it with 20.4's logged near-gap yield instead of 20.5's linear ramp and report the shift; the three discrimination routes and their conditions (incl. dependence on 20.2's memory-loss times); the HV readout ceiling (1.22 central, 1.72 at 1σ, > 2 below 224 eV at 2σ); consistency of 𝔯_coll with 19.5 (collection-only needs 1.128); the summary and nuisance table against the final sections (the 20.2/20.4 paragraphs were drafted from SPINE).
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
