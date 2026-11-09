"""Crowdion as a Frenkel-Kontorova kink (Sect. 19.6): Limit Check 19.6b (lim:19.6b, fig:19-limit-crowdion) and every
crowdion number printed in Sect. 19.6.  Log: limit19_6b.log.  Run: python limit19_6b.py > limit19_6b.log  (about a minute).

Model: the Frenkel-Kontorova chain of App. C.20, eq:C.20-FK, in units a_ch = 1, V_s = 1:
    E = sum_n [ (K/2)(u_{n+1} - u_n)^2 + sin^2(pi u_n) ],  u -> 1 at n -> -inf, u -> 0 at n -> +inf,
kink width d_kink = [K/(2 pi^2)]^(1/2) (eq:C.20-kink with V_s = a_ch = 1).
Continuum (sine-Gordon) results of App. C.20, which are those of Fitzgerald, arXiv:1806.11002 Eqs. (2), (3):
    E_kink = 4 d_kink (eq:C.20-Ekink),  M_kink = (2/pi^2)(1/d_kink) M (eq:C.20-mass),
    E_PN = 16 pi^2 d_kink^2 cosech(pi^2 d_kink) (eq:C.20-EPN; NOT 1806.11002 Eq. (6), which is a factor 2 lower).
Discrete results (computed here): relaxed chain of N = 401 atoms (boundary atoms fixed at 1 and 0) minimized by Newton's
method with the tridiagonal Hessian to |grad| < 1e-13, kink centred between two atoms (minimum) and on an atom
(saddle; the central atom held at u = 1/2 by symmetry).  E_disc = energy at the minimum; E_PN,disc = saddle - minimum;
translation mass M_disc = M sum_n (u_{n+1} - u_n)^2 (MODELLING CHOICE: the lattice form of M sum (du_n/dz_0)^2,
reducing to eq:C.20-mass for d_kink >> 1).
Leading correction to the energy (derived in the text): discrete spring energy = continuum - (K/24) int u''^2 dz
(from 4 sin^2(k/2) = k^2 - k^4/12), evaluated on the kink: E_disc/E_kink = 1 - 1/(72 d_kink^2).
Tungsten numbers: V_s ~ 1 eV and K a_ch^2 ~ 50-100 eV (the ranges quoted by 1806.11002 below its Eq. (6));
a_ch = sqrt(3)/2 x 3.165 A (bcc W lattice constant 3.165 A, Kittel, Introduction to Solid State Physics, Table 1.3);
M_W = 183.84 u.  Band of the kink in the Peierls-Nabarro potential: Mathieu problem
    -(1/2M_kink) psi'' + (E_PN/2)(1 - cos(2 pi z/a_ch)) psi = E psi, Bloch phase 0 and pi, width = E(pi) - E(0),
solved by plane-wave diagonalization (41 waves).  Recoil energy E_rec = pi^2 hbar^2/(2 M_kink a_ch^2).
"""
import os
import numpy as np
from scipy.linalg import solve_banded, eigh
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch19")

HBARC = 1973.269804  # eV A
AMU = 931.49410242e6  # eV


def energy(u, K):
    uf = np.concatenate(([1.0], u, [0.0]))
    return 0.5 * K * np.sum(np.diff(uf) ** 2) + np.sum(np.sin(np.pi * u) ** 2)


def newton(u, K, fix=None, tol=1e-13, itmax=200):
    """Minimize with boundary atoms fixed (1 left, 0 right); optional index held fixed."""
    n = len(u)
    for it in range(itmax):
        uf = np.concatenate(([1.0], u, [0.0]))
        g = K * (2 * uf[1:-1] - uf[:-2] - uf[2:]) + np.pi * np.sin(2 * np.pi * u)
        hd = 2 * K + 2 * np.pi**2 * np.cos(2 * np.pi * u)
        ab = np.zeros((3, n))
        ab[0, 1:] = -K
        ab[1, :] = hd
        ab[2, :-1] = -K
        if fix is not None:
            g[fix] = 0.0
            ab[1, fix] = 1.0
            if fix + 1 < n:
                ab[0, fix + 1] = 0.0
            if fix - 1 >= 0:
                ab[2, fix - 1] = 0.0
        if np.max(np.abs(g)) < tol:
            return u, it
        du = solve_banded((1, 1), ab, -g)
        # damped step if Hessian not positive along du
        step = 1.0
        e0 = energy(u, K)
        while step > 1e-6:
            un = u + step * du
            if energy(un, K) <= e0 + 1e-15 or np.max(np.abs(du)) < 1e-10:
                break
            step *= 0.5
        u = un
    return u, itmax


def kink(K, N=401):
    d = np.sqrt(K / (2 * np.pi**2))
    n = np.arange(N) - (N - 1) / 2  # atom positions; centre index (N-1)/2 at 0
    # minimum: centre between atoms, z0 = 1/2
    u0 = (2 / np.pi) * np.arctan(np.exp(-(n - 0.5) / d))
    umin, _ = newton(u0.copy(), K)
    Emin = energy(umin, K)
    # saddle: centre on atom 0, u = 1/2 there
    u1 = (2 / np.pi) * np.arctan(np.exp(-n / d))
    c = (N - 1) // 2
    u1[c] = 0.5
    usad, _ = newton(u1.copy(), K, fix=c)
    Esad = energy(usad, K)
    uf = np.concatenate(([1.0], umin, [0.0]))
    Mdisc = np.sum(np.diff(uf) ** 2)
    return d, Emin, Esad - Emin, Mdisc, umin, n


def cont(d):
    return 4 * d, 2 / (np.pi**2 * d), 16 * np.pi**2 * d**2 / np.sinh(np.pi**2 * d)


ds = np.linspace(0.35, 3.0, 54)
rows = []
for d in ds:
    K = 2 * np.pi**2 * d**2
    N = int(max(401, 60 * d + 1)) | 1
    dd, E, Epn, M, u, n = kink(K, N)
    Ec, Mc, Epnc = cont(dd)
    rows.append((dd, E / Ec, M / Mc, Epn / Epnc, E, Epn, M))
rows = np.array(rows)
print("  d_kink/a   E_disc/E_kink   M_disc/M_kink   E_PN,disc/E_PN(C.20)   1-1/(72d^2)")
for r in rows[::4]:
    print("  %5.3f   %.5f        %.5f         %.5f              %.5f" % (r[0], r[1], r[2], r[3], 1 - 1 / (72 * r[0] ** 2)))

for d in [1.0, 1.23, 2.0]:
    K = 2 * np.pi**2 * d**2
    dd, E, Epn, M, u, n = kink(K)
    Ec, Mc, Epnc = cont(dd)
    print("d_kink = %.2f a: E ratio %.5f, M ratio %.4f, E_PN ratio %.4f (C.20 quotes 22%% low at 1, 17%% at 1.23)" % (d, E / Ec, M / Mc, Epn / Epnc))


def cross(col, level, lo=0.36, hi=2.99):
    f = lambda d: np.interp(d, rows[:, 0], rows[:, col]) - level
    return brentq(f, lo, hi)


# 10 % points on a fine root search, computed directly (not interpolated) for the reported values
def ratio_at(d, which):
    K = 2 * np.pi**2 * d**2
    dd, E, Epn, M, u, n = kink(K)
    Ec, Mc, Epnc = cont(dd)
    return {"E": E / Ec, "M": M / Mc, "PN": Epn / Epnc}[which]


xing = {}
for which, lev in [("E", 0.9), ("M", 0.9), ("M", 1.1), ("PN", 0.9)]:
    try:
        r = brentq(lambda d: ratio_at(d, which) - lev, 0.36, 2.9, xtol=1e-5)
        xing[(which, lev)] = r
        print("%s ratio crosses %.2f at d_kink/a = %.4f" % (which, lev, r))
    except ValueError:
        print("%s ratio: no crossing of %.2f in [0.36, 2.9]" % (which, lev))

# ---------------- tungsten crowdion ----------------
a_W = 3.165
a_ch = np.sqrt(3) / 2 * a_W
M_W = 183.84 * AMU
print("tungsten: a_ch = %.3f A, M_W = %.4e eV" % (a_ch, M_W))
for Ka2 in [50.0, 100.0]:
    Vs = 1.0
    d = np.sqrt(Ka2 / (2 * np.pi**2 * Vs))
    Ek = (2 / np.pi) * np.sqrt(2 * Vs * Ka2)
    Mk = 2 / (np.pi**2 * d)
    Epn = 16 * np.pi**2 * d**2 * Vs / np.sinh(np.pi**2 * d)
    Mkink = Mk * M_W
    Erec = (np.pi * HBARC / a_ch) ** 2 / (2 * Mkink)
    # Mathieu band, plane waves e^{i(k + 2 pi m/a) z}
    def band(Epn_eV):
        m = np.arange(-20, 21)
        Es = []
        for kph in [0.0, np.pi]:
            G = (kph + 2 * np.pi * m) / a_ch
            H = np.diag(HBARC**2 * G**2 / (2 * Mkink) + Epn_eV / 2)
            for i in range(len(m) - 1):
                H[i, i + 1] = H[i + 1, i] = -Epn_eV / 4
            Es.append(eigh(H, eigvals_only=True)[0])
        return Es[1] - Es[0]
    W = band(Epn)
    print("K a^2 = %.0f eV, V_s = 1 eV: d_kink/a = %.3f, E_kink = %.2f eV, M_kink = %.4f M_W, E_PN = %.3e eV, "
          "E_rec = %.3e eV, depth/E_rec = %.3f, band width = %.3e eV = %.3f K"
          % (Ka2, d, Ek, Mk, Epn, Erec, Epn / Erec, W, W / 8.617333e-5))
    W1 = band(1e-3)
    print("    same mass with the atomistic barrier 1 meV: depth/E_rec = %.2f, band width = %.3e eV = %.3f K"
          % (1e-3 / Erec, W1, W1 / 8.617333e-5))
# confinement by the parent vacancy: the gradient criterion |grad phi| a > Delta (Pushkarov Eq. (17)) with
# phi = V0 (a/r)^3 gives 3 V0 (a/r)^4 > Delta, R0 = a (3 V0/Delta)^(1/4); V0 ~ 1 eV assumed (estimate).
# (The source's Eq. (20), R0 = a (V0/Delta)^(1/3), corresponds to |phi| > Delta; printed as a variant.)
for Wb in [13e-6, 34e-6, 90e-6, 166e-6]:
    print("confinement radius for band %.0f ueV, V0 = 1 eV: R0 = a(3V0/Delta)^(1/4) = %.1f lattice spacings "
          "(variant a(V0/Delta)^(1/3) = %.1f)" % (Wb * 1e6, (3.0 / Wb) ** 0.25, (1.0 / Wb) ** (1 / 3)))
# barrier ratio of the discrete chain below one spacing (wording 'well below one spacing')
for dq in (0.4, 0.55, 0.75):
    jj = np.argmin(np.abs(rows[:, 0] - dq))
    print("barrier ratio discrete/continuum at d_kink/a = %.2f: %.3f" % (rows[jj, 0], rows[jj, 3]))
# kink mass at d = 3a, C.20 check
print("C.20 check: M_kink at d_kink = 3a = %.4f M" % (2 / (np.pi**2 * 3)))
print("C.20 check: E_PN at d_kink = 2a = %.2e V_s" % cont(2.0)[2])

# ---------------- figure ----------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.8, 3.1))
d = rows[:, 0]
inside = (np.abs(rows[:, 1] - 1) <= 0.1) & (np.abs(rows[:, 2] - 1) <= 0.1) & (np.abs(rows[:, 3] - 1) <= 0.1)
dmin_in = d[np.argmax(inside)] if inside.any() else None
print("all three ratios within 10%% of one for d_kink/a >= %.3f (grid of the figure)" % dmin_in)
# shade from the last root-searched 10 % crossing at or below the first grid point inside (the value quoted in the caption)
d_shade = max([v for v in xing.values() if v <= dmin_in + 1e-9] or [dmin_in])
ax.axvspan(d_shade, d.max(), color="0.88", lw=0)
ax.plot(d, rows[:, 1], "r-", lw=1.5, label=r"$E_{\mathrm{disc}}/E_{\mathrm{kink}}$")
ax.plot(d, rows[:, 2], "b-", lw=1.5, label=r"$M_{\mathrm{disc}}/M_{\mathrm{kink}}$")
ax.plot(d, rows[:, 3], "g-", lw=1.5, label=r"$E_{\mathrm{PN,disc}}/E_{\mathrm{PN}}$")
dd = d[d > 0.5]
ax.plot(dd, 1 - 1 / (72 * dd**2), "k:", lw=1.0, label=r"$1 - a_{\mathrm{ch}}^2/72d_{\mathrm{kink}}^2$")
ax.axhline(1.0, color="0.4", lw=0.6)
ax.set_xlim(d.min(), d.max())
ax.set_ylim(0.0, 1.6)
ax.set_xlabel(r"$d_{\mathrm{kink}}/a_{\mathrm{ch}}$")
ax.set_ylabel("discrete / continuum")
ax.legend(loc="lower right", fontsize=7.5, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit19_6b.pdf"))
print("wrote limit19_6b.pdf")
