"""Limit Check 14.3a (lim:14.3a, Sect. 14.3): absorption into magnons. Output tex/figures/ch14/limit14_3a.pdf,
log limit14_3a.log.  Run: python limit14_3a.py (needs ed14_3.npz from ed14_3.py; seconds).

Panel (a), the Larmor statement. Literature formula: all k -> 0 transverse spin weight in one line at omega_Lar = 2 mu_B B0,
    with weight 2<S^z_tot> (Oshikawa and Affleck, cond-mat/0108424 Eqs. (2.4)-(2.5); the one-sublattice rate of
    Mitridate et al. 2005.10256 Eq. (27); Chigusa et al. 2001.10666 Eqs. (25)-(27)). In the plot: ratio 1 for line position
    and weight.
  Fuller result: uniform mode of a saturated ellipsoid with demagnetizing factors (book eq:14.3-kittel), for a thin film
    with B0 in the plane (N_x = N_z = 0, N_y = 1):  omega_Kit/omega_Lar = sqrt(1 + 1/x), and the transverse-averaged weight
    factor (omega_Kit,x + omega_Kit,y)/(2 omega_Kit) = (2 + 1/x)/(2 sqrt(1 + 1/x)), with x = B0/(mu0 M_s) the applied field over
    the shape-anisotropy field. Sphere (N = 1/3 each): both ratios exactly 1, for x > 1/3 (saturation).
  Shaded: x where both film ratios are within 10 % of 1.
  Markers: YIG (mu0 M_s = 0.246 T from we14_3.py) at 10 ueV: film B0 = 27.3 mT, sphere B0 = 86.4 mT.

Panel (b), the antiferromagnetic weight. Formula: uniform transverse weight per antiparallel pair over |S|,
    r = omega_AFMR/(2 omega_E + omega_A) = sqrt(x/(2 + x)), x = omega_A/omega_E (two-sublattice linear spin-wave theory, k = 0;
    book eq:14.3-afmrweight). Leading small-x form sqrt(x/2) (exchange suppression), dashed.
  The isotropic Heisenberg statement (weight 0 at k -> 0, 2005.10256 Eq. (28)) is the x -> 0 end.
  Fuller result: exact diagonalization of the 8-site easy-axis cube (ed14_3.py), total weight <(S^x_tot)^2> per pair, |S| = 1, 3/2,
    shown only where the finite cluster orders (splitting of the two lowest S^z_tot = 0 states below 1 % of omega_AFMR).
  Shaded: x where sqrt(x/2) is within 10 % of r.  Marker: MnF2, x = 0.0174, r = 0.0929 (we14_3.py).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "..", "..")
FIG = os.path.join(BOOK, "tex", "figures", "ch14")
os.makedirs(FIG, exist_ok=True)
LOG = open(os.path.join(HERE, "limit14_3a.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


muB = 5.7883818060e-5
mu0Ms = 0.2460      # T, YIG (we14_3.log)

# ---------- panel (a)
x = np.logspace(-2, 2, 800)
freq = np.sqrt(1 + 1 / x)
wfac = (2 + 1 / x) / (2 * np.sqrt(1 + 1 / x))
ok = (np.abs(freq - 1) <= 0.1) & (np.abs(wfac - 1) <= 0.1)
xlo_a = x[ok].min()
out(f"(a) film: both ratios within 10 % of the Larmor statement for x = B0/mu0Ms >= {xlo_a:.2f}")
# analytic thresholds
out(f"    frequency within 10 %: x >= {1/(1.1**2-1):.2f}; weight within 10 %: x >= {1/1.428:.2f}")
for xv in (0.05, 0.111, 0.351, 1.0, 3.0, 10.0):
    out(f"    x = {xv:6.3f}: omega_Kit/omega_Lar = {np.sqrt(1+1/xv):.3f}, weight factor = {(2+1/xv)/(2*np.sqrt(1+1/xv)):.3f}")
xf = 27.3e-3 / mu0Ms
xs = 86.4e-3 / mu0Ms
out(f"    YIG at 10 ueV: film x = {xf:.3f}, sphere x = {xs:.3f} (sphere saturates at x = 1/3)")

# ---------- panel (b)
d = np.load(os.path.join(HERE, "ed14_3.npz"))
xe = d["x"]
r = lambda t: np.sqrt(t / (2 + t))
xb = np.logspace(-3, np.log10(3), 800)
okb = np.abs(np.sqrt(xb / 2) / r(xb) - 1) <= 0.1
xhi_b = xb[okb].max()
out(f"(b) sqrt(x/2) within 10 % of the closed form for x <= {xhi_b:.2f}")
xM, rM = 0.0174, 0.0929
out(f"    MnF2: x = {xM}, r = {r(xM):.4f}")
# ED points where the cluster orders: splitting of the two lowest S^z_tot = 0 states (ed14_3.npz) / omega_AFMR < 1 %
# omega_AFMR in units of J: z|S| sqrt(x(2+x)), z = 3
split = {2: d["g2"], 3: d["g3"]}
pts = {}
for S2, key in ((2, "w2"), (3, "w3")):
    S = S2 / 2
    wAF = 3 * S * np.sqrt(xe * (2 + xe))
    sel = np.array(split[S2]) / wAF < 0.01
    pts[S2] = (xe[sel], d[key][sel])
    for xv, wv in zip(xe[sel], d[key][sel]):
        out(f"    ED |S| = {S}: x = {xv:.2f}, exact/|S| = {wv:.4f}, LSWT = {r(xv):.4f}, exact/LSWT = {wv/r(xv):.3f}")

fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.1))
ax = axs[0]
ax.axvspan(xlo_a, 100, color="0.88", lw=0, zorder=0)
ax.axhline(1, color="k", lw=1.0, label="Larmor statement")
ax.semilogx(x, freq, color="C3", lw=1.3, label=r"film: $\omega_\mathrm{Kit}/\omega_\mathrm{Lar}$")
ax.semilogx(x, wfac, color="C0", lw=1.3, ls="--", label="film: weight factor")
ax.plot([xs], [1], "s", color="k", ms=4, mfc="w", label="YIG sphere, 10 µeV")
ax.plot([xf, xf], [np.sqrt(1 + 1 / xf), (2 + 1 / xf) / (2 * np.sqrt(1 + 1 / xf))], "o", color="k", ms=3.5,
        label="YIG film, 10 µeV")
ax.axvline(1 / 3, color="0.5", lw=0.6, ls=":")
ax.text(0.30, 3.3, "sphere\nsaturated", fontsize=7, color="0.3", ha="left")
ax.set_xlim(1e-2, 1e2)
ax.set_ylim(0.8, 11)
ax.set_yscale("log")
ax.set_xlabel(r"$B_0/\mu_0M_\mathrm{s}$")
ax.set_ylabel("ratio to the Larmor statement")
ax.set_title("(a) uniform mode with demagnetization", fontsize=8)
ax.legend(fontsize=7, frameon=False, loc="upper right")

ax = axs[1]
ax.axvspan(1e-3, xhi_b, color="0.88", lw=0, zorder=0)
ax.loglog(xb, r(xb), color="C3", lw=1.3, label=r"$\omega_\mathrm{AFMR}/(2\omega_E+\omega_A)$")
ax.loglog(xb, np.sqrt(xb / 2), color="C3", lw=0.9, ls="--", label=r"$(\omega_A/2\omega_E)^{1/2}$")
for S2, mk, lab in ((2, "^", r"exact, $|\mathbf{S}| = 1$"), (3, "o", r"exact, $|\mathbf{S}| = 3/2$")):
    ax.plot(*pts[S2], mk, color="C0", ms=3.5, mfc="none", label=lab)
ax.plot([xM], [rM], "s", color="k", ms=4, mfc="w", label=r"MnF$_2$")
ax.axhline(1, color="0.5", lw=0.6, ls=":")
ax.text(1.2e-3, 1.1, "ferromagnetic pair", fontsize=7, color="0.3")
ax.set_xlim(1e-3, 3)
ax.set_ylim(1e-2, 1.6)
ax.set_xlabel(r"$\omega_A/\omega_E$")
ax.set_ylabel(r"uniform weight per pair $/\,|\mathbf{S}|$")
ax.set_title("(b) antiferromagnetic resonance", fontsize=8)
ax.legend(fontsize=7, frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit14_3a.pdf"))
out("wrote", os.path.join(FIG, "limit14_3a.pdf"))
LOG.close()
