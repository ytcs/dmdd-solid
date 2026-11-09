"""Fig. 18.3 (fig:18-pn10): the pair-number distribution P(N_eh) at omega = 10 eV in silicon for six seeds.

Reads casc18_3.json (written by casc18_3.py, which documents the cascade model and the seeds); writes
tex/figures/ch18/fig18_3.pdf and fig18_3.log. Every plotted number is in casc18_3.log ("omega = 10 eV" block).
Model choices (named in the caption): energy-only random-k cascade of Sect. 18.1 with the silicon constants of Sect. 18.2
(E_g = 1.160 eV, omega_AB = 63 meV, A_AB = 5.703 eV^3, W_h = 12 eV, theta_ii = 1; si_cascade18.py); dark-matter seed = independent-
particle pair weights of the density at q0 = alpha m_e along [100] in the empirical-pseudopotential bands; photon seed =
optical limit of the same bands; both used at the same excess energy omega - E_g; Ramanathan-Kurinsky splits of
2004.10709 Eq. (7) with alpha = 1 and the limits alpha -> 0, infinity; step model eq:1.5-step with eps_eh = 3.749 eV.
"""
import os
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch18", "fig18_3.pdf")
d = json.load(open(os.path.join(HERE, "casc18_3.json")))["P10"]
rows = [("DM", r"dark matter, $q_0$", "C0"), ("photon", "photon", "C1"),
        ("uniform", r"split $\alpha_{\mathrm{RK}} = 1$", "C2"), ("equal", r"equal split", "C4"),
        ("all1", r"all to one", "C3"), ("step", "step model", "0.35")]
N = np.arange(1, 5)
fig, ax = plt.subplots(figsize=(6.0, 3.6))
wbar = 0.13
log = []
for i, (k, lab, col) in enumerate(rows):
    P = np.clip(np.array(d[k])[1:5], 0, None)
    ax.bar(N + (i - 2.5) * wbar, P, wbar, color=col, label=lab, edgecolor="none")
    m = (np.arange(len(d[k])) * np.array(d[k])).sum()
    log.append(f"{k:8s} P(1..4) = " + " ".join(f"{p:.3f}" for p in P) + f"  mean {m:.3f}")
ax.set_xticks(N)
ax.set_xlabel(r"pair number $N_{\mathrm{eh}}$")
ax.set_ylabel(r"$P(N_{\mathrm{eh}})$ at $\omega = 10$ eV")
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(OUT)
open(os.path.join(HERE, "fig18_3.log"), "w").write("\n".join(log) + "\n")
print("\n".join(log))
