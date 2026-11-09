"""Referee: is the PRINTED 1708.08929 rate normalised correctly? Compare it with the loss-function route
dR/dw = rho_chi sigma/(4 pi m rho_T mu^2) Int q dq F^2 eta (2 q^2/e^2) kappa Im eps_r/|eps_r|^2 (CONVENTIONS sec. 8; Im eps_r printed, Eq. epsSM).
At m_chi = 10 keV the Lambda cut is never reached, so the two must agree exactly if the printed prefactor is right."""
import numpy as np, h1708_direct as H
from numpy.polynomial.legendre import leggauss
v=4e-4;Lam=200.;g=2;kap=40.;E2=H.E2
vg,eta=H.eta_table()
def R_elf(m,rho=.4e9/H.CM**3,neV=5e24*60e-30):
    mu=m*H.ME/(m+H.ME); A=E2*g/(24*np.pi**2*kap*v)
    vmax=vg[-1]; wmax=.5*m*vmax**2
    x,wx=leggauss(400); om=.5*wmax*(x+1); wo=.5*wmax*wx; tot=0
    for w,ww in zip(om,wo):
        # q range: vmin(q)=w/q+q/2m < vmax and w>v q
        qlo=m*vmax-np.sqrt(max((m*vmax)**2-2*m*w,0)); qhi=min(m*vmax+np.sqrt(max((m*vmax)**2-2*m*w,0)),w/v)
        if qhi<=qlo: continue
        y,wy=leggauss(300); lq=.5*np.log(qhi/qlo)*(y+1)+np.log(qlo); q=np.exp(lq); wq=.5*np.log(qhi/qlo)*wy*q
        e=np.interp(w/q+q/(2*m),vg,eta,right=0.)
        s=w**2/v**2-q**2
        epsr=1+A*(np.log(np.abs(4*Lam**2/s))+1j*np.pi)
        S=2*q**2/E2*kap*epsr.imag/np.abs(epsr)**2
        tot+=ww*np.sum(wq*q*(H.Q0/q)**4*e*S)
    nV=neV*(100*H.CM)**3/H.KG
    return rho*nV/(4*np.pi*m*mu**2)*tot
for mk in (5,10,20):
    a=H.Rate(mk*1e3,halo=(vg,eta)); b=R_elf(mk*1e3); print(mk,'keV printed/ELF-route = %.4f'%(a/b),flush=True)
