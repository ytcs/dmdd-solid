#!/usr/bin/env bash
# DFT+alpha scan: PBE+SOC reference SCF, then restart with Hubbard ALPHA on Ge-4s. usage: run_alpha.sh K ECUT alpha...
W=/home/ytc/paer-work/work/DC-2-alpha; cd $W
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
K=$1; E=$2; shift 2; T=k${K}e${E}
head() { cat <<EOI
&control
 calculation='scf', prefix='a', pseudo_dir='/home/ytc/paer-work/pseudo/dojo-fr/nc-fr-04_pbe_standard', outdir='./$T', verbosity='high'
/
&system
 ibrav=2, celldm(1)=10.692, nat=2, ntyp=1, ecutwfc=$E, noncolin=.true., lspinorb=.true., nbnd=36
/
&electrons
 conv_thr=1d-9, mixing_beta=0.4 $1
/
ATOMIC_SPECIES
 Ge 72.630 Ge.upf
ATOMIC_POSITIONS crystal
 Ge 0 0 0
 Ge .25 .25 .25
K_POINTS automatic
 $K $K $K 0 0 0
EOI
}
{ head ""; printf "HUBBARD ortho-atomic\nU Ge-4s 1.0d-8\n"; } > $T.ref.in; mpirun --mca btl self,vader -np 2 pw.x -in $T.ref.in > $T.ref.out 2>/dev/null
for a in "$@"; do
  { head ", startingpot='file'"; printf "HUBBARD ortho-atomic\nU Ge-4s 1.0d-8\nALPHA Ge-4s $a\n"; } > $T.a$a.in
  mpirun --mca btl self,vader -np 2 pw.x -in $T.a$a.in > $T.a$a.out 2>/dev/null
done
echo SCAN_DONE
