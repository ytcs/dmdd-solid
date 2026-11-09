"""Does a lower T_chi limit (the Fig. 2 axis starts at 1e-7 GeV) reproduce Fig. 3? converged Q integral."""
import numpy as np, rate as R, recast as C
pl=np.loadtxt('data/pub_dRdw_light.csv',delimiter=','); ph=np.loadtxt('data/pub_dRdw_heavy_x100.csv',delimiter=',')
elf=R.ELF('Si/Si_gpaw_withLFE.dat',2.33); eln=R.ELF('Si/Si_gpaw_noLFE.dat',2.33); ws=pl[:,0]; s=(ws>5)&(ws<30)
for name,e in (('LFE',elf),('noLFE',eln)):
  for med,pub,sc,Qhi in (('light',pl,1,5e3),('heavy',ph,100,5e3)):
    T,dP=R.flux_grid('1keV',med,n=420)
    for Tlo in (50,80,100,120,150,200,300,500):
        k=T>=Tlo; r,_=C.spectrum(e,1e3,T[k],dP[k],med,ws,Qhi=Qhi)
        y=r['src']*sc; yy=r['den']*sc
        print(name,med,'Tlo',Tlo,'int ratio %.3f rms %.3f den/src %.4f'%(np.trapezoid(y,ws)/np.trapezoid(pub[:,1],ws),np.std(np.log(np.maximum(y[s],1e-300)/pub[s,1])),np.trapezoid(yy,ws)/np.trapezoid(y,ws)),' '.join('%.2f'%x for x in (y/pub[:,1])[8:44:6]),flush=True)
