#!/usr/bin/env bash
# DC-91 Gamma stage (COMP-PH 6.1): relax -> celldm into scf -> phG. GaAs stays at a_exp (spec warning). Standard QE GPU path.
NV=/opt/nvidia/hpc_sdk/Linux_x86_64/26.5
export PATH=$NV/comm_libs/mpi/bin:$NV/compilers/bin:$PATH OMPI_ALLOW_RUN_AS_ROOT=1 OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
export LD_LIBRARY_PATH=/root/rtsc/nvtxshim:${LD_LIBRARY_PATH:-} OMP_NUM_THREADS=3
B=/root/rtsc/qe-rtsc/build-gpu/bin
for f in $(find /root/dl -name '*_ONCV_PBE-1.2.upf'); do cp -n $f /root/pseudo/; done
R="mpirun --bind-to none -np 1 -x OMP_NUM_THREADS"
for m in C SiC-3C LiF NaF GaAs; do
  cd /root/dc91/$m; sed -i "s#@PSEUDO@#/root/pseudo#" relax.in scf.in
  date -Is; echo START $m
  if [ $m != GaAs ]; then
    $R $B/pw.x -in relax.in > relax.out 2>&1
    python3 - <<'PY'
import re
t=open('relax.out',errors='ignore').read()
m=re.findall(r'CELL_PARAMETERS \(alat=\s*(\S+)\)\n\s*(\S+)',t)
if m:
    a=float(m[-1][0])*abs(float(m[-1][1]))*2
    s=open('scf.in').read(); s2=re.sub(r'celldm\(1\)\s*=\s*\S+',f'celldm(1) = {a:.5f}',s); open('scf.in','w').write(s2); print('relaxed a bohr',round(a,4))
else: print('NO RELAX RESULT')
PY
  fi
  rm -rf *.save *.wfc* *.xml
  $R $B/pw.x -in scf.in > scf.out 2>&1
  grep -E 'highest occupied|Fermi' scf.out | tail -1
  $R $B/ph.x -in phG.in > phG.out 2>&1; echo "phG rc=$?"
  grep -E 'Error in routine' -A1 scf.out phG.out | head -3
done
echo DC91_GAMMA_DONE
