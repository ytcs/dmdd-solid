"""Transverse dielectric function: eps_T(Q,w) = eps_data(Q=0,w) + [eps_T^Lind(Q,w) - eps_T^Lind(0,w)]  (CW4 section 18 prescription).
Lindhard-transverse of a degenerate electron gas: Im closed form, Re by Kramers-Kronig of Pi = w^2 (eps_T - 1 + wp^2/w^2)."""
import numpy as np
from scipy.interpolate import RegularGridInterpolator as RGI
ALPHA=1/137.035999; E2=4*np.pi*ALPHA; ME=510998.95
def im_lind(w,Q,kF):
    a=ME*w/Q-Q/2; b=ME*w/Q+Q/2
    f=lambda x:np.where(np.abs(x)<kF,(kF**2-x**2)**2,0.)
    return E2/(16*np.pi*ME*Q*w**2)*(f(a)-f(b))
class EpsT:
    def __init__(s,elf,wp,nQ=70,nw=1200):
        n=wp**2*ME/E2; s.kF=(3*np.pi**2*n)**(1/3); vF=s.kF/ME
        Qg=np.r_[0,np.geomspace(10,elf.k[-1]*1.02,nQ)]; wg=np.linspace(.1,100,500)
        D=np.zeros((len(Qg),len(wg)),complex)
        for i,Q in enumerate(Qg[1:],1):
            wm=(Q*Q/(2*ME)+Q*vF)*1.02
            wp_=(np.arange(nw)+.5)*wm/nw
            PiI=wp_**2*im_lind(wp_,Q,s.kF)        # Im Pi on w'>0
            dw=wm/nw
            # Pi(w) = (2/pi) P Int dw' w' Im Pi(w')/(w'^2-w^2) ; mid-point grid never hits w exactly unless aligned
            ww=wg[:,None]; Re=(2/np.pi)*np.sum(wp_[None,:]*PiI[None,:]/(wp_[None,:]**2-ww**2+1e-30),axis=1)*dw
            # subtract Pi(0): gauge invariance at Q->0 handled by data term; static diamagnetic part cancels at order Q^2 only
            D[i]=(Re+1j*wg**2*im_lind(wg,Q,s.kF))/wg**2
        s.i=RGI((Qg,wg),D.real,bounds_error=False,fill_value=None); s.j=RGI((Qg,wg),D.imag,bounds_error=False,fill_value=0.)
        s.elf=elf
    def __call__(s,w,Q):
        Q=np.asarray(Q,float); pts=np.stack(np.broadcast_arrays(Q,w),-1)
        e0=s.elf.eps(w,0*Q+0.)
        return e0+s.i(pts)+1j*s.j(pts)
