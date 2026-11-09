"""Fig. 3.7: germanium and gallium arsenide bands (Sect. 3.3). Output: tex/figures/ch03/fig3_7.pdf.
Prints and asserts the numbers quoted in the caption, the GaAs mass check of Sect. 3.3 and the Kane (k.p) check
in the empirical model (text only).

Panel (a), germanium: the local empirical pseudopotential of Cohen and Bergstresser (epm.py, form factors of Phys. Rev.
141, 789 (1966), a = 5.66 A of the original fit), plane-wave cutoff 21 (2pi/a)^2, with a rigid scissor that shifts all
conduction bands so that the L minimum sits at the measured 0.744 eV. No spin-orbit coupling. The nonlocal
pseudopotential with spin-orbit coupling of Chelikowsky and Cohen, Phys. Rev. B 14, 556 (1976), would be the better
model, but its Ge parameters (and the 1984 erratum, PRB 30, 4828) could not be obtained and verified, so it is not used.
The PBE germanium bands below (which close the gap at the measured a) are kept for the printed comparison only.
Gaps of panel (a) are written to fig3_7.log (run: python3 fig3_7.py > fig3_7.log).

Panel (b) and the PBE numbers: the representative first-principles calculation (App. E.1), qe_ch03.py, cache qe_ge_gaas.npz: Quantum ESPRESSO
7.6, PBE, SG15 norm-conserving pseudopotentials, 60 Ry, Gamma-centred 12^3 density grid, measured room-temperature
lattice constants a = 5.658 A (Ge) and 5.653 A (GaAs) (editor ruling, Sect. 3.3).
  Ge: spin-orbit coupling included (fully relativistic Ge_ONCV_PBE_FR-1.0.upf, two-component spinors). PBE closes the
      gap of germanium; the run uses cold smearing (0.002 Ry). Energies from the Gamma_8 valence level. A scalar-
      relativistic run (Ge_ONCV_PBE-1.2.upf, no spin-orbit coupling) and an 80 Ry check are printed for comparison.
  GaAs: scalar-relativistic, no spin-orbit coupling (Ga_ONCV_PBE-1.2.upf with 3d, As_ONCV_PBE-1.2.upf).
Text check (not used in the figure): the Kane two-level estimate in the local empirical pseudopotential of Cohen and
Bergstresser (epm.py), where v = p/m_e exactly.

Measured values quoted in the caption and text (not used in the calculation):
  Ge: E_g = 0.744 eV at L (Rideau et al., cond-mat/0607510, Table VI), E_dir = Gamma_2' = 0.89 eV (Rideau Table II),
      Delta_SO = 0.296 eV (Rideau Table II).
  GaAs: E_g = E_dir = 1.52 eV at Gamma (Lucero et al. Table I, low temperature), L and X valleys 1.815 and 1.981 eV,
      m*_Gamma = 0.067 (Vurgaftman, Meyer and Ram-Mohan 2001); E_P = 22.9 eV (Gawarecki et al., Table VIII).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from epm import EPM, HBARC                # noqa: E402
import numpy as np                        # noqa: E402
import matplotlib                         # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt           # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ME = 510998.95


def close(x, q, tol, name):
    assert abs(x - q) <= tol, f"{name}: computed {x} vs quoted {q}"
    print(f"  {name:58s} {x:.4f}   (quoted {q})")


def levels(e, lo, hi, tol=2e-3):
    """Distinct levels (energy, degeneracy) of one k point between lo and hi."""
    e = np.sort(e[(e > lo) & (e < hi)])
    out = []
    for x in e:
        if out and abs(x - out[-1][0]) < tol:
            out[-1][1] += 1
        else:
            out.append([x, 1])
    return [(float(a), b) for a, b in out]


d = np.load(os.path.join(HERE, "qe_ge_gaas.npz"))
kp, xp, ticks = d["kp"], d["xp"], list(d["ticks"])
iG = int(np.argmin(np.linalg.norm(kp[:100], axis=1)))

# ---- germanium with spin-orbit coupling --------------------------------------------------------------------------
gs, gb = d["GeSO_scan"], d["GeSO_bands"]          # scan: Gamma, L, X, then Gamma-X in steps of 0.01
LG = levels(gs[0], gs[0, 19] + 1e-3, gs[0, 39])
print("Ge+SO levels at Gamma (E, degeneracy):", [(round(a, 3), b) for a, b in LG])
G8 = [a for a, b in LG if b == 4][0]               # Gamma_8 valence (p, j = 3/2): the lowest fourfold level
G7v = [a for a, b in LG if b == 2 and G8 - 0.6 < a < G8 - 0.1]
G7c = [a for a, b in LG if b == 2 and abs(a - G8) < 0.1]
LL = levels(gs[1], G8 - 1.5, G8 + 2.0)
print("Ge+SO levels at L:", [(round(a - G8, 3), b) for a, b in LL])
L6c = [a for a, b in LL if a > G8 - 0.2][0]
XX = levels(gs[2], G8 - 4, G8 + 2.0)
X5c = [a for a, b in XX if a > G8][0]
line = gs[3:, 28] - G8
dmin = float(line.min())
print(f"Ge+SO (60 Ry): Gamma_7v (split-off) {G7v[0] - G8 if G7v else np.nan:+.3f}; Gamma_7c (s) {G7c[0] - G8 if G7c else np.nan:+.3f};"
      f" L_6c {L6c - G8:+.3f}; X_5c {X5c - G8:+.3f}; lowest band 29 on Gamma-X {dmin:+.3f} eV at "
      f"{np.arange(0, 1.0001, 0.01)[np.argmin(line)]:.2f}")
e80 = d["geso80_edges"]
L80 = levels(e80[0], e80[0, 19] + 1e-3, e80[0, 39])
G880 = [a for a, b in L80 if b == 4][0]
print("  80 Ry: Gamma levels", [(round(a - G880, 3), b) for a, b in L80], "; L", [(round(a - G880, 3), b)
      for a, b in levels(e80[1], G880 - 1.5, G880 + 2.0)])
# scalar-relativistic germanium
sr = d["Ge_scan"]
vS = sr[0, 13]
print(f"Ge scalar-relativistic: Gamma_2'c {sr[0, 14] - vS:+.3f}, L_1c {sr[1, 14] - vS:+.3f}, X_1c {sr[2, 14] - vS:+.3f} eV"
      f" (App. E.1: 0.047, 0.191)")

# ---- GaAs ---------------------------------------------------------------------------------------------------------
a_s = d["GaAs_scan"]
vA = a_s[0, 8]
ga = dict(G=a_s[0, 9] - vA, L=a_s[1, 9] - vA, X=a_s[2, 9] - vA)
print("GaAs: Gamma {G:.3f}, L {L:.3f}, X {X:.3f} eV".format(**ga))
G1 = 2 * np.pi * HBARC / 5.653
j = np.arange(-4, 5) * 0.0025
m100 = G1 ** 2 / (2 * np.polyfit(j[2:7], a_s[3 + 101:3 + 101 + 9, 9][2:7], 2)[0]) / ME
m111 = G1 ** 2 / (2 * np.polyfit(j[2:7], a_s[3 + 101 + 9:, 9][2:7], 2)[0]) / ME
print(f"GaAs PBE Gamma-valley curvature mass (+-0.005 (2pi/a)): [100] {m100:.4f}, [111] {m111:.4f} m_e")

# ---- text check: Kane estimate in the empirical model -------------------------------------------------------------
eGa = EPM("GaAs", ecut=21)
unit = 2 * np.pi * HBARC / eGa.a
h = 0.003
f = [eGa.bands(t * h * np.array([1.0, 0, 0]))[4] for t in (-1, 0, 1)]
mG = 1 / (ME * (f[0] - 2 * f[1] + f[2]) / (h * unit) ** 2)
w, vel = eGa.velocity(np.zeros(3))
EP = 2 * ME * np.sum(np.abs(vel[0, 1:4, 4]) ** 2)
Eg = w[4] - w[3]
print(f"empirical model (text): E_g {Eg:.3f}, E_P {EP:.2f} eV, two-level m* {1/(1+EP/Eg):.4f}, curvature {mG:.4f}")
EPm, Egm, Dso = 22.911, 1.519, 0.341
for g in (0.5, 1.77, Egm):
    print(f"  Kane with E_P = {EPm}, Delta_SO = {Dso} at E_g = {g}: m* = {1/(1 + EPm/3*(2/g + 1/(g+Dso))):.4f}")
print(f"  |v_cv| = sqrt(E_P/2m_e) = {np.sqrt(EPm/(2*ME)):.3e} = {np.sqrt(EPm/(2*ME))/2.650e-3:.2f} v_max")

# ---- germanium panel (a): local empirical pseudopotential with a scissor -----------------------------------------
eGe = EPM("Ge", ecut=21)
raw = eGe.bands(kp, nb=8)
iGp = int(np.argmin(np.linalg.norm(kp, axis=1)))
vbm = raw[iGp, 3]
t = np.linspace(0, 1, 201)[:, None]
dl = eGe.bands(t * np.array([1.0, 0, 0]), nb=5)[:, 4] - vbm        # Gamma-X (Delta line)
e0 = dict(G=eGe.bands(np.zeros(3), nb=5)[4] - vbm, L=eGe.bands(np.array([.5, .5, .5]), nb=5)[4] - vbm,
          X=dl[-1], D=float(dl.min()), kD=float(t[np.argmin(dl), 0]))
SCISSOR = 0.744 - e0["L"]                                          # puts L at the measured gap
epm = {k_: (v_ + SCISSOR if k_ != "kD" else v_) for k_, v_ in e0.items()}
epm_b = raw - vbm
epm_b[:, 4:] += SCISSOR
print(f"Ge panel (a), local EPM (Cohen-Bergstresser), unshifted: L {e0['L']:.3f}, Gamma_2'c {e0['G']:.3f}, "
      f"Delta min {e0['D']:.3f} at {e0['kD']:.2f} (2pi/a), X {e0['X']:.3f} eV")
print(f"  scissor {SCISSOR:+.3f} eV -> indirect gap (L) {epm['L']:.3f}, direct gap (Gamma) {epm['G']:.3f}, "
      f"Delta min {epm['D']:.3f}, X {epm['X']:.3f} eV; Delta_SO = 0 (no spin-orbit coupling in the model)")
print("  measured: L 0.744 (0 K) / 0.66 (300 K), Gamma 0.89, Delta_SO 0.296 eV")
assert e0["L"] < e0["D"] < e0["G"], "ordering L < Delta < Gamma in the local model"

QUOTE = {"G7c[0] - G8": (-0.05, 5e-3), "L6c - G8": (0.10, 6e-3), "G7v[0] - G8": (-0.29, 6e-3),
         "X5c - G8": (0.66, 5e-3), "sr[0, 14] - vS": (0.046, 1e-3), "sr[1, 14] - vS": (0.191, 1e-3),
         "ga['G']": (0.51, 5e-3), "ga['L']": (1.00, 5e-3), "ga['X']": (1.46, 5e-3), "m100": (0.030, 5e-4),
         "Eg": (1.42, 5e-3), "SCISSOR": (-0.21, 5e-3), "epm['G']": (1.01, 5e-3), "epm['D']": (0.81, 5e-3), "EP": (18.3, 0.05), "1/(1+EP/Eg)": (0.0718, 5e-5), "mG": (0.0721, 5e-5)}
d80 = levels(e80[0], e80[0, 19] + 1e-3, e80[0, 39])
assert abs([a for a, b in d80 if b == 2 and abs(a - G880) < 0.1][0] - G880 - (G7c[0] - G8)) < 2e-3, "80 Ry check"
print("Numbers quoted")
for k_, (q_, t_) in QUOTE.items():
    close(eval(k_), q_, t_, k_)

# ---- figure -------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9})
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.2), sharey=True, gridspec_kw={"wspace": 0.08})
labs = ["L", r"$\Gamma$", "X", "W", "K", r"$\Gamma$"]
ax = axs[0]
eb = epm_b
for b in range(8):
    ax.plot(xp, eb[:, b], color="k" if b < 4 else "C0", lw=1.0)
ax.plot([ticks[1]], [epm["G"]], "s", color="C1", ms=4)
ax.text(ticks[1] + 0.05, epm["G"] - 0.55, r"$\Gamma_{2'c}$", color="C1", fontsize=8)   # below the band rising from Gamma
ax.text(ticks[0] + 0.05, epm["L"] - 0.55, r"$L_{1c}$", color="C3", fontsize=8)
ax.plot([ticks[0] + 0.004], [epm["L"]], "o", color="C3", ms=3)
ax.plot([ticks[1] + epm["kD"] * (ticks[2] - ticks[1])], [epm["D"]], "o", color="C3", ms=3)
ax.text(0.02, 0.97, "(a) Ge", transform=ax.transAxes, va="top")
bx = axs[1]
eb = d["GaAs_bands"] - vA
for b in range(5, 13):
    bx.plot(xp, eb[:, b], color="k" if b < 9 else "C0", lw=1.0)
bx.annotate("", xy=(ticks[1] + 0.02, ga["G"]), xytext=(ticks[1] + 0.02, 0),
            arrowprops=dict(arrowstyle="<->", color="C2", lw=1.0))
bx.text(ticks[1] + 0.08, ga["G"] + 0.15, r"$E_{\mathrm{g}}$", color="C2")
bx.plot([ticks[0] + 0.004], [ga["L"]], "o", color="C3", ms=3)
bx.plot([ticks[2]], [ga["X"]], "o", color="C3", ms=3)
bx.text(0.02, 0.97, "(b) GaAs", transform=bx.transAxes, va="top")
for a in axs:
    for t in ticks:
        a.axvline(t, color="0.8", lw=0.5, zorder=0)
    a.axhline(0, color="0.6", lw=0.5, ls=":")
    a.set_xticks(ticks, labs)
    a.set_xlim(ticks[0], ticks[-1])
axs[0].set_ylim(-4, 6.5)
axs[0].set_ylabel(r"$\varepsilon_{n\mathbf{k}}$ $-$ VBM (eV)")
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch03", "fig3_7.pdf")
fig.savefig(out, bbox_inches="tight")
print("wrote", os.path.normpath(out))
