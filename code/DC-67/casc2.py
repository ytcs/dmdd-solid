"""DC-67: two-table generating-function solver for P_casc(N | x_e, x_h; theta) (CW7-153a,b; general case of CW7-errata sec. 1.4).

Units E_g = 1.  G_t(x; z) = E[z^N | carrier of type t at kinetic energy x], t = 0 (e), 1 (h):
  G_t(x) = p_t(x) z [(rho_t G_t)*(rho_t G_t)*(rho_tbar G_tbar)](x - 1)/Phi_t(x - 1) + (1 - p_t(x)) G_t(x - w),   G_t = 1 for x < theta,
  p_t(x) = 1/(1 + lam rho_t(x - w)/Phi_t(x - 1)),  Phi_t = rho_t*rho_t*rho_tbar   (GAP-EF (EF2); same discrete arithmetic as cascade.py).
rho_h may be cut at W = W_v/E_g (Si; narrow-band variant).  With W = None rho_e = rho_h and one table is solved.
Commensurate grid: h = 1/N must divide 1 and theta (check_grid raises otherwise); w must also divide unless frac = True.
Value at the true w (frac = True, production): the phonon step reads G(x - w) as the convex mixture (1 - a) G(n - nf) + a G(n - nf - 1), nf = floor(wN), a = wN - nf, i.e. steps nf, nf + 1
with mean exactly w: a p.g.f. mixture, so sum P = 1 and P >= 0 hold by construction, and p_t uses rho_t at the exact x - w.  a = 0 reproduces the commensurate recursion.
Lagrange interpolation of P over commensurate nodes (GAP-EF-v3's rule for eps, F) was tried first and REJECTED for distributions: it is not moment preserving and gives P < 0 (data/rejected_nodeP/).
z_k = exp(2 pi i k/Nz); only k = 0..Nz/2 are solved, since G(conj z) = conj G(z).  Layout: (Nz/2 + 1, K), convolutions by contiguous dots."""
import numpy as np


def _divides(h, v, tol=1e-9):
    r = v / h
    return abs(r - round(r)) <= tol * max(1.0, abs(r))


def check_grid(h, w, theta):
    bad = [n for n, v in (("E_g", 1.0), ("theta", theta), ("omega_0", w)) if not _divides(h, v)]
    if w < h * (1 - 1e-9):
        bad.append("omega_0 < h")
    if bad:
        raise ValueError("non-commensurate grid h = %.9g: %s" % (h, ", ".join(bad)))


def setup(lam, w, X, N, a=0.5, W=None, theta=1.0, frac=False):
    h = 1.0 / N
    check_grid(h, h if frac else w, theta)
    K = int(round(X * N)) + 1
    x = np.arange(K) * h
    nG = N
    nw = int(np.floor(w * N + 1e-9)) if frac else int(round(w * N))
    af = max(w * N - nw, 0.0) if frac else 0.0
    if af < 1e-9: af = 0.0
    nth = max(nG, int(round(theta * N)))
    re = x ** a
    rh = re if W is None else np.where(x <= W, re, 0.0)
    rho = (re, rh)
    c = lambda f, g: np.convolve(f, g)[:K] * h
    xm = np.maximum(x - w, 0.0) if frac else None
    rm = None if not frac else (xm ** a, np.where(xm <= W, xm ** a, 0.0) if W is not None else xm ** a)
    D = (c(re, rh), c(rh, re))
    Phi = (c(D[0], re), c(D[1], rh))
    p = (np.zeros(K), np.zeros(K))
    for t in (0, 1):
        n = np.arange(nth, K)
        q = n - nG
        ok = Phi[t][q] > 0
        r_at = rm[t][n[ok]] if frac else rho[t][n[ok] - nw]
        p[t][n[ok]] = 1.0 / (1.0 + lam * r_at / Phi[t][q[ok]])
    return dict(h=h, K=K, x=x, nG=nG, nw=nw, af=af, nth=nth, rho=rho, Phi=Phi, p=p, sym=W is None)


def _dotz(A, Brev, q, K):
    """sum_{j<=q} A[:, j] B[:, q - j]; Brev[:, K - 1 - j] = B[:, j]."""
    return np.einsum("ij,ij->i", A[:, :q + 1], Brev[:, K - 1 - q:])


def solve_gf(lam, w, X, N, Nz, a=0.5, W=None, theta=1.0, frac=False):
    """Returns (x, G) with G[t] of shape (K, Nz) on the full circle (conjugates filled)."""
    s = setup(lam, w, X, N, a, W, theta, frac)
    K, h, nG, nw, nth, sym, af = s["K"], s["h"], s["nG"], s["nw"], s["nth"], s["sym"], s["af"]
    nzh = Nz // 2 + 1
    zs = np.exp(2j * np.pi * np.arange(nzh) / Nz)
    T = (0,) if sym else (0, 1)
    G = [np.ones((nzh, K), complex) for _ in T]
    F = [s["rho"][t][None, :] * G[i] for i, t in enumerate(T)]               # f_t = rho_t G_t
    Fr = [np.ascontiguousarray(f[:, ::-1]) for f in F]
    C2 = [np.zeros((nzh, K), complex) for _ in T]
    C2r = None
    C3 = [np.zeros((nzh, K), complex) for _ in T]

    def conv(q):
        for i, t in enumerate(T):
            C2[i][:, q] = h * _dotz(F[i], Fr[i], q, K)
        for i, t in enumerate(T):
            ib = i if sym else 1 - i
            C3[i][:, q] = h * _dotz(C2[i], Fr[ib], q, K)

    for q in range(0, nth - nG):
        conv(q)
    for n in range(nth, K):
        q = n - nG
        conv(q)
        for i, t in enumerate(T):
            Ph = s["Phi"][t][q]
            pn = s["p"][t][n]
            avg = C3[i][:, q] / Ph if Ph > 0 else 1.0
            if af == 0.0:
                G[i][:, n] = pn * zs * avg + (1 - pn) * G[i][:, n - nw]
            elif nw >= 1:
                G[i][:, n] = pn * zs * avg + (1 - pn) * ((1 - af) * G[i][:, n - nw] + af * G[i][:, n - nw - 1])
            else:                                   # w < h: the step-0 branch is implicit
                G[i][:, n] = (pn * zs * avg + (1 - pn) * af * G[i][:, n - 1]) / (1 - (1 - pn) * (1 - af))
            F[i][:, n] = s["rho"][t][n] * G[i][:, n]
            Fr[i][:, K - 1 - n] = F[i][:, n]
    out = []
    for i in range(len(T)):
        full = np.empty((K, Nz), complex)
        full[:, :nzh] = G[i].T
        full[:, nzh:] = np.conj(G[i].T[:, Nz - np.arange(nzh, Nz)])
        out.append(full)
    if sym:
        out = [out[0], out[0]]
    return s["x"], out


def pmf(Grow):
    """P(N = n | x), n = 0..Nz-1 (aliased sum; exact iff P(N >= Nz) = 0).  z_k^{-n}: forward FFT over k, /Nz."""
    return np.real(np.fft.fft(Grow, axis=-1)) / Grow.shape[-1]


def compose(Pe, Ph, nmax=None):
    """P(N | x_e, x_h) = [z^N] z G_e G_h (CW7-153b): N = 1 + N_e + N_h."""
    c = np.convolve(Pe, Ph)
    out = np.concatenate([[0.0], c])
    return out if nmax is None else out[:nmax + 1]
