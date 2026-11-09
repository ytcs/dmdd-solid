"""Fig. 16.7 (fig:16-tls): the standard tunneling model.
(a) Distribution of the tunneling amplitude at fixed splitting Delta_tl, from P(Delta_as, lambda) = P_bar flat
    (Phillips; Anderson, Halperin, Varma; as written in arXiv:1705.01108 Eq. (8) and arXiv:2103.06977 Eq. (12)):
    per unit u = Delta_0/Delta_tl, P_bar/(u (1-u^2)^(1/2)) (curve 1), and the same weighted by the squared transition
    matrix element u^2 (curve 2), whose integral over 0 < u < 1 is exactly P_bar (printed check).  Dotted: the cumulative
    integral of curve 1 from u_min = 1e-6, P_bar ln(2/u_min) asymptotically (the logarithm of arXiv:1705.01108 Eq. (9)).
(b) Line shapes per unit P_bar <|f|^2>: the scattering structure factor of the ensemble (pi/2)/(1 + e^{-omega/T})
    (absorption omega > 0 and emission omega < 0 by the thermal population of the upper level) and the net absorption
    of a classical field, proportional to tanh(omega/2T).
Run: python fig16_7.py > fig16_7.log
"""
import os
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch16")
u = np.geomspace(1e-5, 1 - 1e-9, 600)
p = 1 / (u * np.sqrt(1 - u**2))
pw = u**2 * p
I = quad(lambda x: x / np.sqrt(1 - x**2), 0, 1)[0]
print("int_0^1 u^2 P du / P_bar = %.6f (exact 1)" % I)
umin = 1e-6
print("int_umin^1 P du / P_bar = %.4f vs ln(2/umin) = %.4f (umin = 1e-6)"
      % (quad(lambda x: 1 / (x * np.sqrt(1 - x**2)), umin, 1, limit=200, points=[1e-4, 1e-2])[0], np.log(2 / umin)))
print("fraction of int u^2 P du from u < 0.5: %.4f" % (1 - np.sqrt(1 - 0.25)))
x = np.linspace(-6, 6, 400)
print("S(omega = T)/S(+inf) = %.4f, S(-T)/S(+inf) = %.4f, tanh(1/2) = %.4f" % (1 / (1 + np.exp(-1)), 1 / (1 + np.exp(1)),
                                                                            np.tanh(0.5)))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.8))
a1.loglog(u, p, color="C0", lw=1.5, label=r"$P/\bar P$ per unit $\Delta_0/\Delta_{\mathrm{tl}}$")
a1.loglog(u, pw, color="C3", lw=1.5, label=r"weighted by $(\Delta_0/\Delta_{\mathrm{tl}})^2$")
a1.set_xlabel(r"$\Delta_0/\Delta_{\mathrm{tl}}$")
a1.set_ylabel(r"density per unit $\Delta_0/\Delta_{\mathrm{tl}}$ (units of $\bar P$)")
a1.set_xlim(1e-5, 1)
a1.set_ylim(1e-5, 1e5)
a1.legend(fontsize=6.5, loc="upper right", frameon=False)
a1.text(0.96, 0.05, "(a)", transform=a1.transAxes, ha="right")
a2.plot(x, 1 / (1 + np.exp(-x)), color="C3", lw=1.5, label=r"scattering, $(1 + \mathrm{e}^{-\omega/T})^{-1}$")
a2.plot(x, np.tanh(x / 2), color="C0", lw=1.5, ls="--", label=r"net absorption, $\tanh(\omega/2T)$")
a2.axhline(0, color="k", lw=0.5)
a2.axvline(0, color="k", lw=0.5)
a2.set_xlabel(r"$\omega/T$")
a2.set_ylabel(r"line shape (units of the $T = 0$ value)")
a2.set_ylim(-1.1, 1.15)
a2.legend(fontsize=6.5, loc="lower right", frameon=False)
a2.text(0.04, 0.9, "(b)", transform=a2.transAxes)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig16_7.pdf"))
print("wrote fig16_7.pdf")
