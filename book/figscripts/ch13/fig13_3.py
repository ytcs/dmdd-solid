"""Fig. 13.3 (fig:13-paloss) and every number of Sect. 13.3 and Worked example 13.3 (we:13-onset-exp).

The near-threshold phonon-assisted loss function of silicon at a fixed momentum transfer |q| = 1.0 keV, averaged over the
directions of q, built from the structure derived in Sect. 13.3:
  per valley, phonon branch nu and hole band, at fixed q and T -> 0 (emission only), with parabolic pockets and a vertex
  |M|^2 that is constant across the pockets (eq:6.5-joint with the phonon energy taken at Q* = K - q),
      S(q, omega) = Omega (m*_d m_h)^{3/2} |M|^2 x^2 / (4 pi^2),   x = omega - E_g - omega_nu(Q*(q)),
  and its average over the directions of q,  Sbar = (1/4pi) Int dOmega_q S.
Modelling choices (named in the caption):
  * one valley, K = k_c xhat (the other five give the same average by cubic symmetry);
  * |q| = 1.0 keV; Q* = K - q exact for every direction; phonon energies from the PBE force constants of Sect. 5.2
    (figscripts/ch05/si_ifc.py, full 3D dispersion, branches sorted by energy);
  * equal coefficients C for every branch: TA pair (branches 0, 1), optical (3, 4, 5) with |M|^2 = C;
    LA (branch 2) with |M|^2 = C sin^2(theta_Q), theta_Q the angle between Q* and the valley axis, because the LA amplitude
    vanishes on the axis (G' = 0 class, C4v selection rule, Sect. 13.3); the growth of the LA amplitude across the pockets is
    of the same order and is left out;
  * the tilt of the pair minimum by the phonon group velocity (shift -(1/2) M_x v_g^2, printed below) is neglected.
Inputs and sources:
  a = 5.431 A, E_g = 1.17 eV, m*_par = 0.916, m*_perp = 0.191, m_hh[100] = 0.277 m_e: Table 3.1 (tab:3-materials).
  k_c = 0.85 (2 pi/a): Sect. 3.3.  v_max = 794.5 km/s: Sect. 1.2.  hbar c = 1973.2698 eV A, m_e = 510998.95 eV.
  delta_w = 0.3 eV: off-shell margin of the window (Sect. 13.6), five times the top of the phonon band.
  E_x^b = 14.7 meV (Shaklee and Nahory 1970; Sect. 4.9).
  Ge statement of the text (all branches allowed on the C3v axis) is symmetry only; no Ge numbers are computed here.
Run: python fig13_3.py  (numpy, matplotlib; about 30 s). Log: fig13_3.log (written by tee in the run line below).
     python fig13_3.py | tee fig13_3.log
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch13", "fig13_3.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

HBARC = 1973.269804          # eV A
ME = 510998.95               # eV
A_SI = 5.431                 # A
G1 = 2 * np.pi * HBARC / A_SI   # 2pi/a in eV
KC = 0.85 * G1
EG = 1.17
VMAX = 794.5 / 299792.458
MPAR, MPERP, MHH = 0.916, 0.191, 0.277
MX = (MPAR + MHH) * ME       # pair mass along [100]
MD = (MPAR * MPERP ** 2) ** (1 / 3)
DW = 0.3                     # eV, delta_w
EXB = 14.7e-3
QABS = 1000.0                # eV, |q|
INV_A = HBARC                # 1 A^-1 in eV


def phon(Q):
    """Q: (n,3) Cartesian in eV -> (n,6) frequencies in meV."""
    return si_ifc.phonons(np.atleast_2d(Q) / G1)[0]


print(f"2pi/a = {G1:.1f} eV = {G1/INV_A:.4f} 1/A; k_c = {KC:.0f} eV = {KC/INV_A:.3f} 1/A")
print(f"M_x = m_par + m_hh[100] = {MX/ME:.3f} m_e; m*_d = {MD:.3f} m_e")

# ---------------- on-axis geometry at |q| = 1 keV ----------------
dK = KC - QABS
w_ax = phon(np.array([[dK, 0, 0]]))[0]
print(f"|q| = {QABS:.0f} eV = {QABS/INV_A:.3f} 1/A; d_K = {dK:.0f} eV = {dK/INV_A:.3f} 1/A = {dK/G1:.3f} X")
print("on-axis phonon energies at Q* (meV): TA {:.2f} {:.2f}, LA {:.2f}, optical {:.2f} {:.2f} {:.2f}".format(*w_ax))
# window at this |q| (parabolic E_min along the axis, eq:3.3-Eminpar)
Emin_m_Eg = dK ** 2 / (2 * MX)
print(f"E_min(q) - E_g (parabolic, M_x) = {Emin_m_Eg:.3f} eV; window reaches omega - E_g <= {Emin_m_Eg - DW:.3f} eV "
      f"(delta_w = {DW} eV)")
# grid E_min at |q| = 1 keV from the PBE bands of Sect. 3.3 (figscripts/ch03/qe_si_pbe.npz, 48^3 grid, scissor to E_g),
# same procedure as fig13_1.py; linear interpolation in |q| along [100], [110], [111]
dd = np.load(os.path.join(HERE, "..", "ch03", "qe_si_pbe.npz"))
kp, eb = dd["kp"], dd["bands"]
iG = int(np.argmin(np.linalg.norm(kp[:100], axis=1)))
vbm = eb[iG, 3]
sk, se = dd["scan_k"], dd["scan_e"] - vbm
s_, cb = sk[:61, 0], se[:61, 4]
jj = int(np.argmin(cb)); win = slice(jj - 4, jj + 5)
cc = np.polyfit(s_[win] - s_[jj], cb[win], 2)
scis = EG - np.polyval(cc, -cc[1] / (2 * cc[0]))
for n in ("[100]", "[110]", "[111]"):
    qq, ee = dd["q" + n], dd["E" + n] + scis
    print(f"grid E_min({QABS:.0f} eV, {n}) - E_g = {np.interp(QABS, qq, ee) - EG:.3f} eV (48^3 PBE + scissor)")
# reach: smallest mass that deposits E_g + omega_TA at |q| = 1 keV
Eon = EG + w_ax[0] * 1e-3
mreq = QABS ** 2 / (2 * (QABS * VMAX - Eon))
print(f"onset energy E_g + omega_TA = {Eon:.4f} eV; reachable for m_chi >= {mreq/1e6:.4f} MeV (q v_max = {QABS*VMAX:.3f} eV)")

# Q_w: |Q*| at which the onset meets the window edge, c = phase speed of TA at that |Q|
Qw = np.sqrt(2 * MX * DW)
for _ in range(20):
    c = phon(np.array([[Qw, 0, 0]]))[0][0] * 1e-3 / Qw
    Qw = MX * c + np.sqrt((MX * c) ** 2 + 2 * MX * DW)
print(f"Q_w = M_x c + sqrt(M_x^2 c^2 + 2 M_x delta_w) = {Qw:.0f} eV = {Qw/INV_A:.3f} 1/A "
      f"(leading term sqrt(2 M_x delta_w) = {np.sqrt(2*MX*DW)/INV_A:.3f} 1/A; c_TA phase speed {c*299792.458:.2f} km/s); "
      f"d_K >= Q_w for |q| <= k_c - Q_w = {KC - Qw:.0f} eV")

# tilt shift -(1/2) M_x v_g^2 along [100] at d_K, and curvature of the branches against 1/M_x
h = 5.0
for nu, name in ((0, "TA"), (2, "LA")):
    wp, w0, wm = (phon(np.array([[dK + s, 0, 0]]))[0][nu] * 1e-3 for s in (h, 0.0, -h))
    vg = (wp - wm) / (2 * h)
    curv = (wp - 2 * w0 + wm) / h ** 2
    print(f"{name}: v_g = {vg:.3e} ({vg*299792.458:.2f} km/s); tilt shift (1/2) M_x v_g^2 = {0.5*MX*vg**2*1e3:.4f} meV; "
          f"d^2omega/dQ^2 = {curv:.3e} 1/eV vs 1/M_x = {1/MX:.3e} 1/eV (ratio {curv*MX:.1e})")

# radial and angular threshold curvature b (E_th = E0 + b theta^2), from finite differences at small theta
def qhat(th, ph):
    return np.stack([np.cos(th), np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph)], axis=-1)


th0 = 0.02
phs = np.linspace(0, 2 * np.pi, 64, endpoint=False)
Qs = np.array([KC, 0, 0])[None, :] - QABS * qhat(np.full_like(phs, th0), phs)
wth = phon(Qs)
b = (wth - w_ax[None, :]) / th0 ** 2      # meV, per branch and azimuth
for nu, name in ((0, "TA1"), (1, "TA2"), (2, "LA"), (3, "opt1"), (4, "opt2"), (5, "opt3")):
    print(f"b_{name}(phi): min {b[:, nu].min():.2f}, max {b[:, nu].max():.2f} meV; <1/b> = {np.mean(1/b[:, nu]):.4f} 1/meV")
# crossover: |q| above which the lowest TA threshold has its minimum off the valley axis (min over phi of b_TA1 < 0)
def bmin_TA(qa):
    Qs_ = np.array([KC, 0, 0])[None, :] - qa * qhat(np.full_like(phs, th0), phs)
    w0_ = phon(np.array([[KC - qa, 0, 0]]))[0][0]
    return (phon(Qs_)[:, 0].min() - w0_) / th0 ** 2


lo, hi = 1200.0, 1600.0
for _ in range(30):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if bmin_TA(mid) > 0 else (lo, mid)
print(f"TA on-axis minimum up to |q| = {0.5*(lo+hi):.0f} eV (min over azimuth of b_TA1 changes sign; theta = {th0} rad)")
# radial estimate of b for the lowest TA: omega' |q||K| / (2 d_K)
wp, wm = (phon(np.array([[dK + s, 0, 0]]))[0][0] for s in (h, -h))
wpr = (wp - wm) / (2 * h)       # meV per eV
print(f"radial b_TA = omega' |q| |K| / (2 d_K) = {wpr*QABS*KC/(2*dK):.2f} meV (omega' = {wpr*INV_A:.2f} meV A)")

# ---------------- angle average on a (theta, phi) grid ----------------
N_TH, N_PH = 900, 96
u = (np.arange(N_TH) + 0.5) / N_TH
TH = np.pi * u ** 2
dTH = np.pi * 2 * u / N_TH
PH = (np.arange(N_PH) + 0.5) * 2 * np.pi / N_PH
TT, PP = np.meshgrid(TH, PH, indexing="ij")
QH = qhat(TT, PP).reshape(-1, 3)
QS = np.array([KC, 0, 0])[None, :] - QABS * QH
W = phon(QS).reshape(N_TH, N_PH, 6)
wgt = (np.sin(TT) * dTH[:, None] * (2 * np.pi / N_PH)) / (4 * np.pi)     # dOmega/4pi
print(f"grid check: sum dOmega/4pi = {wgt.sum():.5f}")
cosQ = QS[:, 0].reshape(N_TH, N_PH) / np.linalg.norm(QS, axis=1).reshape(N_TH, N_PH)
sin2Q = 1 - cosQ ** 2
E0 = W.min(axis=(0, 1))                   # meV, minimum over directions, per branch
print("minimum over directions (meV): " + ", ".join(f"{e:.3f}" for e in E0)
      + f"; on axis: " + ", ".join(f"{e:.3f}" for e in w_ax))
# refine the lowest optical onset over directions from the grid minimum (Nelder-Mead in (theta, phi), 40 starts)
from scipy.optimize import minimize
best = 1e9
rng = np.random.default_rng(1)
for st in range(40):
    x0 = np.array([np.pi * rng.random(), 2 * np.pi * rng.random()])
    f = lambda t: phon((np.array([KC, 0, 0]) - QABS * qhat(t[0], t[1]))[None, :])[0][3]
    r = minimize(f, x0, method="Nelder-Mead", options={"xatol": 1e-6, "fatol": 1e-6})
    best = min(best, r.fun)
print(f"lowest optical onset over all directions, refined (Nelder-Mead, 40 starts): {best:.2f} meV above E_g")


def sbar(xabs_meV, nu, weight=None):
    """Sbar/C for branch nu at omega - E_g = xabs (meV), in meV^2 (x measured from E_g)."""
    d = np.clip(xabs_meV[:, None, None] - W[None, :, :, nu], 0, None) ** 2
    ww = wgt if weight is None else wgt * weight
    return (d * ww[None]).sum(axis=(1, 2))


# panel (b): TA pair and LA against the distance from their own on-axis onset
xs = np.logspace(-3, np.log10(30), 120)          # meV above the on-axis onset
S_TA = sbar(w_ax[0] + xs, 0) + sbar(w_ax[1] + xs, 1)
S_TAfix = 2 * xs ** 2                            # on-axis, fixed direction (both TA branches), per unit C
S_LA = sbar(w_ax[2] + xs, 2, sin2Q)
invb_TA = np.mean(1 / b[:, 0]) + np.mean(1 / b[:, 1])
asy_TA = xs ** 3 * invb_TA / 12
invb2_LA = np.mean(1 / b[:, 2] ** 2)
asy_LA = (QABS / dK) ** 2 * xs ** 4 * invb2_LA / 48
r_TA = S_TA / asy_TA
r_LA = S_LA / asy_LA
for lab, r in (("TA", r_TA), ("LA", r_LA)):
    ok = np.where(np.abs(r - 1) > 0.10)[0]
    xlim = xs[ok[0]] if len(ok) else xs[-1]
    print(f"{lab}: numerical average within 10 % of the asymptote for x < {xlim:.3g} meV "
          f"(ratio at 1e-3 meV {r[0]:.3f})")
for xx in (0.01, 0.1, 1.0, 3.0, 10.0):
    i = np.argmin(np.abs(xs - xx))
    loc_TA = np.gradient(np.log(S_TA), np.log(xs))[i]
    loc_LA = np.gradient(np.log(S_LA), np.log(xs))[i]
    print(f"x = {xs[i]:.3g} meV: local exponent TA {loc_TA:.2f}, LA {loc_LA:.2f}; Sbar_TA / S_TA(axis) = {S_TA[i]/S_TAfix[i]:.3e}")

# panel (a): components against omega - E_g, T -> 0
xa = np.linspace(0, 70, 1401)
comp = {"TA": sbar(xa, 0) + sbar(xa, 1),
        "LA": sbar(xa, 2, sin2Q),
        "opt": sbar(xa, 3) + sbar(xa, 4) + sbar(xa, 5)}
tot = sum(comp.values())
for xx in (20.0, 40.0, 70.0):
    i = np.argmin(np.abs(xa - xx))
    print(f"omega - E_g = {xa[i]:.0f} meV: TA {comp['TA'][i]:.3e}, LA {comp['LA'][i]:.3e}, opt {comp['opt'][i]:.3e} meV^2")
print(f"exciton replica of the TA onset: omega - E_g = {w_ax[0] - EXB*1e3:.2f} meV")

# ---------------- figure ----------------
plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.75))
ax = axs[0]
cTA, cLA, cO = "#2a6fb0", "#c4661f", "#7a5ea8"
ax.plot(xa, tot, color="k", lw=1.6, label="sum")
ax.plot(xa, comp["TA"], color=cTA, lw=1.1, ls="--", label="TA (two branches)")
ax.plot(xa, comp["LA"], color=cLA, lw=1.1, ls="--", label="LA (forbidden on the axis)")
ax.plot(xa, comp["opt"], color=cO, lw=1.1, ls="--", label="optical (three branches)")
for e in (w_ax[0], w_ax[2], E0[3]):
    ax.axvline(e, color="0.6", lw=0.6, ls=":")
ax.axvline(w_ax[0] - EXB * 1e3, color="0.6", lw=0.6, ls="-.")
ax.text(w_ax[0] - EXB * 1e3 + 0.8, 0.97, "TA exciton\nreplica", fontsize=6, color="0.4", va="top", ha="left",
        transform=ax.get_xaxis_transform())
ax.set_yscale("log")
ax.set_ylim(1e-2, 1e7)
ax.set_xlim(-12, 70)
ax.set_xlabel(r"$\omega - E_{\mathrm{g}}$ (meV)")
ax.set_ylabel(r"$\bar S^{\mathrm{PA}}/C$ (meV$^2$)")
ax.legend(frameon=True, framealpha=1, edgecolor="none", fontsize=6.5, loc="upper right")
ax.set_title(r"(a) $|\mathbf{q}| = 1.0$ keV, $T \to 0$", fontsize=8)

ax = axs[1]
ax.loglog(xs, S_TAfix, color=cTA, ls="--", lw=1.0, label=r"TA, $\hat{\mathbf{q}}$ on the axis: $x^2$")
ax.loglog(xs, S_TA, color=cTA, lw=1.4, label="TA, averaged")
ax.loglog(xs, asy_TA, color=cTA, ls=":", lw=1.0, label=r"$x^3$ asymptote")
ax.loglog(xs, S_LA, color=cLA, lw=1.4, label="LA, averaged")
ax.loglog(xs, asy_LA, color=cLA, ls=":", lw=1.0, label=r"$x^4$ asymptote")
ax.set_xlim(xs[0], xs[-1])
ax.set_ylim(1e-12, 1e4)
ax.set_xlabel(r"$x$, distance from the on-axis onset (meV)")
ax.legend(frameon=False, fontsize=6.5, loc="upper left")
ax.set_title("(b) onset exponents", fontsize=8)
fig.tight_layout()
fig.savefig(OUT)
print("wrote", OUT)
