"""Fig. 4.10 for Sect. 4.8: the bubble with the cut through its two propagators.

Output: tex/figures/ch04/fig4_10.pdf
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch04")
plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6, "pdf.fonttype": 42})

fig, ax = plt.subplots(1, 1, figsize=(2.9, 1.7))
ax.set_aspect("equal"); ax.axis("off")
ax.set_xlim(-0.4, 3.0); ax.set_ylim(-1.0, 1.0)
t = np.linspace(0, np.pi, 81)
x0, x1, h = 0.4, 2.2, 0.5
xc, r = (x0 + x1) / 2, (x1 - x0) / 2
for xs, ys in [(xc - r * np.cos(t), h * np.sin(t)), (xc + r * np.cos(t), -h * np.sin(t))]:
    ax.plot(xs, ys, color="k", lw=1.0)
    i = 40
    ax.annotate("", xy=(xs[i + 1], ys[i + 1]), xytext=(xs[i - 1], ys[i - 1]),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=0.8, mutation_scale=9))
for a, b in [(-0.3, x0), (x1, 2.9)]:
    ax.plot([a, b], [0, 0], color="k", lw=0.9, ls=(0, (3, 2)))
ax.plot([x0, x1], [0, 0], "o", color="k", ms=3)
ax.plot([xc, xc], [-0.85, 0.85], color="C3", lw=1.6, ls=(0, (4, 2)))
ax.text(xc + 0.06, 0.62, r"$\boldsymbol{k}+\boldsymbol{q}$", fontsize=7.5)
ax.text(xc + 0.06, -0.78, r"$\boldsymbol{k}$", fontsize=7.5)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_10.pdf"))
print("wrote fig4_10.pdf")
