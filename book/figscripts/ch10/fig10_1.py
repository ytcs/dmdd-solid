"""Fig. 10.1: the silicon crystal form factor |f_crys(q, omega)|^2 in the (q, omega) plane, and every number that
Sect. 10.1 quotes about its q dependence. Output: tex/figures/ch10/fig10_1.pdf.

Data: the tabulation of Essig et al., JHEP 05 (2016) 046, arXiv:1509.01598 [E16], read and normalized by si_fcrys.py
(see its header for the normalization and its three checks). PBE + scissor (E_g = 1.11 eV), unscreened, valence to
conduction, angle-averaged, binned in 0.1 eV x 0.02 alpha m_e.
Display choices (named in the caption): the k grid of [E16] leaves most q bins below about 0.5 q0 empty; for the color
map, q bins are merged in groups of five (0.1 q0) and energy bins in groups of five (0.5 eV). Numbers quoted in the text
use bins merged over the stated q window.
Other inputs:
  [CODATA] alpha, m_e; a = 5.431 A (Sect. 1.3), |G_111| = sqrt(3) 2 pi/a = 3.95 keV (Sect. 1.3), k_c = 1.94 keV (Sect. 3.3).
  [A.8]    v_max = 794.5 km/s = 2.650e-3 (eq:A.8-ref); kinematic edge omega <= q v_max - q^2/2 m_chi (eq:1.3-region).
  [EPM]    book EPM S0 at q0 along [100], figscripts/ch08/we8_10_data_NK20.npz (Cohen-Bergstresser, model gap 0.82 eV).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from si_fcrys import load, omega_sbar, ALPHA, ME, OMEGA, Q0, DQ, DE  # noqa: E402

BOOK = os.path.join(HERE, "..", "..")
OUT = os.path.join(BOOK, "tex", "figures", "ch10")
os.makedirs(OUT, exist_ok=True)
VMAX = 794.5 / 299792.458
G111 = np.sqrt(3) * 2 * np.pi / (5.431 / 1973.269804)    # eV
KC = 0.85 * 2 * np.pi / (5.431 / 1973.269804)            # eV, Sect. 3.3

q, E, f2 = load()
qq = q / Q0
OS = omega_sbar(q, f2)                                   # Omega * S-bar, eV^-1
ne = 8 / OMEGA                                           # valence electrons per volume, eV^3

nz = np.nonzero(f2.sum(0))[0]
print(f"table onset: first nonzero energy point {E[nz[0]]:.1f} eV; last {E[nz[-1]]:.1f} eV")
print(f"q unit dq = {DQ:.1f} eV = {DQ/Q0:.4f} q0 (CODATA q0 = {Q0:.1f} eV)")
filled = np.count_nonzero(f2.sum(1)[:25])
print(f"filled q bins below 0.5 q0: {filled} of 25")


def window(lo, hi):
    s = (qq >= lo) & (qq < hi)
    return s


# --- f-sum rule (eq:4.3-fsum), valence density, over the table's 0-50 eV ---
print("\nf-sum fraction int_0^50eV omega S-bar / (pi n_e q^2/m_e), bins merged over the window:")
for lo, hi in [(0.3, 0.5), (0.5, 0.7), (0.9, 1.1), (1.4, 1.6), (1.9, 2.1)]:
    s = window(lo, hi)
    num = np.sum((OS[s] / OMEGA) * E[None, :], axis=1) * DE
    den = np.pi * ne * q[s] ** 2 / ME
    print(f"  q/q0 in [{lo},{hi}): ratio averaged over all bins (empty bins included) = {np.mean(num/den):.3f}"
          f"  (free recoil q^2/2m_e at centre = {((lo+hi)/2*Q0)**2/2/ME:.1f} eV)")

# --- q dependence at fixed omega: merged q bins of 0.1 q0 ---
nm = 5
nqm = len(q) // nm
qm = q[:nqm * nm].reshape(nqm, nm).mean(1)
f2m = f2[:nqm * nm].reshape(nqm, nm, -1).mean(1)
OSm = OS[:nqm * nm].reshape(nqm, nm, -1).mean(1)
print("\nfixed omega (0.5 eV window), q bins merged to 0.1 q0 (empty bins included in each mean):")
for w in (3.0, 5.0, 10.0, 20.0):
    j = (E >= w - 0.25) & (E < w + 0.25)
    fw = f2m[:, j].mean(1)
    sw = OSm[:, j].mean(1)
    ip = np.argmax(fw)
    isb = np.argmax(sw)
    r2 = np.interp(2 * Q0, qm, fw) / np.interp(Q0, qm, fw)
    r3 = np.interp(3 * Q0, qm, fw) / np.interp(Q0, qm, fw)
    print(f"  omega = {w:4.1f} eV: |f|^2 peaks at q = {qm[ip]/Q0:.2f} q0 (max {fw[ip]:.2f}); "
          f"rate weight q*S-bar peaks at {qm[np.argmax(qm*sw)]/Q0:.2f} q0; |f|^2(2q0)/|f|^2(q0) = {r2:.3f}, (3q0)/(q0) = {r3:.2e}")
# small-q power law of |f|^2 integrated over 0-50 eV (q bins merged)
F = f2m.sum(1) * DE
s = (qm / Q0 > 0.3) & (qm / Q0 < 0.75) & (F > 0)
p = np.polyfit(np.log(qm[s]), np.log(F[s]), 1)[0]
print(f"\nsmall-q slope of int |f|^2 d omega over 0.3-0.75 q0: q^{p:.2f}")
s = (qm / Q0 > 2.0) & (qm / Q0 < 4.0) & (F > 0)
p2 = np.polyfit(np.log(qm[s]), np.log(F[s]), 1)[0]
print(f"large-q slope of int |f|^2 d omega (0-50 eV) over 2-4 q0: q^{p2:.1f}")
iF = np.argmax(F)
print(f"int |f|^2 d omega (0-50 eV) peaks at q = {qm[iF]/Q0:.2f} q0")

# --- comparison with the book EPM at q0 ---
d = np.load(os.path.join(HERE, "..", "ch08", "we8_10_data_NK20.npz"))
s = window(0.95, 1.05)
Sb = (OS[s] / OMEGA).mean(0)          # all bins, empty ones included
print("\nS-bar at q0 (table, bins 0.95-1.05 q0, 0.5 eV window) against EPM S0 along [100] (NK = 20):")
for w in (5, 10, 15, 20):
    j = (E >= w - 0.25) & (E < w + 0.25)
    jj = np.argmin(abs(d["OM"] - w))
    print(f"  {w:2d} eV: table {Sb[j].mean():.3e} eV^2, EPM {d['S0_1'][jj]:.3e} eV^2, ratio {Sb[j].mean()/d['S0_1'][jj]:.2f}")

# --- figure ---
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5, "pdf.fonttype": 42,
                     "font.family": "serif", "mathtext.fontset": "cm"})
ne_ = 5
Em = E[:(len(E) // ne_) * ne_].reshape(-1, ne_).mean(1)
F2 = f2m[:, :(len(E) // ne_) * ne_].reshape(nqm, -1, ne_).mean(2)
F2 = np.where(F2 > 0, F2, np.nan)
fig, ax = plt.subplots(figsize=(5.2, 3.7))
qe = np.arange(nqm + 1) * nm * DQ / Q0 + 0.5 * DQ / Q0
ee = np.arange(len(Em) + 1) * ne_ * DE + 0.5 * DE
pc = ax.pcolormesh(qe, ee, F2.T, norm=LogNorm(vmin=1e-3, vmax=30), cmap="viridis", shading="flat", rasterized=True)
cb = fig.colorbar(pc, ax=ax, pad=0.02)
cb.set_label(r"$|f_{\mathrm{crys}}(q,\omega)|^2$")
qline = np.linspace(0.01, 6, 600) * Q0
for m, ls, lab in [(1e6, ":", r"$m_\chi = 1$ MeV"), (1e7, "--", r"$m_\chi = 10$ MeV")]:
    wmax = qline * VMAX - qline**2 / (2 * m)
    ok = wmax > 0
    ax.plot(qline[ok] / Q0, wmax[ok], color="w", ls=ls, lw=1.1, label=lab)
ax.plot(qline / Q0, qline**2 / (2 * ME), color="C3", lw=1.1, label=r"$\omega = q^2/2m_e$")
ax.axvline(G111 / Q0, color="0.85", lw=0.6, ls="-.")
ax.text(G111 / Q0 + 0.05, 46.5, r"$|\mathbf{G}_{111}| = 1.06\,q_0$", color="0.95", fontsize=7.5)
ax.set_xlim(0, 5)
ax.set_ylim(0, 50)
ax.set_xlabel(r"$q/q_0$  ($q_0 = \alpha m_e = 3.73$ keV)")
ax.set_ylabel(r"$\omega$ [eV]")
ax.legend(loc="upper right", frameon=True, facecolor="0.2", edgecolor="0.2", labelcolor="w", fontsize=7)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig10_1.pdf"))
print("\nwrote", os.path.join(OUT, "fig10_1.pdf"))
