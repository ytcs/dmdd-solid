"""Claim 4: convex phonon read vs truth at fixed N, moments and P; analytic prediction; Lagrange-of-P for comparison.  Own solver only."""
import numpy as np, json
import ref_casc as R
out={}
A=5.587791442871094
def case(lab,Eg,om,N,X,Wv=None,Nref=None):
    lam=A/Eg**3; w=om/Eg; W=None if Wv is None else Wv/Eg
    nf=int(np.floor(w*N)); a=w*N-nf
    # same quadrature level: 'lin' at N.  Truth: fine grid.
    xr,mr,er,_=R.moments(lam,w,X,Nref,W=W)
    x,ml,el,_=R.moments(lam,w,X,N,W=W,read='lin') if nf>=1 else (None,)*4
    if nf==0: raise SystemExit
    res=dict(N=N,nf=nf,a=a,w=w)
    k=lambda v,NN:int(round(v*NN))
    # compare on x where both grids meet: interpolate truth linearly on its fine grid
    rows=[]
    for xx in (2,3,5,10,20):
        if xx>X: continue
        i=k(xx,N); xi=x[i]
        mt=np.interp(xi,xr,mr[0]); st=np.interp(xi,xr,er[0]); vt=st-mt**2; v=el[0][i]-ml[0][i]**2
        rows.append((float(xi),float(ml[0][i]),float(mt),float(ml[0][i]/mt-1),float(v),float(vt),float(v/vt-1)))
    res['rows']=rows
    fl=R.fit(x,ml[0],el[0],X/2,X); ft=R.fit(xr,mr[0],er[0],X/2,X)
    # the same quadrature with the cubic read isolates the read
    if nf>=2:
        xc,mc_,ec,_=R.moments(lam,w,X,N,W=W,read='cubic'); fc=R.fit(xc,mc_[0],ec[0],X/2,X)
        res['cubic_same_N']=(fc[0],fc[1])
        res['maxdm_lin_vs_cubic']=float(np.abs(ml[0]-mc_[0]).max())
    res.update(eps_lin=fl[0],F_lin=fl[1],eps_true=ft[0],F_true=ft[1],deps=fl[0]/ft[0]-1,dF=fl[1]/ft[1]-1)
    print(lab,json.dumps(res,default=float),flush=True); out[lab]=res
case('Si production a=.005 N=74',1.164,.063,74,20,12.,1552)
case('Si a=1/2 N=83',1.164,.063,83,20,12.,1552)
case('Si a~1/2 N=46',1.164,.063,46,20,12.,1552)
case('SiO2 nf=1 a~.5 N=93',9.2,.149,93,20,None,3000)
case('SiO2 nf=2 a~.5 N=154',9.2,.149,154,20,None,3000)
case('PbSe production N=60',.17,.0171,60,30,None,1200)
case('PbSe a~.5 N=65',.17,.0171,65,30,None,1200)
case('C nf=1 a~.5 N=50',5.47,.163,50,20,None,2400)
json.dump(out,open('data/convex.json','w'),indent=1,default=float)
# decomposition of the CW7-C7 "+1.3%": symmetric DOS, lam 3.55, no W, X 40; continuum eps at w = 0.054 and at w_eff = 0.06
dec={}
for w_,N in ((.054,1000),(.054,2000),(.06,1000),(.06,2000),(.05,1000),(.05,2000)):
    x,m,e,_=R.moments(3.55,w_,40,N); f=R.fit(x,m[0],e[0],20,40); dec[f'{w_}_{N}']=(f[0],f[1]); print(w_,N,f[0],f[1],flush=True)
json.dump(dec,open('data/c7_decomp.json','w'),indent=1,default=float)
