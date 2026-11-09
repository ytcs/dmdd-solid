"""Limit 11.8c (fig:11-limit-8c): resonant-mass drive of a scalar that changes m_e or alpha.

Model (Sect. 11.8): a thin free-free bar of length L along xi in [-L/2, L/2], sound speed c, under a uniform modulation of its
natural length scale, h(t) = h e^{-i omega t}. Stress sigma = Y (d u_lab/d xi - h), free ends sigma = 0, rho u_lab'' = Y d^2 u_lab/dxi^2.
Exact steady state: u_lab = h sin(k xi)/(k cos(k L/2)), k = omega/c; displacement of the end from its instantaneous equilibrium
    u(L/2) = (h L/2) [tan(x)/x - 1],  x = k L/2 = (pi/2) omega/omega_1,  omega_1 = pi c/L       (eq:11.8-bar).
Damping: c -> c (1 + i/(2 Q))^{-1}, which gives every mode the full width omega_n/Q; Q = 100 (modelling choice, for visibility;
resonant-mass detectors reach 1e6-1e7).
Literature form (Arvanitaki, Dimopoulos, Van Tilburg, arXiv:1508.01798, Eqs. (6)-(8)): one mode with the force -h'' M R J_n, here
for the lowest bar mode u_1 = sin(pi xi/L) (u_1(L/2) = 1), M_1 = M/2, force omega^2 h rho A 2L^2/pi^2:
    D_1/(h L) = (4/pi^2) (omega/omega_1)^2 / [1 - (omega/omega_1)^2 - i (omega/omega_1)/Q].
Low-frequency limits: exact (pi^2/24)(omega/omega_1)^2 = 0.411 (omega/omega_1)^2; one mode (4/pi^2) = 0.405 (sum over odd n of
4/(n^4 pi^2) = pi^2/24). Gray: omega/omega_1 < 2.09, where the one-mode form is within 10 % of the exact response.
The modulus is uniform over the bar while k_phi L = m_phi v L << 1; at omega = omega_1, k_phi L = pi v c_l with c_l in units
of the speed of light, 5e-8 for v = 1e-3 and c_l = 5 km/s, so the boundary k_phi L = 1 lies near omega/omega_1 ~ 2e7, off scale.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

Qf = 100.0
r = np.logspace(-2, 1, 6001)                   # omega/omega_1
x = (np.pi / 2) * r * (1 + 0.5j / Qf)
exact = 0.5 * (np.tan(x) / x - 1)
one = (4 / np.pi**2) * r**2 / (1 - r**2 - 1j * r / Qf)
ratio = np.abs(one) / np.abs(exact)
ok = np.abs(ratio - 1) < 0.10
print("low-frequency coefficients: exact %.4f, one-mode %.4f" % (np.pi**2 / 24, 4 / np.pi**2))
edges = np.flatnonzero(np.diff(ok.astype(int)))
print("at omega -> high (r=10): |exact| = %.3f (static limit 1/2 off resonance)" % abs(exact[-1]))
v, cl = 1e-3, 5.0 / 299792.458
print("k_phi L at omega_1: %.2e; boundary k_phi L = 1 at omega/omega_1 = %.2e" % (np.pi * v * cl, 1 / (np.pi * v * cl)))

fig, ax = plt.subplots(figsize=(4.6, 3.0))
# shade the low-frequency interval in which the one-mode form is within 10 % of the exact response
r_ok = r[np.argmax(~ok)]
print("one-mode within 10 %% of exact for omega/omega_1 < %.3f" % r_ok)
ax.axvspan(1e-2, r_ok, color="0.88", lw=0)
ax.loglog(r, np.abs(exact), color="k", lw=1.2, label="free bar, exact")
ax.loglog(r, np.abs(one), color="k", lw=1.0, ls="--", label=r"lowest mode, drive $\propto \omega^2$")
ax.loglog(r, 0.5 * np.ones_like(r), color="0.5", lw=0.8, ls=":")
ax.set_xlabel(r"$\omega/\omega_1$")
ax.set_ylabel(r"$|u(L_{\mathrm{b}}/2)|/(h_{\mathrm{mod}}L_{\mathrm{b}})$")
ax.set_xlim(1e-2, 10)
ax.set_ylim(1e-5, 100)
ax.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
fig.savefig("../../tex/figures/ch11/limit11_8c.pdf")
print("wrote limit11_8c.pdf")
