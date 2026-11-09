"""Fig. 3.8: silicon bands near the gap in LDA, with quasiparticle corrections and from experiment (Sect. 3.4).
Output: tex/figures/ch03/fig3_8.pdf. Prints the model numbers quoted in the caption and in Sect. 3.4.

Panel (a). Solid: LDA Kohn-Sham bands from qe_ch03.py ("lda" stage; cache qe_si_lda.npz): Quantum ESPRESSO 7.6,
input_dft = 'pz' (Slater exchange + Perdew-Zunger 1981 correlation) on the SG15 Si_ONCV_PBE-1.2.upf pseudopotential
(generated with PBE: functional mismatch in the core region, stated in the caption), 60 Ry, Gamma-centred 12^3 grid,
a = 5.431 A, no spin-orbit coupling; checks at 80 Ry and on a 16^3 grid (printed below).
Dashed: the same conduction bands shifted rigidly by Delta_scis = 1.17 eV - E_g(LDA model) (scissor; modelling choice).
Squares: one-shot G0W0 quasiparticle energies of Rideau et al., cond-mat/0607510, Table II (Gamma states) and Table VI
(L, X states; minimum gap E_g(Delta) = 1.076 eV), with spin-orbit coupling; SO splittings (< 0.05 eV) not resolved.
Circles: measured energies listed in the "Exp." columns of the same tables (each listed value plotted):
  Gamma_15: 3.4, 3.35, 3.05; Gamma_2': 4.15, 4.1, 4.185, 4.21 (Table II)
  L_3' (valence): -1.5, -1.2; L_1: 2.06, 2.1, 2.4; L_3: 3.9, 4.15; X_4 (valence): -2.5, -2.9, -3.3; X_1: 1.13, 1.25, 1.3
  minimum gap at 0.85 X: 1.17 (Table VI; = Ramanathan and Kurinsky Eq. (11), 1.1692 eV)
Panel (b). Minimum gap of silicon from different calculations (the two QE values of this book: LDA of panel (a) and
PBE of Fig. 3.6, both at 5.431 A, plotted with the literature values), with the threshold mass m_min = 2E_g/v_max^2
(Eq. (1.3-mmin), v_max = 2.650e-3, v_max^2 = 7.023e-6) on the right axis:
  LDA 0.52 eV (Aryasetiawan and Gunnarsson, cond-mat/9712013, Table I); PBE 0.602 eV at a_PBE = 5.477 A and
  0.557 eV at 5.431 A (representative calculation of App. E.1, worked example we:E-si-bands); HSE 1.22 eV
  (Lucero et al., 1111.4515, Table I); G0W0 from LDA 1.29 (Hybertsen and Louie 1986), 1.24 (Godby et al. 1988),
  1.25 (Rohlfing et al. 1993), as collected in Aryasetiawan and Gunnarsson Table I; G0W0 converged 1.10 eV
  (Klimes et al. 2014, Sect. IV C); measured 1.17 eV.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch03", "fig3_8.pdf")
EG_MEAS = 1.17
VMAX2 = 7.023e-6

d = np.load(os.path.join(HERE, "qe_si_lda.npz"))
eb = d["bands"]
xp, ticks = d["xp"], list(d["ticks"])
iG = int(np.argmin(np.linalg.norm(d["kp"], axis=1)))
vbm = eb[iG, 3]
assert np.allclose(eb[iG, 1:4], vbm, atol=1e-4)
e = eb - vbm


def edges(ch):
    """Gap, k_c and conduction energies at Gamma, X, L from a check run: k = Gamma, L, X, then G-X 0.70..1.00."""
    v = ch[0, 3]
    G15, L1, X1 = ch[0, 4] - v, ch[1, 4] - v, ch[2, 4] - v
    s = np.round(np.arange(0.70, 1.0000001, 0.005), 6)
    cb = ch[3:, 4] - v
    j = int(np.argmin(cb))
    c = np.polyfit(s[j - 4:j + 5] - s[j], cb[j - 4:j + 5], 2)
    kc = s[j] - c[1] / (2 * c[0])
    return np.polyval(c, kc - s[j]), kc, G15, X1, L1


Eg, kc, G15, X1, L1 = edges(d["lda_chk"])
scis = EG_MEAS - Eg
print(f"LDA (QE, SG15-PBE pseudopotential, 60 Ry, 12^3): E_g = {Eg:.3f} eV at k_c = {kc:.3f} (2pi/a); "
      f"Gamma_15 = {G15:.3f}, X_1 = {X1:.3f}, L_1 = {L1:.3f}; Gamma_2' = {e[iG, 7]:.3f}; X_4v = {e[-1, 2]:.3f}; "
      f"L_3'v = {e[0, 2]:.3f} eV; scissor {scis:.3f} eV")
chk = {}
for name in ("lda80", "lda16", "pbe16"):
    r = edges(d[name + "_chk"])
    chk[name] = r
    print(f"  check {name}: E_g = {r[0]:.4f} at k_c = {r[1]:.3f}; Gamma_15 {r[2]:.3f}, X_1 {r[3]:.3f}, L_1 {r[4]:.3f}")
print(f"  80 Ry - 60 Ry: E_g {1e3*(chk['lda80'][0]-Eg):+.1f} meV; 16^3 - 12^3: {1e3*(chk['lda16'][0]-Eg):+.1f} meV")
EG_PBE = chk["pbe16"][0]
_p = np.load(os.path.join(HERE, "qe_si_pbe.npz"))
_s = _p["scan_e"][:61, 4] - _p["bands"][int(np.argmin(np.linalg.norm(_p["kp"][:100], axis=1))), 3]
_j = int(np.argmin(_s))
_c = np.polyfit(np.arange(-4, 5) * 0.005, _s[_j - 4:_j + 5], 2)
EG_PBE12 = np.polyval(_c, -_c[1] / (2 * _c[0]))
print(f"PBE at 5.431 A (Fig. 3.6 calculation, 12^3): E_g = {EG_PBE12:.4f}; with a 16^3 density {EG_PBE:.4f}")
# pseudopotential-functional mismatch: Troullier-Martins pair generated in LDA and in PBE (qe_ch03.py "tm")
_t = np.load(os.path.join(HERE, "qe_si_tm.npz"))
tmg = {}
for f in ("lda", "pbe"):
    ch = _t["tm_" + f]
    tmg[f] = edges(ch)[0]
print(f"  TM pair: E_g(LDA) - E_g(PBE) = {tmg['lda'] - tmg['pbe']:+.3f} eV (consistent potentials); "
      f"with the PBE-generated SG15 potential: {Eg - EG_PBE:+.3f} eV")
# quasiparticle minus LDA differences quoted in the text
gw = {"Gamma_15": 3.204, "X_1": 1.221, "L_1": 2.095, "E_g": 1.076}
lda = {"Gamma_15": G15, "X_1": X1, "L_1": L1, "E_g": Eg}
print("G0W0 - LDA:", {k: round(gw[k] - lda[k], 3) for k in gw})
def close(x, q, tol, name):
    assert abs(x - q) <= tol, f"{name}: {x} vs {q}"
    print(f"  {name:50s} {x:.4f} (quoted {q})")
close(Eg, 0.40, 5e-3, "LDA gap"); close(kc, 0.848, 1e-3, "LDA k_c"); close(G15, 2.51, 5e-3, "Gamma_15")
close(X1, 0.53, 5e-3, "X_1"); close(L1, 1.43, 5e-3, "L_1"); close(scis, 0.77, 5e-3, "scissor")
close(min(gw[k] - lda[k] for k in ("Gamma_15", "X_1", "L_1")), 0.66, 5e-3, "G0W0 - LDA, smallest (conduction states)")
close(max(gw[k] - lda[k] for k in ("Gamma_15", "X_1", "L_1")), 0.70, 5e-3, "G0W0 - LDA, largest")
close(tmg["lda"] - tmg["pbe"], -0.06, 5e-3, "TM pair LDA - PBE"); close(Eg - EG_PBE, -0.155, 5e-3, "SG15 LDA - PBE")
close(EG_PBE12, 0.557, 5e-4, "PBE gap (Fig. 3.6)")

x = xp
xL, xG, xX = ticks[0], ticks[1], ticks[2]
xc = xG + kc

plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.4, 3.4), gridspec_kw={"width_ratios": [1.45, 1], "wspace": 0.55})
for b in range(eb.shape[1]):
    ax.plot(x, e[:, b], color="k" if b < 4 else "C0", lw=1.0)
    if b >= 4:
        ax.plot(x, e[:, b] + scis, color="C0", lw=0.9, ls="--")
for t in (xL, xG, xX):
    ax.axvline(t, color="0.8", lw=0.5, zorder=0)
ax.axhline(0, color="0.6", lw=0.5, ls=":")
# G0W0 (Rideau Tables II, VI)
gwpts = [(xG, 3.204), (xG, 3.96), (xL, -1.216), (xL, 2.095), (xL, 3.962), (xX, -2.92), (xX, 1.221), (xG + 0.85, 1.076)]
exppts = [(xG, v) for v in (3.4, 3.35, 3.05, 4.15, 4.1, 4.185, 4.21)] + \
         [(xL, v) for v in (-1.5, -1.2, 2.06, 2.1, 2.4, 3.9, 4.15)] + \
         [(xX, v) for v in (-2.5, -2.9, -3.3, 1.13, 1.25, 1.3)] + [(xG + 0.85, 1.17)]
ax.plot(*zip(*gwpts), "s", mfc="none", mec="C3", ms=5, mew=1.0, label=r"$G_0W_0$", clip_on=False)
ax.plot(*zip(*exppts), "o", color="C2", ms=3, label="measured", clip_on=False)
ax.plot([], [], color="k", lw=1.0, label="LDA")
ax.plot([], [], color="C0", lw=0.9, ls="--", label="LDA + scissor")
ax.set_xticks([xL, xG, xX], ["L", r"$\Gamma$", "X"])
ax.set_xlim(xL, xX)
ax.set_ylim(-4, 5)
ax.set_ylabel(r"energy $-$ VBM (eV)")
ax.legend(loc="lower left", fontsize=7, frameon=True, framealpha=0.9, handlelength=1.6)
ax.text(0.02, 0.97, "(a)", transform=ax.transAxes, va="top")

# panel (b): gaps and threshold masses
rows = [("LDA", [0.52, round(Eg, 3)]), ("PBE", [round(EG_PBE12, 3), 0.602]), (r"$G_0W_0$", [1.24, 1.25, 1.29]),
        (r"$G_0W_0$ conv.", [1.10]), ("HSE", [1.22]), ("measured", [1.17])]
for i, (lab, vals) in enumerate(rows):
    col = "C2" if lab == "measured" else ("C0" if lab in ("LDA", "PBE") else "C3")
    bx.plot([i] * len(vals), vals, "o", color=col, ms=4)
    if len(vals) > 1:
        bx.plot([i, i], [min(vals), max(vals)], color=col, lw=1.0)
bx.axhline(EG_MEAS, color="C2", lw=0.6, ls="-.")
bx.set_xticks(range(len(rows)), [r[0] for r in rows], rotation=50, ha="right", fontsize=7.5)
bx.set_xlim(-0.6, len(rows) - 0.4)
bx.set_ylim(0, 1.5)
bx.set_ylabel(r"minimum gap $E_{\mathrm{g}}$ (eV)")
rx = bx.twinx()
rx.set_ylim(0, 2 * 1.5 / VMAX2 / 1e6)
rx.set_ylabel(r"$m_{\mathrm{min}} = 2E_{\mathrm{g}}/v_{\mathrm{max}}^2$ (MeV)")
bx.text(0.04, 0.97, "(b)", transform=bx.transAxes, va="top")
for E in (0.52, 1.17):
    print(f"m_min({E}) = {2 * E / VMAX2 / 1e6:.3f} MeV")
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
