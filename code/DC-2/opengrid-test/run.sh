#!/usr/bin/env bash
# DC-2 control: does open_grid.x unfold spinor wavefunctions correctly? Ge PBE+SOC, 40 Ry, 4^3.
# Route A: symmetric SCF -> open_grid.x -> pw2wannier90 -> wannier90.  Route B: direct nosym full grid (the spec's route).
# Pass criterion: Wannier bands of A and B agree at off-grid k (emitted by compare.py).
set -uo pipefail
W=/home/ytc/paer-work/work/DC-2-ogtest; PS=/home/ytc/paer-work/pseudo/sg15
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
MPI="mpirun --mca btl self,vader -np 2"
kl=$(python3 -c "
for i in range(4):
  for j in range(4):
    for k in range(4): print(f'{i/4:.8f} {j/4:.8f} {k/4:.8f} 1.0')")
head() { cat <<EOI
&control
 calculation='$1', prefix='$2', outdir='./tmp', pseudo_dir='$PS'
/
&system
 ibrav=2, celldm(1)=10.692, nat=2, ntyp=1, ecutwfc=40, noncolin=.true., lspinorb=.true., nbnd=48 $3
/
&electrons
 conv_thr=1d-10, mixing_beta=0.5, diago_full_acc=.true.
/
ATOMIC_SPECIES
 Ge 72.630 Ge_ONCV_PBE_FR-1.0.upf
ATOMIC_POSITIONS crystal
 Ge 0 0 0
 Ge .25 .25 .25
EOI
}
win() { cat <<EOI
num_wann=16
num_bands=28
exclude_bands=1-20
spinors=.true.
dis_froz_max=$1
dis_win_max=$2
dis_num_iter=500
num_iter=200
write_hr=.true.
use_ws_distance=.true.
begin projections
Ge:sp3
end projections
begin unit_cell_cart
bohr
-5.346 0 5.346
0 5.346 5.346
-5.346 5.346 0
end unit_cell_cart
begin atoms_frac
Ge 0 0 0
Ge 0.25 0.25 0.25
end atoms_frac
mp_grid=4 4 4
begin kpoints
$(python3 -c "
for i in range(4):
  for j in range(4):
    for k in range(4): print(f'{i/4:.8f} {j/4:.8f} {k/4:.8f}')")
end kpoints
EOI
}
# Route A
cd $W/A
{ head scf Ge ""; echo "K_POINTS automatic"; echo " 4 4 4 0 0 0"; } > scf.in
$MPI pw.x -in scf.in > scf.out 2>/dev/null
printf "&inputpp\n outdir='./tmp', prefix='Ge', overwrite_prefix=.false.\n/\n" > og.in
$MPI open_grid.x -in og.in > og.out 2>/dev/null
tail -3 og.out
VB=$(grep -E 'highest occupied' scf.out | awk '{print $(NF-1)}'); [ -n "$VB" ] || VB=$(grep -E 'Fermi' scf.out | awk '{print $5}')
F=$(python3 -c "print($VB+3)"); M=$(python3 -c "print($VB+12)")
win $F $M > Ge.win; wannier90.x -pp Ge
printf "&inputpp\n outdir='./tmp', prefix='Ge_open', seedname='Ge', write_mmn=.true., write_amn=.true., write_unk=.false.\n/\n" > p2w.in
$MPI pw2wannier90.x -in p2w.in > p2w.out 2>&1
wannier90.x Ge
# Route B
cd $W/B
{ head scf Ge ""; echo "K_POINTS automatic"; echo " 4 4 4 0 0 0"; } > scf.in
$MPI pw.x -in scf.in > scf.out 2>/dev/null
{ head nscf Ge ", nosym=.true., noinv=.true."; echo "K_POINTS crystal"; echo 64; echo "$kl"; } > nscf.in
$MPI pw.x -in nscf.in > nscf.out 2>/dev/null
win $F $M > Ge.win; wannier90.x -pp Ge
printf "&inputpp\n outdir='./tmp', prefix='Ge', seedname='Ge', write_mmn=.true., write_amn=.true., write_unk=.false.\n/\n" > p2w.in
$MPI pw2wannier90.x -in p2w.in > p2w.out 2>&1
wannier90.x Ge
echo OGTEST_DONE
