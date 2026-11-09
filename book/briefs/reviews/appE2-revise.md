# Appendix E.14–E.27 revision (one reviser)
Revise tex/appE/E-14.tex … E-27.tex and the Summary/opening in tex/appE/appE.tex. All paths are under /home/user/dmdd-solid/book.
Address every item in the four reports in ledgers/REVIEWS/appE2/ (accuracy-1.md, accuracy-2.md, prose.md and reader.md) and in ledgers/REVIEWS/appE2/editor-notes.md, which binds you, plus the App-E items in ledgers/REVIEWS/partII/editor-notes.md.
Follow COMMON.md (including the compute policy: run nothing), STYLE.md, REGISTER.md and NOTATION.md.

## Editor rulings
1. **Rewrite E.14** and break the recipe pattern everywhere.
   - Specifications are argued prose. Each subsection opens with why the quantity matters and what makes it hard, and lets the method, acceptance test and cost follow from that argument.
   - No form headings ("Inputs and codes", "Pitfalls"). Vary the structure across subsections.
   - Keep the summary tables of runs, grids, tests and costs; tables are fine.
2. **Remove project history.** Cut every sentence about the project's past ("has been computed once", "pre-registered", "the old 0.89", "was superseded"). A specification states what to compute, not what was done before.
3. **Make the cuts** to the prose report's word targets: E.14 ≈ 3,000 (≈ 3,600 if it absorbs E.26's GaAs Fano map, which you should do), E.20 ≈ 2,800, E.21 ≈ 2,350, E.22 ≈ 2,900, E.25 ≈ 3,700. Remove the duplications:
   - E.14 with E.5;
   - E.23 with E.11 (one set of numbers, kept in E.11);
   - E.24 with E.13;
   - E.25 with E.12;
   - the configurational-energy rule, stated once.
4. **One shared lattice setting.** PBE, SG15, 60 Ry, at the measured lattice constants (Si 5.431, Ge 5.658, GaAs 5.653 Å), as in App. E.1 and Ch. 5.
   - E.14 and E.17 must agree.
   - Cost each DFPT run once and point to that cost elsewhere.
   - The neutron acceptance test allows for PBE's TA softening (8 % at the measured a, Sect. 5.2); state the tolerance per branch.
5. **Fix every WRONG item** in the accuracy reports:
   - E.14 costs (200–300 and 80–240 core-h) and the onsets 0.3333/0.3375;
   - the E.15 TDA attribution, adding the pass test;
   - units in E.18 (eV⁻² per cell) and in E.17 (per cell versus per volume);
   - the G-vector count (≈ 725 for Si, 821 for Ge);
   - the GaAs scissor targets, all low-temperature, with the L-valley value from a cited source or stated without a value;
   - the E.23 order of magnitude;
   - U_rel in E.25;
   - the essig2016direct equation numbers (A.18)–(A.21).
6. **Fix the reader's items:**
   - wrong pointers (app:D.46 → the correct target or sec:21.2 text; E.4 → E.17; E.3 → E.6);
   - implausible costs (re-estimate E.16 storage and E.18/E.21 cost honestly, and say where a calculation must be restructured, e.g. stored on the fly or reduced in rank);
   - E.22's supercell series;
   - name every target (MOF, magnetoelectric crystal, molecular solids), or point to the section that names it;
   - consistent units of S.
7. **Fill the GAPs**:
   - E.24: the grid reaches the cap, A_AB is stated, and the Ge 77 K pair energy is given with a source or flagged as an input to measure;
   - acceptance tests for E.26's pair absorption and Barkas term;
   - the cosmic-ray spectra in E.27;
   - the NV⁻ cutoff and k grid;
   - the E.23 kernel grid;
   - the bond-breaking target;
   - colour-centre convergence;
   - define α̃ in E.20 and unify the ZrTe₅ value with 7.3 (α̃ = 0.20, g_deg = 2, unless the source says otherwise; state the source);
   - the relativistic-shift naming in E.15/E.16;
   - the Sternheimer-remainder caveat above 1.86 keV.
8. **Register.** Bring "however", "so", "only" and "must" toward REGISTER.md's frequencies. Use American spelling.
9. **Summary.** Extend the appendix Summary with the reviewer's two sentences covering E.14–E.27.
10. **Record alignment.** Update /home/user/dmdd-solid/state/DEFERRED-COMPUTE.md so that its DC rows match the revised text:
    - DC-1/5/6 window values: 0.407 MeV and the ≈ 0.50 MeV allowed-size edge, distinguished;
    - the DC-11/12/14 costs;
    - the flop count;
    - the G count.
    Add a dated note line at the top.

## Deliverables
- The revised files.
- A build in /tmp/build-appE2rev with 0 LaTeX errors and no undefined citations; undefined references only to unwritten targets.
- Lint clean (real hits only).
- ledgers/REVIEWS/appE2/revision.md, one row per item → fix → location, with a reason for each decline.
- Updated SEAMS E-e/f/g/h.md.
- Other agents edit tex/ch06, ch07 and the ledgers. Stay out of those.
- Do not commit. Final message ≤ 10 lines.
