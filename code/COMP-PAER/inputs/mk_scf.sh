#!/bin/bash
# usage: mk_scf.sh ECUT K OUTDIR [calc] [nbnd] -> writes pw input on stdout
EC=$1; K=$2; OD=$3; CALC=${4:-scf}; NB=${5:-8}
cat <<EOI
&control
  calculation='$CALC', prefix='si', outdir='$OD', pseudo_dir='/root/pseudo/sg15', tprnfor=.true., tstress=.true.
/
&system
  ibrav=2, celldm(1)=10.2631, nat=2, ntyp=1, ecutwfc=$EC, nbnd=$NB
/
&electrons
  conv_thr=1d-12
/
ATOMIC_SPECIES
Si 28.0855 Si_ONCV_PBE-1.2.upf
ATOMIC_POSITIONS alat
Si 0.00 0.00 0.00
Si 0.25 0.25 0.25
K_POINTS automatic
$K $K $K 0 0 0
EOI
