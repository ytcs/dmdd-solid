"""Fig. 21.2 (fig:21-hib): the halo-independent bound on eta-tilde(u0) for silicon against the standard-halo eta-tilde at the
cross section of the standard-halo limit, for m_chi = 2 and 10 MeV, heavy mediator. Output tex/figures/ch21/fig21_2.pdf, log
fig21_2.log (every number quoted in Sect. 21.2 from this figure).

Hypothetical search (as in Sect. 21.2): exposure 1 kg yr, no events in the one-, two- and three-pair bins of the energy-only
cascade of Sect. 18.3 (E_g = 1.160 eV, eps_eh = 3.749 eV; hib21.pbin), no background; per-bin upper count N_up = ln 30 = 3.401 (96.7 % per bin), so
that the three bins hold jointly at >= 90 % (Bonferroni, 3 x 3.33 %). Kernel and columns: hib21.py (Essig et al. table).
Bound (eq:21.2-hib): eta-tilde(u0) <= min_n N_up / A_n(u0), the step columns A_n of hib21.column.
Standard halo: eta-tilde(u) = (rho_chi sigma_e/m_chi) eta_SHM(u) (App. D.1 closed form, v_E^ref = 250.5 km/s), at the cross
section sigma_lim where the first bin reaches N_up: sigma_lim = min_n N_up / N_n(sigma = 1 cm^2).
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
import hib21 as B  # noqa: E402
import halo21 as H  # noqa: E402

NUP = np.log(30.0)
BINS = (1, 2, 3)
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch21", "fig21_2.pdf")
LOG = open(os.path.join(HERE, "fig21_2.log"), "w")


def say(s):
    print(s)
    LOG.write(s + "\n")


say(f"N_up per bin = ln 30 = {NUP:.4f}; exposure {B.EXPO} kg yr; cascade of Sect. 18.3, E_g = {B.EG} eV, eps_eh = {B.EPS} eV")
u = np.linspace(150.0, B.VMAX, 1300)
fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2), sharey=False)
for ax, m, lab in zip(axes, (2e6, 10e6), ("(a)", "(b)")):
    A = {n: B.column(m, n, u) for n in BINS}
    with np.errstate(divide="ignore"):
        bnd = {n: np.where(A[n] > 0, NUP / A[n], np.inf) for n in BINS}
    tight = np.minimum.reduce([bnd[n] for n in BINS])
    which = np.argmin(np.array([bnd[n] for n in BINS]), axis=0) + 1
    # standard-halo limit
    unit1 = B.etatilde_unit(m, 1.0)
    Nn = {n: B.counts_eta(m, n, lambda v: unit1 * H.eta_shm(v)) for n in BINS}
    sig = min(NUP / Nn[n] for n in BINS if Nn[n] > 0)
    nbind = min((n for n in BINS if Nn[n] > 0), key=lambda n: NUP / Nn[n])
    say(f"m = {m/1e6:.0f} MeV: SHM counts per cm^2: " + ", ".join(f"bin {n}: {Nn[n]:.4e}" for n in BINS))
    say(f"  SHM limit sigma_lim = {sig:.4e} cm^2 (set by bin {nbind}); counts there: "
        + ", ".join(f"{n}: {sig*Nn[n]:.3f}" for n in BINS))
    eshm = sig * unit1 * H.eta_shm(u)
    # threshold speed of each bin (smallest v_min with weight)
    for n in BINS:
        vm, w, _ = B.cells(m, n)
        if (w > 0).any():
            say(f"  bin {n}: lowest v_min with weight = {vm[w > 0].min():.1f} km/s; A_n(v_max) = {B.column(m, n, B.VMAX):.4e} yr")
    # where the binding bin changes
    ch = np.nonzero(np.diff(which))[0]
    for i in ch:
        f = lambda x: NUP / max(B.column(m, which[i], x), 1e-300) - NUP / max(B.column(m, which[i + 1], x), 1e-300)
        try:
            x0 = brentq(f, u[i], u[i + 1] + 1e-9)
        except ValueError:
            x0 = 0.5 * (u[i] + u[i + 1])
        say(f"  binding bin changes from {which[i]} to {which[i+1]} near u0 = {x0:.1f} km/s")
    ok = np.isfinite(tight) & (eshm > 0)
    r = tight[ok] / eshm[ok]
    i = np.argmin(r)
    say(f"  smallest ratio bound / eta-tilde_SHM = {r[i]:.3f} at u0 = {u[ok][i]:.1f} km/s (plotting grid; refined below)")
    # refine the minimum of the ratio with a fine local grid
    uf = np.linspace(max(150, u[ok][i] - 20), min(B.VMAX - 1e-6, u[ok][i] + 20), 4001)
    Af = np.minimum.reduce([np.where(B.column(m, n, uf) > 0, NUP / np.maximum(B.column(m, n, uf), 1e-300), np.inf)
                            for n in BINS])
    rf = Af / (sig * unit1 * H.eta_shm(uf))
    j = np.argmin(rf)
    say(f"  refined: smallest ratio {rf[j]:.4f} at u0 = {uf[j]:.2f} km/s")
    for u0 in (400.0, 500.0, 600.0, 700.0, 780.0):
        b = min(NUP / B.column(m, n, u0) if B.column(m, n, u0) > 0 else np.inf for n in BINS)
        e = sig * unit1 * H.eta_shm(u0)
        say(f"  u0 = {u0:.0f}: bound {b:.4e} /yr, SHM {e:.4e} /yr, ratio {b/e:.3f}")
    sc = 1e-20
    for n in BINS:
        ax.plot(u, bnd[n] / sc, lw=0.8, ls=(0, (3, 2)), color="0.55")
        k = np.isfinite(bnd[n])
        if k.any():
            pos = {2e6: {1: (470, 0.45), 2: (690, 1.6)}, 10e6: {1: (440, 1.45), 2: (330, 0.45), 3: (455, 1.3)}}[m]
            if n in pos:
                jj = np.argmin(np.abs(u - pos[n][0]))
                ax.text(u[jj], bnd[n][jj] / sc * pos[n][1], f"{n} pair" + ("s" if n > 1 else ""), fontsize=7,
                        color="0.4", ha="center")
    ax.plot(u, tight / sc, color="C0", lw=1.6, label="halo-independent bound")
    ax.plot(u, eshm / sc, color="C3", lw=1.3, ls="--", label=r"standard halo at $\bar\sigma_e^{\mathrm{lim}}$")
    ax.axvline(B.VMAX, color="0.3", lw=0.7, ls=":")
    ax.set_yscale("log")
    ax.set_xlim(250, 820)
    ax.set_ylim((1e-2, 1e2) if m > 5e6 else (1e-1, 1e4))
    ax.set_xlabel(r"$u_0$ (km s$^{-1}$)")
    ax.set_title(f"{lab} $m_\\chi = {m/1e6:.0f}$ MeV", fontsize=9)
    ax.tick_params(labelsize=8)
axes[0].set_ylabel(r"$\tilde\eta(u_0)$ ($10^{-20}$ yr$^{-1}$)")
axes[1].legend(fontsize=7, loc="upper right", frameon=False)
fig.tight_layout()
fig.savefig(OUT)
say(f"wrote {OUT}")
