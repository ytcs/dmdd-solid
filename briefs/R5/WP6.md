# Round R5, brief WP6: rate assembly and uncertainty quantification

## Target
Develop the URF stage from responses and partition to the published exclusion curves:
- **Halo inputs.** The SHM and its parameter conventions; halo-independent formulations for ER and phonon
  channels; the exponential sensitivity at the kinematic edge.
- **Nuisance parameters.** A nuisance-parameter structure for every approximation level of WP0–WP5:
  functional, kernel, q_max, BO order, e–ph order, anharmonic order, temperature, yield model, Fano factor,
  E_g(T).
- **Statistical treatment.** Profile-likelihood or Bayesian propagation into exclusion bands. State how to
  publish and combine experiments with different codes and conventions.
- **Response library.** The data format of a shared, versioned response library: what tables, their
  axes, and their provenance.

LIMITS assigned: L24.
Gaps assigned: G4, G8.

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
  /home/user/dmdd-solid/literature/papers-WP6/. Verify every cited ID against the arXiv API, and delete PDFs at the end.
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine.
- Mark each step DERIVED (with hypotheses), ESTIMATED or CONJECTURED.
- Write the return to /home/user/dmdd-solid/returns/R5/WP6.md (≤ 500 lines) and scripts to /home/user/dmdd-solid/code/WP6/.
- Your final message is a summary of ≤ 15 lines.
