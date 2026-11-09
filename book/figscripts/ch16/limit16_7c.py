"""Limit Check 16.7c (lim:16.7c, fig:16-limit-born): scattering off a whole random medium and the Born limit.
Literature form (Liu, Matsumoto, Sheng, Xing, arXiv:2512.16451, Eqs. (2), (7)-(12)): first Born approximation on the medium,
d sigma_tot/dOmega = (d sigma_chiN/dOmega) |int d^3r e^{iq.r} n(r)|^2, with the homogeneous part n0^2 |int_V e^{iq.r}|^2
(their Eq. (4)-(5)) and the fluctuation part (their Eq. (12)).
The homogeneous part is the Born approximation to the reflection of the dark-matter wave at the faces of the body.  Fuller
result: the exact reflection of a plane wave with normal kinetic energy E_n at a planar face, optical potential
V_opt = 2 pi b n0 / mu (b the dark-matter-nucleon scattering length, sigma_chiN = 4 pi b^2, mu ~ m_chi):
    R = |(k - k')/(k + k')|^2,  k'^2 = k^2 (1 - V_opt/E_n),   total reflection for V_opt > E_n > 0;
Born: R_B = (V_opt / 4 E_n)^2 (leading term of the same expansion; first-order amplitude of the step).
Plotted: R/R_B against |V_opt|/E_n for repulsive (V > 0) and attractive (V < 0) media.  Shaded: within 10 %.
Born criterion |V_opt| << m v^2/2  <=>  sigma_chiN << sigma_crit = m^4 v^4/(4 pi n0^2)  (derived in Sect. 16.7).
Example (arXiv:2512.16451 Eq. (14) and text): Ti-6Al-4V, nucleon density n0 = 2.69e24 cm^-3; m_chi = 20 eV; quoted
reach sigma_chiN ~ 4e-38 cm^2.  V_opt/E = (sigma/sigma_crit)^(1/2).
Run: python limit16_7c.py > limit16_7c.log
"""
import os
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import tls16_7 as L

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch16")


def R_exact(x):
    """x = V/E_n (signed)."""
    x = np.asarray(x, float)
    kp = np.sqrt(np.maximum(1 - x, 0.0))
    R = ((1 - kp) / (1 + kp))**2
    return np.where(x >= 1, 1.0, R)


def R_born(x):
    return (np.asarray(x) / 4)**2


xs = np.geomspace(1e-3, 10, 400)
rp = R_exact(xs) / R_born(xs)
rm = R_exact(-xs) / R_born(-xs)
xp10 = brentq(lambda x: R_exact(x) / R_born(x) - 1.1, 1e-3, 0.99)
xm10 = brentq(lambda x: 1 - R_exact(-x) / R_born(-x) - 0.1, 1e-3, 10)
print("R/R_B within 10%%: repulsive V/E < %.4f; attractive |V|/E < %.4f" % (xp10, xm10))
print("small-x expansion check, x = 0.01: R/R_B = %.5f (repulsive), %.5f (attractive)"
      % (R_exact(0.01) / R_born(0.01), R_exact(-0.01) / R_born(-0.01)))
# sigma_crit
n0 = 2.69e24 * L.CM3
m = 20.0
for v in (1e-3, 1.2e-3, L.P.VMAX):
    sc = m**4 * v**4 / (4 * np.pi * n0**2) / L.CM2
    print("m = 20 eV, v = %.3e: sigma_crit = %.4e cm^2; at sigma = 4e-38 cm^2, V_opt/E = %.3f"
          % (v, sc, np.sqrt(4e-38 / sc)))
# normal component: E_n = E cos^2 theta; the fraction of an isotropic flux on a face with V/E_n > 1
sc1 = m**4 * 1e-6**2 / (4 * np.pi * n0**2) / L.CM2
print("v = 1e-3 m: sigma_crit = %.3e cm^2 (1.2e-38 expected)" % sc1)

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.axvspan(xs[0], min(xp10, xm10), color="0.88", lw=0)
ax.loglog(xs, rp, color="C3", lw=1.5, label=r"exact, repulsive ($V_{\mathrm{opt}} > 0$)")
ax.loglog(xs, rm, color="C0", lw=1.5, label=r"exact, attractive ($V_{\mathrm{opt}} < 0$)")
ax.axhline(1.0, color="k", lw=0.8, ls="--", label="first Born approximation")
ax.axvline(1.86, color="k", lw=0.6, ls=":")
ax.text(1.95, 0.016, "Ti-6Al-4V,\n" + r"$4\times10^{-38}$ cm$^2$," + "\n20 eV", fontsize=6.5)
ax.set_xlim(xs[0], xs[-1])
ax.set_ylim(1e-2, 30)
ax.set_xlabel(r"$|V_{\mathrm{opt}}|/E_n$")
ax.set_ylabel(r"reflectance / Born reflectance")
ax.legend(fontsize=6.5, loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_7c.pdf"))
print("wrote limit16_7c.pdf")
