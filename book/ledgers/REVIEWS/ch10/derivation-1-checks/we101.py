import numpy as np,sys
sys.path.insert(0,'/home/user/dmdd-solid/book/figscripts/ch10')
from si_fcrys import load, DQ, DE
from scipy.integrate import quad
from scipy.special import erf
c=299792.458; v0,ve,vesc=238/c,250.5/c,544/c
# eta by direct numerical integration of truncated Maxwellian (galactic frame truncation), lab frame
def eta_num(vmin):
    # angle-average analytic in cos: f(v) speed dist in lab
    z=vesc/v0; N=np.pi**1.5*v0**3*(erf(z)-2/np.sqrt(np.pi)*z*np.exp(-z*z))
    def g(v): # int dOmega f, f ~ exp(-|v+ve|^2/v0^2) Theta(vesc-|v+ve|)
        # |v+ve|^2 = v^2+ve^2+2 v ve x ; x in [-1, xmax]
        xmax=min(1,(vesc**2-v*v-ve*ve)/(2*v*ve)) if v>0 else 1
        if xmax<-1: return 0
        a=2*v*ve/v0**2
        I=(np.exp(-(v*v+ve*ve)/v0**2)*(np.exp(-a*(-1))-np.exp(-a*xmax))/a)
        return 2*np.pi*I*v*v/N
    vm=vesc+ve
    if vmin>=vm: return 0
    return quad(lambda v: g(v)/v, max(vmin,1e-12), vm, limit=200)[0]
print('norm', quad(lambda v: (lambda vv: 0)(v),0,1)[0])
vs=np.linspace(0,(vesc+ve)*1.0001,4001); et=np.array([eta_num(x) for x in vs])
print('<1/v> =',et[0], ' (book 1041)')
q,E,f2=load()
me=510998.95; m=10e6; mu=m*me/(m+me); q0=me/137.035999177
Q,EE=np.meshgrid(q,E,indexing='ij')
vmin=EE/Q+Q/(2*m); eta=np.interp(vmin,vs,et,right=0)
mask=EE>=1.2-1e-9
for name,F2 in [('heavy',1.0),('light',(q0/Q)**4)]:
    integ=np.sum((eta*F2*f2/Q**2*DQ*DE)[mask])
    spec=np.sum(eta*F2*f2/Q**2*DQ,axis=0)
    mean=np.sum(spec*E)/np.sum(spec); pk=E[np.argmax(spec)]
    frac49=np.sum(spec[E<4.9-1e-9])/np.sum(spec)   # careful binning
    # q distribution
    qw=np.sum((eta*F2*f2/Q**2*DE)*mask,axis=1)
    fqlo=np.sum(qw[q<q0])/np.sum(qw); fqhi=np.sum(qw[q>2*q0])/np.sum(qw)
    ip=np.argmax(spec); qpk=q[np.argmax(eta[:,ip]*F2[:,ip] if np.ndim(F2) else eta[:,ip]*f2[:,ip]/q**2)] 
    print(name,'integral',round(integ,4),'peak',pk,'mean',round(mean,2),'frac<4.9',round(frac49,3),'q<q0',round(fqlo,3),'q>2q0',round(fqhi,3))
pref=30*1e-37*2.99792458e10*(me/mu)**2/137.035999177/(2*28.0855*931.49410242e6/5.609588603e35)*365.25*86400
print('pref',pref, (me/mu)**2, mu)
for name,F2 in [('heavy',1.0),('light',(q0/Q)**4)]:
    spec=np.sum(eta*F2*f2/Q**2*DQ,axis=0); spec[E<1.2-1e-9]=0
    for cut in [4.85,4.95,5.05]:
        print(name,cut,round(np.sum(spec[E<cut])/np.sum(spec),3))
    ip=np.argmax(spec); w=eta[:,ip]*(F2[:,ip] if np.ndim(F2) else 1)*f2[:,ip]/q**2
    print(' q peak at peak energy', q[np.argmax(w)]/q0, q[np.argmax(w)])
