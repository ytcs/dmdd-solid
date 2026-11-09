# Chapter 14 (part 2) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch14/ch14.tex, s14-4.tex … s14-6.tex (no App. D file). Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch14/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch14 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch14/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch14/derivation-2.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch14/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently and state the verdict. Cached data: figscripts/ch14 (all .log files), ch10, ch05 npz. PRIORITY: the neutron no-go (q̂·S·q̂ unreachable) and C_sn(q, g) for Ni²⁺ (0.83, not 1.19) (14.4); the S^z_tot-conservation zero of R_{s^z𝒥}(0, ω≠0), the enantiomer difference, GaAs ⟨|L^ph|⟩ 0.124 vs 0.07 (Matas) — find the cause — and the Alves et al. Sect. III claim (14.5); the coherent-field formulas, the t_coh convention (1/(m v₀²) vs E.26), the Gaussian-field spectrum, and the 1.99 vs 2.7–10 fixed-amplitude factor (14.6). Check the nuisance table rows of 14.4/14.5 against those sections.
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
