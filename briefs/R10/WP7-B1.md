# R10 brief WP7-B1: electronic, low-dimensional and molecular channels that so far sit only inside the master formula

## Target
Turn each of the following catalog rows from "covered by the master formula only" into an explicit
sector treatment. Catalog IDs refer to literature/CATALOG-A.md.
- **E5** Frenkel excitons in organic and molecular crystals (anisotropic molecular form factors; the
  relation to the BSE kernel ladder).
- **E8** exotic and low-dimensional plasmons: CDW plasmons, demon modes, Luttinger modes in 1D, 2D plasmons.
- **E9** heterostructures and layered stacks (the effective dielectric of a stack; the q_z dependence).
- **E10** quantum dots (a finite system inside a matrix; discrete transitions).
- **E12** graphene and carbon nanotubes (2D/1D Dirac with substrate screening, directionality).
- **X6** the Wannier-function and bremsstrahlung pictures of Migdal, as limits of WP3-v3 (W.5).
- **X8** Migdal electronic excitation without ionization (bound final states).
- **A2** absorption in superconductors and metals (the Holstein phonon-assisted process; Mattis–Bardeen
  relation; WP4-v3 consistency).
- **A6** dopant absorption (hydrogenic, k ≈ 0).
- **I3** inelastic DM–electron scattering (Δ_χ ≠ 0) in crystals.
- **I5** boosted and solar-reflected DM (relativistic projectile kinematics in the master formula; where
  the non-relativistic operator basis fails).

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
  /home/user/dmdd-solid/code/WP7-B1/checks.py, and they must pass.
- Literature: use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py, fetching into
  /home/user/dmdd-solid/literature/papers-WP7-B1/. Verify every arXiv ID against the API. Delete the PDFs at the end.
- Write /home/user/dmdd-solid/returns/R10/WP7-B1.md (≤ 550 lines). End with three sections: "Symbols introduced/used" (against
  NOTATION), "Interface flags" and "Proposed LIMITS rows".
- Do not edit any other file. Do not commit.
- Your final message is a summary of ≤ 15 lines.
