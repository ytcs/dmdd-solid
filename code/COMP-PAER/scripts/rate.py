"""Tier-B order-of-magnitude PAER rate and reach in Si (data-calibrated optical limit x first-principles finite-q proxy).
Model [E]:  S̄^{PA}(q,ω) = q² L(q,ω)/(2πα),  L(q,ω) = ε₂^{PA,opt}(ω) F(q) f_win(q,ω) / ε₁(q,ω)²
  ε₂^{PA,opt}: Macfarlane et al. 20 K absorption (via 1202.3454 Fig. 2, digitised), T≈0 (emission branch; excitonic replicas included)
  F(q): finite-q proxy F_ρ from formfactor.py (central); band [F_ρ/3, min(1,3F_ρ)] [E]
  ε₁(q,ω): Cappellini model with ε₁(0,ω) = n(ω)²
  f_win: angular fraction of q̂ with ω <= E_min(q) - δ0 (DFT+scissor E_min, window theorem (M.9)); δ0 = 0.3 eV (strict) or 0 (incl. edge shell)
Rate (M.6): dℛ/dω = ρ_χ σ̄_e/(4π m_χ ρ_T μ²) ∫ q dq F_DM² η(v_min) S̄.  Reach: 3 events, 1 kg·yr, background-free, ω >= E_th ⇒ >= 1 e⁻."""
import numpy as np, json, sys
sys.path.insert(0,'/home/user/dmdd-solid/code/COMP-PAER/scripts')
from halo import make_eta
eta,vmax=make_eta()
alpha=1/137.035999; me=510998.95; hbarc_cm=1.97327e-5; A2eV=1973.27   # q[eV] = q[Å^-1]*1973.27
rho_chi=0.3e9*hbarc_cm**3; rho_T=2.329*5.60959e32*hbarc_cm**3
cm2=1/hbarc_cm**2; KGYR=5.60959e35*3.15576e7/6.58212e-16
D=json.load(open(sys.argv[1]))      # tables: F(q) and E_min angular data
qF=np.array(D['qF']); Fc=np.array(D['F']); Fs=np.array(D['Fsat'])
qE=np.array(D['qE']); Emin_dirs=np.array(D['Emin_dirs'])   # shape (nq, ndir) in eV
def alpha_cm(w):   # T≈0 Si absorption (cm^-1); (αħω)^{1/2} = 0.65 + 78 (ω - 1.212) above the TO knee, linear ramp from 1.160 below
    y=np.where(w>1.212,0.65+78*(w-1.212),np.clip(0.65*(w-1.160)/0.052,0,None))
    return y**2/w
def n_ref(w): return 3.55+0.37*(w-1.17)
def eps2opt(w): return n_ref(w)*alpha_cm(w)*hbarc_cm/w
def eps1(qA,w):
    e0=n_ref(w)**2; q=qA*0.529177; kTF=1.104; wp=0.610
    return 1+1/(1/(e0-1)+1.563*(q/kTF)**2+q**4/(4*wp**2))
Esort=np.sort(Emin_dirs,axis=1)   # angular quantiles of E_min(|q|,q̂)
def fwin(qA,w,delta0):
    i=min(max(np.searchsorted(qE,qA),1),len(qE)-1); t=(qA-qE[i-1])/(qE[i]-qE[i-1])
    Em=(1-t)*Esort[i-1]+t*Esort[i]
    return np.mean(w<=Em-delta0)
def Sbar(qA,w,Fq,delta0):
    L=eps2opt(w)*Fq/eps1(qA,w)**2*fwin(qA,w,delta0)
    return (qA*A2eV)**2*L/(2*np.pi*alpha)
def rate(m,light=False,band='c',delta0=0.3,wgrid=None):
    mu=m*me/(m+me)
    wgrid=np.arange(1.161,1.62,0.004) if wgrid is None else wgrid
    qA=np.linspace(0.05,2.4,240); q=qA*A2eV
    Ftab=np.interp(qA,qF,Fc if band=='c' else (Fs if band=='lo' else np.minimum(1,3*Fc)))
    FDM2=(alpha*me/q)**4 if light else 1.0
    dR=[]
    for w in wgrid:
        vmin=w/q+q/(2*m)
        S=np.array([Sbar(a,w,f,delta0) if vm<vmax else 0 for a,f,vm in zip(qA,Ftab,vmin)])
        dR.append(rho_chi/(4*np.pi*m*rho_T*mu**2)*np.trapezoid(q*FDM2*eta(vmin)*S,q))
    dR=np.array(dR)                     # per eV per σ̄_e[eV^-2]
    R=np.trapezoid(dR,wgrid)*KGYR*cm2   # events /kg/yr per cm^2 of σ̄_e (σ̄[eV^-2] = σ̄[cm^2]·cm2)
    return R, wgrid, dR
if __name__=='__main__':
    out={}
    for light in (False,True):
        for band in ('lo','c','hi'):
            for d0 in (0.3,0.0):
                rows=[]
                for m in [0.334,0.337,0.34,0.35,0.36,0.38,0.40,0.42,0.43,0.46,0.50,0.54,0.60]:
                    R,_,_=rate(m*1e6,light,band,d0)
                    rows.append((m,R,3/R if R>0 else np.inf))
                out[f"{'light' if light else 'heavy'}_{band}_d{d0}"]=rows
    json.dump(out,open(sys.argv[2],'w'),indent=1)
    for k,v in out.items():
        print(k); [print('  %.3f MeV  R/σ=%.3e /kg/yr/cm2  σ95=%.2e cm2'%r) for r in v]
