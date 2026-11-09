"""Reproduction of 1708.08929 Fig. (light mediator). Isotropic ideal Dirac and ZrTe5 with kappa-tilde.
Halo as stated there: rho=0.4, v0=220, vE=232, vesc=550, spherically averaged. eq:epsGap: mu~ = 2 v_F Lambda (lnc = 0)."""
import numpy as np, dirac as d, scatter as s, svgcurves as S, sys, json
F=sys.argv[1]
ps=S.paths(F+'/h_ScatteringReachPlotLightMed.svg')
cal=lambda q:(3*10**((q[:,0]-86.55)/190.6),10**(-32-(q[:,1]-67.94)/17.62))
cols={'gapless':'rgb(46.272278%, 73.330688%, 32.156372%)','gapped':'rgb(59.605408%, 43.527222%, 72.940063%)','Zr_exp':'rgb(66.664124%, 66.664124%, 0%)','Zr_th':'rgb(72.546387%, 32.546997%, 32.546997%)'}
pub={}
for k,c in cols.items():
    q=[p for p in ps if p['color']==c and len(p['pts'])>6][0]['pts']; x,y=cal(q); o=np.argsort(x); pub[k]=np.c_[x[o],y[o]]
    np.savetxt(f'data/pub_h_{k}.csv',pub[k],delimiter=',',header='m[keV],sigma[cm^2] 1708.08929 Fig. light mediator')
h=dict(rho=0.4e9/d.CM**3,v0=220*d.KMS,vesc=550*d.KMS,ve=232*d.KMS)
A=d.ANG
def mk(v,D,Lam_keV,g,kap,neV):
    # neV = n_e V_uc [m^3/kg] -> rho_eff
    p=dict(v=np.array(v),D=D,Lam=np.array([Lam_keV*1e3/A]*3),kap=np.array([kap]*3,float),g=g,rho=1e-3/neV,koff=dict(xy=(0,0),xz=(0,0),yz=(0,0)),lnc=0.)
    p['vvv']=np.prod(p['v']); p['Lt']=Lam_keV*1e3*np.min(p['v']) if False else Lam_keV*1e3*np.prod(p['v'])**(1/3)
    p['EL']=np.sqrt(p['Lt']**2+D**2); p['rhoT']=p['rho']*(1e-3*d.KG)/d.CM**3; p['C']=g*d.E2/(4*np.pi**2*p['vvv']); p['ksym']=np.diag(p['kap'])
    return p
kt=3/(1/187.5+1/9.8+1/90.9); print('kappa-tilde',kt)
cases={'gapless':mk((4e-4,)*3,1e-6,.2,2,40.,5e24*60e-30),'gapped':mk((4e-4,)*3,2.5e-3,.2,2,40.,5e24*60e-30),
       'Zr_th':mk((2.9e-3,5e-4,2.1e-3),17.5e-3,.14,4,kt,8.3e23*795e-30),'Zr_exp':mk((1.3e-3,6.5e-4,1.6e-3),11.75e-3,.14,4,kt,8.3e23*795e-30)}
def setLt(p,L):
    p=dict(p); p['Lt']=L; p['EL']=np.sqrt(L*L+p['D']**2); return p
cases['Zr_th:Lt=Lam*min v']=setLt(cases['Zr_th'],140*5e-4); cases['Zr_th:Lt=Lam*max v']=setLt(cases['Zr_th'],140*2.9e-3)
cases['Zr_exp:Lt=Lam*min v']=setLt(cases['Zr_exp'],140*6.5e-4); cases['Zr_exp:Lt=Lam*max v']=setLt(cases['Zr_exp'],140*1.6e-3)
out={}
for key,p in cases.items():
    k=key.split(':')[0]
    Bt=d.Btab(p); r=[]
    ms=[m for m in (5e3,10e3,20e3,30e3,50e3,100e3,300e3,1000e3) if m/1e3>pub[k][:,0].min()*1.25]
    for m in ms:
        o=s.event_integral(p,m,h,nth=(1 if k.startswith('gap') else 16),nph=(1 if k.startswith('gap') else 24),nq=48,nw=32,nt=24,Bt=Bt,iso_halo=True,kt=kt if k.startswith('Zr') else None)
        N=o['src'].mean(); y=np.exp(np.interp(np.log(m/1e3),np.log(pub[k][:,0]),np.log(pub[k][:,1])))
        r.append((m/1e3,3/N,y))
    print(key,' '.join('%g:%.3f'%(a,b/c) for a,b,c in r),flush=True)
