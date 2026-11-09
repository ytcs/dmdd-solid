"""Film response for the mean-field kernels of Sect. 20.5 (imported by kern20_5.py; checks printed in kern20_5.log).

For a superconducting film with gap Delta_s and escape ratio r = t_l/t0 (Sects. 20.3-20.4) it returns, per phonon of
energy W (in units of Delta_s) that enters the film:
  p_first(W)  probability that it breaks a pair before it escapes, eq:20.4-ppb (exact, any W);
  Y(W)        quasiparticle yield of a phonon that has broken its first pair: the Kaplan cascade of qp20_4.Cascade
              (0.01 Delta grid, the validated numbers of Sect. 20.4), here run up to EMAX = 120 Delta and held at its
              EMAX value above (MODELLING CHOICE; a2F = b W^2 is used beyond the few meV where it holds for Al, as in
              Sect. 20.4; for aluminum 2.4 % of the primary energy is absorbed above 60 Delta and 0.08 % above 120 Delta,
              kern20_5.log);
  S(W)        energy spectrum of the phonons that leave the film (escaped above-gap phonons and the sub-gap phonons of
              quasiparticle relaxation) per first-broken phonon of energy W, on output bins of width BW (Delta units).
S comes from the vector form of the cascade recursion (same kernels as eq:20.4-cascade):
  quasiparticle at E emits W' = E - x with density rho(x) w(E, x) / Z(E) on [1, E]:
      R_q(E) = int rho(x) w(E, x) [Phi(E - x) + R_q(x)] dx / Z(E),   Phi(W') = R_p(W') (W' >= 2), W' e_bin(W') (W' < 2);
  phonon W' >= 2: R_p(W') = (1 - p(W')) W' e_bin(W') + p(W') S(W'),  S(W') = <R_q(E) + R_q(W' - E)>_split.
Grid h = 0.02 Delta, Gauss-Legendre in both segments (W' >= 2 and W' < 2), linear interpolation, fixed point.
Energy closure: sum_bins S(W) = W (1 - Y(W)), checked against the fine-grid cascade.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy import sparse
from qp20_4 import Cascade, I_of, emit_weight, pair_nodes

EMAX = 120.0
BW = 0.1


def p_first(W, r):
    W = np.atleast_1d(np.asarray(W, float))
    out = np.zeros_like(W)
    m = W >= 2.0
    if np.any(m):
        I = I_of(W[m])
        out[m] = 1.0 if np.isinf(r) else I / (I + np.pi / r)
    return out


def _interp_rows(xq, grid):
    """Row-wise linear interpolation weights: returns (cols, weights) of shape xq.shape + (2,)."""
    h = grid[1] - grid[0]
    t = (np.clip(xq, grid[0], grid[-1]) - grid[0]) / h
    i0 = np.clip(np.floor(t).astype(int), 0, len(grid) - 2)
    f = t - i0
    return np.stack([i0, i0 + 1], -1), np.stack([1 - f, f], -1)


class FilmResponse:
    def __init__(self, r, h=0.02, nq=48, tol=1e-11, itmax=400):
        self.r = r
        self.fine = Cascade(r, Emax=EMAX, h=0.01)
        self._args = (h, nq, tol, itmax)
        self.S = None

    def _build(self):
        h, nq, tol, itmax = self._args
        r = self.r
        xg, wg = leggauss(nq)
        self.Eg = np.arange(1.0, EMAX + h / 2, h)          # quasiparticle grid (R_q(1) = 0)
        self.Wg = np.arange(2.0, EMAX + h / 2, h)          # phonon grid
        nE, nW = len(self.Eg), len(self.Wg)
        self.nb = int(round(EMAX / BW))
        self.edges = np.arange(self.nb + 1) * BW
        binof = lambda w: np.clip((w / BW).astype(int), 0, self.nb - 1)
        # --- quasiparticle emission: segments x in [1, E-2] (W' >= 2) and [max(1, E-2), E] (W' < 2)
        rows_q, cols_q, vals_q = [], [], []   # R_q(node) interpolation -> into R_q
        rows_p, cols_p, vals_p = [], [], []   # R_p(W') interpolation -> into R_q
        rows_d, cols_d, vals_d = [], [], []   # direct sub-gap phonon deposits -> output bins
        for i, E in enumerate(self.Eg):
            if i == 0:
                continue
            segs = []
            if E > 3.0:
                U = E - 2.0                               # x in [1, U]: substitution x = 1 + (U-1) s^2
                s = 0.5 * (xg + 1); ws = 0.5 * wg
                x = 1.0 + (U - 1.0) * s**2
                w = 2.0 * x * np.sqrt(U - 1.0) / np.sqrt(x + 1.0) * ws
                segs.append((x, w, True))
                a, b = U, E                               # regular rho on [E-2, E]
                x = 0.5 * (b - a) * xg + 0.5 * (b + a)
                w = 0.5 * (b - a) * wg * x / np.sqrt(x**2 - 1.0)
                segs.append((x, w, False))
            else:
                s = 0.5 * (xg + 1); ws = 0.5 * wg
                x = 1.0 + (E - 1.0) * s**2
                w = 2.0 * x * np.sqrt(E - 1.0) / np.sqrt(x + 1.0) * ws
                segs.append((x, w, False))
            K = [ww * emit_weight(E, xx) for xx, ww, _ in segs]
            Z = sum(k.sum() for k in K)
            for (xx, ww, hard), k in zip(segs, K):
                k = k / Z
                c, f = _interp_rows(xx, self.Eg)
                rows_q.append(np.repeat(i, 2 * len(xx))); cols_q.append(c.ravel()); vals_q.append((k[:, None] * f).ravel())
                Wp = E - xx
                if hard:
                    c, f = _interp_rows(Wp, self.Wg)
                    rows_p.append(np.repeat(i, 2 * len(xx))); cols_p.append(c.ravel()); vals_p.append((k[:, None] * f).ravel())
                else:
                    rows_d.append(np.full(len(xx), i)); cols_d.append(binof(Wp)); vals_d.append(k * Wp)
        cat = np.concatenate
        self.Mqq = sparse.csr_matrix((cat(vals_q), (cat(rows_q), cat(cols_q))), shape=(nE, nE))
        self.Mqp = sparse.csr_matrix((cat(vals_p), (cat(rows_p), cat(cols_p))), shape=(nE, nW))
        self.Dq = sparse.csr_matrix((cat(vals_d), (cat(rows_d), cat(cols_d))), shape=(nE, self.nb)).toarray()
        # --- phonon split: S(W') = <R_q(E) + R_q(W' - E)>
        E1, E2, kp = pair_nodes(self.Wg, +1.0)
        kp = kp / kp.sum(axis=1, keepdims=True)
        rr, cc, vv = [], [], []
        for Ex in (E1, E2):
            c, f = _interp_rows(Ex, self.Eg)
            rr.append(np.repeat(np.arange(nW), Ex.shape[1] * 2)); cc.append(c.reshape(nW, -1).ravel())
            vv.append((kp[:, :, None] * f).reshape(nW, -1).ravel())
        self.Mpq = sparse.csr_matrix((cat(vv), (cat(rr), cat(cc))), shape=(nW, nE))
        self.pW = p_first(self.Wg, r)
        Dp = np.zeros((nW, self.nb))
        Dp[np.arange(nW), binof(self.Wg)] = self.Wg
        self.Dp = (1.0 - self.pW)[:, None] * Dp
        # --- fixed point
        Rq = np.zeros((nE, self.nb))
        for it in range(itmax):
            S = self.Mpq @ Rq
            Rp = self.Dp + self.pW[:, None] * S
            Rq_new = self.Dq + self.Mqp @ Rp + self.Mqq @ Rq
            Rq_new[0] = 0.0
            d = np.abs(Rq_new - Rq).max()
            Rq = Rq_new
            if d < tol:
                break
        self.iters = it + 1
        self.S = self.Mpq @ Rq                              # spectrum per first-broken phonon on Wg

    def Y(self, W):
        W = np.atleast_1d(np.asarray(W, float))
        return self.fine.Y(np.clip(W, 2.0, EMAX))

    def spectrum(self, W):
        """Escaped energy per output bin for a first-broken phonon of energy W (held shape, scaled energy above EMAX)."""
        if self.S is None:
            self._build()
        W = np.atleast_1d(np.asarray(W, float))
        Wc = np.clip(W, 2.0, EMAX)
        c, f = _interp_rows(Wc, self.Wg)
        S = f[:, 0, None] * self.S[c[:, 0]] + f[:, 1, None] * self.S[c[:, 1]]
        return S * (W / Wc)[:, None]

    def closure(self, Ws):
        """max over the given energies of |sum S - W(1 - Y_fine)| / W (relative energy closure against the fine grid)."""
        Ws = np.asarray(Ws, float)
        return (np.abs(self.spectrum(Ws).sum(axis=1) - Ws * (1 - self.Y(Ws))) / Ws).max()
