"""Fig. 13.2 (fig:13-paths): the four paths of the phonon-assisted electron-recoil amplitude as time-ordered diagrams.

Schematic: no number in the figure is sourced or computed. Time runs upward. Solid lines with upward arrows are electrons,
solid lines with downward arrows are holes (the time-ordered convention of old-fashioned perturbation theory); the dashed
line is the dark-matter density vertex, which delivers momentum q and energy omega; the wavy line is the phonon, emitted
with momentum -Q (upper sign) or absorbed with +Q (lower sign). The dotted horizontal line marks the intermediate state,
and the text below each panel gives its energy denominator as in eq:13.2-paths. Final state at the top: electron (c, k'),
k' = k + q + Q, and hole (v, k).
Run: python fig13_2.py   (numpy, matplotlib)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch13", "fig13_2.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})
EL, DM, PH = "k", "#2a6fb0", "#c4661f"


def fermion(ax, p0, p1, up=True, label=None, lpos=0.5, dx=0.03, ha="left"):
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=EL, lw=1.1)
    m = np.array(p0) + 0.55 * (np.array(p1) - np.array(p0))
    d = (np.array(p1) - np.array(p0)) / np.linalg.norm(np.array(p1) - np.array(p0))
    if not up:
        d = -d
    ax.annotate("", xy=m + 0.03 * d, xytext=m - 0.03 * d,
                arrowprops=dict(arrowstyle="-|>", color=EL, lw=1.0, mutation_scale=9))
    if label:
        t = np.array(p0) + lpos * (np.array(p1) - np.array(p0))
        ax.text(t[0] + dx, t[1], label, ha=ha, va="center", fontsize=7.5)


def dashed(ax, p0, p1, label, off=(0, -0.06)):
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=DM, lw=1.2, ls=(0, (3, 2)))
    ax.text(p0[0] + off[0], p0[1] + off[1], label, color=DM, fontsize=7.5, ha="left")


def wavy(ax, p0, p1, label, off=(0, 0.04), ha="right"):
    p0, p1 = np.array(p0), np.array(p1)
    t = np.linspace(0, 1, 300)
    L = np.linalg.norm(p1 - p0)
    d = (p1 - p0) / L
    n = np.array([-d[1], d[0]])
    pts = p0[None, :] + t[:, None] * (p1 - p0)[None, :] + 0.018 * np.sin(2 * np.pi * 7 * t)[:, None] * n[None, :]
    ax.plot(pts[:, 0], pts[:, 1], color=PH, lw=1.1)
    ax.text(p1[0] + off[0], p1[1] + off[1], label, color=PH, fontsize=7.5, ha=ha)


def vertex(ax, p):
    ax.plot([p[0]], [p[1]], "o", color="k", ms=3.2, zorder=5)


def cut(ax, y):
    ax.plot([0.02, 0.98], [y, y], color="0.6", lw=0.7, ls=":")


def frame(ax, title, den):
    ax.set_xlim(0, 1); ax.set_ylim(-0.12, 1.12); ax.axis("off")
    ax.text(0.0, 1.10, title, fontsize=8, va="top")
    ax.text(0.5, -0.08, den, fontsize=7.5, ha="center")


fig, axs = plt.subplots(1, 4, figsize=(6.6, 2.5))
V1, top = (0.5, 0.20), 0.84
dmlab = r"$\mathbfit{q},\,\omega$"
phlab = r"$\mp\mathbfit{Q},\,\nu$"
fin_c = r"$c\,\mathbfit{k}'$"
fin_v = r"$v\,\mathbfit{k}$"

# (a) path A: density first, phonon from the electron (intermediate electron p at k+q, any empty band)
ax = axs[0]; V2 = (0.63, 0.53)
fermion(ax, V1, V2, True, r"$p\,\mathbfit{k}{+}\mathbfit{q}$" + "\n(empty)", 0.30, 0.06)
fermion(ax, V2, (0.72, top), True, fin_c, 0.75, 0.03)
fermion(ax, V1, (0.24, top), False, fin_v, 0.85, -0.03, ha="right")
dashed(ax, (0.0, 0.08), V1, dmlab)
wavy(ax, V2, (0.98, 0.66), phlab, off=(0.0, 0.05))
vertex(ax, V1); vertex(ax, V2); cut(ax, 0.37)
frame(ax, "(a) A: density first,\n     electron emits", r"$\omega - \varepsilon_{p,\mathbfit{k}+\mathbfit{q}} + \varepsilon_{v\mathbfit{k}}$")

# (b) path B: phonon first creates the pair, the density then moves the electron (p at k+Q, empty)
ax = axs[1]; V2 = (0.63, 0.53)
fermion(ax, V1, V2, True, r"$p\,\mathbfit{k}{+}\mathbfit{Q}$" + "\n(empty)", 0.30, 0.06)
fermion(ax, V2, (0.72, top), True, fin_c, 0.75, 0.03)
fermion(ax, V1, (0.24, top), False, fin_v, 0.85, -0.03, ha="right")
wavy(ax, V1, (0.98, 0.10), phlab, off=(0.0, 0.09))
dashed(ax, (0.98, 0.72), V2, dmlab, off=(-0.12, -0.10))
vertex(ax, V1); vertex(ax, V2); cut(ax, 0.37)
frame(ax, "(b) B: phonon first,\n     density on the electron", r"$\varepsilon_{v\mathbfit{k}} - \varepsilon_{p,\mathbfit{k}+\mathbfit{Q}} \mp \omega_{\mathbfit{Q}\nu}$")

# (c) path C: density first creates (c k'; hole p at k+Q, filled), the hole then emits the phonon
ax = axs[2]; V2 = (0.37, 0.53)
fermion(ax, V1, (0.76, top), True, fin_c, 0.85, 0.03)
fermion(ax, V1, V2, False, r"$p\,\mathbfit{k}{+}\mathbfit{Q}$" + "\n(filled)", 0.30, -0.06, ha="right")
fermion(ax, V2, (0.28, top), False, fin_v, 0.75, -0.03, ha="right")
dashed(ax, (0.0, 0.08), V1, dmlab)
wavy(ax, V2, (0.02, 0.66), phlab, off=(0.0, 0.05), ha="left")
vertex(ax, V1); vertex(ax, V2); cut(ax, 0.37)
frame(ax, "(c) C: density first,\n     hole emits", r"$\omega - \varepsilon_{c\mathbfit{k}'} + \varepsilon_{p,\mathbfit{k}+\mathbfit{Q}}$")

# (d) path D: phonon first creates (c k'; hole p at k+q, filled), the density then moves the hole
ax = axs[3]; V2 = (0.37, 0.53)
fermion(ax, V1, (0.76, top), True, fin_c, 0.85, 0.03)
fermion(ax, V1, V2, False, r"$p\,\mathbfit{k}{+}\mathbfit{q}$" + "\n(filled)", 0.30, -0.06, ha="right")
fermion(ax, V2, (0.28, top), False, fin_v, 0.75, -0.03, ha="right")
wavy(ax, V1, (0.98, 0.10), phlab, off=(0.0, 0.09))
dashed(ax, (0.0, 0.42), V2, dmlab, off=(0.0, 0.04))
vertex(ax, V1); vertex(ax, V2); cut(ax, 0.37)
frame(ax, "(d) D: phonon first,\n     density on the hole", r"$\varepsilon_{p,\mathbfit{k}+\mathbfit{q}} - \varepsilon_{c\mathbfit{k}'} \mp \omega_{\mathbfit{Q}\nu}$")

fig.subplots_adjust(left=0.01, right=0.99, top=0.97, bottom=0.03, wspace=0.08)
fig.savefig(OUT)
print("wrote", OUT)
