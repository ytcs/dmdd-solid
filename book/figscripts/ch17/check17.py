"""Chapter 17 revision: the numbers that the revised text quotes and that no other ch17 script prints.
Run: python check17.py  (seconds).  Output: check17.log.  Natural units, energies in eV, speeds in units of c.
Inputs are the book's own values, each with its source in a comment; nothing is fitted.
"""
import os
import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "check17.log"), "w")


def out(s=""):
    print(s)
    LOG.write(s + "\n")


VMAX = 2.650e-3                  # v_esc + v_E of the standard halo (Sect. 1.2)
V0 = 238.0 / 299792.458          # v_0 (Sect. 1.2)
U_GEV = 0.93149410242            # atomic mass unit in GeV
M_SI = 28.0855 * U_GEV * 1e9     # Si atomic mass, eV
HBARC_CM = 1.973269804e-5        # eV cm

# ---- 17.1: free-recoil endpoint at the 89 eV end of the loss-function tables ------------------------------------
def er_max(m):
    mu = m * M_SI / (m + M_SI)
    return 2 * mu**2 * VMAX**2 / M_SI
m89 = brentq(lambda m: er_max(m) - 89.0, 1e7, 1e10)
out("17.1  E_R^max = 2 mu^2 v_max^2/M reaches 89 eV at m = %.1f MeV; E_R^max(300 MeV) = %.1f eV, (500 MeV) = %.1f eV"
    % (m89 / 1e6, er_max(3e8), er_max(5e8)))
# one-phonon against two-or-more phonons of the Poisson weights: 2W e^-2W = 1 - e^-2W - 2W e^-2W  <=>  2x = e^x - 1
x12 = brentq(lambda x: 2 * x - np.expm1(x), 0.5, 3.0)
out("17.1  P(1 phonon) = P(>= 2 phonons) at 2W = %.3f (P1 = P2 at 2W = 2)" % x12)
# nucleon number per mass of the GaAs sublattices (Sect. 8.4, we:8-nucleon): 1.001072 and 1.001046 per u
out("17.1  GaAs nucleon number per mass: Ga 1.001072, As 1.001046 per u (Sect. 8.4); difference %.2e per u (8.4: 2.59e-5)"
    % (1.001072 - 1.001046))

# ---- 17.2: WE handover --------------------------------------------------------------------------------------------
A_SI = 13.297                    # cm^-1 eV^-1/2, onset of the 1s TA replica (abs17_2.log)
FAC = 2.147                      # alpha_GaAs / alpha_Si for equal rate per kg (abs17_2.log)
x10 = (10.0 / (FAC * A_SI))**2
out("17.2  square-root onset alone: 2.147 alpha_Si = 10 cm^-1 at %.1f meV above the replica (full edge of eq:13.8-edge: "
    "40.4 meV, abs17_2.log)" % (x10 * 1e3))
EPS2, W, NR = 2.54e-4, 1.1728, 3.48   # factorized-model eps_2 at 1.1728 eV (abs17_2.log); n_r of GaAs (Skauli)
out("17.2  factorized-model eps_2 = %.3g at %.4f eV with n_r = %.2f: alpha = eps_2 omega/(n_r hbar c) = %.2f cm^-1"
    % (EPS2, W, NR, EPS2 * W / (NR * HBARC_CM)))
out("17.2  Lorentz eps_2 = 4.77e-7 with n_r = 3.48: alpha = %.4f cm^-1" % (4.77e-7 * W / (NR * HBARC_CM)))

# ---- 17.3: endothermic factor for NiO (edge from exo17_3.log, c_M = 1.36e-4) --------------------------------------
for name, edge in (("GaAs LO", 10.35e3), ("NiO magnon", 7.31e3)):
    out("17.3  Si pair floor 0.333 MeV over the %s edge %.2f keV = %.1f" % (name, edge / 1e3, 0.333e6 / edge))
out("17.3  Si pair floor 0.618 MeV at Delta = 1 eV over the GaAs/NiO edges 295/316 keV = %.2f/%.2f" % (618 / 295., 618 / 316.))

# ---- 17.5: CsI floor, diamond-silicon crossing, eta shift, polar log formula, Migdal pole --------------------------
out("17.5  CsI bulk-modulus floor 1.726 km/s over the tabulated 1.379 km/s = %.3f; tabulated/floor = %.3f"
    % (1.726 / 1.379, 1.379 / 1.726))
d = np.load(os.path.join(HERE, "fom17_5_rates.npz"))
m, rs, rc = d["m"], d["Si"], d["C"]
ok = (rs > 0) & (rc > 0)
lr = np.log(rc[ok] / rs[ok])
k = np.where(np.diff(np.sign(lr)) != 0)[0]
mc = np.exp(np.interp(0.0, lr[k[0]:k[0] + 2][::-1], np.log(m[ok][k[0]:k[0] + 2])[::-1]))
out("17.5  diamond and silicon heavy-mediator rates (fom17_5_rates.npz) cross at m = %.1f keV = %.2f Si edges (6.39 keV);"
    " R_C/R_Si at 10 keV = %.2f" % (mc / 1e3, mc / 6.39e3, np.interp(np.log(1e4), np.log(m), rc / rs)))
out("17.5  shift of eta: diamond/Si at 0.3 MeV = 0.9328 (fom17_5.log) -> %.1f %% below the speed ratio" % (100 * (1 - 0.9328)))
wA, wB = 77.2e-3, 36.35e-3       # LiF and GaAs longitudinal energies (Sect. 11.2)
def kratio(mm, v):
    return 1 - np.log(wA / wB) / np.log(2 * mm * v**2 / wB)
for mm in (1e5, 1e6, 1e7):
    out("17.5  asymptotic K ratio LiF/GaAs at %g MeV: v = v_0 %.3f, v = v_max %.3f (full: pol17_5.log)"
        % (mm / 1e6, kratio(mm, V0), kratio(mm, VMAX)))
out("17.5  asymptotic K ratio = 0.9 at m = %.0f MeV (v = v_0), %.1f MeV (v = v_max); full 51.5 MeV (pol17_5.log)"
    % (brentq(lambda mm: kratio(mm, V0) - 0.9, 1e6, 1e10) / 1e6, brentq(lambda mm: kratio(mm, VMAX) - 0.9, 1e5, 1e10) / 1e6))
# Migdal pole factor (eq:17.5-pole) and its dependence on the dispersion of the pole
WP = dict(Si=16.61, LiF=26.06, Ge=15.6)                  # valence plasma frequencies, eV (fom17_5.log; Sect. 10.2)
NUC = dict(Si=16 / 28.0855, LiF=(1 + 49) / 25.939, Ge=16 / 72.63)   # sum N Z_ion^2 / A_cell (Z_ion = 4; 1 and 7; 4)
for x in ("LiF", "Ge"):
    r = NUC[x] / NUC["Si"]
    out("17.5  pole factor %s/Si: nuclear %.3f; dispersionless omega_p^-3: %.3f; Bohm-Gross pole integrated over p "
        "(omega_p^-2): %.3f; free-particle pole omega_pl^2 = omega_p^2 + (p^2/2m)^2 (omega_p^-3/2): %.3f"
        % (x, r, r * (WP["Si"] / WP[x])**3, r * (WP["Si"] / WP[x])**2, r * (WP["Si"] / WP[x])**1.5))
EG = dict(Si=1.17, LiF=14.2)
bL = (WP["Si"]**2 / EG["Si"]**5) / (WP["LiF"]**2 / EG["LiF"]**5)
out("17.5  gap-end bound Si/LiF: L-integral (omega_p^2/E_g^5) ratio %.3g; with the nuclear factor %.3g; (omega_p/E_g)^5 Si = %.3g"
    % (bL, bL * NUC["Si"] / NUC["LiF"], (WP["Si"] / EG["Si"])**5))

# ---- 17.6: X_pole of silicon, offset on TeO2/CaWO4, GaAs polar-rate ratios ----------------------------------------
out("17.6  silicon X_pole ~ 1/(plasmon share of the Migdal probability) = 1/0.04 = %.0f (Sect. 12.3: 4 %%); prior median "
    "sqrt(3) = %.3f" % (1 / 0.04, np.sqrt(3)))
dT = np.log(2.386 / 1.9563)      # TeO2 / CaWO4 heavy-mediator figures of merit (rank17_6.log medians)
s = np.hypot(0.086, 0.02)
out("17.6  TeO2 over CaWO4: Delta = %.4f, sigma = %.4f -> P = %.3f; with the database offset 0.0490 -> P = %.3f"
    % (dT, s, norm.cdf(dT / s), norm.cdf((dT - 0.0490) / s)))
out("17.6  polar rate: LiF 18.99/GaAs 0.1415 = %.0f; sapphire 9.12/0.1415 = %.1f" % (18.99 / 0.1415, 9.12 / 0.1415))
# ---- additions: 17.1 / 17.4 / 17.6 numbers quoted from other logs, combined here ---------------------------------
out("17.1  electron-only acoustic peak at 1 MeV: 4.41e4 (sectors17.log) x elastic pairs 16.73 (exo17_3.log) = %.2e /kg/yr"
    % (4.41e4 * 16.73))
out("17.1  q_max = 2 mu v_max = 18 keV at m = %.2f MeV" % (18e3 / (2 * VMAX) / 1e6))
for name, Z, F in (("Ga", 31, 28.89), ("As", 33, 35.11)):
    out("17.4  %s: (Z^2 + F^2)/Z*^2 = %.0f, Z^2/Z*^2 = %.0f (Z* = 2.11; interf17_4.log)" % (name, (Z**2 + F**2) / 2.11**2, Z**2 / 2.11**2))
out("17.6  pool gaps (rank17_6.py GAPS_TABLE, 1910.10716 Table I): diamond 5.47 (low T), sapphire 8.8, CaWO4 5.2, NaF 11.5,"
    " LiF 14.2 eV (room T)")
out("17.6  DFPT inputs (rank17_6.py DFPT, 1910.10716 Table I): LiF Z* 1.05, eps_inf 2.02, w 77.2 meV; NaF 0.98, 1.78, 49.9 meV")
out("17.2  ZrTe5 zeta at 100 meV: measured-structure row 1.25e-15 against relaxed cell 1.22e-15 (abs17_2.log): %.1f %%"
    % (100 * (1.25 / 1.22 - 1)))
LOG.close()
