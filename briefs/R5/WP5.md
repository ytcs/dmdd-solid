# Round R5, brief WP5: energy partition and measured quanta

## Target
Develop the URF stage from the final-state-resolved response (WP0 §7) to the measured quanta:
- **Hot carriers.** A Boltzmann/master-equation cascade with ab initio e–ph scattering (EPW), impact
  ionization (from the screened Coulomb interaction / GW), and plasmon decay, seeded by the response's
  distribution over (ε_e, ε_h, k_e, k_h), not by ω alone. Output: P(Q | ω, q, T) for Si, Ge, GaAs, and the
  Fano factor and ε_eh as moments.
- **Nuclear recoil.** The heat / defect / charge partition at eV–keV: the BO potential-energy surface,
  displacement thresholds, MD with electronic stopping, and how multiphonon S_NN hands over to it.
- **Quasiparticle yield** in superconductors.

LIMITS assigned: L20, L21, L22, L23.
Gaps assigned: G1, G3, G12 (defects and annealing; also the LEE-relevant stored-energy physics as a
background model).

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
  /home/user/dmdd-solid/literature/papers-WP5/. Verify every cited ID against the arXiv API, and delete PDFs at the end.
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine.
- Mark each step DERIVED (with hypotheses), ESTIMATED or CONJECTURED.
- Write the return to /home/user/dmdd-solid/returns/R5/WP5.md (≤ 500 lines) and scripts to /home/user/dmdd-solid/code/WP5/.
- Your final message is a summary of ≤ 15 lines.
