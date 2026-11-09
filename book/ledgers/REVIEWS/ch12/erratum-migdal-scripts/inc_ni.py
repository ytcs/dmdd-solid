import numpy as np, sys
sys.path.insert(0,'..'); sys.path.insert(0,'.')
from coh import *
NK=4
ks=mesh(NK); base=[solve(k) for k in ks]
rng=np.random.default_rng(7)
Ks=(rng.random((40,3)))@B        # random K over a primitive cell of reciprocal lattice = zone average
sd=0.; sf=0.; n=0
for K in Ks:
    for (ev,cv,Iv),k in zip(base,ks):
        ec,cc,Ic=solve(k+K)
        R=rho(ev,cv,Iv,ec,cc,Ic)
        p=K+GG; pn=np.linalg.norm(p,axis=1)
        a=wcb.w(pn)/Omega
        dE=ec[NV:,None]-ev[None,:NV]
        sd+=np.sum(np.einsum('g,gcv->cv',pn**2*a**2,abs(R)**2)/dE**4)/3
        f=0.
        for s in (+1,-1):
            ph=np.exp(-1j*s*(GG@tau))
            amp=np.einsum('ga,g,gcv->acv',p,a*ph,R)
            f+=0.5*np.sum(abs(amp)**2/dE**4)/3
        sf+=f; n+=1
print('zone-averaged incoherent per q^2 (keV units as run_coh): diag %.4e full %.4e full/diag %.3f'%(sd/n/KEV_PER_AU**-2*0+sd/n*KEV_PER_AU**-2, sf/n*KEV_PER_AU**-2, sf/sd))
