import numpy as np, sys
sys.path.insert(0,'/home/user/dmdd-solid/book/figscripts/ch10')
from scipy.interpolate import RegularGridInterpolator
import abs10_7 as A
d=np.load('/home/user/dmdd-solid/book/figscripts/ch10/si_elf_binned.npz')
OM,QQ,LFt=d['omega'],d['q'],d['lf']
f=RegularGridInterpolator((OM,QQ),LFt,bounds_error=False,fill_value=0.)
def L(Q,w):
    Qc=np.clip(Q,QQ[0],None); v=f(np.c_[np.full_like(Q,w),Qc]); return np.where(Q<=QQ[-1],v,0.)
W=np.arange(1.11,89,0.05); EPS=A.eps_si(W)
def trans(w,eps,v,Qmin,Qmax):
    a,b=w*w*eps.real,w*w*eps.imag
    # analytic: (1/2) int_{x1}^{x2} dx (v^2 - w^2/x) b/((x-a)^2+b^2)
    x1,x2=Qmin**2,Qmax**2
    F1=lambda x: np.arctan((x-a)/b)
    # int b/(x((x-a)^2+b^2)) dx = [ ln x - 0.5 ln((x-a)^2+b^2) + (a/b) arctan((x-a)/b) ] * b/(a^2+b^2)
    F2=lambda x: (np.log(x)-0.5*np.log((x-a)**2+b**2)+(a/b)*np.arctan((x-a)/b))*b/(a*a+b*b)
    return 0.5*(v*v*(F1(x2)-F1(x1)) - w*w*(F2(x2)-F2(x1)))
for v in [0.1,0.3,0.5,0.9,0.99]:
    S=dict(sh=[],eh=[],sl=[],el=[],tr=[])
    for w,e in zip(W,EPS):
        qmin=w/v
        if qmin>=QQ[-1]:
            for k in S: S[k].append(0.); continue
        Q=np.geomspace(qmin,QQ[-1],3000); l=L(Q,w)
        S['sh'].append(np.trapezoid(Q**3*l,Q)); S['eh'].append(np.trapezoid(Q**3*l*(1-w*w/Q**2)**2,Q))
        S['sl'].append(np.trapezoid(Q**3*l/(Q*Q-w*w)**2,Q)); S['el'].append(np.trapezoid(l/Q,Q))
        S['tr'].append(trans(w,e,v,qmin,QQ[-1]))
    S={k:np.array(x) for k,x in S.items()}
    I=lambda y,m=slice(None): np.trapezoid(y[m],W[m])
    lo=W<2; pl=(W>10)&(W<20)
    print(f"v={v}: heavy {I(S['eh'])/I(S['sh']):.4f} light {I(S['el'])/I(S['sl']):.4f} tr/den all {I(S['tr'])/I(S['el']):.3e} <2eV {I(S['tr'],lo)/I(S['el'],lo):.3g} 10-20 {I(S['tr'],pl)/I(S['el'],pl):.3e}")
