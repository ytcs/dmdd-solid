"""Limit Check 16.8c (lim:16.8c, fig:16-limit-hop): thermally activated hopping and tunneling through one barrier.

Literature forms (Lawrence, arXiv:2409.02820): transition-state theory k Z_r = (kappa/2 pi beta) e^{-beta V} (Eq. (1),
one dimension, Z^dagger = 1); Wigner kappa_W = 1 + (beta w)^2/24 (Eq. (2)); parabolic barrier
kappa_PB = (beta w/2)/sin(beta w/2) (Eq. (3)), divergent at the crossover temperature T_x = w/2 pi; instanton
k Z_r = (2 pi)^(-1/2) (-d^2S/dtau^2)^(1/2) e^{-S(tau)} (Eq. (4), one dimension, Z_inst = 1), with the symmetric Eckart
action S(tau) = 2 tau_c V - tau_c^2 V/tau, tau = beta, tau_c = 2 pi/w (Eq. (69)).  hbar = 1.
Fuller result: the exact quantum rate k Z_r = (1/2 pi) int_0^inf P(E) e^{-beta E} dE (Eq. (71)) with the exact
transmission of V(q) = V sech^2(q/L) (Landau-Lifshitz):
  P(E) = sinh^2(pi k L) / [sinh^2(pi k L) + cosh^2((pi/2) sqrt(8 m V L^2 - 1))],  k = sqrt(2 m E).
Parameters of the source (its Sect. III.1): L = 0.66047 a_0, m = 1836 m_e, V = 72/(m pi^2 L^2) (atomic units);
then w = sqrt(2V/(m L^2)), V/w = 6/pi, 8 m V L^2 = 576/pi^2.
Plotted: approximate/exact against T/T_x.  Grey: classical TST x kappa_PB within 10 % of exact (T >= T_10pb).
Wigner's kappa_W (the first two terms of kappa_PB) is computed for the log only and not drawn.
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
HARTREE_EV = 27.211386
KB = 8.617333e-5

L, m = 0.66047, 1836.0
V = 72.0 / (m * np.pi**2 * L**2)
w = np.sqrt(2 * V / (m * L**2))
Tx = w / (2 * np.pi)
tauc = 2 * np.pi / w
g = np.sqrt(8 * m * V * L**2 - 1)
print(f"V = {V*HARTREE_EV*1e3:.2f} meV, w = {w*HARTREE_EV*1e3:.2f} meV, V/w = {V/w:.4f} (6/pi = {6/np.pi:.4f}), "
      f"T_x = {Tx*HARTREE_EV/KB:.1f} K")


def P(E):
    k = np.sqrt(2 * m * E)
    s = np.sinh(np.pi * k * L)
    c = np.cosh(0.5 * np.pi * g)
    return 1.0 / (1.0 + (c / s)**2) if s > 0 else 0.0


def k_exact(beta):
    f = lambda E: P(E) * np.exp(-beta * (E - V))     # scaled by e^{beta V}
    Emax = V + 60 / beta
    pts = sorted({V, max(V - 5 / beta, 0)})
    return quad(f, 0, Emax, points=pts, limit=400, epsabs=0, epsrel=1e-10)[0] / (2 * np.pi)


def k_cl(beta):
    return 1 / (2 * np.pi * beta)                      # times e^{-beta V}


def kap_w(beta):
    return 1 + (beta * w)**2 / 24


def kap_pb(beta):
    u = beta * w / 2
    return u / np.sin(u)


def k_inst(beta):
    S = 2 * tauc * V - tauc**2 * V / beta
    d2 = 2 * tauc**2 * V / beta**3
    return np.sqrt(d2 / (2 * np.pi)) * np.exp(-(S - beta * V))   # scaled by e^{beta V}


TT = np.geomspace(0.25, 4.0, 300)
beta = 1 / (TT * Tx)
ex = np.array([k_exact(b) for b in beta])
cl = np.array([k_cl(b) for b in beta])
rW = cl * kap_w(beta) / ex
rPB = np.where(TT > 1, cl * kap_pb(np.minimum(beta, 0.999 / Tx)) / ex, np.nan)
rI = np.where(TT < 1, np.array([k_inst(b) for b in beta]) / ex, np.nan)
for tt in (0.5, 1.0, 1.5, 2.0, 3.0):
    b = 1 / (tt * Tx)
    print(f"T/T_x = {tt}: exact/classical = {k_exact(b)/k_cl(b):.3f}; Wigner/exact = {k_cl(b)*kap_w(b)/k_exact(b):.3f}; "
          + (f"parabolic/exact = {k_cl(b)*kap_pb(b)/k_exact(b):.3f}; " if tt > 1 else "")
          + (f"instanton/exact = {k_inst(b)/k_exact(b):.3f}" if tt < 1 else ""))
T10 = brentq(lambda tt: k_cl(1/(tt*Tx)) * kap_w(1/(tt*Tx)) / k_exact(1/(tt*Tx)) - 0.9, 1.0, 4.0)
T10pb = brentq(lambda tt: k_cl(1/(tt*Tx)) * kap_pb(1/(tt*Tx)) / k_exact(1/(tt*Tx)) - 1.1, 1.01, 4.0)
T10cl = brentq(lambda tt: k_cl(1/(tt*Tx)) / k_exact(1/(tt*Tx)) - 0.9, 1.0, 30.0)
print(f"Wigner within 10 % for T >= {T10:.3f} T_x; parabolic within 10 % for T >= {T10pb:.3f} T_x; "
      f"classical TST within 10 % for T >= {T10cl:.2f} T_x")
for tt in (0.25, 0.3, 0.4):
    b = 1 / (tt * Tx)
    print(f"  instanton/exact at T/T_x = {tt}: {k_inst(b)/k_exact(b):.3f}")
# leading correction: next term of kappa_PB, 7 u^4/360 with u = beta w/2
for tt in (2.0, 3.0):
    b = 1 / (tt * Tx); u = b * w / 2
    print(f"  T/T_x = {tt}: kappa_PB - kappa_W = {kap_pb(b) - kap_w(b):.4f}; 7u^4/360 = {7*u**4/360:.4f}")

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.axvspan(T10pb, TT[-1], color="0.88", lw=0)
ax.plot(TT, cl / ex, "k-", lw=1.0, label=r"classical, $\kappa = 1$")
ax.plot(TT, rPB, "C3", lw=1.4, label=r"parabolic $\kappa_{\mathrm{PB}}$")
ax.plot(TT, rI, "C2", lw=1.4, label="instanton")
ax.axvline(1, color="0.5", lw=0.6, ls=":")
ax.axhline(1, color="k", lw=0.6)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(TT[0], TT[-1]); ax.set_ylim(1e-3, 3)
from matplotlib.ticker import NullFormatter, FixedLocator
ax.xaxis.set_major_locator(FixedLocator([0.25, 0.5, 1, 2, 4])); ax.set_xticklabels(["0.25", "0.5", "1", "2", "4"])
ax.xaxis.set_minor_formatter(NullFormatter())
ax.set_xlabel(r"$T/T_\times$")
ax.set_ylabel("approximate / exact rate")
ax.legend(frameon=False, fontsize=7.5, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_8c.pdf"))
print("saved limit16_8c.pdf")
