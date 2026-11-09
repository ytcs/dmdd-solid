"""LE-25 / LE-26: pointwise zero-phonon / PAER ratios in Si at the threshold (q, omega) points, in eps2 units (the common 1/eps1^2 cancels).
Zero-phonon side (WP1-v3 [E8], Wannier-Mott continuum at fixed q, isotropic mu_x from a_x = 4.9 nm, E_x^b = 14.7 meV):
  allowed:      S_I  = 4pi |rho|^2            J(e) S_F(e)
  second class: S_II = 4pi |grad_k rho|^2 (2 mu e)/3  J(e) S_F(e) (1 + zeta^2),   J(e) = (2mu)^{3/2} sqrt(e)/(4 pi^2),   eps2 = (2 pi alpha/q^2) S.
  Vertices [CALC]: out/vertex_pair40.json (this package). |grad_k rho|^2 = 2 x (transverse component)^2 (C4v: d/dk_y = d/dk_z, d/dk_x = 0 on the axis).
PAER side [E, COMP-PAER (P.1)]: eps2^PA(q,w) = eps2^{PA,opt}(w) F_rho(q); F_rho from COMP-PAER (<= 1.0 A^-1) and this package (1.155-1.34 A^-1),
  extrapolated past E_min(q) (outside the window: DC convention, WP3-v3 (M.10)); eps2^{PA,opt} = Macfarlane 20 K fit as in COMP-PAER rate.py.
usage: ratio.py out.json"""
import numpy as np, json, sys, os
H=os.path.dirname(os.path.abspath(__file__))
alpha=1/137.035999; me=510998.95; A2eV=1973.27; hbarc_cm=1.97327e-5
Eb=0.0147; ax=4.9e-9/1.97327e-7          # eV^-1
mu=1/(2*Eb*ax**2)                          # eV  (= 0.108 m_e)
def alpha_cm(w):
    y=np.where(w>1.212,0.65+78*(w-1.212),np.clip(0.65*(w-1.160)/0.052,0,None)); return y**2/w
def eps2opt(w): return (3.55+0.37*(w-1.17))*alpha_cm(w)*hbarc_cm/w
qF=[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0]; Fc=[1,.79,.50,.31,.18,.12,.077,.054,.040,.032,.024]
V=json.load(open(f'{H}/../out/vertex40.json')); F0=19.55   # q->0 value of <sum|rho|^2/q^2> (A^2), COMP-PAER ff.json
for qa,dct in V['F_raw'].items(): qF.append(float(qa)); Fc.append(dct['cubic']/F0)
lnF=lambda q: np.exp(np.interp(q,qF,np.log(Fc)))
SF=lambda e: 2*np.pi*np.sqrt(Eb/e)/(1-np.exp(-2*np.pi*np.sqrt(Eb/e)))
J=lambda e: (2*mu)**1.5*np.sqrt(e)/(4*np.pi**2)
P=json.load(open(f'{H}/../out/vertex_pair40.json'))
g2=2*P['gradk_hh_A_0.005']**2/A2eV**2     # eV^-2
out=dict(mu_over_me=mu/me, F_ext={str(q):f for q,f in zip(qF[-3:],Fc[-3:])}, g2_A2=g2*A2eV**2)
def table(qA,Emin,kind,vert):
    rows=[]
    for e in (0.001,Eb,0.1,0.5):
        q=qA*A2eV
        S= 4*np.pi*vert*J(e)*SF(e) if kind=='I' else 4*np.pi*vert*(2*mu*e/3)*J(e)*SF(e)*(1+Eb/e)
        e2x=2*np.pi*alpha/q**2*S; e2p=eps2opt(Emin+e)*lnF(qA)
        rows.append(dict(eps_ex=e, eps2_X0=e2x, eps2_PA=e2p, ratio=e2x/e2p))
    return rows
# second class, G'=0, at the m_ZPL optimum q = 1.39 keV ([100]); E_min from COMP-PH (1.355 eV, a_PBE) - sensitivity: ratio ~ eps2opt(E_min+e)^-1
out['G0_secondclass_q1.39keV']=table(1390/A2eV,1.355,'II',g2)
out['G0_secondclass_q1.39keV_Emin1.389']=table(1390/A2eV,1.389,'II',g2)
# allowed (2bar00) class at q = X ... 1.10 X (light-hole partner; heavy-hole part vanishes on the axis)
for s in ('1.0','1.05','1.1'):
    u=P[f'U200_{s}']; qA=float(s)*2*np.pi/5.431
    out[f'U200_q{s}X']=table(qA,u['Epair_eV'],'I',u['rho2_all'])
# (b) the true G'=0 threshold: off-axis optimum in a {001} mirror plane (out/emin_fast.json, emin_extra.json, vertex_opt2_a10.3507.json).
#     pointwise: only the out-of-plane k_rel component contributes (sigma_z), |grad|^2 = (d rho/d k_z)^2;
#     angle average at fixed |q| over the N_min = 24 equivalent minima (6 valleys x 2 mirror planes x +-theta), ellipse E = E0 + a th^2 + b ph^2:
#     Sbar = N_min [ (pi g_z^2 q^2/(2 b sqrt(ab))) int_0^e u J(e-u) S_F du + (pi/sqrt(ab)) int_0^e G_k^2 (2 mu (e-u)/3) J S_F (1+Eb/(e-u)) du ]
X=json.load(open(f'{H}/../out/emin_extra.json')); O=json.load(open(f'{H}/../out/vertex_opt2_a10.3507.json')); Fz=json.load(open(f'{H}/../out/emin_fast.json'))
a_,b_=X['a_theta_eV_per_rad2'],X['b_z_eV_per_rad2']; gz=O['dqz_top_A']/A2eV; Gk=O['dkz_top_A']/A2eV
qopt=Fz['q_keV']*1e3; E0=1.170+0.7795-0.0006-0.602   # DFT pair energy at a_PBE + scissor (E_g^PBE(a_PBE) = 0.602 eV, COMP-PH)
out['offaxis_inputs']=dict(a_theta=a_,b_z=b_,g_qz_A=O['dqz_top_A'],G_kz_A=O['dkz_top_A'],q_keV=qopt/1e3,E0_DFT=E0,E0_Wannier=Fz['E_pair'],N_min=24)
rows=[]
for e in (0.001,Eb,0.05,0.1,0.2):
    u=np.linspace(0,e,4001)[:-1]+e/8000; w=e-u
    Aterm=np.pi*gz**2*qopt**2/(2*b_*np.sqrt(a_*b_))*np.trapezoid(u*J(w)*SF(w),u)
    Bterm=np.pi/np.sqrt(a_*b_)*np.trapezoid(Gk**2*(2*mu*w/3)*J(w)*SF(w)*(1+Eb/w),u)
    Sb=24*(Aterm+Bterm); e2x=2*np.pi*alpha/qopt**2*Sb; e2p=eps2opt(E0+e)*lnF(qopt/A2eV)
    Sp=4*np.pi*Gk**2*(2*mu*e/3)*J(e)*SF(e)*(1+Eb/e); e2pt=2*np.pi*alpha/qopt**2*Sp
    rows.append(dict(eps_ex=e,ratio_angleavg=e2x/e2p,ratio_pointwise=e2pt/e2p,qz_part=float(Aterm/(Aterm+Bterm)),eps2_PA=e2p))
out['G0_offaxis_optimum']=rows
# (b') SOC-lifted vertex at the same optimum (out/vertex_soc.json; Kramers-pair sum / 2 = scalar-equivalent |rho|^2), constant over the cones
Sc=json.load(open(f'{H}/../out/vertex_soc.json')); r_soc=Sc['mirror_optimum']['top_pair']/2; out['rho2_SOC_scalar_equiv']=r_soc
rows=[]
for e in (0.001,Eb,0.05,0.1,0.2):
    u=np.linspace(0,e,4001)[:-1]+e/8000; w=e-u
    Sb=24*r_soc*np.pi/np.sqrt(a_*b_)*np.trapezoid(J(w)*SF(w),u); e2x=2*np.pi*alpha/qopt**2*Sb; e2p=eps2opt(E0+e)*lnF(qopt/A2eV)
    Sp=4*np.pi*r_soc*J(e)*SF(e); rows.append(dict(eps_ex=e,ratio_SOC_angleavg=e2x/e2p,ratio_SOC_pointwise=2*np.pi*alpha/qopt**2*Sp/e2p))
out['G0_offaxis_SOC']=rows
# (c) allowed-size vertex at the (2bar00)-class edge on the X face (out/vertex_U200opt.json): top hole, c1 and 0.02-0.10 inside the class
U=json.load(open(f'{H}/../out/vertex_U200opt.json')); Xq=X['U200']['q_keV']*1e3/A2eV
for key in ('xc','xc0.05'):
    out[f'U200_Xface_{key}']=table(Xq,U[key]['Epair'],'I',U[key]['rho2_c1_top'])
# WP1-v3 [E14] central inputs for comparison: l_grad = 1-3 A against |rho_ref|; here the absolute |grad_k rho| is used, no eta_PA transfer
json.dump(out,open(sys.argv[1],'w'),indent=1)
for k,v in out.items():
    if isinstance(v,list):
        print(k); [print('   '+'  '.join(f"{a}={b:.3g}" for a,b in r.items())) for r in v]
    else: print(k,v)
