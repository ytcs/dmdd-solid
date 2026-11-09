"""Fig. 16.1 (fig:16-zrte5): ZrTe5 reach as published and corrected.  Reads zrte5_16.npz (run zrte5_16.py first).
(a) Scattering through a light mediator, 3 events in 1 kg yr:
    gray solid   Geilhufe et al., arXiv:1910.02091, ZrTe5 'th.' curve (digitized from the arXiv vector figure);
    gray dashed  the published rule (their Eq. (3.14), q_x^2 v_x^2) recomputed for their implemented row (Delta_D =
                 15.6 meV) with the book's halo, orientation average; gray dotted: the same with (v0, v_E, v_esc) =
                 (220, 232, 600) km/s (the source states no halo);
    black solid  the target with the background in the total epsilon and the central half-gap Delta_D = 11.8 meV;
    black dotted the isotropic model of Sect. 7.3 WE (geometric-mean v_D, harmonic-mean eps_bg) with the total epsilon;
    red solid    Hochberg et al., arXiv:1708.08929, ZrTe5 'th.' (digitized, Fig. 4), isotropised with eps_bg = 25.34;
    red dashed   that curve times 25.34^2 = 642 (exact for their isotropic model).
(b) Absorption of dark-photon dark matter, 3 events in 1 kg yr, rho_T = 6.135 g/cm^3 (their value):
    gray solid   1910.02091 ZrTe5 'th.' (digitized); gray dashed: their rule recomputed with Delta_D = 15.6 meV
                 (agrees to 0.5 %);
    black solid  total epsilon per polarization, unpolarized average, Delta_D = 11.8 meV.
Run: python fig16_1.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch16", "fig16_1.pdf")
z = np.load(os.path.join(HERE, "zrte5_16.npz"))
m = z["masses"] / 1e3
ok = np.isfinite(z["book"]) & (z["book"] < 1e-30)

fig, (a, b) = plt.subplots(1, 2, figsize=(7.2, 3.3))
a.loglog(z["p10"][:, 0], z["p10"][:, 1], color="0.55", lw=1.4, label="published (Geilhufe et al.)")
mP = z["massesP"] / 1e3
okP = np.isfinite(z["srcP"]) & (z["srcP"] < 1e-30)
a.loglog(mP[okP], z["srcP"][okP] * 6.089 / 6.135, color="0.55", lw=1.0, ls="--", label="published rule, recomputed")
okH = np.isfinite(z["srcP_halo"]) & (z["srcP_halo"] < 1e-30)
a.loglog(mP[okH], z["srcP_halo"][okH] * 6.089 / 6.135, color="0.55", lw=1.0, ls=":", label="the same, other halo")
a.loglog(m[ok], z["book"][ok], color="k", lw=1.6, label="total $\\varepsilon$")
a.loglog(m[ok], z["iso"][ok], color="k", lw=1.0, ls=":", label="total $\\varepsilon$, isotropic model")
a.loglog(z["p08"][:, 0], z["p08"][:, 1], color="C3", lw=1.2, label="published (Hochberg et al.)")
a.loglog(z["p08"][:, 0], z["p08"][:, 1] * float(z["ebg08"]) ** 2, color="C3", lw=1.0, ls="--",
         label="the same $\\times\\,642$")
a.set_xlim(6, 1000)
a.set_ylim(1e-45, 1e-31)
a.set_xlabel("$m_\\chi$ (keV)")
a.set_ylabel("$\\bar\\sigma_e^{\\mathrm{lim}}$ (cm$^2$)")
a.set_title("(a) scattering, light mediator", fontsize=8.5, loc="left")
a.legend(fontsize=6.8, loc="upper right", frameon=False)

ma = z["ma"] * 1e3
pa = z["pa"]
b.loglog(pa[:, 0] * 1e3, pa[:, 1], color="0.65", lw=2.4, label="published (Geilhufe et al.)")
b.loglog(z["maP"] * 1e3, z["zsP"], color="0.3", lw=0.9, ls="--", label="published rule, recomputed")
b.loglog(ma, z["zb"], color="k", lw=1.6, label="total $\\varepsilon$")
b.set_xlim(20, 400)
b.set_ylim(1e-17, 1e-14)
b.set_xlabel("$m_\\phi$ (meV)")
b.set_ylabel("$\\zeta^{\\mathrm{lim}}$")
b.set_title("(b) dark-photon absorption", fontsize=8.5, loc="left")
from matplotlib.ticker import FixedLocator, NullFormatter, FixedFormatter
b.xaxis.set_major_locator(FixedLocator([20, 30, 50, 100, 200, 300]))
b.xaxis.set_major_formatter(FixedFormatter(["20", "30", "50", "100", "200", "300"]))
b.xaxis.set_minor_formatter(NullFormatter())
b.legend(fontsize=6.8, loc="lower center", frameon=False)
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT)
print("wrote", os.path.relpath(OUT, HERE))
