"""Sect. 17.6 (ranking under uncertainty): every number printed in Sect. 17.6, Fig. 17.5 (fig:17-rank-floor),
Table 17.x (tab:17-rank) and Worked example 17.6 (we:17-tiers).  Log: rank17_6.log.
Run: python rank17_6.py > rank17_6.log   (about 20 s).

Method (Sect. 17.6, App. C.13, C.14):
  * each input x_j is drawn as ln x_j ~ N(ln x_j0, sigma_j) (lognormal) or as a stated uniform / log-uniform prior;
    sigma_j is the provenance width of Sect. 17.6 (a convention, listed in WIDTH below);
  * same-method inputs of different materials share a component: z = sqrt(r) z_family + sqrt(1 - r) z_own (marginals
    unchanged); r = r_mat = 0, 0.5, 1; independently measured inputs never share a component;
  * N_MC = 20000 draws, seed 20261106; per channel: median and 16/84 percentiles of the figure of merit (68 % interval),
    P(first) = fraction of draws in which the material is best, rank interval = 16/84 percentiles of its rank
    (inverted-CDF percentiles of the integer rank), tiers = heights of the interval order of the 68 % intervals (App. C.13).
  * the halo enters every edge through v_max^-2 or v_max^-1 alike; a common factor changes no order in any draw and is
    not sampled.  v_max = 2.650e-3 (Sect. 1.3, Fig. 3.6 caption).

Figures of merit (Sect. 17.5; better = lower (L) or higher (H)):
  ER floor     m_floor = 2 E_g / v_max^2                      (L, MeV)   eq:1.3-mmin with the gap
  NR heavy     F_NR = (8.956 km/s) / c_NR1                     (H)        c_NR1 = <sum_nu (q.e_nu)^2/c_nu>^-1 (Sect. 11.1, 17.5);
                                                                          8.956 km/s = silicon, measured tensor (Sect. 11.1)
  NR edge      m_min^ac = w_th / [2 c_LA,max (v_max - c_LA,max)], w_th = 1 meV (L, keV)   eq:11.1-edge
  POL rate     I_pol / rho_T                                   (H, meV cm^3/g)  eq:11.2-Ipol, eq:11.2-diatomic
  POL reach    2 w_L / v_max^2, lowest branch carrying >= 5 % of I_pol  (L, keV)
  Migdal       F_Mig = [sum_k Z_ion,k^2 / M_fu] (w_p^val)^-3 X_pole, relative to silicon at X_pole = 1  (H)
               (plasmon-pole factor of Sect. 17.5; X_pole log-uniform on [1, 3], an estimated prior)

Inputs and their sources (book values first; the book-phase corrections are applied):
  Gaps (ER floor): Si 1.17, Ge 0.744, GaAs 1.52 eV at low temperature (tab:3-materials: Ramanathan & Kurinsky 2004.10709
    Eq. (11); Rideau et al. Table VI; Lucero et al. Table I).  All other gaps: Griffin et al. 1910.10716 Table I,
    "experimental values (those with asterisks are measured at low temperature)".  Room-temperature gaps get the shift
    U[0.03, 0.10] eV to low temperature (estimated; family 'dEg'); the three book crystals shift by 0.05 (Si 1.12 -> 1.17),
    0.084 (Ge 0.66 -> 0.744) and 0.10 eV (GaAs 1.42 -> 1.52), tab:3-materials.
  Elastic tensors (NR heavy, NR edge):
    measured: Si 165.6/63.9/79.5 GPa, rho 2.33; Ge 131/49/68, rho 5.3268; diamond 1081/125/579, rho 3.5156 (densities from a = 5.658, 3.567 A as in Sect. 11.1;
      McSkimin et al. via Haxhijaj Table III); CaWO4 C11 145.9, C33 127.4, C12 62.6, C13 39.2, C16 -19.2 (C26 = +19.2),
      C44 33.5, C66 38.7 GPa (Farley & Saunders 1972, as quoted by Popova et al. 2508.08858 p.16), rho 6.115 g/cm^3
      (measured lattice constants a = 5.243, c = 11.376 A with standard atomic masses, 4 f.u. per cell);
      CsI 4.2 K: C11 27.37, C12 7.93, C44 8.25 GPa (Vallin, Beckman, Salama, J. Appl. Phys. 35, 1222 (1964)), rho 4.529
      (a = 4.567 A, room temperature; the 4.2 K cell is denser, which lowers c by up to 2 %).
    computed: JARVIS-DFT OptB88vdW tensors (Choudhary et al. 1804.01033; dft_3d release of 2025-09-24), Voigt order with
      the shear constants assigned to their axes, densities of the computed cells:
      GaAs JVASP-1174 C11 100.0 C12 42.9 C44 51.5, rho 5.102; Al2O3 JVASP-32 C11 469.8 C33 468.9 C12 153.3 C13 114.1
      C14 -20.8 C44 140.9 C66 158.3, rho 3.882; TeO2 JVASP-57128 C11 56.3 C33 114.7 C12 49.1 C13 23.0 C44 29.1 C55 28.8
      C66 72.7, rho 5.917; gamma-LiAlO2 JVASP-9407 C11 141.2 C33 176.9 C12 71.7 C13 69.6 C44 60.7 C66 63.6, rho 2.582;
      LiF JVASP-1130 C11 129.6 C12 46.1 C44 64.3, rho 2.662; NaF JVASP-20326 C11 117.3 C12 21.1 C44 28.1, rho 2.806;
      and, for the check of the computed family only, Si JVASP-1002 150.0/55.9/74.1 rho 2.25, Ge JVASP-890
      100.6/36.8/52.0 rho 5.054, C JVASP-91 1061.0/125.6/559.3 rho 3.50.  Li2MoO4: no tensor (not ranked).
  Polar crystals: GaAs I_pol/rho_T = 0.1415 meV cm^3/g (splitting route, we:11-ipol; the dielectric route gives 0.153);
    sapphire 9.12 (ordinary axis, measured modes, Sect. 11.2); LiF and NaF from eq:11.2-diatomic with the computed
    Z*, eps_inf, w_O,max of 1910.10716 Table I (LiF 1.05, 2.02, 77.2 meV; NaF 0.98, 1.78, 49.9 meV), standard masses.
    Edges: GaAs w_L = 36.35 meV (we:5-lst), NaF 49.9, LiF 77.2 meV (1910.10716), sapphire 112.4 meV (ordinary axis,
    carries 95.2 % of I_pol; every other branch < 5 %), Sect. 11.2.
  Migdal: valence counts Z_ion (Si, Ge, C 4; Ga 3, As 5; Al 3; O 6; Te 6; Ca 2; W 6; Mo 6; Li 1; F 7; Na 1), w_p^val from
    n = Z_val rho / M_fu (free-electron valence plasma frequency, as for Si 16.6 and Ge 15.6 eV in Sect. 10.2);
    densities: Si 2.33, Ge 5.33, C 3.51, GaAs 5.361 (Sect. 11.2), Al2O3 3.98 (Sect. 11.2), CaWO4 6.115, LiF 2.652,
    NaF 2.803 (measured lattice constants), Li2MoO4 3.04 (measured), TeO2 5.917 and LiAlO2 2.582 (computed cells,
    width 0.030).
Provenance widths (sigma of ln x; conventions of Sect. 17.6):
  measured, no stated error: gap 0.01; speeds from a measured tensor 0.02; a measured phonon frequency 0.005;
  sapphire I_pol 0.03 (I_pol proportional to 1/eps_inf at fixed modes, eps_inf 3.1-3.3); GaAs I_pol 0.04 (half the
  spread of its two routes);
  computed, database: speeds 0.086, cell densities 0.030;  computed in a paper (DFPT): Z*, eps_inf 0.07, w 0.05;
  estimated: room-to-low-temperature gap shift U[0.03, 0.10] eV; X_pole log-uniform [1, 3].
"""
import os
import math
import numpy as np
from scipy.stats import norm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch17")
plt.rcParams.update({"font.size": 8, "font.family": "serif", "mathtext.fontset": "cm"})

N_MC = 20000
SEED = 20261106
VMAX = 2.650e-3
C_LIGHT = 299792.458  # km/s
CSI0 = 8.956          # km/s, silicon c_NR1 from the measured tensor (Sect. 11.1)
WTH = 1e-3            # eV

WIDTH = dict(Eg=0.01, c_meas=0.02, w_meas=0.005, Ipol_sapph=0.03, Ipol_GaAs=0.04,
             c_DB=0.086, rho_DB=0.030, Z_DFPT=0.07, eps_DFPT=0.07, w_DFPT=0.05,
             dEg=(0.03, 0.10), Xpole=(1.0, 3.0))

# ----------------------------------------------------------------------------- Christoffel problem
def c4(V):
    idx = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (1, 2): 3, (2, 1): 3, (0, 2): 4, (2, 0): 4, (0, 1): 5, (1, 0): 5}
    C = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    C[i, j, k, l] = V[idx[(i, j)], idx[(k, l)]]
    return C


def voigt(C11, C12, C44, C33=None, C13=None, C55=None, C66=None, C14=0.0, C16=0.0):
    C33 = C11 if C33 is None else C33
    C13 = C12 if C13 is None else C13
    C55 = C44 if C55 is None else C55
    C66 = C44 if C66 is None else C66
    V = np.zeros((6, 6))
    V[0, 0] = V[1, 1] = C11
    V[2, 2] = C33
    V[0, 1] = V[1, 0] = C12
    V[0, 2] = V[2, 0] = V[1, 2] = V[2, 1] = C13
    V[3, 3] = C44
    V[4, 4] = C55
    V[5, 5] = C66
    # trigonal (3m, x along a twofold axis): C24 = -C14, C56 = C14
    V[0, 3] = V[3, 0] = C14
    V[1, 3] = V[3, 1] = -C14
    V[4, 5] = V[5, 4] = C14
    # tetragonal 4/m: C26 = -C16
    V[0, 5] = V[5, 0] = C16
    V[1, 5] = V[5, 1] = -C16
    return V


def christoffel(V, rho, nth=48, nph=96):
    """sphere averages on a Gauss-Legendre (cos theta) x uniform (phi) grid: c_NR1, c_LA,max, mean c_LA (km/s)"""
    C = c4(V)
    x, w = np.polynomial.legendre.leggauss(nth)
    ph = (np.arange(nph) + 0.5) * 2 * np.pi / nph
    acc = 0.0
    wsum = 0.0
    cmax = 0.0
    cla = 0.0
    for ct, wt in zip(x, w):
        st = math.sqrt(1 - ct * ct)
        for p in ph:
            n = np.array([st * math.cos(p), st * math.sin(p), ct])
            G = np.einsum("ijkl,j,l->ik", C, n, n) / rho
            lam, vec = np.linalg.eigh(G)
            c = np.sqrt(lam)
            proj = (vec.T @ n) ** 2
            acc += wt * np.sum(proj / c)
            wsum += wt
            cmax = max(cmax, c[-1])
            cla += wt * c[-1]
    return 1.0 / (acc / wsum), cmax, cla / wsum


TENS = {  # (Voigt, rho, provenance)
    "Si": (voigt(165.6, 63.9, 79.5), 2.33, "meas"),
    "Ge": (voigt(131.0, 49.0, 68.0), 5.3268, "meas"),
    "C": (voigt(1081.0, 125.0, 579.0), 3.5156, "meas"),
    "CaWO4": (voigt(145.9, 62.6, 33.5, C33=127.4, C13=39.2, C66=38.7, C16=-19.2), 6.115, "meas"),
    "CsI": (voigt(27.37, 7.93, 8.25), 4.529, "meas"),
    "GaAs": (voigt(100.0, 42.9, 51.5), 5.102, "DB"),
    "Al2O3": (voigt(469.8, 153.3, 140.9, C33=468.9, C13=114.1, C66=158.3, C14=-20.8), 3.882, "DB"),
    "TeO2": (voigt(56.3, 49.1, 29.1, C33=114.7, C13=23.0, C55=28.8, C66=72.7), 5.917, "DB"),
    "LiAlO2": (voigt(141.2, 71.7, 60.7, C33=176.9, C13=69.6, C66=63.6), 2.582, "DB"),
    "LiF": (voigt(129.6, 46.1, 64.3), 2.662, "DB"),
    "NaF": (voigt(117.3, 21.1, 28.1), 2.806, "DB"),
    "Si_DB": (voigt(150.0, 55.9, 74.1), 2.25, "DB"),
    "Ge_DB": (voigt(100.6, 36.8, 52.0), 5.054, "DB"),
    "C_DB": (voigt(1061.0, 125.6, 559.3), 3.50, "DB"),
}

NAMES = {"Si": "Si", "Ge": "Ge", "GaAs": "GaAs", "C": "diamond", "Al2O3": "Al2O3", "TeO2": "TeO2", "CaWO4": "CaWO4",
         "Li2MoO4": "Li2MoO4", "LiAlO2": "LiAlO2", "LiF": "LiF", "NaF": "NaF"}
POOL = ["Si", "Ge", "GaAs", "C", "Al2O3", "TeO2", "CaWO4", "Li2MoO4", "LiAlO2", "LiF", "NaF"]


# ----------------------------------------------------------------------------- sampling with families
class Sampler:
    def __init__(self, r, seed=SEED, widths=None):
        self.r = r
        self.rng = np.random.default_rng(seed)
        self.fam = {}
        self.W = dict(WIDTH) if widths is None else widths

    def z(self, fam=None):
        own = self.rng.standard_normal(N_MC)
        if fam is None or self.r == 0:
            if fam is not None:  # keep the stream aligned between r values
                self.fam.setdefault(fam, self.rng.standard_normal(N_MC))
            return own
        if fam not in self.fam:
            self.fam[fam] = self.rng.standard_normal(N_MC)
        return math.sqrt(self.r) * self.fam[fam] + math.sqrt(1 - self.r) * own

    def lnN(self, x0, s, fam=None):
        return x0 * np.exp(s * self.z(fam))

    def U(self, a, b, fam=None):
        return a + (b - a) * norm.cdf(self.z(fam))

    def logU(self, a, b, fam=None):
        return np.exp(np.log(a) + (np.log(b) - np.log(a)) * norm.cdf(self.z(fam)))


# ----------------------------------------------------------------------------- analysis helpers
def analyse(S, better):
    """S: dict name -> samples.  better: 'L' or 'H'.  Returns per-material records and the tier list."""
    names = list(S)
    A = np.array([S[n] for n in names])  # (n_mat, N_MC)
    key = -A if better == "L" else A
    order = np.argsort(-key, axis=0)
    ranks = np.empty_like(order)
    for j in range(A.shape[1]):
        ranks[order[:, j], j] = np.arange(1, len(names) + 1)
    rec = {}
    for i, n in enumerate(names):
        lo, med, hi = np.percentile(A[i], [16, 50, 84])
        r16, r84 = np.percentile(ranks[i], [16, 84], method="inverted_cdf")
        rec[n] = dict(med=med, lo=lo, hi=hi, P1=float(np.mean(ranks[i] == 1)), r16=int(r16), r84=int(r84))
    # tiers: interval order on 68 % intervals, oriented so that larger is better
    I = {n: ((-math.log(rec[n]["hi"]), -math.log(rec[n]["lo"])) if better == "L"
             else (math.log(rec[n]["lo"]), math.log(rec[n]["hi"]))) for n in names}
    srt = sorted(names, key=lambda n: -I[n][1])
    h = {}
    for n in srt:
        above = [h[b] for b in h if I[b][0] > I[n][1]]
        h[n] = 1 + (max(above) if above else 0)
    for n in names:
        rec[n]["tier"] = h[n]
    return rec, ranks, names


def pair(S, a, b, better):
    x = S[a] < S[b] if better == "L" else S[a] > S[b]
    return float(np.mean(x))


def show(title, rec, better, unit, fmt="%.3g"):
    print("\n== %s (better = %s; %s)" % (title, "lower" if better == "L" else "higher", unit))
    for n in sorted(rec, key=lambda n: (rec[n]["tier"], rec[n]["med"] if better == "L" else -rec[n]["med"])):
        r = rec[n]
        print(("  %-8s median " + fmt + "  68%% [" + fmt + ", " + fmt + "]  tier %d  P1 %.3f  rank68 %d-%d")
              % (n, r["med"], r["lo"], r["hi"], r["tier"], r["P1"], r["r16"], r["r84"]))


# ----------------------------------------------------------------------------- channels
def mfloor(Eg):  # MeV
    return 2 * Eg / VMAX ** 2 / 1e6


GAPS_TABLE = {  # 1910.10716 Table I; True = measured at low temperature (asterisk)
    "Si": (1.11, False), "Ge": (0.67, False), "NaI": (5.8, False), "CsI": (6.14, False), "CaWO4": (5.2, False),
    "GaAs": (1.42, False), "Al2O3": (8.8, False), "C": (5.47, True), "SiO2": (9.2, False), "PbTe": (0.19, True),
    "InSb": (0.24, True), "AlN": (6.20, False), "CaF2": (11.81, False), "GaN": (3.43, True), "GaSb": (0.720, False),
    "LiF": (14.2, False), "MgF2": (12.4, False), "MgO": (7.83, False), "NaCl": (8.75, False), "NaF": (11.5, False),
    "PbS": (0.29, True), "PbSe": (0.17, True), "ZnO": (3.3, False), "ZnS": (3.80, True)}
GAPS_BOOK = {"Si": 1.17, "Ge": 0.744, "GaAs": 1.52}   # low temperature, tab:3-materials


def er_floor(sm, names):
    a, b = sm.W["dEg"]
    S = {}
    for n in names:
        if n in GAPS_BOOK:
            S[n] = mfloor(sm.lnN(GAPS_BOOK[n], sm.W["Eg"]))
        elif n in GAPS_TABLE:
            e0, lowT = GAPS_TABLE[n]
            E = sm.lnN(e0, sm.W["Eg"])
            if not lowT:
                E = E + sm.U(a, b, "dEg")
            S[n] = mfloor(E)
    return S


CHR = {}


def nr_inputs():
    for m in ["Si", "Ge", "C", "CaWO4", "CsI", "GaAs", "Al2O3", "TeO2", "LiAlO2", "LiF", "NaF", "Si_DB", "Ge_DB", "C_DB"]:
        V, rho, prov = TENS[m]
        CHR[m] = christoffel(V, rho) + (prov,)


def nr_heavy(sm, names):
    S = {}
    for n in names:
        if n not in CHR:
            continue
        c, _, _, prov = CHR[n]
        cs = sm.lnN(c, sm.W["c_meas"]) if prov == "meas" else sm.lnN(c, sm.W["c_DB"], "c_DB")
        S[n] = CSI0 / cs
    return S


def edge_keV(c_kms):
    c = c_kms / C_LIGHT
    return WTH / (2 * c * (VMAX - c)) / 1e3


def nr_edge(sm, names):
    S = {}
    for n in names:
        if n not in CHR:
            continue
        _, cm, _, prov = CHR[n]
        cs = sm.lnN(cm, sm.W["c_meas"]) if prov == "meas" else sm.lnN(cm, sm.W["c_DB"], "c_DB")
        S[n] = edge_keV(cs)
    return S


ALPHA = 1 / 137.035999
U_EV = 931.49410e6
GCC_EV4 = 5.60958860e32 * (1.97326980e-5) ** 3  # 1 g/cm^3 in eV^4


def ipol_diatomic(Z, einf, wL_meV, m1, m2):
    """eq:11.2-diatomic: (pi/2) e^2 Z*^2 / (M_cell mu eps_inf^2 w_L), Heaviside-Lorentz e^2 = 4 pi alpha; meV cm^3/g"""
    M = (m1 + m2) * U_EV
    mu = m1 * m2 / (m1 + m2) * U_EV
    val = (math.pi / 2) * 4 * math.pi * ALPHA * Z ** 2 / (M * mu * einf ** 2 * wL_meV * 1e-3)  # eV^-3
    return val * GCC_EV4 * 1e3


DFPT = {"LiF": (1.05, 2.02, 77.2, 6.941, 18.998), "NaF": (0.98, 1.78, 49.9, 22.990, 18.998)}


def pol_rate(sm, names):
    S = {}
    for n in names:
        if n == "GaAs":
            S[n] = sm.lnN(0.1415, sm.W["Ipol_GaAs"])
        elif n == "Al2O3":
            S[n] = sm.lnN(9.12, sm.W["Ipol_sapph"])
        elif n in DFPT:
            Z, e, w, m1, m2 = DFPT[n]
            I0 = ipol_diatomic(Z, e, w, m1, m2)
            S[n] = (I0 * np.exp(2 * sm.W["Z_DFPT"] * sm.z("Z_DFPT")) * np.exp(-2 * sm.W["eps_DFPT"] * sm.z("eps_DFPT"))
                    * np.exp(-sm.W["w_DFPT"] * sm.z("w_DFPT")))
    return S


WL = {"GaAs": (36.35, "meas"), "NaF": (49.9, "DFPT"), "LiF": (77.2, "DFPT"), "Al2O3": (112.4, "meas")}


def pol_reach(sm, names):
    S = {}
    for n in names:
        if n in WL:
            w0, prov = WL[n]
            w = sm.lnN(w0, sm.W["w_meas"]) if prov == "meas" else sm.lnN(w0, sm.W["w_DFPT"], "w_DFPT")
            S[n] = 2 * w * 1e-3 / VMAX ** 2 / 1e3
    return S


MIG = {  # Z_val per f.u., sum Z^2, M_fu (u), rho (g/cm^3), density provenance
    "Si": (4, 16, 28.0855, 2.33, "meas"), "Ge": (4, 16, 72.630, 5.33, "meas"), "C": (4, 16, 12.011, 3.51, "meas"),
    "GaAs": (8, 34, 144.645, 5.361, "meas"), "Al2O3": (24, 126, 101.961, 3.98, "meas"),
    "TeO2": (18, 108, 159.60, 5.917, "DB"), "CaWO4": (32, 184, 287.92, 6.115, "meas"),
    "Li2MoO4": (32, 182, 173.82, 3.04, "meas"), "LiAlO2": (16, 82, 65.92, 2.582, "DB"),
    "LiF": (8, 50, 25.939, 2.652, "meas"), "NaF": (8, 50, 41.988, 2.803, "meas")}


def wp_val(Zv, M, rho):
    n = Zv * rho / M * 6.02214076e23  # cm^-3
    return 3.71140e-11 * math.sqrt(n)  # eV (hbar omega_p = hbar sqrt(4 pi alpha n hbar c / m_e) in these units)


def migdal(sm, names):
    Zs, Z2s, Ms, rhos, _ = MIG["Si"]
    ref = Z2s / Ms * wp_val(Zs, Ms, rhos) ** -3
    S = {}
    for n in names:
        Zv, Z2, M, rho, prov = MIG[n]
        rr = sm.lnN(rho, sm.W["rho_DB"], "rho_DB") if prov == "DB" else rho
        wp = 3.71140e-11 * np.sqrt(Zv * rr / M * 6.02214076e23)
        S[n] = Z2 / M * wp ** -3 * sm.logU(*sm.W["Xpole"], fam="Xpole") / ref
    return S


# ----------------------------------------------------------------------------- run
def run_all(r, widths=None, quiet=False):
    sm = Sampler(r, widths=widths)
    out = {}
    out["ER_floor"] = (er_floor(sm, POOL), "L")
    out["NR_heavy"] = (nr_heavy(sm, POOL), "H")
    out["NR_edge"] = (nr_edge(sm, POOL), "L")
    out["POL_rate"] = (pol_rate(sm, POOL), "H")
    out["POL_reach"] = (pol_reach(sm, POOL), "L")
    out["Migdal"] = (migdal(sm, POOL), "H")
    return out


def main():
    print("rank17_6.py  N_MC = %d, seed %d, v_max = %.4g" % (N_MC, SEED, VMAX))
    print("widths:", WIDTH)
    nr_inputs()
    print("\n== Christoffel sphere averages (48 x 96 Gauss-Legendre x uniform grid); km/s")
    for m, (cn, cm, cl, prov) in CHR.items():
        print("  %-7s %-4s c_NR1 %.3f  c_LA,max %.3f  mean c_LA %.3f  F_NR = 8.956/c_NR1 = %.3f  edge(1 meV) %.2f keV"
              % (m, prov, cn, cm, cl, CSI0 / cn, edge_keV(cm)))
    print("\n== computed family against measured tensors (ln c_DB/c_meas)")
    d = []
    for m in ["Si", "Ge", "C"]:
        x = math.log(CHR[m + "_DB"][0] / CHR[m][0])
        y = math.log(CHR[m + "_DB"][1] / CHR[m][1])
        d.append(x)
        print("  %-3s c_NR1 %+.4f (%.1f %%)   c_LA,max %+.4f" % (m, x, 100 * (math.exp(x) - 1), y))
    d = np.array(d)
    print("  mean %+.4f  rms %.4f  (convention sigma_c_DB = %.3f)" % (d.mean(), math.sqrt(np.mean(d ** 2)), WIDTH["c_DB"]))
    print("\n== CsI (outside the pool): measured 4.2 K tensor; rho 4.529 (room-T a) and 4.734 (a = 4.50 A, denser bound)")
    for rho in (4.529, 4.734):
        cn, cm, cl = christoffel(TENS["CsI"][0], rho)
        print("  rho %.3f: c_NR1 %.3f  c_LA,max %.3f  F_NR %.2f  edge %.1f keV" % (rho, cn, cm, CSI0 / cn, edge_keV(cm)))
    print("\n== polar band integrals from eq:11.2-diatomic (computed DFPT inputs of 1910.10716 Table I)")
    for m, v in DFPT.items():
        print("  %-4s I_pol/rho_T = %.2f meV cm^3/g" % (m, ipol_diatomic(*v)))
    print("\n== Migdal inputs: sum Z^2/M_fu, w_p^val (eV), F_Mig at X_pole = 1 relative to Si")
    Zs, Z2s, Ms, rhos, _ = MIG["Si"]
    ref = Z2s / Ms * wp_val(Zs, Ms, rhos) ** -3
    for m, (Zv, Z2, M, rho, prov) in MIG.items():
        w = wp_val(Zv, M, rho)
        print("  %-8s %.3f  %.2f  %.3f" % (m, Z2 / M, w, Z2 / M * w ** -3 / ref))
    print("\n== room-to-low-temperature gap shifts of the book crystals (tab:3-materials): Si %.3f, Ge %.3f, GaAs %.3f eV"
          % (1.17 - 1.12, 0.744 - 0.66, 1.52 - 1.42))

    RES = {}
    for r in (0.0, 0.5, 1.0):
        out = run_all(r)
        RES[r] = {}
        print("\n############ r_mat = %.1f" % r)
        units = dict(ER_floor="MeV", NR_heavy="F_NR (Si = 1 at 8.956 km/s)", NR_edge="keV at 1 meV",
                     POL_rate="meV cm^3/g", POL_reach="keV", Migdal="F_Mig (Si at X_pole = 1)")
        for ch, (S, b) in out.items():
            rec, ranks, names = analyse(S, b)
            RES[r][ch] = (S, b, rec)
            show(ch + "  r=%.1f" % r, rec, b, units[ch])
            ntier = max(v["tier"] for v in rec.values())
            print("  tiers: %d; sum P1 = %.4f; not ranked: %s" % (ntier, sum(v["P1"] for v in rec.values()),
                                                                 [n for n in POOL if n not in S]))

    print("\n== pairwise probabilities: Monte Carlo against eq:C.14-pairwise (lognormal, linearized)")
    for (ch, a, b_, sa, sb, rr) in [("NR_heavy", "TeO2", "GaAs", WIDTH["c_DB"], WIDTH["c_DB"], 0.0),
                                    ("NR_heavy", "TeO2", "GaAs", WIDTH["c_DB"], WIDTH["c_DB"], 0.5),
                                    ("NR_heavy", "GaAs", "Ge", WIDTH["c_DB"], WIDTH["c_meas"], 0.0),
                                    ("NR_heavy", "TeO2", "CaWO4", WIDTH["c_DB"], WIDTH["c_meas"], 0.0),
                                    ("NR_heavy", "CaWO4", "GaAs", WIDTH["c_meas"], WIDTH["c_DB"], 0.0),
                                    ("NR_edge", "C", "Al2O3", WIDTH["c_meas"], WIDTH["c_DB"], 0.0)]:
        S, bb, rec = RES[rr][ch]
        mc = pair(S, a, b_, bb)
        c0a = CHR[a][0 if ch == "NR_heavy" else 1]
        c0b = CHR[b_][0 if ch == "NR_heavy" else 1]
        if ch == "NR_heavy":
            delta = math.log(c0b / c0a)
        else:
            delta = math.log(edge_keV(c0b) / edge_keV(c0a))
        rc = rr if (sa == sb == WIDTH["c_DB"]) else 0.0
        an = norm.cdf(delta / math.sqrt(sa ** 2 + sb ** 2 - 2 * rc * sa * sb)) if sa ** 2 + sb ** 2 - 2 * rc * sa * sb > 0 else 1.0
        print("  %-8s %-6s > %-6s r=%.1f  Delta ln = %+.4f  MC %.3f  formula %.3f" % (ch, a, b_, rr, delta, mc, an))
    for r in (0.0, 0.5, 1.0):
        S, bb, rec = RES[r]["NR_heavy"]
        print("  NR_heavy r=%.1f: P(TeO2>GaAs) %.3f  P(GaAs>Ge) %.3f  P(TeO2>CaWO4) %.3f  P(CaWO4>GaAs) %.3f  P(GaAs>CaWO4) %.3f"
              % (r, pair(S, "TeO2", "GaAs", bb), pair(S, "GaAs", "Ge", bb), pair(S, "TeO2", "CaWO4", bb),
                 pair(S, "CaWO4", "GaAs", bb), pair(S, "GaAs", "CaWO4", bb)))
        S, bb, rec = RES[r]["Migdal"]
        top = sorted(rec, key=lambda n: -rec[n]["P1"])[:4]
        print("  Migdal   r=%.1f: P1 %s ; P(NaF>Si) %.3f ; max P1 %.3f (%s)"
              % (r, ", ".join("%s %.3f" % (n, rec[n]["P1"]) for n in top), pair(S, "NaF", "Si", bb),
                 rec[top[0]]["P1"], top[0]))
        S, bb, rec = RES[r]["ER_floor"]
        print("  ER_floor r=%.1f: P1 Ge %.3f" % (r, rec["Ge"]["P1"]))
        S, bb, rec = RES[r]["POL_rate"]
        print("  POL_rate r=%.1f: P(LiF>NaF) %.3f  P(NaF>Al2O3) %.3f" % (r, pair(S, "LiF", "NaF", bb), pair(S, "NaF", "Al2O3", bb)))
    # a common offset of the computed family (mean of the three crystals with both tensors) moved onto GaAs
    off = 0.0490   # the mean printed above (Ge with a = 5.658 A)
    d0 = math.log(CHR["Ge"][0] / CHR["GaAs"][0])
    sg = math.sqrt(WIDTH["c_DB"] ** 2 + WIDTH["c_meas"] ** 2)
    print("  GaAs vs Ge, computed speed raised by the family mean offset %.4f: F_GaAs %.3f, P(GaAs>Ge) = Phi(%.4f/%.4f) = %.3f"
          % (off, CSI0 / (CHR["GaAs"][0] * math.exp(off)), d0 - off, sg, norm.cdf((d0 - off) / sg)))

    print("\n== conditionality: computed-speed width doubled (0.172), r_mat = 0")
    W2 = dict(WIDTH)
    W2["c_DB"] = 2 * WIDTH["c_DB"]
    out2 = run_all(0.0, widths=W2)
    for ch in ("NR_heavy", "NR_edge"):
        S, b = out2[ch]
        rec, _, _ = analyse(S, b)
        show(ch + " (sigma_c_DB doubled)", rec, b, "")
        if ch == "NR_heavy":
            print("  P(TeO2>CaWO4) %.3f  P(GaAs>Ge) %.3f" % (pair(S, "TeO2", "CaWO4", b), pair(S, "GaAs", "Ge", b)))
    print("\n== conditionality: gap shift prior U[0, 0.15] eV instead of U[0.03, 0.10], r = 0 (24 crystals, Ge vs GaSb)")

    # ------------------------------------------------------------------------- ER floor, 24 crystals of Table I
    big = list(GAPS_TABLE)
    RB = {}
    for r in (0.0, 1.0):
        sm = Sampler(r)
        S = er_floor(sm, big)
        rec, ranks, names = analyse(S, "L")
        RB[r] = (S, rec)
        show("ER floor, 24 crystals of 1910.10716 Table I (book gaps for Si, Ge, GaAs)  r=%.1f" % r, rec, "L", "MeV", "%.4g")
        print("  tiers %d;  P(Ge<GaSb) %.3f  P(PbSe<PbTe) %.3f  P(AlN<CsI) %.3f  P(NaCl<Al2O3) %.3f  P(GaN<ZnO) %.3f"
              % (max(v["tier"] for v in rec.values()), pair(S, "Ge", "GaSb", "L"), pair(S, "PbSe", "PbTe", "L"),
                 pair(S, "AlN", "CsI", "L"), pair(S, "NaCl", "Al2O3", "L"), pair(S, "GaN", "ZnO", "L")))
    W3 = dict(WIDTH)
    W3["dEg"] = (0.0, 0.15)
    sm = Sampler(0.0, widths=W3)
    S3 = er_floor(sm, big)
    print("  shift U[0, 0.15]: P(Ge<GaSb) %.3f ; unshifted GaSb floor %.4f MeV vs Ge %.4f MeV"
          % (pair(S3, "Ge", "GaSb", "L"), mfloor(0.720), mfloor(0.744)))

    S0, r0 = RB[0.0]
    print("  ratios: Ge floor / PbSe %.2f, / PbTe %.2f, / PbS %.2f" % (r0["Ge"]["med"] / r0["PbSe"]["med"],
          r0["Ge"]["med"] / r0["PbTe"]["med"], r0["Ge"]["med"] / r0["PbS"]["med"]))
    rp = RES[0.0]
    e = rp["NR_edge"][2]; p = rp["POL_rate"][2]; h = rp["NR_heavy"][2]; m = rp["Migdal"][2]
    print("  ratios: edge sapphire/diamond %.3f; POL LiF/GaAs %.0f, LiF/NaF %.2f; CsI F_NR/TeO2 %.2f-%.2f"
          % (e["Al2O3"]["med"] / e["C"]["med"], p["LiF"]["med"] / p["GaAs"]["med"], p["LiF"]["med"] / p["NaF"]["med"],
             CSI0 / 2.404 / h["TeO2"]["med"], CSI0 / 2.351 / h["TeO2"]["med"]))

    # ------------------------------------------------------------------------- worked example: five NR-heavy intervals
    S, bb, rec = RES[0.0]["NR_heavy"]
    five = ["TeO2", "CaWO4", "GaAs", "Ge", "NaF"]
    print("\n== worked example: five NR-heavy intervals (r = 0), ln F_NR")
    I = {n: (math.log(rec[n]["lo"]), math.log(rec[n]["hi"])) for n in five}
    srt = sorted(five, key=lambda n: -I[n][1])
    h = {}
    for n in srt:
        above = [b for b in h if I[b][0] > I[n][1]]
        h[n] = 1 + (max(h[b] for b in above) if above else 0)
        print("  %-6s F [%.3f, %.3f]  ln [%.4f, %.4f]  resolved above it: %s -> height %d"
              % (n, rec[n]["lo"], rec[n]["hi"], I[n][0], I[n][1], above, h[n]))
    S5 = {n: S[n] for n in five}
    rec5, _, _ = analyse(S5, "H")
    print("  P(first) among the five: " + ", ".join("%s %.3f" % (n, rec5[n]["P1"]) for n in five))
    print("  rank intervals among the five: " + ", ".join("%s %d-%d" % (n, rec5[n]["r16"], rec5[n]["r84"]) for n in five))

    # ------------------------------------------------------------------------- Fig. 17.5
    S, rec = RB[0.0]
    order = sorted(rec, key=lambda n: rec[n]["med"])
    lab = {"C": "diamond", "Al2O3": r"Al$_2$O$_3$", "CaWO4": r"CaWO$_4$", "SiO2": r"SiO$_2$", "CaF2": r"CaF$_2$",
           "MgF2": r"MgF$_2$"}
    book3 = {"Si", "Ge", "GaAs"}
    lowT = {n for n in order if n in book3 or GAPS_TABLE[n][1]}
    fig = plt.figure(figsize=(6.4, 6.0))
    gs = fig.add_gridspec(2, 2, height_ratios=[3.2, 1.0], width_ratios=[1.35, 1], hspace=0.32, wspace=0.05)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1], sharey=ax1)
    ax3 = fig.add_subplot(gs[1, :])
    ntier = max(v["tier"] for v in rec.values())
    cols = plt.cm.viridis(np.linspace(0, 0.9, ntier))
    for k, n in enumerate(order):
        y = len(order) - 1 - k
        r = rec[n]
        c = cols[r["tier"] - 1]
        ax1.plot([r["med"]], [y], "o", ms=4, mec=c, mfc=(c if n in lowT else "white"), mew=1.0)
        ax1.text(r["med"] * 1.12, y, "%d" % r["tier"], va="center", fontsize=6, color=c)
        ax2.plot([r["r16"] - 0.35, r["r84"] + 0.35], [y, y], color=c, lw=3, solid_capstyle="butt")
        ax2.text(28.2, y, ("%.2f" % r["P1"]) if r["P1"] >= 0.005 else "0", va="center", ha="right", fontsize=6)
    ax1.set_xscale("log")
    ax1.set_yticks(range(len(order)))
    ax1.set_yticklabels([lab.get(n, n) for n in order][::-1], fontsize=7)
    ax1.set_xlabel(r"$m_{\mathrm{floor}} = 2E_{\mathrm{g}}/v_{\mathrm{max}}^2$ (MeV), median")
    ax1.set_xlim(0.03, 7)
    plt.setp(ax2.get_yticklabels(), visible=False)
    ax2.set_xlim(0, 28.5)
    ax2.set_xlabel("rank, 68 % interval")
    ax2.text(28.2, len(order) - 0.3, r"$P(\mathrm{first})$", ha="right", fontsize=6)
    ax1.set_title("(a)", fontsize=8, loc="left")
    ax2.set_title("(b)", fontsize=8, loc="left")
    pairs = [("Ge", "GaSb"), ("ZnO", "GaN"), ("CsI", "AlN"), ("NaCl", "Al2O3"), ("NaF", "CaF2")]
    SP = 0.2  # each pair gets 20 % of relative width
    for k, (a, b) in enumerate(pairs):
        ref = rec[a]["med"]
        x0 = k * SP
        ax3.axvline(x0, color="0.85", lw=0.6, zorder=0)
        for dy, n in ((0.12, a), (-0.12, b)):
            r = rec[n]
            c = cols[r["tier"] - 1]
            ax3.plot([x0 + r["lo"] / ref - 1, x0 + r["hi"] / ref - 1], [dy, dy], color=c, lw=4, solid_capstyle="butt")
            ax3.text(x0 + r["hi"] / ref - 1 + 0.004, dy, lab.get(n, n), va="center", fontsize=6)
        ax3.text(x0 - 0.035, -0.42, r"$P = %.2f$" % pair(S, a, b, "L"), fontsize=6, ha="left")
    ax3.set_xlim(-0.05, len(pairs) * SP - 0.05)
    ax3.set_ylim(-0.55, 0.4)
    ax3.set_yticks([])
    ax3.set_xticks([k * SP + t for k in range(len(pairs)) for t in (-0.04, 0.0, 0.04, 0.08)])
    ax3.set_xticklabels(["$-4$", "0", "4", "8"] * len(pairs), fontsize=6)
    ax3.set_xlabel(r"68 % interval of $m_{\mathrm{floor}}$ relative to the median of the upper member (%)")
    ax3.set_title("(c)", fontsize=8, loc="left")
    fig.subplots_adjust(left=0.11, right=0.98, top=0.96, bottom=0.08)
    os.makedirs(FIG, exist_ok=True)
    fig.savefig(os.path.join(FIG, "fig17_5.pdf"))
    print("\nwrote fig17_5.pdf")


if __name__ == "__main__":
    main()
