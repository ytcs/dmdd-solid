# Brief NOTATION-APPLY: campaign-wide conventions and symbol standardisation

## Target
Produce one authoritative convention set and one symbol table for the whole campaign, and an index mapping
every return's symbols onto it. The campaign rules apply:
- returns are the historical record and are NOT edited;
- renames inside returns are owed, not executed;
- one symbol for two objects is a defect.

## Deliverables
1. **/home/user/dmdd-solid/CONVENTIONS.md** (authoritative, overrides every return). Cover:
   - units, charge convention and Fourier conventions;
   - the sign of q and of ω, and the definition of n_q;
   - the normalisation of Bloch states and of ρ_mn;
   - the EPW g convention and phonon normalisation;
   - S, R, Π, ε and L definitions, with the FDT and spin factors;
   - the screening (proper / improper) and DM-side tensor conventions;
   - the halo conventions (2105.00599);
   - σ̄_e / F_DM;
   - the meaning of "Debye–Waller" (Franck–Condon e^{−2W} only) and of "sideband / ZPL / X0 / X+";
   - the truncation multi-index τ (WP0 §6);
   - the error-tag vocabulary.

   For each convention, give one sentence on why it was chosen. Where the campaign's returns disagree,
   decide, and record the disagreement.
2. **/home/user/dmdd-solid/NOTATION.md v3** (rewrite):
   - Start from WP0 §10 (NOTATION v2) and extend it with every symbol in all returns, referee reports and
     state files.
   - One row per symbol per meaning. Mark collisions ⚠ and give each colliding meaning a distinct name.
   - Include a "Returns" column listing where each symbol appears and under which local name.
3. **/home/user/dmdd-solid/state/CORRECTIONS.md**: an index of owed corrections, per return and per site. Include notation
   renames, and the substantive corrections already recorded in state/SOTA.md (W1–W5 from WP6, the WP5
   WP0 defects, the R2 referee corrections), so every reader is routed there before quoting a return.
4. **A consistency audit table.** For each key formula (master rate, S↔L conversion, ε₂^PA, M^{(2)}, M̃,
   halo factor, sum rules), check that all returns that state it agree once mapped to CONVENTIONS. List
   any residual disagreement as a defect for the coordinator.

## Read
Everything under /home/user/dmdd-solid except literature/papers*: STATEMENT, FRAMEWORK, LIMITS, NOTATION, CONTROLS, DONE,
RULES, state/*, returns/**, referees/**, and literature/L1.md.

## Rules
- Do not edit returns/ or referees/. Only write the three files above plus your report.
- Sympy checks are allowed for the consistency audit.
- Write a short report to /home/user/dmdd-solid/returns/R5/NOTATION-APPLY.md (≤ 150 lines) containing the audit table and the
  defects.
- Your final message is a summary of ≤ 15 lines.
