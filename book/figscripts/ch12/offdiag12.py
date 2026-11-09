"""Off-diagonal G != G' elements of the inverse dielectric matrix in the crystal Migdal rate of silicon (Sect. 12.3,
eq:12.1-Skk, eq:12.3-FL; DEFERRED-COMPUTE "Off-diagonal eps^-1_GG' in the crystal Migdal rate"; editor-notes R1').
A cheap model bracket, not the first-principles calculation (which stays deferred).

Question: by how much does the full matrix change the soft-limit Migdal rate relative to the diagonal-only form the book
uses (Limit 12.3a: diagonal of eps^-1 with local fields)?

Three forms of the Migdal-weighted loss function (soft limit, direction-averaged boost, eq:12.3-LMig / eq:12.3-FL):
  L_Mig^(x)(w) = (1/(N_k Omega)) sum_k sum_{G,G'} W^(x)_{GG'}(k) Sp_{GG'}(k, w),     p = k + G, p' = k + G',
  (i)   full:  W = Z(p) Z(p') (p^.p'^) e^{i(G-G').X} e^{-<u_x^2>|G-G'|^2/2},  Sp = spectral part of -eps~^-1,
              averaged over the two atoms X = +-tau of the cell (EPM origin at the bond centre, tau = (a/8)(1,1,1));
              Sp = -(E - E^+)/(2i), E = eps~^-1, eps~ = 1 - v^1/2 R0 v^1/2 (symmetrized, same inverse diagonal);
  (ii)  diagonal of eps^-1 (book form, lim:12.3a 'lf'):  G = G' only;
  (iii) scalar RPA without local fields (lim:12.3a 'rpa'):  Im[-1/eps_GG(k)] at p = k + G.
Derivation of W (App. D.33-amp, -square): the amplitude to pair f is sum_p (q.p) v(p) e^{-ip.X} <f|n(p)|0>/(M w^2),
  v(p) = -Z_ion(p) e^2/p^2; squaring gives sum_{GG'} a_G^* a_G' S^ee_GG', S^ee_GG' = (2|p||p'|/e^2) Sp_GG' (RPA,
  symmetrized), and the direction average of (q.p)(q.p') is q^2 p.p'/3. The structure phase e^{i(G-G').X} is the
  position of the struck nucleus relative to the origin of eps; eq:12.3-FL as printed has it only with the origin on
  the struck atom. The nuclear (lattice) factor between n_kappa(q-k-G) and n_kappa(q-k-G'), integrated over omega_l in
  the soft limit, is <0|e^{i(G-G').u}|0> = exp(-<u_x^2>|G-G'|^2/2) (harmonic, T = 0; <u_x^2> = 2.45e-3 A^2 from
  ch11/imp11.py): these are the q -> q + G umklapp channels of the nuclear kick. (i) is printed with and without it,
  and without the structure phase (the literal eq:12.3-FL at the bond-centre origin) to show that the phase matters.
Q_Mig = L_Mig/(3 w^4) (mig12.qmig convention), dP/dw = 4 alpha v_N^2 Q_Mig; rate: mig12.rate_free kernel (heavy
  mediator, free recoil, exact v_min, q_min = 0, w >= 1.11 eV), with the model Q_Mig in place of the table one.

Model (labelled; the same Bloch states as Figs. 4.7, 10.x): local empirical pseudopotential of Cohen and Bergstresser
  (figscripts/ch03/epm.py; a = 5.43 A, plane waves |G|^2 <= 21 (2pi/a)^2, no spin-orbit). Conduction bands scissored
  so that the model's indirect gap (0.82 eV on a fine line) becomes 1.11 eV (the gap of the KKL tables used by the book).
  RPA bubble: Adler-Wiser sum with resonant (v k -> c k+q) and antiresonant (c k, v k+q) pairs, T = 0, spin 2,
  Gamma-centred k mesh NK^3 over the full zone; q on the same mesh, reduced to the irreducible wedge with the 48
  operations of O_h (the weighted sums are invariant once both atoms are averaged; checked at one q by direct
  evaluation at a rotated q). q = Gamma is replaced by q0 = QG0 (2pi/a)(1, 0.37, 0.21)/|..| with states at k + q0.
  Pairs binned (width DB, linear weights) into spectral matrices; R0(w) by a Lorentzian of half-width ETA.
  Local-field set |G|^2 <= GM (2pi/a)^2.
Validation printed: (iii)/(ii) total and p-resolved against limit12_3a.log (1.350 total; 1.05, 1.24, 1.35 at p = 1, 2,
  3 q_BZ); model per-p weight and P_Mig(E_R = 100 eV) against the KKL table (mig12: 6.1e-3 with Z_ion(p)).
Run: NK=8 GM=19 python3 offdiag12.py > run.log   (env NK, GM, NC, ETA, ECUT, QG0, ROTCHECK, CHUNK, NTH, ZFIX). offdiag12.log
  collects the 11 runs of the convergence study (NK 4-10, |G|^2 <= 11-35, ECUT 21-40, ETA 0.15/0.3) with a summary table
  and the extrapolation used in ledgers/REVIEWS/ch12/editor-notes.md. Main run NK=8 GM=19: about 16 min on one core.
"""
import os
NTH = os.environ.get("NTH", "4")
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = NTH
import sys
import time
import numpy as np
from scipy import sparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
sys.path.insert(0, HERE)
from epm import EPM, RY, BOHR, B, HBARC   # noqa: E402
import mig12 as MG                          # noqa: E402
import imp11 as IMP                         # noqa: E402

HA = 2 * RY
NK = int(os.environ.get("NK", 8))
GM = float(os.environ.get("GM", 19))
NC = int(os.environ.get("NC", 36))
NV = 4
NB = NV + NC
ETA = float(os.environ.get("ETA", 0.15))      # eV
ECUT = float(os.environ.get("ECUT", 21))
QG0 = float(os.environ.get("QG0", 0.03))      # |q0| at Gamma, units 2pi/a
DB = 0.1                                      # bin width, eV (linear weights; ETA >= 0.1 eV)
EG_T = 1.11
ROTCHECK = int(os.environ.get("ROTCHECK", 0))
ZFIX = float(os.environ["ZFIX"]) if "ZFIX" in os.environ else None   # constant ion charge (point ion) instead of Z_ion(p)
WGRID = np.r_[np.arange(0.5, 30.0, 0.05), np.arange(30.0, 60.0 + 1e-9, 0.25)]     # eV

t0 = time.time()
si = EPM("Si", ecut=ECUT)
aA = si.a
a = aA / BOHR
Omega = a**3 / 4                              # bohr^3
tpa = 2 * np.pi / a
unit_eV = 2 * np.pi * HBARC / aA              # |2pi/a| in eV
Gb = si.G
NPW = len(Gb)
key = {tuple(np.rint(g).astype(int)): i for i, g in enumerate(Gb)}
TAU = np.array([1, 1, 1]) / 8.0               # units of a; G.tau = 2pi (G_units . (1,1,1)/8)
UX2 = IMP.UX2_DOS / HBARC**2                  # <u_x^2> in eV^-2

# local-field set
g2 = np.rint((Gb**2).sum(1)).astype(int)
LF = np.where(g2 <= GM + 1e-9)[0]
LF = LF[np.argsort(g2[LF], kind="stable")]
NG = len(LF)
GL = Gb[LF]

# gap of the model on a fine Gamma-X line (indirect, CBM near 0.85 X) and scissor
kl = np.outer(np.linspace(0, 1, 201), [1.0, 0, 0])
eb = si.bands(kl, nb=5)
gap_model = eb[:, 4].min() - eb[0, 3]
SCIS = EG_T - gap_model

# Gamma-centred mesh, crystal coordinates
f = np.arange(NK) / NK
kc = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
kpts = kc @ B
NKT = len(kpts)
Binv = np.linalg.inv(B)
# fold every mesh point to its shortest image (first zone), so that the fixed EPM basis is centred on it
_cand = np.array([(i, j, k) for i in range(-2, 3) for j in range(-2, 3) for k in range(-2, 3)]) @ B
kpts = kpts[:, None, :] + _cand[None, :, :]
kpts = kpts[np.arange(NKT), np.argmin((kpts**2).sum(-1), axis=1)]


def idx_of(crys):
    m = np.rint(np.mod(crys, 1.0) * NK).astype(int) % NK
    return (m[..., 0] * NK + m[..., 1]) * NK + m[..., 2]


# O_h: 48 signed permutation matrices
import itertools  # noqa: E402
OPS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        OPS.append(R)


def irreducible():
    seen = -np.ones(NKT, int)
    reps, wts = [], []
    for i in range(NKT):
        if seen[i] >= 0:
            continue
        orb = set()
        for R in OPS:
            qc = (R @ kpts[i]) @ Binv
            orb.add(int(idx_of(qc)))
        for j in orb:
            seen[j] = i
        reps.append(i)
        wts.append(len(orb))
    return np.array(reps), np.array(wts)


def states(ks):
    w, v = np.linalg.eigh(si.hamiltonian(ks))
    e = w[:, :NB] * RY
    e[:, NV:] += SCIS
    return e, v[:, :, :NB]


_smcache = {}


def shift_map(GU):
    """M[a, g] = basis index of g + G_a + GU (or NPW -> zero row)."""
    k_ = tuple(np.rint(GU).astype(int))
    if k_ not in _smcache:
        M = np.full((NG, NPW), NPW, int)
        for a_, i in enumerate(LF):
            s = Gb[i] + GU
            for j, g in enumerate(Gb):
                M[a_, j] = key.get(tuple(np.rint(g + s).astype(int)), NPW)
        _smcache[k_] = M
    return _smcache[k_]


print(f"[offdiag12] NK={NK} ({NKT} k), GM={GM:g} -> NG={NG}, NPW={NPW} (ECUT {ECUT:g}), bands {NV}+{NC}, "
      f"ETA={ETA} eV, model gap {gap_model:.3f} eV, scissor +{SCIS:.3f} eV, q0(Gamma)={QG0} 2pi/a", flush=True)

E1, C1 = states(kpts)                      # all k of the mesh (once)
emax = min((E1[:, -1].max() - E1[:, 0].min()) + 1.0, 75.0)   # pairs above 75 eV dropped (w^-4)
NBIN = int(emax / DB) + 3
EB = np.arange(NBIN) * DB


def chi0(qvec, onmesh):
    """Binned resonant / antiresonant spectral matrices (NBIN, NG*NG), a.u. scaling pref applied."""
    if onmesh:
        qc = qvec @ Binv
        Mres = np.zeros((NBIN, NG * NG), complex)
        Mant = np.zeros((NBIN, NG * NG), complex)
        kq = kpts + qvec
        j = idx_of(kq @ Binv)
        GU = kq - kpts[j]                    # k + q = k_j + GU
        E2, C2 = E1[j], C1[j]
    else:
        Mres = np.zeros((NBIN, NG * NG), complex)
        Mant = np.zeros((NBIN, NG * NG), complex)
        E2, C2 = states(kpts + qvec)
        GU = np.zeros_like(kpts)
    chunk = int(os.environ.get("CHUNK", 8))
    for c0 in range(0, NKT, chunk):
        rowsR, rowsA, binsR, binsA, wR, wA = [], [], [], [], [], []
        for i in range(c0, min(c0 + chunk, NKT)):
            SM = shift_map(GU[i])
            pad = np.vstack([C2[i], np.zeros((1, NB))])
            cs = pad[SM]                                           # (NG, g, band): c_{k+q}(g + G + GU)
            A = np.einsum("agc,gv->vca", cs[:, :, NV:].conj(), C1[i][:, :NV], optimize=True).reshape(-1, NG)
            Bm = np.einsum("agv,gc->cva", cs[:, :, :NV].conj(), C1[i][:, NV:], optimize=True).reshape(-1, NG)
            dEr = (E2[i][NV:][None, :] - E1[i][:NV][:, None]).reshape(-1)
            dEa = (E1[i][NV:][:, None] - E2[i][:NV][None, :]).reshape(-1)
            for X, dE, rows, bins, ws in ((A, dEr, rowsR, binsR, wR), (Bm, dEa, rowsA, binsA, wA)):
                keep = dE < emax - 2 * DB
                X, dE = X[keep], dE[keep]
                x = dE / DB
                i0 = np.floor(x).astype(int)
                t = x - i0
                rows.append((X.conj()[:, :, None] * X[:, None, :]).reshape(len(X), -1))
                bins.append(i0)
                ws.append(t)
        for rows, bins, ws, M in ((rowsR, binsR, wR, Mres), (rowsA, binsA, wA, Mant)):
            O = np.concatenate(rows)
            b = np.concatenate(bins)
            t = np.concatenate(ws)
            n = len(b)
            S = sparse.csr_matrix((np.r_[1 - t, t], (np.r_[b, b + 1], np.r_[np.arange(n), np.arange(n)])),
                                  shape=(NBIN, n))
            M += S @ O
    pref = 2.0 / (NKT * Omega)
    return Mres * pref, Mant * pref


def weights(qvec):
    """Weight matrices for the forms (i) and variants, on the LF set, for momentum transfer qvec (units 2pi/a)."""
    P = (qvec[None, :] + GL)                          # 2pi/a units
    pn = np.linalg.norm(P, axis=1)
    pe = pn * unit_eV
    Z = MG.z_ion(pe) if ZFIX is None else np.full_like(pe, ZFIX)
    ph = P / pn[:, None]
    cosang = ph @ ph.T
    dG = GL[:, None, :] - GL[None, :, :]
    phase = 2 * np.pi * (dG @ np.array([1, 1, 1]) / 8.0)
    dw = np.exp(-UX2 * ((dG * unit_eV)**2).sum(-1) / 2)
    base = Z[:, None] * Z[None, :] * cosang
    # e^{i(G-G').X} averaged over X = +-tau -> cos; e^{-i...} convention: the amplitude carries e^{-ip.X}, so the
    # quadratic form sum a_G^* a_G' Sp_GG' has e^{+i(G-G').X}; Sp Hermitian -> the average over +-tau is the real cos.
    Wp = base * np.exp(1j * phase) * dw               # atom at +tau
    Wm = base * np.exp(-1j * phase) * dw              # atom at -tau
    return dict(full_p=Wp, full_m=Wm, full_nodw=base * np.cos(phase), nophase=base * dw), Z, pe


def analyse(qvec, Mres, Mant):
    w = WGRID / HA
    eta = ETA / HA
    Eb = EB / HA
    out = {k: np.zeros(len(WGRID)) for k in ("i", "ip", "im", "i_nodw", "i_nophase", "ii", "iii")}
    P = qvec[None, :] + GL
    vC = 4 * np.pi / ((P**2).sum(1) * tpa**2)
    sv = np.sqrt(vC)
    Wd, Z, pe = weights(qvec)
    pdiag_ii = np.zeros((len(WGRID), NG))
    pdiag_iii = np.zeros((len(WGRID), NG))
    I = np.eye(NG)
    for s in range(0, len(w), 120):
        ws = w[s:s + 120]
        g_res = 1.0 / (ws[:, None] - Eb[None, :] + 1j * eta)
        g_ant = 1.0 / (ws[:, None] + Eb[None, :] + 1j * eta)
        R0 = (g_res @ Mres - g_ant @ Mant).reshape(len(ws), NG, NG)
        et = I[None] - sv[None, :, None] * R0 * sv[None, None, :]
        E = np.linalg.inv(et)
        Sp = -(E - np.conj(np.swapaxes(E, 1, 2))) / 2j                  # Hermitian spectral part of -eps~^-1
        Spr = Sp
        d_ii = np.real(np.einsum("wgg->wg", Spr))
        d_iii = np.imag(-1.0 / np.einsum("wgg->wg", et))
        pdiag_ii[s:s + len(ws)] = d_ii * Z[None]**2
        pdiag_iii[s:s + len(ws)] = d_iii * Z[None]**2
        out["ii"][s:s + len(ws)] = (d_ii * Z[None]**2).sum(1)
        out["iii"][s:s + len(ws)] = (d_iii * Z[None]**2).sum(1)
        # quadratic forms sum_GG' W_GG' Sp_G'G ... (W Hermitian, Sp Hermitian): Tr(W^T Sp) = sum W_GG' Sp_GG'
        ip_ = np.real(np.einsum("gh,wgh->w", Wd["full_p"], Spr))
        im_ = np.real(np.einsum("gh,wgh->w", Wd["full_m"], Spr))
        out["ip"][s:s + len(ws)] = ip_
        out["im"][s:s + len(ws)] = im_
        out["i"][s:s + len(ws)] = 0.5 * (ip_ + im_)
        out["i_nodw"][s:s + len(ws)] = np.real(np.einsum("gh,wgh->w", Wd["full_nodw"], Spr))
        out["i_nophase"][s:s + len(ws)] = np.real(np.einsum("gh,wgh->w", Wd["nophase"], Spr))
    return out, pdiag_ii, pdiag_iii, pe


def main():
    reps, wts = irreducible()
    assert wts.sum() == NKT
    print(f"irreducible q: {len(reps)} (weights sum {wts.sum()})", flush=True)
    acc = None
    # per-p diagonal weights for the profile: integral over w >= Eg of Z^2 L / w^4, binned in p
    pbins = np.arange(0, 6.01, 0.25) * MG.QBZ
    prof_ii = np.zeros(len(pbins) - 1)
    prof_iii = np.zeros(len(pbins) - 1)
    sel = WGRID >= EG_T
    w4 = WGRID[sel]**4
    negmin = np.inf
    sym_dev = 0.0
    for n, (iq, wq) in enumerate(zip(reps, wts)):
        qv = kpts[iq].copy()
        onmesh = True
        if np.allclose(qv, 0):
            d = np.array([1.0, 0.37, 0.21])
            qv = QG0 * d / np.linalg.norm(d)
            onmesh = False
        Mr, Ma = chi0(qv, onmesh)
        out, pii, piii, pe = analyse(qv, Mr, Ma)
        # positivity of the single-atom quadratic forms (direction-averaged boost is PSD): relative to the diagonal
        neg = min(np.min(out["ip"][sel] / np.maximum(out["ii"][sel], 1e-300)),
                  np.min(out["im"][sel] / np.maximum(out["ii"][sel], 1e-300)))
        negmin = min(negmin, neg)
        sym_dev = max(sym_dev, np.max(np.abs(out["ip"][sel] - out["im"][sel])) / np.max(np.abs(out["ii"][sel])))
        if acc is None:
            acc = {k: np.zeros(len(WGRID)) for k in out}
        for k in out:
            acc[k] += wq * out[k]
        Iii = np.trapezoid(pii[sel] / w4[:, None], WGRID[sel], axis=0)
        Iiii = np.trapezoid(piii[sel] / w4[:, None], WGRID[sel], axis=0)
        ib = np.digitize(pe, pbins) - 1
        ok = (ib >= 0) & (ib < len(prof_ii))
        np.add.at(prof_ii, ib[ok], wq * Iii[ok])
        np.add.at(prof_iii, ib[ok], wq * Iiii[ok])
        tot = {k: np.trapezoid(out[k][sel] / w4, WGRID[sel]) for k in ("i", "ii", "iii")}
        print(f"  q {n+1:3d}/{len(reps)} [{kpts[iq][0]:+.3f},{kpts[iq][1]:+.3f},{kpts[iq][2]:+.3f}] w={wq:2d}: "
              f"(i)/(ii)={tot['i']/tot['ii']:.4f} (iii)/(ii)={tot['iii']/tot['ii']:.4f}  t={time.time()-t0:.0f}s",
              flush=True)
    if ROTCHECK:
        # direct evaluation at a rotated copy of one non-trivial irreducible q
        iq = reps[np.argmax([np.count_nonzero(kpts[r]) for r in reps])]
        q1 = kpts[iq]
        R = OPS[13]
        q2 = R @ q1
        o1, *_ = analyse(q1, *chi0(q1, True))
        o2, *_ = analyse(q2, *chi0(q2, True))
        for k in ("i", "ii", "iii"):
            t1 = np.trapezoid(o1[k][sel] / w4, WGRID[sel])
            t2 = np.trapezoid(o2[k][sel] / w4, WGRID[sel])
            print(f"  rotation check q={q1} -> {q2}: form ({k}) {t1:.6e} vs {t2:.6e} (rel {abs(t1/t2-1):.1e})")
    # normalize: L_Mig = (1/(N_k Omega)) sum ..., Omega in eV^-3
    Om_eV = (aA**3 / 4) / HBARC**3
    Lmig = {k: acc[k] / (NKT * Om_eV) for k in acc}
    Q = {k: np.where(WGRID >= EG_T, Lmig[k] / (3 * WGRID**4), 0.0) for k in Lmig}
    print(f"positivity: min single-atom form/(ii) over q, w >= Eg: {negmin:+.3e}; |(+tau) - (-tau)|/max(ii): {sym_dev:.1e}")
    tot = {k: np.trapezoid(Q[k][sel], WGRID[sel]) for k in Q}
    r = lambda k: tot[k] / tot["ii"]
    print(f"TOTAL int Q dw (w >= {EG_T}): (i)/(ii) = {r('i'):.4f}; without Debye-Waller {r('i_nodw'):.4f}; "
          f"without structure phase (literal eq:12.3-FL at bond centre) {r('i_nophase'):.4f}; "
          f"(iii)/(ii) = {r('iii'):.4f}")
    # per-omega windows
    for lo, hi in [(1.11, 3), (3, 6), (6, 10), (10, 20), (20, 60)]:
        m = (WGRID >= lo) & (WGRID < hi)
        a_ = {k: np.trapezoid(Q[k][m], WGRID[m]) for k in ("i", "ii", "iii")}
        print(f"  w in [{lo:5.2f},{hi:5.1f}) eV: (i)/(ii) = {a_['i']/a_['ii']:.4f}, (iii)/(ii) = {a_['iii']/a_['ii']:.4f}, "
              f"fraction of (ii) {a_['ii']/tot['ii']:.3f}")
    # p profile
    print("p-resolved diagonal weights, (iii)/(ii) and cumulative fraction of (ii) [lim:12.3a: 0.973@0.5, 1.054@1, "
          "1.148@1.5, 1.238@2, 1.350@3, 1.967@4 q_BZ]")
    cum = np.cumsum(prof_ii) / prof_ii.sum()
    for j in range(len(prof_ii)):
        if prof_ii[j] > 0:
            print(f"  p/q_BZ in [{pbins[j]/MG.QBZ:.2f},{pbins[j+1]/MG.QBZ:.2f}): (iii)/(ii) = {prof_iii[j]/prof_ii[j]:.3f}, "
                  f"cum (ii) = {cum[j]:.3f}")
    # model vs KKL table, diagonal with LF (form ii), absolute: P_Mig at E_R = 100 eV
    ER = 100.0
    v2 = 2 * ER / MG.M
    P_model = 4 * MG.ALPHA * v2 * tot["ii"]
    P_tab = MG.p_total(ER)
    print(f"P_Mig(E_R = 100 eV), form (ii): model {P_model:.3e}, KKL table (mig12) {P_tab:.3e}, ratio {P_model/P_tab:.3f}; "
          f"form (i) model {4*MG.ALPHA*v2*tot['i']:.3e}")
    # model per-p weight vs the table (k^2 Z^2 int L/w^4 per unit p): model per-p density = prof/(N_k Om dp) * (2pi^2)...
    # compare shapes via fractions in p windows
    Qtab = MG.qmig("lf")
    for (plo, phi) in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 6)]:
        mt = MG.qmig("lf", kmin=plo * MG.QBZ, kmax=phi * MG.QBZ)
        ft = np.trapezoid(mt[MG.OM >= MG.EG], MG.OM[MG.OM >= MG.EG]) / np.trapezoid(Qtab[MG.OM >= MG.EG], MG.OM[MG.OM >= MG.EG])
        jm = (pbins[:-1] >= plo * MG.QBZ - 1) & (pbins[1:] <= phi * MG.QBZ + 1)
        fm = prof_ii[jm].sum() / prof_ii.sum()
        print(f"  fraction of (ii) weight at p/q_BZ in [{plo},{phi}): model {fm:.3f}, table {ft:.3f}")
    # rates vs m_chi (model Q in mig12.rate_free kernel, q_min = 0)
    print("rate (exact free-recoil kinematics, q_min = 0, w >= 1.11 eV): ratios to form (ii)")
    for m in [10e6, 30e6, 100e6, 300e6, 1e9]:
        rr = {}
        for k in ("i", "ii", "iii", "i_nodw", "i_nophase"):
            rr[k] = rate_total(m, Q[k])
        print(f"  m_chi = {m/1e6:6.0f} MeV: R(ii) = {rr['ii']:.3e} /kg/yr (sigma_n=1e-38); (i)/(ii) = {rr['i']/rr['ii']:.4f}; "
              f"no-DW {rr['i_nodw']/rr['ii']:.4f}; no-phase {rr['i_nophase']/rr['ii']:.4f}; (iii)/(ii) = {rr['iii']/rr['ii']:.4f}")
    np.savez_compressed(os.path.join(HERE, f"offdiag12_NK{NK}_GM{int(GM)}_ecut{int(ECUT)}_eta{ETA:g}" + (f"_Z{ZFIX:g}" if ZFIX else "") + ".npz"), w=WGRID,
                        **{f"Q_{k}": Q[k] for k in Q}, prof_ii=prof_ii, prof_iii=prof_iii, pbins=pbins)
    print(f"done in {time.time()-t0:.0f} s")


def rate_total(m, Qw):
    """Total rate (events/kg/yr, sigma_n = 1e-38 cm^2) with mig12.rate_free's kernel and the model Q_Mig(w)."""
    R = MG.R
    sig_n = 1e-38 * R.CM**2
    muN, mun = MG.mu(m, MG.M), MG.mu(m, MG.M_N)
    qmax = 2 * muN * R.VMAX
    q = np.linspace(1.0, qmax, 3000)
    D = np.pi * MG.A_SI**2 * sig_n / mun**2
    pref = R.RHO_CHI / (4 * np.pi**2 * m) * D * 2 * np.pi / MG.M
    sel = WGRID >= EG_T
    K = np.zeros(len(WGRID))
    for i in np.where(sel)[0]:
        w = WGRID[i]
        vmin = (w + q**2 / (2 * MG.M)) / q + q / (2 * m)
        K[i] = np.trapezoid(q * R.eta(vmin) * 4 * MG.ALPHA * q**2 / MG.M**2, q)
    return R.to_per_kg_yr(pref * np.trapezoid(K[sel] * Qw[sel], WGRID[sel]))


if __name__ == "__main__":
    main()
