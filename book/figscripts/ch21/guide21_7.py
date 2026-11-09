"""Sect. 21.7 (next targets): every number printed in Sect. 21.7, Table 21.2 (tab:21-guide), Fig. 21.6 (fig:21-leaders)
and Worked example 21.7 (we:21-csi).  Log: guide21_7.log.   Run: python guide21_7.py > guide21_7.log  (about 30 s).

Part A. Rankings of the full pool (42 crystals) and of the survivor pool (the 11 crystals of Sect. 17.6), with the
  method, widths, seed and the 11 survivor inputs of figscripts/ch17/rank17_6.py (imported, unchanged).  The 31
  conditional crystals enter with:
  * gaps: Griffin et al. 1910.10716 Table I (asterisk = low temperature; otherwise + U[0.03, 0.10] eV, family dEg);
    SiC polytypes 2.39 (3C), 3.26 (4H), 3.02 eV (6H), room temperature, Griffin et al. 2008.08560 Table I.
  * elastic tensors: JARVIS-DFT (OptB88vdW; Choudhary et al. 1804.01033), Voigt order with the shear constants on
    their axes, sphere averages c_NR1 and c_LA,max on the same grid as rank17_6 (values below, km/s), width 0.086,
    family c_DB; aluminum from its measured 0 K constants (C11 114.3, C12 61.9, C44 31.6 GPa, rho 2.698; width 0.02);
    CsI from its measured 4.2 K constants (Vallin et al. 1964, rank17_6 TENS), width 0.02.
  * polar band integrals I_pol/rho_T (meV cm^3/g) and lowest polar LO energy (meV): diatomic route eq:11.2-diatomic
    with the DFPT Z*, eps_inf, omega_O,max of 1910.10716 Table I (families Z, eps, w as rank17_6), or the geometric
    mean of that route and a same-run database eps pair with the LST relation (same widths); SiC: measured per-axis
    eps pairs and omega_L of 2008.08560 Table I (width 0.04, omega 0.005); CaF2: database eps pair + LST (DFPT widths);
    quartz and MgF2: interval [lo, hi] from one database eps pair (log-uniform), omega_O,min a lower estimate.
  * Migdal: sum Z_ion^2/M_fu, valence plasma energy (eV) and density as listed (MIGC), X_pole as rank17_6.
  * pair energies (ER quanta): measured: Si 3.749 eV (123 K, Rodrigues et al.), Ge 3.37 eV (50 mK fit of Wei, Wang
    and Mei 1602.08005 Sect. 2.1.4, width 0.015 = the 3.32/3.37 spread), GaAs 4.2 eV (room temperature, as quoted by
    Nielsen and Fischetti) + 1.70 x 0.10 eV (book gap shift, slope d eps/d E_g of limit18_4c), width 0.012; diamond
    12.95 eV (four measurements), width 0.012; SiC 6.9 (3C), 7.83 (4H), 6.7 eV (6H), width 0.02; GaN 9.59 eV (EBIC),
    width 0.075.  Estimates: the cascade of Sect. 18.4 at the gaps of 1910.10716 (figscripts/ch18/limit18_4c.log),
    lognormal width 0.105 (rms of the validation residuals) inside the validated range and 0.21 outside it
    (convention), plus 1.70 x U[0.03, 0.10] eV for a room-temperature gap.
Part B. Internal backgrounds below 1 keV: allowed beta shapes with the non-relativistic Fermi function
  F = 2 pi eta / (1 - exp(-2 pi eta)), eta = alpha Z_d E/p (light daughters: 3H, 40K, 115In), and for the heavy daughters of
  210Pb (Z_d = 83) and 210Bi (Z_d = 84) the relativistic point-nucleus Fermi function
  F = 4 (2 p R)^(2g - 2) e^(pi y) |Gamma(g + i y)|^2 / Gamma(2g + 1)^2, g = (1 - (alpha Z_d)^2)^(1/2), y = alpha Z_d W/p
  (W, p in units of m_e, R = 1.2 A^(1/3) fm in units of hbar/m_e c; Hayen et al. arXiv:1709.07530 Eq. (6); a constant prefactor
  cancels in the fraction f below 1 keV);
  unique-n-th-forbidden shape factor
  sum_k p^2k q^2(n-k) / [(2k+1)! (2n-2k+1)!]; decay data from ENSDF via the IAEA Live Chart (sources/21.7/*.csv).
Part C. Fig. 21.6 (leaders per channel, full pool against survivors).
"""
import os
import sys
import math
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch17"))
import rank17_6 as R  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch21")
plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})

S11 = list(R.POOL)
C31 = ["SiC-3C", "SiC-4H", "SiC-6H", "GaN", "AlN", "GaSb", "SiO2-q", "ZnO", "MgO", "NaCl", "NaI", "CsI", "CaF2",
       "MgF2", "ZnS", "PbTe", "PbS", "PbSe", "SrTiO3", "ZrTe5", "Bi2Se3", "Al", "Nb", "YIG", "NiO", "MnO", "Cr2O3",
       "NiPS3", "hBN", "cBN", "PE"]
FULL = S11 + C31

GAPC = {"SiC-3C": (2.39, False), "SiC-4H": (3.26, False), "SiC-6H": (3.02, False), "GaN": (3.43, True),
        "AlN": (6.2, False), "GaSb": (0.72, False), "SiO2-q": (9.2, False), "ZnO": (3.3, False), "MgO": (7.83, False),
        "NaCl": (8.75, False), "NaI": (5.8, False), "CsI": (6.14, False), "CaF2": (11.81, False),
        "MgF2": (12.4, False), "ZnS": (3.8, True), "PbTe": (0.19, True), "PbS": (0.29, True), "PbSe": (0.17, True)}

NRC = {"SiC-3C": (12.167, 13.043, "DB"), "SiC-4H": (12.142, 13.054, "DB"), "SiC-6H": (12.146, 13.055, "DB"),
       "GaN": (7.351, 7.929, "DB"), "AlN": (10.694, 10.980, "DB"), "GaSb": (3.976, 4.199, "DB"),
       "SiO2-q": (6.011, 6.915, "DB"), "ZnO": (5.897, 6.193, "DB"), "MgO": (9.701, 10.061, "DB"),
       "NaCl": (4.793, 5.269, "DB"), "NaI": (2.916, 3.202, "DB"), "CaF2": (6.763, 7.261, "DB"),
       "MgF2": (7.447, 8.271, "DB"), "ZnS": (5.382, 5.747, "DB"), "PbTe": (3.109, 3.848, "DB"),
       "PbS": (3.670, 4.326, "DB"), "PbSe": (3.337, 3.999, "DB"), "SrTiO3": (8.166, 8.217, "DB"),
       "Bi2Se3": (2.861, 3.458, "DB"), "Al": (6.628, 6.711, "meas"), "Nb": (4.899, 5.390, "DB"),
       "NiO": (6.338, 6.466, "DB"), "hBN": (6.800, 19.636, "DB"), "cBN": (16.071, 16.779, "DB"),
       "PE": (4.891, 17.573, "DB")}

# I_pol/rho_T, lowest polar LO energy (meV), interval lo, hi (None = point value), route
POLC = {"SiC-3C": (3.0021, 120.50, None, None, "meas"), "SiC-4H": (2.9072, 119.50, None, None, "meas"),
        "SiC-6H": (2.8642, 119.70, None, None, "meas"), "GaN": (1.6628, 88.90, None, None, "DFPT"),
        "AlN": (5.5661, 109.00, None, None, "DFPT"), "GaSb": (0.0244, 27.30, None, None, "DFPT"),
        "SiO2-q": (5.8907, 13.70, 1.5749, 22.0329, "interval"), "ZnO": (1.3521, 63.40, None, None, "DFPT"),
        "MgO": (7.9806, 82.60, None, None, "DFPT"), "NaCl": (5.7252, 30.60, None, None, "DFPT"),
        "NaI": (1.6514, 20.00, None, None, "DFPT"), "CsI": (0.8662, 10.00, None, None, "DFPT"),
        "CaF2": (8.7845, 57.79, None, None, "DFPT"), "MgF2": (5.1854, 12.10, 1.8796, 14.3055, "interval"),
        "ZnS": (0.9822, 41.00, None, None, "DFPT"), "PbTe": (0.0938, 13.50, None, None, "DFPT"),
        "PbS": (0.3309, 26.40, None, None, "DFPT"), "PbSe": (0.1379, 16.00, None, None, "DFPT")}

MIGC = {"SiC-3C": (0.7981, 23.025, 3.2000, "meas"), "SiC-4H": (0.7981, 23.025, 3.2000, "meas"),
        "SiC-6H": (0.7981, 23.025, 3.2000, "meas"), "GaN": (0.4061, 21.978, 6.0882, "meas"),
        "AlN": (0.8295, 22.995, 3.2625, "meas"), "GaSb": (0.1776, 13.881, 5.5541, "meas"),
        "SiO2-q": (1.4646, 24.203, 2.6492, "meas"), "ZnO": (0.4915, 21.522, 5.6741, "meas"),
        "MgO": (0.9924, 24.308, 3.5851, "meas"), "NaCl": (0.8555, 15.678, 2.1626, "meas"),
        "NaI": (0.3336, 12.755, 3.6709, "meas"), "CsI": (0.1924, 10.761, 4.5291, "meas"),
        "CaF2": (1.3064, 23.265, 3.1807, "meas"), "MgF2": (1.6372, 26.009, 3.1721, "meas"),
        "ZnS": (0.4105, 16.647, 4.0650, "meas"), "PbTe": (0.1553, 14.323, 8.2724, "meas"),
        "PbS": (0.2173, 16.239, 7.5987, "meas"), "PbSe": (0.1817, 15.497, 8.2763, "meas"),
        "SrTiO3": (0.6976, 23.334, 5.0130, "DB"), "ZrTe5": (0.2688, 15.354, 6.0890, "meas"),
        "Bi2Se3": (0.2413, 16.140, 7.3370, "DB"), "Al": (0.3336, 15.782, 2.6978, "meas"),
        "Nb": (0.2691, 19.420, 8.4390, "DB"), "YIG": (1.0556, 26.539, 5.1730, "meas"),
        "NiO": (1.8208, 34.263, 6.6000, "meas"), "MnO": (1.1982, 28.130, 5.2000, "meas"),
        "Cr2O3": (1.1843, 28.339, 4.9000, "meas"), "NiPS3": (1.2536, 22.270, 3.3640, "DB"),
        "hBN": (1.3700, 24.769, 2.2920, "DB"), "cBN": (1.3700, 30.446, 3.4630, "DB"),
        "PE": (1.2833, 19.613, 1.0830, "DB")}

# pair energies: (value eV, kind, width, room-temperature gap?)  kinds: meas, est_in, est_out
DEPS = 1.70  # d eps / d E_g at fixed constant, limit18_4c / table18_4 logs
EPS = {"Si": (3.749, "meas", 0.01, False), "Ge": (3.37, "meas", 0.015, False),
       "GaAs": (4.2 + DEPS * 0.10, "meas", 0.012, False), "C": (12.95, "meas", 0.012, False),
       "SiC-3C": (6.9, "meas", 0.02, False), "SiC-4H": (7.83, "meas", 0.02, False),
       "SiC-6H": (6.7, "meas", 0.02, False), "GaN": (9.59, "meas", 0.075, False),
       "CaWO4": (10.686, "est_in", 0, True), "Al2O3": (16.518, "est_out", 0, True),
       "LiF": (25.045, "est_out", 0, True), "NaF": (20.494, "est_out", 0, True),
       "NaI": (10.910, "est_out", 0, True), "CsI": (11.212, "est_out", 0, True),
       "PbTe": (1.528, "est_out", 0, False), "PbS": (1.924, "est_out", 0, False),
       "PbSe": (1.564, "est_out", 0, False), "AlN": (12.330, "est_in", 0, True),
       "CaF2": (21.047, "est_out", 0, True), "GaSb": (2.673, "est_out", 0, True),
       "MgF2": (22.129, "est_out", 0, True), "MgO": (14.826, "est_out", 0, True),
       "NaCl": (15.841, "est_out", 0, True), "ZnO": (7.320, "est_in", 0, True),
       "ZnS": (7.946, "est_out", 0, False), "SiO2-q": (17.373, "est_in", 0, True)}
W_EST = {"est_in": 0.105, "est_out": 0.21}


def er_floor_full(sm, names):
    S = R.er_floor(sm, [n for n in names if n in S11])
    a, b = sm.W["dEg"]
    for n in names:
        if n in GAPC:
            e0, lowT = GAPC[n]
            E = sm.lnN(e0, sm.W["Eg"])
            if not lowT:
                E = E + sm.U(a, b, "dEg")
            S[n] = R.mfloor(E)
    return S


def er_quanta(sm, names):
    a, b = sm.W["dEg"]
    S = {}
    for n in names:
        if n not in EPS:
            continue
        e0, kind, w, roomT = EPS[n]
        if kind == "meas":
            S[n] = sm.lnN(e0, w)
        else:
            x = sm.lnN(e0, W_EST[kind], "eps_casc")
            if roomT:
                x = x + DEPS * sm.U(a, b, "dEg")
            S[n] = x
    return S


def nr_full(sm, names, which):
    S = R.nr_heavy(sm, [n for n in names if n in S11 or n == "CsI"]) if which == "heavy" else \
        R.nr_edge(sm, [n for n in names if n in S11 or n == "CsI"])
    for n in names:
        if n in NRC:
            cn, cm, prov = NRC[n]
            c0 = cn if which == "heavy" else cm
            cs = sm.lnN(c0, sm.W["c_meas"]) if prov == "meas" else sm.lnN(c0, sm.W["c_DB"], "c_DB")
            S[n] = R.CSI0 / cs if which == "heavy" else R.edge_keV(cs)
    return S


def pol_full(sm, names, which):
    S = R.pol_rate(sm, [n for n in names if n in S11]) if which == "rate" else \
        R.pol_reach(sm, [n for n in names if n in S11])
    for n in names:
        if n not in POLC:
            continue
        I0, w0, lo, hi, route = POLC[n]
        if which == "rate":
            if route == "meas":
                S[n] = sm.lnN(I0, 0.04)
            elif route == "interval":
                S[n] = sm.logU(lo, hi)
            else:
                S[n] = (I0 * np.exp(2 * sm.W["Z_DFPT"] * sm.z("Z_DFPT")) * np.exp(-2 * sm.W["eps_DFPT"] * sm.z("eps_DFPT"))
                        * np.exp(-sm.W["w_DFPT"] * sm.z("w_DFPT")))
        else:
            w = sm.lnN(w0, sm.W["w_meas"]) if route == "meas" else sm.lnN(w0, sm.W["w_DFPT"], "w_DFPT")
            S[n] = 2 * w * 1e-3 / R.VMAX ** 2 / 1e3
    return S


def migdal_full(sm, names):
    S = R.migdal(sm, [n for n in names if n in S11])
    Zs, Z2s, Ms, rhos, _ = R.MIG["Si"]
    ref = Z2s / Ms * R.wp_val(Zs, Ms, rhos) ** -3
    for n in names:
        if n not in MIGC:
            continue
        nuc, wp, rho, prov = MIGC[n]
        wps = wp * (np.exp(0.5 * sm.W["rho_DB"] * sm.z("rho_DB")) if prov == "DB" else 1.0)
        S[n] = nuc * wps ** -3 * sm.logU(*sm.W["Xpole"], fam="Xpole") / ref
    return S


CH = [("ER_floor", "L", "MeV"), ("ER_quanta", "L", "eV"), ("NR_heavy", "H", "F_NR"), ("NR_edge", "L", "keV"),
      ("POL_rate", "H", "meV cm^3/g"), ("POL_reach", "L", "keV"), ("Migdal", "H", "F_Mig")]


def run(names, r):
    sm = R.Sampler(r)
    out = {"ER_floor": er_floor_full(sm, names), "ER_quanta": er_quanta(sm, names),
           "NR_heavy": nr_full(sm, names, "heavy"), "NR_edge": nr_full(sm, names, "edge"),
           "POL_rate": pol_full(sm, names, "rate"), "POL_reach": pol_full(sm, names, "reach"),
           "Migdal": migdal_full(sm, names)}
    return out


def top(rec, k=5):
    return sorted(rec, key=lambda n: -rec[n]["P1"])[:k]


def ranking_part():
    R.nr_inputs()
    for n in ("SiO2-q", "MgF2"):
        print("== polar interval %s: [%.4g, %.4g], ratio %.2f" % (n, POLC[n][2], POLC[n][3], POLC[n][3] / POLC[n][2]))
    print("== inputs: survivor crystals as rank17_6; CsI measured c_NR1 %.3f c_LA,max %.3f km/s" % R.CHR["CsI"][:2])
    RES = {}
    for pool, names in (("survivors", S11), ("full", FULL)):
        for r in (0.0, 1.0):
            out = run(names, r)
            RES[(pool, r)] = {}
            print("\n############ pool %s (%d crystals), r_mat = %.1f" % (pool, len(names), r))
            for ch, b, unit in CH:
                S = out[ch]
                rec, _, _ = R.analyse(S, b)
                RES[(pool, r)][ch] = (S, b, rec)
                print("\n== %s (%s; better %s); ranked %d, not ranked: %s" % (ch, unit, "lower" if b == "L" else "higher",
                      len(S), [n for n in names if n not in S]))
                for n in sorted(rec, key=lambda n: (rec[n]["tier"], rec[n]["med"] if b == "L" else -rec[n]["med"]))[:8]:
                    x = rec[n]
                    print("  %-8s median %.4g  68%% [%.4g, %.4g]  tier %d  P1 %.3f  rank68 %d-%d"
                          % (n, x["med"], x["lo"], x["hi"], x["tier"], x["P1"], x["r16"], x["r84"]))
                print("  largest P1: " + ", ".join("%s %.3f" % (n, rec[n]["P1"]) for n in top(rec, 4)))
    # pairwise statements used in the text
    S, b, rec = RES[("full", 0.0)]["NR_heavy"]
    print("\n== full pool, NR heavy, r=0: P(CsI > Bi2Se3) %.3f  P(CsI > NaI) %.3f  CsI/TeO2 median %.3f"
          % (R.pair(S, "CsI", "Bi2Se3", b), R.pair(S, "CsI", "NaI", b), rec["CsI"]["med"] / rec["TeO2"]["med"]))
    S, b, rec = RES[("full", 0.0)]["ER_quanta"]
    print("== full pool, ER quanta, r=0: P(PbTe < PbSe) %.3f ; P(Ge < GaSb) %.3f ; Si/Ge %.3f"
          % (R.pair(S, "PbTe", "PbSe", b), R.pair(S, "Ge", "GaSb", b), rec["Si"]["med"] / rec["Ge"]["med"]))
    S, b, rec = RES[("full", 0.0)]["ER_floor"]
    print("== full pool, ER floor, r=0: P(Ge < GaSb) %.3f" % R.pair(S, "Ge", "GaSb", b))
    S, b, rec = RES[("full", 0.0)]["NR_edge"]
    print("== full pool, NR edge, r=0: P(hBN < C) %.3f  P(C < PE) %.3f" % (R.pair(S, "hBN", "C", b), R.pair(S, "C", "PE", b)))
    S, b, rec = RES[("survivors", 0.0)]["ER_quanta"]
    print("== survivors, ER quanta: P(Ge < Si) %.3f ; Ge on the 77 K value 2.96 eV would lead a fortiori" % R.pair(S, "Ge", "Si", b))
    print("\n== background tolerances (medians, survivor pool r=0 and full pool r=0): b_A/b_B < (R_A/R_B)^2 (background-limited),"
          " < R_A/R_B (systematics floor)")
    for pool, ch, a, b_ in (("survivors", "NR_heavy", "TeO2", "CaWO4"), ("survivors", "POL_rate", "LiF", "NaF"),
                            ("full", "NR_heavy", "CsI", "Bi2Se3")):
        rec = RES[(pool, 0.0)][ch][2]
        q = rec[a]["med"] / rec[b_]["med"]
        print("  %-9s %-9s %s/%s: rate ratio %.3f -> tolerated b ratio %.2f (bg-limited), %.2f (systematics floor)"
              % (pool, ch, a, b_, q, q * q, q))
    print("  diamond array of 0.175 g crystals: surface-to-volume ratio x (1/0.175)^(1/3) = %.2f against one 1 g crystal; "
          "crystals for 1 g: %d" % ((1 / 0.175) ** (1 / 3), math.ceil(1 / 0.175)))
    return RES


def csi_example():
    print("\n== worked example: CsI added to the survivor pool (r = 0)")
    names = S11 + ["CsI"]
    out = run(names, 0.0)
    for ch, b, unit in CH:
        S = out[ch]
        if "CsI" not in S:
            print("  %s: CsI not ranked" % ch)
            continue
        rec, _, _ = R.analyse(S, b)
        lead = top(rec, 2)
        print("  %-9s CsI median %.4g [%.4g, %.4g] tier %d rank68 %d-%d P1 %.3f; leaders %s"
              % (ch, rec["CsI"]["med"], rec["CsI"]["lo"], rec["CsI"]["hi"], rec["CsI"]["tier"], rec["CsI"]["r16"],
                 rec["CsI"]["r84"], rec["CsI"]["P1"], ", ".join("%s %.3f" % (n, rec[n]["P1"]) for n in lead)))
        if ch == "NR_heavy":
            q = rec["CsI"]["med"] / rec["TeO2"]["med"]
            print("    P(CsI > TeO2) %.4f ; TeO2 P1 %.3f ; CsI/TeO2 %.3f -> tolerated b ratio %.2f (bg-limited)"
                  % (R.pair(S, "CsI", "TeO2", b), rec["TeO2"]["P1"], q, q * q))
        if ch == "POL_reach":
            print("    P(CsI < GaAs) %.4f ; ratio GaAs/CsI %.2f" % (R.pair(S, "CsI", "GaAs", b), rec["GaAs"]["med"] / rec["CsI"]["med"]))
    # cold-density bound of rank17_6 (4.734 g/cm^3) moves c by sqrt(4.529/4.734)
    f = math.sqrt(4.529 / 4.734)
    print("  denser cold cell: c_NR1 x %.4f -> F_NR %.3f" % (f, R.CSI0 / (R.CHR["CsI"][0] * f)))
    return out


# ----------------------------------------------------------------------------- Part B: internal backgrounds
ALPHA = 1 / 137.035999
ME = 510.99895  # keV


def fermi_rel(T, Zd, A):
    """Relativistic point-nucleus Fermi function (docstring of Part B)."""
    from scipy.special import loggamma
    W = T / ME + 1
    p = math.sqrt(W * W - 1)
    g = math.sqrt(1 - (ALPHA * Zd) ** 2)
    y = ALPHA * Zd * W / p
    R = 1.2 * A ** (1 / 3) / 386.15926796
    return 4 * (2 * p * R) ** (2 * g - 2) * math.exp(math.pi * y + 2 * loggamma(complex(g, y)).real
                                                             - 2 * loggamma(2 * g + 1).real)


def shape(T, Q, Zd, n_unique=0, A=None):
    E = T + ME
    p = math.sqrt(T * T + 2 * T * ME)
    q = Q - T
    if A is not None:
        F = fermi_rel(T, Zd, A) if T > 0 else 0.0
    else:
        eta = ALPHA * Zd * E / p if p > 0 else 1e9
        F = 2 * math.pi * eta / (1 - math.exp(-2 * math.pi * eta))
    S = 1.0
    if n_unique:
        S = sum((p / ME) ** (2 * k) * (q / ME) ** (2 * (n_unique - k))
                / (math.factorial(2 * k + 1) * math.factorial(2 * n_unique - 2 * k + 1)) for k in range(n_unique + 1))
    return p * E * q * q * F * S


def f_below(Q, Zd, n_unique=0, E1=1.0, A=None):
    tot = quad(shape, 1e-9, Q, args=(Q, Zd, n_unique, A), limit=400, points=[min(E1, Q / 2)])[0]
    low = quad(shape, 1e-9, E1, args=(Q, Zd, n_unique, A), limit=200)[0]
    return low / tot


def backgrounds():
    print("\n############ internal backgrounds below 1 keV")
    DAY = 86400.0
    f3H = f_below(18.592, 2)
    print("3H (Q 18.592 keV, allowed, Z_d 2): f(<1 keV) = %.4f" % f3H)
    lam3 = math.log(2) / (12.32 * 365.25)
    for tgt, Rp in (("Si (all components)", 124.0), ("Ge", 82.0)):
        a100 = Rp * (1 - math.exp(-lam3 * 100))
        print("  %-20s production %.0f /(kg d): 100 d at sea level -> %.3f, saturation -> %.2f /(kg d keV)"
              % (tgt, Rp, a100 * f3H, Rp * f3H))
    fPb0 = f_below(63.5, 83, A=210)
    fPb1 = f_below(17.0, 83, A=210)
    fBi = f_below(1161.2, 84, A=210)
    fPb0nr, fBinr = f_below(63.5, 83), f_below(1161.2, 84)
    print("  (non-relativistic Fermi function for comparison: 210Pb gs %.4f, 210Bi %.5f -> %.1f /(kg d keV) per Bq/kg)"
          % (fPb0nr, fBinr, DAY * (0.16 * fPb0nr + fBinr)))
    print("  3H with the relativistic Fermi function (A = 3): f = %.4f" % f_below(18.592, 2, A=3))
    print("210Pb ground-state branch (16 %%, Q 63.5 keV, Z_d 83, relativistic F): f(<1 keV) = %.4f; excited branch (84 %%, endpoint 17.0 keV, + 46.5 keV"
          " de-excitation absorbed in bulk) deposits >= 46.5 keV" % fPb0)
    print("  (excited-branch beta alone would have f = %.4f, not used)" % fPb1)
    print("210Bi (Q 1161.2 keV, Z_d 84, relativistic F, treated as allowed; first-forbidden non-unique in ENSDF): f(<1 keV) = %.5f" % fBi)
    per_Bq = DAY * (0.16 * fPb0 + fBi)
    print("  sub-keV rate per Bq/kg of 210Pb in equilibrium: %.1f /(kg d keV)  [210Pb part %.1f, 210Bi part %.1f = %.3f of it]"
          % (per_Bq, DAY * 0.16 * fPb0, DAY * fBi, fBi / (0.16 * fPb0 + fBi)))
    amax = 1.0 / per_Bq
    print("  budget 1 /(kg d keV) -> a(210Pb) <= %.2e Bq per kg of compound" % amax)
    for comp, wPb in (("PbSe", 207.2 / (207.2 + 78.971)), ("PbTe", 207.2 / (207.2 + 127.60)), ("PbS", 207.2 / (207.2 + 32.06))):
        print("    %-5s lead mass fraction %.3f -> <= %.2f mBq per kg of lead" % (comp, wPb, 1e3 * amax / wPb))
    # 40K
    f40 = f_below(1310.91, 20, n_unique=3)
    NA = 6.02214076e23
    lam40 = math.log(2) / (1.248e9 * 365.25 * DAY)
    spec = NA / 39.0983 * 1.17e-4 * lam40
    print("40K (beta 89.27 %%, Q 1310.9 keV, unique third forbidden): f(<1 keV) = %.3e; natural K %.1f Bq/g" % (f40, spec))
    wK = 39.0983 / (39.0983 + 180.94788 + 3 * 15.999)
    A = 1000 * wK * spec
    print("  KTaO3: K mass fraction %.4f -> A(40K) = %.0f Bq/kg -> beta sub-keV %.2e /(kg d keV)" % (wK, A, A * DAY * 0.8927 * f40))
    # 115In
    fIn_a = f_below(497.489, 50)
    fIn_u = f_below(497.489, 50, n_unique=4)
    wIn = 114.818 / (114.818 + 121.760)
    lamIn = math.log(2) / (4.41e14 * 365.25 * DAY)
    AIn = 1000 * wIn / 114.818 * NA * 0.95719 * lamIn
    print("115In (Q 497.5 keV, fourth forbidden non-unique; bracket allowed / unique fourth): f = %.2e / %.2e" % (fIn_a, fIn_u))
    print("  InSb: A(115In) = %.0f Bq/kg -> %.2e to %.2e /(kg d keV)" % (AIn, AIn * DAY * fIn_u, AIn * DAY * fIn_a))
    # 123Te electron capture bound
    wTe = 127.60 / (127.60 + 2 * 15.999)
    N123 = 1000 * wTe / 127.60 * NA * 0.0089
    lam_up = math.log(2) / (9.2e16 * 365.25)
    print("123Te in TeO2: %.3e nuclei/kg; half-life > 9.2e16 y -> captures < %.0f /(kg d) (bound: all in one keV)" % (N123, N123 * lam_up))
    # Compton plateau at T -> 0 (Klein-Nishina): d sigma/dT = 2 pi r_e^2 m_e / E^2
    re = 2.8179403e-13
    E = 1460.82
    dsig = 2 * math.pi * re ** 2 * ME / E ** 2
    print("Compton, 1460.8 keV line: d sigma/dT (T -> 0) = %.3e cm^2/keV per electron" % dsig)
    # check the T -> 0 limit against the full Klein-Nishina form
    al = E / ME

    def kn(T):
        s = T / E
        return math.pi * re ** 2 / (ME * al ** 2) * (2 + s * s / (al * al * (1 - s) ** 2) + s / (1 - s) * (s - 2 / al))
    print("  full Klein-Nishina at T = 1 keV / formula: %.5f" % (kn(1.0) / dsig))
    # mean escape path from a uniform interior point of a cube (isotropic), in units of the side
    rng = np.random.default_rng(7)
    P = rng.random((400000, 3))
    u = rng.normal(size=(400000, 3))
    u /= np.linalg.norm(u, axis=1)[:, None]
    with np.errstate(divide="ignore"):
        t = np.where(u > 0, (1 - P) / u, -P / u)
    lesc = np.min(t, axis=1).mean()
    print("  cube: mean escape path from the interior %.4f L (mean chord 4V/S = %.4f L)" % (lesc, 2 / 3))
    ne, L = 2e24, 5.0
    print("  illustration: n_e = %.0e cm^-3, side %.0f cm: fraction of photons depositing below 1 keV per keV = %.2e"
          % (ne, L, ne * lesc * L * dsig))


def figure(RES):
    labels = {"ER_floor": "electron-recoil floor", "ER_quanta": "pair energy", "NR_heavy": "nuclear, heavy mediator",
              "NR_edge": "nuclear edge", "POL_rate": "polar rate", "POL_reach": "polar reach", "Migdal": "Migdal"}
    nice = {"C": "diamond", "Al2O3": r"Al$_2$O$_3$", "TeO2": r"TeO$_2$", "hBN": "h-BN", "PbSe": "PbSe",
            "PbTe": "PbTe", "SiO2-q": "quartz"}
    fig, ax = plt.subplots(figsize=(6.0, 3.4))
    chs = [c for c, _, _ in CH]
    y = np.arange(len(chs))[::-1]
    for k, (pool, col, dy, lab) in enumerate((("full", "#eb6834", 0.19, "full pool (42)"),
                                               ("survivors", "#2a78d6", -0.19, "survivor pool (11)"))):
        for yy, ch in zip(y, chs):
            rec = RES[(pool, 0.0)][ch][2]
            n = top(rec, 1)[0]
            p = rec[n]["P1"]
            ax.barh(yy + dy, p, height=0.34, color=col, label=lab if ch == chs[0] else None)
            ax.text(p + 0.012, yy + dy, "%s %.2f (rank %d–%d)" % (nice.get(n, n), p, rec[n]["r16"], rec[n]["r84"]),
                    va="center", fontsize=6.5)
    ax.axvline(0.5, color="0.6", lw=0.6, ls=":")
    ax.set_yticks(y)
    ax.set_yticklabels([labels[c] for c in chs])
    ax.set_xlim(0, 1.55)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xlabel(r"$P(\mathrm{first})$ of the leader, independent method errors")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(loc="lower right", frameon=False, fontsize=7)
    fig.tight_layout()
    os.makedirs(FIG, exist_ok=True)
    fig.savefig(os.path.join(FIG, "fig21_6.pdf"))
    print("\nwrote fig21_6.pdf")


def main():
    print("guide21_7.py  N_MC = %d, seed %d (rank17_6), v_max = %.4g" % (R.N_MC, R.SEED, R.VMAX))
    RES = ranking_part()
    csi_example()
    backgrounds()
    figure(RES)


if __name__ == "__main__":
    main()
