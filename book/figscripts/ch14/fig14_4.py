"""Fig. 14.4 (fig:14-neutron): the neutron geometry and the transverse projector (schematic; no data).
Output tex/figures/ch14/fig14_4.pdf.  Run: python fig14_4.py (instant).

Panel (a): scattering triangle p_n -> p_n', q = p_n - p_n' (the momentum given to the target, as for dark matter,
  App. C.19); the spin density at wavevector q split into the component along q (no field, invisible to the neutron,
  eq:C.19-field) and the two components in the plane perpendicular to q (s_perp = P_T s_e, eq:C.19-amplitude).
Panel (b): the 3x3 spin response S_ab in the standard frame x || q^, y in the scattering plane, z vertical (App. C.19).
  Shading: measured by unpolarized neutrons only as the sum S_yy + S_zz; resolved by polarization analysis
  (S_yy, S_zz, and S_yz, S_zy, whose antisymmetric part is the chiral term); never measured (S_xx, S_xy, S_xz, S_yx, S_zx).
  Side labels: which elements the dark-matter tensors proportional to P_T, to the unit matrix and to q^q^ contract.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Ellipse, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
os.makedirs(FIG, exist_ok=True)


def arrow(ax, p0, p1, color="k", lw=1.4, ls="-", ms=10):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=ms, color=color, lw=lw, ls=ls,
                                 shrinkA=0, shrinkB=0))


fig = plt.figure(figsize=(7.2, 3.0))
ax = fig.add_axes([0.0, 0.0, 0.52, 1.0])
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.2)
ax.set_aspect("equal")
ax.axis("off")
ax.text(0.1, 5.9, "(a)", fontsize=9)

# scattering triangle
O = np.array([1.0, 1.4])
pin = np.array([4.6, 0.0])
pout = np.array([3.4, 2.6])
arrow(ax, O, O + pin, color="C0")
arrow(ax, O, O + pout, color="C0")
arrow(ax, O + pout, O + pin, color="C3", lw=1.8)
ax.text(*(O + pin / 2 + np.array([-0.2, -0.45])), r"$\mathbf{p}_n$", color="C0", fontsize=9)
ax.text(*(O + pout / 2 + np.array([-0.75, 0.15])), r"$\mathbf{p}'_n$", color="C0", fontsize=9)
qv = pin - pout
mid = O + pout + qv / 2
ax.text(*(mid + np.array([0.15, 0.15])), r"$\mathbf{q}$", color="C3", fontsize=10)

# spin density decomposition at a site to the right
C = np.array([7.7, 3.2])
qh = qv / np.linalg.norm(qv)
perp1 = np.array([-qh[1], qh[0]])
ax.add_patch(Ellipse(C, 3.4, 1.15, angle=np.degrees(np.arctan2(perp1[1], perp1[0])), fc="0.9", ec="0.5", lw=0.7))
ax.text(C[0] + 0.15, C[1] + 1.95, "plane $\\perp\\,\\hat{\\mathbf{q}}$:\nseen by neutrons", fontsize=7, ha="left", color="0.25")
arrow(ax, C, C + 1.6 * qh, color="0.45", ls="--", lw=1.3)
ax.text(*(C + 1.75 * qh + np.array([0.0, -0.45])), r"$\hat{\mathbf{q}}\cdot\mathbf{s}_e$: no field", fontsize=7, color="0.35", ha="center")
arrow(ax, C, C + 1.5 * perp1, color="C2", lw=1.6)
arrow(ax, C, C - 1.1 * np.cos(1.0) * perp1 + 0.5 * np.sin(1.0) * qh, color="C2", lw=1.6)  # second in-plane direction, in perspective
ax.text(*(C + 1.5 * perp1 + np.array([-2.6, 0.35])), r"$\mathbf{s}_\perp = P_T\,\mathbf{s}_e$", fontsize=8, color="C2")
arrow(ax, O + pout + qv * 0.5 + np.array([0.6, 0.2]), C - np.array([0.9, 0.3]), color="0.6", lw=0.6, ms=6)

# panel (b): the matrix
bx = fig.add_axes([0.50, 0.02, 0.50, 0.96])
bx.set_xlim(-1.9, 5.6)
bx.set_ylim(-1.6, 3.9)
bx.set_aspect("equal")
bx.axis("off")
bx.text(-1.85, 3.65, "(b)", fontsize=9)
lab = ["x", "y", "z"]
col = {"never": "#f2d0cc", "pol": "#cfe3f2", "sum": "#9cc4e4"}
for i in range(3):
    for j in range(3):
        if i == 0 or j == 0:
            c = col["never"]
        elif i == j:
            c = col["sum"]
        else:
            c = col["pol"]
        bx.add_patch(Rectangle((j, 2 - i), 1, 1, fc=c, ec="k", lw=0.6))
        bx.text(j + 0.5, 2 - i + 0.5, rf"$S_{{{lab[i]}{lab[j]}}}$", ha="center", va="center", fontsize=8)
for k in range(3):
    bx.text(k + 0.5, 3.15, lab[k], ha="center", fontsize=8)
    bx.text(-0.2, 2 - k + 0.5, lab[k], va="center", ha="right", fontsize=8)
bx.text(1.5, 3.55, r"frame: $x \parallel \hat{\mathbf{q}}$, $y$ in plane, $z$ vertical", ha="center", fontsize=6.5)
# legend (left column) and dark-matter tensors (right column), below the matrix
items = [(col["sum"], r"unpolarized: only $S_{yy}+S_{zz}$"), (col["pol"], "resolved by polarization analysis"),
         (col["never"], "never measured")]
for k, (c, t) in enumerate(items):
    bx.add_patch(Rectangle((-0.2, -0.55 - 0.42 * k), 0.25, 0.25, fc=c, ec="k", lw=0.5))
    bx.text(0.15, -0.43 - 0.42 * k, t, fontsize=7, va="center")
bx.text(3.25, 2.95, "dark-matter\ntensor uses", fontsize=7, va="center")
bx.text(3.25, 2.2, r"$P_T$: $S_{yy}+S_{zz}$", fontsize=7, va="center")
bx.text(3.25, 1.5, r"$\mathbb{1}$: $S_{xx}+S_{yy}+S_{zz}$", fontsize=7, va="center")
bx.text(3.25, 0.8, r"$\hat{\mathbf{q}}\hat{\mathbf{q}}$: $S_{xx}$", fontsize=7, va="center")
fig.savefig(os.path.join(FIG, "fig14_4.pdf"))
print("wrote fig14_4.pdf")
