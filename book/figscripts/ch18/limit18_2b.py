"""Limit Check 18.2b (lim:18.2b, fig:18-limit-rpp) and Worked example 18.2 (we:18-rpp): the random-parking (Renyi) limit.
Log: limit18_2b.log.  Run: python limit18_2b.py > limit18_2b.log  (about 3 min).  Solver: mom18_2.py.

Random parking of unit cars on a line (Renyi 1958) is the cascade of Sect. 18.1 with a constant electron density of states,
a delta-function hole density of states (narrow valence band), theta_ii = 1 and no phonons (Subashiev and Luryi,
arXiv:0911.1532, Sect. I).  Exact values used for comparison, all evaluated here with mpmath (30 digits):
  rho_inf = int_0^inf exp(-2 beta(t)) dt,  beta(t) = int_0^t (1 - e^-u)/u du  (0911.1532 Eqs. (17), (23); printed 0.7475987...);
  jammed gap law G(g) = 2 int_0^inf t exp(-g t - 2 beta(t)) dt on 0 <= g <= 1 (0911.1532 Eq. (19));
  F_unc = Var g/(1 + <g>)^2, the uncorrelated final-state ("renewal") value (0911.1532 Eq. (7); printed 0.0439766...);
  F_exact = 2 rho_inf - 1 - (2/rho_inf) int_0^inf (rho_inf - rho(t))^2 e^{2 beta(t)} A(t) dt, rho(t) = int_0^t e^{-2beta},
            A(t) = e^{-t} (e^{-t} + t - 1)/t^2  (0911.1532 Eqs. (44)-(45); printed 0.0510387...).
Cascade solver: lam_ph = 0 by the moment recursions on h = 0.01 and 0.005 with linear Richardson extrapolation (the scheme is O(h)
without phonons); with phonons, lam_ph from 1e-3 to 10 at the silicon w_ph = 0.063/1.160 (interpolated in w over commensurate
nodes; X = 40, or 60 for lam_ph > 5).  Plot: F_eh/F_exact and (1/eps)/rho_inf against lam_ph; shaded where both are within 10 %.
"""
import os
import sys
import time
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mom18_2 import Cascade, run

OUT = os.path.abspath(os.path.join(HERE, "..", "..", "tex", "figures", "ch18"))
t0 = time.time()
mp.mp.dps = 30

beta = lambda t: mp.euler + mp.log(t) + mp.e1(t) if t > 0 else mp.mpf(0)   # Ein(t)
rho_inf = mp.quad(lambda t: mp.exp(-2 * beta(t)), [0, 1, 10, mp.inf])
print("rho_inf = %s  (printed in 0911.1532 Eq. (23): 0.7475987)" % mp.nstr(rho_inf, 12))
print("eps/E_g = 1/rho_inf = %s" % mp.nstr(1 / rho_inf, 10))


def gmom(k):
    """int_0^1 g^k G(g) dg with G(g) = 2 int t exp(-g t - 2 beta(t)) dt."""
    def inner(t):
        return mp.quad(lambda g: g**k * mp.exp(-g * t), [0, 1])
    return mp.quad(lambda t: 2 * t * mp.exp(-2 * beta(t)) * inner(t), [0, 1, 10, 100, mp.inf])


m0, m1, m2 = gmom(0), gmom(1), gmom(2)
gbar = m1 / m0
varg = m2 / m0 - gbar**2
Func = varg / (1 + gbar)**2
print("gap law: int G = %s (= rho_inf), int (1+g) G = %s (= 1)" % (mp.nstr(m0, 12), mp.nstr(m0 + m1, 12)))
print("<g> = %s, Var g = %s, F_unc = Var g/(1+<g>)^2 = %s  (printed in 0911.1532: 0.0439766)" %
      (mp.nstr(gbar, 10), mp.nstr(varg, 10), mp.nstr(Func, 10)))
print("mean gap per car <g> = residual energy per pair; check 1 + <g> - 1/rho_inf = %s; per terminal electron (two per pair, "
      "the hole has zero residual): rbar_c = <g>/2 = %s" % (mp.nstr(1 + gbar - 1 / rho_inf, 3), mp.nstr(gbar / 2, 6)))

rho_t = lambda t: mp.quad(lambda u: mp.exp(-2 * beta(u)), [0, t])


def Afun(t):
    if t < mp.mpf("1e-6"):
        return mp.mpf(1) / 2
    return mp.exp(-t) * (mp.exp(-t) + t - 1) / t**2


def integrand(t):
    rt = rho_inf - rho_t(t)
    return rt**2 * mp.exp(2 * beta(t)) * Afun(t)


I44 = mp.quad(integrand, [0, 1, 5, 20, 60])
tail = mp.quad(integrand, [60, 200])
Fexact = 2 * rho_inf - 1 - 2 / rho_inf * (I44 + tail)
print("F_exact (Eq. (44)) = %s  (printed in 0911.1532 Eq. (2): 0.0510387; tail beyond t = 60 contributes %s)" %
      (mp.nstr(Fexact, 10), mp.nstr(2 / rho_inf * tail, 3)))
print("F_unc/F_exact = %s" % mp.nstr(Func / Fexact, 6))
print("nearest-neighbour value quoted by 0911.1532 p.5: F_unc + 0.007685 = %s (printed 0.05208)" % mp.nstr(Func + 0.007685, 6))
print("printed F_unc 0.0439766 + 0.007685 = %.5f" % (0.0439766 + 0.007685))
rho_inf_f, Fexact_f, Func_f = float(rho_inf), float(Fexact), float(Func)

# cascade solver, lam_ph = 0 (RPP kernel), Richardson in h
def rpp(h, lam=0.0, w=None, X=30.0):
    c = Cascade(lam, w if w else 0.05, X=X, h=h, a=(0.0, 0.0), hole_delta=True, theta=1.0, phonon=(lam > 0))
    return c.slopes()


r1, r2 = rpp(0.01), rpp(0.005)
rich = {k: 2 * r2[k] - r1[k] for k in ("eps", "F", "F_ren", "resid_per_pair")}
print("\nsolver, lam_ph = 0: h = 0.01: 1/eps = %.6f, F = %.6f, F_ren = %.6f;  h = 0.005: %.6f, %.6f, %.6f" %
      (1 / r1["eps"], r1["F"], r1["F_ren"], 1 / r2["eps"], r2["F"], r2["F_ren"]))
print("   Richardson: 1/eps = %.6f (exact %.6f), F = %.6f (exact %.6f), F_ren = %.6f (exact F_unc %.6f), "
      "F_ren/F = %.3f; residual per pair = %.4f E_g (eps - 1 = %.4f)" %
      (1 / rich["eps"], rho_inf_f, rich["F"], Fexact_f, rich["F_ren"], Func_f, rich["F_ren"] / rich["F"],
       rich["resid_per_pair"], rich["eps"] - 1))

# with phonons
EG, OM = 1.160, 0.063
w = OM / EG
lams = [1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0]
rows = []
print("\nRPP kernel with phonons, w_ph = %.5f: lam_ph, 1/eps, (1/eps)/rho_inf, F_eh, F_eh/F_exact, F_ren, F_ren/F_eh" % w)
for lam in lams:
    X = 40.0 if lam <= 5 else 60.0
    # hole_delta kernel through Cascade directly with interpolation in w
    N = 74
    c0 = w * N
    n0 = int(round(c0))
    ks = [n0 - 1, n0, n0 + 1]
    res = [Cascade(lam, k / N, X=X, h=1.0 / N, a=(0.0, 0.0), hole_delta=True, theta=1.0).slopes() for k in ks]
    from mom18_2 import lagrange
    xs = [k / N for k in ks]
    q = {key: lagrange(xs, [rr[key] for rr in res], w) for key in ("eps", "F", "F_ren")}
    rows.append((lam, 1 / q["eps"], q["F"], q["F_ren"]))
    print("  %7.4f  %.5f  %.4f  %.5f  %.4f  %.5f  %.3f" % (lam, 1 / q["eps"], 1 / q["eps"] / rho_inf_f, q["F"], q["F"] / Fexact_f,
                                                          q["F_ren"], q["F_ren"] / q["F"]))
rows = np.array(rows)
base = Cascade(0.0, 0.05, X=40.0, h=1.0 / 74, a=(0.0, 0.0), hole_delta=True, theta=1.0, phonon=False).slopes()
print("same grid (h = 1/74), lam_ph = 0: 1/eps = %.5f (%.2f %% above exact), F = %.5f (%.2f %% above exact)" %
      (1 / base["eps"], 100 * (1 / base["eps"] / rho_inf_f - 1), base["F"], 100 * (base["F"] / Fexact_f - 1)))
print("deviations from the same-grid lam_ph = 0 values: lam_ph, d(1/eps)/(1/eps), dF/F")
for rr in rows:
    print("  %7.4f  %+.4f  %+.4f" % (rr[0], rr[1] * base["eps"] - 1, rr[2] / base["F"] - 1))

# 10 % crossing by root-finding on log lam (linear interpolation of the deviation in log lam is replaced by a fine solve)
def dev(lam):
    N = 74
    c0 = w * N
    n0 = int(round(c0))
    ks = [n0 - 1, n0, n0 + 1]
    from mom18_2 import lagrange
    res = [Cascade(lam, k / N, X=40.0, h=1.0 / N, a=(0.0, 0.0), hole_delta=True, theta=1.0, decomp=False).slopes() for k in ks]
    xs = [k / N for k in ks]
    F = lagrange(xs, [rr["F"] for rr in res], w)
    rho = 1 / lagrange(xs, [rr["eps"] for rr in res], w)
    return max(abs(F / Fexact_f - 1), abs(rho / rho_inf_f - 1)) - 0.10


lo, hi = None, None
for i in range(len(lams) - 1):
    if (max(abs(rows[i, 2] / Fexact_f - 1), abs(rows[i, 1] / rho_inf_f - 1)) - 0.1) * \
       (max(abs(rows[i + 1, 2] / Fexact_f - 1), abs(rows[i + 1, 1] / rho_inf_f - 1)) - 0.1) < 0:
        lo, hi = np.log(lams[i]), np.log(lams[i + 1])
        break
if lo is not None:
    dlo = dev(np.exp(lo))
    for _ in range(25):
        mid = 0.5 * (lo + hi)
        dm = dev(np.exp(mid))
        if dm * dlo > 0:
            lo, dlo = mid, dm
        else:
            hi = mid
    lam10 = np.exp(0.5 * (lo + hi))
    print("\nboth within 10 %% of the random-parking values for lam_ph < %.4f (bisection in ln lam_ph)" % lam10)
else:
    lam10 = None
    print("\nno 10 % crossing in the scanned range")

fig, ax = plt.subplots(figsize=(6.0, 3.8))
if lam10:
    ax.axvspan(lams[0] * 0.5, lam10, color="0.88", lw=0)
L = rows[:, 0]
ax.semilogx(L, rows[:, 2] / Fexact_f, "k-o", ms=3, lw=1.6, label=r"$F_{\mathrm{eh}}/F_{\mathrm{park}}$, cascade with phonons")
ax.semilogx(L, rows[:, 1] / rho_inf_f, "C0-s", ms=3, lw=1.3,
            label=r"$(E_{\mathrm{g}}/\varepsilon_{\mathrm{eh}})/\rho_\infty$, cascade with phonons")
ax.semilogx(L, rows[:, 3] / Fexact_f, "C3--", lw=1.2, label=r"renewal estimate $F_{\mathrm{ren}}/F_{\mathrm{park}}$")
ax.axhline(1.0, color="k", ls=":", lw=1.0)
ax.axhline(Func_f / Fexact_f, color="C3", ls=":", lw=1.0)
ax.text(1.3e-3, Func_f / Fexact_f - 0.025, r"$F_{\mathrm{ren}}/F_{\mathrm{park}} = %.3f$ at $\lambda_{\mathrm{AB}} = 0$" % (Func_f / Fexact_f), fontsize=8, color="C3", va="top")
ax.set_xlim(lams[0] * 0.5, lams[-1] * 1.5)
ax.set_xlabel(r"phonon-loss parameter $\lambda_{\mathrm{AB}}$")
ax.set_ylabel("ratio to the random-parking value")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit18_2b.pdf"))
print("wrote limit18_2b.pdf; %.0f s" % (time.time() - t0))
