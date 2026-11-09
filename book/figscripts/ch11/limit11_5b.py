"""Limit 11.5b (Sect. 11.5): solid helium, quasi-harmonic limit and self-consistent harmonic correction, in a cell model.
Output: tex/figures/ch11/limit11_5b.pdf. Prints every number of the box, its F row and the helium paragraph.

Model (labelled as a model in caption, text and F row; STYLE allows a model figure with reference values):
  one 4He atom in the static field of its 12 nearest neighbours of an fcc lattice (Lennard-Jones--Devonshire cell model),
  the field averaged over the directions of the atom's displacement (spherical cell potential), neighbours fixed.
  Pair potential: Morse, U(s) = D[e^{-2a(s - r_m)} - 2 e^{-a(s - r_m)}], with the well depth D = 10.8 K and position
  r_m = 2.9673 A of the Aziz et al. helium potential (J. Chem. Phys. 70, 4330 (1979)), and a = 6/r_m, which gives the curvature
  2 D a^2 = 72 D/r_m^2 of a 12-6 potential with the same well (modelling choice; finite at s = 0, so Gaussian averages exist).
  Nearest-neighbour distance from the molar volume V_m: d = (sqrt 2 V_m / N_A)^(1/3) (fcc; ideal hcp has the same d).
  Constants: hbar^2/(m_u k_B) = 48.5087 K A^2 (CODATA 2018), m(4He) = 4.002602 u.
Exact: radial Schroedinger equation on 0 < r < 1.3 d, 4000 points (u(r) = r R(r)), l = 0 ground state and lowest l = 1
  state; checked with 8000 points.  Lindemann ratio r_L = <r^2>^(1/2)/d (3D mean-square displacement).
  One-phonon weight per unit q^2 along z: W = |<1, m=0| z |0>|^2 = (1/3)(int u1 u0 r dr)^2; harmonic value hbar^2/(2 m hbar w).
  Kinetic energy per direction: (1/3)(E_0 - <V>).
Quasi-harmonic (static) limit: K_h = V''(0) = (1/3) lap V at the site, hbar w_h = hbar (K_h/m)^(1/2); imaginary if K_h < 0.
SCHA (eq:5.7-scha): K_s = (1/3) <lap V> over the isotropic Gaussian of variance s^2 = hbar/(2 m w_s) per direction, solved by
  iteration; <lap V>_G = <V (r^2/s^4 - 3/s^2)>_G (integration by parts).
Plotted: W_approx / W_exact against r_L, for V_m from 21 to 3 cm^3/mol; gray band where the quasi-harmonic weight is within 10 %.
Reference points (printed, cited in the text): Cazorla and Boronat, arXiv:1409.4945, Table I (diffusion Monte Carlo, Aziz-B
  potential, hcp): r_L = 0.12 at 11.13 A^3/atom (2.0 GPa), 0.10 from 6.68 A^3/atom (14.2 GPa) up.
"""
import os
import numpy as np
from scipy.linalg import eigh_tridiagonal
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
H2M = 48.5087 / 4.002602          # hbar^2/m in K A^2 for 4He
D = 10.8                          # K
RM = 2.9673                       # A
A = 6 / RM                        # A^-1
NA = 6.02214076e23
NZ = 12
KB_MEV = 8.617333e-2              # meV per K


def d_of_vm(vm):
    """Nearest-neighbour distance (A) at molar volume vm (cm^3/mol)."""
    return (np.sqrt(2) * vm * 1e24 / NA)**(1 / 3)


def _I(b, s):
    """int s e^{-b s} ds (antiderivative)."""
    return -np.exp(-b * s) * (s / b + 1 / b**2)


def vcell(r, d):
    """Spherically averaged cell potential (K) at radius r (A), zero at the site."""
    r = np.maximum(np.asarray(r, float), 1e-6)
    lo, hi = np.abs(d - r), d + r

    def avg(b, pref):
        return pref * (_I(b, hi) - _I(b, lo)) / (2 * r * d)
    u = avg(2 * A, D * np.exp(2 * A * RM)) - avg(A, 2 * D * np.exp(A * RM))
    u0 = D * (np.exp(-2 * A * (d - RM)) - 2 * np.exp(-A * (d - RM)))
    return NZ * (u - u0)


def k_static(d, h=1e-3):
    """Curvature V''(0) of the cell potential at the site (K/A^2); V is even in r, V(h) = V(0) + K h^2/2 + O(h^4)."""
    return 2 * (vcell(h, d) - vcell(1e-7, d)) / h**2


def exact(d, n=4000):
    rmax = 1.3 * d
    r = np.linspace(rmax / n, rmax, n)
    h = r[1] - r[0]
    out = {}
    for l in (0, 1):
        diag = H2M / h**2 + vcell(r, d) + H2M * l * (l + 1) / (2 * r**2)
        off = -H2M / (2 * h**2) * np.ones(n - 1)
        E, V = eigh_tridiagonal(diag, off, select="i", select_range=(0, 0))
        u = V[:, 0] / np.sqrt(h)
        out[l] = (E[0], u)
    E0, u0 = out[0]
    E1, u1 = out[1]
    r2 = np.sum(u0**2 * r**2) * h
    vav = np.sum(u0**2 * vcell(r, d)) * h
    dip = np.sum(u1 * u0 * r) * h
    return dict(E0=E0, dE=E1 - E0, r2=r2, rL=np.sqrt(r2) / d, W=dip**2 / 3, kin=(E0 - vav) / 3)


def scha(d, n=6000):
    r = np.linspace(1e-4, 1.6 * d, n)
    h = r[1] - r[0]
    V = vcell(r, d)
    K = max(k_static(d), 1.0)
    for _ in range(500):
        w = np.sqrt(K * H2M)                      # hbar w in K (K in K/A^2)
        s2 = H2M / (2 * w)
        rho = 4 * np.pi * r**2 * np.exp(-r**2 / (2 * s2)) / (2 * np.pi * s2)**1.5
        lap = np.sum(rho * V * (r**2 / s2**2 - 3 / s2)) * h
        Kn = lap / 3
        if abs(Kn - K) < 1e-10 * abs(K):
            break
        K = 0.5 * K + 0.5 * Kn
    return np.sqrt(K * H2M), s2


if __name__ == "__main__":
    vms = np.concatenate([np.linspace(21.0, 8.0, 27), np.linspace(7.5, 3.0, 19)])
    rows = []
    for vm in vms:
        d = d_of_vm(vm)
        ex = exact(d)
        Kh = k_static(d)
        wh = np.sqrt(Kh * H2M) if Kh > 0 else np.nan
        ws, s2 = scha(d)
        Wh = H2M / (2 * wh) if Kh > 0 else np.nan
        Ws = H2M / (2 * ws)
        rows.append((vm, d, ex["rL"], ex["dE"], wh, ws, ex["W"], Wh, Ws, ex["kin"], Kh))
    rows = np.array(rows)
    vm, d, rL, dE, wh, ws, W, Wh, Ws, kin, Kh = rows.T
    ex8 = exact(d_of_vm(21.0), n=8000)
    print("grid check at 21 cm^3/mol: r_L %.4f (8000 pts) vs %.4f; dE %.3f vs %.3f K" % (ex8["rL"], rL[0], ex8["dE"], dE[0]))
    print(" V_m   d(A)   r_L    dE(K)  hw_QH(K) hw_SCHA(K)  W_QH/W  W_SCHA/W  Ekin/dir(K)  QH Ekin/dir  SCHA Ekin/dir")
    for row in rows[::3]:
        print("%5.1f  %.3f  %.3f  %6.2f  %7.2f  %7.2f   %6.3f  %6.3f   %6.2f   %6.2f   %6.2f" %
              (row[0], row[1], row[2], row[3], row[4], row[5], row[7] / row[6], row[8] / row[6], row[9], row[4] / 4, row[5] / 4))
    neg = vm[Kh <= 0]
    if len(neg):
        print("static curvature negative (imaginary harmonic frequency) for V_m >= %.1f cm^3/mol (r_L >= %.3f)" % (neg.min(), rL[Kh <= 0].min()))
    okq = np.abs(Wh / W - 1) <= 0.10
    print("quasi-harmonic one-phonon weight within 10 %% for r_L <= %.3f (V_m <= %.1f cm^3/mol)" % (rL[okq].max(), vm[okq].max()))
    oks = np.abs(Ws / W - 1) <= 0.10
    print("SCHA one-phonon weight within 10 %% for r_L <= %.3f (V_m <= %.1f cm^3/mol); at 21 cm^3/mol SCHA/exact = %.3f"
          % (rL[oks].max(), vm[oks].max(), Ws[0] / W[0]))
    for v in (21.0, 11.13 * NA / 1e24, 6.68 * NA / 1e24):
        j = np.argmin(np.abs(vm - v))
        print("V_m = %.2f cm^3/mol (%.2f A^3/atom): model r_L = %.3f, dE = %.2f K = %.3f meV, QH/exact W = %.3f, SCHA/exact W = %.3f"
              % (vm[j], vm[j] * 1e24 / NA, rL[j], dE[j], dE[j] * KB_MEV, Wh[j] / W[j], Ws[j] / W[j]))

    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(0, rL[okq].max(), color="0.88", lw=0)
    ax.axhline(1.0, color="k", lw=0.6)
    ax.plot(rL, Wh / W, color="C3", lw=1.5, label="quasi-harmonic (static curvature)")
    ax.plot(rL, Ws / W, color="C0", lw=1.5, label="self-consistent harmonic")
    ax.plot(rL, wh / dE, color="C3", lw=0.9, ls="--", label=r"quasi-harmonic, $\omega/\Delta E$")
    ax.plot(rL, ws / dE, color="C0", lw=0.9, ls="--", label=r"self-consistent, $\omega/\Delta E$")
    if len(neg):
        ax.axvline(rL[Kh <= 0].min(), color="C3", lw=0.8, ls=":")
    ax.set_xlim(rL.min() * 0.95, rL.max() * 1.02)
    ax.set_ylim(0, 3.0)
    ax.set_xlabel(r"Lindemann ratio $r_{\mathrm{L}}$ (cell model, exact)")
    ax.set_ylabel("approximate / exact")
    ax.legend(fontsize=7, frameon=False, loc="upper left")
    fig.tight_layout()
    outp = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_5b.pdf")
    fig.savefig(outp)
    print("wrote", os.path.normpath(outp))
