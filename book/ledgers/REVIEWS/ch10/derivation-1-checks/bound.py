import numpy as np
exec(open('elf.py').read().split("for m in [1e6")[0])
st=d['step_lf']
def bound(m,n,wp,Eg=1.11,unit=False):
    q=np.linspace(1,2*m*(vesc+ve)+10,20000)
    wgrid=np.linspace(Eg,m*(vesc+ve)**2/2+1,4000)
    Qm,Wm=np.meshgrid(q,wgrid)
    val=Wm**(-n)*eta(Wm/Qm+Qm/(2*m)); em=val.max(0)
    s=np.ones_like(q) if unit else np.interp(q,Qg,st)
    I=np.trapezoid(q**3*em*s**((1-n)/2),q)
    return pref(m)*Om/(8*np.pi**2*al**2*me**2)*np.pi/2*wp**(n+1)*I
for m in [1e6,10e6]:
    R=rate(m,'lf')
    print(m/1e6,'MeV rate',R)
    for n,wp,u in [(1,31.1,False),(1,16.6,False),(0,31.1,False),(-1,31.1,False),(-1,31.1,True)]:
        b=bound(m,n,wp,unit=u); print('  n',n,'wp',wp,'unit' if u else '','bound',f"{b:.3g}",'ratio',f"{b/R:.3g}")
def bound2(m,n,wp,qmax,Eg=1.11):
    q=np.linspace(1,qmax,20000); wgrid=np.linspace(Eg,m*(vesc+ve)**2/2+1,4000)
    Qm,Wm=np.meshgrid(q,wgrid); em=(Wm**(-n)*eta(Wm/Qm+Qm/(2*m))).max(0)
    s=np.interp(q,Qg,st); I=np.trapezoid(q**3*em*s**((1-n)/2),q)
    return pref(m)*Om/(8*np.pi**2*al**2*me**2)*np.pi/2*wp**(n+1)*I
R=rate(10e6,'lf')
for qm in [22522,15000]:
    print(qm, bound2(10e6,1,31.1,qm)/R, bound2(10e6,-1,31.1,qm)/R)
