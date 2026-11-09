"""Referee: independent integrator of 2401.11971 (S.14). Order of integration swapped relative to DC-54: outer Q (log in Q-omega, no cancellation),
inner T done exactly through cumulative moments A,B,C of the flux with the closed-form threshold E_min(Q,w)=(w+Q sqrt(1+4m^2/s))/2, s=Q^2-w^2."""
import numpy as np
from scipy.interpolate import RegularGridInterpolator as RGI
ALPHA=1/137.035999; E2=4*np.pi*ALPHA; ME=510998.95; Q0=ALPHA*ME
CM=5.067731e4; KG=5.609589e35; SEC=1.519267e15; YR=3.15576e7*SEC
LIT='/home/ytc/paer-work/lit/dc54/'
class ELF:
    def __init__(s,fn,rho):
        a=np.loadtxt(LIT+'darkelf/data/'+fn,skiprows=1); w=np.unique(a[:,0]); k=np.unique(a[:,1])
        a=a[np.lexsort((a[:,1],a[:,0]))]; e=(a[:,2]+1j*a[:,3]).reshape(len(w),len(k))
        s.w,s.k,s.rho=w,k,rho
        s.i1=RGI((w,k),e.real,bounds_error=False,fill_value=1.); s.i2=RGI((w,k),e.imag,bounds_error=False,fill_value=0.)
    def L(s,w,Q):
        p=np.c_[np.full(np.size(Q),w),np.ravel(Q)]; return np.imag(-1/(s.i1(p)+1j*s.i2(p)))
def flux_csv(fn,n=1500):
    a=np.loadtxt(fn,delimiter=','); a=a[np.argsort(a[:,0])]
    T=np.geomspace(a[0,0],a[-1,0],n); y=np.exp(np.interp(np.log(T),np.log(a[:,0]),np.log(a[:,1])))
    return T*1e9,y/(T*1e9)
def moments(T,dP,m):
    E=T+m; p2=E*E-m*m; lt=np.log(T); f=dP*T
    def cum(g):
        h=f*g; c=np.r_[np.cumsum(.5*(h[1:]+h[:-1])*np.diff(lt))[::-1],0.][::1]
        c=np.r_[np.cumsum((.5*(h[1:]+h[:-1])*np.diff(lt))[::-1])[::-1],0.]
        return c
    return E,cum(E*E/p2),cum(E/p2),cum(1/p2)
def rate(elf,m,T,dP,med,ws,Qlo=0.,Qhi=None,sig=1e-34,nQ=1400):
    mu=m*ME/(m+ME); Qhi=Qhi or elf.k[-1]
    pref=sig*CM**2/(elf.rho*1e-3*KG/CM**3*2*np.pi*E2*mu**2)*KG*YR/CM**2/SEC
    Eg,A,B,C=moments(T,dP,m); lE=np.log(Eg)
    src=np.zeros(len(ws)); den=np.zeros(len(ws))
    for i,w in enumerate(ws):
        d0=max(Qlo-w,1e-14*w); d=np.geomspace(d0,Qhi-w,nQ); Q=w+d; s=d*(2*w+d)
        Em=.5*(w+Q*np.sqrt(1+4*m*m/s)); Em=np.maximum(Em,m+w)
        ok=(Em<Eg[-1])&(Em>=0)
        Ee=np.maximum(Em,Eg[0]); le=np.log(Ee)
        a=np.interp(le,lE,A); b=np.interp(le,lE,B); c=np.interp(le,lE,C)
        I=np.where(ok,a-w*b-.25*s*c*0+.25*(w*w-Q*Q)*c,0.)*1.0
        # K=[(2E-w)^2-Q^2]/(4p^2)=E^2/p^2 - w E/p^2 + (w^2-Q^2)/(4p^2)
        F2=(Q0**2/s)**2 if med=='light' else np.ones_like(s)
        g=Q**3*F2*I*elf.L(w,Q); lw=np.gradient(np.log(d))*d
        src[i]=np.sum(g*lw); den[i]=np.sum(g*(s/Q**2)**2*lw)
    return src*pref,den*pref
_a=np.loadtxt(LIT+'aux/2004.10709/tex/Supplementary/p100K.dat')
def Zint(ws,y,Z): return np.trapezoid(np.interp(ws,_a[:,0],_a[:,Z],left=0,right=0)*y,ws)
EX={3:57.71,4:63.03,5:65.56,6:67.73}
def events(ws,y,Zs=(4,5,6)): return sum(Zint(ws,y,z)*EX[z]*1e-3/365.25 for z in Zs)
