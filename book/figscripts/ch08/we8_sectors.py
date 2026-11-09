"""Worked example of Sect. 8.6 (we:8-sectors): a two-level electron coupled to one oscillator, split exactly into the
electron-following, zero-phonon electronic and phonon-dressed electronic sectors. Prints every number quoted in the example.

Model (linear vibronic coupling of a two-level electron to one mode):
    H = omega0 b^dag b + (Delta + gd (b + b^dag)) |e><e| + gn (b + b^dag) (|e><g| + |g><e|),
    x = l0 (b + b^dag), coordinate mass Mx = M/2, l0 = (2 Mx omega0)^(-1/2).
Parameters (all reused from earlier sections of the book):
    omega0 = 64.1 meV   zone-center optical phonon of Si (Nilsson and Nelin 1972, Sect. 5.2); bond coordinate of WE 5.8
    l0     = 0.048 A    zero-point length of that coordinate (Fig. 5.1, WE 5.8); fixes Mx = 1/(2 l0^2 omega0)
    Delta  = 1.17 eV    low-temperature indirect gap of Si (Sect. 3.3), used here as the level spacing at x = 0
    gd     = -sqrt(S_HR) omega0 with S_HR = 2: the displaced oscillator of WE 5.8 (bond lengthened by 0.136 A)
    gn     = 20 meV     off-diagonal (Herzberg-Teller / nonadiabatic) coupling: a model choice, mixing gn/Delta = 0.017
    q l0   = 1          a kick of momentum q = 1/l0 = 41.1 keV along x; recoil energy on the coordinate q^2/(2 Mx) = omega0
Probes: O_e = sigma_x = |e><g| + |g><e| (electronic transition operator), O_k = exp(i q x) (kick of the coordinate).
Sectors: the exact eigenstates are labelled by their overlap with Born-Oppenheimer product states Psi_s(x) chi_{s,m}(x),
computed on the Gauss-Hermite grid (DVR) of the truncated oscillator basis; s = 0 (ground surface) -> electron-following,
s = 1 with m = 0 -> zero-phonon electronic, s = 1 with m >= 1 -> phonon-dressed electronic. The sector projectors are sums
of exact eigenprojectors, so they commute with H and the split is exact.
Run: python we8_sectors.py   (numpy, scipy). Two basis sizes are compared; only digits stable between them are quoted.
Displacement check: S_HR=0 python we8_sectors.py (g_d = 0) gives P_Mig = 3.517e-6 and an electronic-sector first moment
4.343e-6 eV, within 0.3 % of the leading formulas (3.508e-6; 0.225 + 4.105 = 4.330e-6 eV). At S_HR = 2 the exact values
3.939e-6 and 4.722e-6 eV exceed them by 12 % and 8 %: both differences come from the displaced excited surface.
Logs: we8_sectors_SHR2.log, we8_sectors_SHR0.log.
"""
import numpy as np
from scipy.linalg import eigh, expm

HBARC = 1973.269804      # eV Angstrom
omega0 = 0.0641          # eV
l0 = 0.048 / HBARC       # eV^-1
Delta = 1.17             # eV
import os
S_HR = float(os.environ.get("S_HR", 2.0))   # 2.0 in the text; S_HR=0 isolates the displacement effect (see below)
gd = -np.sqrt(S_HR) * omega0
gn = 0.020               # eV
ql0 = 1.0
Mx = 1.0 / (2 * l0 ** 2 * omega0)   # eV
q = ql0 / l0


def run(N):
    b = np.diag(np.sqrt(np.arange(1, N)), 1)
    X = l0 * (b + b.T)                     # coordinate
    num = np.diag(np.arange(N, dtype=float))
    I2, IN = np.eye(2), np.eye(N)
    Pe = np.diag([0.0, 1.0])               # |e><e|, order (g, e)
    sx = np.array([[0.0, 1.0], [1.0, 0.0]])
    sz = np.diag([-1.0, 1.0])
    H = (np.kron(I2, omega0 * num) + np.kron(Pe, Delta * IN) + np.kron(Pe, (gd / l0) * X)
         + np.kron(sx, (gn / l0) * X))
    E, V = eigh(H)
    E0 = E[0]
    # DVR: eigenbasis of X
    xk, U = eigh(X)
    # kinetic energy in DVR: T = omega0 b^dag b - (1/2) Mx omega0^2 X^2 + const (drop constant)
    T = U.T @ (omega0 * num - 0.5 * Mx * omega0 ** 2 * X @ X) @ U
    # adiabatic electronic states at each grid point
    Esurf = np.zeros((2, N)); psi = np.zeros((2, 2, N))
    for k, x in enumerate(xk):
        hel = np.array([[0.0, gn / l0 * x], [gn / l0 * x, Delta + gd / l0 * x]])
        ev, vec = eigh(hel)
        if vec[0, 0] < 0: vec[:, 0] *= -1
        if vec[1, 1] < 0: vec[:, 1] *= -1
        Esurf[:, k] = ev; psi[:, :, k] = vec
    # BO vibrational states on each surface (pot in DVR is diagonal), lift to full space (basis order: el (x) osc)
    BO = []
    for s in (0, 1):
        hv = T + np.diag(Esurf[s] + 0.5 * Mx * omega0 ** 2 * xk ** 2)
        ev, ch = eigh(hv)
        for m in range(90):
            vec_dvr = np.zeros((2, N))
            vec_dvr[0] = psi[0, s] * ch[:, m]; vec_dvr[1] = psi[1, s] * ch[:, m]
            full = np.concatenate([U @ vec_dvr[0], U @ vec_dvr[1]])
            BO.append((s, m, full))
    # Franck-Condon factor of the two computed surfaces, without and with the x-dependent transition dipole cos(2 theta)
    mu = np.array([abs(psi[:, 1, k] @ sx @ psi[:, 0, k]) for k in range(N)])
    c0 = eigh(T + np.diag(Esurf[0] + 0.5 * Mx * omega0 ** 2 * xk ** 2)); c1 = eigh(T + np.diag(Esurf[1] + 0.5 * Mx * omega0 ** 2 * xk ** 2))
    out_fc = ((c1[1][:, 0] @ c0[1][:, 0]) ** 2, (c1[1][:, 0] @ (mu * c0[1][:, 0])) ** 2, c0[0][1] - c0[0][0], c1[0][1] - c1[0][0])
    Bmat = np.array([v for (_, _, v) in BO]).T
    ov = np.abs(Bmat.T @ V) ** 2          # (BO state, exact state)
    nlab = 120
    lab = []
    for f in range(nlab):
        j = np.argmax(ov[:, f]); s, m, _ = BO[j]
        lab.append((s, m, ov[j, f]))
    psi0 = V[:, 0]
    Oe = np.kron(sx, IN)
    Ok = np.kron(I2, expm(1j * q * X))
    ae = V[:, :nlab].T @ (Oe @ psi0)
    ak = V[:, :nlab].T.conj() @ (Ok @ psi0)
    dE = E[:nlab] - E0
    sec = np.array([0 if s == 0 else (1 if m == 0 else 2) for (s, m, _) in lab])
    out = {"fc": out_fc, "E": E[:nlab], "dE": dE, "lab": lab, "sec": sec}
    for name, a in (("e", ae), ("k", ak)):
        w = np.abs(a) ** 2
        out[name + "W"] = [w[sec == A].sum() for A in range(3)]
        out[name + "M"] = [(dE * w)[sec == A].sum() for A in range(3)]
        out[name + "w"] = w
    cross = (dE * ae.conj() * ak)
    out["xM"] = [cross[sec == A].sum() for A in range(3)]
    # exact totals from commutators
    out["fsum_e"] = float(np.real(psi0 @ (-(np.kron(Pe, Delta * IN) * 0) @ psi0)))
    hz = np.kron(np.diag([0, 1]), Delta * IN + (gd / l0) * X)  # (Delta + gd x/l0)|e><e|
    sz_full = np.kron(sz, IN)
    # sum_f (E_f-E_0)|<f|sx|0>|^2 = -<(Delta + gamma x) sigma_z>
    out["fsum_e"] = float(-(psi0 @ (np.kron(sz, Delta * IN + (gd / l0) * X) @ psi0)))
    out["ER"] = q ** 2 / (2 * Mx)
    wmax = np.maximum(np.abs(ae) ** 2, np.abs(ak) ** 2)
    out["minov"] = min(o for (o, wm) in zip([o for (_, _, o) in lab], wmax) if wm > 1e-10)
    out["nrel"] = int(np.sum(wmax > 1e-10))
    out["groundmix"] = float(psi0 @ np.kron(Pe, IN) @ psi0)
    out["Esurf_info"] = None
    return out


for N in (90, 160):
    r = run(N)
    print(f"--- N = {N}")
    print(f"states with weight > 1e-10: {r['nrel']}")
    print(f"min BO overlap of those exact eigenstates: {r['minov']:.5f}; excited-state weight in the ground state: {r['groundmix']:.3e}")
    zpl = [i for i, (s, m, _) in enumerate(r["lab"]) if s == 1 and m == 0][0]
    ph1 = [i for i, (s, m, _) in enumerate(r["lab"]) if s == 0 and m == 1][0]
    print("BO Franck-Condon factor 00: %.4f, with transition dipole %.4f; surface quanta %.2f / %.2f meV" % (r['fc'][0], r['fc'][1], r['fc'][2]*1e3, r['fc'][3]*1e3))
    print(f"one-phonon level (ground surface): {r['dE'][ph1]*1e3:.3f} meV; zero-phonon level: {r['dE'][zpl]:.5f} eV")
    for name, lbl in (("e", "sigma_x"), ("k", "exp(iqx)")):
        W, M = r[name + "W"], r[name + "M"]
        print(f"{lbl}: weights ad/0/+ = {W[0]:.6e} {W[1]:.6e} {W[2]:.6e}  sum {sum(W):.8f}")
        print(f"{lbl}: 1st moments ad/0/+ (eV) = {M[0]:.6e} {M[1]:.6e} {M[2]:.6e}  sum {sum(M):.8e}")
    print(f"sigma_x exact first moment -<(Delta+gamma x) sz> = {r['fsum_e']:.8e} eV")
    print(f"recoil on the coordinate q^2/2Mx = {r['ER']*1e3:.4f} meV")
    xM = r["xM"]
    print("cross first moments ad/0/+ = " + " ".join(f"{z.real:+.4e}{z.imag:+.4e}i" for z in xM) + f"  sum {sum(xM):.2e}")
    w = r["ew"]
    print(f"sigma_x one-phonon electron-following weight {w[ph1]:.5e}; ZPL weight {w[zpl]:.5f}")
    PM = r["kW"][1] + r["kW"][2]
    print(f"P_Mig = {PM:.4e}; electronic-sector first moment {r['kM'][1]+r['kM'][2]:.4e} eV; P_Mig*E_R = {PM*r['ER']:.4e}")

# analytic leading-order estimates for comparison
dM = 4 * gn ** 2 * omega0 / Delta ** 3     # deltaM/Mx = 2 lambda^2/Delta^3 / Mx with lambda = gn/l0
ER = q ** 2 / (2 * Mx)
print("--- leading-order formulas at x = 0, vertical gap Delta")
print(f"deltaM/Mx = 4 gn^2 omega0/Delta^3 = {dM:.4e}; E1Mig = ER*deltaM/Mx = {ER*dM:.4e} eV")
print(f"P_Mig boost estimate (2 omega0 q l0 gn/Delta^2)^2 = {(2*omega0*ql0*gn/Delta**2)**2:.4e}")
print(f"electron-following weight estimate (2 gn/Delta)^2 = {(2*gn/Delta)**2:.4e}")
print(f"ZPL weight e^-S = {np.exp(-S_HR):.5f}; Mx = {Mx/1e9:.4f} GeV; q = {q/1e3:.2f} keV")
