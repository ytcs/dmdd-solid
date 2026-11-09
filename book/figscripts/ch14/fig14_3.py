"""Fig. 14.3 (fig:14-lines, Sect. 14.3): magnon absorption lines of YIG and MnF2 against the applied field.
Output tex/figures/ch14/fig14_3.pdf, log fig14_3.log.  Run: python fig14_3.py (seconds).

(a) YIG, g = 2, mu0 M_s = 0.246 T (we14_3.py: 10 net spins per primitive cell of a^3/2, a = 12.375 A):
    sphere: omega = 2 mu_B B0 for B0 > mu0 M_s/3 (saturated; Kittel = Larmor);
    thin film, B0 in plane: omega = [omega_0 (omega_0 + omega_M)]^(1/2), omega_0 = 2 mu_B B0, omega_M = 2 mu_B mu0 M_s
    (book eq:14.3-kittel with N_x = N_z = 0, N_y = 1);
    film, B0 along the normal (N_z = 1): omega = omega_0 - omega_M for B0 > mu0 M_s.
(b) MnF2, B0 along the easy axis: omega_pm = omega_AFMR pm 2 mu_B B0 below the spin flop, omega_AFMR = [omega_A(2 omega_E + omega_A)]^(1/2)
    with H_E = 47.05 T, H_A = 0.82 T (Vaidya et al. arXiv:2005.01203); each line carries half the weight
    |S| omega_AFMR/(2 omega_E + omega_A) per pair (book eq:14.3-afmrweight). Spin flop at sqrt(H_A(2H_E - H_A)) = 8.75 T.
    Marker: measured zone-centre gap 1.1 meV at 4 K (Bayrakci et al. arXiv:1302.4867).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
LOG = open(os.path.join(HERE, "fig14_3.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


muB = 5.7883818060e-5
mu0Ms = 0.2460
wM = 2 * muB * mu0Ms
HE, HA = 47.05, 0.82
wE, wA = 2 * muB * HE, 2 * muB * HA
wAF = np.sqrt(wA * (2 * wE + wA))
Bsf = np.sqrt(HA * (2 * HE - HA))
out(f"YIG omega_M = {wM*1e6:.2f} ueV; MnF2 omega_AFMR = {wAF*1e3:.3f} meV; spin flop {Bsf:.2f} T;"
    f" lower line at spin flop {(wAF - 2*muB*Bsf)*1e3:.3f} meV")
for B in (0.1, 0.3, 0.5):
    w0 = 2 * muB * B
    out(f"YIG at B0 = {B} T: sphere {w0*1e6:.1f} ueV, film in plane {np.sqrt(w0*(w0+wM))*1e6:.1f} ueV,"
        f" film normal {(w0-wM)*1e6:.1f} ueV")

fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.0))
ax = axs[0]
B = np.linspace(0, 0.5, 600)
w0 = 2 * muB * B
sph = B > mu0Ms / 3
ax.plot(B[sph], w0[sph] * 1e6, color="k", lw=1.3, label="sphere (Larmor)")
ax.plot(B[~sph], w0[~sph] * 1e6, color="k", lw=0.8, ls=":")
ax.plot(B, np.sqrt(w0 * (w0 + wM)) * 1e6, color="C3", lw=1.3, label="film, field in plane")
nm = B > mu0Ms
ax.plot(B[nm], (w0[nm] - wM) * 1e6, color="C0", lw=1.3, label="film, field along normal")
ax.axhline(10, color="0.5", lw=0.6, ls="--")
ax.text(0.40, 11.5, "10 µeV", fontsize=7, color="0.3")
ax.set_xlim(0, 0.5)
ax.set_ylim(0, 75)
ax.set_xlabel(r"$B_0$ (T)")
ax.set_ylabel(r"line energy (µeV)")
ax.set_title(r"(a) YIG, uniform mode", fontsize=8)
ax.legend(fontsize=7, frameon=False, loc="upper left")

ax = axs[1]
B = np.linspace(0, Bsf, 600)
ax.plot(B, (wAF + 2 * muB * B) * 1e3, color="C3", lw=1.3, label=r"$\omega_\mathrm{AFMR} + 2\mu_BB_0$")
ax.plot(B, (wAF - 2 * muB * B) * 1e3, color="C0", lw=1.3, label=r"$\omega_\mathrm{AFMR} - 2\mu_BB_0$")
ax.plot([0], [1.1], "s", color="k", ms=4, mfc="w", label="measured gap, 4 K")
ax.axvline(Bsf, color="0.5", lw=0.6, ls=":")
ax.text(Bsf - 0.15, 1.75, "spin flop", fontsize=7, color="0.3", ha="right")
ax.set_xlim(-0.3, 9.5)
ax.set_ylim(0, 2.2)
ax.set_xlabel(r"$B_0$ (T), along the easy axis")
ax.set_ylabel("line energy (meV)")
ax.set_title(r"(b) MnF$_2$, antiferromagnetic resonance", fontsize=8)
ax.legend(fontsize=7, frameon=False, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig14_3.pdf"))
out("wrote fig14_3.pdf")
LOG.close()
