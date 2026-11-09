"""Fig. 5.6: three-phonon decay channels of the zone-center optical phonon of silicon (Sect. 5.7, WE 5.9).
Output: tex/figures/ch05/fig5_6.pdf. Prints every number of the figure and of the text that comes from this model.

Phonons: the PBE force constants of Sect. 5.2 (fig5_6_fc.npz from fig5_6_data.py; DFPT on a 6^3 grid, a = 5.431 A),
Fourier-interpolated by si_ifc.py (Wigner-Seitz weights, on-site acoustic sum rule; agrees with the matdyn dispersion of
Fig. 5.2 to 0.03 meV). Branches are labeled by energy order: the lowest two TA, the third LA, the upper three optical
(the labeling used by Debernardi, Baroni and Molinari, arXiv cond-mat/9408051).

MODELLING CHOICE (stated in the caption): constant vertex. The decay of the Gamma optical phonon (omega0) produces pairs
(Q nu1, -Q nu2) with omega_Q nu1 + omega_Q nu2 = omega0. We compute the two-phonon density of final states
   D2 = (1/N) sum_Q sum_{nu1 nu2} delta(omega0 - omega_Q nu1 - omega_Q nu2)
and its decomposition rho(omega1) by the energy omega1 of one member of the pair, on a shifted uniform N_g^3 grid of the
first zone with Gaussian delta functions of width SIG. With a constant three-phonon vertex the width is proportional to
D2, the channel fractions are the fractions of D2, and the temperature factor of the width is the D2-weighted average of
1 + n1 + n2. The model does not give the absolute width (that needs Phi^(3)); the full-vertex LDA result is quoted from
Debernardi et al., Table 1 (FWHM 1.43 cm^-1; channels LA+TA 94.3 %, LA+LA 5.7 %).
No coalescence term: omega0 is the highest phonon energy of silicon (checked below), so omega0 + omega1 = omega2 has no
solution. Klemens's model (Phys. Rev. 148, 845 (1966)): both daughters at omega0/2, factor 1 + 2 n_B(omega0/2).
Colors: the three categorical colors of Fig. 5.3 (#2a6fb0, #c4661f, #8a4fa0; dataviz validator, light surface: all checks
pass); the optical branches are drawn in the neutral gray #8c8c8c, deliberately achromatic (context, not a series), which
the validator flags only on the chroma floor (CVD and normal-vision separation from the purple pass).
Run: python fig5_6.py   (numpy, matplotlib; about two minutes)
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from si_ifc import phonons, check_path            # noqa: E402
from fig5_2_qpath import segments                  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch05", "fig5_6.pdf")
CACHE = os.path.join(HERE, "fig5_6_grid.npz")
KB = 8.617333262e-2          # meV/K
NG, SIG = 80, 0.25           # grid N_g^3 and Gaussian width (meV): modelling choices
BREC = np.array([[-1, -1, 1], [1, 1, 1], [-1, 1, -1]], float)   # reciprocal vectors of the fcc cell (2pi/a)


def nB(w, T):
    if T <= 0:
        return 0.0
    with np.errstate(over="ignore"):
        return 1.0 / np.expm1(w / (KB * T))


print("interpolation check, max |dev| from Fig. 5.2 path (meV): all %.3f, away from Gamma %.3f" % check_path())
w0 = phonons([[0, 0, 0]])[0][0, 3]
print("omega0 (PBE) = %.2f meV" % w0)

if os.path.exists(CACHE) and int(np.load(CACHE)["ng"]) == NG:
    W = np.load(CACHE)["W"]
else:
    t = (np.arange(NG) + 0.5) / NG
    q = np.array(np.meshgrid(t, t, t, indexing="ij")).reshape(3, -1).T @ BREC
    W = np.vstack([phonons(q[c:c + 20000])[0] for c in range(0, len(q), 20000)])
    np.savez(CACHE, W=W, ng=NG)
print("grid %d^3, max phonon energy %.2f meV (omega0 is the top: %s)" % (NG, W.max(), W.max() <= w0 + 1e-3))
print("max TA energy in the zone %.2f meV vs omega0/2 = %.2f meV; LA range %.2f-%.2f; lowest optical %.2f meV"
      % (W[:, 1].max(), w0 / 2, W[:, 2].min(), W[:, 2].max(), W[:, 3].min()))

gauss = lambda x: np.exp(-0.5 * (x / SIG) ** 2) / (SIG * np.sqrt(2 * np.pi))
lab = ["TA", "TA", "LA", "O", "O", "O"]
pairs, weights = [], []
for i in range(6):
    for j in range(6):
        g = gauss(w0 - W[:, i] - W[:, j])
        m = g > 1e-12
        pairs.append((i, j, W[m, i], W[m, j], g[m] / len(W)))
D2 = sum(p[4].sum() for p in pairs)
chan = {}
for i, j, _, _, g in pairs:
    key = "+".join(sorted([lab[i], lab[j]], key=lambda s: ["LA", "TA", "O"].index(s)))
    chan[key] = chan.get(key, 0.0) + g.sum()
print("two-phonon density of final states D2 = %.4f per meV (sigma %.2f meV)" % (D2, SIG))
for k, v in sorted(chan.items(), key=lambda kv: -kv[1]):
    print("  channel %-6s %5.1f %%" % (k, 100 * v / D2))
# characteristic energies of the dominant LA+TA pairs
la_ta = [(p[2], p[3], p[4]) for p in pairs if {lab[p[0]], lab[p[1]]} == {"LA", "TA"} and lab[p[0]] == "TA"]
wt = np.concatenate([x[0] for x in la_ta]); gg = np.concatenate([x[2] for x in la_ta])
print("LA+TA pairs: mean TA energy %.1f meV, mean LA energy %.1f meV" % ((wt * gg).sum() / gg.sum(), w0 - (wt * gg).sum() / gg.sum()))

Ts = np.linspace(0, 800, 161)
Fmod = np.array([sum((p[4] * (1 + nB(p[2], T) + nB(p[3], T))).sum() for p in pairs) / D2 for T in Ts])
Fkl = np.array([1 + 2 * nB(w0 / 2, T) for T in Ts])
for T in (0.01, 77, 300, 600):
    fm = sum((p[4] * (1 + nB(p[2], T) + nB(p[3], T))).sum() for p in pairs) / D2
    print("T = %6.2f K: constant-vertex factor %.3f, Klemens 1+2n(omega0/2) %.3f" % (T, fm, 1 + 2 * nB(w0 / 2, T)))

# spectral decomposition rho(omega1) by the branch of phonon 1, and the one-phonon DOS
wax = np.linspace(0, w0, 641)
rho = {"TA": np.zeros_like(wax), "LA": np.zeros_like(wax), "O": np.zeros_like(wax)}
for i, j, wi, wj, g in pairs:
    h, _ = np.histogram(wi, bins=len(wax) - 1, range=(0, w0), weights=g)
    rho[lab[i]][:-1] += h / (wax[1] - wax[0])
gph, _ = np.histogram(W.ravel(), bins=len(wax) - 1, range=(0, w0))
gph = np.append(gph / len(W) / (wax[1] - wax[0]), 0.0)
sm = lambda y: np.convolve(y, np.ones(9) / 9, mode="same")   # 0.9 meV running mean (display only)
print("one-phonon DOS at omega0/2: %.3f per meV per cell; its maximum %.3f" % (sm(gph)[np.argmin(abs(wax - w0 / 2))], sm(gph).max()))

# ---------------- figure
plt.rcParams.update({"font.size": 8, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
                     "font.family": "serif", "mathtext.fontset": "cm"})
BLUE, ORANGE, PURPLE, GRAY = "#2a6fb0", "#c4661f", "#8a4fa0", "#8c8c8c"
col = {"TA": BLUE, "LA": ORANGE, "O": GRAY}
fig = plt.figure(figsize=(6.3, 2.6))
axa = fig.add_axes([0.065, 0.15, 0.36, 0.72])
axb = fig.add_axes([0.475, 0.15, 0.22, 0.72])
axc = fig.add_axes([0.765, 0.15, 0.22, 0.72])

dl, sg, lm, _ = segments()
qp = np.array(dl + sg + lm)
wp = phonons(qp)[0]
ls, lL = np.sqrt(2), np.sqrt(3) / 2
x = np.concatenate([np.linspace(0, 1, len(dl)), 1 + np.linspace(0, ls, len(sg)), 1 + ls + np.linspace(0, lL, len(lm))])
cuts = np.cumsum([len(dl), len(sg)])
for seg in np.split(np.arange(len(x)), cuts):
    for b in range(6):
        axa.plot(x[seg], wp[seg, b], color=col[lab[b]], lw=1.0)
    for b in range(3):
        axa.plot(x[seg], w0 - wp[seg, b], color=col[lab[b]], lw=0.7, ls=(0, (3, 2)))
axa.axhline(w0 / 2, color="0.35", lw=0.6, ls=":")
axa.text(0.03, w0 / 2 + 1.2, r"$\omega_{\mathrm{opt}}/2$", fontsize=7, color="0.25")
ticks = [0, 1, 1 + ls / 4, 1 + ls, 1 + ls + lL]
axa.set_xticks(ticks); axa.set_xticklabels([r"$\Gamma$", r"X$\,|\,$X$'$", "K", r"$\Gamma$", "L"])
for t in ticks[1:-1]:
    axa.axvline(t, color="0.85", lw=0.5, zorder=0)
axa.set_xlim(0, ticks[-1]); axa.set_ylim(0, 68)
axa.set_ylabel(r"$\omega$ (meV)")
axa.plot([], [], color=BLUE, lw=1.0, label="TA"); axa.plot([], [], color=ORANGE, lw=1.0, label="LA")
axa.plot([], [], color=GRAY, lw=1.0, label="optical"); axa.plot([], [], color="0.3", lw=0.7, ls=(0, (3, 2)), label=r"$\omega_{\mathrm{opt}}-\omega$")
axa.legend(loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=4, frameon=False, fontsize=6.5, handlelength=1.8)
axa.text(-0.12, 1.02, "(a)", transform=axa.transAxes, fontsize=8)

for k in ("TA", "LA", "O"):
    axb.plot(sm(rho[k]), wax, color=col[k], lw=1.0)
scale = 0.8 * max(sm(rho["TA"]).max(), sm(rho["LA"]).max()) / sm(gph).max()
axb.fill_betweenx(wax, 0, scale * sm(gph), color="0.88", lw=0, zorder=0)
axb.axhline(w0 / 2, color="0.35", lw=0.6, ls=":")
axb.set_ylim(0, 68); axb.set_xlim(left=0)
axb.set_xlabel(r"$\rho_{\mathrm{pair}}(\omega_1)$ (meV$^{-2}$)"); axb.tick_params(labelleft=False)
axb.text(0.5, 0.17, "TA", color=BLUE, transform=axb.transAxes, fontsize=7)
axb.text(0.5, 0.11, "LA", color=ORANGE, transform=axb.transAxes, fontsize=7)
axb.text(0.5, 0.05, r"$g_{\mathrm{ph}}$ (scaled)", color="0.45", transform=axb.transAxes, fontsize=7)   # in the empty bottom corner, off the DOS peaks
axb.text(-0.08, 1.02, "(b)", transform=axb.transAxes, fontsize=8)

axc.plot(Ts, Fmod, color=PURPLE, lw=1.2, label="constant vertex")
axc.plot(Ts, Fkl, color="0.2", lw=1.0, ls=(0, (3, 2)), label="Klemens")
axc.axvline(300, color="0.85", lw=0.5, zorder=0)
axc.set_xlim(0, 800); axc.set_ylim(0.9, max(Fmod.max(), Fkl.max()) * 1.05)
axc.set_xlabel(r"$T$ (K)"); axc.set_ylabel(r"$\gamma^{\mathrm{anh}}(T)/\gamma^{\mathrm{anh}}(0)$")
axc.legend(loc="upper left", frameon=False, fontsize=6.5, handlelength=1.8)
axc.text(-0.3, 1.02, "(c)", transform=axc.transAxes, fontsize=8)
fig.savefig(OUT)
print("wrote", os.path.relpath(OUT, HERE))
