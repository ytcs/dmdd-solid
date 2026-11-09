"""Independent-particle (and, at a few points, RPA + local-field) response of silicon to the density and the transverse
current, for Sect. 10.4 (Table 10.1, Limit 10.4a, WE 10.4) and App. D.30.

Model: the local empirical pseudopotential of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), via figscripts/ch03/epm.py
(a = 5.43 A, plane waves |k + G|^2 <= 21 (2 pi/a)^2, no spin-orbit coupling; model indirect gap 0.82 eV), the same model as
the box of Sect. 10.1 (limit10_1a.py). The potential is local, so the current vertex needs no nonlocal correction and the
continuity equation holds pair by pair: q.<c,k+q|j_e(q)|v,k> = (e_c - e_v) <c,k+q|n_e(q)|v,k>  (eq:8.1-transverse). The
script asserts it.

Rows (Sect. 8.1, eq:8.1-rows, electrons; atomic units inside, m_e = 1):
  n(q + G):   vertex <c|e^{i(q+G).r}|v> = sum_g c*_{c,k+q}(g + G) c_{v,k}(g)
  j_T1, j_T2: vertex <c|(1/2){p, e^{iq.r}}|v>.e_Ti = sum_g c*_{c,k+q}(g) c_{v,k}(g) (k + g + q/2).e_Ti   (velocity, a.u.)
  j_L:        the same along q-hat (only for the continuity check)
with e_T1, e_T2 orthonormal and perpendicular to q-hat.
Response matrix (eq:4.2-Sab) at T = 0, omega > 0:  S_ab(q, w) = (2 pi / V) sum_f <0|O_a^+|f><f|O_b|0> delta(w - E_f),
spin summed (factor 2), V = N_k Omega. The delta function is a histogram bin of width DW (sum preserving). Units: S_nn in
eV^2 (natural units), S_nj in eV^2 times velocity (units of c), S_jj in eV^2 times velocity^2.
RPA + local fields (only with LFQ set): the Dyson equation on the density rows n(q + G) over the 51 vectors |G|^2 <= 11
(2 pi/a)^2 (as limit10_1a.py), with the currents as external rows and columns:
  R = R0 + R0_{a,G} [v_C (1 - R0_GG' v_C)^{-1}]_{GG'} R0_{G',b},  S_ab = i (R_ab - R_ba^*)  (App. D.30),
Lorentzian broadening ETA = 0.15 eV, resonant and antiresonant terms, averaged over w in [W - 0.5, W + 0.5] eV.
Checks printed: continuity residual; f-sum of S_nn (first moment against pi n_e q^2 / m_e, n_e = 8 / Omega); S_nj_T on the
[100] and [111] axes (zero by symmetry, App. D.30); IP S_jj from the bin route against the Lorentzian route at the LF points.
Run: NK=10 python3 si_jresp.py > si_jresp_NK10.log  (IP grid, 4 directions, 36 conduction bands);
     NK=10 NC=26 SKIPIP=1 LFQ='531:1.0:5;531:1.0:10;531:2.0:5;531:2.0:10;100:1.0:5' LFTAG=a python3 si_jresp.py > si_jresp_lf.log
(env NK, NC, DIRS, QLIST, LFQ; outputs si_jresp_NK{NK}_NC{NC}.npz, si_jresp_lf_NK{NK}_{LFTAG}.npy). Single-threaded BLAS.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, BOHR, B, HBARC   # noqa: E402

HA = 2 * RY
ME = 510998.95
ALPHA = 1 / 137.035999084
NK = int(os.environ.get("NK", 12))
NC, NV = int(os.environ.get("NC", 36)), 4        # 36 conduction bands: band 40 lies >= 45 eV above the valence top
NB = NV + NC
DW = 0.1                                       # eV, histogram bin
WEDGES = np.arange(0.0, 60.0 + DW / 2, DW)
WC = 0.5 * (WEDGES[1:] + WEDGES[:-1])
ETA = 0.15
QLIST = [float(x) for x in os.environ.get(
    "QLIST", "0.12,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.25,1.4,1.55,1.7,1.85,2.0,2.2,2.4,2.6,2.8,3.0,3.3,3.6").split(",")]
DIRS = os.environ.get("DIRS", "100;110;111;531").split(";")
LFQ = [x for x in os.environ.get("LFQ", "").split(";") if x]      # entries "dir:qf:W", e.g. "531:1.0:5"

si = EPM("Si")
a_A = si.a
a = a_A / BOHR
Omega = a**3 / 4
tpa = 2 * np.pi / a
Gb = si.G
NPW = len(Gb)
key = {tuple(np.rint(g).astype(int)): i for i, g in enumerate(Gb)}
unit_eV = 2 * np.pi * HBARC / a_A              # |2 pi / a| in eV
q0 = ALPHA * ME
AU_R_TO_EV2 = (HBARC / BOHR) ** 3 / HA         # 1/(Ha bohr^3) -> eV^2
VEL_AU = ALPHA                                 # 1 a.u. of velocity in units of c
_n = 8
_idx = np.array([(i, j, k) for i in range(-_n, _n + 1) for j in range(-_n, _n + 1) for k in range(-_n, _n + 1)])
cand = _idx @ B
cand = cand[(cand**2).sum(1) <= 80]
LF = np.where((Gb**2).sum(1) <= 11.01)[0]
I0 = int(np.where((Gb**2).sum(1) < 1e-9)[0][0])

f = (np.arange(NK) + 0.5) / NK - 0.5
kc = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
kpts = kc @ B
NKT = len(kpts)
pref_au = 2.0 / (NKT * Omega)                  # spin 2, 1/V


def qhat_of(d):
    v = np.array([float(c) for c in d]) if len(d) == 3 else None
    return v / np.linalg.norm(v)


def tbasis(qh):
    t = np.array([1.0, 0, 0]) if abs(qh[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = t - qh * (t @ qh)
    e1 /= np.linalg.norm(e1)
    return e1, np.cross(qh, e1)


def states(ks):
    w, v = np.linalg.eigh(si.hamiltonian(ks))
    return w[:, :NB] * RY, v[:, :, :NB]


def fold(kq):
    return cand[np.argmin(((kq[None, :] - cand) ** 2).sum(1))]


def make_shift(rows_G):
    maps = {}

    def shift_map(GU):
        k_ = tuple(np.rint(GU).astype(int))
        if k_ not in maps:
            M = -np.ones((len(rows_G), NPW), int)
            for a_, i in enumerate(rows_G):
                s = Gb[i] + GU
                for j, g in enumerate(Gb):
                    M[a_, j] = key.get(tuple(np.rint(g + s).astype(int)), -1)
            maps[k_] = M
        return maps[k_]
    return shift_map


def vertices(ks, i, c1, c2, GUs, SM, qvec, e1, e2, qh, i0):
    """Density vertices at q + G (rows of SM) and current vertices at q for one k; resonant (v -> c) and antiresonant."""
    pad = np.vstack([c2[i], np.zeros((1, NB))])
    cs = pad[SM]                                           # (nrow, g, band) coefficients of the k + q state at g + G + GU
    A = np.einsum("agc,gv->avc", cs[:, :, NV:].conj(), c1[i][:, :NV]).reshape(len(SM), -1)
    Bm = np.einsum("agv,gc->avc", cs[:, :, :NV].conj(), c1[i][:, NV:]).reshape(len(SM), -1)
    mom = (ks[i] + Gb + qvec / 2) * tpa                    # (k + g + q/2) in bohr^-1, initial plane wave k + g
    proj = np.stack([mom @ e1, mom @ e2, mom @ qh], 0)     # (3, g)
    c0 = cs[i0]                                            # (g, band): final-state coefficients at g + GU (G = 0 row)
    J = np.einsum("g,xg,gc,gv->xvc", np.ones(NPW), proj, c0[:, NV:].conj(), c1[i][:, :NV]).reshape(3, -1)
    Jb = np.einsum("g,xg,gv,gc->xcv", np.ones(NPW), proj, c0[:, :NV].conj(), c1[i][:, NV:]).reshape(3, -1)
    return A, Bm, J, Jb


def ip_spectra(d, qf, check=False):
    qh = qhat_of(d)
    e1, e2 = tbasis(qh)
    qvec = qf * q0 / unit_eV * qh
    shift_map = make_shift([I0])
    S = np.zeros((len(WC), 3, 3))                          # rows n, jT1, jT2 (real parts; imaginary parts recorded)
    Sim = np.zeros((len(WC), 3, 3))
    resid, scale = 0.0, 0.0
    chunk = 64
    for c0_ in range(0, NKT, chunk):
        ks = kpts[c0_:c0_ + chunk]
        GUs = np.array([fold(k + qvec) for k in ks])
        en1, c1 = states(ks)
        en2, c2 = states(ks + qvec - GUs)
        for i in range(len(ks)):
            A, Bm, J, Jb = vertices(ks, i, c1, c2, GUs, shift_map(GUs[i]), qvec, e1, e2, qh, 0)
            dE = (en2[i][NV:][None, :] - en1[i][:NV][:, None]).reshape(-1)          # eV
            # continuity: |q| j_L = dE rho (a.u.)
            ql = np.linalg.norm(qvec) * tpa
            resid += np.sum(np.abs(ql * J[2] - dE / HA * A[0]) ** 2)
            scale += np.sum(np.abs(dE / HA * A[0]) ** 2)
            X = np.vstack([A[0], J[0], J[1]])                                        # (3, pairs)
            ib = np.searchsorted(WEDGES, dE) - 1
            ok = (ib >= 0) & (ib < len(WC))
            M = X.conj()[:, None, :] * X[None, :, :]                                 # (3, 3, pairs)
            for a_ in range(3):
                for b_ in range(3):
                    S[:, a_, b_] += np.bincount(ib[ok], weights=M[a_, b_, ok].real, minlength=len(WC))
                    Sim[:, a_, b_] += np.bincount(ib[ok], weights=M[a_, b_, ok].imag, minlength=len(WC))
    conv = 2 * np.pi * pref_au * (HA / DW) * AU_R_TO_EV2   # delta -> 1/(bin width in Ha); S in eV^2 (density units)
    S *= conv
    Sim *= conv
    vel = np.array([1.0, VEL_AU, VEL_AU])
    S *= vel[None, :, None] * vel[None, None, :]
    Sim *= vel[None, :, None] * vel[None, None, :]
    return S, Sim, np.sqrt(resid / scale)


def lf_spectra(d, qf, W):
    """RPA + local fields with the transverse currents as external rows, averaged over [W - 0.5, W + 0.5] eV."""
    qh = qhat_of(d)
    e1, e2 = tbasis(qh)
    qvec = qf * q0 / unit_eV * qh
    qG2 = ((qvec + Gb) ** 2).sum(1)
    NG = len(LF)
    i0 = int(np.where(LF == I0)[0][0])
    vC = 4 * np.pi / (qG2[LF] * tpa**2)
    shift_map = make_shift(LF)
    OM = np.round(np.arange(W - 0.5, W + 0.501, 0.05), 3)
    w_au = OM / HA
    NR = NG + 2
    R0 = np.zeros((len(OM), NR, NR), complex)
    chunk = 32
    for c0_ in range(0, NKT, chunk):
        ks = kpts[c0_:c0_ + chunk]
        GUs = np.array([fold(k + qvec) for k in ks])
        en1, c1 = states(ks)
        en2, c2 = states(ks + qvec - GUs)
        for i in range(len(ks)):
            A, Bm, J, Jb = vertices(ks, i, c1, c2, GUs, shift_map(GUs[i]), qvec, e1, e2, qh, i0)
            X = np.vstack([A, J[0] * VEL_AU, J[1] * VEL_AU])
            Xb = np.vstack([Bm, Jb[0] * VEL_AU, Jb[1] * VEL_AU])
            dEr = ((en2[i][NV:][None, :] - en1[i][:NV][:, None]) / HA).reshape(-1)
            dEa = ((en1[i][NV:][None, :] - en2[i][:NV][:, None]) / HA).reshape(-1)
            dr = 1.0 / (w_au[:, None] - dEr[None, :] + 1j * ETA / HA)
            da = 1.0 / (w_au[:, None] + dEa[None, :] + 1j * ETA / HA)
            R0 += np.einsum("ap,wp,bp->wab", X.conj(), dr, X, optimize=True) \
                - np.einsum("ap,wp,bp->wab", Xb.conj(), da, Xb, optimize=True)
    R0 *= pref_au
    ext = [i0, NG, NG + 1]                     # rows n(q), jT1, jT2
    S_ip = np.zeros((3, 3))
    S_lf = np.zeros((3, 3))
    S_rpa = np.zeros((3, 3))
    for iw in range(len(OM)):
        R0w = R0[iw]
        RGG = R0w[:NG, :NG]
        K = np.diag(vC) @ np.linalg.inv(np.eye(NG) - RGG * vC[None, :])     # v_C (1 - R0 v_C)^{-1}
        R = R0w + R0w[:, :NG] @ K @ R0w[:NG, :]
        # head only (RPA without local fields): Dyson on the single row n(q)
        vh = vC[i0]
        Rh = R0w + np.outer(R0w[:, i0], R0w[i0, :]) * vh / (1 - vh * R0w[i0, i0])
        sub = np.ix_(ext, ext)
        for M, out in ((R0w, S_ip), (R, S_lf), (Rh, S_rpa)):
            Ms = M[sub]
            out += (1j * (Ms - Ms.conj().T)).real
    for out in (S_ip, S_lf, S_rpa):
        out *= AU_R_TO_EV2 / len(OM)
    return S_ip, S_rpa, S_lf


if __name__ == "__main__":
    out = {}
    if os.environ.get("SKIPIP") != "1":
        for d in DIRS:
            Ss, Sis, res = [], [], []
            for qf in QLIST:
                t = time.time()
                S, Sim, r = ip_spectra(d, qf)
                Ss.append(S)
                Sis.append(Sim)
                res.append(r)
                fsum = np.sum(WC * S[:, 0, 0]) * DW
                # pi n_e q^2 / m_e in eV^3: n_e [bohr^-3 -> eV^3], q [eV]
                fexp = np.pi * (8 / Omega) * (HBARC / BOHR) ** 3 * (qf * q0) ** 2 / ME
                iS = S.sum(0) * DW                                     # omega-integrated blocks
                corr = np.sqrt(iS[0, 1]**2 + iS[0, 2]**2) / np.sqrt(iS[0, 0] * (iS[1, 1] + iS[2, 2]))
                trj = np.sum(S[:, 1, 1] + S[:, 2, 2]) * DW
                snn = np.sum(S[:, 0, 0]) * DW
                print(f"[{d}] q = {qf:4.2f} q0: f-sum ratio {fsum/fexp:.3f}; continuity residual {r:.1e}; "
                      f"int S_nn = {snn:.3e} eV^3, int tr S_jTjT = {trj:.3e}; ratio {trj/snn:.3e}; "
                      f"|int S_njT|/sqrt(int S_nn int trS_jj) = {corr:.3f}; Im/Re max {np.abs(Sim).max()/np.abs(S).max():.1e}  "
                      f"({time.time()-t:.0f} s)", flush=True)
            out[f"S_{d}"] = np.array(Ss)
            out[f"Sim_{d}"] = np.array(Sis)
            out[f"res_{d}"] = np.array(res)
        out["Q"] = np.array(QLIST)
        out["WC"] = WC
        np.savez(os.path.join(HERE, f"si_jresp_NK{NK}_NC{NC}.npz"), **out)
    lfres = []
    for entry in LFQ:
        d, qf, W = entry.split(":")
        t = time.time()
        S_ip, S_rpa, S_lf = lf_spectra(d, float(qf), float(W))
        trip, trrpa, trlf = (S_ip[1, 1] + S_ip[2, 2]), (S_rpa[1, 1] + S_rpa[2, 2]), (S_lf[1, 1] + S_lf[2, 2])
        print(f"LF [{d}] q = {float(qf):.2f} q0, w = {W} eV: S_nn IP {S_ip[0,0]:.3e}, RPA {S_rpa[0,0]:.3e}, LF {S_lf[0,0]:.3e}; "
              f"tr S_jTjT IP {trip:.3e}, head {trrpa:.3e}, LF {trlf:.3e}; delta_LF^jT = {trlf/trip - 1:+.3f}; "
              f"|S_njT| IP {np.abs(S_ip[0,1:]).sum():.2e}, LF {np.abs(S_lf[0,1:]).sum():.2e}  ({time.time()-t:.0f} s)",
              flush=True)
        lfres.append([float(qf), float(W), S_ip[0, 0], S_rpa[0, 0], S_lf[0, 0], trip, trrpa, trlf])
    if lfres:
        np.save(os.path.join(HERE, f"si_jresp_lf_NK{NK}_{os.environ.get('LFTAG','')}.npy"), np.array(lfres))
