"""Fig. 3.3: a momentum transfer reduced to the first Brillouin zone (Umklapp), drawn in the k_z = 0 plane of the fcc
reciprocal lattice of silicon (Sect. 3.1); and the numbers of Worked example 3.1. Output: tex/figures/ch03/fig3_3.pdf.

Geometry (definitions). Units of 2pi/a. Reciprocal-lattice vectors G = (2pi/a)(h,k,l) with h,k,l all even or all odd.
In the plane k_z = 0 the only reciprocal-lattice vectors are (2m, 2n, 0); the zones centred on them cut the plane in
octagons |k_x - 2m| <= 1, |k_y - 2n| <= 1, |k_x - 2m| + |k_y - 2n| <= 3/2. The rest of the plane belongs to zones centred
on (h,k,+-1)-type vectors with h,k odd, which lie out of the plane; it is shaded. Display choice: the example transfer
q = (2.2, 0.5, 0)(2pi/a), whose nearest reciprocal-lattice vector is G_q = (2,0,0)(2pi/a) (checked below against all G).
The circle is the maximum momentum transfer 2 m_chi v_max of 1 MeV dark matter.

Inputs and their sources:
  a = 5.431 A                      (CODATA 2022, Mohr et al., RMP 97, 025002 (2025), lattice parameter of silicon)
  hbar c = 1973.2698 eV A          (CODATA 2018)
  v_max = 2.650e-3 (794.5 km/s)    (Sect. 1.2 of the book: v_esc + |v_sun| = 544 + 250.5 km/s)
  E_g = 1.11 eV                    (literature value used for projections, Essig et al. 1509.01598 Eq. (5.2); Sect. 1.3)
  q0 = alpha m_e = 3.728 keV       (Sect. 1.3; alpha = 1/137.035999, m_e = 0.51099895 MeV)
"""
import os
import itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

A = 5.431
HBARC = 1973.2698
U = 2 * np.pi * HBARC / A        # 2pi/a in eV
VMAX = 2.650e-3
EG = 1.11
Q0 = 0.51099895e6 / 137.035999

# ---- reciprocal lattice ------------------------------------------------------------------------------------------
def G_list(nmax):
    r = range(-nmax, nmax + 1)
    return np.array([(h, k, l) for h, k, l in itertools.product(r, r, r) if len({h % 2, k % 2, l % 2}) == 1], float)
G = G_list(4)

def reduce(q):
    d = np.linalg.norm(G - q, axis=1)
    i = np.argmin(d)
    return q - G[i], G[i]

q = np.array([2.2, 0.5, 0.0])
qr, Gq = reduce(q)
assert np.allclose(Gq, [2, 0, 0])
print(f"example: q = {q} (2pi/a), |q| = {np.linalg.norm(q):.3f} (2pi/a) = {np.linalg.norm(q)*U/1e3:.2f} keV;"
      f" G_q = {Gq}, q_r = {qr}, |q_r| = {np.linalg.norm(qr)*U/1e3:.2f} keV")

# ---- Worked example 3.1 ------------------------------------------------------------------------------------------
print(f"2pi/a = {U:.1f} eV; a = {A/HBARC:.4e} eV^-1; q0 = {Q0:.1f} eV = {Q0/U:.3f} (2pi/a)")
print(f"|Gamma L| = {np.sqrt(3)/2*U:.0f} eV (inscribed sphere); |Gamma W| = {np.sqrt(1.25)*U:.0f} eV (circumscribed)")
for m in (1e6, 1e7, 1e8):
    qmax = 2 * m * VMAX
    disc = np.sqrt(1 - 2 * EG / (m * VMAX**2))
    lo, hi = m * VMAX * (1 - disc), m * VMAX * (1 + disc)
    R = qmax / U
    n = int(np.ceil(R)) + 1
    r = range(-n, n + 1)
    if R < 40:
        GG = G_list(n)
        count = int(np.sum(np.linalg.norm(GG, axis=1) < R)) - 1
    else:
        count = None
    est = 4 * np.pi / 3 * R**3 / 4      # number of zone volumes (4 (2pi/a)^3 each) in the ball of radius qmax
    print(f"m_chi = {m/1e6:g} MeV: 2 m v_max = {qmax/1e3:.2f} keV = {R:.2f} (2pi/a);"
          f" E_g reachable for q = {lo:.0f} eV .. {hi/1e3:.2f} keV = {lo/U:.3f} .. {hi/U:.2f} (2pi/a);"
          f" nonzero G inside 2 m v_max: exact {count}, volume estimate {est:.3g}")
print(f"q_min = E_g/v_max = {EG/VMAX:.0f} eV = {EG/VMAX/U:.3f} (2pi/a)")

# ---- figure -------------------------------------------------------------------------------------------------------
def octagon(c):
    pts = [(1, .5), (.5, 1), (-.5, 1), (-1, .5), (-1, -.5), (-.5, -1), (.5, -1), (1, -.5)]
    return np.array(pts) + np.array(c)

fig, ax = plt.subplots(figsize=(4.6, 4.0))
ax.add_patch(Polygon([[-1.6, -1.6], [3.6, -1.6], [3.6, 2.6], [-1.6, 2.6]], closed=True, color="0.9", lw=0, zorder=0))
for m, n in itertools.product(range(-1, 3), range(-1, 2)):
    c = (2 * m, 2 * n)
    first = (m, n) == (0, 0)
    ax.add_patch(Polygon(octagon(c), closed=True, facecolor="#deebf7" if first else "white",
                         edgecolor="0.3", lw=0.8, zorder=1))
    ax.plot(*c, "o", color="k", ms=3, zorder=3)
ax.add_patch(Circle((0, 0), 2 * 1e6 * VMAX / U, fill=False, ls="--", color="#2171b5", lw=0.9, zorder=2))
kw = dict(arrowstyle="-|>", mutation_scale=10, lw=1.4, shrinkA=0, shrinkB=0)
ax.annotate("", xy=q[:2], xytext=(0, 0), arrowprops=dict(color="#cb181d", **kw), zorder=4)
ax.annotate("", xy=Gq[:2], xytext=(0, 0), arrowprops=dict(color="0.2", **kw), zorder=4)
ax.annotate("", xy=q[:2], xytext=Gq[:2], arrowprops=dict(color="#238b45", **kw), zorder=4)
ax.annotate("", xy=qr[:2], xytext=(0, 0), arrowprops=dict(color="#238b45", ls="-", **kw), zorder=4)
ax.text(1.25, 0.43, r"$\boldsymbol{q}$", color="#cb181d", fontsize=11)
ax.text(1.0, -0.22, r"$\boldsymbol{G}_q$", color="0.2", fontsize=11)
ax.text(2.0, 0.14, r"$\boldsymbol{q}_r$", color="#238b45", fontsize=11, ha="right")   # inside the dashed circle
ax.text(-0.22, 0.3, r"$\boldsymbol{q}_r$", color="#238b45", fontsize=11)
ax.text(-0.25, -0.25, r"$\Gamma$", fontsize=10)
ax.text(2.2, -0.62, r"$2m_\chi v_{\max}$" + "\n(1 MeV)", color="#2171b5", fontsize=8, ha="right")   # just inside the circle, clear of zone edges
ax.set_xlim(-1.6, 3.6); ax.set_ylim(-1.6, 2.6)
ax.set_aspect("equal")
ax.set_xlabel(r"$k_x\;[2\pi/a]$")
ax.set_ylabel(r"$k_y\;[2\pi/a]$")
ax.set_xticks([-1, 0, 1, 2, 3]); ax.set_yticks([-1, 0, 1, 2])
plt.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch03", "fig3_3.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
