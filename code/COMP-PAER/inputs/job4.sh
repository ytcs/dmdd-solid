set -e; cd /root/work/COMP-PAER/main
rm -rf out_fs; mkdir out_fs; cp -r out/si.save out_fs/; rm -f out_fs/si.save/wfc*
mpirun -np 4 pw.x -in nscf_fs.in > nscf_fs.out
