# DONE

**Deliverable and phases (user, 2026-11-01):** "just the book is fine for now. Once the book is done we'll look into actually carrying out all the deferred computational work, then expand/revise the book with the numerical results".
- Phase 1 (now): close all loose ends (state/LOOSE-ENDS.md), then write the book (theory, derivations, computational connection; Appendix E).
- Phase 2: run all deferred computations (specifications in the returns and Appendix E′; qe-rtsc fork, CMPMC on the user's compute).
- Phase 3: expand/revise the book with the numerical results.

Polarity: construct (derive and compute). There is no disproof campaign. A NO-GO is still a valid
return, for example "PAER is never leading in Si for any m_χ, because X", with its hypotheses stated.

## v2 (URF) done condition (2026-10-31)
- **Resolved (URF).** WP0–WP6 all returned and refereed (R×2 each). Every LIMITS.md entry is DERIVED or
  REFEREED, or carries an exact remaining gap. Every G1–G13 gap is closed by a formula plus a computation
  specification, or stated as an exact remaining gap. The deliverable is the book (book/SPINE.md); no separate framework paper.
- **Minimum budget for v2:** WP0 + one round of WP1–WP6 + one referee round per WP + synthesis.
- Tiers below refer to M1 (PAER).

## Return types
1. **Tier A resolved.** T1–T4 climbed rungs 1–5 below, the priority check is clean, and the M1 theory is written up
   in the book (Chap. 13); no separate LaTeX note.
2. **Tier B.** Tier A plus T5 numbers, with their uncertainty and inputs.
3. **Tier H.** Tier B plus T6 (production first-principles), with convergence tables and an independent
   recomputation.
4. **Exact remaining gap.** The strongest derived statement, plus the single missing step.

## Verification ladder (SKILL.md §7, adapted to a physics derivation)
1. **Concrete.** Every equation is derived, with its hypotheses. Each step is marked DERIVED, ESTIMATED or
   CONJECTURED. "Standard" is not a step: cite it or derive it.
2. **Control cases** (CONTROLS.md). The formula must visibly reduce to the known limits and must give zero
   where the physics says zero.
3. **Numerical sanity.** Units and dimensions are checked by script. The finite-difference amplitude
   agrees with the sum-over-states amplitude. The sum rules are checked numerically on a model.
4. **Hostile referees.** At least two, isolated from each other. Rubric:
   - a missing time ordering or exchange (hole) path;
   - Pauli blocking in intermediate states;
   - wrong Bose factors or spin factors;
   - phonon normalisation (√(1/2Mω) conventions, EPW g vs bare);
   - momentum conservation mod G (Umklapp);
   - double counting with first-order transitions and with zero-point renormalisation;
   - resonant denominators;
   - screening applied twice or not at all;
   - the dipole limit used outside its validity;
   - DM kinematics (v_esc, v_E, F_DM conventions, σ̄_e normalisation);
   - ionization threshold or yield assumptions;
   - sign of q (q enters as e^{+iq·r} or e^{−iq·r}).
5. **Independent re-derivation.** A fresh agent derives the formula from STATEMENT.md and NOTATION.md
   alone, by a different route (diagrammatic Kubo versus golden-rule perturbation theory). The two must
   agree term by term.
6. **Formalization.** Not applicable (a physics derivation). Rung 5 by two routes, plus numerical
   identities, replaces it.
7. **Attribution.** Cite the human papers combined: phonon-assisted optics, EPW, special displacements,
   DM–electron formalism. State that an LLM ran the campaign.

## Minimum budget
Three rounds before any return:
- R1: two isolated derivations, a literature priority check, and numerics;
- R2: two hostile referees, an independent re-derivation, and corrections;
- R3: the paper, plus a referee of the paper.
Tier H is pre-registered for a later round with remote compute.
