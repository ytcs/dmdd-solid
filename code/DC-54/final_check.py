"""R_Z of Fig. 3 right in the window T>=1e-7 GeV, Q<=5 keV; Ge ratios; Cherenkov (eta) scan; epsT numbers."""
import numpy as np, rate as R, recast as C, epsT, json
pl=np.loadtxt('data/pub_dRdw_light.csv',delimiter=','); ws=pl[:,0]
yl=[253.5,208.0,126.3,77.7,82.7,135.4,214.7,282.3,318.0,337.3]; yh=[327.2,296.9,257.1,231.4,212.5,203.8,205.7,214.6,225.6,238.8]
RZl=[10**(-(y-93.18)/123.03) for y in yl]; RZh=[10**(-(y-93.18)/123.03)/100 for y in yh]
elf=R.ELF('Si/Si_gpaw_withLFE.dat',2.33); ge=R.ELF('Ge/Ge_gpaw_withLFE.dat',5.32); ET=epsT.EpsT(elf,16.6); EG=epsT.EpsT(ge,16.)
E_,P=C.PZ()
wf=np.r_[np.arange(1.2,10,.4),np.arange(10,24,.5),np.arange(24,50.1,1.)]
for med,RZ in (('light',RZl),('heavy',RZh)):
    T,dP=R.flux_grid('1keV',med,n=420); k=T>=100; r,_=C.spectrum(elf,1e3,T[k],dP[k],med,wf,Qhi=5e3)
    z=[np.trapezoid(np.interp(wf,E_,P[:,i],left=0,right=0)*r['src'],wf) for i in range(10)]
    print('R_Z calc/pub',med,' '.join('%.2f'%(a/b) for a,b in zip(z,RZ)),flush=True)
print('P(Z|w)>1e-3 onset:',{Z:float(E_[np.argmax(P[:,Z-1]>1e-3)]) for Z in (3,4,5,6)})
w=np.array([1.5,2,2.5,3,3.3,3.5,4,5,8,12,16]); print('Si Re eps(0,w)',np.round(elf.eps(w,0*w).real,2)); print('Si Im eps(0,w)',np.round(elf.eps(w,0*w).imag,2))
# eta scan on the 1 keV light transverse increment, T>=100
T,dP=R.flux_grid('1keV','light',n=300); k=T>=100; wz=np.arange(4,24,1.)
for eta in (0.,.01,.1):
    class E2:
        def __call__(s,w,Q): return ET(w,Q)+1j*eta
    r,_=C.spectrum(elf,1e3,T[k],dP[k],'light',wz,Qhi=5e3,ET=E2()); print('eta',eta,'tr/den(4-24 eV) %.5f'%(np.trapezoid(r['tr'],wz)/np.trapezoid(r['den'],wz)),'at w=4: %.4f w=8: %.4f'%(r['tr'][0]/r['den'][0],r['tr'][4]/r['den'][4]),flush=True)
for lab,m in (('1keV',1e3),('10keV',1e4),('me',R.ME)):
    for med in ('light','heavy'):
        T,dP=R.flux_grid(lab,med,n=420); k=T>=100; r,_=C.spectrum(ge,m,T[k],dP[k],med,wf,Qhi=5e3,ET=EG)
        print('Ge',lab,med,'T>=100,Q<=5k: den/src %.4f tr/den %.5f'%(np.trapezoid(r['den'],wf)/np.trapezoid(r['src'],wf),np.trapezoid(r['tr'],wf)/np.trapezoid(r['den'],wf)),flush=True)
