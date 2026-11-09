"""Limit 11.2b (Sect. 11.2): the polar matrix element and band integral, tested on the ordinary axis of sapphire.

Literature formula: one polar branch, |M|^2 = e'^2 (omega_L/2)(1/eps_inf - 1/eps_0)/q^2 (Griffin et al. 2018, v1 Eqs. (21)-(22)),
whose light-mediator rate is proportional to omega_L (1/eps_inf - 1/eps_0) K(omega_L, m_chi) (eq:11.2-rate).
Band-integral reading: R proportional to I_pol K(omega_bar), I_pol = (pi/2) sum_nu omega_L nu w_nu, omega_bar the w-weighted mean
LO frequency (eq:11.2-Ipol).
Fuller result: the exact per-branch sum (pi/2) sum_nu omega_L nu w_nu K(omega_L nu, m_chi) for the lossless factorized
eps_perp(omega) built from the four ordinary-ray LO/TO pairs of Griffin et al. 2018 v1 Table II and eps_inf = 3.2 (their
Table I); w_nu are the residues of -1/eps at the LO zeros (pol11_2.factorized_weights), eps_0 = eps_inf prod (wL/wT)^2 = 9.78.
Plotted against m_chi: fuller / band-integral reading (solid) and fuller / one-branch formula with the top LO frequency and the
same (1/eps_inf - 1/eps_0) (dashed). Light mediator, halo of App. A.8, threshold below every LO energy.
Shaded: m_chi > 2 x 2 omega_L,max/v_max^2 = 64 keV, where the band-integral reading is within 7 % (10 % above 61 keV).
Output: tex/figures/ch11/limit11_2b.pdf.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pol11_2 as P

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_2b.pdf")


def main():
    d = P.SAPH_O
    wp, eps0, S = P.factorized_weights(d["wL"], d["wT"], d["epsinf"])
    D = 1 / d["epsinf"] - 1 / eps0
    Ipol = (np.pi / 2) * np.sum(d["wL"] * wp)
    wbar = np.sum(d["wL"] * wp) / np.sum(wp)
    wmax = d["wL"].max()
    print("o-ray LO (meV):", (d["wL"] * 1e3).round(2), " weights w_nu:", wp.round(5), " shares:", (wp / wp.sum()).round(4))
    print(f"sum w = {wp.sum():.5f} = 1/eps_inf - 1/eps_0 = {D:.5f}; eps_0(LST) = {eps0:.3f} (Table I: 9.3)")
    print(f"I_pol = {Ipol*1e3:.3f} meV; omega_bar = {wbar*1e3:.2f} meV; bracket (pi/2) D x [wL_min, wL_max] = "
          f"[{np.pi/2*D*d['wL'].min()*1e3:.3f}, {np.pi/2*D*wmax*1e3:.3f}] meV; upper (pi/2) D wT_max sqrt(eps0/einf) = "
          f"{np.pi/2*D*d['wT'].max()*np.sqrt(eps0/d['epsinf'])*1e3:.3f}")
    print(f"I_pol/rho_T = {Ipol*1e3/P.RHO_SAPH:.3f} meV cm^3/g (rho_T = {P.RHO_SAPH})")
    ms = np.geomspace(12e3, 1e7, 220)
    exact = np.array([(np.pi / 2) * np.sum([wl * w_ * P.K_light(wl, m) for wl, w_ in zip(d["wL"], wp)]) for m in ms])
    band = np.array([Ipol * P.K_light(wbar, m) for m in ms])
    top = np.array([(np.pi / 2) * wmax * D * P.K_light(wmax, m) for m in ms])
    r_band = np.where(band > 0, exact / np.where(band > 0, band, 1), np.nan)
    r_top = np.where(top > 0, exact / np.where(top > 0, top, 1), np.nan)
    mmin = 2 * d["wL"] / P.VMAX**2
    print("edges (keV):", (mmin / 1e3).round(2))
    for mm in (40e3, 64e3, 96e3, 1e6, 1e7):
        i = np.argmin(abs(ms - mm))
        print(f"m = {ms[i]/1e3:8.1f} keV: exact/band {r_band[i]:.3f}, exact/one-branch(top) {r_top[i]:.3f}")
    ok = ms[(np.abs(r_band - 1) < 0.1)]
    print("band reading within 10 % for m >", ok.min() / 1e3 if len(ok) else None, "keV")
    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    ax.semilogx(ms / 1e3, r_band, color="k", lw=1.4, label=r"exact / $\mathcal{I}_{\mathrm{pol}}K(\bar\omega)$")
    ax.semilogx(ms / 1e3, r_top, color="C3", lw=1.0, ls="--", label=r"exact / one branch at $\omega_{\mathrm{L,max}}$")
    ax.axhline(1, color="0.5", lw=0.5)
    ax.axvspan(2 * mmin.max() / 1e3, 1e4, color="0.9", zorder=0)
    for mm in mmin:
        ax.axvline(mm / 1e3, color="0.6", lw=0.5, ls=":")
    ax.set_xlim(12, 1e4)
    ax.set_ylim(0.5, 3.0)
    ax.set_xlabel(r"$m_\chi$ [keV]")
    ax.set_ylabel("ratio of light-mediator rates")
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
