"""CW7 / LE-159 (WP8-S synthesis): per-channel scalar FOMs and rankings from returns/R16/WP8-U-table-v3.csv.
Formulas are the corrected WP8-F-v2 ones (returns/R16/WP8-F-v2.md); every number is [E] from tagged table inputs.
  ER  : continuum floor m_floor = 2 E_g / v_max^2 (measured E_g, room T unless stated), f-sum ceiling Z/A, threshold quanta eps_eh
  NR1 : light-mediator (all m_chi) / heavy-mediator (m_chi <~ 0.1-1 MeV) coefficient pi/(m_u^2 c_LA): rank by 1/c_LA; edge (2.3b) at 1 meV
  POL : diatomic Z* route (2.5b)  I/rho = (pi/2) e^2 Z*^2 / (M_cell mu eps_inf^2 omega_LO), and eps route (pi/2)(1/eps_inf - 1/eps_0) omega_max / rho
  MIG : nuclear factor sum_kappa Z_ion,kappa^2 / A_cell (valence ion charge at small k); the ELF factor Q_Mig needs L(k, omega) (GAP)
Rank resolution delta_rank = 0.2 in ln FOM (WP8-F §5.2): materials closer than that are tied."""
import csv, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "code/WP8-U"))
from materials import VALENCE  # noqa: E402

V3 = os.path.join(ROOT, "returns/R16/WP8-U-table-v3.csv")
rows = list(csv.DictReader(open(V3)))
by = {}
for x in rows:
    by.setdefault(x["material"], []).append(x)
C_KMS = 299792.458
VMAX = 794.5 / C_KMS
ALPHA = 1 / 137.035999
M_U = 931.494e6       # eV
EV_CM3_G = 4.3101e18  # (eV^-3) -> eV cm^3 / g  (1 g/cm^3 = 4.3101e18 eV^4)
DR = 0.2


def num(s):
    m = re.match(r"\s*[<>~]?\s*([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?\d+)?)", str(s))
    return float(m.group(1)) if m else None


def get(mat, props, tags=("FT", "E", "DB"), avoid=()):
    for p in props:
        for t in tags:
            for x in by.get(mat, []):
                if x["property"] == p and x["tag"] == t and not any(a in x["source"] + x["note"] for a in avoid):
                    v = num(x["value"])
                    if v is not None:
                        return v, "%s [%s %s]" % (p, t, x["source"])
    return None, "GAP"


def comp(mat):
    for x in by.get(mat, []):
        if x["property"] == "composition":
            out = []
            for tok in x["value"].split():
                m = re.fullmatch(r"([A-Z][a-z]?)(\d*)", tok)
                out.append((m.group(1), int(m.group(2) or 1)))
            return out
    return None


def amass(mat, el):
    v, _ = get(mat, ["A[%s]" % el], tags=("DB", "FT", "E"))
    return v


def build():
    out = {}
    for mat, xs in by.items():
        vs = [x["value"] for x in xs if x["property"] == "verdict"]
        ver = vs[-1] if vs else xs[0]["verdict"]
        if ver not in ("SURVIVOR", "SURVIVOR-COND"):
            continue
        cp = comp(mat)
        if not cp:
            continue
        r = {"verdict": ver}
        rho, rs = get(mat, ["rho_T"], tags=("FT",))
        if rho is None:
            rho, rs = get(mat, ["rho_T_from_a_exp", "rho_T", "rho_T_DFT"], tags=("E", "FT", "DB"))
        r["rho"] = rho
        eg, es = get(mat, ["E_g"], tags=("FT",), avoid=("1901.07569",) if mat == "Ge" else ())
        r["E_g"] = eg
        r["m_floor_MeV"] = 2 * eg / VMAX ** 2 / 1e6 if eg else None
        za, _ = get(mat, ["Z_over_A"], tags=("E",))
        r["Z_over_A"] = za
        c, cs = get(mat, ["c_LA_recommended", "c_LA_Christoffel_avg", "c_LA", "c_L_iso"], tags=("E", "FT"))
        r["c_LA"], r["c_src"] = c, cs
        if c:
            cl = c / C_KMS
            r["NR1_rel_Si"] = None
            r["m_ac_keV_1meV"] = 1e-3 / (2 * cl * (VMAX - cl)) / 1e3
        # masses
        Ms = [(el, n, amass(mat, el)) for el, n in cp]
        if all(a for _, _, a in Ms):
            Mfu = sum(n * a for _, n, a in Ms)
            r["mig_nuc"] = sum(n * VALENCE.get(el, 0) ** 2 for el, n, _ in Ms) / Mfu
            # POL diatomic route (binary 1:1 compounds only)
            zs, _ = get(mat, ["Zstar_bar", "Zstar_LST"], tags=("FT", "E"))
            einf, _ = get(mat, ["eps_inf"], tags=("FT",))
            wlo, _ = get(mat, ["omega_L", "omega_O_max"], tags=("FT",))
            if len(cp) == 2 and cp[0][1] == 1 and cp[1][1] == 1 and zs and einf and wlo:
                m1, m2 = Ms[0][2] * M_U, Ms[1][2] * M_U
                mu = m1 * m2 / (m1 + m2)
                val = (math.pi / 2) * 4 * math.pi * ALPHA * zs ** 2 / ((m1 + m2) * mu * einf ** 2 * wlo * 1e-3)
                r["POL_Zstar_meVcm3g"] = val * EV_CM3_G * 1e3
            e0 = None
            for x in xs:
                if x["property"] in ("eps_0",) and x["tag"] == "FT":
                    e0 = num(x["value"]); break
            vetted_bad = any(x["property"] == "GAP:eps_0_DFT_vetted" for x in xs)
            if e0 is None and not vetted_bad:
                e0, _ = get(mat, ["eps_0_DFT"], tags=("DB",))
            einf2 = einf or get(mat, ["eps_inf_DFT"], tags=("DB",))[0]
            wmax, _ = get(mat, ["omega_O_max", "omega_Gamma_max_DFT"], tags=("FT", "DB"))
            if e0 and einf2 and wmax and rho and e0 > einf2 and VALENCE and not mat in ("Si", "Ge", "C"):
                r["POL_eps_ub_meVcm3g"] = (math.pi / 2) * (1 / einf2 - 1 / e0) * wmax / rho
        ee, esrc = get(mat, ["eps_eh"], tags=("FT",))
        if ee is None:
            ee, esrc = get(mat, ["eps_eh_pred_GAPEF"], tags=("E",))
        r["eps_eh"], r["eps_src"] = ee, esrc
        s4 = [x["value"] for x in xs if x["property"] == "S4_verdict"]
        r["S4"] = s4[0] if s4 else "PASS (no primordial isotope)"
        out[mat] = r
    if "Si" in out and out["Si"].get("c_LA"):
        for m, r in out.items():
            if r.get("c_LA"):
                r["NR1_rel_Si"] = out["Si"]["c_LA"] / r["c_LA"]
    return out


def ranking(out, key, reverse=True):
    items = [(m, r[key]) for m, r in out.items() if r.get(key)]
    items.sort(key=lambda t: t[1], reverse=reverse)
    ranks, tier, last = [], 0, None
    for m, v in items:
        if last is None or abs(math.log(v) - math.log(last)) >= DR:
            tier += 1; last = v
        ranks.append((m, v, tier))
    return ranks


if __name__ == "__main__":
    out = build()
    res = {"per_material": out}
    for key, rev in (("m_floor_MeV", False), ("NR1_rel_Si", True), ("m_ac_keV_1meV", False), ("POL_Zstar_meVcm3g", True),
                     ("POL_eps_ub_meVcm3g", True), ("mig_nuc", True), ("eps_eh", False)):
        res[key] = ranking(out, key, reverse=rev)
    json.dump(res, open(os.path.join(HERE, "data", "ranking.json"), "w"), indent=1)
    for key in ("m_floor_MeV", "NR1_rel_Si", "POL_Zstar_meVcm3g", "POL_eps_ub_meVcm3g", "mig_nuc", "eps_eh"):
        print(key, ["%s %.3g (t%d)" % t for t in res[key][:12]])
