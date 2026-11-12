#!/usr/bin/env bash
# Representative DFPT calculation behind Fig. 5.2 (silicon phonon dispersion and density of states) and Sect. 5.2.
# Quantum ESPRESSO 7.6 (pw.x, ph.x, q2r.x, matdyn.x), PBE, SG15 ONCV norm-conserving pseudopotential
# Si_ONCV_PBE-1.2.upf (4 valence electrons), ecutwfc = 60 Ry (ecutrho = 240 Ry, the default 4x),
# Gamma-centered 12x12x12 k grid (the representative grid of App. E.1), measured lattice constant
# a = 5.431 Angstrom (celldm(1) = 10.2631 bohr), natural-abundance Si mass 28.0855 u.
# DFPT on a 6x6x6 Gamma-centered Q grid (16 irreducible points), q2r -> real-space force constants
# (acoustic sum rule imposed, 'crystal'), matdyn -> (i) frequencies on a list of Q points along
# Gamma-X, X'-K-Gamma (the [110] line from X' = (1,1,0)2pi/a), Gamma-L, written by fig5_2_qpath.py;
# (ii) density of states on a 48^3 grid (tetrahedra), 0.25 cm^-1 bins.
# Run: bash book/tools/qe/run-heavy.sh SEC5.2-QE bash fig5_2_qe.sh     (work directory /root/work/5.2)
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
W=/root/work/5.2; mkdir -p $W; cd $W
PS=/root/pseudo/sg15
A=10.2631
cat > scf.in <<EOI
&control
  calculation='scf', prefix='Si', outdir='$W/tmp', pseudo_dir='$PS'
/
&system
  ibrav=2, celldm(1)=$A, nat=2, ntyp=1, ecutwfc=60
/
&electrons
  conv_thr=1.0d-12, mixing_beta=0.7
/
ATOMIC_SPECIES
  Si 28.0855 Si_ONCV_PBE-1.2.upf
ATOMIC_POSITIONS alat
  Si 0.00 0.00 0.00
  Si 0.25 0.25 0.25
K_POINTS automatic
  12 12 12 0 0 0
EOI
mpirun -np 4 pw.x -nk 4 -in scf.in > scf.out
cat > ph.in <<EOI
phonons of Si, 6x6x6 grid
&inputph
  prefix='Si', outdir='$W/tmp', fildyn='Si.dyn', tr2_ph=1.0d-16, ldisp=.true., nq1=6, nq2=6, nq3=6
/
EOI
mpirun -np 4 ph.x -nk 4 -in ph.in > ph.out
cat > q2r.in <<EOI
&input
  fildyn='Si.dyn', zasr='crystal', flfrc='Si.fc'
/
EOI
q2r.x < q2r.in > q2r.out
python3 "$HERE/fig5_2_qpath.py" > path.txt
cat > disp.in <<EOI
&input
  asr='crystal', flfrc='Si.fc', amass(1)=28.0855, flfrq='Si.freq', q_in_cryst_coord=.false.
/
EOI
cat path.txt >> disp.in
matdyn.x < disp.in > disp.out
cat > dos.in <<EOI
&input
  asr='crystal', flfrc='Si.fc', amass(1)=28.0855, dos=.true., nk1=48, nk2=48, nk3=48, deltaE=0.25, fldos='Si.dos'
/
EOI
matdyn.x < dos.in > dos.out
