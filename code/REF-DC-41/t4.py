"""Sum rules.  (a) proper response: own residue, f-sum, compressibility, on own w-grid. (b) L level: h = 1/P~ is analytic in the UHP (Herglotz), h -> 3y^2/Q^2 + c,
h(0) = -1, so (2/pi) Int Lam/w dw = -1 - c with Lam = Im h >= 0 = K L.  Any sub-gap delta in L must appear to close this."""
import numpy as np, spec as S, core as c
from scipy.optimize import brentq
def wgrid(Q,top):
    e=np.sqrt(Q*Q+4)
    b=[2.0,top,e,Q]
    b+=[2+2.0**-j for j in range(-3,44)]
    b+=[e+sg*2.0**-j for j in range(-2,40) for sg in(-1,1)]
    b+=[Q+sg*2.0**-j for j in range(-2,30) for sg in(-1,1)]
    t=4.0
    while t<top: b.append(t); t*=1.25
    b=np.array(sorted({x for x in b if 2<=x<=top}))
    return c.gl_panels(b,6)
for Q in (0.3,1,3,5.64,6.41,7.69,12.82,25.64,50):
    top=2000*max(Q,2)
    w,wt=wgrid(Q,top)
    G=np.array([S.Pup(a,Q,n=10)[1] for a in w]); 
    # pole
    g=lambda t:S.avg_d(np.exp(t),Q)[2]
    t0=brentq(g,-600,np.log(1.9999),xtol=1e-12); d=np.exp(t0); wa=2-d
    h=d*1e-5
    dUF=(S.avg_d(d-h,Q)[2]-S.avg_d(d+h,Q)[2])/(2*h)   # dUF/dy
    F=S.avg_d(d,Q)[1]
    Z=-wa*wa*F*F/dUF            # P~ ~ Z/(y-wa)
    fs=(wt@(w*(-G.imag))+np.pi*Z*wa)/(np.pi*Q*Q/6)
    cs=(2/np.pi)*(wt@(-G.imag/w))+2*Z/wa
    ab=np.pi*Z*wa/(np.pi*Q*Q/6)
    # L level
    Lam=np.imag(1/G)
    SL=(2/np.pi)*(wt@(Lam/w))
    # tail of Lam above top is negligible only if Lam decays; print tail fraction
    yb=[30*max(Q,3),100*max(Q,3)]
    cc=[(1/S.Pup(y,Q)[1].real-3*y*y/Q/Q) for y in yb]
    # normal
    wn,wtn=c.gl_panels(np.linspace(0,Q,4001)**1,8)
    Ln=np.imag(1/np.array([S.Pn(a,Q) for a in wn])); SN=(2/np.pi)*(wtn@(Ln/wn))
    print('Q=%g w_AB=%.6g Z=%.4g ABshare=%.4f | fsum=%.6f compress=%.6f | L: SumLam=%.5f expected -1-c=%.5f (c(y1),c(y2)=%.4f,%.4f) normal SumLam=%.5f (4/5) | Lam at top %.2e'%(Q,wa,Z,ab,fs,cs,SL,-1-cc[1],cc[0],cc[1],SN,Lam[-1]),flush=True)
