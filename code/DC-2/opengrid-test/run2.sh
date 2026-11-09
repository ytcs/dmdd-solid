#!/usr/bin/env bash
# Second stage of the control: use open_grid's own k list (A) and write interpolated bands in both routes.
set -uo pipefail
W=/home/ytc/paer-work/work/DC-2-ogtest
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
MPI="mpirun --mca btl self,vader -np 2"
addbands() { python3 - "$1" <<'PY'
import sys,re
t=open(sys.argv[1]).read()
if 'bands_plot' not in t:
    t="bands_plot=true\nbands_num_points=40\nbegin kpoint_path\nL 0.5 0.5 0.5 G 0 0 0\nG 0 0 0 X 0.5 0 0.5\nX 0.5 0 0.5 W 0.5 0.25 0.75\nend kpoint_path\n"+t
open(sys.argv[1],'w').write(t)
PY
}
cd $W/A
python3 - <<'PY'
import re
L=open('og.out',errors='ignore').read().split('List to be put')[1].split('\n')[1:]
k=[]
for l in L:
    p=l.split()
    if len(p)==4:
        try: k.append(p[:3])
        except: pass
    elif k: break
assert len(k)==64,len(k)
t=open('Ge.win').read()
t=re.sub(r'begin kpoints.*end kpoints','begin kpoints\n'+'\n'.join(' '.join(x) for x in k)+'\nend kpoints',t,flags=re.S)
open('Ge.win','w').write(t)
PY
addbands Ge.win; wannier90.x -pp Ge; $MPI pw2wannier90.x -in p2w.in > p2w.out 2>&1; wannier90.x Ge
cd $W/B
[ -f tmp/Ge.save/data-file-schema.xml ] || true
addbands Ge.win; wannier90.x -pp Ge; $MPI pw2wannier90.x -in p2w.in > p2w.out 2>&1; wannier90.x Ge
python3 - <<'PY'
import numpy as np
def rd(f):
    b=[[]]
    for l in open(f):
        p=l.split()
        if p: b[-1].append(float(p[1]))
        elif b[-1]: b.append([])
    return np.array([x for x in b if x])
a=rd('/home/ytc/paer-work/work/DC-2-ogtest/A/Ge_band.dat'); c=rd('/home/ytc/paer-work/work/DC-2-ogtest/B/Ge_band.dat')
print('shape',a.shape,c.shape); d=np.abs(a-c)
print('max |dE| all 16 bands (meV)',1e3*d.max(),' lowest 8+2 (meV)',1e3*d[:10].max())
PY
for r in A B; do grep -E 'Final Spread|Omega Total' $W/$r/Ge.wout | tail -1; done
echo OGTEST2_DONE
