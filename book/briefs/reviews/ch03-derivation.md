# Chapter 3 batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch03/s3-1.tex … s3-6.tex, /home/user/dmdd-solid/book/tex/appC/C-1.tex … C-8.tex, /home/user/dmdd-solid/book/tex/appD/D-4.tex and D-5.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch03/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: numbers produced by the figures that are being regenerated in parallel (Figs. 3.6, 3.7, 3.8, 3.11, 3.12 and the Wannier spreads and interpolation errors of 3.6). Mark each such number "FIG-PASS" and do not check it; a short re-check follows the figure pass.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch03/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch03/derivation.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
