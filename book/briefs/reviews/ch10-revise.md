# Chapter 10 revision (one reviser)
Revise tex/ch10/ch10.tex and s10-1.tex … s10-10.tex (the Summary is at the end of s10-10), and tex/appD/D-29.tex and D-30.tex. In tex/ch08/s8-4.tex, change ONLY Table 8.3 (tab: screening classes) and the sentences that cite its last row. All paths are under /home/user/dmdd-solid/book.
Address every item of the five reports in ledgers/REVIEWS/ch10/ (derivation-1.md, derivation-2.md, prose.md, reader-a.md, reader-b.md) and of ledgers/REVIEWS/ch10/editor-notes.md, which binds you.
Follow COMMON.md (compute policy: rerun only the existing figscripts/ch10 Python scripts, no QE), PARTII.md, STYLE.md, REGISTER.md, NOTATION.md and READER.md.

## Editor rulings
1. **8.4 Table 8.3.** Split its last row into three:
   - transverse current: screened only through local fields;
   - spin current: unscreened;
   - 𝒯_e: head-screened, O(q²) at small q.
   This matches 10.4 and D.30 (verified twice).
2. **Verified corrections, stated as physics.**
   - **10.8:** the ALP dark-Compton correction. Add one sentence locating where the source goes wrong: its Eq. (16) integrates correctly, so the error enters between Eqs. (16) and (17).
   - **10.9 fermionic absorption:** firm up the wording. The free vertex underestimates by at least r (×1.7 for Xe 1s at 56.5 keV); only the (Zα)² correction has unknown sign. Apply this in 10.9, its open problems, lim:10.9c and 10.10.
   - **10.9 Cherenkov-like term:** describe it as the standard Cherenkov term of Fermi's energy-loss formula. Present it as new only in its application to boosted DM in silicon.
   - **W̄₅ and Im W̄₂:** they vanish exactly under PT in Si/Ge, and Catena's nonzero values are numerical. State this without polemic.
3. **Numbers.**
   - 2.5×10⁻³ (10.4);
   - Fermi factor 2.30 at 10 E_x^b (10.5);
   - 16.2 (WE 10.4);
   - 0.525 q₀ (10.1 box);
   - 7.09 keV (10.1);
   - |ε(3 eV)|²: one value book-wide, recomputed;
   - NaI exciton binding relative to GaAs: recompute (≈ 100×?);
   - the 10.2 physical gap is 1.17 eV;
   - the 77 K gap shift given as a number with a source (10.7);
   - the solar-core temperature citation (10.9);
   - Baryakhtar Eqs. (2.1), (2.2) and μ_M ≃ 2/Λ_d;
   - lim:10.9a: say q⁻² and |·| are restored, citing 1509.01598 Eq. (3.13);
   - WE 10-exo: "half-maximum edges".
4. **Rate reconciliation.**
   - 10.2: add a forward pointer to 10.10's reconciliation of 1.60 vs 1.36×10⁵, and state that 10.2's independent-particle rate uses a different table than 10.1.
   - 10.1: say that the small-q f-sum excess is partly unexplained.
   - 10.10: justify carrying the table spread onto the screened rate, or narrow it.
5. **Notation.**
   - Rename 𝒢_GS to a physics name, e.g. 𝒢_rel (also in NOTATION; E.16 goes to the App E pass-2 list).
   - Responses must not use χ (reserved for dark matter).
   - Resolve the bare Λ, K̄/K, ξ, script 𝒯 and n_g clashes (group index vs 𝔗 entry).
   - Propose rows in SEAMS for the ~30 missing symbols.
6. **Prose.**
   - Rewrite the chapter opening's middle sentences as argument; the prose review gives the replacement.
   - Give the flagged sections (10.1, 10.4, 10.9) short noun-phrase titles.
   - Cut the formulaic "truncation label" paragraph after limit boxes, the count-teasers, and project-plan wording ("acceptance test", core-hours, "until that library exists").
   - Make the 10.8 cuts (real-field paragraph, detector-geometry sentence).
   - Write "momentum transfer", not bare "transfer".
   - Define "polar group" and "pyroelectric".
   - Remove the triple statement of the normalization conversions.
   - Bring the connectives toward REGISTER ("however", "typical", "we can" up; "only", "of order" down), using the calibration rewrites in prose.md.
## Deliverables
- Revised files.
- A build in /tmp/build-ch10rev with 0 LaTeX errors and no undefined citations; undefined references only to unwritten targets.
- Lint clean, with no banned terms.
- ledgers/REVIEWS/ch10/revision.md (item → fix → location; declines with reasons).
- Updated SEAMS rows.
- Writers are drafting tex/ch11 in parallel; stay out of those files.
- Do not commit. Final message ≤ 12 lines.
