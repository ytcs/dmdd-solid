"""sigma(u) map and [C] comparison with the published Born curve. u = v_c,Ti ; sigma = m^4 u^4/(4 pi n^2) (mu=m)."""
import numpy as np
c=299792.458; CM=5.067731e4; n=4.42/1.66053907e-24/CM**3
sig=lambda m,u:(m**4*(u/c)**4/(4*np.pi*n**2))/CM**2
a=np.loadtxt('results/force_SUEP_rep.csv',delimiter=',')
u,D=a[:,0],a[:,5]
L=4.8e-14
# first crossing of |Da|=L on log-log interpolation
i=np.where(np.abs(D)>L)[0][0]; ul=np.exp(np.interp(np.log(L),np.log(np.abs(D[i-1:i+1])),np.log(u[i-1:i+1]))); print('u_lim',ul)
# zero crossing
j=np.where(np.sign(D[:-1])!=np.sign(D[1:]))[0][0]; uz=u[j]+(u[j+1]-u[j])*(-D[j])/(D[j+1]-D[j]); print('zero at u=',uz)
b=np.loadtxt('data/pub_limit.csv',delimiter=','); 
for m in (10,20,50,100,300,1000,3000):
    y=np.exp(np.interp(np.log(m/1e3),np.log(b[:,0]),np.log(b[:,1])))
    print('m %g sigma_pub %.2e sigma(u_lim) %.2e ratio %.3g ; sigma_crit(v=1e-3) %.2e sigma(sat u=800) %.2e'%(m,y,sig(m,ul),y/sig(m,ul),sig(m,c*1e-3),sig(m,800)))
# slope at small u
print('slopes',np.diff(np.log(a[:4,3]))/np.diff(np.log(u[:4])),np.diff(np.log(a[:4,1]))/np.diff(np.log(u[:4])))
