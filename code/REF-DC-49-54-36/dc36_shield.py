"""Referee: factor by which a closed can (rho=8) reduces the Born fluctuation force of 2512.16451 at the published 20 eV point (u=420), wind on axis; first-entry filter, slab R_slab at the can, inner reflections ignored."""
import numpy as np, dc36_indep as I
c=299792.458; EVM=5.067731e6; xi=2e-6*EVM
rng=np.random.default_rng(5); N=2000000
def fac(u,m,R=45.,H=50.,rho=8.):
    v=I.sample(N,0.,0.,rng); sp=np.linalg.norm(v,axis=1); d=v/sp[:,None]
    # entry face of a cylinder for a parallel beam: end cap with weight |d_z| pi R^2, side with weight 2 R 2H sqrt(1-d_z^2)
    wE=np.abs(d[:,2])*np.pi*R*R; wS=2*R*2*H*np.sqrt(1-d[:,2]**2); pE=wE/(wE+wS)
    end=rng.random(N)<pE
    ph=np.arcsin(2*rng.random(N)-1)     # incidence azimuth on the side wall, uniform impact parameter
    vperp=np.hypot(v[:,0],v[:,1]); vn=np.where(end,np.abs(v[:,2]),vperp*np.cos(ph))
    T=1-I.Rslab(vn,np.sqrt(u*u*rho/I.NREF))
    k=m*sp/c; Y=4*k*k*xi*xi; Iq=(np.log(1+Y)-Y/(1+Y))/(k**4)
    w=sp*k*(v[:,2]/sp)*Iq
    return (T*w).mean()/w.mean(), T.mean()
for u in (300,365,420,500,560,590): print(u,'fluctuation-force factor %.3g, number transmitted %.3g'%fac(u,20.))
