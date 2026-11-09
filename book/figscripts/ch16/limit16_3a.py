"""Limit Check 16.3a (lim:16.3a, fig:16-limit-ejection) and Fig. 16.3 (fig:16-ejection): vacuum ejection of graphene pi
electrons with plane-wave final states (the published form, Hochberg et al. arXiv:1606.08849 Eqs. (5), (7)) against the
same rate with the final plane wave orthogonalized to the initial orbital (OPW).  Model and inputs: eject16_3.py.

Limit Check plot: x = E_ej (eV), 0.3-300; y = (dR/dlnE_ej)_OPW / (dR/dlnE_ej)_PW for m_chi = 10 and 100 MeV, heavy mediator;
thin line at 1 (the published plane-wave form); dotted: the Fermi factor 2 pi xi/(1 - e^{-2 pi xi}), xi = alpha m_e/p_ej
(eq:2.2-fermi with Z_eff = 1), the unscreened upper end of the final-state interaction; shaded: E_ej where the OPW factor
is within 10 % of 1 for both masses.
Fig. 16.3: dR/dlnE_ej per kg-yr at sigma_e = 1e-37 cm^2, PW (dashed) and OPW (solid), m_chi = 10, 100 MeV, (a) heavy,
(b) light mediator F_DM = (alpha m_e/q)^2.
Also printed: kinematic threshold (m_min, q_min), PW/OPW amplitude-ratio table (q along / across / at 45 degrees to the
orbital axis), integrated rates, Fermi factors, and grid-convergence checks.
Run: python limit16_3a.py  (about one minute)
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
import eject16_3 as E  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")
os.makedirs(FIG, exist_ok=True)

# ---- kinematics -------------------------------------------------------------------------------------------------
vmax = E.VMAX
mmin = 2 * E.PHI_WF / vmax**2
print(f"v_max = {vmax:.4e}; ejection threshold omega >= Phi_wf = {E.PHI_WF} eV")
print(f"  lightest mass that can eject (omega_max = m v_max^2/2): m_min = 2 Phi_wf/v_max^2 = {mmin/1e6:.3f} MeV")
print(f"  smallest momentum transfer at threshold q_min = Phi_wf/v_max = {E.PHI_WF/vmax/1e3:.3f} keV")
print(f"  orbital momentum scale beta = Z_eff/(2 a0) = {E.BETA/1e3:.3f} keV (Z_eff = {E.ZEFF})")
for m in (10e6, 100e6):
    print(f"  m_chi = {m/1e6:.0f} MeV: largest omega = {m*vmax**2/2:.1f} eV, largest E_ej (E_B = 0) = {m*vmax**2/2-E.PHI_WF:.1f} eV")

# ---- OPW amplitude at q -> 0 ---------------------------------------------------------------------------------------
p50 = np.sqrt(2 * E.ME * 50.0)
for q in (1.0, 10.0, 100.0):
    KP, KO = E.K_table(np.array([p50]), np.array([q]))
    print(f"q = {q:5.0f} eV, E_ej = 50 eV: K_PW = {KP[0,0]:.3e}, K_OPW = {KO[0,0]:.3e} eV^-3 (OPW -> 0 as q^2)")

# ---- amplitude-ratio table ---------------------------------------------------------------------------------------
print("\n|M_OPW|^2/|M_PW|^2 integrated over final directions, min-max over q along, across and at 45 deg to the axis:")
qs = np.array([5, 7.5, 15, 25, 40]) * 1e3
print("  E_ej \\ q (keV): " + "  ".join(f"{q/1e3:>9.1f}" for q in qs))
tab = {}
for beta, name in ((E.BETA, "Z_eff = 4.03"), (E.BETA_ALT, "Slater 1.568/a0")):
    lo_all, hi_all = [], []
    for Ek in (10, 50, 100):
        p = np.sqrt(2 * E.ME * Ek)
        rs = []
        for cq in (1.0, 0.0, np.sqrt(0.5)):
            KP, KO = E.K_table(np.array([p]), qs, beta=beta, fixed_cq=cq)
            rs.append(KO[0] / KP[0])
        rs = np.array(rs)
        tab[(name, Ek)] = (rs.min(0), rs.max(0))
        print(f"  [{name}] {Ek:4d} eV (k_f = {p/1e3:.1f} keV): " + "  ".join(f"{a:.2f}-{b:.2f}" for a, b in zip(rs.min(0), rs.max(0))))
        if Ek >= 50:
            lo_all.append(rs.min())
            hi_all.append(rs.max())
    print(f"  [{name}] range at 50-100 eV, q = 5-40 keV: {min(lo_all):.2f} to {max(hi_all):.2f}")

# ---- rate-weighted factor ----------------------------------------------------------------------------------------
Eej = np.geomspace(0.3, 300, 61)
pg = np.sqrt(2 * E.ME * Eej)
qg = np.geomspace(300, 6e5, 220)
KP, KO = E.K_table(pg, qg)
cen, w, meanEB = E.pi_dos()
print(f"\npi band: E_B from 0 to 3t = {3*E.T_HOP:.1f} eV, mean {meanEB:.2f} eV (t = {E.T_HOP} eV)")
res = {}
for light in (False, True):
    for m in (10e6, 100e6):
        RP, RO = E.spectrum(Eej, KP, KO, pg, qg, m, cen, w, light=light)
        res[(light, m)] = (RP, RO)
        lab = "light" if light else "heavy"
        ok = RP > 0
        tot_p = np.trapezoid(RP[ok], np.log(Eej[ok]))
        tot_o = np.trapezoid(RO[ok], np.log(Eej[ok]))
        r = RO[ok] / RP[ok]
        print(f"{lab} m = {m/1e6:.0f} MeV: R_PW = {tot_p:.3e}, R_OPW = {tot_o:.3e} /kg/yr (pi electrons, sigma_e = 1e-37 cm^2);"
              f" OPW/PW total = {tot_o/tot_p:.3f}; spectral ratio from {r.min():.3f} to {r.max():.3f}"
              f" (max at E_ej = {Eej[ok][np.argmax(r)]:.1f} eV); PW peak at {Eej[np.argmax(RP)]:.2f} eV, OPW peak at {Eej[np.argmax(RO)]:.2f} eV")

# 10 % band (heavy) by root-finding on the interpolated log ratio
def ratio_fn(m):
    RP, RO = res[(False, m)]
    ok = RP > 1e-30 * RP.max()
    x, y = np.log(Eej[ok]), np.log(RO[ok] / RP[ok])
    return lambda e: np.interp(np.log(e), x, y), Eej[ok]


lims = {}
for m in (10e6, 100e6):
    f, ee = ratio_fn(m)
    lo = brentq(lambda e: f(e) - np.log(1.1), ee[0], 30)
    lims[m] = [lo]
    if m == 100e6:
        hi = brentq(lambda e: f(e) - np.log(1.1), 60, 200)
        lims[m].append(hi)
    print(f"heavy {m/1e6:.0f} MeV: OPW within 10 % of PW for E_ej < {lo:.2f} eV" + (f" and E_ej > {lims[m][1]:.0f} eV" if m == 100e6 else ""))
    for e0 in (1, 5, 10, 20, 50, 100):
        if e0 <= ee[-1]:
            print(f"    ratio at {e0:5.0f} eV: {np.exp(f(e0)):.3f}")

# Fermi factors
def fermi(Ek):
    xi = E.ALPHA * E.ME / np.sqrt(2 * E.ME * Ek)
    return 2 * np.pi * xi / (1 - np.exp(-2 * np.pi * xi))


print("Fermi factor (Z_eff = 1): " + ", ".join(f"{fermi(e):.2f} at {e} eV" for e in (10, 50, 100)))

# convergence: doubled angular grids at two points
pc = np.sqrt(2 * E.ME * np.array([10.0, 30.0]))
qc = np.array([3e3, 15e3])
a = E.K_table(pc, qc)
b = E.K_table(pc, qc, n_th=96, n_ph=96, n_q=32)
print("grid check (K_OPW/K_PW, standard vs doubled angular grids):",
      np.round(a[1] / a[0], 5).ravel(), np.round(b[1] / b[0], 5).ravel())

# ---- figures -----------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
for m, c in ((10e6, "C0"), (100e6, "C3")):
    RP, RO = res[(False, m)]
    ok = RP > 1e-12 * RP.max()
    ax.plot(Eej[ok], RO[ok] / RP[ok], color=c, lw=1.4, label=rf"OPW/PW, $m_\chi = {m/1e6:.0f}$ MeV")
ax.plot(Eej, fermi(Eej), "k:", lw=1.0, label=r"Fermi factor, $Z_{\mathrm{eff}} = 1$")
ax.axhline(1, color="k", lw=0.6)
ax.axvspan(Eej[0], min(lims[10e6][0], lims[100e6][0]), color="0.85", lw=0)
ax.axvspan(lims[100e6][1], Eej[-1], color="0.85", lw=0)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.3, 300)
ax.set_ylim(0.7, 12)
ax.set_xlabel(r"$E_{\mathrm{ej}}$ (eV)")
ax.set_ylabel("ratio to the plane-wave spectrum")
ax.legend(fontsize=7, loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_3a.pdf"))

fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.8), sharey=False)
for k, light in enumerate((False, True)):
    axx = axs[k]
    for m, c in ((10e6, "C0"), (100e6, "C3")):
        RP, RO = res[(light, m)]
        ok = RP > 1e-8 * RP.max()
        axx.plot(Eej[ok], RO[ok], color=c, lw=1.4, label=rf"$m_\chi = {m/1e6:.0f}$ MeV, OPW")
        axx.plot(Eej[ok], RP[ok], color=c, lw=1.0, ls="--", label="plane wave")
    axx.set_xscale("log")
    axx.set_yscale("log")
    axx.set_xlim(0.3, 300)
    top = max(res[(light, 10e6)][1].max(), res[(light, 100e6)][1].max())
    axx.set_ylim(top * 1e-4, top * 3)
    axx.set_xlabel(r"$E_{\mathrm{ej}}$ (eV)")
    axx.set_title("(a) heavy mediator" if not light else "(b) light mediator", fontsize=9)
axs[0].set_ylabel(r"$\mathrm{d}\mathcal{R}/\mathrm{d}\ln E_{\mathrm{ej}}$ (kg$^{-1}$ yr$^{-1}$)")
axs[0].legend(fontsize=6.5, frameon=False, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig16_3.pdf"))
print("wrote limit16_3a.pdf and fig16_3.pdf")
