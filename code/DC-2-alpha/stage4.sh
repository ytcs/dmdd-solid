#!/usr/bin/env bash
W=/home/ytc/paer-work/work/DC-2-alpha; cd $W
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
M="mpirun --mca btl self,vader -np 3"
date +%T; $M pw.x -in nscf.in > nscf.out 2>/dev/null; date +%T
wannier90.x -pp Ge
printf "&inputpp\n outdir='./k8e80', prefix='a', seedname='Ge', write_mmn=.true., write_amn=.true., write_unk=.false.\n/\n" > p2w.in
$M pw2wannier90.x -in p2w.in > p2w.out 2>&1; date +%T
wannier90.x Ge; date +%T
echo STAGE4_DONE
