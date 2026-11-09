"""Sub-gap structure of P~ and of L: exact real-axis evaluation of the closed form (verified against direct quadrature in t1.py).
For y < 2 everything is real.  Herglotz: eps = 1 - K P~, K = k_TF^2/q^2, rises monotonically in y^2 between poles of P~."""
import numpy as np, core as c
from scipy.optimize import brentq
def nodes(y, Q, n=14):
    d = abs(4 - y * y) ** 0.5 if y != 2 else 0.0
    b = [0.0, Q]
    t = max(d, 1e-16) / 64
    while t < Q:
        b.append(t); t *= 1.5
    if y > 2:
        ss = np.sqrt(y * y - 4); b.append(ss)
        t = 1e-14 * (1 + ss)
        while t < ss:
            b += [ss - t, ss + t]; t *= 1.5
    if y < Q: b.append(y)
    b = np.array(sorted({x for x in b if 0 <= x <= Q}))
    s, w = c.gl_panels(b, n)
    return s, w / Q
def fr(k):
    """f on the real axis, retarded."""
    k = np.asarray(k, float); out = np.empty(k.shape, complex)
    sm = np.abs(k) < 1e-4
    out[sm] = -(1 + 2 * k[sm] / 3 + 8 * k[sm] ** 2 / 15)
    m = (k < 0) & ~sm; a = -k[m]; out[m] = -np.arcsinh(np.sqrt(a)) / np.sqrt(a * (1 + a))
    m = (k > 0) & (k < 1) & ~sm; a = k[m]; out[m] = -np.arcsin(np.sqrt(a)) / np.sqrt(a * (1 - a))
    m = k >= 1; a = np.maximum(k[m], 1 + 1e-16); out[m] = (np.arccosh(np.sqrt(a)) - 0.5j * np.pi) / np.sqrt(a * (a - 1))
    return out
def avg(y, Q, n=14):
    s, w = nodes(y, Q, n)
    u2 = y * y - s * s; k = u2 / 4; f = fr(k)
    mid = np.abs(u2) < 1e-6                                # removable point of (s^2 + y^2 f)/u^2
    t = np.where(mid, 0, (s * s + y * y * f) / np.where(mid, 1, u2))
    t = np.where(mid, -1 - y * y / 4 * (2 / 3.0), t)
    return w @ t, w @ f, w @ (u2 * f)
def Pt(y, Q, n=14):
    p, F, UF = avg(y, Q, n)
    return p, p - y * y * F * F / UF, F, UF
def wab(Q):
    g = lambda t: avg(2 - np.exp(t), Q)[2].real
    lo, hi = np.log(1e-300), np.log(2 - 1e-9)
    return 2 - np.exp(brentq(g, np.log(1e-250), hi, xtol=1e-12)) if g(np.log(1e-250)) * g(hi) < 0 else None

def avg_d(d, Q, n=14):
    """Same as avg for y = 2 - d, 0 < d, with 1 - kappa carried exactly so d may be 1e-300."""
    y = 2 - d
    r = np.sqrt(d * (4 - d))
    b = [0.0, Q]
    t = r / 64
    while t < Q:
        b.append(t); t *= 1.6
    b.append(y)
    b = np.array(sorted({x for x in b if 0 <= x <= Q}))
    s, w = c.gl_panels(b, n); w = w / Q
    om = (r * r + s * s) / 4; k = 1 - om
    u2 = 4 * k
    f = np.empty(s.shape)
    m = k > 1e-4; f[m] = -np.arccos(np.sqrt(om[m])) / np.sqrt(k[m] * om[m])
    m = k < -1e-4; a = -k[m]; f[m] = -np.arcsinh(np.sqrt(a)) / np.sqrt(a * (1 + a))
    m = np.abs(k) <= 1e-4; f[m] = -(1 + 2 * k[m] / 3 + 8 * k[m] ** 2 / 15)
    m = np.abs(k) > 1e-4
    t = np.empty(s.shape); t[m] = (s[m] ** 2 + y * y * f[m]) / u2[m]; t[~m] = -1 - y * y / 4 * (2 / 3.0 + 8 * k[~m] / 15)
    return w @ t, w @ f, w @ (u2 * f)
def Pt_d(d, Q, n=14):
    p, F, UF = avg_d(d, Q, n); y = 2 - d
    return p, p - y * y * F * F / UF, F, UF

def avg_up(y, Q, n=16):
    """y > 2 on the real axis, retarded.  s = ss -+ t^2 removes both inverse-sqrt edges; kappa - 1 carried as (ss - s)(ss + s)/4."""
    d = y - 2
    ss = np.sqrt(d * (y + 2))
    S = []; Wt = []; KM = []
    def seg(sign, tmax):
        b = [0.0, tmax]; t = tmax
        while t > 1e-3 * min(tmax, 1):
            t /= 2; b.append(t)
        if sign > 0:
            t = np.sqrt(ss) if ss < 1 else 1.0
            for extra in (np.sqrt(ss), np.sqrt(max(y - ss, 0)) if y > ss else 0.0, 1.0):
                if 0 < extra < tmax: b.append(extra)
            t = 1.0
            while t < tmax:
                b.append(t); t *= 1.3
        tt, w = c.gl_panels(np.array(sorted(set(b))), n)
        s = ss + sign * tt ** 2
        return s, w * 2 * tt, -sign * tt * tt * (2 * ss + sign * tt ** 2) / 4    # kappa - 1 = (ss^2 - s^2)/4
    top = min(ss, Q)
    if Q >= ss:
        s1, w1, k1 = seg(-1, np.sqrt(ss)); s2, w2, k2 = seg(1, np.sqrt(Q - ss)) if Q > ss else (np.zeros(0),) * 3
        s = np.r_[s1, s2]; w = np.r_[w1, w2] / Q; km = np.r_[k1, k2]
    else:
        tA = np.sqrt(ss); tB = np.sqrt(ss - Q)
        b = np.linspace(tB, tA, 40); tt, ww = c.gl_panels(b, n)
        s = ss - tt ** 2; w = ww * 2 * tt / Q; km = tt * tt * (2 * ss - tt ** 2) / 4
    k = 1 + km; u2 = 4 * k
    f = np.empty(s.shape, complex)
    m = km > 0; a = k[m]; f[m] = (np.arcsinh(np.sqrt(km[m])) - 0.5j * np.pi) / np.sqrt(a * km[m])
    m = (km <= 0) & (k > 1e-4); om = -km[m]; f[m] = -np.arccos(np.sqrt(om)) / np.sqrt(k[m] * om)
    m = k < -1e-4; a = -k[m]; f[m] = -np.arcsinh(np.sqrt(a)) / np.sqrt(a * (1 + a))
    m = np.abs(k) <= 1e-4; f[m] = -(1 + 2 * k[m] / 3 + 8 * k[m] ** 2 / 15)
    mm = np.abs(k) > 1e-4
    t = np.empty(s.shape, complex); t[mm] = (s[mm] ** 2 + y * y * f[mm]) / u2[mm]; t[~mm] = -1 - y * y / 4 * (2 / 3.0 + 8 * k[~mm] / 15)
    return w @ t, w @ f, w @ (u2 * f)
def Pup(y, Q, n=16):
    p, F, UF = avg_up(y, Q, n)
    return p, p - y * y * F * F / UF, F, UF
def Pn(y, Q):
    x = y / Q
    return -1 + 0.5 * x * np.log(abs((x + 1) / (x - 1))) + (-0.5j * np.pi * x if x < 1 else 0)
