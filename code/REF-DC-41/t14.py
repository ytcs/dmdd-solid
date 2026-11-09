"""Mattis-Bardeen test with the absolute floor of P~ (~1e-5, see t13) kept well below |P~|: raise Q with Gam so that P~ ~ Q^2/(6 Gam y) ~ 2e-3, and let D q^2 = Q^2/(6 Gam) -> 0."""
import numpy as np, dirty as d
L=lambda P:np.imag(1/P)
print('MB: y=2.2 .2352, y=2.5 .7440, y=3 1.3024')
for y in (2.2,2.5,3.):
    for G,Q in ((124.,5.64),(124.,3.),(1000.,10.),(1000.,5.),(3000.,10.),(10000.,20.)):
        nn=d.Pfull(y,Q,G,Dl=0.)[0]; p,gg,x=d.Pfull(y,Q,G)
        print(y,'Gam',G,'Q',Q,'Dq2 %.4f |P~| %.2e Lr %.4f'%(Q*Q/6/G,abs(gg),L(gg)/L(nn)),flush=True)
