#!/usr/bin/env bash
# Ge LDA DFPT 6^3 at a_exp (PseudoDojo pw standard, 3d valence). Deviation from the PBE convention, for book Table 5.1 and the TA control.
C=/home/ytc/Projects/bm-paer/campaign/paer/code/DC-4; W=/home/ytc/paer-work/work/DC-4-lda
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
cd $W; date -Is
mpirun --mca btl self,vader -np 10 --oversubscribe pw.x -nk 10 -in $C/inputs-lda/scf.in > scf.out 2>/dev/null
mpirun --mca btl self,vader -np 10 --oversubscribe ph.x -nk 10 -in $C/inputs-lda/ph.in > ph.out 2>/dev/null
date -Is; echo LDA_DONE
