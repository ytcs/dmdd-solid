"""REV-WP8-S checks (labels S2-Cn, cited in returns/R16/WP8-S-v2.md). They test the orderings, tiers and probabilities that the return
states, not only the inputs: every probability and leader printed in the return's machine-checked tables is compared with a fresh
run of rank.py.  Runs rank.run() once (N_MC = 20000, ~2 s) and writes nothing outside code/REV-WP8-S/data/.
R17 ERR-WP8 (v3): reads data/ranking_v3.json (written by `python3 rank.py`, which also stores the r_mat variants); S2-C1, C4, C12, C13, C14, C15
updated for the v3 inputs (row-38 pool, measured CaWO4/Al tensors, CsI B-floor model) and the errata's readings table; S2-C12b replaced;
new checks S3-C1 ... S3-C16, one per correction of returns/R17/WP8-errata.md."""
import hashlib
import json, math, os, re, subprocess, sys, time

import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import rank as R  # noqa: E402

RES = []


def check(label, ok, msg):
    RES.append((label, bool(ok), msg))
    print(("PASS " if ok else "FAIL ") + label + ": " + msg)


res, S = R.run()
CH = ("ER_edge", "ER_quanta", "NR_heavy", "NR_edge", "POL_rate", "POL_edge", "Migdal")
saved = json.load(open(R.OUT))

# S2-C1 pool
vc = {}
for m in R.by:
    vc.setdefault(R.verdict(m), []).append(m)
check("S2-C1", len(R.POOL) == 42 and len(R.SURV) == 11 and set(R.SURV) - {"C"} == {m for m in R.POOL if R.rws(m, "verdict") and R.rws(m, "verdict")[-1]["value"] == "SURVIVOR"} and not set(vc.get("EXCLUDED-RADIO", [])) & set(R.POOL)
      and set(vc["EXCLUDED-RADIO"]) == {"KTaO3", "InSb"},
      "pool from the v4 verdict column + CONVENTIONS row 38 (C promoted): %d = %d SURVIVOR + %d SURVIVOR-COND; KTaO3, InSb (EXCLUDED-RADIO) out" % (len(R.POOL), len(R.SURV), len(R.POOL) - len(R.SURV)))

# S2-C2 coverage: every pool member is ranked or listed with a reason in every channel; Li2MoO4 only in Migdal
cov = True
miss = {}
for ch in CH:
    ranked = set(res[ch]["all"]["order"])
    listed = set(res["not_ranked"][ch]) | (set(res["SC_line"]) if ch == "ER_edge" else set())
    miss[ch] = sorted(set(R.POOL) - ranked - listed)
    cov &= not miss[ch] and not (ranked & set(res["not_ranked"][ch]))
li = [ch for ch in CH if "Li2MoO4" in res[ch]["all"]["order"]]
gapok = all(any(k in " ".join(v) for v in [R.NOTRANK[m]]) for m, k in (("Li2MoO4", "NR-1ph"), ("TeO2", "ER edge")))
check("S2-C2", cov and li == ["Migdal"] and gapok,
      "coverage: every one of the 42 is ranked or in the channel's not-ranked list (missing: %s); Li2MoO4 ranked only in %s; v4 GAP:channel_inputs honoured"
      % ({k: v for k, v in miss.items() if v}, li))

# S2-C3 S4 conditions carried into every row
need = {"TeO2": "123Te", "PbTe": "210Pb", "PbS": "210Pb", "PbSe": "210Pb", "ZrTe5": "S4-COND", "Cr2O3": "S4-COND"}
s4ok = all(any(k in f for f in res["flags"][m]) for m, k in need.items()) and all(not res["flags"][m] for m in ("Si", "Ge", "GaAs", "LiF", "NaF"))
check("S2-C3", s4ok, "S4 flags on TeO2 (123Te), PbTe/PbS/PbSe (bulk 210Pb), ZrTe5, Cr2O3; none on Si, Ge, GaAs, LiF, NaF")

# S2-C4 tiers: interval order on the 68% intervals; transitive; each tier an antichain; recomputed from the saved JSON
ok4, ntier = True, 0
for ch in CH:
    for pool in ("all", "survivors"):
        rows = saved[ch][pool]["rows"]
        sgn = 1 if saved[ch]["better"] == "high" else -1
        iv = {m: sorted([sgn * math.log(r["p16"]), sgn * math.log(r["p84"])]) for m, r in rows.items()}
        beats = {(a, b) for a in iv for b in iv if iv[a][0] > iv[b][1]}
        trans = all((a, c) in beats for (a, b) in beats for (b2, c) in beats if b2 == b)
        for t in set(r["tier"] for r in rows.values()):
            mem = [m for m, r in rows.items() if r["tier"] == t]
            ok4 &= not any((a, b) in beats for a in mem for b in mem)
            ntier += 1
        # height = 1 + longest chain above
        for m, r in rows.items():
            above = [rows[a]["tier"] for (a, b) in beats if b == m]
            ok4 &= r["tier"] == 1 + (max(above) if above else 0)
        ok4 &= trans
NTIER = ntier
check("S2-C4", ok4, "tiers = heights of the interval order of the 68%% intervals: transitive, every one of %d tiers an antichain (no member resolves another), "
      "recomputed from data/ranking_v3.json for 7 channels x 2 pools" % ntier)

# S2-C5 probabilities: sum to 1; the leader by P(first) is in tier 1
ok5 = all(abs(sum(r["P_first"] for r in saved[ch][p]["rows"].values()) - 1) < 1e-9 for ch in CH for p in ("all", "survivors"))
ok5 &= all(saved[ch][p]["rows"][max(saved[ch][p]["rows"], key=lambda m: saved[ch][p]["rows"][m]["P_first"])]["tier"] == 1 for ch in CH for p in ("all", "survivors"))
check("S2-C5", ok5, "sum_i P(i first) = 1 in every channel and pool; the P(first) maximum is always in tier 1")


# S2-C6 MC vs linearised log-error (independent route): P(A beats B) = Phi(d ln / sqrt(sA^2 + sB^2)) for lognormal inputs
def pmc(ch, a, b, high=True):
    x, y = S[ch][a], S[ch][b]
    return float(np.mean(x > y) if high else np.mean(x < y))


sc = R.SIG["c_DB"]
pairs = []
for a, b in (("TeO2", "Ge"), ("Ge", "GaAs"), ("NaF", "LiF"), ("GaAs", "NaF")):          # heavy NR: FOM ~ 1/c_NR1
    lin = norm.cdf(math.log(R.CHR[b]["c_nr1"] / R.CHR[a]["c_nr1"]) / (math.sqrt(2) * sc))
    pairs.append(("NR_heavy", a, b, lin, pmc("NR_heavy", a, b)))
for a, b in (("Al2O3", "Si"), ("Si", "LiF")):                                             # NR edge ~ 1/c_LA,max (c << v)
    lin = norm.cdf(math.log(R.CHR[a]["cLA_max"] / R.CHR[b]["cLA_max"]) / (math.sqrt(2) * sc))
    pairs.append(("NR_edge", a, b, lin, pmc("NR_edge", a, b, high=False)))
ok6 = all(abs(l - m) < 0.012 for _, _, _, l, m in pairs)
check("S2-C6", ok6, "MC = linearised log-error to < 0.012 for %s" % ", ".join("%s %s>%s %.3f/%.3f" % (c, a, b, l, m) for c, a, b, l, m in pairs))

# S2-C7 common halo draw (r = 1) does not reorder the edges: same base draws with and without the halo factor
H = S["_halo"]
er_o = res["ER_edge"]["all"]["order"]
same_er = np.mean(np.all(np.argsort(np.array([H["ER_edge"][m] for m in er_o]), 0) == np.argsort(np.array([S["ER_edge"][m] for m in er_o]), 0), axis=0))
ne = res["NR_edge"]["all"]["order"]
same_nr = np.mean(np.all(np.argsort(np.array([H["NR_edge"][m] for m in ne]), 0) == np.argsort(np.array([S["NR_edge"][m] for m in ne]), 0), axis=0))
check("S2-C7", same_er == 1.0 and same_nr == 1.0, "halo band (v_max sigma_ln %.3f, edges x%.2f-%.2f at 68%%) as one common draw: per-draw orders identical with and without it "
      "(ER edge %.3f, NR edge %.3f of draws), so the ranking samples use v_max = 794.5 km/s" % (R.SIG["halo_vmax"], *res["halo_band_edges"]["edge_factor_68"], same_er, same_nr))

# S2-C8 the ranked eps_eh are the T_op values; range strings are not parsed as their first number (REF-B §D)
ep = res["inputs"]["ER_quanta"]
mq = {m: saved["ER_quanta"]["all"]["rows"][m]["median"] for m in ("Si", "Ge", "GaAs")}
check("S2-C8", R.num1("3.6-3.8") is None and R.num1("~13") == 13.0 and abs(mq["Si"] - 3.72) < 0.01 and abs(mq["Ge"] - 3.37) < 0.01 and mq["GaAs"] > 4.2
      and "5 K" in ep["Si"]["T"] and "50 mK" in ep["Ge"]["T"],
      "eps_eh at T_op: Si %.3f (5 K; not 3.6 from '3.6-3.8'), Ge %.3f (50 mK; not 3.0), GaAs %.2f (25 C value + shift to T_op); num1 rejects ranges" % (mq["Si"], mq["Ge"], mq["GaAs"]))

# S2-C9 GAP-EF values are the v2 ones (results.json), not the stale v4-CSV copies of R14
gaas_csv = [x["value"] for x in R.rws("GaAs", "eps_eh_pred_GAPEF")][0]
check("S2-C9", abs(ep["CsI"]["eps"] - 11.208) < 0.01 and abs(ep["CsI"]["hi"] - 14.33) < 0.01 and "4.58" in gaas_csv and abs(ep["PbTe"]["lo"] - 1.185) < 0.01,
      "GAP-EF-v2 predictions used: CsI %.2f (v4 CSV 11.5), band hi %.2f; PbTe band %.3f-%.3f; the CSV GaAs row '%s' is the R14 band" % (ep["CsI"]["eps"], ep["CsI"]["hi"], ep["PbTe"]["lo"], ep["PbTe"]["hi"], gaas_csv))

# S2-C10 POL: sapphire ranked value = consistent lossless mode sum (<= consistent bound); mixed R16 route below it; GaAs measured-pair range
cm = 0.1239842
o_L, o_T = np.array([906.6, 629.5, 481.7, 387.6]) * cm, np.array([633.6, 569.0, 439.1, 385.0]) * cm
e_L, e_T = np.array([881.1, 510.9]) * cm, np.array([582.4, 397.5]) * cm
e0o, e0e = 3.2 * np.prod((o_L / o_T) ** 2), 3.2 * np.prod((e_L / e_T) ** 2)
b_cons = (2 * (1 / 3.2 - 1 / e0o) * o_L.max() + (1 / 3.2 - 1 / e0e) * e_L.max()) / 3 * math.pi / 2 / 3.98
Isap = res["inputs"]["POL"]["Al2O3"]["I"]
mixed = math.pi / 2 * (1 / 3.26 - 1 / 11.969) * 104.0 / 3.9869
pr = saved["POL_rate"]["all"]["rows"]
check("S2-C10", abs(Isap - 9.27) < 0.01 and Isap <= b_cons and mixed < Isap and 0.140 <= pr["GaAs"]["p16"] and pr["GaAs"]["p84"] <= 0.158
      and "TeO2" in res["POL_bounds"] and "Al2O3" not in res["POL_bounds"],
      "POL: sapphire ranked %.2f = lossless axis-averaged mode sum <= consistent bound %.2f; R16 mixed route %.2f < it; GaAs 68%% [%.3f, %.3f]; TeO2, hBN bound-only"
      % (Isap, b_cons, mixed, pr["GaAs"]["p16"], pr["GaAs"]["p84"]))

# S2-C11 Migdal: Z_ion and n_e^val from the same split for every pool material; NiO convention effect
okv = True
bad = []
for m in R.POOL:
    xs = R.rws(m, "n_e_val")
    mm = re.search(r"(\d+) valence e per f\.u\.|n_val = (\d+) e/f\.u\.", xs[-1]["note"]) if xs else None
    if mm:
        n = int(mm.group(1) or mm.group(2))
        if n != res["inputs"]["Migdal"][m]["zv"]:
            okv = False; bad.append((m, n, res["inputs"]["Migdal"][m]["zv"]))
nio = res["NiO_valence"]
r_cons = nio["2"]["consistent"] / nio["10"]["consistent"]
r_nuc = nio["2"]["nuclear_only"] / nio["10"]["nuclear_only"]
check("S2-C11", okv and abs(r_cons - 0.832) < 0.01 and abs(r_nuc - 0.294) < 0.01,
      "Migdal: sum_k n_k Z_ion,k = the n_e^val count of the v4 table for all 42 (mismatch %s); NiO Ni 4s2 vs 3d8 4s2: x%.3f with one split, x%.3f nuclear factor alone"
      % (bad, r_cons, r_nuc))

# S2-C12 light mediator: c cancels -> no rate row (numerical (2.3a'') with the CONVENTIONS §8 SHM eta vs the 1 - w/(c q) factor)
# CONVENTIONS §8 SHM eta(v_min) (v0 238, v_esc 544, v_E^ref 250.5 km/s), as in code/CW7/checks.py
_V0, _VESC, _VE = 238 / R.C_KMS, 544 / R.C_KMS, 250.5 / R.C_KMS
_v = np.linspace(1e-7, _VESC + _VE, 40001)
_mu = np.clip((_VESC ** 2 - _v ** 2 - _VE ** 2) / (2 * _v * _VE), -1, 1)
_f = _v ** 2 / (_v * _VE) * (np.exp(-(_v - _VE) ** 2 / _V0 ** 2) - np.exp(-(_v ** 2 + _VE ** 2 + 2 * _v * _VE * _mu) / _V0 ** 2)) * (_mu > -1)
_f /= np.trapezoid(_f, _v)
_g = _f / _v
_cum = np.concatenate([[0], np.cumsum((_g[1:] + _g[:-1]) / 2 * np.diff(_v))])
_eta = _cum[-1] - _cum
eta = lambda vmin: float(np.interp(vmin, _v, _eta, right=0.0))  # noqa: E731


def rate(c_kms, qbz, mchi, light):
    c = c_kms / R.C_KMS
    qlo, qup = R.W_TH / c, min(qbz, 2 * mchi * (R.VMAX0 - c))
    if qup <= qlo:
        return 0.0
    f = (lambda q: q ** 2 * (1 / q ** 4 if light else 1) * eta(c + q / (2 * mchi)) / c)
    return quad(f, qlo, qup, limit=200)[0]


qS, qC = res["inputs"]["NR"]["Si"]["q_BZ_eV"], res["inputs"]["NR"]["CsI"]["q_BZ_eV"]
lt = rate(R.CHR["Si"]["c_nr1"], qS, 10e6, True) / rate(res["inputs"]["NR"]["CsI"]["c_nr1"], qC, 10e6, True)
fac = res["NR_light_factor"]["Si"] / res["NR_light_factor"]["CsI"]
hv = rate(res["inputs"]["NR"]["CsI"]["c_nr1"], qC, 0.25e6, False) / rate(R.CHR["Si"]["c_nr1"], qS, 0.25e6, False)
spread = max(res["NR_light_factor"].values()) / min(res["NR_light_factor"].values())
check("S2-C12", abs(lt / fac - 1) < 0.05 and spread < 1.10 and abs(hv / (R.CHR["Si"]["c_nr1"] / res["inputs"]["NR"]["CsI"]["c_nr1"]) - 1) < 0.1,
      "NR-1ph light mediator: Si/CsI rate %.3f = residual factor ratio %.3f (c cancels); factor spread over the pool x%.3f -> no rate row; heavy mediator at 0.25 MeV "
      "CsI/Si %.2f vs 1/c_NR1 ratio %.2f" % (lt, fac, spread, hv, R.CHR["Si"]["c_nr1"] / res["inputs"]["NR"]["CsI"]["c_nr1"]))

# ======================= v3 (R17 ERR-WP8) =======================
import csv  # noqa: E402
import sympy as sp  # noqa: E402

A = lambda ch, p="survivors": saved[ch][p]["rows"]  # noqa: E731
o = lambda ch, p="survivors": saved[ch][p]["order"]  # noqa: E731
V = saved["r_mat_variants"]
CH7 = CH
NRI = res["inputs"]["NR"]

# S3-C1 CaWO4 measured tensor (errata §3): positive definite, Christoffel speeds; 1910.10716 c_LA lies below the measured LA minimum
cw = saved["measured_tensors"]["CaWO4"]
check("S3-C1", cw["posdef"] and abs(cw["c_nr1"] - 4.58) < 0.01 and abs(cw["cLA"] - 4.65) < 0.01 and saved["measured_tensors"]["CaWO4_c_LA_1910"] < cw["cLA_min"]
      and abs(A("NR_heavy")["CaWO4"]["median"] - R.CHR["Si"]["c_nr1"] / cw["c_nr1"]) < 0.01,
      "CaWO4 measured C_ij (4/m, C26 = -C16; 2508.08858 p.16): pos.def.; c_NR1 %.3f, mean c_LA %.3f, LA range [%.3f, %.3f] km/s; 1910.10716 4.257 < LA min "
      "(-%.1f%%); FOM %.3f (v2 proxy 2.07)" % (cw["c_nr1"], cw["cLA"], cw["cLA_min"], cw["cLA_max"], 100 * (1 - 4.2571 / cw["cLA_min"]), A("NR_heavy")["CaWO4"]["median"]))

# S3-C2 CsI bulk-modulus floor [D] and Cauchy nu = 1/4 [D] (sympy); 1910.10716 c_LA below the floor
C11, C12, C44, t = sp.symbols("C11 C12 C44 t", real=True)
B = (C11 + 2 * C12) / 3
L100, L111 = C11, (C11 + 2 * C12 + 4 * C44) / 3
d1, d2 = sp.simplify(L100 - B), sp.simplify(L111 - B)          # 2(C11-C12)/3 >= 0 and 4C44/3 >= 0 under Born stability
lam_, mu_, nu_ = sp.symbols("lambda mu nu", positive=True)
nu_c = sp.simplify((lam_ / (2 * (lam_ + mu_))).subs(lam_, mu_))  # Cauchy C12 = C44 + isotropy C11 - C12 = 2C44 -> lambda = mu
cl2 = sp.simplify((3 * (1 - nu_) / (1 + nu_)).subs(nu_, sp.Rational(1, 2)))
mt = saved["measured_tensors"]["CsI"]
check("S3-C2", sp.simplify(d1 - 2 * (C11 - C12) / 3) == 0 and sp.simplify(d2 - 4 * C44 / 3) == 0 and nu_c == sp.Rational(1, 4) and cl2 == 1
      and mt["c_LA_1910"] < mt["floor_kms"] and abs(mt["floor_kms"] - 1.726) < 0.002 and abs(mt["cauchy_cLA_kms"] - 2.316) < 0.002
      and 3.4 < A("NR_heavy", "all")["CsI"]["median"] < 4.3,
      "CsI: rho c_L^2 - B = 2(C11-C12)/3 [100], 4C44/3 [111] (>= 0; the quartic form interpolates between them), so c_LA >= sqrt(B/rho) = %.3f km/s "
      "(B 13.5 GPa expt., rho %.3f); 1910.10716 1.379 km/s is %.0f%% below it; Cauchy nu = %s gives c_LA %.3f; FOM %.2f (v2 6.39)"
      % (mt["floor_kms"], mt["rho"], 100 * (1 - 1.379 / mt["floor_kms"]), nu_c, mt["cauchy_cLA_kms"], A("NR_heavy", "all")["CsI"]["median"]))

# S3-C3 DATA-ADDENDA supersessions (coordinator, CW8-LIT): Al measured C_ij and a_exp; YIG rho
add = list(csv.DictReader(open(os.path.join(ROOT, "state/DATA-ADDENDA.csv"))))
al = saved["measured_tensors"]["Al"]
check("S3-C3", abs(NRI["Al"]["c_nr1"] - al["c_nr1"]) < 1e-9 and al["c_nr1"] > 1.1 * R.CHR["Al"]["c_nr1"] and abs(res["inputs"]["Migdal"]["YIG"]["rho"] - 5.173) < 1e-9
      and abs(res["inputs"]["Migdal"]["Al"]["rho"] - 2.698) < 0.002 and any(x["material"] == "Al" and "31.6" in x["value"] for x in add),
      "Al: measured C11/C12/C44 114.3/61.9/31.6 GPa (rho %.3f from a_exp 4.05 A) -> c_NR1 %.3f, c_LA,max %.3f km/s replace the v4 DB %.3f/%.3f (C44 16.2); "
      "YIG rho 5.173 (a = 12.3750 A) replaces 4.9475 in Migdal; Ir not in the pool" % (res["inputs"]["Migdal"]["Al"]["rho"], al["c_nr1"], al["cLA_max"],
                                                                                   R.CHR["Al"]["c_nr1"], R.CHR["Al"]["cLA_max"]))

# S3-C4 heavy-mediator window (errata §5): reproduce both referees, then the pairwise windows
qSi_GX, qCsI_GX = 2 * math.pi * 1973.27 / 5.431, math.pi * 1973.27 / 4.567
old = [R.nr_rate(1.379, qCsI_GX, m * 1e6, False) / R.nr_rate(8.757, qSi_GX, m * 1e6, False) for m in (0.1, 0.2, 0.3, 0.43)]
qT, qS_ = NRI["TeO2"]["q_BZ_eV"], NRI["Si"]["q_BZ_eV"]
te = [R.nr_rate(R.CHR["TeO2"]["c_nr1"], qT, m * 1e6, False) / R.nr_rate(R.CHR["Si"]["c_nr1"], qS_, m * 1e6, False) for m in (0.03, 0.1)]
mm = saved["m_min_ac_c_nr1_keV"]
w = saved["NR_heavy_window_vs_Si_fu_MeV"]
ratio = [w[m][0] * 1e3 / mm[m] for m in ("TeO2", "CaWO4", "Ge", "CsI", "NaF", "Al2O3") if w[m]]
check("S3-C4", all(abs(a - b) < 0.12 for a, b in zip(old, (3.42, 6.09, 6.48, 5.60))) and abs(te[0] - 0.83) < 0.05 and abs(te[1] - 2.31) < 0.1
      and all(3.0 < r_ < 6.5 for r_ in ratio) and saved["NR_heavy_common_window_S_fu_MeV"][0] < 0.07 < 0.32 < saved["NR_heavy_common_window_S_fu_MeV"][1],
      "VER-ERR-CW7 (c 1.379, Gamma-X q_top) CsI/Si heavy = %s (3.42, 6.09, 6.48, 5.60); VER-WP8-S-v2 TeO2/Si %.2f, %.2f at 0.03, 0.1 MeV (0.83, 2.31); "
      "10%% onset / m_min^ac(c_NR1) = %s; survivor common window %s (f.u.) / %s (prim) MeV"
      % ([round(x, 2) for x in old], te[0], te[1], [round(x, 1) for x in ratio], [round(x, 3) for x in saved["NR_heavy_common_window_S_fu_MeV"]],
         [round(x, 3) for x in saved["NR_heavy_common_window_S_prim_MeV"]]))

# S3-C5 light mediator O(m_min/m) (errata §6): sympy first-order expansion on a generic eta; numbers
u, um, up, e0, a2, a3 = sp.symbols("u u_m u_p eta0 a2 a3", positive=True)
eta_toy = e0 - a2 * u ** 2 - a3 * u ** 3                      # any smooth lab-frame eta: eta'(0) = 0
I_ex = sp.integrate(eta_toy / u ** 2, (u, um, up))
Kap = up / e0 * sp.integrate((e0 - eta_toy) / u ** 2, (u, 0, up))
fo = e0 / um * (1 - um / up * (1 + Kap))
dif = sp.limit(sp.expand(I_ex - fo), um, 0)                 # remainder is O(u-): relative O(u-^2)
lt_old = [R.nr_rate(1.379, qCsI_GX, m * 1e6, True) / R.nr_rate(8.757, qSi_GX, m * 1e6, True) for m in (0.1, 0.2, 0.3, 0.43, 1.0)]
NL = saved["NR_light"]
fo_ok = all(abs(NL["first_order_ratio_to_Si"][m][k] / NL["ratio_to_Si"][m][k] - 1) < 0.03 for m in ("Ge", "TeO2", "GaAs") for k in (2, 3)
            if NL["first_order_ratio_to_Si"][m][k] is not None)
check("S3-C5", dif == 0 and all(abs(a - b) < 0.03 for a, b in zip(lt_old, (0.11, 0.42, 0.58, 0.69, 0.82))) and fo_ok and abs(NL["kappa_eta"] - 3.14) < 0.05,
      "sympy: int_{u-}^{u+} eta/u^2 = (eta0/u-)[1 - (u-/u+)(1 + kappa_eta)] + O(u-) exactly for eta = eta0 - a2 u^2 - a3 u^3; SHM kappa_eta = %.3f; old-c CsI/Si light = %s "
      "(VER-ERR-CW7 0.11, 0.42, 0.58, 0.69, 0.82); first order within 3%% of the full integral at m >= 10 m_min (Ge, TeO2, GaAs); new CsI/Si %s at %s MeV"
      % (NL["kappa_eta"], [round(x, 2) for x in lt_old], [round(x, 2) for x in NL["ratio_to_Si"]["CsI"]], NL["masses_MeV"]))

# S3-C6 polar: sapphire I ∝ 1/eps_inf at fixed modes (sympy on the partial fractions); width >= 3%; eps-route entries use (8.1)
x_, ei_ = sp.symbols("x eps_inf", positive=True)
wl, wt = sp.symbols("wL1 wL2", positive=True), sp.symbols("wT1 wT2", positive=True)
inv = 1 / (ei_ * (wl[0] ** 2 - x_) * (wl[1] ** 2 - x_) / ((wt[0] ** 2 - x_) * (wt[1] ** 2 - x_)))   # 1/eps(omega^2 = x), factorised
res1 = sp.residue(inv, x_, wl[0] ** 2)
prop = sp.simplify(sp.diff(sp.log(-res1), ei_) + 1 / ei_) == 0
sap = A("POL_rate")["Al2O3"]
multi = [m for m, d in res["inputs"]["POL"].items() if "interval" in d.get("tag", "")]
check("S3-C6", prop and math.log(sap["p84"] / sap["p16"]) / 2 >= 0.03 and set(multi) == {"SiO2-q", "MgF2"} and all("(8.1)" in res["inputs"]["POL"][m]["route"] for m in multi)
      and all("upper bound only" in b["note"] for b in res["POL_bounds"].values()),
      "residues of the factorised 1/eps scale as 1/eps_inf at fixed (omega_L, omega_T) -> I_pol ∝ 1/eps_inf; sapphire 68%% [%.2f, %.2f] (half-width %.1f%% >= 3%%); "
      "eps-route multi-branch entries %s ranked by the (8.1) interval, %s bound-only (omega_T,max sqrt(eps0/eps_inf)); no omega_L,max form ranked"
      % (sap["p16"], sap["p84"], 50 * math.log(sap["p84"] / sap["p16"]), multi, sorted(res["POL_bounds"])))

# S3-C7 r_mat variants (errata §8): marginals and tiers r-independent; P1 moves; the two r = 0 ties resolve at r = 1
flips = sorted({(ch, p, m) for r in V for ch in CH7 for p in ("all", "survivors") for m in V["0.0"][ch][p]["tier"]
                if V[r][ch][p]["tier"][m] != V["0.0"][ch][p]["tier"][m]})
ok7 = len(flips) <= 1 and all(abs(V[r][ch][p]["median"][m] / V["0.0"][ch][p]["median"][m] - 1) < 0.03 for r in V for ch in CH7 for p in ("all", "survivors")
                              for m in V["0.0"][ch][p]["median"])
check("S3-C7", ok7 and V["1.0"]["Migdal"]["all"]["P_first"]["NaCl"] > 0.9 and V["1.0"]["NR_edge"]["all"]["P_first"]["hBN"] > 0.9
      and V["0.0"]["Migdal"]["all"]["P_first"]["NaCl"] < 0.6 and set(V) == {"0.0", "0.5", "0.9", "1.0"},
      "family-wise r_mat = 0, 0.5, 0.9, 1: tiers identical up to MC noise in the interval ends (boundary flips %s), medians within 3%%; P1 moves: Migdal-all NaCl %.3f/%.3f/%.3f/%.3f, NR-edge-all hBN %.3f/%.3f/%.3f/%.3f"
      % tuple([flips] + [V[r]["Migdal"]["all"]["P_first"]["NaCl"] for r in ("0.0", "0.5", "0.9", "1.0")] + [V[r]["NR_edge"]["all"]["P_first"]["hBN"] for r in ("0.0", "0.5", "0.9", "1.0")]))

# S3-C8 Si eps_eh width = the stated +-0.01 eV
si = A("ER_quanta")["Si"]
check("S3-C8", 0.017 < si["p84"] - si["p16"] < 0.023, "Si eps_eh 68%% width %.4f eV = 2 x 0.01 (stated error; v2 used 0.02)" % (si["p84"] - si["p16"]))

# S3-C9 L-S3 valence-convention factor multiplies the whole FOM (sympy) and the NiO numbers
Z_, Zp, So, n_, nprime = sp.symbols("Z Zp S_o n n_p", positive=True)
F = lambda z, nn: (z ** 2 + So) * nn ** sp.Rational(-3, 2)  # noqa: E731
ratio_s = sp.simplify(F(Zp, nprime) / F(Z_, n_) - (Zp ** 2 + So) / (Z_ ** 2 + So) * (nprime / n_) ** sp.Rational(-3, 2))
nio = res["NiO_valence"]
r2, r18 = nio["2"]["consistent"] / nio["10"]["consistent"], nio["18"]["consistent"] / nio["10"]["consistent"]
wrong = (4 / 100) * (8 / 16) ** -1.5 * 100 / (100 + 36) + 36 / 136            # "on the ion's term only" reading
check("S3-C9", ratio_s == 0 and abs(r2 - 0.832) < 0.002 and abs(r18 - 1.441) < 0.002 and abs(wrong - 0.35) < 0.01,
      "F'/F = [(Z'^2 + sum Z_o^2)/(Z^2 + sum Z_o^2)](n'/n)^(-3/2) (sympy); NiO Ni 10 -> 2: x%.3f, -> 18: x%.3f; the 'ion term only' reading would give x%.2f" % (r2, r18, wrong))

# S3-C10 the identity of the dropped rows (VER-ERR-CW7 RC2) and S3-C11 the PE cyclic shift + C33 tolerance (RC1)
ch_ = json.load(open(os.path.join(ROOT, "code/CW7/data/v4_changes.json")))
nonE = sorted((d_["material"], d_["property"]) for d_ in ch_["dropped"] if "[E]" not in d_["value"])
check("S3-C10", nonE == [("GaAs", "screen_S1"), ("SiO2-q", "screen_S1")] and sum("[E]" in d_["value"] for d_ in ch_["dropped"]) == 11,
      "v4 dropped rows: 11 with [E]; the 2 non-[E] are %s (not 'two GaAs rename rows')" % nonE)
J = json.load(open(os.path.join(ROOT, "code/WP8-U-TOP/data/jarvis_top.json")))
pe = np.array(J["PE"]["elastic_tensor"] if not isinstance(J["PE"]["elastic_tensor"], str) else json.loads(J["PE"]["elastic_tensor"]), float)
c4 = R.CHR["PE"]
old_ = (pe[3][3], pe[4][4], pe[5][5])
true_ = (c4["C44"], c4["C55"], c4["C66"])
hexs = [m for m, x in J.items() if x.get("crys") in ("hexagonal", "trigonal") and x.get("elastic_tensor") not in (None, "na") and m in R.CHR]
et = {m: np.array(J[m]["elastic_tensor"] if not isinstance(J[m]["elastic_tensor"], str) else json.loads(J[m]["elastic_tensor"]), float) for m in hexs}
ident = max(abs(et[m][3][3] - (et[m][0][0] - et[m][0][1]) / 2) for m in hexs)
check("S3-C11", np.allclose(old_, (true_[2], true_[0], true_[1])) and not np.allclose(old_, (true_[2], true_[1], true_[0])) and round(ident, 3) <= 0.05,
      "PE: identity reading (C44, C55, C66) = %s = true (C66, C44, C55) %s: a cyclic shift, not a C44<->C66 swap; C33 identity max deviation %.3f GPa <= 0.05 (code tolerance 0.11)"
      % (tuple(round(x, 1) for x in old_), tuple(round(x, 1) for x in true_), ident))

# S3-C12 Ge EC L-lines inside the sub-keV ROI (RC7): E_L/E_K of 1607.04560 Table 1 rises with Z (Cu, Zn, Ga) -> upper bounds for lighter daughters
EK = dict(Ti=4.97, V=5.46, Cr=5.99, Mn=6.54, Fe=7.11, Cu=8.98, Zn=9.66, Ga=10.37)
EL = dict(Cu=1.10, Zn=1.19, Ga=1.30)
rr_ = [EL[k] / EK[k] for k in ("Cu", "Zn", "Ga")]
ub = {k: rr_[0] * EK[k] for k in ("Ti", "V", "Cr", "Mn", "Fe")}
check("S3-C12", rr_[0] < rr_[1] < rr_[2] and max(ub.values()) < 1.0,
      "E_L/E_K = %.4f, %.4f, %.4f (Cu, Zn, Ga; 1607.04560 Table 1 p.25) increase with Z, so E_L <= %.4f E_K below Cu: %s keV, all < 1 keV "
      "(49V->Ti, 51Cr->V, 54Mn->Cr, 55Fe->Mn, 56-58Co->Fe)" % (*rr_, rr_[0], {k: round(v, 2) for k, v in ub.items()}))

# S3-C13 G-F6 isotope list generated from the v4 isotopes[El] rows (43Ca for CaWO4)
iso = {}
for m in R.POOL:
    for x in R.by[m]:
        if x["property"].startswith("isotopes["):
            el = x["property"][9:-1]
            for t_ in x["value"].split(";"):
                mm_ = re.match(r"\s*(\d+)(\w+) x=([\d.eE-]+) J=(\S+)", t_)
                if mm_ and mm_.group(4) != "0+":
                    iso.setdefault(m, set()).add(mm_.group(1) + el)
need13 = {"43Ca", "183W", "17O"}
check("S3-C13", need13 <= iso["CaWO4"] and "1H" in iso["PE"] and len(iso) == 42 and sum(len(v) for v in iso.values()) >= 90,
      "G-F6: odd-A / J != 0 isotopes generated from the v4 isotopes[El] rows for all %d pool materials (%d material-isotope entries); CaWO4 %s"
      % (len(iso), sum(len(v) for v in iso.values()), sorted(iso["CaWO4"])))

# S3-C14 Ge vs Si cosmogenics (VER-WP8-S-v2 row 12)
ge_sum, si_sum, tol = 82 + 74 + 106, 124, saved["background_tolerance"]["ER_quanta"]["b_ratio_bg_limited"]
check("S3-C14", ge_sum / si_sum > tol and 82 / 124 < 1,
      "Ge listed activation sum >= %d vs Si %d: x%.2f > tolerance %.2f (would reorder); 3H alone (the only listed nuclide with a < 1 keV beta tail) x%.2f"
      % (ge_sum, si_sum, ge_sum / si_sum, tol, 82 / 124))

# S3-C15 tier count; statement (ii) (two leading tiers, excluding Migdal)
two = {}
for ch in CH7:
    for m, r_ in A(ch).items():
        if r_["tier"] == 1:
            two.setdefault(m, set()).add(ch)
two_nm = sorted(m for m, v in two.items() if len(v - {"Migdal"}) >= 2)
two_all = sorted(m for m, v in two.items() if len(v) >= 2)
check("S3-C15", NTIER == 117 and two_nm == ["Ge"] and set(two_all) == {"Ge", "LiF", "GaAs"},
      "%d tiers over 7 channels x 2 pools (v2 text 93, v2 JSON 111); survivors in two leading tiers excluding Migdal: %s; including Migdal: %s" % (NTIER, two_nm, two_all))

# S3-C16 CONVENTIONS row 38 re-evaluation: only diamond promoted; NR-edge survivor leader
s2c = [m for m in R.POOL if any(x["value"].startswith("COND") for x in R.rws(m, "screen_S2"))]
only_s2 = [m for m in s2c if all(not x["value"].startswith(("COND", "FAIL")) for p in ("screen_S1", "screen_S3") for x in R.rws(m, p))
           and all(x["value"] == "PASS" for x in R.rws(m, "S4_verdict"))]
check("S3-C16", only_s2 == ["C"] and set(R.ROW38_PROMOTED) == {"C"} and o("NR_edge")[0] == "C" and A("NR_edge")["C"]["P_first"] > 0.99
      and o("NR_edge")[1] == "Al2O3",
      "row 38: of %d S2-COND materials only %s had S2 as the sole COND (others carry S1/S3 COND); diamond promoted -> NR-edge survivor leader C %.2f keV (P1 %.3f), Al2O3 second"
      % (len(s2c), only_s2, A("NR_edge")["C"]["median"], A("NR_edge")["C"]["P_first"]))

# S2-C13 (v3) the orderings the errata states
st = [
    o("ER_edge")[:3] == ["Ge", "Si", "GaAs"] and A("ER_edge")["Ge"]["P_first"] > 0.99,
    o("ER_edge", "all")[:3] == ["PbSe", "PbTe", "PbS"],
    o("ER_quanta")[:3] == ["Ge", "Si", "GaAs"],
    {m for m, r_ in A("NR_heavy").items() if r_["tier"] == 1} == {"TeO2"},
    A("NR_heavy")["CaWO4"]["tier"] == A("NR_heavy")["Ge"]["tier"] == A("NR_heavy")["GaAs"]["tier"] == 2,
    o("NR_heavy", "all")[0] == "CsI",
    o("NR_edge")[0] == "C",
    o("POL_rate")[0] == "LiF" and A("POL_rate")["NaF"]["tier"] == A("POL_rate")["Al2O3"]["tier"],
    o("POL_edge")[0] == "GaAs" and o("POL_edge")[-1] == "Al2O3",
    max(r_["P_first"] for r_ in A("Migdal").values()) < 0.5,
]
check("S2-C13", all(st), "orderings stated in the errata hold: %s" % st)

# S2-C14 (v3) the errata's final readings table equals the run (P to 0.006, tiers exactly; r = 1 column to 0.01)
_mdp = os.path.join(ROOT, "returns/R17/WP8-errata.md")
md = open(_mdp).read() if os.path.exists(_mdp) else ""
rowsP = re.findall(r"^\| (R\d+) \| (\w+) \| (all|S) \| ([\w-]+) \| (P_first|P_pair|tier) \| ([\d.]+) \| ([\d.]+|–) \| ([\w-]+|–) \|", md, re.M)
ok14, bad14 = len(rowsP) >= 20, []
for lab, ch, p, m, kind, val, v1, other in rowsP:
    pool = "all" if p == "all" else "survivors"
    if kind == "P_first":
        got, got1 = saved[ch][pool]["rows"][m]["P_first"], V["1.0"][ch][pool]["P_first"][m]
    elif kind == "tier":
        got, got1 = saved[ch][pool]["rows"][m]["tier"], V["1.0"][ch][pool]["tier"][m]
    else:
        got = pmc(ch, m, other, high=saved[ch]["better"] == "high")
        adj = {(a, b): x for a, b, x in V["1.0"][ch][pool]["adjacent_P"]}
        got1 = adj.get((m, other))
    tol = 0.0 if kind == "tier" else 0.006
    if abs(float(val) - got) > tol + 1e-12 or (v1 != "–" and got1 is not None and abs(float(v1) - got1) > (0 if kind == "tier" else 0.01) + 1e-12):
        ok14 = False; bad14.append((lab, ch, m, val, round(got, 3), v1, got1 if got1 is None else round(got1, 3)))
check("S2-C14", ok14, "%d rows of the errata's final readings table (WP8-errata §16.3) equal the run (r_mat = 0 to 0.006, r_mat = 1 column to 0.01; mismatches %s)" % (len(rowsP), bad14))

# S2-C15 (v3) hygiene: CW7 ranking.json and REV-WP8-S ranking_v2.json unchanged (md5 recorded before the R17 edit); runtime
md5 = lambda p: hashlib.md5(open(os.path.join(ROOT, p), "rb").read()).hexdigest()  # noqa: E731
check("S2-C15", md5("code/CW7/data/ranking.json") == "b0d95a54808fa5f2afc4443f9068819e" and md5("code/REV-WP8-S/data/ranking_v2.json") == "98a678d04114924d29a7bc5ad49167a5"
      and time.time() - T0 < 120, "code/CW7/data/ranking.json and data/ranking_v2.json byte-identical to their pre-R17 md5; checks runtime %.1f s < 120 s" % (time.time() - T0))

nf = sum(1 for r_ in RES if not r_[1])
print("\n%d/%d PASS, %.1f s" % (len(RES) - nf, len(RES), time.time() - T0))
sys.exit(1 if nf else 0)
