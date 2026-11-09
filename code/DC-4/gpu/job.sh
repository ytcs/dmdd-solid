#!/usr/bin/env bash
# DC-4 on the fork: PBE q8-16 (q8 duplicates the CPU run as a cross-check), then LDA 6^3. Runs detached on the pod.
set -uo pipefail
mkdir -p /root/rtsc /root/run/pbe /root/run/lda /root/pseudo; cd /root/rtsc
[ -d qe-rtsc ] || tar -I 'zstd -d' -xf /cache/rtsc-b2x-sm86.tar.zst -C /root/rtsc
NV=/opt/nvidia/hpc_sdk/Linux_x86_64/26.5
export PATH=$NV/comm_libs/mpi/bin:$NV/compilers/bin:$PATH OMPI_ALLOW_RUN_AS_ROOT=1 OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
export LD_LIBRARY_PATH=/root/rtsc/nvtxshim:${LD_LIBRARY_PATH:-} OMP_NUM_THREADS=8
# fork engine declined this case (sternheimer_kernel, strict stop); standard QE GPU path instead
B=/root/rtsc/qe-rtsc/build-gpu/bin
ls -la $B/ph.x $B/pw.x
run() { # dir pseudo extra-ph
  cd /root/run/$1
  cat > scf.in <<EOI
&control
  calculation='scf', prefix='Ge', outdir='./tmp', pseudo_dir='/root/pseudo', tprnfor=.true., tstress=.true.
/
&system
  ibrav=2, celldm(1)=10.692, nat=2, ntyp=1, ecutwfc=80
/
&electrons
  conv_thr=1.0d-12, mixing_beta=0.7
/
ATOMIC_SPECIES
  Ge 72.630 $2
ATOMIC_POSITIONS crystal
  Ge 0 0 0
  Ge .25 .25 .25
K_POINTS automatic
  8 8 8 0 0 0
EOI
  cat > ph.in <<EOI
&inputph
  prefix='Ge', outdir='./tmp', fildyn='Ge.dyn', tr2_ph=1.0d-16, ldisp=.true., nq1=6, nq2=6, nq3=6 $3
/
EOI
  date -Is; mpirun --bind-to none -np 1 -x OMP_NUM_THREADS $B/pw.x -in scf.in > scf.out 2>&1
  date -Is; mpirun --bind-to none -np 1 -x OMP_NUM_THREADS $B/ph.x -in ph.in > ph.out 2>&1; echo "ph rc=$?"
  date -Is
}
run pbe Ge_ONCV_PBE-1.2.upf ", start_q=8, last_q=16"
echo PBE_DONE
run lda Ge_LDA_dojo.upf ""
echo LDA_DONE
