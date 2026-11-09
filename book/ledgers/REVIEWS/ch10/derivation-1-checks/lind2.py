import numpy as np
exec(open('elf.py').read().split("for m in [1e6")[0])
hb=1973.269804; n=8/Om; kF=(3*np.pi**2*n)**(1/3); vF=kF/me; wp=np.sqrt(4*np.pi*al*n/me); kTF2=3*wp**2/vF**2
def epsL(q,w):
    z=q/(2*kF); u=w/(q*vF); a=z-u; b=z+u
    with np.errstate(all='ignore'):
        f1=0.5+1/(8*z)*((1-a*a)*np.log(np.abs((a+1)/(a-1)))+(1-b*b)*np.log(np.abs((b+1)/(b-1))))
    f2=np.where(b<1,np.pi/2*u,np.where(np.abs(a)<1,np.pi/(8*z)*(1-a*a),0.))
    return 1+kTF2/q**2*(f1+1j*f2)
Q=np.linspace(Qg[0],Qg[-1],3000); Wg=np.linspace(1.11,89,1500)
QQ,WW=np.meshgrid(Q,Wg)
e=epsL(QQ,WW); L=(e.imag/np.abs(e)**2)
for m in [1e6,10e6,100e6]:
  for lt in [False,True]:
    vm=WW/QQ+QQ/(2*m); et=eta(vm); F2=(q0/QQ)**4 if lt else 1
    I=np.trapezoid(np.trapezoid(QQ**3*et*F2*L,Q,axis=1),Wg)
    R=pref(m)*Om/(8*np.pi**2*al**2*me**2)*I; print(m/1e6,lt,'Lindhard',R, 'ratio', R/rate(m,'lf',lt))
