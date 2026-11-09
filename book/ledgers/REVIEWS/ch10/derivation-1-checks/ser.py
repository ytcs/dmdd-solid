import sympy as sp, numpy as np
from scipy.optimize import brentq
x=sp.symbols('x',positive=True)
comp=(x+2)*(x**2+2*x+2)/(4*(x+1)**3)
w=-1+sp.sqrt(1+2*x)   # NR recoil photon energy (units m_e)
thom=w/(x*(1+w))
w2=x*(x+2)/(2*(x+1)); thom2=w2/(x*(1+w2))
print('compton',sp.series(comp,x,0,4)); print('thomson NR',sp.series(thom,x,0,4)); print('thomson exact w',sp.series(thom2,x,0,4))
alpT=x**2*(x+2)/(x+1)**3; alpNR=2*x*w/(1+w)
print('alp tree/(2x^2)',sp.series(alpT/(2*x**2),x,0,3))
f=sp.lambdify(x,thom/comp); g=sp.lambdify(x,alpNR/alpT)
me=511.0
print('seagull/exact at 100keV',f(100/me))
print('1% at', brentq(lambda t: f(t)-0.99,0.01,2)*me,' 10% at', brentq(lambda t: f(t)-0.9,0.01,3)*me)
print('alpNR 10% at', brentq(lambda t: g(t)-1.1,0.001,1)*me, ' at 100keV',g(100/me))
print('large x comp ->',sp.limit(comp,x,sp.oo))
