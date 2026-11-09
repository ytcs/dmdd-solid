"""Absorption of bosonic dark matter on the electrons of silicon (Sect. 10.7): Fig. 10.6 and every number of the text and
of Worked example 10.7.  Natural units, Heaviside-Lorentz, e^2 = 4 pi alpha; energies in eV.

Rates per unit target mass (Sect. 8.2, eq:8.2-abs; Sect. 10.7):
  dark photon      R = (rho_chi / (rho_T m)) zeta^2 sigma_1 / |eps|^2 = (rho_chi/(rho_T m)) zeta^2 m L(m)
                   vacuum mixing (no in-medium factor): (rho_chi/(rho_T m)) zeta^2 sigma_1
  ALP, electrons   R = (rho_chi / (rho_T m)) (3 m^2 / (4 m_e^2 e^2)) g_aee^2 sigma_1   (no in-medium factor)
  ALP, photon, B0  R = (rho_chi / (rho_T m)) (g_agg B0)^2 L(m) / m   (cubic crystal; same as the dark photon with
                   zeta = g_agg B0 / m)
  scalar           R = (rho_chi / (rho_T m)) g_phiee^2 S_TT(0, m) / (2 m m_e^2)   (kinetic row, model spectrum of
                   si_scalar10_7.py: empirical pseudopotential, independent particles, pseudo-wavefunctions)
                   density row alone at |p_phi| = v m, v = 1e-3: (rho_chi/(rho_T m)) g^2 (2 p^2/e^2) L / (2 m)
  where sigma_1 = w eps_2, L = eps_2/|eps|^2 at q -> 0 (eps^T = eps, Sect. 4.4).
Dark photon at finite p_phi = v m (Sect. 10.7):  Gamma_T = zeta^2 (m^4 / |w^2 eps - p^2|^2) sigma_1,
  Gamma_L = zeta^2 (m^2/w^2) sigma_1/|eps|^2, w^2 = m^2 + p^2; eps^T(p, w) = eps(0, w) to O((p a)^2) ~ 1e-9.

Inputs and their sources
  Constants, halo density, silicon density, unit conversions: as rate10_2.py (CODATA 2018; rho_chi = 0.3 GeV cm^-3,
     rho_T = 2.33 g cm^-3, Sect. 1.2).  m_Si = 28.0855 u, N_A = 6.02214076e23.
  Optical constants of float-zone silicon at 300 K, 4 meV - 40 eV: Franta et al., Appl. Surf. Sci. 421, 405 (2017),
     refractiveindex.info file Franta-300K.yml (CC0), copy in book/sources/4.4/si_franta_300K.yml, read as fig4_5.py;
     eps = (n + i k)^2.
  Above 40 eV: atomic scattering factors f1, f2 of Henke, Gullikson and Davis, At. Data Nucl. Data Tables 54, 181
     (1993), CXRO file si.nff, copy in book/sources/4.3/si_henke.nff;  
     with n_at the atomic density; written as eps_1 = 1 - C f1/w^2, eps_2 = C f2/w^2,
     C = 4 pi alpha n_at/m_e (dilute-medium form, first order in n_at).  Splice at 40 eV (printed below).
  Low-temperature edge of silicon (Sect. 6.5, Macfarlane et al. 1958): gap 1.17 eV, omega_TA = 18.27 meV, exciton
     binding 14.7 meV; cold optical edge E_g(0) + omega_TA - E_x = 1.1728 eV (excitonic), 1.1875 eV (free pair), with E_g(0) = 1.1692 eV (Sect. 6.3).
  Direct gap E_dir = 3.4 eV (Sect. 3.3).
  Tesla in natural units: 1 T = 195.35 eV^2 (mu_B B = 5.788e-5 eV per tesla, App. A.2).
Modelling choices (named in the caption): splice at 40 eV; 300 K data used untransferred (wrong within tens of meV of
  the edge, Sect. 13.5); EPM scalar spectrum smoothed by a 0.25 eV running mean for the figure.
Output: tex/figures/ch10/fig10_6.pdf
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import rate10_2 as R

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
FIG = os.path.join(BOOK, "tex", "figures", "ch10")
ALPHA, ME, CM = R.ALPHA, R.ME, R.CM
E2 = 4 * np.pi * ALPHA
TESLA = 5.788e-5 * 2 * ME / np.sqrt(E2)          # eV^2 per tesla
N_AT = 2.33 / (28.0855 / 6.02214076e23) / CM**3   # atoms per eV^-3
WSPLICE = 40.0


def franta():
    rows = []
    for line in open(os.path.join(BOOK, "sources", "4.4", "si_franta_300K.yml")):
        p = line.split()
        if len(p) == 3:
            try:
                rows.append([float(x) for x in p])
            except ValueError:
                pass
    lam, n, k = np.array(rows).T
    w = 1.239841984 / lam
    o = np.argsort(w)
    return w[o], ((n + 1j * k) ** 2)[o]


def henke():
    d = np.loadtxt(os.path.join(BOOK, "sources", "4.3", "si_henke.nff"), skiprows=1)
    d = d[d[:, 1] > -9000]
    w, f1, f2 = d.T
    C = E2 * N_AT / ME
    return w, 1 - C * f1 / w**2 + 1j * C * f2 / w**2


def eps_si(w):
    """Complex dielectric function of silicon at q -> 0 on the grid w (eV): Franta below WSPLICE, Henke above."""
    wf, ef = franta()
    wh, eh = henke()
    w = np.asarray(w, float)
    lo = np.interp(w, wf, ef.real) + 1j * np.interp(w, wf, ef.imag)
    hi = np.interp(w, wh, eh.real) + 1j * np.interp(w, wh, eh.imag)
    return np.where(w <= WSPLICE, lo, hi)


def per_kg_yr(x):
    return R.to_per_kg_yr(x)


def rates(m):
    eps = eps_si(m)
    sig1 = m * eps.imag
    L = eps.imag / np.abs(eps)**2
    pre = R.RHO_CHI / (R.RHO_T * m)
    dp = per_kg_yr(pre * sig1 / np.abs(eps)**2)
    dp_vac = per_kg_yr(pre * sig1)
    alp = per_kg_yr(pre * 3 * m**2 / (4 * ME**2 * E2) * sig1)
    return dict(eps=eps, sig1=sig1, L=L, dp=dp, dp_vac=dp_vac, alp=alp)


def main():
    # splice check
    wf, ef = franta()
    wh, eh = henke()
    for w0 in (30.0, 35.0, 40.0):
        a = np.interp(w0, wf, ef.real) + 1j * np.interp(w0, wf, ef.imag)
        b = np.interp(w0, wh, eh.real) + 1j * np.interp(w0, wh, eh.imag)
        print(f"splice check at {w0:.0f} eV: Franta eps = {a.real:.4f} + {a.imag:.4f} i ; Henke eps = {b.real:.4f} + {b.imag:.4f} i;"
              f" L: {a.imag/abs(a)**2:.4f} vs {b.imag/abs(b)**2:.4f}")
    print(f"1 T = {TESLA:.2f} eV^2; n_at = {N_AT:.4e} eV^3 ({N_AT*CM**3:.4e} cm^-3); 4 pi alpha n_at/m_e = {E2*N_AT/ME:.2f} eV^2")

    # Worked example 10.7: m = 10 eV
    m0 = 10.0
    r = rates(np.array([m0]))
    e = r["eps"][0]
    print(f"\nWE 10.7 at m = {m0} eV: eps1 = {e.real:.3f}, eps2 = {e.imag:.3f}, |eps|^2 = {abs(e)**2:.3f}, L = {r['L'][0]:.4f},"
          f" sigma1 = {r['sig1'][0]:.2f} eV")
    print(f"  1/|eps|^2 = {1/abs(e)**2:.4f}; zeta_eff/zeta = {1/abs(e):.4f}; Pi_em = m^2(1 - eps) = {m0**2*(1-e):.2f} eV^2")
    print(f"  1 + 2(1 - eps1) (first order in Pi/m^2) = {1 + 2*(1-e.real):.4f}")
    v = 1e-3
    corr_T = -v**2 + 2 * v**2 * (1 / e).real
    print(f"  finite p = v m, v = {v}: Gamma_T/Gamma_L - 1 = {corr_T:.3e}; Gamma_L / (zeta^2 sigma1/|eps|^2) - 1 = {-v**2:.1e}")
    pre = R.RHO_CHI / (R.RHO_T * m0)
    print(f"  rho_chi/m = {R.RHO_CHI/m0*CM**3:.3e} cm^-3; dark-photon rate R/zeta^2 = {r['dp'][0]:.4e} /kg/yr;"
          f" vacuum-mixing R/zeta^2 = {r['dp_vac'][0]:.4e}")
    z3 = np.sqrt(3 / r["dp"][0])
    print(f"  zeta for 3 events per kg-yr: {z3:.3e} (vacuum mixing would claim {np.sqrt(3/r['dp_vac'][0]):.3e})")
    print(f"  Gamma per particle at zeta = 1e-15: {1e-30*r['sig1'][0]/abs(e)**2:.3e} eV")
    print(f"  ALP electrons: R/g_aee^2 = {r['alp'][0]:.4e} /kg/yr; ratio ALP/(dark photon) at g = zeta: {r['alp'][0]/r['dp'][0]:.3e}")
    print(f"      = (3 m^2/(4 m_e^2 e^2)) |eps|^2 = {3*m0**2/(4*ME**2*E2)*abs(e)**2:.3e}")
    B0 = 10 * TESLA
    g = 1e-10 * 1e-9  # 1e-10 GeV^-1 in eV^-1
    print(f"  ALP photon at B0 = 10 T, g = 1e-10 GeV^-1: zeta-equivalent g B0/m = {g*B0/m0:.3e}; R = {(g*B0/m0)**2*r['dp'][0]:.3e} /kg/yr")

    # numbers for the text at other masses
    for m1 in (3.0, 16.4, 100.0, 1000.0):
        rr = rates(np.array([m1]))
        print(f"m = {m1:7.1f} eV: |eps|^2 = {abs(rr['eps'][0])**2:.4g}, 1/|eps|^2 = {1/abs(rr['eps'][0])**2:.4g}, "
              f"R_dp/zeta^2 = {rr['dp'][0]:.3e}, R_alp/g^2 = {rr['alp'][0]:.3e}")
    # where in-medium is within 10% of vacuum
    mm = np.logspace(0.05, 4.4, 4000)
    rr = rates(mm)
    ratio = rr["dp"] / rr["dp_vac"]
    bad = np.where(np.abs(ratio - 1) > 0.1)[0]
    print(f"in-medium within 10% of vacuum mixing for all m above {mm[bad.max()+1]:.1f} eV")
    sel6 = mm < 63
    k6 = np.argmin(ratio[sel6])
    print(f"in-medium factor below 63 eV: min {ratio[sel6][k6]:.2e} at {mm[sel6][k6]:.2f} eV, max {ratio[sel6].max():.2f}"
          f" at {mm[sel6][np.argmax(ratio[sel6])]:.2f} eV")
    i = np.argmax(rr["dp"] * (mm < 40))
    print(f"dark-photon rate peak below 40 eV at m = {mm[i]:.2f} eV, R/zeta^2 = {rr['dp'][i]:.3e}")
    j = np.argmax(rr["L"] * (mm < 40))
    print(f"loss-function peak at {mm[j]:.2f} eV, L = {rr['L'][j]:.3f}")

    # edge: 300 K data below the cold edge
    for w0 in (1.12, 1.15, 1.17):
        ee = eps_si(np.array([w0]))[0]
        print(f"300 K data at {w0} eV: eps2 = {ee.imag:.3e}, sigma1 = {w0*ee.imag:.3e} eV (cold crystal: zero below 1.1728 eV)")

    # scalar (EPM model)
    d = np.load(os.path.join(HERE, "si_scalar10_7.npz"))
    ws, Stt, eps2m, sig1m = d["omega"], d["S_TT"], d["eps2"], d["sigma1"]
    kern = np.ones(5) / 5
    Sts = np.convolve(Stt, kern, mode="same")
    sig1ms = np.convolve(sig1m, kern, mode="same")
    sel = (ws > 1.0) & (ws < 40.0)
    msc = ws[sel]
    pre_s = R.RHO_CHI / (R.RHO_T * msc)
    scal = per_kg_yr(pre_s * Sts[sel] / (2 * msc * ME**2))
    alp_m = per_kg_yr(pre_s * 3 * msc**2 / (4 * ME**2 * E2) * sig1ms[sel])
    rs = rates(msc)
    dens = per_kg_yr(pre_s * (2 * (1e-3 * msc)**2 / E2) * rs["L"] / (2 * msc))
    for w0 in (4.0, 5.0, 10.0, 14.0, 16.4, 18.0, 20.0, 25.0, 30.0):
        k = np.argmin(abs(msc - w0))
        print(f"scalar model at {w0} eV: R/g^2 = {scal[k]:.3e} /kg/yr; density row alone (v = 1e-3) = {dens[k]:.3e};"
              f" ratio = {dens[k]/scal[k]:.2e}; EPM ALP / data ALP = {alp_m[k]/rs['alp'][k]:.2f}")

    # figure
    fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.5))
    m = np.logspace(np.log10(1.2), 4, 3000)
    rr = rates(m)
    edge = 1.1728
    ax = axs[0]
    ax.loglog(m, rr["dp"], color="C3", lw=1.2, label=r"in medium, $\zeta^2m_\phi L$")
    ax.loglog(m, rr["dp_vac"], color="k", lw=0.9, ls="--", label=r"vacuum mixing, $\zeta^2\sigma_1$")
    ax.set_ylabel(r"$\mathcal{R}/\zeta^2$  [kg$^{-1}$ yr$^{-1}$]")
    ax.set_title(r"(a) dark photon", fontsize=10.5)
    ax.legend(fontsize=10, frameon=False, loc="lower left", bbox_to_anchor=(0.15, 0.0))
    ax = axs[1]
    ax.loglog(m, rr["alp"], color="C0", lw=1.2, label=r"measured $\sigma_1$")
    ax.loglog(msc, alp_m, color="C0", lw=0.8, ls=":", label="model (pseudopotential)")
    ax.set_ylabel(r"$\mathcal{R}/g_{aee}^2$  [kg$^{-1}$ yr$^{-1}$]")
    ax.set_title(r"(b) axion-like particle, electron coupling", fontsize=10.5)
    ax.legend(fontsize=10, frameon=False, loc="lower right")
    ax = axs[2]
    ax.loglog(msc, scal, color="C2", lw=1.2, label="kinetic row $\\mathcal{T}_e$\n(model)")
    ax.loglog(msc, dens, color="C2", lw=0.8, ls="--", label="density row alone,\n$v = 10^{-3}$")
    ax.set_ylabel(r"$\mathcal{R}/g_{\phi ee}^2$  [kg$^{-1}$ yr$^{-1}$]")
    ax.set_title(r"(c) scalar", fontsize=10.5)
    ax.set_xlim(1.0, 40)
    ax.set_ylim(1e24, 1e31)
    ax.legend(fontsize=10, frameon=False, loc="lower right")
    for ax in axs:
        ax.set_xlabel(r"$m_\phi$  [eV]")
        ax.axvline(edge, color="0.5", lw=0.6, ls=":")
        ax.axvline(3.4, color="0.5", lw=0.6, ls="-.")
    axs[0].set_xlim(1.0, 1e4)
    axs[1].set_xlim(1.0, 1e4)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig10_6.pdf"))
    print("wrote fig10_6.pdf")


if __name__ == "__main__":
    main()
