"""Fig. 17.x (fig:17-sectors) of Sect. 17.1: dominant-sector maps of silicon in (m_chi, omega_th) and the rates above
threshold at m_chi = 10 MeV. Reads sectors17.npz (written by sectors17.py, which documents every model choice and
input); prints the region boundaries quoted in the caption to fig17_sectors.log.

(a) nucleon coupling, heavy mediator: at each point the channel with the largest rate above the threshold omega_th on
    the total deposited energy. Lattice (electron-following) sector: one phonon / multiphonon / free recoil (labels as in
    sectors17.py); Migdal: zero-phonon / phonon-dressed (zero-phonon share of the events above or below one half).
    Gray contours: the dominant rate, events per kg and year at sigma_p = 1e-38 cm^2 (decades).
(b) electron coupling, heavy mediator: zero-phonon electron recoil (loss function with local fields) against the
    acoustic peak of an electron-only coupling (model of Limit 10.2a); the phonon-assisted window of Sect. 13.9 drawn
    from Table 13.1: phonon-assisted only from the onset (0.3374 MeV free pair, solid; 0.3332 MeV exciton replica, dashed)
    to the first zero-phonon edge 0.405-0.408 MeV (two independent calculations, solid band); estimated phonon-assisted
    lead to 0.43 MeV (hatched) and two-channel band 0.43-0.51 MeV (cross-hatched). Contours at sigma_e = 1e-37 cm^2.
(c) m_chi = 10 MeV, nucleon coupling: rate above omega_th by channel.
Lines: dashed, the free-recoil endpoint E_R^max = 2 mu_chiN^2 v_max^2 / M; dotted, the largest deposit m_chi v_max^2/2;
dash-dotted, the acoustic edge m_min^ac (eq:11.1-edge) with c_LA,max = 9.35 km/s in (a), 8.43 km/s (the model's) in (b).
Output: tex/figures/ch17/fig17_sectors.pdf.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch10"))
import rate10_2 as R  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch17", "fig17_sectors.pdf")
LOG = open(os.path.join(HERE, "fig17_sectors.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


d = np.load(os.path.join(HERE, "sectors17.npz"))
MS, WTH = d["MS"], d["WTH"]
VMAX = R.VMAX
M = 28.0855 * 931.494e6
KMS = 1 / 299792.458
Q_IMP = 92.5e3
TINY = 1e-12            # events/kg/yr: below this a channel counts as closed (the grid's rates span 1e-300 to 1e7)

# ---- panel (a) classification ---------------------------------------------------------------------------------------
lat1, latm = d["one"], d["multi"] + d["gauss"]
lat = lat1 + latm
mig = d["mig0"] + d["migp"]
cls_a = np.zeros(lat.shape, int)        # 0 none, 1 one phonon, 2 multiphonon, 3 free recoil, 4 Migdal ZP, 5 Migdal P+
latwin = (lat >= mig) & (lat > TINY)
cls_a[latwin & (lat1 >= latm)] = 1
cls_a[latwin & (lat1 < latm) & ~(d["qmed_lat"] >= Q_IMP)] = 2
cls_a[latwin & (lat1 < latm) & (d["qmed_lat"] >= Q_IMP)] = 3
migwin = (mig > lat) & (mig > TINY)
cls_a[migwin & (d["mig0"] >= d["migp"])] = 4
cls_a[migwin & (d["mig0"] < d["migp"])] = 5
dom_a = np.maximum(lat, mig)

# ---- panel (b) classification ---------------------------------------------------------------------------------------
ER, AC = d["ER"].copy(), d["AC"]
MM = MS[:, None] * np.ones_like(WTH)[None, :]
WW = np.ones_like(MS)[:, None] * WTH[None, :]
kin = WW <= MM * VMAX**2 / 2
inwin = (MM >= 0.3332e6) & (MM < 0.51e6) & kin
ER[MM < 0.51e6] = 0.0                      # the table rate is not used inside the window (Sect. 13.9 estimates)
cls_b = np.zeros(ER.shape, int)            # 0 none, 1 acoustic (electron density), 2 zero-phonon ER, 3 window
acw = (AC > TINY) & (AC >= ER)
cls_b[acw] = 1
cls_b[(ER > TINY) & (ER > AC)] = 2
cls_b[inwin & ~acw] = 3
dom_b = np.maximum(ER, AC)

# ---- boundaries for the log ------------------------------------------------------------------------------------------
def edge_ac(w, c_kms):
    c = c_kms * KMS
    return w / (2 * c * (VMAX - c))


out("Free-recoil endpoint E_R^max = 2 mu^2 v_max^2/M: 10 MeV %.4f eV, 100 MeV %.3f eV, 1 GeV %.1f eV"
    % tuple(2 * (m * M / (m + M))**2 * VMAX**2 / M for m in (10e6, 100e6, 1e9)))
out("Largest deposit m v_max^2/2: 0.4 MeV %.3f eV, 1 MeV %.3f eV, 10 MeV %.2f eV, 100 MeV %.1f eV"
    % tuple(m * VMAX**2 / 2 for m in (0.4e6, 1e6, 10e6, 100e6)))
out("Ratio of the two ceilings M/(4 m) for m << M: 1 MeV %.0f, 10 MeV %.0f" % (M / 4e6, M / 4e7))
out("Acoustic edge at omega_th = 1 meV: %.2f keV (c_LA,max = 9.35 km/s); 10 meV: %.1f keV"
    % (edge_ac(1e-3, 9.35) / 1e3, edge_ac(1e-2, 9.35) / 1e3))
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
import phon11 as P11  # noqa: E402
for nm in ("Si", "Ge"):
    av = P11.averages(nm)
    out("%s: c_LA,max = %.3f km/s (measured elastic tensor of phon11.py), acoustic edge at 1 meV = %.2f keV"
        % (nm, av["cLAmax"], P11.mmin_ac(av["cLAmax"], 1e-3) / 1e3))
out("GaAs polar edge 2 omega_L / v_max^2 with omega_L = 36.35 meV: %.2f keV" % (2 * 0.03635 / VMAX**2 / 1e3))
out("Migdal floors 2 E_g/v_max^2: Si (1.17 eV) %.4f MeV, Ge (0.744 eV) %.4f MeV, GaAs (1.519 eV) %.4f MeV"
    % (2 * 1.17 / VMAX**2 / 1e6, 2 * 0.744 / VMAX**2 / 1e6, 2 * 1.519 / VMAX**2 / 1e6))
j1 = np.argmin(abs(WTH - 1e-3))
for name, cl in (("(a)", cls_a), ("(b)", cls_b)):
    for c in np.unique(cl):
        sel = cl == c
        out("panel %s class %d: %d grid points; masses %.3g-%.3g MeV; thresholds %.3g-%.3g eV"
            % (name, c, sel.sum(), MM[sel].min() / 1e6, MM[sel].max() / 1e6, WW[sel].min(), WW[sel].max()))
out("Panel (a) at omega_th = 1 meV, classes along the mass grid:", " ".join(str(c) for c in cls_a[:, j1]))
out("Panel (b) at omega_th = 1 meV, classes along the mass grid:", " ".join(str(c) for c in cls_b[:, j1]))

# ---- figure ----------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})
fig = plt.figure(figsize=(6.4, 6.9))
gs = fig.add_gridspec(2, 2, height_ratios=(1.25, 1.0), hspace=0.36, wspace=0.08)
axa = fig.add_subplot(gs[0, 0])
axb = fig.add_subplot(gs[0, 1], sharey=axa)
axc = fig.add_subplot(gs[1, :])

# cell edges in log space
def edges(x):
    lx = np.log10(x)
    e = np.concatenate([[lx[0] - (lx[1] - lx[0]) / 2], (lx[1:] + lx[:-1]) / 2, [lx[-1] + (lx[-1] - lx[-2]) / 2]])
    return 10**e


XE, YE = edges(MS / 1e6), edges(WTH)
col_a = ["white", "#cfe3f3", "#7fb0d8", "#2f6ea6", "#f6c98d", "#d9822b"]
col_b = ["white", "#bfe3bf", "#e8a0a0", "#c9b6e0"]
axa.pcolormesh(XE, YE, cls_a.T, cmap=ListedColormap(col_a), norm=BoundaryNorm(np.arange(-0.5, 6), 6), shading="flat",
               rasterized=True)
axb.pcolormesh(XE, YE, cls_b.T, cmap=ListedColormap(col_b), norm=BoundaryNorm(np.arange(-0.5, 4), 4), shading="flat",
               rasterized=True)
lv = [1e-2, 1, 1e2, 1e4]
with np.errstate(divide="ignore"):
    ca = axa.contour(MS / 1e6, WTH, np.log10(np.maximum(dom_a, 1e-300)).T, levels=np.log10(lv), colors="0.35",
                     linewidths=0.5)
    cb = axb.contour(MS / 1e6, WTH, np.log10(np.maximum(dom_b, 1e-300)).T, levels=np.log10(lv), colors="0.35",
                     linewidths=0.5)
fmt = {np.log10(v): (r"$10^{%d}$" % np.log10(v)) for v in lv}
axa.clabel(ca, levels=ca.levels[1:], fmt=fmt, fontsize=6, inline=True)   # the 10^-2 label falls on the bunched acoustic edge
axb.clabel(cb, levels=cb.levels[1:], fmt=fmt, fontsize=6, inline=True)

mline = np.geomspace(MS[0], MS[-1], 400)
for ax in (axa, axb):
    ax.plot(mline / 1e6, mline * VMAX**2 / 2, color="k", ls=":", lw=0.9)
axa.plot(mline / 1e6, 2 * (mline * M / (mline + M))**2 * VMAX**2 / M, color="k", ls="--", lw=0.8)
wl = np.geomspace(1e-3, 0.0637, 50)
axa.plot(edge_ac(wl, 9.35) / 1e6, wl, color="k", ls="-.", lw=0.8)
wl2 = np.geomspace(1e-3, R.C_LA * R.Q_X, 50)
axb.plot(edge_ac(wl2, 8.43) / 1e6, wl2, color="k", ls="-.", lw=0.8)

# window of Sect. 13.9 in panel (b)
ytop = lambda m: m * VMAX**2 / 2
for m0, m1, hatch in ((0.405e6, 0.43e6, "////"), (0.43e6, 0.51e6, "xxxx")):
    mm = np.geomspace(m0, m1, 30)
    yb = np.interp(mm, MS, np.array([WTH[cls_b[i] == 1].max() if (cls_b[i] == 1).any() else 1e-3 for i in range(len(MS))]))
    axb.fill_between(mm / 1e6, np.maximum(yb, 1e-3), ytop(mm), facecolor="none", edgecolor="0.25", hatch=hatch, lw=0)
axb.axvspan(0.405, 0.408, color="0.3", alpha=0.6, lw=0)
axb.axvline(0.3374, color="0.15", lw=0.8)
axb.axvline(0.3332, color="0.15", lw=0.8, ls="--")
axb.axvline(0.51, color="0.15", lw=0.6, ls=":")

for ax, lab in ((axa, "(a) nucleon coupling"), (axb, "(b) electron coupling")):
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(XE[0], XE[-1])
    ax.set_ylim(1e-3, 50)
    ax.set_xlabel(r"$m_\chi$ (MeV)")
    ax.set_title(lab, fontsize=8, loc="left")
    ax.set_xticks([1e-2, 1e-1, 1, 10, 100, 1000])
axa.set_ylabel(r"threshold $\omega_{\mathrm{th}}$ (eV)")
plt.setp(axb.get_yticklabels(), visible=False)

la = [Patch(fc=c, ec="0.5", lw=0.4, label=l) for c, l in zip(col_a[1:], ["one phonon", "multiphonon", "free recoil",
                                                                       "Migdal, zero-phonon", "Migdal, phonon-dressed"])]
axa.legend(handles=la, loc="upper left", fontsize=6, frameon=True, framealpha=0.9, handlelength=1.2)
lb = [Patch(fc=col_b[1], ec="0.5", lw=0.4, label="acoustic peak\n(electron density only)"),
      Patch(fc=col_b[2], ec="0.5", lw=0.4, label="zero-phonon recoil"),
      Patch(fc=col_b[3], ec="0.5", lw=0.4, label="phonon-assisted window"),
      Patch(fc="white", ec="0.25", hatch="////", lw=0.4, label="estimated lead"),
      Patch(fc="white", ec="0.25", hatch="xxxx", lw=0.4, label="two-channel band")]
axb.legend(handles=lb, loc="upper right", fontsize=6, frameon=True, framealpha=0.9, handlelength=1.2)
axb.annotate("phonon-assisted\nwindow", xy=(0.42, 0.6), xytext=(0.012, 3.0), fontsize=6.5,
             arrowprops=dict(arrowstyle="-|>", color="0.2", lw=0.6))

# ---- panel (c): 10 MeV ------------------------------------------------------------------------------------------------
sys.path.insert(0, HERE)
import sectors17 as S  # noqa: E402
wc = np.geomspace(1e-3, 3.0, 700)
r = S.nucleon_rates(10e6, wc)
latc = r["one"] + r["multi"] + r["gauss"]
migc = r["mig0"] + r["migp"]
wx = S.cross_log(wc, latc, migc)
kx = np.searchsorted(wc, wx)
sl = -(np.log(latc[kx + 1]) - np.log(latc[kx - 1])) / (wc[kx + 1] - wc[kx - 1])
out("Panel (c), 10 MeV: lattice rate falls by e every %.4f eV at the crossover; a factor 2 in the lattice rate moves "
    "omega_x by %.4f eV, a factor 1.35 in the Migdal rate by %.4f eV" % (1 / sl, np.log(2) / sl, np.log(1.35) / sl))
out("Panel (c), 10 MeV: crossover on the %d-point grid %.3f eV (sectors17.log fine grid: 0.307 eV)" % (len(wc), wx))
axc.loglog(wc, r["one"], color=col_a[1], lw=1.4, label="one phonon")
axc.loglog(wc, r["multi"] + r["gauss"], color=col_a[3], lw=1.4, label=r"multiphonon ($n \geq 2$)")
axc.loglog(wc, r["mig0"], color=col_a[4], lw=1.4, label="Migdal, zero-phonon")
axc.loglog(wc, r["migp"], color=col_a[5], lw=1.4, label="Migdal, phonon-dressed")
axc.loglog(wc, latc, color="k", lw=0.8, ls="--", label="lattice total")
axc.axvline(wx, color="0.3", lw=0.6)
for k in (1, 2, 3, 4):
    axc.axvline(k * 0.0637, color="0.75", lw=0.5, ls=":")
axc.text(wx * 1.05, 3e4, r"$\omega_\times = %.2f$ eV" % wx, fontsize=7)
axc.set_ylim(1e-6, 3e6)
axc.set_xlim(1e-3, 3.0)
axc.set_xlabel(r"threshold $\omega_{\mathrm{th}}$ (eV)")
axc.set_ylabel(r"rate above $\omega_{\mathrm{th}}$ (kg$^{-1}$ yr$^{-1}$)")
axc.set_title(r"(c) nucleon coupling, $m_\chi = 10$ MeV, $\sigma_p = 10^{-38}$ cm$^2$", fontsize=8, loc="left")
axc.legend(fontsize=6.5, loc="lower left", frameon=False)
fig.savefig(OUT, bbox_inches="tight", dpi=300)
out("wrote", OUT)
LOG.close()
