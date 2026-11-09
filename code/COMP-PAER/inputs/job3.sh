set -e; cd /root/work/COMP-PAER/main
rm -rf out_rho; mkdir out_rho; cp -r out/si.save out_rho/; rm -f out_rho/si.save/wfc*
mpirun -np 4 pw.x -in nscf_rho.in > nscf_rho.out
