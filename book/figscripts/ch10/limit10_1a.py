"""Limit-box plot 10.1a (tex/figures/ch10/limit10_1a.pdf): the unscreened crystal-form-factor rate against the screened
rate with local fields, at fixed energy deposited, as a function of the momentum transfer q.

Model (one model for all three curves, so that the comparison isolates screening): the local empirical pseudopotential
of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), via figscripts/ch03/epm.py (a = 5.43 A, 113 plane waves, no
spin-orbit coupling; model indirect gap 0.82 eV), with the bubble, approximations and local-field set of figscripts/ch08/we8_10.py:
  IP (the formula of the box, T_0):      S0 = -2 Im R0_00                      (eq:4.6-R0, eq:A.7-FDT at T = 0)
  RPA, head only (leading correction):    S = -2 Im [R0_00 / (1 - v_C(q) R0_00)] (eq:4.6-rpa)
  RPA + local fields (fuller result):     R = R0 + R0 v_C R over the 51 vectors |G|^2 <= 11 (2 pi/a)^2, S = -2 Im R_00
                                          (at q0 this is the set of we8_10.py up to the ordering of equal |q + G|)
Adler-Wiser sum at T = 0, 4 valence and NC = 26 conduction bands, resonant and antiresonant terms, Lorentzian broadening
ETA = 0.15 eV; spectra averaged over omega in [OMB - 0.5, OMB + 0.5] eV (OMB = 5 eV, the energy of the box) to smooth the
finite k grid. q along the generic direction (5,3,1) (env QDIR), unreduced (never folded; Sect. 3.1): on this ray the
distance min_G |q + G| stays >= 0.83 (2 pi/a) for 0.75 <= q/q0 <= 3, so no Umklapp component q + G is nearly zero. Along [100]
the points q = |G_200| = 1.22 q0 and |G_400| = 2.45 q0 have |q + G| ~ 0.05 (2 pi/a), where v_C(q + G) is huge and the local-field
result depends on the size of the set (at 2.4 q0, 5 eV: LF/IP = 0.50 with the 51-vector set, 0.41 with the set enlarged by
|q + G|^2 <= 11; limit10_1a_NK12.log, limit10_1a_union.log): a measure-zero sliver of the angular average, not used for the box.
Checks: NK = 16 against NK = 12 at q0 along [100]: S0 9.11e7 against 9.21e7 eV^2, LF/IP 0.245 both (limit10_1a_NK16check.log);
local-field set on (5,3,1) at 2.4 q0: see limit10_1a_union_531.log.
EPM basis |k + G|^2 <= 21 (2 pi/a)^2, i.e. momenta up to 2.8 q0: the model has no true high-momentum tails, and the plot stops
at 2.8 q0.
Rate weight (Limit 10.1a, heavy mediator F_DM = 1): d(dR/d omega)/dq proportional to q eta(v_min) S(q, omega) with
v_min = omega/q + q/2 m_chi, m_chi = 10 MeV, book halo (App. A.8; eta closed form of App. D.1, as in we10_1.py).
Shaded: q where |S_LF/S0 - 1| < 0.1. The direction (5,3,1) stands in for the angular average of the box formula.
Run: python3 limit10_1a.py (single-threaded BLAS).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")   # batched small eigenproblems: single-threaded is fastest here
import sys
import time
import numpy as np
from scipy.special import erf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, BOHR, B, HBARC   # noqa: E402

HA = 2 * RY
ME = 510998.95
ALPHA = 1 / 137.035999177
NK = int(os.environ.get("NK", 12))
NC, NV = 26, 4
NB = NV + NC
ETA = 0.15
OMB = 5.0
OM = np.round(np.arange(OMB - 0.5, OMB + 0.501, 0.05), 3)
QLIST = [float(x) for x in os.environ.get(
    "QLIST", "0.25,0.35,0.5,0.65,0.8,1.0,1.2,1.4,1.7,2.0,2.4,2.8,3.3").split(",")]
QDIR = [float(x) for x in os.environ.get("QDIR", "5,3,1").split(",")]
QHAT = np.array(QDIR) / np.linalg.norm(QDIR)
OUTNPZ = os.path.join(HERE, f"limit10_1a_data_NK{NK}_{''.join(str(int(x)) for x in QDIR)}{os.environ.get('OUTTAG', '')}.npz")

si = EPM("Si")
a_A = si.a
a = a_A / BOHR
Omega = a**3 / 4
tpa = 2 * np.pi / a
Gb = si.G
NPW = len(Gb)
key = {tuple(np.rint(g).astype(int)): i for i, g in enumerate(Gb)}
unit_eV = 2 * np.pi * HBARC / a_A
q0 = ALPHA * ME
AU_R_TO_EV2 = (HBARC / BOHR) ** 3 / HA
_n = 8
_idx = np.array([(i, j, k) for i in range(-_n, _n + 1) for j in range(-_n, _n + 1) for k in range(-_n, _n + 1)])
cand = _idx @ B
cand = cand[(cand**2).sum(1) <= 80]                      # fold candidates, radius 8.9 (2 pi/a)
LF = np.where((Gb**2).sum(1) <= 11.01)[0]                # local-field set: shells |G|^2 = 0, 3, 4, 8, 11 (51 vectors)
I0 = int(np.where((Gb**2).sum(1) < 1e-9)[0][0])

f = (np.arange(NK) + 0.5) / NK - 0.5
kc = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
kpts = kc @ B
NKT = len(kpts)
pref_au = 2.0 / (NKT * Omega)


def states(ks):
    w, v = np.linalg.eigh(si.hamiltonian(ks))
    return w[:, :NB] * RY, v[:, :, :NB]


def fold(kq):
    # reciprocal vector that brings k + q into the first zone (nearest lattice point of the reciprocal lattice)
    return cand[np.argmin(((kq[None, :] - cand) ** 2).sum(1))]


def spectra(qf):
    qvec = qf * q0 / unit_eV * QHAT
    qG2 = ((qvec + Gb) ** 2).sum(1)
    LFq = LF
    if os.environ.get("LFMODE") == "union":   # check: add the vectors with |q + G|^2 <= 11 (2 pi/a)^2 (around G = -q)
        LFq = np.union1d(LF, np.where(qG2 <= 11.01)[0])
    i0 = int(np.where(LFq == I0)[0][0])
    NG = len(LFq)
    vC = 4 * np.pi / (qG2[LFq] * tpa**2)
    maps = {}

    def shift_map(GU):
        k_ = tuple(np.rint(GU).astype(int))
        if k_ not in maps:
            M = -np.ones((NG, NPW), int)
            for a_, i in enumerate(LFq):
                s = Gb[i] + GU
                for j, g in enumerate(Gb):
                    M[a_, j] = key.get(tuple(np.rint(g + s).astype(int)), -1)
            maps[k_] = M
        return maps[k_]

    w_au = OM / HA
    R0 = np.zeros((len(OM), NG, NG), complex)
    chunk = 32
    for c0 in range(0, NKT, chunk):
        ks = kpts[c0:c0 + chunk]
        GUs = np.array([fold(k + qvec) for k in ks])
        e1, c1 = states(ks)
        e2, c2 = states(ks + qvec - GUs)
        for i in range(len(ks)):
            SM = shift_map(GUs[i])
            pad = np.vstack([c2[i], np.zeros((1, NB))])
            cs = pad[SM]
            A = np.einsum("agc,gv->avc", cs[:, :, NV:].conj(), c1[i][:, :NV]).reshape(NG, -1)
            Bm = np.einsum("agv,gc->avc", cs[:, :, :NV].conj(), c1[i][:, NV:]).reshape(NG, -1)
            dEr = ((e2[i][NV:][None, :] - e1[i][:NV][:, None]) / HA).reshape(-1)
            dEa = ((e1[i][NV:][None, :] - e2[i][:NV][:, None]) / HA).reshape(-1)
            dr = 1.0 / (w_au[:, None] - dEr[None, :] + 1j * ETA / HA)
            da = 1.0 / (w_au[:, None] + dEa[None, :] + 1j * ETA / HA)
            R0 += np.einsum("ap,wp,bp->wab", A.conj(), dr, A, optimize=True) \
                - np.einsum("ap,wp,bp->wab", Bm.conj(), da, Bm, optimize=True)
    R0 *= pref_au
    S0 = -2 * R0[:, i0, i0].imag * AU_R_TO_EV2
    epsH = 1 - vC[i0] * R0[:, i0, i0]
    S_rpa = -2 * (R0[:, i0, i0] / epsH).imag * AU_R_TO_EV2
    S_lf = np.empty(len(OM))
    for iw in range(len(OM)):
        R = np.linalg.solve(np.eye(NG) - R0[iw] * vC[None, :], R0[iw])
        S_lf[iw] = -2 * R[i0, i0].imag * AU_R_TO_EV2
    return S0.mean(), S_rpa.mean(), S_lf.mean(), np.abs(epsH).mean()


if os.environ.get("PLOT_ONLY") != "1":
    res = []
    for qf in QLIST:
        t = time.time()
        r = spectra(qf)
        dmin = np.min(np.linalg.norm(qf * q0 / unit_eV * QHAT + cand, axis=1))
        res.append(r)
        print(f"q = {qf:4.2f} q0: S0 = {r[0]:.3e}, S_RPA = {r[1]:.3e}, S_RPA+LF = {r[2]:.3e} eV^2; "
              f"min|q+G| = {dmin:.2f} (2pi/a); LF/IP = {r[2]/r[0]:.3f}, RPA/IP = {r[1]/r[0]:.3f}, |eps_head| = {r[3]:.2f}  ({time.time()-t:.0f} s)",
              flush=True)
    np.savez(OUTNPZ, Q=np.array(QLIST), RES=np.array(res))

# ---------------- plot ----------------
if os.environ.get("NOPLOT") == "1":
    sys.exit(0)
d = np.load(OUTNPZ)
Q, RES = d["Q"], d["RES"]
S0, Srpa, Slf = RES[:, 0], RES[:, 1], RES[:, 2]
CKM = 299792.458
V0, VESC, VE = 238.0, 544.0, 250.5
Z = VESC / V0
NESC = np.pi**1.5 * V0**3 * (erf(Z) - 2 / np.sqrt(np.pi) * Z * np.exp(-Z**2))


def eta(u):
    k = np.pi * V0**2 / (VE * NESC)
    u = np.maximum(u, 0.0)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(Z) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-Z**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0))


MCHI = 10e6
qe = Q * q0
wgt = qe * eta((OMB / qe + qe / (2 * MCHI)) * CKM)
r_lf = Slf / S0
print("\nq/q0, LF/IP, RPA/IP:", [(round(a_, 2), round(b_, 3), round(c_, 3)) for a_, b_, c_ in zip(Q, r_lf, Srpa / S0)])
# validity: |LF/IP - 1| < 0.1, from the largest q downward
ok = np.abs(r_lf - 1) < 0.1
# rate at fixed omega (trapezoid over the computed q points, heavy mediator)
I0 = np.trapezoid(wgt * S0, qe)
Ilf = np.trapezoid(wgt * Slf, qe)
Irpa = np.trapezoid(wgt * Srpa, qe)
print(f"q-integrated rate at omega = {OMB} eV (heavy, m = 10 MeV, q from {Q[0]} to {Q[-1]} q0): "
      f"RPA+LF/IP = {Ilf/I0:.3f}, RPA/IP = {Irpa/I0:.3f}")
qmin = OMB / ((VESC + VE) / CKM)
print(f"kinematic q_min at {OMB} eV: {qmin/q0:.2f} q0")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5, "pdf.fonttype": 42,
                     "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.0))
norm = (wgt * S0).max()
ax.plot(Q, wgt * S0 / norm, "k-", lw=1.4, marker="o", ms=2.5, label=r"independent particles")
ax.plot(Q, wgt * Srpa / norm, color="0.45", ls=":", lw=1.3, label=r"screened, $1/|\varepsilon|^2$ only")
ax.plot(Q, wgt * Slf / norm, color="C3", ls="--", lw=1.4, marker="s", ms=2.5, label=r"screened, with local fields")
# validity: shade q where |LF/IP - 1| < 0.1 (none within the plotted range on (5,3,1) at 5 eV; STYLE fallback then marks the
# 10 percent crossing of the head-only (RPA) ratio instead)
def crossing(r):
    bad = np.where(np.abs(r - 1) >= 0.1)[0]
    if len(bad) == 0:
        return Q[0]
    i1 = bad[-1]
    if i1 + 1 >= len(Q):
        return None
    y1, y2 = abs(r[i1] - 1), abs(r[i1 + 1] - 1)
    return Q[i1] + (y1 - 0.1) * (Q[i1 + 1] - Q[i1]) / (y1 - y2)
qv = crossing(r_lf)
qh = crossing(Srpa / S0)
print(f"LF within 10% of IP for q > {qv} q0; head-only RPA within 10% for q > {qh:.2f} q0 = {qh*q0/1e3:.2f} keV")
if qv is not None:
    ax.axvspan(qv, Q[-1] * 1.05, color="0.9", lw=0)
if qh is not None:
    ax.axvline(qh, color="0.45", lw=0.8, ls=":")
    ax.text(qh + 0.03, 0.55, "RPA head\nwithin 10%", fontsize=6.5, color="0.35", va="top")
ax.axvline(qmin / q0, color="0.6", lw=0.7, ls="-.")
ax.text(qmin / q0 + 0.03, 0.05, r"$q_{\min}$", fontsize=7.5, color="0.35")
ax.set_xlim(0.4, Q[-1] + 0.1)
ax.set_ylim(0, 1.36 * max((wgt * S0 / norm).max(), (wgt * Slf / norm).max()))
ax.set_xlabel(r"$q/q_0$")
ax.set_ylabel(r"$q\,\eta(v_{\min})\,S(q,\omega)$ (normalized)")
ax.legend(loc="upper right", frameon=True, framealpha=1, edgecolor="none")
fig.tight_layout()
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
os.makedirs(OUT, exist_ok=True)
fig.savefig(os.path.join(OUT, "limit10_1a.pdf"))
print("wrote limit10_1a.pdf")
