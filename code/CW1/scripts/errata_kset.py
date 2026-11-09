"""ERR-CW1: k set for the errata reruns (fractional 2pi/a, the same fractional points at a_exp as in CW1 pass 5 / vertex_soc).
 (a) Gamma, the on-axis extremum k_c = 0.8429 X, the on-axis 1.39 keV pair (0.052 / 0.6609);
 (b) 3x3x3 stencils (step h = 0.02) around the hole k_h and the electron k_e = k_h + q of the Wannier joint optimum (out/emin_fast.json);
 (c) the q* = 0.90 keV joint optimum (Wannier, re-minimised here over q-hat and k at |q| = 0.90 keV; out/emin_qstar.json has only E, theta).
usage: errata_kset.py kfile labels.json"""
import numpy as np, sys, json, itertools, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wannier_si import bands, sc, kc, tpiba, nv
from scipy.optimize import minimize
H=os.path.dirname(os.path.abspath(__file__)); F=json.load(open(f'{H}/../out/emin_fast.json'))
kh=np.array(F['k_v']); ke=kh+np.array(F['q_vec_2pi_a']); h=0.02
K=1/(3.7289*tpiba); pairE=lambda k,q: bands((k+q)[None])[0,nv]-bands(k[None])[0,nv-1]+sc
sph=lambda t,p: np.array([np.cos(t),np.sin(t)*np.cos(p),np.sin(t)*np.sin(p)])
best=None
for t0,p0 in [(0.3356,0),(0.3,0.05),(0.36,-0.05)]:
    f=lambda x: pairE(x[2:],sph(x[0],x[1])*0.9*K)
    r=minimize(f,np.r_[t0,p0,-0.22*(sph(t0,p0)*0.9*K-kc)],method='Nelder-Mead',options=dict(xatol=1e-8,fatol=1e-10,maxiter=20000,maxfev=20000,adaptive=True))
    if best is None or r.fun<best[0]: best=(r.fun,r.x)
qs=sph(best[1][0],best[1][1])*0.9*K; khs=best[1][2:]
pts=[('G',[0,0,0]),('kc',[0.8429,0,0]),('axv',[0.052,0,0]),('axc',[0.6609,0,0])]
for s in itertools.product((-1,0,1),repeat=3): pts.append((f'h{s[0]:+d}{s[1]:+d}{s[2]:+d}',list(kh+h*np.array(s))))
for s in itertools.product((-1,0,1),repeat=3): pts.append((f'e{s[0]:+d}{s[1]:+d}{s[2]:+d}',list(ke+h*np.array(s))))
pts+= [('qsv',list(khs)),('qsc',list(khs+qs))]
open(sys.argv[1],'w').write(f"{len(pts)}\n"+'\n'.join(f"{k[0]:.10f} {k[1]:.10f} {k[2]:.10f} 1" for _,k in pts)+'\n')
json.dump(dict(labels=[l for l,_ in pts],h=h,k_h=kh.tolist(),k_e=ke.tolist(),qstar=dict(E_wannier=float(best[0]),theta=float(best[1][0]),q=qs.tolist(),k_v=khs.tolist())),open(sys.argv[2],'w'),indent=1)
print(len(pts),best[0],best[1][:2])
