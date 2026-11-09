# Round R5, brief WP2: lattice sector

## Target
Develop the nuclear/lattice sector of the URF:
- the harmonic expansion of S_NN at all phonon orders;
- single phonon → multiphonon → impulse, including the coherent/incoherent crossover (cf. 2607.24933);
- the anharmonic expansion;
- polar couplings: dark photon via Born charges, ε_∞, LO–TO;
- the full q-vector anisotropy and daily modulation;
- nuclear-spin couplings into phonons;
- the Debye–Waller and Franck–Condon structure, consistent with the WP0 sum rules.

LIMITS assigned: L4, L5, L6, L18, L19 (lattice part).
Gaps assigned: G11 (lattice), G13, and the lattice side of G3 (deliver the multiphonon S_NN that WP5 needs).

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
  /home/user/dmdd-solid/literature/papers-WP2/. Verify every cited ID against the arXiv API, and delete PDFs at the end.
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine.
- Mark each step DERIVED (with hypotheses), ESTIMATED or CONJECTURED.
- Write the return to /home/user/dmdd-solid/returns/R5/WP2.md (≤ 500 lines) and scripts to /home/user/dmdd-solid/code/WP2/.
- Your final message is a summary of ≤ 15 lines.
