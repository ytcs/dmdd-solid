"""Coherent zero-phonon Migdal amplitude vs diagonal/incoherent forms in a local-pseudopotential model of Si.
Non-interacting electrons in rigid screened ions w(p) (Cohen-Bergstresser form factors, PCHIP in p^2);
the same w is the Hamiltonian potential and the vertex, so the force (acoustic) sum rule holds exactly.
Hartree a.u."""
import numpy as np, sys, time
from model import a, Omega
import wcb
b=2*np.pi/a
B=b*np.array([[-1,1,1],[1,-1,1],[1,1,-1]],float)
Binv=np.linalg.inv(B)
tau=a/8*np.ones(3)
HA=27.211386; KEV_PER_AU=3.72894
ECUT=float(sys.argv[1]) if len(sys.argv)>1 else 6.0
NV,NC=4,12
NGRID=40
r=np.arange(-9,10)
IALL=np.array(np.meshgrid(r,r,r,indexing='ij')).reshape(3,-1).T
GALL=IALL@B
def solve(k):
    kg=k+GALL; T=0.5*(kg**2).sum(1); m=T<=ECUT
    G=GALL[m]; I=IALL[m]
    dG=G[:,None,:]-G[None,:,:]
    V=wcb.w(np.linalg.norm(dG,axis=2))*np.cos(dG@tau)*2/Omega
    np.fill_diagonal(V,0.0)
    e,c=np.linalg.eigh(V+np.diag(T[m]))
    return e[:NV+NC],c[:,:NV+NC],I
def to_grid(c,I):
    g=np.zeros((NGRID,NGRID,NGRID,c.shape[1]),complex)
    g[I[:,0]%NGRID,I[:,1]%NGRID,I[:,2]%NGRID]=c
    return g
# transfer G list: those with |G| <= 6 b (+ margin)
mG=np.linalg.norm(GALL,axis=1)<=6.6*b
IG=IALL[mG]; GG=GALL[mG]
S=2*np.cos(GG@tau)
def rho(ev,cv,Iv,ec,cc,Ic):
    """rho[g, c, v] = <c,k'| e^{i(k'-k+G)r} |v,k> for G in IG."""
    gc=to_grid(cc[:,NV:],Ic)               # conduction coefficients on grid
    idx=(Iv[None,:,:]+IG[:,None,:])%NGRID  # (nG, nPWv, 3)
    gath=gc[idx[...,0],idx[...,1],idx[...,2]]   # (nG,nPWv,NC)
    return np.einsum('gpc,pv->gcv',gath.conj(),cv[:,:NV])
def mesh(n,shift=0.5):
    t=(np.arange(n)+shift)/n
    f=np.array(np.meshgrid(t,t,t,indexing='ij')).reshape(3,-1).T
    return f@B
