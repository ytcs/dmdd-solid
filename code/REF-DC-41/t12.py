import numpy as np, dirty as d, sys
L=lambda P:np.imag(1/P)
for y,Q,G in [(2.2,5.64,124.),(2.2,1.,1000.),(2.2,1.,300.),(2.5,6.41,124.),(2.2,5.64,12.4)]:
    n=d.Pfull(y,Q,G,Dl=0.)[0]
    for E in (3e4,3e5,3e6,3e7):
        p,g,x=d.Pfull(y,Q,G,E=E); print(y,Q,G,'E %.0e P33 %.6f%+.6fj D %.6e%+.6ej P~ %.7f%+.7fj Lr %.5f'%(E,p.real,p.imag,x['D'].real,x['D'].imag,g.real,g.imag,L(g)/L(n)),flush=True)
