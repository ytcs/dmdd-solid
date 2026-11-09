"""Fig. 17.5 (fig:17-window): heavy-mediator one-phonon rate ratios divided by the ratio of the figures of merit 1/c_NR1,
against the dark-matter mass.  Reads fom17_5_rates.npz written by fom17_5.py (rates of eq:11.1-rate with the book's halo,
omega_th = 1 meV, orientation average, q <= q_BZ; tensors and sources in fom17_5.py and figscripts/ch11/phon11.py).
Log: fig17_window.log.  Run: python fig17_window.py > fig17_window.log
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch17")
d = np.load(os.path.join(HERE, "fom17_5_rates.npz"))
m = d["m"]
names = ("Si", "Ge", "C", "CsI")
c = dict(zip(names, d["cNR1"]))
mhi = dict(zip(names, d["mhi"]))
pairs = [("Ge", "Si", "C1", "-"), ("C", "Si", "C0", "-"), ("CsI", "Si", "C2", "-"), ("C", "Ge", "C3", "--"),
         ("C", "CsI", "C4", "--")]
fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.axhspan(0.9, 1.1, color="0.9", lw=0)
ax.axhline(1, color="k", lw=0.7)
for A, B, col, ls in pairs:
    with np.errstate(divide="ignore", invalid="ignore"):
        r = d[A] / d[B] * c[A] / c[B]
    cap = min(mhi[A], mhi[B])
    sel = np.isfinite(r) & (r > 0)
    s1 = sel & (m <= cap)
    s2 = sel & (m >= cap)
    lab = {"C": "diamond"}.get(A, A) + "/" + {"C": "diamond"}.get(B, B)
    ax.plot(m[s1] / 1e3, r[s1], color=col, ls=ls, lw=1.4, label=lab)
    ax.plot(m[s2] / 1e3, r[s2], color=col, ls=":", lw=0.9)
    j = np.argmin(np.abs(m - cap))
    print("%-7s ratio near the cap (%.3f MeV): %.4f; at 0.1 MeV %.4f" % (lab, cap / 1e6, r[j], np.interp(1e5, m, r)))
for nm in names:
    ax.axvline(mhi[nm] / 1e3, color="0.6", lw=0.5, ls=":")
ax.set_xscale("log")
ax.set_xlim(8, 660)
ax.set_ylim(0.6, 1.4)
ax.set_xlabel(r"$m_\chi$ (keV)")
ax.set_ylabel(r"$(\mathcal{R}_A/\mathcal{R}_B)\,(c_{\mathrm{NR1},A}/c_{\mathrm{NR1},B})$")
ax.legend(fontsize=7.5, ncol=2, loc="lower right", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig17_window.pdf"))
print("wrote fig17_window.pdf")
