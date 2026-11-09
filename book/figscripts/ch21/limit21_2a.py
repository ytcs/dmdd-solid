"""Limit Check 21.2a (lim:21.2a): the halo-independent bound for a speed-only response, eq:21.2-hib,
    eta-tilde(u0) <= min_n N_up / A_n(u0)      (Chen, Gelmini, Takhistov arXiv:2105.08101 Sect. 2 for electrons; the step
                                                columns of Bernreuther et al. arXiv:2311.04957 Eqs. (2.17)-(2.18)),
against the fuller result, the linear program over galactic-frame streams with the direction-dependent stream kernel of a
silicon crystal fixed in the laboratory and averaged over the sidereal day, as a function of the speed u0.
Output tex/figures/ch21/limit21_2a.pdf; every number in limit21_2a.log.

Set-up
  m_chi = 2 MeV, heavy mediator; exposure 1 kg yr; bins: one and two pairs of the energy-only cascade of Sect. 18.3
  (hib21.pbin; E_g = 1.160 eV, eps_eh = 3.749 eV); the three-pair bin opens only above 614 km/s at 2 MeV with a column
  250 times below the one-pair column at v_max (fig21_2.log) and never binds, so it is left out; N_up = ln 30 = 3.401 per
  bin (as fig21_2.py).
  Kernel (hib21.py): k_n(v, vhat) = K0_n(v) + sum_{l=4,6,8} K_l,n(v) Y^c_l(vhat) in crystal axes; isotropic part from the
  tabulated form factor of Essig et al., direction dependence from the model ratios a_l of Sect. 11.7 (labelled model).
  Laboratory: latitude 45 deg N, crystal [100] east, [010] north, [001] up (WE 11.8). A stream of laboratory velocity v
  (Earth-centred, non-rotating axes; v_E fixed, |v_E| = 250.5 km/s at declination 47.5 deg, no annual motion) of
  declination dec is seen along the crystal directions of local_dir(dec, H) over the hour angle H; the time-integrated count is
  k_n(v, dec) = K0 + sum_l K_l G_l(dec), G_l the sidereal-day mean of Y^c_l.  Galactic support |v + v_E| <= v_esc = 544 km/s
  (hib21.feasible).  Objective eta-tilde(u0) = int dXi Theta(|v| - u0)/|v| (laboratory speed).
  Grid: |v| from 330 km/s (below the lowest v_min with weight, 332.7 km/s) to v_max in steps of 2.5 km/s; dec in steps of 2 deg.
  u0 sampled from 340 km/s in 5 km/s steps. Between the one-pair onset 332.7 km/s and 337.5 km/s the column holds a single
  table cell of weight 151 yr (1e-17 of its value at v_max), the bound is 0.02 per yr and the LP is numerically degenerate;
  the ratio is not sampled there (stated in the text).
  LP: scipy.optimize.linprog (HiGHS), maximize, two inequality constraints; duals lambda_n = -marginals.
Leading correction: first order in the anisotropy for the bin j that binds the isotropic formula,
  Phi1 = Phi_iso [1 - min_dec sum_l K_l,j(u0) G_l(dec) / K0_j(u0)]  (min over declinations allowed at |v| = u0).
Shaded: u0 where the formula is within 10 % of the linear program (ratio found on the u0 grid of 1 km/s steps near the
  crossing by bisection on the LP).
Leakage (printed, not plotted): at u0 = 600 km/s, the coarse-grid LP (10 km/s, 6 deg) and its dual are checked on a fine grid
  (1 km/s, 0.5 deg); defect delta = max(0, -min g) + L h_fine, L the largest finite-difference gradient of g in velocity units,
  h_fine the covering radius of the fine grid; bracket Phi_h <= Phi_max <= sum lambda N_up + delta N_tot / kappa_v (eq:C.12-leak,
  eq:D.46-defect), kappa_v the smallest over the support of the largest bin kernel.
"""
import os
import sys
import numpy as np
from scipy.optimize import linprog, brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
import hib21 as B  # noqa: E402
import aniso11 as AN  # noqa: E402

M = 2e6
BINS = (1, 2)
NUP = np.log(30.0)
CK = B.CKM
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch21", "limit21_2a.pdf")
LOG = open(os.path.join(HERE, "limit21_2a.log"), "w")


def say(s):
    print(s)
    LOG.write(s + "\n")


say(f"m_chi = {M/1e6:.0f} MeV, bins {BINS}, N_up = {NUP:.4f}, exposure {B.EXPO} kg yr")
say(f"circle-average identity (App. C.3 addition theorem): max deviation {B.check_circle():.1e}")
a = B.aniso_on_table()
say("model ratios a_l on the table grid (omega <= 7.1 eV, q <= 2.84 q0): " + ", ".join(
    f"l={l}: [{a[l][:, :72].min():+.3f}, {a[l][:, :72].max():+.3f}]" for l in B.LS))


def grid(du, ddeg, umin=330.0):
    us = np.arange(umin, B.VMAX + 1e-9, du)
    if us[-1] < B.VMAX - 1e-9:
        us = np.append(us, B.VMAX)
    decs = np.radians(np.arange(-90.0, 90.0 + 1e-9, ddeg))
    K = {n: B.multipole_kernels(M, n, us, a) for n in BINS}
    G = B.daily_harmonics(decs)
    U, D = np.meshgrid(us, decs, indexing="ij")
    feas = B.feasible(U, D)
    kb = {}
    for n in BINS:
        k = K[n][0][:, None] + sum(K[n][l][:, None] * G[l][None, :] for l in B.LS)
        kb[n] = k
    return us, decs, U, D, feas, kb, K, G


def solve(us, U, feas, kb, u0):
    sel = feas & (U >= u0 - 1e-9) & (np.minimum.reduce([kb[n] for n in BINS]) >= 0)
    # streams below u0 never help the objective (f = 0 there) and only use up the bounds: drop them
    cols = np.nonzero(sel.ravel())[0]
    f = (1.0 / (U.ravel()[cols] / CK))
    Aub = np.array([kb[n].ravel()[cols] for n in BINS])
    sA, sf = 1e20, 1e3                  # scaling for the solver: y = sA x, objective f/sf
    res = linprog(-f / sf, A_ub=Aub / sA, b_ub=np.full(len(BINS), NUP), bounds=(0, None), method="highs")
    assert res.status == 0, res.message
    lam = -res.ineqlin.marginals * sf / sA
    x = res.x / sA
    return -res.fun * sf / sA, lam, cols, x


us, decs, U, D, feas, kb, K, G = grid(2.5, 2.0)
say(f"grid: {len(us)} speeds x {len(decs)} declinations, {feas.sum()} feasible points")
for l in B.LS:
    say(f"  G_{l}(dec): range [{G[l].min():+.4f}, {G[l].max():+.4f}] (crystal-frame Y^c_{l} range "
        f"[{AN.ycub(l, AN._QS).min():+.3f}, {AN.ycub(l, AN._QS).max():+.3f}])")
# positivity of the crystal-frame kernel (before the daily average) on a sphere grid
qs = AN._QS[::7]
Y = {l: AN.ycub(l, qs) for l in B.LS}
worst = np.inf
for n in BINS:
    for i, v in enumerate(us):
        if K[n][0][i] <= 0:
            continue
        kk = K[n][0][i] + sum(K[n][l][i] * Y[l] for l in B.LS)
        worst = min(worst, kk.min() / K[n][0][i])
say(f"smallest crystal-frame kernel over directions, relative to its angle average: {worst:.4f} (positive: no negative pieces)")
# largest relative anisotropy of the daily-averaged kernel
for n in BINS:
    ok = K[n][0] > 0
    rel = (kb[n][ok] - K[n][0][ok][:, None]) / K[n][0][ok][:, None]
    say(f"bin {n}: daily-averaged kernel varies with declination by {rel.min():+.4f} to {rel.max():+.4f} of its isotropic part")
    for v0 in (400, 500, 600, 700, 750, 790):
        i = np.argmin(np.abs(us - v0))
        if ok[i]:
            r = (kb[n][i] - K[n][0][i]) / K[n][0][i]
            fr = feas[i]
            say(f"   |v| = {us[i]:.1f}: allowed dec {np.degrees(decs[fr]).min():+.0f}..{np.degrees(decs[fr]).max():+.0f} deg, "
                f"relative variation over allowed dec {r[fr].min():+.4f} .. {r[fr].max():+.4f}")


def iso(u0):
    return min(NUP / B.column(M, n, u0) if B.column(M, n, u0) > 0 else np.inf for n in BINS)


def binding(u0):
    return min(BINS, key=lambda n: NUP / B.column(M, n, u0) if B.column(M, n, u0) > 0 else np.inf)


def first_order(u0):
    j = binding(u0)
    Kj = B.multipole_kernels(M, j, [u0], a)
    fr = B.feasible(u0, decs)
    corr = (sum(Kj[l][0] * G[l] for l in B.LS) / Kj[0][0])[fr].min()
    return iso(u0) * (1 - corr)


u0s = np.arange(340.0, 791.0, 5.0)
rows = []
for u0 in u0s:
    phi, lam, cols, x = solve(us, U, feas, kb, u0)
    phi_iso = iso(u0)
    phi1 = first_order(u0)
    k = x > 1e-12 * x.max()
    st = [(U.ravel()[cols][j], np.degrees(D.ravel()[cols][j])) for j in np.nonzero(k)[0]]
    rows.append((u0, phi, phi_iso, phi1, lam, st))
    say(f"u0 = {u0:.0f}: LP {phi:.4e}, formula {phi_iso:.4e} (bin {binding(u0)}), ratio LP/formula {phi/phi_iso:.4f}, "
        f"first order {phi1/phi_iso:.4f}; lambda = {np.array2string(lam, precision=3)}; streams: "
        + "; ".join(f"|v| {s[0]:.1f} dec {s[1]:+.0f}" for s in st))
R = np.array([r[1] / r[2] for r in rows])
R1 = np.array([r[3] / r[2] for r in rows])
say(f"largest LP/formula ratio on the grid: {R.max():.4f} at u0 = {u0s[np.argmax(R)]:.0f} km/s")
# intervals of u0 where the formula is within 10 % of the LP (ratio <= 1.1 and >= 1/1.1), on the 5 km/s grid of speeds
inside = (R <= 1.1) & (R >= 1 / 1.1)
spans = []
j = 0
while j < len(u0s):
    if inside[j]:
        k = j
        while k + 1 < len(u0s) and inside[k + 1]:
            k += 1
        spans.append((u0s[j] - (2.5 if j > 0 else 0), u0s[k] + (2.5 if k < len(u0s) - 1 else 10)))
        j = k + 1
    else:
        j += 1
say("u0 (5 km/s grid) where the formula is NOT within 10 %: " + ", ".join(f"{x:.0f}" for x in u0s[~inside])
    + "; ratios there: " + ", ".join(f"{x:.3f}" for x in R[~inside]))
say("shaded spans (km/s): " + "; ".join(f"{a_:.1f}-{b_:.1f}" for a_, b_ in spans))
for lo, hi in ((340, 400), (400, 560), (560, 700), (700, 791)):
    mk = (u0s >= lo) & (u0s < hi)
    say(f"  u0 in [{lo}, {hi}): LP/formula from {R[mk].min():.4f} to {R[mk].max():.4f}; first order reproduces the LP to "
        f"{np.abs(R1[mk] / R[mk] - 1).max():.4f}")

# leakage bracket at u0 = 600 km/s
U0 = 600.0
uc, dc, Uc, Dc, fc, kc, Kc, Gc = grid(10.0, 6.0)
phih, lamh, colsh, xh = solve(uc, Uc, fc, kc, U0)
uf, df, Uf, Df, ff, kf, Kf, Gf = grid(1.0, 0.5, umin=U0)
phif, lamf, _, _ = solve(uf, Uf, ff, kf, U0)
supp = ff & (Uf >= U0)
g = sum(lamh[i] * kf[n] for i, n in enumerate(BINS)) - 1.0 / (Uf / CK)
gmin = g[supp].min()
# Lipschitz constant of g in velocity units on the fine grid (finite differences; dec step in km/s is u * d dec)
gu = np.abs(np.diff(g, axis=0)) / np.diff(uf)[:, None]
gd = np.abs(np.diff(g, axis=1)) / (Uf[:, 1:] * np.radians(0.5))
mu = supp[1:, :] & supp[:-1, :]
md = supp[:, 1:] & supp[:, :-1]
L = max(gu[mu].max(), gd[md].max())
hfine = 0.5 * np.hypot(1.0, B.VMAX * np.radians(0.5))
delta = max(0.0, -gmin) + L * hfine
kappa = np.max(np.array([kf[n] for n in BINS]), axis=0)[supp].min()
upper = float(np.dot(lamh, np.full(len(BINS), NUP)) + delta * len(BINS) * NUP / kappa)
say(f"leakage at u0 = {U0:.0f} km/s: coarse LP Phi_h = {phih:.5e}, dual value {np.dot(lamh, [NUP]*len(BINS)):.5e}, "
    f"lambda_h = {np.array2string(lamh, precision=4)}")
say(f"  fine-grid LP = {phif:.5e}; min g on fine grid = {gmin:.4e} (relative to f there: {gmin/(CK/U0):.2e}); "
    f"L = {L:.4e} per km/s, h_fine = {hfine:.3f} km/s, defect delta = {delta:.4e}")
say(f"  kappa_v = {kappa:.4e}, N_tot = {len(BINS)*NUP:.3f}; bracket {phih:.5e} <= Phi_max <= {upper:.5e} "
    f"(width {(upper/phih - 1)*100:.2f} %)")
say(f"  isotropic formula at 600: {iso(U0):.5e}")

# figure
fig, ax = plt.subplots(figsize=(5.0, 3.3))
for a_, b_ in spans:
    ax.axvspan(a_, b_, color="0.88", lw=0)
ax.axhline(1.0, color="C0", lw=1.5, label=r"formula, $\min_i N^{\mathrm{up}}_i/\mathcal{A}_i(u_0)$")
ax.plot(u0s, R, "o", ms=2.4, color="k", label="linear program, directional kernel")
ax.plot(u0s, R1, color="C3", ls="--", lw=1.1, label="first order in the anisotropy")
ax.axvline(B.VMAX, color="0.3", lw=0.7, ls=":")
ax.set_xlim(u0s[0], 800)
ax.set_xlabel(r"$u_0$ (km s$^{-1}$)")
ax.set_ylabel(r"$\tilde\eta_{\max}(u_0)$ / formula")
ax.axhline(1.1, color="0.4", lw=0.7, ls=":")
ax.set_ylim(0.98, 1.17)
ax.legend(fontsize=7, frameon=False, loc="upper right")
ax.tick_params(labelsize=8)
fig.tight_layout()
fig.savefig(OUT)
say(f"wrote {OUT}")
# size of the final-state leakage factor 2 omega_max / Delta_i (eq:D.46-fsleak): silicon, highest phonon omega_max = 63.7 meV
# (the computed band top of NOTATION, Sects. 11.3, 17.1); bin width Delta_i = int P_casc(i|omega) d omega of the cascade bins
# (hib21.pbin on a 1 meV grid), against the calibrated pair energy 3.749 eV
_w = np.arange(1.0, 21.16, 0.001)
for n in (1, 2, 3):
    de = np.trapezoid(B.pbin(n, _w), _w)
    say(f"bin {n}: Delta = int P dw = {de:.3f} eV; 2 omega_max / Delta = 2 x 0.0637 / {de:.3f} = {2 * 0.0637 / de:.4f}")
say(f"(with Delta = eps_eh = 3.749 eV: {2 * 0.0637 / 3.749:.4f})")
