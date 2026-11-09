import sys; sys.path.insert(0,'/home/ytc/Projects/bm-paer/campaign/paer/code/DC-2-alpha')
import numpy as np, json
from wanbands import *
from scipy.optimize import minimize
Rc,Hm=load('/home/ytc/paer-work/work/DC-2-alpha/Ge_hr.dat'); nv=8
B=lambda k: bands(Rc,Hm,k)[0]
G=np.zeros(3); L=np.array([.5,.5,.5]); X=np.array([1.,0,0])
vbm=B(G)[nv-1]; print('VBM',round(vbm,4),'valence at G',np.round(B(G)[:nv]-vbm,3))
res={k:float(B(v)[nv]-vbm) for k,v in dict(G=G,L=L,X=X).items()}; print('Wannier edges',{k:round(v,4) for k,v in res.items()},' DFT: G 0.918 L 0.749 X 1.014')
d=[(x,float(B(np.array([x,0,0]))[nv]-vbm)) for x in np.arange(.70,1.001,.02)]; xm=min(d,key=lambda t:t[1]); print('Delta min Wannier',xm,' DFT 0.8263 at 0.80')
RY=13.605693; t=2*np.pi/AL
def mass(k0,u,band,hs=(.004,.008,.016)):
    u=np.array(u,float); u/=np.linalg.norm(u); out=[]
    for h in hs:
        e0=B(k0)[band]; ep=B(k0+h*u)[band]; em=B(k0-h*u)[band]
        c=(ep+em-2*e0)/(h*t)**2      # eV bohr^2 = d2E/dk2
        out.append(2*RY/c)           # m*/m_e = hbar^2/(d2E/dk2), hbar^2/m_e = 2 Ry bohr^2
    return np.round(out,4)
print('m_l  [111]  ',mass(L,[1,1,1],nv),' target 1.59 +- 0.15')
print('m_t  [1-10] ',mass(L,[1,-1,0],nv),' target 0.082 +- 0.010')
print('m_t  [11-2] ',mass(L,[1,1,-2],nv))
print('m_G  [100]  ',mass(G,[1,0,0],nv),' target 0.038 +- 0.005')
print('m_G  [111]  ',mass(G,[1,1,1],nv))
print('m_Delta l at min',mass(np.array([xm[0],0,0]),[1,0,0],nv,(.01,.02)),' t',mass(np.array([xm[0],0,0]),[0,1,0],nv,(.01,.02)))
