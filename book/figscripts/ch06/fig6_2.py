"""Fig. 6.2 (fig:6-gQ) and the numbers of Sect. 6.2 and Worked example 6.2 (we:6-frohlich).

|g| against |Q| for three long-wavelength forms of the electron-phonon vertex, in the normalization of App. A.6
(H_ep = N^{-1/2} sum g c^dag c B, g in eV):
  (1) acoustic deformation potential, Si conduction electron, LA phonon:   |g| = Xi(theta) Q l_Q,
      l_Q = (2 M_cell omega_Q)^{-1/2} (eq:A.6-ell), Xi(theta) = Xi_d + Xi_u cos^2 theta (Herring-Vogt form,
      Li, Graziosi, Neophytou, PRB 104, 195201 (2021), arXiv:2104.08998, Eq. (13)).
      Xi_d = 1.01 eV, Xi_u = 8.84 eV: DFPT values of the same paper (text after Eq. (14)).
      theta = 0 (Q along the valley axis [001]): Xi = 9.85 eV;  theta = pi/2 (Q along [100]): Xi = 1.01 eV.
      Both directions are Gamma-X lines, so the LA dispersion of both is the DFPT LA branch along Gamma-X of Fig. 5.2
      (figscripts/ch05/fig5_2_data.npz: indices 0..60 = (0,0,z), z = 0..1 in units of 2pi/a; column 2 = LA, in cm^-1;
      small-Q points, indices 183..188, give c_LA = 8.34 km/s; a = 5.431 A, as in fig5_2_qe.sh).
  (2) optical deformation potential, Si holes at the valence maximum, zone-center optical phonon:
      |g| = l_0 D_ODP, with D_ODP = 10.45 eV/A, the DFPT value of Li et al. combined in quadrature over the degenerate
      valence bands (their Eq. (12) and the text below it). omega_O = 64.1 meV (measured, as in fig6_1.py / Sect. 5.1).
      Li et al. Eq. (2): g = sqrt(hbar / 2 m0 omega) M with m0 the total cell mass, which is l_Q M in our normalization,
      so their M (eV/A) and their slopes D_ADP = M/|q| transfer without conversion.
  (3) Froehlich vertex, GaAs conduction electron, LO phonon, intraband with rho = 1:  |g| = C_F / Q,
      C_F^2 = (e^2 omega_L / 2 Omega)(1/eps_inf - 1/eps_0)   (eq:D.14-frohlich, Heaviside-Lorentz, e^2 = 4 pi alpha).
      omega_L = 8.79 THz = 36.35 meV (Strauch and Dorner 1990, as tabulated by Dehghani et al. 2025, Table I; Sect. 5.5),
      eps_inf = 10.88 (Lockwood et al. 2005), eps_0 = 12.9 (same; Sect. 5.5), a = 5.638 A, Omega = a^3/4 = 44.80 A^3 (Sect. 5.5).
      m* = 0.067 m_e (Vurgaftman et al. 2001; Sect. 3.3) for the Froehlich constant
      alpha_F = alpha (1/eps_inf - 1/eps_0) sqrt(m*/(2 omega_L)).
Modelling choice: these are the long-wavelength forms, not directly computed vertices. They are drawn solid for
Q <= 0.1 A^-1 (the range over which Li et al., Fig. 5, find the Si acoustic matrix elements linear in q) and dotted beyond,
up to the X point of Si, 2 pi/a = 1.157 A^-1.
Run: python fig6_2.py   (numpy, scipy, matplotlib; a few seconds)
"""
import os
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch06", "fig6_2.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

ALPHA = 1 / 137.035999                # CODATA (App. A.2)
E2 = 4 * np.pi * ALPHA                # e^2, Heaviside-Lorentz
ME = 0.51099895e6                     # eV
U = 931.49410242e6                    # eV per atomic mass unit
HBARC = 1973.269804                   # eV A
CM = 1.23984198e-4                    # eV per cm^-1
THZ = 4.135667696e-3                  # eV per THz
C_KMS = 299792.458

# ---------------- silicon ----------------
A_SI = 5.431                          # A
M_CELL_SI = 2 * 28.0855 * U           # eV
XI_D, XI_U = 1.01, 8.84               # eV, Li et al. (DFPT)
D_ODP = 10.45                         # eV/A, Li et al., holes, combined over degenerate bands
W_OPT_SI = 64.1e-3                    # eV, measured zone-center optical phonon (Sect. 5.1)

d = np.load(os.path.join(HERE, "..", "ch05", "fig5_2_data.npz"))
qz = d["q"][:61, 2]                   # units 2pi/a along (0,0,z)
wLA = d["f"][:61, 2] * CM             # eV
Qsi = qz * 2 * np.pi / A_SI           # A^-1
Qs, ws = Qsi[1:], wLA[1:]
small_Q = np.linalg.norm(d["q"][183:189], axis=1) * 2 * np.pi / A_SI
small_w = d["f"][183:189, 2] * CM
c_LA = small_w[0] / (small_Q[0] * HBARC) * C_KMS


def ell(M, w):
    """zero-point length (2 M omega)^-1/2 in eV^-1"""
    return 1 / np.sqrt(2 * M * w)


def g_ac(Q_A, w, Xi):
    return Xi * Q_A * HBARC * ell(M_CELL_SI, w)          # eV


# interpolate the LA branch on a fine grid; below the first DFPT point use omega = c Q
Qfine = np.logspace(-3, np.log10(Qsi[-1]), 400)
w_fine = np.where(Qfine < Qs[0], c_LA / C_KMS * Qfine * HBARC, np.interp(Qfine, Qs, ws))
g_par = g_ac(Qfine, w_fine, XI_D + XI_U)
g_perp = g_ac(Qfine, w_fine, XI_D)
l0_si = ell(M_CELL_SI, W_OPT_SI)
g_opt = D_ODP * HBARC * l0_si * np.ones_like(Qfine)

# ---------------- GaAs ----------------
W_L = 8.79 * THZ                      # eV
W_T = 8.13 * THZ
EPS_INF, EPS_0 = 10.88, 12.9
A_GAAS = 5.638
OMEGA_A3 = A_GAAS ** 3 / 4            # A^3
OMEGA = OMEGA_A3 / HBARC ** 3         # eV^-3
MSTAR = 0.067 * ME
DEPS = 1 / EPS_INF - 1 / EPS_0
CF2 = E2 * W_L / (2 * OMEGA) * DEPS   # eV^4
CF = np.sqrt(CF2)                     # eV^2
g_fr = CF / (Qfine * HBARC)
alphaF = ALPHA * DEPS * np.sqrt(MSTAR / (2 * W_L))
r_p = 1 / np.sqrt(2 * MSTAR * W_L)    # eV^-1


# check alpha_F as the second-order shift: -(Omega C_F^2 / 2 pi^2) int_0^inf dQ / (omega_L + Q^2/2m*)
shift = OMEGA * CF2 / (2 * np.pi ** 2) * quad(lambda Q: 1 / (W_L + Q * Q / (2 * MSTAR)), 0, np.inf)[0]
assert abs(shift / (alphaF * W_L) - 1) < 1e-8
# check C_F against the LST route: e^2 Z*^2/(Omega eps_inf mu) = omega_L^2 - omega_T^2 (eq:D.14-LOTO)
MU = 69.723 * 74.922 / (69.723 + 74.922) * U
Zs = np.sqrt(OMEGA * EPS_INF * MU * (W_L ** 2 - W_T ** 2) / E2)
CF_Z = E2 * Zs / (OMEGA * EPS_INF * np.sqrt(2 * W_L * MU))
CF_LST = np.sqrt(E2 * W_L / (2 * OMEGA) * (1 / EPS_INF) * (1 - W_T ** 2 / W_L ** 2))

if __name__ == "__main__":
    print(f"Si: c_LA(DFPT, [001]) = {c_LA:.2f} km/s; M_cell = {M_CELL_SI/1e9:.3f} GeV")
    for QA in (0.01, 0.1):
        wq = np.interp(QA, Qfine, w_fine)
        print(f"  Q = {QA} A^-1 ({QA*HBARC:.1f} eV): omega_LA = {wq*1e3:.3f} meV, l_Q = {ell(M_CELL_SI, wq)*HBARC:.4f} A,"
              f" |g| axis {g_ac(QA, wq, XI_D+XI_U)*1e3:.2f} meV, perp {g_ac(QA, wq, XI_D)*1e3:.3f} meV")
    print(f"  large-angle-averaged LA: sqrt(Xi_d^2 + Xi_d Xi_u + 3/8 Xi_u^2) = {np.sqrt(XI_D**2+XI_D*XI_U+3/8*XI_U**2):.2f} eV (Li Eq. 15)")
    print(f"  optical: l_0 = {l0_si*HBARC:.4f} A, |g| = {g_opt[0]*1e3:.0f} meV")
    print(f"GaAs: omega_L = {W_L*1e3:.2f} meV, omega_T = {W_T*1e3:.2f} meV, 1/eps_inf - 1/eps_0 = {DEPS:.5f}")
    print(f"  Omega = {OMEGA_A3:.2f} A^3 = {OMEGA:.4e} eV^-3; e^2 = {E2:.4f}")
    print(f"  C_F^2 = {CF2:.4e} eV^4, C_F = {CF:.4e} eV^2 = {CF/HBARC*1e3:.3f} meV/A^-1 x ...;"
          f" C_F/(1 A^-1) = {CF/HBARC*1e3:.3f} meV")
    print(f"  via Z* (={Zs:.3f}): C_F = {CF_Z:.4e}; via LST form: {CF_LST:.4e}")
    for QA in (0.01, 0.1, 1 / (r_p * HBARC)):
        print(f"  |g| at Q = {QA:.4f} A^-1: {CF/(QA*HBARC)*1e3:.2f} meV")
    print(f"  m* = 0.067 m_e = {MSTAR/1e3:.2f} keV; sqrt(m*/2 omega_L) = {np.sqrt(MSTAR/(2*W_L)):.1f}")
    print(f"  alpha_F = {alphaF:.4f}; shift alpha_F omega_L = {alphaF*W_L*1e3:.3f} meV")
    DEPS_LST = (1 / EPS_INF) * (1 - W_T ** 2 / W_L ** 2)
    print(f"  LST route: (1/eps_inf)(1 - omega_T^2/omega_L^2) = {DEPS_LST:.5f}; alpha_F = {ALPHA*DEPS_LST*np.sqrt(MSTAR/(2*W_L)):.4f}"
          f" ({(DEPS_LST/DEPS-1)*100:+.1f} % in 1/eps_inf - 1/eps_0)")
    print(f"  r_p = (2 m* omega_L)^-1/2 = {r_p*HBARC:.1f} A; 1/r_p = {1/(r_p*HBARC):.4f} A^-1 = {1/r_p:.0f} eV")
    print(f"  ratio GaAs/Si-axis at 0.01 A^-1: {CF/(0.01*HBARC)/g_ac(0.01, np.interp(0.01,Qfine,w_fine), XI_D+XI_U):.1f}")

    plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
                         "font.family": "serif", "mathtext.fontset": "cm"})
    BLUE, ORANGE, GREEN = "#2a6fb0", "#c4661f", "#3a8a3a"
    fig, ax = plt.subplots(figsize=(4.4, 3.1))
    lo = Qfine <= 0.1
    hi = Qfine >= 0.1
    for y, col, ls_lab in ((g_fr, ORANGE, "GaAs, LO (Fröhlich)"),
                           (g_opt, GREEN, "Si holes, optical"),
                           (g_par, BLUE, r"Si electrons, LA, $\mathbfit{Q}\parallel$ valley axis"),
                           (g_perp, BLUE, r"Si electrons, LA, $\mathbfit{Q}\perp$ valley axis")):
        dash = (0, (4, 2)) if "perp" in ls_lab or "\\perp" in ls_lab else "-"
        ax.plot(Qfine[lo], y[lo] * 1e3, color=col, lw=1.3, ls=dash, label=ls_lab)
        ax.plot(Qfine[hi], y[hi] * 1e3, color=col, lw=0.9, ls=":")
    ax.axvspan(0.1, Qsi[-1], color="0.93", lw=0)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-3, Qsi[-1])
    ax.set_ylim(0.5, 5e4)
    ax.set_xlabel(r"$|\mathbfit{Q}|$ (\AA$^{-1}$)".replace(r"\AA", "Å"))
    ax.set_ylabel(r"$|g|$ (meV)")
    ax.text(2.5e-3, 3.0e3, r"$\propto Q^{-1}$", color=ORANGE)
    ax.text(1.6e-3, 330, r"$\propto Q^{0}$", color=GREEN)
    ax.text(2.5e-3, 28, r"$\propto Q^{1/2}$", color=BLUE)
    ax.text(0.12, 3.5e4, "outside the\nlong-wavelength\nrange", fontsize=7, color="0.4", va="top")
    top = ax.secondary_xaxis("top", functions=(lambda x: x * HBARC / 1e3, lambda y: y * 1e3 / HBARC))
    top.set_xlabel(r"$|\mathbfit{Q}|$ (keV)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, frameon=False, fontsize=6.5)
    fig.savefig(OUT, bbox_inches="tight")
    print("wrote", OUT)
