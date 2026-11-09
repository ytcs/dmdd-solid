import sys; sys.dont_write_bytecode=True
import numpy as np, dc36_indep as I, time
def scan(lab,us,**k):
    r=[]
    for u in us:
        a,e=I.harmonic(I.SUEP,float(u),seed=int(u)+11,**k); r.append((u,a[0],a[1],a[1]-a[0],np.hypot(*e)))
    r=np.array(r); D=r[:,3]; z=[r[j,0]+(r[j+1,0]-r[j,0])*(-D[j])/(D[j+1]-D[j]) for j in range(len(D)-1) if D[j]*D[j+1]<0]
    print(lab,'zeros',['%.0f'%x for x in z]); 
    for x in r: print('   u=%5.0f aPt %.3e aTi %.3e Da %+.3e +- %.1e'%tuple(x))
    sys.stdout.flush(); return r
U=[100,200,250,300,350,400,600,1000]
scan('baseline own tracer',U)
for p in (.9,.7,.5,.2,0.): scan('specular fraction p=%.1f'%p,U,p=p)
for b in (30,60): scan('wind tilt %d deg out of the rotation plane'%b,U,beta=np.deg2rad(b))
for R,H in ((45.,50.),(90.,90.)):
    scan('closed can rho=8 R=%g H=%g slab both ways'%(R,H),U,can=dict(R=R,H=H,rho=8.0))
scan('closed can rho=4.5 (Ti inner housing) R=45 H=50',U,can=dict(R=45.,H=50.,rho=4.5))
scan('closed can rho=8 R=45 H=50, p=0.5',U,can=dict(R=45.,H=50.,rho=8.0),p=.5)
