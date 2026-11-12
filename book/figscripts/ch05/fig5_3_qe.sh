#!/usr/bin/env bash
# Fig. 5.3 (Sect. 5.4): Fourier interpolation of DFPT force constants and the acoustic sum rule, silicon.
# Reuses the representative DFPT run of fig5_2_qe.sh (work directory /root/work/5.2; Quantum ESPRESSO 7.6, PBE,
# SG15 ONCV Si_ONCV_PBE-1.2.upf, ecutwfc 60 Ry, Gamma-centered 12^3 k grid, a = 5.431 A, natural Si mass 28.0855 u;
# ph.x on a 6^3 Gamma-centered Q grid, 16 irreducible points, files Si.dyn0..Si.dyn16). No new SCF and no new grid run.
# (1) Coarse grids from the same dynamical matrices: the 2^3 and 3^3 Gamma-centered grids are subgrids of the 6^3 grid.
#     Irreducible points of the 6^3 run that lie on them (crystal coordinates n_i/6 with n_i = 0 mod 3, resp. 0 mod 2):
#       2^3: Si.dyn1 (Gamma), Si.dyn4 (L), Si.dyn13 (X)                    -> 3 irreducible points
#       3^3: Si.dyn1 (Gamma), Si.dyn3, Si.dyn10, Si.dyn12                  -> 4 irreducible points
#     Each dyn file holds the full star of its point, so q2r sees every point of the coarse grid.
# (2) q2r (zasr='crystal') for each grid; matdyn on the points of fig5_3_qpath.py with asr='crystal';
#     for the 6^3 grid also with asr='no' (sum rule not imposed).
# (3) Direct ph.x at three points on none of the grids (fig5_3_qpath.OFFGRID), same settings as the 6^3 run
#     (tr2_ph = 1e-16), reading a copy of the 5.2 ground state: the test of the interpolation.
# Run: bash book/tools/qe/run-heavy.sh SEC5.4-QE bash fig5_3_qe.sh     (work directory /root/work/5.4, deleted after parsing)
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
SRC=/root/work/5.2
W=/root/work/5.4; mkdir -p $W; cd $W
python3 "$HERE/fig5_3_qpath.py" > path.txt

mkgrid () {   # $1 = N, rest = indices of the 6^3 dyn files on the N^3 subgrid
  local N=$1; shift
  local D=$W/g$N; mkdir -p $D
  { printf "%4d%4d%4d\n%4d\n" $N $N $N $#; for i in "$@"; do sed -n "$((i+2))p" $SRC/Si.dyn0; done; } > $D/Si.dyn0
  local j=1; for i in "$@"; do cp $SRC/Si.dyn$i $D/Si.dyn$j; j=$((j+1)); done
}
mkgrid 2 1 4 13
mkgrid 3 1 3 10 12
mkdir -p g6; cp $SRC/Si.dyn* g6/

for N in 2 3 6; do
  cd $W/g$N
  printf "&input\n  fildyn='Si.dyn', zasr='crystal', flfrc='Si.fc'\n/\n" > q2r.in
  q2r.x < q2r.in > q2r.out
  for ASR in crystal no; do
    [ "$N" != 6 ] && [ "$ASR" = no ] && continue
    { printf "&input\n  asr='%s', flfrc='Si.fc', amass(1)=28.0855, flfrq='freq_%s', q_in_cryst_coord=.false.\n/\n" $ASR $ASR
      cat $W/path.txt; } > disp_$ASR.in
    matdyn.x < disp_$ASR.in > disp_$ASR.out
  done
done

cd $W
mkdir -p tmp; cp -r $SRC/tmp/Si.save $SRC/tmp/Si.xml tmp/
i=0
for q in "0.0 0.0 0.5" "0.5 0.5 0.0" "0.25 0.25 0.25"; do
  i=$((i+1))
  cat > ph_off$i.in <<EOI
off-grid phonon $i
&inputph
  prefix='Si', outdir='$W/tmp', fildyn='off$i.dyn', tr2_ph=1.0d-16
/
$q
EOI
  mpirun -np 4 ph.x -nk 4 -in ph_off$i.in > ph_off$i.out
done
