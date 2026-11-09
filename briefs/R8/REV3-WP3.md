# R8 correction brief REV3-WP3: WP3-v3, applying the R7 hostile review

## Inputs
- Your package: /home/user/dmdd-solid/returns/R6/WP3-v2.md and /home/user/dmdd-solid/code/WP3-v2/checks.py.
- Both referee reports: /home/user/dmdd-solid/referees/R7/REF-WP3-A.md and REF-WP3-B.md.
- Authoritative files: /home/user/dmdd-solid/CONVENTIONS.md, /home/user/dmdd-solid/NOTATION.md (v4) and /home/user/dmdd-solid/state/CORRECTIONS.md.
- /home/user/dmdd-solid/state/SOTA.md, the "R7 referee reports" section, for the coordinator's cross-package notes.
- Wait for nothing, but read /home/user/dmdd-solid/returns/R8/WP1-v3.md if it exists when you reach the window section. If it
  does not, use the referee estimates (Si zero-phonon exciton ≈ 0.40–0.43 MeV, allowed Umklapp 0.594 MeV;
  Ge ≈ 0.26–0.32 MeV), mark them [E], and flag them.
- Restate the M1 window honestly:
  - the strictly PAER-only window;
  - the region where PAER coexists with forbidden-class zero-phonon channels;
  - Ge.
- Settle the LA-kink disagreement (REF-A: LA forbidden on axis, exponent 4; REF-B: off-axis minima from
  anisotropic c_TA) with a symmetry analysis. Give final p̄_on values for WP6.
- Adopt the wider pair-screening envelope unless you derive the signs.

## Task
Produce /home/user/dmdd-solid/returns/R8/WP3-v3.md, standalone and corrected.
- **Address every verdict.**
  - FALLS: remove or replace the claim. If it can be repaired, give the repaired claim with a derivation.
  - STANDS WITH CORRECTION: apply the correction.
  - Rebuttal: if you think a referee is wrong, do not apply silently; rebut with an explicit derivation in
    a section "Rebuttals". Rebuttals go back to that referee.
- **Referee disagreements.** Where the two referees disagree, settle it with a derivation and state which
  one is right, and why.
- **Literature claims.** Keep only claims rated CONFIRMED against published papers. Drop REFUTED ones.
  Mark UNRESOLVED ones as such.
- **Closing table.** One row per referee item (A-#, B-#): applied / rebutted / dropped, and where.
- **Checks.** Copy checks.py to /home/user/dmdd-solid/code/WP3-v3/, fix any check the referees called vacuous or wrong, add
  checks for the new derivations, and run all of them: they must pass. Sympy only; no numerical
  simulation.
- **Notation.** Keep NOTATION v4 and CONVENTIONS. Flag any new symbol in "Symbols introduced/used".
- **Interfaces.** Flag every change that alters a quantity another package uses, in an "Interface flags"
  section.
- Do not edit any other file. Do not commit.

Your final message is a ≤ 12-line summary: counts applied / rebutted / dropped, the disagreements and how
they were settled, the interface flags, and the check results.
