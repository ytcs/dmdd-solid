"""Sect. 17.5 (figures of merit per channel): every number printed in Sect. 17.5 except those of Limit Check 17.5a
(limit17_5a.py), Table 17.1 (tab:17-fom), Worked example 17.5 (we:17-window) and Fig. 17.5 (fig:17-window).
Log: fom17_5.log.  Run: python fom17_5.py > fom17_5.log   (a few minutes; the heavy-mediator rates dominate).

Natural units, speeds as fractions of c.  Halo, elastic tensors of Si, Ge, diamond, Christoffel averages and the one-phonon rate
eq:11.1-rate are imported from figscripts/ch11/phon11.py (Sect. 11.1; its docstring gives every source):
  standard halo of Sect. 1.2 (v0 = 238, v_esc = 544, v_E = 250.5 km/s, v_max = 794.5 km/s), rho_chi = 0.3 GeV/cm^3;
  Si C11, C12, C44 = 165.6, 63.9, 79.5 GPa, rho 2.33 g/cm^3; Ge 131, 49, 68 GPa, a = 5.658 A; diamond 1081, 125, 579 GPa, a = 3.567 A.
  Momentum transfers cut at q_BZ = (6 pi^2/Omega)^(1/3); the window of the heavy-mediator ratio is also capped at the smaller
  q_BZ/(2 v_max) of the pair (m_hi), where eq:11.1-Sac stops holding (Sect. 11.1).

Other inputs (each with its source):
  Griffin et al., arXiv:1910.10716, Table I: c_s^LA in units of 1e-5 c: Si 2.84, Ge 1.61, diamond 5.98, GaN 4.17, AlN 5.70,
     ZnO 4.18, CsI 0.46, CaWO4 1.42; band gaps LiF 14.2 eV, diamond 5.47 eV.  Table III: measured lattice constants (A)
     GaN 3.189/5.186, AlN 3.111/4.978, ZnO 3.250/5.207, CaWO4 5.243/11.376, CsI 4.567, LiF 4.020.
  GaN, AlN elastic constants (c11, c12, c13, c33, c44 in GPa), as quoted by Lopuszynski and Majewski, arXiv:1110.1346,
     Table I: "recommended values" of Vurgaftman and Meyer (J. Appl. Phys. 94, 3675 (2003)): AlN 396 137 108 373 116,
     GaN 390 145 106 398 105; "experimental values" of the Madelung handbook: AlN 411 149 99 389 125, GaN 377 160 114 209 81.
  ZnO measured (Brillouin; Carlotti et al. 1995) C11 C12 C33 C13 C44 = 206 118 211 118 44 GPa, as quoted by Gopal and Spaldin,
     arXiv:cond-mat/0507217, Table III, row "measured ZnO".
  CaWO4 (Laue class 4/m) C11 145.9, C33 127.4, C12 62.6, C13 39.2, C16 -19.2 (C26 = -C16), C44 33.5, C66 38.7 GPa:
     Farley and Saunders 1972 (ultrasonic), as quoted by arXiv:2508.08858, p. 16 (its Ref. [73]).
  CsI measured at 4.2 K: C11 27.37, C12 7.93, C44 8.25 GPa (Vallin, Beckman and Salama, J. Appl. Phys. 35, 1222 (1964),
     doi:10.1063/1.1713597; values as given in its abstract).  Room-temperature bulk modulus 13.5 GPa (experiment quoted in
     arXiv:cond-mat/9408044, Table I).  rho_T(CsI) = 4.529 g/cm^3 from a = 4.567 A (room temperature).
  Atomic masses (u, natural): H... Li 6.94, C 12.011, N 14.007, O 15.999, F 18.998, Al 26.982, Si 28.0855, Ca 40.078,
     Zn 65.38, Ga 69.723, Ge 72.63, I 126.904, Cs 132.905, W 183.84.
  Valence densities: Si 2.00e23 cm^-3 (App. A.2), so omega_p^val = 16.6 eV (Sect. 4.3); Ge omega_p^val = 15.6 eV (Sect. 10.6);
     LiF 8 valence electrons per formula unit (Li 2s, F 2s 2p), 4 formula units per cubic cell of 4.020 A.
  Gaps of the book: Si 1.17 eV (physical, low T), 1.11 eV (scissor gap of the tables); Ge 0.744 eV; GaAs 1.52 eV.
  Longitudinal optical energies of the book: GaAs 36.35 meV, LiF 77.2 meV (1910.10716 Table I), sapphire 112.4 meV (Sect. 11.2).
  Small-p ion charges Z_ion: Si 4 (1s2 2s2 2p6 core), Li 1 (1s2), F 7 (1s2), Ge 4 (3d in the core).
"""
import os
import sys
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch11"))
import phon11 as P  # noqa: E402

KMS = P.KMS
U_KG = 1.66053906660e-27
VMAX = P.VMAX
print("halo: v_max = %.1f km/s, eta(0) = 1/(%.1f km/s)" % (P.VMAX_KMS, P.C_KMS / P.ETA0))

# ---------------------------------------------------------------------------------------------------------------------
# 1. Edges and floors (reach figures of merit)
# ---------------------------------------------------------------------------------------------------------------------
print("\n== gap floors 2 E_g / v_max^2 (MeV)")
for nm, eg in (("Si 1.17", 1.17), ("Si 1.11 (tables)", 1.11), ("Ge 0.744", 0.744), ("GaAs 1.52", 1.52),
               ("diamond 5.47", 5.47), ("LiF 14.2", 14.2)):
    print("  %-18s %.4f" % (nm, 2 * eg / VMAX**2 / 1e6))
print("== polar edges 2 omega_L / v_max^2 (keV)")
for nm, wl in (("GaAs", 36.35e-3), ("LiF", 77.2e-3), ("sapphire", 112.4e-3)):
    print("  %-10s %.2f" % (nm, 2 * wl / VMAX**2 / 1e3))

# ---------------------------------------------------------------------------------------------------------------------
# 2. Single phonons: c_NR1, edges, the eta shift
# ---------------------------------------------------------------------------------------------------------------------
av = {nm: P.averages(nm) for nm in ("Si", "Ge", "C")}
print("\n== Christoffel averages (book tensors, 48x96 grid)")
for nm, a in av.items():
    mhi = a["qBZ"] / (2 * VMAX)
    print("  %-2s c_NR1 = %.3f, cbar_LA = %.3f, c_LA,max = %.3f km/s; edge(c_LA,max) = %.2f keV, edge(c_NR1) = %.2f keV;"
          " q_BZ = %.3f keV, m_hi = %.3f MeV" % (nm, a["cNR1"], a["cbarLA"], a["cLAmax"], P.mmin_ac(a["cLAmax"]) / 1e3,
                                                P.mmin_ac(a["cNR1"]) / 1e3, a["qBZ"] / 1e3, mhi / 1e6))
print("  heavy FOM 1/c_NR1 relative to Si: Ge %.3f, C %.3f" % (av["Si"]["cNR1"] / av["Ge"]["cNR1"],
                                                            av["Si"]["cNR1"] / av["C"]["cNR1"]))

I0 = quad(lambda u: u**2 * float(P.eta(u)), 0, VMAX, limit=400, points=[(P.VESC - P.VE) * KMS])[0]
I1 = quad(lambda u: u * float(P.eta(u)), 0, VMAX, limit=400, points=[(P.VESC - P.VE) * KMS])[0]
I2 = quad(lambda u: float(P.eta(u)), 0, VMAX, limit=400, points=[(P.VESC - P.VE) * KMS])[0]
kshift = 2 * I1 / I0
print("\n== eta shift: I0 = %.4e, I1 = %.4e, I2 = %.4e; 2 I1/I0 = %.3f / v_max  (= 1/(%.1f km/s))"
      % (I0, I1, I2, kshift * VMAX, 1 / kshift / KMS))


def large_m_factor(c_kms):
    """Exact large-mass factor of the direction-averaged rate times c_NR1, single speed: int_c^vmax (v-c)^2 eta dv / I0."""
    c = c_kms * KMS
    return quad(lambda v: (v - c)**2 * float(P.eta(v)), c, VMAX, limit=400, points=[(P.VESC - P.VE) * KMS])[0] / I0


for nm, a in av.items():
    c = a["cNR1"]
    print("  %-2s first order 1 - 2 I1 c/I0 = %.4f; to second order %.4f; exact single speed %.4f"
          % (nm, 1 - kshift * c * KMS, 1 - kshift * c * KMS + I2 * (c * KMS)**2 / I0, large_m_factor(c)))
for A, B in (("C", "Si"), ("Ge", "Si"), ("C", "Ge")):
    fa, fb = 1 - kshift * av[A]["cNR1"] * KMS, 1 - kshift * av[B]["cNR1"] * KMS
    print("  pair %s/%s: first-order large-m ratio (R_A/R_B)(c_A/c_B) = %.4f; linearized 1 - 2(I1/I0)(c_A - c_B) = %.4f"
          % (A, B, fa / fb, 1 - kshift * (av[A]["cNR1"] - av[B]["cNR1"]) * KMS))

# heavy-mediator rates on a mass grid
print("\n== heavy-mediator one-phonon rates (sigma_p = 1e-40 cm^2, omega_th = 1 meV, q <= q_BZ)")
plateau = {nm: 2 * P.RHO_CHI * 1e-40 * P.CM2 * I0 / P.M_U**2 * a["inv_eff"] * P.KMS**-1 * P.KG * P.YEAR
           for nm, a in av.items()}
# inv_eff is in (km/s)^-1; convert: 1/c with c in natural units = inv_eff[1/(km/s)] / KMS^-1 ... done above via P.KMS**-1
for nm in av:
    print("  plateau eq:11.1-heavy %-2s %.1f /kg/yr" % (nm, plateau[nm]))
mgrid = np.geomspace(4e3, 0.66e6, 70)
R = {nm: np.array([P.rate_per_mass(m, nm, "heavy", av=av[nm]) for m in mgrid]) for nm in av}
np.savez(os.path.join(HERE, "fom17_5_rates.npz"), m=mgrid, **{k: v for k, v in R.items()},
         cNR1=np.array([av[n]["cNR1"] for n in ("Si", "Ge", "C")]))


def rate(nm, m):
    return P.rate_per_mass(m, nm, "heavy", av=av[nm])


for nm in av:
    frac = R[nm] / plateau[nm]
    i = np.argmax(frac)
    m90 = brentq(lambda m: rate(nm, m) / plateau[nm] - 0.9, mgrid[0], mgrid[i]) if frac.max() > 0.9 else np.nan
    print("  %-2s max R/plateau = %.3f at %.3f MeV; R/plateau = 0.9 at %.1f keV = %.2f edge(c_NR1)"
          % (nm, frac.max(), mgrid[i] / 1e6, m90 / 1e3, m90 / P.mmin_ac(av[nm]["cNR1"])))


def pair_ratio(A, B, m):
    return rate(A, m) / rate(B, m) * av[A]["cNR1"] / av[B]["cNR1"]


print("\n== pairwise windows W_AB: contiguous range with |(R_A/R_B)(c_A/c_B) - 1| < 0.1, capped at min(m_hi)")
for A, B in (("C", "Si"), ("Ge", "Si"), ("C", "Ge")):
    with np.errstate(divide="ignore", invalid="ignore"):
        r = R[A] / R[B] * av[A]["cNR1"] / av[B]["cNR1"]
    mcap = min(av[A]["qBZ"], av[B]["qBZ"]) / (2 * VMAX)
    ok = np.abs(r - 1) < 0.1
    print("  %s/%s: cap m_hi = %.3f MeV" % (A, B, mcap / 1e6))
    for m_, r_ in zip(mgrid, r):
        if m_ in mgrid[::5]:
            print("      m = %8.2f keV  ratio = %.4f" % (m_ / 1e3, r_))
    # lower crossing
    idx = np.where(ok & (mgrid <= mcap))[0]
    if len(idx) == 0:
        print("    no window below the cap")
        continue
    j = idx[0]
    lo = brentq(lambda m: abs(pair_ratio(A, B, m) - 1) - 0.1, mgrid[j - 1], mgrid[j]) if j > 0 else mgrid[0]
    # upper end: first exit above lo, or the cap
    seg = idx[idx >= j]
    breaks = np.where(np.diff(seg) > 1)[0]
    jend = seg[breaks[0]] if len(breaks) else seg[-1]
    if jend + 1 < len(mgrid) and mgrid[jend + 1] <= mcap and not ok[jend + 1]:
        hi = brentq(lambda m: abs(pair_ratio(A, B, m) - 1) - 0.1, mgrid[jend], mgrid[jend + 1])
    else:
        hi = mcap
    rcap = pair_ratio(A, B, mcap)
    softer = A if av[A]["cNR1"] < av[B]["cNR1"] else B
    print("    W = %.1f keV - %.3f MeV; lower end = %.2f x edge(c_NR1) of the softer (%s, %.2f keV); ratio at the cap %.4f;"
          " min/max ratio inside W: %.4f / %.4f"
          % (lo / 1e3, hi / 1e6, lo / P.mmin_ac(av[softer]["cNR1"]), softer, P.mmin_ac(av[softer]["cNR1"]) / 1e3, rcap,
             r[(mgrid >= lo) & (mgrid <= hi)].min(), r[(mgrid >= lo) & (mgrid <= hi)].max()))
# WE values at chosen masses
print("\n== WE 17.5 diamond vs silicon at chosen masses")
for m in (10e3, 20e3, 30e3, 45e3, 0.1e6, 0.2e6, 0.3e6, 0.42e6):
    rs, rc = rate("Si", m), rate("C", m)
    print("  m = %6.0f keV: R_Si = %7.1f, R_C = %7.1f /kg/yr; R_C/R_Si = %.4f; x c_C/c_Si = %.4f; 1/c ratio = %.4f"
          % (m / 1e3, rs, rc, rc / rs, rc / rs * av["C"]["cNR1"] / av["Si"]["cNR1"], av["Si"]["cNR1"] / av["C"]["cNR1"]))
for nm in ("Si", "C"):
    a = av[nm]
    for m in (20e3, 0.3e6):
        c = a["cNR1"] * KMS
        um = 1e-3 / (2 * m * c)
        print("  %s lower cut u_- = omega_th/(2 m c_NR1) at %.0f keV: %.1f km/s = %.3f v_max" % (nm, m / 1e3, um / KMS, um / VMAX))

# ---------------------------------------------------------------------------------------------------------------------
# 3. Tabulated sound speeds against measured elasticity
# ---------------------------------------------------------------------------------------------------------------------
VOIGT = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (1, 2): 3, (2, 1): 3, (0, 2): 4, (2, 0): 4, (0, 1): 5, (1, 0): 5}


def tensor(Cv):
    C = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    C[i, j, k, l] = Cv[VOIGT[(i, j)], VOIGT[(k, l)]]
    return C


def hexagonal(c11, c12, c13, c33, c44):
    Cv = np.zeros((6, 6))
    Cv[0, 0] = Cv[1, 1] = c11
    Cv[2, 2] = c33
    Cv[0, 1] = Cv[1, 0] = c12
    Cv[0, 2] = Cv[2, 0] = Cv[1, 2] = Cv[2, 1] = c13
    Cv[3, 3] = Cv[4, 4] = c44
    Cv[5, 5] = (c11 - c12) / 2
    return Cv


def cubic(c11, c12, c44):
    Cv = np.zeros((6, 6))
    for i in range(3):
        Cv[i, i] = c11
        Cv[i + 3, i + 3] = c44
    for i in range(3):
        for j in range(3):
            if i != j:
                Cv[i, j] = c12
    return Cv


def tetragonal_4m(c11, c33, c12, c13, c16, c44, c66):
    Cv = np.zeros((6, 6))
    Cv[0, 0] = Cv[1, 1] = c11
    Cv[2, 2] = c33
    Cv[0, 1] = Cv[1, 0] = c12
    Cv[0, 2] = Cv[2, 0] = Cv[1, 2] = Cv[2, 1] = c13
    Cv[0, 5] = Cv[5, 0] = c16
    Cv[1, 5] = Cv[5, 1] = -c16
    Cv[3, 3] = Cv[4, 4] = c44
    Cv[5, 5] = c66
    return Cv


def stats(Cv, rho_gcc):
    assert np.linalg.eigvalsh(Cv).min() > 0, "not positive definite"
    c, ev = P.christoffel(tensor(Cv), rho_gcc * 1e3)
    proj2 = np.einsum("ni,nik->nk", P.QH, ev)**2
    return dict(min=c[:, 2].min(), max=c[:, 2].max(), mean=np.sum(P.WQ * c[:, 2]),
                cNR1=1 / np.sum(P.WQ * (proj2 / c).sum(1)), mineig=np.linalg.eigvalsh(Cv).min())


def rho_wurtzite(a, c, mfu):
    return 2 * mfu * U_KG / (np.sqrt(3) / 2 * a**2 * c * 1e-30) / 1e3


GR = 1e-5 * P.C_KMS     # Griffin et al. unit, km/s
mass = dict(Li=6.94, N=14.007, O=15.999, F=18.998, Al=26.982, Ca=40.078, Zn=65.38, Ga=69.723, I=126.904, Cs=132.905,
            W=183.84)
cases = [
    ("GaN rec.", hexagonal(390, 145, 106, 398, 105), rho_wurtzite(3.189, 5.186, mass["Ga"] + mass["N"]), 4.17),
    ("GaN expt.", hexagonal(377, 160, 114, 209, 81), rho_wurtzite(3.189, 5.186, mass["Ga"] + mass["N"]), 4.17),
    ("AlN rec.", hexagonal(396, 137, 108, 373, 116), rho_wurtzite(3.111, 4.978, mass["Al"] + mass["N"]), 5.70),
    ("AlN expt.", hexagonal(411, 149, 99, 389, 125), rho_wurtzite(3.111, 4.978, mass["Al"] + mass["N"]), 5.70),
    ("ZnO meas.", hexagonal(206, 118, 118, 211, 44), rho_wurtzite(3.250, 5.207, mass["Zn"] + mass["O"]), 4.18),
    ("CaWO4", tetragonal_4m(145.9, 127.4, 62.6, 39.2, -19.2, 33.5, 38.7),
     4 * (mass["Ca"] + mass["W"] + 4 * mass["O"]) * U_KG / (5.243**2 * 11.376 * 1e-30) / 1e3, 1.42),
    ("CsI 4.2 K", cubic(27.37, 7.93, 8.25), 4.529, 0.46),
]
print("\n== 1910.10716 Table I c_LA against measured elasticity (km/s)")
res = {}
for nm, Cv, rho, cg in cases:
    s = stats(Cv, rho)
    res[nm] = s
    cgk = cg * GR
    print("  %-10s rho %.3f g/cm3; LA min %.2f, mean %.2f, max %.2f; c_NR1 %.2f; min eig %.1f GPa; table %.3f km/s"
          " = %.3f x max, %.3f x min, %.3f x mean" % (nm, rho, s["min"], s["mean"], s["max"], s["cNR1"], s["mineig"], cgk,
                                                    cgk / s["max"], cgk / s["min"], cgk / s["mean"]))
B_cs_rt = 13.5
Bm = (27.37 + 2 * 7.93) / 3
for lab, B in (("RT B = 13.5 GPa", B_cs_rt), ("4.2 K tensor B = %.2f GPa" % Bm, Bm)):
    fl = np.sqrt(B * 1e9 / 4529) / 1e3
    print("  CsI floor sqrt(B/rho) with %s: %.3f km/s; table 1.379 km/s is %.1f %% below it" % (lab, fl, 100 * (1 - 0.46 * GR / fl)))
print("  CsI Zener ratio %.3f" % (2 * 8.25 / (27.37 - 7.93)))
for nm in ("CaWO4", "CsI 4.2 K"):
    s = res[nm]
    print("  %s heavy FOM 1/c_NR1 relative to Si: %.2f; acoustic edge (c_LA,max) %.1f keV"
          % (nm, av["Si"]["cNR1"] / s["cNR1"], P.mmin_ac(s["max"]) / 1e3))
print("  Si: table %.2f km/s vs cbar_LA %.3f (%.1f %%)" % (2.84 * GR, av["Si"]["cbarLA"], 100 * (2.84 * GR / av["Si"]["cbarLA"] - 1)))

# ---------------------------------------------------------------------------------------------------------------------
# 4. Migdal plasmon-pole factor
# ---------------------------------------------------------------------------------------------------------------------
HBARC_CM = 1.973269804e-5
ME = 0.51099895e6
E2 = 4 * np.pi / 137.035999


def wp(n_cm3):
    return np.sqrt(E2 * n_cm3 * HBARC_CM**3 / ME)


n_lif = 4 * 8 / (4.020e-8)**3
print("\n== Migdal pole factor")
print("  Si omega_p^val = %.2f eV (n = 2.00e23); LiF n_val = %.3e cm^-3, omega_p^val = %.2f eV" % (wp(2.00e23), n_lif, wp(n_lif)))
A_si, A_lif, A_ge = 28.0855, mass["Li"] + mass["F"], 72.63
nf = {"Si": 16 / A_si, "LiF": (1 + 49) / A_lif, "Ge": 16 / A_ge}
w = {"Si": 16.6, "LiF": wp(n_lif), "Ge": 15.6}
eg = {"Si": 1.17, "LiF": 14.2, "Ge": 0.744}
for k in nf:
    print("  %-3s sum Z_ion^2/A_cell = %.4f, pole factor (pi/2) w^-3 = %.4e eV^-3, product %.4e; f-sum bound (pi/2) w^2/Eg^5 = %.3e"
          % (k, nf[k], np.pi / 2 * w[k]**-3, nf[k] * np.pi / 2 * w[k]**-3, np.pi / 2 * w[k]**2 / eg[k]**5))
print("  LiF/Si: nuclear factor %.3f, pole ratio Q(Si)/Q(LiF) = %.3f, net %.3f; bound ratio (Si/LiF) %.3e"
      % (nf["LiF"] / nf["Si"], (w["LiF"] / w["Si"])**3, nf["LiF"] / nf["Si"] / (w["LiF"] / w["Si"])**3,
         (w["Si"]**2 / eg["Si"]**5) / (w["LiF"]**2 / eg["LiF"]**5)))
print("  Ge/Si: nuclear factor %.3f, pole %.3f, net %.3f" % (nf["Ge"] / nf["Si"], (w["Si"] / w["Ge"])**3,
                                                         nf["Ge"] / nf["Si"] * (w["Si"] / w["Ge"])**3))
print("  bound/pole for Si: (w/Eg)^5 = %.3e" % ((16.6 / 1.17)**5))

# ---------------------------------------------------------------------------------------------------------------------
# 5. A soft cubic crystal in the pairwise comparison: CsI with its measured 4.2 K tensor (simple cubic, two atoms per cell)
# ---------------------------------------------------------------------------------------------------------------------
P.MATS["CsI"] = (27.37, 7.93, 8.25, 4.567, (mass["Cs"] + mass["I"]) / 2, 2)
acs = P.averages("CsI")
acs["qBZ"] = (6 * np.pi**2 / (4.567e-10)**3)**(1 / 3) * 1e-10 * P.ANG**-1     # primitive cell = cubic cell, Omega = a^3
av["CsI"] = acs
print("\n== CsI (4.2 K tensor, rho %.3f g/cm3): c_NR1 %.3f, c_LA,max %.3f km/s, edge(c_NR1) %.2f keV, q_BZ %.3f keV, m_hi %.3f MeV"
      % (acs["rho"] / 1e3, acs["cNR1"], acs["cLAmax"], P.mmin_ac(acs["cNR1"]) / 1e3, acs["qBZ"] / 1e3,
         acs["qBZ"] / (2 * VMAX) / 1e6))
print("  exact large-m single-speed factor: CsI %.4f, Si %.4f, C %.4f" % (large_m_factor(acs["cNR1"]),
      large_m_factor(av["Si"]["cNR1"]), large_m_factor(av["C"]["cNR1"])))
R["CsI"] = np.array([rate("CsI", m) for m in mgrid])
np.savez(os.path.join(HERE, "fom17_5_rates.npz"), m=mgrid, **{k: v for k, v in R.items()},
         cNR1=np.array([av[n]["cNR1"] for n in ("Si", "Ge", "C", "CsI")]),
         mhi=np.array([av[n]["qBZ"] / (2 * VMAX) for n in ("Si", "Ge", "C", "CsI")]))
for A, B in (("CsI", "Si"), ("C", "CsI")):
    with np.errstate(divide="ignore", invalid="ignore"):
        r = R[A] / R[B] * av[A]["cNR1"] / av[B]["cNR1"]
    mcap = min(av[A]["qBZ"], av[B]["qBZ"]) / (2 * VMAX)
    sel = (mgrid <= mcap) & np.isfinite(r)
    ok = sel & (np.abs(r - 1) < 0.1)
    print("  %s/%s: cap %.3f MeV; ratio at 0.1, 0.2, cap: %.4f %.4f %.4f; |r-1| < 0.1 on %s"
          % (A, B, mcap / 1e6, pair_ratio(A, B, 0.1e6), pair_ratio(A, B, 0.2e6), pair_ratio(A, B, mcap),
             "none of the grid" if not ok.any() else "%.1f-%.1f keV (grid)" % (mgrid[ok].min() / 1e3, mgrid[ok].max() / 1e3)))
    if ok.any():
        j = np.where(ok)[0][0]
        lo = brentq(lambda m: abs(pair_ratio(A, B, m) - 1) - 0.1, mgrid[j - 1], mgrid[j])
        print("    lower end %.1f keV" % (lo / 1e3))
    print("    max over m <= cap of the ratio: %.4f, min %.4f" % (np.nanmax(r[sel & (mgrid > 50e3)]), np.nanmin(r[sel & (mgrid > 50e3)])))
    ok_idx = np.where(ok)[0]
    jlast = ok_idx[-1]
    if jlast + 1 < len(mgrid) and mgrid[jlast + 1] <= mcap and np.isfinite(r[jlast + 1]):
        hi = brentq(lambda m: abs(pair_ratio(A, B, m) - 1) - 0.1, mgrid[jlast], mgrid[jlast + 1])
        print("    upper end %.1f keV (the ratio leaves the 10 %% band below the cap)" % (hi / 1e3))
    else:
        print("    upper end = cap %.1f keV" % (mcap / 1e3))
