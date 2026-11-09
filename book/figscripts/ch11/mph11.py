"""Shared harmonic inputs for Sect. 11.3 (multiphonon response of silicon) and App. D.31.
Used by limit11_3a.py, fig11_3.py and we11_4.py. Run directly to print the checks.

Phonons: PBE force constants of Sect. 5.2 (DFPT, 6^3 grid, a = 5.431 A, natural Si mass 28.0855 u), Fourier-interpolated by
  figscripts/ch05/si_ifc.py. Eigenvectors in the cell-phase convention of Eq. (5.3-u), u_{R kappa} ~ e_kappa(Q) e^{i Q.R}
  (checked below: the force-constant blocks of nearest neighbours sit at pair vectors R + tau_k - tau_k' of length 2.35 A,
  and the largest off-site displacement correlations B_12(dR) sit on the four bonds).
Static correlation tensor at T = 0 (eq:E.17-Bkk, Sect. 11.3):
  B_{kk'}(dR) = (1/N) sum_{Q nu} e_{k nu}(Q) e_{k' nu}(Q)^dagger e^{i Q.dR} / (2 omega_{Q nu} M),   B_{kk}(0) = B_k,
  on an N^3 grid of Q by FFT. The three acoustic modes at Q = 0 are excluded; the excluded cell is replaced by a sphere of the
  same volume treated in the long-wavelength limit (e_k = ehat/sqrt 2, omega = c_nu Q, isotropic average of 1/c_nu over the
  Christoffel speeds of the same force constants), which adds (Omega/(2pi)^3) * (pi Q_s^2 / M_cell) * <sum_nu 1/c_nu>/3 * 1 to every
  B_{kk'}(dR) with |dR| << 1/Q_s (modelling choice; it adds 5.5e-7 A^2, 0.02 % of <u_x^2>, on a 48^3 grid; printed).
Units: eV, Angstrom; hbar c = 1973.2698 eV A; M = 28.0855 u x 931.494 MeV = 26.162 GeV.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc  # noqa: E402

A_ANG = 5.431
HBARC = 1973.269804              # eV A
M_SI = 28.0855 * 931.494e6       # eV
OMEGA = A_ANG**3 / 4             # A^3, primitive cell
QBZ = (6 * np.pi**2 / OMEGA)**(1 / 3)    # A^-1
QBZ_KEV = QBZ * HBARC / 1e3
TAU = si_ifc.TAU                 # alat units
A1 = si_ifc.A1                   # primitive vectors (rows), alat units
B1 = np.linalg.inv(A1).T         # reciprocal vectors (rows), 2pi/a units: A1 . B1^T = 1
NAT = 2
UX2_WE57 = 2.45e-3               # A^2, T = 0, WE 5.7 (DFPT DOS)


def grid_phonons(N):
    """Frequencies (eV) and eigenvectors on the N^3 grid Q = (i b1 + j b2 + l b3)/N, i,j,l = 0..N-1."""
    idx = np.array(np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing="ij")).reshape(3, -1).T
    Q = (idx / N) @ B1                                   # 2pi/a Cartesian
    ws, evs = [], []
    for c in np.array_split(np.arange(len(Q)), max(1, len(Q) // 4000)):
        w, ev = si_ifc.phonons(Q[c])
        ws.append(w * 1e-3)
        evs.append(ev)
    return idx, Q, np.concatenate(ws), np.concatenate(evs)


def lw_speed_avg():
    """<sum_nu 1/c_nu>/3 over directions (c in units of c = 1), from the same force constants."""
    sys.path.insert(0, HERE)
    import phon11 as P
    qh, wq = P.sphere_grid(24, 48)
    eps = 0.004
    w, _ = si_ifc.phonons(eps * qh)
    c = w[:, :3] * 1e-3 / (eps * 2 * np.pi / A_ANG * HBARC)   # eV / (eV) -> dimensionless speed
    return np.sum(wq[:, None] * (1 / c)) / 3, c


def B_tensor(N, T=0.0):
    """Return dict with grid data and B[k,k'](dR) as array (N,N,N,2,2,3,3) in A^2 (index = dR in primitive coords mod N)."""
    idx, Q, w, ev = grid_phonons(N)
    nQ = len(Q)
    # e_{k nu}^alpha = ev[:, 3k+alpha, nu]
    e = ev.reshape(nQ, NAT, 3, 6)
    wsafe = w.copy()
    mask = np.ones_like(w, bool)
    mask[0, :3] = False                                  # Q = 0 acoustic excluded
    wsafe[~mask] = 1.0
    occ = 1.0 if T == 0 else 1 / np.tanh(wsafe / (2 * T))
    weight = np.where(mask, occ / (2 * wsafe * M_SI), 0.0) * HBARC**2     # A^2
    # F[Q, k, a, k', b] = sum_nu e_{k nu}^a e_{k' nu}^b* weight
    F = np.einsum("qkan,qlbn,qn->qkalb", e, np.conj(e), weight)
    F = F.reshape(N, N, N, NAT, 3, NAT, 3)
    # B(dR) = (1/N^3) sum_Q F(Q) e^{i Q.dR}; Q.dR = 2pi (idx/N).m for dR = m . A1  -> inverse FFT with sign +
    Bk = np.fft.ifftn(F, axes=(0, 1, 2))                 # (1/N^3) sum e^{+2pi i idx.m/N}
    # small-sphere correction for the excluded acoustic cell
    inv_c3, _ = lw_speed_avg()
    Qs = (3 * (2 * np.pi)**3 / (4 * np.pi * OMEGA * nQ))**(1 / 3)      # A^-1
    Mcell = NAT * M_SI
    # Omega/(2pi)^3 int_{|Q|<Qs} d^3Q sum_nu ehat ehat/(2 Mcell c_nu Q hbar c) (hbar c)^2 = Omega/(2pi)^3 pi Qs^2 hbar c/Mcell <sum 1/c>/3
    dB = OMEGA / (2 * np.pi)**3 * np.pi * Qs**2 / Mcell * inv_c3 * HBARC   # A^3 A^-2 eV^-1 (eV A) = A^2
    Bk = np.transpose(Bk, (0, 1, 2, 3, 5, 4, 6))          # (m1,m2,m3,k,k',a,b)
    for k in range(NAT):
        for kp in range(NAT):
            Bk[..., k, kp, :, :] += dB * np.eye(3)
    return dict(N=N, idx=idx, Q=Q, w=w, ev=ev, B=Bk, dB=dB)


def pair_table(Bd, rmax=40.0):
    """List of (d_vec [A], k, k', B_{kk'}(dR) 3x3) for all pairs with |dR + tau_k - tau_k'| <= rmax, excluding none."""
    N = Bd["N"]
    B = Bd["B"]
    rng = np.arange(-N // 2, N // 2)
    m = np.array(np.meshgrid(rng, rng, rng, indexing="ij")).reshape(3, -1).T
    R = (m @ A1) * A_ANG
    out_d, out_B, out_k = [], [], []
    for k in range(NAT):
        for kp in range(NAT):
            d = R + (TAU[k] - TAU[kp]) * A_ANG
            r = np.linalg.norm(d, axis=1)
            sel = r <= rmax
            mm = m[sel] % N
            out_d.append(d[sel])
            out_B.append(B[mm[:, 0], mm[:, 1], mm[:, 2], k, kp])
            out_k.append(np.tile([k, kp], (sel.sum(), 1)))
    return np.concatenate(out_d), np.concatenate(out_k), np.concatenate(out_B)


def convention_test(Bd):
    """Largest |B_01(dR)| pairs: their lengths with the cell-phase sign (+) and with the opposite assignment (-)."""
    N = Bd["N"]
    B = Bd["B"]
    rng = np.arange(-3, 4)
    m = np.array(np.meshgrid(rng, rng, rng, indexing="ij")).reshape(3, -1).T
    res = []
    for mm in m:
        b = B[mm[0] % N, mm[1] % N, mm[2] % N, 0, 1]
        dplus = np.linalg.norm((mm @ A1 + TAU[0] - TAU[1]) * A_ANG)
        dminus = np.linalg.norm((-mm @ A1 + TAU[0] - TAU[1]) * A_ANG)
        res.append((np.abs(b).max(), dplus, dminus, mm))
    res.sort(key=lambda t: -t[0])
    return res[:6]


if __name__ == "__main__":
    # numbers quoted in Sect. 11.3 that need no phonons
    ab = {28: 0.92223, 29: 0.04685, 30: 0.03092}            # natural Si, IUPAC 2013 (Meija et al. 2016)
    mA = sum(a * x for a, x in ab.items())
    vA = sum(a * a * x for a, x in ab.items()) - mA**2
    print("natural Si: <A> = %.4f, var(A) = %.3f, var/<A>^2 = %.2e, <A>^2 = %.1f" % (mA, vA, vA / mA**2, mA**2))
    C11, C12, C44, RHO = 165.6e9, 63.9e9, 79.5e9, 2330.0      # Pa, kg m^-3 (Sect. 11.1, Martinez et al. 2019)
    print("slowest acoustic speed of Si, [110] TA polarized [1-10]: sqrt((C11-C12)/2 rho) = %.3f km/s; [100] TA sqrt(C44/rho) = %.3f km/s"
          % (np.sqrt((C11 - C12) / 2 / RHO) / 1e3, np.sqrt(C44 / RHO) / 1e3))
    for N in (24, 32, 48):
        Bd = B_tensor(N)
        Bon = Bd["B"][0, 0, 0, 0, 0].real
        print("N = %d: on-site B_k (A^2) diag = %s (WE 5.7: %.3e); small-sphere term %.2e A^2"
              % (N, np.round(np.diag(Bon), 6), UX2_WE57, Bd["dB"]))
        for t in convention_test(Bd):
            print("   |B_01| = %.3e A^2 at |dR+tau0-tau1| = %.3f A (cell-phase) vs %.3f A (opposite)" % t[:3])
