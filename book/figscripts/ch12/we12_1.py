"""Worked example 12.1 (we:12-oscillator): the joint response of the kick exp(iqx) for one displaced oscillator coupled to a
two-level electron.  Prints every number quoted in the example (log: we12_1.log).

Model and parameters: those of Worked example 8.x (we:8-sectors, figscripts/ch08/we8_sectors.py), unchanged:
    H = omega0 b^dag b + (Delta + gd (b + b^dag)) |up><up| + gn (b + b^dag) (|up><lo| + |lo><up|),   x = l0 (b + b^dag),
    omega0 = 64.1 meV (Si zone-center optical phonon, Sect. 5.2), l0 = 0.048 A (bond coordinate of WE 5.8),
    Delta = 1.17 eV (Si gap), gd = -sqrt(S_HR) omega0 with S_HR = 2 (WE 5.8), gn = 20 meV (model choice), q l0 = 1 (q = 41.1 keV).
Joint response of O = exp(iqx) from the ground state (T = 0): each exact eigenstate f is labelled by the Born-Oppenheimer product
state it overlaps most (overlaps >= 0.996, as in we8_sectors.py); a state on the excited surface with vibrational level m is
assigned omega_e = E(up, 0) - E_0, the zero-phonon energy of the excited level, and omega_l = E_f - E_0 - omega_e.
Leading entries compared with the exact weights (all at n_B = 2):
  (a) Condon, excited-surface vibrational states: amplitude f(0) <chi_up,m| e^{iqx} |chi_lo,0>, f(x) = q d_10(x)/(Mx DeltaE(x));
  (b) the same with f(x) kept as a function of x inside the vibrational matrix element (non-Condon);
  (c) ground-surface vibrational states and the vertical gap (the lattice final states of the electron-following sector):
      Poisson weights of mean (q l0)^2 at omega_l = m omega0, omega_e = Delta;
  (d) analytic equal-frequency harmonic surfaces: Poisson of mean (q l0)^2 + S_HR at omega_l = m omega0.
Run: python we12_1.py (numpy, scipy; about 10 s).  N = 140 and 200 oscillator states agree to the digits printed.
"""
import numpy as np
from math import factorial
from scipy.linalg import eigh, expm

HBARC = 1973.269804      # eV A
omega0, l0, Delta = 0.0641, 0.048 / HBARC, 1.17
S_HR, gn, ql0 = 2.0, 0.020, 1.0
gd = -np.sqrt(S_HR) * omega0
Mx = 1 / (2 * l0**2 * omega0)
q = ql0 / l0
ER = q**2 / (2 * Mx)


def run(N, nm=30):
    b = np.diag(np.sqrt(np.arange(1, N)), 1)
    X = l0 * (b + b.T)
    num = np.diag(np.arange(N, dtype=float))
    I2, IN = np.eye(2), np.eye(N)
    Pe = np.diag([0.0, 1.0])
    sx = np.array([[0.0, 1.0], [1.0, 0.0]])
    H = np.kron(I2, omega0 * num) + np.kron(Pe, Delta * IN) + np.kron(Pe, (gd / l0) * X) + np.kron(sx, (gn / l0) * X)
    E, V = eigh(H)
    xk, U = eigh(X)
    T = U.T @ (omega0 * num - 0.5 * Mx * omega0**2 * X @ X) @ U
    Es = np.zeros((2, N)); psi = np.zeros((2, 2, N))
    for k, x in enumerate(xk):
        ev, vec = eigh(np.array([[0.0, gn / l0 * x], [gn / l0 * x, Delta + gd / l0 * x]]))
        if vec[0, 0] < 0: vec[:, 0] *= -1
        if vec[1, 1] < 0: vec[:, 1] *= -1
        Es[:, k] = ev; psi[:, :, k] = vec
    vib = [eigh(T + np.diag(Es[s] + 0.5 * Mx * omega0**2 * xk**2)) for s in (0, 1)]
    BO = []
    for s in (0, 1):
        for m in range(60):
            vd = psi[:, s, :] * vib[s][1][:, m]
            BO.append((s, m, np.concatenate([U @ vd[0], U @ vd[1]])))
    Bm = np.array([v for (_, _, v) in BO]).T
    nl = 200
    ov = np.abs(Bm.T @ V[:, :nl])**2
    lab = [BO[np.argmax(ov[:, f])][:2] for f in range(nl)]
    ak = V[:, :nl].T.conj() @ (np.kron(I2, expm(1j * q * X)) @ V[:, 0])
    w = np.abs(ak)**2
    dE = E[:nl] - E[0]
    zpl = [i for i, (s, m) in enumerate(lab) if s == 1 and m == 0][0]
    we = dE[zpl]
    exact = np.zeros(nm)
    for f in range(nl):
        s, m = lab[f]
        if s == 1 and m < nm:
            exact[m] += w[f]
    wl_exact = np.array([dE[[i for i, (s, mm) in enumerate(lab) if s == 1 and mm == m][0]] - we for m in range(20)])
    # leading entries on the computed surfaces
    p0, p1 = psi[:, 0, :], psi[:, 1, :]
    d10 = np.sum(p1 * np.gradient(p0, xk, axis=1), axis=0)
    fx = q * d10 / (Mx * (Es[1] - Es[0]))
    f0 = np.interp(0.0, xk, fx)
    kick = np.exp(1j * q * xk)
    c0, c1 = vib[0][1][:, 0], vib[1][1]
    A_c = np.array([c1[:, m] @ (f0 * kick * c0) for m in range(nm)])
    A_x = np.array([c1[:, m] @ (fx * kick * c0) for m in range(nm)])
    lev1 = vib[1][0][:nm] - vib[1][0][0]
    return dict(we=we, exact=exact, wl_exact=wl_exact, Pc=np.abs(A_c)**2, Px=np.abs(A_x)**2, lev1=lev1, f0=f0,
                quanta=(vib[0][0][1] - vib[0][0][0], vib[1][0][1] - vib[1][0][0]))


for N in (140, 200):
    r = run(N)
    ex, Pc, Px, lev = r["exact"], r["Pc"], r["Px"], r["lev1"]
    Pex = ex.sum()
    print("--- N = %d" % N)
    print("zero-phonon energy of the excited level omega_e = %.4f eV (vertical gap %.2f eV, Delta - S_HR omega0 = %.4f eV)"
          % (r["we"], Delta, Delta - S_HR * omega0))
    print("vibrational quanta: ground surface %.1f meV, excited surface %.1f meV" % (r["quanta"][0] * 1e3, r["quanta"][1] * 1e3))
    print("exact P_Mig = %.4e; (a) Condon %.4e; (b) x-dependent %.4e; boost formula (2 omega0 q l0 gn/Delta^2)^2 = %.4e"
          % (Pex, Pc.sum(), Px.sum(), (2 * omega0 * ql0 * gn / Delta**2)**2))
    print(" m  omega_l(meV)  exact frac   (a) frac   (b) frac   (c) Poisson(1)  (d) Poisson(3)")
    b2 = ql0**2 + S_HR
    for m in range(7):
        print("%2d  %8.1f    %.4f     %.4f     %.4f     %.4f        %.4f"
              % (m, r["wl_exact"][m] * 1e3, ex[m] / Pex, Pc[m] / Pc.sum(), Px[m] / Px.sum(),
                 np.exp(-ql0**2) * ql0**(2 * m) / factorial(m), np.exp(-b2) * b2**m / factorial(m)))
    mex = (r["wl_exact"] * ex[:20]).sum() / ex[:20].sum()
    mexall = None
    mc = (lev * Pc).sum() / Pc.sum()
    mx = (lev * Px).sum() / Px.sum()
    print("mean omega_l in Migdal events: exact %.4f eV, (a) %.4f, (b) %.4f, (c) (q l0)^2 omega0 = E_R = %.4f, "
          "(d) [(q l0)^2 + S_HR] omega0 = %.4f eV" % (mex, mc, mx, ER, b2 * omega0))
    print("mean omega_l + omega_e: exact %.4f, (a) %.4f, (b) %.4f, (c) Delta + E_R = %.4f eV"
          % (mex + r["we"], mc + r["we"], mx + r["we"], Delta + ER))
    print("relaxation energy of the excited surface S_HR omega0 = %.4f eV; E_R = %.4f eV" % (S_HR * omega0, ER))
