import numpy as np, sys
sys.path.insert(0,'.')
from model import *
import wcb
b=2*np.pi/a
B=b*np.array([[-1,1,1],[1,-1,1],[1,1,-1]],float)  # rows
tau=a/8*np.ones(3)
def gset(Ecut):
    N=8; r=np.arange(-N,N+1)
    I=np.array(np.meshgrid(r,r,r,indexing='ij')).reshape(3,-1).T
    G=I@B
    m=0.5*(G**2).sum(1)<=Ecut*1.6
    return I[m],G[m]
def build(wfun,Ecut):
    I,G=gset(Ecut)
    return I,G
def ham(k,I,G,wfun,Ecut):
    kg=k+G; T=0.5*(kg**2).sum(1)
    m=T<=Ecut
    Gs=G[m]; Is=I[m]
    dG=Gs[:,None,:]-Gs[None,:,:]
    dn=np.linalg.norm(dG,axis=2)
    V=wfun(dn)*np.cos(dG@tau)*2/Omega
    np.fill_diagonal(V,0.0)
    H=V+np.diag(T[m])
    e,c=np.linalg.eigh(H)
    return e,c,Is
if __name__=="__main__":
    Ecut=float(sys.argv[1]) if len(sys.argv)>1 else 6
    I,G=gset(Ecut)
    pts={'G':np.zeros(3),'X':b*np.array([0,0,1.]),'L':b*np.array([.5,.5,.5])}
    for nm,k in pts.items():
        e,c,Is=ham(k,I,G,wcb.w,Ecut)
        print(nm,len(Is),np.round(e[:8]*27.211,3))
    # find CBM along Gamma-X
    eG,_,_=ham(np.zeros(3),I,G,wcb.w,Ecut); vbm=eG[3]
    best=1e9
    for t in np.linspace(0,1,41):
        e,_,_=ham(b*np.array([0,0,t]),I,G,wcb.w,Ecut); best=min(best,e[4])
    print('indirect gap eV',(best-vbm)*27.211,'direct Gamma',(eG[4]-eG[3])*27.211)
