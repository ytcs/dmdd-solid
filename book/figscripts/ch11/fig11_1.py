"""Fig. 11.1: single-acoustic-phonon rate per unit target mass for silicon, germanium and diamond, light and heavy mediators.
Output: tex/figures/ch11/fig11_1.pdf. Prints the plotted values at a few masses.

Rate: eq:11.1-rate (phon11.rate_per_mass): long-wavelength acoustic branches from the Christoffel problem of the measured
room-temperature tensors (phon11.MATS: Si [M19], Ge and diamond [H26]), orientation-averaged (halo through eta, Sect. 1.3),
G = 0, e^{-2W} = 1, F_N = 1, equal proton and neutron couplings, omega_th = 1 meV, momentum transfers q <= q_BZ.
Normalization: sigma_p = 1e-45 cm^2 with F_DM = (q0/q)^2, q0 = alpha m_e (light); sigma_p = 1e-40 cm^2 with F_DM = 1 (heavy);
rho_chi = 0.3 GeV/cm^3; standard halo of Sect. 1.2.
Light panel, dotted: the target-independent limit eq:11.1-light. Heavy panel: solid up to m_hi = q_BZ/(2 v_max), dashed above,
where the cut q <= q_BZ, not the physics, sets the fall (multiphonon and Umklapp terms, Sect. 11.3, take over).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phon11 as P  # noqa: E402

SIG_L, SIG_H = 1e-45, 1e-40
GRID = P.sphere_grid(16, 32)        # 512 directions: rates change by < 0.1 % against the 48 x 96 grid (checked below)
ms = np.logspace(np.log10(2.5e3), 7, 60)
_full, _fast = P.rate_per_mass(0.1e6, "Si", "heavy"), P.rate_per_mass(0.1e6, "Si", "heavy", av=P.averages("Si", *GRID))
print("grid check, Si heavy at 0.1 MeV: 4608 directions %.3f, 512 directions %.3f" % (_full, _fast))
lab = {"Si": "Si", "Ge": "Ge", "C": "diamond"}
col = {"Si": "C3", "Ge": "C0", "C": "C2"}
fig, axs = plt.subplots(1, 2, figsize=(7.0, 3.1))
for nm in ("Si", "Ge", "C"):
    av = P.averages(nm, *GRID)
    RL = np.array([P.rate_per_mass(m, nm, "light", sigp=SIG_L, av=av) for m in ms])
    RH = np.array([P.rate_per_mass(m, nm, "heavy", sigp=SIG_H, av=av) for m in ms])
    mhi = av["qBZ"] / (2 * P.VMAX)
    axs[0].loglog(ms / 1e6, np.where(RL > 0, RL, np.nan), color=col[nm], lw=1.4, label=lab[nm])
    lo = ms <= mhi
    axs[1].loglog(ms[lo] / 1e6, np.where(RH[lo] > 0, RH[lo], np.nan), color=col[nm], lw=1.4, label=lab[nm])
    axs[1].loglog(ms[~lo] / 1e6, RH[~lo], color=col[nm], lw=1.0, ls="--")
    for m in (0.01e6, 0.03e6, 0.1e6, 0.3e6, 1e6):
        print("%-2s m = %5.2f MeV: light %.3e, heavy %.3e events/kg/yr"
              % (nm, m / 1e6, P.rate_per_mass(m, nm, "light", sigp=SIG_L, av=av), P.rate_per_mass(m, nm, "heavy", sigp=SIG_H, av=av)))
    print("   edge m_min^ac at c_LA,max = %.2f keV; heavy plateau 0.2 MeV: %.0f; ratio to Si plateau x c ratio below"
          % (P.mmin_ac(av["cLAmax"]) / 1e3, P.rate_per_mass(0.2e6, nm, "heavy", sigp=SIG_H, av=av)))
avs = {nm: P.averages(nm, *GRID) for nm in ("Si", "Ge", "C")}
for nm in ("Ge", "C"):
    r = P.rate_per_mass(0.2e6, nm, "heavy", sigp=SIG_H, av=avs[nm]) / P.rate_per_mass(0.2e6, "Si", "heavy", sigp=SIG_H, av=avs["Si"])
    print("heavy %s/Si at 0.2 MeV = %.3f; inverse ratio of effective speeds = %.3f" % (nm, r, avs["Si"]["cNR1"] / avs[nm]["cNR1"]))
axs[0].loglog(ms / 1e6, [P.light_leading(m, sigp=SIG_L) for m in ms], color="k", lw=0.8, ls=":", label=r"$\propto 1/\omega_{\mathrm{th}}$ limit")
axs[0].set_title(r"light mediator, $\sigma_p = 10^{-45}\,\mathrm{cm^2}$", fontsize=9)
axs[1].set_title(r"heavy mediator, $\sigma_p = 10^{-40}\,\mathrm{cm^2}$", fontsize=9)
for ax in axs:
    ax.set_xlim(2.5e-3, 10)
    ax.set_xlabel(r"$m_\chi$ [MeV]")
    ax.legend(fontsize=7, frameon=False, loc="lower center" if ax is axs[1] else "upper right")
axs[0].set_ylim(1e-1, 1e7)
axs[1].set_ylim(1, 3e3)
axs[0].set_ylabel(r"rate [events kg$^{-1}$ yr$^{-1}$]")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "fig11_1.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
