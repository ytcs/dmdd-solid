# Chapter 19 (part 1) batch review: derivation check (isolated)
You are the derivation verifier (long-form-writing SKILL.md §5). Under review: /home/user/dmdd-solid/book/tex/ch19/ch19.tex, s19-1.tex, s19-2.tex, s19-3.tex. Also read /home/user/dmdd-solid/book/NOTATION.md and /home/user/dmdd-solid/book/STYLE.md, and the public sources that are cited; fetch them with /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py into /home/user/dmdd-solid/book/sources/review-ch19/ and delete the PDFs afterwards.
Check the following.
- Redo every step that is not a definition from the previous line, using sympy for the algebra.
- Do dimensional analysis on every displayed result, and check every limiting case the text claims.
- Recompute every number in the text and the worked examples.
- Check each cited value or equation against its source.
- Report factor-of-2, π, sign or convention drift against NOTATION.
EXCLUDE: nothing; QE outputs are cached in figscripts/ch19 (npz, gaas_cache) — recompute numbers from them, do not run QE.
Known items: everything in /home/user/dmdd-solid/book/ledgers/REVIEWS/ch19/editor-notes.md that concerns your files.
Output /home/user/dmdd-solid/book/ledgers/REVIEWS/ch19/derivation-1.md, ≤ 250 lines: location → CHECKED / WRONG / GAP, with the correction. Run nothing heavy: no QE runs (the machine's compute is busy). Do not edit the tex. Do not commit. Final message ≤ 10 lines.
- PRIORITY: every item in ledgers/REVIEWS/ch19/editor-notes.md and ledgers/REVIEWS/partII/editor-notes.md for your sections; verify each independently (sympy or a small script) and state the verdict. Cached data: figscripts/ch19, figscripts/ch10 si_elf_binned.npz, ch05 npz. PRIORITY: the Wigner hand-over and the claim that classical propagation reproduces eq:11.4-IA (mean, width; misses c₃); the smooth-step threshold (σ_ω 0.72 eV; 1.6°); the Si regime boundaries and their m_χ; the partition identities; the binary threshold E_R,th = (M/m_e)E_g²/(16E_F) (352/399 eV; 336/387 with v_N²); the EPM promotable fraction; the Landau–Zener kernel and Born parameter ~15; the Migdal part of Y_q (3.9–4.4e-4); the Lindhard-equation solver and the 13 % soft-collision band (is the band honest?); the Bethe validity 1.84 v_F; the Si mean excitation energy (L shell 2/3).
- Any number traceable to campaign returns: check it against state/CORRECTIONS.md and SOTA.md, and flag any use of a superseded value.
- A parallel compute effort is posting results in state/DC-RESULTS.md and returns/R18/. If any of those bear on a number in your sections, compare them and report the difference; respect any quoting restriction stated in DC-RESULTS.md.
