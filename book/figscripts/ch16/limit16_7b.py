"""Limit Check 16.7b (lim:16.7b, fig:16-limit-dp): dark-photon absorption on the two-level systems of a glass.
Formula (Sect. 16.7, from Gamma = zeta^2 m L, eq. 10.7-dp, with eps_2 = eps_r tan(delta_0) tanh(m/2T)):
    R = (rho_chi/rho_T) zeta^2 tan(delta_0) tanh(m_phi/2T) / eps_r .
The loss tangent is the electric form of Mueller, Cole, Lisenfeld (arXiv:1705.01108) Eq. (20) at T -> 0,
tan delta_0 = pi P_bar p^2/(3 eps_r) (Heaviside-Lorentz).
Fuller result: L = eps_2/(eps_1^2 + eps_2^2) with eps_1 = eps_r and eps_2 = eps_r tan(delta_0) x [resonant + one-phonon
relaxation] (the ensemble loss of limit16_7a.py, same K).
Inputs: thermal SiO2, tan delta_0 = 3.0e-4 [OC08 Table I, lower end of 3.0-3.3e-4]; eps_r = 3.9 (assumed); rho_T = 2.2 g/cm^3;
rho_chi = 0.3 GeV/cm^3; K from tls16_7.py (gamma_l = 1 eV assumed).  T = 10 mK and 100 mK.
Plotted: zeta for 3 events in 1 kg yr against m_phi.  Shaded: full within 10 % of the formula at 10 mK.
Run: python limit16_7b.py > limit16_7b.log
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import tls16_7 as L

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch16")
K = L.k_jackle()
TAN = L.TAND_THERMAL
EPS = L.EPS_R
EXPO = L.KG * L.YEAR
PRE = L.RHO_CHI / L.RHO_T * EXPO          # events per (zeta^2 L) per kg yr


def rate_formula(m, T):
    return PRE * TAN * np.tanh(m / (2 * T)) / EPS


def rate_full(m, T):
    e2 = EPS * TAN * L.loss_ratio(m, T, K)
    return PRE * e2 / (EPS**2 + e2**2)


print("events per kg yr per zeta^2 at saturation (tanh = 1): %.4e" % (PRE * TAN / EPS))
print("zeta(3 events/kg yr) at saturation: %.4e" % np.sqrt(3 / (PRE * TAN / EPS)))
ms = np.geomspace(1e-10, 1e-3, 120)
Ts = (0.01, 0.1)
cur = {}
for TK in Ts:
    T = TK * L.KELVIN
    ff = np.array([rate_formula(m, T) for m in ms])
    fu = np.array([rate_full(m, T) for m in ms])
    cur[TK] = (np.sqrt(3 / ff), np.sqrt(3 / fu))
    g = lambda lm: rate_full(np.exp(lm), T) / rate_formula(np.exp(lm), T) - 1.1
    m10 = np.exp(brentq(g, np.log(1e-12), np.log(1e-5)))
    cur[(TK, "m10")] = m10
    print("T = %.0f mK: full within 10%% of formula for m_phi > %.4e eV (%.3f MHz); 2T = %.4e eV"
          % (TK * 1e3, m10, m10 / L.GHZ * 1e3, 2 * T))
    for m in (1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4):
        print("   m = %.0e eV: tanh = %.4e, formula = %.4e, full = %.4e /(kg yr zeta^2), ratio %.4f"
              % (m, np.tanh(m / 2 / T), rate_formula(m, T), rate_full(m, T), rate_full(m, T) / rate_formula(m, T)))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.axvspan(cur[(0.01, "m10")], ms[-1], color="0.88", lw=0)
cols = {0.01: "C3", 0.1: "C0"}
for TK in Ts:
    ax.loglog(ms, cur[TK][0], color=cols[TK], ls="--", lw=1.2, label=r"$\tanh$ formula, %d mK" % round(TK * 1e3))
    ax.loglog(ms, cur[TK][1], color=cols[TK], lw=1.5, label=r"resonant + relaxation, %d mK" % round(TK * 1e3))
ax.set_xlim(ms[0], ms[-1])
ax.set_xlabel(r"$m_\phi$ (eV)")
ax.set_ylabel(r"$\zeta$ for 3 events per kg yr")
ax.legend(fontsize=6.5, loc="upper right", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_7b.pdf"))
print("wrote limit16_7b.pdf")
