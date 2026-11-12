"""Two-insertion processes in silicon (Sect. 10.8): pair absorption and dark Compton scattering; Fig. 10.7 and the
numbers of the text.  Natural units, Heaviside-Lorentz, e^2 = 4 pi alpha; energies in eV.

Pair absorption of a complex scalar phi (mass m) with the contact couplings of arXiv:2507.14287 Eq. (3)
  H = m_e phi^dag phi psibar (G_S + i G_P gamma^5) psi + i (phi^dag d<->_mu phi) psibar gamma^mu (G_V + G_A gamma^5) psi
Rate per unit volume (Sect. 10.8, eq:10.8-pair), with n = n_bar = rho_chi/(2m) per species:
  Gamma/V = n n_bar < sum_ab Gcal_a* Gcal_b S_ab(p + pbar, E + Ebar) > / (4 m^2)
  S: kinetic row, Gcal = G_S:     Gamma/V = n nbar G_S^2 S_TT(0, 2m) / (4 m^2)
     density row, Gcal = m_e G_S: Gamma/V = n nbar m_e^2 G_S^2 (2 q^2/e^2) L(2m) / (4 m^2), <q^2> = m^2 <|v + vbar|^2>
  P: axioelectric row at 2m:      Gamma/V = n nbar G_P^2 S_JJ(0, 2m),  S_JJ(0, w) = (3/4)(2 w sigma_1/e^2)  (Sect. 10.7)
  V: dark-photon row at 2m:       Gamma/V = n nbar (2 G_V^2/e^2) m^2 <|v - vbar|^2> L(2m)
  A: order v^4 without spin-orbit coupling or magnetic order; not plotted.
Event rate per unit target mass: (Gamma/V)/rho_T.
Inputs
  Constants, halo (v0 = 238, v_esc = 544, v_E = 250.5 km/s), rho_chi = 0.3 GeV cm^-3, rho_T = 2.33 g cm^-3: rate10_2.py.
  Measured eps of silicon (Franta 300 K below 40 eV, Henke above): abs10_7.eps_si (same splice as Fig. 10.6).
  Kinetic-row spectrum S_TT(0, w): si_scalar10_7.npz (empirical pseudopotential model of Sect. 4.6, 16^3 k points,
     0.05 eV bins; smoothed by the same 5-bin running mean as Fig. 10.6).  A model, not a prediction for silicon.
  G_F = 1.1663788e-5 GeV^-2 (CODATA 2018) as the reference coupling.
  Photon cross sections above 30 keV: NIST XCOM (file xcom_si.txt); dark-photon absorption there
     R = (rho_chi/m) zeta^2 (mu_PE/rho) (eps -> 1; within 1e-4 of 1 above 1 keV); below 30 keV abs10_7 (Henke).
  Dark Compton: arXiv:2109.08168 Eq. (2) (exact tree level, compton10_8.py), all 14 electrons (n_e/rho_T = Z/(A u)),
     Si A = 28.0855; K edge 1.839 keV (XCOM).  ALP: corrected tree-level form (compton10_8.py) and Eq. (3).
Normalization of arXiv:2507.14287 Eq. (8): xi = 44.8 with an escape cut at 2.5 beta_c gives each species rho/(2m)
  (checked below).
Output: tex/figures/ch10/fig10_7.pdf; printed numbers (pair10_8.log).
"""
import os
import numpy as np
from scipy.special import erf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import rate10_2 as R
import abs10_7 as A
import compton10_8 as C

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
FIG = os.path.join(BOOK, "tex", "figures", "ch10")
ME, E2 = R.ME, 4 * np.pi * R.ALPHA
CKM = R.CKM
GF = 1.1663788e-5 * 1e-18     # eV^-2
EK_SI = 1839.0                # eV, K edge (XCOM)


def halo_samples(n=2_000_000, seed=1):
    """Laboratory-frame velocities (units of c) of the standard halo of Sect. 1.2, truncated at v_esc."""
    rng = np.random.default_rng(seed)
    out = []
    while sum(len(o) for o in out) < n:
        u = rng.normal(0, R.V0 / np.sqrt(2), size=(n, 3))
        u = u[np.linalg.norm(u, axis=1) < R.VESC]
        out.append(u)
    u = np.concatenate(out)[:n]
    v = u - np.array([0, 0, R.VE])
    return v / CKM


def moments():
    v = halo_samples()
    vb = np.roll(v, 1, axis=0)
    m = dict(v2=np.mean(np.sum(v**2, 1)), dif2=np.mean(np.sum((v - vb)**2, 1)), sum2=np.mean(np.sum((v + vb)**2, 1)),
             s=0.5 * (np.sum(v**2, 1) + np.sum(vb**2, 1)))
    return m


def bauer_xi():
    # n per species = xi rho/(2 g m^4 bc^3) g int d^3p/(2pi)^3 exp(-p^2/(m bc)^2) Theta(2.5 bc m - p)
    z = 2.5
    trunc = erf(z) - 2 * z / np.sqrt(np.pi) * np.exp(-z**2)
    xi = 8 * np.pi**1.5 / trunc
    return xi, trunc


def xcom(path="xcom_si.txt"):
    d = np.loadtxt(os.path.join(BOOK, "figscripts", "data", "10.8", path), comments="#")
    return d[:, 0] * 1e6, d[:, 2], d[:, 3]          # eV, incoherent, photoelectric (cm^2/g)


def mu_pe(m):
    Ee, inc, pe = xcom()
    return np.exp(np.interp(np.log(m), np.log(Ee), np.log(pe)))


def pair_rates(m, mo):
    """Pair-absorption rates per kg-year at G = G_F, against the mass m of one particle."""
    n = R.RHO_CHI / (2 * m)
    w = 2 * m
    eps = A.eps_si(w)
    L = eps.imag / np.abs(eps)**2
    sig1 = w * eps.imag
    d = np.load(os.path.join(HERE, "si_scalar10_7.npz"))
    Stt = np.convolve(d["S_TT"], np.ones(5) / 5, mode="same")
    S_TT = np.interp(w, d["omega"], Stt)
    gS = n * n * GF**2 * S_TT / (4 * m**2)
    gS_dens = n * n * ME**2 * GF**2 * (2 * m**2 * mo["sum2"] / E2) * L / (4 * m**2)
    gP = n * n * GF**2 * 0.75 * (2 * w * sig1 / E2)
    gV = n * n * (2 * GF**2 / E2) * m**2 * mo["dif2"] * L
    f = lambda x: R.to_per_kg_yr(x / R.RHO_T)
    return dict(S=f(gS), Sd=f(gS_dens), P=f(gP), V=f(gV), S_TT=S_TT, sig1=sig1, L=L)


def single_rates_equiv(m, mo):
    """Check: pair rate = single-absorption rate at 2m with g_eff^2 = n_bar m_e^2 G^2 / m (per particle phi)."""
    n = R.RHO_CHI / (2 * m)
    geff2 = n * ME**2 * GF**2 / m
    w = 2 * m
    d = np.load(os.path.join(HERE, "si_scalar10_7.npz"))
    Stt = np.convolve(d["S_TT"], np.ones(5) / 5, mode="same")
    S_TT = np.interp(w, d["omega"], Stt)
    gam1 = geff2 * S_TT / (2 * w * ME**2)          # single scalar absorption per particle, Sect. 10.7
    return R.to_per_kg_yr(n * gam1 / R.RHO_T)


def main():
    xi, tr = bauer_xi()
    print(f"2507.14287 Eq. (8): truncation factor erf(2.5) - ... = {tr:.5f}; xi giving rho/(2m) per species = {xi:.2f} (source: 44.8)")
    print(f"density rescaling (0.3/0.39)^2 = {(0.3/0.39)**2:.3f}")
    mo = moments()
    v2 = mo["v2"] * CKM**2
    print(f"halo (lab frame): <v^2>^1/2 = {np.sqrt(v2):.1f} km/s; <|v - vbar|^2>^1/2 = {np.sqrt(mo['dif2'])*CKM:.1f} km/s"
          f" (untruncated 3 v0^2 -> {np.sqrt(3)*R.V0:.1f}); <|v + vbar|^2>^1/2 = {np.sqrt(mo['sum2'])*CKM:.1f} km/s")
    s = mo["s"]
    print(f"pair kinetic energy K = m s: <s> = {s.mean():.4e}, std {s.std():.4e}, max {s.max():.4e}; <s>/v2 = {s.mean()/mo['v2']:.3f}")
    print(f"total momentum q = |p + pbar| <= 2 m v_max = {2*R.VMAX:.2e} m; at 2m = 10 eV, q a = {2*5*R.VMAX*R.A_SI/R.HBARC:.2e}")

    for m0 in (0.6, 1.0, 2.0, 5.0, 8.2, 10.0):
        r = pair_rates(np.array([m0]), mo)
        chk = single_rates_equiv(np.array([m0]), mo)
        print(f"m = {m0:5.2f} eV (2m = {2*m0:5.2f}): per kg-yr at G = G_F: S {r['S'][0]:.3e} (density row {r['Sd'][0]:.2e}, "
              f"ratio {r['Sd'][0]/max(r['S'][0],1e-300):.1e}), P {r['P'][0]:.3e}, V {r['V'][0]:.3e}; S via single-absorption map {chk[0]:.3e}")
    # couplings for 3 events/kg-yr
    for m0 in (1.0, 5.0):
        r = pair_rates(np.array([m0]), mo)
        for k in ("S", "P", "V"):
            print(f"   m = {m0} eV, {k}: G for 3 events per kg-yr = {np.sqrt(3/r[k][0]):.2e} G_F")
    # effective coupling of the pair partner
    for m0 in (1.0, 5.0):
        geff = np.sqrt(R.RHO_CHI / (2 * m0) * ME**2 * GF**2 / m0)
        print(f"   g_eff = m_e G_F sqrt(rho/(2 m^2)) at m = {m0} eV: {geff:.2e}")

    # dark Compton vs absorption, silicon
    for m0 in (1e3, 1e4, 4.3e4, 5e4, 1e5, 3e5, 1e6):
        x = m0 / ME
        wC = m0**2 / (2 * (m0 + ME))
        print(f"m = {m0/1e3:7.1f} keV: omega_C = {wC:.1f} eV (K edge 1839 eV), omega' = {m0 - wC:.1f} eV")
    # m where omega_C = E_K
    mK = EK_SI + np.sqrt(EK_SI**2 + 2 * EK_SI * ME)
    mL = 100 + np.sqrt(100**2 + 2 * 100 * ME)
    print(f"omega_C = E_K at m = {mK/1e3:.1f} keV; omega_C = 100 eV at m = {mL/1e3:.1f} keV")
    # splice Henke/XCOM at 30 keV
    m30 = np.array([2.9e4])
    eps = A.eps_si(m30)
    henke_rate = R.to_per_kg_yr(R.RHO_CHI / (R.RHO_T * m30) * m30 * eps.imag)   # vacuum mixing sigma1, eps ~ 1
    xcom_rate = R.RHO_CHI / m30 * mu_pe(m30) * (1 / R.CM**2) * (R.KG_EV * 1e-3)  # (eV^3)(cm^2/g) -> per eV per g...
    # convert carefully: R [1/(g s)] = (rho/m)[cm^-3] * mu[cm^2/g] * c[cm/s]
    rho_cm3 = 0.3e9 / m30           # particles per cm^3
    xr = rho_cm3 * mu_pe(m30) * 2.99792458e10 * 1e3 * R.YR_S
    print(f"splice at 29 keV: Henke-based dark-photon rate {henke_rate[0]:.4e}, XCOM-based {xr[0]:.4e} per kg-yr per zeta^2"
          f" (ratio {henke_rate[0]/xr[0]:.3f}); eps at 29 keV = {eps[0]:.6f}")

    # ---------------- figure ----------------
    fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.5))
    ax = axs[0]
    mm = np.logspace(np.log10(0.59), np.log10(20), 600)
    r = pair_rates(mm, mo)
    Sm = np.where(r["S"] > 1e-16, r["S"], np.nan)          # the model has no kinetic-row strength below its 3.12 eV vertical gap
    ax.loglog(mm, Sm, color="C2", lw=1.2, label=r"$G_{\mathrm{S}}$: kinetic row (model)")
    ax.loglog(mm, r["Sd"], color="C2", lw=0.8, ls="--", label=r"$G_{\mathrm{S}}$: density row alone")
    ax.loglog(mm, r["P"], color="C0", lw=1.2, label=r"$G_{\mathrm{P}}$: axioelectric row")
    ax.loglog(mm, r["V"], color="C3", lw=1.2, label=r"$G_{\mathrm{V}}$: current row, $L(2m_\phi)$")
    ax.axvline(1.1728 / 2, color="0.5", lw=0.6, ls=":")   # cold excitonic edge, E_g(0) = 1.1692 eV
    ax.set_xlabel(r"$m_\phi$  [eV]")
    ax.set_ylabel(r"$\mathcal{R}$ at $G = G_{\mathrm{F}}$  [kg$^{-1}$ yr$^{-1}$]")
    ax.set_title("(a) pair absorption", fontsize=10.5)
    ax.set_xlim(0.55, 20)
    ax.set_ylim(1e-38, 1e-9)
    ax.legend(fontsize=10, frameon=False, loc="lower right")

    Ee, inc, pe = xcom()
    mk = np.logspace(3, 6, 800)
    # absorption: Henke-based below 29 keV, XCOM above
    lo = mk < 2.9e4
    epsk = A.eps_si(mk[lo])
    absv = np.empty_like(mk)
    absv[lo] = R.to_per_kg_yr(R.RHO_CHI / (R.RHO_T * mk[lo]) * mk[lo] * epsk.imag / np.abs(epsk)**2)
    absv[~lo] = 0.3e9 / mk[~lo] * mu_pe(mk[~lo]) * 2.99792458e10 * 1e3 * R.YR_S
    ne_g = 14 / (28.0855 * 1.66053907e-24)
    per = 0.3e9 / mk * ne_g * 2.99792458e10 * 1e3 * R.YR_S / R.CM**2
    compv = per * C.sv_eq2(mk)
    absa = absv * 3 * mk**2 / (4 * ME**2 * E2)      # same sigma_1 (eps -> 1 above 63 eV), Eq. (10.7-alp)
    absa[lo] = R.to_per_kg_yr(R.RHO_CHI / (R.RHO_T * mk[lo]) * 3 * mk[lo]**2 / (4 * ME**2 * E2) * mk[lo] * epsk.imag)
    compa = per * C.sv_alp_corr(mk)
    compa3 = per * C.sv_eq3(mk)
    ax = axs[1]
    ax.loglog(mk / 1e3, absv, color="k", lw=1.0, label="absorption")
    ax.loglog(mk / 1e3, compv, color="C3", lw=1.2, label="dark Compton")
    ax.loglog(mk / 1e3, absv + compv, color="C3", lw=0.7, ls=":", label="sum")
    ax.set_ylabel(r"$\mathcal{R}/\zeta^2$  [kg$^{-1}$ yr$^{-1}$]")
    ax.set_title("(b) dark photon", fontsize=10.5)
    ax.legend(fontsize=10, frameon=False, loc="upper right")
    ax = axs[2]
    ax.loglog(mk / 1e3, absa, color="k", lw=1.0, label="absorption")
    ax.loglog(mk / 1e3, compa, color="C0", lw=1.2, label="dark Compton")
    ax.set_ylabel(r"$\mathcal{R}/g_{aee}^2$  [kg$^{-1}$ yr$^{-1}$]")
    ax.set_title("(c) axion-like particle", fontsize=10.5)
    ax.legend(fontsize=10, frameon=False, loc="upper right")
    for ax in axs[1:]:
        ax.set_xlabel(r"$m_\phi$  [keV]")
        ax.axvspan(1, mK / 1e3, color="0.88", lw=0)
        ax.axvline(29, color="0.5", lw=0.6, ls=":")
        ax.set_xlim(1, 1e3)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig10_7.pdf"))
    k100 = np.argmin(abs(mk - 1e5))
    print(f"at 100 keV: dark photon absorption {absv[k100]:.3e}, Compton {compv[k100]:.3e}; ALP absorption {absa[k100]:.3e},"
          f" Compton {compa[k100]:.3e}, with Eq. (3) {compa3[k100]:.3e} per kg-yr per coupling^2")
    print("wrote fig10_7.pdf")


if __name__ == "__main__":
    main()
