"""Data for Fig. 4.11 of Sect. 4.9 (excitons and the Bethe-Salpeter equation): the macroscopic dielectric function of
silicon at q -> 0 in the transition basis, in three approximations computed from one Hamiltonian,
    H = Delta + 2 K^x - K^d          (singlet, Tamm-Dancoff; eq. D.12-eig with the kernels of eq. D.12-crystal),
  IP       : kernels off                      (identical to eq:4.6-eps2 on the same grid),
  RPA + LF : 2 K^x only (K^x = exchange kernel WITHOUT its G = 0 term),
  BSE      : 2 K^x - K^d,
plus the full (non-Tamm-Dancoff) RPA + LF from the reciprocal-vector Dyson equation on the same states as a check.
Writes fig4_11_data.npz next to this file.

Model (the modelling choice behind Fig. 4.11, named in its caption)
  Bands and states: the local empirical pseudopotential of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), as in
     figscripts/ch03/epm.py and Fig. 4.7 (fig4_7_data.py): fitted to measured transition energies, so the band
     energies play the role of quasiparticle energies, and no scissor is applied.  v_mn = p_mn/m_e (local potential).
  Transition basis: 4 valence and NCB = 3 conduction bands (the IP spectrum below 6 eV changes by < 0.6 % of its peak
     from 3 to 26 conduction bands on the same grid), shifted Monkhorst-Pack grid NK^3 = 12^3 over the full zone
     (no symmetry): N_t = 12^3 x 4 x 3 = 20,736 transitions.
  Exchange kernel: K^x_{t t'} = (1/V) sum_{G != 0} v_C(|G|) rho_cv(k, G) rho_c'v'(k', G)^*, G over the 59 shortest
     reciprocal vectors (|G|^2 <= 12 (2 pi/a)^2), q -> 0.
  Direct kernel: K^d_{t t'} = (1/V) sum_G rho_c'c(k, p + G)^* W_G(p) rho_v'v(k, p + G), p = k' - k, same 59 G,
     with a diagonal screened interaction W_G(p) = (eps^-1)_GG(p) v_C(|p + G|), as in S. Albrecht et al., Phys. Rev.
     Lett. 80, 4510 (1998), who found the off-diagonal elements of eps^-1 invisible in the spectrum of silicon.
  Screening: the model's own static RPA dielectric matrix with local fields, eps_GG' = delta - v_C R^0_GG'(p, 0),
     R^0 from eq:4.6-R0 with 4 valence and 26 conduction bands (the band set of Fig. 4.7), with states on the Gamma-centred 12^3 grid (symmetric under the cubic group), on the 12^3 grid of
     differences p (Gamma-centred), inverted on the 59-vector set; its diagonal is kept.  For vectors outside that set
     (|G|^2 up to 40 (2 pi/a)^2, reached by p + G) the diagonal value 1/(1 - v_C R^0_GG) is used.  The matrix is
     computed on the irreducible wedge of the difference grid and mapped to the full grid with the 48 operations of
     the cubic group (diagonal elements carry no fractional-translation phase); the map is checked against a direct
     calculation at two p (agreement to < 1e-3: the band cut can split a degenerate multiplet).  At p = 0 the head is the cell average 4 pi <1/q^2> over the grid cell around
     q = 0 divided by the model's eps_inf (RPA + LF, same states), and the body comes from the q -> 0 block inversion
     with the optical head and wings (velocity matrix elements, as in fig4_7_data.py).
  Spectra: Haydock (Lanczos) continued fraction, NLANCZOS steps, Lorentzian broadening ETA = 0.15 eV (the 12^3 grid
     resolves the converged IP spectrum of Fig. 4.7 to about 3 % of its peak at this broadening, against 4 % at
     0.10 eV); antiresonant part with poles at -E_lambda.  Static eps_inf: one linear solve H x = b (conjugate
     gradients), eps_inf = 1 + 16 pi/V b^+ H^-1 b with b_t = v^x_cv/Delta_cvk (scaled optical vertex).
Units: hartree atomic units, Gaussian (e = 1, v_C = 4 pi/q^2) inside; energies printed in eV.
Checks (asserted): Hermiticity of H; K^d diagonal real and positive; IP eps_2 from Haydock = direct Lorentzian sum;
  symmetry map vs direct screening at two p; exact equality (non-Tamm-Dancoff, NK = 4) of the transition-space RPA + LF
  with the reciprocal-vector Dyson equation; aliasing bound of the real-space grid.
Run: python3 fig4_11_data.py   (about 2.2 h with 2 threads on a loaded 4-core box, peak memory about 6 GB).
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
NK = int(os.environ.get("NK", 12))
NV, NCB, NCS = 4, 3, 26          # valence, conduction bands in the BSE basis, conduction bands in the screening
NB = NV + NCS
ETA = 0.15 / HA
NLANCZOS = int(os.environ.get("NLANCZOS", 400))
NR = 12                          # real-space grid per primitive direction (aliasing bound asserted below)
W = np.linspace(0.0, 10.0, 1001) / HA
WORK = 2

t0 = time.time()
si = EPM("Si")
a = si.a / BOHR
Omega = a**3 / 4
tpa = 2 * np.pi / a
Gb = si.G
NPW = len(Gb)
Binv = np.linalg.inv(B)
MI = np.rint(Gb @ Binv).astype(int)                  # integer coordinates of the basis
assert np.allclose(MI @ B, Gb)
log = lambda s: print(f"[{time.time() - t0:7.0f} s] {s}", flush=True)

# reciprocal-vector sets: integer coordinates, sorted by |G|^2 (stable)
mm = np.array([(i, j, k) for i in range(-8, 9) for j in range(-8, 9) for k in range(-8, 9)])
g2 = np.rint(((mm @ B) ** 2).sum(1)).astype(int)
o = np.lexsort((np.arange(len(mm)), g2))
mm, g2 = mm[o], g2[o]
BIG = mm[g2 <= 40]                                   # 283 vectors
NBIG = len(BIG)
NG = int((g2 <= 12).sum())                           # 59: the leading part of BIG
assert NG == 59 and np.all(BIG[0] == 0)
bigkey = {tuple(m): i for i, m in enumerate(BIG)}
LUT = -np.ones((17, 17, 17), int)                    # integer coords in [-8, 8]^3 -> index in BIG (or -1)
LUT[BIG[:, 0] + 8, BIG[:, 1] + 8, BIG[:, 2] + 8] = np.arange(len(BIG))
# aliasing: products of two states have integer coordinates up to 2 max|MI|; we extract up to max|BIG| + 1 (fold)
assert NR > 2 * np.abs(MI).max() + np.abs(BIG).max() + 1, "real-space grid too small"


def cart(m):
    return np.asarray(m) @ B                          # units 2 pi/a


# ------------------------------------------------------------------ states
# The screening is computed on the Gamma-centred grid, which is invariant under the cubic group (so that the
# symmetry map is exact); the Bethe-Salpeter basis uses the shifted grid of Fig. 4.7.  Both have NK^3 points.
NKT = NK**3
V = NKT * Omega
SHIFT = None


def make_states(shift):
    """Bands, plane-wave coefficients and real-space periodic parts u_nk(r) (complex64, NR^3 grid of the cell,
    u = sum_G c(G) e^{iG.r}) on the grid (j + shift)/NK - 1/2 along the reciprocal primitive vectors."""
    global kp, EN, CV, U, SHIFT
    SHIFT = shift
    f = (np.arange(NK) + shift) / NK - 0.5
    kc = np.array(np.meshgrid(f, f, f, indexing="ij")).reshape(3, -1).T
    kp = kc @ B
    EN = np.empty((NKT, NB))
    CV = np.empty((NKT, NPW, NB), complex)
    for c0 in range(0, NKT, 64):
        w_, v_ = np.linalg.eigh(si.hamiltonian(kp[c0:c0 + 64]))
        EN[c0:c0 + 64] = w_[:, :NB] * (RY / HA)
        CV[c0:c0 + 64] = v_[:, :, :NB]
    U = np.zeros((NKT, NB, NR, NR, NR), np.complex64)
    mi = MI % NR
    for ik in range(NKT):
        box = np.zeros((NB, NR, NR, NR), complex)
        box[:, mi[:, 0], mi[:, 1], mi[:, 2]] = CV[ik].T
        U[ik] = sfft.ifftn(box, axes=(1, 2, 3), workers=WORK) * NR**3
    log(f"states: NK = {NK}^3, shift {shift}, NPW = {NPW}, bands {NV}+{NCS}, U {U.nbytes / 1e9:.2f} GB")


make_states(0.0)


def kindex(kcart):
    """Index on the shifted grid and folding vector (integer coords) of a point equal to a grid point mod G."""
    c = kcart @ Binv
    j = np.rint((c + 0.5) * NK - SHIFT).astype(int)
    fold = np.floor_divide(j, NK)
    jj = j - fold * NK
    assert np.allclose((jj + SHIFT) / NK - 0.5 + fold, c, atol=1e-9)
    return (jj[..., 0] * NK + jj[..., 1]) * NK + jj[..., 2], fold


def extract(F, mlist):
    """Fourier coefficients F~(-m) of real-space products F (..., NR, NR, NR) already transformed by fftn/NR^3."""
    i = (-mlist) % NR
    return F[..., i[:, 0], i[:, 1], i[:, 2]]


def rho_pairs(uA, uB, mlist):
    """rho(G) = (1/Omega) int uA^* uB e^{iG.r} for the integer vectors mlist; uA (..., a, R), uB (..., b, R)
    -> (..., len(mlist), a, b)."""
    prod = np.conj(uA)[..., :, None, :, :, :] * uB[..., None, :, :, :, :]
    F = sfft.fftn(prod, axes=(-3, -2, -1), workers=WORK) / NR**3
    out = extract(F, mlist)                           # (..., a, b, nG)
    return np.moveaxis(out, -1, -3)


# ------------------------------------------------------------------ static screening on the difference grid
gam = np.array(np.meshgrid(np.arange(NK), np.arange(NK), np.arange(NK), indexing="ij")).reshape(3, -1).T / NK
gam = np.where(gam >= 0.5, gam - 1, gam)
P = gam @ B
for j in range(len(P)):                               # Wigner-Seitz (minimum-norm) representatives
    cand = P[j] + np.array([(i, k, l) for i in (-1, 0, 1) for k in (-1, 0, 1) for l in (-1, 0, 1)]) @ B
    P[j] = cand[np.argmin((cand**2).sum(1))]
NP = len(P)
Pint = np.rint(P @ Binv * NK).astype(int)             # integer coords in units of 1/NK


def pindex(pcart):
    c = np.rint(pcart @ Binv * NK).astype(int)
    jj = c % NK
    return (jj[..., 0] * NK + jj[..., 1]) * NK + jj[..., 2]


pidx_of = pindex(P)
order_p = np.empty(NP, int)
order_p[pidx_of] = np.arange(NP)                      # index in P of the canonical index
ops = []
import itertools
for perm in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        S = np.zeros((3, 3))
        for r, cidx in enumerate(perm):
            S[r, cidx] = s[r]
        ops.append(S)
ops = np.array(ops)
rep = -np.ones(NP, int)
opi = np.zeros(NP, int)
reps = []
for j in range(NP):
    if rep[j] >= 0:
        continue
    reps.append(j)
    for io, S in enumerate(ops):
        jj = order_p[pindex(S @ P[j])]
        if rep[jj] < 0:
            rep[jj], opi[jj] = j, io
log(f"difference grid: {NP} points, {len(reps)} irreducible")


def screening_at(p, k_list=None):
    """Static RPA screening at p != 0: returns diag of eps^-1 on BIG (full inverse on the 59 set, diagonal beyond)."""
    R0 = np.zeros((NG, NG), complex)
    R0d = np.zeros(NBIG)
    jk, fold = kindex(kp + p)
    for ik in range(NKT):
        j2, G1 = jk[ik], fold[ik]
        ms = BIG + G1                                   # u_{k+p} = e^{-i G1.r} u_{k_j2}: extract at G + G1
        # pair (v at k, c at k+p): rho_cv(k, p+G) = <c,k+p| e^{i(p+G)r} |v,k>
        rcv = rho_pairs(U[j2, NV:], U[ik, :NV], ms)     # (NBIG, NCS, NV)
        dcv = EN[j2, NV:, None] - EN[ik, None, :NV]
        # pair (c at k, v at k+p): rho_vc(k, p+G) = <v,k+p| e^{i(p+G)r} |c,k>
        rvc = rho_pairs(U[j2, :NV], U[ik, NV:], ms)     # (NBIG, NV, NCS)
        dvc = EN[ik, None, NV:] - EN[j2, :NV, None]
        A = (rcv / np.sqrt(dcv)).reshape(NBIG, -1)
        Bm = (rvc / np.sqrt(dvc)).reshape(NBIG, -1)
        R0 -= A[:NG].conj() @ A[:NG].T + Bm[:NG].conj() @ Bm[:NG].T
        R0d -= (np.abs(A)**2).sum(1) + (np.abs(Bm)**2).sum(1)
    R0 *= 2 / V
    R0d *= 2 / V
    vq = 4 * np.pi / ((cart(BIG) * tpa + p * tpa) ** 2).sum(1)
    eps = np.eye(NG) - vq[:NG, None] * R0
    ed = 1 / (1 - vq * R0d)
    ed[:NG] = np.diag(np.linalg.inv(eps)).real
    return ed


def screening_q0():
    """p = 0: optical head and wings (x direction), body; returns diag of eps^-1 on BIG (index 0 = 1/eps_mac) and
    eps_mac of the model (RPA + LF, same states)."""
    r00 = 0.0
    rw = np.zeros(NG - 1, complex)                     # R0_{G0}/q  (scaled wing), G != 0
    R0b = np.zeros((NG - 1, NG - 1), complex)
    R0d = np.zeros(NBIG)
    for ik in range(NKT):
        c = CV[ik]
        e = EN[ik]
        kx = (kp[ik][0] + Gb[:, 0]) * tpa
        vx = np.einsum("gm,g,gn->mn", c.conj(), kx, c)
        dE = e[NV:, None] - e[None, :NV]                # (NCS, NV)
        rcv = rho_pairs(U[ik, NV:], U[ik, :NV], BIG)    # <c|e^{iGr}|v>, (NBIG, NCS, NV)
        rvc = rho_pairs(U[ik, :NV], U[ik, NV:], BIG)    # <v|e^{iGr}|c>, (NBIG, NV, NCS)
        hcv = vx[NV:, :NV] / dE                          # rho_cv(q)/q
        hvc = vx[:NV, NV:] / (-dE.T)                     # rho_vc(q)/q
        A = np.concatenate([hcv.reshape(1, -1), rcv[1:].reshape(NBIG - 1, -1)]) / np.sqrt(dE).reshape(1, -1)
        Bm = np.concatenate([hvc.reshape(1, -1), rvc[1:].reshape(NBIG - 1, -1)]) / np.sqrt(dE.T).reshape(1, -1)
        M = -(A[:NG].conj() @ A[:NG].T + Bm[:NG].conj() @ Bm[:NG].T)
        r00 += M[0, 0].real
        rw += M[1:, 0]
        R0b += M[1:, 1:]
        R0d[1:] -= (np.abs(A[1:]) ** 2).sum(1) + (np.abs(Bm[1:]) ** 2).sum(1)
    r00 *= 2 / V
    rw *= 2 / V
    R0b *= 2 / V
    R0d *= 2 / V
    vG = 4 * np.pi / ((cart(BIG[1:]) * tpa) ** 2).sum(1)
    # full scaled matrix (head scaled by q^2, wings by q): eps_mac = 1 - 4 pi Rbar_00 with Rbar = R0 + R0 vbar Rbar
    R0s = np.zeros((NG, NG), complex)
    R0s[0, 0] = r00
    R0s[1:, 0] = rw
    R0s[0, 1:] = rw.conj()
    R0s[1:, 1:] = R0b
    vb = np.zeros(NG)
    vb[1:] = vG[:NG - 1]
    Rb = np.linalg.solve(np.eye(NG) - R0s @ np.diag(vb), R0s)
    epsmac = 1 - 4 * np.pi * Rb[0, 0].real
    # body of eps^-1 at q -> 0: [eps_body - eps_b0 eps_0b / eps_00]^-1 (scaled factors are finite)
    e00 = 1 - 4 * np.pi * r00
    eb0 = -vG[:NG - 1] * rw                             # eps_{G0}/q
    e0b = -4 * np.pi * rw.conj()                         # q eps_{0G}
    eb = np.eye(NG - 1) - vG[:NG - 1, None] * R0b
    inv = np.linalg.inv(eb - np.outer(eb0, e0b) / e00)
    ed = 1 / (1 - np.concatenate([[0.0], vG]) * R0d)
    ed[1:NG] = np.diag(inv).real
    ed[0] = 1 / epsmac
    return ed, epsmac, 1 - 4 * np.pi * r00


EINV = np.zeros((NP, NBIG))
ed0, epsmac_model, epsip_model = screening_q0()
EINV[0] = ed0
assert np.allclose(P[0], 0)
log(f"q -> 0 screening: eps_inf IP {epsip_model:.4f}, RPA+LF {epsmac_model:.4f} (Fig. 4.7, 20^3: 11.45, 10.22)")


def little_group_average(j, ed):
    """Average the diagonal over the operations that leave P_j invariant mod G (restores the symmetry that the band
    cut at 4 + 26 breaks at the 1e-4 level; at p = 0 it is the cubic average over the field direction)."""
    acc = np.zeros(NBIG)
    cnt = np.zeros(NBIG)
    for S in ops:
        G0 = (P[j] - S @ P[j]) @ Binv
        if not np.allclose(G0, np.rint(G0), atol=1e-8):
            continue
        G0 = np.rint(G0).astype(int)
        hp = np.rint((cart(BIG + G0) @ S) @ Binv).astype(int)     # rows: S^-1 (h + G0) = (h + G0) S
        ok = (np.abs(hp) <= 8).all(1)
        i2 = -np.ones(NBIG, int)
        i2[ok] = LUT[hp[ok, 0] + 8, hp[ok, 1] + 8, hp[ok, 2] + 8]
        good = i2 >= 0
        acc[good] += ed[i2[good]]
        cnt[good] += 1
    out = ed.copy()
    out[cnt > 0] = acc[cnt > 0] / cnt[cnt > 0]
    if j == 0:
        out[0] = ed[0]
    return out


EINV[0] = little_group_average(0, EINV[0])
red = {}
for j in reps[1:]:
    red[j] = little_group_average(j, screening_at(P[j]))
log(f"irreducible screening done ({len(reps) - 1} points)")
for j in range(1, NP):
    S = ops[opi[j]]
    r = rep[j]
    G0 = np.rint((P[j] - S @ P[r]) @ Binv).astype(int)   # P_j = S P_r + G0
    Sinv = S.T
    for h in range(NBIG):
        hp = np.rint((Sinv @ cart(BIG[h] + G0)) @ Binv).astype(int)
        i2 = bigkey.get(tuple(hp), -1)
        EINV[j, h] = red[r][i2] if i2 >= 0 else 1.0
    if j == r:
        EINV[j] = red[r]
# check the symmetry map at two general points
for j in [jj for jj in range(1, NP) if rep[jj] != jj][:2]:
    direct = screening_at(P[j])
    err = np.abs(direct[:NG] - EINV[j, :NG]).max()
    log(f"symmetry-map check at p index {j}: max |diff| on 59 G = {err:.2e}")
    assert err < 1e-3   # not exact: the band cut at 4 + 26 can split a degenerate multiplet at symmetric k
    direct = little_group_average(j, direct)
    err = np.abs(direct[:NG] - EINV[j, :NG]).max()
    log(f"   after averaging both over the little group: {err:.2e}")
    assert err < 1e-4
# cell average of 1/q^2 over the grid cell around q = 0 (parallelepiped of B/NK), subdivided n^3 times,
# the subcell at the origin replaced by the sphere of equal volume (3/R^2)
nsub = 40
s = (np.arange(nsub) + 0.5) / nsub - 0.5
sc = np.array(np.meshgrid(s, s, s, indexing="ij")).reshape(3, -1).T / NK
q2 = ((sc @ B * tpa) ** 2).sum(1)
vcell = abs(np.linalg.det(B * tpa)) / NK**3
i0 = np.argmin(q2)
Rsph = (3 * vcell / nsub**3 / (4 * np.pi)) ** (1 / 3)
inv_q2 = (np.sum(1 / np.delete(q2, i0)) + 3 / Rsph**2) / nsub**3
log(f"<1/q^2> over the cell = {inv_q2:.4f} bohr^2 (sphere of equal volume: "
    f"{3 / (3 * vcell / (4 * np.pi)) ** (2 / 3):.4f})")

# ------------------------------------------------------------------ transition basis (shifted grid)
make_states(0.5)
NT = NKT * NV * NCB
tidx = lambda ik, iv, ic: (ik * NV + iv) * NCB + ic
DELTA = (EN[:, None, NV:NV + NCB] - EN[:, :NV, None]).reshape(-1)        # (k, v, c)
bvec = np.empty(NT, complex)                                            # b_t = v^x_cv / Delta
X = np.empty((NT, NG - 1), complex)                                     # sqrt(v(G)/V) rho_cv(k, G), G != 0
vG59 = 4 * np.pi / ((cart(BIG[1:NG]) * tpa) ** 2).sum(1)
for ik in range(NKT):
    c = CV[ik][:, :NV + NCB]
    kx = (kp[ik][0] + Gb[:, 0]) * tpa
    vx = np.einsum("gm,g,gn->mn", c.conj(), kx, c)
    dE = EN[ik, None, NV:NV + NCB] - EN[ik, :NV, None]                    # (v, c)
    sl = slice(ik * NV * NCB, (ik + 1) * NV * NCB)
    bvec[sl] = (vx[NV:, :NV].T / dE).reshape(-1)
    r = rho_pairs(U[ik, NV:NV + NCB], U[ik, :NV], BIG[1:NG])            # (58, c, v)
    X[sl] = (np.sqrt(vG59 / V)[:, None, None] * r).transpose(2, 1, 0).reshape(-1, NG - 1)
log(f"transition basis: N_t = {NT}, min transition {DELTA.min() * HA:.3f} eV")

# ------------------------------------------------------------------ direct kernel, dense
H = np.zeros((NT, NT), np.complex64)
Kd_diag = np.zeros(NT)
mLF = BIG[:NG]
n_out = 0
for ik in range(NKT):
    p = kp - kp[ik]                                     # k' - k for all k' (raw differences)
    jp = order_p[pindex(p)]
    Gf = np.rint((p - P[jp]) @ Binv).astype(int)        # p = P_j + Gf
    # W_G(p) for G in the 59 set: eps^-1_{G+Gf, G+Gf}(P_j) v(|p+G|)
    hh = Gf[:, None, :] + mLF[None, :, :]
    assert np.abs(hh).max() <= 8
    hidx = LUT[hh[..., 0] + 8, hh[..., 1] + 8, hh[..., 2] + 8]
    einv = np.where(hidx >= 0, EINV[jp[:, None], hidx], 1.0)    # beyond |G|^2 = 40: unscreened
    n_out += int((hidx < 0).sum())
    pg2 = (((p[:, None, :] + cart(mLF)[None]) * tpa) ** 2).sum(-1)
    with np.errstate(divide="ignore"):
        Wk = einv * 4 * np.pi / pg2
    z = np.where(pg2 < 1e-12)
    Wk[z] = EINV[0, 0] * 4 * np.pi * inv_q2
    Wk /= V
    # rho_c'c(k, p+G) = <c',k'| e^{i(p+G)r} |c,k>: products u_{c'k'}^* u_{ck}, extract at -G (no folding: k+p = k')
    rc = rho_pairs(U[:, NV:NV + NCB], U[ik, None, NV:NV + NCB], mLF)    # (k', G, c', c)
    rv = rho_pairs(U[:, :NV], U[ik, None, :NV], mLF)                    # (k', G, v', v)
    # K^d[(k v c),(k' v' c')] = sum_G conj(rc[k',G,c',c]) W[k',G] rv[k',G,v',v]
    blk = np.einsum("kgac,kg,kgbv->vckba", rc.conj(), Wk, rv, optimize=True)   # (v, c, k', v', c')
    H[ik * NV * NCB:(ik + 1) * NV * NCB] = -blk.reshape(NV * NCB, NT)
    Kd_diag[ik * NV * NCB:(ik + 1) * NV * NCB] = np.diagonal(
        blk[:, :, ik].reshape(NV * NCB, NV * NCB)).real
    if ik % 200 == 0:
        log(f"  K^d row block {ik}/{NKT}")
del U
log(f"fraction of (k, k', G) terms with p + G beyond the screened set (taken unscreened): {n_out / (NKT * NKT * NG):.2e}")
# Hermiticity defect and symmetrization, block by block (no full-size temporaries)
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
log(f"K^d built; Hermiticity defect {herm:.2e}; K^d diagonal: min {Kd_diag.min() * HA * 1e3:.2f} meV, "
    f"mean {Kd_diag.mean() * HA * 1e3:.2f} meV")
assert herm < 1e-4
assert Kd_diag.min() > 0
Kx_diag = (np.abs(X) ** 2).sum(1)
# add Delta and 2 K^x (in blocks)
for r0 in range(0, NT, 2048):
    H[r0:r0 + 2048] += (2 * X[r0:r0 + 2048] @ X.conj().T).astype(np.complex64)
H[np.arange(NT), np.arange(NT)] += DELTA.astype(np.float32)
log(f"H built ({H.nbytes / 1e9:.2f} GB); K^x diagonal mean {Kx_diag.mean() * HA * 1e3:.3f} meV")


# ------------------------------------------------------------------ Haydock and static solves
def mv_ip(x):
    return DELTA * x


def mv_lf(x):
    return DELTA * x + 2 * (X @ (X.conj().T @ x))


def mv_bse(x):
    return (H @ x.astype(np.complex64)).astype(complex)


def mv_kd(x):                                           # attraction only (exchange off), for the record
    return mv_bse(x) - 2 * (X @ (X.conj().T @ x))


def haydock(mv, b, n):
    nb = np.linalg.norm(b)
    q_prev = np.zeros_like(b)
    q = b / nb
    al, be = [], [0.0]
    for _ in range(n):
        w = mv(q) - be[-1] * q_prev
        a_ = np.vdot(q, w).real
        w = w - a_ * q
        b_ = np.linalg.norm(w)
        al.append(a_)
        be.append(b_)
        q_prev, q = q, w / b_
    return nb**2, np.array(al), np.array(be[1:])


def cfrac(z, nb2, al, be):
    """b^+ (z - H)^-1 b from the Lanczos coefficients (terminated with the square-root terminator)."""
    a_inf, b_inf = al[-50:].mean(), be[-50:].mean()
    sq = np.sqrt((z - a_inf) ** 2 - 4 * b_inf**2 + 0j)
    t1, t2 = (z - a_inf - sq) / (2 * b_inf**2), (z - a_inf + sq) / (2 * b_inf**2)
    t = np.where(t1.imag * np.sign(z.imag) < 0, t1, t2)   # the root with the analytic sign of a resolvent
    g = t
    for a_, b_ in zip(al[::-1], be[::-1]):
        g = 1 / (z - a_ - b_**2 * g)
    return nb2 * g


def eps_of(mv):
    nb2, al, be = haydock(mv, bvec, NLANCZOS)
    z = W + 1j * ETA
    F = cfrac(z, nb2, al, be) + cfrac(-z, nb2, al, be)
    return 1 - 4 * np.pi * 2 / V * F


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


eps = {}
stat = {}
for name, mv in (("ip", mv_ip), ("lf", mv_lf), ("bse", mv_bse), ("kd", mv_kd)):
    eps[name] = eps_of(mv)
    x, nit = cg(mv, bvec)
    stat[name] = 1 + 16 * np.pi / V * np.vdot(bvec, x).real
    log(f"{name:4s}: eps_inf {stat[name]:.4f} (CG {nit} it); eps(0) from Haydock {eps[name][0].real:.4f}")
# IP: Haydock vs direct Lorentzian sum
lor = (bvec.conj() * bvec).real
direct = 1 - 8 * np.pi / V * np.array([(lor * (1 / (x + 1j * ETA - DELTA) - 1 / (x + 1j * ETA + DELTA))).sum()
                                       for x in W])
errip = np.abs(direct - eps["ip"]).max() / np.abs(direct.imag).max()
log(f"IP Haydock vs direct sum: max rel. difference {errip:.2e}")
assert errip < 1e-3

# Reciprocal-vector check on the same transitions (q -> 0).  With A_G = rho_cv(k, G)^* (A_0 = b^*) and, for the
# reverse pair, B_G = rho_vc(k, G)^* = rho_cv(k, -G) (B_0 = -b), the bubble is
#   R0_GG'(w)/q^.. = (2/V) sum_t [A_G A_G'^* /(w - D_t + i eta) - B_G B_G'^* /(w + D_t + i eta)],
# and eps_mac = 1 - 4 pi Rbar_00 with Rbar = R0 + R0 vbar Rbar.  (i) With the resonant term alone, the Dyson equation
# is the Woodbury form of the transition-space resolvent with Delta + 2 K^x, so its head must equal the Haydock
# fraction of mv_lf exactly (this pins the prefactor, the 1/V and the sign of K^x).  (ii) With both terms it is the full
# RPA + LF without the Tamm-Dancoff approximation; the difference measures the Tamm-Dancoff error.
log("reciprocal-vector Dyson check on the same transitions")
neg = np.array([bigkey[tuple(-m)] for m in BIG[:NG]])
assert neg.max() < NG
Acol = np.empty((NT, NG), complex)
Acol[:, 0] = bvec.conj()
Acol[:, 1:] = (X / np.sqrt(vG59 / V)[None, :]).conj()
rhoG = np.empty((NT, NG), complex)                       # rho_cv(k, G), with the scaled head at G = 0
rhoG[:, 0] = bvec
rhoG[:, 1:] = X / np.sqrt(vG59 / V)[None, :]
Bcol = rhoG[:, neg]                                     # rho_cv(k, -G)
Bcol[:, 0] = -bvec
DE = 0.005 / HA
nbin = int(DELTA.max() / DE) + 3
xb = DELTA / DE
i0 = np.floor(xb).astype(int)
wt = xb - i0
Mres = np.zeros((nbin, NG * NG), complex)
Mant = np.zeros((nbin, NG * NG), complex)
for c0 in range(0, NT, 1024):
    sl = slice(c0, c0 + 1024)
    oR = (Acol[sl, :, None] * Acol[sl, None, :].conj()).reshape(-1, NG * NG)
    oA = (Bcol[sl, :, None] * Bcol[sl, None, :].conj()).reshape(-1, NG * NG)
    np.add.at(Mres, i0[sl], (1 - wt[sl])[:, None] * oR)
    np.add.at(Mres, i0[sl] + 1, wt[sl][:, None] * oR)
    np.add.at(Mant, i0[sl], (1 - wt[sl])[:, None] * oA)
    np.add.at(Mant, i0[sl] + 1, wt[sl][:, None] * oA)
Eb = np.arange(nbin) * DE
vbar = np.zeros(NG)
vbar[1:] = vG59
Kh = np.diag(vbar)
eps_full = np.empty(len(W), complex)
res_dyson = np.empty(len(W), complex)
for iw, x in enumerate(W):
    gr = 1 / (x + 1j * ETA - Eb)
    ga = 1 / (x + 1j * ETA + Eb)
    R0r = (2 / V) * (gr @ Mres).reshape(NG, NG)
    R0 = R0r - (2 / V) * (ga @ Mant).reshape(NG, NG)
    Rr = np.linalg.solve(np.eye(NG) - R0r @ Kh, R0r)
    Rf = np.linalg.solve(np.eye(NG) - R0 @ Kh, R0)
    res_dyson[iw] = Rr[0, 0]
    eps_full[iw] = 1 - 4 * np.pi * Rf[0, 0]
nb2, al, be = haydock(mv_lf, bvec, NLANCZOS)
res_tr = (2 / V) * cfrac(W + 1j * ETA, nb2, al, be)
# binning moves each pole by at most DE/2; compare on the broadened curves
errdy = np.abs(res_dyson - res_tr).max() / np.abs(res_tr).max()
log(f"resonant Dyson vs transition-space resolvent: max rel. difference {errdy:.2e}")
assert errdy < 5e-3
m = (W * HA > 2.5) & (W * HA < 6)
tda = np.abs(eps_full.imag - eps["lf"].imag)[m].max() / eps_full.imag[m].max()
log(f"Tamm-Dancoff error of RPA + LF eps_2 (2.5-6 eV): max {tda:.3%} of the peak")

np.savez_compressed(os.path.join(HERE, "fig4_11_data.npz"), w=W * HA,
                    eps_ip=eps["ip"], eps_lf=eps["lf"], eps_bse=eps["bse"], eps_kd=eps["kd"], eps_lf_full=eps_full,
                    st_ip=stat["ip"], st_lf=stat["lf"], st_bse=stat["bse"], st_kd=stat["kd"],
                    epsmac_model=epsmac_model, epsip_model=epsip_model, NK=NK, NV=NV, NCB=NCB, NCS=NCS, NG=NG,
                    eta=ETA * HA, Omega=Omega, Emin=DELTA.min() * HA, Kd_mean=Kd_diag.mean() * HA,
                    Kd_min=Kd_diag.min() * HA, Kx_mean=Kx_diag.mean() * HA, einv00=EINV[0, 0],
                    inv_q2=inv_q2, tda=tda, herm=herm, errip=errip, errdy=errdy)
log("saved fig4_11_data.npz")
