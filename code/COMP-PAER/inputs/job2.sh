set -e; cd /root/work/COMP-PAER/main
mpirun -np 4 ph.x -in ph44.in > ph44.out
q2r.x < q2r.in > q2r.out
cp -r out out_nscf; sed -i "s#'./out'#'./out_nscf'#" nscf40.in
mpirun -np 4 pw.x -npool 4 -in nscf40.in > nscf40.out
