"""Fig. 21.5 (fig:21-dirac-recast): recasting published Dirac-material reaches to the total dielectric function.

(a) Ideal Dirac material of Hochberg et al., arXiv:1708.08929 (v_D = 4e-4, eps_bg = 40, g_deg = 2, cutoff 0.2 keV; light
    mediator, 3 events in 1 kg yr), gapped (Delta_D = 2.5 meV) and gapless curves, digitized from the vector figure of the
    arXiv source (figscripts/ch16/data/pub_h_gapped.csv, pub_h_gapless.csv; Sect. 16.1, we:16-factor), and the same
    curves times eps_bg^2 = 1600, the exact recast of eq:16.1-ratio (L_pub = eps_bg^2 L at every (q, omega)).
(b) Recast factor sigma_e^lim(total eps) / sigma_e^lim(published rule) against m_chi:
    black  ZrTe5 with the anisotropic background tensor (308.4, 20.75, 126.1) of Geilhufe et al., arXiv:1910.02091
           Table 2, measured-structure row (Delta_D = 11.8 meV), book halo, orientation average: the ratio of the two event
           integrals, from figscripts/ch16/zrte5_16.npz ('book' and 'src' reaches; Sect. 16.1);
    flat   1600 (ideal material, eps_bg = 40) and 642 = 25.34^2 (isotropized ZrTe5 of 1708.08929), exact;
    gray   the harmonic-mean square 50.53^2 = 2554 and the on-axis factors eps_bg,ii^2 = 431, 1.59e4, 9.51e4.
Every printed number is in fig21_5.log.
Run: python fig21_5.py > fig21_5.log
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
D16 = os.path.join(HERE, "..", "ch16")
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch21", "fig21_5.pdf")

gp = np.loadtxt(os.path.join(D16, "data", "pub_h_gapped.csv"), delimiter=",")
gl = np.loadtxt(os.path.join(D16, "data", "pub_h_gapless.csv"), delimiter=",")
z = np.load(os.path.join(D16, "zrte5_16.npz"))
EBG = 40.0
EBG_ZR08 = 25.34
EBG_AX = np.array([308.4, 20.75, 126.1])
EBG_HM = 3.0 / np.sum(1.0 / EBG_AX)

gp = gp[gp[:, 1] < 1e-30]
gl = gl[gl[:, 1] < 1e-30]
m = z["masses"] / 1e3
with np.errstate(invalid="ignore", divide="ignore"):
    fac = z["book"] / z["src"]
ok = np.isfinite(fac) & (z["book"] < 1e-30)

print(f"(a) ideal Dirac material, recast factor eps_bg^2 = {EBG**2:.0f}")
i_min = int(np.argmin(gp[:, 1]))
print(f"    published gapped minimum {gp[i_min,1]:.2e} cm^2 at {gp[i_min,0]:.1f} keV (digitized point) -> {gp[i_min,1]*EBG**2:.2e} cm^2")
j100 = int(np.argmin(np.abs(gl[:, 0] - 100)))
print(f"    published gapless at {gl[j100,0]:.0f} keV: {gl[j100,1]:.2e} -> {gl[j100,1]*EBG**2:.2e} cm^2")
print(f"(b) harmonic mean of the ZrTe5 tensor {EBG_HM:.2f}, square {EBG_HM**2:.0f}; on-axis squares "
      + ", ".join(f"{x**2:.3g}" for x in EBG_AX) + f"; isotropized 1708.08929: {EBG_ZR08**2:.0f}")
sel = ok & (m >= 20) & (m <= 1000)
f20 = np.interp(20.0, m[ok], fac[ok])
print(f"    anisotropic ZrTe5 recast factor, 20 keV - 1 MeV (grid points and the value interpolated at 20 keV): "
      f"{min(f20, fac[sel].min()):.0f} to {fac[sel].max():.0f}; ratio to the harmonic-mean square "
      f"{min(f20, fac[sel].min())/EBG_HM**2:.2f} to {fac[sel].max()/EBG_HM**2:.2f}")
print(f"    lowest mass on the grid {m[ok][0]:.2f} keV: factor {fac[ok][0]:.0f}; at 10.0 keV: {np.interp(10.0, m[ok], fac[ok]):.0f};"
      f" at 15 keV: {np.interp(15.0, m[ok], fac[ok]):.0f}")
for mm in (20, 50, 100, 300, 1000):
    print(f"    m = {mm:5d} keV: factor {np.interp(mm, m[ok], fac[ok]):.0f}")

plt.rcParams.update({"font.size": 8.5})
fig, (a, b) = plt.subplots(1, 2, figsize=(7.0, 3.1))
a.loglog(gp[:, 0], gp[:, 1], color="0.5", lw=1.3, label="published, gapped")
a.loglog(gl[:, 0], gl[:, 1], color="0.5", lw=1.3, ls="--", label="published, gapless")
a.loglog(gp[:, 0], gp[:, 1] * EBG**2, color="k", lw=1.6, label=r"$\times\,\varepsilon_{\mathrm{bg}}^2 = 1600$, gapped")
a.loglog(gl[:, 0], gl[:, 1] * EBG**2, color="k", lw=1.6, ls="--", label=r"$\times\,1600$, gapless")
a.set_xlabel(r"$m_\chi$ (keV)")
a.set_ylabel(r"$\bar\sigma_e^{\mathrm{lim}}$ (cm$^2$)")
a.set_xlim(2, 1000)
a.set_ylim(1e-48, 1e-37)
a.legend(frameon=False, fontsize=7, loc="upper left")
a.text(0.97, 0.04, "(a)", transform=a.transAxes, ha="right")

b.loglog(m[ok], fac[ok], color="k", lw=1.6, label=r"ZrTe$_5$, anisotropic $\varepsilon_{\mathrm{bg}}$")
b.axhline(EBG**2, color="C0", lw=1.5, label=r"ideal material, $40^2$")
b.axhline(EBG_ZR08**2, color="C3", lw=1.2, label=r"ZrTe$_5$ isotropized, $25.34^2$")
b.axhline(EBG_HM**2, color="0.45", lw=1.0, ls="--", label=r"harmonic mean squared, $50.5^2$")
for x in EBG_AX:
    b.axhline(x**2, color="0.6", lw=0.8, ls=":")
b.text(1.05e3, EBG_AX[1]**2 * 0.72, r"$\varepsilon_{yy}^2$", fontsize=7, ha="right", color="0.4")
b.text(1.05e3, EBG_AX[2]**2 * 1.15, r"$\varepsilon_{zz}^2$", fontsize=7, ha="right", color="0.4")
b.text(1.05e3, EBG_AX[0]**2 * 0.6, r"$\varepsilon_{xx}^2$", fontsize=7, ha="right", color="0.4")
b.set_xlabel(r"$m_\chi$ (keV)")
b.set_ylabel(r"recast factor $\bar\sigma_e^{\mathrm{lim}}/\bar\sigma_{e,\mathrm{pub}}^{\mathrm{lim}}$")
b.set_xlim(7, 1100)
b.set_ylim(2e2, 3e6)
b.legend(frameon=False, fontsize=7, loc="upper left", ncol=1)
b.text(0.03, 0.04, "(b)", transform=b.transAxes, ha="left")
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT)
print("wrote", os.path.relpath(OUT, HERE))
