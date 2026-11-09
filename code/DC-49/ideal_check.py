"""Size of the Re(delta eps) factor N_URF/N_lead (the '0.55-0.62' of WP4 5.4(i)) for the 1708.08929 ideal isotropic parameters and two cutoff schemes."""
import numpy as np, dirac as d, scatter as s
h=dict(rho=0.4e9/d.CM**3,v0=220*d.KMS,vesc=550*d.KMS,ve=232*d.KMS)
def mk(D,lnc,v=4e-4,kap=40.,g=2,Lam=200.):
    p=dict(v=np.array((v,)*3),D=D,Lam=np.array([Lam/d.ANG*1e0]*3),kap=np.array([kap]*3),g=g,rho=3.33,koff=dict(xy=(0,0),xz=(0,0),yz=(0,0)),lnc=lnc)
    p['vvv']=v**3; p['Lt']=Lam*v; p['EL']=np.sqrt(p['Lt']**2+D**2); p['rhoT']=1.; p['C']=g*d.E2/(4*np.pi**2*p['vvv']); p['ksym']=np.diag(p['kap']); return p
for D,lnc,lab in ((1e-6,0.,'gapless mu=2vL'),(1e-6,-5/3,'gapless e^{-5/3}'),(2.5e-3,0.,'gapped mu=2vL'),(2.5e-3,-5/3,'gapped e^{-5/3}')):
    p=mk(D,lnc); Bt=d.Btab(p); r=[]
    for m in (10e3,100e3,1000e3):
        o=s.event_integral(p,m,h,nth=1,nph=1,nq=48,nw=32,nt=24,Bt=Bt,iso_halo=True); r.append((o['URF'].mean()/o['lead'].mean(),o['src'].mean()/o['URF'].mean()))
    print(lab,'N_URF/N_lead at 10,100,1000 keV:',' '.join('%.3f'%a for a,b in r),' Nsrc/NURF',' '.join('%.1f'%b for a,b in r))
