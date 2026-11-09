"""ERR-CW1: corrected angle-averaged ZPL/PAER ratios (LE-26, VER-CW1 V10/V11, §2 (CW1.4)) and the X-face sensitivity (V8).
Same ZPL [E8] / PAER (P.1) models and constants as scripts/ratio.py (copied, not imported: ratio.py writes on import). Changes:
 (a) cone geometry: the 4 minima around one valley axis ({001} planes, +-theta) lie on a circle of radius theta_ZP; the independent-cone sum (CW1.4) double counts
     once adjacent ellipses overlap, at eps_touch = theta^2 b_th b_z/(b_th + b_z).  Here: 'min-of-cones' (each direction assigned to its lowest cone) on a 2-D grid;
 (b) relaxed-pair q coefficient g_rel (out/errata_qe.json, S12 'vertex'), instead of d/dq_z at fixed k_v;
 (c) the mirror-even second heavy hole: on-axis edge (Wannier, a_PBE), isotropic-in-azimuth curvature beta_2 of its pair energy under tilt, q-gradient 2.21 A
     (out/vertex_offaxis40.json, Delta_5 pair sum, assigned entirely to band 2: an upper estimate of its ZPL);
 (d) edges per channel at the best value (a_exp, PBE+SOC, DFT re-minimised: out/errata_qe_it2_SOC.json);
 (e) the X-face (2bar00) opening with c1 alone and c1 + c2.
usage: errata_ratio.py out.json"""
import numpy as np, json, sys, os
H=os.path.dirname(os.path.abspath(__file__)); O=lambda f: json.load(open(f'{H}/../out/{f}'))
sys.path.insert(0,H)
alpha=1/137.035999; me=510998.95; A2eV=1973.27; hbarc_cm=1.97327e-5; vmax=794.5/299792.458
Eb=0.0147; ax=4.9e-9/1.97327e-7; mu=1/(2*Eb*ax**2)
def alpha_cm(w):
    y=np.where(w>1.212,0.65+78*(w-1.212),np.clip(0.65*(w-1.160)/0.052,0,None)); return y**2/w
def eps2opt(w): return (3.55+0.37*(w-1.17))*alpha_cm(w)*hbarc_cm/w
qF=[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0]; Fc=[1,.79,.50,.31,.18,.12,.077,.054,.040,.032,.024]
V=O('vertex40.json'); F0=19.55
for qa,dct in V['F_raw'].items(): qF.append(float(qa)); Fc.append(dct['cubic']/F0)
lnF=lambda q: np.exp(np.interp(q,qF,np.log(Fc)))
SF=lambda e: 2*np.pi*np.sqrt(Eb/e)/(1-np.exp(-2*np.pi*np.sqrt(Eb/e)))
J=lambda e: (2*mu)**1.5*np.sqrt(np.clip(e,0,None))/(4*np.pi**2)
X=O('emin_extra.json'); Fz=O('emin_fast.json'); Q1=O('errata_qe.json'); Q2=O('errata_qe_it2_SOC.json'); P=O('vertex_pair40.json'); Vo=O('vertex_offaxis40.json')
bt,bz=X['a_theta_eV_per_rad2'],X['b_z_eV_per_rad2']; th0=Fz['theta_rad']
g_fix=O('vertex_opt2_a10.3507.json')['dqz_top_A']; g_rel=Q1['S12']['vertex']['g_rel_A']; Gk=Q1['S12']['vertex']['dkz_A']
q1=Q2['SOC']['q_keV_reminimised']*1e3; m1=Q2['SOC']['m_center']; E1=q1*vmax-q1**2/(2*m1*1e6)
res=dict(eps_touch=th0**2*bt*bz/(bt+bz),eps_axis=bt*th0**2,g_fix=g_fix,g_rel=g_rel,Gk=Gk,q1_keV=q1/1e3,m1=m1,E1=E1)
# --- (a) min-of-cones on a grid around one valley axis (6 valleys identical) ---
n=1201; t=np.linspace(-0.6,0.6,n); dA=(t[1]-t[0])**2; TY,TZ=np.meshgrid(t,t,indexing='ij')
Ec=[];R2=[]
for a in (0,np.pi/2,np.pi,3*np.pi/2):
    c=th0*np.array([np.cos(a),np.sin(a)]); rr=np.array([np.cos(a),np.sin(a)]); tt=np.array([-np.sin(a),np.cos(a)])
    dy,dz=TY-c[0],TZ-c[1]; thl=dy*rr[0]+dz*rr[1]; phl=dy*tt[0]+dz*tt[1]; Ec.append(bt*thl**2+bz*phl**2); R2.append(phl**2)
Ec=np.array(Ec); R2=np.array(R2); imin=np.argmin(Ec,0); Emin=np.take_along_axis(Ec,imin[None],0)[0]; ph2=np.take_along_axis(R2,imin[None],0)[0]
def Sbar_grid(e,g,mode):
    if mode=='indep': EE,PP=Ec,R2
    else: EE,PP=Emin[None],ph2[None]
    w=e-EE; ok=w>0; w=np.where(ok,w,1)
    qterm=np.where(ok,(g/A2eV)**2*q1**2*PP*J(w)*SF(w),0); kterm=np.where(ok,(Gk/A2eV)**2*(2*mu*w/3)*J(w)*SF(w)*(1+Eb/w),0)
    return 6*np.sum(qterm+kterm)*dA
def Sbar_closed(e,g):
    u=np.linspace(0,e,4001)[:-1]+e/8000; w=e-u
    return 24*(np.pi*(g/A2eV)**2*q1**2/(2*bz*np.sqrt(bt*bz))*np.trapezoid(u*J(w)*SF(w),u)+np.pi/np.sqrt(bt*bz)*np.trapezoid((Gk/A2eV)**2*(2*mu*w/3)*J(w)*SF(w)*(1+Eb/w),u))
ratio=lambda S,E0,e,q: (2*np.pi*alpha/q**2*S)/(eps2opt(E0+e)*lnF(q/A2eV))
rows=[]
for e in (0.001,Eb,0.03,0.05,0.1,0.2):
    rows.append(dict(eps=e,closed_gfix=ratio(Sbar_closed(e,g_fix),E1,e,q1),grid_indep_gfix=ratio(Sbar_grid(e,g_fix,'indep'),E1,e,q1),
                     mincones_gfix=ratio(Sbar_grid(e,g_fix,'min'),E1,e,q1),mincones_grel=ratio(Sbar_grid(e,g_rel,'min'),E1,e,q1)))
res['first_channel']=rows
# true Wannier E at the midpoint between adjacent cones ({011}-type tilt, theta = th0/sqrt2) vs the min-of-cones model
from wannier_si import bands, sc, kc, tpiba, nv
from scipy.optimize import minimize
K=1/(3.7289*tpiba)
def pE(k,q,b=nv-1): return bands((k+q)[None])[0,nv]-bands(k[None])[0,b]+sc
def emin(q,b=nv-1):
    return min(minimize(lambda k: pE(k,q,b),k0,method='Nelder-Mead',options=dict(xatol=1e-8,fatol=1e-10,maxiter=8000,adaptive=True)).fun for k0 in (-0.22*(q-kc),np.zeros(3)))
qa=Fz['q_keV']*K; sph=lambda th,az: np.array([np.cos(th),np.sin(th)*np.cos(az),np.sin(th)*np.sin(az)])
E0w=emin(qa*sph(th0,0)); Emid=emin(qa*sph(th0/np.sqrt(2),np.pi/4)); # min-of-cones model at the midpoint direction (th0/2)(1,1): for the cone at (th0,0) the radial offset is -th0/2 and the tangential th0/2
res['midpoint']=dict(E_true_minus_E0=Emid-E0w,model=bt*(th0/2)**2+bz*(th0/2)**2)
# --- (c) second heavy hole on axis ---
best=None
for qk in np.linspace(1.33,1.45,13):
    q=np.array([qk*K,0,0]); E=emin(q,nv-2); m=(qk*1e3)**2/(2*(qk*1e3*vmax-E))/1e6
    if best is None or m<best[0]: best=(m,qk,E)
m2w,q2,E2=best; tilt=[]
for az in (0,np.pi/8,np.pi/4):
    for th in (0.02,0.04):
        q=q2*K*sph(th,az); tilt.append((az,th,emin(q,nv-2)-E2))
b2=[d/th**2 for az,th,d in tilt if th==0.02]; b2_4=[d/th**2 for az,th,d in tilt if th==0.04]
inv2=np.mean([1/b**2 for b in b2])                      # (1/2pi) int dalpha / beta(alpha)^2, beta sampled at 0, pi/8, pi/4 (C4v)
res['second_band']=dict(m_axis_wannier=m2w,q_keV=q2,E_axis=E2,beta2_002=b2,beta2_004=b2_4)
g2=Vo['o0.005']['g_perp_A']; Gk2=np.sqrt(2)*P['gradk_hh_A_0.005']
# edge of channel 2: 'low' = Wannier a_PBE value; 'central' = + the scalar a_PBE-Wannier -> a_exp-DFT shift found for channel 1 (+0.0045 MeV, [E] transfer)
# + its own SOC shift (on-axis pair +0.9 meV -> +0.0002 MeV)
dm_lat=O('errata_qe_it2_S12.json')['S12']['m_center']-Fz['m_ZPL']; m2=dict(low=m2w,central=m2w+dm_lat+0.0002)
res['second_band'].update(g_perp=g2,Gk=Gk2,m_edge=m2)
def S2(e,inv_b2,b2mean):
    u=np.linspace(0,e,4001)[:-1]+e/8000; w=e-u
    return 6*(np.pi*inv_b2*(g2/A2eV)**2*(q2*1e3)**2*np.trapezoid(u*J(w)*SF(w),u)+np.pi/b2mean*np.trapezoid((Gk2/A2eV)**2*(2*mu*w/3)*J(w)*SF(w)*(1+Eb/w),u))
# --- (d) in m_chi ---
def emax(m,q,medge): E=q*vmax-q**2/(2*medge*1e6); return q*vmax-q**2/(2*m*1e6)-E
tab=[]
for m in (0.41,0.415,0.42,0.43,0.44,0.45):
    e1=emax(m,q1,m1); r1=ratio(Sbar_grid(e1,g_rel,'min'),E1,e1,q1) if e1>0 else 0
    row=dict(m=m,eps1=e1,ratio1=r1)
    for lab,me_ in m2.items():
        e2=emax(m,q2*1e3,me_); E2e=q2*1e3*vmax-(q2*1e3)**2/(2*me_*1e6)
        row[f'eps2_{lab}']=e2; row[f'ratio2_{lab}']=ratio(S2(e2,inv2,np.mean(b2)),E2e,e2,q2*1e3) if e2>0 else 0
    soc=O('errata_qe.json')['SOC']['soc_mirror_optimum']['top_pair_over2']
    if e1>0:
        u=np.linspace(0,e1,4001)[:-1]+e1/8000; w=e1-u; Ss=24*soc*np.pi/np.sqrt(bt*bz)*np.trapezoid(J(w)*SF(w),u); row['ratio_soc']=ratio(Ss,E1,e1,q1)
    row['total_central']=row['ratio1']+row['ratio2_central']+row.get('ratio_soc',0); row['total_low']=row['ratio1']+row['ratio2_low']+row.get('ratio_soc',0)
    tab.append(row)
res['in_m']=tab
# --- (e) X-face opening: c1 alone vs c1 + c2 (out/vertex_U200opt.json), same model as ratio.py table() kind I
U=O('vertex_U200opt.json'); Xq=X['U200']['q_keV']*1e3
xf=[]
for e in (0.001,Eb,0.05,0.1):
    for key in ('xc','xc0.05'):
        for lab in ('rho2_c1_top','rho2_c12_top'):
            S=4*np.pi*U[key][lab]*J(e)*SF(e); xf.append(dict(eps=e,point=key,vertex=lab,ratio=ratio(S,U[key]['Epair'],e,Xq)))
res['Xface']=xf
json.dump(res,open(sys.argv[1],'w'),indent=1); print(json.dumps(res,indent=1))
