"""ERR-CW1 analysis of the regenerated QE runs (inputs/errata/, run by scripts/run_errata_qe.sh; a_exp = 10.2631 bohr, 40 Ry, nscf on the 60-point
k set of scripts/errata_kset.py).  Three variants: S12 = SG15 Si_ONCV_PBE-1.2 (scalar, the CW1 pseudopotential); FRav = Si_ONCV_PBE_FR-1.1 with
lspinorb = .false. (j-averaged, scalar: same pseudo family as SOC); SOC = FR-1.1 noncollinear + lspinorb.
Outputs (out/errata_qe.json):
 (1) PBE gap E(k_c) - E(Gamma), pair energy at the CW1 mirror-plane optimum (k_h, k_e = k_h + q), scissored to E_g(0) = 1.170 eV against each run's own gap;
 (2) local re-minimisation of m = |q|^2 / 2(|q| v_max - E) over (k_e, k_h) (6-D) with full quadratic fits (10 parameters) of eps_c around k_e and eps_v around
     k_h on 3x3x3 stencils (h = 0.02 2pi/a): this is (CW1.1) re-minimised on DFT bands, per variant;
 (3) SOC vertices: Gamma_8 quartet sum at the on-axis extremum, single top Kramers pair (gauge dependent), and the mirror-optimum lift;
 (4) scalar vertices at the mirror optimum: per band, d/dk_z (both legs), d/dq_z (electron leg), hole leg alone, the relaxed-pair q coefficient;
 (5) the q* = 0.90 keV pair (IF-CW1-3) per variant.
usage: errata_analysis.py workdir labels.json out.json"""
import numpy as np, h5py, sys, json, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eig import read
from scipy.optimize import minimize
W, labf, out = sys.argv[1:4]; VARS=sys.argv[4:] or ['S12','FRav','SOC']; L=json.load(open(labf)); lab=L['labels']; I={l:i for i,l in enumerate(lab)}; h=L['h']
al=10.2631; A=0.529177; tp=2*np.pi/al; K=1/(3.7289*tp)   # keV -> 2pi/a at a_exp
vmax=794.5/299792.458; Eg0=1.170
def wfs(d,i,spin):
    with h5py.File(f'{d}/wfc{i+1}.hdf5','r') as f: mi=f['MillerIndices'][:]; e=f['evc'][:]
    c=e[:,0::2]+1j*e[:,1::2]; n=len(mi); return {tuple(r):j for j,r in enumerate(mi)}, c, n
def rho(d,ic,iv,spin):
    a_,ca,na=wfs(d,ic,spin); b_,cb,nb=wfs(d,iv,spin); keys=[g for g in a_ if g in b_]
    ia=np.array([a_[g] for g in keys]); ib=np.array([b_[g] for g in keys])
    if spin: A_=np.concatenate([ca[:,ia],ca[:,na+ia]],1); B_=np.concatenate([cb[:,ib],cb[:,nb+ib]],1)
    else: A_=ca[:,ia]; B_=cb[:,ib]
    return np.conj(A_)@B_.T
def mval(ke,kh,Ec,Ev,sc):
    q=np.linalg.norm(ke-kh)/K*1e3; den=q*vmax-(Ec-Ev+sc); return q*q/(2*den)/1e6
def qfit(pts,vals):   # full quadratic in 3-D: 1, x, y, z, xx, yy, zz, xy, xz, yz
    X=np.array([[1,*p,p[0]**2,p[1]**2,p[2]**2,p[0]*p[1],p[0]*p[2],p[1]*p[2]] for p in pts]); c,res,_,_=np.linalg.lstsq(X,vals,rcond=None)
    g=c[1:4]; Hm=np.array([[2*c[4],c[7],c[8]],[c[7],2*c[5],c[9]],[c[8],c[9],2*c[6]]]); rms=np.sqrt(np.mean((X@c-vals)**2)); return c[0],g,Hm,rms
R={}
for v in VARS:
    d=f'{W}/{v}/si.save'; k,E=read(d); spin=(v=='SOC'); iv,ic=(7,8) if spin else (3,4)
    gap=E[I['kc'],ic]-E[I['G'],iv]; sc=Eg0-gap; vbm=E[I['G'],iv]
    Ev0=E[I['h+0+0+0'],iv]; Ec0=E[I['e+0+0+0'],ic]; kh=np.array(L['k_h']); ke=np.array(L['k_e'])
    r=dict(gap_PBE=float(gap),Epair_PBE=float(Ec0-Ev0),E_scissored=float(Ec0-Ev0+sc),Ev_minus_vbm=float(Ev0-vbm),m_center=float(mval(ke,kh,Ec0,Ev0,sc)))
    S=list(itertools.product((-1,0,1),repeat=3)); P=[h*np.array(s) for s in S]
    vv=np.array([E[I[f'h{s[0]:+d}{s[1]:+d}{s[2]:+d}'],iv] for s in S]); cc=np.array([E[I[f'e{s[0]:+d}{s[1]:+d}{s[2]:+d}'],ic] for s in S])
    fv=qfit(P,vv); fc=qfit(P,cc)
    ev=lambda x: fv[0]+fv[1]@x+0.5*x@fv[2]@x; ec=lambda x: fc[0]+fc[1]@x+0.5*x@fc[2]@x
    fun=lambda x: mval(ke+x[:3],kh+x[3:],ec(x[:3]),ev(x[3:]),sc)
    o=minimize(fun,np.zeros(6),method='Nelder-Mead',options=dict(xatol=1e-9,fatol=1e-12,maxiter=40000,maxfev=40000,adaptive=True))
    x=o.x; r.update(m_reminimised=float(o.fun),dk_e=x[:3].tolist(),dk_h=x[3:].tolist(),step_max=float(np.max(abs(x))),fit_rms_meV=[float(fv[3]*1e3),float(fc[3]*1e3)],
                  E_reminimised=float(ec(x[:3])-ev(x[3:])+sc),q_keV_reminimised=float(np.linalg.norm(ke+x[:3]-kh-x[3:])/K))
    # hole and electron inverse-mass tensors (1/m_e): eps = hbar^2 k^2 / 2m, k in 2pi/a -> hbar^2 (2pi/a)^2 / m_e = 2 Ry * (2pi/a_bohr)^2 * ... use 7.61996 eV A^2
    conv=(tp/A)**2*7.61996                         # eV per (1/m_e) for unit (2pi/a)^2 curvature
    r['hole_inv_mass_eig']=np.linalg.eigvalsh(-fv[2]/conv).tolist(); r['elec_inv_mass_eig']=np.linalg.eigvalsh(fc[2]/conv).tolist()
    r['hole_mzz']=float(conv/(-fv[2][2,2])); r['elec_mzz']=float(conv/fc[2][2,2])
    # axis pair and q* pair
    r['axis_pair_E']=float(E[I['axc'],ic]-E[I['axv'],iv]+sc); r['qstar_E']=float(E[I['qsc'],ic]-E[I['qsv'],iv]+sc)
    if spin:
        rq=rho(d,I['kc'],I['G'],True); rm=rho(d,I['e+0+0+0'],I['h+0+0+0'],True)
        r['Gamma8_levels_meV']=((E[I['G'],4:8]-vbm)*1e3).tolist()
        r['soc_axis_extremum']=dict(quartet_over2=float(np.sum(abs(rq[8:10,4:8])**2)/2),top_pair_over2=float(np.sum(abs(rq[8:10,6:8])**2)/2),
                                    second_pair_over2=float(np.sum(abs(rq[8:10,4:6])**2)/2),all_valence_over2=float(np.sum(abs(rq[8:10,2:8])**2)/2))
        r['soc_mirror_optimum']=dict(top_pair_over2=float(np.sum(abs(rm[8:10,6:8])**2)/2),second_pair_over2=float(np.sum(abs(rm[8:10,4:6])**2)/2))
    else:
        rm=rho(d,I['e+0+0+0'],I['h+0+0+0'],False); dz=h*tp/A
        def r2(e,hh,b=iv): return float(abs(rho(d,I[e],I[hh],False)[ic,b])**2)
        a2=(r2('e+0+0+1','h+0+0+0')+r2('e+0+0-1','h+0+0+0'))/2            # electron leg alone (= d/dq_z at fixed k_v, CW1 'dqz')
        b2=(r2('e+0+0+0','h+0+0+1')+r2('e+0+0+0','h+0+0-1'))/2            # hole leg alone
        p2=(r2('e+0+0+1','h+0+0+1')+r2('e+0+0-1','h+0+0-1'))/2            # both legs (= d/dk_z at fixed q, CW1 'dkz')
        m2=(r2('e+0+0+1','h+0+0-1')+r2('e+0+0-1','h+0+0+1'))/2
        reab=(p2-m2)/4                                                      # Re(alpha beta*) delta^2
        fe=r['elec_mzz']/(r['hole_mzz']+r['elec_mzz']); fh=1-fe            # relaxed pair (centre of mass): k_e moves by m_e/(m_e+m_h) dq_z, k_h by -m_h/(m_e+m_h) dq_z
        grel2=fe**2*a2+fh**2*b2-2*fe*fh*reab
        r['vertex']=dict(rho2_per_band=[float(abs(rm[ic,b])**2) for b in range(4)],dqz_A=float(np.sqrt(a2)/dz),dhz_A=float(np.sqrt(b2)/dz),dkz_A=float(np.sqrt(p2)/dz),
                         cos_ab=float(reab/np.sqrt(a2*b2)),f_e=float(fe),g_rel_A=float(np.sqrt(grel2)/dz),bias_rel=float(grel2/a2),
                         bias_band=[float((np.sqrt(a2)-np.sqrt(b2))**2/a2),float((np.sqrt(a2)+np.sqrt(b2))**2/a2)])
    R[v]=r
if len(VARS)==3:
  R['SOC_minus_S12_meV']=dict(center=1e3*(R['SOC']['E_scissored']-R['S12']['E_scissored']),axis=1e3*(R['SOC']['axis_pair_E']-R['S12']['axis_pair_E']),
                            qstar=1e3*(R['SOC']['qstar_E']-R['S12']['qstar_E']))
  R['SOC_minus_FRav_meV']=dict(center=1e3*(R['SOC']['E_scissored']-R['FRav']['E_scissored']),axis=1e3*(R['SOC']['axis_pair_E']-R['FRav']['axis_pair_E']),
                             qstar=1e3*(R['SOC']['qstar_E']-R['FRav']['qstar_E']))
  qs=L['qstar']; R['qstar']=dict(q_keV=0.9,E_wannier_aPBE=qs['E_wannier'],**{f'E_{v}':R[v]['qstar_E'] for v in ('S12','FRav','SOC')})
json.dump(R,open(out,'w'),indent=1); print(json.dumps(R,indent=1))
