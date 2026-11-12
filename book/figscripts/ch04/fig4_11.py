"""Fig. 4.11 of Sect. 4.9 (excitons and the Bethe-Salpeter equation) and every number quoted in Sect. 4.9, including
Worked example 4.15 (the Wannier-Mott exciton of GaAs).  Reads fig4_11_data.npz, written by fig4_11_data.py (the model
calculation; its docstring documents the model, the kernels and the numerical parameters).

Output: tex/figures/ch04/fig4_11.pdf
  (a) eps_2 of silicon at q -> 0 from one transition-basis Hamiltonian: independent particles, RPA with local fields
      (exchange kernel only), Bethe-Salpeter (exchange and screened direct kernel), and the measured spectrum.
  (b) loss function L = Im(-1/eps_mac), log scale, same curves plus the RPA without local fields.

Inputs and their sources
  Model spectra: fig4_11_data.npz (Cohen-Bergstresser empirical pseudopotential, Phys. Rev. 141, 789 (1966); 12^3
     shifted grid, 4 valence + 3 conduction bands, Lorentzian broadening 0.15 eV, Tamm-Dancoff).
  Measured optical constants of crystalline silicon at 300 K: Franta et al., Appl. Surf. Sci. 421, 405 (2017),
     refractiveindex.info file Franta-300K.yml, read as in fig4_7.py; eps = (n + i k)^2.  Measured peaks E1 3.42 eV
     (height 36) and E2 4.24 eV (height 46), as asserted in fig4_7.py.
  Sect. 4.6 values (fig4_7_data.npz, 20^3 grid, 26 conduction bands, 0.10 eV): eps_inf IP 11.45, RPA+LF 10.22, ALDA 10.81.
  Wannier-Mott numbers: Rydberg alpha^2 m_e/2 = 13.6057 eV and a_0 = 0.529177 A (CODATA 2022);
     silicon: measured exciton binding 14.7 meV (Shaklee and Nahory, Phys. Rev. Lett. 24, 942 (1970)), eps_inf = 11.7
     (Franta 2017; book convention), a = 5.431 A, valley masses 0.916 / 0.191 and heavy-hole masses 0.277 [100] /
     0.718 [111] (Table 3.1), |G_111| = sqrt(3) 2 pi/a;
     GaAs: m* = 0.067, gamma_1 = 6.98 (Table 3.1, Vurgaftman et al. 2001), a = 5.653 A (room temperature, caption of
     fig:3-ge-gaas in Sect. 3.3), eps_inf = 10.88 (measured, Lockwood et al. 2005, lockwood2005optical, as in Sect. 5.5),
     eps_0 = 12.9 (Griffin et al., arXiv:1807.10291, Table I), optical phonons near 35 meV (same paper, Fig. 2), measured
     binding 4.2 meV (Sell, Phys. Rev. B 6, 3750 (1972)), gap 1.52 eV (Table 3.1).
Modelling choices: as in fig4_11_data.py; the hydrogenic estimate for silicon averages the inverse electron mass over
  directions, (1/3)(1/m_par + 2/m_perp), and brackets the hole mass by its [100] and [111] heavy-hole values.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(BOOK, "tex", "figures", "ch04")
RY = 13.605693122994
A0 = 0.529177210544
HBARC = 1973.269804   # eV A


def close(a, b, rtol=5e-3, name=""):
    assert abs(a - b) <= rtol * abs(b), f"{name}: {a} vs {b}"
    print(f"  {name:66s} {a:.6g}   (quoted {b})")


# ------------------------------------------------------------------ Wannier-Mott numbers (Sect. 4.9, WE 4.15)
print("Wannier-Mott: silicon")
mu = 14.7e-3 / RY * 11.7**2
ax = 11.7 * A0 / mu
close(mu, 0.148, 2e-3, "mu_x from 14.7 meV and eps_inf = 11.7 [m_e]")
close(ax / 10, 4.2, 5e-3, "a_x [nm]")
close(ax / 5.431, 7.7, 5e-3, "a_x / a ('nearly eight')")
close(1 / ax, 0.024, 2e-2, "1/a_x [1/A]")
G111 = np.sqrt(3) * 2 * np.pi / 5.431
close(G111, 2.0, 5e-3, "|G_111| [1/A]")
close((1 / ax) / G111, 0.012, 0.05, "1/a_x over |G_111| ('about one percent')")
mstar = 3 / (1 / 0.916 + 2 / 0.191)
close(mstar, 0.26, 5e-3, "direction-averaged electron mass")
lo = mstar * 0.277 / (mstar + 0.277) * RY / 11.7**2 * 1e3
hi = mstar * 0.718 / (mstar + 0.718) * RY / 11.7**2 * 1e3
close(lo, 13, 3e-2, "spherical estimate, heavy hole [100] [meV]")
close(hi, 19, 3e-2, "spherical estimate, heavy hole [111] [meV]")
assert lo < 14.7 < hi
close(14.7e-3 / 1.17, 0.013, 4e-2, "binding / gap ('1.3 percent')")
print("Wannier-Mott: GaAs (Worked example 4.15)")
inv = 1 / 0.067 + 6.98
close(inv, 21.9, 2e-3, "m_e/mu_x")
mu = 1 / inv
close(mu, 0.0457, 2e-3, "mu_x")
Einf = mu * RY / 10.88**2 * 1e3
close(Einf, 5.25, 2e-3, "E_x^b with eps_inf [meV]")
close(10.88 * A0 / mu / 10, 12.6, 3e-3, "a_x with eps_inf [nm]")
close(10.88 * A0 / mu / 5.653, 22, 2e-2, "a_x / a")
close(Einf / 4.2 - 1, 0.25, 0.1, "overbinding with eps_inf ('a quarter')")
close(35 / 4.2, 8, 0.05, "optical phonon / binding ('eight times')")
E0 = mu * RY / 12.9**2 * 1e3
close(E0, 3.73, 2e-3, "E_x^b with eps_0 [meV]")
close(12.9 * A0 / mu / 10, 15.0, 4e-3, "a_x with eps_0 [nm]")
close(4.2 - E0, 0.5, 0.1, "remaining difference [meV]")
close(RY, 13.61, 1e-3, "Rydberg [eV]")

# ------------------------------------------------------------------ model spectra
d = np.load(os.path.join(HERE, "fig4_11_data.npz"))
w = d["w"]
E = {k: d["eps_" + k] for k in ("ip", "lf", "bse", "kd", "lf_full")}
print(f"model: NK = {int(d['NK'])}^3, bands {int(d['NV'])}+{int(d['NCB'])}, eta = {float(d['eta']):.2f} eV")
for k in ("herm", "errip", "errdy", "tda"):
    print(f"  check {k}: {float(d[k]):.3g}")

rows = []
for line in open(os.path.join(BOOK, "figscripts", "data", "4.4", "si_franta_300K.yml")):
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


xE1, yE1 = peaks(wx, epsx.imag, 3.0, 3.8)
xE2, yE2 = peaks(wx, epsx.imag, 3.8, 5.0)
close(xE1, 3.42, 3e-3, "measured E1 [eV]"); close(yE1, 36, 1e-2, "measured E1 height")
close(xE2, 4.24, 3e-3, "measured E2 [eV]"); close(yE2, 46, 1e-2, "measured E2 height")
res = {}
for kk in ("ip", "lf", "lf_full", "bse", "kd"):
    e2 = E[kk].imag
    x2, y2 = peaks(w, e2, 3.8, 5.0)
    x1, y1 = peaks(w, e2, 2.8, 3.8)
    res[kk] = dict(E2=(x2, y2), E1=(x1, y1), at342=np.interp(3.42, w, e2))
    fs = np.trapezoid(w * e2, w)
    print(f"  {kk:8s} E2 {x2:.2f} eV / {y2:.1f}; max in 2.8-3.8 eV {x1:.2f} eV / {y1:.1f}; at 3.42 eV {res[kk]['at342']:.1f};"
          f"  int w eps2 (0-10 eV) {fs:.1f}")
st = {k: float(d["st_" + k]) for k in ("ip", "lf", "bse", "kd")}
print(f"  static (12-band basis): IP {st['ip']:.3f}  RPA+LF {st['lf']:.3f}  BSE {st['bse']:.3f}  K^d only {st['kd']:.3f}")
print(f"  ratios: LF/IP {st['lf'] / st['ip']:.4f}, BSE/LF {st['bse'] / st['lf']:.4f}, BSE/IP {st['bse'] / st['ip']:.4f}")
print(f"  model screening eps_inf (26 bands, Gamma grid): IP {float(d['epsip_model']):.3f}, RPA+LF {float(d['epsmac_model']):.3f}")
print(f"  K^d diagonal mean {float(d['Kd_mean']) * 1e3:.1f} meV, K^x diagonal mean {float(d['Kx_mean']) * 1e3:.2f} meV")
for x in (2.0, 3.0, 4.0, 5.0, 6.0):
    Ls = {kk: np.interp(x, w, (-1 / E[kk]).imag) for kk in ("ip", "lf", "bse")}
    print(f"  L at {x} eV: RPA {Ls['ip']:.4f}, RPA+LF {Ls['lf']:.4f}, BSE {Ls['bse']:.4f}; BSE/LF {Ls['bse'] / Ls['lf']:.2f};"
          f" measured {np.interp(x, wx, Lx):.4f}")

print("Numbers quoted in Sect. 4.9")


def pk(kk, lo, hi):
    return peaks(w, E[kk].imag, lo, hi)


close(np.interp(3.42, w, E["ip"].imag), 15, 2e-2, "IP eps_2 at 3.42 eV")
close(np.interp(3.42, w, E["lf"].imag), 13, 4e-2, "RPA+LF eps_2 at 3.42 eV")
close(pk("bse", 3.0, 3.6)[0], 3.36, 3e-3, "BSE lower peak position [eV]")
close(pk("bse", 3.0, 3.6)[1], 34, 1.5e-2, "BSE lower peak height")
close(pk("ip", 3.6, 4.6)[0], 4.24, 3e-3, "IP upper peak position [eV]")
close(pk("ip", 3.6, 4.6)[1], 38, 1.5e-2, "IP upper peak height")
close(pk("lf", 3.6, 4.6)[0], 4.29, 3e-3, "RPA+LF upper peak position [eV]")
close(pk("lf", 3.6, 4.6)[1], 32, 1.5e-2, "RPA+LF upper peak height")
close(pk("bse", 3.6, 4.6)[0], 3.88, 3e-3, "BSE upper peak position [eV]")
close(pk("bse", 3.6, 4.6)[1], 40, 1.5e-2, "BSE upper peak height")
close(4.24 - pk("bse", 3.6, 4.6)[0], 0.36, 3e-2, "BSE upper peak below measured [eV]")
close(st["bse"] / st["lf"] - 1, 0.17, 2e-2, "BSE raises eps_inf over RPA+LF (same basis)")
close(1 - st["lf"] / st["ip"], 0.055, 2e-2, "LF lowers eps_inf (same basis)")
close(10.22 * st["bse"] / st["lf"], 11.9, 3e-3, "converged RPA+LF 10.22 scaled by the BSE ratio")
close(float(d["tda"]), 0.034, 3e-2, "Tamm-Dancoff error of RPA+LF eps_2 (fraction of peak)")
close(float(d["Kd_mean"]) * 1e3, 81, 1e-2, "mean diagonal K^d [meV]")
r3 = np.interp(3.0, w, (-1 / E["bse"]).imag) / np.interp(3.0, w, (-1 / E["lf"]).imag)
close(r3, 1.36, 1e-2, "L(BSE)/L(RPA+LF) at 3 eV")
for x in (4.0, 5.0, 6.0):
    r = np.interp(x, w, (-1 / E["bse"]).imag) / np.interp(x, w, (-1 / E["lf"]).imag)
    assert abs(r - 1) < 0.035, r
close(float(d["Emin"]), 3.13, 3e-3, "smallest vertical transition on the grid [eV]")

# ------------------------------------------------------------------ figure
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.85))
col = {"ip": "0.45", "lf": "#1f5fa8", "bse": "#b2182b"}
m = wx <= 8
ax1.plot(wx[m], epsx.imag[m], "k-", lw=1.6, label="measured")
ax1.plot(w, E["ip"].imag, "--", color=col["ip"], lw=1.1, label="independent particles")
ax1.plot(w, E["lf"].imag, "-", color=col["lf"], lw=1.1, label="RPA + local fields")
ax1.plot(w, E["bse"].imag, "-", color=col["bse"], lw=1.3, label="Bethe\u2013Salpeter")
ax1.set_xlim(2, 7)
ax1.set_ylim(0, 74)   # headroom: the legend sits above the 46 peak
ax1.set_xlabel(r"$\omega$ (eV)")
ax1.set_ylabel(r"$\varepsilon_2$")
ax1.text(0.03, 0.95, "(a)", transform=ax1.transAxes, va="top")
ax1.legend(frameon=False, fontsize=7, loc="upper right", bbox_to_anchor=(1.0, 1.0))

ax2.semilogy(wx, Lx, "k-", lw=1.6, label="measured")
ax2.semilogy(w, (-1 / E["ip"]).imag, ":", color=col["lf"], lw=1.2, label="RPA, no local fields")
ax2.semilogy(w, (-1 / E["lf"]).imag, "-", color=col["lf"], lw=1.1, label="RPA + local fields")
ax2.semilogy(w, (-1 / E["bse"]).imag, "-", color=col["bse"], lw=1.3, label="Bethe\u2013Salpeter")
ax2.set_xlim(1, 7)
ax2.set_ylim(1e-4, 1)
ax2.set_xlabel(r"$\omega$ (eV)")
ax2.set_ylabel(r"$L = \mathrm{Im}(-1/\varepsilon_{\mathrm{mac}})$")
ax2.text(0.03, 0.95, "(b)", transform=ax2.transAxes, va="top")
ax2.legend(frameon=False, fontsize=6.5, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_11.pdf"))
print("wrote fig4_11.pdf")
