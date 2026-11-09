"""Referee: 1708.08929 curves through the DC-49 integrator (read-only import) with the log convention the gapless curve demands (lnc=-5/3 = Eq. epsSM / RdiffNoGap),
Lambda~ = Lambda max v (App. anperm, printed), and both readings of the target mass normalisation. Also ELF-route normalisation check of the printed rate."""
import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'../DC-49')
import numpy as np, dirac as d, scatter as s
h=dict(rho=0.4e9/d.CM**3,v0=220*d.KMS,vesc=550*d.KMS,ve=232*d.KMS)
kt=3/(1/187.5+1/9.8+1/90.9)
def mk(v,D,Lt,g,kap,rho,lnc):
    p=dict(v=np.array(v),D=D,Lam=np.array([1.]*3),kap=np.array([kap]*3,float),g=g,rho=rho,koff=dict(xy=(0,0),xz=(0,0),yz=(0,0)),lnc=lnc)
    p['vvv']=np.prod(p['v']); p['Lt']=Lt; p['EL']=np.sqrt(Lt**2+D**2); p['rhoT']=rho*(1e-3*d.KG)/d.CM**3; p['C']=g*d.E2/(4*np.pi**2*p['vvv']); p['ksym']=np.diag(p['kap']); return p
rho_id=1e-3/(5e24*60e-30)
def run(lab,key,p,zr=False,masses=(10e3,30e3,100e3,300e3,1000e3)):
    pub=np.loadtxt(f'../DC-49/data/pub_h_{key}.csv',delimiter=','); Bt=d.Btab(p); r=[]
    for m in masses:
        if m/1e3<pub[:,0].min()*1.25: continue
        o=s.event_integral(p,m,h,nth=(16 if zr else 1),nph=(24 if zr else 1),nq=48,nw=32,nt=24,Bt=Bt,iso_halo=True,kt=kt if zr else None)
        y=np.exp(np.interp(np.log(m/1e3),np.log(pub[:,0]),np.log(pub[:,1]))); r.append((m/1e3,3/o['src'].mean()/y))
    print(lab,' '.join('%g:%.3f'%x for x in r),flush=True)
for lnc in (0.,-5/3):
    run(f'gapless lnc={lnc:.2f}','gapless',mk((4e-4,)*3,1e-6,.08,2,40.,rho_id,lnc))
    run(f'gapped  lnc={lnc:.2f}','gapped',mk((4e-4,)*3,2.5e-3,.08,2,40.,rho_id,lnc))
for key,v,D in (('Zr_th',(2.9e-3,5e-4,2.1e-3),17.5e-3),('Zr_exp',(1.3e-3,6.5e-4,1.6e-3),11.75e-3)):
    for rl,rho in (('rho=1/(n_e V_uc)=1.516',1e-3/(8.3e23*795e-30)),('rho_T=6.1',6.1)):
        for ll,Lt in (('max',140*max(v)),('min',140*min(v))):
            run(f'{key} {rl} Lt={ll} lnc=-5/3',key,mk(v,D,Lt,4,kt,rho,-5/3),zr=True,masses=(30e3,100e3,300e3,1000e3))
