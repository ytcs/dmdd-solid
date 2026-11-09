"""omega_nu(Q*), Q* = K_pk - q (G'=0 class), on the PAER window grid; E_th(|q|) = E_g + min_{qhat,nu} omega(Q*);
mass edges via WP6-v3 (3.1'). usage: phwin.py MAT alat flfrc kc_x(2pi/a) Eg Exb Emin.json out.json"""
import numpy as np, sys, json, subprocess, os
m,al,flfrc,kcx,Eg,Exb,ej,out=sys.argv[1],float(sys.argv[2]),sys.argv[3],float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),sys.argv[7],sys.argv[8]
tpiba=2*np.pi/al; KEV=3.7289  # keV per bohr^-1
axis=np.array([1,1,1])/np.sqrt(3) if m=='Ge' else np.array([1.,0,0])
K=axis*kcx*(np.sqrt(3) if m=='Ge' else 1)   # 2pi/a ; Ge: kc_x is the L component (0.5)
Kn=np.linalg.norm(K)*tpiba*KEV
qs=np.round(np.arange(0.40,2.001,0.02),3)
ths=np.linspace(0,0.7,15); phis=np.linspace(0,np.pi/2,7)
# orthonormal frame around axis
e1=np.cross(axis,[0,0,1.]) if m=='Ge' else np.array([0,1.,0]); e1/=np.linalg.norm(e1); e2=np.cross(axis,e1)
pts=[];lab=[]
for q in qs:
    for th in ths:
        for ph in (phis if th>0 else [0.]):
            qh=np.cos(th)*axis+np.sin(th)*(np.cos(ph)*e1+np.sin(ph)*e2)
            Q=K-qh*q/KEV/tpiba; pts.append(Q); lab.append((q,th,ph))
pts=np.array(pts)
w=os.path.dirname(flfrc); fin=f"{w}/win.in"
open(fin,'w').write(f"&input\n asr='crystal', flfrc='{flfrc}', flfrq='{w}/win.freq', fleig='{w}/win.eig', fldos=' ', q_in_band_form=.false., eigen_similarity=.false.\n/\n{len(pts)}\n"+''.join(f"{a:.8f} {b:.8f} {c:.8f}\n" for a,b,c in pts))
env=dict(os.environ,PATH='/root/mamba/envs/qe/bin:'+os.environ['PATH'])
subprocess.run(['matdyn.x','-in',fin],cwd=w,env=env,stdout=open(f"{w}/win.out",'w'),check=True)
# parse freq file (cm-1)
t=open(f"{w}/win.freq").read().split('\n'); nb=int(t[0].split('nbnd=')[1].split(',')[0]); vals=[]
toks=' '.join(t[1:]).split(); per=4+nb
arr=np.array([float(x) for x in toks[:per*len(pts)]]).reshape(len(pts),per)[:,4:]
CM=0.123984  # meV per cm-1
om=arr*CM
E=json.load(open(ej)) if ej!='none' else None; 
res=dict(K_pk_keV=Kn, axis=list(axis), q_keV=list(qs), rows=[])
vmax=794.5/299792.458
for q in qs:
    sel=[i for i,l in enumerate(lab) if l[0]==q]
    ax=[i for i in sel if lab[i][1]==0][0]
    wmin=om[sel,0].min(); imin=sel[int(np.argmin(om[sel,0]))]
    row=dict(q=float(q), Qstar_axis_invA=float(np.linalg.norm(pts[ax])*tpiba/0.529177), w_axis=[float(x) for x in om[ax,:3]],
             w_TA_min=float(wmin), theta_min=float(lab[imin][1]), phi_min=float(lab[imin][2]))
    res['rows'].append(row)
def mmin(Eth):  # (3.1') with q in keV, E in eV -> MeV
    qq=np.array(qs)*1e3; d=qq*vmax-np.array(Eth); ok=d>0
    mm=np.where(ok,qq**2/(2*np.where(ok,d,1)),np.inf)/1e6; i=int(np.argmin(mm)); return float(mm[i]), float(qs[i])
Ec=[Eg+r['w_TA_min']/1e3 for r in res['rows']]; Ex=[Eg-Exb+r['w_TA_min']/1e3 for r in res['rows']]
res['m_PAER_continuum']=mmin(Ec); res['m_PAER_replica']=mmin(Ex)
res['m_floor_Eg']=2*Eg/vmax**2/1e6; res['m_floor_Ex']=2*(Eg-Exb)/vmax**2/1e6
if E is not None:
    # ZPL kinematic edge: E_min(|q|) min over sampled directions, interpolated onto qs
    qe_=np.array(E['q_keV']); Emin=np.min(np.array([E['Emin'][d] for d in E['Emin']]),axis=0)
    res['Emin_minDir']=list(map(float,Emin))
    qq=np.linspace(qe_[0],qe_[-1],400); Ei=np.interp(qq,qe_,Emin); d=qq*1e3*vmax-Ei
    mm=np.where(d>0,(qq*1e3)**2/(2*np.where(d>0,d,1)),np.inf)/1e6; i=int(np.argmin(mm))
    res['m_ZPL_kin']=(float(mm[i]),float(qq[i]),float(Ei[i]))
else:
    res['m_ZPL_kin']=None
json.dump(res,open(out,'w'),indent=1)
for r in res['rows']: print(f"q={r['q']:.2f} keV |Q*|axis={r['Qstar_axis_invA']:.3f}/A  w_axis TA,TA,LA={r['w_axis']}  minTA={r['w_TA_min']:.2f} at th={r['theta_min']:.2f}")
print('m_PAER cont',res['m_PAER_continuum'],'replica',res['m_PAER_replica'],'floors',res['m_floor_Eg'],res['m_floor_Ex'],'m_ZPL_kin',res['m_ZPL_kin'])
