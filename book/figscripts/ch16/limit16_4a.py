"""Limit Check 16.4a (lim:16.4a, fig:16-limit-frenkel): the binned (incoherent) Frenkel rate, the sum of molecular |f|^2 at
the molecular line energies (the published form, arXiv:1912.02822 Eq. (19), arXiv:2103.08601 Eq. (8)), against the full
Frenkel-exciton response of the anthracene model of frenkel16_4.py, as a function of the dark-matter mass.

Full response at momentum transfer q (unreduced): all 49 pi-electron singlets on both molecules (98 states), Frenkel
Hamiltonian H = diag(E_x + delta) + J(q) + M(q), with J the intermolecular coupling (macroscopic term removed) and M(q) the
macroscopic term (4 pi e^2/Omega) F(q) F(q)^dagger/q^2, so that H is the complete density response in this basis (weights not
divided by |eps|^2; App. D.12).  delta is fixed so that the lowest optically allowed exciton at Q -> 0 (transverse, the
absorption line) lies at the bare L_a energy, 3.1 eV: both curves then share the measured optical edge.  Weights
W_lambda = |sum A^lambda* F(q)|^2; isotropic halo:
   R = rho_chi sigma_e/(2 m_chi mu^2 M_cell) int q dq eta(v_min) F_DM^2 <sum_lambda W_lambda>   (bare: sum_{o,x} |f|^2 at E_x).
Plot: y = R_full/R_bare against m_chi (MeV), heavy (solid) and light (dashed) mediator; dash-dotted: full response without the
macroscopic term (heavy); thin line at 1: the binned bare sum; shaded: masses where the heavy-mediator ratio is within 10 %.
Quadrature: 44 values of q, log-spaced 0.6-45 keV; 120 Fibonacci directions; trapezoid in ln q.  Printed: the ratios at
selected masses, the 10 % crossing (root-finder on a cubic interpolation in ln m), and a direction-grid check.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import numpy as np
from scipy.optimize import brentq
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import frenkel16_4 as F  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")
st = list(range(len(F.E_X)))
EB = np.concatenate([F.E_X, F.E_X])

# ---- calibrate delta: lowest Q -> 0 exciton with an optical dipole at 3.1 eV --------------------------------------
dvec = np.vstack([F.dipoles(F.R1), F.dipoles(F.R2)])
Q0 = 1e-3 * F.RECIP[1]
J0 = F.frenkel_J(Q0, st)
E, A = np.linalg.eigh(np.diag(EB) + J0)
dl = np.abs(A.conj().T @ dvec)
bright = np.where((dl**2).sum(1) > 1e-3)[0]
delta = F.S1_EXP - E[bright[0]]
print(f"lowest optically allowed Q->0 exciton of the full model at {E[bright[0]]:.4f} eV (dipole {np.round(dl[bright[0]],3)} eA"
      f" along a, b, c'); lowest exciton {E[0]:.4f} eV; shift delta = {delta:+.4f} eV")
EF = EB + delta


def tables(dirs, qk, with_macro=True):
    """Exciton energies and weights on (q, direction): arrays (nq, ndir, 98)."""
    En = np.zeros((len(qk), len(dirs), len(EF)))
    Wn = np.zeros_like(En)
    Wb = np.zeros((len(qk), len(dirs), len(EF)))
    for i, q in enumerate(qk):
        for j, d in enumerate(dirs):
            qv = d * q / F.KEV_PER_INVA
            V = F.frenkel_J(qv, st)
            if with_macro:
                V = V + F.macro_term(qv, st)
            e, a = np.linalg.eigh(np.diag(EF) + V)
            Fv = F.F_cell(qv[None, :], st)[:, 0]
            En[i, j] = e
            Wn[i, j] = np.abs(a.conj().T @ Fv) ** 2
            Wb[i, j] = np.abs(Fv) ** 2
    return En, Wn, Wb


def rate_iso(m, qk, En, Wn, light=False):
    """Relative isotropic rate int q dq eta F^2 <sum W> (common prefactor dropped); eta in the closed form of App. D.1."""
    mu = m * F.ME / (m + F.ME)
    q = qk * 1e3
    w = np.gradient(np.log(q))
    w[0] *= 0.5
    w[-1] *= 0.5
    FDM2 = (F.ALPHA * F.ME / q) ** 4 if light else np.ones_like(q)
    vmin = (En / q[:, None, None] + q[:, None, None] / (2 * m)) * F.C_KMS
    eta = F.eta(vmin)
    return (q**2 * w * FDM2 * (eta * Wn).sum(-1).mean(-1)).sum() / mu**2


dirs = F.fib_sphere(120)
qk = np.geomspace(0.6, 45.0, 44)
Ef, Wf, Wb = tables(dirs, qk)
El, Wl, _ = tables(dirs, qk, with_macro=False)
Ebare = np.broadcast_to(EB, Wb.shape)
print(f"check: sum of weights full/bare over all states, all q and directions = {Wf.sum()/Wb.sum():.8f} (unitarity)")

masses = np.geomspace(0.75e6, 1e9, 40)
res = []
for m in masses:
    rb = rate_iso(m, qk, Ebare, Wb)
    rf = rate_iso(m, qk, Ef, Wf)
    rl = rate_iso(m, qk, El, Wl)
    rbL = rate_iso(m, qk, Ebare, Wb, light=True)
    rfL = rate_iso(m, qk, Ef, Wf, light=True)
    res.append((m, rf / rb if rb > 0 else np.nan, rl / rb if rb > 0 else np.nan, rfL / rbL if rbL > 0 else np.nan, rb, rf))
res = np.array(res)
mm, rH, rLF, rL, rb, rf = res.T
for m, a, b, c, x, y in res:
    print(f"m = {m/1e6:8.3f} MeV: full/bare heavy = {a:.3f}, light = {c:.3f}; without macroscopic term (heavy) = {b:.3f}"
          f"  [bare {x:.3e}, full {y:.3e}]")
mth_b = 2 * F.S1_EXP / F.VMAX**2
mth_f = 2 * Ef.min() / F.VMAX**2
print(f"threshold masses: bare 2 E(L_a)/v_max^2 = {mth_b/1e6:.3f} MeV; full model, lowest exciton {Ef.min():.3f} eV on the grid:"
      f" {mth_f/1e6:.3f} MeV")
lm = np.log(mm)
fin = np.isfinite(rH)
for name, arr in (("heavy", rH), ("light", rL)):
    g = np.isfinite(arr)
    f = interp1d(lm[g], np.abs(arr[g] - 1) - 0.1, kind="cubic")
    xs = np.linspace(lm[g][0], lm[g][-1], 4000)
    v = f(xs)
    idx = np.where(np.diff(np.sign(v)) != 0)[0]
    roots = [np.exp(brentq(f, xs[i], xs[i + 1])) / 1e6 for i in idx]
    print(f"{name}: |ratio - 1| = 0.1 at m = {np.round(roots, 3)} MeV")
    for m0 in (1.0, 2.0, 5.0, 10.0, 100.0, 1000.0):
        if np.log(m0 * 1e6) >= lm[g][0]:
            print(f"   ratio at {m0:6.1f} MeV: {float(interp1d(lm[g], arr[g], kind='cubic')(np.log(m0*1e6))):.3f}")
# direction-grid check
Ef2, Wf2, Wb2 = tables(F.fib_sphere(40), qk[::3])
for m0 in (2e6, 100e6):
    a = rate_iso(m0, qk[::3], Ef2, Wf2) / rate_iso(m0, qk[::3], np.broadcast_to(EB, Wb2.shape), Wb2)
    print(f"grid check (40 directions, every third q) at {m0/1e6:.0f} MeV: ratio {a:.3f}")

# ---- plot ----------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
g = np.isfinite(rH)
mf = np.geomspace(mm[g][0], mm[g][-1], 500)
rHf = interp1d(lm[g], rH[g], kind="cubic")(np.log(mf))
ax.fill_between(mf / 1e6, 0, 10, where=np.abs(rHf - 1) <= 0.1, color="0.88", lw=0)
ax.axhline(1.0, color="k", lw=0.8, label="binned bare sum (published form)")
ax.semilogx(mf / 1e6, rHf, color="C0", lw=1.6, label="full Frenkel response, heavy mediator")
gl = np.isfinite(rL)
ax.semilogx(mm[gl] / 1e6, rL[gl], color="C3", lw=1.2, ls="--", label="full Frenkel response, light mediator")
ax.semilogx(mm[g] / 1e6, rLF[g], color="C2", lw=1.0, ls="-.", label="without the macroscopic term, heavy")
ax.axvline(mth_b / 1e6, color="0.5", lw=0.6, ls=":")
ax.set_xlim(0.75, 1000)
ax.set_ylim(0.0, 3.0)
ax.set_xlabel(r"dark-matter mass $m_\chi$ (MeV)")
ax.set_ylabel(r"$\mathcal{R}_{\mathrm{full}}/\mathcal{R}_{\mathrm{binned}}$")
ax.legend(loc="upper right", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "limit16_4a.pdf"))
print("wrote limit16_4a.pdf")
