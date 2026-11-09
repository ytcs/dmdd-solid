import numpy as np
from scipy.special import erf
d=np.load('/home/user/dmdd-solid/book/figscripts/ch10/si_elf_binned.npz')
W,Qg=d['omega'],d['q']
c=299792.458; v0,ve,vesc=238/c,250.5/c,544/c
z=vesc/v0; N=np.pi**1.5*v0**3*(erf(z)-2/np.sqrt(np.pi)*z*np.exp(-z*z))
def eta(u):  # standard closed form (Savage/McCabe) with galactic escape cut
    u=np.asarray(u,float); k=np.pi*v0**2/(ve*N)
    r=np.zeros_like(u)
    a=u<vesc-ve; b=(u>=vesc-ve)&(u<vesc+ve)
    r[a]=k*(np.sqrt(np.pi)*v0/2*(erf((u[a]+ve)/v0)-erf((u[a]-ve)/v0))-2*ve*np.exp(-z*z))
    r[b]=k*(np.sqrt(np.pi)*v0/2*(erf(z)-erf((u[b]-ve)/v0))-(vesc+ve-u[b])*np.exp(-z*z))
    return r
print('eta0',eta(np.array([0.0])))
me=510998.95; al=1/137.035999177; q0=al*me
hbarc=1973.269804; Om=5.431**3/4/hbarc**3
Mc=2*28.0855*931.49410242e6
def pref(m):
    mu=m*me/(m+me)
    return 0.3e9/m*1e-37*2.99792458e10*al*me**2/mu**2/(Mc/5.609588603e35)*365.25*86400
def rate(m,key,light=False,wth=1.11,qmin=None,qmax=None,retq=False):
    Q,Ww=np.meshgrid(Qg,W,indexing='xy')  # shape (nw,nq)
    vm=Ww/Q+Q/(2*m); e=eta(vm)
    F2=(q0/Q)**4 if light else 1
    integ=Q**3*e*F2*d[key]
    mask=(Ww>=wth)
    if qmin is not None: mask&=Q>qmin
    if qmax is not None: mask&=Q<qmax
    I=np.trapezoid(np.trapezoid(integ*mask,Qg,axis=1),W)
    return pref(m)*Om/(8*np.pi**2*al**2*me**2)*I
for m in [1e6,10e6,100e6]:
    for lt in [False,True]:
        r={k:rate(m,k,lt) for k in ['ip','rpa','lf']}
        print(f"m={m/1e6:g} MeV light={lt}: IP {r['ip']:.4g} RPA {r['rpa']:.4g} LF {r['lf']:.4g}  IP/LF {r['ip']/r['lf']:.3g} RPA/LF {r['rpa']/r['lf']:.3g} IP/RPA {r['ip']/r['rpa']:.3g}")
m=10e6; tot=rate(m,'lf'); print('LF share q>6.7keV',rate(m,'lf',qmin=6700)/tot,' q>2q0',rate(m,'lf',qmin=2*q0)/tot,' q>15keV',rate(m,'lf',qmin=15000)/tot)
print('e2lf/LF ratio (KKL comparison) heavy/light 10,100 MeV:',[round(rate(mm,'e2lf',lt)/rate(mm,'lf',lt),3) for mm in [10e6,100e6] for lt in [False,True]])
