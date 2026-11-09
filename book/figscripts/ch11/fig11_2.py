"""Fig. 11.2 (Sect. 11.2): single-phonon rate of a dark photon (total-charge coupling) in GaAs, and the reach of GaAs and LiF.

(a) Rate per kg-year at sigma_e = 1e-40 cm^2 against m_chi, light (F_DM = (alpha m_e/q)^2) and heavy (F_DM = 1) mediator.
    Solid: Born-charge one-phonon formula eq:11.2-SZZ evaluated with the full DFPT phonons of Sect. 5.5 (the three optical
    branches; dotted, the three acoustic branches with the same rigid Born charges, which give them only the internal-strain
    part of their piezoelectric charge, see the text;
    frequencies and eigenvectors at the actual q, site phases exp(i q.tau), Umklapp included by the periodicity of the
    dynamical matrix), averaged over the directions of q (146-point Fibonacci sphere), inserted in eq:A.8-rateiso.
    Dashed: one LO branch at the zone center, eq:11.2-onebranch with eq:11.2-rate (the closed form of Griffin et al. 2018,
    v1 Eq. (24), averaged over the halo).
    Common inputs, so that the ratio isolates dispersion and branch structure: Z* = 2.11 (WE 5.6, from the measured splitting),
    eps_inf = 10.88 (measured), omega_L(Gamma) = 36.34 meV (DFPT; measured 36.35), a = 5.638 A, rho_T = 5.361 g/cm^3.
    Modelling choices: direction-averaged structure factor in the isotropic kernel eq:A.8-eta (daily modulation is Sect. 11.7);
    T = 0; energy threshold 1 meV (removes only acoustic deposits); rigid Born charges at all q (the vertex is not valid at q comparable with 2 pi/a = 2.20 keV: hatched beyond
    2 m_chi v_max = 0.2 x 2 pi/a for the heavy mediator, where the rate is set by the largest momenta).
(b) Reach (3 events, 1 kg-yr, zero background, threshold 1 meV) for the light mediator: GaAs (full and one-branch)
    and LiF (one branch; Griffin et al. 2020 Table I: Zbar* = 1.05, eps_inf = 2.02, omega_O top 77.2 meV, computed values).
Sources: see pol11_2.py and gaas11_2.py. Output: tex/figures/ch11/fig11_2.pdf.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pol11_2 as P
import gaas11_2 as G

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "fig11_2.pdf")

ZS, EPSI = P.GAAS["Zs"], P.GAAS["epsinf"]
A = P.GAAS["a"]
QUNIT = 2 * np.pi / A * P.HBARC                     # eV per (2 pi/a)
MC = (P.M_GA + P.M_AS) * P.U_EV
OMEGA = (A**3 / 4) / P.HBARC**3                     # eV^-3
RHO = MC / OMEGA
OMEGA_TH = 1.0e-3                                   # eV; energy threshold (modelling choice, 1 meV as Griffin et al. 2020)


def fib_sphere(n):
    i = np.arange(n) + 0.5
    th = np.arccos(1 - 2 * i / n)
    ph = np.pi * (1 + 5**0.5) * i
    return np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], 1)


def phonon_table(nq=90, ndir=146):
    qmag = np.geomspace(2.0, 6000.0, nq)            # eV
    dirs = fib_sphere(ndir)
    qs = (qmag[:, None, None] * dirs[None]).reshape(-1, 3) / QUNIT
    w, e = G.run_matdyn(qs, f"fig11_2_n{nq}_d{ndir}")
    B = G.born_weights(qs, w, e)                    # |..|^2/(2 omega), Z* = 1, masses u, omega meV
    return qmag, w.reshape(nq, ndir, 6) * 1e-3, B.reshape(nq, ndir, 6) / (P.U_EV * 1e-3)   # -> eV units


def rate_full(m, qmag, w, B, light=True, branches=(3, 4, 5)):
    """R per unit target mass (natural units) at sigma_e (in prefactor), eq:A.8-rateiso with S_ZZ of eq:11.2-SZZ:
    R = rho_chi sigma Z*^2/(2 m mu^2 eps^2 M_cell) int q^3 dq F^2 < sum_nu B_nu eta(vmin(q, w_nu)) >."""
    mu = m * P.ME / (m + P.ME)
    sigma = 1e-40 / (P.HBARC * 1e-8)**2
    # B and w vary slowly with q and are interpolated in log q onto a fine grid; eta varies sharply and is evaluated there
    qf = np.geomspace(qmag[0], qmag[-1], 6000)
    lq, lqf = np.log(qmag), np.log(qf)
    nd = w.shape[1]
    integ = np.zeros_like(qf)
    for d in range(nd):
        for nu in branches:
            wf = np.interp(lqf, lq, w[:, d, nu])
            Bf = np.interp(lqf, lq, B[:, d, nu])
            integ += Bf * P.eta(qf / (2 * m) + wf / qf) * (wf >= OMEGA_TH)
    integ /= nd
    F2 = (P.Q0 / qf)**4 if light else np.ones_like(qf)
    I = np.trapezoid(qf**3 * F2 * integ, qf)
    return P.RHO_CHI * sigma * ZS**2 / (2 * m * mu**2 * EPSI**2 * MC) * I


def rate_onebranch(m, Zs, epsinf, wL, m1, m2, light=True):
    """One LO branch at the zone center: prefactor x (pi wL/2) w x K, with (pi wL/2) w/rho_T = I_pol/rho_T (Omega-free)."""
    Ipol_rho = (np.pi / 2) * P.E2 * Zs**2 / ((m1 + m2) * P.U_EV * P.mu_red(m1, m2) * P.U_EV * epsinf**2 * wL)   # eV^-3
    mu = m * P.ME / (m + P.ME)
    sigma = 1e-40 / (P.HBARC * 1e-8)**2
    K = P.K_light(wL, m) if light else P.K_heavy(wL, m)
    return P.RHO_CHI * sigma * P.Q0**4 / (2 * np.pi * m * mu**2 * P.E2) * Ipol_rho * K


def main():
    qmag, w, B = phonon_table()
    wL0 = 36.342e-3
    ms = np.geomspace(10.6e3, 1.0e6, 60)
    out = {}
    for light in (True, False):
        full = np.array([rate_full(m, qmag, w, B, light) for m in ms])
        one = np.array([rate_onebranch(m, ZS, EPSI, wL0, P.M_GA, P.M_AS, light) for m in ms])
        out[light] = (P.per_kg_yr(full), P.per_kg_yr(one))
    acou = P.per_kg_yr(np.array([rate_full(m, qmag, w, B, True, branches=(0, 1, 2)) for m in ms]))
    for mm in (11e3, 15e3, 20e3, 100e3, 1e6):
        i = np.argmin(abs(ms - mm))
        print(f"m = {ms[i]/1e3:7.1f} keV  acoustic (rigid Born charges, light) / optical = {acou[i]/out[True][0][i]:.4f}")
    lif = np.array([rate_onebranch(m, 1.05, 2.02, 77.2e-3, P.M_LI, P.M_F, True) for m in ms])
    lif = P.per_kg_yr(lif)
    mmin_gaas = 2 * wL0 / P.VMAX**2
    mmin_lif = 2 * 77.2e-3 / P.VMAX**2
    # printed numbers for the text
    for mm in (20e3, 30e3, 100e3, 1e6):
        i = np.argmin(abs(ms - mm))
        print(f"m = {ms[i]/1e3:7.1f} keV  light full {out[True][0][i]:.3e} one {out[True][1][i]:.3e} ratio {out[True][0][i]/out[True][1][i]:.4f}"
              f" | heavy full {out[False][0][i]:.3e} one {out[False][1][i]:.3e} ratio {out[False][0][i]/out[False][1][i]:.4f} | LiF/GaAs(one) {lif[i]/out[True][1][i]:.2f}")
    print("edges (keV): GaAs", mmin_gaas / 1e3, " LiF", mmin_lif / 1e3)
    reach_g = 3 * 1e-40 / out[True][0]
    reach_l = 3 * 1e-40 / np.where(lif > 0, lif, np.nan)
    cross = ms[np.nanargmin(np.abs(np.log(reach_g / reach_l)))]
    print("light-mediator reach crossing GaAs = LiF at m =", cross / 1e3, "keV")
    mheavy_valid = 0.2 * QUNIT / (2 * P.VMAX)
    print("heavy mediator: 2 m v_max = 0.2 x 2pi/a at m =", mheavy_valid / 1e3, "keV")
    np.savez(os.path.join(HERE, "fig11_2_rates.npz"), ms=ms, light_full=out[True][0], light_one=out[True][1],
             heavy_full=out[False][0], heavy_one=out[False][1], lif=lif)

    fig, ax = plt.subplots(1, 2, figsize=(7.4, 3.3))
    a = ax[0]
    a.loglog(ms / 1e3, out[True][0], color="k", lw=1.4, label="light, full phonons")
    a.loglog(ms / 1e3, out[True][1], color="k", lw=1.0, ls="--", label="light, one LO branch")
    a.loglog(ms / 1e3, out[False][0], color="C3", lw=1.4, label="heavy, full phonons")
    a.loglog(ms / 1e3, out[False][1], color="C3", lw=1.0, ls="--", label="heavy, one LO branch")
    a.loglog(ms / 1e3, acou, color="0.45", lw=1.0, ls=":", label="light, acoustic (rigid $Z^*$)")
    a.axvspan(mheavy_valid / 1e3, 1e3, color="0.9", zorder=0)
    a.axvline(mmin_gaas / 1e3, color="0.5", lw=0.6, ls=":")
    a.set_xlim(10, 1000)
    a.set_ylim(1e-6, 1e6)
    a.set_xlabel(r"$m_\chi$ [keV]")
    a.set_ylabel(r"events / (kg yr) at $\bar\sigma_e = 10^{-40}$ cm$^2$")
    a.set_title("(a) GaAs, dark-photon mediator", fontsize=9)
    a.legend(fontsize=6.5, frameon=False, loc="upper right", ncol=1)
    b = ax[1]
    b.loglog(ms / 1e3, reach_g, color="k", lw=1.4, label="GaAs, full phonons")
    b.loglog(ms / 1e3, 3 * 1e-40 / out[True][1], color="k", lw=1.0, ls="--", label="GaAs, one LO branch")
    b.loglog(ms / 1e3, reach_l, color="C0", lw=1.4, label="LiF, one LO branch")
    b.axvline(mmin_gaas / 1e3, color="0.5", lw=0.6, ls=":")
    b.axvline(mmin_lif / 1e3, color="C0", lw=0.6, ls=":")
    b.set_xlim(10, 1000)
    b.set_ylim(1e-45, 1e-36)
    b.set_xlabel(r"$m_\chi$ [keV]")
    b.set_ylabel(r"reach $\bar\sigma_e$ [cm$^2$], 1 kg yr")
    b.set_title("(b) light mediator", fontsize=9)
    b.legend(fontsize=7, frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
