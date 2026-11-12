# Coherent zero-phonon Migdal response vs eq:8.3-boostward in the local-pseudopotential Si model.
import numpy as np, sys, time
from migcoh12 import *
NK=int(sys.argv[2]) if len(sys.argv)>2 else 6
rng=np.random.default_rng(1)
dirs=rng.normal(size=(int(sys.argv[3]) if len(sys.argv)>3 else 8,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
ks=mesh(NK)
t0=time.time()
base=[solve(k) for k in ks]
qkeV=np.array([0.1,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.5,3.0,4.0,5.0,7.0,10.0])
out=[]
for qk in qkeV:
    acc=dict(coh=0.,cohdiag=0.,ident=0.,incK=0.)
    for d in dirs:
        q=qk/KEV_PER_AU*d
        for (ev,cv,Iv),k in zip(base,ks):
            ec,cc,Ic=solve(k+q)
            R=rho(ev,cv,Iv,ec,cc,Ic)                 # (nG,NC,NV)
            p=q+GG; pn=np.linalg.norm(p,axis=1)
            vert=(p@q)*wcb.w(pn)/Omega                 # (nG,)
            dE=ec[NV:,None]-ev[None,:NV]               # (NC,NV)
            C=np.einsum('g,gcv->cv',vert*S,R)
            i0=np.argmin(pn-np.linalg.norm(q)+np.linalg.norm(GG,axis=1)*10)  # G=0 index
            i0=np.where((IG==0).all(1))[0][0]
            acc['coh']+=0.5*np.sum(abs(C)**2/dE**4)
            acc['cohdiag']+=0.5*np.sum(np.einsum('g,gcv->cv',abs(vert*S)**2,abs(R)**2)/dE**4)
            acc['ident']+=0.5*np.sum(abs(R[i0])**2)
            acc['incK']+=np.sum(np.einsum('g,gcv->cv',abs(vert)**2,abs(R)**2)/dE**4)
    n=len(dirs)*len(ks)
    row=[qk]+[acc[x]/n/qk**2 for x in ['coh','cohdiag','ident','incK']]
    out.append(row)
    print(f"q={qk:5.2f} keV coh/q2={row[1]:.4e} cohdiag={row[2]:.4e} ident={row[3]:.4e} incK={row[4]:.4e}  coh/ident={row[1]/row[3]:.3f} coh/cohdiag={row[1]/row[2]:.3f}  t={time.time()-t0:.0f}s",flush=True)
