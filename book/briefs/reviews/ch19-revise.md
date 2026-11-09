# Chapter 19 revision (one reviser)
Revise tex/ch19/ch19.tex and s19-1.tex … s19-6.tex, s19-summary.tex and tex/appD/D-45.tex, the Ch19 rows of tex/appF/F-rows.tex, and the figscripts/ch19 scripts and figures they need. All paths are under /home/user/dmdd-solid/book.
Narrow edits are also allowed in tex/appE/E-11.tex (65 fs), E-23.tex ("lattice heat", ℓ_int, p_FP) and E-25.tex (ρ_g − 1 ≈ 0.25), and for the g_Luke rename wherever the Luke gain occurs outside Ch19 (grep). Re-read before each exact Edit.

Address every item in the five reports in ledgers/REVIEWS/ch19/ (derivation-1.md, derivation-2.md, prose.md, reader-a.md, reader-b.md). The rulings R1–R8 at the end of ledgers/REVIEWS/ch19/editor-notes.md bind you, as do the earlier items in that file that are addressed to the review. R1–R2 (the ε_eh/y_C recalibration of the 19.5 calibration chain, with every dependent number rerun) and R6 (moving the calibration machinery into 19.5) are the substantive items; do them first.

Follow:
- COMMON.md (compute policy: run only the light Python figscripts, no QE);
- PARTII.md and STYLE.md (Limit Check naming, boxed worked examples, no restating the master rate, prose patterns 18–26);
- REGISTER.md, including the connectives the prose review found nearly absent and the overused words;
- NOTATION.md and READER.md.

Register new symbols in NOTATION.md and resolve the clashes listed in R8.

Every number must appear in a script log. Rerun map13.py. Build privately with -outdir=/tmp/claude-0/build-ch19rev and get 0 LaTeX errors and 0 undefined citations. Write ledgers/REVIEWS/ch19/revision.md (item → done/how). Also list there every change that the campaign ledgers (state/CORRECTIONS.md, SOTA.md, LOOSE-ENDS, NOVELTY, DEFERRED-COMPUTE) need; do not edit them yourself. Do not commit. Final message ≤ 10 lines.
