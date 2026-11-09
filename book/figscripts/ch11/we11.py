"""Numbers of Sect. 11.1 not printed by the figure scripts: worked examples 11.1 and 11.2, the heavy-mediator plateau and its
window, the opening estimate, the Rayleigh bound and the Debye temperatures. Inputs and sources: phon11.py.
1910.10716 Table I sound speeds (c_s^LA in units of 1e-5 c): Si 2.84, Ge 1.61, diamond 5.98.
1901.07569 Table I and 2008.08560 Table I: Theta_D = 2220 (C), 645 (Si), 374 (Ge) K; c_s = 13360, 5880, 3550 m/s.
Run: python we11.py
"""
import os
import sys
import numpy as np
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phon11 as P  # noqa: E402

av = {nm: P.averages(nm) for nm in ("Si", "Ge", "C")}
si = av["Si"]

# opening estimate
m = 1e5
q = 2 * m * P.VMAX
M = 28.0855 * P.M_U
print("opening: m = 100 keV, q_max = %.3f keV, q^2/2M = %.2f micro-eV, c_LA q (c = 9.017 km/s, q = 2m(v_max - c)) = %.1f meV"
      % (q / 1e3, q**2 / (2 * M) * 1e6, si["cbarLA"] * P.KMS * 2 * m * (P.VMAX - si["cbarLA"] * P.KMS) * 1e3))
print("F_N: q R at 5 keV with R = 3.47 fm: %.1e" % (5e3 * 3.47e-15 / 1.973269804e-7))

# WE 11.1: silicon c_bar_LA
c11, c12, c44 = 165.6, 63.9, 79.5
rho = 2.33e3
for lab, num in (("[100]", c11), ("[110]", (c11 + c12 + 2 * c44) / 2), ("[111]", (c11 + 2 * c12 + 4 * c44) / 3)):
    print("WE 11.1: %s rho c_LA^2 = %.2f GPa, c_LA = %.3f km/s" % (lab, num, np.sqrt(num * 1e9 / rho) / 1e3))
for nt, nph in ((6, 12), (12, 24), (24, 48), (48, 96)):
    qh, wq = P.sphere_grid(nt, nph)
    c, _ = P.christoffel(P.ctensor(c11, c12, c44), rho, qh)
    print("WE 11.1: grid %2d x %2d (%4d directions): <c_LA> = %.4f km/s" % (nt, nph, nt * nph, np.sum(wq * c[:, 2])))
# closed-form check: first-order average, rho c_LA^2 = C11 - 2 Delta s, <s> = 1/5
D = c11 - c12 - 2 * c44
print("WE 11.1: Delta = %.1f GPa; first-order <rho c^2> = C11 - 2 Delta/5 = %.2f GPa -> sqrt = %.3f km/s; "
      "isotropic-Voigt v_L = %.3f; 1/<1/c_LA> = %.3f; eff. speed 1/<sum (q.e)^2/c> = %.3f; c_LA min/max = %.3f/%.3f"
      % (D, c11 - 2 * D / 5, np.sqrt((c11 - 2 * D / 5) * 1e9 / rho) / 1e3, si["vLV"], 1 / si["inv_LA"], si["cNR1"], si["cLAmin"], si["cLAmax"]))
for nm, tab in (("Si", 2.84), ("Ge", 1.61), ("C", 5.98)):
    ct = tab * 1e-5 * P.C_KMS
    print("1910.10716 Table I %s: c_LA = %.3f km/s vs c_bar_LA = %.3f (%.1f %%)" % (nm, ct, av[nm]["cbarLA"], 100 * (ct / av[nm]["cbarLA"] - 1)))

# Rayleigh bound and Debye temperatures
for nm, td, cs in (("Si", 645, 5880), ("Ge", 374, 3550), ("C", 2220, 13360)):
    a = av[nm]
    print("%s: B = %.1f GPa, sqrt(B/rho) = %.3f km/s (%.0f %% below c_LA,min %.3f); Theta_D exact %.0f K (cbar %.3f), "
          "Hill %.0f (V %.0f, R %.0f), quoted %d K (%.1f %%); cbar vs quoted c_s %.0f m/s: %.1f %%"
          % (nm, a["B"], a["rayleigh"], 100 * (1 - a["rayleigh"] / a["cLAmin"]), a["cLAmin"], a["ThetaD"], a["cDebye"],
             a["ThetaDH"], a["ThetaDV"], a["ThetaDR"], td, 100 * (a["ThetaDH"] / td - 1), cs, 100 * (a["cDebye"] * 1e3 / cs - 1)))
print("Si acoustic-only (primitive-cell) convention: Theta_D / 2^(1/3) = %.0f K" % (si["ThetaD"] / 2**(1 / 3)))

# WE 11.2: light-mediator correction at 3 m_min^ac (silicon, effective speed)
mm = P.mmin_ac(si["cNR1"])
print("WE 11.2: m_min^ac(8.956 km/s, 1 meV) = %.3f keV; with c_LA,max %.3f keV" % (mm / 1e3, P.mmin_ac(si["cLAmax"]) / 1e3))
kap = P.kappa_eta(P.VMAX - si["cNR1"] * P.KMS)
for x in (3.0, 10.0, 44.0, 100.0):
    mx = x * mm
    full = P.rate_per_mass(mx, "Si", "light", av=si) / P.light_leading(mx)
    print("WE 11.2: x = %5.1f (m = %.1f keV): R/R_lead = %.4f; first order (kappa %.3f) %.4f; q range %.0f-%.0f eV"
          % (x, mx / 1e3, full, kap, 1 - (1 + kap) / x, 1e-3 / (si["cNR1"] * P.KMS), 2 * mx * (P.VMAX - si["cNR1"] * P.KMS)))
print("WE 11.2: light leading rate at 19.2 keV, sigma_p = 1e-45 cm^2: %.3e events/kg/yr" % P.light_leading(3 * mm, sigp=1e-45))

# heavy-mediator plateau: R = 2 rho sigma_p / m_u^2 <sum (q.e)^2/c> I0 for m << m_p, I0 = int_0^vmax u^2 eta(u) du
I0 = quad(lambda u: u**2 * float(P.eta(u)), 0, P.VMAX, limit=400)[0]
print("I0 = %.4e (natural units); eta0 v_max^3/3 = %.4e" % (I0, P.ETA0 * P.VMAX**3 / 3))
for nm in ("Si", "Ge", "C"):
    a = av[nm]
    plat = 2 * P.RHO_CHI * 1e-40 * P.CM2 / P.M_U**2 * a["inv_eff"] / P.KMS * I0 * P.KG * P.YEAR
    ms = np.logspace(np.log10(1.05 * P.mmin_ac(a["cLAmax"])), np.log10(a["qBZ"] / (2 * P.VMAX)), 16)
    R = np.array([P.rate_per_mass(mx, nm, "heavy", av=a) for mx in ms]) * (np.array([P.mu(mx, P.M_P) for mx in ms]) / ms)**2
    ok = ms[R / plat >= 0.9]
    mmn = P.mmin_ac(a["cNR1"])
    print("%s heavy plateau (m << m_p, sigma_p = 1e-40): %.1f events/kg/yr; first m with R >= 0.9 plateau: %s (x %s); "
          "largest R/plateau below m_hi %.3f; m_hi = %.3f MeV"
          % (nm, plat, ("%.1f keV" % (ok.min() / 1e3)) if len(ok) else "none", ("%.2f" % (ok.min() / mmn)) if len(ok) else "-",
             (R / plat).max(), a["qBZ"] / (2 * P.VMAX) / 1e6))
print("heavy Ge/Si plateau = %.3f; C/Si = %.3f" % (av["Si"]["cNR1"] / av["Ge"]["cNR1"], av["Si"]["cNR1"] / av["C"]["cNR1"]))
