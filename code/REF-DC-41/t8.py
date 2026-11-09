"""Direct points left over; amplitude channel with DOS slope; Delta->0 and neutral controls; full-matrix RPA; plasmon; threshold; s_eff decomposition; edge table reproduction."""
import numpy as np, core as c, spec as S
from scipy.special import ellipk, ellipe
from scipy.optimize import brentq
def gI(y):
    k=(y-2)/(y+2); return (1+2/y)*ellipe(k*k)-4*ellipk(k*k)/(y+2)
R=.39; Lam=lambda P:np.imag(1/P)
print("E. edge table reproduced (own closed-form evaluator)")
sb={2.2:4.01}
print(" y Q v_GRPA s_eff_bare s_eff_GRPA L/gLn bare L/gLn GRPA L/Ln GRPA |eps|/|eps_nor| |P33|/|Pn| ReP~ ")
for y in (2.02,2.05,2.1,2.2,2.5,3,3.5,5,7,10,20):
    Q=y/R; p,g,F,UF=S.Pup(y,Q); n=S.Pn(y,Q)
    print(y,round(Q,3),'%.4f %.3f %.3f %.3f %.3f %.3f %.3f %.3f %.4f'%(g.imag/p.imag-1,Q*(n.real-p.real),Q*(n.real-g.real),Lam(p)/Lam(n)/gI(y),Lam(g)/Lam(n)/gI(y),Lam(g)/Lam(n),abs(g)/abs(n),abs(p)/abs(n),g.real))
print("F. threshold on the edge Q=5.128 (y=2 edge) and Q=5.64, 12.82: L/Lnor as y->2+")
for Q in (5.128,5.64,12.82):
    print(' Q',Q,' '.join('%.0e:%.3g(g%.3g,Im %.3g)'%(dd,Lam(S.Pup(2+dd,Q)[1])/Lam(S.Pn(2+dd,Q)),Lam(S.Pup(2+dd,Q)[0])/Lam(S.Pn(2+dd,Q)),S.Pup(2+dd,Q)[1].imag) for dd in (1e-12,1e-9,1e-6,1e-4,1e-3,1e-2,0.03,0.1)))
print("G. Delta->0 control at fixed x = omega/qv_F: scale y,Q up")
for x in (0.39,0.8,1.5):
    for Q in (1e2,1e3,1e4,1e5):
        y=x*Q; p,g,F,UF=S.Pup(y,Q); n=S.Pn(y,Q); print(' x',x,'Q %g |P~-Lind|=%.2e |P33-Lind|=%.2e  L/Lnor %.5f'%(Q,abs(g-n),abs(p-n),Lam(g)/Lam(n) if x<1 else float('nan')))
print("H. neutral control: pole retained, w_AB/(Q/sqrt3); and charged: eps(y<2) with the '1' at K=(k_TF/q)^2 ; full 2x2 matrix RPA vs R~/(1-vR~)")
kTF=4051.88; vF=6.8e-3; Dl=1.8e-4
for Q in (0.01,0.1,0.5,1,3,5.64):
    g=lambda t:S.avg_d(np.exp(t),Q)[2]; t0=brentq(g,-300,np.log(1.99999),xtol=1e-12); wa=2-np.exp(t0)
    K=(kTF/(Q*Dl/vF))**2
    # scan eps on (0,2): sign changes that are zeros, not poles
    ys=np.r_[np.linspace(1e-3,wa*(1-1e-6),300),wa+(2-wa)*np.geomspace(1e-6,1-1e-9,300)]
    eps=np.array([1-K*S.Pt_d(2-y,Q)[1] for y in ys]); 
    sc=[(ys[i],ys[i+1]) for i in range(len(ys)-1) if eps[i]*eps[i+1]<0]
    # full matrix: channels (n, phase), kernel diag(v, 1/D-type): chi = Pi (1 - W Pi)^-1
    y=wa*0.7
    p,F,UF=S.avg_d(2-y,Q)[0],S.avg_d(2-y,Q)[1],S.avg_d(2-y,Q)[2]
    P32=1j*y/2*F ; P23=-P32 ; Dn=-UF/4 ; P22m=-Dn   # P22 - P22(0,0) = -Dn
    # 2N-normalised: gap-channel kernel g/2 -> at the saddle Pi22 + 2/g = -Dn
    Pi=np.array([[p,P32],[P23,0]],complex)
    # RPA in (n,theta): phi = W delta ; solved exactly
    v=K  # v*2N = K
    A=np.array([[1-v*p,-v*P32*0+ -0j],[0,0]],complex)
    # delta n = p (phi_e + v dn + th) ...: unknowns dn, th (th=effective tau2 potential); dn = p(phi+v dn)+P32 th ; -Dn th = ... from (1+g/2 chi22)th = -(g/2) chi23 (phi+v dn) => Dn*th = P23 (phi + v dn)*(+1)
    M=np.array([[1-v*p,-P32],[-P23*v,Dn]],complex); rhs=np.array([p,P23],complex)
    dn=np.linalg.solve(M,rhs)[0]
    Pt=p+P32*P23/Dn
    print(' Q %g w_AB %.6f ratio to Q/sqrt3 %.5f | y<2 sign changes of eps (pole excluded): %s | matrix chi %.6e vs R~/(1-vR~) %.6e'%(Q,wa,wa/(Q/3**.5),[ (round(a,5),round(b,5)) for a,b in sc if not (a<=wa<=b)],dn.real*1,(Pt/(1-v*Pt)).real))
print("I. Plasmon: root of 1 = K P~(y) at small Q; Al")
for Q in (0.3,5.64,100.):
    K=(kTF/(Q*Dl/vF))**2
    f=lambda y:1-K*S.Pup(y,Q)[1].real
    fn=lambda y:1-K*S.Pn(y,Q).real
    yp=kTF*vF/3**.5/Dl
    a=brentq(f,yp*.9,yp*1.1); b=brentq(fn,yp*.9,yp*1.1)
    print(' Q',Q,'omega_pl(GRPA)=%.4f eV  normal %.4f eV  (k_TF v_F/sqrt3=%.4f)'%(a*Dl,b*Dl,yp*Dl))
print("J. s_eff decomposition: Re P~ - Re Pn = sum over windows (KK)")
def wg(a,b,n=8,m=240):
    if b<=a: return np.zeros(0),np.zeros(0)
    return c.gl_panels(np.linspace(a,b,m),n)
for y in (2.2,3,5,10):
    Q=y/R; p,g,F,UF=S.Pup(y,Q); n=S.Pn(y,Q)
    gfun=lambda t:S.avg_d(np.exp(t),Q)[2]; t0=brentq(gfun,-600,np.log(1.9999),xtol=1e-12); d=np.exp(t0); wa=2-d
    h=d*1e-5; dUF=(S.avg_d(d-h,Q)[2]-S.avg_d(d+h,Q)[2])/(2*h); Fp=S.avg_d(d,Q)[1]; Z=-wa*wa*Fp*Fp/dUF
    pole=2*Z*wa/(y*y-wa*wa)
    # normal weight removed below 2
    w,wt=wg(0,2); rem=(2/np.pi)*(wt@(w*(-0.5*np.pi*w/Q)/(w*w-y*y)))*(-1)*(-1)
    # continuum windows with subtraction for PV about y
    def win(a,b,I,Iy):
        out=0
        e=np.geomspace(1e-9,1,40)
        pts=sorted({a,b,*[p_ for p_ in list(y+(b-a)*e)+list(y-(b-a)*e) if a<p_<b],*(np.geomspace(max(a,1e-3),b,60) if b>a else [])})
        w,wt=c.gl_panels(np.array(pts),6)
        return w,wt
    def ImG(a): return S.Pup(a,Q)[1].imag
    def ImN(a): return S.Pn(a,Q).imag
    top=3000.*Q
    pts=sorted({2.,*(2+np.geomspace(1e-10,1,60)),y,*(y+np.geomspace(1e-9,1,40)),*(y-np.geomspace(1e-9,y-2-1e-9,40)),Q,*(Q+np.geomspace(1e-8,1,30)),*(Q-np.geomspace(1e-8,1,30)),*np.geomspace(2,top,300),(Q*Q+4)**.5})
    w,wt=c.gl_panels(np.array([x for x in pts if 2<=x<=top]),6)
    IG=np.array([ImG(a) for a in w]); IN=np.array([ImN(a) if a<Q else 0. for a in w]); dI=-(IG-IN); dIy=-(g.imag-n.imag)
    # Re dP(y) = (2/pi) Int w dI(w)/(y^2-w^2)... subtraction
    ker=lambda m:(2/np.pi)*(wt[m]@(w[m]*(dI[m]-dIy)/(y*y-w[m]**2)))
    lo=(w<y); mid=(w>=y)&(w<Q); hi=w>=Q
    A0=(2/np.pi)*dIy*(-0.5)*np.log(abs((top**2-y*y)/(4-y*y)))
    below=(2/np.pi)*(wt@(w*0)) 
    wl,wtl=wg(0,2); Bn=(2/np.pi)*(wtl@(wl*(-0.5*np.pi*wl/Q)/(y*y-wl**2)))*(-1)*(-1)
    # normal weight below 2 removed: dI = -I_n = -(pi/2) w/Q
    tot=pole+Bn+ker(lo)+ker(mid)+ker(hi)+A0
    print(' y',y,'Q %.2f: Re dP direct %.4f; KK sum %.4f = pole %.4f + removed-normal-below-2 %.4f + [2,y) %.4f + (y,Q) %.4f + >Q %.4f + subtr %.4f | s_eff=%.3f, s_eff without pole=%.3f'%(Q,g.real-n.real,tot,pole,Bn,ker(lo),ker(mid),ker(hi),A0,Q*(n.real-g.real),Q*(n.real-g.real+pole)),flush=True)
