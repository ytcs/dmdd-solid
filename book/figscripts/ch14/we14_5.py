"""Numbers of Sect. 14.5 outside the Limit Checks, and Worked Example 14.5 (we:14-quartz). Log we14_5.log.
Run: python we14_5.py  (seconds).

1. Point group 32 (alpha-quartz, tellurium): the six matrices with the threefold axis along z and a twofold axis along x;
   invariant counts from eq:C.17-ninv for the gyration tensor (character det R (1 + 2 cos theta)^2, eq:C.17-gyration), the polar
   vector (l = 1 part of a scalar odd response), the l = 3 harmonics and the rank-three polar tensor; the invariant gyration tensor
   from the projector Q = |P|^-1 sum_R D(R) acting on all 9 components (the axial-polar product representation (det R) R x R).
2. Gyration tensor of alpha-quartz from DFPT: Zabalo and Stengel, arXiv:2304.00048, Table I (LDA, experimental structure):
   g11 = -0.071 bohr, g33 = 0.125 bohr; their Eq. (4): rotatory power rho = omega^2 g33/(2 c^2) along the optic axis.
   Orientation average of qhat.g.qhat: (2 g11 + g33)/3.  Scale q|g33| at the optical and at the dark-matter momenta.
3. Born-charge magnetic moment of the lowest-band phonons of GaAs (2301.07617 Eq. (7); 2511.20461 Eq. (12)):
   mu^ph_z = sum_kappa (e Z*_kappa / 2 M_kappa) L^ph_kappa,z, in nuclear magnetons, with the PBE Born charges of the force-constant
   file (+-2.094; the book's GaAs value 2.11 of Sect. 5.5 changes the result by 1 %), per-atom L^ph_kappa = -i e*_kappa x e_kappa.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
LOG = open(os.path.join(HERE, "we14_5.log"), "w")


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


# ---------------- 1. point group 32
def rot(axis, th):
    a = np.asarray(axis, float); a /= np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K


Rs = [np.eye(3), rot([0, 0, 1], 2 * np.pi / 3), rot([0, 0, 1], -2 * np.pi / 3)]
Rs += [rot([np.cos(p), np.sin(p), 0], np.pi) for p in (0, 2 * np.pi / 3, 4 * np.pi / 3)]
P = len(Rs)
th = [np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)) for R in Rs]
dets = [np.linalg.det(R) for R in Rs]
cV = [d * (1 + 2 * np.cos(t)) for d, t in zip(dets, th)]
gyr = sum(d * (1 + 2 * np.cos(t))**2 for d, t in zip(dets, th)) / P
pol = sum(cV) / P
l3 = sum((np.sin(3.5 * t) / np.sin(t / 2) if t > 1e-9 else 7.0) for t in th) / P
r3 = sum(c**3 for c in cV) / P
out(f"point group 32: order {P}; N_gyr = {gyr:.3f}; polar-vector invariants = {pol:.3f}; l = 3 invariants = {l3:.3f};"
    f" rank-3 polar invariants = {r3:.3f}")
Q = sum(np.linalg.det(R) * np.kron(R, R) for R in Rs) / P    # acts on vec(g), g_ml with m axial, l polar
evals, evecs = np.linalg.eigh(0.5 * (Q + Q.T))
inv = evecs[:, evals > 0.5]
out(f"  invariant gyration tensors (rank of the projector = {inv.shape[1]}):")
for i in range(inv.shape[1]):
    out("   ", np.round(inv[:, i].reshape(3, 3), 3).tolist())
out("  character check of the two-dimensional irrep E on (1, C3, C2'): sum |c|^2 / 6 =", (4 + 2 * 1 + 3 * 0) / 6)

# ---------------- 2. alpha-quartz gyration
BOHR_NM = 0.0529177210903
HBARC = 197.3269804           # eV nm
g11, g33 = -0.071, 0.125      # bohr
out(f"alpha-quartz (LDA, 2304.00048 Table I): g11 = {g11} bohr, g33 = {g33} bohr; orientation average (2 g11 + g33)/3 = "
    f"{(2*g11+g33)/3:.4f} bohr = {(2*g11+g33)/3/g33:.3f} of g33")
for E in (2.105,):
    k = E / HBARC                 # nm^-1
    rho = k**2 * g33 * BOHR_NM / 2   # rad/nm
    out(f"  rotatory power along the optic axis at {E} eV (589 nm): rho = {rho*1e6:.4f} rad/mm = {np.degrees(rho*1e6):.2f} deg/mm"
        f" (= {np.degrees(rho*1e6)/E**2:.2f} deg/(mm eV^2); source: 4.9)")
    out(f"  q|g33| for a vacuum photon of {E} eV: {k*g33*BOHR_NM:.2e}")
for qk in (1.0, 3.77):
    q = qk * 1e3 / HBARC          # nm^-1
    out(f"  q|g33| at q = {qk} keV: {q*g33*BOHR_NM:.4f}")
vmax = (544.0 + 250.5) / 299792.458
out(f"  smallest dark-matter momentum at energy omega: omega/v_max = {1/vmax:.0f} omega (v_max = {vmax:.3e}); at 10 eV: "
    f"{10/vmax/1e3:.2f} keV")

# ---------------- 3. Born-charge moment of GaAs lowest-band phonons
import gaas_ifc14 as G     # noqa: E402
B = np.array([[-1, -1, 1], [1, 1, 1], [-1, 1, -1]], float)
N = 20
g = (np.array([(i, j, k) for i in range(N) for j in range(N) for k in range(N)], float) + 0.5) / N
w, ev = G.phonons(g @ B)
e = ev.reshape(len(g), 2, 3, 6)
Lk = np.real(-1j * np.cross(np.conj(e), e, axis=2))          # (Q, kappa, 3, nu)
Zs = np.array([G.ZEU[0, 0, 0], G.ZEU[1, 0, 0]])
Mu = np.array([69.723, 74.9216]) * 931.49410242 / 938.27208816   # in proton masses
mu = np.einsum("k,qkav->qav", Zs / Mu, Lk)                    # units of mu_N (e hbar / 2 m_p)
mu1 = np.linalg.norm(mu[:, :, 0], axis=1)
out(f"GaAs Born charges +-{Zs[0]:.3f}; lowest band: max |mu^ph| = {mu1.max():.4f} mu_N, mean {mu1.mean():.4f} mu_N;"
    f" all bands max {np.linalg.norm(mu, axis=1).max():.4f} mu_N")
out(f"  bound for |L^ph| = 1 on one sublattice: Ga {Zs[0]/Mu[0]:.4f} mu_N, As {abs(Zs[1])/Mu[1]:.4f} mu_N;"
    f" mu_B/mu_N = {938.27208816/0.51099895:.1f}")
LOG.close()
