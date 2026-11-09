"""Fig. 12.1 (Sect. 12.1): the (omega_l, omega_e) plane of the joint response of silicon at q = 50 keV.
Output: tex/figures/ch12/fig12_1.pdf.  Prints every number of Sect. 12.1 that rests on this model (log: fig12_1.log).

What is plotted, per nucleus and normalized as probabilities (the joint response divided by its zeroth moment 2 pi n_kappa):
  * electron-following sector (omega_e = 0): the incoherent T = 0 lattice spectrum s(q, omega_l) of one Si nucleus, weight
    1 - P_Mig, with its zero-phonon part e^{-2W(q)} delta(omega_l);
  * Migdal sectors (omega_e > 0): the leading entry eq:12.1-Skk, diagonal in G, with the lattice factor in the
    incoherent approximation (eq:D.33-diag):
        d2P/domega_l domega_e = [4 alpha Z^2 / (M^2 omega_e^4)] int d^3p/(2 pi)^3 (q.p)^2/p^2 L(p, omega_e)
                                 x [ s(|q - p|, omega_l) + e^{-2W(|q - p|)} delta(omega_l) ],
    split into the zero-phonon part (delta(omega_l), sector P_0) and the rest (sector P_+).
Inputs (all reused, nothing recomputed from first principles):
  L(p, omega): random-phase loss function of Si with local fields, Knapen, Kozaczuk and Lin GPAW tables (arXiv:2101.08275,
    distributed with DarkELF), averaged over directions of p in 100-eV bins: figscripts/ch10/si_elf_binned.npz, column 'lf'.
    p <= 22.5 keV, omega <= 89 eV, valence electrons only, scissor gap 1.11 eV.
  s(Q, omega_l), 2W(Q): incoherent T = 0 self response of a Si nucleus from the PBE/DFPT phonon density of states of Sect. 5.2,
    by FFT of the generating function: figscripts/ch11/imp11.spectrum (Sect. 11.3, 11.4); 2W = Q^2 <u_x^2>, <u_x^2> = 2.446e-3 A^2.
  M = 28.0855 u (natural Si), alpha = 1/137.036, Z = 4 (valence charge of the pseudo-ion, Coulomb tail -Z e^2/p^2, Sect. 6.2).
Modelling choices (stated in the caption): valence electrons only, point pseudo-ion of charge 4 (no core form factor Z_ion(p),
Sect. 12.3), diagonal of the dielectric matrix only (no off-diagonal local-field terms in the vertex), Condon approximation in
the crystal frame (lattice factor at |q - p|), lattice final states on the ground surface, incoherent lattice response, T = 0.
Runtime: about 20 s.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
import imp11 as I  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch12")
os.makedirs(OUT, exist_ok=True)

ALPHA = 1 / 137.035999
Z = 4.0
M = I.M                              # eV, 28.0855 u
Q = 50e3                             # eV

# ---- loss function --------------------------------------------------------------------------------------------------
d = np.load(os.path.join(HERE, "..", "ch10", "si_elf_binned.npz"))
pg, we, L = d["q"], d["omega"], d["lf"]          # eV, eV, L[omega, p]
wp = np.gradient(pg)                              # trapezoid-like weights on the nonuniform p grid
ww = np.gradient(we)

# ---- lattice response on a grid of |q - p| ----------------------------------------------------------------------------
DWL = 1e-3                                         # 1-meV bins in omega_l
WL = np.arange(0, 0.40, DWL) + DWL / 2             # bin centers, eV
QG = np.arange(25e3, 76e3, 1e3)
SQ = np.zeros((QG.size, WL.size))
E0 = np.zeros(QG.size)
for i, qq in enumerate(QG):
    w, s, e0 = I.spectrum(qq, h=I.DW, wtop=0.42)
    c = np.concatenate([[0], np.cumsum(s) * I.DW])
    wc = np.concatenate([[0], w + I.DW / 2])
    edges = np.arange(0, 0.40 + DWL / 2, DWL)
    SQ[i] = np.diff(np.interp(edges, wc, c)) / DWL   # bin-averaged density, eV^-1
    E0[i] = e0

# ---- Migdal joint density -----------------------------------------------------------------------------------------
xm, wm = np.polynomial.legendre.leggauss(64)       # mu = cos(angle between q and p)
P, MU = np.meshgrid(pg, xm, indexing="ij")
QP = np.sqrt(Q**2 + P**2 - 2 * Q * P * MU)          # |q - p|
iq = np.clip((QP - QG[0]) / 1e3, 0, QG.size - 1.0001)
i0 = iq.astype(int)
f = iq - i0
S_qp = (1 - f)[..., None] * SQ[i0] + f[..., None] * SQ[i0 + 1]        # (p, mu, omega_l)
E_qp = (1 - f) * E0[i0] + f * E0[i0 + 1]
ang = wm * xm**2                                    # weights of the mu integral times mu^2
A_plus = np.einsum("pm,pml->pl", ang[None, :] * np.ones_like(P), S_qp)  # (p, omega_l)
A_zero = (ang[None, :] * E_qp).sum(axis=1)          # (p,)
A_soft = (ang).sum() * np.ones_like(pg)             # soft limit: lattice factor of unit weight at Q = q
C = 4 * ALPHA * Z**2 * Q**2 / (M**2 * 4 * np.pi**2)
with np.errstate(divide="ignore", invalid="ignore"):
    pref = np.where(we > 0, C / we**4, 0.0)        # eV^-4 ... per omega_e
Jp = pref[:, None] * np.einsum("p,ep,pl->el", wp * pg**2, L, A_plus)   # d2P/domega_e domega_l, eV^-2  [omega_e, omega_l]
J0 = pref * ((wp * pg**2 * A_zero)[None, :] * L).sum(axis=1)            # dP/domega_e of the zero-phonon line, eV^-1
Js = pref * ((wp * pg**2 * A_soft)[None, :] * L).sum(axis=1)            # soft-limit marginal, eV^-1

Pplus = (Jp.sum(axis=1) * DWL * ww).sum()
Pzero = (J0 * ww).sum()
Pmig = Pplus + Pzero
Psoft = (Js * ww).sum()
marg = Jp.sum(axis=1) * DWL + J0                    # dP/domega_e
mean_we = (we * marg * ww).sum() / Pmig
mean_wl = (Jp.sum(axis=0) * WL).sum() * 0 + ((Jp * WL[None, :]).sum(axis=1) * DWL * ww).sum() / Pmig
ER = Q**2 / (2 * M)
w_ad, s_ad, e0_ad = I.spectrum(Q, h=I.DW, wtop=0.42)
mean_ad = (w_ad * s_ad).sum() * I.DW               # first moment of the electron-following lattice spectrum, = E_R
# energy at which half of P_Mig has accumulated, and the share below 10 eV
cum = np.cumsum(marg * ww) / Pmig
w_half = np.interp(0.5, cum, we)
share10 = np.interp(10.0, we, cum)
pk = we[np.argmax(we * marg)]

print("Si, q = %.0f keV: E_R = %.2f meV, 2W = %.3f, e^-2W = %.4f; electron-following first moment %.2f meV"
      % (Q / 1e3, ER * 1e3, I.two_w(Q), np.exp(-I.two_w(Q)), mean_ad * 1e3))
print("P_Mig = %.3e (zero-phonon %.3e = %.1f %%, phonon-dressed %.3e); soft limit (lattice at q, unit weight) %.3e, ratio %.3f"
      % (Pmig, Pzero, 100 * Pzero / Pmig, Pplus, Psoft, Pmig / Psoft))
print("Migdal events: mean omega_e = %.2f eV, half of P_Mig below %.2f eV, %.1f %% below 10 eV, peak of omega_e dP/domega_e at %.2f eV"
      % (mean_we, w_half, 100 * share10, pk))
print("Migdal events: mean omega_l = %.2f meV (E_R = %.2f meV); zero-phonon fraction %.3f vs e^-2W(q) = %.3f"
      % (mean_wl * 1e3, ER * 1e3, Pzero / Pmig, np.exp(-I.two_w(Q))))
print("Mean energy deposited in a Migdal event omega_l + omega_e = %.2f eV; ratio of electronic to lattice energy %.0f"
      % (mean_we + mean_wl, mean_we / mean_wl))
print("electron-following weight 1 - P_Mig = %.8f" % (1 - Pmig))
p2 = 2 * M * (mean_wl - ER)
vN = Q / M
print("<p^2>^(1/2) of the momentum taken by the electrons, from mean omega_l - E_R = <p^2>/2M: %.2f keV; "
      "v_N = %.3e; v_N p_rms / (half-P_Mig energy) = %.1e; (E_R / half-P_Mig energy)^2 = %.1e"
      % (np.sqrt(p2) / 1e3, vN, vN * np.sqrt(p2) / w_half, (ER / w_half)**2))
dM = 14 * 0.51099895e6 / M
print("estimate (E_R/<omega_e>)(delta M/M) with the atomic drag mass 14 m_e (delta M/M = %.3e): %.2e" % (dM, ER / mean_we * dM))

# ---- figure -------------------------------------------------------------------------------------------------------
fig = plt.figure(figsize=(5.6, 4.6))
gs = fig.add_gridspec(2, 4, width_ratios=(0.22, 4, 1.2, 0.12), height_ratios=(1.15, 4), wspace=0.07, hspace=0.07,
                      left=0.12, right=0.89, bottom=0.11, top=0.97)
ax = fig.add_subplot(gs[1, 1])
ax0 = fig.add_subplot(gs[1, 0], sharey=ax)
axt = fig.add_subplot(gs[0, 1], sharex=ax)
axr = fig.add_subplot(gs[1, 2], sharey=ax)
cax = fig.add_subplot(gs[1, 3])

WLmax = 0.25
kl = WL < WLmax
ke = (we > 1.0) & (we < 60)
Z2 = Jp[np.ix_(ke, kl)]
vtop = max(Z2.max(), (J0[ke] / DWL).max())
norm = LogNorm(vmin=vtop * 1e-5, vmax=vtop)
pc = ax.pcolormesh(WL[kl] * 1e3, we[ke], Z2, norm=norm, cmap="viridis", shading="nearest", rasterized=True)
# zero-phonon Migdal line at omega_l = 0 (sector P_0), shown per 1-meV bin so that it shares the color scale
yk = we[ke]
ye = np.concatenate([[yk[0] - (yk[1] - yk[0]) / 2], (yk[1:] + yk[:-1]) / 2, [yk[-1] + (yk[-1] - yk[-2]) / 2]])
ax0.pcolormesh([0, 1], ye, (J0[ke] / DWL)[:, None], norm=norm, cmap="viridis", shading="flat", rasterized=True)
ax0.set_xlim(0, 1)
ax0.set_xticks([0.5]); ax0.set_xticklabels(["0"])
ax0.set_ylabel(r"energy given to the electrons $\omega_e$ (eV)")
ax0.text(0.5, 40, r"$\mathcal{P}_0$", color="w", fontsize=7, ha="center", va="center")
ax.tick_params(labelleft=False)
ax.axvline(ER * 1e3, color="w", lw=0.7, ls="--")
ax.text(ER * 1e3 + 3, 45, r"$E_R$", color="w", fontsize=8)
ax.text(150, 30, r"$\mathcal{P}_+$", color="w", fontsize=9)
ax.set_yscale("log")
ax.set_ylim(1.0, 60)
ax.set_xlim(0, WLmax * 1e3)
ax.set_xlabel(r"energy given to the lattice $\omega_l$ (meV)")
cb = fig.colorbar(pc, cax=cax)
cb.set_label(r"$\mathrm{d}^2P/\mathrm{d}\omega_l\,\mathrm{d}\omega_e$ (eV$^{-2}$)", fontsize=7)
cb.ax.tick_params(labelsize=6)

# top: electron-following sector, omega_e = 0
kk = w_ad < WLmax
axt.plot(w_ad[kk] * 1e3, s_ad[kk], color="k", lw=1.0)
axt.text(0.98, 0.9, r"$\mathcal{P}_{\mathrm{ad}}$: $\omega_e = 0$; zero-phonon weight $\mathrm{e}^{-2W} = %.2f$ at $\omega_l = 0$" % e0_ad,
         transform=axt.transAxes, ha="right", va="top", fontsize=7)
axt.set_ylabel(r"$s^{\mathrm{inc}}_\kappa$ (eV$^{-1}$)", fontsize=8)
axt.tick_params(labelbottom=False, labelsize=7)
axt.set_ylim(0, s_ad[kk].max() * 1.25)

# right: marginal over omega_l
axr.plot(we[ke] * marg[ke], we[ke], color="C1", lw=1.1)
axr.set_xscale("log")
axr.set_xlabel(r"$\omega_e\,\mathrm{d}P_{\mathrm{Mig}}/\mathrm{d}\omega_e$", fontsize=8)
axr.tick_params(labelleft=False, labelsize=6)
axr.set_xlim((we[ke] * marg[ke]).max() * 1e-3, (we[ke] * marg[ke]).max() * 2)

fig.savefig(os.path.join(OUT, "fig12_1.pdf"))
print("wrote", os.path.join(OUT, "fig12_1.pdf"))
