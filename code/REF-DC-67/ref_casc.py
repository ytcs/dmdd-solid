"""REF-DC-67: referee's own cascade solver.  Shares no code or quadrature with cascade.py / casc2.py.
Units E_g = 1.  Discretisation differs on purpose from DC-67:
  * rho_t enters as EXACT cell masses mu_t[j] = int_{(j-1/2)h}^{(j+1/2)h} rho_t (hole cut exactly at W, also when W is off grid); DC-67 point-samples rho (rectangle rule, O(h^{3/2}));
  * p_t uses the closed-form Phi_t; DC-67 uses the discrete sum;
  * triple convolutions by FFT per block of N bins (x - 1 is one block back, so a block is explicit); DC-67 uses online dots.
Phonon read: 'exact' (w N integer), 'lin' (the convex read of DC-67), 'cubic' (4-point Lagrange in x; the reference for non-commensurate w).
Hole rows above W are not physical and are not solved (kept at G = 1 / m = 0, weight zero)."""
import numpy as np
from scipy import fft as sf
from math import gamma
WK = 1

def masses(a, h, K, W=None):
    up = (np.arange(K) + .5) * h; lo = np.maximum(up - h, 0.0)
    if W is not None:
        up = np.minimum(up, W); lo = np.minimum(lo, W)
    return (up ** (a + 1) - lo ** (a + 1)) / (a + 1)

def _rho(x, a):
    return np.maximum(x, 0.0) ** a

def phi_exact(t, y, a, W):
    """Phi_e = rho_e*rho_e*rho_h (hole <= W); Phi_h = rho_h*rho_h*rho_e (y < W on all physical rows: uncut).  Closed form for a = 1/2, 1."""
    y = np.asarray(y, float)
    B = gamma(a + 1) ** 3 / gamma(3 * a + 3)
    if W is None or t == 1:
        return B * y ** (3 * a + 2)
    m = np.minimum(y, W)
    if a == .5:      # int_0^m s^{1/2} (pi/8)(y - s)^2 ds
        return (np.pi / 8) * (y * y * (2 / 3) * m ** 1.5 - 2 * y * (2 / 5) * m ** 2.5 + (2 / 7) * m ** 3.5)
    if a == 1.0:     # int_0^m s (y - s)^3/6 ds
        return (y ** 3 * m ** 2 / 2 - 3 * y * y * m ** 3 / 3 + 3 * y * m ** 4 / 4 - m ** 5 / 5) / 6
    raise ValueError

class Setup:
    def __init__(s, lam, w, X, N, a=.5, W=None, theta=1.0, read="auto"):
        s.lam, s.w, s.N, s.a, s.W, s.theta = lam, w, N, a, W, theta
        s.h = 1.0 / N; s.K = int(round(X * N)) + 1; s.x = np.arange(s.K) * s.h
        s.nth = int(round(theta * N)); assert abs(s.nth - theta * N) < 1e-9
        s.nf = int(np.floor(w * N + 1e-9)); s.fr = max(w * N - s.nf, 0.0)
        if s.fr < 1e-9: s.fr = 0.0
        s.read = ("exact" if s.fr == 0 else "cubic") if read == "auto" else read
        if s.read == "exact": assert s.fr == 0
        if s.read == "cubic": assert s.nf >= 2
        s.mu = (masses(a, s.h, s.K), masses(a, s.h, s.K, W))
        s.Kh = s.K if W is None else min(s.K, int(np.floor(W * N + .5)) + 1)   # last physical hole row
        p = []
        for t in (0, 1):
            y = s.x - 1.0
            ph = np.zeros(s.K); ok = y > 0
            ph[ok] = phi_exact(t, y[ok], a, W if t == 0 else None)
            r = _rho(s.x - w, a)
            pt = np.zeros(s.K); q = ok & (s.x >= theta - 1e-12)
            pt[q] = 1.0 / (1.0 + lam * r[q] / ph[q]); p.append(pt)
        s.p = p
        s.cs = {"exact": max(s.nf, 1), "lin": max(s.nf, 1), "cubic": max(s.nf - 1, 1)}[s.read]
        d = s.fr
        s.wts = {"exact": [(0, 1.0)], "lin": [(0, 1 - d), (1, d)],     # offsets below n - nf
                 "cubic": [(-1, -d * (1 - d) * (2 - d) / 6), (0, (1 + d) * (1 - d) * (2 - d) / 2), (1, (1 + d) * d * (2 - d) / 2), (2, -(1 + d) * d * (1 - d) / 6)]}[s.read]

    def phon(s, A, lo, hi):
        """value of A (.., K) at x - w for rows lo..hi-1"""
        out = 0
        for off, c in s.wts:
            out = out + c * A[..., lo - s.nf - off:hi - s.nf - off]
        return out

def _triple(u, v, k, L, q0, q1):
    return sf.irfft(sf.rfft(u, L, workers=WK) * sf.rfft(v, L, workers=WK) * sf.rfft(k, L, workers=WK), L, workers=WK)[q0:q1]

def moments(lam, w, X, N, a=.5, W=None, theta=1.0, read="auto"):
    """E[N], E[N^2] per carrier type on the grid."""
    s = Setup(lam, w, X, N, a, W, theta, read); K, nG = s.K, N
    m = [np.zeros(K), np.zeros(K)]; e2 = [np.zeros(K), np.zeros(K)]
    mu = s.mu
    b = s.nth
    while b < K:
        e = min(b + N if b > N else b + N, K)
        e = min(max(s.nth, (b // N + 1) * N), K) if b % N else min(b + N, K)
        q0, q1 = b - nG, e - nG
        J = b                    # entries < b are final; q < e - nG <= b
        L = sf.next_fast_len(3 * J, real=True)
        u = [mu[t][:J] for t in (0, 1)]; M = [mu[t][:J] * m[t][:J] for t in (0, 1)]; Q = [mu[t][:J] * e2[t][:J] for t in (0, 1)]
        U = [sf.rfft(v, L, workers=WK) for v in u]; MM = [sf.rfft(v, L, workers=WK) for v in M]; QQ = [sf.rfft(v, L, workers=WK) for v in Q]
        I1 = []; I2 = []
        for t in (0, 1):
            tb = 1 - t
            S = sf.irfft(U[t] * U[t] * U[tb], L, workers=WK)[q0:q1]
            n1 = sf.irfft(2 * MM[t] * U[t] * U[tb] + U[t] * U[t] * MM[tb], L, workers=WK)[q0:q1]
            n2 = sf.irfft(2 * QQ[t] * U[t] * U[tb] + U[t] * U[t] * QQ[tb] + 2 * (MM[t] * MM[t] * U[tb] + 2 * MM[t] * U[t] * MM[tb]), L, workers=WK)[q0:q1]
            ok = S > 0
            a1 = np.where(ok, n1 / np.where(ok, S, 1), 0.0); a2 = np.where(ok, n2 / np.where(ok, S, 1), 0.0)
            I1.append(a1); I2.append(a2)
        for lo in range(b, e, s.cs):
            hi = min(lo + s.cs, e)
            for t in (0, 1):
                if t == 1 and lo >= s.Kh: continue
                h2 = hi if t == 0 else min(hi, s.Kh)
                p = s.p[t][lo:h2]; A1 = I1[t][lo - b:h2 - b]; A2 = I2[t][lo - b:h2 - b]
                m[t][lo:h2] = p * (1 + A1) + (1 - p) * s.phon(m[t], lo, h2)
                e2[t][lo:h2] = p * (1 + 2 * A1 + A2) + (1 - p) * s.phon(e2[t], lo, h2)
        b = e
    return s.x, m, e2, s

def gf(lam, w, X, N, Nz, a=.5, W=None, theta=1.0, read="auto", rows=None):
    """P_t(n | x) at the z_k roots.  Returns x, [Pe, Ph] with shape (K, Nz) (or only `rows` indices if given)."""
    s = Setup(lam, w, X, N, a, W, theta, read); K, nG = s.K, N
    nzh = Nz // 2 + 1; z = np.exp(2j * np.pi * np.arange(nzh) / Nz)[:, None]
    G = [np.ones((nzh, K), complex), np.ones((nzh, K), complex)]
    mu = s.mu
    b = s.nth
    while b < K:
        e = min(max(s.nth, (b // N + 1) * N), K) if b % N else min(b + N, K)
        q0, q1 = b - nG, e - nG; J = b
        L = sf.next_fast_len(3 * J)
        FF = [sf.fft(mu[t][None, :J] * G[t][:, :J], L, axis=1, workers=WK) for t in (0, 1)]
        U = [sf.rfft(mu[t][:J], L, workers=WK) for t in (0, 1)]
        I = []
        for t in (0, 1):
            tb = 1 - t
            S = sf.irfft(U[t] * U[t] * U[tb], L, workers=WK)[q0:q1]
            c = sf.ifft(FF[t] * FF[t] * FF[tb], axis=1, workers=WK)[:, q0:q1]
            ok = S > 0
            I.append(np.where(ok[None, :], c / np.where(ok, S, 1)[None, :], 1.0))
        del FF
        for lo in range(b, e, s.cs):
            hi = min(lo + s.cs, e)
            for t in (0, 1):
                if t == 1 and lo >= s.Kh: continue
                h2 = hi if t == 0 else min(hi, s.Kh)
                p = s.p[t][None, lo:h2]
                G[t][:, lo:h2] = p * z * I[t][:, lo - b:h2 - b] + (1 - p) * s.phon(G[t], lo, h2)
        b = e
    out = []
    for t in (0, 1):
        g = G[t] if rows is None else G[t][:, rows]
        full = np.empty((g.shape[1], Nz), complex); full[:, :nzh] = g.T
        full[:, nzh:] = np.conj(g.T[:, Nz - np.arange(nzh, Nz)])
        out.append(np.real(sf.fft(full, axis=1)) / Nz)
    return (s.x if rows is None else s.x[rows]), out, s

def fit(x, m, e2, lo, hi, offset=1.0):
    """DC-67-equivalent definition: LSQ slopes of mean and variance vs omega = 1 + x on [lo, hi]."""
    sel = (x >= lo) & (x <= hi); om = 1 + x[sel]
    v = e2[sel] - m[sel] ** 2
    sm, b = np.polyfit(om, 1 + m[sel], 1); sv, c = np.polyfit(om, v, 1)
    return 1 / sm, sv / sm, b, c

def mc(lam, w, x0, M, W=None, theta=1.0, a=.5, seed=1, carrier=0):
    """Own event-by-event MC: explicit stack per history batch.  Continuous energies, true w.  Returns N (ii events) per history."""
    rng = np.random.default_rng(seed)
    E = np.full(M, float(x0)); T = np.full(M, carrier, np.int8); H = np.arange(M); cnt = np.zeros(M, np.int32)
    while E.size:
        k = E >= theta; E, T, H = E[k], T[k], H[k]
        if not E.size: break
        y = E - 1
        Phi = np.where(T == 0, phi_exact(0, np.maximum(y, 0), a, W), phi_exact(1, np.maximum(y, 0), a, None))
        r = np.maximum(E - w, 0) ** a
        p = np.zeros(E.size); o = Phi > 0
        p[o] = 1 / (1 + lam * r[o] / Phi[o])
        ii = rng.random(E.size) < p
        np.add.at(cnt, H[ii], 1)
        yi, ti, hi = y[ii], T[ii], H[ii]
        # (t, t, tbar) split with density x1^a x2^a x3^a on the simplex; rejection of holes above W
        D = np.empty((yi.size, 3)); todo = np.arange(yi.size)
        while todo.size:
            g = rng.standard_gamma(a + 1, (todo.size, 3)); g = g / g.sum(1, keepdims=True) * yi[todo, None]
            if W is None: ok = np.ones(todo.size, bool)
            else:
                tt = ti[todo]
                ok = np.where(tt == 0, g[:, 2] <= W, (g[:, 0] <= W) & (g[:, 1] <= W))
            D[todo[ok]] = g[ok]; todo = todo[~ok]
        Tn = np.stack([ti, ti, 1 - ti], 1).ravel().astype(np.int8)
        E = np.concatenate([E[~ii] - w, D.ravel()]); T = np.concatenate([T[~ii], Tn]); H = np.concatenate([H[~ii], np.repeat(hi, 3)])
    return cnt
