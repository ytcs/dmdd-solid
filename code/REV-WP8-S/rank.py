"""REV-WP8-S (WP8-S v2): substrate ranking per interaction channel with propagated uncertainties.

Starts from code/CW7/rank.py (R16 CW7 §12) and replaces it. Inputs (the current ones only):
  returns/R16/WP8-U-table-v4.csv          properties, verdicts, S4 rows (reading rule of WP8-U-v3 §0: last "supersedes" row wins;
                                           GAP:<x>_vetted rows override the DB value they name)
  code/CW7/data/christoffel_v4.json       Voigt-ordered (shear-order-fixed) Christoffel speeds: c_nr1 (= c_NR1_heavy), cLA_max, cLA
  code/GAP-EF-v2/data/results.json        eps_eh, F_eh predictions with bands (GAP-EF-v2 §3; the errata leave the table unchanged)
  returns/R16/WP8-F-v3.md                 the FOMs (§0, §2.3 (2.3a''), §2.5, §2.7 (2.7'), §5.1) and the needed accuracies (§5.2)
Every number written is [E] from tagged inputs. Uncertainty model (declared in WP8-S-v2 §1):
  [FT] measured  -> stated error, else the family width below;  [FT] DFT-in-paper -> family width;  [DB] -> family width derived
  from this table where both a DB and a non-DB value exist;  [E] model values (GAP-EF, plasmon pole, room->0 K shifts) -> wide.
Propagation: Monte Carlo, N_MC draws, independent per material (r_mat = 0: the conservative choice for rankings when the
elasticities have the same sign, CONVENTIONS row 29 as re-issued in CW7-errata §2.1), one common halo draw (r = 1).
Tiers: interval order on the 68% intervals (A beats B iff A's interval lies wholly on the better side of B's); tier = height in that
order (each tier is an antichain: no member resolves any other).  Runtime ~5 s.

R17 ERR-WP8 revision (v3; writes data/ranking_v3.json, ranking_v2.json is left untouched).  Input changes (WP8-errata §§3-12):
  CaWO4  measured C_ij [FT 2508.08858 p.16, quoting Farley & Saunders 1972] -> Christoffel c_NR1, c_LA,max (replaces the 1910.10716 proxy);
  CsI    1910.10716 c_LA 1.379 km/s lies below the bulk-modulus floor sqrt(B/rho) = 1.73 km/s (B = 13.5 GPa expt. [FT cond-mat/9408044
         Table I p.18]); replaced by c_LA = sqrt(3B(1-nu)/((1+nu)rho)), nu in U[0.20, 0.35] around the Cauchy value 1/4 [E];
  Al     measured C_ij (state/DATA-ADDENDA.csv, CW8-LIT: C44 31.6 vs DB 16.2 GPa) and rho from a_exp 4.05 A replace the v4 DB tensor;
  YIG    rho_T 5.173 g/cm3 from the measured a = 12.3750 A (DATA-ADDENDA, COD 2101364) replaces v4 4.9475;
  Si eps_eh sigma = the stated +-0.01 eV (v2 code doubled it); sapphire POL eps_inf sensitivity sigma_ln 0.03 (I_pol ∝ 1/eps_inf at fixed modes);
  r_mat: run(r_mat) correlates the draws family-wise (CONVENTIONS §13 row 29: same-method nuisances share a component
         z = sqrt(r) z_family + sqrt(1 - r) z_own; independently measured [FT] inputs stay independent); variants r = 0, 0.5, 0.9, 1;
  NR heavy window: pairwise, eta-weighted (10% criterion on R_A/R_B vs c_B/c_A), f.u.-Debye and primitive-cell q_BZ;
  NR light: first-order O(m_min^ac/m_chi) correction with the SHM constant kappa_eta."""
import csv, json, math, os, re, sys, time, zlib

import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "code/WP8-U"))
from materials import VALENCE  # noqa: E402  (the WP8-U valence convention; also used for n_e^val in the v4 table)

V4 = os.path.join(ROOT, "returns/R16/WP8-U-table-v4.csv")
CHR = json.load(open(os.path.join(ROOT, "code/CW7/data/christoffel_v4.json")))
GEF = json.load(open(os.path.join(ROOT, "code/GAP-EF-v2/data/results.json")))
OUT = os.path.join(HERE, "data", "ranking_v3.json")
ADD = list(csv.DictReader(open(os.path.join(ROOT, "state/DATA-ADDENDA.csv"))))

N_MC = int(os.environ.get("N_MC", "20000"))
SEED = 20261101
C_KMS = 299792.458
VMAX0 = 794.5 / C_KMS                     # CONVENTIONS §8
ALPHA = 1 / 137.035999
M_U = 931.494e6                           # eV
EV_CM3_G = 4.3101e18                      # eV^-3 -> eV cm^3/g
HBARC = 1973.2698                         # eV Angstrom
NA = 0.602214                             # (g/mol)/(g/cm^3) -> Angstrom^3 conversion: Omega = M/(rho*NA)
OMP = 28.816                              # hbar omega_p [eV] = OMP * sqrt(rho[g/cc] * n_e/f.u. / M[g/mol])
W_TH = 1e-3                               # eV, NR-1ph threshold of the edge row (WP8-F-v3 (2.3b) at 1 meV)

rows = list(csv.DictReader(open(V4)))
by = {}
for x in rows:
    by.setdefault(x["material"], []).append(x)


def rws(m, p):
    return [x for x in by.get(m, []) if x["property"] == p]


def num1(s):
    """a single number (optionally '~'-prefixed); ranges, lists and bounds return None (fixes the R16 first-number parser)."""
    s = str(s).strip()
    mm = re.fullmatch(r"~?\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)", s)
    return float(mm.group(1)) if mm else None


def pick(m, p, src=None, avoid=None, nondb=False):
    """reading rule: among rows of (m, p) [optionally from source src], the last whose note says 'supersedes' wins, else the first."""
    xs = [x for x in rws(m, p) if (src is None or src in x["source"]) and (avoid is None or avoid not in x["source"])
          and (not nondb or x["tag"] != "DB")]
    sup = [x for x in xs if "supersedes" in x["note"]]
    x = (sup or xs or [None])[-1 if sup else 0]
    return (num1(x["value"]), x) if x else (None, None)


# CONVENTIONS §13 row 38 (user decision, R17): S2 = >= 1 g total target mass, reachable as an array/stack of individually instrumented crystals
# of >= ~0.1 g each with demonstrated mK readout.  Re-evaluated over every S2-COND material (WP8-errata §13): only diamond had S2 as its
# sole COND and passes (0.175 g CVD crystals at mK, W-TES 16.8 eV [FT 2310.05815]); every other S2-COND material also carries an S1 or S3
# COND (or S4-COND) and keeps SURVIVOR-COND.  Array penalties are caveats, not FAILs (ARRAY_CAVEAT).
ROW38_PROMOTED = {"C": "S2 PASS under CONVENTIONS §13 row 38: 0.175 g CVD single crystals with demonstrated mK W-TES readout (16.8 eV) [FT 2310.05815 p.1]; "
                       "S1, S3 PASS and S4 PASS in v4"}
ARRAY_CAVEAT = {"C": "array of >= 6 x 0.175 g crystals for 1 g: per-crystal readout channels and thresholds; surface-to-volume x(1 g/0.175 g)^(1/3) = 1.8 "
                     "for surface backgrounds; per-crystal LEE / stress-release rates (GAP)"}


def verdict(m):
    if m in ROW38_PROMOTED:
        return "SURVIVOR"
    v = rws(m, "verdict")
    return v[-1]["value"] if v else by[m][0]["verdict"]


POOL = [m for m in by if verdict(m) in ("SURVIVOR", "SURVIVOR-COND")]
SURV = [m for m in POOL if verdict(m) == "SURVIVOR"]


def comp(m):
    x = rws(m, "composition")[0]["value"]
    return [(mm.group(1), int(mm.group(2) or 1)) for mm in (re.fullmatch(r"([A-Z][a-z]?)(\d*)", t) for t in x.split())]


def mfu(m):
    return sum(n * float(rws(m, "A[%s]" % el)[0]["value"]) for el, n in comp(m))


# ---------------- provenance families (derived from the table where possible) ----------------
def addenda(m, p):
    xs = [x for x in ADD if x["material"] == m and x["property"] == p]
    return xs[-1] if xs else None


def rho_best(m):
    """V6: [FT] measured > [E] from a_exp > [DB] DFT density; returns (value, tag, sigma_ln).
    R17: state/DATA-ADDENDA.csv supersedes v4 (YIG rho from the measured a = 12.3750 A; Al rho from a_exp 4.05 A, fcc, 4 atoms)."""
    x = addenda(m, "rho_T_from_a_exp_measured")
    if x:
        return float(x["value"]), "E (a_exp measured, DATA-ADDENDA: %s)" % x["source"][:30], 0.005
    if m == "Al" and addenda("Al", "a_exp"):
        a = float(addenda("Al", "a_exp")["value"])
        return 4 * float(rws("Al", "A[Al]")[0]["value"]) / (NA * a ** 3), "E (a_exp 4.05 A FT 2109.13551, DATA-ADDENDA)", 0.005
    v, x = pick(m, "rho_T")
    if v is not None:
        return v, "FT " + x["source"], 0.005
    v, x = pick(m, "rho_T_from_a_exp")
    if v is not None:
        return v, "E (a_exp FT)", 0.005
    v, x = pick(m, "rho_T_DFT")
    if v is not None:
        return v, "DB (OptB88vdW cell; DFT proxy)", None   # family width filled below
    return None, "GAP", None


_r = [math.log(pick(m, "rho_T_DFT")[0] / rho_best(m)[0]) for m in by if pick(m, "rho_T_DFT")[0] and rho_best(m)[1][:2] != "DB"
      and not addenda(m, "rho_T_from_a_exp_measured") and m != "Al"]       # v2 family width kept (DATA-ADDENDA rows excluded)
SIG = {
    "rho_DB": float(np.sqrt(np.mean(np.square(_r)))),               # DB density vs measured / a_exp
    "c_DB": None,                                                    # below
    "eps_DB": math.log(1.15),                                        # "±15% DB eps fields" (WP8-F-v3 §2.5)
    "omega_DB": 0.05,                                                # DFPT Gamma frequencies [E]
    "FT_DFT_Zstar": 0.07, "FT_DFT_eps": 0.07, "FT_DFT_omega": 0.05,  # 1910.10716 DFPT numbers, no stated errors [E family]
    "FT_DFT_c_suspect": 0.30,                                        # v2 only (CsI, CaWO4 proxies); not used in v3
    "C_meas": 0.02,                                                  # measured (ultrasonic) C_ij, secondary quote, T not stated -> sigma_ln of the speeds [E]
    "B_CSI": 0.07,                                                   # CsI expt. bulk modulus (EOS fit, secondary quote) [E]
    "nu_CsI": (0.20, 0.35),                                          # Poisson ratio band around the Cauchy value 1/4 [E]
    "iso_CsI": 0.05,                                                 # isotropic-modulus -> sphere-average c_LA and branch factor [E]
    "eps_inf_sapphire": 0.03,                                        # I_pol ∝ 1/eps_inf at fixed modes; eps_inf 3.1-3.3 (VER-WP8-S-v2 row 8)
    "Eg_meas": 0.01,                                                 # measured gap, needed accuracy 1% (WP8-F-v3 §5.2)
    "pole_X": (1.0, 3.0),                                            # Migdal: true/pole ratio, log-uniform [E] (WP8-F-v3 §2.7)
    "dEg_room_to_0K": (0.03, 0.10),                                  # eV, uniform [E]; bracketed by Si 1.127->1.169 and Ge 0.67->0.73(77 K)
    "deps_dEg": (1.6, 2.8),                                          # d eps_eh / d E_g [E]: GAP-EF-v2 slope 1.61 .. Klein 2.8
    "halo_vmax": 0.045,                                              # common v_max band 2-7% (WP8-F-v3 §4), sigma_ln, r = 1
}
_c = [math.log(float(x["value"])) for x in rows if x["property"] == "c_LA_check_1910"] + [math.log(1.20), math.log(1.08)]
SIG["c_DB"] = float(np.sqrt(np.mean(np.square(_c))))               # Christoffel(DB) vs 1910 (17 rows) + like-for-like DB/FT c_L

from scipy.stats import norm as _norm  # noqa: E402

R_MAT = 0.0
COMMON = {}


def reset(r_mat=0.0):
    """reseed and set the family correlation r_mat (CONVENTIONS §13 row 29). Every input is rebuilt after this call."""
    global rng, HALO, VMAX, R_MAT, COMMON
    rng = np.random.default_rng(SEED)
    R_MAT, COMMON = float(r_mat), {}
    HALO = np.exp(SIG["halo_vmax"] * rng.standard_normal(N_MC))     # common factor on v_max (one draw per MC sample, all materials)
    VMAX = VMAX0 * HALO


def Z(fam=None):
    """standard normal draws; fam = a same-method nuisance family: z = sqrt(r) z_fam + sqrt(1 - r) z_own (marginal unchanged)"""
    z = rng.standard_normal(N_MC)
    if fam is None or R_MAT == 0.0:
        return z
    if fam not in COMMON:
        COMMON[fam] = np.random.default_rng(zlib.crc32(fam.encode()) + SEED).standard_normal(N_MC)
    return math.sqrt(R_MAT) * COMMON[fam] + math.sqrt(1 - R_MAT) * z


def U(a, b, fam=None):
    return a + (b - a) * _norm.cdf(Z(fam))


def lnN(x0, s, fam=None):
    return x0 * np.exp(s * Z(fam))


def split(x0, lo, hi, fam=None):
    z = Z(fam)
    return x0 * np.exp(np.where(z > 0, z * math.log(hi / x0), z * math.log(x0 / lo)))


def logu(a, b, fam=None):
    return np.exp(U(math.log(a), math.log(b), fam))


reset(0.0)


S4 = {}
for m in POOL:
    f = []
    s4 = [x["value"] for x in rws(m, "S4_verdict")]
    if s4 and s4[0] == "COND":
        f.append({"TeO2": "S4-COND (123Te EC)", "PbTe": "S4-COND (EC T1/2 limit)", "ZrTe5": "S4-COND (123Te EC)",
                  "Cr2O3": "S4-COND (50Cr EC)"}.get(m, "S4-COND"))
    if rws(m, "S4_cond_Pb210"):
        f.append("S4-COND (bulk 210Pb <~ 1.5 mBq/kg needed)")
    if rws(m, "flag_rho_T_DFT_proxy"):
        f.append("rho DFT proxy")
    S4[m] = f

NOTRANK = {m: [x["value"] for x in rws(m, "GAP:channel_inputs")] for m in POOL}


# =============================== channel inputs ===============================
def er_edge_inputs():
    out, nr = {}, {}
    for m in POOL:
        if m == "Si":
            et = rws(m, "E_g_T")[0]
            out[m] = dict(Eg=1.169, T="0 K", src="FT 2004.10709 Table I p.5 (E_g_T)", draw=lambda: lnN(1.169, SIG["Eg_meas"]))
            continue
        if m == "Ge":   # [FT] (1909.05806 p.15, as read by GAP-EF-v2 §2) (77 K); 77 K -> 0 K adds <= 15 meV [E]
            out[m] = dict(Eg=0.73, T="77 K (+0-15 meV to 0 K)", src="FT (1909.05806 p.15, as read by GAP-EF-v2 §2)",
                          draw=lambda: lnN(0.73, SIG["Eg_meas"]) + U(0, 0.015, "dEg"))
            continue
        xs = [x for x in rws(m, "E_g") if x["tag"] == "FT" and num1(x["value"])]
        if not xs:
            nr[m] = "no measured E_g (DFT gaps excluded by V1)" if m not in ("Al", "Nb") else "superconductor: floor 2*Delta_BCS (SC line)"
            continue
        low = [x for x in xs if "low T" in x["note"]]
        x = (low or xs)[0]
        e0 = num1(x["value"])
        if low:
            out[m] = dict(Eg=e0, T="low T ('*')", src="FT %s %s" % (x["source"].replace("arXiv:", ""), x["locator"]),
                          draw=(lambda e0=e0: lnN(e0, SIG["Eg_meas"])))
        else:
            a, b = SIG["dEg_room_to_0K"]
            out[m] = dict(Eg=e0, T="room T + [0.03, 0.10] eV shift to 0 K [E]", src="FT %s %s" % (x["source"].replace("arXiv:", ""), x["locator"]),
                          draw=(lambda e0=e0: lnN(e0, SIG["Eg_meas"]) + U(a, b, "dEg")))
    return out, nr


def eps_inputs():
    a, b = SIG["dEg_room_to_0K"]
    k0, k1 = SIG["deps_dEg"]
    sh = lambda: U(a, b, "dEg") * U(k0, k1, "deps_dEg")  # noqa: E731   room-T value -> T_op (same [E] model for all: one family each)
    meas = {
        "Si": (3.72, "5 K and 6-70 K", "FT 2004.10709 Table I p.5 (+-0.01 as stated; v2 code doubled it)", lambda: lnN(3.72, 0.01 / 3.72)),
        "Ge": (3.37, "50 mK (model-dependent)", "FT 1602.08005 p.12 (+-0.01; widened to the p.11 value 3.32)", lambda: lnN(3.37, 0.05 / 3.37)),
        "GaAs": (4.2, "25 C (+ shift to T_op)", "FT Del Sordo 2009 Table 1 (compilations 4.2-4.3)", lambda: lnN(4.2, 0.015) + sh()),
        "C": (12.95, "room T (+ shift)", "FT 2311.05011 p.30 (4 values 12.82-13.25, weighted mean)", lambda: lnN(12.95, 0.012) + sh()),
        "SiC-4H": (7.83, "25 C (+ shift)", "FT 2311.03902 Table 1 p.2 (+-0.02)", lambda: lnN(7.83, 0.003) + sh()),
        "SiC-3C": (6.9, "T not stated (+ shift)", "FT 2610.16949 Table II (Makarov 1975)", lambda: lnN(6.9, 0.05) + sh()),
        "SiC-6H": (6.7, "T not stated (+ shift)", "FT 2008.08560 Table I (secondary quote)", lambda: lnN(6.7, 0.05) + sh()),
        "GaN": (9.59, "room T EBIC (+ shift)", "FT (2308.03893 pp.18-19, as read by GAP-EF-v2 §2); 8.9 compilation sets sigma", lambda: lnN(9.59, math.log(9.59 / 8.9)) + sh()),
    }
    out, nr = {}, {}
    pr = GEF["predictions"]
    alias = {"SiC-4H": "4H-SiC"}
    for m in POOL:
        if m in meas:
            v, T, s, d = meas[m]
            out[m] = dict(eps=v, T=T, src=s, tag="FT", draw=d)
            continue
        if m in pr:
            p = pr[m]
            egT = "low-T gap" if m in ("PbTe", "PbS", "PbSe", "C", "GaN", "ZnS") else ("DFT gap proxy [DB], 0 K" if "DB" in p["prov"] else "room-T gap")
            if egT == "room-T gap":
                d = (lambda p=p: split(p["eps"], p["eps_lo"], p["eps_hi"], "GAPEF") + sh())
                T = "T of its E_g input: room T (+ shift to T_op)"
            else:
                d = (lambda p=p: split(p["eps"], p["eps_lo"], p["eps_hi"], "GAPEF"))
                T = "T of its E_g input: " + egT
            out[m] = dict(eps=p["eps"], lo=p["eps_lo"], hi=p["eps_hi"], T=T, src="E GAP-EF-v2 §3 (results.json; E_g %s)" % p["prov"][:40], tag="E", draw=d)
            continue
        nr[m] = "no measured eps_eh and no GAP-EF input (E_g or omega_0 GAP)"
    F = {"Si": (0.119, "FT 2004.11499 (123 K)"), "Ge": (0.14, "FT 1602.08005 (50 mK, model-dependent)"),
         "SiC-4H": (0.1, "FT 2311.03902 (conflict with <= 0.04)")}
    for m, d in out.items():
        if m in F:
            d["F"], d["F_src"] = F[m]
        elif m in pr or alias.get(m) in pr:
            p = pr.get(m) or pr[alias[m]]
            d["F"], d["F_src"] = p["F"], "E GAP-EF-v2 (%.3f-%.3f)" % (p["F_lo"], p["F_hi"])
    return out, nr


def qbz(m, rho):
    """Debye wavevector of one formula unit, an upper estimate of q_BZ [E]"""
    om = mfu(m) / (rho * NA)
    return HBARC * (6 * math.pi ** 2 / om) ** (1 / 3)


_mix = np.median([v["c_nr1"] / v["cLA"] for k, v in CHR.items() if k in POOL and v["crys"] == "cubic"])
_mx = np.median([v["cLA_max"] / v["cLA"] for k, v in CHR.items() if k in POOL and v["crys"] == "cubic"])


def C4of(Cv):
    I = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (1, 2): 3, (2, 1): 3, (0, 2): 4, (2, 0): 4, (0, 1): 5, (1, 0): 5}
    C = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    C[i, j, k, l] = Cv[I[(i, j)], I[(k, l)]]
    return C


def christoffel(Cv, rho, N=40000, seed=1):
    """Christoffel speeds (km/s) from a Voigt tensor (GPa) and rho (g/cm3): sphere-mean c_LA, its range, c_NR1 = <sum_nu (q.e_nu)^2/c_nu>^-1
    (the christoffel_v4 / CW7-C34 construction)."""
    nn = np.random.default_rng(seed).normal(size=(N, 3))
    nn /= np.linalg.norm(nn, axis=1)[:, None]
    G = np.einsum("ijkl,nj,nl->nik", C4of(np.asarray(Cv, float)), nn, nn) * 1e9 / (rho * 1e3)
    w, Uv = np.linalg.eigh(G)
    c = np.sqrt(w) / 1e3
    proj = np.einsum("nk,nkv->nv", nn, Uv) ** 2
    return dict(cLA=float(c[:, 2].mean()), cLA_min=float(c[:, 2].min()), cLA_max=float(c[:, 2].max()), c_nr1=float(1 / np.mean(np.sum(proj / c, axis=1))),
                cT_min=float(c[:, 0].min()), posdef=bool(np.linalg.eigvalsh(np.asarray(Cv, float)).min() > 0))


# measured tensors (R17)
_c = dict(C11=145.9, C33=127.4, C12=62.6, C13=39.2, C16=-19.2, C44=33.5, C66=38.7)      # CaWO4, 4/m (C26 = -C16) [FT 2508.08858 p.16 <- Farley & Saunders 1972]
CV_CAWO4 = [[_c["C11"], _c["C12"], _c["C13"], 0, 0, _c["C16"]], [_c["C12"], _c["C11"], _c["C13"], 0, 0, -_c["C16"]], [_c["C13"], _c["C13"], _c["C33"], 0, 0, 0],
            [0, 0, 0, _c["C44"], 0, 0], [0, 0, 0, 0, _c["C44"], 0], [_c["C16"], -_c["C16"], 0, 0, 0, _c["C66"]]]
_al = dict(kv.split("=") for kv in addenda("Al", "C_ij_exp_0K")["value"].replace(" ", "").split(";"))
_a11, _a12, _a44 = float(_al["C11"]), float(_al["C12"]), float(_al["C44"])
CV_AL = [[_a11, _a12, _a12, 0, 0, 0], [_a12, _a11, _a12, 0, 0, 0], [_a12, _a12, _a11, 0, 0, 0], [0, 0, 0, _a44, 0, 0], [0, 0, 0, 0, _a44, 0], [0, 0, 0, 0, 0, _a44]]
CHR_MEAS = {"CaWO4": christoffel(CV_CAWO4, rho_best("CaWO4")[0]), "Al": christoffel(CV_AL, rho_best("Al")[0])}
B_CSI = 13.5                                                   # GPa, expt. [FT cond-mat/9408044 Table I p.18, citing its ref. [11]]
RHO_CSI = rho_best("CsI")[0]
CSI_FLOOR = math.sqrt(B_CSI * 1e9 / (RHO_CSI * 1e3)) / 1e3     # km/s: c_LA >= sqrt(B/rho) in every direction (cubic) [D]
CSI_CAUCHY = CSI_FLOOR * math.sqrt(3 * 0.75 / 1.25)            # nu = 1/4 (Cauchy relation C12 = C44 + isotropy) [D]
C_1910 = {m: pick(m, "c_LA")[0] for m in ("CsI", "CaWO4")}
# f.u. per primitive cell (standard crystallography [E, not from a text read]); q_BZ(prim) = q_BZ(f.u.)/Z_prim^(1/3)
Z_PRIM = dict(Si=2, Ge=2, C=2, GaAs=1, GaSb=1, ZnS=1, NaF=1, LiF=1, NaCl=1, NaI=1, CsI=1, MgO=1, NiO=1, CaF2=1, PbTe=1, PbS=1, PbSe=1, SrTiO3=1, cBN=1,
              Al=1, Nb=1, Bi2Se3=1, MgF2=2, GaN=2, AlN=2, ZnO=2, hBN=2, Al2O3=2, CaWO4=2, LiAlO2=4, TeO2=4, PE=4, **{"SiO2-q": 3, "SiC-3C": 1, "SiC-4H": 4, "SiC-6H": 6})


def nr_inputs():
    out, nr = {}, {}
    for m in POOL:
        rho = rho_best(m)[0]
        if m in CHR_MEAS:
            c = CHR_MEAS[m]
            out[m] = dict(c_nr1=c["c_nr1"], c_max=c["cLA_max"], cLA=c["cLA"], src="FT measured C_ij (%s) + Christoffel; rho %s" % (
                "2508.08858 p.16 <- Farley & Saunders 1972" if m == "CaWO4" else "DATA-ADDENDA: 2109.13551 Table 2 <- Kamm & Alers 1964; supersedes v4 DB (C44 16.2)",
                rho_best(m)[1]), tag="FT (measured C_ij)", s=SIG["C_meas"], fam=None)
        elif m in CHR:
            c = CHR[m]
            out[m] = dict(c_nr1=c["c_nr1"], c_max=c["cLA_max"], cLA=c["cLA"], src="E (christoffel_v4: Voigt-ordered JARVIS C_ij, rho_DFT)", tag="E/DB",
                          s=SIG["c_DB"], fam="c_DB")
        elif m == "CsI":
            out[m] = dict(c_nr1=CSI_CAUCHY * _mix, c_max=CSI_CAUCHY * _mx, cLA=CSI_CAUCHY, floor=CSI_FLOOR, c_1910=C_1910["CsI"],
                          src="B-floor model: c_LA = sqrt(3B(1-nu)/((1+nu)rho)), B 13.5 GPa expt. [FT cond-mat/9408044 Table I p.18], nu U[0.20,0.35] [E], x median cubic branch factor; "
                              "1910.10716 c_LA 1.379 km/s < floor %.3f km/s (rejected)" % CSI_FLOOR, tag="E from FT B", s=None, fam=None)
        else:
            nr[m] = "no elastic tensor (" + ("V5 fails" if m == "MnO" else "GAP") + ")"
            continue
        if rho:
            q = qbz(m, rho)
            out[m]["q_BZ_eV"] = q
            out[m]["q_BZ_prim_eV"] = q / Z_PRIM.get(m, 1) ** (1 / 3)
    for m, d in out.items():
        if m == "CsI":
            nu = U(*SIG["nu_CsI"])
            cl = CSI_FLOOR * np.exp(0.5 * SIG["B_CSI"] * Z()) * np.sqrt(3 * (1 - nu) / (1 + nu)) * np.exp(SIG["iso_CsI"] * Z())
            d["draw_c"] = (lambda cl=cl: cl * _mix)
            d["draw_cmax"] = (lambda cl=cl: cl * _mx)
            continue
        z = Z(d["fam"])
        d["draw_c"] = (lambda d=d, z=z: d["c_nr1"] * np.exp(d["s"] * z))
        d["draw_cmax"] = (lambda d=d, z=z: d["c_max"] * np.exp(d["s"] * z))     # same draw z: one tensor per material
    return out, nr


def modesum(einf, wL, wT):
    wL, wT = np.asarray(wL, float), np.asarray(wT, float)
    tot, D = 0.0, []
    for j, l in enumerate(wL):
        B = np.prod(wT ** 2 - l ** 2) / np.prod([wL[k] ** 2 - l ** 2 for k in range(len(wL)) if k != j]) / einf
        D.append(-B / l ** 2)
        tot += math.pi * l / 2 * D[-1]
    return tot, D


def zstar_route(m, rho):
    cp = comp(m)
    if len(cp) != 2 or cp[0][1] != 1 or cp[1][1] != 1:
        return None
    zs, xz = pick(m, "Zstar_bar", src="1910.10716")
    ei, _ = pick(m, "eps_inf", src="1910.10716")
    w, _ = pick(m, "omega_O_max", src="1910.10716")
    if not (zs and ei and w):
        return None
    m1, m2 = (float(rws(m, "A[%s]" % el)[0]["value"]) * M_U for el, _ in cp)
    mu = m1 * m2 / (m1 + m2)
    val = (math.pi / 2) * 4 * math.pi * ALPHA * zs ** 2 / ((m1 + m2) * mu * ei ** 2 * w * 1e-3) * EV_CM3_G * 1e3
    # rigid-ion LST cross-check: omega_L^2 - omega_T^2 = 4 pi alpha (hbar c)^3 Z*^2 / (eps_inf mu Omega_cell)  (REF-WP8-S-A §6(d))
    rho = rho_best(m)[0]
    om = mfu(m) / (rho * NA)
    d2 = 4 * math.pi * ALPHA * HBARC ** 3 * zs ** 2 / (ei * mu * om)
    wT = math.sqrt(max((w * 1e-3) ** 2 - d2, 0.0)) * 1e3
    return dict(I=val, w=w, zs=zs, ei=ei, omega_T_LST=wT)


SINGLE_BRANCH_CUBIC = {"MgO", "NaF", "NaCl", "NaI", "LiF", "PbS", "PbSe", "PbTe", "NiO", "MnO", "CsI", "GaAs", "GaSb", "ZnS",
                       "SiC-3C", "cBN", "CaF2"}


def pol_inputs():
    out, nr, bound = {}, {}, {}
    cm = 0.1239842
    for m in POOL:
        rho, rtag, rs = rho_best(m)
        rf = "rho_DB" if rs is None else None
        rs = rs if rs is not None else SIG["rho_DB"]
        if m in ("Si", "Ge", "C"):
            nr[m] = "non-polar (Z* = 0 [D]); quadrupolar vertex, dynamical quadrupoles GAP"
            continue
        if m in ("Al", "Nb"):
            nr[m] = "metal: polar coupling screened (no optical-phonon POL channel)"
            continue
        if m == "Al2O3":   # FT 1807.10291 Table II p.31: lossless per-axis mode sums, axis average (1/3)(2 o + e), Eq. (40)
            o_L, o_T = np.array([906.6, 629.5, 481.7, 387.6]) * cm, np.array([633.6, 569.0, 439.1, 385.0]) * cm
            e_L, e_T = np.array([881.1, 510.9]) * cm, np.array([582.4, 397.5]) * cm
            Io, Do = modesum(3.2, o_L, o_T)
            Ie, De = modesum(3.2, e_L, e_T)
            I = (2 * Io + Ie) / 3 / 3.98
            wts = sorted([(o_L[j], 2 * math.pi * o_L[j] / 2 * Do[j]) for j in range(4)] + [(e_L[j], math.pi * e_L[j] / 2 * De[j]) for j in range(2)])
            tot = sum(w for _, w in wts)
            w_edge = min(l for l, w in wts if w / tot >= 0.05)
            AL2O3_W = [(float(l), float(w / tot)) for l, w in wts]
            out[m] = dict(I=I, route="FT mode sum (1807.10291 Table II, lossless, axis-averaged; one eps model per axis)", tag="E from FT",
                          w_edge=float(o_L.min()), w_edge5=float(w_edge), branch_weights=AL2O3_W, draw=(lambda I=I: I * U(1.0, 1.03) * np.exp(0.005 * Z()) * np.exp(SIG["eps_inf_sapphire"] * Z())), wsrc="FT 1807.10291: lowest LO carrying >= 5%% of I_pol (e-ray 881.1 cm-1); the lowest LO, 387.6 cm-1, carries %.2g%%" % (100 * min(w for _, w in wts) / tot))
            continue
        if m == "GaAs":    # WP8-F-v3 §2.5: measured eps pair (1807.10291 Table I) + LST, 0.144-0.153
            out[m] = dict(I=0.1485, route="FT measured eps pair + LST (WP8-F-v3 §2.5: 0.144-0.153)", tag="E from FT", w_edge=34.9, w_edge5=34.9,
                          draw=lambda rs=rs, rf=rf: U(0.144, 0.153) * np.exp(rs * Z(rf)), wsrc="FT 1910.10716 omega_L 34.9 meV (LST 36.2 with omega_TO 33.3 [UNVERIFIED])")
            continue
        if m in ("SiC-3C", "SiC-4H", "SiC-6H"):   # FT 2008.08560 Table I: measured per-axis eps pair and omega_L (LST-consistent to 1.2%, CW7-C28)
            if m == "SiC-3C":
                ax = [(6.5, 9.7, 120.5)] * 3
            elif m == "SiC-4H":
                ax = [(6.6, 9.76, 120.0), (6.6, 9.76, 120.0), (6.8, 10.32, 119.5)]
            else:
                ax = [(6.6, 9.67, 120.3), (6.6, 9.67, 120.3), (6.7, 10.03, 119.7)]
            I = sum((math.pi / 2) * (1 / a - 1 / b) * w for a, b, w in ax) / 3 / 3.2
            out[m] = dict(I=I, route="FT measured per-axis eps pair and omega_L (2008.08560 Table I), single branch per axis", tag="E from FT",
                          w_edge=min(w for _, _, w in ax), w_edge5=min(w for _, _, w in ax), draw=(lambda I=I, rs=rs, rf=rf: I * np.exp(0.03 * Z() + rs * Z(rf))),
                          wsrc="FT 2008.08560 omega_L")
            continue
        zr = zstar_route(m, rho) if rho else None
        ei, _ = pick(m, "eps_inf_DFT")
        xei = [x for x in rws(m, "eps_inf_DFT") if "dfpt" in x["locator"]]
        e0, _ = pick(m, "eps_0_DFT")
        vet = bool(rws(m, "GAP:eps_0_DFT_vetted"))
        wT, _ = pick(m, "omega_T_maxIR_DFT")
        db = None
        if xei and e0 and not vet and wT and e0 > ei and rho:
            D = 1 / ei - 1 / e0
            wL = wT * math.sqrt(e0 / ei)
            if m in SINGLE_BRANCH_CUBIC:
                db = dict(I=(math.pi / 2) * D * wL / rho, wL=wL, exact=True, D=D)
            else:
                wlo, _ = pick(m, "omega_O_min", src="1910.10716")
                db = dict(ub=(math.pi / 2) * D * wL / rho, lb=((math.pi / 2) * D * wlo / rho) if wlo else None, wL=wL, wlo=wlo, exact=False, D=D)
        if zr and db and db.get("exact"):
            Ic = math.sqrt(zr["I"] * db["I"])
            half = abs(math.log(zr["I"] / db["I"])) / 2
            sZ = math.sqrt((2 * SIG["FT_DFT_Zstar"]) ** 2 + (2 * SIG["FT_DFT_eps"]) ** 2 + SIG["FT_DFT_omega"] ** 2)
            s_m = math.sqrt((sZ ** -2 + 1.0 / ((1.5 * SIG["eps_DB"]) ** 2 + SIG["omega_DB"] ** 2)) ** -1)
            s = math.sqrt(half ** 2 + s_m ** 2 + rs ** 2)
            out[m] = dict(I=Ic, route="two routes: Z* (FT 1910.10716 DFPT) %.3g and same-run DB eps pair + LST %.3g; geometric mean, half-spread added" % (zr["I"], db["I"]),
                          tag="E from FT-DFT + DB", w_edge=min(zr["w"], db["wL"]), w_edge5=min(zr["w"], db["wL"]),
                          draw=(lambda Ic=Ic, h_=half, s_m=s_m, rs=rs, rf=rf: Ic * np.exp(h_ * Z() + s_m * Z("pol_method") + rs * Z(rf))),
                          wsrc="min(omega_O,max FT-DFT, LST omega_L DB)")
        elif db and db.get("exact"):
            s = math.sqrt((1.5 * SIG["eps_DB"]) ** 2 + SIG["omega_DB"] ** 2)
            out[m] = dict(I=db["I"], route="same-run DB eps pair (eps_inf, eps_0, omega_T,maxIR) + LST, single polar branch (exact for one branch)",
                          tag="E from DB", w_edge=db["wL"], w_edge5=db["wL"], draw=(lambda I=db["I"], s=s, rs=rs, rf=rf: I * np.exp(s * Z("eps_DB") + rs * Z(rf))), wsrc="LST omega_L (DB)")
        elif zr:
            sZ = math.sqrt((2 * SIG["FT_DFT_Zstar"]) ** 2 + (2 * SIG["FT_DFT_eps"]) ** 2 + SIG["FT_DFT_omega"] ** 2)
            out[m] = dict(I=zr["I"], route="Z* route (2.5b), FT 1910.10716 DFPT Z*, eps_inf, omega_O,max as omega_LO", tag="E from FT-DFT", omega_T_LST=zr["omega_T_LST"],
                          w_edge=zr["w"], w_edge5=zr["w"], draw=(lambda I=zr["I"], s=sZ, rs=rs, rf=rf: I * np.exp(s * Z("FT_DFT") + rs * Z(rf))), wsrc="FT-DFT omega_O,max")
            if m in SINGLE_BRANCH_CUBIC and vet:
                out[m]["route"] += "; DB eps_0 fails V2"
        elif db and not db.get("exact"):
            lab = "orientation-maximal (V4)"
            if db["lb"]:
                out[m] = dict(I=math.sqrt(db["ub"] * db["lb"]), lo=db["lb"], hi=db["ub"], tag="E from DB (multi-branch interval)",
                              route="(8.1)-type interval on one DB eps pair: [(pi/2)D omega_O,min, (pi/2)D omega_T,max sqrt(eps0/eps_inf)]/rho, %s" % lab,
                              w_edge=db["wlo"], w_edge5=db["wlo"], draw=(lambda a=db["lb"], b=db["ub"], rs=rs, rf=rf: logu(a, b) * np.exp(1.5 * SIG["eps_DB"] * Z("eps_DB") + rs * Z(rf))),
                              wsrc="FT-DFT omega_O,min (lower estimate of the lowest LO)")
            else:
                bound[m] = dict(ub=db["ub"], note="upper bound only (no lower frequency in the table), %s" % lab)
                nr[m] = "multi-branch: only an upper bound <= %.3g (no omega_T,min), %s" % (db["ub"], lab)
        else:
            nr[m] = "no Z* and no V2-valid eps pair (GAP)"
    for m, d in out.items():
        d["edge_keV"] = 2 * d["w_edge5"] * 1e-3 / VMAX0 ** 2 / 1e3              # lowest branch carrying >= 5% of I_pol
        d["edge_kin_keV"] = 2 * d["w_edge"] * 1e-3 / VMAX0 ** 2 / 1e3          # lowest branch with any weight
    return out, nr, bound


def migdal_inputs():
    out, nr, nio = {}, {}, {}
    for m in POOL:
        rho, rtag, rs = rho_best(m)
        if not rho:
            nr[m] = "rho GAP"
            continue
        rf = "rho_DB" if rs is None else None
        rs = rs if rs is not None else SIG["rho_DB"]
        cp = comp(m)
        M = mfu(m)
        z2 = sum(n * VALENCE[el] ** 2 for el, n in cp)
        zv = sum(n * VALENCE[el] for el, n in cp)
        wp = OMP * math.sqrt(rho * zv / M)
        nuc = z2 / M
        eg = None
        xs = [x for x in rws(m, "E_g") if x["tag"] == "FT" and num1(x["value"])]
        if xs:
            eg = num1(xs[0]["value"])
        out[m] = dict(nuc=nuc, wp=wp, zv=zv, z2=z2, F=nuc * wp ** -3, rho=rho, rtag=rtag,
                      fsum_ub=(nuc * (math.pi / 2) * wp ** 2 / eg ** 5) if eg else None,
                      draw=(lambda nuc=nuc, rho=rho, zv=zv, M=M, rs=rs, rf=rf: nuc * (OMP * np.sqrt(rho * np.exp(rs * Z(rf)) * zv / M)) ** -3 * logu(*SIG["pole_X"], "pole_X")))
    # NiO valence convention: Ni = 10 (3d8 4s2, the WP8-U VALENCE) vs 2 (4s2) vs 18 (3s3p3d4s), with Z_ion and n_e^val from the same split
    rho = rho_best("NiO")[0]
    M = mfu("NiO")
    for zni in (2, 10, 18):
        z2, zv = zni ** 2 + 36, zni + 6
        nio[zni] = dict(consistent=z2 / M * (OMP * math.sqrt(rho * zv / M)) ** -3, nuclear_only=z2 / M)
    return out, nr, nio


# =============================== NR-1ph rate integrals (CONVENTIONS §8 SHM eta) ===============================
_V0, _VESC, _VE = 238 / C_KMS, 544 / C_KMS, 250.5 / C_KMS
_v = np.linspace(1e-7, _VESC + _VE, 40001)
_mu = np.clip((_VESC ** 2 - _v ** 2 - _VE ** 2) / (2 * _v * _VE), -1, 1)
_f = _v ** 2 / (_v * _VE) * (np.exp(-(_v - _VE) ** 2 / _V0 ** 2) - np.exp(-(_v ** 2 + _VE ** 2 + 2 * _v * _VE * _mu) / _V0 ** 2)) * (_mu > -1)
_f /= np.trapezoid(_f, _v)
_g = _f / _v
_cum = np.concatenate([[0], np.cumsum((_g[1:] + _g[:-1]) / 2 * np.diff(_v))])
_eta = _cum[-1] - _cum


def eta(vmin):
    return np.interp(vmin, _v, _eta, right=0.0)


def nr_rate(c_kms, qbz_, mchi, light, n=3000):
    """(2.3a'') per mass, constants dropped: (1/c) int_{w/c}^{q_up} q^2 F^2 eta(c + q/2m) dq, q_up = min(q_BZ, 2m(v_max - c))"""
    c = c_kms / C_KMS
    qlo, qup = W_TH / c, min(qbz_, 2 * mchi * (VMAX0 - c))
    if qup <= qlo:
        return 0.0
    q = np.geomspace(qlo, qup, n)
    return float(np.trapezoid(q ** 2 * (q ** -4 if light else 1.0) * eta(c + q / (2 * mchi)) / c, q))


ETA0 = float(_eta[0])
_u = _v[_v <= VMAX0]
KAPPA_ETA = float(VMAX0 / ETA0 * np.trapezoid((ETA0 - eta(_u[1:])) / _u[1:] ** 2, _u[1:]))   # (u_+/eta0) int_0^{u_+} (eta0 - eta)/u^2 du at u_+ = v_max
MGRID = np.geomspace(0.005e6, 3e6, 140)                                                        # eV


def _window(g, tol=0.10, mcap=None):
    """the contiguous mass range (MeV) around the best point where |g - 1| < tol, capped at m_hi = min q_BZ/(2 v_max) of the pair
    (above it the q << q_BZ single-phonon form (2.3a'') itself fails: Umklapp, multiphonon), so a coincidental 10% agreement there is not used"""
    ok = np.abs(g - 1) < tol
    if mcap is not None:
        ok &= MGRID <= mcap
    if not ok.any():
        return None
    dev = np.where(MGRID <= (mcap if mcap is not None else np.inf), np.abs(g - 1), np.inf)
    i0 = int(np.argmin(dev))
    if not ok[i0]:
        return None
    a = b = i0
    while a > 0 and ok[a - 1]:
        a -= 1
    while b < len(g) - 1 and ok[b + 1]:
        b += 1
    return [float(MGRID[a] / 1e6), float(MGRID[b] / 1e6)]


def nr_windows(nr1, res):
    """heavy mediator: R_A/R_B = (c_B/c_A) within 10% -> pairwise window; per material vs Si; both q_BZ conventions."""
    out = {"NR_heavy_kappa_note": "10% criterion on (R_A/R_B)/(c_B/c_A), CONVENTIONS §8 SHM, omega_th = 1 meV"}
    for conv, key in (("fu", "q_BZ_eV"), ("prim", "q_BZ_prim_eV")):
        R = {m: np.array([nr_rate(d["c_nr1"], d[key], mm, False) for mm in MGRID]) for m, d in nr1.items() if key in d}
        vsSi = {}
        for m in R:
            with np.errstate(divide="ignore", invalid="ignore"):
                g = (R[m] / R["Si"]) / (nr1["Si"]["c_nr1"] / nr1[m]["c_nr1"])
            vsSi[m] = _window(np.nan_to_num(g, nan=0.0), mcap=min(nr1[m][key], nr1["Si"][key]) / (2 * VMAX0)) if m != "Si" else None
        pair = {}
        for pool in ("survivors", "all"):
            o = res["NR_heavy"][pool]["order"]
            for a, b in zip(o[:-1], o[1:]):
                with np.errstate(divide="ignore", invalid="ignore"):
                    g = (R[a] / R[b]) / (nr1[b]["c_nr1"] / nr1[a]["c_nr1"])
                pair["%s/%s" % (a, b)] = _window(np.nan_to_num(g, nan=0.0), mcap=min(nr1[a][key], nr1[b][key]) / (2 * VMAX0))
        def common(ms):
            ws = [vsSi[m] for m in ms if m != "Si"]
            if any(w is None for w in ws):
                return None
            return [max(w[0] for w in ws), min(w[1] for w in ws)]
        out["NR_heavy_window_vs_Si_%s_MeV" % conv] = vsSi
        out["NR_heavy_window_adjacent_%s_MeV" % conv] = pair
        out["NR_heavy_common_window_S_%s_MeV" % conv] = common(res["NR_heavy"]["survivors"]["order"])
        out["NR_heavy_common_window_all_%s_MeV" % conv] = common(res["NR_heavy"]["all"]["order"])
        out["m_min_ac_c_nr1_keV"] = {m: W_TH / (2 * (d["c_nr1"] / C_KMS) * (VMAX0 - d["c_nr1"] / C_KMS)) / 1e3 for m, d in nr1.items()}
    out["NR_heavy_common_window_S_MeV"] = out["NR_heavy_common_window_S_fu_MeV"]
    out["NR_heavy_common_window_MeV"] = out["NR_heavy_common_window_all_fu_MeV"]
    return out


def nr_light(nr1):
    """light mediator: full (2.3a'') ratio to Si at fixed masses vs the first-order formula 1 - (1 + kappa_eta) m_min^ac/m (m <= m_hi)."""
    ms = (0.1e6, 0.2e6, 0.3e6, 0.43e6, 1e6, 10e6)
    out = {"kappa_eta": KAPPA_ETA, "masses_MeV": [m / 1e6 for m in ms], "ratio_to_Si": {}, "first_order_ratio_to_Si": {}}
    for mt, d in nr1.items():
        if "q_BZ_eV" not in d:
            continue
        r = [nr_rate(d["c_nr1"], d["q_BZ_eV"], mm, True) / nr_rate(nr1["Si"]["c_nr1"], nr1["Si"]["q_BZ_eV"], mm, True) for mm in ms]
        out["ratio_to_Si"][mt] = r
        def fo(dd, mm):
            c = dd["c_nr1"] / C_KMS
            mmin = W_TH / (2 * c * (VMAX0 - c))
            return 1 - (1 + KAPPA_ETA) * mmin / mm if 2 * mm * (VMAX0 - c) <= dd["q_BZ_eV"] else None
        out["first_order_ratio_to_Si"][mt] = [(fo(d, mm) / fo(nr1["Si"], mm)) if fo(d, mm) is not None and fo(nr1["Si"], mm) is not None else None for mm in ms]
    return out


# =============================== MC, ranks, tiers ===============================
def analyse(samples, better, pool_names):
    names = [m for m in pool_names if m in samples]
    if not names:
        return {}
    X = np.array([samples[m] for m in names])
    sgn = 1.0 if better == "high" else -1.0
    Y = sgn * np.log(X)                                   # larger = better
    order = np.argsort(-Y, axis=0)
    ranks = np.empty_like(order)
    for k in range(X.shape[1]):
        ranks[order[:, k], k] = np.arange(1, len(names) + 1)
    pfirst = np.mean(ranks == 1, axis=1)
    lo, med, hi = np.percentile(X, [16, 50, 84], axis=1)
    ylo, yhi = sgn * np.log(lo if better == "high" else hi), sgn * np.log(hi if better == "high" else lo)
    idx = np.argsort(-np.median(Y, axis=1))
    height = {}
    for i in idx:                                         # interval order: j beats i iff ylo[j] > yhi[i]
        h = 1
        for j in idx:
            if ylo[j] > yhi[i] and j in height:
                h = max(h, height[j] + 1)
        height[i] = h
    res = {}
    for i in idx:
        r16, r84 = np.percentile(ranks[i], [16, 84])
        res[names[i]] = dict(median=float(med[i]), p16=float(lo[i]), p84=float(hi[i]), P_first=float(pfirst[i]),
                             rank_68=[int(round(r16)), int(round(r84))], tier=int(height[i]))
    adj = []
    for a, b in zip(idx[:-1], idx[1:]):
        adj.append([names[a], names[b], float(np.mean(Y[a] > Y[b]))])
    return dict(order=[names[i] for i in idx], rows=res, adjacent_P=adj)


def run(r_mat=0.0):
    reset(r_mat)
    er, er_nr = er_edge_inputs()
    ep, ep_nr = eps_inputs()
    nr1, nr1_nr = nr_inputs()
    pol, pol_nr, pol_bound = pol_inputs()
    mig, mig_nr, nio = migdal_inputs()
    S = {k: {} for k in ("ER_edge", "ER_quanta", "NR_heavy", "NR_edge", "POL_rate", "POL_edge", "Migdal")}
    SH = {"ER_edge": {}, "NR_edge": {}}
    for m, d in er.items():
        eg = d["draw"]()
        S["ER_edge"][m] = 2 * eg / VMAX0 ** 2 / 1e6                            # MeV, at the reference v_max (ranking samples)
        SH["ER_edge"][m] = 2 * eg / VMAX ** 2 / 1e6                            # same draws with the common halo draw (band; check S2-C7)
    for m, d in ep.items():
        S["ER_quanta"][m] = d["draw"]()
    for m, d in nr1.items():                                                   # FOM = c_NR1(Si, central) / c_NR1(m): rate relative to Si
        S["NR_heavy"][m] = nr1["Si"]["c_nr1"] / d["draw_c"]()
        cm_ = d["draw_cmax"]() / C_KMS
        S["NR_edge"][m] = W_TH / (2 * cm_ * (VMAX0 - cm_)) / 1e3                # keV
        SH["NR_edge"][m] = W_TH / (2 * cm_ * (VMAX - cm_)) / 1e3
    for m, d in pol.items():
        S["POL_rate"][m] = d["draw"]()
        S["POL_edge"][m] = 2 * d["w_edge5"] * 1e-3 * np.exp(SIG["omega_DB"] * Z(None if m in ("Al2O3", "SiC-3C", "SiC-4H", "SiC-6H") else "omega_DB")) / VMAX0 ** 2 / 1e3
    for m, d in mig.items():                                                   # relative to the Si pole value (a constant)
        S["Migdal"][m] = d["draw"]() / mig["Si"]["F"]
    better = dict(ER_edge="low", ER_quanta="low", NR_heavy="high", NR_edge="low", POL_rate="high", POL_edge="low", Migdal="high")
    res = {"N_MC": N_MC, "seed": SEED, "r_mat": r_mat, "sigma_families": SIG, "pool": POOL, "survivors": SURV,
           "verdict": {m: verdict(m) for m in POOL}, "flags": S4}
    for ch, b in better.items():
        res[ch] = {"all": analyse(S[ch], b, POOL), "survivors": analyse(S[ch], b, SURV), "better": b}
    # no-halo rerun of the ranks (the common v_max draw must not reorder: check)
    res["inputs"] = {
        "ER_edge": {m: {k: v for k, v in d.items() if k != "draw"} for m, d in er.items()},
        "ER_quanta": {m: {k: v for k, v in d.items() if k != "draw"} for m, d in ep.items()},
        "NR": {m: {k: v for k, v in d.items() if not k.startswith("draw")} for m, d in nr1.items()},
        "POL": {m: {k: v for k, v in d.items() if k != "draw"} for m, d in pol.items()},
        "Migdal": {m: {k: v for k, v in d.items() if k != "draw"} for m, d in mig.items()},
    }
    res["not_ranked"] = {"ER_edge": er_nr, "ER_quanta": ep_nr, "NR_heavy": nr1_nr, "NR_edge": nr1_nr, "POL_rate": pol_nr,
                         "POL_edge": pol_nr, "Migdal": mig_nr}
    res["POL_bounds"] = pol_bound
    res["NiO_valence"] = {str(k): v for k, v in nio.items()}
    # SC line: Delta values as owed against v4 by state/CORRECTIONS.md §19.13 (CW4-errata §B OC-11(b), (c)); not yet rows of the v4 CSV
    res["SC_line"] = {"Al": dict(Delta_meV=[0.18, 0.3], m_floor_keV=[2 * 2 * d * 1e-3 / VMAX0 ** 2 / 1e3 for d in (0.18, 0.3)],
                                 src="bulk 0.18 [E, 2305.06084 T_c; CW4-errata OC-11(b)]; 0.3 = 2109.04473 working value [FT], film-like (x1.7)"),
                      "Nb": dict(Delta_meV=[1.50, 1.61], m_floor_keV=[2 * 2 * d * 1e-3 / VMAX0 ** 2 / 1e3 for d in (1.50, 1.61)],
                                 src="1.50-1.61 [FT 1805.06359 p.3, secondary; CW4-errata OC-11(c)]; v4 row 1.63 [E, DFT T_c]")}
    # heavy-mediator windows (R17, pairwise, eta-weighted): see nr_windows()
    res.update(nr_windows(nr1, res))
    # light mediator (R17): first-order form 1 - (m_min^ac/m)(1 + kappa_eta) below m_hi, 1 - (w/(c q_BZ))(1 + kappa(q_BZ/2m)) above; full integral at fixed masses
    res["NR_light_factor"] = {m: 1 - W_TH / (d["c_nr1"] / C_KMS * d["q_BZ_eV"]) for m, d in nr1.items() if "q_BZ_eV" in d}
    res["NR_light"] = nr_light(nr1)
    # background tolerance: survivors' leader vs runner-up (rate channels): b ratio the leader can afford
    tol = {}
    for ch in ("NR_heavy", "POL_rate", "Migdal", "ER_quanta"):
        o = res[ch]["survivors"]["order"]
        r_ = res[ch]["survivors"]["rows"]
        a, b_ = r_[o[0]]["median"], r_[o[1]]["median"]
        R = a / b_ if better[ch] == "high" else b_ / a
        tol[ch] = dict(leader=o[0], runner_up=o[1], rate_ratio=R, b_ratio_bg_limited=R ** 2, b_ratio_sys_floor=R)
    res["background_tolerance"] = tol
    res["runtime_s"] = time.time() - T0
    res["halo_band_edges"] = {"sigma_ln_vmax": SIG["halo_vmax"], "edge_factor_68": [float(np.percentile(HALO ** -2, 16)), float(np.percentile(HALO ** -2, 84))]}
    S["_halo"] = SH
    return res, S


R_VARIANTS = (0.0, 0.5, 0.9, 1.0)


def variants():
    """P(first) and adjacent P(A > B) at r_mat = 0, 0.5, 0.9, 1 (family-wise; CONVENTIONS §13 row 29). Medians, intervals and tiers are r-independent."""
    out = {}
    for r in R_VARIANTS:
        rr, _ = run(r)
        out[str(r)] = {ch: {p: dict(P_first={m: rr[ch][p]["rows"][m]["P_first"] for m in rr[ch][p]["order"]},
                                    tier={m: rr[ch][p]["rows"][m]["tier"] for m in rr[ch][p]["order"]},
                                    median={m: rr[ch][p]["rows"][m]["median"] for m in rr[ch][p]["order"]},
                                    adjacent_P=rr[ch][p]["adjacent_P"]) for p in ("all", "survivors")}
                       for ch in ("ER_edge", "ER_quanta", "NR_heavy", "NR_edge", "POL_rate", "POL_edge", "Migdal")}
    return out


if __name__ == "__main__":
    VAR = variants()
    res, S = run(0.0)
    res["r_mat_variants"] = VAR
    res["row38"] = {"promoted": ROW38_PROMOTED, "array_caveat": ARRAY_CAVEAT}
    res["measured_tensors"] = {"CaWO4": CHR_MEAS["CaWO4"], "Al": CHR_MEAS["Al"], "Al_v4_DB": {k: CHR["Al"][k] for k in ("cLA", "cLA_max", "c_nr1")},
                               "CsI": dict(B_GPa=B_CSI, rho=RHO_CSI, floor_kms=CSI_FLOOR, cauchy_cLA_kms=CSI_CAUCHY, c_LA_1910=C_1910["CsI"]),
                               "CaWO4_c_LA_1910": C_1910["CaWO4"]}
    json.dump(res, open(OUT, "w"), indent=1, default=float)
    for ch in ("ER_edge", "ER_quanta", "NR_heavy", "NR_edge", "POL_rate", "POL_edge", "Migdal"):
        for pool in ("all", "survivors"):
            a = res[ch][pool]
            print("%s [%s]" % (ch, pool))
            for m in a["order"]:
                r = a["rows"][m]
                print("   t%d %-8s %9.4g [%9.4g, %9.4g] P1=%.3f (r=.5 %.3f, .9 %.3f, 1 %.3f) rank68=%s %s" % (
                    r["tier"], m, r["median"], r["p16"], r["p84"], r["P_first"], VAR["0.5"][ch][pool]["P_first"][m], VAR["0.9"][ch][pool]["P_first"][m],
                    VAR["1.0"][ch][pool]["P_first"][m], r["rank_68"], ",".join(res["flags"][m])))
    print("sigma families:", {k: v for k, v in SIG.items()})
    for k in ("NR_heavy_common_window_S_fu_MeV", "NR_heavy_common_window_all_fu_MeV", "NR_heavy_common_window_S_prim_MeV", "NR_heavy_common_window_all_prim_MeV"):
        print(k, res[k])
    print("vs Si (fu):", {m: (None if w is None else [round(w[0], 3), round(w[1], 3)]) for m, w in res["NR_heavy_window_vs_Si_fu_MeV"].items()})
    print("vs Si (prim):", {m: (None if w is None else [round(w[0], 3), round(w[1], 3)]) for m, w in res["NR_heavy_window_vs_Si_prim_MeV"].items()})
    print("adjacent (fu):", res["NR_heavy_window_adjacent_fu_MeV"])
    print("adjacent (prim):", res["NR_heavy_window_adjacent_prim_MeV"])
    print("light:", res["NR_light"]["kappa_eta"], {m: [round(x, 3) for x in v] for m, v in res["NR_light"]["ratio_to_Si"].items() if m in ("CsI", "TeO2", "Ge", "Al2O3", "CaWO4")})
    print("light first order:", {m: v for m, v in res["NR_light"]["first_order_ratio_to_Si"].items() if m in ("CsI", "TeO2", "Ge")})
    print("measured tensors:", res["measured_tensors"])
    print("NiO valence:", res["NiO_valence"])
    print("bg tolerance:", res["background_tolerance"])
    print("runtime %.1f s" % (time.time() - T0))
