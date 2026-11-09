# Chapter 13 revision (one reviser)
Revise tex/ch13/ch13.tex and s13-1.tex … s13-9.tex (the Summary is at the end of s13-9), tex/appD/D-35.tex, D-36.tex and D-37.tex, the Ch13 rows of tex/appF/F-rows.tex, and the figscripts/ch13 scripts and figures they need. All paths are under /home/user/dmdd-solid/book.
Narrowly scoped edits are also allowed in tex/appE (the E.14, E.15 and E.16 lines named in the rulings), and in s6-5/s10-7 only to align the cold excitonic edge (R5). Re-read before each small exact Edit.

Address every item in the five reports in ledgers/REVIEWS/ch13/ (derivation-1.md, derivation-2.md, prose.md, reader-a.md, reader-b.md). The rulings R1–R10 at the end of ledgers/REVIEWS/ch13/editor-notes.md bind you, as do the earlier items in that file that are addressed to the review. R2 (the interim factor) is the one substantive item: do it first, put every input and assumption in interim13.py and its log, and report the range you arrive at.

Follow:
- COMMON.md (compute policy: run only the light Python figscripts, no QE);
- PARTII.md and STYLE.md (Limit Check naming, boxed worked examples, no restating the master rate, prose patterns 18–26);
- REGISTER.md, including the connectives the prose review found nearly absent and the overused words;
- NOTATION.md and READER.md.

Register new symbols in NOTATION.md and resolve the clashes the reports list (M^±, ς, x, s_Q, η, F(q), Γ̂, z_qp, W^{scr,R}, ω_TA(Q*)). Widen the M^± row to the three-argument dimensionless form.

Every number must appear in a script log. Rerun map13.py. Build privately with -outdir=/tmp/claude-0/build-ch13rev and get 0 LaTeX errors and 0 undefined citations. Write ledgers/REVIEWS/ch13/revision.md (item → done/how). Also list there every change that the campaign ledgers (state/CORRECTIONS.md, SOTA.md, LOOSE-ENDS, NOVELTY N7, CONTROLS C8) need; do not edit them yourself. Do not commit. Final message ≤ 10 lines.
