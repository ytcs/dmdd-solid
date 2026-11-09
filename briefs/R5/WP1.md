# Round R5, brief WP1: electronic sector (clamped nuclei)

## Target
Develop the clamped-nucleus electronic sector of the URF. Cover:
- the XC kernel ladder IP → RPA → RPA+LFE → TDDFT → BSE, as truncations of the WP0 response;
- excitons, including dark/indirect excitons and their selection rules at finite q;
- core and relativistic states (scalar-relativistic + SOC; the factorisation question raised by 2509.14534);
- non-density NR-EFT operators in-medium: the screening of spin and current channels and the transverse
  response;
- plasmons;
- anisotropy (the full q-vector response; modulation);
- homogeneous-electron-gas limits.

LIMITS assigned: L1, L2, L3, L10, L11, L14, L17 (with WP0), L19 (electronic part).
Gaps assigned: G5, G7, G10, G11 (electronic), and the exciton gaps in catalog-processes §12.

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
  /home/user/dmdd-solid/literature/papers-WP1/. Verify every cited ID against the arXiv API, and delete PDFs at the end.
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine.
- Mark each step DERIVED (with hypotheses), ESTIMATED or CONJECTURED.
- Write the return to /home/user/dmdd-solid/returns/R5/WP1.md (≤ 500 lines) and scripts to /home/user/dmdd-solid/code/WP1/.
- Your final message is a summary of ≤ 15 lines.
