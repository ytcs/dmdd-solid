"""(i) reader across the theta_ii = 3/2 jump (V1); (ii) direct calibration of the true asymptote of Si to 3.749 eV."""
import numpy as np, sys, json
from scipy.optimize import brentq
sys.path.insert(0,'../DC-67')
from P_casc_lib import Lib
import ref_casc as R
o={}
for m in ('LiF','Si','Ge','C'):
    L=Lib(m); xs=L.d['x_V1']; 
    i=np.searchsorted(xs,1.5-1e-9); lo,hi=xs[i-1],xs[i]
    r=[]
    for x in (1.45,1.47,1.49,1.499,1.5):
        P=L.carrier('V1',x,'e'); r.append((x,round(float(P[0]),4)))
    print(m,'rows around theta',lo,hi,'P(N_sub=0|x) reader (must be 1 for x<1.5):',r); o[m]=r
    print('   seed below threshold x_e=1.49,x_h=0.2: P(N=1) =',round(float(L.seed('V1',1.49,.2)[1]),4))
A0=5.587791442871094;Eg=1.164;w=.063/Eg;W=12/Eg
def f(A,N=776,X=160.):
    x,m,e,_=R.moments(A/Eg**3,w,X,N,W=W); r=R.fit(x,m[0],e[0],80,160); return r[0]*Eg,r[1]
Ac=brentq(lambda A:f(A)[0]-3.749,5.60,5.63,xtol=2e-6)
e,F=f(Ac); o['asym']=dict(A=Ac,eps=e,F=F,sig=(.119-F)/.002); print(o['asym'])
json.dump(o,open('data/final.json','w'),indent=1,default=float)
