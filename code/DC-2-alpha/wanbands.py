"""Interpolate Wannier bands from Ge_hr.dat + Ge_wsvec.dat (same construction as code/COMP-PH/emin.py). k in cartesian 2pi/a."""
import numpy as np, os
AL=10.692
def load(W):
    L=open(W).read().split('\n'); nw=int(L[1]); nr=int(L[2]); deg=[]; i=3
    while len(deg)<nr: deg+=[int(x) for x in L[i].split()]; i+=1
    d=np.array([[float(x) for x in l.split()] for l in L[i:] if l.strip()])
    R=d[::nw*nw,:3].astype(int); H=(d[:,5]+1j*d[:,6]).reshape(nr,nw*nw)
    mm=d[:nw*nw,3].astype(int)-1; nn=d[:nw*nw,4].astype(int)-1
    H0=np.zeros((nr,nw,nw),complex); H0[:,mm,nn]=H; H0/=np.array(deg)[:,None,None]
    Lw=open(W.replace('_hr.dat','_wsvec.dat')).read().split('\n')[1:]; j=0; idx={tuple(r):i for i,r in enumerate(R)}; acc={}
    while j<len(Lw) and Lw[j].strip():
        r1,r2,r3,a,b=map(int,Lw[j].split()); nT=int(Lw[j+1]); Ts=[list(map(int,Lw[j+2+t].split())) for t in range(nT)]
        h=H0[idx[(r1,r2,r3)],a-1,b-1]
        for T in Ts:
            acc.setdefault((r1+T[0],r2+T[1],r3+T[2]),np.zeros((nw,nw),complex))[a-1,b-1]+=h/nT
        j+=2+nT
    R=np.array(list(acc.keys())); Hm=np.array(list(acc.values()))
    A=AL/2*np.array([[-1,0,1],[0,1,1],[-1,1,0]]); return R@A,Hm
def bands(Rc,Hm,k):
    ph=np.exp(1j*(np.atleast_2d(k)*2*np.pi/AL)@Rc.T); return np.linalg.eigvalsh(np.einsum('nr,rij->nij',ph,Hm))
