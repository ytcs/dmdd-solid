"""Shared inputs and functions for Sect. 11.1 (acoustic phonons): halo, elastic tensors, Christoffel averages, one-phonon rates.
Used by fig11_1.py, limit11_1a.py, limit11_1b.py, limit11_1c.py and we11.py. Run directly to print every number of Sect. 11.1.

Sources of every input:
  [B]   Baxter et al., EPJC 81, 907 (2021), arXiv:2105.00599, Table 1: v0 = 238 km/s, v_esc = 544 km/s, |v_E^ref| = 250.5 km/s,
        rho_chi = 0.3 GeV/cm^3 (the book's halo, Sects. 1.2-1.3; eta(v_min) in closed form from App. D.1, as figscripts/ch01/fig1_6.py).
  [M19] Martinez et al., Phys. Rev. Applied 11, 064025 (2019), Table I: Si C11, C12, C44 = 165.6, 63.9, 79.5 GPa, rho = 2.33 g/cm^3
        (the values of App. C.18 and WE 5.3).
  [H26] Haxhijaj et al., arXiv:2601.11177, Table III, rows "Expt.": diamond 1081, 125, 579 GPa; Ge 131, 49, 68 GPa (room temperature,
        not corrected for zero-point expansion; the Ge values are those of Sect. 5.3).
  Lattice constants: Si 5.431 A (Sect. 3.1), Ge 5.658 A (room temperature, Sect. 3.3), diamond 3.567 A (Kurinsky et al., arXiv:1901.07569, Table I).
  Atomic masses (u): C 12.011, Si 28.0855, Ge 72.63 (natural mixtures); mass numbers of the natural mixtures A = M/m_u to 0.1 %.
  m_u = 931.494 MeV; 1 GPa = 1e9 Pa; hbar c = 197.327 MeV fm.
Modelling choices (stated in the text and captions): long-wavelength acoustic branches with the Christoffel speeds and polarizations
of the room-temperature tensor; G = 0; e^{-2W} = 1; nuclear form factor F_N = 1; equal couplings to protons and neutrons,
c_kappa = A_kappa x (nucleon coupling); orientation average of the crystal (so the halo enters through eta, Sect. 1.3);
momentum transfers cut at q_BZ = (6 pi^2/Omega)^(1/3) (sphere of the zone's volume, Omega the primitive-cell volume).
"""
import numpy as np
from scipy.special import erf
from scipy.integrate import quad

# ---- units: eV, natural units; speeds as fractions of c --------------------------------------------------------------
C_KMS = 299792.458
KMS = 1.0 / C_KMS
M_U = 931.494e6                        # eV
HBARC_EV_CM = 1.973269804e-5           # eV cm
GEV_CM3 = 1e9 * HBARC_EV_CM**3         # 1 GeV/cm^3 in eV^4
RHO_CHI = 0.3 * GEV_CM3                # eV^4 [B]
ALPHA = 1 / 137.035999
M_E = 0.51099895e6
Q0 = ALPHA * M_E                       # eV, q0 = alpha m_e = 3.73 keV
M_P = 938.272e6
SEC = 1 / 6.582119569e-16              # 1 s in eV^-1
YEAR = 3.15576e7 * SEC
KG = 5.60958860e35                     # 1 kg in eV
CM2 = 1 / HBARC_EV_CM**2               # 1 cm^2 in eV^-2
ANG = 1e-8 / HBARC_EV_CM               # 1 Angstrom in eV^-1

# ---- halo [B] ------------------------------------------------------------------------------------------------------
V0, VESC, VE = 238.0, 544.0, 250.5     # km/s
VMAX_KMS = VESC + VE                   # 794.5 km/s
VMAX = VMAX_KMS * KMS
_Z = VESC / V0
_NESC = np.pi**1.5 * V0**3 * (erf(_Z) - 2 / np.sqrt(np.pi) * _Z * np.exp(-_Z**2))


def eta_kms(u, ve=VE):
    """eta(v_min) in (km/s)^-1, v_min in km/s (App. D.1, all branches)."""
    k = np.pi * V0**2 / (ve * _NESC)
    u = np.maximum(np.asarray(u, float), 0.0)
    b1 = k * (np.sqrt(np.pi) * V0 / 2 * (erf((u + ve) / V0) - erf((u - ve) / V0)) - 2 * ve * np.exp(-_Z**2))
    b2 = k * (np.sqrt(np.pi) * V0 / 2 * (erf(_Z) - erf((u - ve) / V0)) - (VESC + ve - u) * np.exp(-_Z**2))
    return np.where(u < VESC - ve, b1, np.where(u < VESC + ve, b2, 0.0))


def eta(v):
    """eta in natural units (dimensionless speeds)."""
    return eta_kms(np.asarray(v) * C_KMS) * C_KMS


ETA0 = float(eta(0.0))


def kappa_eta(u_plus=VMAX):
    """kappa_eta = (u+/eta0) int_0^{u+} (eta0 - eta(u)) u^-2 du (Sect. 11.1)."""
    f = lambda u: (ETA0 - float(eta(u))) / u**2 if u > 0 else 0.0
    val = quad(f, 0.0, u_plus, limit=400, points=[(VESC - VE) * KMS])[0]
    return u_plus / ETA0 * val


# ---- materials ----------------------------------------------------------------------------------------------------
MATS = {
    # name: (C11, C12, C44 [GPa], a [A], atomic mass [u], atoms per cubic cell)
    "Si": (165.6, 63.9, 79.5, 5.431, 28.0855, 8),    # [M19]
    "Ge": (131.0, 49.0, 68.0, 5.658, 72.63, 8),      # [H26]
    "C": (1081.0, 125.0, 579.0, 3.567, 12.011, 8),   # [H26]
}
U_KG = 1.66053906660e-27


def density(name):
    """kg/m^3 from the lattice constant; Si uses the tabulated 2.33 g/cm^3 of [M19] (2.329 from a)."""
    C11, C12, C44, a, m, n = MATS[name]
    if name == "Si":
        return 2.33e3
    return n * m * U_KG / (a * 1e-10)**3


def ctensor(C11, C12, C44):
    C = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if i == j == k == l:
                        C[i, j, k, l] = C11
                    elif i == j and k == l:
                        C[i, j, k, l] = C12
                    elif (i == k and j == l) or (i == l and j == k):
                        C[i, j, k, l] = C44
    return C


def sphere_grid(nt=48, nphi=96):
    """Gauss-Legendre in cos(theta) x uniform phi; weights sum to 1 (App. C.18 quadrature)."""
    x, w = np.polynomial.legendre.leggauss(nt)
    ph = (np.arange(nphi) + 0.5) * 2 * np.pi / nphi
    X, P = np.meshgrid(x, ph, indexing="ij")
    W = np.repeat(w[:, None], nphi, axis=1) / (2 * nphi)
    s = np.sqrt(1 - X**2)
    q = np.stack([s * np.cos(P), s * np.sin(P), X], axis=-1).reshape(-1, 3)
    return q, W.reshape(-1)


QH, WQ = sphere_grid()


def christoffel(Cijkl_gpa, rho, qh=QH):
    """Speeds (km/s, ascending: TA1, TA2, LA) and unit polarizations (n,3,3; columns) on directions qh."""
    M = np.einsum("ijkl,nj,nl->nik", Cijkl_gpa * 1e9, qh, qh)
    lam, ev = np.linalg.eigh(M)
    return np.sqrt(lam / rho) / 1e3, ev


def averages(name, qh=QH, wq=WQ):
    C11, C12, C44, a, m, n = MATS[name]
    rho = density(name)
    c, ev = christoffel(ctensor(C11, C12, C44), rho, qh)
    proj2 = np.einsum("ni,nik->nk", qh, ev)**2            # (q.e_nu)^2
    out = dict(rho=rho, c=c, proj2=proj2, wq=wq)
    out["cbarLA"] = np.sum(wq * c[:, 2])                   # <c_LA>
    out["inv_eff"] = np.sum(wq * (proj2 / c).sum(1))       # <sum_nu (q.e)^2 / c_nu>
    out["cNR1"] = 1 / out["inv_eff"]
    out["inv_LA"] = np.sum(wq * 1 / c[:, 2])
    out["cLAmax"] = c[:, 2].max()
    out["cLAmin"] = c[:, 2].min()
    out["cDebye"] = (np.sum(wq * (c**-3).sum(1)) / 3)**(-1 / 3)   # Sect. 5.2, 3/cbar^3 = sum <c^-3>
    B = (C11 + 2 * C12) / 3
    out["B"] = B
    out["rayleigh"] = np.sqrt(B * 1e9 / rho) / 1e3
    out["zener"] = 2 * C44 / (C11 - C12)
    # Voigt, Reuss, Hill shear moduli of a cubic polycrystal; isotropic speeds; mean speed 3/v_m^3 = 1/v_L^3 + 2/v_T^3
    GV = (C11 - C12 + 3 * C44) / 5
    GR = 5 * (C11 - C12) * C44 / (4 * C44 + 3 * (C11 - C12))
    for tag, G in (("V", GV), ("R", GR), ("H", (GV + GR) / 2)):
        vL = np.sqrt((B + 4 * G / 3) * 1e9 / rho) / 1e3
        vT = np.sqrt(G * 1e9 / rho) / 1e3
        vm = (3 / (1 / vL**3 + 2 / vT**3))**(1 / 3)
        out["G" + tag], out["vL" + tag], out["vT" + tag], out["vm" + tag] = G, vL, vT, vm
    nat = n / (a * 1e-10)**3                               # atoms per m^3
    QD = (6 * np.pi**2 * nat)**(1 / 3)                     # 1/m
    HB, KB = 1.054571817e-34, 1.380649e-23
    out["QD_Ainv"] = QD * 1e-10
    out["ThetaD"] = HB * out["cDebye"] * 1e3 * QD / KB
    for tag in "VRH":
        out["ThetaD" + tag] = HB * out["vm" + tag] * 1e3 * QD / KB
    Omega = (a * 1e-10)**3 / 4                             # primitive cell of fcc (two atoms)
    out["qBZ"] = (6 * np.pi**2 / Omega)**(1 / 3) * 1e-10 * ANG**-1   # eV
    out["M_atom"] = m * M_U
    return out


# ---- one-phonon rates per unit target mass ---------------------------------------------------------------------
def mu(a, b):
    return a * b / (a + b)


_GL = {}


def _gl(n):
    if n not in _GL:
        _GL[n] = np.polynomial.legendre.leggauss(n)
    return _GL[n]


def rate_per_mass(mchi, name, med, wth=1e-3, sigp=1e-40, av=None, qcap=True, nq=400):
    """Events per kg per year, orientation-averaged long-wavelength one-phonon rate (Sect. 11.1, eq:11.1-rate).
    med = 'heavy' (F_DM = 1) or 'light' (F_DM = (q0/q)^2); sigma_p in cm^2; wth in eV."""
    av = av or averages(name)
    pref = RHO_CHI * sigp * CM2 / (4 * mchi * mu(mchi, M_P)**2 * M_U**2)
    tot = 0.0
    c = av["c"] * KMS                                       # (n,3)
    qbz = av["qBZ"] if qcap else np.inf
    for nu in range(3):
        cn = c[:, nu]
        qlo = wth / cn
        qhi = np.minimum(2 * mchi * (VMAX - cn), qbz)
        val = np.zeros(len(cn))
        ok = qhi > qlo
        # vectorised Gauss-Legendre in log q between qlo and qhi
        x, w = _gl(nq)
        L0, L1 = np.log(qlo[ok]), np.log(qhi[ok])
        lq = 0.5 * (L1 - L0)[:, None] * x[None, :] + 0.5 * (L1 + L0)[:, None]
        q = np.exp(lq)
        jac = 0.5 * (L1 - L0)[:, None] * q
        fdm2 = 1.0 if med == "heavy" else (Q0 / q)**4
        integrand = q**2 * fdm2 * eta(cn[ok, None] + q / (2 * mchi)) * jac
        val[ok] = (integrand * w[None, :]).sum(1)
        tot += np.sum(av["wq"] * av["proj2"][:, nu] / cn * val)
    return pref * tot * KG * YEAR


def light_leading(mchi, wth=1e-3, sigp=1e-40):
    """Target-independent light-mediator rate per mass (events/kg/yr): rho sigma_p q0^4 eta0 / (4 m mu^2 m_u^2 wth)."""
    return RHO_CHI * sigp * CM2 * Q0**4 * ETA0 / (4 * mchi * mu(mchi, M_P)**2 * M_U**2 * wth) * KG * YEAR


def mmin_ac(c_kms, wth=1e-3):
    c = c_kms * KMS
    return wth / (2 * c * (VMAX - c))


if __name__ == "__main__":
    print("eta(0) = %.1f (natural) = 1/(%.1f km/s);  v_max = %.1f km/s = %.4e" % (ETA0, C_KMS / ETA0, VMAX_KMS, VMAX))
    print("kappa_eta (u+ = v_max) = %.3f;  (u+ = v_max - 9 km/s) = %.3f" % (kappa_eta(), kappa_eta(VMAX - 9 * KMS)))
    print("q0 = %.1f eV" % Q0)
    for nm in MATS:
        a = averages(nm)
        print("\n== %s: rho = %.4f g/cm3, Zener A = %.3f, B = %.1f GPa" % (nm, a["rho"] / 1e3, a["zener"], a["B"]))
        print("  cbar_LA = %.3f, 1/<1/c_LA> = %.3f, c_NR1 = %.3f, c_LA min/max = %.3f/%.3f, Rayleigh sqrt(B/rho) = %.3f km/s"
              % (a["cbarLA"], 1 / a["inv_LA"], a["cNR1"], a["cLAmin"], a["cLAmax"], a["rayleigh"]))
        print("  Debye cbar (5.2) = %.3f km/s, Q_D = %.4f 1/A, Theta_D = %.1f K" % (a["cDebye"], a["QD_Ainv"], a["ThetaD"]))
        for t in "VRH":
            print("  %s: G = %.2f GPa, vL = %.3f, vT = %.3f, vm = %.3f km/s, Theta_D = %.1f K"
                  % (t, a["G" + t], a["vL" + t], a["vT" + t], a["vm" + t], a["ThetaD" + t]))
        print("  q_BZ = %.3f keV; m_hi = q_BZ/(2 v_max) = %.3f MeV" % (a["qBZ"] / 1e3, a["qBZ"] / (2 * VMAX) / 1e6))
        print("  m_min^ac(1 meV): c_LA,max %.2f keV, cbar_LA %.2f keV, c_NR1 %.2f keV"
              % (mmin_ac(a["cLAmax"]) / 1e3, mmin_ac(a["cbarLA"]) / 1e3, mmin_ac(a["cNR1"]) / 1e3))
