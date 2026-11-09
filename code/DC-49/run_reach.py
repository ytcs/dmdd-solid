"""DC-49 production run. Writes results/reach_<mat>.csv, abs_<mat>.csv, summary.json."""
import numpy as np, dirac as d, scatter as s, absorption as A, json, os, sys, time
os.makedirs('results',exist_ok=True)
H=dict(rho=0.3e9/d.CM**3,v0=220*d.KMS,vesc=600*d.KMS,ve=232*d.KMS)   # best of fit_halo.py
OV={'ZrTe5_th':{},'ZrTe5_exp':dict(v=(1.3e-3,6.5e-4,1.6e-3),Lam=(.07,.07,.07)),'BNQ':{},'Yb':dict(g=12)}
RHOFIX=6.135*(1e-3*d.KG)/d.CM**3
summ={}
for n in OV:
    p=d.setup(n,**OV[n]); p['rhoT']=RHOFIX; Bt=d.Btab(p)
    pub=np.loadtxt(f'data/pub_scat_{n}.csv',delimiter=','); pub=pub[np.argsort(pub[:,0])]
    mth=pub[:,0].min()
    ms=np.unique(np.r_[mth*np.array([1.1,1.25,1.5,2,3]),np.geomspace(mth*4,1000,10)])
    rows=[]
    for mk in ms:
        o=s.event_integral(p,mk*1e3,H,Bt=Bt)
        N={r:o[r].mean() for r in o}
        y=np.exp(np.interp(np.log(mk),np.log(pub[:,0]),np.log(pub[:,1])))
        rows.append([mk,y,3/N['src'],3/N['src']/y,N['src']/N['URF'],N['src']/N['URFo'],N['URF']/N['lead'],y*N['src']/N['URF'],s.mod_amp(o['src']),s.mod_amp(o['URF']),N['src']/N['bare']])
        print(n,' '.join('%.4g'%x for x in rows[-1]),flush=True)
    rows=np.array(rows)
    np.savetxt(f'results/reach_{n}.csv',rows,delimiter=',',header='m[keV],sigma_pub,sigma_calc_src,calc/pub,Nsrc/NURF,Nsrc/NURFo,NURF/Nlead,sigma_URF,A_src,A_URF,Nsrc/Nbare')
# convergence
p=d.setup('ZrTe5_th'); p['rhoT']=RHOFIX; Bt=d.Btab(p); c=[]
for kw in (dict(),dict(nth=48,nph=72,nq=64,nw=48,nt=48)):
    t=time.time(); o=s.event_integral(p,50e3,H,Bt=Bt,**kw); c.append((o['src'].mean(),o['URF'].mean(),time.time()-t))
print('conv',c, c[1][0]/c[0][0],c[1][1]/c[0][1])
p=d.setup('BNQ'); p['rhoT']=RHOFIX; Bt=d.Btab(p); c=[]
for kw in (dict(),dict(nth=48,nph=72,nq=64,nw=48,nt=48)):
    o=s.event_integral(p,10e3,H,Bt=Bt,**kw); c.append((o['src'].mean(),o['URF'].mean()))
print('conv BNQ',c[1][0]/c[0][0],c[1][1]/c[0][1])
# absorption
OVA={'ZrTe5_th':{},'ZrTe5_exp':{},'BNQ':{},'Yb':{}}
for n in OVA:
    p=d.setup(n); pub=np.loadtxt(f'data/pub_abs_{n}.csv',delimiter=',')
    pub=pub[(pub[:,1]<1e-14)&(pub[:,0]>2*p['D']*1.3)&(pub[:,0]<2*p['EL']*.98)]; sel=pub[::max(1,len(pub)//40)]
    m=sel[:,0]
    es=A.eps_lim(p,m,'src'); eu=A.eps_lim(p,m,'URF'); el=A.eps_lim(p,m,'lead')
    np.savetxt(f'results/abs_{n}.csv',np.c_[m,sel[:,1],es,es/sel[:,1],eu/es,sel[:,1]*eu/es,(eu/el)**-2],delimiter=',',header='m[eV],eps_pub,eps_calc_src,calc/pub,eps_URF/eps_src,eps_URF(pub-scaled),Gam_URF/Gam_lead')
    print('abs',n,'calc/pub %.4f..%.4f  eps factor %.3f..%.3f  URF/lead %.3f..%.3f'%((es/sel[:,1]).min(),(es/sel[:,1]).max(),(eu/es).min(),(eu/es).max(),((eu/el)**-2).min(),((eu/el)**-2).max()),flush=True)
