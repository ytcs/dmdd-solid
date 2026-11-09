# Chapter 1 batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch01/s1-1.tex to s1-5.tex, /home/user/dmdd-solid/book/tex/appC/C-9.tex and /home/user/dmdd-solid/book/tex/appD/D-1.tex. Also read: /home/user/dmdd-solid/book/NOTATION.md, /home/user/dmdd-solid/book/STYLE.md, and the cited public sources (fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch01/, and delete the PDFs).

Check the following.
- Redo every non-definitional step from the previous line. Use sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited equation against the source, with page and equation number.
- Report factor-of-2, π, sign or convention drift against NOTATION.

Known items to rule on:
- v_min is written with an absolute value in 1.3, while D.1 has a sentence in signed form.
- Is the §1.4 benchmark σ̄_e = 3.0×10⁻³⁹ cm² right? Lin's text says ~10⁻³⁷.
- In §1.5: the Al gap (bulk 2Δ ≈ 0.36 meV from T_c, against 0.6 meV in films), and the toy rate in Worked example 1.7.
- In §1.1: the freeze-out estimate (2.2 vs 3 ×10⁻²⁶).
- Si numbers: a = 5.431 Å (CODATA); E_g(0) = 1.1692 eV (Ramanathan–Kurinsky Eq. (11)).

Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch01/derivation.md, ≤ 250 lines. For each equation or number give: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy. Do not edit the tex. Do not commit. Final message ≤ 10 lines.
