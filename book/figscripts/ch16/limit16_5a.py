"""Limit Check 16.5a (lim:16.5a, fig:16-limit-dopant): dark-photon absorption by donors.  The published form,
R = zeta^2 (rho_chi/rho_T) W(0, m_phi) with W = eps_2^D/|eps_host|^2 (Du et al., arXiv:2212.04504v1, Eqs. (10), (12) and
the absorption sentence after Eq. (12)), is the first order in n_D of the loss function of the doped crystal.  The
fuller result is the loss function of the effective medium, L = Im[-1/eps_eff], eps_eff = eps_host (1 + 2y)/(1 - y),
y = eps^D/(3 eps_host) (Clausius-Mossotti / Maxwell Garnett form; Sect. 16.3 uses the same form for dots).

Plot: x = n_D (cm^-3), 1e13 - 3e18; y = L_full/L_lin.  Donor model of donor16_5.py: central-cell ground state (r_c = 3.2 A,
1s at the measured 45.59 meV; 'CC0.10'); curves at m_phi = 60 meV
(continuum) and at the 1s(A1) -> 2p0 line centre, 34.11 meV, with full widths 0.034 cm^-1 (4.2 ueV, the narrowest
measured width, in 28Si, quoted by Vinh et al., arXiv:0812.0148, p. 5) and 0.1 meV (an illustrative concentration-broadened
line).  Dotted: the expansion 1 - 4 Re y + 4(3 Re y^2 - Im y^2) for the continuum curve and the line at 4.2 ueV.
Shading: grey where the 60 meV ratio is within 10 % of one; hatched n_D >= 0.3 n_c with
n_c = 3e18 cm^-3, the metal-insulator density of uncompensated Si:P quoted by Du et al. (Sect. II, ">~ 3e18").
Continuum: Gaussian sigma 1.5 meV on the box-discretized states (donorspec16_5.py).
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
import donorspec16_5 as S  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")
os.makedirs(FIG, exist_ok=True)
G_NARROW = 0.034 * 1.239842e-1      # meV (0.034 cm^-1)
G_BROAD = 0.1
SIG = 1.5
NC = 3e18
W2P0 = 45.59 - 11.48

mods = {"CC0.10": S.model("CC0.10")}
nD = np.geomspace(1e13, 3e18, 400)


def ratio(s, om, gam, n):
    A = S.A_of_omega(s, om, gam, SIG)[0]
    eD = S.epsD(A, n)
    return S.L_full(eD) / S.L_lin(eD), eD


print(f"eps_host = {S.EPS}; 2p0 line at {W2P0:.2f} meV; widths {G_NARROW*1e3:.2f} ueV and {G_BROAD} meV")
curves = {}
for key, s in mods.items():
    for lab, om, gam in (("60 meV", 60.0, G_NARROW), ("2p0, 4.2 ueV", W2P0, G_NARROW), ("2p0, 0.1 meV", W2P0, G_BROAD)):
        A = S.A_of_omega(s, om, gam, SIG)[0]
        y1 = S.epsD(A, 1e15) / (3 * S.EPS)
        r = np.array([ratio(s, om, gam, n)[0] for n in nD])
        curves[(key, lab)] = (r, A)
        print(f"[{key}] {lab}: eps^D per 1e15 cm^-3 = {S.epsD(A,1e15):.4g}; y per 1e15 = {y1:.4g}")
        tgt = 1.1 if r[-1] > 1 else 0.9
        n10 = brentq(lambda lx: ratio(s, om, gam, 10**lx)[0] - tgt, 12, np.log10(3e18))
        print(f"     L_full/L_lin = {tgt} at n_D = {10**n10:.3g} cm^-3 (ratio at 3e18: {r[-1]:.3f}); there "
              f"eps^D/eps_host = {ratio(s, om, gam, 10**n10)[1]/S.EPS:.3g}")
        for n in (1e15, 1e16, 1e17, 1e18):
            print(f"     n_D = {n:.0e}: ratio {ratio(s, om, gam, n)[0]:.4f}, eps^D/eps_host = {ratio(s, om, gam, n)[1]/S.EPS:.4g}")

fig, ax = plt.subplots(figsize=(5.2, 3.5))
cols = {"60 meV": "#2a78d6", "2p0, 4.2 ueV": "#d0452b", "2p0, 0.1 meV": "#e6a23c"}
labs = {"60 meV": r"$m_\phi = 60$ meV (continuum)", "2p0, 4.2 ueV": r"2p$_0$ line, width 4.2 $\mu$eV",
        "2p0, 0.1 meV": r"2p$_0$ line, width 0.1 meV"}
for (key, lab), (r, A) in curves.items():
    ax.plot(nD, r, color=cols[lab], ls="-" if key == "CC0.10" else "--", lw=1.4,
            label=labs[lab] if key == "CC0.10" else None)
for lab in ("60 meV", "2p0, 4.2 ueV"):
    r, A = curves[("CC0.10", lab)]
    y = S.epsD(A, nD) / (3 * S.EPS)
    lead = 1 - 4 * y.real + 4 * (3 * y.real**2 - y.imag**2)
    ax.plot(nD, lead, color=cols[lab], ls=":", lw=1.0)
ax.axhline(1, color="k", lw=0.6)
# validity: 60 meV within 10 %
ok = np.minimum.reduce([np.abs(curves[(k, "60 meV")][0] - 1) for k in mods]) * 0 + \
    np.maximum.reduce([np.abs(curves[(k, "60 meV")][0] - 1) for k in mods])
edge = nD[np.argmax(ok > 0.1)] if np.any(ok > 0.1) else nD[-1]
ax.axvspan(nD[0], edge, color="0.88", zorder=0)
ax.axvspan(0.3 * NC, nD[-1], facecolor="none", edgecolor="0.5", hatch="///", lw=0, zorder=0)
ax.text(np.sqrt(0.3 * NC * 3e18), 0.6, "impurity\nband", fontsize=6.5, color="0.3", ha="center", va="center", bbox=dict(fc="white", ec="none", pad=0.5))
print(f"shaded: 60 meV ratio within 10 % below n_D = {edge:.2e} cm^-3")
ax.set_xscale("log")
ax.set_xlim(nD[0], nD[-1])
ax.set_ylim(0, 1.6)
ax.set_xlabel(r"donor density $\mathcal{n}_{\mathrm{D}}$ (cm$^{-3}$)")
ax.set_ylabel(r"$L_{\mathrm{eff}}\,/\,(\varepsilon_2^{\mathrm{D}}/\varepsilon_{\mathrm{host}}^2)$")
ax.legend(fontsize=7, loc="lower left", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_5a.pdf"))
print("wrote limit16_5a.pdf")
