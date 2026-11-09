"""Fig. 13.4 (fig:13-screening): the three kinds of screening of the phonon-assisted amplitude, as diagrams.

Schematic: no number in the figure is sourced or computed. Conventions follow fig13_2.py: time runs upward, solid lines
are electrons (arrow up) and holes (arrow down), the dashed blue line is the dark-matter potential at (q, omega), the wavy
orange line is the phonon. New here: zigzag lines are Coulomb chains summed to all orders (the external column
(eps~^-1)_G0(q, omega), the retarded screened interaction W^scr,R(q+Q, omega_f) at the pair), circles are loops of Kohn-Sham
electrons, the gray disk is the screened vertex g of density-functional perturbation theory, and the black square the
local third derivative k_xc of the exchange-correlation energy (adiabatic local-density kernel only).
(a) four-path term M[rho^scr] (one path drawn); (b) pair channel, eq:13.4-Mscr; (c) adiabatic local-density source,
eq:13.4-kxc.
Run: python fig13_4.py   (numpy, matplotlib)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch13", "fig13_4.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})
EL, DM, PH, CH = "k", "#2a6fb0", "#c4661f", "#5a5a5a"


def fermion(ax, p0, p1, up=True, label=None, lpos=0.5, dx=0.03, ha="left"):
    p0, p1 = np.array(p0, float), np.array(p1, float)
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=EL, lw=1.1)
    m = p0 + 0.55 * (p1 - p0)
    d = (p1 - p0) / np.linalg.norm(p1 - p0)
    if not up:
        d = -d
    ax.annotate("", xy=m + 0.03 * d, xytext=m - 0.03 * d,
                arrowprops=dict(arrowstyle="-|>", color=EL, lw=1.0, mutation_scale=9))
    if label:
        t = p0 + lpos * (p1 - p0)
        ax.text(t[0] + dx, t[1], label, ha=ha, va="center", fontsize=7.5)


def dashed(ax, p0, p1, label=None, off=(0.0, -0.06)):
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=DM, lw=1.2, ls=(0, (3, 2)))
    if label:
        ax.text(p0[0] + off[0], p0[1] + off[1], label, color=DM, fontsize=7.5, ha="left")


def wavy(ax, p0, p1, label=None, off=(0.0, 0.04), ha="left"):
    p0, p1 = np.array(p0, float), np.array(p1, float)
    t = np.linspace(0, 1, 300)
    d = (p1 - p0) / np.linalg.norm(p1 - p0)
    n = np.array([-d[1], d[0]])
    pts = p0[None, :] + t[:, None] * (p1 - p0)[None, :] + 0.016 * np.sin(2 * np.pi * 6 * t)[:, None] * n[None, :]
    ax.plot(pts[:, 0], pts[:, 1], color=PH, lw=1.1)
    if label:
        ax.text(p1[0] + off[0], p1[1] + off[1], label, color=PH, fontsize=7.5, ha=ha)


def zigzag(ax, p0, p1, label=None, off=(0.0, 0.04), ha="center", nz=9):
    p0, p1 = np.array(p0, float), np.array(p1, float)
    d = (p1 - p0) / np.linalg.norm(p1 - p0)
    n = np.array([-d[1], d[0]])
    t = np.linspace(0, 1, 2 * nz + 1)
    amp = np.where(np.arange(len(t)) % 2 == 0, 0.0, 1.0) * np.where(np.arange(len(t)) % 4 == 1, 1.0, -1.0) * 0.022
    amp[0] = amp[-1] = 0.0
    pts = p0[None, :] + t[:, None] * (p1 - p0)[None, :] + amp[:, None] * n[None, :]
    ax.plot(pts[:, 0], pts[:, 1], color=CH, lw=1.0)
    if label:
        m = 0.5 * (p0 + p1)
        ax.text(m[0] + off[0], m[1] + off[1], label, color=CH, fontsize=7.2, ha=ha)


def vertex(ax, p):
    ax.plot([p[0]], [p[1]], "o", color="k", ms=3.0, zorder=5)


def gblob(ax, p, r=0.032):
    ax.add_patch(Circle(p, r, facecolor="0.72", edgecolor="k", lw=0.8, zorder=6))


def loop(ax, c, r):
    ax.add_patch(Circle(c, r, facecolor="none", edgecolor=EL, lw=1.1, zorder=4))


def setup(ax, title):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(0.0, 0.98, title, fontsize=8.5, ha="left", va="top")


fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.75))

# (a) four-path term with the screened density vertex and the screened phonon vertex
ax = axs[0]
setup(ax, "(a)")
v1, v2 = (0.55, 0.36), (0.55, 0.66)
fermion(ax, (0.55, 0.10), v1, up=True, label=r"$v,\mathbf{k}$", lpos=0.25, dx=0.03)
fermion(ax, v1, v2, up=True, label=r"$p$", lpos=0.5, dx=0.03)
fermion(ax, v2, (0.55, 0.92), up=True, label=r"$c,\mathbf{k}'$", lpos=0.75, dx=0.03)
dashed(ax, (0.03, 0.36), (0.16, 0.36), r"$(\mathbf{q},\omega)$", off=(0.0, -0.08))
zigzag(ax, (0.16, 0.36), v1, r"$(\tilde\varepsilon^{-1})_{\mathbf{G}0}(\mathbf{q},\omega)$", off=(0.0, 0.05))
vertex(ax, v1)
gblob(ax, v2)
ax.text(0.47, 0.66, r"$g$", fontsize=8, ha="right", va="center")
wavy(ax, (0.585, 0.66), (0.90, 0.80), r"$-\mathbf{Q},\nu$", off=(-0.06, 0.05))
ax.text(0.5, 0.01, r"$M^\pm[\rho^{\mathrm{scr}}]$", ha="center", fontsize=8)

# (b) pair channel
ax = axs[1]
setup(ax, "(b)")
lc, lr = np.array([0.30, 0.42]), 0.10
loop(ax, lc, lr)
pin = lc + lr * np.array([-1.0, 0.0])
pg = lc + lr * np.array([0.0, -1.0])
pout = lc + lr * np.array([np.cos(np.pi / 4), np.sin(np.pi / 4)])
dashed(ax, (0.0, 0.42), (0.07, 0.42))
zigzag(ax, (0.07, 0.42), pin, None, nz=4)
vertex(ax, pin)
ax.text(0.04, 0.33, r"$(\mathbf{q},\omega)$", color=DM, fontsize=7.2)
gblob(ax, pg, r=0.028)
wavy(ax, pg + np.array([0.0, -0.03]), (0.47, 0.12), r"$-\mathbf{Q},\nu$", off=(0.01, -0.01))
ax.text(0.31, 0.43, r"$\delta\mathscr{n}^{(2)}$", fontsize=7.5, ha="center", va="center")
pv = np.array([0.74, 0.62])
zigzag(ax, pout, pv, None, nz=6)
ax.text(0.66, 0.40, r"$W^{\mathrm{scr,R}}(\mathbf{q}+\mathbf{Q},\omega_f)$", color=CH, fontsize=7.2, ha="center")
vertex(ax, pv)
fermion(ax, pv, (0.92, 0.92), up=True, label=r"$c,\mathbf{k}'$", lpos=0.85, dx=-0.02, ha="right")
fermion(ax, (0.56, 0.92), pv, up=False, label=r"$v,\mathbf{k}$", lpos=0.15, dx=-0.02, ha="right")
ax.text(0.99, 0.57, r"$\rho_{cv}(\mathbf{k},\mathbf{q}+\mathbf{Q}+\mathbf{G})$", fontsize=6.6, ha="right", va="top")
ax.text(0.5, 0.01, r"pair channel", ha="center", fontsize=8)

# (c) adiabatic local-density source
ax = axs[2]
setup(ax, "(c)")
l1, l2, r = np.array([0.22, 0.66]), np.array([0.22, 0.30]), 0.075
loop(ax, l1, r)
loop(ax, l2, r)
dashed(ax, (0.0, 0.66), (0.06, 0.66))
zigzag(ax, (0.06, 0.66), l1 - np.array([r, 0.0]), None, nz=3)
vertex(ax, l1 - np.array([r, 0.0]))
ax.text(0.01, 0.74, r"$(\mathbf{q},\omega)$", color=DM, fontsize=7.2)
gblob(ax, l2 - np.array([r, 0.0]), r=0.026)
wavy(ax, l2 - np.array([r + 0.02, 0.02]), (0.04, 0.16), None)
ax.text(0.08, 0.15, r"$-\mathbf{Q},\nu$", color=PH, fontsize=7.2, ha="left", va="top")
sq = np.array([0.50, 0.48])
ax.plot([l1[0] + r * 0.8, sq[0]], [l1[1] - r * 0.6, sq[1]], color=CH, lw=1.0)
ax.plot([l2[0] + r * 0.8, sq[0]], [l2[1] + r * 0.6, sq[1]], color=CH, lw=1.0)
ax.text(0.33, 0.66, r"$\delta\mathscr{n}_{\mathsf{x}}$", fontsize=7.2)
ax.text(0.33, 0.28, r"$\delta\mathscr{n}_{\mathsf{y}}$", fontsize=7.2)
ax.add_patch(Rectangle(sq - 0.022, 0.044, 0.044, facecolor="k", zorder=6))
ax.text(sq[0], sq[1] - 0.06, r"$k_{\mathrm{xc}}$", fontsize=7.5, ha="center", va="top")
pv = np.array([0.80, 0.62])
zigzag(ax, sq, pv, None, nz=5)
ax.text(0.58, 0.60, r"$\tilde\varepsilon^{-1}$", color=CH, fontsize=7.2, ha="center")
vertex(ax, pv)
fermion(ax, pv, (0.97, 0.92), up=True, label=r"$c$", lpos=0.8, dx=-0.02, ha="right")
fermion(ax, (0.63, 0.92), pv, up=False, label=r"$v$", lpos=0.2, dx=-0.02, ha="right")
ax.text(0.5, 0.01, r"adiabatic local-density source", ha="center", fontsize=8)

fig.tight_layout(w_pad=0.6)
fig.savefig(OUT)
print("written", os.path.abspath(OUT))
