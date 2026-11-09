"""Limit 12.6a (lim:12.6a): Migdal-type absorption of a scalar coupled to nucleon number in silicon.
Natural units, Heaviside-Lorentz, e^2 = 4 pi alpha; energies in eV.

Formulas (Sect. 12.6)
  Crystal (eq:12.6-absrate), coupling proportional to mass, c_kappa = c~ M_kappa, at k = m_phi v -> 0:
      Gamma_abs = c~^2 m_e^2 k^2 L(omega) / (e^2 omega),   L = Im[-1/eps(0, omega)],  omega = m_phi.
  Literature limit (Dzuba, Flambaum and Samsonov, arXiv:2312.10566, Eqs. (14), (17)): per atom
      sigma_phi = g^2 (m_e^2 / m_p^2) (k / omega) sigma_gamma / (4 pi alpha);  Gamma = n_at sigma_phi v.
      Applied to the crystal with the measured photoabsorption (attenuation) n_at sigma_gamma = omega eps_2 / n_r,
      this is the crystal formula with L -> eps_2 / n_r.  (c~ = g/m_p for c_kappa = g A_kappa and M_kappa = A m_p.)
  Ratio crystal / literature = n_r / |eps|^2 = 1 + (3/2) omega_p^2/omega^2 + ... for eps = 1 - omega_p^2/omega^2 + i eps_2,
      omega_p from the electrons bound below omega (Si: 4 valence below the L edge 99.8 eV, +6 (2p) to 150 eV,
      +2 (2s) to the K edge 1839 eV, 14 above); binding energies of the X-Ray Data Booklet (Sect. 10.6 uses them).
  Rate per unit mass: R = rho_chi / (m_phi rho_T) <Gamma_abs>, <k^2> = m_phi^2 <v^2>, <v^2> in the lab frame of the
      truncated standard halo (v0, v_esc, v_E = 238, 544, 250.5 km/s; computed below).  Coupling normalization for the
      plot: g_phipp = g_phinn = g, c_kappa = g A_kappa, c~ = g A_Si / M_Si.
Inputs: Si eps(omega): Franta et al. 2017 (300 K) below 40 eV, Henke et al. 1993 above (../ch10/abs10_7.eps_si, the
  splice of Sect. 10.7).
Output: tex/figures/ch12/limit12_6a.pdf
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

ALPHA, ME, CM = R.ALPHA, R.ME, R.CM
E2 = 4 * np.pi * ALPHA
U = 931.49410e6
M_SI = 28.0855 * U
A_SI = 28.0855
N_AT = ABS.N_AT
FIG = os.path.join(BOOK, "tex", "figures", "ch12")
EDGES = [(0.0, 4), (99.8, 10), (149.7, 12), (1839.0, 14)]   # electrons per atom bound below omega


def v2_lab():
    from scipy.integrate import quad
    v0, ve, vesc = R.V0, R.VE, R.VESC
    num = quad(lambda u: u**4 * np.exp(-u**2 / v0**2), 0, vesc)[0]
    den = quad(lambda u: u**2 * np.exp(-u**2 / v0**2), 0, vesc)[0]
    return (num / den + ve**2) / R.CKM**2


def wp2_bound(w):
    ne = np.zeros_like(w)
    for e, n in EDGES:
        ne = np.where(w >= e, n, ne)
    return E2 * N_AT * ne / ME


def main():
    w = np.geomspace(1.2, 1.0e4, 1500)
    eps = ABS.eps_si(w)
    nr = np.sqrt(eps).real
    L = eps.imag / np.abs(eps)**2
    lit = eps.imag / nr
    ratio = L / lit
    corr = 1 + 1.5 * wp2_bound(w) / w**2
    v2 = v2_lab()
    ctil = A_SI / M_SI                      # per unit g
    pre = R.RHO_CHI / (w * R.RHO_T)
    Rcr = R.to_per_kg_yr(pre * ctil**2 * ME**2 * w**2 * v2 * L / (E2 * w))
    Rlit = R.to_per_kg_yr(pre * ctil**2 * ME**2 * w**2 * v2 * lit / (E2 * w))
    print(f"<v^2>_lab = {v2:.4e} (v_rms = {np.sqrt(v2)*R.CKM:.1f} km/s)")
    print(f"omega_p (4 e/atom) = {np.sqrt(E2*N_AT*4/ME):.2f} eV; (12 e/atom) = {np.sqrt(E2*N_AT*12/ME):.2f} eV")
    for w0 in [3.0, 4.2, 10.0, 16.4, 30.0, 50.0, 100.0, 200.0, 500.0, 1000.0, 3000.0, 1e4]:
        j = np.argmin(abs(w - w0))
        print(f"  m_phi = {w[j]:8.1f} eV: n_r = {nr[j]:.4f}, |eps|^2 = {abs(eps[j])**2:.4f}, ratio n_r/|eps|^2 = {ratio[j]:.5f},"
              f" 1 + 1.5 wp^2/w^2 = {corr[j]:.5f}; R/g^2 = {Rcr[j]:.3e} /kg/yr (literature {Rlit[j]:.3e})")
    ok = np.abs(ratio - 1) <= 0.1
    # lowest omega above which the ratio stays within 10 %
    bad = np.where(~ok)[0]
    w10 = w[bad[-1] + 1] if len(bad) else w[0]
    print(f"literature formula within 10 % for m_phi >= {w10:.1f} eV (last failure at {w[bad[-1]]:.1f} eV)")
    m = w > 200
    print(f"max |ratio - corr| / (ratio - 1) above 200 eV: {np.max(np.abs(ratio[m]-corr[m])/np.abs(ratio[m]-1)):.2f}")
    print(f"min ratio {ratio.min():.3f} at {w[np.argmin(ratio)]:.2f} eV; max ratio {ratio.max():.2f} at {w[np.argmax(ratio)]:.2f} eV")

    plt.rcParams.update({"font.size": 9})
    fig, ax = plt.subplots(2, 1, figsize=(4.6, 4.4), sharex=True, gridspec_kw=dict(height_ratios=[1.3, 1]))
    ax[0].plot(w, Rcr, color="C0", lw=1.4, label="crystal: loss function")
    ax[0].plot(w, Rlit, color="C3", lw=1.0, ls="--", label="atoms: photoabsorption")
    ax[0].set_yscale("log"); ax[0].set_xscale("log")
    ax[0].set_ylabel(r"$\mathcal{R}/g^2$ (kg$^{-1}$ yr$^{-1}$)")
    ax[0].legend(frameon=False, fontsize=7)
    ax[1].plot(w, ratio, color="C0", lw=1.4, label=r"$n_r/|\varepsilon|^2$")
    mm = w >= 30
    ax[1].plot(w[mm], corr[mm], color="k", lw=0.9, ls=":", label=r"$1 + \frac{3}{2}\omega_p^2/\omega^2$")
    ax[1].axhline(1, color="0.5", lw=0.6)
    ax[1].axvspan(w10, w[-1], color="0.85", lw=0)
    ax[1].set_yscale("log")
    ax[1].set_ylim(0.1, 20)
    ax[1].set_xlabel(r"$m_\phi$ (eV)")
    ax[1].set_ylabel("crystal / atoms")
    ax[1].legend(frameon=False, fontsize=7, loc="lower right")
    fig.tight_layout()
    os.makedirs(FIG, exist_ok=True)
    fig.savefig(os.path.join(FIG, "limit12_6a.pdf"))
    print("wrote limit12_6a.pdf")


if __name__ == "__main__":
    main()
