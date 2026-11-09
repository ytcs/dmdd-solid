"""CW7 / LE-153: generating-function solver for the continuous P_casc(N | Lambda) of the energy-only cascade.

Hypotheses: GAP-EF (H-EF1)-(H-EF7) with identical electron and hole DOS (symmetric case: t = t-bar, one G), units E_g = 1.
The general case (rho_e != rho_h) needs two coupled tables G_e, G_h with the same recursion; it is specified, not coded here.
ERR-CW7: solve_gf fixed for theta_ii > 1 (sum_N P = 1 to 1e-15 at theta_ii = 3/2; checks.py CW7-C5b).
A carrier with kinetic energy x >= theta_ii:
  ii (probability p(x)):  x -> x1 + x2 + x3 (two of its own type, one of the other), x1+x2+x3 = x - 1, density rho rho rho / Phi(x - 1)
  ph (probability 1-p):   x -> x - w (one optical phonon w = omega_0/E_g),  p = 1/(1 + lam rho(x - w)/Phi(x - 1))   (GAP-EF (EF2))
Below threshold the carrier is terminal.  N = number of ii events in the subtree.
Generating function  G(x; z) = E[z^N | x]  obeys the first-step equation
  G(x; z) = p(x) z <G(x1) G(x2) G(x3)> + (1 - p(x)) G(x - w; z),  G = 1 for x < theta_ii,                       (CW7-153a)
whose z-derivatives at z = 1 are GAP-EF (EF3)-(EF4).  P(N = n | x) is recovered exactly by a discrete Fourier transform on |z| = 1.
ERR-WP8 (VER-ERR-CW7 §C2, RC3): COMMENSURATE GRID.  The solver reads G, rho and p at x - E_g, x - omega_0 and x >= theta_ii E_g on the grid,
so h must divide E_g (= 1), theta_ii and omega_0.  Otherwise it silently solves the problem with omega_0,eff = h round(omega_0/h)
(0.054 -> 0.06 at h = 0.02, 0.05 at h = 0.01): the h-sequence is then non-monotone and h-Richardson is invalid (mean N at x = 8,
lam 3.55, theta_ii 3/2 biased by -1.7% at h = 0.02).  CascadeGF and moments_fast now raise ValueError on a non-commensurate grid
(strict=True, the default); strict=False runs on the quantised grid and records omega_0,eff in .w_eff.  commensurate_h(w, theta, hmax)
returns the largest h = 1/N <= hmax that divides 1, theta and w (omega_0 = 0.054 -> h = 0.002, 0.001, ...).
"""
import math
import warnings
from fractions import Fraction

import numpy as np


def _divides(h, v, tol=1e-9):
    r = v / h
    return abs(r - round(r)) <= tol * max(1.0, abs(r))


def check_grid(h, w, theta, strict=True):
    """h must divide E_g = 1, theta_ii and omega_0 (all in units of E_g). Returns omega_0,eff = h round(w/h)."""
    bad = [n for n, v in (("E_g", 1.0), ("theta_ii", theta), ("omega_0", w)) if not _divides(h, v)]
    w_eff = max(1, int(round(w / h))) * h
    if bad:
        msg = "grid h = %g does not divide %s: the solver would use omega_0,eff = %g (theta_ii,eff = %g); h-Richardson invalid" % (
            h, ", ".join(bad), w_eff, max(1.0, round(theta / h) * h))
        if strict:
            raise ValueError(msg + " (use commensurate_h)")
        warnings.warn(msg)
    return w_eff


def commensurate_h(w, theta=1.0, hmax=0.02, maxden=10 ** 6):
    """largest h = 1/N <= hmax with N w, N theta integers (E_g = 1)."""
    L = 1
    for v in (w, theta):
        L = L * Fraction(v).limit_denominator(maxden).denominator // math.gcd(L, Fraction(v).limit_denominator(maxden).denominator)
    N = L * math.ceil((1.0 / hmax) / L - 1e-12)
    return 1.0 / N


class CascadeGF:
    def __init__(self, X=10.0, h=0.02, a=0.5, lam=0.0, w=0.054, theta=1.0, zs=None, strict=True):
        self.w_eff = check_grid(h, w, theta, strict)
        self.h = h
        K = int(round(X / h)) + 1
        self.K = K
        x = np.arange(K) * h
        self.x = x
        self.nG = int(round(1.0 / h))
        self.nw = max(1, int(round(w / h)))
        self.nth = max(self.nG, int(round(theta / h)))
        self.rho = x ** a if a > 0 else np.ones(K)
        c = lambda f, g: np.convolve(f, g)[:K] * h
        self.Phi = c(c(self.rho, self.rho), self.rho)
        self.p = np.zeros(K)
        for n in range(self.nth, K):
            q = n - self.nG
            if self.Phi[q] > 0:
                self.p[n] = 1.0 / (1.0 + lam * self.rho[n - self.nw] / self.Phi[q])
        self.zs = np.ones(1, complex) if zs is None else np.asarray(zs, complex)

    def solve_gf(self):
        """G[n, k] = G(x_n; z_k). Incremental triple convolution, O(K^2 N_z)."""
        K, h, nG, nw, rho = self.K, self.h, self.nG, self.nw, self.rho
        Nz = len(self.zs)
        G = np.ones((K, Nz), complex)
        f = rho[:, None] * G                     # rho * G, final once G(x_n) is known
        C2 = np.zeros((K, Nz), complex)
        C3 = np.zeros((K, Nz), complex)
        # ERR-CW7 fix (VER-CW7 §B2): for theta_ii > 1 the loop below starts at q = nth - nG > 0, so the convolutions at
        # q < nth - nG were never formed (left 0) although G = 1 there; ii products with x_i < (theta_ii - 1) E_g were dropped
        # and sum_N P < 1 (0.953 at theta_ii = 3/2).  Every f[j] with j < nth is final (G = 1), so precompute them here.
        for q in range(0, self.nth - nG):
            C2[q] = h * np.sum(f[:q + 1] * f[q::-1], axis=0)
            C3[q] = h * np.sum(C2[:q + 1] * f[q::-1], axis=0)
        for n in range(self.nth, K):
            q = n - nG                            # q < n: every f[0..q] is final
            C2[q] = h * np.sum(f[:q + 1] * f[q::-1], axis=0)
            C3[q] = h * np.sum(C2[:q + 1] * f[q::-1], axis=0)
            avg = C3[q] / self.Phi[q] if self.Phi[q] > 0 else 1.0
            G[n] = self.p[n] * self.zs * avg + (1 - self.p[n]) * G[n - nw]
            f[n] = rho[n] * G[n]
        self.G = G
        return G


def moments_fast(X=40.0, h=0.02, a=0.5, lam=0.0, w=0.054, theta=1.0, strict=True):
    """O(K^2) moment recursion with incremental two-fold convolutions (for asymptotic slopes). Same grid rule as CascadeGF."""
    if lam > 0:          # at lam = 0 the phonon branch has probability 0 and omega_0 never enters (CW7-C6)
        check_grid(h, w, theta, strict)
    else:
        check_grid(h, 1.0, theta, strict)
    K = int(round(X / h)) + 1
    x = np.arange(K) * h
    nG = int(round(1.0 / h)); nw = max(1, int(round(w / h))); nth = max(nG, int(round(theta / h)))
    rho = x ** a if a > 0 else np.ones(K)
    rr = np.convolve(rho, rho)[:K] * h
    Phi = np.convolve(rr, rho)[:K] * h
    m = np.zeros(K); s = np.zeros(K)
    fm = np.zeros(K); fs = np.zeros(K)                 # rho m, rho s
    D_mr = np.zeros(K); D_mm = np.zeros(K); D_sr = np.zeros(K)   # (rho m)*rho, (rho m)*(rho m), (rho s)*rho
    rr = np.ascontiguousarray(rho[::-1])                 # rho[q::-1] == rr[K-1-q:] (contiguous: BLAS dot, ERR-WP8 speed-up, same arithmetic)
    for n in range(nth, K):
        q = n - nG
        rq = rr[K - 1 - q:]
        D_mr[q] = h * np.dot(fm[:q + 1], rq)
        D_mm[q] = h * np.dot(fm[:q + 1], fm[q::-1])
        D_sr[q] = h * np.dot(fs[:q + 1], rq)
        if Phi[q] <= 0:                                  # x = E_g exactly: no ii phase space (as in CascadeGF)
            m[n] = m[n - nw]; s[n] = s[n - nw]; fm[n] = rho[n] * m[n]; fs[n] = rho[n] * s[n]
            continue
        em = h * np.dot(D_mr[:q + 1], rq) / Phi[q]
        emm = h * np.dot(D_mm[:q + 1], rq) / Phi[q]
        es = h * np.dot(D_sr[:q + 1], rq) / Phi[q]
        p = 1.0 / (1.0 + lam * rho[n - nw] / Phi[q])
        m[n] = p * (1 + 3 * em) + (1 - p) * m[n - nw]
        s[n] = p * (1 + 6 * em + 3 * es + 6 * emm) + (1 - p) * s[n - nw]
        fm[n] = rho[n] * m[n]; fs[n] = rho[n] * s[n]
    return x, m, s


def pmf_from_gf(G_row, zs):
    """P(N = n) from G on the N_z roots of unity.  The DFT returns sum_k P(n + k N_z) (aliasing): it equals P(n) exactly
    if P(N) = 0 for N >= N_z; otherwise choose N_z >= N_bar + 8 sigma_N (ERR-CW7, VER-CW7 §B2)."""
    Nz = len(zs)
    return np.real(np.fft.fft(G_row) / Nz)   # G(z_k) = sum_n P_n z_k^n, z_k = exp(2 pi i k / Nz) -> P_n = (1/Nz) sum_k G_k z_k^{-n}
