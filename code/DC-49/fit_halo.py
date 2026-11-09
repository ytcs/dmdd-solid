"""Halo constants are unstated in 1910.02091. Candidate round sets vs the four published curves; scale not fitted."""
import numpy as np, dirac as d, scatter as s
OV={'ZrTe5_th':{},'ZrTe5_exp':dict(v=(1.3e-3,6.5e-4,1.6e-3),Lam=(.07,.07,.07)),'BNQ':{},'Yb':dict(g=12)}
RHOFIX=6.135*(1e-3*d.KG)/d.CM**3
P={};B={};PUB={}
for n in OV:
    P[n]=d.setup(n,**OV[n]); P[n]['rhoT']=RHOFIX; B[n]=d.Btab(P[n]); a=np.loadtxt(f'data/pub_scat_{n}.csv',delimiter=','); PUB[n]=a[np.argsort(a[:,0])]
for v0,ve,vesc in [(220,244,550),(220,244,544),(220,250,544),(220,240,550),(220,232,600),(220,240,600),(225,240,544),(225,244,544),(220,247,544),(230,232,544),(220,255,533),(220,235,560)]:
    h=dict(rho=.3e9/d.CM**3,v0=v0*d.KMS,vesc=vesc*d.KMS,ve=ve*d.KMS); line=[];w=0
    for n in OV:
        mth=PUB[n][:,0].min(); ms=np.geomspace(mth*1.5,1000,12); r=[]
        for mk in ms:
            N=s.event_integral(P[n],mk*1e3,h,nth=12,nph=18,nq=28,nw=20,nt=12,Bt=B[n])['src'].mean()
            r.append(3/N/np.exp(np.interp(np.log(mk),np.log(PUB[n][:,0]),np.log(PUB[n][:,1]))))
        r=np.array(r); w=max(w,np.abs(np.log(r)).max()); line.append('%s %.3f..%.3f rms %.3f'%(n[:7],r.min(),r.max(),np.sqrt(np.mean(np.log(r)**2))))
    print((v0,ve,vesc),'max|ln r|=%.3f'%w,' | '.join(line),flush=True)
