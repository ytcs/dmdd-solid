"""Fig. 7.5 (configuration-coordinate diagrams of the silicon T center and the diamond NV- center, and their
zero-temperature emission weights) and every number of Sect. 7.4 on color centers and displacement thresholds, including
worked example "Zero-phonon fractions".  Natural units hbar = c = k_B = 1.

Output: tex/figures/ch07/fig7_5.pdf

Inputs and their sources
  T center (silicon):
    zero-phonon line 935.1 meV (Bergeron et al., arXiv:2006.08794, Fig. 1; 1326 nm in Bergeron et al., PRX Quantum 1,
       020301 (2020), arXiv:2006.08793); hc/1326 nm = 0.935 eV.
    zero-phonon fraction of the emitted photons ("Debye-Waller factor") 0.23(1), excited-state lifetime 0.94(1) us,
       measured at 1.4-4.2 K (Bergeron et al., PRX Quantum 1, 020301, abstract and Sect. A).
  NV- center (diamond):
    zero-phonon line 1.945 eV (Doherty et al., Phys. Rep. 528, 1 (2013), arXiv:1302.3288, Sect. 1.1).
    Huang-Rhys factor S = 3.85 +- 0.05 from the measured lineshape; measured zero-phonon fraction of the luminescence
       3.2 % (S~ = -ln w = 3.45); dominant effective phonon 64 meV (65 meV computed); spectrum at 8 K
       (Alkauskas et al., New J. Phys. 16, 073026 (2014), arXiv:1405.7313, Sects. 2.2, 3 and 4.3).
    Luminescence lineshape L(w) = C w^3 A(w) (Alkauskas Eq. (2)): the photon rate carries the cube of the photon energy.
  Silicon: optical phonon 64 meV (Sect. 5.3); M_Si = 26.16 GeV (Sect. 5.6); v_max = 2.650e-3, v_max^2 = 7.023e-6
     (Sect. 1.3, 3.3); gap m_min = 0.333 MeV (Sect. 3.3).
  Displacement thresholds of silicon from DFT molecular dynamics (Holmstrom, Kuronen and Nordlund, Phys. Rev. B 78,
     045202 (2008), Table IV, LDA): <111> 12.5 eV (global minimum), <100> 20.5 eV (GGA 19.5; abstract 20), average for
     Frenkel pairs 36 eV, for any defect including bond defects 24 eV.  Formation energies (Table III, LDA/GGA): vacancy
     3.4/3.9, tetrahedral interstitial 5.7/5.8, split <110> 4.7/4.9, ground-state close Frenkel pair (tetrahedral
     interstitial 4.7 A from its vacancy) 6.8/7.5, bond defect 2.6/3.0 eV.  Experimental onset 12.9 +- 0.6 eV (Loferski
     and Rappaport, Phys. Rev. 111, 432 (1958)).
  Maximum nuclear recoil energy E_R,max = 2 mu^2 v_max^2 / M (Sect. 1.3).

Modelling choices (named in the caption)
  Each center is drawn with a single effective mode, the same in both electronic states, in the Condon approximation
  (Sect. 5.6).  Energies in units of that mode's energy omega_0, coordinate Q in units of omega_0^{-1/2} (mass-weighted),
  so that the curves depend on S_HR only.  The vertical gap E_ZPL between the two surfaces is not to scale.
  T center: S_HR = -ln 0.23 (photon-count value; the omega^3 correction is not applied, no sourced phonon energy).
"""
import os
import numpy as np
from math import factorial
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch07")
os.makedirs(OUT, exist_ok=True)
vmax, vmax2 = 2.650e-3, 7.023e-6


def close(x, ref, rtol=5e-3, name=""):
    assert abs(x - ref) <= rtol * abs(ref), f"{name}: {x} vs {ref}"
    print(f"  {name:62s} {x:.6g}   (quoted {ref})")


def poisson(S, p):
    return np.exp(-S) * S**p / factorial(p)


print("T center")
close(1239.84198 / 1326, 0.935, 1e-3, "hc/1326 nm [eV]")
S_T = -np.log(0.23)
close(S_T, 1.47, 3e-3, "S_HR = -ln 0.23")
close(np.exp(-S_T), 0.23, 1e-9, "e^-S")
close(S_T * 0.064 * 3 / 0.935, 0.30, 0.02, "bound on omega^3 shift of S, 3 S w/E with w = 64 meV")
pT = [poisson(S_T, p) for p in range(6)]
print("  weights p = 0..5:", np.round(pT, 3))
close(pT[1], 0.338, 3e-3, "one-phonon weight")
close(1 - pT[0] - pT[1], 0.432, 3e-3, "two or more phonons")

print("NV- center")
S_N, w_N, E_N = 3.85, 0.064, 1.945
close(np.exp(-S_N), 0.0213, 3e-3, "e^-S (S = 3.85)")
pN = [poisson(S_N, p) for p in range(40)]
x = w_N / E_N
mean_cube = sum(pN[p] * (1 - p * x)**3 for p in range(40))
close(mean_cube, 0.677, 3e-3, "<(1 - p w/E)^3> over the Poisson weights")
close(np.exp(-S_N) / mean_cube, 0.0314, 5e-3, "photon-weighted zero-phonon fraction (measured 0.032)")
close(-np.log(0.032), 3.44, 3e-3, "S~ = -ln 0.032 (Alkauskas 3.45)")
close(S_N * w_N, 0.246, 3e-3, "relaxation energy S w [eV]")
close(E_N + S_N * w_N, 2.19, 3e-3, "absorption maximum E_ZPL + S w [eV]")
close(E_N - S_N * w_N, 1.70, 3e-3, "emission maximum E_ZPL - S w [eV]")
close(2 * S_N * w_N, 0.493, 3e-3, "Stokes shift [eV]")
close(np.exp(-S_T) / np.exp(-S_N), 10.8, 0.01, "ratio of T and NV zero-phonon weights")
close(np.sqrt(2 * S_N), 2.77, 3e-3, "displacement in units of omega^-1/2")
print("  NV weights p = 0..6:", np.round(pN[:7], 3), " max at p =", int(np.argmax(pN)))
close(0.064 / (8 * 8.617333e-5), 92.8, 3e-3, "omega/T at 8 K")

print("Thermal occupation at the measurement temperatures")
close(np.exp(-0.010 / (4.2 * 8.617333e-5)), 1.0e-12, 0.01, "exp(-10 meV / 4.2 K)")

print("Kinematic thresholds for exciting the centers (m_min = 2E/v_max^2, q = 2E/v_max)")
close(2 * 0.935 / vmax2 / 1e6, 0.266, 3e-3, "T center m_min [MeV]")
close(2 * 0.935 / vmax / 1e3, 0.706, 3e-3, "T center q [keV]")
close(2 * 1.945 / vmax2 / 1e6, 0.554, 3e-3, "NV m_min [MeV]")
close(2 * 1.945 / vmax / 1e3, 1.468, 3e-3, "NV q at threshold [keV]")
close(2 * 1.17 / vmax2 / 1e6, 0.333, 3e-3, "silicon gap m_min [MeV]")

print("Displacement: dark-matter mass whose maximum recoil reaches E_d (E_R,max = 2 mu^2 v^2 / M)")
M = 26.16e9
for Ed, ref in ((12.5, 0.1535), (36.0, 0.2615)):
    mu = np.sqrt(Ed * M / 2) / vmax
    m = mu * M / (M - mu)
    close(m / 1e9, ref, 3e-3, f"m_chi reaching E_d = {Ed} eV [GeV]")
close(7.5 / 36, 0.21, 0.02, "share of the average threshold stored in a close pair (GGA)")
close(6.8 / 12.5, 0.54, 0.02, "share of the minimum threshold stored in a close pair (LDA)")

# --------------------------------------------------------------------------- figure
blue, orange, gray = "#2a78d6", "#eb6834", "0.45"
fig, axs = plt.subplots(1, 3, figsize=(6.5, 2.8), gridspec_kw=dict(width_ratios=[1, 1, 1.15]))
GAP = 13.0      # drawn vertical offset of the excited surface (units of omega_0), not to scale
for ax, S, name, c, ezpl in ((axs[0], S_T, "T center (Si)", blue, r"$E_{\mathrm{ZPL}} =$" "\n0.935 eV"),
                             (axs[1], S_N, r"NV$^-$ center (diamond)", orange, r"$E_{\mathrm{ZPL}} =$" "\n1.945 eV")):
    d = np.sqrt(2 * S)
    q = np.linspace(-3.2, d + 3.2, 300)
    ax.plot(q, q**2 / 2, color=gray, lw=1.4)
    ax.plot(q, GAP + (q - d)**2 / 2, color=c, lw=1.4)
    ax.set_ylim(-0.5, GAP + 8.0)
    ax.annotate("", xy=(0, GAP + d**2 / 2), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="k", lw=0.8))
    ax.annotate("", xy=(d, d**2 / 2), xytext=(d, GAP), arrowprops=dict(arrowstyle="->", color=c, lw=0.8))
    ax.hlines([0, GAP], [-0.9, d - 0.9], [0.9, d + 0.9], color="k", lw=0.6, ls=":")
    ax.text(0.15, GAP / 2, "absorption", fontsize=7, rotation=90, va="center", ha="left")
    ax.text(d + 0.15, GAP / 2 + 2.5, "emission", fontsize=7, rotation=90, va="center")   # clear of the ground surface
    ax.set_title(("(a) " if S < 2 else "(b) ") + name + rf", $S_{{\mathrm{{HR}}}} = {S:.2f}$", fontsize=7.5)
    ax.annotate("", xy=(d + 0.7, d**2 / 2), xytext=(d + 0.7, 0), arrowprops=dict(arrowstyle="<->", color=gray, lw=0.7))
    ax.text(d + 0.85, d**2 / 4, rf"$S_{{\mathrm{{HR}}}}\omega_0$", fontsize=7, va="center")
    # left of the absorption arrow, between the two surfaces: the only free area at this font size
    ax.text(-3.4, GAP - 1.0, ezpl + "\n(gap not\nto scale)", fontsize=7, va="top", ha="left", linespacing=1.15)
    ax.set_xlabel(r"configuration coordinate $Q\,\omega_0^{1/2}$", fontsize=7.5)
    ax.tick_params(labelsize=7)
    for sname in ("top", "right"):
        ax.spines[sname].set_visible(False)
axs[0].set_ylabel(r"energy / $\omega_0$", fontsize=7.5)
ax = axs[2]
p = np.arange(0, 11)
ax.bar(p - 0.2, [poisson(S_T, k) for k in p], width=0.38, color=blue, label=r"T center, $p = 0$: 0.23")
ax.bar(p + 0.2, [poisson(S_N, k) for k in p], width=0.38, color=orange, label=r"NV$^-$, $p = 0$: 0.021")
ax.set_xlabel(r"phonons emitted $p$", fontsize=7.5)
ax.set_ylabel(r"weight $\mathrm{e}^{-S_{\mathrm{HR}}}S_{\mathrm{HR}}^p/p!$", fontsize=7.5)
ax.set_xticks(range(0, 11, 2))
ax.set_ylim(0, 0.40)
ax.tick_params(labelsize=7)
ax.legend(fontsize=7, frameon=False, loc="upper right")
for sname in ("top", "right"):
    ax.spines[sname].set_visible(False)
for a, lab in zip(axs[2:], "c"):
    a.text(-0.02, 1.02, f"({lab})", transform=a.transAxes, fontsize=8, ha="right", va="bottom")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig7_5.pdf"))
print("wrote fig7_5.pdf")
