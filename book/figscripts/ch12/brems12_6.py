"""Nuclear-recoil bremsstrahlung in crystals (Sect. 12.6): Fig. 12.5 (fig:12-brems) and every number of the
bremsstrahlung subsections and of Worked example 12.6 (we:12-gaas).  Natural units, Heaviside-Lorentz,
e^2 = 4 pi alpha; energies in eV.

Formulas (Sect. 12.6)
  Photons per kick, nucleus kappa, velocity v_N = q/M_kappa, photon energy w below the gap and above the phonons:
      dN/dw = (2 alpha / 3 pi) n_r(w) |Z*_kappa(w)|^2 v_N^2 / w                              (eq:12.6-dN)
  Translation sum rule at frequency w (eq:12.6-sum):
      sum_kappa Z*_kappa(w) = -(Omega m_e w^2 / e^2) [eps(w) - 1],  eps the electronic (clamped-nuclei) dielectric
      function; -> 0 as w -> 0 (neutrality, eq:5.5-neutral) and -> sum_kappa Z_kappa as w -> infinity.
      Si, Ge (two sites related by inversion): Z*(w) = -(Omega m_e w^2 / 2 e^2) [eps(w) - 1].
      GaAs: Z*_Ga = Z*(0) + Sigma/2 + b, Z*_As = -Z*(0) + Sigma/2 - b with Sigma = the sum above; the model takes
      b = 0 (equal split); the band takes |Z*_kappa(w) - Z*_kappa(0)| <= 0.9 (w/eV)^2 (App. E.17 bound), i.e.
      |b| <= 0.9 w^2 - |Sigma|/2.
  Free atom (dilute limit of the sum rule; Kouvaris-Pradler 1607.01789 Eq. (8), their f(w) = our Z*_atom):
      Z*_atom(w) = -(m_e w^2 / e^2) alpha_pol^HL(w),  alpha_pol^HL = 4 pi a0^3 x (polarizability in atomic units);
      modelling choice: static polarizability (lowest dipole excitations of Si, Ge, Ga, As lie at 3-5 eV, so the
      dynamic correction is (w/w_1)^2, a few percent at 1 eV); vacuum n_r = 1.
  Rate per unit target mass, heavy mediator, F_N = 1, free recoil w_l = q^2/2M (any lattice regime with mean E_R
      gives the same to the precision of the figure; see the text):
      dR/dw = sum_kappa rho_chi/(4 pi^2 m_chi) (pi A_kappa^2 sigma_n / mu_n^2) (2 pi / M_cell)
              int dq q eta(v_min) (2 alpha/3 pi) n_r |Z*_kappa|^2 (q^2/M_kappa^2)/w,
      v_min = (w + q^2/2M_kappa)/q + q/2m_chi  (the prefactor structure of mig12.rate_free).
Inputs and their sources
  Halo, eta(v_min), constants: ../ch10/rate10_2.py (v0, v_esc, v_E = 238, 544, 250.5 km/s; rho_chi = 0.3 GeV cm^-3).
  Silicon eps(w), 300 K: Franta et al. 2017 (book/sources/4.4/si_franta_300K.yml) through ../ch10/abs10_7.eps_si.
      a = 5.431 A (Sect. 3.1).  Transparent range used: 0.1-1.1 eV (indirect gap 1.12 eV at 300 K).
  Germanium n(w), 293 K: H. H. Li, J. Phys. Chem. Ref. Data 9, 561 (1980), refractiveindex.info file Ge/nk/Li-293K.yml
      (CC0), copy in book/sources/12.6/ge_li_293K.yml; 1.9-18 um, i.e. 0.069-0.653 eV; eps = n^2. a = 5.658 A.
  GaAs n(w), 22 C: Skauli et al., J. Appl. Phys. 94, 6447 (2003), refractiveindex.info Ge... file GaAs/nk/Skauli.yml
      (CC0), copy in book/sources/12.6/gaas_skauli.yml; valid 0.97-17 um, i.e. 0.073-1.28 eV; used to 1.27 eV.  The last Sellmeier
      term (pole at 36.9 um, the TO phonon) is the lattice part; it is kept in n_r and removed from the electronic
      eps of the sum rule.  a = 5.638 A, Z*(0) = 2.11 (WE 5.1, from the measured LO-TO splitting), masses 69.723
      and 74.922 u (Sect. 5.5).
  Atomic polarizabilities (a.u.): Si 37.3, Ga 50, Ge 40, As 30, the recommended values of Schwerdtfeger and Nagle,
      Mol. Phys. 117, 1200 (2019), 2023 update (copy of the table in book/sources/12.6/schwerdtfeger2023_table.txt).
  Si Migdal probability at E_R = 100 eV: 6.1e-3 (Sect. 12.3, mig12.py), for comparison only.
Output: tex/figures/ch12/fig12_5.pdf
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
import rate10_2 as R  # noqa: E402
import abs10_7 as ABS  # noqa: E402

ALPHA, ME, HBARC, CM = R.ALPHA, R.ME, R.HBARC, R.CM
E2 = 4 * np.pi * ALPHA
U = 931.49410e6
A0 = 0.529177                  # bohr in A
M_N = 939.0e6                  # nucleon mass in mu_n, as mig12.py
FIG = os.path.join(BOOK, "tex", "figures", "ch12")
SRC = os.path.join(BOOK, "sources", "12.6")
LAM2W = 1.239841984            # eV um


def omega_cell(a):
    return (a / HBARC) ** 3 / 4.0          # eV^-3, fcc primitive cell


def alpha_hl(au):
    return 4 * np.pi * au * (A0 / HBARC) ** 3   # eV^-3


# ---------------------------------------------------------------- optical inputs
def ge_n(w):
    rows = []
    for line in open(os.path.join(SRC, "ge_li_293K.yml")):
        p = line.split()
        if len(p) == 2:
            try:
                rows.append([float(p[0]), float(p[1])])
            except ValueError:
                pass
    lam, n = np.array(rows).T
    ww = LAM2W / lam
    o = np.argsort(ww)
    return np.interp(w, ww[o], n[o], left=np.nan, right=np.nan)


SK = [4.372514, 5.466742, 0.4431307, 0.02429960, 0.8746453, 1.957522, 36.9166]


def gaas_eps(w, electronic=False):
    lam = LAM2W / np.asarray(w, float)
    l2 = lam ** 2
    e = 1 + SK[0] + SK[1] * l2 / (l2 - SK[2] ** 2) + SK[3] * l2 / (l2 - SK[4] ** 2)
    if not electronic:
        e = e + SK[5] * l2 / (l2 - SK[6] ** 2)
    ok = (lam >= 0.97) & (lam <= 17.0)
    return np.where(ok, e, np.nan)


def si_eps(w):
    return ABS.eps_si(w)


MAT = {
    "Si": dict(a=5.431, sites=[("Si", 14, 28.0855, 37.3)], w=(0.1, 1.1)),
    "Ge": dict(a=5.658, sites=[("Ge", 32, 72.63, 40.0)], w=(0.1, 0.65)),
    "GaAs": dict(a=5.638, sites=[("Ga", 31, 69.723, 50.0), ("As", 33, 74.922, 30.0)], w=(0.1, 1.27)),
}
ZSTAR0 = 2.11


def optics(name, w):
    """n_r and electronic eps on w."""
    w = np.asarray(w, float)
    if name == "Si":
        e = si_eps(w)
        return np.sqrt(e).real, e.real
    if name == "Ge":
        n = ge_n(w)
        return n, n ** 2
    e = gaas_eps(w)
    return np.sqrt(e), gaas_eps(w, electronic=True)


def zsum(name, w):
    """sum_kappa Z*_kappa(w) from the translation sum rule (eq:12.6-sum)."""
    _, eel = optics(name, w)
    return -(omega_cell(MAT[name]["a"]) * ME * np.asarray(w) ** 2 / E2) * (eel - 1)


def zstar(name, w, b=0.0):
    """List of Z*_kappa(w) per site; b is the antisymmetric part (GaAs only)."""
    S = zsum(name, w)
    if name in ("Si", "Ge"):
        return [S / 2, S / 2]
    return [ZSTAR0 + S / 2 + b, -ZSTAR0 + S / 2 - b]


def zatom(au, w):
    return -(ME * np.asarray(w) ** 2 / E2) * alpha_hl(au)


def gaas_bmax(w):
    return np.maximum(0.9 * np.asarray(w) ** 2 - np.abs(zsum("GaAs", w)) / 2, 0.0)


# ---------------------------------------------------------------- rates
def mu(a, b):
    return a * b / (a + b)


def spectrum(name, m, w, atom=False, b=0.0, sig_n=1e-38, q_n=3000):
    """dR/dw (events kg^-1 yr^-1 eV^-1) on w."""
    sites = MAT[name]["sites"]
    mcell = sum(s[2] for s in sites) * U
    nr, _ = optics(name, w)
    if atom:
        nr = np.ones_like(nr)
        zs = [zatom(s[3], w) for s in sites]
    else:
        zs = zstar(name, w, b) if name == "GaAs" else zstar(name, w)[:1]
    out = np.zeros_like(np.asarray(w, float))
    for (lab, Z, A, au), zk in zip(sites, zs):
        M = A * U
        muN, mun = mu(m, M), mu(m, M_N)
        D = np.pi * A ** 2 * sig_n * CM ** 2 / mun ** 2
        pref = R.RHO_CHI / (4 * np.pi ** 2 * m) * D * 2 * np.pi / mcell
        qmax = 2 * muN * R.VMAX
        q = np.linspace(1.0, qmax, q_n)
        for i, wi in enumerate(np.atleast_1d(w)):
            vmin = (wi + q ** 2 / (2 * M)) / q + q / (2 * m)
            I = np.trapezoid(q * R.eta(vmin) * q ** 2 / M ** 2, q)
            out[i] += pref * I * (2 * ALPHA / (3 * np.pi)) * nr[i] * np.abs(zk[i]) ** 2 / wi
    return R.to_per_kg_yr(out)


def per_kick(name, ER, w, site=0, b=0.0):
    """Photons per kick of recoil energy ER on site `site`: integrand dN/dw on w."""
    lab, Z, A, au = MAT[name]["sites"][site]
    M = A * U
    nr, _ = optics(name, w)
    zk = zstar(name, w, b)[site]
    return (2 * ALPHA / (3 * np.pi)) * nr * np.abs(zk) ** 2 * (2 * ER / M) / w


def main():
    print("== checks of the translation sum rule")
    for name in MAT:
        Om = omega_cell(MAT[name]["a"])
        print(f"{name}: Omega = {Om*HBARC**3:.2f} A^3 = {Om:.4e} eV^-3; Omega m_e/e^2 = {Om*ME/E2:.4e} eV^-2")
    # high-frequency limit with the free-electron eps of all electrons: sum -> N_e
    Om = omega_cell(5.431)
    for w in [1e3, 1e4]:
        wp2 = E2 * 28 / (Om * ME)
        print(f"  Si, eps = 1 - w_p^2/w^2 (28 e per cell), w = {w:.0f} eV: sum Z* = {-(Om*ME*w**2/E2)*(-wp2/w**2):.3f} (sum Z_kappa = 28)")
    # dilute limit: eps - 1 = n_at alpha -> per-atom alpha
    print("  dilute limit: Omega (eps-1)/2 per atom -> alpha_pol^HL; Z*_atom = -(m_e w^2/e^2) alpha^HL (KP f(w))")
    # Kouvaris-Pradler normalization: alpha_KP(w) = -(alpha/(m_e w^2)) f  in units e^2 = alpha  <=> our form with HL
    print("== Z*(w) values")
    for name in MAT:
        w = np.array([0.1, 0.3, 0.5, 0.65, 1.0, 1.1, 1.27])
        w = w[(w >= MAT[name]["w"][0]) & (w <= MAT[name]["w"][1])]
        nr, eel = optics(name, w)
        S = zsum(name, w)
        for wi, n, e, s in zip(w, nr, eel, S):
            line = f"  {name} w = {wi:4.2f} eV: n_r = {n:.4f}, eps_el = {e:.3f}, sum Z* = {s:+.4f}"
            if name != "GaAs":
                line += f", Z* = {s/2:+.4f}, C = -Z*/w^2 = {-s/2/wi**2:.4f} eV^-2"
            else:
                line += f", Z*_Ga = {ZSTAR0+s/2:+.4f}, Z*_As = {-ZSTAR0+s/2:+.4f}, |b|max = {gaas_bmax(wi):.3f}"
            print(line)
    for name, a in [("Si", 5.431), ("Ge", 5.658)]:
        epsinf = 11.7 if name == "Si" else optics("Ge", np.array([0.1]))[1][0]
        C = omega_cell(a) * ME * (epsinf - 1) / (2 * E2)
        print(f"  {name}: C_kappa = Omega m_e (eps_inf - 1)/2e^2 = {C:.4f} eV^-2 with eps_inf = {epsinf:.2f}")
    # valence plasma form for Si: Z* = -(N_val/2)(eps-1) w^2/w_p,val^2, N_val = 8
    print(f"  Si check: -(8/2)(eps-1)(1/16.6)^2 at 1 eV = {-4*(optics('Si', np.array([1.0]))[1][0]-1)/16.6**2:.4f}")
    print("== crystal against atom, per photon, n_r |Z*|^2 / |f|^2")
    for name in MAT:
        for w in [0.3, 0.5, 1.0]:
            if w > MAT[name]["w"][1]:
                continue
            ww = np.array([w])
            nr, _ = optics(name, ww)
            zc = zstar(name, ww)
            sites = MAT[name]["sites"]
            num = sum(abs(z[0]) ** 2 * (s[2] / s[2]) for z, s in zip(zc, sites)) if name == "GaAs" else abs(zc[0][0]) ** 2
            den = sum(abs(zatom(s[3], ww)[0]) ** 2 for s in sites) if name == "GaAs" else abs(zatom(sites[0][3], ww)[0]) ** 2
            print(f"  {name} w = {w} eV: n_r = {nr[0]:.3f}; crystal sum |Z*|^2 = {num:.4e}; atomic sum |f|^2 = {den:.4e};"
                  f" ratio n_r|Z*|^2/|f|^2 = {nr[0]*num/den:.3g}")
        for (lab, Z, A, au) in MAT[name]["sites"]:
            print(f"    {lab}: alpha^HL = {au*4*np.pi*A0**3:.1f} A^3; f(1 eV) = {zatom(au, np.array([1.0]))[0]:.4f}")
        if name in ("Si", "Ge"):
            ww = np.array([min(1.0, MAT[name]["w"][1])])
            pol = omega_cell(MAT[name]["a"]) * (optics(name, ww)[1][0] - 1) / 2 * HBARC ** 3
            print(f"    crystal polarizability per atom Omega(eps-1)/2 at {ww[0]} eV = {pol:.1f} A^3")

    print("== photons per kick at E_R = 100 eV, integrated over the transparent range")
    for name in MAT:
        lo, hi = MAT[name]["w"]
        w = np.geomspace(lo, hi, 400)
        tot = 0.0
        for k in range(len(MAT[name]["sites"])):
            tot += np.trapezoid(per_kick(name, 100.0, w, site=k), w)
        tot /= len(MAT[name]["sites"])
        print(f"  {name}: {tot:.3e} photons per 100-eV recoil ({lo}-{hi} eV), mean over sites;"
              f" Si Migdal at 100 eV: 6.1e-3 (ratio {tot/6.1e-3:.1e})")

    print("== rates, sigma_n = 1e-38 cm^2, heavy mediator")
    res = {}
    for m in [100e6, 1e9]:
        for name in MAT:
            lo, hi = MAT[name]["w"]
            w = np.geomspace(lo, hi, 120)
            cr = spectrum(name, m, w)
            at = spectrum(name, m, w, atom=True)
            Rc, Ra = np.trapezoid(cr, w), np.trapezoid(at, w)
            line = (f"  m = {m/1e6:6.0f} MeV {name:4s}: crystal {Rc:.3e}, atom {Ra:.3e} /kg/yr in {lo}-{hi} eV;"
                    f" ratio {Rc/Ra:.3g}; at 1 eV: dR/dw crystal/atom = ")
            j = np.argmin(abs(w - min(1.0, hi)))
            line += f"{cr[j]/at[j]:.3g} (w = {w[j]:.2f})"
            if name == "GaAs":
                bm = gaas_bmax(w)
                up = spectrum(name, m, w, b=bm)
                dn = spectrum(name, m, w, b=-bm)
                line += f"; band {np.trapezoid(dn, w):.3e}-{np.trapezoid(up, w):.3e}"
                res[(m, name, "up")], res[(m, name, "dn")] = up, dn
                # fraction of photons above 0.5 eV
                c = np.cumsum(np.r_[0, 0.5 * (cr[1:] + cr[:-1]) * np.diff(w)]) / Rc
                line += f"; median photon {np.interp(0.5, c, w):.3f} eV"
            res[(m, name)] = (w, cr, at)
            print(line)
    # Worked example numbers (GaAs, 1 eV, m = 100 MeV)
    print("== WE 12.6 (GaAs)")
    w1 = np.array([1.0])
    nr, eel = optics("GaAs", w1)
    S = zsum("GaAs", w1)[0]
    print(f"  n_r(1 eV) = {nr[0]:.4f}; eps_el(1 eV) = {eel[0]:.4f}; Omega m_e/e^2 = {omega_cell(5.638)*ME/E2:.4e} eV^-2;"
          f" Sigma(1 eV) = {S:.4f}; Z*_Ga = {ZSTAR0+S/2:.4f}, Z*_As = {-ZSTAR0+S/2:.4f}")
    fG, fA = zatom(50.0, w1)[0], zatom(30.0, w1)[0]
    zg, za = ZSTAR0 + S / 2, -ZSTAR0 + S / 2
    print(f"  f_Ga(1 eV) = {fG:.4f}, f_As(1 eV) = {fA:.4f}; per-photon ratio, mean of sites ="
          f" {nr[0]*(zg**2+za**2)/(fG**2+fA**2):.4g}; Ga alone {nr[0]*zg**2/fG**2:.4g}, As alone {nr[0]*za**2/fA**2:.4g}")
    w = np.geomspace(0.1, 1.27, 400)
    nrw, _ = optics("GaAs", w)
    print(f"  int_{{0.1}}^{{1.27}} n_r dw/w = {np.trapezoid(nrw/w, w):.4f}; ln(12.7) = {np.log(12.7):.4f}")
    zz = zstar("GaAs", w)
    I_cr = np.trapezoid(nrw * (zz[0] ** 2 + zz[1] ** 2) / w, w)
    I_at = np.trapezoid((zatom(50.0, w) ** 2 + zatom(30.0, w) ** 2) / w, w)
    print(f"  int n_r sum|Z*|^2 dw/w = {I_cr:.4f}; atom int sum|f|^2 dw/w = {I_at:.4e}; ratio {I_cr/I_at:.4g}")
    P = (2 * ALPHA / (3 * np.pi)) * (2 * 100.0 / (69.723 * U)) * np.trapezoid(nrw * zz[0] ** 2 / w, w)
    print(f"  Ga at E_R = 100 eV: v_N^2 = {2*100/(69.723*U):.4e}, 2alpha/3pi = {2*ALPHA/(3*np.pi):.4e}, photons = {P:.3e}")

    # ------------------------------------------------------------ figure
    plt.rcParams.update({"font.size": 9})
    fig, ax = plt.subplots(1, 2, figsize=(7.2, 3.0))
    col = {"Si": "C0", "Ge": "C2", "GaAs": "C3"}
    for name in MAT:
        lo, hi = MAT[name]["w"]
        w = np.geomspace(lo, hi, 200)
        if name == "GaAs":
            zz = zstar(name, w)
            ax[0].plot(w, np.abs(zz[0]), color=col[name], lw=1.4, label=r"GaAs: Ga")
            ax[0].plot(w, np.abs(zz[1]), color=col[name], lw=1.4, ls="-.", label=r"GaAs: As")
            bm = gaas_bmax(w)
            ax[0].fill_between(w, np.abs(zz[0]) - bm, np.abs(zz[0]) + bm, color=col[name], alpha=0.15, lw=0)
        else:
            ax[0].plot(w, np.abs(zstar(name, w)[0]), color=col[name], lw=1.4, label=name)
    ax[0].set_xscale("log"); ax[0].set_yscale("log")
    ax[0].set_xlabel(r"photon energy $\omega_\gamma$ (eV)")
    ax[0].set_ylabel(r"$|Z^*_\kappa(\omega_\gamma)|$")
    ax[0].set_ylim(1e-4, 10)
    ax[0].legend(frameon=False, fontsize=7, loc="lower right")
    ax[0].text(0.03, 0.05, "(a)", transform=ax[0].transAxes, va="bottom")
    m = 100e6
    for name in ["Si", "GaAs"]:
        w, cr, at = res[(m, name)]
        ax[1].plot(w, cr, color=col[name], lw=1.4, label=name)
        if name == "GaAs":
            ax[1].fill_between(w, res[(m, name, "dn")], res[(m, name, "up")], color=col[name], alpha=0.15, lw=0)
    ax[1].set_xscale("log"); ax[1].set_yscale("log")
    ax[1].set_xlabel(r"photon energy $\omega_\gamma$ (eV)")
    ax[1].set_ylabel(r"$\mathrm{d}\mathcal{R}/\mathrm{d}\omega_\gamma$ (kg$^{-1}$ yr$^{-1}$ eV$^{-1}$)")
    ax[1].legend(frameon=False, fontsize=7, loc="center left", bbox_to_anchor=(0.0, 0.62))
    ax[1].text(0.97, 0.95, "(b)", transform=ax[1].transAxes, va="top", ha="right")
    fig.tight_layout()
    os.makedirs(FIG, exist_ok=True)
    fig.savefig(os.path.join(FIG, "fig12_5.pdf"))
    print("wrote fig12_5.pdf")


if __name__ == "__main__":
    main()
