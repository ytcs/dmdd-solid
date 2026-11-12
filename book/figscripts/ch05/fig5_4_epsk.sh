#!/usr/bin/env bash
# Sect. 5.5: k-grid convergence of the PBE electronic dielectric constant and Born charges of GaAs at Gamma.
# Same settings as tab5_1_gaas_qe.sh (QE 7.6, PBE, SG15 ONCV Ga_ONCV_PBE-1.2 (13 e, 3d included) and As_ONCV_PBE-1.2 (5 e),
# ecutwfc = 60 Ry, measured a = 5.638 A [Csonka et al., PRB 79, 155107 (2009), Table II, as in Table E.1]),
# with Gamma-centered 12^3 ... 28^3 k grids (NKS="12 16" by default; run again with NKS="20 24 28"); ph.x with trans=.false., epsil=.true. (eps_inf and Z* = dF/dE only).
# The 8^3 values come from the full phonon run of tab5_1_gaas_qe.sh.
# Run: bash book/tools/qe/run-heavy.sh SEC5.5-EPSK bash fig5_4_epsk.sh   (work directory /root/work/5.5)
set -euo pipefail
W=/root/work/5.5; mkdir -p $W; cd $W
PS=/root/pseudo/sg15
CELLDM=$(python3 -c "print(5.638/0.529177210903)")
for NK in ${NKS:-12 16}; do
cat > scf$NK.in <<EOI
&control
  calculation='scf', prefix='GaAs$NK', outdir='$W/tmp', pseudo_dir='$PS'
/
&system
  ibrav=2, celldm(1)=$CELLDM, nat=2, ntyp=2, ecutwfc=60.0, nbnd=24
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
  $NK $NK $NK 0 0 0
EOI
mpirun -np 4 pw.x -nk 4 -in scf$NK.in > scf$NK.out
cat > eps$NK.in <<EOI
eps and Z* of GaAs, k $NK^3
&inputph
  prefix='GaAs$NK', outdir='$W/tmp', fildyn='GaAs$NK.dyn', tr2_ph=1.0d-16, trans=.false., epsil=.true.
/
0.0 0.0 0.0
EOI
mpirun -np 4 ph.x -nk 4 -in eps$NK.in > eps$NK.out
rm -rf $W/tmp/_ph0 $W/tmp/GaAs$NK.save/wfc*
done
