import numpy as np, dirty as d, spec as S, core as c, time
from scipy.integrate import quad
print("A. normal state, Gam>0: code vs Mermin-Lindhard")
def mermin(y,Q,G):
    z=y+2j*G; x=z/Q; P0=-1+0.5*x*np.log((x+1)/(x-1)); return z*P0/(y-2j*G*P0)
for y,Q,G in [(2.2,5.64,0.1),(3,7.69,1.),(3,7.69,10.),(2.2,5.64,120.),(10,25.64,3.)]:
    p=d.Pfull(y,Q,G,Dl=0.0)[0]; print(y,Q,G,np.round(p,6),np.round(mermin(y,Q,G),6))
print("B. dirty limit vs Mattis-Bardeen: L^BCS/L^nor -> Re(1/sigma~)")
def MB(y):
    D=1.
    g=lambda e:(e*e+1+y*e)
    s1=quad(lambda t:g(t)/np.sqrt(abs((t*t-1)*((t+y)**2-1))),1-y,-1,limit=400)[0]/y if y>2 else 0
    lo=max(1-y,-1)
    s2=quad(lambda t:g(t)/np.sqrt(abs((1-t*t)*((t+y)**2-1))),lo,1,limit=400)[0]/y
    return s1,s2
for y,Q,G in [(3.,1.,100.),(2.2,1.,100.),(5.,2.,300.),(1.5,1.,100.)]:
    s1,s2=MB(y); sig=s1+1j*s2
    p,g,x=d.Pfull(y,Q,G); pn=d.Pfull(y,Q,G,Dl=0.)[0]
    print(y,Q,G,'sig1,sig2 %.4f %.4f'%(s1,s2),'P~/Pnor',np.round(g/pn,4),'sigma~(MB)',np.round(sig,4),' L ratio %.4f MB %.4f'%(np.imag(1/g)/np.imag(1/pn),np.real(1/sig)),' bare P33/Pnor',np.round(p/pn,3))
print("C. conservation with impurities: z P~ = R_jn (Ward), and q->0 Goldstone")
for y,Q,G in [(2.2,5.64,1.),(3.,7.69,5.),(1.5,3.,.5),(2.5,0.05,1.)]:
    p,g,x=d.Pfull(y,Q,G); M=x['M'];J=x['J'];D=x['D']
    Rj=(J[0,3]+J[0,2]*M[2,3]/D)
    print(y,Q,G,'P~',np.round(g,5),'bare',np.round(p,5),'y P~',np.round(y*g,5),'Rjn*?',np.round(Rj,5),' Q^2/(3y^2) %.6f'%(Q*Q/3/y/y))
