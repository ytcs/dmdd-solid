"""Helpers for Sect. 16.5 plots: load the donor model of donor16_5.py (donor16_5.npz) and evaluate the donor part of
the dielectric function, eps^D(omega) = n_D alpha_pol(omega) = 8 pi eps_host n_D a*^3 A(omega), with the measured ground
state 1s(A1) = 45.59 meV.  Line positions of 2p0, 2p+-, 3p0 are the measured ones (Vinh et al., arXiv:0812.0148, Fig. 1)
and 3p+- the effective-mass 3.12 meV (Sect. 7.4); the model's own values differ by less than 0.1 meV (donor16_5.log).
Bound lines get a Lorentzian of full width GAMMA (argument); the box-discretized continuum and the higher Rydberg
states (n >= 5) a Gaussian of standard deviation SIG_CONT (stated in each caption).
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D = np.load(os.path.join(HERE, "donor16_5.npz"))
RYS, AS, EPS = float(D["RYS"]), float(D["AS"]), float(D["EPS"])
HBARC, ALPHA = 1973.2698, 1 / 137.035999
E1S = 45.59
EI = -E1S / RYS
MEAS = {("z", 0): 11.48, ("x", 0): 6.40, ("z", 1): 5.47, ("x", 1): 3.12}   # binding (meV) of the n = 2, 3 lines
WT = {"z": 1 / 3, "x": 2 / 3}


def model(key):
    s = {}
    for ax in ("z", "x"):
        th = D[f"{key}_{ax}_th"].copy()
        w = D[f"{key}_{ax}_w"].copy()
        nb = 0
        for i in range(len(th)):
            if th[i] < 0 and w[i] > 1e-10 and (ax, nb) in MEAS:
                th[i] = -MEAS[(ax, nb)] / RYS
                nb += 1
        s[ax] = (th, w, float(D[f"{key}_{ax}_rem"]))
    return s


def A_of_omega(s, om_meV, gamma_meV, sig_cont_meV, nlines=3):
    """Cubic-average reduced polarizability A(omega) (a*^2/Ry*), complex.  Lines: the lowest nlines bound states of
    each series, Lorentzian with full width gamma; other states: imaginary part Gaussian (sigma sig_cont), real part
    principal value from the discrete states (adequate away from them)."""
    om = np.atleast_1d(om_meV) / RYS
    g = gamma_meV / RYS / 2
    sg = sig_cont_meV / RYS
    tot = np.zeros(len(om), complex)
    for ax in ("z", "x"):
        th, w, rem = s[ax]
        d = th - EI
        isline = np.zeros(len(th), bool)
        idx = np.where((th < 0) & (w > 1e-10))[0][:nlines]
        isline[idx] = True
        dl, wl = d[isline], w[isline]
        res = np.sum(wl[None, :] * (1 / (dl[None, :] - om[:, None] - 1j * g) + 1 / (dl[None, :] + om[:, None])), axis=1)
        dc, wc = d[~isline], w[~isline]
        re_c = np.sum(wc[None, :] * (1 / (dc[None, :] - om[:, None]) + 1 / (dc[None, :] + om[:, None]))
                      * (np.abs(dc[None, :] - om[:, None]) > 2 * sg), axis=1)
        im_c = np.pi * np.sum(wc[None, :] * np.exp(-0.5 * ((om[:, None] - dc[None, :]) / sg) ** 2)
                              / (np.sqrt(2 * np.pi) * sg), axis=1)
        tot += WT[ax] * (res + re_c + 1j * im_c + rem)
    return tot


def epsD(A, nD):
    return 8 * np.pi * EPS * nD * 1e-24 * AS**3 * A


def L_lin(eD):
    return np.imag(eD) / EPS**2


def L_full(eD):
    y = eD / (3 * EPS)
    return np.imag(-1 / (EPS * (1 + 2 * y) / (1 - y)))


def line_strength(s, ax, n):
    """Cubic-average |<f|e.r|i>|^2 (A^2) of the n-th line (n = 0: 2p) of series ax."""
    th, w, _ = s[ax]
    idx = np.where((th < 0) & (w > 1e-10))[0]
    return WT[ax] * w[idx[n]] * AS**2, (th[idx[n]] - EI) * RYS
