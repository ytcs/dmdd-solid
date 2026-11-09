# R10 brief WP7-D: extensions beyond single-vertex golden-rule rates

## Target
Extend the framework to the catalog's "not covered" (D) rows that are reachable, and state precisely why
the others stay outside.
1. **The coherent classical-field regime** (S4 nuclear-spin precession / CASPEr; S9 magnetoelectric axion
   coupling; A9 piezoelectric BAR/hBAR; §10(ii) oscillating constants, resonators and clocks).
   - Show how wave-like DM, a classical field with coherence time τ_c ~ 1/(m v²), driving the target maps
     onto the WP0-v3 retarded response R at q ≈ m v.
   - Cover both the absorbed power, and the coherent signal amplitude and its signal-to-noise ratio, as a
     function of the integration time against τ_c.
   - Show the golden-rule rate as the incoherent limit.
   - Give conditions, formulas and computation specifications.
2. **Fermionic absorption** (A10: DM + target → ν or another light fermion, plus a target excitation).
   - Add the missing operator class to the operator basis.
   - Give the rate in terms of the existing response functions, including the relativistic final-state
     phase space.
   - Recover the published formulas as limits.
3. **Two-insertion processes** (A11 pair absorption, dark Compton; §11.9 scattering plus mediator
   absorption).
   - Give the second-order formulas in the DM couplings and the response functions they need, e.g.
     three-point functions, and when they reduce to products of two-point functions.
4. **Out of scope, with reasons:**
   - D3 and D4, damage tracks and paleo-detectors. These are non-perturbative multiple scattering. Give the
     interface instead: the stopping power as the high-energy limit of the master formula, plus the
     hand-off to transport.
   - I2, DM-side radiative de-excitation. This has no target response.

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
  /home/user/dmdd-solid/code/WP7-D/checks.py, and they must pass.
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py, fetching into
  /home/user/dmdd-solid/literature/papers-WP7-D/. Verify every arXiv ID against the API. Delete the PDFs at the end.
- Write /home/user/dmdd-solid/returns/R10/WP7-D.md (≤ 550 lines). End with three sections: "Symbols introduced/used" (against
  NOTATION), "Interface flags" and "Proposed LIMITS rows".
- Do not edit any other file. Do not commit.
- Your final message is a summary of ≤ 15 lines.
