# Appendix E batch review: derivation check, part 1 (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/appE/E-1.tex to E-6.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the cited public sources. Fetch those with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-appE/ and delete the PDFs afterwards.
Check:
- every non-definitional step, redone from the previous line, with sympy for the algebra;
- dimensional analysis of every displayed result, and every limiting case the text claims;
- every number in the text and the worked examples, recomputed. Cost and flop estimates must be order-of-magnitude consistent. Silicon numbers must agree across sections: ε∞ = 11.7, gap 1.17 eV at low T, PBE ε∞ = 13.04;
- each cited value or equation, against its source;
- factor-of-2, π, sign or convention drift against NOTATION.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/appE/editor-notes.md that concerns your sections.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/appE/derivation-1.md, at most 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy (no DFT runs). Do not edit the tex. Do not commit. Final message at most 10 lines.
