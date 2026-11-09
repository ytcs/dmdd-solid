"""Claim 1: Gaussian/Edgeworth match beyond the table.  Own P(n|x) to x = 320 (Si V0, A = 5.5878), every grid row sampled."""
import numpy as np, json, time
from scipy.stats import norm
import ref_casc as R
A0=5.587791442871094; Eg=1.164; w=.063/Eg; W=12/Eg
N=128; X=240.0; Nz=128
import os
t0=time.time()
if os.path.exists('data/x1_P_Si.npz'):
    _d=np.load('data/x1_P_Si.npz'); x=_d['x']; Pe=_d['P']
else:
    idx=np.arange(int(4*N),int(X*N)+1,N//8)     # every 1/8 E_g from x = 4
    x,(Pe,Ph),s=R.gf(A0/Eg**3,w,X,N,Nz,W=W,rows=idx)
    np.savez_compressed('data/x1_P_Si.npz',x=x,P=Pe.astype(np.float64))
print('solve',time.time()-t0,flush=True)
n=np.arange(Nz)
m1=Pe@n; c=n[None,:]-m1[:,None]
k2=(Pe*c**2).sum(1); k3=(Pe*c**3).sum(1); k4=(Pe*c**4).sum(1)-3*k2**2
print('sumP-1',np.abs(Pe.sum(1)-1).max(),'Pmin',Pe.min())
sel=x>=80
pk=[np.polyfit(1+x[sel],k[sel],1) for k in (m1+1,k2,k3,k4)]
print('linear fits (slope, offset) of cumulants vs omega',pk)
eps=1/pk[0][0]; Fas=pk[1][0]/pk[0][0]
# author's inputs (library m1 row of Si): fitted on [X/2, X] with X = 40
e_lib,F_lib,b_lib=3.7490/Eg,0.1138,None
def bin_g(mean,var):
    sd=np.sqrt(var)
    return norm.cdf((n+.5-mean)/sd)-norm.cdf((n-.5-mean)/sd)
def pt(mean,var):
    sd=np.sqrt(var); return np.exp(-.5*((n-mean)/sd)**2)/np.sqrt(2*np.pi)/sd
def edge(mean,k2_,k3_,k4_,order):
    sd=np.sqrt(k2_); z=(n-mean)/sd
    He3=z**3-3*z; He4=z**4-6*z**2+3; He6=z**6-15*z**4+45*z**2-15
    g1=k3_/sd**3; g2=k4_/sd**4
    corr=1+g1*He3/6
    if order>=2: corr=corr+g2*He4/24+g1**2*He6/72
    return np.exp(-.5*z*z)/np.sqrt(2*np.pi)/sd*corr
rows=[]
for i,xi in enumerate(x):
    P=Pe[i]; om=1+xi; mean_as=om/eps+pk[0][1]; var_as=Fas*om/eps+pk[1][1]
    Nmean=m1[i]; v=k2[i]
    # all compared in N_sub; asymptotic mean is of 1 + N_sub
    r=dict(x=xi,mean=Nmean,var=v,
      B_as=np.abs(P-bin_g(mean_as-1,Fas*om/eps)).max(),
      B_ex=np.abs(P-bin_g(Nmean,v)).max(),
      S_ex=np.abs(P-bin_g(Nmean,v-1/12)).max() if v>1/12 else np.nan,
      L_ex=np.abs(P-pt(Nmean,v)).max(),
      E1_ex=np.abs(P-edge(Nmean,v,k3[i],k4[i],1)).max(),
      E2_ex=np.abs(P-edge(Nmean,v,k3[i],k4[i],2)).max(),
      E1_as=np.abs(P-edge(mean_as-1,var_as,np.polyval(pk[2],om),np.polyval(pk[3],om),1)).max(),
      E2_as=np.abs(P-edge(mean_as-1,var_as,np.polyval(pk[2],om),np.polyval(pk[3],om),2)).max())
    rows.append(r)
keys=[k for k in rows[0] if k not in('x','mean','var')]
A={k:np.array([r[k] for r in rows]) for k in keys}
print('x-window envelope  max over [a, 1.5a)  '+' '.join(keys))
env={}
for a in (5,7.5,10,15,20,30,40,60,80,120,160):
    s_=(x>=a)&(x<1.5*a)
    env[a]={k:float(A[k][s_].max()) for k in keys}
    print(a,' '.join('%.2e'%env[a][k] for k in keys))
for k in keys:
    a_=np.array([a for a in env if a>=40]);v=np.array([env[a][k] for a in a_]); print(k,'envelope exponent x>=40: %.3f'%np.polyfit(np.log(a_),np.log(v),1)[0],' C = E*x at largest %.3f'%(v[-1]*a_[-1]))
# author's own sample points
for xx in (10,15,20,30,40):
    i=np.argmin(abs(x-xx)); print(xx,{k:'%.2e'%A[k][i] for k in keys},'mean %.3f var %.3f'%(m1[i],k2[i]),flush=True)
# predicted coefficient
K3=pk[2][0]/pk[0][0]; Fm=pk[1][0]/pk[0][0]
print('K3 = k3 per pair %.4f, F %.4f; predicted E*x = 0.0917 K3/F^2 * eps = %.3f'%(K3,Fm,.0917*abs(K3)/Fm**2*eps))
json.dump(dict(pk=[list(map(float,p)) for p in pk],env={str(k):v for k,v in env.items()},K3=float(K3),F=float(Fm),eps=float(eps)),open('data/x1_gauss.json','w'),indent=1)
