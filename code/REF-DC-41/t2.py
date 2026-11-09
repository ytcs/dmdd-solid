import numpy as np, spec as S
from scipy.optimize import brentq
print("Q  d=2-w_AB | P~(2^-) at d=1e-200,1e-100,1e-30 | d0 = 2-y0, zero of P~ in (w_AB,2) | P33(2-)")
out=[]
for Q in [0.5,1,2,3,4,4.5,5,5.13,5.3,5.64,6,6.41,7,7.69,8,9,10,12.82,16,20,25.64,40,100]:
    g=lambda t:S.avg_d(np.exp(t),Q)[2]
    tl,th=-690.0,np.log(1.999)
    if g(tl)*g(th)>0: print(Q,'UF same sign',g(tl),g(th)); continue
    t0=brentq(g,tl,th,xtol=1e-10); d=np.exp(t0)
    ptn=lambda t:S.Pt_d(np.exp(t),Q)[1]
    P2=[ptn(np.log(e)) for e in (1e-200,1e-100,1e-30)]
    ts=np.linspace(t0-1e-7,-690,900); v=np.array([ptn(t) for t in ts]); idx=np.where(v[:-1]*v[1:]<0)[0]
    z=None
    if len(idx): z=np.exp(brentq(ptn,ts[idx[0]+1],ts[idx[0]],xtol=1e-11))
    print(Q,'d=%.4g'%d,' '.join('%.5f'%p for p in P2),'d0=',z,flush=True)
