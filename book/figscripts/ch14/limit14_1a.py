"""Limit Check 14.1a (lim:14.1a, fig:14-limit): the one-magnon spectral weight of linear spin-wave theory against the
weights that the spin sum rule fixes, as functions of the expansion parameter 1/(2|S|).

Curves (App. D.38, per magnetic ion, in units of the linear spin-wave one-magnon weight W_perp = |S|(1 + 2 Delta S)):
  literature formula (one-magnon rate at linear spin-wave order, 1905.13744 Eqs. (5)-(12); 2009.13534 Eq. (38)): 1;
  one-magnon weight fixed by the sum rule |S|(|S|+1) = W_perp + <S^z>^2 + W_par with the linear spin-wave
     <S^z> = |S| - Delta S and W_par = Delta S (1 + Delta S): (|S| - Delta S)(1 + 2 Delta S)/W_perp = 1 - Delta S/|S|;
  two-magnon (longitudinal) weight W_par/W_perp = Delta S (1 + Delta S)/(|S|(1 + 2 Delta S));
  one- plus two-magnon weight: 1 - Delta S^2/(|S|(1 + 2 Delta S)).
Delta S is computed here for the NiO lattice (Hutchings-Samuelsen J1, J2; magnon14.py) on a 100^3 offset grid; it is
independent of |S| at this order, so the curves vary |S| at fixed lattice and exchange ratios.
Validity (shaded): Delta S/|S| < 0.1, i.e. 1/(2|S|) < 1/(20 Delta S).
Markers: |S| = 1/2, 1 (Ni2+, NiO), 3/2, 2, 5/2 (Mn2+, Fe3+).
Outputs: tex/figures/ch14/limit14_1a.pdf; figscripts/ch14/limit14_1a.log.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import magnon14 as m

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch14", "limit14_1a.pdf")
LOG = open(os.path.join(HERE, "limit14_1a.log"), "w")


def out(s):
    print(s)
    LOG.write(s + "\n")


k = m.zone_grid(100, 4 * np.pi / m.A_NIO)
dS = m.v2(*m.ab_nio(k)).mean()
out(f"Delta S (NiO lattice, 100^3 grid) = {dS:.4f}")
x = np.linspace(0.02, 1.0, 400)
S = 1 / (2 * x)
one_sr = 1 - dS / S
two = dS * (1 + dS) / (S * (1 + 2 * dS))
tot = 1 - dS**2 / (S * (1 + 2 * dS))
xv = 1 / (20 * dS)
out(f"validity Delta S/|S| < 0.1: 1/(2|S|) < {xv:.3f}")
for Sm in (0.5, 1.0, 1.5, 2.0, 2.5):
    out(f"  |S| = {Sm}: 1 - dS/|S| = {1 - dS/Sm:.4f}; W_par/W_perp = {dS*(1+dS)/(Sm*(1+2*dS)):.4f};"
        f" one+two = {1 - dS**2/(Sm*(1+2*dS)):.5f}")

plt.rcParams.update({"font.size": 8.5})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.axvspan(0, xv, color="0.9", lw=0)
ax.text(0.03, 0.55, r"$\Delta S/|\mathbf{S}| < 0.1$", fontsize=7.5, color="0.35")
ax.plot(x, np.ones_like(x), color="k", lw=1.0, label=r"linear spin-wave one-magnon weight")
ax.plot(x, one_sr, color="C3", lw=1.2, label=r"one-magnon weight from the sum rule, $1 - \Delta S/|\mathbf{S}|$")
ax.plot(x, tot, color="C0", lw=1.0, ls="--", label=r"one- plus two-magnon weight")
ax.plot(x, two, color="C2", lw=1.2, label=r"two-magnon weight $W_\parallel/W_\perp$")
for Sm, lab in ((0.5, r"$\frac{1}{2}$"), (1.0, "1 (NiO)"), (1.5, r"$\frac{3}{2}$"), (2.0, "2"), (2.5, r"$\frac{5}{2}$")):
    xm = 1 / (2 * Sm)
    ax.plot([xm], [1 - dS / Sm], "o", color="C3", ms=3)
    ax.plot([xm], [dS * (1 + dS) / (Sm * (1 + 2 * dS))], "o", color="C2", ms=3)
    ax.text(xm, 1.035, lab, ha="center", fontsize=7, color="0.3")
ax.text(0.1, 1.035, r"$|\mathbf{S}| =$", ha="center", fontsize=7, color="0.3")
ax.set_xlim(0, 1.02)
ax.set_ylim(0, 1.12)
ax.set_xlabel(r"$1/(2|\mathbf{S}|)$")
ax.set_ylabel(r"weight / $|\mathbf{S}|(1 + 2\Delta S)$")
ax.legend(fontsize=6.5, frameon=False, loc="center right", bbox_to_anchor=(1.0, 0.42))
fig.tight_layout()
fig.savefig(OUT)
out(f"wrote {OUT}")
LOG.close()
