"""Limit Check 16.7d (lim:16.7d, fig:16-limit-ir): absorption of a glass below the Ioffe-Regel frequency.
Formula (Taraskin, Simdyankin, Elliott, Neilson, Lo, arXiv:cond-mat/0604205, Eq. (1); derived in Sect. 16.7):
    alpha(omega) = C(omega) g(omega),  C(omega) = A + B omega^2,
fitted to THz time-domain data of g-SiO2 (Spectrosil WF, room temperature) with A = 4000 cm^-2, B = 0.3 (C in cm^-2,
omega/2 pi c in cm^-1; their Fig. 1 caption), Debye VDOS g = 3 w~^2 / w~_D^3 with Theta_D = 330 K (their Fig. 1 inset);
valid below the Ioffe-Regel crossover, w~_IR ~ 35 cm^-1 for g-SiO2 (their p. 3).
Dark-photon rate (Bloch et al. arXiv:2603.22390 Eq. (2); eq. 10.7-dp): R = (rho_chi/rho_T) zeta^2 L,
L = eps_2/(eps_1^2 + eps_2^2), eps_2 = n_r alpha c/omega = n_r alpha/(2 pi w~), eps_1 = eps_r = 3.9 (assumed), n_r = eps_r^(1/2).
Curves: A term alone (the incoherent random-charge estimate), A + B omega^2 (formula); the TLS rate of Limit Check 16.7b
at saturation (tan delta_0 = 3e-4, thermal oxide) for comparison.  Shaded: omega < omega_IR.
Run: python limit16_7d.py > limit16_7d.log
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import tls16_7 as L

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch16")
CM1 = 1.239841984e-4                  # eV per cm^-1
A, B = 4000.0, 0.3
WD = 330.0 * 0.6950348                # Debye wavenumber, cm^-1
WIR = 35.0
EPS = L.EPS_R
NR = np.sqrt(EPS)
PRE = L.RHO_CHI / L.RHO_T * L.KG * L.YEAR


def alpha(wt, b=B):
    return (A + b * wt**2) * 3 * wt**2 / WD**3


def Lfun(wt, b=B):
    e2 = NR * alpha(wt, b) / (2 * np.pi * wt)
    return e2 / (EPS**2 + e2**2)


L_TLS = L.TAND_THERMAL / EPS
print("Debye wavenumber %.2f cm^-1 (%.3f meV); omega_IR = 35 cm^-1 = %.3f meV" % (WD, WD * CM1 * 1e3, WIR * CM1 * 1e3))
print("B w^2 = A at w~ = %.1f cm^-1 (%.2f meV); B w^2/A at omega_IR = %.4f" % (np.sqrt(A / B), np.sqrt(A / B) * CM1 * 1e3,
                                                                             B * WIR**2 / A))
for wt in (1.0, 5.0, 10.0, 20.0, 35.0):
    print("w~ = %5.1f cm^-1 (%.3f meV): alpha = %.4e cm^-1, eps2 = %.4e, L = %.4e, rate = %.4e /(kg yr zeta^2)"
          % (wt, wt * CM1 * 1e3, alpha(wt), NR * alpha(wt) / (2 * np.pi * wt), Lfun(wt), PRE * Lfun(wt)))
wx = brentq(lambda w: Lfun(w) - L_TLS, 0.1, 30)
print("TLS L (tan d0 = 3e-4, eps 3.9) = %.4e, rate %.4e; vibrational L equals it at w~ = %.3f cm^-1 = %.4f meV"
      % (L_TLS, PRE * L_TLS, wx, wx * CM1 * 1e3))
wx5 = brentq(lambda w: Lfun(w) - L.TAND_PECVD / EPS, 0.1, 100)
print("with tan d0 = 5e-3 the crossing is at w~ = %.3f cm^-1 = %.4f meV" % (wx5, wx5 * CM1 * 1e3))

wt = np.geomspace(0.5, 120, 300)
m = wt * CM1 * 1e3
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.axvspan(m[0], WIR * CM1 * 1e3, color="0.88", lw=0)
ax.loglog(m, PRE * Lfun(wt), color="C3", lw=1.5, label=r"$C^{\mathrm{IR}} = A^{\mathrm{IR}} + B^{\mathrm{IR}}\omega^2$")
ax.loglog(m, PRE * Lfun(wt, b=0.0), color="C0", lw=1.2, ls="--", label=r"$A^{\mathrm{IR}}$ alone")
ax.axhline(PRE * L_TLS, color="k", lw=0.8, ls=":", label=r"two-level systems, $\tan\delta_0 = 3\times10^{-4}$")
ax.set_xlim(m[0], m[-1])
ax.set_xlabel(r"$m_\phi$ (meV)")
ax.set_ylabel(r"events per kg yr per $\zeta^2$")
ax.legend(fontsize=6.5, loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_7d.pdf"))
print("wrote limit16_7d.pdf")
