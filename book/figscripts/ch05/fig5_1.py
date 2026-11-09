"""Fig. 5.1: energy and length scales of electrons and nuclei in silicon, and the Born-Oppenheimer surface (Sect. 5.1).
Output: tex/figures/ch05/fig5_1.pdf. Prints every number quoted in Sect. 5.1 and its worked example.
Data: fig5_1_data.npz from fig5_1_data.py (Quantum ESPRESSO run of fig5_1_qe.sh: PBE, SG15 ONCV Si_ONCV_PBE-1.2.upf,
ecutwfc 50 Ry, 8^3 k grid, a = 5.431 A, natural Si mass 28.0855 u; DFPT 4^3 q grid, matdyn DOS on 40^3).
Constants and inputs (sources):
  m_e = 0.51099895 MeV, Hartree alpha^2 m_e = 27.211386 eV, a_0 = 0.529177 A, u = 931.49410242 MeV (CODATA 2018)
  M = 28.0855 u = 26.16 GeV (natural silicon, as in App. D.13 / C.6)  -> kappa_BO = (m_e/M)^(1/4)
  zone-center optical phonon 15.5 THz (Nilsson and Nelin, PRB 6, 3777 (1972)) -> 64.1 meV
  E_g = 1.17 eV (low T), E_dir = 3.4 eV at Gamma (Sect. 3.3), plasma energy 16.6 eV (Sect. 4.3)
  a = 5.431 A (Sect. 3.1), bond length sqrt(3) a/4
  <u_x^2> = 0.005941 A^2 at 293 K (Flensburg and Stewart, PRB 60, 284 (1999), abstract; one Cartesian component,
  B = 8 pi^2 <u_x^2> = 0.469 A^2); zero-temperature <u_x^2> from the DFPT phonon DOS:
  <u_x^2> = (1/6) int dw g(w) coth(w/2T) / (2 M w), g normalized to 6 modes per two-atom cell
  (average over the 2 atoms and 3 directions, which are equivalent by symmetry).
Panel (c): frozen zone-center optical displacement along [111]; u = change of the length of the [111] bond.
  Harmonic + cubic + quartic polynomial fit of E(u) over |u| <= 0.10 A (modelling choice);
  Phi_opt = d^2E/du^2 at u = 0 per cell, omega^2 = 2 Phi_opt / M (reduced mass M/2 of the bond coordinate);
  zero-point length of the coordinate l = (2 (M/2) omega)^(-1/2), shaded +-l.
  Hellmann-Feynman check: F_u from pw.x forces against -dE/du from a degree-6 polynomial fit of E over all points,
  compared for |u| <= 0.2 A (curve drawn for |u| <= 0.25 A).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch05", "fig5_1.pdf")
HC = 1973.2698            # eV A
ME, HA, A0, AMU = 0.51099895e6, 27.211386, 0.529177, 931.49410242e6
M28 = 27.9769265 * AMU
MNAT = 28.0855 * AMU
CM1 = 1.23984198e-4       # eV per cm^-1
KB = 8.617333e-5          # eV/K

kap = (ME / MNAT) ** 0.25
w_meas = 4.135667696e-15 * 15.5e12
EG, EDIR, WP, A = 1.17, 3.4, 16.6, 5.431
bond = np.sqrt(3) * A / 4
print(f"m_e/M = {ME/MNAT:.4e}; kappa = {kap:.4f}, kappa^2 = {kap**2:.3e}, kappa^3 = {kap**3:.3e}, kappa^4 = {kap**4:.3e}")
print(f"kappa a0 = {kap*A0:.4f} A; kappa^2 Ha = {kap**2*HA:.4f} eV; kappa^3 Ha = {kap**3*HA*1e3:.2f} meV; "
      f"kappa^4 Ha = {kap**4*HA*1e3:.3f} meV; kappa^6 Ha = {kap**6*HA:.2e} eV")
print(f"omega = {w_meas*1e3:.1f} meV; omega/Ha = {w_meas/HA:.3e} = {w_meas/HA/kap**2:.2f} kappa^2; "
      f"omega/E_g = {w_meas/EG:.4f} = {w_meas/EG/kap**2:.1f} kappa^2; Ha/E_g = {HA/EG:.1f}")

d = np.load(os.path.join(HERE, "fig5_1_data.npz"))
u, E, Fu, dos = d["u"], d["E"], d["Fu"], d["dos"]

# zero-point and 293 K amplitudes from the DOS
ux0 = ux293 = np.nan
if dos.size:
    w = dos[:, 0] * CM1
    g = dos[:, 1] / CM1
    m = w > 1e-4
    w, g = w[m], g[m]
    norm = np.trapezoid(g, w)
    g *= 6 / norm
    def uxx(T):
        c = 1.0 if T == 0 else 1 / np.tanh(w / (2 * KB * T))
        return np.trapezoid(g * c / (2 * MNAT * w), w) / 6 * HC**2
    ux0, ux293 = np.sqrt(uxx(0)), np.sqrt(uxx(293))
    print(f"DOS norm (raw) {norm:.3f}; DFPT <u_x^2>^(1/2): T=0 {ux0:.4f} A, 293 K {ux293:.4f} A "
          f"(<u_x^2> = {ux293**2:.5f} A^2 vs measured 0.005941); max freq {w.max()*1e3:.1f} meV")
ux293m = np.sqrt(0.005941)
print(f"measured 293 K {ux293m:.4f} A; u/a: T=0 {ux0/A:.4f}, 293 K {ux293m/A:.4f}; u/bond: T=0 {ux0/bond:.4f}; "
      f"u0/(kappa a0) = {ux0/(kap*A0):.2f}; kappa a0/a = {kap*A0/A:.4f}; a/a0 = {A/A0:.2f}")

# frozen phonon
sel = np.abs(u) <= 0.1001
c = np.polyfit(u[sel], E[sel], 4)
phi2, phi3 = 2 * c[-3], 6 * c[-4]
wopt = HC * np.sqrt(2 * phi2 / MNAT)
lz = HC / np.sqrt(MNAT * wopt)
print(f"Phi_opt = {phi2:.2f} eV/A^2, Phi3 = {phi3:.1f} eV/A^3; omega_opt = {wopt*1e3:.1f} meV; l_zp(u) = {lz:.4f} A")
print(f"cubic/harmonic at u = l: Phi3 l/(3 Phi2) = {phi3*lz/(3*phi2):.4f} (kappa = {kap:.4f}); "
      f"Phi3 l^3/6 = {phi3*lz**3/6*1e3:.3f} meV")
cf = np.polyfit(u, E, 6)
dE = -np.polyval(np.polyder(cf), u)
rel = np.abs(Fu - dE)
print("HF check  u, F_u, -dE/du:", *[f"{a:+.2f}:{b:+.4f}/{cc:+.4f}" for a, b, cc in zip(u, Fu, dE)])
m2 = (np.abs(u) <= 0.2001) & (u != 0)
print(f"|u| <= 0.2 A: max relative |F_u + dE/du|/|F_u| = {np.max(rel[m2]/np.abs(Fu[m2]))*100:.3f} % "
      f"(the end points |u| = 0.3 A are limited by the polynomial derivative)")

plt.rcParams.update({"font.size": 8.5})
fig, (ax, bx, cx) = plt.subplots(1, 3, figsize=(6.6, 3.0), gridspec_kw={"width_ratios": [1, 1, 1.5], "wspace": 1.3})
CE, CN, CK = "C0", "C3", "0.45"

def ladder(axis, items, unit, nudge={}):
    for val, lab, col, ls in items:
        axis.plot([0, 1], [val, val], color=col, lw=1.4, ls=ls)
        axis.text(1.08, val * nudge.get(lab, 1.0), lab, va="center", fontsize=6.5, color="k")
    axis.set_yscale("log"); axis.set_xlim(0, 1); axis.set_xticks([])
    for s in ("top", "right", "bottom"):
        axis.spines[s].set_visible(False)
    axis.set_ylabel(unit)

ladder(ax, [(HA, r"$\alpha^2m_e$ 27.2", CE, "-"), (WP, r"$\omega_p$ 16.6", CE, "-"), (EDIR, r"$E_{\mathrm{dir}}$ 3.4", CE, "-"),
            (EG, r"$E_{\mathrm{g}}$ 1.17", CE, "-"), (kap**2 * HA, r"$\kappa_{\mathrm{BO}}^2\alpha^2m_e$ 0.12", CK, "--"),
            (w_meas, r"$\omega_{\mathrm{opt}}$ 0.064", CN, "-"), (kap**3 * HA, r"$\kappa_{\mathrm{BO}}^3\alpha^2m_e$", CK, "--"),
            (kap**4 * HA, r"$\kappa_{\mathrm{BO}}^4\alpha^2m_e$", CK, "--"), (kap**6 * HA, r"$\kappa_{\mathrm{BO}}^6\alpha^2m_e$", CK, "--")],
       "energy (eV)", nudge={r"$\alpha^2m_e$ 27.2": 1.45, r"$\omega_p$ 16.6": 0.7,
                              r"$\kappa_{\mathrm{BO}}^2\alpha^2m_e$ 0.12": 1.5, r"$\omega_{\mathrm{opt}}$ 0.064": 0.65})
ax.set_ylim(1e-6, 60)
ax.set_title("(a) energies", fontsize=8.5, loc="left")
items = [(A, r"$a$ 5.43", CE, "-"), (bond, "bond 2.35", CE, "-"), (A0, r"$a_0$ 0.53", CE, "-"),
         (ux293m, "293 K", CN, "-"), (ux0, r"$T = 0$", CN, "-"), (kap * A0, r"$\kappa_{\mathrm{BO}}a_0$", CK, "--")]
ladder(bx, [i for i in items if np.isfinite(i[0])], "length (Å)")
bx.set_ylim(0.02, 8)
bx.set_yticks([0.03, 0.1, 0.3, 1, 3], ["0.03", "0.1", "0.3", "1", "3"]); bx.minorticks_off()
bx.set_title("(b) lengths", fontsize=8.5, loc="left")

uu = np.linspace(-0.32, 0.32, 300)
cx.axvspan(-lz, lz, color="0.9", lw=0)
cx.plot(uu, np.polyval(cf, uu) * 1e3, color="k", lw=1.0, label=r"$E^{\mathrm{ad}}_{\mathrm{cell}}$ (fit)")
cx.plot(uu, 0.5 * phi2 * uu**2 * 1e3, color=CK, lw=0.9, ls="--", label="harmonic")
cx.plot(u, E * 1e3, "o", color="k", ms=3.2)
cx.set_xlabel(r"bond stretch $u$ (Å)"); cx.set_ylabel(r"$E^{\mathrm{ad}}_{\mathrm{cell}}$ (meV)")
cx.set_ylim(-20, 900)
ins = cx.inset_axes([0.37, 0.5, 0.38, 0.37])
ins.plot(u, Fu, "o", color=CN, ms=2.4, label="H–F")
ui = uu[np.abs(uu) <= 0.25]
ins.plot(ui, -np.polyval(np.polyder(cf), ui), color="k", lw=0.8, label=r"$-\mathrm{d}E/\mathrm{d}u$")
ins.axhline(0, color="0.7", lw=0.4)
ins.set_xticks([-0.2, 0, 0.2], ["−0.2", "0", "0.2"]); ins.set_yticks([-2, 0, 2, 4, 6])
ins.tick_params(labelsize=6.2, pad=1.5); ins.set_title("force (eV/Å)", fontsize=6.2, pad=2); ins.set_xlabel(r"$u$ (Å)", fontsize=6.2, labelpad=1)
# no legend in the small inset: the caption names the circles (Hellmann-Feynman force) and the line (-dE/du)
cx.set_title("(c) silicon, PBE", fontsize=8.5, loc="left")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
