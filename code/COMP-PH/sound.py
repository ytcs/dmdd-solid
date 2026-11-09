"""Sound speeds from acoustic slopes (matdyn on the q2r force constants). usage: sound.py MAT phdir alat"""
import sys, os, subprocess, numpy as np, json
m,d,al=sys.argv[1],sys.argv[2],float(sys.argv[3])
env=dict(os.environ,PATH='/root/mamba/envs/qe/bin:'+os.environ['PATH'])
dirs={'100':np.array([1,0,0.]),'110':np.array([1,1,0.])/np.sqrt(2),'111':np.array([1,1,1.])/np.sqrt(3)}
xs=[0.005,0.01,0.02]; pts=[v*x for v in dirs.values() for x in xs]
open(f"{d}/snd.in",'w').write(f"&input\n asr='crystal', flfrc='{m}.fc', flfrq='snd.freq', q_in_band_form=.false.\n/\n{len(pts)}\n"+''.join(f"{a:.8f} {b:.8f} {c:.8f}\n" for a,b,c in pts))
subprocess.run(['matdyn.x','-in','snd.in'],cwd=d,env=env,stdout=open(f"{d}/snd.out",'w'),check=True)
t=open(f"{d}/snd.freq").read().split('\n'); nb=int(t[0].split('nbnd=')[1].split(',')[0]); tok=' '.join(t[1:]).split()
w=np.array([float(x) for x in tok[:len(pts)*(4+nb)]]).reshape(len(pts),4+nb)[:,4:]  # cm-1
out={}
for i,(k,v) in enumerate(dirs.items()):
    for j,x in enumerate(xs):
        Q=x*2*np.pi/(al*0.529177e-10); om=w[i*len(xs)+j,:3]*2*np.pi*2.99792458e10
        out.setdefault(k,[]).append([x]+list(np.round(om/Q/1e3,4)))  # km/s
for k,v in out.items(): print(k,v)
json.dump(out,open(f"{d}/sound.json",'w'),indent=1)
