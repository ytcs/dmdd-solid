"""T-window study. (a) T_hi dependence of the Eq.(5) pole at m=1 keV; (b) reproduction and ratios in the Fig. 2 window T>=1e-7 GeV, Q<=5 keV,
for all three benchmark masses, Z=4..6 weighted; (c) quadrature convergence of the pole."""
import numpy as np, rate as R, recast as C, epsT, json
pl=np.loadtxt('data/pub_dRdw_light.csv',delimiter=','); ph=np.loadtxt('data/pub_dRdw_heavy_x100.csv',delimiter=',')
elf=R.ELF('Si/Si_gpaw_withLFE.dat',2.33); ET=epsT.EpsT(elf,16.6); ws=pl[:,0]; s=(ws>5)&(ws<30)
EX={3:57.71,4:63.03,5:65.56,6:67.73}
ev=lambda y:sum(C.Zrates(ws,y)[z]*EX[z]*1e-3/365.25 for z in (4,5,6))
out={}
T,dP=R.flux_grid('1keV','light',n=420)
print('(a) m=1keV light, T>=100 eV, Q<=5keV: T_hi, int(src)/pub, rms, den/src')
for Th in (1e5,1e6,1e7,1e8,3e8,1e9):
    k=(T>=100)&(T<=Th); r,_=C.spectrum(elf,1e3,T[k],dP[k],'light',ws,Qhi=5e3); y=r['src']
    print('%.0e %.3f rms %.3f den/src %.4f'%(Th,np.trapezoid(y,ws)/np.trapezoid(pl[:,1],ws),np.std(np.log(np.maximum(y[s],1e-300)/pl[s,1])),np.trapezoid(r['den'],ws)/np.trapezoid(y,ws)),' '.join('%.2f'%x for x in (y/pl[:,1])[8:44:6]),flush=True)
print('(c) convergence: nodes 160 -> 320, T grid 420 -> 840')
k=T>=100; r1,_=C.spectrum(elf,1e3,T[k],dP[k],'light',ws[::6],Qhi=5e3)
C.XQ,C.WQ=np.polynomial.legendre.leggauss(320); r2,_=C.spectrum(elf,1e3,T[k],dP[k],'light',ws[::6],Qhi=5e3)
T2,d2=R.flux_grid('1keV','light',n=840); k2=T2>=100; r3,_=C.spectrum(elf,1e3,T2[k2],d2[k2],'light',ws[::6],Qhi=5e3)
print(np.sum(r2['src'])/np.sum(r1['src']),np.sum(r3['src'])/np.sum(r1['src']),np.sum(r3['den'])/np.sum(r1['den']))
C.XQ,C.WQ=np.polynomial.legendre.leggauss(160)
print('(b) window T>=100 eV')
for lab,m in (('1keV',1e3),('10keV',1e4),('me',R.ME)):
    for med in ('light','heavy'):
        T,dP=R.flux_grid(lab,med,n=420)
        for nm,Tlo,kw in (('T>=100,Q<=5k',100.,dict(Qhi=5e3)),('T>=10,Q<=5k',0.,dict(Qhi=5e3)),('T>=100,all Q',100.,{})):
            k=T>=Tlo; r,_=C.spectrum(elf,m,T[k],dP[k],med,ws,ET=ET,**kw)
            e={q:ev(r[q]) for q in ('src','den','tr','trc')}
            o=dict(ev=e,den_src=e['den']/e['src'],tr_den=e['tr']/e['den'],trc_den=e['trc']/e['den'],sig_src=1e-34*np.sqrt(2.3/e['src']),sig_den=1e-34*np.sqrt(2.3/e['den']),sig_tr=1e-34*np.sqrt(2.3/e['tr']))
            out[f'{lab}|{med}|{nm}']=o; print(lab,med,nm,'ev456 src %.3g den/src %.4g tr/den %.4f trc/den %.4f sigma_src %.3g sigma_URF %.3g shift %.3g'%(e['src'],o['den_src'],o['tr_den'],o['trc_den'],o['sig_src'],o['sig_tr'],o['sig_tr']/o['sig_src']),flush=True)
json.dump(out,open('results/window.json','w'),indent=1)
