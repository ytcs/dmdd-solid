#!/usr/bin/env bash
# DC-2 diagnostic: Gamma/L ordering vs EXX numerics. k 4^3 (Gamma, L, X on grid), 80 Ry, HSE06 + SOC, a_exp.
source /root/rtsc/env.sh
export OMP_NUM_THREADS=8
B=/root/rtsc/qe-rtsc/build-gpu/bin/pw.x; mkdir -p /root/run/sw; cd /root/run/sw
run() { # tag k nq ecutfock dft
cat > $1.in <<EOI
&control
 calculation='scf', prefix='$1', pseudo_dir='/root/pseudo', outdir='./t$1', verbosity='high', disk_io='none'
/
&system
 ibrav=2, celldm(1)=10.692, nat=2, ntyp=1, ecutwfc=80, $( [ "$5" = hse ] && echo "ecutfock=$4, input_dft='hse', nqx1=$3, nqx2=$3, nqx3=$3," ) noncolin=.true., lspinorb=.true., nbnd=36
/
&electrons
 conv_thr=1d-9, mixing_beta=0.5
/
ATOMIC_SPECIES
 Ge 72.630 Ge_ONCV_PBE_FR-1.0.upf
ATOMIC_POSITIONS crystal
 Ge 0 0 0
 Ge .25 .25 .25
K_POINTS automatic
 $2 $2 $2 0 0 0
EOI
s=$(date +%s); mpirun -np 1 $B -in $1.in > $1.out 2>&1; echo "$1 wall $(( $(date +%s)-s )) s" >> times.log
}
while ! grep -q SWEEP_DONE times.log; do sleep 10; done
run k6q6f160 6 6 160 hse
run k6q3f160 6 3 160 hse
echo SWEEP2_DONE >> times.log
