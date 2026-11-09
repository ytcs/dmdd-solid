import numpy as np, dirty as d
L=lambda P:np.imag(1/P)
G0=d.grid
def setg(n,g): d.grid=lambda y,E=3e5,Dl=1.0,**k:G0(y,E,Dl,n=n,g=g)
for y,Q,G in [(2.2,5.64,124.),(2.2,1.,1000.),(2.2,1.,300.),(2.2,1.,3000.),(3.,1.,3000.),(2.2,5.64,3.7)]:
    d.grid=G0; nn=d.Pfull(y,Q,G,Dl=0.)[0]
    for n,g in ((10,1e-7),(10,1e-10),(16,1e-10),(16,1e-13),(24,1e-13)):
        setg(n,g); p,gg,x=d.Pfull(y,Q,G); print(y,Q,G,n,g,'P~ %.8f%+.8fj Lr %.5f'%(gg.real,gg.imag,L(gg)/L(nn)),flush=True)
