"""Limit Check 13.7a (lim:13.7a, Sect. 13.7): the special (Zacharias-Giustino) displacement as a one-configuration
quadrature of the adiabatic thermal average, against the Allen-Heine-Cardona (AHC) thermal average, as a function of
supercell size. Output: tex/figures/ch13/limit13_7a.pdf, log limit13_7a.log.

This is a labelled MODEL, not silicon. It is chosen so that every quantity is exact and cheap:
  * lattice: simple cubic, a = 2.70 A, one atom of mass M = 28.0855 u per cell;
  * phonons: central springs to the 6 nearest neighbours (k1) and the 12 next-nearest neighbours (k2), harmonic (top of the band 64.6 meV at X);
    D_ab(Q) = (1/M) sum_d k_d n_a n_b [1 - cos(Q.d)], k1 = 4.0 eV/A^2, k2 = 1.5 eV/A^2;
  * electrons: one s orbital per atom, nearest-neighbour hopping t(d) = -t0 (a/d)^6 (a steep power, standing for the
    near-exponential decay of s-orbital overlaps; it sets the band-bottom shift at a few tens of meV), t0 = 1.0 eV, so that the band bottom at k = 0 is -6 t0 with mass 1/(2 t0 a^2) = 0.52 m_e;
  * observable: the energy of the band bottom (the lowest one-electron level), T = 0 (zero point).
Literature formula: the ZG displacement (Zacharias and Giustino, arXiv:1604.02394, Eq. (5); in the set-B form of
arXiv:1912.10929, Eq. (2) = eq:E.8-zg of the book): one configuration with every normal coordinate at +-sigma_Qnu,
sigma^2 = (2n+1)/(2 omega), signs alternating along the modes sorted by frequency, Q = -Q (mod G) modes left out;
the band-bottom shift of that one supercell is the estimate of the thermal average.
Fuller results:
  (i) AHC: the second-order (adiabatic Fan + Allen-Heine) thermal average, analytic for this model,
      Fan  = (1/N) sum_{Q != 0, nu} t'^2 |sum_a e_a 2 sin(Q_a a)|^2 (2n+1)/(2 M omega) / (eps_0 - eps_Q),
      AH   = 2 sum_a [ t'/(2a) sum_{b != a} <D_b^2>_a + t''/2 <D_a^2>_a ],
      <D_b D_c>_a = (1/(N M)) sum_{Q nu} e_b e_c 2[1 - cos(Q_a a)] (2n+1)/(2 omega),
      t' = 6 t0 / a, t'' = -42 t0 / a^2, on the N^3 grid of the supercell and extrapolated to N -> infinity
      (fit a + b/N + c/N^2 on N = 16..128; Ponce et al. 1504.05992 Table II: adiabatic, non-polar, band extremum
      converges as 1/N);
  (ii) the exact adiabatic (Williams-Lax) average of the same supercell: Monte Carlo over Gaussian configurations of all
      modes (antithetic pairs), all orders in the displacements.
Check printed: the Allen-Heine term of a uniform translation (Q -> 0 acoustic) vanishes.
Run: python limit13_7a.py  (about 3 minutes on 4 cores)
"""
import os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch13")
LOG = open(os.path.join(HERE, "limit13_7a.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.write(s + "\n")


HBARC = 1973.269804               # eV A
AMU = 931.49410242e6              # eV
A = 2.70                          # A
M = 28.0855 * AMU / HBARC**2      # eV^-1 A^-2 * ... : mass in eV / (eV A)^2 -> M omega^2 in eV/A^2 when omega in eV
T0 = 1.0                          # eV
P = 6                             # hopping exponent, t = -t0 (a/d)^P
K1, K2 = 4.0, 1.5                 # eV/A^2
TP = P * T0 / A                   # dt/dd at d = a (eV/A)
TPP = -P * (P + 1) * T0 / A**2    # d2t/dd2 at d = a (eV/A^2)
EPS0 = -6 * T0

NN = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)
NNN = np.array([[s1, s2, 0] for s1 in (1, -1) for s2 in (1, -1)] + [[s1, 0, s2] for s1 in (1, -1) for s2 in (1, -1)]
               + [[0, s1, s2] for s1 in (1, -1) for s2 in (1, -1)], float)


def phonons(Qa):
    """Qa: (n,3) wavevector times a (dimensionless). Returns omega (n,3) in eV and real eigenvectors (n,3,3)."""
    D = np.zeros((len(Qa), 3, 3))
    for d, k in [(NN, K1), (NNN, K2)]:
        for v in d:
            nv = v / np.linalg.norm(v)
            D += k * (1 - np.cos(Qa @ v))[:, None, None] * np.outer(nv, nv)[None]
    D /= M
    w2, e = np.linalg.eigh(D)
    return np.sqrt(np.clip(w2, 0, None)), e


def ahc(N, chunk=200000):
    """Adiabatic AHC zero-point shift of the band bottom on the N^3 grid (Q = 0 left out). Returns (Fan, AH) in eV."""
    g = 2 * np.pi * np.arange(N) / N
    Qa = np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)[1:]
    fan, DD = 0.0, np.zeros((3, 3, 3))           # DD[alpha, b, c] = sum e_b e_c 2(1-cos Q_alpha a)/(2 omega)
    for i in range(0, len(Qa), chunk):
        q = Qa[i:i + chunk]
        w, e = phonons(q)
        s = np.sin(q)
        proj = np.einsum("na,nam->nm", s, e)     # sum_a sin(Q_a a) e_a  per branch m
        epsQ = -2 * T0 * np.cos(q).sum(1)
        fan += np.sum(TP**2 * 4 * proj**2 / (2 * M * w) / (EPS0 - epsQ)[:, None])
        for al in range(3):
            fac = 2 * (1 - np.cos(q[:, al]))[:, None] / (2 * w)
            DD[al] += np.einsum("nbm,ncm,nm->bc", e, e, fac)
    fan /= N**3
    DD /= N**3 * M
    ah = 0.0
    for al in range(3):
        perp = sum(DD[al][b, b] for b in range(3) if b != al)
        ah += 2 * (TP / (2 * A) * perp + 0.5 * TPP * DD[al][al, al])
    return fan, ah


def hamiltonian(N, u):
    """Sparse supercell Hamiltonian with displacements u (N^3,3) in A; exact t(d)."""
    idx = np.arange(N**3).reshape(N, N, N)
    rows, cols, vals = [], [], []
    for al in range(3):
        j = np.roll(idx, -1, axis=al).ravel()
        dvec = A * np.eye(3)[al][None] + u[j] - u
        d = np.linalg.norm(dvec, axis=1)
        t = -T0 * (A / d) ** P
        rows += [idx.ravel(), j]
        cols += [j, idx.ravel()]
        vals += [t, t]
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N**3, N**3))


def lowest(N, u):
    H = hamiltonian(N, u)
    v0 = np.ones(N**3)
    val = spla.eigsh(H, k=1, which="SA", v0=v0, tol=1e-10)[0][0]
    return val - EPS0


def modes(N):
    """Commensurate modes: set B (one of each +-Q pair, self-partners separate). Returns lists of (Qa, omega, e)."""
    g = 2 * np.pi * np.arange(N) / N
    seen, B, S = set(), [], []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if (i, j, k) == (0, 0, 0):
                    continue
                mi = ((-i) % N, (-j) % N, (-k) % N)
                if (i, j, k) in seen:
                    continue
                seen.add((i, j, k)); seen.add(mi)
                (S if mi == (i, j, k) else B).append((i, j, k))
    return [np.array([[g[i], g[j], g[k]] for i, j, k in L]).reshape(-1, 3) for L in (B, S)]


def positions(N):
    r = np.arange(N)
    return np.stack(np.meshgrid(r, r, r, indexing="ij"), -1).reshape(-1, 3).astype(float)


def zg_shift(N):
    QB, _ = modes(N)
    w, e = phonons(QB)
    R = positions(N)
    # flatten (Q, nu), sort by frequency, alternate signs; gauge: first nonzero component positive
    Qf = np.repeat(QB, 3, axis=0)
    wf = w.ravel()
    ef = np.transpose(e, (0, 2, 1)).reshape(-1, 3)
    for n in range(len(ef)):
        nz = np.flatnonzero(np.abs(ef[n]) > 1e-8)
        if ef[n, nz[0]] < 0:
            ef[n] *= -1
    order = np.argsort(wf, kind="stable")
    sgn = np.empty(len(wf)); sgn[order] = (-1.0) ** np.arange(len(wf))
    amp = sgn * np.sqrt(1.0 / (2 * N**3 * M * wf)) * 2       # T = 0: 2n+1 = 1
    u = np.zeros((N**3, 3))
    for i in range(0, len(wf), 3000):
        c = np.cos(R @ Qf[i:i + 3000].T)                      # (N^3, chunk)
        u += c @ (amp[i:i + 3000, None] * ef[i:i + 3000])
    return lowest(N, u), u


def mc_shift(N, nsamp, rng):
    QB, QS = modes(N)
    wB, eB = phonons(QB)
    R = positions(N)
    cB, sB = np.cos(R @ QB.T), np.sin(R @ QB.T)
    if len(QS):
        wS, eS = phonons(QS)
        cS = np.cos(R @ QS.T)
    vals = []
    for _ in range(nsamp // 2):
        # complex X_Q for set B: Re, Im each variance 1/(4 omega); u = (1/sqrt(N M)) sum 2 Re[e X e^{iQR}]
        xr = rng.standard_normal(wB.shape) * np.sqrt(1 / (4 * wB))
        xi = rng.standard_normal(wB.shape) * np.sqrt(1 / (4 * wB))
        u = 2 * (cB @ np.einsum("qam,qm->qa", eB, xr) - sB @ np.einsum("qam,qm->qa", eB, xi))
        if len(QS):
            xs = rng.standard_normal(wS.shape) * np.sqrt(1 / (2 * wS))
            u += cS @ np.einsum("qam,qm->qa", eS, xs)
        u /= np.sqrt(N**3 * M)
        vals.append(0.5 * (lowest(N, u) + lowest(N, -u)))
    vals = np.array(vals)
    return vals.mean(), vals.std(ddof=1) / np.sqrt(len(vals))


out("Model: simple cubic, a = %.2f A, M = 28.0855 u, k1 = %.1f, k2 = %.1f eV/A^2, t0 = %.1f eV, t ~ d^-%d" % (A, K1, K2, T0, P))
wX = phonons(np.array([[np.pi, 0, 0], [np.pi, np.pi, np.pi]]))[0]
out("phonons at X (meV):", np.round(wX[0] * 1e3, 2), " at R:", np.round(wX[1] * 1e3, 2))
out("band-bottom mass 1/(2 t0 a^2) = %.3f m_e" % (HBARC**2 / (2 * T0 * A**2) / 510998.95))

# a uniform translation changes nothing: Allen-Heine weight of acoustic modes vanishes as Q -> 0
for qa in (1e-2, 1e-3):
    w, e = phonons(np.array([[qa, 0, 0]]))
    tot = []
    for m in range(3):
        acc = 0.0
        for al in range(3):
            fac = 2 * (1 - np.cos([qa, 0, 0][al])) / (2 * w[0, m])
            ee = np.outer(e[0, :, m], e[0, :, m]) * fac / M
            acc += 2 * (TP / (2 * A) * sum(ee[b, b] for b in range(3) if b != al) + 0.5 * TPP * ee[al, al])
        tot.append(acc)
    out("Allen-Heine weight of the three acoustic modes at Q a = %g (eV per mode):" % qa, np.array(tot))

# AHC on grids and extrapolation
Ngrid = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 48, 64, 96, 128]
ahcN = {}
for N in Ngrid:
    f, h = ahc(N)
    ahcN[N] = f + h
    out("AHC N = %3d: Fan %.2f  AH %.2f  total %.3f meV" % (N, f * 1e3, h * 1e3, (f + h) * 1e3))
xs = np.array([N for N in Ngrid if N >= 16], float)
ys = np.array([ahcN[int(N)] for N in xs])
cf = np.polyfit(1 / xs, ys, 2)
AHCINF = cf[-1]
out("AHC extrapolated (a + b/N + c/N^2, N >= 16): %.3f meV; b = %.1f meV" % (AHCINF * 1e3, cf[-2] * 1e3))

# ZG one-shot and Monte Carlo
rng = np.random.default_rng(13)
NZG = [3, 4, 5, 6, 8, 10, 12, 14, 16, 20, 24]
zg = {}
for N in NZG:
    zg[N] = zg_shift(N)[0]
    out("ZG  N = %2d (%5d atoms): %.3f meV   [AHC same grid %.3f, limit %.3f]" % (N, N**3, zg[N] * 1e3, ahcN.get(N, ahc(N)[0] + ahc(N)[1]) * 1e3, AHCINF * 1e3))
NMC = [4, 6, 8, 12, 16]
mc = {}
for N in NMC:
    mc[N] = mc_shift(N, 256 if N <= 8 else (64 if N <= 12 else 32), rng)
    out("MC  N = %2d: exact adiabatic average %.3f +- %.3f meV" % (N, mc[N][0] * 1e3, mc[N][1] * 1e3))

# validity: ZG within 2 meV of the converged AHC average
ok = [N for N in NZG if abs(zg[N] - AHCINF) * 1e3 <= 2.0]
nval = min(N for N in NZG if all(abs(zg[n] - AHCINF) * 1e3 <= 2.0 for n in NZG if n >= N))
out("ZG within 2 meV of the converged AHC for N >=", nval, "(", nval**3, "atoms )")
out("fourth-order (all-orders minus AHC on the same grid):",
    ", ".join("N=%d: %+.2f meV" % (N, (mc[N][0] - (ahcN[N] if N in ahcN else sum(ahc(N)))) * 1e3) for N in NMC))

# ---------------- figure ----------------
plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6, "pdf.fonttype": 42})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
Nl = np.linspace(2.6, 26, 200)
ax.axvspan(nval - 0.5, 26, color="0.93", lw=0, zorder=0)
ax.axhspan((AHCINF - 0.002) * 1e3, (AHCINF + 0.002) * 1e3, color="tab:blue", alpha=0.10, lw=0, zorder=0)
ax.axhline(AHCINF * 1e3, color="k", lw=0.9, ls="--", label="AHC thermal average, converged", zorder=1)
Na = [N for N in Ngrid if 3 <= N <= 24]
ax.plot(Na, [ahcN[N] * 1e3 for N in Na], color="0.45", lw=0.9, marker="s", ms=3, label="AHC on the same grid", zorder=2)
ax.plot(NZG, [zg[N] * 1e3 for N in NZG], "o", color="tab:red", ms=4.5, label="special displacement (one configuration)", zorder=4)
ax.errorbar(NMC, [mc[N][0] * 1e3 for N in NMC], yerr=[mc[N][1] * 1e3 for N in NMC], fmt="D", mfc="none", mec="tab:blue",
            ecolor="tab:blue", ms=4.5, lw=0.8, label="exact adiabatic average (Monte Carlo)", zorder=3)
ax.text(nval + 0.3, (AHCINF + 0.0022) * 1e3, r"$\pm$2 meV", fontsize=7, color="tab:blue", va="bottom")
ax.set_xlim(2.5, 25.5)
ax.set_ylim(-47.5, -36.5)
ax.set_xlabel(r"cells along each edge of the supercell")
ax.set_ylabel("zero-point shift of the band bottom (meV)")
ax.legend(fontsize=7, frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit13_7a.pdf"))
out("wrote limit13_7a.pdf")
