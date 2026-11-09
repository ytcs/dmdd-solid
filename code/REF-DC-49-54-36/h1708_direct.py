"""Referee: direct quadrature of the PRINTED 1708.08929 Eqs. (RtotNoGap)+(IvFLambdaM) for the gapless ideal curve.
No W reduction, no use of DC-49 code. eta is built by brute-force from the boosted truncated Maxwellian."""
import numpy as np, sys
from numpy.polynomial.legendre import leggauss
ALPHA=1/137.035999; E2=4*np.pi*ALPHA; ME=510998.95; Q0=ALPHA*ME
CM=5.067731e4; KG=5.609589e35; YR=3.15576e7*1.519267e15; KMS=1/299792.458
def eta_table(v0=220*KMS,vE=232*KMS,vesc=550*KMS,n=4000):
    """eta(vmin)=int d3v/v g(v) theta(v-vmin), g(v) = angle-averaged lab distribution"""
    from scipy.special import erf
    # sample: galactic-frame speed u, angle; lab v=|u+vE|  -> speed pdf via 2D quadrature
    uu,wu=leggauss(600); u=.5*vesc*(uu+1); wu=wu*.5*vesc
    cc,wc=leggauss(400)
    f=np.exp(-u*u/v0**2)*u*u
    N=2*np.pi*np.sum(wu*f)*2
    v=np.sqrt(u[:,None]**2+vE**2+2*u[:,None]*vE*cc[None,:])
    W=(2*np.pi*wu*f/N)[:,None]*wc[None,:]
    vg=np.linspace(0,vesc+vE,n); h,_=np.histogram(v.ravel(),bins=vg,weights=(W/v).ravel())
    eta=np.r_[np.cumsum(h[::-1])[::-1],0.]
    return vg,eta
def Rate(m,v=4e-4,Lam=200.,g=2,kap=40.,neV=5e24*60e-30,rho=0.4e9/CM**3,eps='printed',nl=60,nc=60,nq=160,halo=None):
    vg,eta=halo or eta_table()
    mu=m*ME/(m+ME)
    xl,wl=leggauss(nl); l=.5*Lam*(xl+1); wl=.5*Lam*wl
    xc,wc=leggauss(nc); xq,wq=leggauss(nq)
    Lp=Lam*np.exp(12*np.pi**2*kap*v/(g*E2))
    I=0.
    for li,wi in zip(l,wl):
        for c,wcc in zip(xc,wc):
            qm=-li*c+np.sqrt(Lam**2-li**2*(1-c*c))
            # cluster at small q
            lq=.5*np.log(qm/1e-4)*(xq+1)+np.log(1e-4); q=np.exp(lq); wqq=.5*np.log(qm/1e-4)*wq*q
            lp=np.sqrt(li**2+q**2+2*li*q*c); om=v*(li+lp)
            vmin=om/q+q/(2*m)
            e=np.interp(vmin,vg,eta,right=0.)
            cosll=(li**2+li*q*c)/(li*lp)
            s=om**2/v**2-q**2
            if eps=='printed':   # Eq. (RdiffNoGap), Lambda' absorbs the 1
                den=np.log(np.abs(4*Lp**2/s))**2+np.pi**2
            elif eps=='gap':     # Delta->0 of Eq. (epsGap): add 5/3 to the log
                den=(np.log(np.abs(4*Lp**2/s))+5/3)**2+np.pi**2
            I+=wi*wcc*np.sum(wqq*li**2*q/(om**2-q**2)**2*e/den*(1-cosll))
    Vc=(1e-10*CM*0+1) # placeholder
    neV_eV=neV/(1e-3/1e-3)   # m^3/kg
    nV=neV*(100*CM)**3/KG     # eV^-3 . eV^-1 -> eV^-4
    pref=36*np.pi**2/E2**2*Q0**4*(rho/m)/mu**2*nV*kap**2/g*v**2
    return pref*I*CM**-2*0+pref*I   # per (eV^-2 of sigma) per eV.. rate per mass per sigma[eV^-2]
def sig3(m,**k):
    R=Rate(m,**k)            # eV^4... R[per mass, per time] with sigma in eV^-2
    # sigma[cm^2] = 3/(R * KG*YR) in eV^-2 -> cm^2
    s=3/(R*KG*YR)            # eV^-2
    return s/CM**2
if __name__=='__main__':
    pub=np.loadtxt('../DC-49/data/pub_h_gapless.csv',delimiter=','); H=eta_table()
    for mk in (5,10,30,100,300,1000):
        y=np.exp(np.interp(np.log(mk),np.log(pub[:,0]),np.log(pub[:,1])))
        a=sig3(mk*1e3,halo=H); b=sig3(mk*1e3,halo=H,eps='gap')
        print(mk,'pub %.3e printed-eq calc %.3e calc/pub %.3f | gap-form calc/pub %.3f'%(y,a,a/y,b/y),flush=True)
