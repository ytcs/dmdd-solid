"""Direct DFT masses (no Wannier): bands calculation at explicit k around L and Gamma, alpha 1.0, k8e80 charge."""
import numpy as np, re, sys, subprocess, os
W='/home/ytc/paer-work/work/DC-2-alpha'; os.chdir(W)
L=np.array([.5,.5,.5]); G=np.zeros(3)
D={'ml':(L,[1,1,1]),'mt':(L,[1,-1,0]),'mG':(G,[1,0,0])}; hs=[.02,.04]
ks=[]; idx={}
for n,(k0,u) in D.items():
    u=np.array(u,float)/np.linalg.norm(u)
    idx[n,0]=len(ks); ks.append(k0)
    for h in hs:
        for s in (1,-1): idx[n,h,s]=len(ks); ks.append(k0+s*h*u)
t=open('k8e80.a1.0.in').read().replace("calculation='scf'","calculation='bands'").replace(", startingpot='file'","").replace("nbnd=36","nbnd=32")
i=t.index('K_POINTS'); hub=t[i:][t[i:].index('HUBBARD'):]
open('dm.in','w').write(t[:i]+f"K_POINTS tpiba\n{len(ks)}\n"+''.join(f"{a:.6f} {b:.6f} {c:.6f} 1\n" for a,b,c in ks)+hub)
env=dict(os.environ,OMP_NUM_THREADS='1',PATH='/home/ytc/paer-work/mamba/envs/qe/bin:'+os.environ['PATH'])
subprocess.run('mpirun --mca btl self,vader -np 3 pw.x -in dm.in > dm.out 2>/dev/null',shell=True,env=env)
s=open('dm.out',errors='ignore').read(); s=s[s.rfind('End of band'):]
B=re.findall(r'k =\s*(-?[\d.]+)\s*(-?[\d.]+)\s*(-?[\d.]+)\s*\(.*?\n\n(.*?)\n\n',s,flags=re.S)
E=[[float(x) for x in re.findall(r'-?\d+\.\d+',b[3])] for b in B]; print(len(E),len(ks))
RY=13.605693; t2=2*np.pi/10.692
for n in D:
    for h in hs:
        c=(E[idx[n,h,1]][28]+E[idx[n,h,-1]][28]-2*E[idx[n,0]][28])/(h*t2)**2
        print(n,'h',h,'m*',round(2*RY/c,4))
