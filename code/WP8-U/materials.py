"""WP8-U material registry: candidate pool, database pointers and screening verdicts.

Every database pointer here was chosen by inspection of the JARVIS dft_3d (9-24-2025) dump and the MP / Alexandria
OPTIMADE endpoints (2026-11-01). Selection rule: experimental space group, then the entry with the most populated fields;
an entry whose max_ir_mode < 20 cm^-1 is a failed IR calculation (treated as GAP), and the sibling entry with the same
mp-ID and a physical IR mode is preferred when it exists (InSb, TeO2).
"""

# key: (label, composition per formula unit, JARVIS jid or None, MP id, Alexandria filter (formula, spg) or None, group)
MATERIALS = {
    "Si":      ("Si (diamond)",            {"Si": 1},                 "JVASP-1002",  "mp-149",    None, "elemental"),
    "Ge":      ("Ge (diamond)",            {"Ge": 1},                 "JVASP-890",   "mp-32",     None, "elemental"),
    "C":       ("C diamond",               {"C": 1},                  "JVASP-91",    "mp-66",     None, "elemental"),
    "SiC-3C":  ("3C-SiC",                  {"Si": 1, "C": 1},         "JVASP-8158",  "mp-8062",   None, "SiC"),
    "SiC-4H":  ("4H-SiC",                  {"Si": 1, "C": 1},         "JVASP-107",   "mp-11714",  None, "SiC"),
    "SiC-6H":  ("6H-SiC",                  {"Si": 1, "C": 1},         "JVASP-182",   "mp-7631",   None, "SiC"),
    "GaAs":    ("GaAs (zincblende)",       {"Ga": 1, "As": 1},        "JVASP-1174",  "mp-2534",   None, "III-V"),
    "GaN":     ("GaN (wurtzite)",          {"Ga": 1, "N": 1},         "JVASP-30",    "mp-804",    None, "III-V"),
    "AlN":     ("AlN (wurtzite)",          {"Al": 1, "N": 1},         "JVASP-39",    "mp-661",    None, "III-V"),
    "InSb":    ("InSb (zincblende)",       {"In": 1, "Sb": 1},        "JVASP-17580", "mp-20012",  None, "narrow-gap"),
    "GaSb":    ("GaSb (zincblende)",       {"Ga": 1, "Sb": 1},        "JVASP-1177",  "mp-1156",   None, "narrow-gap"),
    "Al2O3":   ("Al2O3 sapphire",          {"Al": 2, "O": 3},         "JVASP-32",    "mp-1143",   None, "oxide"),
    "SiO2-q":  ("alpha-SiO2 quartz",       {"Si": 1, "O": 2},         "JVASP-41",    "mp-6930",   None, "oxide"),
    "SiO2-a":  ("amorphous SiO2",          {"Si": 1, "O": 2},         None,          None,        None, "amorphous"),
    "ZnO":     ("ZnO (wurtzite)",          {"Zn": 1, "O": 1},         "JVASP-1195",  "mp-2133",   None, "oxide"),
    "MgO":     ("MgO",                     {"Mg": 1, "O": 1},         "JVASP-116",   "mp-1265",   None, "oxide"),
    "TeO2":    ("alpha-TeO2 paratellurite",{"Te": 1, "O": 2},         "JVASP-57128", "mp-561224", None, "oxide"),
    "CaWO4":   ("CaWO4 scheelite",         {"Ca": 1, "W": 1, "O": 4}, "JVASP-88542", "mp-19426",  None, "scintillator"),
    "Li2MoO4": ("Li2MoO4",                 {"Li": 2, "Mo": 1, "O": 4},None,          "mp-18050",  ("Li2MoO4", 148), "Li-rich"),
    "LiAlO2":  ("gamma-LiAlO2",            {"Li": 1, "Al": 1, "O": 2},"JVASP-9407",  "mp-3427",   None, "Li-rich"),
    "LiF":     ("LiF",                     {"Li": 1, "F": 1},         "JVASP-1130",  "mp-1138",   None, "Li-rich"),
    "NaF":     ("NaF",                     {"Na": 1, "F": 1},         "JVASP-20326", "mp-682",    None, "halide"),
    "NaCl":    ("NaCl",                    {"Na": 1, "Cl": 1},        "JVASP-23862", "mp-22862",  None, "halide"),
    "NaI":     ("NaI",                     {"Na": 1, "I": 1},         "JVASP-1996",  "mp-23268",  None, "halide"),
    "CsI":     ("CsI (CsCl type)",         {"Cs": 1, "I": 1},         None,          "mp-614603", ("CsI", 221), "halide"),
    "CaF2":    ("CaF2",                    {"Ca": 1, "F": 2},         "JVASP-20800", "mp-2741",   None, "halide"),
    "MgF2":    ("MgF2 (rutile)",           {"Mg": 1, "F": 2},         "JVASP-20134", "mp-1249",   None, "halide"),
    "ZnS":     ("ZnS (zincblende)",        {"Zn": 1, "S": 1},         "JVASP-1702",  "mp-10695",  None, "II-VI"),
    "PbTe":    ("PbTe",                    {"Pb": 1, "Te": 1},        "JVASP-1103",  "mp-19717",  None, "polar/narrow-gap"),
    "PbS":     ("PbS",                     {"Pb": 1, "S": 1},         "JVASP-254",   "mp-21276",  None, "polar/narrow-gap"),
    "PbSe":    ("PbSe",                    {"Pb": 1, "Se": 1},        "JVASP-21",    "mp-2201",   None, "polar/narrow-gap"),
    "SrTiO3":  ("SrTiO3",                  {"Sr": 1, "Ti": 1, "O": 3},"JVASP-8082",  "mp-5229",   None, "polar"),
    "KTaO3":   ("KTaO3",                   {"K": 1, "Ta": 1, "O": 3}, "JVASP-1127",  "mp-3614",   None, "polar"),
    "ZrTe5":   ("ZrTe5",                   {"Zr": 1, "Te": 5},        "JVASP-86924", "mp-605",    None, "Dirac"),
    "Bi2Se3":  ("Bi2Se3",                  {"Bi": 2, "Se": 3},        "JVASP-1067",  "mp-541837", None, "Dirac"),
    "Al":      ("Al",                      {"Al": 1},                 "JVASP-816",   "mp-134",    None, "superconductor"),
    "Nb":      ("Nb",                      {"Nb": 1},                 "JVASP-934",   "mp-75",     None, "superconductor"),
    "YIG":     ("Y3Fe5O12 (YIG)",          {"Y": 3, "Fe": 5, "O": 12},None,          "mp-4704",   ("Fe5O12Y3", 230), "magnetic"),
    "NiO":     ("NiO",                     {"Ni": 1, "O": 1},         "JVASP-7871",  "mp-19009",  None, "magnetic"),
    "MnO":     ("MnO",                     {"Mn": 1, "O": 1},         "JVASP-7870",  "mp-19006",  None, "magnetic"),
    "Cr2O3":   ("Cr2O3",                   {"Cr": 2, "O": 3},         "JVASP-12241", "mp-19399",  None, "magnetic"),
    # excluded or reference-only; kept for the exclusion record and sparse rows
    "NiPS3":   ("NiPS3",                   {"Ni": 1, "P": 1, "S": 3}, "JVASP-29973", "mp-676040", None, "magnetic"),
    "hBN":     ("h-BN",                    {"B": 1, "N": 1},          "JVASP-17",    "mp-984",    None, "BN"),
    "cBN":     ("c-BN",                    {"B": 1, "N": 1},          "JVASP-7836",  "mp-1639",   None, "BN"),
    "PE":      ("polyethylene (CH2)n",     {"C": 1, "H": 2},          "JVASP-33878", "mp-985782", None, "H-rich"),
    "He-s":    ("solid He (hcp)",          {"He": 1},                 "JVASP-25167", "mp-23156",  None, "reference"),
    "He-l":    ("superfluid 4He",          {"He": 1},                 None,          None,        None, "reference"),
}

# Elemental valence-electron convention for n_e (count per atom). Outer s+p for main-group elements; outer s+d for
# open-d transition metals; filled d10 shells (Zn, Ga, In, Ge, As, Se, Sb, Te, Pb, Bi, Cd) are semicore and NOT counted.
# This is a stated convention [E]; it reproduces 4 e/atom for C, Si, Ge (2008.08560 Table I, 1901.07569).
VALENCE = {"H": 1, "He": 2, "Li": 1, "B": 3, "C": 4, "N": 5, "O": 6, "F": 7, "Na": 1, "Mg": 2, "Al": 3, "Si": 4,
           "P": 5, "S": 6, "Cl": 7, "K": 1, "Ca": 2, "Ti": 4, "Cr": 6, "Mn": 7, "Fe": 8, "Ni": 10, "Zn": 2, "Ga": 3,
           "Ge": 4, "As": 5, "Se": 6, "Sr": 2, "Y": 3, "Zr": 4, "Nb": 5, "Mo": 6, "In": 3, "Sb": 5, "Te": 6, "I": 7,
           "Cs": 1, "Ta": 5, "W": 6, "Pb": 4, "Bi": 5}

ELEMENTS = sorted({e for v in MATERIALS.values() for e in v[1]})
