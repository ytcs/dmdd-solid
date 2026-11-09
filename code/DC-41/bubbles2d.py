"""DC-41 direct path: CW4 (1.1) by 2-D quadrature from the Bogoliubov spinors; no closed form is used.  Units Delta = 1.
Pi_ij(q,w) = (N/2) Int dmu Int dxi [ M_i* M_j/(w - W + i0) - M_i M_j*/(w + W + i0) ],  W = E + E',  xi' = xi + s,  s = Q mu (q^2/2m dropped; see sec. 2).
|+> = (u,v), |-> = (-v,u);  M_3 = <+'|tau_3|->,  M_2 = <+'|tau_2|->,  M_1 = <+'|tau_1|-> (amplitude channel, control).
Gauss-Legendre in mu (panels at mu*, y/Q); xi = eta - s/2, eta in [0, Lam] (integrand even in eta): Gauss panels graded at the root eta0 and at eta = s/2.
Im: delta(w - W) at the two roots +-eta0 (eta0 by bisection on W(eta) = w, no closed form).  Re: both poles subtracted, 2 r eta0/(eta0^2 - eta^2), analytic PV.
Pi22(0,0) enters through its integrand at the same cutoff: per eta, -2/sqrt(eta^2 + 1) ... the difference Pi22(0,0) - Pi22(q,w) is integrated pointwise, tail O(1/Lam^2)."""
import numpy as np
from scipy.optimize import brentq

def spinor(xi):
    E = np.sqrt(xi * xi + 1.0)
    return np.sqrt(0.5 * (1 + xi / E)), np.sqrt(0.5 * (1 - xi / E)), E

def amps(eta, s):
    """M_3, M_2, M_1 for the pair (xi, xi') from the spinors: <+'|tau|-> with |-> = (-v, u)."""
    xi, xp = eta - 0.5 * s, eta + 0.5 * s
    u, v, E = spinor(xi); up, vp, Ep = spinor(xp)
    ket = np.array([-v, u], dtype=complex)                     # |->
    bra = np.array([up, vp], dtype=complex)                    # <+'| (real)
    t3 = np.array([ket[0], -ket[1]]); t2 = np.array([-1j * ket[1], 1j * ket[0]]); t1 = np.array([ket[1], ket[0]])
    M3 = bra[0] * t3[0] + bra[1] * t3[1]
    M2 = bra[0] * t2[0] + bra[1] * t2[1]
    M1 = bra[0] * t1[0] + bra[1] * t1[1]
    return M3, M2, M1, E + Ep

def Wof(eta, s):
    return np.sqrt((eta - .5 * s) ** 2 + 1) + np.sqrt((eta + .5 * s) ** 2 + 1)

def eta_panels(s, eta0, Lam, nk):
    b = [0.0, Lam, 0.5 * abs(s)]
    sc = [1.0, abs(s) if s else 1.0]
    p = 0.5 * abs(s)
    for j in range(-6, 60):
        for sg in (-1, 1):
            b.append(p + sg * 2.0 ** j)
        b.append(2.0 ** j)
    if eta0 is not None:
        b.append(eta0)
        for j in range(1, nk):
            b += [eta0 * (1 - 2.0 ** -j), eta0 * (1 + 2.0 ** -j)]
    b = np.array(sorted({x for x in b if 0 <= x <= Lam}))
    return b

def fixed_s(y, s, n=10, Lam=None, nk=8):
    """Int dxi of the (1.1) brackets at fixed s.  Returns dict B33, B23s (= M3* M2 bracket / i), B22d (= Pi22(0,0)-Pi22 integrand), B31 (amplitude-density), complex."""
    if Lam is None:
        Lam = 1e3 * max(1.0, abs(s), y)
    wmin = Wof(0.0, s)
    eta0 = None
    if y > wmin:
        eta0 = brentq(lambda e: Wof(e, s) - y, 0.0, 2 * y + abs(s), xtol=1e-13, rtol=1e-13)
    b = eta_panels(s, eta0, Lam, nk)
    xg, wg = np.polynomial.legendre.leggauss(n)
    a, c = b[:-1, None], b[1:, None]
    eta = (0.5 * (c - a) * xg + 0.5 * (c + a)).ravel(); w = (0.5 * (c - a) * wg).ravel()
    M3, M2, M1, W = amps(eta, s)
    out = {}
    for name, (Afun) in {"33": lambda a3, a2, a1: np.conj(a3) * a3, "32": lambda a3, a2, a1: np.conj(a3) * a2,
                         "22": lambda a3, a2, a1: np.conj(a2) * a2}.items():
        A = Afun(M3, M2, M1); Ab = np.conj(A)
        reg = -Ab / (y + W)
        extra = 0.0
        if name == "22":
            extra = 1.0 / np.sqrt(eta * eta + 1.0)            # + Pi22(0,0) per half line has -1/E: we integrate Pi22 - Pi22(0,0), Pi22(0,0) integrand -1/E
        if eta0 is None:
            val = 2 * (w @ (A / (y - W) + reg + extra))
        else:
            a0 = Afun(*[m[0] for m in amps(np.array([eta0]), s)[:3]])
            h = 1e-6 * max(eta0, 1e-3)
            Wp = (Wof(eta0 + h, s) - Wof(eta0 - h, s)) / (2 * h)
            r = a0 / Wp
            sub = 2 * r * eta0 / (eta0 ** 2 - eta ** 2)
            I = w @ (A / (y - W) - sub + reg + extra)
            pv = r * np.log((Lam + eta0) / (Lam - eta0))
            val = 2 * (I + pv) - 2j * np.pi * r              # two roots, each -i pi r  (2 = both signs of eta)
        out[name] = val
    return out, Wof(0.0, s), eta0

def mu_nodes(y, Q, nmu):
    """Gauss panels in s on [0, Q] with sqrt clustering at s* (fixed order, doubled by nmu)."""
    b = [0.0, Q]
    if y > 2:
        ss = np.sqrt(y * y - 4)
        b.append(ss)
        for j in range(1, 26):
            b += [ss * (1 - 2.0 ** -j), ss + (ss + 1) * 2.0 ** -j]
    b.append(y)
    t = 2 * max(y, 2.0)
    while t < Q:
        b.append(t); t *= 2
    b = np.array(sorted({x for x in b if 0 <= x <= Q}))
    xg, wg = np.polynomial.legendre.leggauss(nmu)
    a, c = b[:-1, None], b[1:, None]
    return (0.5 * (c - a) * xg + 0.5 * (c + a)).ravel(), (0.5 * (c - a) * wg).ravel()

def bubbles(y, Q, nmu=6, n=10, Lam=None, nk=8):
    """Normalised P33, P32 (= Pi32/2N), D = [Pi22(0,0) - Pi22]/2N.  (N/2) Int_-1^1 dmu = N Int_0^1 dmu (s-even); /2N -> (1/2)<.>."""
    s, ws = mu_nodes(y, Q, nmu); ws = ws / Q
    acc = dict.fromkeys(("33", "32", "22"), 0.0 + 0j)
    for si, wi in zip(s, ws):
        o, _, _ = fixed_s(y, si, n=n, Lam=Lam, nk=nk)
        for k in acc:
            acc[k] = acc[k] + wi * o[k]
    return dict(P33=0.5 * acc["33"], P32=0.5 * acc["32"], D=-0.5 * acc["22"])

def grpa(b):
    """R~ = Pi33 + Pi32 D^-1 Pi23 with Pi23 from (1.1) directly: bracket of M2* M3.  Antisymmetry Pi23 = -Pi32 is carried explicitly (checked in checks.py)."""
    return b["P33"] + b["P32"] * (-b["P32"]) / b["D"]
