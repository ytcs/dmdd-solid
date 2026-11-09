"""Fig. 6.3 (fig:6-chain): the chain from DFT and DFPT on coarse grids to Wannier-interpolated electron-phonon vertices
on fine grids, with the long-range (Froehlich) part subtracted before the Wannier transform and restored after it.
A schematic: no numbers. The steps follow Sect. 6.2 and App. E.4, E.5 (eq:E.5-ginterp, eq:E.5-gL); the scheme is that of
Giustino, Cohen and Louie, PRB 76, 165108 (2007), extended to polar crystals by Verdi and Giustino, PRL 115, 176401 (2015).
Run: python fig6_3.py   (matplotlib only)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch06", "fig6_3.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

plt.rcParams.update({"font.size": 7.5, "font.family": "serif", "mathtext.fontset": "cm"})
BLUE, ORANGE, GREY = "#2a6fb0", "#c4661f", "0.35"

fig, ax = plt.subplots(figsize=(6.4, 3.3))
ax.set_xlim(0, 100)
ax.set_ylim(0, 54)
ax.axis("off")

W, H = 29, 9.4
boxes = {
    # column 1: first principles on coarse grids
    "dft":  (1, 40, "DFT ground state\n$\\psi_{n\\mathbfit{k}}$, $\\varepsilon_{n\\mathbfit{k}}$ on a coarse $\\mathbfit{k}$ grid", BLUE),
    "dfpt": (1, 24, "DFPT (Sternheimer)\n$\\partial_{\\kappa\\alpha,\\mathbfit{Q}}V_{\\mathrm{KS}}$, $\\omega_{\\mathbfit{Q}\\nu}$, $\\mathbfit{e}_{\\kappa\\nu}$ \non a coarse $\\mathbfit{Q}$ grid; $Z^*_\\kappa$, $\\varepsilon_\\infty$", BLUE),
    "gco":  (1, 8, "coarse vertices\n$g_{mn\\nu}(\\mathbfit{k},\\mathbfit{Q}) = g^{\\mathrm{S}} + g^{\\mathrm{L}}$", BLUE),
    # column 2: real space
    "wan":  (35.5, 40, "Wannier gauge $U(\\mathbfit{k})$\n$H^W(\\mathbfit{R})$", GREY),
    "gw":   (35.5, 16, "subtract $g^{\\mathrm{L}}$, rotate with $U$,\nundo $\\mathbfit{e}_{\\kappa\\nu}$, Fourier transform:\n$g^W(\\mathbfit{R}_e,\\mathbfit{R}_p)$, short-ranged", GREY),
    # column 3: fine grids
    "fine": (70, 40, "$\\varepsilon_{n\\mathbfit{k}}$, $U(\\mathbfit{k})$ from $H^W$;\n$\\omega_{\\mathbfit{Q}\\nu}$, $\\mathbfit{e}_{\\kappa\\nu}$ \nfrom the force constants", ORANGE),
    "gs":   (70, 24, "$g^{\\mathrm{S}}$ at any $(\\mathbfit{k},\\mathbfit{Q})$\nfrom $g^W$ and $U$", ORANGE),
    "gfin": (70, 8, "add $g^{\\mathrm{L}}$ analytically\n(from $Z^*_\\kappa$, $\\varepsilon_\\infty$):\n$g_{mn\\nu}(\\mathbfit{k},\\mathbfit{Q})$ on fine grids", ORANGE),
}
centers = {}
for key, (x, y, txt, col) in boxes.items():
    ax.add_patch(FancyBboxPatch((x, y), W, H, boxstyle="round,pad=0.4,rounding_size=1.2",
                                fc="white", ec=col, lw=1.0))
    ax.text(x + W / 2, y + H / 2, txt, ha="center", va="center", fontsize=6.6, linespacing=1.35)
    centers[key] = (x, y)


def arrow(a, b, side_a, side_b, text=None, dx=0, dy=0):
    def pt(k, s):
        x, y = centers[k]
        return {"r": (x + W + 0.6, y + H / 2), "l": (x - 0.6, y + H / 2),
                "t": (x + W / 2, y + H + 0.6), "b": (x + W / 2, y - 0.6)}[s]
    p, q = pt(a, side_a), pt(b, side_b)
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", lw=0.8, color="0.2", shrinkA=0, shrinkB=0))
    if text:
        ax.text((p[0] + q[0]) / 2 + dx, (p[1] + q[1]) / 2 + dy, text, fontsize=6, ha="center", color="0.25")


arrow("dft", "dfpt", "b", "t")
arrow("dfpt", "gco", "b", "t")
arrow("dft", "wan", "r", "l")
arrow("gco", "gw", "r", "l")
arrow("wan", "gw", "b", "t")
arrow("wan", "fine", "r", "l")
arrow("gw", "gs", "r", "l")
arrow("fine", "gs", "b", "t")
arrow("gs", "gfin", "b", "t")

for x, lab in ((1 + W / 2, "DFT and DFPT, coarse grids"), (35.5 + W / 2, "Wannier representation"),
               (70 + W / 2, "interpolation, fine grids")):
    ax.text(x, 53.5, lab, ha="center", va="center", fontsize=7.2, style="italic")

fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
