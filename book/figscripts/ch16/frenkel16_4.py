"""Shared model for Sect. 16.4 (molecular crystals): pi-electron singlets of anthracene, their molecular form factors, the
Frenkel coupling between molecules of the crystal, and the Frenkel-exciton rate of halo dark matter.
Run directly to print the model checks (log: frenkel16_4.log).  Used by we16_4.py, limit16_4a.py and fig16_4.py.

Model and inputs (every number sourced or named as a modelling choice):
  crystal      anthracene, P2_1/a, a = 8.5526, b = 6.0158, c = 11.1720 A, beta = 124.596 deg, Z = 2, carbon fractional
               coordinates of the molecule at the origin from Brock and Dunitz, Acta Cryst. B 46, 795 (1990), as deposited
               in the Crystallography Open Database, entry 5000168 (file COD-5000168.cif).  The second molecule
               is the image under (1/2 - x, 1/2 + y, -z), a twofold rotation about b plus the translation (a + b)/2.
               Cartesian frame: x along a, y along b, z along c' = a x b (perpendicular to a and b).
  orbitals     Hueckel pi orbitals on the 14 carbons, nearest-neighbour resonance integral beta_mn = -0.63 hbar^2/(m_e x_mn^2)
               with the measured bond lengths x_mn (Blanco, Kahn, Lillard, McDermott, arXiv:2103.08601, Eq. (A1); -2.45 eV
               at 1.40 A), refined by a Pariser-Parr-Pople (PPP) self-consistent field in zero differential overlap (ZDO)
               with the one-centre repulsion U = 11.13 eV and the Mataga-Nishimoto interpolation gamma_mn = e^2/(R_mn + e^2/U)
               (modelling choices: the standard pi-electron parameters of the PPP method that 2103.08601 and
               arXiv:1912.02822 use for t-stilbene and benzene).
  singlets     configuration interaction of single excitations (CIS) on the PPP orbitals, 7 x 7 = 49 singlet
               configurations, A_{ia,jb} = (e_a - e_i) d d + 2 (ia|jb) - (ij|ab).  Energies shifted rigidly so that the lowest
               singlet sits at the measured crystal value S1 = 3.1 eV (Rangel et al., arXiv:1604.00041, Table III, Exp.).
  form factor  f_{0x}(q) = <x| sum_j exp(i q.(r_j - r_o)) |0> = sqrt(2) sum_{ia} d^x_{ia} <a| e^{iq.r} |i>  (singlet sqrt(2) as in
               1912.02822 Eq. (10) and 2103.08601 Eq. (9)); in ZDO <a|e^{iq.r}|i> = F_pz(q) sum_m c_ma c_mi exp(i q.R_m), with
               F_pz(q) = J0(q) - 2 J2(q) P2(qhat.n) the form factor of the density of one Slater 2p_z orbital with
               Z_eff = 3.15 (1912.02822 Eq. (2); 2103.08601 Eq. (2)), n the molecular normal.  A real-space check with the
               two-centre (overlap) densities of Loewdin-orthogonalized Slater orbitals is in check_zdo().
  coupling     Frenkel coupling J(Q) between the transition densities of different molecules, as point transition charges
               q_m = sqrt(2) sum d c_mi c_ma on the carbons, summed over the lattice by Ewald's method with the macroscopic
               term (k = Q) removed and the self-molecule pairs excluded; checked for independence of the Ewald parameter.
  halo         book standard halo (App. A.8, Table 1.1): rho_chi = 0.3 GeV/cm^3, v0 = 238, v_esc = 544, v_E = 250.5 km/s;
               velocity integral (1/q) fhat(v_min + v_E qhat.vhat_E) with the Radon transform fhat of Sect. 11.7.
  rate         per unit target mass, incoherent (binned) Frenkel rate
               R(vhat_E) = rho_chi sigma_e/(m_chi mu^2 M_cell) sum_{o,x} int d^3q/(4 pi q) F_DM^2 |f^(o)_{0x}(q)|^2
                           fhat(v_min^x(q) + v_E qhat.vhat_E),  v_min^x = E_x/q + q/(2 m_chi)
               (Sect. 16.4; isotropic average = 1912.02822 Eq. (19) per molecule, 2103.08601 Eq. (8)).  M_cell = 2 x 178.234 u.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")   # small matrices: threading only adds overhead
import numpy as np
from scipy.special import erf, erfc

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "data", "16.4")

# ---- constants --------------------------------------------------------------------------------------------------
ALPHA = 1 / 137.035999084
ME = 510998.95                       # eV
HBARC = 1973.269804                  # eV A
E2 = ALPHA * HBARC                   # e^2/(4 pi eps0) in eV A = 14.39964
H2M = HBARC**2 / ME                  # hbar^2/m_e in eV A^2 = 7.6200
A0_A = HBARC / (ALPHA * ME)          # Bohr radius in A
KEV_PER_INVA = HBARC / 1000.0        # 1 A^-1 = 1.97327 keV
C_KMS = 299792.458
V0, VESC, VE = 238.0, 544.0, 250.5
VMAX = (VESC + VE) / C_KMS
_Z = VESC / V0
NESC = np.pi**1.5 * V0**3 * (erf(_Z) - 2 / np.sqrt(np.pi) * _Z * np.exp(-_Z**2))
RHO_CHI = 0.3e9                      # eV/cm^3
U_AMU_EV = 931.49410242e6
M_MOL_U = 178.234                    # C14H10, g/mol
M_CELL_EV = 2 * M_MOL_U * U_AMU_EV
CM_PER_INVEV = 1.973269804e-5        # 1 eV^-1 in cm
YR = 365.25 * 86400
KG_EV = 5.609588604e35               # eV per kg

# ---- model parameters -------------------------------------------------------------------------------------------
ZEFF = 3.15                          # Slater 2p_z exponent Z_eff (1912.02822 Eq. (2))
ZETA = ZEFF / (2 * A0_A)             # A^-1
U_PPP = 11.13                        # eV, one-centre repulsion (modelling choice)
S1_EXP = 3.1                         # eV, crystal S1 (1604.00041 Table III)

# ---- crystal ----------------------------------------------------------------------------------------------------
A_LAT, B_LAT, C_LAT, BETA_DEG = 8.5526, 6.0158, 11.1720, 124.596
_bt = np.radians(BETA_DEG)
AVEC = np.array([A_LAT, 0, 0])
BVEC = np.array([0, B_LAT, 0])
CVEC = np.array([C_LAT * np.cos(_bt), 0, C_LAT * np.sin(_bt)])
LAT = np.array([AVEC, BVEC, CVEC])   # rows
OMEGA = abs(np.linalg.det(LAT))      # A^3
RECIP = 2 * np.pi * np.linalg.inv(LAT).T   # rows b_i with a_i.b_j = 2 pi delta


def _read_carbons():
    path = os.path.join(SRC, "COD-5000168.cif")
    out = []
    with open(path) as fh:
        for line in fh:
            t = line.split()
            if len(t) == 5 and t[1] == "C":
                out.append([float(s.split("(")[0]) for s in t[2:5]])
    return np.array(out)


FRAC1 = _read_carbons()              # 14 carbons, molecule at the origin
R1 = FRAC1 @ LAT                     # Cartesian, A; centred on the inversion centre at the origin
C2Y = np.diag([-1.0, 1.0, -1.0])     # twofold rotation about b in the Cartesian frame
R2_SHIFT = 0.5 * (AVEC + BVEC)
R2 = R1 @ C2Y.T + R2_SHIFT
NAT = len(R1)


def molecular_axes(R):
    """Long axis L, short in-plane axis M, normal N of a planar molecule (SVD of the centred coordinates)."""
    X = R - R.mean(0)
    _, _, vt = np.linalg.svd(X)
    L, M = vt[0], vt[1]
    N = np.cross(L, M)
    return L, M, N / np.linalg.norm(N)


AX1 = molecular_axes(R1)
AX2 = molecular_axes(R2)


def bonds(R, cut=1.6):
    d = np.linalg.norm(R[:, None] - R[None], axis=-1)
    return (d > 0.1) & (d < cut), d


# ---- PPP SCF + CIS ----------------------------------------------------------------------------------------------
def ppp(R=R1, nocc=7):
    adj, d = bonds(R)
    beta = np.where(adj, -0.63 * H2M / np.where(adj, d, 1.0) ** 2, 0.0)
    gam = E2 / (d + E2 / U_PPP)
    np.fill_diagonal(gam, U_PPP)
    # Hueckel start
    e, c = np.linalg.eigh(beta)
    for _ in range(200):
        P = 2 * c[:, :nocc] @ c[:, :nocc].T
        F = beta - 0.5 * P * gam
        np.fill_diagonal(F, 0.5 * np.diag(P) * U_PPP + gam @ (np.diag(P) - 1) - np.diag(gam) * (np.diag(P) - 1))
        e_new, c_new = np.linalg.eigh(F)
        if np.max(np.abs(np.abs(c_new) - np.abs(c))) < 1e-10:
            e, c = e_new, c_new
            break
        e, c = e_new, c_new
    occ = range(nocc)
    vir = range(nocc, len(e))
    pairs = [(i, a) for i in occ for a in vir]
    n = len(pairs)
    A = np.zeros((n, n))
    for I, (i, a) in enumerate(pairs):
        for J, (j, b) in enumerate(pairs):
            ia = c[:, i] * c[:, a]
            jb = c[:, j] * c[:, b]
            ij = c[:, i] * c[:, j]
            ab = c[:, a] * c[:, b]
            A[I, J] = 2 * ia @ gam @ jb - ij @ gam @ ab
        A[I, I] += e[a] - e[i]
    E, D = np.linalg.eigh(A)
    return dict(e=e, c=c, pairs=pairs, E_ppp=E, D=D, nocc=nocc, beta=beta, gam=gam)


MODEL = ppp()
SHIFT = S1_EXP - MODEL["E_ppp"][0]
E_X = MODEL["E_ppp"] + SHIFT         # shifted singlet energies, eV
# transition charges q^x_m = sqrt(2) sum_{ia} d^x_{ia} c_mi c_ma  (ZDO; sum_m q_m = 0)
_C = MODEL["c"]
_PAIRPROD = np.array([_C[:, i] * _C[:, a] for (i, a) in MODEL["pairs"]])      # (49, 14)
QCH = np.sqrt(2) * MODEL["D"].T @ _PAIRPROD                                     # (nstate, 14)


def dipoles(R=R1):
    """Transition dipoles d_x = sum_m q_m R_m (e A), molecule frame as given by R."""
    return QCH @ (R - R.mean(0))


def osc_strength(R=R1):
    """f^osc_x = 2 m_e E_x |d|^2 / 3 averaged over directions (eq:4.3-osc), and along unit vector e: 2 m_e E |e.d|^2."""
    d = dipoles(R)
    return 2 * E_X * (d**2).sum(1) / H2M / 3.0


# ---- form factors -----------------------------------------------------------------------------------------------
def radial_J(qA, L):
    """J_L(q) = int rho(r) j_L(q r) dr, rho = (2 zeta)^5 r^4 e^{-2 zeta r}/24 (Slater 2p radial density), q in A^-1."""
    from math import factorial
    q = np.maximum(np.asarray(qA, float), 1e-8)
    a = 2 * ZETA
    z = a - 1j * q
    c = a**5 / 24.0
    S = lambda n: factorial(n) * np.imag(z ** (-(n + 1)))   # noqa: E731
    C = lambda n: factorial(n) * np.real(z ** (-(n + 1)))   # noqa: E731
    if L == 0:
        return c * S(3) / q
    return c * (3 / q**3 * S(1) - S(3) / q - 3 / q**2 * C(2))


def F_pz(qvec, normal):
    """Form factor of the density of one Slater 2p_z orbital along `normal`; qvec (..., 3) in A^-1."""
    q = np.linalg.norm(qvec, axis=-1)
    ct = np.where(q > 0, (qvec @ normal) / np.maximum(q, 1e-12), 1.0)
    P2 = 0.5 * (3 * ct**2 - 1)
    return radial_J(q, 0) - 2 * radial_J(q, 2) * P2


def formfactors(qvec, mol=1, states=None):
    """f^(o)_{0x}(q) for molecule o in {1, 2}, phase relative to the molecular centre; qvec (N, 3) in A^-1.
    Returns (nstate, N) complex."""
    R = R1 if mol == 1 else R2 - R2_SHIFT
    normal = AX1[2] if mol == 1 else AX2[2]
    ph = np.exp(1j * qvec @ R.T)                       # (N, 14)
    Fz = F_pz(qvec, normal)                            # (N,)
    Q = QCH if states is None else QCH[states]
    return (Q @ ph.T) * Fz[None, :]


def F_cell(qvec, states):
    """Crystal-frame vertices F_{o x}(q) = exp(i q.r_o) f^(o)_{0x}(q); returns (2*nstates, N), molecule-major."""
    f1 = formfactors(qvec, 1, states)
    f2 = formfactors(qvec, 2, states) * np.exp(1j * qvec @ R2_SHIFT)[None, :]
    return np.vstack([f1, f2])


# ---- Frenkel coupling (Ewald) -----------------------------------------------------------------------------------
_RS_CACHE = {}


def _realspace_kernels(kappa, rmax):
    """erfc(kappa r)/r kernels for the four molecule pairs over the lattice vectors (cached), self-molecule pair removed,
    and the erf self-correction matrices."""
    key = (kappa, rmax)
    if key in _RS_CACHE:
        return _RS_CACHE[key]
    pos = [R1, R2]
    nr = [int(np.ceil(rmax / np.linalg.norm(LAT[i]) * 1.5)) + 1 for i in range(3)]
    rngr = [np.arange(-n, n + 1) for n in nr]
    Rl = np.array(np.meshgrid(*rngr, indexing="ij")).reshape(3, -1).T @ LAT
    kern = {}
    for o in range(2):
        for p in range(2):
            d = pos[o][:, None, None, :] - pos[p][None, :, None, :] - Rl[None, None, :, :]
            r = np.linalg.norm(d, axis=-1)
            K = np.where(r > 1e-9, E2 * erfc(kappa * r) / np.maximum(r, 1e-12), 0.0)
            if o == p:
                K[:, :, np.all(np.abs(Rl) < 1e-9, axis=1)] = 0.0          # exclude the self-molecule pairs
            kern[(o, p)] = K
    selfc = []
    for o in range(2):
        r = np.linalg.norm(pos[o][:, None, :] - pos[o][None, :, :], axis=-1)
        selfc.append(np.where(r > 1e-9, E2 * erf(kappa * r) / np.maximum(r, 1e-12), E2 * 2 * kappa / np.sqrt(np.pi)))
    _RS_CACHE[key] = (Rl, kern, selfc)
    return _RS_CACHE[key]


def frenkel_J(Qvec, states, kappa=0.35, gmax=5.0, rmax=None):
    """J_{ox,o'x'}(Q) in eV for molecules o, o' in {1,2} and the listed states (point transition charges, Ewald).
    Macroscopic term k = Q removed; self-molecule pairs (R = 0, o = o') excluded.  Basis order: molecule-major.
    Reciprocal sum over |Q + G| < gmax (kappa = 0.35 A^-1: the Gaussian factor is below e^-50 at 5 A^-1); real-space sum
    to rmax = 6/kappa (erfc(6) = 2e-17)."""
    Qvec = np.asarray(Qvec, float)
    pos = [R1, R2]
    qs = QCH[states]
    ns = len(states)
    J = np.zeros((2 * ns, 2 * ns), complex)
    # the lattice sum is periodic in Q: sum over k = Q_r + G with Q_r = Q reduced by the nearest reciprocal vector;
    # only the removal of the macroscopic term refers to the unreduced Q (the term k = Q, as in eq:4.9-kernels)
    Qfrac = np.linalg.solve(RECIP.T, Qvec)
    Qr = Qvec - np.round(Qfrac) @ RECIP
    nmax = [int(np.ceil((gmax + np.linalg.norm(Qr)) / np.linalg.norm(RECIP[i]) * 1.5)) + 1 for i in range(3)]
    rng = [np.arange(-n, n + 1) for n in nmax]
    Gi = np.array(np.meshgrid(*rng, indexing="ij")).reshape(3, -1).T
    G = Gi @ RECIP
    k = Qr[None, :] + G
    k2 = (k**2).sum(1)
    keep = (k2 < gmax**2) & (k2 > 1e-14)
    k, k2 = k[keep], k2[keep]
    wk = 4 * np.pi * E2 / OMEGA * np.exp(-k2 / (4 * kappa**2)) / k2
    S = [qs @ np.exp(1j * pos[o] @ k.T) for o in range(2)]
    if rmax is None:
        rmax = 6.0 / kappa
    Rl, kern, selfc = _realspace_kernels(kappa, rmax)
    ph = np.exp(1j * Rl @ Qr)
    for o in range(2):
        for p in range(2):
            blk = (S[o] * wk) @ S[p].conj().T
            M = kern[(o, p)] @ ph
            blk = blk + qs @ M @ qs.T
            if o == p:
                blk = blk - qs @ selfc[o] @ qs.T
            J[o * ns:(o + 1) * ns, p * ns:(p + 1) * ns] = blk
    # remove the macroscopic term k = Q in full (undamped): (4 pi e^2/Omega) S_o(Q) S_p(Q)^*/Q^2
    Q2 = Qvec @ Qvec
    if Q2 > 1e-14:
        SQ = np.concatenate([qs @ np.exp(1j * pos[o] @ Qvec) for o in range(2)])
        J -= 4 * np.pi * E2 / OMEGA * np.outer(SQ, SQ.conj()) / Q2
    return 0.5 * (J + J.conj().T)


def macro_term(qvec, states):
    """(4 pi e^2/Omega) F(q) F(q)^dagger / q^2 (the macroscopic, k = q, term) with the smeared ZDO vertices; eV."""
    Fv = F_cell(qvec[None, :], states)[:, 0]
    q2 = qvec @ qvec
    return 4 * np.pi * E2 / OMEGA * np.outer(Fv, Fv.conj()) / q2


# ---- halo and rate ----------------------------------------------------------------------------------------------
def fhat(s_kms):
    s = np.asarray(s_kms, float)
    return np.where(np.abs(s) < VESC, np.pi * V0**2 / NESC * (np.exp(-s**2 / V0**2) - np.exp(-_Z**2)), 0.0)


def eta_from_fhat(vmin_kms, n=400):
    """eta(v_min) = int_{-1}^{1} dx fhat(v_min + v_E x), (km/s)^-1 (Sect. 11.7)."""
    x, w = np.polynomial.legendre.leggauss(n)
    v = np.atleast_1d(vmin_kms)
    return (w[None, :] * fhat(v[:, None] + VE * x[None, :])).sum(1)


def eta(vmin_kms):
    """eta(v_min) in (km/s)^-1, closed form of App. D.1 (the same function as figscripts/ch16/eject16_3.py), equal to
    eta_from_fhat (checked in __main__)."""
    u = np.maximum(np.asarray(vmin_kms, float), 0.0)
    k = np.pi * V0**2 / (VE * NESC)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + VE) / V0) - erf((u - VE) / V0)) - 2 * VE * np.exp(-_Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(_Z) - erf((u - VE) / V0)) - (VESC + VE - u) * np.exp(-_Z**2))
    return np.where(u < VESC - VE, b1, np.where(u < VESC + VE, b2, 0.0))


def fib_sphere(n):
    i = np.arange(n) + 0.5
    ct = 1 - 2 * i / n
    ph = np.pi * (1 + 5**0.5) * i
    st = np.sqrt(1 - ct**2)
    return np.stack([st * np.cos(ph), st * np.sin(ph), ct], -1)


def ff2_table(qkeV, dirs, states):
    """sum over the two molecules of |f^(o)_{0x}(q)|^2 on (q magnitudes) x (directions): (nstate, nq, ndir)."""
    out = np.zeros((len(states), len(qkeV), len(dirs)))
    for iq, q in enumerate(qkeV):
        qv = dirs * (q / KEV_PER_INVA)
        for mol in (1, 2):
            out[:, iq, :] += np.abs(formfactors(qv, mol, states)) ** 2
    return out


def rate(m_eV, vhats, qkeV, dirs, ff2, states, light=False, sigma_cm2=1e-37):
    """Events per kg-year for wind directions vhats (nv, 3) [unit vectors along v_E in crystal axes].
    ff2 from ff2_table on (qkeV x dirs); quadrature: trapezoid in ln q, equal weights on the Fibonacci sphere."""
    mu = m_eV * ME / (m_eV + ME)
    q = np.asarray(qkeV) * 1e3                          # eV
    lnq = np.log(q)
    wq = np.gradient(lnq)                               # d ln q weights (trapezoid-like on a uniform log grid)
    wq[0] *= 0.5
    wq[-1] *= 0.5
    wdir = 4 * np.pi / len(dirs)
    FDM2 = ((ALPHA * ME / q) ** 4) if light else np.ones_like(q)
    x = dirs @ np.atleast_2d(vhats).T                    # (ndir, nv)
    tot = np.zeros(len(np.atleast_2d(vhats)))
    for s_i, s in enumerate(states):
        vmin = (E_X[s] / q + q / (2 * m_eV)) * C_KMS     # km/s
        ok = vmin < VESC + VE
        if not ok.any():
            continue
        fh = fhat(vmin[ok, None, None] + VE * x[None, :, :])          # (nq', ndir, nv) in (km/s)^-1
        integrand = ff2[s_i][ok][:, :, None] * fh                      # (nq', ndir, nv)
        # d^3q/(4 pi q) = q^2 dq dOmega/(4 pi q) = q^2 dlnq dOmega/(4 pi)
        tot += np.einsum("q,qdv->v", (q[ok] ** 2 * wq[ok] * FDM2[ok]) / (4 * np.pi), integrand) * wdir
    # fhat is per (km/s): convert to natural units (per unit c) -> multiply by C_KMS
    tot *= C_KMS
    sig = sigma_cm2 / CM_PER_INVEV**2                   # eV^-2
    pref = RHO_CHI * CM_PER_INVEV**3 * sig / (m_eV * mu**2 * M_CELL_EV)   # eV^4 * eV^-2 /(eV^3 eV) -> eV^-2 ... times q^2 [eV^2]
    # R [eV] per (target mass eV) -> events per kg per year
    R_per_eV_mass = pref * tot                           # 1/(time in eV^-1) per eV of target mass
    return R_per_eV_mass * KG_EV / (6.582119569e-16) * YR


# ---- ZDO check ----------------------------------------------------------------------------------------------------
def check_zdo(states=(0, 1), N=160, box=24.0, qks=(1.0, 2.0, 4.0, 8.0)):
    """Compare |f_{0x}|^2 in ZDO with the full LCAO result (Loewdin-orthogonalized Slater 2p_z orbitals, overlap densities
    kept), on a real-space grid of N^3 points in a cubic box (spacing 0.15 A; shells of width 2 pi/box); molecule 1 in its
    own frame (axes L, M, N).  Returns {state: (full shell averages, ZDO shell averages)} at the momenta qks (keV), the
    integrals of the transition densities, and the full/ZDO ratio of state 0 along L and M at the grid points near 2, 4 keV."""
    L, M, Nn = AX1
    Rot = np.array([L, M, Nn])
    Rm = (R1 - R1.mean(0)) @ Rot.T
    h = box / N
    x = (np.arange(N) - N // 2) * h
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    norm = np.sqrt(ZETA**5 / np.pi)
    phis = np.array([(norm * (Z - r[2]) * np.exp(-ZETA * np.sqrt((X - r[0])**2 + (Y - r[1])**2 + (Z - r[2])**2)))
                     .astype(np.float32) for r in Rm])
    Sg = np.einsum("aijk,bijk->ab", phis, phis, dtype=np.float64) * h**3
    w, v = np.linalg.eigh(Sg)
    Sm12 = v @ np.diag(w**-0.5) @ v.T
    lam = np.einsum("ba,bijk->aijk", Sm12.astype(np.float32), phis)
    mos = np.einsum("ma,mijk->aijk", MODEL["c"].astype(np.float32), lam)
    del lam
    k = 2 * np.pi * np.fft.fftfreq(N, d=h)
    KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
    KK = np.sqrt(KX**2 + KY**2 + KZ**2)
    shells = [np.abs(KK - qk / KEV_PER_INVA) < 0.5 * (2 * np.pi / box) for qk in qks]
    out, integ, axis = {}, {}, {}
    for st in states:
        D = MODEL["D"][:, st]
        rho_full = np.zeros((N, N, N))
        for (I, (i, a)) in enumerate(MODEL["pairs"]):
            if abs(D[I]) > 1e-4:
                rho_full += np.sqrt(2) * D[I] * mos[i] * mos[a]
        rho_zdo = np.einsum("m,mijk->ijk", QCH[st], phis.astype(np.float64) ** 2)
        Pf = np.abs(np.fft.fftn(rho_full)) ** 2 * h**6      # |f(q)|^2 (|.| makes the FFT sign convention immaterial)
        Pz = np.abs(np.fft.fftn(rho_zdo)) ** 2 * h**6
        out[st] = (np.array([Pf[s].mean() for s in shells]), np.array([Pz[s].mean() for s in shells]))
        integ[st] = (rho_full.sum() * h**3, rho_zdo.sum() * h**3)
        if st == 0:
            for qk in (2.0, 4.0):
                j = int(round(qk / KEV_PER_INVA / (2 * np.pi / box)))
                axis[qk] = (Pf[j, 0, 0] / Pz[j, 0, 0], Pf[0, j, 0] / Pz[0, j, 0], j * 2 * np.pi / box * KEV_PER_INVA,
                            Pf[0, 0, j], Pz[0, 0, j], Pf[j, 0, 0], Pf[0, j, 0])
    return out, integ, axis


if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)
    print("== crystal ==")
    print(f"Omega = {OMEGA:.3f} A^3 (CIF 473.168); rho_T = {M_CELL_EV/U_AMU_EV*1.66053907e-24/(OMEGA*1e-24):.4f} g/cm^3")
    print("C-C bonds per molecule:", bonds(R1)[0].sum() // 2, "; bond lengths (A):",
          np.round(np.unique(np.round(bonds(R1)[1][bonds(R1)[0]], 3)), 3))
    for name, ax in (("molecule 1", AX1), ("molecule 2", AX2)):
        L, M, N = ax
        ang = lambda u, v: np.degrees(np.arccos(abs(u @ v)))   # noqa: E731
        print(f"{name}: angles of L, M, N to (a, b, c'):",
              [tuple(round(ang(u, e), 1) for e in np.eye(3)) for u in (L, M, N)])
    print(f"angle between the molecular normals N1, N2: {np.degrees(np.arccos(abs(AX1[2] @ AX2[2]))):.1f} deg")
    span = (R1 - R1.mean(0)) @ AX1[0]
    rms = np.sqrt(((R1 - R1.mean(0)) ** 2).sum(1).mean())
    print(f"carbon span along L: {span.max()-span.min():.3f} A; rms radius of the carbon frame a_mol = {rms:.3f} A")
    print(f"  q a_mol = 1 at q = {1/rms*KEV_PER_INVA:.3f} keV; threshold q_min = S1/v_max = {S1_EXP/VMAX/1e3:.3f} keV, q_min a_mol = {S1_EXP/VMAX/1e3/KEV_PER_INVA*rms:.2f}")
    print(f"threshold mass 2 S1/v_max^2 = {2*S1_EXP/VMAX**2/1e6:.3f} MeV (v_max = {VMAX:.4e})")
    print("\n== PPP orbitals and singlets ==")
    e = MODEL["e"]
    print("orbital energies (eV):", np.round(e, 3))
    print(f"HOMO-LUMO orbital gap {e[7]-e[6]:.3f} eV; Hueckel resonance integral at 1.40 A: {-0.63*H2M/1.4**2:.3f} eV")
    print(f"rigid shift applied to the CIS energies: {SHIFT:+.3f} eV (PPP-CIS S1 = {MODEL['E_ppp'][0]:.3f} eV)")
    d = dipoles(R1)
    fo = osc_strength(R1)
    L, M, N = AX1
    print(" state  E_PPP   E_x    |d| (eA)  dL     dM     dN    f_osc   leading configurations")
    for s in range(12):
        Dv = MODEL["D"][:, s]
        top = np.argsort(-np.abs(Dv))[:2]
        cfg = ", ".join(f"{MODEL['pairs'][t][0]+1}->{MODEL['pairs'][t][1]+1} ({Dv[t]:+.2f})" for t in top)
        print(f"  {s:3d}  {MODEL['E_ppp'][s]:6.3f} {E_X[s]:6.3f}  {np.linalg.norm(d[s]):7.3f} {d[s]@L:6.3f} {d[s]@M:6.3f} {d[s]@N:6.3f} {fo[s]:7.4f}   {cfg}")
    print(f"sum of f_osc over all 49 CIS singlets: {fo.sum():.3f}")
    vv = np.array([0.0, 150.0, 300.0, 500.0, 700.0, 790.0])
    print("eta closed form vs Legendre integral of fhat (km/s)^-1:", np.round(eta(vv) * 1e3, 6), np.round(eta_from_fhat(vv) * 1e3, 6))
    print("\n== form-factor checks ==")
    qv = np.array([[1e-4, 0, 0], [0, 1e-4, 0]]) @ np.array([L, M, N])
    f0 = formfactors(qv, 1, [0, 1, 2])
    print("f(q -> 0)/q along L and M for states 0-2 (should equal i e.d):", np.round(np.abs(f0) / 1e-4, 4))
    print("compare |e.d| along L, M:", np.round(np.abs(d[:3] @ L), 4), np.round(np.abs(d[:3] @ M), 4))
    fn = formfactors(np.array([N * 2.0]), 1, list(range(10)))
    print("|f| for q = 2 A^-1 along the molecular normal (exactly zero in ZDO):", np.round(np.abs(fn[:, 0]), 8))
    print("\n== Ewald convergence of the Frenkel coupling (default kappa = 0.35, gmax = 5 against other splittings) ==")
    for Q in (0.01 * RECIP[1], 0.3 * RECIP[0] + 0.2 * RECIP[2] + 1.7 * RECIP[1]):
        for kap, gm in ((0.35, 5.0), (0.25, 14.0), (0.5, 14.0)):
            J = frenkel_J(Q, [0, 4], kappa=kap, gmax=gm)
            print(f"  Q = {np.round(Q,3)} A^-1, kappa = {kap}, gmax = {gm}: J(L_a,L_a)_11 = {J[0,0].real*1e3:9.4f} meV,"
                  f" |J(L_a,L_a)_12| = {abs(J[0,2])*1e3:8.4f} meV, |J(L_a,B_b)_12| = {abs(J[0,3])*1e3:8.4f} meV")
    print("\n== ZDO versus full LCAO (overlap densities kept) ==")
    qks = (1.0, 2.0, 4.0, 8.0)
    out, integ, axis = check_zdo((0, 1, 3), qks=qks)
    for st in (0, 1, 3):
        print(f"  state {st}: integral of the transition density (should be 0): full {integ[st][0]:.1e}, ZDO {integ[st][1]:.1e}")
    for n, qk in enumerate(qks):
        a, b = out[0][0][n], out[0][1][n]
        print(f"  q = {qk:4.1f} keV: L_a shell-averaged |f|^2 full = {a:.4e}, ZDO = {b:.4e}, full/ZDO = {a/b:.3f};"
              f" full |f|^2 of state 1 (L_b) and state 3 over full L_a: {out[1][0][n]/a:.4f}, {out[3][0][n]/a:.4f}"
              f" (ZDO: {out[1][1][n]/b:.1e}, {out[3][1][n]/b:.1e})")
    for qk, v in axis.items():
        print(f"  q = {v[2]:.2f} keV: L_a full/ZDO along L {v[0]:.3f}, along M {v[1]:.3f}; |f|^2 along the normal N:"
              f" full {v[3]:.2e}, ZDO {v[4]:.1e}; full along L {v[5]:.2e}, along M {v[6]:.2e}")
