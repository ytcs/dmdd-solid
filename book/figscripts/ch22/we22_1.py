"""Worked example 22.1: the f-sum check that a phonon-assisted calculation of silicon must pass (Sect. 22.1).

Every number printed in WE 22.1 is written to we22_1.log by this script.

Part 1 (model): band-sum form of the f-sum rule for one valence state,
    sum_m (eps_{m,k+q} - eps_{v,k}) |rho_mv(k,q)|^2 = q.v_v + q^2/2m_e + delta_NL      (App. E.14, eq:E.14-remainder)
evaluated in the local empirical pseudopotential (EPM) of Cohen and Bergstresser (figscripts/ch03/epm.py, Sect. 3.3),
for which delta_NL = 0 exactly. With a fixed plane-wave set {G} for k and k+q the identity holds exactly in the basis,
so the truncated sum over the lowest N states plus the remainder
    <phi| H(k+q) - eps_vk |phi>,  phi = P_N^perp u_vk
must reproduce q.v + q^2/2m_e to machine precision. We print the fraction reached by the lowest N bands and the closure
residual. Model choice: local EPM (no nonlocal term, no spin-orbit), lattice constant 5.43 A of the original fit,
basis |G|^2 <= 60 (2pi/a)^2 (531 plane waves; the fractions agree to 1e-4 with 40 and 90). This is a model of the check, not of PBE silicon.

Part 2 (arithmetic from book values):
  * q^2/2m_e at |q| = 1 keV.
  * theta_ep = 0.010-0.016 at the absorption edge (tab:8-truncation row theta_ep, Sect. 8.5; tab:13-nuisances).
    The first moment of S^PA relative to the f-sum is of order theta_ep (Sect. 13.3).
  * f-sum tolerance of a converged electronic table: 2 % (App. E.16).
  * Electron-following share of the f-sum: Z_v m_e / M_cell (Sect. 13.7), Z_v = 8 valence electrons per cell,
    M_cell = 2 x 28.0855 u.
  * Allowed misfit of the transfer rule eq:13.7-fsum relative to its own size, estimated as
    (theta_ep^2 + Z_v m_e/M_cell)/theta_ep  (O(g^4) term taken as theta_ep^2 of the f-sum; an estimate).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch03"))
from epm import EPM, RY, HBARC  # noqa: E402

ME = 510998.95          # eV (CODATA 2022)
U_MEV = 931.49410242    # MeV (CODATA 2022)
M_SI = 28.0855          # u, standard atomic weight

out = []


def log(s=""):
    print(s)
    out.append(s)


log("WE 22.1: f-sum check of a phonon-assisted calculation of silicon")
log("=" * 70)

# ---------------- Part 1: band-sum identity in the local EPM -----------------
si = EPM("Si", ecut=60.0)   # basis |G|^2 <= 60 (2pi/a)^2: band-sum fractions converged to 1e-4 against 21, 40, 90
a = si.a
qkeV = 1.0
q_inv_A = qkeV * 1000.0 / HBARC                      # 1/Angstrom
q_red = q_inv_A * a / (2 * np.pi)                    # units of 2pi/a
log(f"EPM silicon, a = {a} A (original fit), basis size N_G = {len(si.G)} plane waves")
log(f"|q| = {qkeV:.1f} keV = {q_inv_A:.4f} 1/A = {q_red:.5f} (2pi/a), along [100]")

q2_over_2m = (qkeV * 1000.0) ** 2 / (2 * ME)          # eV
log(f"q^2/2m_e = {q2_over_2m:.4f} eV")

NLIST = [8, 16, 30, 60, 100]


def band_sum(k, qvec, nval=4):
    """Return per-valence-band target, truncated sums for NLIST, full sum, and remainder closure."""
    Hk = si.hamiltonian(k)
    Hkq = si.hamiltonian(k + qvec)
    ek, uk = np.linalg.eigh(Hk)          # Ry
    ekq, ukq = np.linalg.eigh(Hkq)
    rho = ukq.conj().T @ uk[:, :nval]    # rho_mv = <u_{m,k+q}|u_{v,k}>, same G set
    res = []
    for v in range(nval):
        dE = (ekq - ek[v]) * RY          # eV
        w = np.abs(rho[:, v]) ** 2
        # exact target in the basis: <u_v|H(k+q)-H(k)|u_v> = sum_G |c_v(G)|^2 (|k+q+G|^2 - |k+G|^2)
        kin_k = ((k + si.G) ** 2).sum(-1) * si.k2unit
        kin_kq = ((k + qvec + si.G) ** 2).sum(-1) * si.k2unit
        target = (np.abs(uk[:, v]) ** 2 * (kin_kq - kin_k)).sum() * RY
        full = (dE * w).sum()
        trunc = {N: (dE[:N] * w[:N]).sum() for N in NLIST}
        rem = {}
        for N in NLIST:
            P = ukq[:, :N]
            phi = uk[:, v] - P @ (P.conj().T @ uk[:, v])
            rem[N] = np.real(phi.conj() @ (Hkq @ phi) - ek[v] * (phi.conj() @ phi)) * RY
        res.append((target, full, trunc, rem))
    return res


qvec = np.array([q_red, 0.0, 0.0])
for label, k in [("Gamma", np.zeros(3)), ("k = (0.10, 0.20, 0.30) 2pi/a", np.array([0.10, 0.20, 0.30]))]:
    res = band_sum(k, qvec)
    log("")
    log(f"Point {label}:")
    tgt = sum(r[0] for r in res)
    log(f"  sum over the 4 valence bands of q.v + q^2/2m_e (exact, in the basis) = {tgt:.6f} eV"
        f"  (4 q^2/2m_e = {4*q2_over_2m:.6f} eV)")
    full = sum(r[1] for r in res)
    log(f"  full band sum over all {len(si.G)} states: {full:.6f} eV, relative residual {abs(full-tgt)/tgt:.1e}")
    for N in NLIST:
        tr = sum(r[2][N] for r in res)
        rm = sum(r[3][N] for r in res)
        log(f"  N = {N:3d}: truncated sum / target = {tr/tgt:.4f}; remainder / target = {rm/tgt:.4f};"
            f" closure |trunc + rem - target|/target = {abs(tr+rm-tgt)/tgt:.1e}")

# ---------------- Part 2: arithmetic ------------------------------------------------
log("")
log("Part 2: sizes that set the tolerance of the transfer rule")
th_lo, th_hi = 0.010, 0.016
tol_table = 0.02
Mcell = 2 * M_SI * U_MEV               # MeV
foll = 8 * (ME / 1e6) / Mcell
log(f"theta_ep at the edge = {th_lo:.3f}-{th_hi:.3f} (Sect. 8.5)")
log(f"f-sum tolerance of a converged table (App. E.16) = {tol_table:.2f}; ratio tolerance/theta_ep = "
    f"{tol_table/th_hi:.2f}-{tol_table/th_lo:.2f}")
log(f"electron-following share Z_v m_e/M_cell = 8 x {ME/1e6:.6f} MeV / {Mcell:.1f} MeV = {foll:.2e}")
for th in (th_lo, th_hi):
    mis = (th ** 2 + foll) / th
    log(f"  theta_ep = {th:.3f}: allowed misfit of eq:13.7-fsum relative to its size ~ (theta^2 + share)/theta = {mis:.3f}")

with open(os.path.join(HERE, "we22_1.log"), "w") as f:
    f.write("\n".join(out) + "\n")
