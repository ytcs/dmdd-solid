"""PAER continuum edge mass: E^PA(q) = E_g + min over valleys ω_TA(K_val − q) (matdyn from 4^3 DFPT IFCs), reach condition
min_q [E^PA/q + q/2m] <= v_max; also with the exciton replica E_x = E_g − 14.7 meV. Writes matdyn input/output in cwd."""
import numpy as np, subprocess, json, sys
tp=1.1569120590283817; kc=0.85
def fib(n):
    i=np.arange(n)+0.5; th=np.arccos(1-2*i/n); ph=np.pi*(1+5**0.5)*i
    return np.stack([np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)],1)
dirs=fib(300); qA=np.arange(0.2,1.3,0.02)
Q=np.array([kc*np.array([1,0,0])-q/tp*d for q in qA for d in dirs])   # +x valley, units 2π/a (other valleys by symmetry for the min)
with open('md.in','w') as f:
    f.write("&input\n asr='crystal', flfrc='si444.fc', flfrq='md.freq', q_in_cryst_coord=.false.\n/\n%d\n"%len(Q))
    for x in Q: f.write('%.8f %.8f %.8f\n'%tuple(x))
subprocess.run('/root/mamba/envs/qe/bin/matdyn.x < md.in > md.out',shell=True,check=True)
L=open('md.freq').read().split('/',1)[1].split()
fr=np.array(L,float).reshape(-1,10)[:,4:]   # 4 coords (incl. path length) + 6 freqs (cm^-1) per q
wTA=fr[:,0].reshape(len(qA),len(dirs))*1.23984e-4   # eV
EPA=1.170+wTA.min(1); C=299792.458; vmax=794.5/C
def mreach(E):
    q=qA*1973.27
    for m in np.linspace(0.3e6,0.6e6,30001):
        if np.any(E/q+q/(2*m)<=vmax): return m/1e6
out=dict(m_PA_cont=mreach(EPA),m_PA_exc=mreach(EPA-0.0147),qA=qA.tolist(),wTAmin=wTA.min(1).tolist())
# frequencies at X and at K=0.85X for the record
json.dump(out,open(sys.argv[1],'w')); print(out['m_PA_cont'],out['m_PA_exc'])
