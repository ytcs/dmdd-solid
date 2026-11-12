#!/usr/bin/env bash
# GaAs row of Table 5.1 (Sect. 5.3): DFPT phonons, density of states and atom-projected densities of states of GaAs.
# Quantum ESPRESSO 7.6 (pw.x, ph.x, q2r.x, matdyn.x), PBE, SG15 ONCV norm-conserving pseudopotentials
# Ga_ONCV_PBE-1.2.upf (13 valence electrons, 3d included) and As_ONCV_PBE-1.2.upf (5 valence electrons),
# ecutwfc = 60 Ry (ecutrho = 240 Ry), Gamma-centered 8x8x8 k grid, zinc-blende structure with the measured
# lattice constant a = 5.638 Angstrom (zero-temperature value with the zero-point expansion removed,
# Csonka et al., PRB 79, 155107 (2009), Table II, as in Table E.1), natural masses Ga 69.723 u, As 74.9216 u.
# DFPT on a 4x4x4 Gamma-centered Q grid (8 irreducible points; ph.x computes eps_inf and the Born charges at Gamma
# and q2r/matdyn add the long-range dipole term), q2r with zasr='crystal', matdyn:
#  (i) frequencies at Gamma (along [100], LO and TO), X = (1,0,0)2pi/a and L = (1/2,1/2,1/2)2pi/a;
#  (ii) total and atom-projected density of states on a 32^3 grid (tetrahedra), 0.25 cm^-1 bins.
# Run: bash book/tools/qe/run-heavy.sh SEC5.3-QE bash tab5_1_gaas_qe.sh   (work directory /root/work/5.3)
set -euo pipefail
W=/root/work/5.3; mkdir -p $W; cd $W
PS=/root/pseudo/sg15
CELLDM=$(python3 -c "print(5.638/0.529177210903)")
cat > scf.in <<EOI
&control
  calculation='scf', prefix='GaAs', outdir='$W/tmp', pseudo_dir='$PS'
/
&system
  ibrav=2, celldm(1)=$CELLDM, nat=2, ntyp=2, ecutwfc=60.0
/
&electrons
  conv_thr=1.0d-12
/
ATOMIC_SPECIES
  Ga 69.723  Ga_ONCV_PBE-1.2.upf
  As 74.9216 As_ONCV_PBE-1.2.upf
ATOMIC_POSITIONS crystal
  Ga 0.00 0.00 0.00
  As 0.25 0.25 0.25
K_POINTS automatic
  8 8 8 0 0 0
EOI
mpirun -np 4 pw.x -nk 4 -in scf.in > scf.out
cat > ph.in <<EOI
phonons of GaAs on a 4^3 grid
&inputph
  prefix='GaAs', outdir='$W/tmp', fildyn='GaAs.dyn', tr2_ph=1.0d-16,
  ldisp=.true., nq1=4, nq2=4, nq3=4
/
EOI
mpirun -np 4 ph.x -nk 4 -in ph.in > ph.out
printf "&input\n  fildyn='GaAs.dyn', zasr='crystal', flfrc='GaAs.fc'\n/\n" > q2r.in
q2r.x < q2r.in > q2r.out
cat > disp.in <<EOI
&input
  asr='crystal', flfrc='GaAs.fc', amass(1)=69.723, amass(2)=74.9216, flfrq='GaAs.freq', q_in_cryst_coord=.false.
/
4
0.001 0.0 0.0
1.0 0.0 0.0
0.5 0.5 0.5
0.0 0.0 0.001
EOI
matdyn.x < disp.in > disp.out
cat > dos.in <<EOI
&input
  asr='crystal', flfrc='GaAs.fc', amass(1)=69.723, amass(2)=74.9216, dos=.true., fldos='GaAs.dos',
  nk1=32, nk2=32, nk3=32, deltaE=0.25
/
EOI
matdyn.x < dos.in > dos.out
