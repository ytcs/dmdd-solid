"""Referee checks on DC-49 with its integrator (read-only import; validated independently by h1708_direct.py: 0.503 vs 0.502-0.504).
(1) material orientation prescribed by 1910.02091 sec. 4 (smallest v_F -> lab y, largest -> lab z; BNQ footnote) and modulation fraction vs ZrTe5_details.pdf
(2) sensitivity of N_src/N_URF to inferred inputs (halo, Lambda, v_F,x); (3) decomposition of the 'x640' comparison."""
import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'../DC-49')
import numpy as np, dirac as d, scatter as s
H=dict(rho=0.3e9/d.CM**3,v0=220*d.KMS,vesc=600*d.KMS,ve=232*d.KMS)
HC=dict(rho=0.3e9/d.CM**3,v0=238*d.KMS,vesc=544*d.KMS,ve=250.5*d.KMS)
H544=dict(rho=0.3e9/d.CM**3,v0=220*d.KMS,vesc=544*d.KMS,ve=232*d.KMS)
RH=6.135*(1e-3*d.KG)/d.CM**3
kw=dict(nth=24,nph=36,nq=36,nw=24,nt=24)
def setp(n,perm=None,**o):
    p=d.setup(n,**o); p['rhoT']=RH
    if perm is not None:
        p['v']=p['v'][list(perm)]; p['kap']=p['kap'][list(perm)]; p['Lam']=p['Lam'][list(perm)]
        p['ksym']=p['ksym'][np.ix_(perm,perm)]
    return p
def ev(p,m,h=H):
    Bt=d.Btab(p); o=s.event_integral(p,m*1e3,h,Bt=Bt,**kw)
    return o
print('(1) ZrTe5 th: A_src vs published; orientation as used by DC-49 (x,y,z)=table, and as prescribed (largest v_F along lab z)')
pub=np.loadtxt('../DC-49/data/pub_modfrac_ZrTe5_th.csv',delimiter=','); pub=pub[np.argsort(pub[:,0])]
print(' pub file head',pub[:2],pub[-1])
for lab,perm in (('DC-49 orientation',None),('prescribed: swap x<->z',(2,1,0))):
    r=[]
    for m in (20,50,100,175,300,500,1000):
        o=ev(setp('ZrTe5_th',perm),m); r.append((m,s.mod_amp(o['src']),s.mod_amp(o['URF']),o['src'].mean()/o['URF'].mean()))
        
    print(' ',lab,' '.join('%g: A_src %.3f A_URF %.3f ratio %.0f pub %.3f |'%(a,b,c,e,np.interp(np.log(a),np.log(pub[:,0]),pub[:,1])) for a,b,c,e in r),flush=True)
print('    ZrTe5 exp (largest v_F already z)')
pe=np.loadtxt('../DC-49/data/pub_modfrac_ZrTe5_exp.csv',delimiter=','); pe=pe[np.argsort(pe[:,0])]
r=[]
for m in (20,50,100,300,700):
    o=ev(setp('ZrTe5_exp',None,v=(1.3e-3,6.5e-4,1.6e-3),Lam=(.07,.07,.07)),m); r.append((m,s.mod_amp(o['src']),np.interp(np.log(m),np.log(pe[:,0]),pe[:,1])))
print('  ',' '.join('%g: %.3f pub %.3f |'%x for x in r),flush=True)
print(' BNQ: table order v=(2,2,1),kappa=(18.7,5.6,10.3); prescribed: smallest v_F -> y, smallest kappa of the rest -> z: lab=(table x, table z, table y)')
for lab,perm in (('DC-49',None),('prescribed',(0,2,1))):
    r=[]
    for m in (10,21.5,90.9,1000):
        o=ev(setp('BNQ',perm),m); r.append((m,s.mod_amp(o['src']),s.mod_amp(o['URF']),o['src'].mean()/o['URF'].mean()))
    print(' ',lab,' '.join('%g: A_src %.3f A_URF %.3f ratio %.1f |'%x for x in r),flush=True)
print('(2) sensitivity of N_src/N_URF at m=100 keV and 1.5 m_thr')
for n,o_,ms in (('ZrTe5_th',{},(20,100,1000)),('ZrTe5_exp',dict(v=(1.3e-3,6.5e-4,1.6e-3),Lam=(.07,.07,.07)),(20,100,1000)),('BNQ',{},(15,100,1000))):
    for hl,h in (('fit 220/232/600',H),('220/232/544',H544),('campaign 238/250.5/544',HC)):
        r=[ev(setp(n,None,**o_),m,h) for m in ms]; print(' ',n,hl,' '.join('%g: %.0f'%(m,x['src'].mean()/x['URF'].mean()) for m,x in zip(ms,r)),flush=True)
for lab,o_ in (('Lam=.07 v_x=1.3 (DC-49)',dict(v=(1.3e-3,6.5e-4,1.6e-3),Lam=(.07,.07,.07))),('Lam=table v_x=1.3',dict(v=(1.3e-3,6.5e-4,1.6e-3))),('Lam=.07 v_x=1.1',dict(v=(1.1e-3,6.5e-4,1.6e-3),Lam=(.07,.07,.07)))):
    r=[ev(setp('ZrTe5_exp',None,**o_),m) for m in (30,100,1000)]; print('  exp',lab,' '.join('%g: %.0f'%(m,x['src'].mean()/x['URF'].mean()) for m,x in zip((30,100,1000),r)),flush=True)
print('(3) x640 decomposition, 1910 ZrTe5 th band structure')
ka=(308.4,20.75,126.1); kh=(187.5,9.8,90.9)
ht=lambda k:3/sum(1/x for x in k)
print('  harmonic means: 1910 table %.2f -> x%.0f ; 1708 table %.2f -> x%.0f'%(ht(ka),ht(ka)**2,ht(kh),ht(kh)**2))
for lab,k in (('1910 kappa tensor',ka),('1708 kappa tensor',kh)):
    r=[]
    for m in (30,100,1000):
        o=ev(setp('ZrTe5_th',None,kap=k),m); r.append((m,o['src'].mean()/o['URF'].mean()))
    print('  anisotropic rule,',lab,' '.join('%g: %.0f'%x for x in r),flush=True)
