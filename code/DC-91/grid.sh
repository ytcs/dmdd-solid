#!/usr/bin/env bash
# DC-91 stage 2: ph 4^3 -> q2r -> matdyn for the materials that passed the Gamma controls. Standard QE GPU path.
NV=/opt/nvidia/hpc_sdk/Linux_x86_64/26.5
export PATH=$NV/comm_libs/mpi/bin:$NV/compilers/bin:$PATH OMPI_ALLOW_RUN_AS_ROOT=1 OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
export LD_LIBRARY_PATH=/root/rtsc/nvtxshim:${LD_LIBRARY_PATH:-} OMP_NUM_THREADS=3
B=/root/rtsc/qe-rtsc/build-gpu/bin; R="mpirun --bind-to none -np 1 -x OMP_NUM_THREADS"
for m in C LiF NaF SiC-3C; do
  cd /root/dc91/$m; date -Is; echo START $m
  $R $B/ph.x -in ph.in > ph.out 2>&1; echo "ph rc=$?"
  $R $B/q2r.x -in q2r.in > q2r.out 2>&1; echo "q2r rc=$?"
  $R $B/matdyn.x -in matdyn.in > matdyn.out 2>&1; echo "matdyn rc=$?"
done
echo DC91_GRID_DONE
# Deviation from code/COMP-PH/formulated/*/ph.in: epsil=.true. added for LiF, NaF, 3C-SiC (polar: q2r needs Z*, eps for the long-range part).
