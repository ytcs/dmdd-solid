#!/usr/bin/env bash
# Delta-line conduction minimum at the last alpha of the k8e80 scan (alpha 1.0). Bands along Gamma-X, 0.70-1.00 X.
W=/home/ytc/paer-work/work/DC-2-alpha; cd $W
export PATH=/home/ytc/paer-work/mamba/envs/qe/bin:$PATH OMP_NUM_THREADS=1
while ! grep -q SCAN_DONE scan2.log; do sleep 20; done
python3 - <<'PY'
t=open('k8e80.a1.0.in').read()
t=t.replace("calculation='scf'","calculation='bands'").replace(", startingpot='file'","")
i=t.index('K_POINTS'); h=t[i:]; body=t[:i]; hub=h[h.index('HUBBARD'):]
ks=[0.70+0.02*j for j in range(16)]
kb="K_POINTS tpiba\n%d\n"%(len(ks)+1)+"0 0 0 1\n"+''.join(f"{x:.3f} 0 0 1\n" for x in ks)
open('k8e80.dline.in','w').write(body+kb+hub)
PY
mpirun --mca btl self,vader -np 2 pw.x -in k8e80.dline.in > k8e80.dline.out 2>/dev/null
python3 - <<'PY'
import re
t=open('k8e80.dline.out',errors='ignore').read()
print(re.findall(r'Error in routine.*\n.*',t)[:1])
B=re.findall(r'k =\s*(-?[\d.]+)\s*(-?[\d.]+)\s*(-?[\d.]+)\s*\(.*?\n\n(.*?)\n\n',t[t.rfind('End of band'):],flags=re.S)
r=[(float(k[0]),[float(x) for x in re.findall(r'-?\d+\.\d+',k[3])]) for k in B]
v=r[0][1][27]
for x,e in r[1:]: print(f'{x:.2f} {e[28]-v:.4f}')
m=min((e[28]-v,x) for x,e in r[1:]); print('DELTA_MIN',m)
PY
echo DLINE_DONE
