"""Re-implementation of the 1910.02091 model (Geilhufe, Kahlhoefer, Winkler).
All quantities in eV (hbar = c = 1). Equation numbers = arXiv v2 TeX source (DM4DM.tex):
 (2.x) Rate; (3.8)-(3.9) pi(q~^2) with mu~ = 2 e^{-5/6} Lambda~; (3.13) Pi tensor; (3.14) F_med.
Reduction used here (exact, see returns/R18/DC-49.md section 2): with k,k' -> (E,E') the k-integral of the
overlap at fixed (q, omega=E+E') is closed form, so the rate is a 3+1 dimensional integral.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
ALPHA = 1/137.035999; E2 = 4*np.pi*ALPHA; ME = 510998.95
ANG = 1973.2698      # 1 / Angstrom in eV
CM = 5.067731e4      # 1 cm in eV^-1
KG = 5.609589e35     # 1 kg in eV
YR = 3.15576e7*1.519267e15   # 1 yr in eV^-1
KMS = 1/299792.458
Q0 = ALPHA*ME

# Tables 1-2 of 1910.02091, bold ("implemented") rows; rho from the Fig. in section 4 (g/cm^3).
# Exp. row: Lambda column is blank in Table 1; we keep the ISIF7 Lambda_i.
# TWO INPUTS DIFFER FROM THE PRINTED TABLES, fixed by reproducing Summary_absorption.pdf to 0.5% (return section 3):
#  ZrTe5 (exp.): v_F,x = 1.1e-3 (the DFT value), not the printed 1.3e-3;  Yb3PbO: g = 24, not the printed 12.
# rho = "this work" row of the structure table for all three materials (same reason).
MAT = {
 'ZrTe5_th':  dict(v=(1.1e-3,4.4e-4,9.1e-4), D=15.6e-3, Lam=(.23,.216,.1), kap=(308.4,20.75,126.1), g=2,  rho=6.135,
                   koff=dict(xy=(-.97,.5), xz=(-1.2,-1.2), yz=(-.38,-.02))),
 'ZrTe5_exp': dict(v=(1.1e-3,6.5e-4,1.6e-3), D=11.75e-3,Lam=(.23,.216,.1), kap=(308.4,20.75,126.1), g=2,  rho=6.135,
                   koff=dict(xy=(-.97,.5), xz=(-1.2,-1.2), yz=(-.38,-.02))),
 'Yb':        dict(v=(8.9e-4,)*3,            D=19.4e-3, Lam=(.45,.45,.45), kap=(42.8,42.8,42.8),    g=24, rho=11.596,
                   koff=dict(xy=(-12.38,8.58), xz=(8.58,-12.38), yz=(-12.38,8.58))),
 'BNQ':       dict(v=(2e-4,2e-4,1e-4),       D=5.0e-3,  Lam=(.3,.3,.1),    kap=(18.7,5.6,10.3),     g=8,  rho=1.659,
                   koff=dict(xy=(-.05,-.05), xz=(.07,.07), yz=(-1.,-1.))),
}
def setup(name, **over):
    p = dict(MAT[name]); p.update(over)
    p['v'] = np.array(p['v']); p['kap'] = np.array(p['kap'], float); p['Lam'] = np.array(p['Lam'])
    p['vvv'] = np.prod(p['v'])
    p['Lt'] = np.min(p['Lam']*ANG*p['v'])                 # (2.22) Lambda~ = min_i Lambda_i v_F,i
    p['EL'] = np.sqrt(p['Lt']**2+p['D']**2)
    p['rhoT'] = p['rho']*(1e-3*KG)/CM**3   # eV^4
    p['C'] = p['g']*E2/(4*np.pi**2*p['vvv'])              # prefactor of -pi(q~^2)
    # symmetric background tensor (q.kappa.q only sees the symmetric part of Table 2)
    k = np.diag(p['kap']); o = p['koff']
    k[0,1]=k[1,0]=.5*sum(o['xy']); k[0,2]=k[2,0]=.5*sum(o['xz']); k[1,2]=k[2,1]=.5*sum(o['yz'])
    p['ksym'] = k
    return p

_x, _w = leggauss(200)
def Bfun(s, D, Lt, lnc=-5/3):
    """bracket of (3.9): -pi = C * B(s), B = Re + i Im, for s = omega^2 - q~^2 > 0 (array)."""
    s = np.atleast_1d(s).astype(complex).real
    re = np.empty_like(s); im = np.zeros_like(s)
    for i, si in enumerate(s):
        if si > 4*D*D:
            be = np.sqrt(1-4*D*D/si); a, b = (1-be)/2, (1+be)/2
            segs = [(0,a),(a,.5),(.5,b),(b,1)] if a > 0 else [(0,.5),(.5,1)]
        else:
            segs = [(0,.5),(.5,1)]; be = 0
        tot = 0.
        for lo, hi in segs:
            # tanh-sinh-free: map to remove the log endpoint singularity with u^3 stretching
            t = .5*(_x+1); u = t*t*(3-2*t); du = 6*t*(1-t)*.5*_w
            x = lo+(hi-lo)*u; wx = (hi-lo)*du
            tot += np.sum(wx*x*(1-x)*np.log(np.abs(4*np.exp(lnc)*Lt**2/(D*D-x*(1-x)*si+1e-300))))
        re[i] = tot
        if si > 4*D*D: im[i] = (np.pi/6)*(1+2*D*D/si)*be
    return re+1j*im

class Btab:
    """1D table of B(s) on log(s-4D^2) (massive) or log s (massless)."""
    def __init__(self, p, n=500):
        D, Lt = p['D'], p['Lt']; s0 = 4*D*D
        self.s0 = s0
        lo = 1e-10*max(s0, 1e-8); hi = 8*(p['EL']**2)*4
        self.t = np.linspace(np.log(lo), np.log(hi), n)
        v = Bfun(s0+np.exp(self.t), D, Lt, p.get('lnc',-5/3)); self.re = v.real; self.im = v.imag
    def __call__(self, s):
        t = np.log(np.maximum(s-self.s0, 1e-300))
        return np.interp(t, self.t, self.re)+1j*np.interp(t, self.t, self.im)
