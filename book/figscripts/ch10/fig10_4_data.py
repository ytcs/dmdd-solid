"""Data for Fig. 10.4 of Sect. 10.5 (excitons at finite momentum): the loss function of silicon at a finite momentum
transfer q along [100], with and without the electron-hole attraction, in the transition-basis model of Fig. 4.11
(figscripts/ch04/fig4_11_data.py) carried to finite q.  Writes fig10_4_data.npz next to this file.

Hamiltonian (singlet; eq:4.9-bse with the kernels eq:4.9-kernels at finite q; Tamm-Dancoff resonant block)
    H = Delta + 2 K^x - K^d,   Delta_t = e_{c,k+q} - e_{v,k},   t = (k, v, c)
  IP       : kernels off,
  RPA + LF : 2 K^x only (K^x = exchange kernel WITHOUT its G = 0 term; q lies inside the first zone, G_q = 0),
  BSE      : 2 K^x - K^d.
  eps_mac(q, w) = 1 - v_C(q) (2/V) [g(w + i eta) + g(-w - i eta)],  g(z) = b^+ (z - H)^-1 b,  b_t = rho_cv(k, q)
    (eq:4.9-epsmac: retarded Tamm-Dancoff form, resonant poles at +E_lambda and their antiresonant mirror at -E_lambda);
  eps_res(q, w) = 1 - v_C(q) (2/V) g(w + i eta)   (resonant-only form: one time ordering, the form that Limit 10.5a
    tests; its imaginary part at w > 0 equals that of eps_mac, its real part does not);
  L = Im(-1/eps).
  Full (beyond Tamm-Dancoff) RPA + LF from the reciprocal-vector Dyson equation on the same transitions, with the
  antiresonant pairs (c at k, v at k + q) computed explicitly: R0_GG' = (2/V) sum [rho_cv^*(q+G) rho_cv(q+G')/(w - D + i eta)
  - rho_vc^*(q+G) rho_vc(q+G')/(w + D' + i eta)],  Rbar = R0 + R0 vbar Rbar (vbar = v_C(|q+G|), G != 0),
  eps_mac = 1 - v_C(q) Rbar_00.  Its resonant part alone must equal the transition-space resolvent of Delta + 2 K^x
  (asserted): this pins the prefactor, the 1/V and the sign of K^x at finite q.  The difference between the full and the
  retarded Tamm-Dancoff RPA + LF is the coupling-block error of the exchange kernel at this q (printed).

Model (the modelling choices behind Fig. 10.4, named in its caption)
  Bands and states: the local empirical pseudopotential of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), as in
     figscripts/ch03/epm.py, Figs. 4.7 and 4.11: fitted to measured optical transition energies, no scissor, no
     spin-orbit coupling; model indirect gap 0.82 eV (the model of Sect. 10.4).
  Transition basis: NV = 4 valence and NCB = 4 conduction bands, shifted grid NK^3 over the full zone (no symmetry),
     q = (2 JQ/NK, 0, 0) 2 pi/a, so that k + q is a grid point; default NK = 10, JQ = 2: q = 0.4 (2 pi/a) = 0.913 keV.
  Exchange kernel: the 58 nonzero vectors of the 59 shortest reciprocal vectors (|G|^2 <= 12 (2 pi/a)^2), as Fig. 4.11.
  Direct kernel: same 59 G with a diagonal model screened interaction W_G(p) = v_C(|p+G|)/eps_C(|p+G|), where eps_C is
     the model dielectric function of Cappellini, Del Sole, Reining and Bechstedt, Phys. Rev. B 47, 9892 (1993),
     eps_C(Q) = 1 + 1/[1/(eps_inf - 1) + alpha_C (Q/k_TF)^2 + Q^4/(4 m_e^2 omega_p^2)], alpha_C = 1.563,
     with the measured eps_inf = 11.7 (Sect. 4.4), k_TF = 4.12 keV (Worked example 4.8), omega_p = 16.6 eV (Sect. 4.3),
     the same function as in figscripts/ch10/fig10_2.py.  (Fig. 4.11 used the model's own RPA + LF screening; the
     analytic model removes the screening calculation, which dominated that run.)  At p + G = 0 the head is the cell
     average 4 pi <1/Q^2> over the grid cell around Q = 0, divided by eps_inf, as in Fig. 4.11.
  Spectra: Haydock (Lanczos) continued fraction, NLANCZOS steps, Lorentzian broadening ETA = 0.15 eV.
  Static values: conjugate gradients on H x = b.
Units: hartree atomic units, Gaussian (e = 1, v_C = 4 pi/Q^2) inside; energies printed in eV.
Modes: IPONLY=1 computes only the independent-particle and RPA (head) loss functions by direct sums (grid gate).
Run: python3 fig10_4_data.py   (NK = 10: about 45 min with 2 threads on a shared 4-core box; peak memory about 3 GB).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import sys
import time
import numpy as np
import scipy.fft as sfft

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, BOHR, B   # noqa: E402

HA = 2 * RY
NK = int(os.environ.get("NK", 10))
JQ = int(os.environ.get("JQ", 2))
NV, NCB = 4, int(os.environ.get("NCB", 4))
NB = NV + NCB
ETA = float(os.environ.get("ETA", 0.15)) / HA
NLANCZOS = int(os.environ.get("NLANCZOS", 400))
IPONLY = os.environ.get("IPONLY", "0") == "1"
NR = 12
W = np.linspace(0.0, 10.0, 1001) / HA
WORK = 2
EPS_INF, KTF_EV, WP_EV, ALPHA_C = 11.7, 4120.0, 16.6, 1.563
AM_E = 3728.9403                      # alpha m_e in eV = 1 bohr^-1 (momentum conversion)

t0 = time.time()
log = lambda s: print(f"[{time.time() - t0:7.0f} s] {s}", flush=True)
si = EPM("Si")
a = si.a / BOHR
Omega = a**3 / 4
tpa = 2 * np.pi / a
Gb = si.G
NPW = len(Gb)
Binv = np.linalg.inv(B)
MI = np.rint(Gb @ Binv).astype(int)
assert np.allclose(MI @ B, Gb)

mm = np.array([(i, j, k) for i in range(-8, 9) for j in range(-8, 9) for k in range(-8, 9)])
g2 = np.rint(((mm @ B) ** 2).sum(1)).astype(int)
o = np.lexsort((np.arange(len(mm)), g2))
mm, g2 = mm[o], g2[o]
NG = int((g2 <= 12).sum())
GS = mm[:NG]                                           # 59 vectors, GS[0] = 0
assert NG == 59 and np.all(GS[0] == 0)
neg = np.array([np.where((GS == -m).all(1))[0][0] for m in GS])
assert NR > 2 * np.abs(MI).max() + np.abs(GS).max() + 2 + 1, "real-space grid too small (fold of k + q included)"


def cart(m):
    return np.asarray(m) @ B                            # units 2 pi/a


NKT = NK**3
V = NKT * Omega
qred = np.array([0, JQ, JQ]) / NK                       # in units of the reciprocal primitive vectors
qc = qred @ B                                           # cartesian, units 2 pi/a: (2 JQ/NK, 0, 0)
assert np.allclose(qc, [2 * JQ / NK, 0, 0])
qabs = np.linalg.norm(qc) * tpa                          # bohr^-1
log(f"NK = {NK}, q = {qc} 2pi/a, |q| = {qabs * AM_E:.1f} eV = {qabs / BOHR:.4f} A^-1")


def states(kp):
    """Bands (hartree) and periodic parts u_nk on the NR^3 cell grid for the k points kp (units 2 pi/a)."""
    n = len(kp)
    EN = np.empty((n, NB))
    U = np.zeros((n, NB, NR, NR, NR), np.complex64)
    mi = MI % NR
    for c0 in range(0, n, 64):
        w_, v_ = np.linalg.eigh(si.hamiltonian(kp[c0:c0 + 64]))
        EN[c0:c0 + 64] = w_[:, :NB] * (RY / HA)
        for i in range(len(w_)):
            box = np.zeros((NB, NR, NR, NR), complex)
            box[:, mi[:, 0], mi[:, 1], mi[:, 2]] = v_[i][:, :NB].T
            U[c0 + i] = sfft.ifftn(box, axes=(1, 2, 3), workers=WORK) * NR**3
    return EN, U


def rho_pairs(uA, uB, mlist):
    """rho(G) = (1/Omega) int uA^* uB e^{iG.r}; uA (..., a, R), uB (..., b, R) -> (..., nG, a, b)."""
    prod = np.conj(uA)[..., :, None, :, :, :] * uB[..., None, :, :, :, :]
    F = sfft.fftn(prod, axes=(-3, -2, -1), workers=WORK) / NR**3
    i = (-mlist) % NR
    out = F[..., i[:, 0], i[:, 1], i[:, 2]]
    return np.moveaxis(out, -1, -3)


f = (np.arange(NK) + 0.5) / NK - 0.5
kred = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
kp = kred @ B
EK, UK = states(kp)                                      # bands and periodic parts at k
# k + q is a grid point up to a reciprocal vector G1: u_{k+q}(r) = e^{-i G1.r} u_{k_j}(r) (exact on the cell grid;
# the empirical pseudopotential uses a fixed plane-wave set, so the bands are not recomputed at k + q)
cq = kred + qred
jq = np.rint((cq + 0.5) * NK - 0.5).astype(int)
G1 = np.floor_divide(jq, NK)
jq = jq - G1 * NK
assert np.allclose((jq + 0.5) / NK - 0.5 + G1, cq, atol=1e-9)
jidx = (jq[:, 0] * NK + jq[:, 1]) * NK + jq[:, 2]
EQ = EK[jidx]
nn = np.array(np.meshgrid(np.arange(NR), np.arange(NR), np.arange(NR), indexing="ij"))
UQ = np.empty_like(UK)
for ik in range(NKT):
    ph = np.exp(-2j * np.pi * np.tensordot(G1[ik], nn, axes=(0, 0)) / NR).astype(np.complex64)
    UQ[ik] = UK[jidx[ik]] * ph[None]
log(f"states: {NKT} k points, {NB} bands; k + q folded with |G1| <= {np.abs(G1).max()}")
egap = (EK[:, NV].min() - EK[:, NV - 1].max()) * HA
log(f"model indirect gap on this grid {egap:.3f} eV")

NT = NKT * NV * NCB
DELTA = (EQ[:, None, NV:NB] - EK[:, :NV, None]).reshape(-1)          # (k, v, c): e_{c,k+q} - e_{v,k}
DELTAP = (EK[:, None, NV:NB] - EQ[:, :NV, None]).reshape(-1)         # antiresonant pairs: e_{c,k} - e_{v,k+q}
vq = 4 * np.pi / qabs**2
vG = 4 * np.pi / (((cart(GS) + qc) * tpa) ** 2).sum(1)                # v_C(|q + G|), index 0 = v_C(q)
RHO = np.empty((NT, NG), complex)                       # rho_cv(k, q + G), G in GS
RHOA = np.empty((NT, NG), complex)                      # rho_vc(k, q + G) = <v,k+q| e^{i(q+G)r} |c,k>
for ik in range(NKT):
    sl = slice(ik * NV * NCB, (ik + 1) * NV * NCB)
    r = rho_pairs(UQ[ik, NV:NB], UK[ik, :NV], GS)                     # (G, c, v)
    RHO[sl] = r.transpose(2, 1, 0).reshape(-1, NG)
    ra = rho_pairs(UQ[ik, :NV], UK[ik, NV:NB], GS)                    # (G, v, c)
    RHOA[sl] = ra.transpose(1, 2, 0).reshape(-1, NG)
log(f"vertices: N_t = {NT}; min transition {DELTA.min() * HA:.3f} eV; min antiresonant {DELTAP.min() * HA:.3f} eV")
bvec = RHO[:, 0].copy()
# inversion + time reversal: the antiresonant pairs carry the same head weights as the resonant ones (sums compared;
# single weights inside degenerate multiplets depend on the gauge)
s_r, s_a = (np.abs(RHO[:, 0])**2).sum(), (np.abs(RHOA[:, 0])**2).sum()
m_r, m_a = (np.abs(RHO[:, 0])**2 / DELTA).sum(), (np.abs(RHOA[:, 0])**2 / DELTAP).sum()
log(f"antiresonant vs resonant head weight: sum {s_a / s_r - 1:.1e}, inverse moment {m_a / m_r - 1:.1e}")
assert abs(s_a / s_r - 1) < 1e-3 and abs(m_a / m_r - 1) < 1e-3   # band cut can split a multiplet


def eps_direct(weights, D, Dp=None, wp=None):
    """IP eps_mac from Lorentzian sums: 1 - v(q) (2/V) [sum w/(z - D) - sum w'/(z + D')]."""
    if Dp is None:
        Dp, wp = D, weights
    z = W + 1j * ETA
    res = np.array([(weights / (x - D)).sum() for x in z])
    ant = np.array([(wp / (x + Dp)).sum() for x in z])
    return 1 - vq * 2 / V * (res - ant), 1 - vq * 2 / V * res


e_ip, e_ip_res = eps_direct(np.abs(bvec)**2, DELTA, DELTAP, np.abs(RHOA[:, 0])**2)
e_ip_s = 1 + 2 * vq * 2 / V * (np.abs(bvec)**2 / DELTA).sum()
L = lambda e: (-1 / e).imag
iw = lambda x: int(np.argmin(abs(W * HA - x)))
log(f"IP: eps(q,0) = {e_ip_s:.4f}; eps2 peak {e_ip.imag.max():.3f} at {W[np.argmax(e_ip.imag)] * HA:.2f} eV")
for x in (2.0, 3.0, 4.0, 5.0, 6.0, 8.0):
    log(f"  w = {x:.1f} eV: eps2_IP = {e_ip[iw(x)].imag:.4f}, L_RPA(head) = {L(e_ip[iw(x)]):.5f}")
if IPONLY:
    np.savez_compressed(os.path.join(HERE, f"fig10_4_ip_NK{NK}_JQ{JQ}_NCB{NCB}.npz"), w=W * HA, eps_ip=e_ip,
                        q=qabs * AM_E, NK=NK)
    log("IPONLY: saved")
    sys.exit(0)

# ------------------------------------------------------------------ kernels
X = RHO[:, 1:] * np.sqrt(vG[1:] / V)[None, :]           # K^x = X X^+  (G != 0)


def eps_C(Q):
    """Cappellini model dielectric function; Q in bohr^-1."""
    k_tf = KTF_EV / AM_E
    wp = WP_EV / HA
    return 1 + 1 / (1 / (EPS_INF - 1) + ALPHA_C * (Q / k_tf)**2 + Q**4 / (4 * wp**2))


# cell average of 1/Q^2 around Q = 0 (parallelepiped of B/NK), as in fig4_11_data.py
nsub = 40
s = (np.arange(nsub) + 0.5) / nsub - 0.5
sc = np.array(np.meshgrid(s, s, s, indexing="ij")).reshape(3, -1).T / NK
q2 = ((sc @ B * tpa) ** 2).sum(1)
vcell = abs(np.linalg.det(B * tpa)) / NK**3
i0 = np.argmin(q2)
Rsph = (3 * vcell / nsub**3 / (4 * np.pi)) ** (1 / 3)
inv_q2 = (np.sum(1 / np.delete(q2, i0)) + 3 / Rsph**2) / nsub**3

H = np.zeros((NT, NT), np.complex64)
Kd_diag = np.zeros(NT)
cGS = cart(GS)
for ik in range(NKT):
    p = kp - kp[ik]                                     # k' - k for all k'
    pg2 = (((p[:, None, :] + cGS[None]) * tpa) ** 2).sum(-1)
    with np.errstate(divide="ignore", invalid="ignore"):
        Wk = 4 * np.pi / pg2 / eps_C(np.sqrt(pg2))
    z = np.where(pg2 < 1e-12)
    Wk[z] = 4 * np.pi * inv_q2 / EPS_INF
    Wk /= V
    rc = rho_pairs(UQ[:, NV:NB], UQ[ik, None, NV:NB], GS)            # (k', G, c', c): conduction at k'+q, k+q
    rv = rho_pairs(UK[:, :NV], UK[ik, None, :NV], GS)                # (k', G, v', v)
    blk = np.einsum("kgac,kg,kgbv->vckba", rc.conj(), Wk, rv, optimize=True)
    H[ik * NV * NCB:(ik + 1) * NV * NCB] = -blk.reshape(NV * NCB, NT)
    Kd_diag[ik * NV * NCB:(ik + 1) * NV * NCB] = np.diagonal(blk[:, :, ik].reshape(NV * NCB, NV * NCB)).real
    if ik % 200 == 0:
        log(f"  K^d row block {ik}/{NKT}")
del UK, UQ
herm, hmax, BS = 0.0, 0.0, 2048
for r0 in range(0, NT, BS):
    for c0 in range(r0, NT, BS):
        A_ = H[r0:r0 + BS, c0:c0 + BS]
        B_ = H[c0:c0 + BS, r0:r0 + BS].conj().T
        herm = max(herm, float(np.abs(A_ - B_).max()))
        hmax = max(hmax, float(np.abs(A_).max()))
        avg = 0.5 * (A_ + B_)
        H[r0:r0 + BS, c0:c0 + BS] = avg
        H[c0:c0 + BS, r0:r0 + BS] = avg.conj().T
herm /= hmax
log(f"K^d built; Hermiticity defect {herm:.2e}; K^d diagonal min {Kd_diag.min() * HA * 1e3:.2f} meV, "
    f"mean {Kd_diag.mean() * HA * 1e3:.2f} meV")
assert herm < 1e-4
assert Kd_diag.min() > 0
for r0 in range(0, NT, 2048):
    H[r0:r0 + 2048] += (2 * X[r0:r0 + 2048] @ X.conj().T).astype(np.complex64)
H[np.arange(NT), np.arange(NT)] += DELTA.astype(np.float32)
Kx_diag = (np.abs(X)**2).sum(1)
log(f"H built ({H.nbytes / 1e9:.2f} GB); K^x diagonal mean {Kx_diag.mean() * HA * 1e3:.3f} meV")


def mv_ip(x):
    return DELTA * x


def mv_lf(x):
    return DELTA * x + 2 * (X @ (X.conj().T @ x))


def mv_bse(x):
    return (H @ x.astype(np.complex64)).astype(complex)


def mv_trip(x):                                         # triplet: exchange off, attraction on (H^T = Delta - K^d)
    return mv_bse(x) - 2 * (X @ (X.conj().T @ x))


def haydock(mv, b, n):
    nb = np.linalg.norm(b)
    q_prev = np.zeros_like(b)
    qv = b / nb
    al, be = [], [0.0]
    for _ in range(n):
        w = mv(qv) - be[-1] * q_prev
        a_ = np.vdot(qv, w).real
        w = w - a_ * qv
        b_ = np.linalg.norm(w)
        al.append(a_)
        be.append(b_)
        q_prev, qv = qv, w / b_
    return nb**2, np.array(al), np.array(be[1:])


def cfrac(z, nb2, al, be):
    a_inf, b_inf = al[-50:].mean(), be[-50:].mean()
    sq = np.sqrt((z - a_inf) ** 2 - 4 * b_inf**2 + 0j)
    t1, t2 = (z - a_inf - sq) / (2 * b_inf**2), (z - a_inf + sq) / (2 * b_inf**2)
    t = np.where(t1.imag * np.sign(z.imag) < 0, t1, t2)
    g = t
    for a_, b_ in zip(al[::-1], be[::-1]):
        g = 1 / (z - a_ - b_**2 * g)
    return nb2 * g


def cg(mv, b, tol=1e-6, nmax=3000):
    x = np.zeros_like(b)
    r = b.copy()
    pp = r.copy()
    rr = np.vdot(r, r).real
    for it in range(nmax):
        Ap = mv(pp)
        alpha = rr / np.vdot(pp, Ap).real
        x += alpha * pp
        r -= alpha * Ap
        rn = np.vdot(r, r).real
        if np.sqrt(rn) < tol * np.linalg.norm(b):
            return x, it
        pp = r + (rn / rr) * pp
        rr = rn
    raise RuntimeError("CG did not converge")


z = W + 1j * ETA
eps, epsres, stat = {}, {}, {}
for name, mv in (("ip", mv_ip), ("lf", mv_lf), ("bse", mv_bse)):
    nb2, al, be = haydock(mv, bvec, NLANCZOS)
    gp, gm = cfrac(z, nb2, al, be), cfrac(-z, nb2, al, be)
    eps[name] = 1 - vq * 2 / V * (gp + gm)
    epsres[name] = 1 - vq * 2 / V * gp
    x, nit = cg(mv, bvec)
    stat[name] = 1 + 2 * vq * 2 / V * np.vdot(bvec, x).real
    log(f"{name:4s}: eps(q,0) {stat[name]:.4f} (CG {nit} it); Haydock eps(0) {eps[name][0].real:.4f}")
# triplet (spin-density) spectrum: unscreened, -Im g(w) / pi per unit V/(2 g_deg); compared with the IP one
nb2, al, be = haydock(mv_trip, bvec, NLANCZOS)
spec_trip = -cfrac(z, nb2, al, be).imag / np.pi
nb2, al, be = haydock(mv_ip, bvec, NLANCZOS)
spec_ip = -cfrac(z, nb2, al, be).imag / np.pi
for lo, hi in ((0, 2.5), (0, 3.0), (2.5, 4.0), (4.0, 7.0)):
    mm_ = (W * HA >= lo) & (W * HA < hi)
    log(f"triplet / IP spectral weight in [{lo}, {hi}) eV: {spec_trip[mm_].sum() / spec_ip[mm_].sum():.3f}")
errip = np.abs(e_ip - eps["ip"]).max() / np.abs(e_ip.imag).max()
log(f"IP Haydock vs direct sum: max rel. difference {errip:.2e}")
assert errip < 1e-3

# ------------------------------------------------------------------ reciprocal-vector Dyson (RPA + LF) on the same pairs
DE = 0.005 / HA
nbin = int(max(DELTA.max(), DELTAP.max()) / DE) + 3


def binned(D, M):
    xb = D / DE
    i0_ = np.floor(xb).astype(int)
    wt = xb - i0_
    out = np.zeros((nbin, NG * NG), complex)
    for c0 in range(0, NT, 1024):
        sl = slice(c0, c0 + 1024)
        o_ = (M[sl, :, None].conj() * M[sl, None, :]).reshape(-1, NG * NG)   # rho^*(G) rho(G')
        np.add.at(out, i0_[sl], (1 - wt[sl])[:, None] * o_)
        np.add.at(out, i0_[sl] + 1, wt[sl][:, None] * o_)
    return out


Mres = binned(DELTA, RHO)
Mant = binned(DELTAP, RHOA)
Eb = np.arange(nbin) * DE
vbar = vG.copy()
vbar[0] = 0.0
Kh = np.diag(vbar)
eps_full = np.empty(len(W), complex)
res_dyson = np.empty(len(W), complex)
for i_, x in enumerate(z):
    R0r = (2 / V) * ((1 / (x - Eb)) @ Mres).reshape(NG, NG)
    R0 = R0r - (2 / V) * ((1 / (x + Eb)) @ Mant).reshape(NG, NG)
    Rr = np.linalg.solve(np.eye(NG) - R0r @ Kh, R0r)
    Rf = np.linalg.solve(np.eye(NG) - R0 @ Kh, R0)
    res_dyson[i_] = Rr[0, 0]
    eps_full[i_] = 1 - vq * Rf[0, 0]
nb2, al, be = haydock(mv_lf, bvec, NLANCZOS)
res_tr = (2 / V) * cfrac(z, nb2, al, be)
errdy = np.abs(res_dyson - res_tr).max() / np.abs(res_tr).max()
log(f"resonant Dyson vs transition-space resolvent: max rel. difference {errdy:.2e}")
assert errdy < 5e-3
m = (W * HA > 1.5) & (W * HA < 8)
cpl_e2 = np.abs(eps_full.imag - eps["lf"].imag)[m].max() / eps_full.imag[m].max()
cpl_L = np.abs(L(eps_full) - L(eps["lf"]))[m].max() / L(eps_full)[m].max()
log(f"coupling-block error of RPA + LF (retarded TDA vs full), 1.5-8 eV: eps2 {cpl_e2:.3%}, L {cpl_L:.3%} of peak")

for x in (1.3, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0):
    j = iw(x)
    log(f"  w = {x:.1f} eV: L_IP-RPA {L(eps['ip'][j]):.5f}  L_LF {L(eps['lf'][j]):.5f}  L_BSE {L(eps['bse'][j]):.5f}"
        f"  L_LF,full {L(eps_full[j]):.5f}  L_BSE,res {L(epsres['bse'][j]):.5f}  eps1_BSE {eps['bse'][j].real:.3f}"
        f"  eps1_BSE,res {epsres['bse'][j].real:.3f}")

np.savez_compressed(os.path.join(HERE, "fig10_4_data.npz"), w=W * HA, q=qabs * AM_E, qA=qabs / BOHR,
                    eps_ip=eps["ip"], eps_lf=eps["lf"], eps_bse=eps["bse"], eps_lf_full=eps_full,
                    epsres_ip=epsres["ip"], epsres_lf=epsres["lf"], epsres_bse=epsres["bse"],
                    st_ip=stat["ip"], st_lf=stat["lf"], st_bse=stat["bse"], NK=NK, NV=NV, NCB=NCB, NG=NG,
                    eta=ETA * HA, egap=egap, spec_trip=spec_trip, spec_ip=spec_ip, Emin=DELTA.min() * HA, Kd_mean=Kd_diag.mean() * HA,
                    Kx_mean=Kx_diag.mean() * HA, herm=herm, errip=errip, errdy=errdy, cpl_e2=cpl_e2, cpl_L=cpl_L)
log("saved fig10_4_data.npz")
