# Chapter 2 batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch02/s2-1.tex to s2-5.tex, /home/user/dmdd-solid/book/tex/appA/A-1.tex … A-9.tex, /home/user/dmdd-solid/book/tex/appD/D-2.tex and D-3.tex. Also read: /home/user/dmdd-solid/book/NOTATION.md, /home/user/dmdd-solid/book/STYLE.md, and the cited public sources (fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch02/, and delete the PDFs).

Check the following.
- Redo every non-definitional step from the previous line. Use sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited equation against the source, with page and equation number.
- Report factor-of-2, π, sign or convention drift against NOTATION.

Known items to rule on: everything listed in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch02/editor-notes.md. Also the new finding in the §2.2 limit box: for hydrogen 1s the Fermi-corrected plane wave reaches only 0.46 of the exact rate at 1 GeV, against Essig et al.'s "within 30%" for heavy atoms.

Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch02/derivation.md, ≤ 250 lines. For each equation or number give: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy. Do not edit the tex. Do not commit. Final message ≤ 10 lines.
