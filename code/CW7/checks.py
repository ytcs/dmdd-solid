"""CW7 checks, ERR-CW7 revision (numpy + scipy + sympy). Labels CW7-Cn (cited in returns/R16/CW7.md, CW7-errata.md,
WP8-U-v3.md, WP8-F-v3.md). Offline. Runtime < 1 min on the box.
ERR-CW7 changes (VER-CW7 §F): tautological checks replaced (C3 finite-LP duality -> cross-grid dual certificate; C11 -> the
Delta P < 0 counterexample and the corrected bound; C15 one threshold convention; C16 signed elasticities; C18 rigid-ion model
instead of substituting the conclusion; C20 (sympy of a hand-written expression) -> Migdal plasmon-pole and f-sum bound;
C27 (solve-for-the-symbol) -> light/heavy-mediator NR-1ph scaling; C31 no longer re-runs rank.py and tests the POL bound as an
inequality; C19 computes f_<1keV instead of hard-coding it); tolerances tightened; new checks C33-C38 for every correction.
The superseded R16 version is kept verbatim in git history (no file other than code/CW7/ was edited).
ERR-WP8 (R17, VER-ERR-CW7 RC3): every LE-153 solver call now runs on a commensurate grid (h | E_g, theta_ii E_g, omega_0; omega_0 = 0.054
-> h = 0.002, 0.001); C5, C5b, C7, C8 moved to it; new C5c: independent Monte Carlo of the exact cascade vs the solver, the strict
grid guard, and the size of the old quantisation bias."""
import csv, json, math, os, re, sys, time
import numpy as np
import sympy as sp
from scipy.optimize import linprog

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from cascade_gf import CascadeGF, moments_fast, pmf_from_gf, commensurate_h  # noqa: E402

T0 = time.time()
RES = []


def check(label, ok, msg):
    RES.append((label, bool(ok), msg))
    print(("PASS " if ok else "FAIL ") + label + ": " + msg)


rng = np.random.default_rng(20261101)
CKMS = 299792.458

# ---------------- SHM eta (CONVENTIONS §8: v0 238, v_esc 544, v_E^ref 250.5 km/s; v_max 794.5) ----------------
V0, VESC, VE = 238 / CKMS, 544 / CKMS, 250.5 / CKMS
VMAX = VESC + VE
_v = np.linspace(1e-7, VMAX, 40001)
_mu = np.clip((VESC ** 2 - _v ** 2 - VE ** 2) / (2 * _v * VE), -1, 1)
_f = _v ** 2 / (_v * VE) * (np.exp(-(_v - VE) ** 2 / V0 ** 2) - np.exp(-(_v ** 2 + VE ** 2 + 2 * _v * VE * _mu) / V0 ** 2)) * (_mu > -1)
_f /= np.trapezoid(_f, _v)
_g = _f / _v
_cum = np.concatenate([[0], np.cumsum((_g[1:] + _g[:-1]) / 2 * np.diff(_v))])
_eta = _cum[-1] - _cum


def eta(vmin):
    return np.interp(vmin, _v, _eta, right=0.0)


# ---------------- LE-152: stream (extreme-point) halo-independent bounds ----------------
v = np.linspace(50, 800, 76)
A = np.abs(rng.normal(1, 0.5, (3, v.size))) * (v / 800) ** 2 + 0.05   # non-monotone columns
N = np.array([2.3, 3.9, 5.3])
u0 = 300.0
sel = v >= u0
ok = True
for i in range(3):
    r = linprog(-sel.astype(float), A_ub=A[i:i + 1], b_ub=N[i:i + 1], bounds=(0, None), method="highs")
    ok &= abs(-r.fun - N[i] / A[i][sel].min()) < 1e-9 * N[i] / A[i][sel].min()
check("CW7-C1", ok, "LE-152 (iv) isotropic lab-frame reduction: single-bin LP sup eta~(u0) = N_i / inf_{v>=u0} A_i(v) to 1e-9 (non-monotone columns)")
r = linprog(-sel.astype(float), A_ub=A, b_ub=N, bounds=(0, None), method="highs")
nz = int(np.sum(r.x > 1e-12))
check("CW7-C2", (-r.fun <= min(N[i] / A[i][sel].min() for i in range(3)) * (1 + 1e-12)) and nz <= 3,
      "LE-152 multi-bin LP <= min_i single-bin bounds; optimum on %d <= N_b = 3 atoms" % nz)
# C3 (replaces the finite-LP duality tautology): the semi-infinite statement. Solve on a coarse stream grid, refine the grid
# (nested: coarse points kept, 3x more random streams added), and certify with the COARSE dual: lambda_c scaled by
# s = max_fine phi/(lambda_c.K) is feasible on the fine grid, so U = s lambda_c.N bounds the fine (and, as the grid fills B,
# the continuum) optimum. Then one column-generation round (add the most violated streams) must close the gap monotonically.
nd = 60
k = np.arange(nd) + 0.5
th = np.arccos(1 - 2 * k / nd); ph = np.pi * (1 + 5 ** 0.5) * k
dirs = np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], 1)
Vc = (dirs[:, None, :] * np.linspace(100, 800, 15)[None, :, None]).reshape(-1, 3)
extra = rng.normal(size=(3 * len(Vc), 3)); extra /= np.linalg.norm(extra, axis=1)[:, None]
extra *= rng.uniform(100, 800, len(extra))[:, None]
Vf = np.vstack([Vc, extra])
nb = 4
axes = rng.normal(size=(nb, 3)); axes /= np.linalg.norm(axes, axis=1)[:, None]
kern = lambda V: np.array([np.clip(V @ a - 150, 0, None) ** 1.5 / 1e3 + 0.01 * np.linalg.norm(V, axis=1) / 800 for a in axes])
phif = lambda V: (np.linalg.norm(V, axis=1) >= 400).astype(float) * (1 + 0.5 * V[:, 2] / np.linalg.norm(V, axis=1))
Nb = np.array([3.0, 2.3, 4.0, 6.0])
Kc, Kf = kern(Vc), kern(Vf)
rc = linprog(-phif(Vc), A_ub=Kc, b_ub=Nb, bounds=(0, None), method="highs")
rf = linprog(-phif(Vf), A_ub=Kf, b_ub=Nb, bounds=(0, None), method="highs")
lam_c = -rc.ineqlin.marginals
s_scale = max(1.0, np.max(phif(Vf) / (lam_c @ Kf)))
U = s_scale * lam_c @ Nb
viol = np.argsort(phif(Vf) - lam_c @ Kf)[-20:]
Vg = np.vstack([Vc, Vf[viol]])
rg = linprog(-phif(Vg), A_ub=kern(Vg), b_ub=Nb, bounds=(0, None), method="highs")
nzf = int(np.sum(rf.x > 1e-12))
check("CW7-C3", (-rc.fun <= -rg.fun + 1e-12) and (-rg.fun <= -rf.fun + 1e-12) and (-rf.fun <= U * (1 + 1e-12)) and nzf <= nb and s_scale > 1,
      "LE-152 semi-infinite LP: coarse %.4f <= after one column-generation round %.4f <= refined %.4f <= coarse-dual certificate %.4f "
      "(scale %.3f > 1: the coarse dual is NOT feasible on the refined grid, so grid refinement is needed); %d <= %d atoms"
      % (-rc.fun, -rg.fun, -rf.fun, U, s_scale, nzf, nb))
# C4 (replaces linearity of an average): (iv) needs the LAB-frame ball. An isotropic lab kernel A(|w - v_E|) read with a
# galactic-frame weight phi(w) = Theta(|w| - u0)/|w| does not give N/inf A (VER-CW7 §B1).
ve = np.array([0.0, 250.5, 0.0])
Wg = (dirs[:, None, :] * np.linspace(20, 544, 40)[None, :, None]).reshape(-1, 3)
Afun = lambda s: 0.05 + (s / 800) ** 2
vlab = np.linalg.norm(Wg - ve, axis=1)
lab_ok, gal_dev = True, 0.0
for frame in ("lab", "gal"):
    sp_ = vlab if frame == "lab" else np.linalg.norm(Wg, axis=1)
    phi_ = (sp_ >= u0) / np.maximum(sp_, 1e-9)
    Kr = (Afun(vlab) / np.maximum(vlab, 1e-9))[None, :]       # one bin; mu = int A(v)/v dF with eta-shell normalisation
    rr = linprog(-phi_, A_ub=Kr, b_ub=[2.3], bounds=(0, None), method="highs")
    exact = 2.3 / Afun(vlab[vlab >= u0]).min()
    if frame == "lab":
        lab_ok = abs(-rr.fun / exact - 1) < 1e-9
    else:
        gal_dev = abs(-rr.fun / exact - 1)
check("CW7-C4", lab_ok and gal_dev > 0.01,
      "LE-152 (iv) frame: N/inf A reproduced to 1e-9 with the lab-frame weight; galactic-frame |w| weight deviates by %.1f%% (statement holds in the lab frame only)" % (100 * gal_dev))

# ---------------- LE-153: generating-function cascade ----------------
# ERR-WP8: commensurate grid (h divides E_g = 1, theta_ii and omega_0 = 0.054): h = 0.002 (and 0.001 for the h-sequence)
HC = commensurate_h(0.054, 1.5, 0.02)
Nz = 32
zs = np.exp(2j * np.pi * np.arange(Nz) / Nz)
ok, msg = True, []
for lam_, th_ii in ((0.0, 1.0), (3.55, 1.0), (3.55, 1.5), (3.55, 2.0)):
    cg = CascadeGF(X=8.0, h=HC, a=0.5, lam=lam_, w=0.054, theta=th_ii, zs=zs)
    G = cg.solve_gf()
    x, m, s = moments_fast(X=8.0, h=HC, a=0.5, lam=lam_, w=0.054, theta=th_ii)
    P = pmf_from_gf(G[-1], zs); n = np.arange(Nz)
    ok &= abs(P.sum() - 1) < 1e-12 and P.min() > -1e-13 and abs((n * P).sum() - m[-1]) < 1e-9 and abs((n * n * P).sum() - s[-1]) < 1e-8
    msg.append("(lam %.2f, theta %.1f): sumP-1 %.0e, mean %.6f = %.6f" % (lam_, th_ii, P.sum() - 1, (n * P).sum(), m[-1]))
check("CW7-C5", ok and abs(HC - 0.002) < 1e-15, "LE-153 (CW7-153a) solver incl. theta_ii > 1 (ERR-CW7 fix) on the commensurate grid h = %.3g: sum P = 1, P >= 0, G'(1), G''(1) = moment recursion; " % HC + "; ".join(msg))
cg8 = CascadeGF(X=8.0, h=HC, a=0.5, lam=3.55, w=0.054, theta=1.5, zs=np.exp(2j * np.pi * np.arange(4) / 4)); G8 = cg8.solve_gf()
P4 = pmf_from_gf(G8[-1], cg8.zs)
cg32 = CascadeGF(X=8.0, h=HC, a=0.5, lam=3.55, w=0.054, theta=1.5, zs=zs); P32 = pmf_from_gf(cg32.solve_gf()[-1], zs)
alias = np.array([P32[j::4].sum() for j in range(4)])
check("CW7-C5b", np.max(np.abs(P4 - alias)) < 1e-12 and P32[4:].sum() > 1e-3,
      "LE-153 (CW7-153b) wording: with N_z = 4 the DFT returns sum_k P(n + 4k) (max dev %.0e) while P(N >= 4) = %.3f: 'exact iff P(N >= N_z) = 0', not 'exact for N < N_z'"
      % (np.max(np.abs(P4 - alias)), P32[4:].sum()))
# C5c (ERR-WP8, VER-ERR-CW7 §C2): independent Monte Carlo of the exact cascade (ii split Dirichlet(3/2,3/2,3/2) of x - 1, phonon step omega_0,
# p = 1/(1 + lam rho(x - w)/Phi(x - 1)), Phi(y) = Gamma(3/2)^3/Gamma(9/2) y^(7/2)) vs the solver on commensurate grids; strict guard; old bias
from scipy.special import gamma as _gam  # noqa: E402


def mc_cascade(x0, lam, th, w, n, seed):
    r_ = np.random.default_rng(seed)
    PhiC = _gam(1.5) ** 3 / _gam(4.5)
    E_, own, N_ = np.full(n, x0), np.arange(n), np.zeros(n)
    while E_.size:
        a_ = E_ >= th
        E_, own = E_[a_], own[a_]
        if not E_.size:
            break
        p_ = 1 / (1 + lam * np.sqrt(np.maximum(E_ - w, 0)) / (PhiC * (E_ - 1) ** 3.5))
        ii = r_.random(E_.size) < p_
        Ei, oi = E_[ii] - 1, own[ii]
        np.add.at(N_, oi, 1)
        D_ = r_.dirichlet([1.5, 1.5, 1.5], size=Ei.size) * Ei[:, None]
        E_, own = np.concatenate([E_[~ii] - w, D_.ravel()]), np.concatenate([own[~ii], np.repeat(oi, 3)])
    return N_.mean(), N_.std() / math.sqrt(n)


okc, msgc = True, []
for w_ in (0.054, 0.05):
    mmc, smc = mc_cascade(8.0, 3.55, 1.5, w_, 200000, 11)
    hs = [commensurate_h(w_, 1.5, 0.002), commensurate_h(w_, 1.5, 0.001)]
    mg = [moments_fast(X=8.0, h=h_, a=0.5, lam=3.55, w=w_, theta=1.5)[1][-1] for h_ in hs]
    okc &= abs(mg[1] - mmc) < 3 * smc and abs(mg[1] - mg[0]) < 1e-4
    msgc.append("omega_0 %.3f: MC %.4f +- %.4f, grid %.5f (h %.4g) / %.5f (h %.4g)" % (w_, mmc, smc, mg[0], hs[0], mg[1], hs[1]))
try:
    CascadeGF(X=8.0, h=0.02, a=0.5, lam=3.55, w=0.054, theta=1.5)
    guard = False
except ValueError:
    guard = True
import warnings as _w  # noqa: E402
with _w.catch_warnings():
    _w.simplefilter("ignore")
    old = moments_fast(X=8.0, h=0.02, a=0.5, lam=3.55, w=0.054, theta=1.5, strict=False)[1][-1]
mg054 = moments_fast(X=8.0, h=0.001, a=0.5, lam=3.55, w=0.054, theta=1.5)[1][-1]
check("CW7-C5c", okc and guard and -0.02 < old / mg054 - 1 < -0.015,
      "LE-153 commensurate grid (VER-ERR-CW7 RC3): %s; non-commensurate h = 0.02 now raises (guard %s); the old quantised run (omega_0,eff 0.06) is biased by %.2f%%"
      % ("; ".join(msgc), guard, 100 * (old / mg054 - 1)))
ce = []
for h in (0.02, 0.01):
    x, m, s = moments_fast(X=40.0, h=h, a=0.5, lam=0.0, w=0.054)
    selx = x > 20
    a1 = np.polyfit(x[selx], m[selx], 1)[0]; a2 = np.polyfit(x[selx], (s - m * m)[selx], 1)[0]
    ce.append((1 / a1, a2 / a1))
c0 = 2 * ce[1][0] - ce[0][0]
ce3 = []
for h in (0.02, 0.01):
    x, m, s = moments_fast(X=40.0, h=h, a=0.5, lam=0.0, w=0.054, theta=1.5)
    selx = x > 20
    ce3.append(1 / np.polyfit(x[selx], m[selx], 1)[0])
c03 = 2 * ce3[1] - ce3[0]
check("CW7-C6", abs(c0 - 1.585) < 0.0006 and abs(ce[1][1] - 0.081) < 0.0006 and abs(c03 - 2.056) < 0.0006,
      "LE-153 vs GAP-EF §1.6 (lam_ph -> 0; omega_0 does not enter, so h = 0.02, 0.01 are commensurate): eps/E_g Richardson %.4f (1.585, theta 1), %.4f (2.056, theta 3/2); F %.4f (0.081)" % (c0, c03, ce[1][1]))
x, m, s = moments_fast(X=40.0, h=HC, a=0.5, lam=3.55, w=0.054)
selx = x > 20
F_si = np.polyfit(x[selx], (s - m * m)[selx], 1)[0] / np.polyfit(x[selx], m[selx], 1)[0]
eps_si = 1 / np.polyfit(x[selx], m[selx], 1)[0]
with _w.catch_warnings():
    _w.simplefilter("ignore")
    x2, m2, s2 = moments_fast(X=40.0, h=0.02, a=0.5, lam=3.55, w=0.054, strict=False)
F_old = np.polyfit(x2[x2 > 20], (s2 - m2 * m2)[x2 > 20], 1)[0] / np.polyfit(x2[x2 > 20], m2[x2 > 20], 1)[0]
eps_old = 1 / np.polyfit(x2[x2 > 20], m2[x2 > 20], 1)[0]
check("CW7-C7", abs(F_si - 0.114) < 0.001 and abs(eps_old / eps_si - 1 - 0.0132) < 0.002,
      "LE-153 Si case (lam_ph 3.55, w0 0.054) on the commensurate grid h = %.3g: F = %.4f, eps/E_g = %.4f (GAP-EF 0.114; the h = 0.02 run with omega_0,eff = 0.06, "
      "as in code/GAP-EF/cascade.py, gives F %.4f, eps/E_g %.4f: +%.1f%%)" % (HC, F_si, eps_si, F_old, eps_old, 100 * (eps_old / eps_si - 1)))
cg = CascadeGF(X=6.0, h=HC, a=0.5, lam=3.55, w=0.054, theta=1.5, zs=zs); G = cg.solve_gf()
ie, ih = int(round(4.0 / HC)), int(round(1.5 / HC))
Pl = pmf_from_gf(zs * G[ie] * G[ih], zs)
x6, m6, _ = moments_fast(X=6.0, h=HC, a=0.5, lam=3.55, w=0.054, theta=1.5)
check("CW7-C8", abs((np.arange(Nz) * Pl).sum() - (1 + m6[ie] + m6[ih])) < 1e-9 and Pl[0] < 1e-13 and abs(Pl.sum() - 1) < 1e-12,
      "LE-153 Lambda-seeding at theta_ii = 3/2 (h = %.3g): <N|Lambda> = 1 + m(x_e) + m(x_h) = %.5f; P(0|Lambda) = 0; sum P = 1" % (HC, 1 + m6[ie] + m6[ih]))

# ---------------- LE-154: leakage of hypothesis (P) ----------------
E = np.linspace(0, 40, 40001); dE = E[1] - E[0]
ok = True
for _ in range(5):
    f = np.cumsum(rng.normal(0, 1, E.size)) * 0.01 + np.sin(E)
    sh = int(round(0.37 / dE))
    ok &= np.sum(np.abs(f[sh:] - f[:-sh])) * dE <= 0.37 * np.sum(np.abs(np.diff(f))) * (1 + 1e-12)
check("CW7-C9", ok, "LE-154 lemma: int |f(E) - f(E - h)| dE <= h TV(f) on random BV functions")
eps, wq = 3.749, 0.0623
Pi = ((E >= 2 * eps) & (E < 3 * eps)).astype(float)
sh = int(round(wq / dE))
lhs = np.sum(np.abs(Pi[sh:] - Pi[:-sh])) * dE
check("CW7-C10", abs(lhs - 2 * wq) < 1.01 * dE and abs(np.sum(np.abs(np.diff(Pi))) - 2) < 1e-12,
      "LE-154 step bin: int |P(i|E) - P(i|E - omega_Q)| dE = 2 omega_Q = %.4f eV; 2 omega_max/eps_eh = %.4f (Si)" % (lhs, 2 * wq / eps))
# C11 (replaces the toy built to avoid the Delta P < 0 region): VER-CW7 §B3 counterexample. A_tot >= 0, A_X+ >= 0 everywhere, with
# a narrow A_X+ peak above A_tot at the LOWER bin edge, where Delta P = P_X+ - P_X0 = -1; there the summed kernel is
# P_X+ A_tot + |Delta P| A_X0 = A_X0 < 0. The R16 bound (CW7-154) with [A_X+]_- gives 0; the corrected one uses max([A_X+]_-, [A_X0]_-).
w = np.linspace(4, 16, 240001); dw = w[1] - w[0]
Atot = 0.2 + np.exp(-((w - 9) / 3) ** 2)
AXp = 0.3 * np.exp(-((w - 9) / 3) ** 2) + 1.2 * np.exp(-((w - (2 * eps + 0.03)) / 0.012) ** 2)
AX0 = Atot - AXp
P0 = ((w >= 2 * eps) & (w < 3 * eps)).astype(float)
P1 = (((w - wq) >= 2 * eps) & ((w - wq) < 3 * eps)).astype(float)
tot = P0 * AX0 + P1 * AXp
leak = -np.sum(np.minimum(tot, 0)) * dw
old_bound = 2 * wq * np.max(np.maximum(-AXp, 0))
new_bound = 2 * wq * np.max(np.maximum(np.maximum(-AXp, 0), np.maximum(-AX0, 0)))
mu_i = np.sum(P0 * Atot) * dw
check("CW7-C11", leak > 0 and old_bound == 0 and leak <= new_bound and AXp.min() >= 0 and Atot.min() > 0,
      "LE-154 counterexample: negative part %.2e with [A_X+]_- = 0 (R16 bound %.0f: FALLS); corrected bound 2 omega_Q sup max([A_X+]_-,[A_X0]_-) = %.2e holds; lambda_i = %.1e"
      % (leak, old_bound, new_bound, leak / mu_i))

# ---------------- LE-155: scalar absorption ----------------
xs_ = sp.symbols("x", real=True)
p2 = lambda f: -sp.diff(f, xs_, 2)
ok = True
Vh = xs_ ** 2 / 2
for n_ in (0, 1, 2):
    psi_n = sp.hermite(n_, xs_) * sp.exp(-xs_ ** 2 / 2)
    comm = lambda F, G_, f: F(G_(f)) - G_(F(f))
    inner = lambda f: comm(p2, lambda g: Vh * g, f)
    dc = inner(p2(psi_n)) - p2(inner(psi_n))
    lhs = sp.integrate(sp.expand(psi_n * dc), (xs_, -sp.oo, sp.oo))
    rhs = 4 * sp.integrate(psi_n ** 2 * sp.diff(Vh, xs_) ** 2, (xs_, -sp.oo, sp.oo))
    ok &= sp.simplify(lhs - rhs) == 0
check("CW7-C12", ok, "LE-155 sympy: <n|[[p^2,V],p^2]|n> = 4m<n|V'^2|n> for HO eigenstates n = 0, 1, 2 (one-body, regular V)")
r_, Zs, e_ = sp.symbols("r Z epsilon", positive=True)
psi1s2 = Zs ** 3 / sp.pi * sp.exp(-2 * Zs * r_)
gradV2 = Zs ** 2 / r_ ** 4
I_eps = sp.integrate(4 * sp.pi * r_ ** 2 * psi1s2 * gradV2, (r_, e_, sp.oo))
lead = sp.limit(I_eps * e_, e_, 0)
check("CW7-C12b", sp.simplify(lead - 4 * Zs ** 5) == 0,
      "LE-155 sum rule diverges for Coulomb V: hydrogenic 1s <(grad V)^2>_{r>eps} ~ %s/eps as eps -> 0 (VER-CW7 §B4 confirmed)" % sp.simplify(lead))
Ng, L = 600, 14.0
xg = np.linspace(-L / 2, L / 2, Ng); d = xg[1] - xg[0]
D2 = (np.diag(np.ones(Ng - 1), 1) + np.diag(np.ones(Ng - 1), -1) - 2 * np.eye(Ng)) / d ** 2
Wnl = rng.normal(size=(Ng, 12)); Vnl = 0.05 * Wnl @ Wnl.T * np.exp(-xg[:, None] ** 2 / 4) * np.exp(-xg[None, :] ** 2 / 4)  # nonlocal, Hermitian
Hm = -D2 / 2 + np.diag(xg ** 2 / 2) + Vnl
Ev, Um = np.linalg.eigh(Hm)
P2m = Um.T @ (-D2) @ Um
Vtot = Um.T @ (np.diag(xg ** 2 / 2) + Vnl) @ Um
offd = ~np.eye(8, dtype=bool)
check("CW7-C12c", np.max(np.abs((P2m[:8, :8] + 2 * Vtot[:8, :8])[offd])) < 1e-9 * np.max(np.abs(P2m[:8, :8])),
      "LE-155 replacement check: <c|p^2|v> = -2m<c|V|v> (c != v) exact for a NONLOCAL V (max rel. dev %.0e)" %
      (np.max(np.abs((P2m[:8, :8] + 2 * Vtot[:8, :8])[offd])) / np.max(np.abs(P2m[:8, :8]))))
Ng, L = 900, 14.0
xg = np.linspace(-L / 2, L / 2, Ng); d = xg[1] - xg[0]
D2 = (np.diag(np.ones(Ng - 1), 1) + np.diag(np.ones(Ng - 1), -1) - 2 * np.eye(Ng)) / d ** 2
Vn = xg ** 2 / 2 + 0.1 * xg ** 4
Ev, U_ = np.linalg.eigh(-D2 / 2 + np.diag(Vn))
amp = U_.T @ (-D2 @ U_[:, 0])
ratio13 = np.sum((Ev - Ev[0]) * amp ** 2) / (2 * np.sum(U_[:, 0] ** 2 * (xg + 0.4 * xg ** 3) ** 2))
check("CW7-C13", abs(ratio13 - 1) < 0.003, "LE-155 anharmonic 1D (regular V): sum_f (E_f-E_0)|<f|p^2|0>|^2 / (2m<V'^2>) = %.4f" % ratio13)

# ---------------- LE-156: magnon nuisance numbers ----------------
nk = 40
kk = (np.arange(nk) + 0.5) * 2 * np.pi / nk
KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing="ij")
gam = (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
dS = np.mean((1 / np.sqrt(1 - gam ** 2) - 1) / 2)
r2m = {S: dS * (1 + dS) / (S * (1 + 2 * dS)) for S in (0.5, 1.5, 2.5)}
check("CW7-C14", abs(dS - 0.0782) < 0.0005 and abs(r2m[0.5] - 0.1458) < 0.0005,
      "LE-156 simple-cubic AFM LSWT: Delta S = %.4f; r_2m = %.4f (S=1/2), %.4f (3/2), %.4f (5/2)" % (dS, r2m[0.5], r2m[1.5], r2m[2.5]))
S_, d_ = sp.symbols("S DeltaS", positive=True)
n2 = d_ * (1 + 2 * d_)                                  # <n^2> in the Bogoliubov vacuum (Wick, same-site <aa> = 0)
Wperp_exact = S_ * (S_ + 1) - (S_ ** 2 - 2 * S_ * d_ + n2)   # S(S+1) - <(S - n)^2>
Wperp_lswt = S_ * (1 + 2 * d_)
rel = sp.simplify((Wperp_lswt - Wperp_exact) / Wperp_lswt)
check("CW7-C14b", sp.simplify(Wperp_exact - (S_ - d_) * (1 + 2 * d_)) == 0 and sp.simplify(rel - d_ / S_) == 0,
      "LE-156 r^M derived: Casimir S(S+1) = W_perp + <(S^z)^2> gives W_perp = (S - DeltaS)(1 + 2 DeltaS); LSWT S(1 + 2 DeltaS) overstates it by DeltaS/S "
      "= %.3f, %.3f, %.3f at S = 1/2, 3/2, 5/2 (one r^M for WP6 and WP8-F)" % (dS / 0.5, dS / 1.5, dS / 2.5))

# ---------------- LE-157: SC one-sided nuisance (one threshold convention) ----------------
yK, kkinf, kcut = np.array([2.2, 2.5, 3, 5, 10]), np.array([1.42, 0.88, 0.53, 0.16, 0.04]), np.array([1.04, 0.57, 0.30, 0.07, 0.01])
ymask = lambda col: math.exp(np.interp(math.log(0.3), np.log(col[::-1]), np.log(yK[::-1])))
yk, yc = ymask(kkinf), ymask(kcut)
sig5, sig10 = 0.16 - 0.07, 0.04 - 0.01
th_ = np.linspace(-6, 6, 12001)
tgt = 2 * 2.303                              # zero observed events: -2 ln L = 2 mu; theta = 0 limit mu = 2.303 (Poisson 90%)
lims = []
for sg in (sig5, sig10):
    lo, hi = 0.1, 20.0
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if np.min(2 * mid * np.exp(-np.abs(th_) * sg) + th_ ** 2) < tgt else (lo, mid)
    lims.append(lo)
check("CW7-C15", abs(yk - 3.82) < 0.01 and abs(yc - 3.0) < 0.01 and all(l >= 2.303 - 1e-6 for l in lims) and abs(sig5 - 0.09) < 1e-12,
      "LE-157: mask |dL/L| > 0.3 at y < %.2f (KK-inf column, defines the mask) vs %.2f (cut column); sigma_BCS %.2f/%.2f; profiled limits %.3f, %.3f >= 2.303 "
      "(one convention: Poisson 90%%, Delta(-2lnL) = 4.605 at n = 0)" % (yk, yc, sig5, sig10, lims[0], lims[1]))

# ---------------- LE-160: r_mat with signed elasticities ----------------
a_, b_, r__ = sp.symbols("a b r", real=True)
vs = a_ ** 2 + b_ ** 2 + 2 * r__ * a_ * b_        # Var(sum) / (s delta)^2 with signed elasticities a, b
vr = a_ ** 2 + b_ ** 2 - 2 * r__ * a_ * b_        # Var ln(ratio)
ok = True
for (av, bv) in ((0.3, 0.2), (0.3, -0.2), (-0.1, -0.4), (0.25, -0.25)):
    f_s = [float(vs.subs({a_: av, b_: bv, r__: rv})) for rv in (0, 1)]
    f_r = [float(vr.subs({a_: av, b_: bv, r__: rv})) for rv in (0, 1)]
    same = av * bv > 0
    ok &= (np.argmax(f_s) == (1 if same else 0)) and (np.argmax(f_r) == (0 if same else 1))
check("CW7-C16", ok, "LE-160: over r_mat in [0,1] the sum variance is maximal at r = 1 and the ratio variance at r = 0 ONLY for same-sign elasticities; "
      "opposite signs swap both (VER-CW7 §B7)")

# ---------------- LE-176: soft-mode eps_0 insensitivity ----------------
dlt = lambda ei, e0: 1 / ei - 1 / e0
pbte = [abs(dlt(26.3, e) / dlt(26.3, 498.585) - 1) for e in (1000.0, 1e12)]
ktao = abs(dlt(5.428, 5000.0) / dlt(5.428, 385.935) - 1)
pbs = abs(dlt(15.0, 1e12) / dlt(15.0, 160.533) - 1)
sto = abs(dlt(6.345, 2e4) / dlt(6.345, 9.963) - 1)
check("CW7-C17", abs(pbte[0] - 0.0279) < 0.0002 and abs(pbte[1] - 0.0557) < 0.0002 and abs(ktao - 0.0132) < 0.0002 and abs(pbs - 0.1031) < 0.0002 and abs(sto - 1.753) < 0.002,
      "LE-176 POL weight shift DFPT -> measured: PbTe %.3f (eps_0 = 1000) to %.3f (-> inf), KTaO3 %.3f, PbS %.3f (-> inf); SrTiO3 x%.2f"
      % (pbte[0], pbte[1], ktao, pbs, 1 + sto))
wT, ei, Sosc = sp.symbols("omega_T epsilon_inf S_osc", positive=True)
e0_model = ei + Sosc / wT ** 2                   # rigid-ion one-mode model: eps_0 = eps_inf + S_osc/omega_T^2
wL2_model = wT ** 2 * e0_model / ei              # LST
check("CW7-C18", sp.limit(wL2_model, wT, 0) == Sosc / ei and sp.limit(e0_model, wT, 0) == sp.oo,
      "LE-176 rigid-ion model: eps_0 -> inf as omega_T -> 0 while omega_L^2 -> S_osc/eps_inf (finite): omega_L, eps_inf, Z* regular")


# ---------------- LE-177: cosmogenic activity; 210Pb ----------------
def frac_beta_below(Q, Z, Ecut=1.0, n=200001):
    me = 511.0
    T = np.linspace(1e-7, Q, n)
    W = T / me + 1
    p = np.sqrt(W ** 2 - 1)
    etaF = Z / 137.036 * W / p
    F = 2 * np.pi * etaF / (1 - np.exp(-2 * np.pi * etaF))
    s = F * p * W * (Q - T) ** 2
    cdf = np.concatenate([[0], np.cumsum((s[1:] + s[:-1]) / 2 * np.diff(T))])
    return np.interp(Ecut, T, cdf) / cdf[-1]


f3 = frac_beta_below(18.591, 2)
lam3 = math.log(2) / (12.32 * 365.25)
A100 = 124 * (1 - math.exp(-lam3 * 100))
check("CW7-C19", abs(f3 - 0.0892) < 0.0003 and abs(A100 * f3 - 0.169) < 0.001 and abs(124 * f3 - 11.06) < 0.03,
      "LE-177: f_<1keV(3H) = %.4f computed (allowed shape x Fermi, Z = 2); Si 3H sub-keV rate %.3f (100 d), %.2f (saturation) /(kg d keV)" % (f3, A100 * f3, 124 * f3))
fpb, fbi = frac_beta_below(63.5, 83), frac_beta_below(1162.0, 84)
rpb = 86400 * (0.16 * fpb + fbi)
ch4 = json.load(open(os.path.join(HERE, "data", "v4_changes.json")))["Pb210"]
check("CW7-C35", abs(rpb - ch4["rate_per_Bq"]) / rpb < 0.01 and 1e-3 < 1 / rpb < 2e-3,
      "Pb salts (REF-WP8-S-A §8): 210Pb + 210Bi in equilibrium give %.0f /(kg d keV) below 1 keV per Bq/kg (f = %.4f g.s. branch, %.5f Bi) [E, scheme UNVERIFIED]; "
      "S4 needs a(210Pb) <~ %.1e Bq/kg" % (rpb, fpb, fbi, 1 / rpb))

# ---------------- WP8-F-v3 corrections ----------------
# C20 (replaces the hand-written sympy identity): Migdal Q_Mig at the plasmon pole and the f-sum bound
w_, wp, Eg = sp.symbols("omega omega_p E_g", positive=True)
Qpole = sp.integrate(sp.pi / 2 * wp * sp.DiracDelta(w_ - wp) / w_ ** 4, (w_, 0, sp.oo))
ww = np.linspace(1e-3, 200, 400001)
okb = True
for egv, w0, gm in ((1.1, 4.0, 2.0), (14.2, 20.0, 6.0), (8.8, 25.0, 9.0)):
    Lm = np.where(ww > egv, ww * gm / ((ww ** 2 - w0 ** 2) ** 2 + (ww * gm) ** 2), 0.0)
    Lm *= (np.pi / 2) * w0 ** 2 / np.trapezoid(ww * Lm, ww)          # f-sum normalised: int omega L = (pi/2) omega_p^2, omega_p = w0
    okb &= np.trapezoid(Lm / ww ** 4, ww) <= (np.pi / 2) * w0 ** 2 / egv ** 5
nuc = {"LiF": (1 ** 2 + 7 ** 2) / (6.94 + 18.998), "Si": 4 ** 2 / 28.085}
pole_ratio = (26.1 / 16.6) ** 3
net = nuc["LiF"] / nuc["Si"] / pole_ratio
check("CW7-C20", sp.simplify(Qpole - sp.pi / (2 * wp ** 3)) == 0 and okb and abs(pole_ratio - 3.89) < 0.01 and abs(net - 0.87) < 0.01,
      "WP8-F-v3 (2.7''): plasmon pole int L/omega^4 = (pi/2) omega_p^-3; f-sum bound int L/omega^4 <= (pi/2) omega_p^2/E_g^5 on 3 model ELFs; "
      "nuclear factor LiF/Si %.2f x pole Q ratio 1/%.2f = %.2f (the nuclear-factor order is not the Migdal order)" % (nuc["LiF"] / nuc["Si"], pole_ratio, net))
# C21: (2.3c) derived from the two-site cell (A-§E(a)), not only its angle average
q, a, M1, M2, mp, wLO, Om = sp.symbols("q a M1 M2 m_p omega_LO Omega_c", positive=True)
A1s, A2s = M1 / mp, M2 / mp
Mc = M1 + M2
nq = sp.Matrix(sp.symbols("n1 n2 n3", real=True))
r2 = a * sp.Matrix([1, 1, 1]) / 4
e1, e2 = sp.sqrt(M2 / Mc), -sp.sqrt(M1 / Mc)            # LO eigenvector amplitudes along q (mass-weighted, normalised)
ph_ = q * (nq.T * r2)[0]
amp = q * (A1s * e1 / sp.sqrt(M1) + A2s * e2 / sp.sqrt(M2) * sp.exp(sp.I * ph_))
amp2 = sp.expand(sp.simplify(amp * sp.conjugate(amp)).subs({nq[0]: 0, nq[1]: 0, nq[2]: 1}))   # q along z: (q.r2)^2 = q^2 a^2/16 = angle average q^2|r2|^2/3
amp2_avg = sp.expand(sp.series(sp.expand(amp2.rewrite(sp.cos)), q, 0, 5).removeO())
S_LO = 2 * sp.pi / Om * amp2_avg / (2 * wLO)
S_eq31 = 2 * sp.pi / Om * q ** 4 * a ** 2 * (M1 / mp) * (M2 / mp) / (32 * wLO * mp * (M1 / mp + M2 / mp))
check("CW7-C21", sp.simplify(S_LO - S_eq31) == 0,
      "WP8-F-v3 (2.3c) derived: two-site cell, c_kappa = A_kappa = M_kappa/m_p, LO eigenvector, intra-cell phase -> S_LO = (2pi/Omega) q^4 a^2 A1A2/(32 omega_LO m_p (A1+A2)) "
      "= 2205.02250 Eq. (31); the q^2 term cancels identically for A prop. to M")
wD = sp.symbols("omega_D", positive=True)
D = 3 * w_ ** 2 / wD ** 3
jens = sp.simplify(sp.integrate(D * w_, (w_, 0, wD)) * sp.integrate(D / w_, (w_, 0, wD)))
check("CW7-C22", jens == sp.Rational(9, 8), "WP8-F §2.4: Debye DOS <omega><omega^-1> = 9/8 (2W uses <omega^-1>, Jensen)")


# C23 (A-§E(c) as requested): per-branch light-mediator weight K(omega; m) = int dq/q eta(v_min) for sapphire at 2-3x the 112 meV edge
def Kpol(om, m, n=4000):
    s2 = 1 - 2 * om / (m * VMAX ** 2)
    if s2 <= 0:
        return 0.0
    s1 = math.sqrt(s2); qq = np.geomspace(m * VMAX * (1 - s1), m * VMAX * (1 + s1), n)
    return np.trapezoid(eta(om / qq + qq / (2 * m)) / qq, qq)


edge = 2 * 0.1124 / VMAX ** 2
Kr = {fac: Kpol(0.048, fac * edge) / Kpol(0.1124, fac * edge) for fac in (2, 3)}
K1 = Kpol(0.048, 1e6) / Kpol(0.1124, 1e6)
sens = lambda pb: (3.5 + pb) * 0.5 * math.sqrt(1 / 1.05) / (1 - math.sqrt(1 / 1.05))
check("CW7-C23", Kr[2] > 10 and Kr[3] > 5 and 1.3 < K1 < 1.5 and abs(sens(3) - 131.6) < 0.1 and abs(sens(1.5) - 101.2) < 0.1,
      "WP8-F-v3 §2.5: sapphire K(48 meV)/K(112 meV) = %.1f (2x edge = %.0f keV), %.1f (3x), %.2f (1 MeV; ln ratio 1.18): the band-uniform reading fails near the edge; "
      "near-edge log-sensitivity %.1f / %.1f" % (Kr[2], 2 * edge / 1e3, Kr[3], K1, sens(3), sens(1.5)))
Dsw, mxx, vv, qq_ = sp.symbols("D_sw m_chi v q", positive=True)
qmax = [s for s in sp.solve(sp.Eq(Dsw * qq_ ** 2, qq_ * vv - qq_ ** 2 / (2 * mxx)), qq_) if s != 0][0]
check("CW7-C24", sp.simplify(qmax - vv / (Dsw + 1 / (2 * mxx))) == 0, "WP8-F §2.6: FM magnon (omega = D_sw q^2) edge q_max = v/(D_sw + 1/2m_chi)")
einf_, e0_ = 10.89, 12.9
s_inf, s_0 = -e0_ / (e0_ - einf_), einf_ / (e0_ - einf_)
dZ = 2 - (1 - einf_ / e0_)
check("CW7-C25", abs(abs(s_inf) - 6.418) < 0.001 and abs(s_0 - 5.418) < 0.001 and abs(math.sqrt(e0_ / einf_) - 1.0884) < 0.0001 and abs(dZ - 1.8442) < 0.0001,
      "WP8-F POL sensitivities (GaAs): %.3f, %.3f; LST ratio %.4f; dln I/dln Z* (fixed omega_T) = %.4f" % (s_inf, s_0, math.sqrt(e0_ / einf_), dZ))
ZA = {"Pb": 82 / 207.2, "H2O": 10 / 18.015, "LiH": 4 / 7.949}
check("CW7-C26", ZA["Pb"] < 0.40 and ZA["H2O"] > 0.5 and ZA["LiH"] > 0.5, "WP8-F Z/A outside [0.40, 0.50]: Pb %.3f, H2O %.3f, LiH %.3f" % (ZA["Pb"], ZA["H2O"], ZA["LiH"]))


# C27 (replaces the solve-for-the-symbol floor): single-LA-phonon rate per mass, SHM eta, Theta(c q >= omega_th), q <= q_top (Gamma-X)
def nr1(c_kms, qtop, m, light, wth=1e-3, n=6000):
    c = c_kms / CKMS
    qlo, qhi = wth / c, min(qtop, 2 * m * (VMAX - c))
    if qhi <= qlo:
        return 0.0
    qv = np.geomspace(qlo, qhi, n)
    F2 = (1 / qv ** 4) if light else 1.0
    return np.trapezoid(qv * F2 * eta(c + qv / (2 * m)) * qv / c, qv)    # q F^2 eta x (pi q/(m_u^2 c)) / q  [per-mass, constants dropped]


qSi, qCsI = 2 * math.pi * 1973.27 / 5.431, math.pi * 1973.27 / 4.567      # eV (Gamma-X), a_exp [FT 1910.10716 Table III]
light = {m: nr1(1.379, qCsI, m, True) / nr1(8.757, qSi, m, True) for m in (0.3e6, 1e6, 10e6)}
heavy = nr1(1.379, qCsI, 0.3e6, False) / nr1(8.757, qSi, 0.3e6, False)
# derived large-m_chi light-mediator ratio: rate prop. to (1/omega_th - 1/(c q_top)) (c cancels in the leading term)
pred = (1 - 1e-3 / (1.379 / CKMS * qCsI)) / (1 - 1e-3 / (8.757 / CKMS * qSi))
check("CW7-C27", abs(light[10e6] / pred - 1) < 0.02 and all(0.5 < x < 1.0 for x in light.values()) and abs(heavy / (8.757 / 1.379) - 1) < 0.05,
      "WP8-F-v3 §2.3 (REF-WP8-S-B E1): light-mediator 1-phonon rate CsI/Si = %.2f, %.2f, %.2f at 0.3, 1, 10 MeV vs derived (1 - w_th/(c q_top)) ratio %.3f "
      "(not 1/c = 6.35; 1910.10716 Eq. (35)); heavy mediator at 0.3 MeV %.2f (≈ 1/c ratio 6.35, Eq. (37) window)" % (light[0.3e6], light[1e6], light[10e6], pred, heavy))
sic = {"4H": ((97.0, 98.8), (119.5, 120.0), (10.32, 9.76), (6.8, 6.6)), "6H": ((97.7, 98.8), (119.7, 120.3), (10.03, 9.67), (6.7, 6.6))}
dev = [abs((wl_[j] / wt_[j]) ** 2 / (e0s[j] / eis[j]) - 1) for (wt_, wl_, e0s, eis) in sic.values() for j in (0, 1)]
dev.append(abs((120.5 / 98.7) ** 2 / (9.7 / 6.5) - 1))
check("CW7-C28", max(dev) < 0.0125, "WP8-U LST on SiC with (A1 = par, E1 = perp): max residual %.4f" % max(dev))

# ---------------- v4 table integrity (replaces the v3 C29) ----------------
v3r = list(csv.DictReader(open(os.path.join(ROOT, "returns/R16/WP8-U-table-v3.csv"))))
v4r = list(csv.DictReader(open(os.path.join(ROOT, "returns/R16/WP8-U-table-v4.csv"))))
ch = json.load(open(os.path.join(HERE, "data", "v4_changes.json")))
keys = [(x["material"], x["property"]) for x in v4r if re.fullmatch(r"screen_S[123]", x["property"])]
uniq = len(keys) == len(set(keys))
noE = not any("[E]" in x["value"] for x in v4r if re.fullmatch(r"screen_S[123]", x["property"]))
fin = {}
for x in v4r:
    if x["property"] == "verdict":
        fin[x["material"]] = x["value"]
vcol = all(x["verdict"] == fin[x["material"]] for x in v4r if x["material"] in fin)
dropped_ok = len(ch["dropped"]) == 13 and all(any(all(y[k] == d[k] for k in ("material", "property", "value", "note")) for y in v3r) for d in ch["dropped"])
n3 = len(v3r) - 13
kept_ok = all(v4r[i]["material"] == x["material"] and v4r[i]["property"] == x["property"] for i, x in enumerate([y for y in v3r if not any(
    all(y[k] == d[k] for k in ("material", "property", "value", "note")) for d in ch["dropped"])]))
newrows = v4r[n3:]
tag_ok = all(x["tag"] in ("FT", "DB", "E", "D", "GAP", "UNVERIFIED") and (x["source"] or x["tag"] == "GAP") for x in newrows)
check("CW7-C29", uniq and noE and vcol and dropped_ok and kept_ok and tag_ok and len(ch["retagged"]) + 11 == 55,
      "v4 CSV: %d screening keys unique; no [E] screening evidence (44 retagged + 11 dropped = the 55 of VER-CW7 §A); verdict column = final verdict; "
      "13 superseded rows dropped (recorded verbatim); %d new rows tagged" % (len(keys), len(newrows)))
failed = json.load(open(os.path.join(HERE, "data", "failed_ir.json")))
ref_list = {"NaI", "ZnS", "ZnO", "SrTiO3", "LiAlO2", "Bi2Se3", "LiF", "PbTe", "KTaO3", "NaCl", "SiC-3C", "cBN", "PE"}
check("CW7-C30", {f[0] for f in failed} == ref_list | {"InSb"}, "WP8-U vetting rule V2 drops eps_0_DFT for the referees' 13 failed-IR runs + InSb (metallic run)")


# ---------------- C31: the POL eps-route bound as an inequality (replaces the rank.py rerun) ----------------
def modesum(einf, wL, wT):
    """lossless factorised eps: int L domega = sum_nu (pi omega_L,nu/2) Delta_nu, Delta_nu from the partial fractions of 1/eps"""
    wL, wT = np.asarray(wL, float), np.asarray(wT, float)
    tot, Dsum = 0.0, 0.0
    for j, l in enumerate(wL):
        B = np.prod(wT ** 2 - l ** 2) / np.prod([wL[k] ** 2 - l ** 2 for k in range(len(wL)) if k != j]) / einf
        Dn = -B / l ** 2
        tot += math.pi * l / 2 * Dn; Dsum += Dn
    return tot, Dsum


cm = 0.1239842
o_L, o_T = np.array([906.6, 629.5, 481.7, 387.6]) * cm, np.array([633.6, 569.0, 439.1, 385.0]) * cm
e_L, e_T = np.array([881.1, 510.9]) * cm, np.array([582.4, 397.5]) * cm
I_o, D_o = modesum(3.2, o_L, o_T)
I_e, _ = modesum(3.2, e_L, e_T)
e0o, e0e = 3.2 * np.prod((o_L / o_T) ** 2), 3.2 * np.prod((e_L / e_T) ** 2)
I_avg = (2 * I_o + I_e) / 3 / 3.98                                  # (1/3) sum_i L_ii, 1807.10291 Eq. (40)
b_cons = (2 * (1 / 3.2 - 1 / e0o) * o_L.max() + (1 / 3.2 - 1 / e0e) * e_L.max()) / 3 * math.pi / 2 / 3.98
b_81 = (2 * (1 / 3.2 - 1 / e0o) * o_T.max() * math.sqrt(e0o / 3.2) + (1 / 3.2 - 1 / e0e) * e_T.max() * math.sqrt(e0e / 3.2)) / 3 * math.pi / 2 / 3.98
mixed = math.pi / 2 * (1 / 3.26 - 1 / 11.969) * 104.0 / 3.9869
check("CW7-C31", abs(D_o - (1 / 3.2 - 1 / e0o)) < 1e-12 and I_avg <= b_cons <= b_81 and mixed < I_avg,
      "WP8-F-v3 §2.5/§8: sapphire lossless axis-averaged mode sum %.2f <= consistent per-axis bound (same eps pair, omega_L,max) %.2f <= (8.1) %.2f meV cm^3/g; "
      "the R16 mixed-input 'upper' route %.2f is below the mode sum: not a bound (o-ray alone: lossless %.2f; the damped 9.40 adds the O(gamma/omega) tail)"
      % (I_avg, b_cons, b_81, mixed, I_o / 3.98))

# ---------------- C32: literature record ----------------
idf = os.path.join(HERE, "data", "arxiv_verified.json")
ver = json.load(open(idf)) if os.path.exists(idf) else {}
cited = set()
for fn in ("returns/R16/CW7.md", "returns/R16/WP8-U-v2.md", "returns/R16/WP8-F-v2.md", "returns/R16/CW7-errata.md", "returns/R16/WP8-U-v3.md", "returns/R16/WP8-F-v3.md"):
    p = os.path.join(ROOT, fn)
    if os.path.exists(p):
        cited |= set(re.findall(r"(?<![\d.])(\d{4}\.\d{4,5})(?![\d])", open(p).read()))
missing = sorted(i for i in cited if i not in ver)
LIT = os.path.join(ROOT, "literature", "papers-ERR-CW7")
quotes = {"1910.10716": "dependence on the target properties drops out", "1908.06755": "should be accompanied by a 3 H component",
          "1607.04560": "1.1 and 1.3 keV (the energies of the L-shell lines for 65 Zn and 68 Ge"}
qok = all(os.path.exists(os.path.join(LIT, i + ".txt")) and q_ in re.sub(r"\s+", " ", open(os.path.join(LIT, i + ".txt")).read()) for i, q_ in quotes.items())
check("CW7-C32", len(cited) > 0 and not missing and qok,
      "record check (not physics): %d arXiv IDs cited in the R16 CW7 files are API-verified (missing %s); the three ERR-CW7 quotes are in the fetched texts" % (len(cited), missing))

# ---------------- C33-C34: elastic tensors (REF-WP8-S-A §5) ----------------
J = json.load(open(os.path.join(ROOT, "code/WP8-U-TOP/data/jarvis_top.json")))
c4 = json.load(open(os.path.join(HERE, "data", "christoffel_v4.json")))
hexs = [m for m, x in J.items() if x.get("crys") in ("hexagonal", "trigonal") and x.get("elastic_tensor") not in (None, "na") and m in c4]
ident = max(abs(J[m]["elastic_tensor"][3][3] - (J[m]["elastic_tensor"][0][0] - J[m]["elastic_tensor"][0][1]) / 2) for m in hexs)
uni = [m for m, x in c4.items() if x["crys"] in ("hexagonal", "trigonal", "tetragonal")]
deg_new = max(abs(c4[m]["T001"][0] / c4[m]["T001"][1] - 1) for m in uni)
deg_old = sum(1 for m in uni if abs(math.sqrt(J[m]["elastic_tensor"][3][3] / J[m]["elastic_tensor"][4][4]) - 1) > 0.02)
check("CW7-C33", ident < 0.11 and deg_new < 0.01 and deg_old >= 8 and abs(c4["TeO2"]["cLA"] - 4.10) < 0.01,
      "JARVIS shear order is (xy,yz,zx): C66 = (C11-C12)/2 at index 3 for all %d hexagonal/trigonal entries (max dev %.2f GPa); after re-indexing the [001] TA pair "
      "is degenerate to %.1f%% in all %d uniaxial entries (old order broke it in %d); TeO2 c_LA %.3f km/s (REF-WP8-S-A: 4.10)"
      % (len(hexs), ident, 100 * deg_new, len(uni), deg_old, c4["TeO2"]["cLA"]))
# completeness: sum_nu (q.e_nu)^2 = 1 (light mediator branch- and direction-free); heavy scalar reproduces REF-A's 3.77 with the old order
Cj = np.array(J["TeO2"]["elastic_tensor"], float)
IDXo = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]


def C4of(Cv):
    C = np.zeros((3, 3, 3, 3))
    for I, (i, j) in enumerate(IDXo):
        for K, (k, l) in enumerate(IDXo):
            for aa, bb in ((i, j), (j, i)):
                for cc, dd in ((k, l), (l, k)):
                    C[aa, bb, cc, dd] = Cv[I, K]
    return C


nn = rng.normal(size=(4000, 3)); nn /= np.linalg.norm(nn, axis=1)[:, None]
Gm = np.einsum("ijkl,nj,nl->nik", C4of(Cj), nn, nn) * 1e9 / (J["TeO2"]["density"] * 1e3)
wv, Uv = np.linalg.eigh(Gm)
cv = np.sqrt(wv) / 1e3
proj = np.einsum("nk,nkv->nv", nn, Uv) ** 2
c_old = 1 / np.mean(np.sum(proj / cv, axis=1))
check("CW7-C34", np.max(np.abs(proj.sum(1) - 1)) < 1e-12 and abs(c_old - 3.77) < 0.02 and abs(c4["TeO2"]["c_nr1"] - 3.76) < 0.02,
      "NR-1ph scalars: sum_nu (q.e_nu)^2 = 1 (max dev %.0e); TeO2 <sum (q.e)^2/c>^-1 = %.3f with the R16 tensor (REF-WP8-S-A 3.77), %.3f re-indexed; c_LA mean %.3f"
      % (np.max(np.abs(proj.sum(1) - 1)), c_old, c4["TeO2"]["c_nr1"], c4["TeO2"]["cLA"]))

# ---------------- C36: G-F6 incoherence of the SD one-phonon term ----------------
ok = True
for Jn in (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2)):
    mz = [-Jn + k_ for k_ in range(int(2 * Jn) + 1)]
    ok &= sum(mz) == 0 and sp.simplify(sum(x_ ** 2 for x_ in mz) / (2 * Jn + 1) - Jn * (Jn + 1) / 3) == 0
Nsite, Ntr = 64, 4000
pos = rng.uniform(0, 10, (Nsite, 3))
qv = np.array([0.7, 0.0, 0.0])
Sz = rng.choice([-0.5, 0.5], size=(Ntr, Nsite))
coh = np.abs((Sz * np.exp(1j * pos @ qv)[None, :]).sum(1)) ** 2
check("CW7-C36", ok and abs(coh.mean() / (Nsite * 0.25) - 1) < 0.05 and abs(Sz.sum(1).mean()) < 0.5,
      "G-F6: unpolarised spins: Tr J_z = 0, Tr J_z^2/(2J+1) = J(J+1)/3; <|sum_k S_k e^{iq.r_k}|^2> = N<S_z^2> (ratio %.3f): incoherent, no coherent SD one-phonon term"
      % (coh.mean() / (Nsite * 0.25)))

nf = sum(1 for r_ in RES if not r_[1])
print("\n%d/%d PASS, %.1f s" % (len(RES) - nf, len(RES), time.time() - T0))
sys.exit(1 if nf else 0)
