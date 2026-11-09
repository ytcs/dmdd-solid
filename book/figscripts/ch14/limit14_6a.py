"""Limit Check 14.6a (lim:14.6a, Sect. 14.6): transverse magnetization of a polarized nuclear-spin ensemble driven by
an axion-like field.  Output tex/figures/ch14/limit14_6a.pdf, log limit14_6a.log.  Run: python limit14_6a.py (seconds).

Literature formulas (fixed drive amplitude, on resonance, linear in the drive).
  Budker et al. 1306.6089 Eq. (1): |M_perp| = M0 Omega_Rabi t for t << T2 (its envelope sin(delta t)/delta at delta -> 0,
    with d_n eps_S E* the shift of each level; see text).
  Aybas et al. 2101.01241 Eq. (1) (u = 1, homogeneous line): |M_perp| = M0 Omega_Rabi T2 for t >> T2.
  Both are limits of the linearized Bloch solution with a fixed drive, |M_perp| = M0 Omega T2 (1 - e^{-t/T2}) on resonance
  (book eq:14.6-mperp), drawn grey.
Fuller result: the drive is the Gaussian random field of the standard halo (coh14.py; book eq:14.6-Fphi).  Ensemble rms
  of |M_perp| from the same linear Bloch equation, Larmor frequency at the peak of the field line:
    <|M_perp|^2>/(M0 Omega_rms)^2 = int dx F(x) |1 - e^{-(iD + 1/T2) t}|^2/(D^2 + 1/T2^2),   D = x_Lar - x
  (Omega_rms: Rabi frequency of a fixed field with the mean energy density, amplitude sqrt(2 rho_chi)/m_phi).
  Two spin coherence times: T2 = 10 t_coh (long-T2 solid with decoupling) and T2 = 0.1 t_coh.
  Monte Carlo check: 1500 realizations of 2000 plane-wave modes, exact convolution, at six times (T2 = 10 t_coh).
Plotted: y = rms |M_perp|/(M0 Omega_rms T2) against x = t/t_coh.
Shaded: x where the Gaussian-field rms is within 10 % of the fixed-drive formula for T2 = 10 t_coh.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import coh14 as C

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch14")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "limit14_6a.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


x = np.logspace(-3, 3, 241)
res = {}
for T2 in (10.0, 0.1):
    fixed = 1.0 - np.exp(-x / T2)
    gauss = np.array([np.sqrt(C.bloch_ms(t, T2, C.X_PEAK)) / T2 for t in x])
    res[T2] = (fixed, gauss)
    r = gauss / fixed
    out(f"T2 = {T2} t_coh: Gaussian rms / fixed drive at t/t_coh = 0.01, 0.1, 0.3, 1, 3, 10, 100:",
        ", ".join(f"{np.interp(np.log(v), np.log(x), r):.3f}" for v in (0.01, 0.1, 0.3, 1, 3, 10, 100)))
    out(f"   saturated rms / (M0 Omega T2) = {gauss[-1]:.4f}")

fixed10, gauss10 = res[10.0]
ok = np.abs(gauss10 / fixed10 - 1) <= 0.1
x10 = x[np.argmin(ok) - 1]
out(f"T2 = 10 t_coh: within 10 % of the fixed drive for t <= {x10:.3g} t_coh")
# long-time limit for T2 >> t_coh: rms -> Omega sqrt(pi F(x_peak) T2) in M0 units (golden-rule balance)
for T2 in (10.0, 100.0, 1000.0):
    sat = np.sqrt(C.bloch_ms(50 * T2, T2, C.X_PEAK))
    out(f"T2 = {T2:6.0f} t_coh: saturated rms/(M0 Omega) = {sat:.4f}; sqrt(pi F_peak T2) = {np.sqrt(np.pi*C.F_PEAK*T2):.4f}")
# random walk regime t_coh << t << T2: rms ~ Omega sqrt(2 pi F_peak t)? check coefficient
for t in (30.0, 100.0):
    T2 = 1e5
    out(f"t = {t} t_coh, T2 = 1e5: rms/(M0 Omega) = {np.sqrt(C.bloch_ms(t, T2, C.X_PEAK)):.4f}; "
        f"sqrt(2 pi F_peak t) = {np.sqrt(2*np.pi*C.F_PEAK*t):.4f}")

# Monte Carlo check of the Gaussian-field rms
rng = np.random.default_rng(14061)
tm = np.array([0.03, 0.3, 1.0, 3.0, 10.0, 30.0])
g = 1.0 / 10.0
acc = np.zeros(len(tm))
nreal, nmod = 1500, 2000
for r in range(nreal):
    v = C.sample_velocities(nmod, rng)
    xj = np.sum(v ** 2, axis=1) / (2 * C.V0 ** 2)
    a = np.exp(1j * rng.uniform(0, 2 * np.pi, nmod)) / np.sqrt(nmod)
    D = xj - C.X_PEAK
    m = np.array([np.sum(a * (np.exp(1j * D * t) - np.exp(-g * t)) / (g + 1j * D)) for t in tm])
    acc += np.abs(m) ** 2
mc = np.sqrt(acc / nreal) / 10.0
an = np.array([np.sqrt(C.bloch_ms(t, 10.0, C.X_PEAK)) / 10.0 for t in tm])
for t, a1, a2 in zip(tm, mc, an):
    out(f"  MC check T2 = 10: t = {t:5.2f}: MC {a1:.4f}, analytic {a2:.4f}, ratio {a1/a2:.3f}")

fig, ax = plt.subplots(figsize=(4.3, 3.0))
ax.axvspan(x.min(), x10, color="0.9", lw=0)
for T2, col in ((10.0, "C3"), (0.1, "C0")):
    fx, gs = res[T2]
    ax.loglog(x, fx, color="0.55", lw=1.0)
    ax.loglog(x, gs, color=col, lw=1.6, label=rf"Gaussian field, $T_2 = {T2:g}\,t_{{\mathrm{{coh}}}}$")
    ax.loglog(x, x / T2, color="k", lw=0.7, ls="--")
ax.axhline(1.0, color="k", lw=0.7, ls=":")
ax.plot(tm, mc, "o", ms=3.5, mfc="w", mec="C3", label="Monte Carlo")
ax.loglog([], [], color="0.55", lw=1.0, label="fixed drive")
ax.loglog([], [], color="k", lw=0.7, ls="--", label=r"$\Omega_{\mathrm{Rabi}}t$ (transient)")
ax.loglog([], [], color="k", lw=0.7, ls=":", label=r"$\Omega_{\mathrm{Rabi}}T_2$ (steady state)")
ax.set_xlim(x.min(), x.max())
ax.set_ylim(1e-4, 2.0)
ax.set_xlabel(r"$t/t_{\mathrm{coh}}$")
ax.set_ylabel(r"$|M_\perp|_{\mathrm{rms}}/(M_0\Omega_{\mathrm{Rabi}}T_2)$")
ax.legend(fontsize=6.0, frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit14_6a.pdf"))
out("wrote limit14_6a.pdf")
