#!/usr/bin/env bash
# Representative plane-wave calculation behind Fig. 5.1(b) and the zero-point amplitude of Sect. 5.1.
# Quantum ESPRESSO 7.6 (pw.x, ph.x, q2r.x, matdyn.x), PBE, SG15 ONCV norm-conserving pseudopotential
# Si_ONCV_PBE-1.2.upf (4 valence electrons), ecutwfc = 50 Ry, Gamma-centered 8x8x8 k grid,
# measured lattice constant a = 5.431 Angstrom (celldm(1) = 10.2631 bohr; NIST/CODATA 2022 value used in the book),
# natural-abundance Si mass 28.0855 u (phonons are compared with measurements on natural silicon).
# (1) Frozen zone-center optical displacement: atom 1 moves by -(u/2) n and atom 2 by +(u/2) n, n = [111]/sqrt(3)
#     (u = change of the bond length along the bond), u = -0.30 ... +0.30 Angstrom; total energy and forces.
# (2) DFPT on a 4x4x4 q grid -> q2r -> matdyn phonon DOS on a 40^3 grid (for <u_x^2>). Result: Gamma optical 15.41 THz
#     = 63.7 meV (frozen phonon: 63.7 meV); <u_x^2>^(1/2) = 0.0497 A (T = 0), 0.0812 A (293 K; measured 0.0771 A).
# Work directory /root/work/5.1 (outputs are parsed by fig5_1_data.py).
set -euo pipefail
W=/root/work/5.1; mkdir -p $W; cd $W
PS=/root/pseudo/sg15
A=10.2631
scf() { # $1 label, $2 x1, $3 x2 (crystal coords along (1,1,1)/4 direction, in alat units Cartesian)
cat > $1.in <<EOI
&control
  calculation='scf', prefix='$1', outdir='$W/tmp', pseudo_dir='$PS', tprnfor=.true.
/
&system
  ibrav=2, celldm(1)=$A, nat=2, ntyp=1, ecutwfc=50
/
&electrons
  conv_thr=1.0d-12, mixing_beta=0.7
/
ATOMIC_SPECIES
  Si 28.0855 Si_ONCV_PBE-1.2.upf
ATOMIC_POSITIONS alat
  Si $2 $2 $2
  Si $3 $3 $3
K_POINTS automatic
  8 8 8 0 0 0
EOI
mpirun -np 4 pw.x -nk 2 -in $1.in > $1.out
}
# displacement u (Angstrom) along the bond: each Cartesian component of atom 1 shifts by (u/2)/sqrt(3)/a
for u in -0.30 -0.20 -0.15 -0.10 -0.06 -0.03 0.00 0.03 0.06 0.10 0.15 0.20 0.30; do
  d=$(python3 -c "print(f'{($u/2)/3**0.5/5.431:.8f}')")
  x1=$(python3 -c "print(f'{-$d:.8f}')")     # atom 1 moves away from atom 2 for u>0
  x2=$(python3 -c "print(f'{0.25+$d:.8f}')")
  scf fp_$u $x1 $x2
done
# ground state + DFPT
scf Si 0.0 0.25
cat > ph.in <<EOI
&inputph
  prefix='Si', outdir='$W/tmp', fildyn='Si.dyn', tr2_ph=1.0d-16, ldisp=.true., nq1=4, nq2=4, nq3=4
/
EOI
mpirun -np 4 ph.x -nk 2 -in ph.in > ph.out
cat > q2r.in <<EOI
&input
  fildyn='Si.dyn', zasr='crystal', flfrc='Si.fc'
/
EOI
q2r.x < q2r.in > q2r.out
cat > dos.in <<EOI
&input
  asr='crystal', flfrc='Si.fc', amass(1)=28.0855, dos=.true., nk1=40, nk2=40, nk3=40, deltaE=0.5, fldos='Si.dos'
/
EOI
matdyn.x < dos.in > dos.out
