CW2 formulated-job inputs (rtsc/bench layout of github.com/ytcs/qe-rtsc: `@PSEUDO@` placeholder, SG15 ONCV PBE v1.2 via rtsc/pseudo.sh,
outdir './', stages scf -> ph -> q2r -> matdyn as in rtsc/bench/run-fork.sh). Not run here (compute-formulate rows; returns/R16/CW2.md §0).
SG15 v1.2 valences: Si 4, Ge 14 (3d semicore), Ga 13 (3d), As 5; Ge and GaAs therefore need ecutwfc >= 80 Ry (COMP-PH conv/ scan). @QLIST@: generated 48^3 (or Lebedev x |q|) list, one q per line, preceded by the count.
Lattice: experimental low-T a (Si 5.431, Ge 5.658, GaAs 5.653 A); a PBE vc-relax variant is the convergence/systematics partner (pitfall: PBE a is ~0.7-1% large, phonons ~2-4% soft).
