"""Worked example 18.2 (we:18-parking): the random-parking (Renyi) limit, exact values and the moment-recursion check.
Log: limit18_2b.log.  Run: python limit18_2b.py > limit18_2b.log.  Solver: mom18_2.py.  (The Limit Check box and its figure
limit18_2b.pdf, the parking kernel with phonons, were removed; this script now writes no figure.)

Random parking of unit cars on a line (Renyi 1958) is the cascade of Sect. 18.1 with a constant electron density of states,
a delta-function hole density of states (narrow valence band), theta_ii = 1 and no phonons (Subashiev and Luryi,
arXiv:0911.1532, Sect. I).  Exact values, evaluated here with mpmath (30 digits):
  rho_inf = int_0^inf exp(-2 beta(t)) dt,  beta(t) = int_0^t (1 - e^-u)/u du  (0911.1532 Eqs. (17), (23));
  F_exact = 2 rho_inf - 1 - (2/rho_inf) int_0^inf (rho_inf - rho(t))^2 e^{2 beta(t)} A(t) dt, rho(t) = int_0^t e^{-2beta},
            A(t) = e^{-t} (e^{-t} + t - 1)/t^2  (0911.1532 Eqs. (44)-(45)).
Cascade solver: lam_ph = 0 by the moment recursions on h = 0.01 and 0.005 with linear Richardson extrapolation (the scheme is O(h)
without phonons).
"""
import os
import sys
import time
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mom18_2 import Cascade, run

t0 = time.time()
mp.mp.dps = 30

beta = lambda t: mp.euler + mp.log(t) + mp.e1(t) if t > 0 else mp.mpf(0)   # Ein(t)
rho_inf = mp.quad(lambda t: mp.exp(-2 * beta(t)), [0, 1, 10, mp.inf])
print("rho_inf = %s" % mp.nstr(rho_inf, 12))
print("eps/E_g = 1/rho_inf = %s" % mp.nstr(1 / rho_inf, 10))



rho_t = lambda t: mp.quad(lambda u: mp.exp(-2 * beta(u)), [0, t])


def Afun(t):
    if t < mp.mpf("1e-6"):
        return mp.mpf(1) / 2
    return mp.exp(-t) * (mp.exp(-t) + t - 1) / t**2


def integrand(t):
    rt = rho_inf - rho_t(t)
    return rt**2 * mp.exp(2 * beta(t)) * Afun(t)


I44 = mp.quad(integrand, [0, 1, 5, 20, 60])
tail = mp.quad(integrand, [60, 200])
Fexact = 2 * rho_inf - 1 - 2 / rho_inf * (I44 + tail)
print("F_exact (Eq. (44)) = %s  (0911.1532 Eq. (44); tail beyond t = 60 contributes %s)" %
      (mp.nstr(Fexact, 10), mp.nstr(2 / rho_inf * tail, 3)))
rho_inf_f, Fexact_f = float(rho_inf), float(Fexact)

# cascade solver, lam_ph = 0 (RPP kernel), Richardson in h
def rpp(h, lam=0.0, w=None, X=30.0):
    c = Cascade(lam, w if w else 0.05, X=X, h=h, a=(0.0, 0.0), hole_delta=True, theta=1.0, phonon=(lam > 0))
    return c.slopes()


r1, r2 = rpp(0.01), rpp(0.005)
rich = {k: 2 * r2[k] - r1[k] for k in ("eps", "F")}
print("\nsolver, lam_ph = 0: h = 0.01: 1/eps = %.6f, F = %.6f;  h = 0.005: %.6f, %.6f" %
      (1 / r1["eps"], r1["F"], 1 / r2["eps"], r2["F"]))
print("   Richardson: 1/eps = %.6f (exact %.6f), F = %.6f (exact %.6f)" %
      (1 / rich["eps"], rho_inf_f, rich["F"], Fexact_f))
print("%.0f s" % (time.time() - t0))
