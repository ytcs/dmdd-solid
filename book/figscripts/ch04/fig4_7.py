"""Fig. 4.7 of Sect. 4.6 (RPA, local fields and TDDFT kernels), Worked example 4.11, and every number quoted in
Sect. 4.6.  Reads fig4_7_data.npz, written by fig4_7_data.py (the model calculation; its docstring documents the model,
the kernels and the numerical parameters).  Run fig4_7_data.py first (NK=20 for the published figure, about 25 min on
one core), then this script.

Output: tex/figures/ch04/fig4_7.pdf
  (a) eps_2 of silicon at q -> 0: independent particles (identical to the RPA without local fields), RPA with local
      fields, adiabatic LDA, and the measured spectrum.
  (b) loss function L = Im(-1/eps_mac) at q -> 0, log scale: RPA without and with local fields, adiabatic LDA,
      measured; and the unscreened eps_2 of independent particles for comparison.

Inputs and their sources
  Model spectra: fig4_7_data.npz (Cohen-Bergstresser empirical pseudopotential, Phys. Rev. 141, 789 (1966)).
  Measured optical constants of crystalline silicon at 300 K: Franta et al., Appl. Surf. Sci. 421, 405 (2017),
     file Franta-300K.yml of the refractiveindex.info database (CC0), copy in book/sources/4.4/si_franta_300K.yml,
     read as in fig4_5.py; eps = (n + i k)^2; optical (transverse) data equal the longitudinal ones at q -> 0.
  Book values: eps_inf = 11.7 (Franta 2017; NOTATION editor ruling); PBE density-functional-perturbation value 13.04
     (Sect. 3.4, App. E.1); silicon valence density 2.00e23 cm^-3, r_s = 2.0, k_F = 3.57 keV, k_TF = 4.12 keV,
     q_0 = alpha m_e = 3.73 keV, Lindhard eps(q_0, 0) = 2.10 (Sects. 4.4, 4.5).
  Electron-gas exchange-correlation: Slater exchange and Perdew-Zunger correlation (as in fig4_7_data.py).
Modelling choices
  The model spectra carry a Lorentzian broadening of 0.10 eV; the measured spectrum is at 300 K.  No scissor shift:
  the empirical bands already have the measured transition energies.  The ALDA kernel is evaluated on the model's
  pseudo valence density.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(BOOK, "tex", "figures", "ch04")


def close(a, b, rtol=5e-3, name=""):
    assert abs(a - b) <= rtol * abs(b), f"{name}: {a} vs {b}"
    print(f"  {name:62s} {a:.6g}   (quoted {b})")


d = np.load(os.path.join(HERE, "fig4_7_data.npz"))
w = d["w"]
E = {k: d["eps_" + k].astype(complex) for k in ("ip", "rpa", "alda")}
print(f"model: NK = {int(d['NK'])}^3, NG = {int(d['NG'])} (check {int(d['NGc'])}), eta = {float(d['eta']):.2f} eV")

# ------------------------------------------------------------------ measured data
rows = []
for line in open(os.path.join(BOOK, "sources", "4.4", "si_franta_300K.yml")):
    p = line.split()
    if len(p) == 3:
        try:
            rows.append([float(x) for x in p])
        except ValueError:
            pass
lam, n, k = np.array(rows).T
wx = 1.239841984 / lam
o = np.argsort(wx)
wx, epsx = wx[o], ((n + 1j * k) ** 2)[o]
Lx = epsx.imag / np.abs(epsx) ** 2


def peaks(x, y, lo, hi):
    m = (x > lo) & (x < hi)
    i = np.argmax(y[m])
    return x[m][i], y[m][i]


print("Measured spectrum (Franta 2017, 300 K)")
close(epsx.real[0], 11.7, 2e-3, "eps_1 at 4 meV")
xE1, yE1 = peaks(wx, epsx.imag, 3.0, 3.8)
xE2, yE2 = peaks(wx, epsx.imag, 3.8, 5.0)
close(xE1, 3.42, 3e-3, "E1 peak position [eV]")
close(xE2, 4.24, 3e-3, "E2 peak position [eV]")
print(f"  measured heights: E1 {yE1:.2f}, E2 {yE2:.2f}")

print("Model spectra")
res = {}
for kk in ("ip", "rpa", "alda"):
    e2 = E[kk].imag
    x2, y2 = peaks(w, e2, 3.8, 5.0)
    x1, y1 = peaks(w, e2, 3.0, 3.8)
    il = np.argmax((-1 / E[kk]).imag)
    res[kk] = dict(eps0=E[kk][0].real, E2=(x2, y2), E1=(x1, y1), Lpk=(w[il], (-1 / E[kk]).imag[il]))
    print(f"  {kk:5s} eps(0) {E[kk][0].real:.3f}  E2 peak {x2:.2f} eV height {y2:.2f}  "
          f"value at 3.42 eV {np.interp(3.42, w, e2):.2f}  loss peak {w[il]:.2f} eV height {(-1 / E[kk]).imag[il]:.2f}")
ip = E["ip"]
wp2 = 4 * np.pi * 8 / float(d["Omega"]) * (2 * 13.605693122994) ** 2
fs = np.trapezoid(w * ip.imag, w) / (np.pi / 2 * wp2)
kk_ = 1 + 2 / np.pi * np.trapezoid(ip.imag[1:] / w[1:], w[1:])
print(f"  f-sum fraction of IP eps_2 below 30 eV {fs:.3f}; all included bands {float(d['fsum_full']):.3f}")
print(f"  Kramers-Kronig eps_1(0) of IP {kk_:.3f} vs direct {ip[0].real:.3f}")
assert abs(kk_ - ip[0].real) < 0.02 * ip[0].real
for kk in ("rpa", "alda"):   # f-sum with local fields (App. D.7)
    print(f"  f-sum fraction below 30 eV, {kk}: {np.trapezoid(w * E[kk].imag, w) / (np.pi / 2 * wp2):.3f}")
st59, st113 = d["st59"], d["st113"]
print(f"  static eps_mac (59 G): IP {st59[0]:.3f}, RPA+LF {st59[1]:.3f}, ALDA {st59[2]:.3f}")
print(f"  static eps_mac (113 G): IP {st113[0]:.3f}, RPA+LF {st113[1]:.3f}, ALDA {st113[2]:.3f}")
print(f"  LF reduction {1 - st113[1] / st113[0]:.3f}; ALDA increase over RPA+LF {st113[2] / st113[1] - 1:.3f}")
print(f"  ratio of screening factors (IP/RPA+LF)^2 = {(st113[0] / st113[1]) ** 2:.3f}")
print(f"  min transition energy on the grid {float(d['Emin']):.3f} eV; density range {float(d['nmin']):.4f}-"
      f"{float(d['nmax']):.4f} bohr^-3")

print("Numbers quoted in Sect. 4.6 and Worked example 4.11")
close(yE1, 36, 1e-2, "measured E1 height");  close(yE2, 46, 1e-2, "measured E2 height")
close(res["ip"]["E2"][0], 4.26, 3e-3, "IP E2 position [eV]"); close(res["ip"]["E2"][1], 41, 1.5e-2, "IP E2 height")
close(np.interp(3.42, w, E["ip"].imag), 15, 3e-2, "IP eps_2 at 3.42 eV")
close(res["rpa"]["E2"][0], 4.32, 3e-3, "RPA+LF E2 position [eV]"); close(res["rpa"]["E2"][1], 34, 1.5e-2, "RPA+LF E2 height")
close(np.interp(3.42, w, E["rpa"].imag), 13, 3e-2, "RPA+LF eps_2 at 3.42 eV")
close(res["alda"]["E2"][1], 37, 1.5e-2, "ALDA E2 height")
close(st59[0], 11.45, 1e-3, "eps_inf IP"); close(st59[1], 10.22, 1e-3, "eps_inf RPA+LF (59 G)")
close(st113[1], 10.22, 1e-3, "eps_inf RPA+LF (113 G)"); close(st59[2], 10.81, 1e-3, "eps_inf ALDA (59 G)")
close(1 - st59[1] / st59[0], 0.11, 3e-2, "local-field reduction"); close(st59[2] / st59[1] - 1, 0.06, 5e-2, "ALDA increase")
close((st59[2] - st59[1]) / (st59[0] - st59[1]), 0.5, 5e-2, "fraction of the LF reduction undone by ALDA")
close(1 - st59[0] / 11.7, 0.02, 0.1, "IP below measured"); close(1 - st59[2] / 11.7, 0.08, 0.06, "ALDA below measured")
close(13.04 / 11.7 - 1, 0.11, 0.05, "PBE above measured")
close((st59[0] / st59[1]) ** 2, 1.25, 5e-3, "screening-factor ratio")
close(res["ip"]["Lpk"][1], 7.6, 1e-2, "loss peak height, RPA no LF"); close(res["rpa"]["Lpk"][1], 3.4, 1e-2, "loss peak height, RPA+LF")
close(res["rpa"]["Lpk"][0] - 16.4, 2.0, 0.1, "model loss peak above measured [eV]")
for x in (3.0, 6.0, 12.0):
    r = np.interp(x, w, (-1 / E["rpa"]).imag) / np.interp(x, w, (-1 / E["ip"]).imag)
    assert 1.10 <= r <= 1.35, r
    print(f"  L(RPA+LF)/L(RPA, no LF) at {x} eV: {r:.3f}")
for x in (3.0, 4.0, 6.0):
    r = np.interp(x, w, E["ip"].imag) / np.interp(x, w, (-1 / E["ip"]).imag)
    assert 100 <= r <= 2000, r
    print(f"  eps_2/L at {x} eV: {r:.0f}")
# k-grid convergence record (static values, fig4_7_data.py with NK=8): IP 11.4585, RPA+LF 10.2315, ALDA 10.8183 (59 G)
for v8, v20 in zip((11.4585, 10.2315, 10.8183), st59):
    assert abs(v8 / v20 - 1) < 1e-3

# ------------------------------------------------------------------ electron gas at r_s = 2: ALDA local-field factor
print("Electron gas, r_s = 2.0: ALDA static local-field factor")


def exc(nn):
    rs = (3 / (4 * np.pi * nn)) ** (1 / 3)
    ex = -0.75 * (3 * nn / np.pi) ** (1 / 3)
    ec = -0.1423 / (1 + 1.0529 * np.sqrt(rs) + 0.3334 * rs)
    return ex + ec


rs = 2.0
nn = 3 / (4 * np.pi * rs**3)
kFa = (3 * np.pi**2 * nn) ** (1 / 3)
h = 1e-4
F = lambda x: x * exc(x)
fxc = (F(nn * (1 + h)) - 2 * F(nn) + F(nn * (1 - h))) / (nn * h) ** 2      # hartree bohr^3 (Gaussian, e = 1)
A_xc = -fxc * kFa**2 / (4 * np.pi)
close(-(np.pi / kFa**2) * kFa**2 / (4 * np.pi), -0.25, 1e-12, "exchange-only f_x = -e^2/4k_F^2 -> -A_x")
close(A_xc, 0.267, 3e-3, "ALDA coefficient A, G_LF = A q^2/k_F^2")
kTF2_kF2 = 4 / (np.pi * kFa)                      # k_TF^2/k_F^2 = 4/(pi k_F a_0) in atomic units
close(kTF2_kF2, 1.326, 2e-3, "k_TF^2/k_F^2 at r_s = 2")
kap = 1 / (1 - A_xc * kTF2_kF2)
close(kap, 1.55, 5e-3, "kappa/kappa_0 = 1/(1 - A k_TF^2/k_F^2)")
# static screening at q0 = alpha m_e = 3.73 keV, k_F = 3.57 keV (book values)
y = 3.73 / 3.57 / 2
FL = 0.5 + (1 - y * y) / (4 * y) * np.log(abs((1 + y) / (1 - y)))
X = kTF2_kF2 / (2 * y) ** 2 * FL
close(1 + X, 2.10, 5e-3, "Lindhard eps(q0, 0)")
GLF = A_xc * (2 * y) ** 2
close(GLF, 0.29, 1e-2, "ALDA G_LF(q0)")
eALDA = 1 + X / (1 - GLF * X)
close(eALDA, 2.62, 2e-3, "eps(q0, 0) with the ALDA local-field factor")

# ------------------------------------------------------------------ figure
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.85))
col = {"ip": "0.45", "rpa": "#1f5fa8", "alda": "#d0731b"}
m = wx <= 8
ax1.plot(wx[m], epsx.imag[m], "k-", lw=1.6, label="measured")
ax1.plot(w, E["ip"].imag, "--", color=col["ip"], lw=1.1, label="independent particles")
ax1.plot(w, E["rpa"].imag, "-", color=col["rpa"], lw=1.1, label="RPA + local fields")
ax1.plot(w, E["alda"].imag, "-.", color=col["alda"], lw=1.1, label="adiabatic LDA")
ax1.set_xlim(2, 8)
ax1.set_ylim(0, 62)
ax1.set_xlabel(r"$\omega$ (eV)")
ax1.set_ylabel(r"$\varepsilon_2$")
ax1.text(0.03, 0.95, "(a)", transform=ax1.transAxes, va="top")
ax1.legend(frameon=False, fontsize=7, loc="upper right", bbox_to_anchor=(1.0, 1.0))
# static limits of the three model approximations against the measured eps_inf = 11.7 (Li 1980 / Franta 2017, Sect. 4.4)
ax1.text(0.97, 0.62, "$\\varepsilon_\\infty$ of the model:\nIP %.2f, RPA+LF %.2f,\nadiabatic LDA %.2f;\nmeasured 11.7"
         % (st59[0], st59[1], st59[2]), transform=ax1.transAxes, fontsize=6, va="top", ha="right")

ax2.semilogy(wx, Lx, "k-", lw=1.6, label="measured")
ax2.semilogy(w, (-1 / E["rpa"]).imag, "-", color=col["rpa"], lw=1.1, label="RPA + local fields")
ax2.semilogy(w, (-1 / E["alda"]).imag, "-.", color=col["alda"], lw=1.1, label="adiabatic LDA")
ax2.semilogy(w, (-1 / E["ip"]).imag, ":", color=col["rpa"], lw=1.2, label="RPA, no local fields")
ax2.semilogy(w, E["ip"].imag, "--", color=col["ip"], lw=0.9, label=r"$\varepsilon_2$, unscreened")
# measured loss peak (16.4 eV, Sect. 4.4) and the dark-matter window: omega <= q v_max at q = 2pi/a = 2.28 keV
ax2.axvline(16.4, color="k", ls=":", lw=0.8)
ax2.text(16.6, 25, "16.4 eV", fontsize=6.5)
WDM = 2 * np.pi * 1973.269804 / 5.431 * 2.650e-3
ax2.axvspan(0, WDM, color="0.85", zorder=0, lw=0)
ax2.text(WDM - 0.8, 0.12, r"$\omega \leq qv_{\mathrm{max}}$, $q = 2\pi/a$", fontsize=6.5, rotation=90)   # between the curves
print(f"  dark-matter window shaded up to q v_max = {WDM:.2f} eV at q = 2pi/a")
ax2.set_xlim(0, 30)
ax2.set_ylim(1e-3, 60)
ax2.set_xlabel(r"$\omega$ (eV)")
ax2.set_ylabel(r"$L = \mathrm{Im}(-1/\varepsilon_{\mathrm{mac}})$")
ax2.text(0.03, 0.95, "(b)", transform=ax2.transAxes, va="top")
# styles shared with panel (a) are named in its legend; here only the two curves that (a) does not have
h, l = ax2.get_legend_handles_labels()
ax2.legend(h[3:], l[3:], frameon=False, fontsize=6.5, loc="lower right")   # right of the 16.4 eV line
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_7.pdf"))
print("wrote fig4_7.pdf")
