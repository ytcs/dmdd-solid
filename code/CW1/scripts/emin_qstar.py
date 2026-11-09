"""IF to WP8-F G-F5: E_min^{ZPL}(|q|) minimised over q-hat AND k (joint Nelder-Mead from tilted starts in the {001} and {011} planes and
[210], [111]) at |q| = 0.90 keV (the PAER-edge q*, COMP-PH §4) and 1.0, 1.1 keV; Wannier TB of COMP-PH (a_PBE). usage: emin_qstar.py out.json"""
import numpy as np, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from wannier_si import bands, sc, kc, tpiba, nv
from scipy.optimize import minimize
K=1/(3.7289*tpiba)
pairE=lambda k,q: bands((k+q)[None])[0,nv]-bands(k[None])[0,nv-1]+sc
def sph(t,p): return np.array([np.cos(t),np.sin(t)*np.cos(p),np.sin(t)*np.sin(p)])
res={}
for qk in (0.90,1.00,1.10):
    best=None
    for t0,p0 in [(0,0),(0.2,0),(0.35,0),(0.5,0),(0.2,np.pi/4),(0.46,0),(0.62,np.pi/4),(0.3,0.3)]:
        f=lambda x: pairE(x[2:],sph(x[0],x[1])*qk*K)
        x0=np.r_[t0,p0,-0.22*(sph(t0,p0)*qk*K-kc)]
        r=minimize(f,x0,method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-8,maxiter=20000,maxfev=20000,adaptive=True))
        if best is None or r.fun<best[0]: best=(r.fun,r.x)
    res[str(qk)]=dict(Emin=float(best[0]),theta=float(best[1][0]),phi=float(best[1][1]%(2*np.pi)),E_axis=float(minimize(lambda k: pairE(k,np.array([qk*K,0,0])),-0.22*(np.array([qk*K,0,0])-kc),method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-8,maxiter=6000)).fun))
    print(qk,res[str(qk)],flush=True)
json.dump(res,open(sys.argv[1],'w'),indent=1)
