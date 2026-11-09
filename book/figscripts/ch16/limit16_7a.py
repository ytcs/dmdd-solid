"""Limit Check 16.7a (lim:16.7a, fig:16-limit-tls): the response of an ensemble of two-level systems to a classical
strain or field, Q^-1 = tan delta = pi C tanh(omega/2T) (resonant part; Buchenau arXiv:2012.10139 Eq. (6); Meissner et al.
arXiv:2103.06977 Eqs. (4), (12), (13), (15) with delta Delta_as = 2 gamma S; Mueller, Cole, Lisenfeld arXiv:1705.01108
Eq. (20), electric form at T -> 0).
Fuller result: the standard-tunneling-model ensemble with both the resonant and the relaxation contribution
(arXiv:2103.06977 Eqs. (4), (6), (12), (13)), the relaxation time from one-phonon emission and absorption (Jaeckle;
arXiv:2103.06977 Eq. (7) = arXiv:2012.10139 Eq. (9)), tau^-1 = K E^3 (Delta_0/E)^2 coth(E/2T),
K = (gamma_l^2/v_l^5 + 2 gamma_t^2/v_t^5)/(2 pi rho).  Ratio of the full loss to pi C:
    tanh(w/2T) + (2/pi) int dE (1/2T) sech^2(E/2T) int_0^1 du sqrt(1-u^2)/u  w tau/(1 + w^2 tau^2)
(derived in Sect. 16.7; plateau 1/2 for w tau_min << 1; low-T limit (pi^3/12) K T^3/w, checked below).
Inputs (tls16_7.py): vitreous SiO2, rho = 2200 kg/m^3, v_l = 5800, v_t = 3800 m/s [Bu20 Table I]; gamma_l = 1 eV (assumed),
gamma_l/gamma_t = 1.6 [Zh15].  The curves depend on these only through K.  Frequencies 0.5 GHz and 5 GHz.
Shaded: full loss within 10 % of the tanh law (5 GHz curve); thresholds by root finding.
Run: python limit16_7a.py > limit16_7a.log
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
nus = (0.5, 5.0)
TK = np.geomspace(3e-3, 30, 160)
print("K = %.4e eV^-2" % K)
res = {}
for nu in nus:
    w = nu * L.GHZ
    full = np.array([L.loss_ratio(w, t * L.KELVIN, K) for t in TK])
    res[nu] = full
    f = lambda t: L.loss_ratio(w, t * L.KELVIN, K) / np.tanh(w / (2 * t * L.KELVIN)) - 1.1
    t10 = brentq(f, 1e-2, 30)
    T_low = (0.1 * 6 * w**2 / (np.pi**3 * K))**0.25 / L.KELVIN
    print("nu = %.1f GHz (hbar w/k_B = %.4f K): full within 10%% of tanh for T < %.4f K (low-T estimate "
          "[0.6 w^2/(pi^3 K)]^(1/4) = %.4f K)" % (nu, w / L.KELVIN, t10, T_low))
    res[(nu, "t10")] = t10
    for t in (0.01, 0.1, 1.0, 10.0, 30.0):
        print("   T = %6.3f K: tanh = %.4e, full/(pi C) = %.4e, relaxation part = %.4e"
              % (t, np.tanh(w / (2 * t * L.KELVIN)), L.loss_ratio(w, t * L.KELVIN, K), L.relax_ratio(w, t * L.KELVIN, K)))
# asymptote check
w = 5 * L.GHZ
t = 0.3 * L.KELVIN
print("check low-T relaxation at 5 GHz, 0.3 K: numeric %.4e, (pi^3/12) K T^3 / w = %.4e"
      % (L.relax_ratio(w, t, K), np.pi**3 / 12 * K * t**3 / w))
print("check plateau at 0.5 GHz, 300 K: %.4f (1/2)" % L.relax_ratio(0.5 * L.GHZ, 300 * L.KELVIN, K))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.axvspan(TK[0], res[(5.0, "t10")], color="0.88", lw=0)
cols = {0.5: "C0", 5.0: "C3"}
for nu in nus:
    w = nu * L.GHZ
    ax.loglog(TK, np.tanh(w / (2 * TK * L.KELVIN)), color=cols[nu], ls="--", lw=1.2,
              label=r"$\tanh(\omega/2T)$, %.1f GHz" % nu)
    ax.loglog(TK, res[nu], color=cols[nu], lw=1.5, label="resonant + relaxation, %.1f GHz" % nu)
ax.axhline(0.5, color="k", lw=0.6, ls=":")
ax.text(25, 0.6, "relaxation plateau 1/2", ha="right", fontsize=7)
ax.set_xlim(TK[0], TK[-1])
ax.set_ylim(1e-4, 2)
ax.set_xlabel(r"$T$ (K)")
ax.set_ylabel(r"$Q^{-1}/\pi C$  $=\tan\delta/\tan\delta_0$")
ax.legend(fontsize=6.5, loc="lower left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_7a.pdf"))
print("wrote limit16_7a.pdf")
