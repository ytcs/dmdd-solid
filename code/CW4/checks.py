#!/usr/bin/env python3
"""R16 / CW4 checks (returns/R16/CW4.md, as amended by returns/R16/CW4-errata.md). Cited CW4-Kn.
Run: python3 checks.py   (< 1 min; numpy/scipy/sympy only). Each check prints PASS/FAIL; exit status non-zero on any FAIL.
Errata version (ERR-CW4, 2026-11-01): tolerances tightened to the tabulated values; circular checks K1a, K6 (dimensions), K11, K14
replaced by non-circular ones; K3b, K7c, K15-K18 added for the VER-CW4 corrections. Labels as in CW4-errata.md section D."""
import sys, time, pathlib, itertools, numpy as np, sympy as sp
from scipy import integrate
from scipy.special import ellipk, ellipe, erf, k0 as K0, i0 as I0
from scipy.optimize import brentq

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[2]          # campaign/paer
RES = []
def chk(name, ok, info=""):
    RES.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""))

# ---------- shared: case-I function (WP4-v3 [4.2]) ----------
def gI(y):
    k = (y - 2) / (y + 2)
    return (1 + 2 / y) * ellipe(k * k) - 4 * ellipk(k * k) / (y + 2)

# ======================= K1: Nambu second order for the Holstein process (LE-108) =======================
# (a) [errata: non-circular] Fock space of the pair (k up, -k dn), Jordan-Wigner. j(q=0) = v (n1 - n2) (v_{-k} = -v_k) commutes with
#     H_BCS = xi (n1 + n2) + D (c1+ c2+ + c2 c1); control: the density n1 + n2 does NOT commute (so the test is not vacuous).
a1 = np.array([[0, 1], [0, 0.]]); Zs = np.diag([1, -1.]); I2 = np.eye(2)
c1, c2 = np.kron(a1, I2), np.kron(Zs, a1)
n1, n2 = c1.T @ c1, c2.T @ c2
xi0, D0, v0_ = 0.7, 0.4, 1.3
Hb = xi0 * (n1 + n2) + D0 * (c1.T @ c2.T + c2 @ c1)
jq = v0_ * (n1 - n2); dens = n1 + n2
comm = lambda A, B: A @ B - B @ A
nambu_ok = np.allclose(n1 + c2 @ c2.T, n1 + np.eye(4) - n2)          # Psi^+ tau0 Psi = n1 + 1 - n2
chk("K1a [j(q=0), H_BCS] = 0 in Fock space; control [n1+n2, H_BCS] != 0; Psi^+ tau0 Psi = n1 - n2 + 1",
    np.abs(comm(jq, Hb)).max() < 1e-14 and np.abs(comm(dens, Hb)).max() > 0.1 and nambu_ok)
xi, xp, D, vk = sp.symbols('xi xip Delta v_k', positive=True)
Ek, Ekp = sp.sqrt(xi**2 + D**2), sp.sqrt(xp**2 + D**2)
t1 = sp.Matrix([[0, 1], [1, 0]]); t3 = sp.Matrix([[1, 0], [0, -1]]); t2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); t0 = sp.eye(2)
u = sp.sqrt((1 + xi / Ek) / 2); v = sp.sqrt((1 - xi / Ek) / 2)
up = sp.sqrt((1 + xp / Ekp) / 2); vp = sp.sqrt((1 - xp / Ekp) / 2)
plus, minus = sp.Matrix([u, v]), sp.Matrix([-v, u]); plusp = sp.Matrix([up, vp])
M = {i: (plusp.T * t * minus)[0] for i, t in ((0, t0), (1, t1), (2, t2), (3, t3))}
qp_cur = sp.simplify((plus.T * t0 * plus)[0])
chk("K1b QP carries v_k(u^2+v^2) = v_k; tau_0 pair creation at q=0 vanishes",
    sp.simplify(qp_cur - 1) == 0 and sp.simplify(M[0].subs(xp, xi)) == 0)
C3 = sp.expand(M[3]**2); target = sp.Rational(1, 2) * (1 - (xi * xp - D**2) / (Ek * Ekp))
C2 = sp.expand(M[2] * sp.conjugate(M[2])); t22 = sp.Rational(1, 2) * (1 + (xi * xp + D**2) / (Ek * Ekp))
pts = [(0.3, -1.2), (2.0, 0.7), (-0.4, -3.0), (5.0, 5.0), (-2.2, 0.1), (0.0, 0.0)]
num = [abs(float((C3 - target).subs({xi: a, xp: b, D: 1.0}))) for a, b in pts] + \
      [abs(complex((C2 - t22).subs({xi: a, xp: b, D: 1.0}))) for a, b in pts]
chk("K1c coherence: |tau3|^2 = (1-(xx'-D^2)/EE')/2 (case I), |tau2|^2 = (1+(xx'+D^2)/EE')/2 (6 points, 1e-13)", max(num) < 1e-13)
ok = True
for x in (2.05, 2.3, 3.0, 5.0, 12.0, 40.0):    # algebraic endpoint weight handles the 1/sqrt edges exactly
    g = lambda E: (E * (x - E) + 1) / np.sqrt((E + 1) * (x - E + 1))
    I = integrate.quad(g, 1, x - 1, weight='alg', wvar=(-0.5, -0.5), epsabs=1e-13, epsrel=1e-13)[0]
    ok &= abs(I / x - gI(x)) < 1e-10 and abs(gI(x) - ellipe(1 - 4 / x**2)) < 1e-12
chk("K1d xi-integrated case-I pair density = x gI = x E(1-4/y^2) (1604.06800 Eq. 17 integrand), 1e-10", ok)

# ======================= K2: resummed screening (LE-104) =======================
# (i) [errata] symbolic: (8.1) is L^BCS/L^nor computed directly from Im eps/|eps|^2 with eps^nor = R(1+i r), eps^BCS = R(1+d) + i g R r;
#     first-order reduction to [4.2'] = g(1 - 2d).
R_, r_, d_, g_, s_ = sp.symbols('R r d g s', positive=True)
Lof = lambda e: sp.im(e) / (sp.re(e)**2 + sp.im(e)**2)
ratio81 = sp.simplify(Lof(R_ * (1 + d_) + sp.I * g_ * R_ * r_) / Lof(R_ * (1 + sp.I * r_)))
f81 = g_ * (1 + r_**2) / ((1 + d_)**2 + g_**2 * r_**2)
first = sp.series(f81.subs(r_, 0).subs(d_, s_ * d_), s_, 0, 2).removeO().subs(s_, 1)
sym_ok = sp.simplify(ratio81 - f81) == 0 and sp.simplify(first - g_ * (1 - 2 * d_)) == 0
def f_I(yp): return np.where(yp > 2, gI(np.maximum(yp, 2.0000001)) - 1, -1.0)
def sBCS(y, Y=None):
    gg = lambda yp: yp**2 * f_I(yp)
    top = 1e4 if Y is None else Y
    hfun = lambda yp: (gg(yp) - gg(y)) / (yp**2 - y**2) if abs(yp - y) > 1e-9 else 0.0
    I1 = integrate.quad(hfun, 0, top, points=[2.0, y] if top > y else [2.0], limit=800)[0]
    I2 = gg(y) / (2 * y) * np.log(abs((top - y) / (top + y)))
    tail = integrate.quad(lambda yp: yp**2 * (gI(yp) - 1) / (yp**2 - y**2), 1e4, np.inf, limit=200)[0] if Y is None else 0.0
    return I1 + I2 + tail
r = 0.39  # v_max/v_F (Al)
ReLin = 1 - r / 2 * np.log((1 + r) / (1 - r))       # Re f_Lin at w/(q v_F) = r (WP4-v3 sec. 4.5)
tab_ref = {2.2: (4.01, 1.42, 0.33, 0.40), 2.5: (2.82, 0.88, 0.45, 0.54), 3: (2.03, 0.53, 0.58, 0.66),
           5: (1.05, 0.16, 0.80, 0.86), 10: (0.50, 0.04, 0.94, 0.96)}   # CW4 sec. 8 table: s_BCS, first order, (8.1) KK-inf, (8.1) cut
tab = []; ok = sym_ok
for y, (sref, fref, kref, cref) in tab_ref.items():
    s = sBCS(y); fo = 2 * r * s / y
    dl = r * s / y / ReLin; rr = np.pi / 2 * r / ReLin
    res = (1 + rr**2) / ((1 + dl)**2 + gI(y)**2 * rr**2)
    sc = sBCS(y, Y=y / r); dlc = r * sc / y / ReLin
    resc = (1 + rr**2) / ((1 + dlc)**2 + gI(y)**2 * rr**2)
    tab.append((y, float(round(s, 3)), float(round(fo, 3)), float(round(res, 3)), float(round(resc, 3))))
    ok &= abs(s - sref) < 0.006 and abs(fo - fref) < 0.006 and abs(res - kref) < 0.006 and abs(resc - cref) < 0.006
ok &= abs(ReLin - 0.839) < 5e-4 and abs(np.pi / 2 * r / ReLin - 0.730) < 5e-4 and abs(1 / ReLin - 1.191) < 1e-3
chk("K2 (8.1) = direct Im eps/|eps|^2 ratio (sympy) -> [4.2'] at 1st order; sec. 8 table to +-0.006; Re f_Lin(0.39) = 0.839, "
    "r = 0.730, 1/0.839 = 1.191 (IF-CW4-1: k_TF^2/q^2 is 19% above)", ok, str(tab))

# ======================= K3: 1D massive Dirac interband bubble (LE-113) =======================
def ImR1D(q, w, Dd=1.0, vv=1.0, g=1):
    E = lambda k: np.sqrt(vv * vv * k * k + Dd * Dd)
    F = lambda k: 0.5 * (1 - (vv * vv * k * (k + q) + Dd * Dd) / (E(k) * E(k + q)))
    f = lambda k: E(k) + E(k + q) - w
    kc = -q / 2; tot = 0.0
    if f(kc) >= 0: return 0.0
    for a, b in ((kc, kc + 50 * w / vv), (kc - 50 * w / vv, kc)):
        rt = brentq(f, a, b, xtol=1e-14)
        tot += F(rt) / abs(vv * vv * rt / E(rt) + vv * vv * (rt + q) / E(rt + q))
    return g / 2 * tot
ok = True
for (q, w, vv) in ((0.5, 2.5, 1.0), (2, 3, 1.0), (3.0, 2.6, 0.5), (0.3, 2.1, 2.0)):
    s = w * w - vv * vv * q * q
    ok &= abs(ImR1D(q, w, vv=vv) / (2 * vv * q * q / (s**1.5 * np.sqrt(s - 4))) - 1) < 1e-8
wt = integrate.quad(lambda t: 1 / (t**1.5 * np.sqrt(t - 1)), 1, np.inf, epsabs=1e-12)[0] / 2
chk("K3 1D massive Dirac: closed form (1e-8); massless limit weight g v q^2 delta(s) (1e-8)", ok and abs(wt - 1) < 1e-8)

# K3b [errata, V24]: the I0 K0 kernel is the CYLINDRICAL CHARGE SHELL: ring average of the 1D Coulomb transform 2K0(q|rho-rho'|) = 2 I0 K0.
ok = True
for qR in (0.05, 0.3, 1.0, 3.0):
    avg = integrate.quad(lambda ph: K0(2 * qR * abs(np.sin(ph / 2))), 0, 2 * np.pi, points=[np.pi], limit=400, epsabs=1e-12)[0] / (2 * np.pi)
    ok &= abs(avg / (I0(qR) * K0(qR)) - 1) < 1e-8
chk("K3b shell kernel: <K0(q|R-R'|)>_ring = I0(qR)K0(qR) (1e-8)", ok)

# ======================= K4: OPW and FSI sizes (LE-113) [E] =======================
# [errata, V5] deterministic Fibonacci sphere (2e4 final directions), q along z (orbital axis), x (in-plane) and 45 deg, full q x E_kin grid;
# compared to the independent VER-CW4 V5 rerun (random 2e4 directions) at 8 % (its Monte-Carlo noise), and the errata table at 0.005.
al, me = 1 / 137.035999, 511e3
zeta = 1.568 * al * me / 1e3
def Psi(p):
    p2 = (p**2).sum(-1); return 32 * np.pi * zeta * np.sqrt(zeta**5 / np.pi) * p[..., 2] / (p2 + zeta**2)**3
def Fel(q):
    qq = np.linalg.norm(q); ct = q[2] / qq
    j0 = integrate.quad(lambda r: (zeta**5 / np.pi) * r**4 * np.exp(-2 * zeta * r) * np.sinc(qq * r / np.pi) * 4 * np.pi / 3, 0, 60 / zeta, limit=200)[0]
    j2f = lambda r: (zeta**5 / np.pi) * r**4 * np.exp(-2 * zeta * r) * 4 * np.pi / 3 * (
        (3 / (qq * r)**3 - 1 / (qq * r)) * np.sin(qq * r) - 3 * np.cos(qq * r) / (qq * r)**2 if qq * r > 1e-3 else (qq * r)**2 / 15)
    j2 = integrate.quad(j2f, 0, 60 / zeta, limit=200)[0]
    return j0 - 2 * j2 * (1.5 * ct * ct - 0.5)
Nd = 20000; ii = np.arange(Nd) + 0.5
th = np.arccos(1 - 2 * ii / Nd); ph = np.pi * (1 + 5**0.5) * ii
dirs = np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], -1)
qdirs = (np.array([0, 0, 1.0]), np.array([1.0, 0, 0]), np.array([1.0, 0, 1.0]) / np.sqrt(2))
ver = {10: [(0.70, 1.20), (0.76, 2.98), (2.1, 67), (7, 274), (7.6, 508)],
       50: [(0.66, 0.96), (0.73, 1.00), (0.65, 0.91), (0.97, 1.49), (1.18, 4.25)],
       100: [(0.67, 0.97), (0.90, 1.11), (0.91, 0.98), (0.73, 0.93), (0.40, 0.92)]}
errt = {10: [(0.70, 1.22), (0.74, 3.02), (2.09, 67.4), (6.87, 275), (7.52, 509)],
        50: [(0.66, 0.96), (0.73, 1.00), (0.65, 0.91), (0.94, 1.51), (1.16, 4.28)],
        100: [(0.67, 0.97), (0.90, 1.11), (0.91, 0.98), (0.73, 0.93), (0.39, 0.92)]}
qs4 = (5.0, 7.5, 15.0, 25.0, 40.0)
ok_v, ok_e, out = True, True, {}
for Ekin in (10, 50, 100):
    kf = np.sqrt(2 * me * Ekin) / 1e3; row = []
    for j, qm in enumerate(qs4):
        rs = []
        for qd in qdirs:
            qv = qm * qd; m0 = Psi(kf * dirs - qv); m1 = m0 - Psi(kf * dirs) * Fel(qv)
            rs.append((m1**2).mean() / (m0**2).mean())
        lo, hi = min(rs), max(rs); row.append((float(round(lo, 3)), float(round(hi, 3))))
        ok_v &= abs(lo / ver[Ekin][j][0] - 1) < 0.08 and abs(hi / ver[Ekin][j][1] - 1) < 0.08
        ok_e &= abs(lo / errt[Ekin][j][0] - 1) < 0.005 + 0.005 / errt[Ekin][j][0] and abs(hi / errt[Ekin][j][1] - 1) < 0.005 + 0.005 / errt[Ekin][j][1]
    out[Ekin] = row
Ssom = []
for Ekin in (10, 50, 100):
    zS = al * me / np.sqrt(2 * me * Ekin); Ssom.append(2 * np.pi * zS / (1 - np.exp(-2 * np.pi * zS)))
ok_s = all(abs(a - b) < 0.05 for a, b in zip(Ssom, (7.33, 3.41, 2.57)))
chk("K4 OPW |M_OPW|^2/|M_PW|^2 min-max over q-direction: agrees with VER-CW4 V5 (8%) and errata table; Sommerfeld 7.33/3.41/2.57",
    ok_v and ok_e and ok_s, str(out))

# ======================= K5: 2212.04504 Eq. (12) misprint impact (LE-109), |eps| fixed [E] =======================
c = 299792.458; v0, vesc, vEr = 238 / c, 544 / c, 250.5 / c
Nesc = erf(vesc / v0) - 2 / np.sqrt(np.pi) * vesc / v0 * np.exp(-vesc**2 / v0**2)
def eta(vm):
    vm = np.asarray(vm, float); o = np.zeros_like(vm)
    a = vm < vesc - vEr; b = (vm >= vesc - vEr) & (vm < vesc + vEr)
    o[a] = (erf((vm[a] + vEr) / v0) - erf((vm[a] - vEr) / v0)) / (2 * vEr) - np.exp(-vesc**2 / v0**2) / (np.sqrt(np.pi) * v0)
    o[b] = (erf(vesc / v0) - erf((vm[b] - vEr) / v0)) / (2 * vEr) - np.exp(-vesc**2 / v0**2) * (vesc + vEr - vm[b]) / (2 * np.sqrt(np.pi) * v0 * vEr)
    return o / Nesc
astar = 23 / (al * me); EI = 0.045; mst = 0.3 * me
def Bgos(qt, kt, mis):
    numr = (3 * qt if mis else 3 * qt**2) + kt**2 + 1
    return numr * np.exp(-2 / kt * np.arctan2(2 * kt, qt**2 - kt**2 + 1)) / (((qt + kt)**2 + 1)**3 * ((qt - kt)**2 + 1)**3 * (1 - np.exp(-2 * np.pi / kt)))
def rate(mchi, light, mis):
    vmax = vesc + vEr; mu = mchi * me / (mchi + me); wmax = 0.5 * mu * vmax**2
    ws = np.linspace(EI * 1.0001, wmax, 160); res = []
    for w in ws:
        kt = np.sqrt(2 * mst * (w - EI)) * astar; rt = np.sqrt(max(0, 1 - 2 * w / (mchi * vmax**2)))
        qs = np.geomspace(mchi * vmax * (1 - rt) * 1.000001, mchi * vmax * (1 + rt) * 0.999999, 240)
        F2 = (al * me / qs)**4 if light else 1.0
        res.append(np.trapezoid(qs**3 * F2 * eta(w / qs + qs / (2 * mchi)) * Bgos(qs * astar, kt, mis), qs))
    return np.trapezoid(res, ws)
k5ref = {0.02: (1.47, 1.46), 0.1: (0.91, 1.24), 1.0: (0.59, 1.07), 10.0: (0.56, 1.06)}
imp = []; ok = True
for m, (hr, lr) in k5ref.items():
    h_ = rate(m * 1e6, False, True) / rate(m * 1e6, False, False); l_ = rate(m * 1e6, True, True) / rate(m * 1e6, True, False)
    imp.append((m, float(round(h_, 3)), float(round(l_, 3)))); ok &= abs(h_ - hr) < 0.01 and abs(l_ - lr) < 0.01
chk("K5 misprint impact R_printed/R_correct (m_chi MeV, heavy, light) = CW4 sec. 13 table to +-0.01", ok, str(imp))

# ======================= K6: 2208.05967 Eq. (6) vs URF (LE-110) =======================
# [errata: non-circular] (i) the angular delta integral of 1509.01598 Eq. (3.9) done by sympy: int dcos delta(a - q v cos) = 1/(q v);
#     hence <sigma v> = (sig/(2 mu^2)) int q dq eta F^2 |f|^2 and dR/dlnE = N_t E rho sig/(2 m mu^2) int ... = (14.1).
#     (ii) mass dimensions computed from a dimension table (not typed in per formula). (iii) depolarisation criterion as an exact identity.
aa, qq_, vv_, cc_ = sp.symbols('a q v c', positive=True)
ang = sp.integrate(sp.DiracDelta(aa - qq_ * vv_ * cc_), (cc_, -1, 1))
ang_ok = sp.simplify(ang.subs(aa, qq_ * vv_ / 2) - 1 / (qq_ * vv_)) == 0
mu_, E_, m_, rho, sig, Nt, q_ = sp.symbols('mu E m rho sigma N_t q', positive=True)
sigv_pref = sig / mu_**2 * (2 * sp.pi) / (4 * sp.pi)                     # (sig/mu^2) * (1/4pi) * 2pi from the azimuth, times 1/v from ang
pref141 = Nt * E_ * rho / m_ * sigv_pref                                   # x E for d/dlnE
pref6 = Nt * rho * sig / (8 * m_ * mu_)
ratio = sp.simplify(pref6 / pref141)
dim = {'rho': 4, 'm': 1, 'sigma': -2, 'mu': 1, 'E': 1, 'qdq': 2, 'dq/q2': -1, 'f10': -1, 'f12': 0, 'alpha': 0, 'me2/mu2': 0}
d141 = dim['E'] + dim['rho'] - dim['m'] + dim['sigma'] - 2 * dim['mu'] + dim['qdq'] + dim['f10']
d6_10 = dim['rho'] - dim['m'] + dim['sigma'] - dim['mu'] + dim['qdq'] + dim['f10']
d6_12 = dim['rho'] - dim['m'] + dim['sigma'] - dim['mu'] + dim['qdq'] + dim['f12']
d142 = dim['rho'] - dim['m'] + dim['sigma'] + dim['alpha'] + dim['me2/mu2'] + dim['E'] + dim['dq/q2'] + dim['f12']
eps1, eps2, eo = sp.symbols('epsilon_1 epsilon_2 epsilon_o', real=True)
dep = sp.expand(9 * (eps1**2 + eps2**2) - ((eps1 + 2 * eo)**2 + eps2**2) - 8 * (eps1**2 + eps2**2 - eo / 2 * (eps1 + eo)))
mu10 = 10e6 * me / (10e6 + me)
chk("K6 angular delta -> 1/(qv) (sympy); Eq.(6)/(14.1) = mu/(4E); dims: (14.1),(14.2),(6)+(10) = 1, (6)+(12) = 2; "
    "9|e|^2-|e+2eo|^2 = 8[|e|^2-(eo/2)(e1+eo)] exactly",
    ang_ok and sp.simplify(ratio - mu_ / (4 * E_)) == 0 and (d141, d142, d6_10, d6_12) == (1, 1, 1, 2) and dep == 0
    and abs(mu10 / 12 - 4.05e4) < 0.01e4, "mu/(4E) at m_chi=10 MeV, E=3 eV: %.3e" % (mu10 / 12))

# ======================= K7: (H_W) restricted boost (LE-115) =======================
rng = np.random.default_rng(1)
n = 7; A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); Rm = (A + A.conj().T) / 2
e = np.sort(rng.uniform(-3, 3, n)); H = np.diag(e); mm = 1.3
F = mm * (H @ (H @ Rm - Rm @ H) - (H @ Rm - Rm @ H) @ H)
B = rng.normal(size=(n, 3)); Pw = B @ np.linalg.pinv(B)
cI, vI = 6, 1
lhs = (F @ Pw)[cI, vI]; rhs = mm * sum((e[cI] - e[k])**2 * Rm[cI, k] * Pw[k, vI] for k in range(n))
Pd = np.zeros((n, n)); Pd[vI, vI] = 1.0
chk("K7 <c|F P|v> = m sum (e_c-e_m)^2 R_cm P_mv; rigid (flat) limit = m w^2 <c|R P|v> (1e-10)",
    abs(lhs - rhs) < 1e-10 and abs((F @ Pd)[cI, vI] - mm * (e[cI] - e[vI])**2 * (Rm @ Pd)[cI, vI]) < 1e-10)
Pval = np.zeros((n, n)); Pval[[0, vI, 2], [0, vI, 2]] = 1.0
full = mm * (e[cI] - e[vI])**2 * Rm[cI, vI]
ket = (F @ Pval)[cI, vI]; herm = 0.5 * ((F @ Pval) + (Pval @ F))[cI, vI]
chk("K7b ket-side ordering satisfies the sum rule (full boost); symmetrised ordering gives half", abs(ket - full) < 1e-10 and abs(herm - full / 2) < 1e-10)
# K7c [errata, V6]: absolute bound |A - (mq/M)<c|r P|v>| <= (mq/M)(2W/w + W^2/w^2) sum_v' |r_cv' P_v'v| (random projectors inside the
# valence manifold); and a cancellation example where <c|r P|v> = 0 but A != 0, so no relative bound on the sum exists.
val = [0, 1, 2]; Wb = e[val].max() - e[val].min(); okb = True
for _ in range(500):
    Bv = np.zeros((n, 2), complex); Bv[val] = rng.normal(size=(3, 2)) + 1j * rng.normal(size=(3, 2))
    P = Bv @ np.linalg.pinv(Bv); vv = val[rng.integers(3)]; w_ = e[cI] - e[vv]
    Aex = sum((e[cI] - e[k])**2 / w_**2 * Rm[cI, k] * P[k, vv] for k in val); rig = (Rm @ P)[cI, vv]
    okb &= abs(Aex - rig) <= (2 * Wb / w_ + Wb**2 / w_**2) * sum(abs(Rm[cI, k] * P[k, vv]) for k in val) + 1e-12
rc = Rm[cI, val]; wv = np.cross(np.conj(rc), rng.normal(size=3)).conj()          # w with sum_k rc_k w_k = 0
wv = wv / np.linalg.norm(wv); P1 = np.zeros((n, n), complex); P1[np.ix_(val, val)] = np.outer(wv, wv.conj())
rig1 = (Rm @ P1)[cI, vI]; A1 = sum((e[cI] - e[k])**2 / (e[cI] - e[vI])**2 * Rm[cI, k] * P1[k, vI] for k in val)
chk("K7c absolute W/w bound holds (500 random site projectors); cancellation case <c|rP|v> = 0, A != 0 (relative bound fails)",
    okb and abs(rig1) < 1e-12 and abs(A1) > 1e-3, "|A|=%.3g, rigid=%.1e" % (abs(A1), abs(rig1)))

# ======================= K8: two-sublattice AFM at k = 0 (LE-116) =======================
def colpa(Hm):
    nn = Hm.shape[0] // 2; Kc = np.linalg.cholesky(Hm).conj().T
    gm = np.diag([1] * nn + [-1] * nn); w, U = np.linalg.eigh(Kc @ gm @ Kc.conj().T)
    idx = np.argsort(-w); w = w[idx]; U = U[:, idx]
    Em = gm @ np.diag(w); T = np.linalg.inv(Kc) @ U @ np.sqrt(np.abs(Em))
    return w[:nn], T
ok = True
for (Aa, Bb, S) in ((1.2, 1.0, 2.5), (5.0, 1.0, 1.0), (1.01, 1.0, 0.5)):
    Hm = np.array([[Aa, 0, 0, Bb], [0, Aa, Bb, 0], [0, Bb, Aa, 0], [Bb, 0, 0, Aa]], float)
    w, T = colpa(Hm); vec = np.sqrt(S / 2) * np.ones(4)
    wt = sum(abs(vec @ T[:, nu])**2 for nu in range(2))
    ok &= abs(w[0] - np.sqrt(Aa**2 - Bb**2)) < 1e-9 and abs(wt - S * np.sqrt((Aa - Bb) / (Aa + Bb))) < 1e-9
tt = sp.symbols('t', positive=True)       # [errata, V8] symbolic closure: u = cosh t, v = sinh t, tanh 2t = B/A => (u-v)^4 = (A-B)/(A+B)
sym8 = sp.simplify(((1 - sp.tanh(2 * tt)) / (1 + sp.tanh(2 * tt))).rewrite(sp.exp) - (sp.cosh(tt) - sp.sinh(tt)).rewrite(sp.exp)**4) == 0
chk("K8 AFM k=0: omega = sqrt(A^2-B^2), weight S(u-v)^2 = S sqrt((A-B)/(A+B)) (Colpa 1e-9; sympy closed)", ok and sym8)

# ======================= K9: Dirac re-plot factors (LE-105) =======================
ok = True
for _ in range(200):
    eb = rng.uniform(2, 300); de = complex(rng.uniform(-50, 50), rng.uniform(1e-3, 50))
    er = 1 + de / eb; Lu = de.imag / abs(eb + de)**2; Ls = de.imag / abs(er)**2
    Gu = (eb * er).imag / abs(eb * er)**2; Gs = er.imag / abs(er)**2
    ok &= abs(Ls / Lu / eb**2 - 1) < 1e-10 and abs(Gs / Gu / eb - 1) < 1e-10
chk("K9 Rate_src/Rate_URF = eps_bg^2, Gamma_src/Gamma_URF = eps_bg (exact, any de); x1600/x6.3 (40), x640/x5.0 (25.3)",
    ok and round(40**2) == 1600 and abs(25.3**2 - 640) < 1 and abs(40**0.5 - 6.32) < 0.01 and abs(25.3**0.5 - 5.03) < 0.01)

# ======================= K10: massive 3D Dirac exciton (LE-102) =======================
# [errata, V10/V18 + LE-102 spec] Ry_D = D(alpha_t/g)^2/4 checked against the independent hydrogenic 1/(2 mu a^2), a = eps/(mu alpha),
# mu = D/(2 v^2); ZrTe5 with D_D = 11.8 meV (documented value, CW4 sec. 10); a_D vs the k-grids of the CW4 sec. 6 spec.
hcA = 1973.2698  # eV Angstrom
def exc(Dd, vF, eb, g=2):
    at = al * g / (eb * vF); mu = Dd / (2 * vF**2); a_ = eb / (mu * al)
    return Dd * (at / g)**2 / 4, 1 / (2 * mu * a_**2), at, a_
b1 = exc(1.0, 4e-4, 40); z1 = exc(11.8e-3, 1.3e-3, 25.3)
aD_A = z1[3] * hcA
dk60 = 2 * 0.23 / 60                                # 60 points across [-Lambda_x, Lambda_x], Lambda_x = 0.23 1/A (1910.02091 Table 1)
dk24 = 2 * np.pi / (13.7 * 24)                      # 24 points along the longest reciprocal axis, a_max ~ 13.7 A (ZrTe5)
ok = abs(b1[0] - 0.052) < 1e-3 and abs(b1[0] / b1[1] - 1) < 1e-12 and abs(b1[2] - 0.91) < 0.005 and abs(z1[0] * 1e3 - 0.145) < 1e-3 \
     and abs(z1[2] - 0.44) < 0.005 and 1.8e3 < aD_A < 2.2e3 and dk60 * aD_A > 10 and dk24 * aD_A > 10
chk("K10 Ry_D/D = %.4f (alpha_t %.3f), = 1/(2 mu a^2); ZrTe5 Ry_D = %.4f meV, a_D = %.0f A; Dk*a_D = %.0f (60 pts), %.0f (24^3): unresolved"
    % (b1[0], b1[2], z1[0] * 1e3, aD_A, dk60 * aD_A, dk24 * aD_A), ok)

# ======================= K11: relativistic density row (LE-114) =======================
# [errata: replaces the circular K11] (i) contraction of two conserved currents in the density row (j_T = 0): J.j = rho J0 (1 - w^2/Q^2);
# (ii) m_V -> 0: (1 - w^2/Q^2)/(Q^2 - w^2) = 1/Q^2 (Coulombic); (iii) kinematics w <= v_chi Q from the convex dispersion (1e5 samples),
# so (1 - w^2/Q^2)^2 in [(1-v^2)^2, 1]; (iv) the bound is <= 2 % only for v <= 0.1 and vacuous for CRDM (v -> 1).
Q, w, mV, rho_e, J0 = sp.symbols('Q omega m_V rho J_0', positive=True)
jL = w * rho_e / Q; JL = w * J0 / Q
contr = sp.simplify(J0 * rho_e - JL * jL)
amp = contr / (Q**2 - w**2 + mV**2); amp_src = J0 * rho_e / (Q**2 - w**2 + mV**2)
s11 = sp.simplify(amp / amp_src - (1 - w**2 / Q**2)) == 0 and sp.simplify(amp.subs(mV, 0) - J0 * rho_e / Q**2) == 0
mchi_ = 1.0; okk = True
P = rng.uniform(0.01, 20, (100000, 1)) * np.array([[0, 0, 1.0]]); Qv = rng.normal(size=(100000, 3)) * rng.uniform(0.001, 5, (100000, 1))
Ep = np.sqrt(mchi_**2 + (P**2).sum(1)); Epq = np.sqrt(mchi_**2 + ((P - Qv)**2).sum(1)); wq = Ep - Epq
vch = np.sqrt((P**2).sum(1)) / Ep; Qm = np.linalg.norm(Qv, axis=1)
okk = np.all(wq <= vch * Qm + 1e-12)
lb = lambda vx: (1 - vx**2)**2
chk("K11 J.j = rho J0(1-w^2/Q^2) (current conservation); m_V->0 Coulombic 1/Q^2; w <= v Q (1e5 relativistic samples); "
    "lower bound %.4f (v=0.1), %.1e (v=0.99)" % (lb(0.1), lb(0.99)), s11 and okk and lb(0.1) > 0.98 and lb(0.99) < 1e-3)

# ======================= K12: unpolarised neutrons (LE-117) =======================
ok = True
for _ in range(50):
    Sm = rng.normal(size=(3, 3)); Sm = Sm @ Sm.T; qv = rng.normal(size=3); qv /= np.linalg.norm(qv)
    Qr, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    PT = lambda x: np.eye(3) - np.outer(x, x)
    ok &= abs(np.sum(PT(Qr @ qv) * (Qr @ Sm @ Qr.T)) - np.sum(PT(qv) * Sm)) < 1e-10
Sp, Sq = 1.7, 0.4
def unpol(cth): return Sp * (1 - cth**2) + Sq * (1 + cth**2)
c1_, c2_ = 0.2, 0.9; Mx = np.array([[1 - c1_**2, 1 + c1_**2], [1 - c2_**2, 1 + c2_**2]])
sol = np.linalg.solve(Mx, [unpol(c1_), unpol(c2_)])
chk("K12 symmetry-equivalent q give one equation; (H_iso) two-angle inversion recovers S_par, S_perp", ok and np.allclose(sol, [Sp, Sq], atol=1e-12))

# ======================= K13: Foerster coupling size (LE-111) [E] =======================
hc = 197.327e-9
J = (1 / 137.036) * hc * (0.3e-9)**2 * 2 * (3 * 2.5 / (17 + 2 * 2.5))**2 / (2.5 * (6e-9)**3)
chk("K13 J_F = %.2e eV (VER-CW4 V22: 5.6e-5, 2 %%) << level spacing 0.1 eV" % J, abs(J / 5.6e-5 - 1) < 0.02)

# ======================= K14: data rows (LE-106, LE-107) =======================
# [errata: replaces arithmetic-only K14] (i) the rows the owed correction OC-11 targets exist with the quoted content in R14 v2 and R16 v3;
# (ii) 1603.05351 Table I v_F (1e5 m/s) -> units of c reproduce the 1910.02091 'Exp. [52]' velocities to the 2 printed digits;
# (iii) Al 1.764 k_B T_c, the 0.3 meV ratio; Nb 1.764 k_B x 10.72 K = 1.63 meV and 2D/k_BT_c of the [FT] range.
def find(path, pref, must=()):
    with open(path, encoding='utf-8') as fh:
        for i, L in enumerate(fh, 1):
            if L.startswith(pref) and all(m in L for m in must): return i
    return 0
v2 = ROOT / "returns/R14/WP8-U-table-v2.csv"; v3 = ROOT / "returns/R16/WP8-U-table-v3.csv"
found = {}
for tag_, pth in (("v2", v2), ("v3", v3)):
    found[tag_] = (find(pth, "ZrTe5,ZrTe5,Dirac,SURVIVOR-COND,Delta_D,", ("11.75",)),
                   find(pth, "Al,Al,superconductor,SURVIVOR-COND,Delta_BCS,0.3,meV,FT,arXiv:2109.04473"),
                   find(pth, "Nb,Nb,superconductor,SURVIVOR-COND,Delta_BCS_E,1.63,meV,E,"))
found["v3+"] = (find(v3, "Al,Al,superconductor,SURVIVOR-COND,flag_Delta_BCS,"),
                find(v3, "ZrTe5,ZrTe5,Dirac,SURVIVOR-COND,Delta_D_definition,", ("11.75 meV is the half-gap",)))
rows_ok = all(all(x > 0 for x in t) for t in found.values())
cl = 2.99792458e8
vF = [round(x * 1e5 / cl, 7) for x in (4.03, 1.94, 4.89)]
vF_ok = [float("%.2g" % x) for x in vF] == [1.3e-3, 6.5e-4, 1.6e-3]
kB = 8.617333e-5
Al12, Al1175, Nb = 1.764 * kB * 1.2e3, 1.764 * kB * 1.175e3, 1.764 * kB * 10.72e3
r2D = (2 * 1.50 / (kB * 9.3e3), 2 * 1.61 / (kB * 9.25e3))
ok = rows_ok and vF_ok and abs(Al12 - 0.182) < 1e-3 and abs(Al1175 - 0.179) < 1e-3 and abs(0.3 / 0.18 - 1.67) < 0.01 \
     and abs(Nb - 1.63) < 0.005 and abs(r2D[0] - 3.74) < 0.01 and abs(r2D[1] - 4.04) < 0.01
chk("K14 OC-11 target rows found %s; [52] v_F -> %s c; Al %.3f/%.3f meV; Nb %.3f meV; 2D/kTc %.2f-%.2f"
    % (found, vF, Al12, Al1175, Nb, *r2D), ok)

# ======================= K15 [errata, V21]: Si valley-orbit momentum transfers, with umklapp (exact rationals) =======================
k0f = sp.Rational(85, 100)
Gs = [g for g in itertools.product(range(-3, 4), repeat=3) if all(x % 2 == 0 for x in g) or all(x % 2 for x in g)]   # fcc reciprocal (2pi/a units)
def qset(dv): return sorted({sp.sqrt(sum((sp.Rational(d) + gg)**2 for d, gg in zip(dv, g))) for g in Gs}, key=float)[:3]
qg = qset((2 * k0f, 0, 0)); qf = qset((k0f, -k0f, 0))
b_keV = 2 * np.pi / 5.431 * 1.9732698
qg_keV = [float(x) * b_keV for x in qg]; qf_keV = [float(x) * b_keV for x in qf]
chk("K15 Si (2pi/a = %.3f keV): g-process %s keV, f-process %s keV (lowest f: G=(1,-1,+-1), |q|^2=1.045 (2pi/a)^2)"
    % (b_keV, [round(x, 2) for x in qg_keV], [round(x, 2) for x in qf_keV]),
    qg[0] == sp.Rational(3, 10) and qf[0] == sp.sqrt(sp.Rational(1045, 1000)) and abs(qg_keV[0] - 0.685) < 2e-3
    and abs(qf_keV[0] - 2.334) < 2e-3 and abs(qf_keV[1] - 2.744) < 2e-3 and any(abs(x - 3.881) < 2e-3 for x in qg_keV))

# ======================= K16 [errata, V20]: BCS limit of the strong-coupling pair weight =======================
Es, Ep_, Dl = sp.symbols('E Ep Delta', positive=True)
Ns = lambda x: x / sp.sqrt(x**2 - Dl**2); Ps = lambda x: Dl / sp.sqrt(x**2 - Dl**2)
k16 = sp.simplify(Ns(Es) * Ns(Ep_) + Ps(Es) * Ps(Ep_) - (Es * Ep_ + Dl**2) / (sp.sqrt(Es**2 - Dl**2) * sp.sqrt(Ep_**2 - Dl**2))) == 0
k16b = sp.simplify(Ns(Es) * Ns(Ep_) * (1 + Dl**2 / (Es * Ep_)) - (Ns(Es) * Ns(Ep_) + Ps(Es) * Ps(Ep_))) == 0
chk("K16 N_sN_s' + P_sP_s' = (EE'+D^2)/sqrt(..) = N_sN_s'(1 + D^2/EE') (BCS limit of the CW4 sec. 12 strong-coupling weight)", k16 and k16b)

# ======================= K17 [errata, V16]: identical-magnon pair counting =======================
# M = 4 modes, total momentum qP; O+ = sum_k A_k a+_k a+_{qP-k} with A symmetric. ||O+|0>||^2 = 2 sum_k |A_k|^2 (ordered sum double counts);
# the unordered, normalised pair basis gives the correct weight.
Mm, nmax = 4, 3
ab = np.diag(np.sqrt(np.arange(1, nmax)), 1)
def op(k):
    mats = [np.eye(nmax)] * Mm; mats = mats[:k] + [ab] + mats[k + 1:]
    out_ = mats[0]
    for m_ in mats[1:]: out_ = np.kron(out_, m_)
    return out_
aop = [op(k) for k in range(Mm)]; vac = np.zeros(nmax**Mm); vac[0] = 1
qP = 2; Ak = rng.normal(size=Mm) + 1j * rng.normal(size=Mm); Ak = np.array([Ak[k] + Ak[(qP - k) % Mm] for k in range(Mm)]) / 2
psi = sum(Ak[k] * aop[k].T @ aop[(qP - k) % Mm].T @ vac for k in range(Mm))
nrm = np.vdot(psi, psi).real
unordered = 0.0
for k in range(Mm):
    kk = (qP - k) % Mm
    if k > kk: continue
    st = aop[k].T @ aop[kk].T @ vac; st = st / np.linalg.norm(st)
    unordered += abs(np.vdot(st, psi))**2
chk("K17 two-magnon weight: ||O+|0>||^2 = 2 sum|A_k|^2 = sum over unordered normalised pairs (k <-> q-k, nu = nu')",
    abs(nrm - 2 * np.sum(abs(Ak)**2)) < 1e-12 and abs(nrm - unordered) < 1e-12)

# ======================= K18 [errata, V28]: closure counts parsed from the CW4 sec. 0 table =======================
cnt = {"CLOSED": 0, "EG": 0, "split": 0, "rem": 0}
for L in (ROOT / "returns/R16/CW4.md").read_text(encoding='utf-8').splitlines():
    if not L.startswith("| LE-"): continue
    st = L.split("|")[4]
    hasC = "**CLOSED**" in st; hasG = "**CLOSED-AS-EXACT-GAP**" in st
    if hasC and hasG: cnt["split"] += 1
    elif hasG: cnt["EG"] += 1
    elif hasC:
        cnt["CLOSED"] += 1; cnt["rem"] += ("exact gap" in st.lower())
chk("K18 CW4 sec. 0: CLOSED %d (with exact-gap remainder %d), CLOSED-AS-EXACT-GAP %d, split rows %d (LE-107)"
    % (cnt["CLOSED"], cnt["rem"], cnt["EG"], cnt["split"]), (cnt["CLOSED"], cnt["rem"], cnt["EG"], cnt["split"]) == (16, 4, 4, 1))

print("%d/%d PASS  (%.1f s)" % (sum(RES), len(RES), time.time() - T0))
sys.exit(0 if all(RES) else 1)
