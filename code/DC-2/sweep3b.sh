#!/usr/bin/env bash
# DC-2 diagnostic: is Gamma-below-L caused by the pseudopotential? k 4^3, nq 4, HSE06, a_exp.
source /root/rtsc/env.sh
export OMP_NUM_THREADS=8
B=/root/rtsc/qe-rtsc/build-gpu/bin/pw.x; cd /root/run/sw
run() { # tag upf socflags nbnd ecut alat
cat > $1.in <<EOI
&control
 calculation='scf', prefix='$1', pseudo_dir='/root/pseudo', outdir='./t$1', verbosity='high', disk_io='none'
/
&system
 ibrav=2, celldm(1)=$6, nat=2, ntyp=1, ecutwfc=$5, ecutfock=$((2*$5)), input_dft='hse', nqx1=4, nqx2=4, nqx3=4, $3 nbnd=$4
/
&electrons
 conv_thr=1d-9, mixing_beta=0.5
/
ATOMIC_SPECIES
 Ge 72.630 $2
ATOMIC_POSITIONS crystal
 Ge 0 0 0
 Ge .25 .25 .25
K_POINTS automatic
 4 4 4 0 0 0
EOI
s=$(date +%s); mpirun -np 1 $B -in $1.in > $1.out 2>&1; echo "$1 wall $(( $(date +%s)-s )) s" >> times.log
}
while ! grep -q SWEEP3_DONE times.log; do sleep 10; done
run dojoFR Ge_dojo_FR.upf "noncolin=.true., lspinorb=.true.," 36 80 10.692
run dojoFR652 Ge_dojo_FR.upf "noncolin=.true., lspinorb=.true.," 36 80 10.681
echo SWEEP3B_DONE >> times.log
