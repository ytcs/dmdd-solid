#!/usr/bin/env bash
# Resume Ge LDA DFPT. tr2_ph 1e-15: at 1e-16 the pools disagreed on convergence at the numerical floor (check_all_convt stop).
C=/home/ytc/Projects/bm-paer/campaign/paer/code/DC-4; W=/home/ytc/paer-work/work/DC-4-lda
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
cd $W; rm -f CRASH; date -Is
mpirun --mca btl self,vader -np 10 --oversubscribe ph.x -nk 10 -in $C/inputs-lda/ph.in >> ph.out 2>/dev/null
rc=$?; date -Is; [ -f CRASH ] && rc=99; echo "LDA_EXIT rc=$rc"
