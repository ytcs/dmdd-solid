import numpy as np, dirty as d, spec as S
from scipy.integrate import quad
from scipy.special import ellipk, ellipe
def gI(y):
    k=(y-2)/(y+2); return (1+2/y)*ellipe(k*k)-4*ellipk(k*k)/(y+2)
def MB(y):
    g=lambda e:(e*e+1+y*e)
    s1=abs(quad(lambda t:g(t)/np.sqrt(abs((t*t-1)*((t+y)**2-1))),1-y,-1,limit=400)[0])/y
    s2=quad(lambda t:g(t)/np.sqrt(abs((1-t*t)*((t+y)**2-1))),max(1-y,-1),1,limit=400)[0]/y
    return s1,s2
print("MB convergence (sigma1 by magnitude: sqrt(E^2-1) negative for E<-1 in the integrand convention)")
for y in (2.05,2.2,2.5,3.):
    s=MB(y); mb=np.real(1/(s[0]+1j*s[1]))
    o=[]
    for G in (124.,300.,1000.,3000.,10000.):
        p,g,x=d.Pfull(y,1.,G); n=d.Pfull(y,1.,G,Dl=0.)[0]; o.append('%g:%.4f'%(G,np.imag(1/g)/np.imag(1/n)))
    print('y',y,'MB %.4f'%mb,' '.join(o),flush=True)
print("same at the edge Q, Gam=124 vs Q=1: q dependence")
for y in (2.2,2.5):
    for Q in (1.,y/.39):
        p,g,x=d.Pfull(y,Q,124.); n=d.Pfull(y,Q,124.,Dl=0.)[0]; print(y,round(Q,2),round(np.imag(1/g)/np.imag(1/n),4))
print("bare Im = g_I Im nor, own evaluator; Q >= sqrt(y^2-4) vs below")
for y,Q in ((2.2,5.64),(5,12.82),(10,25.64),(5,100.),(30,300.),(5,4.7),(5,3.)):
    r=S.Pup(y,Q)[0].imag/S.Pn(y,Q).imag/gI(y) if y<Q else None
    print(y,Q,'s*=%.3f'%np.sqrt(y*y-4),'ratio-1',None if r is None else '%.2e'%(r-1))
