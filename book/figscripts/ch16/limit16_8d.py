"""Limit Check 16.8d (lim:16.8d, fig:16-limit-heat): heat release of a glass cooled from T_hi to T_lo.

Literature form: Qdot = (pi^2/24) Pbar V (T_hi^2 - T_lo^2)/t (Sahling et al., arXiv:1610.03974, Eq. (6), with
k_B = 1), for a distribution flat in the asymmetry Delta_as and the tunneling parameter lambda (its Eq. (1)).
Fuller result (model, Sect. 16.8): the same flat distribution, cut at lambda_min <= lambda <= lambda_max, with
Delta0 = Omega0 e^{-lambda}, E = sqrt(Delta_as^2 + Delta0^2) (the exact energy, not E ~ Delta_as), the one-phonon rate
Gamma_1 = A E Delta0^2 coth(E/2T_lo) at the final temperature (eq:16.8-jackle written as A E Delta0^2 coth), and the
instantaneous quench: each defect starts in equilibrium at T_hi and relaxes exponentially to equilibrium at T_lo,
releasing (E/2)[tanh(E/2T_lo) - tanh(E/2T_hi)]:
  Qdot(t) = V Pbar int dDelta_as int dlambda (E/2)[tanh(E/2T_lo) - tanh(E/2T_hi)] Gamma_1 e^{-Gamma_1 t}.
Units: energies in T_hi, time in tau_min = 1/(A T_hi Omega0^2 e^{-2 lambda_min}), the relaxation time of the fastest
defect at E = T_hi.  Model choices (stated in the caption): T_lo/T_hi = 1/480 (10 mK after a quench from 4.8 K),
Omega0 e^{-lambda_min} = 0.1 T_lo, lambda_max - lambda_min = 14.  The plateau value does not depend on A or Omega0.
Plotted: t Qdot / [(pi^2/24) V Pbar (T_hi^2 - T_lo^2)] against t/tau_min.  Grey: within 10 % of one.
"""
import os
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")

Thi, Tlo = 1.0, 1.0 / 480
D0max = 0.1 * Tlo
DL = 14.0                     # lambda_max - lambda_min


def excess(E):
    return 0.5 * E * (np.tanh(E / (2 * Tlo)) - np.tanh(E / (2 * Thi)))


def lam_integral(E, t, D0max_):
    """int dlambda Gamma e^{-Gamma t} over lambda in [0, DL] with Delta0 = D0max e^{-lambda} (lambda from lambda_min).
    Gamma = a e^{-2 lambda}, a = E D0max^2 coth(E/2T_lo)/(A T_hi D0max^2 units) -> in units of 1/tau_min:
    tau_min^-1 = T_hi * D0max^2  (A = 1)."""
    a = E * D0max_**2 / np.tanh(E / (2 * Tlo)) / (Thi * D0max_**2)   # in units of 1/tau_min
    # int_0^DL dl a e^{-2l} exp(-a e^{-2l} t) = [exp(-a t e^{-2 DL}) - exp(-a t)]/(2 t)
    return (np.exp(-a * t * np.exp(-2 * DL)) - np.exp(-a * t)) / (2 * t)


def qdot_model(t):
    """Integral over Delta_as >= 0 with E = sqrt(Delta_as^2 + Delta0^2); Delta0 <= D0max << T_lo, so the E-shift is
    kept through a second lambda-dependent correction computed exactly below."""
    def inner(das):
        # exact: integrate over lambda numerically with E depending on Delta0
        def f(l):
            D0 = D0max * np.exp(-l)
            E = np.sqrt(das**2 + D0**2)
            G = E * D0**2 / np.tanh(E / (2 * Tlo)) / (Thi * D0max**2)
            return excess(E) * G * np.exp(-G * t)
        return quad(f, 0, DL, limit=200, epsrel=1e-8, epsabs=0)[0]
    pts = [Tlo, 10 * Tlo, Thi]
    return quad(inner, 0, 40 * Thi, points=pts, limit=400, epsrel=1e-7, epsabs=0)[0]


stm = (np.pi**2 / 24) * (Thi**2 - Tlo**2)
check = quad(excess, 0, 60 * Thi, points=[Tlo, Thi], limit=400)[0]
print(f"stored energy per unit Pbar V per unit lambda: {check:.6f} vs pi^2 (T_hi^2 - T_lo^2)/12 = {np.pi**2*(Thi**2-Tlo**2)/12:.6f}")
tt = np.geomspace(1e-2, 1e18, 121)
r = np.array([t * qdot_model(t) / stm for t in tt])
i_in = np.where(np.abs(r - 1) < 0.1)[0]
lo = brentq(lambda lt: 10**lt * qdot_model(10**lt) / stm - 0.9, -2, 6)
hi = brentq(lambda lt: 10**lt * qdot_model(10**lt) / stm - 0.9, 8, 18)
print(f"within 10 %: {10**lo:.3g} <= t/tau_min <= {10**hi:.3g} (window width {hi-lo:.2f} decades; "
      f"e^(2 x 14) = {np.exp(28):.3g})")
mid = 10**(0.5 * (lo + hi))
print(f"plateau value at t = {mid:.3g} tau_min: {mid*qdot_model(mid)/stm:.5f}")
for t in (1e0, 1e2, 1e4, 1e8, 1e12, 1e14, 1e16):
    print(f"  t/tau_min = {t:.0e}: t Qdot/STM = {t*qdot_model(t)/stm:.4f}")
# slowest relevant defect: E ~ T_lo, lambda_max
amin = 2 * Tlo * np.exp(-2 * DL) / Thi
print(f"  rate of the slowest defect carrying energy (E ~ 2 T_lo, lambda_max): {amin:.3g} / tau_min -> 1/rate = {1/amin:.3g}")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.axvspan(10**lo, 10**hi, color="0.88", lw=0)
ax.plot(tt, r, "C3", lw=1.5, label="flat distribution, cut in $\\lambda_{\\mathrm{tun}}$")
ax.axhline(1, color="k", lw=0.8, label=r"$(\pi^2/24)\bar P\mathcal{V}(T_{\mathrm{hi}}^2 - T_{\mathrm{lo}}^2)/t$")
ax.set_xscale("log")
ax.set_xlim(tt[0], tt[-1]); ax.set_ylim(0, 1.15)
ax.set_xlabel(r"$t/\tau_{\min}$")
ax.set_ylabel(r"$t\,\dot Q_{\mathrm{TLS}}$ / literature form")
ax.legend(frameon=False, fontsize=7.5, loc="lower center")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_8d.pdf"))
print("saved limit16_8d.pdf")
