import numpy as np
from scipy.optimize import brentq
from mpmath import mp, erfc, exp, sqrt, pi, quad, mpf
me=510998.95; hbarc=1973.269804; Om=5.431**3/4/hbarc**3
n=8/Om; kF=(3*np.pi**2*n)**(1/3); vF=kF/me; al=1/137.035999177; wp=np.sqrt(4*np.pi*al*n/me)
print('kF',kF,'vF',vF,'wp',wp,'rs',(3/(4*np.pi*n))**(1/3)/(1/(al*me)))
kTF2=3*wp**2/vF**2
def eps1(q,w):
    z=q/(2*kF); u=w/(q*vF)
    a=z-u; b=z+u
    f=0.5+1/(8*z)*((1-a*a)*np.log(abs((a+1)/(a-1)))+(1-b*b)*np.log(abs((b+1)/(b-1))))
    return 1+kTF2/q**2*f
def wpl(q):
    wplus=q*vF+q*q/(2*me)
    return brentq(lambda w: eps1(q,w), wplus*(1+1e-12)+1e-9, 200)
# q_c: where zero meets w+
def g(q):
    wplus=q*vF+q*q/(2*me)
    return eps1(q,wplus*(1+1e-9))
qs=np.linspace(500,3000,2501); vals=[g(q) for q in qs]
i=np.where(np.diff(np.sign(vals)))[0]; print('sign change near q', qs[i])
qc=brentq(g,qs[i[0]],qs[i[0]+1]); print('qc',qc,'w+',qc*vF+qc*qc/2/me)
# quadratic cutoff
fq=lambda q: np.sqrt(wp**2+0.6*q*q*vF*vF)-(q*vF+q*q/2/me); print('quadratic qc',brentq(fq,500,4000), np.sqrt(wp**2+0.6*2240**2*vF**2))
print('wp-fixed',brentq(lambda q: wp-(q*vF+q*q/2/me),100,4000))
vmax=794.5/299792.458
Q=np.linspace(200,qc*0.9999,3000); W=np.array([wpl(q) for q in Q]); d=W-Q*vmax; j=np.argmin(d); print('closest approach exact', Q[j], d[j])
ph=W/Q; j=np.argmin(ph); print('min phase velocity at q/qc',Q[j]/qc, ph[j], (qc*vF+qc*qc/2/me)/qc)
# residue check at 0.1, 0.3 kF
for x in [0.1,0.3]:
    q=x*kF; w0=wpl(q); h=1e-6*w0; de=(eps1(q,w0+h)-eps1(q,w0-h))/(2*h)
    xx=0.6*q*q*vF*vF/w0**2  # small-q form uses omega_pl
    wq=np.sqrt(wp**2+0.6*q*q*vF*vF); xq=0.6*q*q*vF*vF/wq**2
    Zs=(1+xq)/(1+2*xq); exact=np.pi/de; small=np.pi*wq/2*Zs
    print('residue',x, exact/small-1)
for f in [0.5,0.9]:
    q=f*qc; w0=wpl(q); h=1e-7*w0; de=(eps1(q,w0+h)-eps1(q,w0-h))/(2*h)
    print('line f-sum share at',f,'qc:', w0*np.pi/de/(np.pi/2*wp**2))
# Maxwellian tail fraction lab frame, no escape cut
mp.dps=50
v0=mpf(238); vE=mpf(250.5)
def P(V):
    V=mpf(V)
    return (erfc((V-vE)/v0)+erfc((V+vE)/v0))/2 + v0/(2*sqrt(pi)*vE)*(exp(-(V+vE)**2/v0**2)-exp(-(V-vE)**2/v0**2))
print('tail 2750',P(2750),' 2860',P(2860), ' (V-vE)/v0', (2750-250.5)/238,(2860-250.5)/238)
def P2(V):
    V=mpf(V); return (erfc((V-vE)/v0)+erfc((V+vE)/v0))/2 + v0/(2*sqrt(pi)*vE)*(exp(-(V-vE)**2/v0**2)-exp(-(V+vE)**2/v0**2))
print('tail', P2(2750), P2(2860), 'check P2(0)=',P2(0))
for x in [0.1,0.3]:
    q=x*kF; w0=wpl(q); h=1e-6*w0; de=(eps1(q,w0+h)-eps1(q,w0-h))/(2*h); exact=np.pi/de
    wq=np.sqrt(wp**2+0.6*q*q*vF*vF)
    for lab,ww,xx in [('quad w, x(quad)',wq,0.6*q*q*vF*vF/wq**2),('exact w, x(exact)',w0,0.6*q*q*vF*vF/w0**2),('exact w, Z=1-3/5 q2vF2/wp2',w0,None)]:
        Z=(1+xx)/(1+2*xx) if xx is not None else 1-0.6*q*q*vF*vF/wp**2
        print(x,lab, np.pi*ww/2*Z/exact-1)
for x in [0.1,0.3]:
    q=x*kF; w0=wpl(q)
    for h in [1e-4,1e-6,1e-8]:
        hh=h*w0; de=(eps1(q,w0+hh)-eps1(q,w0-hh))/(2*hh); print(x,h,'w0',w0,'exact',np.pi/de)
    wq=np.sqrt(wp**2+0.6*q*q*vF*vF); xq=0.6*q*q*vF*vF/wq**2; print('formula quad', np.pi*wq/2*(1+xq)/(1+2*xq), 'w quad', wq)
