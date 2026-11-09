"""Clean-limit sensitivity. (a) Born impurities, conserving (GRPA + impurity ladder); (b) AB pole vs Gam; (c) gap anisotropy (separable, phi independent of mu)."""
import numpy as np, dirty as d, spec as S, csv
from scipy.optimize import brentq
from scipy.special import ellipk, ellipe
def gI(y):
    k=(y-2)/(y+2); return (1+2/y)*ellipe(k*k)-4*ellipk(k*k)/(y+2)
R=0.39; Lam=lambda P:np.imag(1/P)
hbarv=197.3269804*6.8e-3; Dl=1.8e-4
ell=lambda G: hbarv/(2*G*Dl)   # nm
Gs=[1e-3,0.01,0.037,0.1,0.37,1,3.7,12.4,37,124]
ys=[2.05,2.2,2.5,3,5,10]
rows=[]
print("L^BCS/(g_I L^nor(Gam)) on the edge Q = y/0.39, conserving; [L^BCS/L^nor(Gam) in brackets]; l in nm")
print('Gam   l_nm  '+'  '.join('y=%-12g'%y for y in ys))
for G in Gs:
    o=[]
    for y in ys:
        Q=y/R; p,g,x=d.Pfull(y,Q,G); n=d.Pfull(y,Q,G,Dl=0.)[0]
        r=Lam(g)/Lam(n); o.append('%.3f[%.3f]'%(r/gI(y),r))
        rows.append(dict(Gam=G,l_nm=ell(G),y=y,Q=Q,ReP=g.real,ImP=g.imag,ReN=n.real,ImN=n.imag,L_over_Lnor=r,L_over_gLnor=r/gI(y),L_over_Lnor_clean=Lam(g)/Lam(S.Pn(y,Q)),qell=Q/(2*G)))
    print('%-6g %-7.3g '%(G,ell(G))+'  '.join('%-14s'%a for a in o),flush=True)
w=csv.DictWriter(open('data/dirty_edge.csv','w',newline=''),fieldnames=list(rows[0])); w.writeheader(); [w.writerow(r) for r in rows]
print("\nAB pole of R~ vs Gam: zero of D(y) on y<2.  d = 2 - w_AB; share = pi Z w/(pi Q^2/6)")
ab=[]
for Q in (3.,5.64,6.41,7.69,12.82):
    for G in (1e-3,0.01,0.037,0.1,0.37,1.,3.7,12.4,124.):
        Dn=lambda y:d.Pfull(y,Q,G)[2]['D'].real
        yy=np.r_[np.linspace(0.05,1.9,20),2-np.geomspace(0.09,2e-4,24)]
        v=[Dn(y) for y in yy]; idx=[i for i in range(len(yy)-1) if v[i]*v[i+1]<0]
        if idx:
            i=idx[-1]; wa=brentq(Dn,yy[i],yy[i+1],xtol=1e-7)
            h=1e-4*min(2-wa,0.5); dD=(Dn(wa+h)-Dn(wa-h))/(2*h); x=d.Pfull(wa,Q,G)[2]
            # P~ = P33 + M32 M23 / D ; D ~ dD (y-wa)  => Z = M32 M23 / dD
            Z=(x['M'][3,2]*x['M'][2,3]).real/dD; sh=Z*wa/(Q*Q/6)
            print('Q=%g Gam=%g l=%.3g nm: w_AB=%.5f d=%.3g Z=%.4g share=%.4f'%(Q,G,ell(G),wa,2-wa,Z,sh),flush=True); ab.append((Q,G,wa,Z,sh))
        else: print('Q=%g Gam=%g: no zero of D below y=%.4f; D(top)=%.3g'%(Q,G,yy[-1],v[-1]),flush=True)
np.savetxt('data/ab_vs_gam.csv',np.array(ab),header='Q Gam w_AB Z share',comments='')
print("\nGap anisotropy, clean: phi Gaussian (sigma), Gauss-Hermite; separable ladder; goldstone kept")
xs,ws=np.polynomial.hermite_e.hermegauss(24); ws=ws/ws.sum()
def Pani(y,Q,sig):
    a=b=cc=0
    for x,w in zip(xs,ws):
        ph=1+sig*x
        if ph<=0.2: continue
        yp,Qp=y/ph,Q/ph
        if yp>2: p,F,UF=S.avg_up(yp,Qp)
        else: p,F,UF=S.avg_d(2-yp,Qp) if yp<2 else S.avg_up(2+1e-12,Qp)
        a=a+w*p; b=b+w*F; cc=cc+w*ph*ph*UF
    return a,a-y*y*b*b/cc
print('sigma  '+'  '.join('y=%-7g'%y for y in ys))
for sig in (0,0.02,0.05,0.1):
    o=[]
    for y in ys:
        Q=y/R
        if sig==0: g=S.Pup(y,Q)[1]
        else: g=Pani(y,Q,sig)[1]
        o.append('%.3f'%(Lam(g)/Lam(S.Pn(y,Q))/gI(y)))
    print('%-5g '%sig+'  '.join('%-9s'%a for a in o),flush=True)
