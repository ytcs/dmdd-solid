#!/usr/bin/env bash
# DC-2 diagnostic: q->0 treatment of screened exchange. k 4^3 (nq 2, 4) and k 6^3 (nq 6), HSE06+SOC, a_exp.
source /root/rtsc/env.sh
export OMP_NUM_THREADS=8
B=/root/rtsc/qe-rtsc/build-gpu/bin/pw.x; cd /root/run/sw
run() { # tag k nq extra
cat > $1.in <<EOI
&control
 calculation='scf', prefix='$1', pseudo_dir='/root/pseudo', outdir='./t$1', verbosity='high', disk_io='none'
/
&system
 ibrav=2, celldm(1)=10.692, nat=2, ntyp=1, ecutwfc=80, ecutfock=160, input_dft='hse', nqx1=$3, nqx2=$3, nqx3=$3, noncolin=.true., lspinorb=.true., nbnd=36, $4
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
run noX_gb_q2 4 2 "x_gamma_extrapolation=.false."
run noX_gb_q4 4 4 "x_gamma_extrapolation=.false."
run noX_none_q2 4 2 "x_gamma_extrapolation=.false., exxdiv_treatment='none'"
run noX_none_q4 4 4 "x_gamma_extrapolation=.false., exxdiv_treatment='none'"
run X_none_q4 4 4 "x_gamma_extrapolation=.true., exxdiv_treatment='none'"
echo SWEEP4_DONE >> times.log
