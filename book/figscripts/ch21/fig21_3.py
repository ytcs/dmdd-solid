"""Fig. 21.3 (fig:21-edge), worked example 21.3 (we:21-gapshift) and every number of Sect. 21.3 (log: fig21_3.log).

Model of the low-mass edge of a silicon electron-recoil limit (phonon-assisted onset, Sects. 13.1, 13.3, 13.9).
  Response: direction-averaged loss function C x^p above the onset E_th(q) = E_g + omega_TA(k_c - q) on the [100] valley axis,
     x = omega - E_th(q), p = 3 (free-pair transverse acoustic edge, eq:13.3-pon). TA branch from the book's PBE force constants
     (figscripts/ch05/si_ifc.py, Sect. 5.2) on a spline through 401 points. E_g = 1.17 eV, k_c = 0.85 (2 pi/a), a = 5.431 A
     (Sect. 3.3). This is the model of fig13_9.py (Sect. 13.9), whose onset is m0 = 0.33738 MeV.
  Rate: q^3 F_DM^2 int dx eta(v_min) C x^p with v_min = v_max - (x_max(q) - x)/q (Sect. 13.9); F_DM = 1 (heavy mediator) unless
     stated; light mediator F_DM = (q0/q)^2 as a check of the exponent only.
  Halo: isotropic galactic distribution f_k(u) of Lisanti et al., arXiv:1010.4300 Eq. (1),
         f_k(u) ~ [exp((v_esc^2 - u^2)/(k v0^2)) - 1]^k Theta(v_esc - u),
     k = 0 read as the sharp-cut Maxwellian of the book (Table 1.1, eq:1.2-fgal), k = 1 the King model (their Eq. (12)),
     k = 1.5-3.5 the range of their fits to simulated halos (their Sect. II, below Eq. (11), and Sect. III B).
     Same v0 = 238 km/s, v_esc = 544 km/s and v_E = 250.5 km/s for every k (Table 1.1), each f_k normalized.
     Lab-frame eta from the speed distribution of an isotropic f: for v_min > v_esc - v_E,
         eta(v_max - delta) = [2 pi/(v_E N_k)] int_0^delta dt (delta - t)(v_esc - t) f_k(v_esc - t),
     which for k = 0 is the integral above eq:1.3-edge. Tabulated by quadrature on a log grid of delta, log-log spline.
  Limit: sigma_lim(m) proportional to 1/R(m) for a fixed number of events and exposure (background-free, Sect. 1.5);
     only ratios are printed.
  Annual average: v_E(t) = 251.9 + 14.5 cos(2 pi (t - t_peak)/yr) km/s, which reproduces the extremes 266.4 and 237.4 km/s
     of Sect. 1.2; the year average of R over 400 equally spaced days; eta recomputed at each v_E.
  Zero-phonon edge coefficients: envelope theorem on eq:13.1-mZP at the joint minimum of Sect. 13.9
     (|q| = 1.33 keV, pair energy 1.355 eV, m = 0.407 MeV), with a rigid gap shift dE_min/dE_g = 1.
Run: python fig21_3.py  (numpy, scipy, matplotlib; a few minutes). Output: tex/figures/ch21/fig21_3.pdf and fig21_3.log.
"""
import os
import sys
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar, brentq
from scipy.special import beta as Beta
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch21", "fig21_3.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
LOG = open(os.path.join(HERE, "fig21_3.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


HBARC = 1973.269804          # eV A
CKM = 299792.458
A_SI = 5.431
G1 = 2 * np.pi * HBARC / A_SI
KC = 0.85 * G1
EG = 1.17
V0, VESC, VE = 238.0, 544.0, 250.5
Q0 = 3730.0                  # alpha m_e, eV (eq:1.3-q0), light-mediator check only
P = 3.0

# ---------------------------------------------------------------- TA branch along [100]
Qf = np.linspace(0.0, 1.0, 401)
w, _ = si_ifc.phonons(np.c_[Qf, 0 * Qf, 0 * Qf])
TA = CubicSpline(Qf * G1, w[:, 0] * 1e-3)


# ---------------------------------------------------------------- halo
def fk(u, k, vesc=VESC, v0=V0):
    u = np.asarray(u, float)
    if k == 0:
        val = np.exp(-u ** 2 / v0 ** 2)
    else:
        val = np.expm1((vesc ** 2 - u ** 2) / (k * v0 ** 2)) ** k
    return np.where(u < vesc, val, 0.0)


class Halo:
    """eta(v_max - delta) for the galactic f_k, lab speed v_E, escape speed v_esc (km/s); eta in natural units."""

    def __init__(self, k, vE=VE, vesc=VESC, v0=V0):
        self.k, self.vE, self.vesc, self.v0 = k, vE, vesc, v0
        self.vmax = (vesc + vE) / CKM
        N, _ = quad(lambda u: 4 * np.pi * u * u * fk(u, k, vesc, v0), 0, vesc, epsabs=0, epsrel=1e-12, limit=200)
        self.N = N
        self.fcut = None
        d = np.geomspace(1e-7, 300.0, 500)
        e = np.array([self._eta(x) for x in d])
        self.lnd, self.lne = np.log(d), np.log(e)
        self.spl = CubicSpline(self.lnd, self.lne)

    def _eta(self, delta):
        g = lambda t: (delta - t) * (self.vesc - t) * fk(self.vesc - t, self.k, self.vesc, self.v0)
        val, _ = quad(g, 0.0, delta, epsabs=0, epsrel=1e-11, limit=200)
        return 2 * np.pi / (self.vE * self.N) * val * CKM

    def eta(self, delta):
        """delta in km/s (array); zero for delta <= 0."""
        delta = np.asarray(delta, float)
        res = np.zeros_like(delta)
        ok = delta > 0
        dd = np.clip(delta[ok], 1e-7, 300.0)
        res[ok] = np.exp(self.spl(np.log(dd)))
        return res


# ---------------------------------------------------------------- rate model
def Eth(q, gap):
    return gap + TA(KC - q)


def xmax(q, m, gap, vmax):
    return q * vmax - q * q / (2 * m) - Eth(q, gap)


def onset(gap, vmax):
    def fm(m):
        r = minimize_scalar(lambda q: -xmax(q, m, gap, vmax), bounds=(0.3 * KC, 0.75 * KC), method="bounded",
                            options={"xatol": 1e-6})
        return -r.fun
    return brentq(fm, 2.9e5, 3.8e5, xtol=1e-9, rtol=1e-15)


GX, GW = np.polynomial.legendre.leggauss(80)


def rate(m, gap, halo, p=P, light=False):
    vmax = halo.vmax
    r = minimize_scalar(lambda q: -xmax(q, m, gap, vmax), bounds=(0.3 * KC, 0.75 * KC), method="bounded",
                        options={"xatol": 1e-7})
    qs, f0 = r.x, -r.fun
    if f0 <= 0:
        return 0.0
    h = np.sqrt(2 * m * f0)
    lo = brentq(lambda q: xmax(q, m, gap, vmax), qs - 3 * h, qs, xtol=1e-10)
    hi = brentq(lambda q: xmax(q, m, gap, vmax), qs, qs + 3 * h, xtol=1e-10)
    th = 0.5 * np.pi * GX
    c, d = 0.5 * (lo + hi), 0.5 * (hi - lo)
    q = c + d * np.sin(th)
    jac = d * np.cos(th) * 0.5 * np.pi
    fq = np.clip(xmax(q, m, gap, vmax), 0, None)
    xs = 0.5 * fq[:, None] * (GX[None, :] + 1)                     # (nq, nx)
    delta = (fq[:, None] - xs) / q[:, None] * CKM
    inner = 0.5 * fq * np.sum(GW[None, :] * halo.eta(delta) * xs ** p, axis=1)
    wq = q ** 3 * (Q0 / q) ** 4 if light else q ** 3
    return float(np.sum(GW * jac * wq * inner))


def local_exponent(m0, gap, halo, dm, **kw):
    R = np.array([rate(m0 + x, gap, halo, **kw) for x in dm])
    return R, np.gradient(np.log(R), np.log(dm))


# ================================================================ 1. halo edges
out("== halo edges (Lisanti et al. f_k; v0 = 238, v_esc = 544, v_E = 250.5 km/s)")
halos = {k: Halo(k) for k in (0, 1, 1.5, 2.5, 3.5)}
VMAX = halos[0].vmax
out("v_max = %.1f km/s = %.4e" % (VMAX * CKM, VMAX))
for k, H in halos.items():
    d1, d2 = 0.1, 1.0
    s = (np.log(H._eta(d2)) - np.log(H._eta(d1))) / np.log(d2 / d1)
    # lens formula: eta ~ 2 pi f_k' v_esc delta^(k+2) / (v_E (k+1)(k+2)) with f ~ f_k' y^k, y = v_esc - u
    y = 1e-4
    fprime = fk(VESC - y, k) / y ** k / H.N
    lens = 2 * np.pi * fprime * VESC * d1 ** (k + 2) / (VE * (k + 1) * (k + 2)) * CKM
    out("k = %.1f: local power of eta at delta = 0.1-1 km/s: %.3f (k + 2 = %.1f); eta(0.1 km/s)/lens formula = %.4f"
        % (k, s, k + 2, H._eta(d1) / lens))
H0 = halos[0]
Aeta = np.pi * VESC * np.exp(-VESC ** 2 / V0 ** 2) / (VE * H0.N)   # eq:1.3-edge, per (km/s)^2... in 1/(km/s)^3
out("k = 0 check against eq:1.3-edge: eta(34.5)/[A_eta delta^2 (1 + delta/173)] = %.4f"
    % (H0._eta(34.5) / (Aeta * 34.5 ** 2 * (1 + 34.5 / 173.0) * CKM)))
for k in (1, 2.5):
    out("k = %.1f: linear range of the bracket, y << k v0^2/(2 v_esc) = %.0f km/s" % (k, k * V0 ** 2 / (2 * VESC)))

# fraction of halo particles with lab speed above v_max - dd: (2 pi/(v_E N)) int_0^dd dt (v_esc - t) f(v_esc - t) [v_max (dd - t) - (dd^2 - t^2)/2]
for dd in (5.0, 12.0):
    for k in (0, 1, 2.5):
        H = halos[k]
        vm = VESC + VE
        g = lambda t: (VESC - t) * fk(VESC - t, k) * (vm * (dd - t) - 0.5 * (dd * dd - t * t))
        val, _ = quad(g, 0, dd, epsabs=0, epsrel=1e-10)
        out("fraction of particles with lab speed within %.0f km/s of v_max, k = %.1f: %.2e" % (dd, k, 2 * np.pi / (VE * H.N) * val))

# ================================================================ 2. edge exponents in the silicon model
out("\n== edge exponents, silicon phonon-assisted model (p_on = 3)")
m0 = onset(EG, VMAX)
out("onset m0 = %.5f MeV (fig13_9: 0.33738)" % (m0 / 1e6))
out("x*_max = v_max^2 dm/2 per 0.001 MeV: %.3f meV; dm at x*_max = 1.3 meV: %.2e MeV"
    % (0.5 * VMAX ** 2 * 1e3 * 1e3, 2 * 1.3e-3 / VMAX ** 2 / 1e6))
out("delta_v0 = (v_max/2) dm/m0 at dm = 0.001, 0.01 MeV: %.2f, %.1f km/s"
    % (VMAX * CKM / 2 * 1e3 / m0, VMAX * CKM / 2 * 1e4 / m0))
dm = np.geomspace(1e-6, 2e-2, 22) * 1e6
LOC = {}
for k in (0, 1, 2.5):
    R, loc = local_exponent(m0, EG, halos[k], dm)
    LOC[k] = loc
    out("k = %.1f, asymptote p + k + 7/2 = %.2f" % (k, P + k + 3.5))
    for x, l in zip(dm[::3], loc[::3]):
        out("   m - m0 = %.1e MeV   local exponent %.3f" % (x / 1e6, l))
_, locL = local_exponent(m0, EG, H0, dm, light=True)
out("light mediator, k = 0: local exponent at 1e-6, 1e-4, 1e-2 MeV: %.3f, %.3f, %.3f"
    % (locL[0], np.interp(np.log(1e2), np.log(dm), locL), np.interp(np.log(1e4), np.log(dm), locL)))

# ---- coefficient of the asymptote (beta functions), k = 0, heavy mediator: check that R/(dm)^n -> const
n0 = P + 3.5
Rsmall = np.array([rate(m0 + x, EG, H0) for x in (1e0, 1e1)])
out("R(dm)/dm^n at dm = 1, 10 eV: ratio %.4f (1 for a pure power)" % ((Rsmall[1] / 10 ** n0) / Rsmall[0]))

out("limit ratio sigma_lim(k)/sigma_lim(standard halo), same v0, v_esc, v_E, heavy mediator:")
for x in (1e3, 3e3, 1e4, 2e4):
    Rb = rate(m0 + x, EG, H0)
    out("   m0 + %.3f MeV: k = 1: %.3g   k = 2.5: %.3g" % (x / 1e6, Rb / rate(m0 + x, EG, halos[1]), Rb / rate(m0 + x, EG, halos[2.5])))

R35 = rate(0.35e6, EG, H0)
for x in (1e2, 1e3, 3e3, 5e3, 1e4):
    out("sigma_lim(m0 + %.4f MeV)/sigma_lim(0.35 MeV), standard halo: %.3g" % (x / 1e6, R35 / rate(m0 + x, EG, H0)))
out("delta_on = (v_max/2) dm/m0 at dm = 0.003 MeV: %.2f km/s" % (VMAX * CKM / 2 * 3e3 / m0))

out("exposure x 10 at fixed sigma: distance to the edge x 10^(-1/n): n = 6.5: %.4f, n = 7.5: %.4f" % (10 ** (-1 / 6.5), 10 ** (-1 / 7.5)))

# ================================================================ 3. gap shift and halo degeneracy (WE 21.3)
out("\n== worked example: gap +10 meV")
dE = 0.010
m0g = onset(EG + dE, VMAX)
out("m0(E_g + 10 meV) = %.5f MeV, shift %.5f MeV = %.3f %% (2 dE/v_max^2 = %.5f MeV)"
    % (m0g / 1e6, (m0g - m0) / 1e6, 100 * (m0g - m0) / m0, 2 * dE / VMAX ** 2 / 1e6))
Eon = 0.5 * m0 * VMAX ** 2
out("onset energy E_on = m0 v_max^2/2 = %.4f eV; equivalent v_max shift -(v_max/2) dE/E_on = %.2f km/s"
    % (Eon, -0.5 * VMAX * CKM * dE / Eon))


dvesc = brentq(lambda d: onset(EG, (VESC + d + VE) / CKM) - m0g, -8, 0, xtol=1e-6)
Hv = Halo(0, vesc=VESC + dvesc)
m0v = onset(EG, Hv.vmax)
out("escape speed that gives the same edge: v_esc = %.2f km/s (shift %.2f km/s); m0 = %.5f MeV" % (VESC + dvesc, dvesc, m0v / 1e6))
for x in (3e3, 5e3, 1e4, 2e4):
    Rb = rate(m0 + x, EG, H0)
    Rg = rate(m0 + x, EG + dE, H0)
    Rv = rate(m0 + x, EG, Hv)
    out("m = m0 + %.3f MeV: R(gap+10)/R = %.4f (limit x %.3g); power law (1 - dm_g/dm)^6.5 = %.4f; R(v_esc shifted)/R(gap+10) = %.4f"
        % (x / 1e6, Rg / Rb, Rb / Rg, (1 - (m0g - m0) / x) ** 6.5, Rv / Rg))
for x in (1e2, 1e3):
    out("   amplitude ratio R(v_esc shifted)/R(gap+10) at %.4f MeV above the common edge: %.4f"
        % (x / 1e6, rate(m0g + x, EG, Hv) / rate(m0g + x, EG + dE, H0)))
# amplitude at a fixed edge: R ~ A v_max^(2(p+k)+8) dm^(p+k+7/2) (heavy mediator; light: v_max^(2(p+k)+4)),
# A = pi v_esc e^{-v_esc^2/v0^2}/(v_E N_esc) for k = 0 (eq:1.3-edge)
eps = 1e-3
dlnN = (np.log(Halo(0, vesc=VESC + eps).N) - np.log(Halo(0, vesc=VESC - eps).N)) / (2 * eps)
dlnA = -2 * VESC / V0 ** 2 + 1 / VESC - dlnN
out("d ln A_eta/d v_esc = -2 v_esc/v0^2 + 1/v_esc - d ln N_esc/d v_esc = %.4f + %.5f - %.5f = %.4f per km/s"
    % (-2 * VESC / V0 ** 2, 1 / VESC, dlnN, dlnA))
out("(2 p_on + 8)/v_max = %.4f, (2 p_on + 4)/v_max = %.4f per km/s" % ((2 * P + 8) / (VMAX * CKM), (2 * P + 4) / (VMAX * CKM)))
out("predicted amplitude ratio (v_esc shifted)/(gap shifted): heavy %.4f, light %.4f"
    % (np.exp((dlnA + (2 * P + 8) / (VMAX * CKM)) * dvesc), np.exp((dlnA + (2 * P + 4) / (VMAX * CKM)) * dvesc)))
out("computed, light mediator, 0.001 MeV above the common edge: %.4f"
    % (rate(m0g + 1e3, EG, Hv, light=True) / rate(m0g + 1e3, EG + dE, H0, light=True)))
dlnNv0 = (np.log(Halo(0, v0=V0 + eps).N) - np.log(Halo(0, v0=V0 - eps).N)) / (2 * eps)
out("d ln A_eta/d v0 = 2 v_esc^2/v0^3 - d ln N_esc/d v0 = %.4f - %.4f = %.4f per km/s; v0 +/- 6 km/s: x %.3f / %.3f"
    % (2 * VESC ** 2 / V0 ** 3, dlnNv0, 2 * VESC ** 2 / V0 ** 3 - dlnNv0,
       np.exp(6 * (2 * VESC ** 2 / V0 ** 3 - dlnNv0)), np.exp(-6 * (2 * VESC ** 2 / V0 ** 3 - dlnNv0))))
Hv0 = Halo(0, v0=V0 + 6)
out("computed: R(v0 + 6)/R(v0) at 0.001 MeV above the edge: %.4f" % (rate(m0 + 1e3, EG, Hv0) / rate(m0 + 1e3, EG, H0)))
# v_esc uncertainty 25 km/s for comparison
out("v_esc - 25 km/s: v_max %.1f km/s, m0 shift %.2f %%" % (VESC - 25 + VE, 100 * ((VMAX / ((VESC - 25 + VE) / CKM)) ** 2 - 1)))
dE_eq = 0.5 * m0 * ((VESC + VE) ** 2 - (VESC - 25 + VE) ** 2) / CKM ** 2
out("   equivalent gap shift: %.1f meV" % (dE_eq * 1e3))
for dv in (-25.0, 25.0):
    r = (VMAX / ((VESC + dv + VE) / CKM)) ** 2
    out("v_esc %+.0f km/s: edge shift %+.2f %%; onset-energy error with the same edge shift E_on[(v_max/v_max')^2 - 1] = %+.1f meV"
        % (dv, 100 * (r - 1), 1e3 * Eon * (r - 1)))
out("v_E annual 237.4-266.4 km/s: m0 moves %.2f %% / %.2f %%"
    % (100 * ((VMAX / ((VESC + 266.4) / CKM)) ** 2 - 1), 100 * ((VMAX / ((VESC + 237.4) / CKM)) ** 2 - 1)))

# ================================================================ 4. zero-phonon edge coefficients (Sect. 13.9 numbers)
out("\n== zero-phonon edge sensitivities (envelope theorem, eq:13.1-mZP)")
qz, Ez, EGz = 1330.0, 1.355, 1.170
den = qz * VMAX - Ez
mz = qz ** 2 / (2 * den)
out("q v_max = %.4f eV, den = q v_max - E = %.4f eV, m = %.4f MeV" % (qz * VMAX, den, mz / 1e6))
out("d ln m/d ln E_g = E_g/den = %.3f; d ln m/d ln v_max = -q v_max/den = %.3f; ratio %.2f (phonon-assisted: 1, -2, ratio 2)"
    % (EGz / den, -qz * VMAX / den, qz * VMAX / EGz))
out("10 meV gap shift moves the zero-phonon edge by %.5f MeV (%.2f %%)" % (mz * 0.010 / den / 1e6, 100 * 0.010 / den))
dzh = mz * (qz * VMAX / den) * (-dvesc / (VMAX * CKM))
out("escape speed %.2f km/s (WE): zero-phonon edge moves %.5f MeV (%.3f %%); phonon-assisted %.5f MeV"
    % (dvesc, dzh / 1e6, 100 * dzh / mz, (m0g - m0) / 1e6))
out("change of the distance between the two edges: gap +10 meV %.5f MeV; escape-speed shift %.5f MeV"
    % ((mz * 0.010 / den - (m0g - m0)) / 1e6, (dzh - (m0g - m0)) / 1e6))
out("0.5 %% of v_max = %.2f km/s; v_esc uncertainty / WE shift = %.1f" % (0.005 * VMAX * CKM, 25 / -dvesc))
out("1 %% in v_max moves it by %.2f %% (phonon-assisted %.2f %%)" % (100 * qz * VMAX / den * 0.01, 2.0))

out("x*_max per 0.001 MeV above the zero-phonon edge, q*^2/(2 m^2) dm: %.2f meV; dm at x* = 14.7 meV (exciton binding): %.4f MeV; at 49 meV (cones touch): %.4f MeV"
    % (qz ** 2 / (2 * mz ** 2) * 1e3 * 1e3, 0.0147 / (qz ** 2 / (2 * mz ** 2)) / 1e6, 0.049 / (qz ** 2 / (2 * mz ** 2)) / 1e6))
out("phonon-assisted: dm at x* = 14.7 meV: %.4f MeV" % (0.0147 / (0.5 * VMAX ** 2) / 1e6))

# ---- free nuclear recoil with a sharp energy threshold: corner contact, line response -> exponent 3 + k_tail
out("\n== free nuclear recoil (Si nucleus, threshold 10 eV, heavy mediator, nuclear form factor 1)")
MN = 28.0855 * 931.494e6
ETH = 10.0


def rate_nr(m, halo):
    mu = m * MN / (m + MN)
    qth = np.sqrt(2 * MN * ETH)
    qmx = 2 * mu * halo.vmax
    if qmx <= qth:
        return 0.0
    qq = qth + 0.5 * (qmx - qth) * (GX + 1)
    dd = (halo.vmax - qq / (2 * mu)) * CKM
    return float(0.5 * (qmx - qth) * np.sum(GW * qq * halo.eta(dd)) / mu ** 2)


mnr = brentq(lambda m: 2 * (m * MN / (m + MN)) * VMAX - np.sqrt(2 * MN * ETH), 1e6, 1e9)
out("edge mass %.4f MeV" % (mnr / 1e6))
for k in (0, 1):
    dmn = np.geomspace(1e-5, 1e-2, 7) * mnr
    Rn = np.array([rate_nr(mnr + x, halos[k]) for x in dmn])
    ln = np.gradient(np.log(Rn), np.log(dmn))
    out("k = %d: local exponent at dm/m = 1e-5, 1e-3, 1e-2: %.3f, %.3f, %.3f (3 + k = %d)" % (k, ln[0], ln[4], ln[6], 3 + k))

# ================================================================ 5. annual average
out("\n== year-averaged rate")
# t in units of a year from the June maximum; by symmetry t in [0, 1/2]; nodes dense near June: t = u^2/2, dt = u du
NU = 240
uu = (np.arange(NU) + 0.5) / NU
tt = 0.5 * uu ** 2
wt = uu / NU                      # dt weights; sum = 1/2
vEt = 251.9 + 14.5 * np.cos(2 * np.pi * tt)
vE_J = 251.9 + 14.5
m0J = onset(EG, (VESC + vE_J) / CKM)
out("June v_E = %.2f km/s: m0^June = %.5f MeV (%.2f %% below m0)" % (vE_J, m0J / 1e6, 100 * (1 - m0J / m0)))
Hts = [Halo(0, vE=v) for v in vEt]
dmJ = np.geomspace(1e-5, 3e-2, 14) * 1e6


def Ryear(m):
    return 2 * np.sum([w_ * rate(m, EG, H) for w_, H in zip(wt, Hts)])


RY = np.array([Ryear(m0J + x) for x in dmJ])
locY = np.gradient(np.log(RY), np.log(dmJ))
out("asymptote p + k + 4 = %.1f" % (P + 4.0))
for x, l in zip(dmJ, locY):
    out("   m - m0^June = %.1e MeV   local exponent of the year average %.3f" % (x / 1e6, l))
for m in (m0 + 3e3, m0 + 1e4, m0 + 2e4):
    out("year average / reference-speed rate at m = %.5f MeV: %.3g" % (m / 1e6, Ryear(m) / max(rate(m, EG, H0), 1e-300)))

# ================================================================ 6. figure
plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.6, 3.3), gridspec_kw={"wspace": 0.34, "width_ratios": [1.25, 1]})

mm = np.linspace(0.3225e6, 0.3565e6, 170)
mref = 0.350e6
Rref = rate(mref, EG, H0)
curves = [
    ("standard halo", lambda m: rate(m, EG, H0), dict(color="k", lw=1.3)),
    (r"$E_{\mathrm{g}} + 10$ meV", lambda m: rate(m, EG + dE, H0), dict(color="C3", lw=1.1)),
    (r"$v_{\mathrm{esc}} - %.1f$ km/s" % (-dvesc), lambda m: rate(m, EG, Hv), dict(color="C0", lw=1.0, ls="--")),
    (r"King, $k_{\mathrm{tail}} = 1$", lambda m: rate(m, EG, halos[1]), dict(color="C2", lw=1.1, ls="-.")),
    ("year average", Ryear, dict(color="C1", lw=1.1, ls=":")),
]
for lab, fn, sty in curves:
    mmm = mm if lab != "year average" else mm[::4]
    R = np.array([fn(m) for m in mmm])
    ok = R > 0
    ax.semilogy(mmm[ok] / 1e6, Rref / R[ok], label=lab, **sty)
ax.axvline(m0 / 1e6, color="k", lw=0.5)
ax.axvline(m0J / 1e6, color="C1", lw=0.5)
ax.set_xlim(0.3225, 0.3565)
ax.set_ylim(1e-2, 1e8)
ax.set_xlabel(r"$m_\chi$ (MeV)")
ax.set_ylabel(r"$\bar\sigma_e^{\mathrm{lim}}(m_\chi)/\bar\sigma_e^{\mathrm{lim}}(0.35\,\mathrm{MeV})$")
# legend above the panel: the curves of (a) diverge through every corner of the plot area
ax.legend(fontsize=6.8, frameon=False, loc="lower left", bbox_to_anchor=(-0.02, 1.07), ncol=3, columnspacing=1.0, handlelength=1.8)
ax.set_title("(a)", loc="left", fontsize=8)

cols = {0: "k", 1: "C2", 2.5: "C4"}
for k, loc in LOC.items():
    bx.semilogx(dm / 1e6, loc, color=cols[k], lw=1.2, label=r"$k_{\mathrm{tail}} = %g$" % k)
    bx.axhline(P + k + 3.5, color=cols[k], lw=0.6, ls=":")
bx.semilogx(dmJ / 1e6, locY, color="C1", lw=1.1, ls=":", label="year average")
bx.axhline(P + 4.0, color="C1", lw=0.6, ls=":")
bx.axvline(2 * 1.3e-3 / VMAX ** 2 / 1e6, color="0.5", lw=0.6, ls="--")
bx.set_xlabel(r"$m_\chi - m_{\mathrm{edge}}$ (MeV)")
bx.set_ylabel(r"$\mathrm{d}\ln\mathcal{R}/\mathrm{d}\ln(m_\chi - m_{\mathrm{edge}})$")
bx.set_ylim(6.0, 9.5)
bx.legend(fontsize=6.8, frameon=False, loc="center left", bbox_to_anchor=(0.0, 0.62))
bx.set_title("(b)", loc="left", fontsize=8)

fig.subplots_adjust(left=0.10, right=0.98, bottom=0.14, top=0.80)
fig.savefig(OUT)
out("wrote", OUT)
