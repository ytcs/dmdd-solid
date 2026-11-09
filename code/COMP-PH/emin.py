"""E_min^{ZPL}(q) = min_k [eps_c(k+q) - eps_v(k)] (lowest c, highest v; q unreduced, any direction) from the Wannier TB
Hamiltonian (seed_hr.dat), PBE + scissor. usage: emin.py MAT alat_bohr nv(in wannier subspace) Eg_target_eV out.json"""
import numpy as np, sys, json
from scipy.optimize import minimize
m, al, nv, Egt, out = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
W=f"/root/work/COMP-PH/{m}/wan/{m}_hr.dat"
L=open(W).read().split('\n'); nw=int(L[1]); nr=int(L[2]); deg=[]
i=3
while len(deg)<nr: deg+= [int(x) for x in L[i].split()]; i+=1
dat=np.array([[float(x) for x in l.split()] for l in L[i:] if l.strip()])
R=dat[::nw*nw,:3].astype(int); H=(dat[:,5]+1j*dat[:,6]).reshape(nr,nw,nw).transpose(0,2,1)  # H[R][m,n] (file: n fastest? see below)
H=(dat[:,5]+1j*dat[:,6]).reshape(nr,nw*nw)
mm=dat[:nw*nw,3].astype(int)-1; nn=dat[:nw*nw,4].astype(int)-1
Hm0=np.zeros((nr,nw,nw),complex); Hm0[:,mm,nn]=H; Hm0/=np.array(deg)[:,None,None]
import os
WS=W.replace('_hr.dat','_wsvec.dat'); acc={}
if os.path.exists(WS) and 'true' in open(WS).readline():
    Lw=open(WS).read().split('\n')[1:]; j=0; Ridx={tuple(r):i for i,r in enumerate(R)}
    while j<len(Lw) and Lw[j].strip():
        r1,r2,r3,a_,b_=map(int,Lw[j].split()); nT=int(Lw[j+1]); Ts=[list(map(int,Lw[j+2+t].split())) for t in range(nT)]; j+=2+nT
        h=Hm0[Ridx[(r1,r2,r3)],a_-1,b_-1]
        for T in Ts:
            key=(r1+T[0],r2+T[1],r3+T[2]); acc.setdefault(key,np.zeros((nw,nw),complex))[a_-1,b_-1]+=h/nT
    R=np.array(list(acc.keys())); Hm=np.array(list(acc.values())); print('ws_distance: using',len(R),'vectors')
else:
    Hm=Hm0
A=al/2*np.array([[-1,0,1],[0,1,1],[-1,1,0]]); Rc=R@A
tpiba=2*np.pi/al
def bands(kc):  # kc: (N,3) cartesian in 2pi/a
    ph=np.exp(1j*(kc*tpiba)@Rc.T)            # N x nr
    Hk=np.einsum('nr,rij->nij',ph,Hm)
    return np.linalg.eigvalsh(Hk)
# gap and valley
g=np.linspace(0,1,201); kx=np.stack([g,0*g,0*g],1); e=bands(kx)
vbm=bands(np.zeros((1,3)))[0,nv-1]; ic=np.argmin(e[:,nv]); cbm=e[ic,nv]
Egpbe=cbm-vbm
eL=bands(np.array([[.5,.5,.5]]))[0]; eX=bands(np.array([[1.,0,0]]))[0]; eG=bands(np.zeros((1,3)))[0]
# refine CBM over all k (Ge: L)
res=minimize(lambda k: bands(k[None])[0,nv], x0=[g[ic],0,0] if eX[nv]<eL[nv] or m=='Si' else [.5,.5,.5], method='Nelder-Mead', options=dict(xatol=1e-6,fatol=1e-7))
kc=res.x; cbm=res.fun; Egpbe=cbm-vbm; sc=Egt-Egpbe
print(f"{m}: VBM {vbm:.4f} CBM {cbm:.4f} at k={kc} (2pi/a); E_g^PBE {Egpbe:.4f} eV; Gamma direct {eG[nv]-eG[nv-1]:.4f}; L c {eL[nv]-vbm:.4f}; X c {eX[nv]-vbm:.4f}; scissor {sc:+.4f}")
# E_min(q): q in keV; 1 bohr^-1 = 3.7289 keV; q (2pi/a units) = q_keV/3.7289/tpiba
def emin_vec(qc):
    f=lambda k: bands((k+qc)[None])[0,nv]-bands(k[None])[0,nv-1]
    # coarse search over k in a grid near Gamma and near (valley - q)
    best=None
    ev=bands(KG)[:,nv-1]; ec=bands(KG+qc)[:,nv]; d=ec-ev; idx=np.argsort(d)[:4]
    starts=[KG[i] for i in idx]
    for k0 in starts+[np.zeros(3)]+[s*v-qc for v in np.eye(3)*np.linalg.norm(kc) for s in (1,-1)]+[np.array(v)*.5*s-qc for v in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)] for s in (1,-1)]:
        r=minimize(f,k0,method='Nelder-Mead',options=dict(xatol=1e-5,fatol=1e-6,maxiter=4000))
        if best is None or r.fun<best[0]: best=(r.fun,r.x)
    return best[0]+sc
b=np.array([[-1,-1,1],[1,1,1],[-1,1,-1]],float)  # fcc recip (2pi/a)
b=np.array([[-1,-1,1],[1,1,1],[-1,1,-1]],float)
ng=18; ii=np.arange(ng)/ng
KG=np.array([[x,y,z] for x in ii for y in ii for z in ii])@b
qs=[0.25,0.5,0.75,0.9,1.0,1.1,1.25,1.5,1.75,2.0,2.25,2.5,3.0]
dirs={'100':(1,0,0),'110':(1,1,0),'111':(1,1,1),'210':(2,1,0),'211':(2,1,1)}
tab={}
for d,v in dirs.items():
    v=np.array(v,float)/np.linalg.norm(v)
    tab[d]=[emin_vec(v*q/3.7289/tpiba) for q in qs]
    print(d,' '.join(f"{q}:{x:.4f}" for q,x in zip(qs,tab[d])),flush=True)
json.dump(dict(Eg_pbe=Egpbe,scissor=sc,kc=list(kc),vbm=vbm,gamma_direct=float(eG[nv]-eG[nv-1]),Lc=float(eL[nv]-vbm),Xc=float(eX[nv]-vbm),q_keV=qs,Emin=tab),open(out,'w'),indent=1)
