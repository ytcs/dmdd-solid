"""Fig. 14.5 (fig:14-cd, Sect. 14.5): circular dichroism of a chiral crystal such as tellurium, SCHEMATIC.
Output tex/figures/ch14/fig14_5.pdf, log fig14_5.log.  Run: python fig14_5.py  (seconds).

Everything here is a labelled model; no number in the figure is a property of tellurium.
(a) Absorption of the two helicities, S_-+ = S_T (1 +- d), with S_T a band-edge shape sqrt(x - 1) exp(-(x-1)/2), x = omega/E_g,
    and the dissymmetry d(q, omega) = q.G_OA/S_T (eq:14.5-helicity) taken as q |g| times a smooth function of x. Solid: S_-, dashed: S_+, for the
    right-handed crystal; the left-handed one exchanges the helicities. Two momenta: an optical one (q|g| = 1e-4, so the split is
    invisible) and a dark-matter one (q|g| = 0.05).
(b) |d| against q at omega = 1.5 E_g, for |g| = 0.1 bohr (the order of the DFPT gyration of trigonal crystals, 2304.00048 Table I)
    with the schematic finite-q shape d = q|g| / [1 + (q c/pi)^2], c = 6 A (a helix pitch of this order); dashed: the linear term
    alone. Marked: optical momenta (vacuum photon at 1-3 eV) and the dark-matter momenta q >= omega/v_max = 377 omega at
    omega = 1-3 eV. The shape beyond the linear term is the finite-q optical activity that App. E.20 specifies; it is not known.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
LOG = open(os.path.join(HERE, "fig14_5.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


x = np.linspace(0.9, 4, 600)
ST = np.where(x > 1, np.sqrt(np.clip(x - 1, 0, None)) * np.exp(-(x - 1) / 2), 0.0)
shape = np.where(x > 1, np.exp(-(x - 1.5)**2 / 1.5), 0.0)
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.0))
ax = axs[0]
for qg, col, lab in ((1e-4, "0.5", r"optical $q$"), (0.05 * 4, "C3", r"dark-matter $q$ (split $\times 4$)")):
    d = qg * shape
    ax.plot(x, ST * (1 + d), color=col, lw=1.3, label=lab + r": $S_-$")
    ax.plot(x, ST * (1 - d), color=col, lw=1.3, ls="--", label=lab + r": $S_+$")
ax.text(2.75, 0.30, "left-handed crystal:\n" + r"$S_+ \leftrightarrow S_-$", fontsize=7, color="0.3")
ax.set_xlabel(r"$\omega/E_{\mathrm{g}}$")
ax.set_ylabel(r"absorption, arbitrary units")
ax.set_title("(a) the two helicities, right-handed crystal", fontsize=8)
ax.legend(fontsize=7, frameon=False, loc="upper right")
ax.set_ylim(0, 1.05)

ax = axs[1]
BOHR = 0.529177210903e-10
HBARC = 197.3269804e-9 * 1.0   # eV m
g = 0.1 * BOHR
c = 6e-10
q_kev = np.logspace(-6, 1.5, 500)
q = q_kev * 1e3 / HBARC        # m^-1
lin = q * g
d = lin / (1 + (q * c / np.pi)**2)
ax.loglog(q_kev, lin, color="0.4", lw=0.9, ls="--", label="linear term (gyration tensor)")
ax.loglog(q_kev, d, color="C3", lw=1.3, label="schematic finite-$q$ odd part")
qo = np.array([1, 3]) * 1e-3
vmax = (544.0 + 250.5) / 299792.458
qd = np.array([1, 3]) / vmax * 1e-3
ax.axvspan(qo[0], qo[1], color="C0", alpha=0.25, lw=0)
ax.axvspan(qd[0], qd[1], color="C3", alpha=0.18, lw=0)
ax.text(np.sqrt(qo[0] * qo[1]), 3e-7, "optical", fontsize=7, color="C0", ha="center")
ax.text(np.sqrt(qd[0] * qd[1]), 3e-7, "dark matter\n(1–3 eV)", fontsize=7, color="C3", ha="center")
ax.set_xlim(1e-6, 30)
ax.set_ylim(1e-8, 1)
ax.set_xlabel(r"$|\vect{q}|$ (keV)".replace(r"\vect{q}", r"\mathbf{q}"))
ax.set_ylabel(r"dissymmetry $|S_- - S_+|/(S_- + S_+)$")
ax.set_title(r"(b) dissymmetry against $|\mathbf{q}|$", fontsize=8)
ax.legend(fontsize=7, frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig14_5.pdf"))
out(f"schematic: |g| = 0.1 bohr, c = 6 A; linear dissymmetry at optical q (1-3 eV photons): {qo[0]*1e3/HBARC*g:.1e}-{qo[1]*1e3/HBARC*g:.1e}")
out(f"  dark-matter q at 1-3 eV: {qd[0]:.2f}-{qd[1]:.2f} keV; linear term there {qd[0]*1e3/HBARC*g:.3f}-{qd[1]*1e3/HBARC*g:.3f}")
out("wrote", os.path.join(FIG, "fig14_5.pdf"))
LOG.close()
