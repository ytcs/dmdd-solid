"""Limit Check 17.5a (lim:17.5a, fig:17-limit-a): the partial (valence) f-sum of silicon.
Log: limit17_5a.log.  Run: python limit17_5a.py > limit17_5a.log  (seconds).

Formula tested: int_0^{omega_c} omega L(omega) d omega = (pi/2) (omega_p^val)^2 for an upper limit omega_c between the valence
spectrum and the first core edge, with omega_p^val = 16.6 eV (valence density 2.00e23 cm^-3, Sect. 4.3 and Worked example 4.10;
measured plasmon energy 16.6 +- 0.1 eV, Ramanathan and Kurinsky, arXiv:2004.10709, Table I).  The fuller result is the running
integral of the measured q -> 0 loss function, with the core background of the derivation in the text:
  int_0^{omega_c} omega L = (pi/2) (omega_p^val)^2 / eps_core^2,  eps_core = 1 + chi_core(0),
  chi_core(0) = (2/pi) int_{core} eps_2(omega)/omega d omega  (Kramers-Kronig at omega = 0 for the core part).

Data (both as used in Sects. 4.3, 4.4 and 10.7):
  0 - 35 eV: optical constants of float-zone silicon at 300 K, Franta et al., Appl. Surf. Sci. 421, 405 (2017) (refractiveindex.info
     file Franta-300K.yml, copy in book/sources/4.4/si_franta_300K.yml; columns wavelength (um), n, k; eps = (n + i k)^2).
  35 eV - 30 keV: Henke, Gullikson and Davis, At. Data Nucl. Data Tables 54, 181 (1993), CXRO table si.nff (copy in
     book/sources/4.3/si_henke.nff; columns E, f1, f2 per atom).  eps = 1 - (omega_a^2/omega^2)(f1 - i f2),
     omega_a^2 = e^2 n_at/m_e, n_at = 5.00e22 cm^-3 (8 atoms per (5.431 A)^3).  This is the standard first-order relation
     n = 1 - delta - i beta with delta, beta = r_e lambda^2 n_at (f1, f2)/(2 pi), eps = 1 - 2 delta - 2 i beta.
  Modelling choices: the join at 35 eV (the two data sets differ there by the amount printed below); the L-edge position 99.8 eV
  (step of f2 in the Henke table); the core spectrum for chi_core(0) is eps_2 of the Henke table above 99.8 eV, minus the valence
  tail continued from 60-99 eV as a power law (printed: both with and without the subtraction).
Validity region shaded: omega_c below the L edge where the running L-sum lies within 10 % of the formula.
"""
import os
import numpy as np
from scipy.integrate import cumulative_trapezoid, trapezoid
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(BOOK, "tex", "figures", "ch17")
os.makedirs(OUT, exist_ok=True)

ME = 510998.95
E2 = 4 * np.pi / 137.035999
HBARC_CM = 1.973269804e-5
HC_EV_UM = 1.23984198

def wp2(n_cm3):
    return E2 * n_cm3 * HBARC_CM**3 / ME

WPV = 16.6
SUM0 = np.pi / 2 * WPV**2
print("omega_p^val from n = 2.00e23: %.3f eV; (pi/2)(16.6 eV)^2 = %.1f eV^2" % (np.sqrt(wp2(2.00e23)), SUM0))
NAT = 8 / (5.431e-8)**3
WA2 = wp2(NAT)
print("n_at = %.4e cm^-3, omega_a^2 = %.3f eV^2, 14 omega_a^2 = (%.2f eV)^2" % (NAT, WA2, np.sqrt(14 * WA2)))

# Franta
lam, n, k = [], [], []
inside = False
for line in open(os.path.join(BOOK, "sources", "4.4", "si_franta_300K.yml")):
    s = line.strip()
    if s.startswith("data: |"):
        inside = True
        continue
    if inside:
        p = s.split()
        if len(p) == 3:
            try:
                lam.append(float(p[0])); n.append(float(p[1])); k.append(float(p[2]))
            except ValueError:
                inside = False
        elif s and not s[0].isdigit():
            inside = False
lam, n, k = map(np.array, (lam, n, k))
wf = HC_EV_UM / lam
o = np.argsort(wf)
wf, n, k = wf[o], n[o], k[o]
epsf = (n + 1j * k)**2
Lf = epsf.imag / np.abs(epsf)**2
print("Franta: %d points, %.3g - %.2f eV" % (len(wf), wf.min(), wf.max()))

# Henke
d = np.loadtxt(os.path.join(BOOK, "sources", "4.3", "si_henke.nff"), skiprows=1)
wh, f1, f2 = d[:, 0], d[:, 1], d[:, 2]
selh = f1 > -9000
wh, f1, f2 = wh[selh], f1[selh], f2[selh]
epsh = 1 - WA2 / wh**2 * (f1 - 1j * f2)
Lh = epsh.imag / np.abs(epsh)**2

WJ = 35.0
for wj in (30.0, 35.0, 40.0):
    print("  at %.0f eV: L Franta %.4f, Henke %.4f; eps2 Franta %.4f, Henke %.4f" % (
        wj, np.interp(wj, wf, Lf), np.interp(wj, wh, Lh), np.interp(wj, wf, epsf.imag), np.interp(wj, wh, epsh.imag)))

w = np.concatenate([wf[wf <= WJ], wh[wh > WJ]])
L = np.concatenate([Lf[wf <= WJ], Lh[wh > WJ]])
e2 = np.concatenate([epsf.imag[wf <= WJ], epsh.imag[wh > WJ]])
SL = cumulative_trapezoid(w * L, w, initial=0) / SUM0
SE = cumulative_trapezoid(w * e2, w, initial=0) / SUM0

EL = 99.8
def at(x, arr):
    return np.interp(x, w, arr)
for x in (10, 16.6, 20, 30, 40, 60, 80, 99.0, 150, 300, 1000, 1839, 5000, 30000):
    print("  running sums at %7.1f eV: L %.4f  eps2 %.4f" % (x, at(x, SL), at(x, SE)))
print("  all-electron asymptote 14/4 = 3.5; running L-sum at 30 keV = %.3f" % SL[-1])

# core background chi_core(0)
selc = wh > EL
# valence tail: power-law fit of eps2 (Henke) on 60-99 eV, continued above the edge
selt = (wh > 60) & (wh < 99)
pfit = np.polyfit(np.log(wh[selt]), np.log(epsh.imag[selt]), 1)
tail = np.exp(np.polyval(pfit, np.log(wh)))
print("  valence-tail power law eps2 ~ omega^%.2f on 60-99 eV" % pfit[0])
chi_all = 2 / np.pi * trapezoid(epsh.imag[selc] / wh[selc], wh[selc])
chi_core = 2 / np.pi * trapezoid((epsh.imag[selc] - tail[selc]) / wh[selc], wh[selc])
for lab, chi in (("eps2 above the L edge", chi_all), ("minus the continued valence tail", chi_core)):
    print("  chi_core(0) from %s: %.4f -> 1/eps_core^2 = %.4f" % (lab, chi, 1 / (1 + chi)**2))
fac = 1 / (1 + chi_core)**2

# validity: below the edge, within 10 % of the formula
sel = (w < EL) & (np.abs(SL - 1) < 0.1)
wv = w[sel]
lo = wv.min() if len(wv) else np.nan
# first crossing of 0.9 from below
idx = np.where((SL[:-1] < 0.9) & (SL[1:] >= 0.9))[0]
w09 = w[idx[0]] + (0.9 - SL[idx[0]]) * (w[idx[0] + 1] - w[idx[0]]) / (SL[idx[0] + 1] - SL[idx[0]])
print("  running L-sum reaches 0.9 at %.1f eV = %.2f omega_p^val; valid region %.1f - %.1f eV" % (w09, w09 / WPV, w09, EL))
print("  L-sum just below the edge (99 eV) / (1/eps_core^2) = %.4f" % (at(99.0, SL) / fac))

for wj in (30.0, 40.0):
    ww = np.concatenate([wf[wf <= wj], wh[wh > wj]])
    LL = np.concatenate([Lf[wf <= wj], Lh[wh > wj]])
    EE = np.concatenate([epsf.imag[wf <= wj], epsh.imag[wh > wj]])
    sl = cumulative_trapezoid(ww * LL, ww, initial=0) / SUM0
    se = cumulative_trapezoid(ww * EE, ww, initial=0) / SUM0
    print("  join at %.0f eV: L-sum at 99 eV %.4f, eps2-sum %.4f, L-sum at 30 keV %.4f" % (wj, np.interp(99, ww, sl), np.interp(99, ww, se), sl[-1]))

fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.axvspan(w09, EL, color="0.88", lw=0)
ax.plot(w, SL, color="C0", lw=1.6, label=r"$\int_0^{\omega_c}\omega L\,\mathrm{d}\omega$ (measured)")
ax.plot(w, SE, color="C1", lw=1.0, ls="-.", label=r"$\int_0^{\omega_c}\omega\varepsilon_2\,\mathrm{d}\omega$ (measured)")
ax.axhline(1.0, color="k", ls="--", lw=1.0, label=r"$(\pi/2)(\omega_p^{\mathrm{val}})^2$")
ax.axhline(fac, color="C0", ls=":", lw=1.2, label=r"$(\pi/2)(\omega_p^{\mathrm{val}})^2/\varepsilon_{\mathrm{core}}^2$")
ax.axhline(3.5, color="0.4", ls=(0, (1, 3)), lw=0.9)
ax.text(1.2e4, 3.25, "14 electrons", fontsize=8, color="0.3", ha="center")
for x, lab in ((EL, "L"), (1839, "K")):
    ax.axvline(x, color="0.5", lw=0.6, ls=":")
    ax.text(x * 1.06, 0.12, lab, fontsize=8, color="0.3")
ax.axvline(WPV, color="0.5", lw=0.6, ls="-")
ax.text(WPV * 1.05, 2.7, r"$\omega_p^{\mathrm{val}}$", fontsize=8, color="0.3")
ax.set_xscale("log")
ax.set_xlim(3, 3e4)
ax.set_ylim(0, 3.8)
ax.set_xlabel(r"upper limit $\omega_c$ (eV)")
ax.set_ylabel(r"running sum / $(\pi/2)(\omega_p^{\mathrm{val}})^2$")
lg = ax.legend(fontsize=7.5, loc="upper right", bbox_to_anchor=(1.0, 0.8), frameon=True, framealpha=1.0, facecolor="white", edgecolor="none")
lg.set_zorder(5)   # opaque: the K-edge line passes behind it
fig.tight_layout()
fig.savefig(os.path.join(OUT, "limit17_5a.pdf"))
print("wrote limit17_5a.pdf")
VMAX = 794.5 / 299792.458
print("largest deposit below the L edge: (1/2) m v_max^2 < 99.8 eV for m < %.2f MeV" % (2 * EL / VMAX**2 / 1e6))
for nm, zv, A in (("Si", 4, 28.0855), ("Ge", 4, 72.63), ("diamond", 4, 12.011), ("LiF", 8, 6.94 + 18.998)):
    print("  valence electrons per nucleon Z_val/A_cell %-8s %.4f" % (nm, zv / A))
