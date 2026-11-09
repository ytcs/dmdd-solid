#!/usr/bin/env bash
# DC-2-gw S1: PBE+SOC ground state and 400-band nscf (SG15 FR Ge, 3d valence, a_exp, 80 Ry, k 8^3 with symmetry).
W=/home/ytc/paer-work/work/DC-2-gw/S1; cd $W
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
mk() { cat <<EOI
&control
 calculation='$1', prefix='Ge', outdir='./tmp', pseudo_dir='/home/ytc/paer-work/pseudo/sg15', verbosity='high'
/
&system
 ibrav=2, celldm(1)=10.692, nat=2, ntyp=1, ecutwfc=80, noncolin=.true., lspinorb=.true., nbnd=$2, force_symmorphic=.true.
/
&electrons
 conv_thr=1d-10, mixing_beta=0.5, diago_full_acc=.true., diago_thr_init=1d-6
/
ATOMIC_SPECIES
 Ge 72.630 Ge_ONCV_PBE_FR-1.0.upf
ATOMIC_POSITIONS crystal
 Ge 0 0 0
 Ge .25 .25 .25
K_POINTS automatic
 8 8 8 0 0 0
EOI
}
mk scf 36 > scf.in; mk nscf 400 > nscf.in
date -Is; mpirun --mca btl self,vader -np 3 pw.x -nk 3 -in scf.in > scf.out 2>/dev/null; echo scf rc=$?
date -Is; mpirun --mca btl self,vader -np 3 pw.x -nk 3 -in nscf.in > nscf.out 2>/dev/null; echo nscf rc=$?
date -Is; echo S1_QE_DONE
