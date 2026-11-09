import numpy as np
c=299792.458; CM=5.067731e4; n=4.42/1.66053907e-24/CM**3
sig=lambda m,u:(m**4*(u/c)**4/(4*np.pi*n**2))/CM**2
A={k:np.loadtxt(f'dc36_rerun_{k}.csv',delimiter=',') for k in ('SUEP_rep','SUEP_att','SUREF_rep')}
L=4.8e-14
for k,a in A.items():
    u,D=a[:,0],a[:,5]; i=np.argmax(np.abs(D[:9])); print(k,'first |Da| max in u<=500: %.3e at u=%.0f ; saturated a_in %.3e a_out %.3e Da %.3e'%(D[i],u[i],a[-1,1],a[-1,3],D[-1]))
    z=[u[j]+(u[j+1]-u[j])*(-D[j])/(D[j+1]-D[j]) for j in range(len(u)-1) if D[j]*D[j+1]<0]; print('   zeros',np.round(z,1))
    x=[np.exp(np.interp(np.log(L),np.log(np.abs(D[j:j+2])),np.log(u[j:j+2]))) if abs(D[j])<abs(D[j+1]) else np.exp(np.interp(-np.log(L),-np.log(np.abs(D[j:j+2])),np.log(u[j:j+2]))) for j in range(len(u)-1) if (abs(D[j])-L)*(abs(D[j+1])-L)<0]
    print('   |Da|=4.8e-14 at u =',np.round(x,0))
a=A['SUEP_rep']; u,D=a[:,0],a[:,5]
ul=373.
b=np.loadtxt('../DC-36/data/pub_limit.csv',delimiter=',')
print('m sigma_pub u_pub  Da(u_pub) [rho=.3]  x4/3 [rho=.4]  sigma(u=%g)  sigma_pub/sigma(u)'%ul)
for m in (20,50,100,170,300,1000):
    y=np.exp(np.interp(np.log(m/1e3),np.log(b[:,0]),np.log(b[:,1]))); up=(y*CM**2*4*np.pi*n**2/m**4)**.25*c
    d=np.interp(up,u,D); print('%5g %.2e %.0f %+.2e %+.2e %.2e %.3g'%(m,y,up,d,d*4/3,sig(m,ul),y/sig(m,ul)))
