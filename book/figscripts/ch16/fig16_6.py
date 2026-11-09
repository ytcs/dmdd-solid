"""Fig. 16.6 (fig:16-lif): the F-center creation threshold in LiF.

(a) Lightest dark-matter mass that can create an F center, against the threshold energy E_th of the step:
    fluorine recoil displacing itself, m_min from E_R^max(m, M_F) = E_th (eq. 1.3-ERmax, v_max = 2.650e-3);
    lithium recoil that displaces a fluorine neighbor, needing E_R >= E_th / f_LiF with the head-on transfer fraction
    f_LiF = 4 M_Li M_F / (M_Li + M_F)^2 (kinematic upper bound on the energy one collision passes on);
    electronic route (exciton -> F-H pair): m_min = 2 E / v_max^2 at E = 14.2 eV, the band gap of LiF, an upper bound on the
    exciton-route threshold, which opens at the free-exciton energy below the gap (no open source read for its value); gap
    from Guerrero Perez et al. 2025, quoting Piacentini et al. 1976.
    Marked: E_d = 27 eV, the threshold of the TRIM runs of Cogswell et al. 2021 (Table I).
(b) Displacements made by a fluorine recoil, Kinchin-Pease count with the Lindhard damage energy (cc16_6.lindhard,
    Z = 9, A = 19, single-element form; an extrapolation below about 1 keV) and, dashed, with no electronic loss (T_d = E_R), E_d = 27 eV; arrows: recoil endpoints E_R^max for m_chi = 0.2, 0.5, 1 GeV.
Run: python fig16_6.py > fig16_6.log
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import cc16_6 as C

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch16")
F_LIF = 4 * C.M_LI * C.M_F / (C.M_LI + C.M_F)**2

E = np.geomspace(5, 100, 300)
mF = C.m_threshold(E, C.M_F)
mLi = C.m_threshold(E / F_LIF, C.M_LI)
m_el = 2 * C.GAP_LIF / C.VMAX**2

print("head-on transfer fraction Li -> F: %.4f" % F_LIF)
for Et in (10.0, 27.0, 50.0):
    print("E_th = %4.0f eV: m_min(F recoil) = %.4f GeV, m_min(Li recoil -> F) = %.4f GeV, Li own displacement at E_th: %.4f GeV"
          % (Et, C.m_threshold(Et, C.M_F) / 1e9, C.m_threshold(Et / F_LIF, C.M_LI) / 1e9, C.m_threshold(Et, C.M_LI) / 1e9))
print("electronic route at the gap %.1f eV: m_min = 2E/v_max^2 = %.3f MeV" % (C.GAP_LIF, m_el / 1e6))
print("F band %.1f eV: m_min to excite an existing center = %.3f MeV" % (C.FBAND_LIF, 2 * C.FBAND_LIF / C.VMAX**2 / 1e6))

ER = np.geomspace(10, 1e4, 600)
y, Td, k, eps, g = C.lindhard(ER, 9, 19)
Nd = C.kinchin_pease(Td, C.E_D_LIF)
y1, T1, k1, e1, g1 = C.lindhard(np.array([1000.0]), 9, 19)
print("Lindhard F in LiF at 1 keV: k = %.4f, eps = %.4f, g = %.4f, y_L = %.4f, T_d = %.1f eV, KP count = %.2f"
      % (k1, e1[0], g1[0], y1[0], T1[0], T1[0] / (2 * C.E_D_LIF)))
marks = {}
for m in (0.2e9, 0.5e9, 1.0e9):
    em = C.er_max(m, C.M_F)
    ym, Tm, *_ = C.lindhard(np.array([em]), 9, 19)
    marks[m] = em
    print("m = %.1f GeV: E_R^max(F) = %.1f eV, y_L = %.3f, T_d = %.1f eV, KP count = %.2f"
          % (m / 1e9, em, ym[0], Tm[0], float(C.kinchin_pease(Tm, C.E_D_LIF)[0])))
# energy at which T_d reaches E_d and 2 E_d
from scipy.optimize import brentq
for mult in (1, 2):
    e0 = brentq(lambda e: float(C.lindhard(np.array([e]), 9, 19)[1][0]) - mult * C.E_D_LIF, 1, 1e4)
    print("T_d = %d E_d at E_R = %.1f eV" % (mult, e0))
print("KP count with T_d = E_R at 1 keV: %.2f; at 187.7 eV: %.2f" % (1000 / (2 * C.E_D_LIF), 187.7 / (2 * C.E_D_LIF)))

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.9))
a1.loglog(E, mF / 1e9, color="C3", lw=1.5, label="F recoil")
a1.loglog(E, mLi / 1e9, color="C0", lw=1.5, label=r"Li recoil $\to$ F")
a1.axhline(m_el / 1e9, color="C2", lw=1.2, ls="--", label="exciton route, upper bound (gap)")
a1.axvline(C.E_D_LIF, color="0.5", lw=0.8, ls=":")
a1.text(C.E_D_LIF * 1.05, 0.55, r"$E_{\mathrm{d}} = 27$ eV", fontsize=7, color="0.3")
a1.set_xlabel(r"threshold energy $E_{\mathrm{th}}$ (eV)")
a1.set_ylabel(r"lightest $m_\chi$ (GeV)")
a1.set_ylim(1e-3, 1.0)
a1.set_title("(a) mass threshold", fontsize=9)
a1.legend(fontsize=7, frameon=False, loc="center left", bbox_to_anchor=(0.0, 0.42))
a2.semilogx(ER, Nd, color="C3", lw=1.5, label="Lindhard damage energy")
a2.semilogx(ER, C.kinchin_pease(ER, C.E_D_LIF), color="k", lw=1.0, ls="--", label=r"$T_{\mathrm{d}} = E_R$")
a2.legend(fontsize=7, frameon=False, loc="center left")
for m, em in marks.items():
    a2.annotate("%.1f GeV" % (m / 1e9), xy=(em, 0.0), xytext=(em, 11.0) if m < 0.9e9 else (em, 4.5), fontsize=7, ha="center",
                arrowprops=dict(arrowstyle="->", lw=0.7))
a2.set_xlabel(r"fluorine recoil energy $E_R$ (eV)")
a2.set_ylabel("displaced atoms")
a2.set_ylim(0, 12.5)
a2.set_xlim(10, 1e3)
a2.set_title("(b) Kinchin–Pease count", fontsize=9)
fig.tight_layout()
out = os.path.join(FIG, "fig16_6.pdf")
fig.savefig(out)
print("wrote", out)
