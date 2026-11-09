"""Worked example 11.5 (Sect. 11.4): the impulse width at q = 100 keV in silicon. Prints every number of the example.

Inputs: imp11.py (Si PBE DOS of Sect. 5.2, <omega> = 40.9 meV, M = 26.162 GeV); incoherent T = 0 spectrum by FFT of the
generating function (eq:5.6-gen); Gaussian of the impulse approximation with variance 4 E_R K, K = <p_q^2>/2M = <omega>/4 at
T = 0 (eq:11.4-width); cumulants c_k = E_R <omega^{k-1}> (eq:8.5-cumulants).
Ge at the same q: labelled estimate <omega> = 23.6 meV (imp11.py), M = 72.63 u.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import imp11 as I  # noqa: E402

q = 100e3
ER = I.e_r(q)
xr = ER / I.W_MEAN
W2 = I.two_w(q)
K0 = I.kin_q(0.0)
sig = np.sqrt(4 * ER * K0)
g1 = I.W2_MEAN / I.W_MEAN**2 / np.sqrt(xr)
g2 = I.W3_MEAN / I.W_MEAN**3 / xr
print("q = 100 keV: E_R = %.1f meV, x_R = %.2f, 2W = %.2f (e^-2W = %.1e), K = <omega>/4 = %.2f meV" % (ER * 1e3, xr, W2, np.exp(-W2), K0 * 1e3))
print("width sigma = (4 E_R K)^(1/2) = %.1f meV, sigma/E_R = %.3f (x_R^-1/2 = %.3f); FWHM of the Gaussian %.0f meV" % (sig * 1e3, sig / ER, xr**-0.5, 2.3548 * sig * 1e3))
print("skewness = (<w^2>/<w>^2) x_R^-1/2 = %.3f; excess kurtosis = (<w^3>/<w>^3)/x_R = %.3f; Edgeworth mode shift -skew sigma/2 = %.1f meV"
      % (g1, g2, -g1 * sig / 2 * 1e3))
# nuclear speed and recoil speed
vN = np.sqrt(2 * K0 / I.M)
vR = q / I.M
print("rms nuclear speed along q (2K/M)^(1/2) = %.0f m/s; recoil speed q/M = %.2f km/s; sigma/E_R = 2 v_N/v_R = %.4f"
      % (vN * 2.99792458e8, vR * 2.99792458e5, 2 * vN / vR))
w, s, e0 = I.spectrum(q, h=I.DW, wtop=1.5)
dw = w[1] - w[0]
tot = s.sum() * dw
mean = (w * s).sum() * dw / tot
var = ((w - mean)**2 * s).sum() * dw / tot
mode = w[np.argmax(s)]
half = s >= s.max() / 2
fwhm = w[half].max() - w[half].min()
inside = s[(w >= ER - sig) & (w <= ER + sig)].sum() * dw / tot
below = s[w < ER / 2].sum() * dw / tot
gs = I.gauss(w, q)
gin = 0.6827
gbelow = gs[w < ER / 2].sum() * dw
print("exact incoherent spectrum: weight %.4f, mean %.1f meV, rms width %.1f meV, mode %.1f meV, FWHM %.0f meV" % (tot, mean * 1e3, np.sqrt(var) * 1e3, mode * 1e3, fwhm * 1e3))
print("   weight within E_R +- sigma: exact %.3f, Gaussian %.3f; below E_R/2: exact %.3f, Gaussian %.3f; peak height exact/Gaussian %.2f"
      % (inside, gin, below, gbelow, s.max() / gs.max()))
dmax = np.max(np.abs(s / tot - gs)) / gs.max()
print("   max |exact - Gaussian| / Gaussian peak = %.2f" % dmax)
# Gaussian with the third cumulant (Edgeworth)
z = (w - ER) / sig
edge = gs * (1 + g1 / 6 * (z**3 - 3 * z))
print("   with the skewness term: max |exact - Edgeworth| / peak = %.2f" % (np.max(np.abs(s / tot - edge)) / gs.max()))
for T, lab in ((300 * I.KB, "300 K"), (77 * I.KB, "77 K")):
    K = I.kin_q(T)
    print("%s: K = %.2f meV, sigma = %.1f meV (x %.2f of T = 0)" % (lab, K * 1e3, np.sqrt(4 * ER * K) * 1e3, np.sqrt(K / K0)))
# Ge, labelled estimate
wge = 0.75 * I.KB * I.THETA_GE * I.W_MEAN / (0.75 * I.OMEGA_D_SI)
ERg = I.e_r(q, I.M_GE)
print("Ge (estimate <w> = %.1f meV): E_R = %.1f meV, x_R = %.2f, sigma = %.1f meV, sigma/E_R = %.2f"
      % (wge * 1e3, ERg * 1e3, ERg / wge, np.sqrt(ERg * wge) * 1e3, np.sqrt(wge / ERg)))
# halo: a dark-matter particle that reaches q = 100 keV
print("q = 100 keV needs m_chi >= q/(2 v_max) = %.1f MeV" % (q / (2 * I.VMAX) / 1e6))
