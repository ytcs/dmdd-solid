# Round R5, brief WP3: mixed electron–lattice sector (non-adiabatic)

## Extra inputs
X1 and X2 have returned (returns/R3/X1.md, X2.md). Integrate them. Reconcile the WP0 eq. 4.9 control with X1's C7a–e, and the X2 screened amplitude M̃ with WP0 eqs 5.6–5.7. Both X1 and X2 are unrefereed: check them as you use them.

## Target
Develop the mixed sector of the URF from the WP0 BO / non-adiabatic expansion, in one consistent framework:
- all Migdal versions: the atomic sudden limit, the crystal ELF, the small-q EFT with phonon final states,
  and phonon-mediated Migdal;
- PAER (milestone M1). Take the refereed state from state/SOTA.md, and incorporate X1/X2 if their returns
  exist when you start (returns/R3/X1.md, X2.md). Otherwise state what they must deliver;
- phonon-assisted absorption;
- finite-T and zero-point renormalisation of electronic responses (AHC; the special-displacement /
  Zacharias–Giustino route as a stochastic evaluation);
- crystal NR bremsstrahlung;
- exciton–phonon replicas.

The central deliverable is a joint S(q; ω_ph, ω_e) for DM–nucleus and DM–electron couplings at a given BO
order. It must have consistent sum rules, with no double counting between multiphonon and Migdal or between
PAER and zero-phonon renormalisation, and it must show how each published Migdal formula is a truncation of
it.

LIMITS assigned: L7a, L7b, L7c, L7d, L8, L9, L9b (with WP1), L12.
Gaps assigned: G2, G6, the exciton–phonon part of G5, and crystal NR bremsstrahlung (catalog-processes §12).

## Read
- /home/user/dmdd-solid/STATEMENT.md, /home/user/dmdd-solid/FRAMEWORK.md, /home/user/dmdd-solid/LIMITS.md, /home/user/dmdd-solid/NOTATION.md, /home/user/dmdd-solid/state/SOTA.md
- /home/user/dmdd-solid/returns/R4/WP0.md: the architecture. Cite its equation numbers, use its notation, and do not
  re-derive it. If you find an error in WP0, state it in a section "WP0 defects".
- /home/user/dmdd-solid/surveys/dm-solid-state-processes/README.md, plus the relevant sections of
  catalog-processes.md and catalog-analysis-and-gaps.md in that folder
- /home/user/dmdd-solid/returns/R1/D1.md, D2.md; /home/user/dmdd-solid/referees/R2/REF-A.md, REF-B.md; /home/user/dmdd-solid/returns/R3/X1.md and X2.md if present

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
  /home/user/dmdd-solid/literature/papers-WP3/. Verify every cited ID against the arXiv API, and delete PDFs at the end.
- Theory only. Run no numerical simulations; sympy checks of ≤ 2 min are fine.
- Mark each step DERIVED (with hypotheses), ESTIMATED or CONJECTURED.
- Write the return to /home/user/dmdd-solid/returns/R5/WP3.md (≤ 500 lines) and scripts to /home/user/dmdd-solid/code/WP3/.
- Your final message is a summary of ≤ 15 lines.
