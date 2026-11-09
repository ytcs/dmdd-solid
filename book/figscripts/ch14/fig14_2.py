"""Fig. 14.2: one- and two-magnon weights of NiO at linear spin-wave order (Sect. 14.2).
Output: tex/figures/ch14/fig14_2.pdf. Prints every NiO number quoted in Sect. 14.2 (log: fig14_2.log).

Model (modelling choices, also named in the caption):
  Heisenberg model H = sum_<ij> J_ij S_i.S_j, each pair once, J > 0 antiferromagnetic (eq:7.1-heis), undistorted fcc
  lattice of Ni2+, type-II order, nearest- and next-nearest-neighbour exchange only, no anisotropy, |S| = 1, T = 0.
  Two-sublattice linear spin-wave theory of App. D.19 (eq:D.19-Hk, eq:D.19-bogo, eq:D.19-omega):
    A_k = J_AB(0) - J_AA(0) + J_AA(k), B_k = J_AB(k), omega_k = |S| sqrt(A_k^2 - B_k^2),
    u_k = cosh theta_k, v_k = sinh theta_k, tanh 2 theta_k = B_k / A_k (sign of v_k follows B_k).
  Wavevectors are used in the extended zone: B_{k+G} = +-B_k, so v_{k+G} = +-v_k, and the formulas below are
  invariant (Sect. 14.2).  Weights per magnetic ion, magnetic form factor set to 1 (it multiplies both channels).
  One-magnon (transverse, both branches):  w_perp(q) = |S| (u_q - v_q)^2.
  Two-magnon (longitudinal):  w_par(q) = (1/2) < (u_k v_{k-q} - v_k u_{k-q})^2 >_k   (eq:14.2-wpar),
  two-magnon spectral density per ion  rho(q, w) = (1/2) < (...)^2 delta(w - omega_k - omega_{k-q}) >_k,
  so that S^(2m)_zz(q, w) = (2 pi / Omega) |F^mag|^2 rho(q, w)  (eq:14.2-S2m).
  Averages over k: uniform grid shifted by half a step in the cube |k_i| < 2 pi/a, which is one period of A_k, B_k^2
  (it holds four zones of one sublattice). Panel (b) samples 3e6 random wavevectors in the same cell.
Inputs (sources):
  J2 = 19.01 meV, J1 = -1.37 meV (book convention): Hutchings and Samuelsen, PRB 6, 3447 (1972), abstract
     (sources/7.1/hutchings1972_abstract.txt), as in Sect. 7.1 (fig7_1.py).
  a = 4.17 A: Fischer et al., PRB 80, 014408 (2009), Table I, as in Sect. 7.1.
  v_max = 2.650e-3 (Sect. 1.3); NiO magnon speed 1.39e-4 (J2 only, worked example 7.2, fig7_1.py).
Checks printed: J2-only Delta S equals the simple-cubic antiferromagnet value (each type-II sublattice set of the fcc
  lattice decouples into simple-cubic antiferromagnets when J1 = 0); zone averages of w_perp and w_par equal
  |S|(1 + 2 Delta S) and Delta S (1 + Delta S); grid convergence.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch14", "fig14_2.pdf")
J1, J2, S, A = -1.37, 19.01, 1.0, 4.17
VMAX, CMAG = 2.650e-3, 1.39e-4
HC = 1973.2698  # eV A

nn = []
for v in [(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1)]:
    nn += [np.array(v), -np.array(v)]
nn = np.array(nn, float)
par = nn[np.isclose(nn.sum(1), 0)] * A / 2      # same (111) plane: parallel
anti = nn[~np.isclose(nn.sum(1), 0)] * A / 2    # adjacent planes: antiparallel
nnn = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], float) * A
G = 2 * np.pi / A


def lswt(k, j1=J1, j2=J2):
    """omega_k (meV), u_k, v_k for wavevectors k (Angstrom^-1), shape (n, 3)."""
    k = np.atleast_2d(k)
    jaa = j1 * np.cos(k @ par.T).sum(1)
    jab = j1 * np.cos(k @ anti.T).sum(1) + j2 * np.cos(k @ nnn.T).sum(1)
    ak = 6 * j2 + jaa                     # J_AB(0) - J_AA(0) = 6 J2
    bk = jab
    root = np.sqrt(np.maximum(ak**2 - bk**2, 1e-30))
    u = np.sqrt(0.5 * (ak / root + 1))
    v = np.sign(bk) * np.sqrt(0.5 * (ak / root - 1))
    return S * root, u, v


def grid(n):
    x = (np.arange(n) + 0.5) / n * 2 - 1
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    return np.stack([X.ravel(), Y.ravel(), Z.ravel()], 1) * G


def delta_s(n, **kw):
    _, _, v = lswt(grid(n), **kw)
    return np.mean(v**2)


print("== zero-point spin reduction Delta S = <(v^M_k)^2> ==")
for n in (48, 64, 96, 128):
    print(f"  grid {n}^3: J1+J2 {delta_s(n):.5f}   J2 only {delta_s(n, j1=0.0):.5f}")
DS = delta_s(128)
W_perp = S * (1 + 2 * DS)
W_par = DS * (1 + DS)
print(f"NiO (J1+J2): Delta S = {DS:.4f}, Delta S/|S| = {DS/S:.4f}")
print(f"  W_perp = |S|(1+2DS) = {W_perp:.4f}; W_par = DS(1+DS) = {W_par:.4f}; ratio W_par/W_perp = {W_par/W_perp:.4f}")
print(f"  Casimir form of the transverse weight (|S| - DS)(1 + 2DS) = {(S-DS)*(1+2*DS):.4f}; "
      f"sum check W_perp(Casimir) + W_par + (|S|-DS)^2 = {(S-DS)*(1+2*DS)+W_par+(S-DS)**2:.4f} vs |S|(|S|+1) = {S*(S+1):.4f}")
print(f"  order-counting parameter 1/(2|S|) = {1/(2*S):.2f}")

KG = grid(64)
WK, UK, VK = lswt(KG)


def wpar(q):
    w2, u2, v2 = lswt(KG - q[None, :])
    amp = UK * v2 - VK * u2
    return 0.5 * np.mean(amp**2)


def wperp(q):
    _, u, v = lswt(q[None, :])
    return S * (u[0] - v[0])**2


# zone averages of the q-resolved weights (Parseval check), q on a coarse shifted grid over the same period cell
QG = grid(12)
avg_par = np.mean([wpar(q) for q in QG])
_, UQ, VQ = lswt(grid(128))
avg_perp = np.mean(S * (UQ - VQ)**2)
print("== sum-rule check (w_par: q on 12^3 shifted points, k on 64^3; w_perp: q on 128^3) ==")
print(f"  <w_par>_q = {avg_par:.4f} (expected {W_par:.4f}); <w_perp>_q = {avg_perp:.4f} (expected {W_perp:.4f})")

print("== q-resolved weights along [111] (q in units of 2 pi/a) ==")
for t in (0.02, 0.05, 0.1, 0.25, 0.4, 0.45):
    q = np.array([t, t, t]) * G
    wp, wl = wperp(q), wpar(q)
    qa = np.linalg.norm(q)
    print(f"  q = ({t},{t},{t}): |q| = {qa:.3f} 1/A = {qa*HC/1e3:.3f} keV; w_perp = {wp:.4f}, w_par = {wl:.4f}, "
          f"ratio = {wl/wp:.4f}; w_par/(|q|a)^2 = {wl/(qa*A)**2:.4f}; w_perp/(|q|a) = {wp/(qa*A):.4f}")
ts = np.linspace(0.01, 0.49, 49)
rat = [wpar(np.array([t, t, t]) * G) / wperp(np.array([t, t, t]) * G) for t in ts]
i = int(np.argmax(rat))
print(f"  max of w_par/w_perp along [111]: {rat[i]:.4f} at t = {ts[i]:.2f} (|q| = {np.sqrt(3)*ts[i]*G*HC/1e3:.3f} keV)")
for t in (0.25, 0.5, 1.0):
    q = np.array([t, 0, 0]) * G
    print(f"  q = ({t},0,0): w_perp = {wperp(q):.4f}, w_par = {wpar(q):.4f}")

print("== continuum edges at fixed q (k on 64^3; meV) ==")
EDGE_Q = {"(1/4,1/4,1/4)": np.array([0.25, 0.25, 0.25]) * G, "(1/2,1/2,1/2)": np.array([0.5, 0.5, 0.5]) * G,
          "(1/2,0,0)": np.array([0.5, 0, 0]) * G}
for name, q in EDGE_Q.items():
    w2, _, _ = lswt(KG - q[None, :])
    tot = WK + w2
    w1 = lswt(q[None, :])[0][0]
    f = lambda k: lswt(k[None, :])[0][0] + lswt((k - q)[None, :])[0][0]
    starts = [np.zeros(3), q.copy()] + [KG[i] for i in np.argsort(tot)[:20]]
    lo = min(minimize(f, x0, method="Nelder-Mead", options={"xatol": 1e-7, "fatol": 1e-6, "maxiter": 4000}).fun for x0 in starts)
    hi = -min(minimize(lambda k: -f(k), KG[i], method="Nelder-Mead").fun for i in np.argsort(tot)[-10:])
    print(f"  q = {name}: one-magnon {w1:.1f}; continuum {lo:.1f} to {hi:.1f} (grid {tot.min():.1f} to {tot.max():.1f})")
WMAX = WK.max()
print(f"  grid maximum one-magnon energy {WMAX:.1f} meV; 2 x that = {2*WMAX:.1f} meV")

print("== kinematic minimum masses (threshold w_th) ==")
r = VMAX**2 / (4 * CMAG * (VMAX - CMAG))
print(f"  ratio one-magnon / two-magnon minimum mass v^2/(4c(v-c)) = {r:.2f} (c = {CMAG}, v_max = {VMAX})")
for wth in (1e-3, 10e-3):
    m1 = wth / (2 * CMAG * (VMAX - CMAG))
    m2 = 2 * wth / VMAX**2
    print(f"  w_th = {wth*1e3:.0f} meV: one magnon m >= {m1/1e3:.2f} keV, two magnons m >= {m2/1e3:.3f} keV")

# ---- figure ---------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 8.5})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.0, 2.9))
segs = [((0, 0, 0), (0.5, 0.5, 0.5)), ((0.5, 0.5, 0.5), (1, 1, 1)), ((0, 0, 0), (1, 0, 0))]
x0, ticks = 0.0, [0.0]
for i, (p, q) in enumerate(segs):
    p, q = np.array(p, float) * G, np.array(q, float) * G
    t = np.linspace(0.004, 0.996, 121)
    ks = p[None, :] + t[:, None] * (q - p)[None, :]
    L = np.linalg.norm(q - p)
    x = x0 + t * L
    ax.semilogy(x, [wperp(k) for k in ks], color="k", lw=1.2, label="one magnon, $w_\\perp$" if i == 0 else None)
    ax.semilogy(x, [wpar(k) for k in ks], color="#c0392b", lw=1.2, label="two magnons, $w_\\parallel$" if i == 0 else None)
    x0 += L
    ticks.append(x0)
    if i < len(segs) - 1:
        ax.axvline(x0, color="0.6", lw=0.6)
ax.set_xticks(ticks)
ax.set_xticklabels([r"$\Gamma$", r"$(\frac{1}{2},\frac{1}{2},\frac{1}{2})$", r"$(1,1,1)\,|\,\Gamma$", r"$(1,0,0)$"])
ax.set_xlim(0, ticks[-1])
ax.set_ylim(1e-3, 30)
ax.set_ylabel("weight per ion")
ax.set_title(r"(a) $\omega$-integrated weights", fontsize=8.5, loc="left")
ax.legend(fontsize=6.5, frameon=False, loc="upper right")

# panel (b): 3e6 random wavevectors in the period cell (a regular grid puts points next to the zeros of the
# dispersion and produces spikes at low energy); 4-meV bins
KF = np.random.default_rng(7).uniform(-1, 1, (3000000, 3)) * G
WF, UF, VF = lswt(KF)
bins = np.arange(0, 252, 4.0)
cols = ["#1f5fa8", "#c0392b", "#2e8b57"]
for (name, q), c in zip(EDGE_Q.items(), cols):
    w2, u2, v2 = lswt(KF - q[None, :])
    amp2 = (UF * v2 - VF * u2)**2
    h, e = np.histogram(WF + w2, bins=bins, weights=0.5 * amp2 / len(KF))
    rho = h / np.diff(e)
    bx.plot(0.5 * (e[1:] + e[:-1]), rho * 1e3, color=c, lw=1.1, label=r"$\mathbf{q} = " + name.replace("1/4", r"\frac{1}{4}").replace("1/2", r"\frac{1}{2}") + "$")
    w1 = lswt(q[None, :])[0][0]
    bx.axvline(w1, color=c, lw=0.7, ls=":")
    print(f"  spectral check {name}: integral of rho = {np.sum(h):.4f} vs w_par (3e6 random k) = {0.5*np.mean(amp2):.4f}")
bx.set_xlim(0, 250)
bx.set_ylim(bottom=0)
bx.set_xlabel(r"$\omega$ (meV)")
bx.set_ylabel(r"two-magnon density per ion (eV$^{-1}$)")
bx.set_title("(b) two-magnon continuum", fontsize=8.5, loc="left")
bx.legend(fontsize=6.5, frameon=False, loc="upper right")
fig.tight_layout()
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT)
print("wrote", os.path.relpath(OUT, HERE))
