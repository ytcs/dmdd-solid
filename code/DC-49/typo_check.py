"""Do the published curves contain the printed q_x^2 v_F,z^2? calc/pub with and without it (best halo)."""
import numpy as np, dirac as d, scatter as s
H=dict(rho=0.3e9/d.CM**3,v0=220*d.KMS,vesc=600*d.KMS,ve=232*d.KMS); RH=6.135*(1e-3*d.KG)/d.CM**3
for n,ov in (('BNQ',{}),('ZrTe5_exp',dict(v=(1.3e-3,6.5e-4,1.6e-3),Lam=(.07,.07,.07))),('ZrTe5_th',{})):
    pub=np.loadtxt(f'data/pub_scat_{n}.csv',delimiter=','); pub=pub[np.argsort(pub[:,0])]
    for typo in (False,True):
        p=d.setup(n,**ov); p['rhoT']=RH; p['typo']=typo; Bt=d.Btab(p); r=[]
        for m in (pub[:,0].min()*2,30,100,300,1000):
            o=s.event_integral(p,m*1e3,H,nth=16,nph=24,nq=32,nw=24,nt=12,Bt=Bt); r.append(3/o['src'].mean()/np.exp(np.interp(np.log(m),np.log(pub[:,0]),np.log(pub[:,1]))))
        print(n,'typo' if typo else 'fixed',' '.join('%.3f'%x for x in r),flush=True)
