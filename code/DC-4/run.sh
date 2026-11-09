#!/usr/bin/env bash
# DC-4: Ge PBE DFPT 6^3 at a_exp (same settings as code/COMP-PH/chain.py phgrid: 80 Ry, k 8^3, 10.692 bohr).
set -euo pipefail
C=/home/ytc/Projects/bm-paer/campaign/paer/code/DC-4; W=/home/ytc/paer-work/work/DC-4
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
cd $W
date -Is; mpirun -np 8 --oversubscribe pw.x -nk 8 -in $C/inputs/scf.in > scf.out
date -Is; mpirun -np 8 --oversubscribe ph.x -nk 8 -in $C/inputs/ph.in > ph.out
date -Is; echo PH_DONE
