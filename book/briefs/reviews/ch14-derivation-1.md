# Chapter 14 (part 1) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch14/ch14.tex, s14-1.tex … s14-3.tex, /home/user/dmdd-solid/book/tex/appD/D-38.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch14/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch14 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch14/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch14/derivation-1.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch14/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently (sympy or a small script) and state the verdict. Cached data: figscripts/ch14, figscripts/ch10 si_elf_binned.npz, ch05 npz. PRIORITY: the one-magnon response at full momentum transfer and the rate (14.1, D.38); the ΔS sum-rule bound and the NiO numbers (14.1/14.2 consistency); the magnetoelastic vs exchange-striction mixing claim and the YIG hybridization gap (14.2); the Larmor line, λ_S = g_J − 1 scope, the Kittel and AFMR weights, and the YIG worked example (14.3). Check that every Limit Check box number printed matches the chapter map.
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
