# App. E.14–E.27 (computational specifications) batch review: accuracy check, part 1 (isolated)
Under review: /home/user/dmdd-solid/book/tex/appE/E-14.tex to E-20.tex. These are specifications of deferred calculations, not results.
For each section, check the following:
- **Fidelity.** Every quantity, number, threshold, cost and acceptance test must agree with the research record: /home/user/dmdd-solid/state/DEFERRED-COMPUTE.md (the DC items listed in the matching SPINE row's writer-only list), /home/user/dmdd-solid/state/SOTA.md, /home/user/dmdd-solid/state/LOOSE-ENDS.md, and the SEAMS file /home/user/dmdd-solid/book/ledgers/SEAMS/E-*.md. Flag any number that contradicts the established state. One known case: E.14's "allowed (2̄00) zero-phonon line opens at ≈ 0.50 MeV". Check it against the SOTA zero-phonon edge of 0.405–0.408 MeV and the PAER onset of 0.333/0.337 MeV, and make sure the text distinguishes these quantities.
- **Physics and units.** Each displayed formula is dimensionally correct, and the stated method actually computes the stated quantity.
- **Executability.** Each specification is complete: inputs, codes, grids, convergence, acceptance tests and cost. List anything missing that a computational group would need.
- **No internal labels.** Grep for DC-, LE-, CW, WP, COMP-, [CALC] and the BANNED-TERMS.txt list.
- **Cited values.** Check them against fetchable sources, using /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-appE2/; delete the PDFs afterwards.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/appE2/accuracy-1.md, ≤ 220 lines: location → CHECKED / WRONG / GAP / MISSING, with the correction. Run no heavy computation. Do not edit the tex. Do not commit. Final message ≤ 10 lines.
