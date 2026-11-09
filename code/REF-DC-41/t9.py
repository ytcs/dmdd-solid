"""Amplitude channel: particle-hole-exact zero, then DOS slope N(xi) = N(0)(1 + a xi), a = Delta/(2 E_F)-type, cutoff |eta| < Lc (omega_D ~ 200 Delta); own bubbles, no closed form.
Also: leftover direct-vs-closed points; GRPA s_eff at Q >> y; sign change in x."""
import numpy as np, core as c, spec as S
from scipy.optimize import brentq
pairs=[(3,1),(1,3),(2,1),(1,2),(1,1),(3,3),(3,2),(2,3),(2,2)]
def bub(z,Q,a,Lc=200.,n=12,ns=8):
    s,ws=c.s_nodes(z.real,Q,ns,z.imag); ws=ws/Q
    acc={k:0 for k in pairs}; a11=a22=0
    for sg in (1,-1):
        for si,wi in zip(s,ws):
            sv=sg*si
            wf=lambda e:(1+a*e)*(np.abs(e)<Lc)
            o=c.bubble_fixed_s(z,sv,pairs,n,1.0,wf)
            for k in pairs: acc[k]+=0.5*wi*o[k]
            b=c.eta_grid(sv,z.real,z.imag,n); eta,w=c.gl_panels(b,n); w=w*wf(eta)
            Pp,Pm,E=c.proj(eta)
            for idx in (1,2):
                A=np.einsum('ab,nbc,cd,nda->n',c.T[idx],Pp,c.T[idx],Pm); B=np.einsum('ab,nbc,cd,nda->n',c.T[idx],Pm,c.T[idx],Pp)
                v=w@(A/(-2*E)-B/(2*E))
                if idx==1: a11+=0.5*wi*v
                else: a22+=0.5*wi*v
    h=lambda k:0.5*acc[k]
    return h,0.5*a11,0.5*a22
aAl=1.8e-4/(2*11.7)
print('a(Al)=Delta/(2E_F)=%.3e'%aAl)
for (y,g,Q) in [(2.2,0.01,5.64),(3,0.01,7.69),(1.9,0.0,5.64)]:
    z=complex(y,g)
    for a in (0.,aAl,1e-2):
        h,a11,a22=bub(z,Q,a)
        D11=a22-h((1,1)); D22=a22-h((2,2))   # gap equation: 2/g = -Pi22(0,0) also in the amplitude channel
        P0=h((3,3))+h((3,2))*h((2,3))/D22
        M=np.array([[D11,-h((1,2))],[-h((2,1)),D22]])
        row=np.array([h((3,1)),h((3,2))]); col=np.array([h((1,3)),h((2,3))])
        P1=h((3,3))+row@np.linalg.solve(M,col)
        print('y',y,'g',g,'Q',Q,'a %.3e |P31| %.3e |P21| %.3e D11 %.4f%+.4fj D22 %.4f%+.4fj | P~(2ch) %.6f%+.6fj | P~(3ch) %.6f%+.6fj | rel diff %.3e'%(a,abs(h((3,1))),abs(h((2,1))),D11.real,D11.imag,D22.real,D22.imag,P0.real,P0.imag,P1.real,P1.imag,abs(P1-P0)/abs(P0)),flush=True)
