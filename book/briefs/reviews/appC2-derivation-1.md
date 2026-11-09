# App. C.10–C.20 acceptance review, part 1: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/appC/C-10.tex to C-14.tex. These mathematical-tools sections were drafted with their chapters and reviewed only alongside them; this is their acceptance review. Also read /home/user/dmdd-solid/book/NOTATION.md, /home/user/dmdd-solid/book/STYLE.md and the SPINE.md App C rows (their "Used by" lists).
Check:
- Redo every step that is not a definition, with sympy; dimensional analysis on displayed results; every limiting case claimed; every numerical value recomputed.
- Each section supplies what its "Used by" chapters actually use: grep the \cref{app:C.n} and \cref{eq:C.n-...} uses in tex/ch*/ and check that the cited result exists here in the form and convention the chapter uses (sign, factor 2π, normalization). Flag any chapter citing a C result that is absent or different.
- Cited sources: check against fetchable sources with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-appC2/; delete PDFs afterwards.
- Notation drift against NOTATION (note: the kink width is being renamed d_kink in C.20 by a parallel edit; ignore that rename).
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/appC2/derivation-1.md, ≤ 220 lines: location → CHECKED / WRONG / GAP, with the correction. No heavy computation. Do not edit tex. Do not commit. Final message ≤ 10 lines.
