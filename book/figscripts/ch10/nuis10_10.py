"""Sect. 10.10: the electronic nuisances of silicon and Worked example 10.10 (nuisance band at m_chi = 3 MeV).
Prints every number of the section; no figure.  Runs in a few seconds.

Inputs (all reused, nothing recomputed from first principles)
  rate10_2.py          constants, standard halo (rho_chi = 0.3 GeV/cm^3, v0 = 238, v_esc = 544, v_E = 250.5 km/s),
                       eta of App. D.1 and the loss-function rate eq:10.2-rate.
  si_elf_binned.npz    the silicon GPAW tables of Knapen, Kozaczuk and Lin (arXiv:2101.08275) via DarkELF: IP eps2 of the
                       head, RPA and RPA + LF loss functions, direction-averaged in 100 eV bins of |q|, q <= 22.5 keV,
                       omega <= 89 eV, scissor to the measured T = 0 gap, 1.17 eV (arXiv:2101.08275 Sect. III B;
                       the 1.11 eV of the DarkELF constants file is the step-model conversion constant, not this gap).
  si_fcrys.py          the crystal form factor tabulated by Essig et al. (arXiv:1509.01598), PBE + scissor to 1.11 eV,
                       onset 1.2 eV, q <= 18 q0, omega <= 50 eV (normalization of Sect. 10.1).
Sizes taken from earlier sections (quoted, not recomputed here)
  BSE step on L near the edge: +0.27 to +0.29 from the onset to 3.5 eV (model of Fig. 10.4, |q| = 0.91 keV), coupling
     block about 10 percent of the proper eps2 (Sect. 10.5, estimate).
  Gap: G0W0 - LDA corrections 0.53-0.64 eV across conduction states, scissor accuracy about 0.1 eV in Si (Sect. 3.4).
  Exciton binding 14.7 meV; total line weight = free continuum within 8.0 E_x^b of the edge (Sect. 10.5).

Modelling choices of this script (also stated in the text)
  * Central value: RPA + LF tables as published (their scissor already gives the low-temperature gap 1.17 eV), counted
    from omega >= 1.17 eV.  (A former 0.06 eV shift double-counted the cold gap and is removed.)
  * Excitonic nuisance RPA + LF -> BSE: normalization-like template delta_X = +0.28 over the window (omega <= 10.5 eV at
    3 MeV), the midpoint of the model's 0.27-0.29; coupling-block uncertainty +-0.10 on it (estimate).
  * Gap nuisance: delta E = 0.10 eV (non-rigid quasiparticle shift), applied as S(q, omega - dE) with the threshold
    moving with it.
  * Large-q local fields: template = (RPA - LF)/LF restricted to q > 2 q0, i.e. theta = 1 removes the local-field
    suppression above 2 q0 (the size that is not settled); shown for heavy and light mediators.
  * Table spread in a fixed approximation: IP from the two tables (Essig vs Knapen-Kozaczuk-Lin), same halo, same threshold
    convention (each table's own onset).
  * Band: power form eq:8.8-M, independent nuisances, sigma_ln = ln(1 + delta) added in quadrature (eq:C.14-quadrature).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rate10_2 as R  # noqa: E402

d = R.load()
q, om = d["q"], d["omega"]
EG_TAB = EG_PHYS = 1.17          # tables' gap = measured T = 0 gap
DSHIFT = 0.0


def spec_shift(m, resp, light=False, dE=0.0, dq_cut=None):
    """dR/domega [per kg yr eV] at sigma_e = 1e-37 cm^2 with the table spectrum shifted up by dE (threshold form),
    integrated from the shifted gap.  dq_cut = (qlo, qhi) restricts the q integral."""
    w = np.arange(EG_TAB + dE, om[-1] + dE, 0.01)
    r = d[resp]
    rf = np.array([np.interp(w - dE, om, r[:, j], left=0.0) for j in range(len(q))]).T
    W, Q = np.meshgrid(w, q, indexing="ij")
    integ = Q**3 * R.eta(W / Q + Q / (2 * m)) * R.fdm2(Q, light) * rf
    if dq_cut is not None:
        integ = np.where((Q >= dq_cut[0]) & (Q < dq_cut[1]), integ, 0.0)
    return w, R.to_per_kg_yr(np.trapezoid(integ, q, axis=1) * R.prefactor(m))


def tot(m, resp, light=False, dE=0.0, dq_cut=None, wmax=None):
    w, s = spec_shift(m, resp, light, dE, dq_cut)
    if wmax is not None:
        s = np.where(w <= wmax, s, 0.0)
    return np.trapezoid(s, w)


# ---- gate: reproduce Sect. 10.2 -----------------------------------------------------------------------------------
print("Gate against Sect. 10.2 (10 MeV, heavy, threshold 1.11 eV, per kg-yr at 1e-37 cm^2):")
g = {k: R.total(10e6, k, d) for k in ("ip", "rpa", "lf")}
gl = {k: R.total(10e6, k, d, light=True) for k in ("ip", "rpa", "lf")}
print("  IP %.3g  RPA %.3g  RPA+LF %.3g ; RPA/LF heavy %.2f light %.2f ; IP/LF heavy %.2f light %.2f"
      % (g["ip"], g["rpa"], g["lf"], g["rpa"] / g["lf"], gl["rpa"] / gl["lf"], g["ip"] / g["lf"], gl["ip"] / gl["lf"]))
assert abs(g["ip"] / 1.36e5 - 1) < 0.005 and abs(g["rpa"] / 8.6e4 - 1) < 0.01 and abs(g["lf"] / 5.9e4 - 1) < 0.01
assert round(g["rpa"] / g["lf"], 2) == 1.46 and round(gl["rpa"] / gl["lf"], 2) == 1.27
# own integrator at dE = 0 agrees with rate10_2
assert abs(tot(10e6, "lf") / g["lf"] - 1) < 0.01

# ---- IP, RPA, RPA + LF at 3 MeV -------------------------------------------------------------------------------------
M = 3e6
wmax_kin = 0.5 * M * R.VMAX**2
print("\nm_chi = 3 MeV: largest energy deposited %.2f eV; largest q 2 m v_max = %.1f keV" % (wmax_kin, 2 * M * R.VMAX / 1e3))
for light in (False, True):
    lab = "light" if light else "heavy"
    t = {k: tot(M, k, light) for k in ("ip", "rpa", "lf")}
    print("  %s, from the tables' gap 1.17 eV: IP %.3g  RPA %.3g  RPA+LF %.3g ; steps IP->RPA %.3f, RPA->LF %.3f ; IP/LF %.2f"
          % (lab, t["ip"], t["rpa"], t["lf"], t["rpa"] / t["ip"] - 1, t["lf"] / t["rpa"] - 1, t["ip"] / t["lf"]))

# ---- central value with the physical gap ------------------------------------------------------------------------
print("\nCentral value: RPA + LF from the tables' gap 1.17 eV (no shift, %.2f eV):" % DSHIFT)
cen = {}
for light in (False, True):
    lab = "light" if light else "heavy"
    r0 = tot(M, "lf", light)
    r1 = tot(M, "lf", light, dE=DSHIFT)
    cen[light] = r1
    w, s = spec_shift(M, "lf", light, dE=DSHIFT)
    mean = np.trapezoid(w * s, w) / np.trapezoid(s, w)
    below3 = np.trapezoid(np.where(w < 3.0, s, 0), w) / np.trapezoid(s, w)
    print("  %s: %.3g -> %.3g (central), change %.3f ; mean omega %.2f eV ; share below 3 eV %.2f"
          % (lab, r0, r1, r1 / r0 - 1, mean, below3))

# ---- gap nuisance -------------------------------------------------------------------------------------------------
print("\nGap nuisance, dE = +-0.10 eV about the physical gap:")
dgap = {}
for light in (False, True):
    lab = "light" if light else "heavy"
    up = tot(M, "lf", light, dE=DSHIFT + 0.10) / cen[light] - 1
    dn = tot(M, "lf", light, dE=DSHIFT - 0.10) / cen[light] - 1
    dgap[light] = (up, dn)
    print("  %s: +0.10 eV -> %.3f ; -0.10 eV -> %+.3f" % (lab, up, dn))
for m in (10e6,):
    c = tot(m, "lf", False, dE=DSHIFT)
    print("  (10 MeV heavy for comparison: +0.10 eV -> %.3f)" % (tot(m, "lf", False, dE=DSHIFT + 0.10) / c - 1))
for light in (False, True):
    print("  %s: measured edge, +-5 meV -> %+.4f" % ("light" if light else "heavy",
          tot(M, "lf", light, dE=DSHIFT + 0.005) / cen[light] - 1))
print("  central heavy per kg-day: %.1f" % (cen[False] / 365.25))
mmin = lambda eg: 2 * eg / R.VMAX**2 / 1e6
print("  threshold mass 2 E_g/v_max^2: %.3f MeV (1.11), %.3f MeV (1.17); 0.1 eV = %.1f %% of 1.17 eV"
      % (mmin(1.11), mmin(1.17), 10 / 1.17))

# ---- large-q local fields -----------------------------------------------------------------------------------------
print("\nLarge-q local fields (q > 2 q0 = %.2f keV):" % (2 * R.Q0 / 1e3))
dlq = {}
for m in (3e6, 10e6):
    for light in (False, True):
        lab = "light" if light else "heavy"
        sh = DSHIFT if m == 3e6 else 0.0
        full = tot(m, "lf", light, dE=sh)
        hi_lf = tot(m, "lf", light, dE=sh, dq_cut=(2 * R.Q0, 1e9))
        hi_rpa = tot(m, "rpa", light, dE=sh, dq_cut=(2 * R.Q0, 1e9))
        delta = (hi_rpa - hi_lf) / full
        if m == 3e6:
            dlq[light] = delta
        print("  %4.0f MeV %s: share of rate from q > 2 q0 %.3f ; removing LF there changes the rate by %+.3f"
              % (m / 1e6, lab, hi_lf / full, delta))

# reconciliation with Limit 10.1a (EPM, 5 eV, 2-2.8 q0): tables at 5 eV
print("\nTables at omega = 5 eV (same quantity as the EPM box of Sect. 10.1):")
j5 = np.argmin(abs(om - 5.0))
for qq in (7.46e3, 8.2e3, 9.0e3, 10.4e3):
    jq = np.argmin(abs(q - qq))
    ip, rpa, lf = d["ip"][j5, jq], d["rpa"][j5, jq], d["lf"][j5, jq]
    print("  q = %5.2f q0 (%5.0f eV), omega = %.2f eV: LF/IP %.2f  RPA/IP %.2f  LF/RPA %.2f"
          % (q[jq] / R.Q0, q[jq], om[j5], lf / ip, rpa / ip, lf / rpa))
# omega-integrated per-q ratio over 4-6 eV band
band = (om > 4.0) & (om < 6.1)
for qq in (7.46e3, 8.2e3, 10.4e3):
    jq = np.argmin(abs(q - qq))
    print("  q = %5.2f q0, 4-6 eV band: LF/IP %.2f, LF/RPA %.2f"
          % (q[jq] / R.Q0, d["lf"][band, jq].sum() / d["ip"][band, jq].sum(), d["lf"][band, jq].sum() / d["rpa"][band, jq].sum()))

# ---- bound lines (new support) ------------------------------------------------------------------------------------
EXB = 0.0147
wline = 8.0 * EXB
print("\nBound exciton lines: total line weight = free continuum within %.3f eV of the onset (Sect. 10.5)" % wline)
for light in (False, True):
    lab = "light" if light else "heavy"
    w, s = spec_shift(M, "ip", light, dE=DSHIFT)
    frac = np.trapezoid(np.where(w < EG_PHYS + wline, s, 0), w) / np.trapezoid(s, w)
    print("  %s, IP spectrum: share within %.2f eV of the onset %.4f (resolution of the tables 0.2 eV: order of magnitude)"
          % (lab, wline, frac))

# ---- table spread, fixed approx. -----------------------------------------------------------------------------------
from si_fcrys import load as fload, M_CELL, Q0 as Q0F, DE  # noqa: E402
qf, Ef, f2 = fload()
dqf = qf[1] - qf[0]


def essig_total(m, light):
    mu = m * R.ME / (m + R.ME)
    RHO = 0.3e9
    pref = (RHO / m) * 1e-37 * 2.99792458e10 * R.ALPHA * R.ME**2 / mu**2 / M_CELL * 5.609588603e35 * 365.25 * 86400
    vm = Ef[None, :] / qf[:, None] + qf[:, None] / (2 * m)
    F2 = (Q0F / qf) ** 4 if light else np.ones_like(qf)
    integ = dqf / qf[:, None] ** 2 * R.eta(vm) * F2[:, None] * f2
    return pref * integ.sum() * DE


print("\nf-sum ratio of the IP tables at small q (valence, (pi/2) omega_p^2, omega_p = 16.6 eV; KKL to 89 eV):")
for qq in (1138.0, 1972.0, 2569.0, 3743.0):
    j = np.argmin(abs(q - qq))
    print("  KKL q = %.2f q0: %.2f" % (q[j] / R.Q0, np.trapezoid(om * d["ip"][:, j], om) / (np.pi / 2 * 16.6**2)))
print("  (Essig table, Sect. 10.1 / fig10_1.py: 1.1-1.2 at 0.3-0.7 q0, 1.03 at q0)")

print("\nTable spread with independent particles (each table's own onset; same halo):")
spread = {}
for m in (3e6, 10e6):
    for light in (False, True):
        lab = "light" if light else "heavy"
        e = essig_total(m, light)
        k = R.total(m, "ip", d, light)
        spread[(m, light)] = e / k - 1
        print("  %4.0f MeV %s: Essig %.3g  KKL %.3g  ratio %.3f" % (m / 1e6, lab, e, k, e / k))

# ---- the band at 3 MeV -------------------------------------------------------------------------------------------
print("\nNuisance band at 3 MeV (power form, quadrature of ln(1 + delta)):")
for light in (False, True):
    lab = "light" if light else "heavy"
    c = cen[light]
    items = {
        "excitonic LF->BSE": 0.28,
        "gap 0.1 eV": dgap[light][0],
        "large-q LF": dlq[light],
        "table spread": spread[(3e6, light)],
    }
    sig = np.sqrt(sum(np.log(1 + v) ** 2 for v in items.values()))
    for k, v in items.items():
        print("   %-14s delta = %+.3f  ln(1+delta) = %+.3f" % (k, v, np.log(1 + v)))
    print("  %s: central %.3g per kg-yr; 1 sigma factor exp(%.3f) = %.2f ; band %.3g - %.3g"
          % (lab, c, sig, np.exp(sig), c / np.exp(sig), c * np.exp(sig)))
    print("   with the excitonic step at its upper model value +0.49 instead: %.2f"
          % np.exp(np.sqrt(sig**2 - np.log(1.28) ** 2 + np.log(1.49) ** 2)))
    print("   the excitonic nuisance at theta = 1 alone moves the central value to %.3g" % (c * 1.28))
    print("   coupling block +-0.10 on the BSE step: ln(1.38/1.28) = %.3f" % np.log(1.38 / 1.28))
