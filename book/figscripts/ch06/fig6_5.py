"""Fig. 6.5 (fig:6-bubble): the two second-order diagrams of the electron-phonon interaction, and the phonon Dyson series.

(a) electron self-energy (Fan-Migdal, Sect. 6.3, App. D.16): electron (n, k) emits and reabsorbs a phonon (Q, nu),
    intermediate electron (m, k+Q).
(b) phonon self-energy Pi_nu(Q, omega) (Sect. 6.4, eq:D.17-Pi): phonon (Q, nu) creates an electron-hole pair
    (m, k+Q; n, k) through g_mn nu(k, Q) (left vertex) and destroys it through g* (right vertex).
(c) Dyson series D = D0 + D0 Pi D0 + ... (eq:D.17-Pi): double wavy line, the dressed phonon.
Line styles follow Fig. 4.9 (figscripts/ch04/fig4_9.py): solid with arrow = electron G0, wavy = phonon D0,
double wavy = dressed propagator, dots = vertices g. Schematic; no data.
Run: python fig6_5.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch06", "fig6_5.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6, "pdf.fonttype": 42})


def arrow_mid(ax, xs, ys):
    i = len(xs) // 2
    ax.annotate("", xy=(xs[i + 1], ys[i + 1]), xytext=(xs[i - 1], ys[i - 1]),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=0.8, mutation_scale=9))


def fline(ax, xs, ys):
    ax.plot(xs, ys, color="k", lw=1.0)
    arrow_mid(ax, xs, ys)


def wavy(ax, xs, ys, n=8, amp=0.05, double=False):
    xs, ys = np.asarray(xs, float), np.asarray(ys, float)
    s = np.concatenate([[0], np.cumsum(np.hypot(np.diff(xs), np.diff(ys)))])
    tx, ty = np.gradient(xs), np.gradient(ys)
    nrm = np.hypot(tx, ty)
    nx, ny = -ty / nrm, tx / nrm
    ph = 2 * np.pi * n * s / s[-1]
    for o in ([0.0] if not double else [-0.03, 0.03]):
        ax.plot(xs + (amp * np.sin(ph) + o) * nx, ys + (amp * np.sin(ph) + o) * ny, color="k", lw=0.8)


def bubble(ax, x0, x1, h=0.42, label=True):
    t = np.linspace(0, np.pi, 81)
    xc, r = (x0 + x1) / 2, (x1 - x0) / 2
    fline(ax, xc - r * np.cos(t), h * np.sin(t))           # upper arc, left to right: electron m, k+Q
    fline(ax, xc + r * np.cos(t), -h * np.sin(t))          # lower arc, right to left: hole n, k
    ax.plot([x0, x1], [0, 0], "o", color="k", ms=3)
    if label:
        ax.text(xc, h + 0.1, r"$m,\boldsymbol{k}+\boldsymbol{Q}$", ha="center", fontsize=7.5)
        ax.text(xc, -h - 0.28, r"$n,\boldsymbol{k}$", ha="center", fontsize=7.5)


def hline(ax, x0, x1, n=6, double=False):
    wavy(ax, np.linspace(x0, x1, 60), np.zeros(60), n=n, double=double)


fig = plt.figure(figsize=(6.4, 2.9))
gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 0.85])
axa, axb, axc = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, :])
for ax in (axa, axb, axc):
    ax.set_aspect("equal"); ax.axis("off")

# (a) electron self-energy
ax = axa
ax.set_xlim(-0.3, 3.0); ax.set_ylim(-0.6, 1.25)
xs = np.linspace(0, 2.7, 61)
fline(ax, xs[:15], np.zeros(15)); fline(ax, xs[14:47], np.zeros(33)); fline(ax, xs[46:], np.zeros(15))
ax.plot([xs[14], xs[46]], [0, 0], "o", color="k", ms=3)
t = np.linspace(np.pi, 0, 60)
xc, r = (xs[14] + xs[46]) / 2, (xs[46] - xs[14]) / 2
wavy(ax, xc + r * np.cos(t), 0.8 * r * np.sin(t), n=6)
ax.text(xc, 0.8 * r + 0.15, r"$\boldsymbol{Q}\nu$", ha="center", fontsize=7.5)
ax.text(xc, -0.32, r"$m,\boldsymbol{k}+\boldsymbol{Q}$", ha="center", fontsize=7.5)
ax.text(xs[2], 0.1, r"$n\boldsymbol{k}$", fontsize=7.5)
ax.text(-0.25, 1.05, "(a)")

# (b) phonon self-energy
ax = axb
ax.set_xlim(-0.3, 3.0); ax.set_ylim(-0.75, 1.1)
hline(ax, -0.15, 0.6, n=4); bubble(ax, 0.6, 2.1); hline(ax, 2.1, 2.85, n=4)
ax.text(-0.1, 0.14, r"$\boldsymbol{Q}\nu$", fontsize=7.5); ax.text(2.45, 0.14, r"$\boldsymbol{Q}\nu$", fontsize=7.5)
ax.text(0.45, -0.3, r"$g$", fontsize=7.5); ax.text(2.12, -0.3, r"$g^*$", fontsize=7.5)
ax.text(-0.25, 0.9, "(b)")

# (c) Dyson series for the dressed phonon
ax = axc
ax.set_xlim(-0.3, 9.6); ax.set_ylim(-0.45, 0.5)
hline(ax, 0.0, 0.9, n=5, double=True)
ax.text(1.1, -0.08, "=", fontsize=10)
hline(ax, 1.45, 2.3, n=5)
ax.text(2.5, -0.08, "+", fontsize=10)
hline(ax, 2.85, 3.5, n=4); bubble(ax, 3.5, 4.3, h=0.28, label=False); hline(ax, 4.3, 4.95, n=4)
ax.text(5.15, -0.08, "+", fontsize=10)
hline(ax, 5.5, 6.0, n=3); bubble(ax, 6.0, 6.7, h=0.25, label=False); hline(ax, 6.7, 7.2, n=3)
bubble(ax, 7.2, 7.9, h=0.25, label=False); hline(ax, 7.9, 8.4, n=3)
ax.text(8.6, -0.08, r"+ $\cdots$", fontsize=10)
ax.text(0.15, 0.22, r"$\mathsf{D}_\nu$", fontsize=7.5); ax.text(1.65, 0.18, r"$\mathsf{D}_0$", fontsize=7.5)
ax.text(-0.25, 0.3, "(c)")

fig.tight_layout()
fig.savefig(OUT)
print("wrote", OUT)
