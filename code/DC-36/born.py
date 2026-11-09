"""Reproduction of 2512.16451 Fig. (MICROSCOPE curve) from its Eq. for a_z with |F_fluc|^2 (Born, sphere of equal mass), and size of the |F_homo|^2 term.
Natural units eV. a = (rho/m)(1/M) Int d3v f v Int dOmega q_par (sigma/4pi) N^2 |F(q)|^2 (wind along z, q_par = k(1-cos th) v_hat)."""
import numpy as np, sys
sys.path.insert(0,'../DC-49'); import svgcurves as S
from numpy.polynomial.legendre import leggauss
CM=5.067731e4; M_=1/.1973269804e-6     # 1 m = 5.0677e6 eV^-1
KG=5.609589e35; c=299792.458
xi=2e-6*5.067731e6; n0=2.69e24/CM**3; dn2=(7.29e22/CM**3)**2
Mt=.300939*KG; rhoTi=4.42*1e-3*KG/CM**3; V=Mt/rhoTi; R=(3*V/(4*np.pi))**(1/3); N=n0*V
print('R[cm]=%.3f'%(R/CM))
def sample(n,rho_gev=.4,v0=238.,vesc=544.,W=250.5,seed=1):
    r=np.random.default_rng(seed); u=r.normal(0,v0/np.sqrt(2),(int(n*1.1),3)); u=u[(u*u).sum(1)<vesc**2][:n]; u[:,2]+=W; return u/c
X,Wg=leggauss(600)
def acc(m,which='fluc',sig=1.,rho_gev=.4,n=4000):
    v=sample(n); sp=np.sqrt((v*v).sum(1)); k=m*sp
    # theta integral: x=cos th, Gauss nodes concentrated in log(1-x)
    t=np.linspace(-14,np.log(2),800); om=np.exp(t); dw=np.gradient(t)*om     # om = 1-cos th
    q=np.sqrt(2*om)[None,:]*k[:,None]                                         # q^2 = 2k^2(1-cos)
    if which=='fluc': F=dn2/n0**2*6*xi**3/(R**3*(1+q*q*xi*xi)**2)
    elif which=='homo':
        x=q*R; F=np.where(x<30,9*(np.sin(x)-x*np.cos(x))**2/np.maximum(x,1e-9)**6,4.5/x**4)
    I=(dw[None,:]*om[None,:]*F).sum(1)/2       # Int dOmega/(4 pi) (1-cos) F = (1/2) Int dx ..
    pz=v[:,2]/sp
    a=(rho_gev*1e9/CM**3/m)*(1/Mt)*sig*N**2*np.mean(sp*k*pz*I)     # eV^2 units -> acceleration
    return a*(1/5.067731e6)**-0*1.0
EV2=(1/1.973269804e-7)  # 1 eV (as acceleration, c=hbar=1) in ... handled below
def to_si(a): # a [eV] -> m/s^2 : a c^2 / (hbar c)  with 1 eV^-1 = 1.97327e-7 m
    return a*299792458.**2/(1/ (1.973269804e-7)**-1) if False else a*(299792458.**2)*(1/1.973269804e-7)
F=sys.argv[1]; ps=S.paths(F+'/limit.svg')
q=[p for p in ps if p['color'].startswith('rgb(83.5') and len(p['pts'])>8][0]['pts']
mk=10**(-3+(q[:,0]-57.03)/83.23); sg=10**(-28-(q[:,1]-8.5)/12.86); o=np.argsort(mk); mk,sg=mk[o],sg[o]
np.savetxt('data/pub_limit.csv',np.c_[mk,sg],delimiter=',',header='m[keV],sigma[cm^2] 2512.16451 Fig limit (red)')
print('m[eV] sigma_pub  sigma_Born(fluc,4.8e-14)  ratio  a_homo/a_fluc  V/E(v=1e-3) u[km/s]')
rows=[]
for m in (1,3,10,20,50,100,300,1000,3000):
    af=to_si(acc(m,'fluc',sig=CM**-0*1.)); ah=to_si(acc(m,'homo'))
    # sigma in eV^-2: a(sig)=af*sig -> sig_lim
    sl=4.8e-14/af*CM**-2*1.0     # eV^-2 -> cm^2
    y=np.exp(np.interp(np.log(m/1e3),np.log(mk),np.log(sg)))
    b=np.sqrt(y*CM**2/(4*np.pi)); u=np.sqrt(4*np.pi*b*n0)/m*c
    print('%6g %.3e %.3e %.3f %.3g %.3g %.0f'%(m,y,sl,sl/y,ah/af,2*np.pi*b*n0/m/(.5*m*1e-6),u)); rows.append([m,y,sl,sl/y,ah/af,u])
np.savetxt('data/born_check.csv',rows,delimiter=',',header='m[eV],sigma_pub,sigma_Born,ratio,a_homo/a_fluc,u_at_pub[km/s]')
