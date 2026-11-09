"""Light mediator, Si, window T in [1e-7,1] GeV, Q<=5 keV: den/src for intermediate masses, flux from crdm.py (Eqs. 1-3 + Boschini fit)."""
import numpy as np, rate as R, recast as C, crdm
elf=R.ELF('Si/Si_gpaw_withLFE.dat',2.33); ws=np.r_[np.arange(5,24,.75),np.arange(24,50.1,2.)]
EX={4:63.03,5:65.56,6:67.73}
for mk in (1,1.5,2,3,5,7,10,30):
    m=mk*1e3; Tg=np.geomspace(1e-7,1,300); dP=crdm.flux(Tg,m*1e-9,'light')*1e-9   # per eV
    r,_=C.spectrum(elf,m,Tg*1e9,dP,'light',ws,Qhi=5e3)
    e=lambda y:sum(C.Zrates(ws,y)[z]*EX[z]*1e-3/365.25 for z in EX)
    a,b=e(r['src']),e(r['den']); print('m %g keV den/src %.4f sigma_src %.3g sigma_den %.3g'%(mk,b/a,1e-34*np.sqrt(2.3/a),1e-34*np.sqrt(2.3/b)),flush=True)
