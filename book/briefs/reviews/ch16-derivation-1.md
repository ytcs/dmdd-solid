# Chapter 16 (part 1) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch16/ch16.tex, s16-1.tex, s16-2.tex, s16-3.tex, tex/appD/D-41.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch16/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch16 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch16/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch16/derivation-1.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch16/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently (sympy or a small script) and state the verdict. Cached data: figscripts/ch16, figscripts/ch10 si_elf_binned.npz, ch05 npz. PRIORITY: the Dirac ε_bg² / ε_bg overstatement (D.41), the lower bound (α/v_max)² = 7.6 and the reversed design rule; the ZrTe₅ ×4800–6600; the 0.63–0.72 recomputation gap (halo?); the exact two-layer in-plane response eq:16.2-inplane and its coefficient, and the real constant vs 2110.01587 Eq. (19); the nanotube ×4 / ×2.1 claim; graphene orthogonalization ×1.44/×1.84; hard-wall dots 0.70–1.03 and −9π/(8kR); Blanco Eq. (6) too large by μ/(4ω); the Hochberg Eq. (7) state count; graphene v_D 3.41e-3 vs 3.02e-3: recommend one.
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
