# Chapter 22 (part 1) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch22/ch22.tex, s22-1.tex, s22-summary.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch22/ and delete the PDFs afterwards. Chapter 22 is a synthesis chapter: most of its numbers are quoted from Chapters 10–21, so consistency with the accepted text of those chapters is the main check.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples (figscripts/ch22 logs).
- Check each cited value or equation against its source, and each cross-chapter number against the cited chapter's tex.
- Report factor-of-2, π, sign or convention drift against NOTATION.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch22/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch22/derivation-1.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy (no QE). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: 22.1 (calculation programme, tab:22-calc): every number quoted from earlier chapters must match the ACCEPTED chapter text and the latest state/CORRECTIONS.md, SOTA.md and DC-RESULTS.md (including R19 FBC: ε_eh 4.15 eV, F 0.114, step model ~10× high; spin-current g_aee ≈ 6.1e-13; 𝔯_coll 0.81–1.02; Ch12 Migdal band ≥99.8 %). Check each channel's classification by limiting factor against the chapter it comes from. Check that the summary matches final 22.1/22.2/22.3 (the 22.1 paragraph was drafted early).
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value. Respect any quoting restriction in state/DC-RESULTS.md.
