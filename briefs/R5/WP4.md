# Round R5, brief WP4: spin, superconducting and special targets

## Target
Develop the URF sectors for:
- magnetic targets: magnons at linear spin-wave order, two-magnon continua, magnon–phonon coupling;
- chiral and circular-dichroism responses;
- superconductors and thin films: a broken-symmetry ground state, the BCS RPA with coherence factors, film
  geometry and disorder, branch-cut / causality issues (2101.08263), and quasiparticle generation;
- Dirac and narrow-gap materials;
- dopants and colour centres as final states (first-principles defect wavefunctions);
- exothermic/inelastic DM into collective modes (phonons, magnons).

LIMITS assigned: L13, L15, L16.
Gaps assigned: G9, G12 (electronic and dopant part), and the catalog-processes §12 gaps: two-magnon,
chiral/CD, dopant/NV final states, exothermic into collective modes.

## Read
- /home/user/dmdd-solid/STATEMENT.md, /home/user/dmdd-solid/FRAMEWORK.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/state/SOTA.md
- /home/user/dmdd-solid/returns/R4/WP0.md: the architecture. Cite its equation numbers, use its notation, and do not
  re-derive it. If you find an error in WP0, state it in a section "WP0 defects".
- /home/user/dmdd-solid/surveys/dm-solid-state-processes/README.md, plus the relevant sections of
  catalog-processes.md and catalog-analysis-and-gaps.md in that folder


## Required for every LIMITS entry assigned to you
- The source formula, quoted from FULL TEXT with its arXiv ID and equation number. Fetch with lit.py.
- The explicit truncation chain from the WP0 master formula.
- The validity conditions, with numbers for Si/Ge where possible.
- The leading correction the framework predicts beyond it.
- Any normalisation or convention discrepancy you find in the source.

## Required for every gap assigned to you
- The formula that closes it.
- The computation specification: inputs, codes such as QE/EPW/BerkeleyGW/phonopy/Yambo or a new module,
  grids, convergence parameters, cost scaling, outputs.
- Or, failing that, an exact remaining gap.

## Literature and rules
- Use /home/user/dmdd-solid/skills/breakthrough-maths/scripts/lit.py: arxiv; fetch <id> -o
  /home/user/dmdd-solid/literature/papers-WP4/. Verify every cited ID against the arXiv API, and delete PDFs at the end.
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine.
- Mark each step DERIVED (with hypotheses), ESTIMATED or CONJECTURED.
- Write the return to /home/user/dmdd-solid/returns/R5/WP4.md (≤ 500 lines) and scripts to /home/user/dmdd-solid/code/WP4/.
- Your final message is a summary of ≤ 15 lines.
