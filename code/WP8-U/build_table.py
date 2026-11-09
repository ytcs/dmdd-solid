"""WP8-U: build returns/R13/WP8-U-table.csv (long format, one provenance tag per value) from the cached extracts.

Offline. Inputs: data/*.json (fetch_db.py), lit_values.py (full text), screening.py, materials.py.
Closed-form [E] estimates only (densities from lattice constants, Debye temperature, plasma frequency, isotope
mass variance, Tamura coefficient, LST, specific activity). No first-principles numerics.
Usage: python3 -I build_table.py [out.csv]   (also writes data/coverage.json for the md coverage matrix)
"""
import csv, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from materials import MATERIALS, VALENCE  # noqa: E402
from lit_values import FT  # noqa: E402
from screening import S as SCREEN  # noqa: E402

D = lambda f: json.load(open(os.path.join(HERE, "data", f)))
J, MP, AL, NIST, IA = D("jarvis_extract.json"), D("optimade_mp.json"), D("optimade_alex.json"), D("nist_isotopes.json"), D("iaea_gs.json")["rows"]

NA, HBAR, KB, EV, ME, EPS0, CM1_MEV = 6.02214076e23, 1.054571817e-34, 1.380649e-23, 1.602176634e-19, 9.1093837015e-31, 8.8541878128e-12, 0.12398419843
YEAR = 3.15576e7
DBJ = "JARVIS-DFT dft_3d 9-24-2025 (figshare 64391379)"
rows = []


def add(m, p, v, u, tag, src, loc="", note=""):
    rows.append({"material": m, "label": MATERIALS[m][0], "group": MATERIALS[m][5], "verdict": SCREEN[m][3],
                 "property": p, "value": v, "unit": u, "tag": tag, "source": src, "locator": loc, "note": note})


def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def mean_mass(el):
    iso = NIST[el]["isotopes"]
    s = sum(i["abundance"] for i in iso if i["abundance"])
    return sum(i["mass"] * i["abundance"] for i in iso if i["abundance"]) / s


def g2(el):  # isotope mass-variance parameter g2 = sum_i x_i (1 - m_i/mbar)^2
    iso = [i for i in NIST[el]["isotopes"] if i["abundance"]]
    mb = mean_mass(el)
    return sum(i["abundance"] * (1 - i["mass"] / mb) ** 2 for i in iso)


def spin(el, A):
    for r in IA:
        if r["sym"] == el and r["A"] == A:
            return r["jp"]
    return "?"


def cell_volume(lat):
    a, b, c = lat
    return abs(a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0]))


def ft(m, p):
    return [r for r in FT if r[0] == m and r[1] == p]


# formula units per conventional cell and cell-volume law, for densities from experimental lattice constants
CELL = {"Si": (8, "cub"), "Ge": (8, "cub"), "C": (8, "cub"), "GaAs": (4, "cub"), "InSb": (4, "cub"), "GaSb": (4, "cub"),
        "ZnS": (4, "cub"), "LiF": (4, "cub"), "NaF": (4, "cub"), "NaCl": (4, "cub"), "NaI": (4, "cub"), "MgO": (4, "cub"),
        "PbS": (4, "cub"), "PbSe": (4, "cub"), "PbTe": (4, "cub"), "CaF2": (4, "cub"), "CsI": (1, "cub"),
        "GaN": (2, "hex"), "AlN": (2, "hex"), "ZnO": (2, "hex"), "Al2O3": (6, "hex"), "SiO2-q": (3, "hex"),
        "CaWO4": (4, "tet"), "MgF2": (2, "tet"), "YIG": (8, "cub")}


def rho_from_lattice(m):
    a = [r[2] for r in ft(m, "a_exp")]
    c = [r[2] for r in ft(m, "c_exp")]
    if m not in CELL or not a or not num(a[0]):
        return None
    z, law = CELL[m]
    a = a[0] * 1e-8
    V = a ** 3 if law == "cub" else (math.sqrt(3) / 2 * a * a * c[0] * 1e-8 if law == "hex" else a * a * c[0] * 1e-8)
    M = sum(n * mean_mass(e) for e, n in MATERIALS[m][1].items())
    return z * M / (NA * V)


COV = {}
for m, (label, comp, jid, mp, alex, group) in MATERIALS.items():
    Mfu = sum(n * mean_mass(e) for e, n in comp.items())
    nat_fu = sum(comp.values())
    # --- screening
    for i, c in enumerate(("screen_C1", "screen_C2", "screen_C3")):
        add(m, c, SCREEN[m][i], "-", "see text", "screening.py", "", "")
    add(m, "verdict", SCREEN[m][3], "-", "-", "screening.py")
    # --- composition, Z, A, isotopes, nuclear spins (NIST + IAEA)
    add(m, "composition", " ".join(f"{e}{n if n > 1 else ''}" for e, n in comp.items()), "-", "-", "materials.py")
    for e in comp:
        iso = [i for i in NIST[e]["isotopes"] if i["abundance"]]
        add(m, f"Z[{e}]", NIST[e]["Z"], "-", "DB", "NIST Atomic Weights & Isotopic Compositions (ascii2)")
        add(m, f"A[{e}]", round(mean_mass(e), 4), "u", "DB", "NIST ascii2 (abundance-weighted relative atomic mass)",
            "", f"std weight {NIST[e]['std_weight']}")
        add(m, f"isotopes[{e}]", "; ".join(f"{i['A']}{e} x={i['abundance']} J={spin(e, i['A'])}" for i in iso), "-", "DB",
            "NIST ascii2 (x); IAEA LiveChart ground_states ENSDF (J^pi)")
        odd = [f"{i['A']}{e}({spin(e, i['A'])}, x={i['abundance']})" for i in iso if spin(e, i["A"]) not in ("0+", "?")]
        add(m, f"nuclear_spin[{e}]", "; ".join(odd) if odd else "none (all J=0)", "-", "DB", "IAEA LiveChart ground_states")
        add(m, f"g2_iso[{e}]", f"{g2(e):.3e}", "-", "E", "from NIST ascii2", "", "g2 = sum_i x_i (1 - m_i/mbar)^2")
    # --- primordial radio-isotopes of constituents and specific activity
    act, lst, lower = 0.0, [], False
    for e, n in comp.items():
        for r in IA:
            if r["sym"] == e and r["abundance_pct"] and r["half_life"] not in ("STABLE", "") and r["unit_hl"] == "Y":
                T = float(r["half_life"]) * YEAR
                N = n * float(r["abundance_pct"]) / 100 * NA / Mfu * 1000  # per kg
                a = math.log(2) / T * N
                op = r["operator_hl"]
                lst.append(f"{r['A']}{e} ({r['decay_1']}, T1/2 {'>' if op in ('GT', 'GE') else ''}{r['half_life']} y)")
                if op in ("GT", "GE"):
                    lower = True
                act += a
    if not lst:
        add(m, "primordial_radioisotopes", "none among natural isotopes of the constituents", "-", "DB", "IAEA LiveChart ground_states",
            "", "cosmogenic and contamination backgrounds not covered")
    if lst:
        add(m, "primordial_radioisotopes", "; ".join(lst), "-", "DB", "IAEA LiveChart ground_states")
        add(m, "specific_activity_intrinsic", f"{act:.3g}", "Bq/kg", "E", "from IAEA half-lives and NIST abundances", "",
            "upper bound (some T1/2 are lower limits)" if lower else "")
    # --- JARVIS database values
    if jid:
        x = J[jid]
        src = f"{DBJ} {jid}"
        add(m, "db_ids", f"{jid}; {mp}; spg {x['spg_symbol']} ({x['spg_number']}); nat {x['nat']}", "-", "DB", src)
        if num(x["density"]):
            add(m, "rho_T_DFT", x["density"], "g/cm3", "DB", src, "density", "OptB88vdW-relaxed cell")
        for k, name in (("optb88vdw_bandgap", "OptB88vdW"), ("mbj_bandgap", "TBmBJ"), ("hse_gap", "HSE06")):
            if num(x[k]):
                add(m, f"E_g_DFT_{name}", x[k], "eV", "DB", src, k, "DFT proxy, not the low-T experimental gap" +
                    ("; magnetic oxide without +U: gap not physical" if group == "magnetic" and x[k] < 0.8 else ""))
        metallic = (num(x["optb88vdw_bandgap"]) and x["optb88vdw_bandgap"] < 0.05) and not (num(x["mbj_bandgap"]) and x["mbj_bandgap"] > 0.05)
        if num(x["dfpt_piezo_max_dielectric_electronic"]) and x["dfpt_piezo_max_dielectric_electronic"] < 60:
            add(m, "eps_inf_DFT", round(x["dfpt_piezo_max_dielectric_electronic"], 3), "-", "DB", src,
                "dfpt_piezo_max_dielectric_electronic", "DFPT OptB88vdW, max principal value")
        elif all(num(x[k]) for k in ("mepsx", "mepsy", "mepsz")) and not metallic and not (num(x["mbj_bandgap"]) and x["mbj_bandgap"] < 0.05):
            add(m, "eps_inf_DFT", round((x["mepsx"] + x["mepsy"] + x["mepsz"]) / 3, 3), "-", "DB", src, "mepsx/y/z mean",
                "TBmBJ linear optics, IP without local fields")
        if num(x["dfpt_piezo_max_dielectric"]) and x["dfpt_piezo_max_dielectric"] < 1000 and not metallic:
            add(m, "eps_0_DFT", round(x["dfpt_piezo_max_dielectric"], 3), "-", "DB", src, "dfpt_piezo_max_dielectric",
                "DFPT total (electronic + ionic), max principal value; 0 K harmonic")
        if num(x["max_ir_mode"]) and x["max_ir_mode"] >= 20:
            add(m, "omega_T_maxIR_DFT", round(x["max_ir_mode"] * CM1_MEV, 2), "meV", "DB", src, "max_ir_mode",
                f"{x['max_ir_mode']} cm-1, highest IR-active Gamma mode")
        if isinstance(x["modes"], list) and x["modes"] and x["nat"] > 1:
            add(m, "omega_Gamma_max_DFT", round(max(x["modes"]) * CM1_MEV, 2), "meV", "DB", src, "modes",
                f"max finite-difference Gamma mode {max(x['modes'])} cm-1")
        for k, name in (("bulk_modulus_kv", "B_V"), ("shear_modulus_gv", "G_V")):
            if num(x[k]):
                add(m, name, x[k], "GPa", "DB", src, k, "Voigt average, OptB88vdW")
        for k, name in (("avg_elec_mass", "m_e_eff"), ("avg_hole_mass", "m_h_eff")):
            if num(x[k]) and x[k] > 0.005:
                add(m, name, round(x[k], 3), "m_e", "DB", src, k, "BoltzTraP 300 K conductivity mass, OptB88vdW")
        if num(x["magmom_outcar"]) and abs(x["magmom_outcar"]) > 0.1:
            add(m, "magmom_DFT", x["magmom_outcar"], "mu_B/cell", "DB", src, "magmom_outcar", "net moment (AFM cells ~0 ideal)")
        if num(x["Tc_supercon"]):
            add(m, "Tc_DFT", round(x["Tc_supercon"], 3), "K", "DB", src, "Tc_supercon", "DFT-predicted (McMillan), not measured")
        # [E] sound speeds and Debye temperature from the Voigt moduli
        if num(x["bulk_modulus_kv"]) and num(x["shear_modulus_gv"]) and x["shear_modulus_gv"] > 0 and num(x["density"]):
            rho = x["density"] * 1000
            vl = math.sqrt((x["bulk_modulus_kv"] + 4 / 3 * x["shear_modulus_gv"]) * 1e9 / rho)
            vt = math.sqrt(x["shear_modulus_gv"] * 1e9 / rho)
            vm = (1 / 3 * (2 / vt ** 3 + 1 / vl ** 3)) ** (-1 / 3)
            nat = x["nat"] / (cell_volume(x["lattice_mat"]) * 1e-30)
            th = HBAR / KB * vm * (6 * math.pi ** 2 * nat) ** (1 / 3)
            add(m, "c_L_iso", round(vl / 1000, 3), "km/s", "E", src, "sqrt((B+4G/3)/rho)", "isotropic Voigt estimate")
            add(m, "c_T_iso", round(vt / 1000, 3), "km/s", "E", src, "sqrt(G/rho)", "isotropic Voigt estimate")
            add(m, "theta_D_E", round(th, 1), "K", "E", src, "Anderson: (hbar/kB) v_m (6 pi^2 n_at)^(1/3)", "elastic Debye T")
            if len(comp) == 1:  # Tamura isotope coefficient tau^-1 = A_iso omega^4, A_iso = V_a g2/(4 pi v_m^3)
                e = list(comp)[0]
                A = (1 / nat) * g2(e) / (4 * math.pi * vm ** 3)
                add(m, "A_iso_Tamura", f"{A:.3e}", "s^3", "E", "g2 (NIST) + v_m (JARVIS moduli)", "tau^-1 = A omega^4",
                    "isotropic Debye-averaged; nu-form A(2 pi)^4 = %.3e s^3" % (A * (2 * math.pi) ** 4))
        # [E] LST omega_L for binary cubic crystals with physical DB inputs
        if (x["spg_number"] in ("216", "225", "221")) and len(comp) == 2 and num(x["max_ir_mode"]) and x["max_ir_mode"] >= 20 \
                and num(x["dfpt_piezo_max_dielectric"]) and num(x["dfpt_piezo_max_dielectric_electronic"]) and not metallic:
            wl = x["max_ir_mode"] * CM1_MEV * math.sqrt(x["dfpt_piezo_max_dielectric"] / x["dfpt_piezo_max_dielectric_electronic"])
            add(m, "omega_L_LST", round(wl, 2), "meV", "E", src, "omega_T sqrt(eps_0/eps_inf), single polar mode", "")
    if mp and mp in MP:
        eh = MP[mp]["e_above_hull"]
        k = "r2scan" if eh.get("r2scan") is not None else ("gga_gga+u" if "gga_gga+u" in eh else None)
        if k:
            add(m, "E_hull_MP", round(eh[k], 4), "eV/atom", "DB", f"MP OPTIMADE {mp}", "_mp_stability." + k, "energy above hull")
    if alex:
        r = AL[m][0]
        src = f"Alexandria PBE OPTIMADE {r['id']}"
        add(m, "E_g_DFT_PBE", r["_alexandria_band_gap"], "eV", "DB", src, "_alexandria_band_gap",
            "PBE; " + ("PBE without U, magnetic insulator predicted metallic: not physical" if m == "YIG" else "DFT proxy"))
        add(m, "E_g_direct_DFT_PBE", r["_alexandria_band_gap_direct"], "eV", "DB", src, "_alexandria_band_gap_direct")
        if abs(r["_alexandria_magnetization"]) > 0.5:
            add(m, "magmom_DFT", r["_alexandria_magnetization"], "mu_B/cell", "DB", src, "_alexandria_magnetization",
                f"{r['nsites']}-site cell")
    # --- full-text values
    for (mm, p, v, u, tag, s, loc, note) in FT:
        if mm == m:
            add(m, p, v, u, tag, s, loc, note)
    if group == "elemental":
        add(m, "Zstar_bar", 0, "e", "E", "symmetry", "", "elemental crystal, all sites equivalent + acoustic sum rule => Z* = 0")
    # --- [E] densities, valence electron density, plasma frequency
    rl = rho_from_lattice(m)
    if rl:
        add(m, "rho_T_from_a_exp", round(rl, 4), "g/cm3", "E", "a_exp (FT) + NIST masses", "", f"{CELL[m][0]} f.u. per cell")
    rho_ft = [r[2] for r in ft(m, "rho_T") if num(r[2])]
    rho_best = rho_ft[0] if rho_ft else (rl if rl else (J[jid]["density"] if jid and num(J[jid]["density"]) else None))
    if rho_best and all(e in VALENCE for e in comp):
        nval = sum(n * VALENCE[e] for e, n in comp.items())
        ne = rho_best * NA * nval / Mfu  # cm^-3
        wp = HBAR * math.sqrt(ne * 1e6 * EV ** 2 / (EPS0 * ME)) / EV
        add(m, "n_e_val", f"{ne / 1e23:.4f}", "1e23/cm3", "E", "rho (best) + valence convention (materials.VALENCE)",
            "", f"{nval} valence e per f.u.; rho={rho_best:.4g}")
        add(m, "omega_p_E", round(wp, 2), "eV", "E", "free-electron sqrt(n_e e^2/(eps0 m_e))", "", "valence plasma energy")

    # --- coverage of the brief's default property list (best tag per item; FT > DB > E > GAP)
    have = {}
    for r in rows:
        if r["material"] == m:
            have.setdefault(r["property"], []).append(r["tag"])
    REQ = {"rho": ["rho_T", "rho_T_from_a_exp", "rho_T_DFT"], "Z,A,iso": ["Z[", "A[", "isotopes["],
           "E_g": ["E_g", "E_g_T", "E_g_DFT_TBmBJ", "E_g_DFT_HSE06", "E_g_DFT_OptB88vdW", "E_g_DFT_PBE", "Delta_BCS", "Delta_D"],
           "eps_inf": ["eps_inf", "eps_inf_DFT", "eps_tensor"], "eps_0": ["eps_0", "eps_0_DFT", "eps_tensor"],
           "Z*": ["Zstar_bar"], "omega_T": ["omega_T", "omega_T_maxIR_DFT"],
           "omega_L": ["omega_L", "omega_L_LST"], "omega_max": ["omega_O_max", "omega_L", "omega_Gamma_max_DFT"],
           "c_sound": ["c_avg", "c_LA", "c_L_iso", "magnon_speed"], "theta_D": ["theta_D", "theta_D_E"],
           "n_e,omega_p": ["omega_p_meas", "omega_pl_meas", "n_e_val"], "m_eff": ["m_e_eff", "m_h_eff", "v_F", "E_F"],
           "eps_eh": ["eps_eh"], "F_eh": ["F_eh"], "ph_lifetime": ["phonon_lifetime", "phonon_mfp"],
           "isotope_scatt": ["A_iso_Tamura", "isotope_scattering", "g2_iso["], "nuc_spin": ["nuclear_spin["],
           "radio": ["radio_note", "isotopes_radioactive", "primordial_radioisotopes"]}
    if group == "magnetic":
        REQ["spin/magnon"] = ["spin_density", "spins", "c1_spin", "magnon_dispersion", "magmom_DFT", "magnon_gap"]
    cov = {}
    for item, props in REQ.items():
        tags = [t for p in props for k, ts in have.items() if (k == p or (p.endswith("[") and k.startswith(p))) for t in ts]
        best = next((t for t in ("FT", "DB", "E") if t in tags), "GAP")
        if best == "GAP" and group == "superconductor" and item in ("eps_inf", "eps_0", "Z*", "omega_T", "omega_L", "eps_eh", "F_eh"):
            best = "n/a"
        cov[item] = best
        if best == "GAP" and SCREEN[m][3] not in ("EXCLUDED", "REFERENCE"):
            add(m, "GAP:" + item, "GAP", "-", "GAP", "-", "", "not found in the sources read")
    COV[m] = cov

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "returns", "R13", "WP8-U-table.csv")
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
json.dump(COV, open(os.path.join(HERE, "data", "coverage.json"), "w"), indent=0)
print(len(rows), "rows ->", os.path.abspath(out))
