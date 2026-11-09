"""Fig. 4.4 of Sect. 4.4: schematic of the geometric series R = R~ + R~ v_C R~ + R~ v_C R~ v_C R~ + ...
Proper parts R~ drawn as shaded blobs, Coulomb kernels v_C(q) as wavy lines.  Schematic only: no numbers, no data.
Output: tex/figures/ch04/fig4_4.pdf
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.abspath(os.path.join(HERE, "..", "..")), "tex", "figures", "ch04")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "font.family": "serif", "mathtext.fontset": "cm"})

fig, ax = plt.subplots(figsize=(6.3, 1.25))
ax.set_xlim(0, 13.6); ax.set_ylim(-0.55, 0.55); ax.set_aspect("equal"); ax.axis("off")


def blob(x, label, shaded=True):
    th = np.linspace(0, 2 * np.pi, 100)
    ax.fill(x + 0.32 * np.cos(th), 0.32 * np.sin(th), color="C0" if shaded else "C1", alpha=0.25, lw=0)
    ax.plot(x + 0.32 * np.cos(th), 0.32 * np.sin(th), color="C0" if shaded else "C1", lw=1.0)
    ax.text(x, -0.02, label, ha="center", va="center")


def wavy(x0, x1):
    xs = np.linspace(x0, x1, 200)
    ax.plot(xs, 0.07 * np.sin(2 * np.pi * (xs - x0) / 0.18), color="0.25", lw=1.0)


def leg(x0, x1):
    ax.plot([x0, x1], [0, 0], color="0.25", lw=1.0)


x = 0.25
leg(x, x + 0.25); blob(x + 0.57, r"$R$", shaded=False); leg(x + 0.89, x + 1.14)
ax.text(x + 1.5, 0, "=", ha="center", va="center", fontsize=12)
x = 2.0
leg(x, x + 0.2); blob(x + 0.52, r"$\tilde R$"); leg(x + 0.84, x + 1.04)
ax.text(x + 1.3, 0, "+", ha="center", va="center", fontsize=12)
x = 3.55
leg(x, x + 0.2); blob(x + 0.52, r"$\tilde R$"); wavy(x + 0.84, x + 1.5); blob(x + 1.82, r"$\tilde R$"); leg(x + 2.14, x + 2.34)
ax.text(x + 1.17, 0.27, r"$v_{\mathrm{C}}$", ha="center", fontsize=9)
ax.text(x + 2.6, 0, "+", ha="center", va="center", fontsize=12)
x = 6.4
leg(x, x + 0.2); blob(x + 0.52, r"$\tilde R$"); wavy(x + 0.84, x + 1.5); blob(x + 1.82, r"$\tilde R$")
wavy(x + 2.14, x + 2.8); blob(x + 3.12, r"$\tilde R$"); leg(x + 3.44, x + 3.64)
ax.text(x + 3.85, 0, r"$+\ \cdots$", ha="left", va="center", fontsize=12)   # gap after the last leg
ax.text(11.35, 0, r"$= \tilde R + \tilde R\,v_{\mathrm{C}}R$", ha="left", va="center", fontsize=10)
fig.savefig(os.path.join(OUT, "fig4_4.pdf"), bbox_inches="tight")
print("wrote fig4_4.pdf")
