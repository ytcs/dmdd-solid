import numpy as np, dirty as d, core as c
from scipy.optimize import brentq
print("dirty sum rules Q=5.64"); Q=5.64
for G in (3.7,):
    b=np.r_[2.0,2+np.geomspace(1e-5,1,24),np.geomspace(3.2,1e4,45)]
    w,wt=c.gl_panels(b,4)
    P=np.array([d.Pfull(a,Q,G)[1] for a in w])
    Dn=lambda y:d.Pfull(y,Q,G)[2]['D'].real
    yy=np.linspace(0.3,1.99,40); v=[Dn(y) for y in yy]; i=[j for j in range(39) if v[j]*v[j+1]<0][-1]
    wa=brentq(Dn,yy[i],yy[i+1],xtol=1e-7); h=1e-3*(2-wa); dD=(Dn(wa+h)-Dn(wa-h))/(2*h); x=d.Pfull(wa,Q,G)[2]; Z=(x['M'][3,2]*x['M'][2,3]).real/dD
    fs=(wt@(w*(-P.imag))+np.pi*Z*wa)/(np.pi*Q*Q/6); cs=(2/np.pi)*(wt@(-P.imag/w))+2*Z/wa
    print('Gam',G,'w_AB %.5f pole share %.4f f-sum %.4f compress %.4f  sub-2 Im P~ at y=1.5: %.2e'%(wa,np.pi*Z*wa/(np.pi*Q*Q/6),fs,cs,d.Pfull(1.5,Q,G)[1].imag),flush=True)
print("dirty AB velocity: w_AB vs (Q/sqrt3) sqrt(rho_s/rho), rho_s/rho ~ pi/(2 Gam) for Gam>>1")
for G,Q in ((124.,5.64),(124.,3.),(37.,3.)):
    Dn=lambda y:d.Pfull(y,Q,G)[2]['D'].real
    yy=np.linspace(0.05,1.9,12); v=[Dn(y) for y in yy]; i=[j for j in range(11) if v[j]*v[j+1]<0][-1]
    print(G,Q,brentq(Dn,yy[i],yy[i+1],xtol=1e-6),Q/3**.5*(np.pi/2/G)**.5,flush=True)
