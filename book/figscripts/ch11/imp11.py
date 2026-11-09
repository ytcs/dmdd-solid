"""Shared inputs for Sect. 11.4 (impulse limit and free nuclear recoil) and App. D.32.
Used by fig11_4.py, limit11_4a.py, limit11_4b.py and we11_5.py. Run directly to print the checks and every number of the
section that is not printed by those scripts.

Inputs (all reused, nothing recomputed from first principles):
  Si constants from mph11.py: M = 28.0855 u = 26.162 GeV, hbar c = 1973.27 eV A, <u_x^2> = 2.45e-3 A^2 at T = 0 (WE 5.7).
  Si phonon density of states: PBE/DFPT of Sect. 5.2 (figscripts/ch05/fig5_2_data.npz, column 'dos', cm^-1), on a 0.1-meV
    midpoint grid as in we11_4.py. Per-atom DOS of Si has the shape of the total DOS (two equivalent atoms, cubic sites).
  Halo (v0, v_esc, v_E = 238, 544, 250.5 km/s; v_max = 794.5 km/s) and eta(v_min) from phon11.py (App. D.1).
  Helm form factor (eq:2.2-helm) with the Lewin-Smith parameters of Sect. 2.2: c = 1.23 A^(1/3) - 0.60 fm, a = 0.52 fm,
    s = 0.9 fm, R^2 = c^2 + (7/3) pi^2 a^2 - 5 s^2 (Si: R = 3.47 fm).
  Ge (estimate only, no DFPT DOS in the book, Table 5.1): M = 72.63 u; Theta_D = 373 K from the measured elastic constants
    (Sect. 5.3); <omega> = (3/4) k_B Theta_D times the Si ratio of the DFPT mean to the Debye mean (printed below).
Incoherent self response at T = 0, per nucleus and normalized to unit weight:
  s(q, w) = (1/2pi) int dt e^{i w t} exp(2W [phi(t) - 1]) - e^{-2W} delta(w),   phi(t) = int dw' P1(w') e^{-i w' t},
  P1 = g(w)/w normalized (eq:5.6-gen, eq:5.6-multi), 2W = q^2 <u_x^2> = E_R <w^-1>.  Evaluated by FFT on an adaptive grid,
  phi summed directly over the 0.1-meV DOS grid, so the grid spacing h can exceed the DOS spacing without error in phi.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mph11 as MP  # noqa: E402
import phon11 as P  # noqa: E402

HBARC = MP.HBARC                     # eV A
M = MP.M_SI                          # eV
UX2_A2 = MP.UX2_WE57                 # A^2
CM = 0.123984198e-3                  # eV per cm^-1
VMAX = P.VMAX                        # v_max / c
M_U = 931.494e6
M_GE = 72.63 * M_U
KB = 8.617333e-5                     # eV/K
THETA_GE = 373.0                     # K (Sect. 5.3, Table 5.1)
OMEGA_D_SI = 55.6e-3                 # eV (WE 5.3)
HBARC_FM = 197.3269804e6             # eV fm

_d = np.load(os.path.join(HERE, "..", "ch05", "fig5_2_data.npz"))
_wd, _gd = _d["dos"][:, 0] * CM, _d["dos"][:, 1]
_m = _wd > 0
_wd, _gd = _wd[_m], _gd[_m]
DW = 0.1e-3
WG = np.arange(DW / 2, 0.08, DW)                      # eV, covers the band (ends at 63.7 meV)
G = np.interp(WG, _wd, _gd, left=0, right=0)
G = G / (G.sum() * DW)                                # normalized per-atom, per-direction DOS (cubic site)
P1 = G / WG
P1 = P1 / (P1.sum() * DW)
W_MEAN = np.sum(G * WG) * DW                          # <omega>, arithmetic mean
W_INV = 1 / (np.sum(G / WG) * DW)                     # <omega^-1>^-1
W2_MEAN = np.sum(G * WG**2) * DW                      # <omega^2>
W3_MEAN = np.sum(G * WG**3) * DW
UX2_DOS = 1 / (2 * M * W_INV) * HBARC**2              # A^2, should equal 2.45e-3


def two_w(q, ux2=None):
    """2W = q^2 <u_x^2>, q in eV; by default <u_x^2> from the same DOS (2.446e-3 A^2, 0.16 % below the rounded 2.45e-3 of
    WE 5.7), so that the first moment of the spectrum is exactly E_R."""
    return (q / HBARC)**2 * (UX2_DOS if ux2 is None else ux2)


def e_r(q, mass=M):
    return q**2 / (2 * mass)


def kin_q(T):
    """Kinetic energy along q-hat per nucleus, <p_q^2>/2M = (1/4) <omega coth(omega/2T)> (eV)."""
    if T == 0:
        return W_MEAN / 4
    return np.sum(G * WG / np.tanh(WG / (2 * T))) * DW / 4


def phi(t):
    """Characteristic function of P1 at times t (eV^-1)."""
    t = np.atleast_1d(t)
    out = np.empty(t.shape, complex)
    for c in np.array_split(np.arange(t.size), max(1, t.size // 2000)):
        out[c] = (np.exp(-1j * np.outer(t[c], WG)) * P1).sum(axis=1) * DW
    return out


def spectrum(q, h=None, wtop=None):
    """Incoherent T = 0 spectrum of one nucleus at momentum q (eV), zero-phonon term removed.
    Returns (w grid, s(w) in eV^-1, e^{-2W}). The integral of s is 1 - e^{-2W}."""
    W2 = two_w(q)
    ER = e_r(q)
    sig = np.sqrt(ER * W_MEAN)
    if wtop is None:
        wtop = max(ER + 14 * sig + 0.1, 0.4)
    if h is None:
        h = max(DW, sig / 60)
    n = int(2 ** np.ceil(np.log2(1.6 * wtop / h)))
    t = 2 * np.pi * np.fft.fftfreq(n, d=h)
    ph = phi(t)
    chi = np.exp(W2 * (ph - 1)) - np.exp(-W2)
    # s(w_j) = (1/2pi) sum_k chi(t_k) e^{+i w_j t_k} dt, dt = 2pi/(n h): the inverse FFT divided by h
    s = np.fft.ifft(chi).real / h
    w = np.arange(n) * h
    keep = w <= wtop
    return w[keep], s[keep], np.exp(-W2)


def gauss(w, q, T=0.0):
    ER = e_r(q)
    var = 4 * ER * kin_q(T)
    return np.exp(-(w - ER)**2 / (2 * var)) / np.sqrt(2 * np.pi * var)


def helm(q, A):
    """Helm form factor, q in eV (Sect. 2.2, Lewin-Smith parameters)."""
    c = 1.23 * A**(1 / 3) - 0.60
    a, s = 0.52, 0.9
    R = np.sqrt(c**2 + 7 / 3 * np.pi**2 * a**2 - 5 * s**2)
    x = np.maximum(q * R / HBARC_FM, 1e-8)
    j1 = np.sin(x) / x**2 - np.cos(x) / x
    return 3 * j1 / x * np.exp(-(q * s / HBARC_FM)**2 / 2), R


def onset(xr, mass, wmean):
    """q (eV) at which E_R = xr <omega>."""
    return np.sqrt(2 * mass * xr * wmean)


if __name__ == "__main__":
    print("Si DOS: <w> = %.2f meV, <w^-1>^-1 = %.2f meV, <w><w^-1> = %.3f, <w^2>^(1/2) = %.2f meV, <w^2>/<w>^2 = %.3f, "
          "<w^3>/<w>^3 = %.3f" % (W_MEAN * 1e3, W_INV * 1e3, W_MEAN / W_INV, np.sqrt(W2_MEAN) * 1e3, W2_MEAN / W_MEAN**2,
                                  W3_MEAN / W_MEAN**3))
    print("<u_x^2> from the same DOS = %.4e A^2 (WE 5.7: %.3e)" % (UX2_DOS, UX2_A2))
    for T in (0.0, 77 * KB, 300 * KB):
        K = kin_q(T)
        print("T = %5.1f K: kinetic energy along q-hat K = %.2f meV per nucleus (total 3K = %.2f meV); equivalent classical "
              "temperature 2K = %.1f K" % (T / KB, K * 1e3, 3 * K * 1e3, 2 * K / KB))
    # Debye estimate for Ge, calibrated on Si
    debye_si = 0.75 * OMEGA_D_SI
    ratio = W_MEAN / debye_si
    w_ge = 0.75 * KB * THETA_GE * ratio
    print("Si: Debye mean (3/4) omega_D = %.2f meV; DFPT/Debye = %.4f.  Ge: omega_D = %.2f meV, (3/4) omega_D = %.2f meV, "
          "estimate <w>_Ge = %.1f meV" % (debye_si * 1e3, ratio, KB * THETA_GE * 1e3, 0.75 * KB * THETA_GE * 1e3, w_ge * 1e3))
    for name, mass, wm in (("Si", M, W_MEAN), ("Ge", M_GE, w_ge)):
        for xr in (1, 4, 9):
            q = onset(xr, mass, wm)
            print("%s: x_R = %d at q = %.1f keV, E_R = %.0f meV, endpoint mass q/(2 v_max) = %.1f MeV"
                  % (name, xr, q / 1e3, xr * wm * 1e3, q / (2 * VMAX) / 1e6))
    # Helm radii
    for A in (28.0855, 72.63):
        F, R = helm(1e6, A)
        print("Helm A = %.2f: R_nuc = %.2f fm, first zero at q = %.0f MeV" % (A, R, 4.4934 * HBARC_FM / R / 1e6))
    # regression test against WE 11.4 (we11_4.log): weight above 3 omega_D at 10, 30, 50 keV = 6.07e-7, 6.18e-4, 1.72e-2
    E = 3 * OMEGA_D_SI
    for qk, ref in ((10, 6.071e-7), (30, 6.175e-4), (50, 1.722e-2), (93.5, 4.633e-1)):
        w, s, e0 = spectrum(qk * 1e3, h=DW, wtop=1.2)
        above = s[w >= E].sum() * DW
        print("FFT check q = %5.1f keV: weight above 3 omega_D = %.3e (WE 11.4 script %.3e); total %.6f vs 1 - e^-2W = %.6f; "
              "mean %.2f meV vs E_R %.2f meV" % (qk, above, ref, s.sum() * DW, 1 - e0, (w * s).sum() * DW * 1e3, e_r(qk * 1e3) * 1e3))
