"""Kinetic-energy (scalar) and current (dark-photon / ALP) absorption spectra of silicon at q -> 0 in the empirical
pseudopotential model, for Sect. 10.7 (Fig. 10.6, the scalar text and the sum-rule check of Limit 10.7b).

Model: the local empirical pseudopotential of Cohen and Bergstresser, Phys. Rev. 141, 789 (1966), via figscripts/ch03/epm.py
(a = 5.43 A, plane waves |k + G| <= sqrt(21) (2 pi/a), 113 plane waves, no spin-orbit coupling, model indirect gap 0.82 eV;
the same model as Sects. 10.1 and 10.4).  Independent particles, pseudo-wavefunctions (no core states, no core
oscillations of the valence and conduction states), clamped nuclei, T = 0.
Rows (Sect. 8.1, eq:8.1-rows, electrons, q = 0):
  T_cv = <c k| p^2/2m_e |v k> = sum_G c*_{cG} |k + G|^2 c_{vG}   (kinetic energy in eV; the row T_e(0))
  v_cv = <c k| p/m_e |v k>       (velocity, units of c; the row j_e(0))
Response functions at q -> 0, T = 0, spin summed (factor 2), V = N_k Omega:
  S_TT(0, w) = (2 pi / V) 2 sum_{c v k} |T_cv|^2 delta(w - E_cv)                   [eV^2]
  eps_2(w)   = (8 pi^2 alpha / (Omega N_k w^2)) sum_{cvk} |e.v_cv|^2 delta(w - E_cv)  (cubic average |v|^2/3)
  sigma_1    = w eps_2
The delta function is a histogram bin of width DW (sum preserving).
Sum rule for a one-body local potential (Sect. 10.7): sum_f (E_f - E_0)|<f|T|0>|^2 = (1/2)<0|[[T,H],T]|0>
  = -(1/2)<[[T,V],V]> = <|grad V|^2>/(2 m_e) per electron.  In the finite plane-wave basis the first equality holds
  exactly (matrix identity); the script checks it (finite-basis double commutator against the spectral first moment) and
  compares with the continuum <|grad V|^2>/2m evaluated with the same wavefunctions.
Inputs: constants as rate10_2.py (CODATA 2018); Ry = 13.605693 eV, bohr = 0.529177 A (CODATA 2022, epm.py).
Run: NK=16 python3 si_scalar10_7.py > si_scalar10_7.log   (about one minute; writes si_scalar10_7.npz)
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, BOHR, HBARC   # noqa: E402

ALPHA = 1 / 137.035999084
NK = int(os.environ.get("NK", 16))
NV = 4
DW = 0.05
WEDGES = np.arange(0.0, 120.0 + DW / 2, DW)
WC = 0.5 * (WEDGES[1:] + WEDGES[:-1])

si = EPM("Si")
G = si.G
NG = len(G)
a_eV = si.a / HBARC                  # lattice constant in eV^-1
Omega = a_eV**3 / 4                  # eV^-3
U = si.U                             # Ry

# Monkhorst-Pack grid over the full zone (fcc reciprocal primitive vectors b_i, units 2 pi/a)
Bm = np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)
f = (np.arange(NK) + 0.5) / NK
kk = np.array([[x, y, z] for x in f for y in f for z in f]) @ Bm

hTT = np.zeros(len(WC))
hjj = np.zeros(len(WC))
first_moment = 0.0          # sum over cvk of w |T_cv|^2  (spectral, all conduction bands in the basis)
dc_basis = 0.0              # -(1/2) sum_v <v|[[T,V],V]|v>  (finite basis)
gradV = 0.0                 # sum_v <v|grad V|^2|v>/2m  (continuum operator, same wavefunctions)
first_vv = 0.0              # valence-valence part of the single-particle sums (cancels in the many-body sum)
edge_T, edge_j = [], []

# continuum |grad V|^2 in plane waves: W(K) = -sum_G G.(K - G) U(G) U(K - G); built as a matrix on the basis


def Uof(vec):
    """U at reciprocal vector vec (units 2 pi/a) for the Si form factors of epm.py (symmetric, origin at bond centre)."""
    s = int(np.rint((vec**2).sum()))
    VS = {3: -0.21, 8: 0.04, 11: 0.08}
    if s not in VS:
        return 0.0
    return VS[s] * np.cos(2 * np.pi * vec.sum() / 8.0)


# shells of potential vectors
shell = np.array([g for g in G if int(np.rint((g**2).sum())) in (3, 8, 11)])
Ush = np.array([Uof(g) for g in shell])
W = np.zeros((NG, NG))
for i1 in range(NG):
    for i2 in range(NG):
        K = G[i1] - G[i2]
        acc = 0.0
        for gs, us in zip(shell, Ush):
            r = K - gs
            ur = Uof(r)
            if ur != 0.0:
                acc -= np.dot(gs, r) * us * ur
        W[i1, i2] = acc               # Ry^2 (2 pi/a)^2
W_eV = W * si.k2unit * RY**3          # <|grad V|^2>/2m in eV^3 (hbar^2/2m = 1 Ry bohr^2)

for k in kk:
    H = si.hamiltonian(k)
    w, v = np.linalg.eigh(H)
    E = w * RY
    kin = ((k + G)**2).sum(-1) * si.k2unit * RY                      # eV
    T = v.conj().T @ (kin[:, None] * v)                             # eV, all bands
    kG = (k + G) * (2 * np.pi * HBARC / si.a)                         # eV
    vel = np.einsum("gm,gi,gn->imn", v.conj(), kG, v) / 510998.95    # c
    Ev, Ec = E[:NV], E[NV:]
    dE = Ec[:, None] - Ev[None, :]
    T2 = np.abs(T[NV:, :NV])**2
    v2 = (np.abs(vel[:, NV:, :NV])**2).sum(0) / 3.0
    hTT += np.histogram(dE.ravel(), WEDGES, weights=T2.ravel())[0]
    hjj += np.histogram(dE.ravel(), WEDGES, weights=v2.ravel())[0]
    first_moment += (dE * T2).sum()
    dvv = Ev[:, None] - Ev[None, :]
    first_vv += (dvv * np.abs(T[:NV, :NV])**2).sum()
    # finite-basis double commutator with V = H - T (matrices in the plane-wave basis)
    Tm = np.diag(kin)
    Vm = H * RY - Tm
    X = Tm @ Vm - Vm @ Tm
    Y = X @ Vm - Vm @ X
    cv = v[:, :NV]
    dc_basis += -0.5 * np.real(np.einsum("gi,gh,hi->", cv.conj(), Y, cv))
    gradV += np.real(np.einsum("gi,gh,hi->", cv.conj(), W_eV, cv))
    edge_T.append(dE.min())

Nk = len(kk)
S_TT = (4 * np.pi / (Omega * Nk)) * hTT / DW                       # eV^2 (spin summed)
eps2 = (8 * np.pi**2 * ALPHA / (Omega * Nk)) * hjj / DW / np.maximum(WC, 1e-9)**2
sig1 = WC * eps2

print(f"EPM silicon, {NG} plane waves, NK = {NK} ({Nk} k points), bins {DW} eV")
print(f"smallest vertical (q = 0) gap on the grid: {min(edge_T):.3f} eV")
print(f"spectral first moment sum_cvk w|T|^2 / N_k            = {first_moment/Nk:.4e} eV^3 per cell (4 bands, one spin)")
print(f"valence-valence part (cancels in the many-body sum)    = {first_vv/Nk:.2e} eV^3")
print(f"finite-basis double commutator -(1/2)<[[T,V],V]>       = {dc_basis/Nk:.4e} eV^3")
print(f"continuum <|grad V|^2>/2m with the same wavefunctions   = {gradV/Nk:.4e} eV^3")
print(f"ratio spectral/double commutator = {first_moment/dc_basis:.6f}; continuum/double commutator = {gradV/dc_basis:.4f}")
per_e = dc_basis / Nk / 4
print(f"sum rule per valence electron <|grad V|^2>/2m = {per_e:.4e} eV^3 = {(per_e)**(1/3):.2f} eV cubed root")
cum = np.cumsum(WC * hTT) / first_moment
for L in (5, 10, 20, 30, 40, 60):
    print(f"  fraction of the first moment below {L:3d} eV: {np.interp(L, WEDGES[1:], cum):.3f}")
# where does S_TT start? report first bins above 1e-3 of max
m = S_TT.max()
on = WC[np.argmax(S_TT > 1e-3 * m)]
on_j = WC[np.argmax(sig1 > 1e-3 * sig1.max())]
print(f"onset (1e-3 of peak): S_TT {on:.2f} eV, sigma_1 {on_j:.2f} eV")
for w0 in (3.0, 4.0, 5.0, 10.0, 20.0):
    i = np.argmin(abs(WC - w0))
    sl = slice(max(i - 5, 0), i + 5)
    print(f"  w = {w0:4.1f} eV: S_TT = {S_TT[sl].mean():.3e} eV^2, eps2 = {eps2[sl].mean():.3f}, sigma1 = {sig1[sl].mean():.3f} eV")
np.savez(os.path.join(HERE, "si_scalar10_7.npz"), omega=WC, S_TT=S_TT, eps2=eps2, sigma1=sig1, NK=NK,
         first_moment=first_moment / Nk, dc_basis=dc_basis / Nk, gradV=gradV / Nk, Omega=Omega)
