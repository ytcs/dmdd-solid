"""Seed distributions of Sect. 18.3: how a deposit omega in silicon is shared between the electron and the hole of the
prompt pair, for a dark-matter kick at q0 and for an absorbed photon, over a grid of excess energies omega - E_g.

Output: seeds18_3.json (histograms of the electron share x = E_e/(E_e + E_h), 40 bins on [0, 1], per excess energy) and
seeds18_3.log (every printed number). Used by casc18_3.py.

Model (the modelling choice behind the seeds of Fig. 18.3, Worked example 18.3 and Limit Check 18.3a)
  Bands and states: the local empirical pseudopotential of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), as in
     figscripts/ch03/epm.py (Sect. 3.3), the model of Worked example 8.7 (figscripts/ch08/we8_pairs.py). No spin-orbit
     coupling; spin enters as a common factor 2 and drops out of the normalized seeds.
  Dark-matter seed: the independent-particle pair-resolved response of the density at q = q0 = alpha m_e along [100]
     (eq:8.7-IP), weight |rho_cv(k, q0)|^2 delta(omega - e_{c,k+q} + e_{vk}), with the density vertex of eq:3.2-rhopw,
     q kept unreduced and k + q folded back as in we8_pairs.py. Screening is left out: at 10 eV, the screened
     (RPA + local fields, out-state) shares of we8_pairs.py differ from these by at most 0.03 in each statistic quoted in
     Sect. 8.7, and the check against the cached screened histogram is printed by casc18_3.py.
  Photon seed: the optical limit q -> 0, vertical pairs weighted by |v^x_cv|^2/(e_c - e_v)^2 (eq:3.2-optical).
  Delta functions: Gaussian of standard deviation SIG = 0.10 eV, as in Worked example 8.7.
  Carrier energies: E_e = e_{c,k+q} - E_CBM, E_h = E_VBM - e_{vk}; E_VBM at Gamma; E_CBM the minimum of the lowest
     conduction band on Gamma-X. The model gap is 0.82 eV against the 1.160 eV (123 K) of the cascade of
     casc18_3.py. The seeds are therefore tabulated against the EXCESS energy omega - E_g of the model, and casc18_3.py
     uses the share distribution of excess energy omega - E_g at the same excess energy above the measured gap. This is
     the one mapping between the model bands and the cascade, and it is stated in the captions.
Numerical parameters: NK^3 shifted Monkhorst-Pack grid over the full zone (no symmetry), 4 valence and NC = 20
  conduction bands (the highest band lies more than 26 eV above the valence maximum everywhere on the grid, against at
  most 21 eV needed), excess energies 0.25 ... 20 eV in steps of 0.25 eV.
Run: python3 seeds18_3.py (NK = 24, about 1.5 min, one core); NK=16 python3 seeds18_3.py is the convergence check.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import json
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, B, HBARC   # noqa: E402

ME = 510998.95                       # eV (CODATA 2022)
ALPHA = 1 / 137.035999177            # CODATA 2022
NK = int(os.environ.get("NK", 24))
NV, NC = 4, 20
NB = NV + NC
SIG = 0.10                           # eV
EXC = np.arange(0.25, 20.0 + 1e-9, 0.25)   # excess energies omega - E_g (eV)
NBIN = 40

t0 = time.time()
si = EPM("Si")
Gb = si.G
key = {tuple(np.rint(g).astype(int)): i for i, g in enumerate(Gb)}
unit_eV = 2 * np.pi * HBARC / si.a
q0 = ALPHA * ME
qvec = np.array([q0 / unit_eV, 0.0, 0.0])
cand = Gb[(Gb ** 2).sum(1) <= 12.5]

gx = np.linspace(0, 1, 401)[:, None] * np.array([1.0, 0, 0])
eb = si.bands(gx, nb=6)
E_VBM = eb[0, 3]
E_CBM = eb[:, 4].min()
Eg = E_CBM - E_VBM
OMEGAS = EXC + Eg
log = []


def say(s):
    print(s, flush=True)
    log.append(s)


say(f"q0 = {q0:.2f} eV = {qvec[0]:.4f} (2pi/a) along [100]; model E_g = {Eg:.4f} eV; NK = {NK}; SIG = {SIG} eV")

f = (np.arange(NK) + 0.5) / NK - 0.5
kpts = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T @ B
H = {s: np.zeros((len(EXC), NBIN)) for s in ("DM", "OPT")}
MOM = {s: np.zeros((len(EXC), 3)) for s in H}    # sum w, sum w E_e, sum w E_h
emax_top = []
_shift = {}


def shift_index(GU):
    k_ = tuple(np.rint(GU).astype(int))
    if k_ not in _shift:
        _shift[k_] = np.array([key.get(tuple(np.rint(g + GU).astype(int)), -1) for g in Gb])
    return _shift[k_]


def states(ks):
    w, v = np.linalg.eigh(si.hamiltonian(ks))
    return w[:, :NB] * RY, v[:, :, :NB]


def kern(x):
    return np.exp(-x ** 2 / (2 * SIG ** 2)) / (np.sqrt(2 * np.pi) * SIG)


def accumulate(s, dE, Ee, Eh, w0):
    """dE, Ee, Eh, w0: (v, c) arrays for one k; adds Gaussian-broadened weights to every omega and x bin."""
    L = kern(OMEGAS[:, None, None] - dE[None]) * w0[None]          # (n_omega, v, c)
    x = np.clip(Ee / np.maximum(Ee + Eh, 1e-12), 0, 1 - 1e-12)
    ib = (x * NBIN).astype(int).ravel()
    Lr = L.reshape(len(EXC), -1)
    for j in range(Lr.shape[1]):
        H[s][:, ib[j]] += Lr[:, j]
    MOM[s][:, 0] += Lr.sum(1)
    MOM[s][:, 1] += Lr @ Ee.ravel()
    MOM[s][:, 2] += Lr @ Eh.ravel()


chunk = 64
for c0 in range(0, len(kpts), chunk):
    ks = kpts[c0:c0 + chunk]
    GUs = np.array([cand[np.argmin(((k + qvec - cand) ** 2).sum(1))] for k in ks])
    e1, c1 = states(ks)
    e2, c2 = states(ks + qvec - GUs)
    emax_top.append(min(e1[:, -1].min(), e2[:, -1].min()) - E_VBM)
    for i in range(len(ks)):
        # density vertex at G = 0: rho_cv = sum_G'' c*_{c,k'}(G'' + G_U) c_{v,k}(G'')
        idx = shift_index(GUs[i])
        pad = np.vstack([c2[i], np.zeros((1, NB))])
        cs = pad[idx]
        rho = cs[:, NV:].conj().T @ c1[i][:, :NV]                  # (c, v)
        dE = e2[i][NV:][None, :] - e1[i][:NV][:, None]              # (v, c)
        Ee = e2[i][NV:][None, :] - E_CBM + 0 * dE
        Eh = E_VBM - e1[i][:NV][:, None] + 0 * dE
        accumulate("DM", dE, Ee, Eh, np.abs(rho.T) ** 2)
        kxG = (ks[i][0] + Gb[:, 0]) * unit_eV
        vx = c1[i][:, NV:].conj().T @ (kxG[:, None] * c1[i][:, :NV])   # (c, v), momentum matrix element
        dEv = e1[i][NV:][None, :] - e1[i][:NV][:, None]
        Eev = e1[i][NV:][None, :] - E_CBM + 0 * dEv
        Ehv = E_VBM - e1[i][:NV][:, None] + 0 * dEv
        accumulate("OPT", dEv, Eev, Ehv, np.abs(vx.T) ** 2 / dEv ** 2)

say(f"lowest top band on the grid: {min(emax_top):.1f} eV above the valence maximum")
out = dict(NK=NK, SIG=SIG, Eg_model=Eg, exc=EXC.tolist(), nbin=NBIN, hist={}, mean={})
for s in H:
    out["hist"][s] = (H[s] / np.maximum(H[s].sum(1, keepdims=True), 1e-300)).tolist()
    mE = MOM[s][:, 1] / MOM[s][:, 0]
    mH = MOM[s][:, 2] / MOM[s][:, 0]
    out["mean"][s] = dict(Ee=mE.tolist(), Eh=mH.tolist())
for e in (1.0, 2.0, 3.0, 3.75, 4.0, 5.0, 6.0, 8.0, 9.25, 10.0, 12.0, 15.0, 20.0):
    j = int(np.argmin(np.abs(EXC - e)))
    for s in H:
        h = np.array(out["hist"][s][j])
        say(f"excess {EXC[j]:5.2f} eV  {s:3s}: <E_e> = {out['mean'][s]['Ee'][j]:.2f} eV, <E_h> = {out['mean'][s]['Eh'][j]:.2f} eV, "
            f"P(x > 1/2) = {h[NBIN // 2:].sum():.3f}, P(x < 1/4 or x > 3/4) = {h[:NBIN // 4].sum() + h[3 * NBIN // 4:].sum():.3f}")
with open(os.path.join(HERE, f"seeds18_3{'' if NK == 24 else '_NK%d' % NK}.json"), "w") as fh:
    json.dump(out, fh)
say(f"total time {time.time() - t0:.0f} s")
with open(os.path.join(HERE, f"seeds18_3{'' if NK == 24 else '_NK%d' % NK}.log"), "w") as fh:
    fh.write("\n".join(log) + "\n")
