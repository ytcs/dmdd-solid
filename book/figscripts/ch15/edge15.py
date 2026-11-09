"""Clean, quasiclassical BCS density response at the pair-breaking edge (Sect. 15.2, App. D.39).

All energies in units of Delta_BCS; y = omega/Delta_BCS, Q = q v_F/Delta_BCS, nu = omega/(q v_F) = y/Q.
Hypotheses (Sect. 15.2): T = 0, constant density of states over the energies involved, q << k_F, q << k_TF
(the "1" of epsilon dropped), linearized band xi' - xi = v_F q mu (q^2/2m_e dropped), clean (no impurities).
With these, epsilon = -(k_TF^2/q^2) P(y, Q), and every loss-function ratio depends on (y, Q) alone.

Normal metal (Lindhard at q << k_F, Eq. (4.5-lindhard) of the book with nu_pm -> nu):
  P_nor(nu) = -[1 - (nu/2) ln|(1+nu)/(1-nu)|] - i (pi/2) nu Theta(1 - nu).
Case-I coherence integral (Eq. 7.2-pairspec; closed form of Eq. 15.1-gI):
  g_I(y) = (1 + 2/y) E(k) - 4 K(k)/(y + 2),  k = (y-2)/(y+2)  (modulus k; scipy uses m = k^2).
Kramers-Kronig correction function (Eq. 15.1-sBCS; numerics in App. D.39):
  s_BCS(y; Ycut) = PV int_0^Ycut dy' y'^2 [g_I(y') Theta(y'-2) - 1]/(y'^2 - y^2),  Ycut = infinity or Q.
Resummed bare loss function (Eq. 15.2-LBCS):
  L/(g_I L_nor) = (1 + r^2)/[(1 + d)^2 + g_I^2 r^2],  r = Im eps_nor/Re eps_nor,  d = (1/Q) s_BCS/Re f(nu),
  Re f(nu) = 1 - (nu/2) ln[(1+nu)/(1-nu)].
Bare bubble and conserving (pair-field ladder) response in the closed form of Sect. 15.1 (Eq. 15.1-Rcons):
  s = Q mu, u^2 = y^2 - s^2, kappa = u^2/4, <X> = int_0^1 dmu X,
  f = -asinh(sqrt|k|)/sqrt(|k|(1+|k|))       (kappa < 0)
    = -asin(sqrt k)/sqrt(k(1-k))              (0 < kappa < 1)
    = [acosh(sqrt k) - i pi/2]/sqrt(k(k-1))   (kappa > 1, omega + i0),
  P33 = <(s^2 + y^2 f)/u^2>,  P_cons = P33 - y^2 <f>^2/<u^2 f>.
Loss-function ratios: L_X/L_nor = Im(1/P_X)/Im(1/P_nor).
"""
import numpy as np
from scipy import integrate, special

PI = np.pi


def g_I(y):
    y = np.asarray(y, dtype=float)
    out = np.zeros_like(y)
    m = y > 2
    k = (y[m] - 2) / (y[m] + 2)
    out[m] = (1 + 2 / y[m]) * special.ellipe(k**2) - 4 * special.ellipk(k**2) / (y[m] + 2)
    return out


def g_I_integral(y):
    """7.2-pairspec form: (1/y) int_1^{y-1} dx [x(y-x) + 1]/sqrt((x^2-1)((y-x)^2-1)), x = E/Delta."""
    # substitution x = 1 + (y-2) sin^2(t) removes both edge singularities
    a = y - 2.0

    def f(t):
        x = 1 + a * np.sin(t) ** 2
        dx = 2 * a * np.sin(t) * np.cos(t)
        return (x * (y - x) + 1) / np.sqrt((x * x - 1) * ((y - x) ** 2 - 1)) * dx

    val, _ = integrate.quad(f, 0, PI / 2, limit=200)
    return val / y


def ref_lin(nu):
    return 1 - 0.5 * nu * np.log(abs((1 + nu) / (1 - nu)))


def P_nor(nu):
    im = -0.5 * PI * nu if nu < 1 else 0.0
    return -ref_lin(nu) + 1j * im


def _gm1(yp):
    return (g_I(np.array([yp]))[0] if yp > 2 else 0.0) - 1.0


def s_BCS(y, ycut=np.inf):
    """PV int_0^ycut dy' y'^2 [g_I Theta(y'-2) - 1]/(y'^2 - y^2), principal value at y' = y.
    Written as int dy' [h(y') - h(y)]/(y' - y) + h(y) ln|(ycut - y)/y| with h(y') = y'^2 [..]/(y' + y),
    for y' < 2 the bracket is -1 (analytic); the log singularity of g_I at y' = 2 is integrable."""
    def h(yp):
        return yp * yp * _gm1(yp) / (yp + y)

    hy = h(y)
    pts = sorted(set([2.0, y]))
    total = 0.0
    upper = ycut if np.isfinite(ycut) else None
    # finite pieces
    segs = []
    prev = 0.0
    for p in pts:
        segs.append((prev, p))
        prev = p
    big = 4 * max(y, 2.0) + 20
    if upper is None:
        segs.append((prev, big))
    else:
        segs.append((prev, upper))
    for a, b in segs:
        if b <= a:
            continue
        val, _ = integrate.quad(lambda t: (h(t) - hy) / (t - y) if t != y else 0.0, a, b, limit=400,
                                epsabs=1e-12, epsrel=1e-10)
        total += val
    if upper is None:
        # tail beyond 'big': integrand y'^2 (g_I - 1)/(y'^2 - y^2); g_I - 1 ~ (2 ln(2y') - 1)/y'^2
        tail = lambda t: t * t * _gm1(t) / (t * t - y * y)
        val1, _ = integrate.quad(tail, big, 1e4, limit=400, epsabs=1e-13, epsrel=1e-10)
        # beyond 1e4: g_I - 1 = (2 ln(2y') - 1)/y'^2 + O(y'^-4), so the integrand is (2 ln(2t) - 1)/t^2
        # and int_T^inf (2 ln(2t) - 1)/t^2 dt = (2 ln(2T) + 1)/T
        T = 1e4
        val = val1 + (2 * np.log(2 * T) + 1) / T
        # subtract the hy part that the principal-value split assigned to [0, big]
        total += val + hy * np.log(abs((big - y) / y))
    else:
        total += hy * np.log(abs((upper - y) / y))
    return total


def resummed(y, Q, ycut=np.inf):
    """Bare resummed L/(g_I L_nor) and its ingredients."""
    nu = y / Q
    rf = ref_lin(nu)
    r = 0.5 * PI * nu / rf
    s = s_BCS(y, ycut)
    d = s / Q / rf
    g = g_I(np.array([y]))[0]
    ratio = (1 + r * r) / ((1 + d) ** 2 + g * g * r * r)
    return dict(nu=nu, ref=rf, r=r, s=s, d=d, g=g, ratio=ratio, first=2 * s / Q)


# ---------------------------------------------------------------- closed form of Eq. 15.1-Rcons
def tsuneto(kap):
    """f(kappa) for omega + i0 (Delta = 1); complex."""
    if abs(kap) < 1e-6:
        return -1.0 - 2 * kap / 3 - 8 * kap * kap / 15 + 0j
    if kap == 1.0:  # integrable inverse-square-root point, met only at a quadrature endpoint
        kap = 1.0 + 1e-15
    if kap < 0:
        a = -kap
        return -np.arcsinh(np.sqrt(a)) / np.sqrt(a * (1 + a)) + 0j
    if kap < 1:
        return -np.arcsin(np.sqrt(kap)) / np.sqrt(kap * (1 - kap)) + 0j
    return (np.arccosh(np.sqrt(kap)) - 0.5j * PI) / np.sqrt(kap * (kap - 1))


def _p33_integrand(s, y):
    u2 = y * y - s * s
    kap = u2 / 4
    if abs(kap) < 1e-6:
        return -1.0 + y * y * (-1.0 / 6 - 2 * kap / 15) + 0j
    return -1.0 + y * y * (1 + tsuneto(kap)) / u2


def _avg(fun, y, Q):
    """<X> = (1/Q) int_0^Q ds X(s); substitution s = s* -/+ t^2 at the inverse-square-root point s* = sqrt(y^2-4)."""
    sst = np.sqrt(y * y - 4) if y > 2 else None
    pieces = []
    if sst is not None and sst < Q:
        pieces.append(("in", sst))
        pieces.append(("out", sst))
    else:
        pieces.append(("plain", None))
    tot = 0j
    for kind, ss in pieces:
        for part in (np.real, np.imag):
            if kind == "in":
                f = lambda t: part(fun(ss - t * t, y)) * 2 * t
                a, b = 0.0, np.sqrt(ss)
            elif kind == "out":
                f = lambda t: part(fun(ss + t * t, y)) * 2 * t
                a, b = 0.0, np.sqrt(Q - ss)
            else:
                f = lambda s: part(fun(s, y))
                a, b = 0.0, Q
            br = []
            if kind == "out" and y < Q and y > ss:
                br = [np.sqrt(y - ss)]
            if kind == "plain" and y < Q:
                br = [y]
            val, _ = integrate.quad(f, a, b, points=br or None, limit=400, epsabs=1e-13, epsrel=1e-11)
            tot += val if part is np.real else 1j * val
    return tot / Q


def responses(y, Q):
    """Return dict with P33 (bare), Pc (conserving), Pn (normal) and derived ratios."""
    P33 = _avg(_p33_integrand, y, Q)
    fav = _avg(lambda s, yy: tsuneto((yy * yy - s * s) / 4), y, Q)
    u2f = _avg(lambda s, yy: (yy * yy - s * s) * tsuneto((yy * yy - s * s) / 4), y, Q)
    Pc = P33 - y * y * fav**2 / u2f
    Pn = P_nor(y / Q)
    g = g_I(np.array([y]))[0] if y > 2 else 0.0

    def L(P):
        return (1 / P).imag

    out = dict(P33=P33, Pc=Pc, Pn=Pn, g=g)
    out["Lbare_nor"] = L(P33) / L(Pn)
    out["Lcons_nor"] = L(Pc) / L(Pn)
    out["v"] = (Pc - P33).imag / P33.imag if P33.imag != 0 else np.nan
    out["ImRatio"] = P33.imag / Pn.imag if Pn.imag != 0 else np.nan
    out["absratio"] = abs(Pc) / abs(Pn)
    return out
