"""Limit 11.6a (fig:11-limit-6a): incoherent one-phonon absorption through unpolarized nuclear spins in natural silicon.
Formula (Bloch, Knapen, Madden, Marocco, arXiv:2411.10542, Eq. (31)): the rate per mass is proportional to the host projected density
of states D(omega) at omega = m_phi, for every spin-carrying isotope. Fuller result (this section): the spin sits on 29Si, which is
heavier than the mean by 3.2 %, and its own local density of states D_29(omega) follows from the single-defect (Lifshitz) Green
function, Eq. (11.6-lifshitz), exact for one defect in the harmonic host. The plotted ratio R_exact/R_formula = D_29/D is independent
of the coupling. Leading correction: first order in the mass defect, 1 + delta_29 h(omega), Eq. (11.6-first).
Inputs and model: iso11.py (PBE DOS of Sect. 5.2, AME2020 masses, IUPAC abundances). Shaded: |D_29/D - 1| <= 0.10.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import iso11 as I  # noqa: E402

d29 = I.DELTA[1]
om = np.linspace(0.5e-3, I.WMAX * 0.9995, 2500)
Dh = np.interp(om, I.W, I.D)
ok = Dh > 1e-3 * Dh.max()
om, Dh = om[ok], Dh[ok]
r = I.ldos_ratio(om, d29)
r1 = 1 + d29 * I.h_first(om)
good = np.abs(r - 1) <= 0.10
bad = om[~good]
print(f"delta_29 = {d29:+.5f}; omega_max = {I.WMAX*1e3:.2f} meV")
print(f"max |D_29/D - 1| below 60 meV: {np.max(np.abs(r[om < 0.060] - 1)):.4f}; first-order max error vs exact below 60 meV: "
      f"{np.max(np.abs(r1[om < 0.060] - r[om < 0.060])):.4f}")
print(f"frequencies with |D_29/D - 1| > 0.10: {bad.min()*1e3 if bad.size else np.nan:.2f} - {bad.max()*1e3 if bad.size else np.nan:.2f} meV"
      f" ({bad.size} of {om.size} points)")
for o in (0.010, 0.020, 0.030, 0.040, 0.050, 0.058, 0.060, 0.062, 0.063):
    k = np.argmin(abs(om - o))
    print(f"  {om[k]*1e3:5.1f} meV: exact {r[k]:.4f}, first order {r1[k]:.4f}")
lo = om < 0.055
print(f"below 55 meV: ratio range {r[lo].min():.4f} - {r[lo].max():.4f}; max |first order - exact| = {np.max(np.abs(r1[lo]-r[lo])):.4f}")
# rate-weighted mean over the band (weight D): integral of D_29 over integral of D = 1 (sum rule check)
print(f"int D_29 / int D over the band = {np.sum(r*Dh)/np.sum(Dh):.4f}")
# first frequency from below at which the ratio leaves the 10 % window
edge = om[np.argmax(~good)] if (~good).any() else np.nan
print(f"formula within 10 % for omega < {edge*1e3:.2f} meV = {edge/I.WMAX:.3f} omega_max")

fig, ax = plt.subplots(figsize=(5.0, 3.3))
ax.axvspan(0, edge * 1e3, color="0.88", lw=0)
ax.axhline(1.0, color="k", ls="--", lw=1.0, label="host density of states (formula)")
ax.plot(om * 1e3, r1, color="0.35", ls=":", lw=1.2, label=r"first order, $1 + \delta_{29}h(\omega)$")
ax.plot(om * 1e3, r, color="C3", lw=1.5, label=r"single defect, exact")
ax.set_xlim(0, I.WMAX * 1e3 + 0.5)
ax.set_ylim(0.6, 1.85)
ax.set_xlabel(r"$\omega = m_\phi$ (meV)")
ax.set_ylabel(r"$g_{29}(\omega)/g_{\mathrm{ph},\kappa}(\omega)$")
ax.legend(fontsize=7, frameon=False, loc="upper left")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_6a.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
