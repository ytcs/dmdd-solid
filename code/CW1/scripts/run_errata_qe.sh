#!/bin/bash
# ERR-CW1 QE reruns: single core, < 3 min in total (outside the heavy lock: one core, short). Work dir /root/work/CW1 (regenerated).
set -e
export PATH=/root/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
C=/home/user/dmdd-solid/code/CW1; I=$C/inputs/errata; mkdir -p /root/work/CW1; cd /root/work/CW1
python3 $C/scripts/errata_kset.py kset.txt labels.json            # same k set as embedded in inputs/errata/nscf_*.in
cp kset.txt $I/kset_errata.txt; cp labels.json $I/kset_errata_labels.json
for v in S12 FRav SOC; do for c in scf nscf; do pw.x -in $I/${c}_$v.in > ${c}_$v.out 2>&1; done; done
python3 $C/scripts/errata_analysis.py /root/work/CW1 labels.json $C/out/errata_qe.json > /dev/null
for v in S12 SOC; do
  python3 $C/scripts/errata_kset2.py $C/out/errata_qe.json labels.json $v kset2_$v.txt labels2_$v.json
  rm -rf it2/$v; mkdir -p it2; cp -r $v it2/$v
  sed -e "s#outdir='./$v'#outdir='./it2/$v'#" -e '/^K_POINTS/,$d' $I/nscf_$v.in > nscf2_$v.in; { echo "K_POINTS tpiba"; cat kset2_$v.txt; } >> nscf2_$v.in
  cp nscf2_$v.in kset2_$v.txt labels2_$v.json $I/
  pw.x -in nscf2_$v.in > nscf2_$v.out 2>&1
done
mkdir -p it2x; for v in S12 SOC; do ln -sfn ../it2/$v it2x/$v; done
python3 $C/scripts/errata_analysis.py /root/work/CW1/it2 labels2_SOC.json $C/out/errata_qe_it2_SOC.json SOC > /dev/null
python3 $C/scripts/errata_analysis.py /root/work/CW1/it2 labels2_S12.json $C/out/errata_qe_it2_S12.json S12 > /dev/null
for v in FRav SOC; do rm -rf xf/$v; mkdir -p xf; cp -r $v xf/$v; pw.x -in $I/nscf_xface_$v.in > nscf_xface_$v.out 2>&1; done
python3 $C/scripts/errata_xface.py /root/work/CW1 $C/out/errata_xface_soc.json > /dev/null
