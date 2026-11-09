"""Limit Check 18.3a (lim:18.3a, fig:18-limit-a): the step model and the Ramanathan-Kurinsky split distributions against
the cascade seeded with the resolved dark-matter final states, in silicon, as a function of the deposit omega.

y = total-variation distance (1/2) sum_N |P_model(N) - P_DM(N)| between the pair-number distribution of each phenomenological
seed and that of the dark-matter seed at q0 = alpha m_e (both run through the same energy-only cascade of Sect. 18.1 with
the silicon constants of Sect. 18.2). Curves: step model (eq:1.5-step, eps_eh = 3.749 eV); Ramanathan-Kurinsky splits
(2004.10709 Eq. (7)) alpha -> infinity (equal split), alpha = 1 (uniform) and alpha -> 0 (all to one), hole above W_h
dropped; the photon (q -> 0) split of the same band model, the seed a photon calibration measures.
Shading: dark gray, omega below 4.37 eV, where the step model is within 0.1 of the dark-matter seed (and so are the
alpha = 1 and alpha -> infinity splits); light gray, omega above 12.95 eV, where the alpha = 1 and alpha -> infinity
splits are both within 0.1 (fine grid, 0.02 eV, casc18_3.log "fine grid" block). The 0.1 line is drawn.
Reads casc18_3.json; writes tex/figures/ch18/limit18_3a.pdf and limit18_3a.log.
"""
import os
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch18", "limit18_3a.pdf")
D = json.load(open(os.path.join(HERE, "casc18_3.json")))
f = D["fine"]
om = np.array(f["omega"])
env = np.maximum(np.array(f["uniform"]), np.array(f["equal"]))
lo = om[np.where(env > 0.1)[0][0]]
hi = om[np.where(env > 0.1)[0][-1]]
fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.axvspan(om[0], lo, color="0.80", lw=0)
ax.axvspan(hi, om[-1], color="0.90", lw=0)
ax.axhline(0.1, color="0.5", lw=0.6, ls=":")
ax.plot(om, f["step"], color="0.25", lw=1.2, label="step model")
ax.plot(om, f["equal"], color="C4", lw=1.2, label=r"R–K, equal split ($\alpha_{\mathrm{RK}}\to\infty$)")
ax.plot(om, f["uniform"], color="C2", lw=1.2, label=r"R–K, uniform ($\alpha_{\mathrm{RK}} = 1$)")
ax.plot(om, f["all1"], color="C3", lw=1.0, ls="--", label=r"R–K, all to one ($\alpha_{\mathrm{RK}}\to0$)")
ax.plot(om, f["photon"], color="C1", lw=1.6, label=r"photon seed ($q\to0$)")
ax.set_xlim(om[0], om[-1])
ax.set_ylim(0, 1.18)
ax.set_xlabel(r"deposit $\omega$ (eV)")
ax.set_ylabel(r"distance to dark-matter seed, $d_{\mathrm{TV}}$")
ax.legend(fontsize=7.2, frameon=False, loc="upper center", ncol=2)
fig.tight_layout()
fig.savefig(OUT)
log = [f"step-model region (TV <= 0.1, envelope too): omega < {lo:.2f} eV; envelope of alpha = 1, infinity within 0.1 above {hi:.2f} eV",
       f"photon seed max TV {max(f['photon']):.3f} at {om[int(np.argmax(f['photon']))]:.2f} eV",
       f"TV at 21 eV: all-to-one {f['all1'][-1]:.3f}, uniform {f['uniform'][-1]:.3f}, equal {f['equal'][-1]:.3f}, step {f['step'][-1]:.3f}, "
       f"photon {f['photon'][-1]:.3f}"]
st = np.array(f["step"])
for a in (4.92, 9.0):
    s_ = om > a
    log.append(f"step model: min TV for omega > {a} eV: {st[s_].min():.3f} at {om[s_][np.argmin(st[s_])]:.2f} eV")
open(os.path.join(HERE, "limit18_3a.log"), "w").write("\n".join(log) + "\n")
print("\n".join(log))
