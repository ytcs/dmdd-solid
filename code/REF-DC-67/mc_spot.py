"""Claim 5 spot check: own MC vs library rows vs own high-N solver.  SiO2-q (worst row of DC-67 conv_h), m1; then Si m1.  Rows chosen by argv."""
import numpy as np, csv, json, sys, time
import ref_casc as R
D='../DC-67/data/'
S={(r['material'],r['cfg']):r for r in csv.DictReader(open(D+'library_summary.csv'))}
out={}
def spot(m,c,xs,M,k,carrier=0):
    r=S[(m,c)]; N=int(r['N']); lam=float(r['lam']); w=float(r['w']); W=None if r['W']=='' else float(r['W']); Nz=int(r['Nz'])
    d=np.load(D+'lib/'+m+'.npz'); xt=d['x_'+c]; P=d[('Pe_' if carrier==0 else 'Ph_')+c]
    x,Q,s=R.gf(lam,w,max(xs)+.5,N*k,Nz,W=W); Q=Q[carrier]
    res=[]
    for xx in xs:
        i=np.argmin(abs(xt-xx)); x0=xt[i]
        t=time.time(); c_=np.concatenate([R.mc(lam,w,x0,500000,W=W,seed=int(1e6*x0)%99991+j,carrier=carrier) for j in range(M//500000)])
        hst=np.bincount(c_,minlength=Nz)[:Nz]/c_.size; se=np.sqrt(np.maximum(hst*(1-hst),1e-30)/c_.size)
        p=np.zeros(Nz); p[:min(Nz,P.shape[1])]=P[i][:Nz]
        q=Q[int(round(x0*N*k))]
        sel=hst>2e-4
        zlib=((p-hst)[sel]/se[sel]); zref=((q-hst)[sel]/se[sel])
        row=dict(x=float(x0),lib_vs_mc=float(np.abs(p-hst).max()),ref_vs_mc=float(np.abs(q-hst).max()),lib_vs_ref=float(np.abs(p-q).max()),zmax_lib=float(np.abs(zlib).max()),zmax_ref=float(np.abs(zref).max()),chi2_ref=float((zref**2).sum()),dof=int(sel.sum()),mean_mc=float(c_.mean()),mean_lib=float(p@np.arange(Nz)),var_mc=float(c_.var()),var_lib=float(p@np.arange(Nz)**2-(p@np.arange(Nz))**2),se=float(se.max()))
        print(m,c,carrier,row,time.time()-t,flush=True); res.append(row)
    out[f'{m}_{c}_{carrier}']=res
for a in sys.argv[1:]:
    m,c,car,k,M,xs=a.split(':'); spot(m,c,[float(v) for v in xs.split(',')],int(M),int(k),int(car))
json.dump(out,open('data/mc_spot_%s.json'%sys.argv[1].split(':')[0],'w'),indent=1)
