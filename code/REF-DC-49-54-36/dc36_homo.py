"""Referee: size of the dropped |F_homo|^2 term of 2512.16451, closed-form angular integrals (no truncated theta grid).
Int dOmega/4pi (1-cos) F(q) = I. sphere: I_h = G(2kR)/(4 k^4 R^4), G(X)=Int_0^X x^3 F(x) dx, F=9(sin x-x cos x)^2/x^6
fluctuation: I_f = (dn2/n0^2)(6 xi^3/R^3) [ln(1+Y)-Y/(1+Y)]/(8 k^4 xi^4), Y=4k^2 xi^2.  a ~ <v k vz/v I>.
Also DC-36's truncated grid (om >= e^-14) for comparison, the differential (Ti minus PtRh) of the homogeneous term, and the ratio of the true-geometry exact surface force to the published benchmark."""
import numpy as np
from scipy.integrate import quad
CM=5.067731e4; KG=5.609589e35; c=299792.458; EVM=5.067731e6
xi=2e-6*EVM; n0=2.69e24/CM**3; dn2=(7.29e22/CM**3)**2
Mt=.300939*KG; rT=4.42*1e-3*KG/CM**3; V=Mt/rT; R=(3*V/(4*np.pi))**(1/3); N=n0*V
Mp=.401706*KG; rP=19.972*1e-3*KG/CM**3; Vp=Mp/rP; Rp=(3*Vp/(4*np.pi))**(1/3); npt=19.972/1.66053907e-24/CM**3; Np=npt*Vp
xs=np.geomspace(1e-3,3e7,60001); F=lambda x:np.where(x<60,9*(np.sin(x)-x*np.cos(x))**2/x**6,4.5/x**4)
g=xs**3*F(xs); Gc=np.r_[0,np.cumsum(.5*(g[1:]+g[:-1])*np.diff(xs))]
G=lambda X:np.interp(X,xs,Gc)
rng=np.random.default_rng(3); u=rng.normal(0,238/np.sqrt(2),(400000,3)); u=u[(u*u).sum(1)<544**2]; u[:,2]+=250.5; v=u/c; sp=np.sqrt((v*v).sum(1))
def acc(m,which,Rr=R,Nn=N,Mm=Mt):
    k=m*sp
    if which=='homo': I=G(2*k*Rr)/(4*k**4*Rr**4)
    else:
        Y=4*k*k*xi*xi; I=dn2/n0**2*6*xi**3/Rr**3*(np.log(1+Y)-Y/(1+Y))/(8*k**4*xi**4)
    return Nn**2/Mm/m*np.mean(sp*k*(v[:,2]/sp)*I)
def acc_trunc(m):
    k=m*sp[:40000]; t=np.linspace(-14,np.log(2),800); om=np.exp(t); dw=np.gradient(t)*om; q=np.sqrt(2*om)[None,:]*k[:,None]; x=q*R
    Fh=np.where(x<30,9*(np.sin(x)-x*np.cos(x))**2/np.maximum(x,1e-9)**6,4.5/x**4); I=(dw[None,:]*om[None,:]*Fh).sum(1)/2
    return N**2/Mt/m*np.mean(sp[:40000]*k*(v[:40000,2]/sp[:40000])*I)
print('m  a_h/a_f (DC-36 grid)  a_h/a_f (exact)  |a_h(Ti)-a_h(Pt)|/a_f')
ms=np.array([10,20,50,100,170,200,300,500,700,1000,2000,3000.]); rr=[];dd=[]
for m in ms:
    af=acc(m,'fluc'); ah=acc(m,'homo'); ap=acc(m,'homo',Rp,Np,Mp); rr.append(ah/af); dd.append(abs(ah-ap)/af)
    print('%6g %8.3g %8.3g %8.3g   (a_Pt/a_Ti homo %.2f)'%(m,acc_trunc(m)/af,ah/af,abs(ah-ap)/af,ap/ah))
for nm,y in (('Ti homo = Ti fluc',rr),('|Ti-Pt homo| = Ti fluc',dd)):
    y=np.array(y); j=np.where((y[:-1]>1)&(y[1:]<=1))[0]; print(nm,('crossing at m = %.0f eV'%np.exp(np.interp(0,np.log(y[j[0]:j[0]+2])[::-1],np.log(ms[j[0]:j[0]+2])[::-1]))) if len(j) else 'no crossing up to 3 keV')
