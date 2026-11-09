import numpy as np, dc54_int as D
D54='../DC-54/data/'
pl=np.loadtxt(D54+'pub_dRdw_light.csv',delimiter=','); ph=np.loadtxt(D54+'pub_dRdw_heavy_x100.csv',delimiter=','); ws=pl[:,0]; s=(ws>5)&(ws<30)
elf=D.ELF('Si/Si_gpaw_withLFE.dat',2.33)
Tl,dl=D.flux_csv(D54+'pub_flux_light_1keV.csv'); Th,dh=D.flux_csv(D54+'pub_flux_heavy_1keV.csv')
print('heavy level vs T-grid n (Q<=5k):')
for n in (420,840,1500,4000):
    T,d=D.flux_csv(D54+'pub_flux_heavy_1keV.csv',n=n); y,_=D.rate(elf,1e3,T,d,'heavy',ws,Qhi=5e3); rr=y[s]*100/ph[s,1]; print(n,'int %.4f mean(5-30) %.4f rms %.4f'%(np.trapezoid(y*100,ws)/np.trapezoid(ph[:,1],ws),np.exp(np.log(rr).mean()),np.log(rr).std()),flush=True)
y,_=D.rate(elf,1e3,Th,dh,'heavy',ws,Qhi=5e3,nQ=6000); print('nQ=6000 int %.4f'%(np.trapezoid(y*100,ws)/np.trapezoid(ph[:,1],ws)))
print('light Tlo fine, Q<=5k; ratio calc/pub at omega ~ 8,12,15,17,20,24,28')
idx=[np.argmin(abs(ws-x)) for x in (8,12,15,17,20,24,28)]
for Tlo in (25,28,30,32,35,40,45):
    k=Tl>=Tlo; y,yd=D.rate(elf,1e3,Tl[k],dl[k],'light',ws,Qhi=5e3); r=y/pl[:,1]; rr=np.log(r[s])
    print(Tlo,'int %.3f mean %.3f rms %.3f R(Z4-6) %.4f |'%(np.trapezoid(y,ws)/np.trapezoid(pl[:,1],ws),np.exp(rr.mean()),rr.std(),D.events(ws,yd)/D.events(ws,y)),' '.join('%.2f'%r[i] for i in idx),flush=True)
print('2D (Tlo,Qlo): int, shape rms')
for Tlo in (20,30,40,60,100):
  for Qlo in (100,200,250,300,350):
    k=Tl>=Tlo; y,yd=D.rate(elf,1e3,Tl[k],dl[k],'light',ws,Qlo=Qlo,Qhi=5e3,nQ=500); rr=np.log(np.maximum(y[s],1e-300)/pl[s,1])
    print(Tlo,Qlo,'int %.3f rms %.3f R %.4f'%(np.trapezoid(y,ws)/np.trapezoid(pl[:,1],ws),rr.std(),D.events(ws,yd)/D.events(ws,y)),flush=True)
