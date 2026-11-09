"""Shared loader: Si Wannier TB Hamiltonian of COMP-PH (PBE, a_PBE = 10.3507 bohr, 8 sp3 WFs, 14^3 k, ws_distance), band function bands(k)
(k cartesian, 2pi/a), VBM, CBM position kc and the scissor sc to E_g(0) = 1.170 eV.
(reads /root/work/COMP-PH/Si/wan/Si_hr.dat, _wsvec.dat; read-only)"""
import numpy as np, sys, json, os
from scipy.optimize import minimize
al=10.3507; nv=4; Egt=1.170
import gzip
W="/root/work/COMP-PH/Si/wan/Si_hr.dat"
HERE=os.path.dirname(os.path.abspath(__file__))
def _open(p):   # committed copies (code/CW1/out/*.gz, sha256 of Si_hr.dat starts 35552c44b7d6c259) if the COMP-PH work dir is gone
    return open(p).read() if os.path.exists(p) else gzip.open(f"{HERE}/../out/{os.path.basename(p)}.gz",'rt').read()
L=_open(W).split('\n'); nw=int(L[1]); nr=int(L[2]); deg=[]; i=3
while len(deg)<nr: deg+=[int(x) for x in L[i].split()]; i+=1
dat=np.array([[float(x) for x in l.split()] for l in L[i:] if l.strip()])
R=dat[::nw*nw,:3].astype(int); H=(dat[:,5]+1j*dat[:,6]).reshape(nr,nw*nw)
mm=dat[:nw*nw,3].astype(int)-1; nn=dat[:nw*nw,4].astype(int)-1
Hm0=np.zeros((nr,nw,nw),complex); Hm0[:,mm,nn]=H; Hm0/=np.array(deg)[:,None,None]
WS=W.replace('_hr.dat','_wsvec.dat'); acc={}
Lw=_open(WS).split('\n')[1:]; j=0; Ridx={tuple(r):i for i,r in enumerate(R)}
while j<len(Lw) and Lw[j].strip():
    r1,r2,r3,a_,b_=map(int,Lw[j].split()); nT=int(Lw[j+1]); Ts=[list(map(int,Lw[j+2+t].split())) for t in range(nT)]; j+=2+nT
    h=Hm0[Ridx[(r1,r2,r3)],a_-1,b_-1]
    for T in Ts:
        key=(r1+T[0],r2+T[1],r3+T[2]); acc.setdefault(key,np.zeros((nw,nw),complex))[a_-1,b_-1]+=h/nT
R=np.array(list(acc.keys())); Hm=np.array(list(acc.values()))
A=al/2*np.array([[-1,0,1],[0,1,1],[-1,1,0]]); Rc=R@A; tpiba=2*np.pi/al
def bands(kc):
    ph=np.exp(1j*(kc*tpiba)@Rc.T); return np.linalg.eigvalsh(np.einsum('nr,rij->nij',ph,Hm))
vbm=bands(np.zeros((1,3)))[0,nv-1]
r=minimize(lambda k: bands(k[None])[0,nv],x0=[0.84,0,0],method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-8))
kc=r.x; sc=Egt-(r.fun-vbm)
