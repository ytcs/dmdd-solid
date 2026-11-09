# Chapter 12 (part 1) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch12/ch12.tex, s12-1.tex … s12-3.tex, /home/user/dmdd-solid/book/tex/appD/D-33.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch12/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch12 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch12/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch12/derivation-1.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item marked PRIORITY or 'for the Ch11 review' in ledgers/REVIEWS/ch12/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently (sympy or a small script) and state the verdict. Cached data: figscripts/ch12 (incl. osc12_4.py, ge_elf_binned.npz), figscripts/ch10 si_elf_binned.npz, ch05 npz. Rulings R9 (12.3 bracket) and R13 (12.6 sum rule, bremsstrahlung, scalar absorption) are PRIORITY.
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
