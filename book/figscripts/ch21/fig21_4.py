"""Fig. 21.4 (fig:21-band): a silicon electron-recoil limit with its theory band, and the nuisance that dominates it.
Every number of Sect. 21.4 that concerns the silicon band across masses is printed to fig21_4.log.

Search: silicon, exposure 1 kg yr, one bin with every event of at least one pair (omega >= E_g = 1.17 eV), no event
  observed, no background.  Classical 90% upper limit N_90 = ln 10 = 2.303 (eq:1.5-N90), so
  sigma_lim = N_90 sigma_ref / (R(sigma_ref) x 1 kg yr), sigma_ref = 1e-37 cm^2 (eq:1.5-limit).
Rate and nuisances: nuis21.py (the Sect. 10.10 inputs and templates at every mass; see its docstring).
  Central value: RPA + LF tables as published (their scissor gives the measured T = 0 gap, 1.17 eV), from 1.17 eV.
  Random-phase level: RPA tables from the same gap (dotted line).
Band (keyresult eq:21.4-band, App. D.47): for one bin the limit scales as 1/rate, so g_k = -c_k with
  c_k = ln(rate at theta_k = 1 / central rate); sigma_g = (sum_k g_k^2)^(1/2); band sigma_lim exp(+-sigma_g).
Profiled limit: one lognormal nuisance of log-width sigma_g (independent standard-normal theta_k on one bin reduce to it,
  App. D.47), zero counts, zero background, in the book's construction (Neyman construction with the nuisance at its
  conditional best fit, Sect. 21.5): ratio exp(sigma_g^2 N_90), exact for one bin (nuis21.profile_ratio).
Mass range 1-10 MeV: below 1 MeV the first energy bins of the Essig table make the tabulation spread unreliable; above
  10 MeV the q <= 22.5 keV range of the KKL tables truncates the heavy-mediator rate.
Crossings of the nuisance sizes are found with brentq on the mass, not read from the plotting grid.
Run: python fig21_4.py (about 2 min).  Output: tex/figures/ch21/fig21_4.pdf, fig21_4.log.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nuis21 as N  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch21", "fig21_4.pdf")
LOG = open(os.path.join(HERE, "fig21_4.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")
    LOG.flush()


KEYS = ["attraction", "tabulation", "gap", "large-q LF"]
LAB = {"attraction": "electron–hole attraction", "tabulation": "tabulation spread",
       "gap": r"band energies ($0.1$ eV)", "large-q LF": r"local fields above $2q_0$"}
COL = {"attraction": "#c0392b", "tabulation": "#2471a3", "gap": "#7d3c98", "large-q LF": "#1e8449"}


def limit(rate):
    return N.N90 * N.SIG_REF / (rate * N.YR_EXPO)


def row(m, light):
    rc, c, fx = N.nuisances(m, light)
    sg = np.sqrt(sum(c[k] ** 2 for k in KEYS))
    rpa = N.tot(m, resp="rpa", light=light, dE=0.0)
    return rc, c, sg, rpa, fx


out("Sect. 21.4: silicon, 1 kg yr, one-pair bin (omega >= 1.17 eV), zero events, zero background, N_90 = %.4f" % N.N90)
out("profiled limit: Neyman construction at the conditional best fit, ratio exp(sigma^2 N_90)")

masses = np.geomspace(1e6, 10e6, 25)
res = {}
for light in (False, True):
    lab = "light" if light else "heavy"
    res[light] = [row(m, light) for m in masses]

# ---- printed points ----------------------------------------------------------------------------------------------
for light in (False, True):
    lab = "light" if light else "heavy"
    out("\n%s mediator:" % lab)
    for m in (1e6, 2e6, 3e6, 5e6, 10e6):
        rc, c, sg, rpa, fx = row(m, light)
        lim = limit(rc)
        prof = N.profile_ratio(sg)
        out("  %4.1f MeV: central rate %.4g /kg/yr -> sigma_lim %.3e cm2 ; RPA level rate %.4g -> %.3e cm2"
            " (central/RPA limit ratio %.3f)" % (m / 1e6, rc, lim, rpa, limit(rpa), limit(rc) / limit(rpa)))
        out("      c_k: " + "  ".join("%s %+.3f" % (k, c[k]) for k in KEYS) + " ; share omega<=10.5 eV %.3f" % fx)
        out("      rate factors 1 + delta_k = exp(c_k): " + "  ".join("%s %.3f" % (k, np.exp(c[k])) for k in KEYS))
        out("      sigma_g %.3f -> band x%.2f : %.3e - %.3e cm2 ; profiled/nominal %.3f -> %.3e cm2"
            % (sg, np.exp(sg), lim / np.exp(sg), lim * np.exp(sg), prof, lim * prof))
        out("      RPA-level limit inside the band: %s (ratio to central %.3f, lower band edge %.3f)"
            % (lim / np.exp(sg) <= limit(rpa) <= lim * np.exp(sg), limit(rpa) / lim, np.exp(-sg)))
        dom = max(KEYS, key=lambda k: abs(c[k]))
        out("      dominant: %s (%.0f %% of the variance)" % (dom, 100 * c[dom] ** 2 / sg**2))


# ---- crossings by root finding -----------------------------------------------------------------------------------
def diff(m, a, b, light):
    _, c, _ = N.nuisances(m, light)
    return abs(c[a]) - abs(c[b])


out("\nCrossings (brentq on the mass):")
for (a, b, lo, hi, light) in (("gap", "attraction", 1e6, 2e6, False), ("tabulation", "attraction", 3e6, 5e6, False),
                              ("large-q LF", "tabulation", 5e6, 10e6, False), ("gap", "attraction", 1e6, 2e6, True),
                              ("tabulation", "attraction", 5e6, 10e6, True)):
    try:
        mx = brentq(diff, lo, hi, args=(a, b, light), xtol=1e3)
        out("  %s: |%s| = |%s| at %.2f MeV" % ("light" if light else "heavy", a, b, mx / 1e6))
    except ValueError:
        out("  %s: |%s| - |%s| has no sign change on %.0f-%.0f MeV" % ("light" if light else "heavy", a, b, lo / 1e6,
                                                                           hi / 1e6))

# ---- figure -----------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6})
fig, ax = plt.subplots(1, 2, figsize=(7.0, 3.0))
mm = masses / 1e6
for light, col, name in ((False, "k", "heavy"), (True, "#b9770e", "light")):
    rc = np.array([r[0] for r in res[light]])
    sg = np.array([r[2] for r in res[light]])
    rpa = np.array([r[3] for r in res[light]])
    lim = limit(rc)
    ax[0].fill_between(mm, lim / np.exp(sg), lim * np.exp(sg), color=col, alpha=0.15, lw=0)
    ax[0].plot(mm, lim, color=col, lw=1.2, label="%s mediator" % name)
    ax[0].plot(mm, lim * np.array([N.profile_ratio(s) for s in sg]), color=col, lw=1.0, ls="--")
    ax[0].plot(mm, limit(rpa), color=col, lw=0.9, ls=":")
ax[0].set_xscale("log")
ax[0].set_yscale("log")
ax[0].set_xlabel(r"$m_\chi$ (MeV)")
ax[0].set_ylabel(r"$\bar\sigma_e^{\mathrm{lim}}$ (cm$^2$)")
ax[0].set_xlim(1, 10)
ax[0].legend(frameon=False, fontsize=8, loc="upper right")
ax[0].text(0.03, 0.04, "(a)", transform=ax[0].transAxes)

for k in KEYS:
    for light, ls in ((False, "-"), (True, "--")):
        ax[1].plot(mm, [abs(r[1][k]) for r in res[light]], color=COL[k], ls=ls, lw=1.1,
                   label=LAB[k] if not light else None)
ax[1].plot(mm, [r[2] for r in res[False]], color="k", lw=1.4, label=r"$\sigma_\beta$ (all four)")
ax[1].plot(mm, [r[2] for r in res[True]], color="k", lw=1.4, ls="--")
ax[1].set_xscale("log")
ax[1].set_xlim(1, 10)
ax[1].set_ylim(0, 1.3)
ax[1].set_xlabel(r"$m_\chi$ (MeV)")
ax[1].set_ylabel(r"$|\beta_k| = |\ln(1+\delta_k)|$")
ax[1].legend(frameon=False, fontsize=7, loc="upper right")
ax[1].text(0.03, 0.04, "(b)", transform=ax[1].transAxes)
fig.tight_layout()
fig.savefig(OUT)
out("\nwrote", os.path.relpath(OUT, HERE))
