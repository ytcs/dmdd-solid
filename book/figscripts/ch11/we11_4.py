"""Worked example 11.4 (Sect. 11.3): the Poisson tail of the silicon nuclear response above 3 omega_D, T = 0.
Prints every number of the worked example.

Inputs: natural Si, M = 28.0855 u = 26.162 GeV; <u_x^2> = 2.45e-3 A^2 (T = 0, DFPT density of states, WE 5.7);
  omega_D = 55.6 meV (WE 5.3, from the measured elastic constants); highest phonon of the PBE density of states 63.67 meV
  (fig5_2_data.npz; the measured zone-centre optical phonon is 64.1 meV, Nilsson and Nelin 1972).
Incoherent response (eq:5.6-multi, self part): e^{-2W} sum_n (2W)^n/n! P_n(omega), P_n the n-fold convolution of
  P_1 ~ g_ph(omega)/omega (0.1 meV grid), n <= 40.  Weight above E = sum_n p^ph_n int_E^inf P_n.
Poisson bound: P_n vanishes above n omega_max, so the weight above E is at most P[Pois(2W) >= ceil(E/omega_max)].
First-moment share of the orders n >= N: P[Pois(2W) >= N - 1] (eq:11.3-fsum), exact with the coherent terms.
Einstein comparison: one mode at <omega^-1>^-1 = 30.4 meV (same 2W at T = 0, WE 5.7): weight above E = P[Pois(2W) >= ceil(E/30.4 meV)].
Free nucleus: delta(omega - E_R), zero above E for E_R < E.  Halo: v_max = 794.5 km/s (Sect. 1.2).
"""
import os
import sys
from math import factorial, ceil
import numpy as np
from scipy.stats import poisson

HERE = os.path.dirname(os.path.abspath(__file__))
HBARC = 1973.269804
M = 28.0855 * 931.494e6
UX2 = 2.45e-3 / HBARC**2
WD = 55.6e-3
E = 3 * WD
VMAX = 794.5 / 299792.458
CM = 0.123984198e-3

d = np.load(os.path.join(HERE, "..", "ch05", "fig5_2_data.npz"))
wd, gd = d["dos"][:, 0] * CM, d["dos"][:, 1]
m = wd > 0
wd, gd = wd[m], gd[m]
dw = 0.1e-3
wg = np.arange(dw / 2, 3.0, dw)
g = np.interp(wg, wd, gd, left=0, right=0)
P1 = g / wg
P1 /= P1.sum() * dw
wmax = wd[gd > 1e-3 * gd.max()].max()
# <omega^-1>^-1 over the DOS (the 30.4 meV of WE 5.7)
gw = g / (g.sum() * dw)
wE = 1 / np.sum(gw * dw / wg)
print("3 omega_D = %.1f meV; omega_max (PBE DOS) = %.2f meV; ceil(3 omega_D/omega_max) = %d; <omega^-1>^-1 = %.1f meV"
      % (E * 1e3, wmax * 1e3, ceil(E / wmax), wE * 1e3))
NMAX = 40
Pn = [None, P1]
tail = [0.0, 0.0]
iE = np.searchsorted(wg, E)
F = np.fft.rfft(P1 * dw, 2 * len(wg))
for n in range(2, NMAX + 1):
    c = np.fft.irfft(F**n, 2 * len(wg))[:len(wg)] / dw
    # midpoint grid: the n-fold sum of midpoints sits (n-1) dw/2 above; shift
    c = np.interp(wg, wg + (n - 1) * dw / 2, c, left=0, right=0)
    c /= c.sum() * dw
    Pn.append(c)
for n in range(2, NMAX + 1):
    tail.append(Pn[n][iE:].sum() * dw)
tail[1] = Pn[1][iE:].sum() * dw
print("fraction of P_n above 3 omega_D: n = 2: %.2e, 3: %.3f, 4: %.3f, 5: %.3f, 6: %.3f" % tuple(tail[2:7]))
for qk in (10, 30, 50, 93.5):
    q = qk * 1e3
    W2 = q**2 * UX2
    ER = q**2 / (2 * M)
    pn = np.array([np.exp(-W2) * W2**n / factorial(n) for n in range(NMAX + 1)])
    w_above = np.sum(pn[1:] * np.array(tail[1:]))
    bound = poisson.sf(ceil(E / wmax) - 1, W2)
    fsum3 = poisson.sf(1, W2)                    # share of the first moment in orders n >= 3
    einst = poisson.sf(ceil(E / wE) - 1, W2)
    mean = np.sum([pn[n] * np.sum(Pn[n] * wg) * dw for n in range(1, NMAX + 1)])
    print("q = %4.1f keV: E_R = %6.2f meV, 2W = %.3f, x_R-type ratio E_R/3omega_D = %.2f" % (qk, ER * 1e3, W2, ER / E))
    print("    weight above 3 omega_D = %.3e; Poisson bound P[n >= %d] = %.3e (ratio %.2f); Einstein (30.4 meV, n >= %d) = %.3e;"
          " first-moment share of n >= 3 = %.3f; mean deposit %.2f meV (E_R %.2f)"
          % (w_above, ceil(E / wmax), bound, w_above / bound, ceil(E / wE), einst, fsum3, mean * 1e3, ER * 1e3))
    print("    contributions by n: " + ", ".join("%d: %.2e" % (n, pn[n] * tail[n]) for n in range(3, 8)))
# kinematics: free recoil of a light particle deposits at most 2 m^2 v^2/M (m << M)
mfree = np.sqrt(M * E / 2) / VMAX
print("free recoil above 3 omega_D needs q >= sqrt(2 M E) = %.1f keV, m_chi >= %.1f MeV" % (np.sqrt(2 * M * E) / 1e3, mfree / 1e6))
for mchi in (10e6, 5e6):
    qmax = 2 * mchi * VMAX
    print("m_chi = %.0f MeV: q_max = 2 m v_max = %.1f keV; v_min at q_max, omega = 3omega_D: %.3e (v_max %.3e)"
          % (mchi / 1e6, qmax / 1e3, E / qmax + qmax / (2 * mchi), VMAX))
