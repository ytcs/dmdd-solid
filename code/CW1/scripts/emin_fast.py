"""LE-24: Si zero-phonon kinematic edge m_ZPL = min over (q, k) of |q|^2 / [2(|q| v_max - (eps_c(k+q) - eps_v(k)))] on the COMP-PH Wannier TB
(PBE, a_PBE, scissor to E_g(0) = 1.170 eV). m is monotone in the pair energy at fixed q, so the joint 6-D minimum over (q, k) equals WP1-v3 [E13]
with E_min(q) = min_k (continuum edge). Also: E_min(|q|, theta) in the (001) and (011) tilt planes about [100] (joint min over k at fixed q).
usage: emin_fast.py out.json"""
import numpy as np, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from wannier_si import bands, sc, kc, tpiba, nv
from scipy.optimize import minimize
vmax=794.5/299792.458; K=1/(3.7289*tpiba)     # keV -> 2pi/a  (1 bohr^-1 = 3.7289 keV)
def pairE(k,q): return bands((k+q)[None])[0,nv]-bands(k[None])[0,nv-1]+sc
def m_of(x):
    q=x[:3]; qa=np.linalg.norm(q)/K*1e3
    den=qa*vmax-pairE(x[3:],q)
    return 1e9 if den<=0 else qa**2/(2*den)/1e6
best=[]
for qd in [(1,0,0),(1,.05,0),(1,.1,0),(1,.07,.07),(2,1,0),(1,.2,0),(1,.15,.15)]:
    for qk in (1.30,1.39,1.48):
        v=np.array(qd,float); v/=np.linalg.norm(v); q=v*qk*K; kv=-0.22*(q-kc)
        r=minimize(m_of,np.r_[q,kv],method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-9,maxiter=20000,maxfev=20000,adaptive=True))
        best.append((r.fun,r.x.tolist()))
best.sort(); f,x=best[0]; q=np.array(x[:3]); k=np.array(x[3:])
res=dict(scissor=float(sc),kc=list(map(float,kc)),m_ZPL=f,q_vec_2pi_a=list(q),q_keV=float(np.linalg.norm(q)/K),
         theta_rad=float(np.arccos(np.max(abs(q))/np.linalg.norm(q))),k_v=list(k),E_pair=float(pairE(k,q)),all=[b[0] for b in best])
print(json.dumps({a:b for a,b in res.items() if a!='all'},indent=1)); print('starts:',np.round(sorted(res['all']),5),flush=True)
def emin_q(q,k0):
    r=minimize(lambda k: pairE(k,q),k0,method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-8,maxiter=4000,adaptive=True)); return r.fun,r.x
scan={}
for qk in (1.20,1.30,1.39,1.48):
    for plane,u in (('001',np.array([0,1,0.])),('011',np.array([0,1,1.])/2**.5)):
        rows=[]
        for th in np.arange(0,0.41,0.025):
            v=np.cos(th)*np.array([1,0,0])+np.sin(th)*u; q=v*qk*K
            e=min(emin_q(q,k0)[0] for k0 in (-0.22*(q-kc),np.zeros(3)))
            rows.append((float(th),float(e),float((qk*1e3)**2/(2*(qk*1e3*vmax-e))/1e6)))
        scan[f'{qk}_{plane}']=rows
        print(qk,plane,' '.join(f'{t:.3f}:{e:.4f}' for t,e,_ in rows),flush=True)
res['scan']=scan; json.dump(res,open(sys.argv[1],'w'),indent=1)
