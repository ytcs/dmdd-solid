"""Worked example of Sect. 8.8 (we:8-lf-nuisance): the local-field nuisance of the random-phase rate in silicon,
computed as the local-field difference S(RPA + LF) - S(RPA, head only) of the density structure factor.

Model (the same as we8_pairs.py of Sect. 8.7, whose header documents it; repeated here in brief)
  Bands and states: local empirical pseudopotential of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), via figscripts/ch03/epm.py
     (a = 5.43 A, 113 plane waves, no spin-orbit coupling; model indirect gap 0.82 eV).
  Momentum transfer: q along [100], unreduced; q0 = alpha m_e = 3.7289 keV (= 1/bohr), and 2 q0 for comparison.
  Bubble: Adler-Wiser sum eq:4.6-R0 at T = 0 with 4 valence and NC = 26 conduction bands, resonant and antiresonant terms,
     Lorentzian broadening (i0+ -> i ETA) with ETA = 0.10 eV.
  Approximations (Sect. 4.6): RPA, head only: S = -2 Im[R0_00/(1 - v_C(q) R0_00)] (eq:4.6-rpa);
     RPA + LF: R = R0 + R0 v_C R as matrices over the local-field set {G : |q+G|^2 <= GMAX2 (2 pi/a)^2} (eq:4.6-rpaLF), S = -2 Im R_00.
  The fractional size of the truncation (eq:8.8-delta) is delta_X(q, omega) = S(RPA+LF)/S(RPA) - 1.
  f-sum check: both approximations have local, frequency-independent kernels and so the same first moment (eq:4.3-firstmoment; App. D.7);
     the script prints int omega [S_LF - S_RPA] d omega / int omega S_RPA d omega over the grid (Lorentzian tails and the finite grid
     leave a residual; the band sum is the same for both approximations, so the check is internal to the model).
Numerical parameters: NK^3 shifted grid over the full zone (no symmetry); NK = 16 by default, NK = 20 as a check (env NK).
At q0 and 10 eV the 8.7 worked example (we8_pairs.py) gives S(RPA+LF) = 4.90e7 eV^2 at NK = 20 and 4.86e7 at NK = 24 (quoted 4.9e7);
this script gives 4.888e7 at NK = 20 (same model and local-field set).
The 8.7 'further 13 percent' compares |eps^-1_00|^2 S0 with S(RPA+LF) inside one approximation; delta_X here compares two approximations.
The text quotes energies from 2 eV up (model gap 0.82 eV) and the values on which NK = 16 and 20 agree to 0.01.
Convergence record (NK = 16 / 20; delta_X = S(RPA+LF)/S(RPA) - 1):
  q0:  2 eV -0.059/-0.059; 3 eV -0.056/-0.060; 4 eV +0.003/-0.000; 5 eV -0.038/-0.033; 7 eV -0.028/-0.026; 10 eV -0.064/-0.061;
       minimum -0.148 at 17.75 eV / -0.147 at 17.50 eV; zero crossing 25.62/25.62 eV; 30 eV +0.022/+0.018;
       first moments (LF - RPA)/RPA over 0.5-100 eV -0.0000/-0.0001; zeroth moments -0.0206/-0.0206; S_RPA-weighted mean on
       1.5-30 eV -0.058/-0.058.
  2q0: 2 eV -0.439/-0.438; 4 eV -0.301/-0.303; 10 eV -0.224/-0.223; 20 eV -0.066/-0.057; zero crossing 28.6/28.4 eV;
       first moments +0.0001/+0.0002; zeroth moments -0.0302/-0.0301; weighted mean -0.092/-0.092.
Run: NK=20 python3 we8_10.py   (about 15 min on 4 cores; writes we8_10_data_NK20.npz next to the script). No figure.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "4")
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, BOHR, B, HBARC   # noqa: E402

HA = 2 * RY
ME = 510998.95                           # eV (CODATA 2022)
ALPHA = 1 / 137.035999177                # CODATA 2022
NK = int(os.environ.get("NK", 16))
NC, NV = 26, 4
NB = NV + NC
GMAX2 = 12.0
ETA = 0.10                               # eV
OM = np.round(np.arange(0.5, 100.01, 0.25), 3)   # eV grid (the 26-band model has weight up to ~80 eV)
QFAC = [float(x) for x in os.environ.get("QFAC", "1,2").split(",")]

t0 = time.time()
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
cand = Gb[(Gb**2).sum(1) <= 12.5]

f = (np.arange(NK) + 0.5) / NK - 0.5
kc = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
kpts = kc @ B
NKT = len(kpts)
pref_au = 2.0 / (NKT * Omega)


def states(ks):
    w, v = np.linalg.eigh(si.hamiltonian(ks))
    return w[:, :NB] * RY, v[:, :, :NB]


def fold(kq):
    return cand[np.argmin(((kq[None, :] - cand) ** 2).sum(1))]


out = {}
for qf in QFAC:
    tt = time.time()
    qvec = np.array([qf * q0 / unit_eV, 0.0, 0.0])
    qG2 = ((qvec + Gb) ** 2).sum(1)
    # local-field set: the 51 vectors with the shortest |q + G| (at q0 this is the set |q+G|^2 <= 12 (2 pi/a)^2 of Sect. 8.7)
    LF = np.argsort(qG2, kind="stable")[:51]
    i0 = int(np.where(np.all(np.isclose(Gb[LF], 0), axis=1))[0][0])
    NG = len(LF)
    vC = 4 * np.pi / (qG2[LF] * tpa**2)
    maps = {}

    def shift_map(GU):
        k_ = tuple(np.rint(GU).astype(int))
        if k_ not in maps:
            M = -np.ones((NG, NPW), int)
            for a_, i in enumerate(LF):
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
            dr = 1.0 / (w_au[:, None] - dEr[None, :] + 1j * ETA / HA)      # (nw, npair)
            da = 1.0 / (w_au[:, None] + dEa[None, :] + 1j * ETA / HA)
            Ac = A.conj()
            Bc = Bm.conj()
            R0 += np.einsum("ap,wp,bp->wab", Ac, dr, A, optimize=True) - np.einsum("ap,wp,bp->wab", Bc, da, Bm, optimize=True)
    R0 *= pref_au
    S0 = -2 * R0[:, i0, i0].imag * AU_R_TO_EV2
    epsH = 1 - vC[i0] * R0[:, i0, i0]
    S_rpa = -2 * (R0[:, i0, i0] / epsH).imag * AU_R_TO_EV2
    S_lf = np.empty(len(OM))
    for iw in range(len(OM)):
        R = np.linalg.solve(np.eye(NG) - R0[iw] * vC[None, :], R0[iw])
        S_lf[iw] = -2 * R[i0, i0].imag * AU_R_TO_EV2
    dlt = S_lf / S_rpa - 1
    m1_rpa = np.trapezoid(OM * S_rpa, OM)
    m1_lf = np.trapezoid(OM * S_lf, OM)
    m1_0 = np.trapezoid(OM * S0, OM)
    m0_rpa = np.trapezoid(S_rpa, OM)
    m0_lf = np.trapezoid(S_lf, OM)
    out[qf] = dict(S0=S0, S_rpa=S_rpa, S_lf=S_lf, dlt=dlt)
    qkeV = qf * q0 / 1e3
    print(f"\n=== q = {qf:g} q0 = {qkeV:.2f} keV along [100]; NK = {NK}; NG = {NG}; {time.time()-tt:.0f} s ===")
    for w in (2, 3, 4, 5, 7, 10, 12, 15, 17, 20, 25, 30):
        j = int(np.argmin(abs(OM - w)))
        print(f"omega = {OM[j]:5.2f} eV: S0 = {S0[j]:.3e}, S_RPA = {S_rpa[j]:.3e}, S_RPA+LF = {S_lf[j]:.3e} eV^2, "
              f"delta = {dlt[j]:+.3f}")
    # sign changes and extremes
    sgn = np.where(np.diff(np.sign(dlt[OM > 1.5])) != 0)[0]
    om_s = OM[OM > 1.5]
    print("sign changes of delta at omega =", [round((om_s[k] + om_s[k + 1]) / 2, 2) for k in sgn])
    sel = (OM >= 1.5) & (OM <= 30)
    print(f"delta range on 1.5-30 eV: min {dlt[sel].min():+.3f} at {OM[sel][dlt[sel].argmin()]:.2f} eV, "
          f"max {dlt[sel].max():+.3f} at {OM[sel][dlt[sel].argmax()]:.2f} eV")
    print(f"first moments over 0.5-100 eV: IP {m1_0:.4e}, RPA {m1_rpa:.4e}, RPA+LF {m1_lf:.4e} eV^3; "
          f"(LF - RPA)/RPA = {(m1_lf - m1_rpa)/m1_rpa:+.4f}")
    print(f"zeroth moments: RPA {m0_rpa:.4e}, RPA+LF {m0_lf:.4e}; (LF - RPA)/RPA = {(m0_lf - m0_rpa)/m0_rpa:+.4f}")
    # spectrum-weighted mean of delta over windows (weights S_RPA)
    for lo, hi in ((1.5, 5), (5, 15), (15, 30), (1.5, 30)):
        s = (OM >= lo) & (OM <= hi)
        print(f"S_RPA-weighted mean delta on {lo}-{hi} eV: {np.sum(dlt[s]*S_rpa[s])/np.sum(S_rpa[s]):+.3f}")

np.savez(os.path.join(HERE, f"we8_10_data_NK{NK}.npz"), OM=OM, q0=q0,
         **{f"{k}_{qf:g}": v for qf, d in out.items() for k, v in d.items()})
print(f"\ntotal time {time.time()-t0:.0f} s")
