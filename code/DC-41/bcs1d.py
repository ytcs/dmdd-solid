"""DC-41 closed-form path (units Delta_BCS = 1, Q = q v_F/Delta_BCS, y = omega/Delta_BCS, s = Q mu).  Derived in returns/R18/DC-41.md sec. 2; checked against
the direct spinor quadrature bubbles2d.py (CW4 (1.1)).  With u^2 = y^2 - s^2, kappa = u^2/4 and the Tsuneto function
  f(y,s) = Int dxi (E+E')/(E E') / (y^2 - (E+E')^2),   retarded branch y + i0,
all pair bubbles at fixed s follow from f.  Normalised P_ij = Pi^N_ij/(2 N(0)); <X> = Int_0^1 dmu X(Q mu):
  P33 = -1 - (y^2/4) <c>,  c = (-f - 1)/kappa;     Pi32 Pi23/(2N(0))^2 = (y/2)^2 <f>^2;     D/(2N(0)) = -(1/4)<u^2 f> = -<kappa f>;
  P~ = P33 - y^2 <f>^2 / (4 <kappa f>)   [GRPA].          epsilon ~ -(k_TF^2/q^2) P  (k_TF >> q)."""
import numpy as np
from scipy.special import ellipk, ellipe
from scipy import integrate

GL = {}
def gl(n):
    if n not in GL:
        GL[n] = np.polynomial.legendre.leggauss(n)
    return GL[n]

SER = [2 / 3, 8 / 15, 16 / 35, 128 / 315, 256 / 693, 1024 / 3003, 2048 / 6435, 32768 / 109395]   # arcsin(r)/(r sqrt(1-r^2)) = 1 + kappa (2/3 + 8k/15 + ...)

def c_of(k):
    """c(kappa) = (-f - 1)/kappa, stable at kappa -> 0."""
    k = np.asarray(k, float)
    return _fc(k)[1]

def f_of(k):
    return _fc(np.asarray(k, float))[0]

def _fc(k):
    f = np.empty(k.shape, complex); c = np.empty(k.shape, complex)
    small = np.abs(k) < 2e-2
    ks = k[small]; cs = np.zeros(ks.shape)
    for a in SER[::-1]:
        cs = cs * ks + a
    c[small] = cs; f[small] = -(1 + ks * cs)
    m = (k < 0) & ~small
    a = -k[m]; f[m] = -np.arcsinh(np.sqrt(a)) / np.sqrt(a * (1 + a))
    m = (k >= 0) & (k < 1) & ~small
    a = k[m]; f[m] = -np.arcsin(np.sqrt(a)) / np.sqrt(a * (1 - a))
    m = k >= 1
    a = np.maximum(k[m], 1 + 1e-15); f[m] = (np.arccosh(np.sqrt(a)) - 0.5j * np.pi) / np.sqrt(a * (a - 1))
    m = ~small
    c[m] = (-f[m] - 1) / k[m]
    return f, c

def _grade(p, lo, hi, nk=44):
    out = []
    for sgn, L in ((-1, p - lo), (1, hi - p)):
        if L <= 0: continue
        out += [p + sgn * L * 2.0 ** (-j) for j in range(1, nk)]
    return out

def panels(y, S, refine=1):
    """Break points on [0, S] for the s integral: inverse-sqrt edge at s* = sqrt(y^2 - 4) (y > 2), peak at s = 0 of width sqrt(4 - y^2) (y < 2), s = y, geometric tail."""
    b = [0.0, S]
    top = max(y, 2.0) * 2
    if y > 2:
        ss = np.sqrt(y * y - 4); b += _grade(ss, 0.0, 2 * ss + 2.0); b.append(ss)
    else:
        d = max(np.sqrt(max(4 - y * y, 0.0)), 1e-300)
        t = d / 16
        while t < top * 2:
            b.append(t); t *= 2
    b.append(y)
    t = top
    while t < S:
        b.append(t); t *= 1.5
    b = np.array(sorted(x for x in set(b) if 0.0 <= x <= S))
    if refine > 1:
        b = np.unique(np.concatenate([b + (b[1:].tolist() + [b[-1]] - b) * j / refine for j in range(refine)]))
    return b

def snodes(y, S, n=12, refine=1):
    b = panels(y, S, refine); xg, wg = gl(n)
    a, c = b[:-1, None], b[1:, None]
    return (0.5 * (c - a) * xg + 0.5 * (c + a)).ravel(), (0.5 * (c - a) * wg).ravel()

def avgs(y, Q, n=12, refine=1, dq=0.0):
    """<c>, <f>, <kappa f> with mu in [0,1] (dq = 0).  dq = q^2/2m in units of Delta: s = Q mu + dq, mu in [-1,1], <X> = (1/2) Int dmu X."""
    if dq == 0.0:
        s, w = snodes(y, Q, n, refine); w = w / Q
    else:
        s1, w1 = snodes(y, Q + dq, n, refine); s2, w2 = snodes(y, Q - dq, n, refine)
        s = np.concatenate([s1, s2]); w = np.concatenate([w1, w2]) / (2 * Q)
    k = 0.25 * (y * y - s * s)
    f, c = _fc(k)
    return w @ c, w @ f, w @ (k * f)

def P33(y, Q, **kw):
    C, F, KF = avgs(y, Q, **kw)
    return -1 - 0.25 * y * y * C

def Pg(y, Q, **kw):
    """(P33, P~ GRPA)."""
    C, F, KF = avgs(y, Q, **kw)
    p = -1 - 0.25 * y * y * C
    return p, p - 0.25 * y * y * F * F / KF

def pnor(y, Q):
    x = y / Q
    re = -1 + 0.5 * x * np.log(abs((1 + x) / (1 - x)))
    return re + (-0.5j * np.pi * x if x < 1 else 0.0)

def gI(y):
    y = np.asarray(y, float)
    k = (y - 2) / (y + 2)
    return (1 + 2 / y) * ellipe(k * k) - 4 * ellipk(k * k) / (y + 2)

def gI_int(y):
    """[4.2] via this return's u-form: 4 y Int_2^y du/(u^2 sqrt(u^2-4) sqrt(y^2-u^2)) (t = substitution removes both edges)."""
    a, b = 2.0, y
    fn = lambda th: 4 * y / ((a + (b - a) * np.sin(th) ** 2) ** 2 * np.sqrt((a + (b - a) * np.sin(th) ** 2 + 2) * (y + a + (b - a) * np.sin(th) ** 2))) * 2
    return integrate.quad(fn, 0, np.pi / 2, limit=400)[0]

def s_bcs(y, Y=None):
    """CW4 K2 s_BCS(y) (code/CW4/checks.py, copied): Y = None: KK to infinity; Y: cut at y' = Y."""
    def f_I(yp): return np.where(yp > 2, gI(np.maximum(yp, 2.0000001)) - 1, -1.0)
    gg = lambda yp: yp ** 2 * f_I(yp)
    top = 1e4 if Y is None else Y
    hf = lambda yp: (gg(yp) - gg(y)) / (yp ** 2 - y ** 2) if abs(yp - y) > 1e-9 else 0.0
    I1 = integrate.quad(hf, 0, top, points=[2.0, y] if top > y else [2.0], limit=800)[0]
    I2 = gg(y) / (2 * y) * np.log(abs((top - y) / (top + y)))
    tail = integrate.quad(lambda yp: yp ** 2 * (gI(yp) - 1) / (yp ** 2 - y ** 2), 1e4, np.inf, limit=200)[0] if Y is None else 0.0
    return float(I1 + I2 + tail)

def ab_pole(Q, **kw):
    """Anderson-Bogoliubov pole of the ladder: <kappa f>(omega) = 0 on (0,2); returns (omega_AB, Z) with P~ ~ Z/(omega - omega_AB + i0), or (2, 0) if 2 - omega_AB < 1e-13.
    <kappa f> > 0 at small omega and -> -inf (log) at omega -> 2-: there is a zero for every Q."""
    from scipy.optimize import brentq
    g = lambda d: np.real(avgs(2 - d, Q, **kw)[2])        # d = 2 - omega
    DMIN = 1e-13
    hi = 2 - 1e-9
    if g(hi) <= 0: return None, 0.0, None
    if g(DMIN) > 0: return 2.0, 0.0, 0.0                  # pole closer to 2 than DMIN: residue ~ d ln^2(d)/Q < 1e-10, dropped
    ld = brentq(lambda t: g(np.exp(t)), np.log(DMIN), np.log(hi), xtol=1e-10)
    d = np.exp(ld); w = 2 - d
    h = d * 1e-4
    dg = (g(d + h) - g(d - h)) / (2 * h)          # d<kf>/dd = -d<kf>/domega
    C, F, KF = avgs(w, Q, **kw)
    Z = -0.25 * w * w * np.real(F) ** 2 / (-dg)    # P~ = -(w^2/4) F^2/KF, KF ~ (-dg)(omega - w)
    return w, Z, d
