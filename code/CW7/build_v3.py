"""CW7 (LE-19, LE-176, LE-177): build returns/R16/WP8-U-table-v3.csv from returns/R14/WP8-U-table-v2.csv.
Every v2 row is kept verbatim. Changes are NEW rows; a row that replaces a v2 value has a note starting
'supersedes R14 <property>=<value>' (or 'supersedes R13 ...' where the v2 row is an R13 row).
Offline: every value below is quoted from a full text in literature/papers-CW7/ (page = PDF page), from the cached
JARVIS extract code/WP8-U/data/jarvis_extract.json, or from a campaign return (GAP-EF §3)."""
import csv, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
V2 = os.path.join(ROOT, "returns/R14/WP8-U-table-v2.csv")
V3 = os.path.join(ROOT, "returns/R16/WP8-U-table-v3.csv")
JAR = os.path.join(ROOT, "code/WP8-U/data/jarvis_extract.json")
GAPEF = os.path.join(ROOT, "returns/R14/GAP-EF.md")
COLS = ["material", "label", "group", "verdict", "property", "value", "unit", "tag", "source", "locator", "note"]

rows = list(csv.DictReader(open(V2)))
meta = {}
for x in rows:
    meta.setdefault(x["material"], (x["label"], x["group"], x["verdict"]))
new = []


def add(mat, prop, val, unit, tag, src, loc, note, verdict=None):
    lab, grp, ver = meta.get(mat, (mat, "-", "-"))
    new.append(dict(material=mat, label=lab, group=grp, verdict=verdict or ver, property=prop, value=str(val), unit=unit,
                    tag=tag, source=src, locator=loc, note=note))


def v2(mat, prop):
    return [x for x in rows if x["material"] == mat and x["property"] == prop]


# 1. screening renames screen_C* -> screen_S* (REF-WP8-U-A D4); values copied verbatim
for x in rows:
    m = re.fullmatch(r"screen_C([123])", x["property"])
    if m:
        y = dict(x); y["property"] = "screen_S" + m.group(1)
        y["note"] = ("renames R13 " + x["property"] + " (collides with CONTROLS C1-C8); " + x["note"]).strip("; ")
        new.append(y)
# GaAs S1/S2 from the full text (REF-WP8-U-A F3, REF-WP8-U-B V1)
add("GaAs", "screen_S2", "PASS: 'a 4.3 g GaAs (GaAs-1)' and 3.5 g GaAs-2 crystals operated as scintillating calorimeters",
    "-", "FT", "arXiv:2507.07119", "p.1 abstract; p.2 (0.5 mm, 4.3 g; 0.325 mm, 3.5 g)",
    "supersedes R13 screen_C2=PASS [E]; >= 1 g detector-grade GaAs demonstrated, so GaAs stays SURVIVOR")
add("GaAs", "screen_S1", "PASS: mK scintillating-calorimeter operation", "-", "FT", "arXiv:2507.07119", "p.1-2",
    "supersedes R13 screen_C1 evidence tag [ABS]")
# 1b. one screening rule (REF-WP8-U-A F3, V3; REF-WP8-U-B V2): FAIL needs positive evidence against the criterion; an item shown
#     only as a proposal, or with an unshown mass, is COND everywhere. S1 PASS needs a demonstrated mK operation.
for mat in ("NiPS3", "hBN", "cBN", "PE"):
    add(mat, "verdict", "SURVIVOR-COND", "-", "see text", "WP8-U-v2 §2 (one rule)", "-",
        "supersedes R13 verdict=EXCLUDED: the FAIL rested on [E]/[UNVERIFIED] or proposal-only evidence", verdict="SURVIVOR-COND")
for mat in ("GaN", "AlN", "ZnO", "GaSb", "MgO", "CaF2", "MgF2", "SiC-3C", "SiC-4H", "SiC-6H", "SiO2-q"):
    add(mat, "screen_S1", "COND: no harmful transition expected [UNVERIFIED]; no mK operation demonstrated in the sources read", "-",
        "UNVERIFIED", "WP8-U-v2 §2", "-", "supersedes R13 screen_C1=PASS [E]: [E] is a step tag, not evidence; verdict unchanged (SURVIVOR-COND)")
# 2. Ge-76 (REF-WP8-U-A E2(i), REF-WP8-U-B C5)
add("Ge", "primordial_radioisotopes", "76Ge (2nu-beta-beta)", "-", "FT", "arXiv:1901.07569", "Table I p.2 (natural radioactive isotopes row)",
    "supersedes R13 primordial_radioisotopes=none (the cached IAEA extract lists 76Ge as STABLE)")
add("Ge", "GAP:specific_activity_76Ge", "GAP", "Bq/kg", "GAP", "-", "-",
    "T1/2(76Ge) not read in full text here; referees quote ~1e-5 Bq/kg [UNVERIFIED]; negligible against the S4 budget either way")
# 3. lower-limit-driven activities printed as upper bounds
for mat in ("TeO2", "PbTe", "PbS", "PbSe", "ZrTe5", "ZnO", "ZnS", "Cr2O3"):
    for x in v2(mat, "specific_activity_intrinsic"):
        add(mat, "specific_activity_intrinsic_ub", "< " + x["value"], "Bq/kg", "E", x["source"], "-",
            "supersedes R13 specific_activity_intrinsic=" + x["value"] + " (dominated by T1/2 lower limits: an upper bound, not an activity)")
add("TeO2", "specific_activity_observed_E", "3.6e-05", "Bq/kg", "E", "IAEA half-lives x NIST abundances (128Te, 130Te only)", "-",
    "observed 2nu-beta-beta emitters only (REF-WP8-U-A E2(ii)); the 123Te EC term is an unobserved-decay bound")
# 4. SiC-6H E_d and 3C eps_eh label (REF-WP8-U-A E3, D7)
add("SiC-6H", "E_d", "22 (C)", "eV", "FT", "arXiv:2008.08560", "Table I p.5 (Edefect row, 6H column)", "fills the missing explicit item")
add("SiC-3C", "eps_eh_estimated", "5.7-7.7", "eV", "FT", "arXiv:2008.08560", "Table I p.5 (dagger: estimated in the text)",
    "supersedes R13 eps_eh label: an estimate of 2008.08560, not a measurement (measured 3C value: 6.9 eV, 2610.16949 Table II, R14 row)")
# 5. non-polar crystals: eps_inf = eps_0 (REF-WP8-U-A D1)
for mat, v in (("Si", "11.7"), ("Ge", "16.0"), ("C", "5.7")):
    add(mat, "eps_inf", v, "-", "FT", "arXiv:1901.07569", "Table I p.2 ('relative permittivity')",
        "non-polar (Z* = 0, WP2-v3 (4.5) [D]): eps_inf = eps_0; supersedes the use of the R13 eps_inf_DFT row as eps_inf")
# 6. IR-failure gate applied to eps_0_DFT (REF-WP8-U-A E1, REF-WP8-U-B C1); InSb metallic-run rule (B C2)
jar = json.load(open(JAR))
failed = []
for x in rows:
    if x["property"] != "eps_0_DFT":
        continue
    jid = re.search(r"JVASP-\d+", x["source"]).group(0)
    ir = jar.get(jid, {}).get("max_ir_mode", "na")
    gap = jar.get(jid, {}).get("optb88vdw_bandgap", "na")
    bad_ir = (ir == "na") or (float(ir) < 20.0)
    bad_gap = (gap != "na") and float(gap) < 0.05
    if bad_ir or bad_gap:
        failed.append((x["material"], jid, ir, gap))
        why = ("max_ir_mode = %s cm-1 (< 20: failed IR run)" % ir) if bad_ir else ""
        why += ("; " if why and bad_gap else "") + ("OptB88vdW gap %s eV (metallic DFPT ground state)" % gap if bad_gap else "")
        add(x["material"], "GAP:eps_0_DFT_vetted", "GAP", "-", "GAP", x["source"], "-",
            "supersedes R13 eps_0_DFT=" + x["value"] + ": " + why + "; WP8-U-v2 vetting rule V2")
json.dump(failed, open(os.path.join(HERE, "data", "failed_ir.json"), "w"), indent=1)
add("SrTiO3", "polymorph_note", "properties from cubic Pm-3m JVASP-8082; the mK phase is tetragonal I4/mcm (JVASP-269)", "-", "DB",
    "JARVIS-DFT dft_3d 9-24-2025", "-", "declared exception to the space-group rule (REF-WP8-U-A D5)")
# 7. LE-176: measured low-T eps_0 of the incipient ferroelectrics
add("SrTiO3", "eps_0_lowT", "~2e4 (chi^-1 = 5e-5 at 0.3 K)", "-", "FT", "arXiv:0903.1445", "Table 1 p.6 (a = chi^-1, fit at 0.3 K)",
    "supersedes R13 eps_0_DFT=9.963; single crystal; quantum paraelectric")
add("SrTiO3", "eps_0_lowT", "23,000 at 4 K (literature value quoted); 27,400 extracted from a resonator", "-", "FT", "arXiv:1607.08146",
    "p.1 (eps_r = 23,000 at 4K, refs [7-]); p.2 (27,400)", "the 27,400 is a film-on-substrate device extraction")
add("KTaO3", "eps_0_lowT", "~5e3 (chi^-1 = 2e-4 at 0.3 K)", "-", "FT", "arXiv:0903.1445", "Table 1 p.6",
    "supersedes R13 eps_0_DFT=385.9; KTaO3 is EXCLUDED-RADIO (S4) in any case")
add("PbTe", "eps_0_lowT", "> 1000 at low temperature", "-", "FT", "arXiv:1003.5140", "p.11 ('huge dielectric constant of PbTe at low temperatures ( > 1000)')",
    "supersedes R13 eps_0_DFT=498.6 as a low-T value (lower bound only)")
for mat in ("PbS", "PbSe"):
    add(mat, "GAP:eps_0_lowT", "GAP", "-", "GAP", "-", "-",
        "no measured low-T eps_0 in the full texts read; DFPT value (soft TO) unusable; POL/ER FOMs shown insensitive to eps_0 (CW7 LE-176)")
# 8. flags without values (referee numbers that are [UNVERIFIED] are carried as flags, not values)
add("Al", "flag_Delta_BCS", "0.3 meV is the working value of 2109.04473; 1.764 k_B T_c ~ 0.18 meV for T_c = 1.2 K [UNVERIFIED]", "-", "E",
    "REF-WP8-U-A C6", "-", "a FOM using 0.3 meV carries a factor ~1.7 uncertainty until a measured bulk gap is tabulated (IF-U6)")
add("ZrTe5", "Delta_D_definition", "half-gap: '2 Delta is the band gap' (Eq. (1.1)); 'band gap ... 23.6 meV, which corresponds to Delta = 11.8 meV'",
    "-", "FT", "arXiv:1910.02091", "Eq. (1.1); text near Table 1 (REF-WP8-U-A C4, REF-WP8-U-B L3)",
    "IF-U5 closed: Delta_D = 11.75 meV is the half-gap; the Table 1 caption word 'band gaps' is loose")
for mat in ("GaN", "AlN", "ZnO", "SiO2-q", "NaCl"):
    add(mat, "flag_c_LA_1910", "suspect, pending measured C_ij (DFT vs DFT disagreement; outside every Christoffel direction)", "-", "E",
        "REF-WP8-U-B L2; WP8-U-TOP §3.2", "-", "use c_LA_recommended; status word 'source defect' withdrawn")
for mat in ("SiC-3C", "SiC-4H", "SiC-6H"):
    add(mat, "flag_c_avg", "2008.08560 'cs' is undefined and exceeds c_L_iso; not an average phonon speed", "-", "E", "REF-WP8-U-B C3", "-",
        "supersedes R13 c_avg note ''cs' average phonon speed (measured)''")
add("C", "flag_omega_T", "non-polar: TO = LO at Gamma; use omega_max 161-163 meV, no omega_T", "-", "D", "REF-WP8-U-B C9", "-",
    "the 141/148 meV entries are not zone-centre values")
add("Ge", "flag_E_g_054", "0.54 eV (1901.07569) matches no tabulated Ge gap [UNVERIFIED]; do not use", "-", "E", "REF-WP8-U-B C8", "-", "")
add("YIG", "s_spin", "S_cell/Omega = 20/a^3 (net spin density); Fe density 40/a^3", "-", "FT", "arXiv:1905.13744", "p.4",
    "renames R13 spin_density (REF-WP8-U-A C5, REF-WP8-U-B C4)")
# 9. LE-177: cosmogenic production rates at sea level [FT]
CW = "literature/papers-CW7"
for iso, nn, tot in (("3H", "112 +- 24", "124 +- 25"), ("7Be", "8.1 +- 1.9", "9.4 +- 2.0"), ("22Na", "43.0 +- 7.2", "49.6 +- 7.4")):
    add("Si", "cosmo_rate_" + iso, "%s (neutrons); %s (all cosmic rays)" % (nn, tot), "atoms/(kg d)", "FT", "arXiv:2007.10584", "p.1 abstract",
        "sea level; measured with a neutron beam plus model for other particles")
for iso, val, loc in (("3H", "82 +- 21", "p.2, p.21 (text); Table p.28: 82 +- 12 (fit errors)"), ("49V", "2.8 +- 0.6", "p.21; Table p.28"),
                      ("55Fe", "4.6 +- 0.7", "p.21; Table p.28"), ("65Zn", "106 +- 13", "p.21 (text); Table p.28: 106 +- 10"),
                      ("68Ge", ">= 74 (90% C.L. lower limit); Table p.28: 202 +- 16 (fit), 84 +- 3 (saturation assumption)", "p.2, p.21; Table p.28")):
    add("Ge", "cosmo_rate_" + iso, val, "nuclei/(kg d)", "FT", "arXiv:1607.04560", loc, "sea level; EDELWEISS-III Ge detectors")
for iso, val in (("126I", "283 +- 36"), ("125I", "220 +- 10"), ("127mTe", "10.2 +- 0.4"), ("125mTe", "28.2 +- 1.3"), ("123mTe", "31.6 +- 1.1"),
                 ("121mTe", "23.5 +- 0.8"), ("121Te", "9.9 +- 3.7"), ("22Na", "45.1 +- 1.9")):
    add("NaI", "cosmo_rate_" + iso, val, "/(kg d)", "FT", "arXiv:1411.0106", "Table 6 p.15", "sea level, deduced from ANAIS underground data")
for iso, val in (("124Sb", "182.0"), ("110mAg", "2.39"), ("60Co", "0.81"), ("22Na", "1.01")):
    add("TeO2", "cosmo_Asat_natTe_" + iso, val, "uBq/kg (natTe)", "FT", "arXiv:1411.5947", "Table 4 p.10",
        "calc. (ACTIVIA, Armstrong-Gehrels flux); per kg of natural Te, not TeO2")
add("CaWO4", "cosmo_identified", "179Ta (EC), 181W (EC) and the associated 3H observed in CRESST data", "-", "FT", "arXiv:1908.06755", "p.4 §2.3.2; p.15",
    "production rates at sea level not given; GAP for the rate")
for mat in sorted(meta):
    v = meta[mat][2]
    if v in ("SURVIVOR", "SURVIVOR-COND") and mat not in ("Si", "Ge", "NaI", "TeO2"):
        add(mat, "GAP:cosmo_production", "GAP", "atoms/(kg d)", "GAP", "-", "-",
            "no measured or computed sea-level production rate in the full texts read; computation spec: CW7 LE-177 (ACTIVIA/Geant4)")
add("ALL", "GAP:Pb210_U_Th", "GAP", "Bq/kg", "GAP", "-", "-",
    "210Pb, U/Th: process and surface contamination, not a material property (WP8-F §2.8(iii)); lead salts: depends on the lead source")
# 10. GAP-EF predictions [E] for materials without a measurement (IF-EF3)
names = {"SiO2-q": "SiO2-q", "4H-SiC": "SiC-4H"}
txt = open(GAPEF).read().split("\n")
i0 = [k for k, l in enumerate(txt) if l.startswith("| Material (WP8-U verdict)")][0]
for l in txt[i0 + 2:]:
    if not l.startswith("|"):
        break
    c = [s.strip() for s in l.strip("|").split("|")]
    mat = c[0].split(" (")[0].replace("₂", "2").replace("₃", "3").replace("₄", "4")
    mat = names.get(mat, mat)
    if mat not in meta:
        continue
    fonly = "F only" in c[0]
    if not fonly:
        add(mat, "eps_eh_pred_GAPEF", c[3], "eV", "E", "returns/R14/GAP-EF.md", "§3 table", "one-parameter cascade model; band in brackets; prefer [FT] where present")
    add(mat, "F_eh_pred_GAPEF", c[5], "-", "E", "returns/R14/GAP-EF.md", "§3 table", "one-parameter cascade model; band in brackets")

with open(V3, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    for x in rows + new:
        w.writerow({k: x[k] for k in COLS})
print("v2 rows", len(rows), "new rows", len(new), "failed-IR/metallic eps_0 rows", len(failed))
