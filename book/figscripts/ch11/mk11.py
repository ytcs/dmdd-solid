"""Markov-Krein band (App. C.10) for Sect. 11.5: shared functions for fig11_5.py, limit11_5c.py and we11_6.py.

Band (eq:C.10-band): for moments mu_0..mu_4 of a normalized distribution and a point xi, the canonical representation through
  xi has nodes xi and the two roots of K(x, xi) = v(x)^T H^{-1} v(xi) (eq:C.10-kernel), weights from the first three moments
  (the quadrature eq:C.10-quadrature is exact to degree 4); lower = sum of weights at nodes < xi, upper = lower + rho(xi),
  rho = 1/K(xi, xi) (eq:C.10-rho).  Computed in the standardized variable z = (x - mu_1)/sigma for conditioning.
Silicon response: the incoherent T = 0 self response of imp11.py (PBE density of states of Sect. 5.2) at momentum q, with the
  zero-phonon weight e^{-2W} at omega = 0 included (it belongs to the cumulative distribution).  Its cumulants are
  c_k = E_R <omega^(k-1)> (eq:D.32-ck at T = 0); moments are checked against the numerical spectrum.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import imp11 as I  # noqa: E402


def moments_from_cumulants(c1, c2, c3, c4):
    """Raw moments mu_0..mu_4 from the first four cumulants."""
    m1 = c1
    m2 = c2 + c1**2
    m3 = c3 + 3 * c2 * c1 + c1**3
    m4 = c4 + 4 * c3 * c1 + 3 * c2**2 + 6 * c2 * c1**2 + c1**4
    return np.array([1.0, m1, m2, m3, m4])


def standardize(mu):
    """Moments of z = (x - mu1)/sigma."""
    m1 = mu[1]
    s = np.sqrt(mu[2] - m1**2)
    from math import comb
    zm = np.zeros(5)
    for k in range(5):
        zm[k] = sum(comb(k, j) * mu[j] * (-m1)**(k - j) for j in range(k + 1)) / s**k
    return zm, m1, s


def canonical(zm, xi):
    """Nodes and weights of the canonical representation through xi (standardized moments zm)."""
    H = np.array([[zm[i + j] for j in range(3)] for i in range(3)])
    kv = np.linalg.solve(H, np.array([1.0, xi, xi**2]))
    K = kv @ np.array([1.0, xi, xi**2])
    rho = 1 / K
    c0, c1, c2 = kv
    if abs(c2) < 1e-14:
        roots = np.array([-c0 / c1])
    else:
        roots = np.roots([c2, c1, c0]).real
    nodes = np.concatenate(([xi], roots))
    V = np.vstack([nodes**0, nodes, nodes**2])
    if len(nodes) == 3:
        w = np.linalg.solve(V, zm[:3])
    else:
        w = np.linalg.lstsq(V, zm[:3], rcond=None)[0]
    return nodes, w, rho


def band(zm, xis):
    lo, hi, rho, nmin = (np.empty(len(xis)) for _ in range(4))
    for i, xi in enumerate(xis):
        nodes, w, r = canonical(zm, xi)
        lo[i] = w[nodes < xi - 1e-12].sum()
        hi[i] = lo[i] + r
        rho[i] = r
        nmin[i] = nodes.min()
    return lo, hi, rho, nmin


def gauss_rho(z):
    return 2 / (3 + z**4)                       # eq:C.10-gauss


def si_response(q, h=None):
    """Silicon T = 0 incoherent response at q (eV): grid, density (normalized with the zero-phonon weight), e^{-2W},
    cumulative F on the grid (zero-phonon step at 0 included), analytic and numerical moments."""
    w, s, e0 = I.spectrum(q, h=h)
    dw = w[1] - w[0]
    F = e0 + np.cumsum(s) * dw - 0.5 * s * dw        # midpoint cumulative
    num = np.array([1.0] + [np.sum(w**k * s) * dw for k in range(1, 5)])
    num[0] = e0 + np.sum(s) * dw
    ER = I.e_r(q)
    c = [ER, ER * I.W_MEAN, ER * I.W2_MEAN, ER * I.W3_MEAN]
    mu = moments_from_cumulants(*c)
    return w, s, e0, F, mu, num
