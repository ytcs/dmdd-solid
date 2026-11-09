"""Fig. 3.6: silicon bands with E_g, E_dir and k_c marked, and the minimum pair energy E_min(q) (Sect. 3.3).
Output: tex/figures/ch03/fig3_6.pdf. Prints and asserts the numbers of Sect. 3.3 that come from the figure, the
k.p effective-mass check (empirical model, text only) and worked example 3.5.

Bands: the book's representative first-principles calculation (App. E.1) at the measured lattice constant, run by
qe_ch03.py (cache qe_si_pbe.npz): Quantum ESPRESSO 7.6, PBE, SG15 norm-conserving Si_ONCV_PBE-1.2.upf, 60 Ry,
Gamma-centred 12^3 grid for the density, a = 5.431 A, no spin-orbit coupling; bands non-self-consistently on the path
(80 points per segment), on a fine Gamma-X scan (step 0.005 (2pi/a)) with transverse lines through the valley, and on
the full 48^3 grid k = sum_i m_i b_i / 48 (2769 points inequivalent under O_h, unfolded).

E_min(q) = min over k of [eps_5(k+q) - eps_4(k)] (lowest conduction band minus highest valence band) on the 48^3 grid,
with q on the same grid along [100], [110] and [111]. Modelling choice for panel (b): the PBE indirect gap is moved to
the measured low-temperature gap 1.17 eV (Ramanathan and Kurinsky, Eq. (11), E_g(0) = 1.1692 eV) by a rigid upward
shift of the conduction bands (scissor, Sect. 3.4), so that the reach curves are compared with the measured gap. The
shape of E_min(q) is that of the PBE bands.

Text check (not used in the figure): the k.p mass sum over all bands is exact only for a local potential, so it is
demonstrated in the empirical pseudopotential of Cohen and Bergstresser (1966), epm.py (113 plane waves), whose
velocity operator is p/m_e.

Measured values quoted in captions/text (not used in the calculation):
  a = 5.431 A (CODATA 2022, Sect. 3.1); E_g(0) = 1.17 eV (Ramanathan and Kurinsky Eq. (11)); E_dir = Gamma_15 =
  3.4 eV and L 3.45 eV (Rideau et al., cond-mat/0607510, Tables II, VI); k_c = 0.85 (2pi/a) (Feher 1959);
  m_l = 0.9163, m_t = 0.1905 (Hensel et al. 1965, as listed in Rideau et al. Table VII). v_max = 2.650e-3 (Sect. 1.2).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from epm import EPM, HBARC              # noqa: E402  (sets single-threaded BLAS before numpy loads)
import numpy as np                      # noqa: E402
import matplotlib                       # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt         # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ME = 510998.95            # eV
VMAX = 2.650e-3
EG_MEAS = 1.17            # eV, low temperature
A_MEAS = 5.431            # Angstrom
G1 = 2 * np.pi * HBARC / A_MEAS     # 2pi/a in eV


def close(x, q, tol, name):
    assert abs(x - q) <= tol, f"{name}: computed {x} vs quoted {q}"
    print(f"  {name:58s} {x:.4f}   (quoted {q})")


d = np.load(os.path.join(HERE, "qe_si_pbe.npz"))
assert abs(float(d["a"]) - A_MEAS) < 1e-9
kp, xp, ticks, eb = d["kp"], d["xp"], list(d["ticks"]), d["bands"]
iG = int(np.argmin(np.linalg.norm(kp[:100], axis=1)))
vbm = eb[iG, 3]
assert np.allclose(eb[iG, 1:4], vbm, atol=1e-4), "threefold valence-band maximum at Gamma"
assert eb[:, 3].max() <= vbm + 1e-4, "VBM at Gamma"
e = eb - vbm

# ---- band edges from the fine scan ------------------------------------------------------------------------------
sk, se = d["scan_k"], d["scan_e"] - vbm
nline = 61
s, cb = sk[:nline, 0], se[:nline, 4]
j = int(np.argmin(cb))
win = slice(j - 4, j + 5)                                 # nine points within +-0.02 (2pi/a), as in App. E.1
c = np.polyfit(s[win] - s[j], cb[win], 2)
kc = s[j] - c[1] / (2 * c[0])
Eg = np.polyval(c, kc - s[j])
ml = G1 ** 2 / (2 * c[0]) / ME
tr = sk[nline:].reshape(4, 9, 3)
te = se[nline:, 4].reshape(4, 9)
it = int(np.argmin(np.abs(tr[:, 0, 0] - kc)))
ct = np.polyfit(tr[it, :, 1], te[it], 2)
mt = G1 ** 2 / (2 * ct[0]) / ME
Edir_G = e[iG, 4]
iX = int(np.argmin(np.linalg.norm(kp - np.array([1.0, 0, 0]), axis=1)))
iL = 0
print(f"PBE (QE, a = {A_MEAS}): CBM on Gamma-X at k_c = {kc:.4f} (2pi/a), E_g = {Eg:.4f} eV; m_l = {ml:.3f}, "
      f"m_t = {mt:.3f} (curvature, nine points, transverse line at {tr[it, 0, 0]:.3f})")
print(f"  Gamma_15c - Gamma_25'v = {Edir_G:.3f}; X_1c = {e[iX, 4]:.3f}; L_1c = {e[iL, 4]:.3f}; Gamma_2'c = {e[iG, 7]:.3f}; "
      f"valence width {-e[iG, 0]:.2f} eV")
edir_path = np.min(e[:, 4] - e[:, 3])
ip = int(np.argmin(e[:, 4] - e[:, 3]))
print(f"  smallest vertical gap on the path {edir_path:.3f} eV at k = {np.round(kp[ip], 3)}; on the 48^3 grid "
      f"{float(d['grid_edir']):.3f} eV; vertical gap at L {e[iL, 4] - e[iL, 3]:.3f} eV")
scis = EG_MEAS - Eg
print(f"  scissor to the measured gap: {scis:.3f} eV")

# ---- E_min(q) on the grid ---------------------------------------------------------------------------------------
Emin = {n: (d["q" + n], d["E" + n] - 0.0) for n in ("[100]", "[110]", "[111]")}
q100, E100 = Emin["[100]"]
assert abs(E100[0] - float(d["grid_edir"])) < 1e-9
assert abs(E100[-1] - E100[0]) < 1e-6, "q -> q + G_200 leaves E_min unchanged"
print(f"grid {int(d['N'])}^3: CBM on the grid {float(d['grid_c5_min']) - vbm:.4f} eV (grid points miss k_c by "
      f"< 0.021 (2pi/a)); [100] minimum of E_min {E100.min() + scis:.3f} eV (scissored) at q = "
      f"{q100[np.argmin(E100)] / 1e3:.3f} keV")

# ---- worked example 3.5 (measured a, measured gap) --------------------------------------------------------------
qc = 0.85 * G1
print(f"WE 3.5: 2pi/a = {G1:.1f} eV; q_c = 0.85 (2pi/a) = {qc:.0f} eV")
mchi = 1e6
disc = (mchi * VMAX) ** 2 - 2 * mchi * EG_MEAS
qlo, qhi = mchi * VMAX - np.sqrt(disc), mchi * VMAX + np.sqrt(disc)
wmax = qc * VMAX - qc ** 2 / (2 * mchi)
print(f"  m = 1 MeV: window q = {qlo:.0f} .. {qhi:.0f} eV at omega = 1.17 eV; omega_max(q_c) = {wmax:.3f} eV; "
      f"2 m v_max = {2*mchi*VMAX:.0f} eV")
mneed = qc ** 2 / (2 * (qc * VMAX - EG_MEAS))
mmin = 2 * EG_MEAS / VMAX ** 2
qstar = mmin * VMAX
print(f"  smallest mass that deposits E_g at q = q_c: {mneed/1e6:.3f} MeV; m_min = 2E_g/v^2 = {mmin/1e6:.3f} MeV "
      f"at q* = {qstar:.0f} eV = {qstar/G1:.2f} (2pi/a)")
Eq_star = np.interp(qstar, q100, E100) + scis
print(f"  scissored PBE E_min([100]) at q* = {Eq_star:.3f} eV (> E_g)")
res = {}
for name, (qs, es) in Emin.items():
    jm = np.argmin(es)
    res[name] = (es[jm] + scis, qs[jm])
    print(f"  {name}: min scissored E_min = {es[jm]+scis:.3f} eV at q = {qs[jm]/1e3:.2f} keV; "
          f"E_min(0) = {es[0]+scis:.3f} eV; at q = 2.57 keV: {np.interp(2570, qs, es)+scis:.3f} eV; "
          f"max over q <= 2.57 keV of E_min: {np.max(es[qs <= 2570] + scis):.3f}")
for name, (qs, es) in Emin.items():
    E = es + scis
    ok = qs * VMAX > E
    mreq = np.where(ok, qs ** 2 / (2 * np.where(ok, qs * VMAX - E, 1)), np.inf)
    jm = np.argmin(mreq)
    print(f"  {name}: lightest mass reaching E_min(q) on the grid: {mreq[jm]/1e6:.3f} MeV at q = {qs[jm]/1e3:.2f} keV "
          f"(E_min = {E[jm]:.2f} eV)")

# ---- text check: k.p mass sum in the empirical (local) pseudopotential -----------------------------------------
epm = EPM("Si", ecut=21)
unit = 2 * np.pi * HBARC / epm.a
h = 0.004
e5 = lambda k: epm.bands(np.asarray(k, float), nb=5)[4]
sline = np.linspace(0.70, 1.0, 3001)
k0 = np.array([sline[np.argmin(epm.bands(sline[:, None] * np.array([1.0, 0, 0]), nb=5)[:, 4])], 0, 0])
f = [e5(k0 + dd * np.array([h, 0, 0])) for dd in (-1, 0, 1)]
k0 = k0 + np.array([0.5 * h * (f[0] - f[2]) / (f[0] - 2 * f[1] + f[2]), 0, 0])
c0 = e5(k0)
ml_e = 1 / (ME * (e5(k0 + [h, 0, 0]) - 2 * c0 + e5(k0 - [h, 0, 0])) / (h * unit) ** 2)
mt_e = 1 / (ME * (e5(k0 + [0, h, 0]) - 2 * c0 + e5(k0 - [0, h, 0])) / (h * unit) ** 2)
w, vel = epm.velocity(k0)
dE = w[4] - w
mask = np.abs(dE) > 1e-6
inv_l = 1 + 2 * ME * np.sum(np.abs(vel[0, :, 4][mask]) ** 2 / dE[mask])
inv_t = 1 + 2 * ME * np.sum(np.abs(vel[1, :, 4][mask]) ** 2 / dE[mask])
terms = 2 * ME * np.abs(vel[1, :, 4]) ** 2 / np.where(mask, dE, np.inf)
jt = int(np.argmax(np.abs(terms)))
print(f"empirical model (text check): k_c = {k0[0]:.3f}; m_l = {ml_e:.3f}, m_t = {mt_e:.3f} (finite differences); "
      f"k.p sum over {len(w)} bands: {1/inv_l:.3f}, {1/inv_t:.3f}; largest transverse term: band {jt+1}, "
      f"{dE[jt]:+.2f} eV, |v| = {np.abs(vel[1, jt, 4]):.2e}, contributes {terms[jt]:.2f} of {inv_t:.2f}")
assert abs(1 / inv_l - ml_e) / ml_e < 2e-3 and abs(1 / inv_t - mt_e) / mt_e < 2e-3

print("Numbers quoted in Sect. 3.3 and the caption of Fig. 3.6")
close(kc, 0.843, 5e-4, "k_c (2pi/a)")
close(Eg, 0.557, 5e-4, "E_g PBE (eV)")
close(Edir_G, 2.56, 5e-3, "E_dir = Gamma_15c - Gamma_25'v (eV)")
close(e[iL, 4] - e[iL, 3], 2.70, 5e-3, "vertical gap at L (eV)")
close(e[iX, 4], 0.69, 5e-3, "X_1c (eV)")
close(e[iL, 4], 1.51, 5e-3, "L_1c (eV)")
close(scis, 0.61, 5e-3, "scissor (eV)")
close(ml, 0.95, 5e-3, "m_l PBE"); close(mt, 0.193, 5e-4, "m_t PBE")
close(float(d["grid_edir"]), Edir_G, 1e-6, "smallest vertical gap on the grid = Gamma")
close(Edir_G + scis, 3.17, 5e-3, "scissored E_dir = E_min(0) (eV)")
close(res["[110]"][0], 1.26, 5e-3, "[110] lowest E_min (eV)"); close(res["[110]"][1] / 1e3, 3.1, 0.05, "  at q (keV)")
close(res["[111]"][0], 2.13, 5e-3, "[111] lowest E_min (eV)")
close(Eq_star, 1.9, 0.05, "E_min([100]) at q* = 0.88 keV (eV)")
for name, (qs, es) in Emin.items():
    assert np.interp(2570, qs, es) + scis < 2570 * VMAX - 2570 ** 2 / (2 * 0.968e6), "0.968 MeV reaches every direction"
close(ml_e, 0.872, 5e-4, "empirical m_l"); close(mt_e, 0.184, 5e-4, "empirical m_t")
close(dE[jt], 3.73, 5e-3, "empirical: band below the minimum (eV)"); close(terms[jt], 2.27, 5e-3, "  its term (one of a degenerate pair; the pair gives 4.53)")
close(inv_t, 5.43, 0.01, "empirical m_e/m_t")

# ---- figure -------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.4, 3.4), gridspec_kw={"width_ratios": [1.35, 1], "wspace": 0.32})
labs = ["L", r"$\Gamma$", "X", "W", "K", r"$\Gamma$"]
for b in range(8):
    ax.plot(xp, e[:, b], color="k" if b < 4 else "C0", lw=1.0)
for t in ticks:
    ax.axvline(t, color="0.8", lw=0.5, zorder=0)
ax.set_xticks(ticks, labs)
ax.set_xlim(ticks[0], ticks[-1])
ax.set_ylim(-4, 6.5)
ax.set_ylabel(r"$\varepsilon_{n\mathbf{k}}$ $-$ VBM (eV)")
xG = ticks[1]
xc = xG + kc
ax.annotate("", xy=(xc, Eg), xytext=(xc, 0), arrowprops=dict(arrowstyle="<->", color="C3", lw=1.0))
ax.text(xc + 0.04, -0.75, r"$E_{\mathrm{g}}$", color="C3")
ax.annotate("", xy=(xG + 0.02, Edir_G), xytext=(xG + 0.02, 0), arrowprops=dict(arrowstyle="<->", color="C2", lw=1.0))
ax.text(xG + 0.06, 1.0, r"$E_{\mathrm{dir}}$", color="C2")   # below the conduction band
ax.plot([xc], [Eg], "o", color="C3", ms=3)
ax.axvline(xc, color="C3", lw=0.6, ls="--", ymax=0.45)
ax.text(xc + 0.03, -3.7, r"$k_{\mathrm{c}}$", color="C3")
ax.axhline(0, color="0.6", lw=0.5, ls=":")
ax.text(0.02, 0.97, "(a)", transform=ax.transAxes, va="top")

colors = {"[100]": "C0", "[110]": "C1", "[111]": "C2"}
for name, (qs, es) in Emin.items():
    bx.plot(qs / 1e3, es + scis, color=colors[name], lw=1.1, label=name)
qq = np.linspace(0, 6e3, 400)
bx.plot(qq / 1e3, qq * VMAX - qq ** 2 / 2e6, color="k", ls="--", lw=0.9)
bx.plot(qq / 1e3, qq * VMAX, color="k", ls=":", lw=0.9)
bx.text(4.45, 2.45, "1 MeV", fontsize=8)
bx.text(1.25, 4.55, r"$qv_{\mathrm{max}}$", fontsize=8)
bx.axhline(EG_MEAS, color="C3", lw=0.6, ls="-.")
bx.axvline(qc / 1e3, color="0.5", lw=0.6)
bx.text(qc / 1e3 + 0.05, 0.25, r"$k_{\mathrm{c}}$", color="0.3")
bx.set_xlim(0, 5.5)
bx.set_ylim(0, 6)
bx.set_xlabel(r"$|\mathbf{q}|$ (keV)")
bx.set_ylabel(r"$E_{\mathrm{min}}(\mathbf{q})$, $\omega$ (eV)")
bx.legend(loc="upper right", fontsize=7, frameon=False, handlelength=1.5)
bx.text(0.02, 0.97, "(b)", transform=bx.transAxes, va="top")
bx.text(5.0, 1.25, r"$E_{\mathrm{g}}$", color="C3", fontsize=8)   # right end, clear of the dashed and dotted lines
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch03", "fig3_6.pdf")
fig.savefig(out, bbox_inches="tight")
print("wrote", os.path.normpath(out))
