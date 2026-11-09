# R10 brief WP7-T: low-temperature defect quantum kinetics (crowdions, defectons, tunnelling two-level systems)

## Target
Build the URF sector for defect quantum states and their kinetics at mK temperatures, in three roles.
1. **Pre-existing defects as targets.**
   - Tunnelling two-level systems (the standard tunnelling model; the strain and electric-dipole couplings)
     and defecton bands (Andreev–Lifshitz; delocalised vacancies and interstitials in quantum crystals, and
     light interstitials).
   - Give the DM response through WP0-v3 operators (density, strain via phonon operators, spin), weighted by
     the defect concentration.
   - Give rates and figures of merit, including amorphous layers and sensor films.
2. **Defect kinetics at mK.**
   - Quantum tunnelling of mobile defects (crowdions in metals such as Al, W and WSi; light interstitials;
     Frenkel-pair recombination), as opposed to classical Arrhenius kinetics.
   - Tunnelling-assisted annealing and recombination rates: formula, input parameters, and their
     temperature dependence at mK.
   - The energy released per event and its phonon/photon spectrum.
3. **Defect creation by DM.**
   - The interface to WP5-v3: the displacement thresholds, the configuration (crowdion, dumbbell,
     tetrahedral), and the stored energy.
   - Output a stored-energy distribution and a release-time kernel, to feed the WP7-E reconciliation.

Recover the standard tunnelling-model and Arrhenius forms as limits, quoted from full text.

## Authoritative inputs
- The architecture: /home/user/dmdd-solid/returns/R8/WP0-v3.md. Cite its equation numbers and do not re-derive it.
- Neighbouring refereed packages, as needed: /home/user/dmdd-solid/returns/R8/WP1-v3.md … WP6-v3.md.
- /home/user/dmdd-solid/CONVENTIONS.md and /home/user/dmdd-solid/NOTATION.md (v4 plus the R9 rows): follow them exactly.
- /home/user/dmdd-solid/state/CORRECTIONS.md: read it before quoting any return.
- /home/user/dmdd-solid/literature/CATALOG-A.md and CATALOG-B.md, for the catalog rows.
- /home/user/dmdd-solid/surveys/dm-solid-state-processes/README.md.

## Required for every item
- Truncation chain: state which WP0-v3 truncation (operator rows, sector, kernel rung, order) produces it.
- Formula: give the explicit target-response formula, DERIVED with its hypotheses.
- Literature limit: where a widely used formula exists, quote it from FULL TEXT (arXiv ID and equation
  number), show it as a limit, and give the leading correction. Add it to the list in "Proposed LIMITS
  rows".
- Computation specification: inputs, codes (or a new module), grids, convergence parameters, cost,
  outputs.
- If the item cannot be done: an exact remaining gap, saying why.
- Keep the DERIVED / ESTIMATED / CONJECTURED tags.

## Rules
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine. Put the checks in
  /home/user/dmdd-solid/code/WP7-T/checks.py, and they must pass.
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py, fetching into
  /home/user/dmdd-solid/literature/papers-WP7-T/. Verify every arXiv ID against the API. Delete the PDFs at the end.
- Write /home/user/dmdd-solid/returns/R10/WP7-T.md (≤ 550 lines). End with three sections: "Symbols introduced/used" (against
  NOTATION), "Interface flags" and "Proposed LIMITS rows".
- Do not edit any other file. Do not commit.
- Your final message is a summary of ≤ 15 lines.
