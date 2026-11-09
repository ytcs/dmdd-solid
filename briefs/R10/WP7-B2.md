# R10 brief WP7-B2: lattice, spin, amorphous, defect and Migdal-absorption channels that so far sit only inside the master formula

## Target
Turn each of the following catalog rows into an explicit sector treatment. Catalog IDs refer to
literature/CATALOG-A.md.
- **L9 and S8** chiral phonons and single-molecule magnets (magnetic moments of chiral phonons; the
  coupling to DM spin operators).
- **L10 and A7** amorphous targets: configurational averaging of S_NN and of phonon absorption; the boson
  peak; the relation to WP2-v3.
- **L11** solid helium (quantum crystal; large zero-point motion; the harmonic expansion fails).
- **S2** boson absorption into magnons (Kittel and in-field modes, written out).
- **S5** phonons from the axion–nuclear-spin coupling (absorption form).
- **S6** spin responses from measured neutron-scattering data (a data-driven S with uncertainty).
- **D2** colour-centre creation (formation thresholds and yields; the interface to WP5-v3).
- **D5** bond breaking in molecular solids.
- **A4** single-phonon absorption, written out from WP0-v3 (3.5) with WP2-v3.
- **X10 and §10(iv)** Migdal-type effects in absorption (scalar–nucleon couplings).
- **§10(iii)** quadratic couplings scattering off density fluctuations in random media.

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
  /home/user/dmdd-solid/code/WP7-B2/checks.py, and they must pass.
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py, fetching into
  /home/user/dmdd-solid/literature/papers-WP7-B2/. Verify every arXiv ID against the API. Delete the PDFs at the end.
- Write /home/user/dmdd-solid/returns/R10/WP7-B2.md (≤ 550 lines). End with three sections: "Symbols introduced/used" (against
  NOTATION), "Interface flags" and "Proposed LIMITS rows".
- Do not edit any other file. Do not commit.
- Your final message is a summary of ≤ 15 lines.
