import numpy as np, dc54_int as D
D54='../DC-54/data/'
pl=np.loadtxt(D54+'pub_dRdw_light.csv',delimiter=','); ph=np.loadtxt(D54+'pub_dRdw_heavy_x100.csv',delimiter=','); ws=pl[:,0]; s=(ws>5)&(ws<30)
elf=D.ELF('Si/Si_gpaw_withLFE.dat',2.33)
Tl,dl=D.flux_csv(D54+'pub_flux_light_1keV.csv'); Th,dh=D.flux_csv(D54+'pub_flux_heavy_1keV.csv')
print('T range of the Fig.2 vector path [GeV]:',Tl[0]/1e9,Tl[-1]/1e9)
a=np.loadtxt(D54+'pub_flux_light_1keV.csv',delimiter=','); r=np.diff(np.log10(a[:,0])); print('path log10 steps: mean %.5f std %.2e n=%d  (logspace(-8,0,100) gives %.5f)'%(r.mean(),r.std(),len(a),8/99))
def rep(tag,y,yd,pub,sc=1):
    y=y*sc; yd=yd*sc; rr=np.log(np.maximum(y[s],1e-300)/pub[s,1])
    print(tag,'int %.3f rms(about mean) %.3f rms(abs) %.3f den/src(int) %.4f | Z3-6 %.4f Z4-6 %.4f'%(np.trapezoid(y,ws)/np.trapezoid(pub[:,1],ws),rr.std(),np.sqrt(np.mean(rr**2)),np.trapezoid(yd,ws)/np.trapezoid(y,ws),D.events(ws,yd,(3,4,5,6))/D.events(ws,y,(3,4,5,6)),D.events(ws,yd)/D.events(ws,y)),flush=True)
print('--- cross-check vs DC-54 window'); k=Tl>=100; y,yd=D.rate(elf,1e3,Tl[k],dl[k],'light',ws,Qhi=5e3); rep('light T>=1e-7 Q<=5k',y,yd,pl)
k=Th>=100; y,yd=D.rate(elf,1e3,Th[k],dh[k],'heavy',ws,Qhi=5e3); rep('heavy T>=1e-7 Q<=5k',y,yd,ph,100)
print('--- heavy: Q cap scan (all T)')
for Qh in (3e3,4e3,4.5e3,5e3,5.5e3,6e3,8e3,1e4,1.5e4,22.5e3):
    y,yd=D.rate(elf,1e3,Th,dh,'heavy',ws,Qhi=Qh); rep('heavy Qhi=%g'%Qh,y,yd,ph,100)
print('--- light: T_lo scan, Qlo=0, Qhi=5k')
for Tlo in (10,20,30,50,70,100,150):
    k=Tl>=Tlo; y,yd=D.rate(elf,1e3,Tl[k],dl[k],'light',ws,Qhi=5e3); rep('light Tlo=%g'%Tlo,y,yd,pl)
print('--- light: all T, Qlo scan (no T cut)')
for Qlo in (50,100,150,200,250,300,350,400,493):
    y,yd=D.rate(elf,1e3,Tl,dl,'light',ws,Qlo=Qlo,Qhi=5e3); rep('light allT Qlo=%g'%Qlo,y,yd,pl)
