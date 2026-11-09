"""Claim 3: Si epsilon, F, recalibration, own solver; X and fit-window dependence.  Output data/si_claim3.json"""
import numpy as np, json, sys
from scipy.optimize import brentq
import ref_casc as R
A0=5.587791442871094; Eg=1.164; w=.063/Eg; W=12/Eg
def run(A,N=1552,X=40.0,win=None,w_=w,Eg_=Eg):
    x,m,e2,s=R.moments(A/Eg_**3,w_,X,N,W=12/Eg_)
    f=R.fit(x,m[0],e2[0],*(win or (X/2,X)))
    return f[0]*Eg_,f[1],f[2],(x,m,e2)
out={}
e,F,b,_=run(A0); out['A0']=dict(A=A0,eps=e,F=F,b=b)
Ac=brentq(lambda A:run(A)[0]-3.749,5.5,5.7,xtol=1e-6)
e,F,b,_=run(Ac); out['recal']=dict(A=Ac,eps=e,F=F,b=b,sig=(.119-F)/.002)
print(out,flush=True)
# X / window dependence at A0 and Ac, N = 776
wins={}
for A,lab in ((A0,'A0'),(Ac,'Ac')):
    _,_,_,(x,m,e2)=run(A,N=776,X=320.0)
    for lo,hi in ((10,20),(15,30),(20,40),(40,80),(80,160),(160,320),(20,320)):
        f=R.fit(x,m[0],e2[0],lo,hi); wins[f'{lab}_{lo}_{hi}']=(f[0]*Eg,f[1],f[2],f[3]); print(lab,lo,hi,f[0]*Eg,f[1],f[2],f[3],flush=True)
    # secant at large x
    i=lambda v:int(round(v*776))
    v=e2[0]-m[0]**2
    print('secant 160-320 eps',Eg*(320-160)/(m[0][i(320)]-m[0][i(160)]),'F',(v[i(320)]-v[i(160)])/(m[0][i(320)]-m[0][i(160)]),flush=True)
    wins[lab+'_sec']=(Eg*(320-160)/(m[0][i(320)]-m[0][i(160)]),(v[i(320)]-v[i(160)])/(m[0][i(320)]-m[0][i(160)]))
out['win']=wins
# sensitivities: F, eps vs A
for dA in (.05,):
    e1,F1,_,_=run(A0+dA); e0,F0,_,_=run(A0); out['dedA']=(e1-e0)/dA; out['dFdA']=(F1-F0)/dA
# calibrating at the production number: v3 grid offset
print(out['dedA'],out['dFdA'])
json.dump(out,open('data/si_claim3.json','w'),indent=1,default=float)
