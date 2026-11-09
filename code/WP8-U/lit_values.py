"""WP8-U full-text values. Each row: (material key, property, value, unit, tag, source, locator, note).

Every arXiv ID below was verified against export.arxiv.org (titles in WP8-U.md §7). The PDFs were read with
pdftotext -layout; 'p.N' is the PDF page (form-feed count). Values are transcribed verbatim from the cited table/line.
"""

FT = []
def add(m, p, v, u, src, loc, note="", tag="FT"):
    FT.append((m, p, v, u, tag, src, loc, note))

# ---------------------------------------------------------------------------------------------------------------
# 1910.10716 (Griffin, Inzani, Trickle, Zhang, Zurek, "Multichannel direct detection of light DM: target comparison")
# Table I, p.2: Eg [eV] experimental ('*' = measured at low T), c_s^LA [1e-5 c] (DFT, averaged over a q ~ 10 eV
# sphere, App. A3 p.13), A_j, Zbar* = Tr Z*_+/3 (DFPT), eps_inf = Tr eps_inf/3 (DFPT), omega_O range [meV] (DFT),
# Q [1e-7] (their Eq. (27) quality factor).
T1 = [  # name, key, Eg, star, cLA, A, Z, einf, wO_lo, wO_hi, Q
    ("Si", "Si", 1.11, 0, 2.84, "28.1", None, None, 62.3, 62.3, None),
    ("Ge", "Ge", 0.67, 0, 1.61, "72.6", None, None, 34.8, 34.8, None),
    ("NaI", "NaI", 5.8, 0, 0.90, "23.0, 127", 1.20, 3.27, 12.4, 20.0, 23),
    ("CsI", "CsI", 6.14, 0, 0.46, "133, 127", 1.22, 2.70, 6.9, 10.0, 12),
    ("CaWO4", "CaWO4", 5.2, 0, 1.42, "40, 184, 16", "2.84, 4.67", 3.84, 8.48, 106, 45),
    ("GaAs", "GaAs", 1.42, 0, 1.57, "69.7, 74.9", 2.27, 10.9, 31.8, 34.9, 2.4),
    ("Al2O3", "Al2O3", 8.8, 0, 3.51, "27.0, 16.0", 2.97, 3.26, 35.6, 104, 130),
    ("Diamond", "C", 5.47, 1, 5.98, "12.0", None, None, 161, 161, None),
    ("SiO2", "SiO2-q", 9.2, 0, 5.76, "28.1, 16.0", 3.38, 2.41, 13.7, 149, 200),
    ("PbTe", "PbTe", 0.19, 1, 1.17, "207, 128", 5.69, 26.3, 3.91, 13.5, 1.3),
    ("InSb", "InSb", 0.24, 1, 1.13, "115, 122", 2.40, 23.7, 20.5, 21.5, 0.34),
    ("AlN", "AlN", 6.20, 0, 5.70, "27.0, 14.0", 2.57, 4.54, 29.4, 109, 78),
    ("CaF2", "CaF2", 11.81, 0, 2.15, "40, 19.0", 2.36, 2.26, 28.4, 55.6, 130),
    ("GaN", "GaN", 3.43, 1, 4.17, "69.7, 14.0", 2.74, 6.10, 16.7, 88.9, 23),
    ("GaSb", "GaSb", 0.720, 0, 1.32, "69.7, 122", 1.92, 21.6, 26.4, 27.3, 0.33),
    ("LiF", "LiF", 14.2, 0, 2.17, "6.9, 19.0", 1.05, 2.02, 33.5, 77.2, 270),
    ("MgF2", "MgF2", 12.4, 0, 2.43, "24.3, 19.0", 2.00, 1.97, 12.1, 73.7, 130),
    ("MgO", "MgO", 7.83, 0, 3.11, "24.3, 16.0", 1.97, 3.38, 46.3, 82.6, 110),
    ("NaCl", "NaCl", 8.75, 0, 1.19, "23.0, 35.5", 1.09, 2.44, 19.1, 30.6, 80),
    ("NaF", "NaF", 11.5, 0, 1.78, "23.0, 19.0", 0.98, 1.78, 29.6, 49.9, 140),
    ("PbS", "PbS", 0.29, 1, 1.41, "207, 32.1", 4.45, 15.0, 7.27, 26.9, 4.9),
    ("PbSe", "PbSe", 0.17, 1, 1.27, "207, 79.0", 4.86, 19.5, 4.86, 17.1, 2.2),
    ("ZnO", "ZnO", 3.3, 0, 4.18, "65.4, 16.0", 2.17, 6.13, 11.1, 63.4, 19),
    ("ZnS", "ZnS", 3.80, 1, 1.53, "65.4, 32.1", 2.03, 5.91, 32.8, 41.0, 14),
]
S = "arXiv:1910.10716"
for name, k, eg, star, cla, A, Z, einf, wlo, whi, Q in T1:
    L = f"Table I p.2 row '{name}'"
    add(k, "E_g", eg, "eV", S, L, "experimental gap; " + ("measured at low T ('*')" if star else "T not stated (room T)"))
    add(k, "c_LA", round(cla * 2.99792458, 4), "km/s", S, L, f"DFT, = {cla}e-5 c, angular average (App. A3 p.13)")
    if Z is not None:
        add(k, "Zstar_bar", Z, "e", S, L, "DFPT Tr Z*_+/3 of the cation(s)")
    if einf is not None:
        add(k, "eps_inf", einf, "-", S, L, "DFPT Tr eps_inf/3")
    add(k, "omega_O_min", wlo, "meV", S, L, "DFT optical-branch range, lower end")
    add(k, "omega_O_max", whi, "meV", S, L, "DFT optical-branch range, upper end (= max phonon energy)")
    if Q is not None:
        add(k, "Q_polar", Q, "1e-7", S, L, "their Eq.(27) dark-photon optical-phonon quality factor")

# Table III p.14: experimental lattice parameters (a, c) in Angstrom
T3 = {"Al2O3": (4.759, 12.991), "AlN": (3.111, 4.978), "CaF2": (5.463, None), "CaWO4": (5.243, 11.376),
      "CsI": (4.567, None), "C": (3.567, None), "GaAs": (5.653, None), "GaN": (3.189, 5.186), "GaSb": (6.118, None),
      "Ge": (5.657, None), "InSb": (6.478, None), "LiF": (4.020, None), "MgF2": (4.623, 3.052), "MgO": (4.211, None),
      "NaCl": (5.641, None), "NaF": (4.634, None), "NaI": (6.473, None), "PbS": (5.936, None), "PbSe": (6.124, None),
      "PbTe": (6.454, None), "Si": (5.431, None), "SiO2-q": (4.913, 5.405), "ZnO": (3.250, 5.207), "ZnS": (5.420, None)}
for k, (a, c) in T3.items():
    add(k, "a_exp", a, "Angstrom", S, "Table III p.14 'exp.' column")
    if c:
        add(k, "c_exp", c, "Angstrom", S, "Table III p.14 'exp.' column")

# ---------------------------------------------------------------------------------------------------------------
# 2008.08560 (Griffin, Hochberg, Inzani, Kurinsky, Lin, Yu, "SiC detectors for sub-GeV DM") Table I p.5.
S = "arXiv:2008.08560"; L = "Table I p.5"
for k, v in {"C": 3.51, "Si": 2.33}.items():
    add(k, "rho_T", v, "g/cm3", S, L)
for k in ("SiC-3C", "SiC-4H", "SiC-6H"):
    add(k, "rho_T", 3.2, "g/cm3", S, L, "'~3.2' for all polytypes")
for k, v in {"C": 22, "Si": 16.6, "SiC-3C": 22.1, "SiC-4H": 22.1, "SiC-6H": 22.1}.items():
    add(k, "omega_p_meas", v, "eV", S, L, "'hbar omega_p' row" + (" (SiC value from their Ref.[33], all polytypes)" if k.startswith("SiC") else ""))
for k, v in {"C": 3.54, "Si": 1.0, "SiC-3C": 1.95, "SiC-4H": 1.95, "SiC-6H": 1.95}.items():
    add(k, "n_e_quoted", v, "1e23/cm3", S, L, "'ne' row as printed; see checks.py U5 (inconsistent with 4 e/atom)")
for k, v in {"C": 5.47, "Si": 1.12, "SiC-3C": 2.39, "SiC-6H": 3.02, "SiC-4H": 3.26}.items():
    add(k, "E_g", v, "eV", S, L, "indirect ('All gaps are indirect', caption); T not stated")
for k, v in {"C": "~13", "Si": "3.6-3.8", "SiC-3C": "5.7-7.7 (estimated, dagger)", "SiC-6H": "6.7",
             "SiC-4H": "7.7-7.8"}.items():
    add(k, "eps_eh", v, "eV", S, L, "'Eeh' row; dagger = estimated in their text")
for k, v in {"C": "38-48", "Si": "11-22", "SiC-3C": "19 (C), 38 (Si)", "SiC-4H": "22-35"}.items():
    add(k, "E_d", v, "eV", S, L, "displacement (defect creation) energy, their Refs.[40-42]")
for k, v in {"C": 5.7, "Si": 11.7, "SiC-3C": 9.7}.items():
    add(k, "eps_0", v, "-", S, L)
add("SiC-6H", "eps_0", "9.67 (perp), 10.03 (par)", "-", S, L, "perp/par to c axis")
add("SiC-4H", "eps_0", "9.76 (perp), 10.32 (par)", "-", S, L, "perp/par to c axis")
add("SiC-3C", "eps_inf", 6.5, "-", S, L, "their Ref.[39]")
add("SiC-6H", "eps_inf", "6.6 (perp), 6.7 (par)", "-", S, L)
add("SiC-4H", "eps_inf", "6.6 (perp), 6.8 (par)", "-", S, L)
for k, v in {"C": 2220, "Si": 645, "SiC-3C": 1430, "SiC-6H": 1200, "SiC-4H": 1200}.items():
    add(k, "theta_D", v, "K", S, L)
for k, v in {"C": 148, "Si": 59, "SiC-3C": 98.7, "SiC-6H": "97.7, 98.8", "SiC-4H": "97.0, 98.8"}.items():
    add(k, "omega_T", v, "meV", S, L, "column positions read from the -layout text (6H, 4H pairs)")
for k, v in {"C": 163, "Si": 63, "SiC-3C": 120.5, "SiC-6H": "119.7, 120.3", "SiC-4H": "119.5, 120.0"}.items():
    add(k, "omega_L", v, "meV", S, L)
for k, v in {"C": 13360, "Si": 5880, "SiC-3C": 12600, "SiC-6H": 13300, "SiC-4H": 13730}.items():
    add(k, "c_avg", v / 1000, "km/s", S, L, "'cs' average phonon speed (measured)")
add("SiC-4H", "C2_evidence", "only 3C, 4H, 6H commercial; 6H most widely available in large wafers", "-", S,
    "p.2 l.122-126 and p.21 l.1668-1686", "'availability of large boules of SiC, unlike for diamond'")

# ---------------------------------------------------------------------------------------------------------------
# 1901.07569 (Kurinsky, Yu, Hochberg, Cabrera, "Diamond detectors for direct detection of sub-GeV DM") Table I p.2
S = "arXiv:1901.07569"; L = "Table I p.2"
for k, (eg, eeh, er, th, wto, wlo, cs, mfp, tau) in {
        "C": (5.47, "~13", 5.7, 2220, 141, 163, 13360, 25.6, 19.2),
        "Si": (1.12, "3.6-3.8", 11.7, 645, 59, 63, 5880, 11.4, 19.4),
        "Ge": (0.54, "3.0", 16.0, 374, None, 37, 3550, 6.9, 19.5)}.items():
    add(k, "E_g", eg, "eV", S, L, "T not stated" + ("; differs from 1910.10716 (0.67) - see IF" if k == "Ge" else ""))
    add(k, "eps_eh", eeh, "eV", S, L)
    add(k, "eps_0", er, "-", S, L, "'relative permittivity'")
    add(k, "theta_D", th, "K", S, L)
    if wto:
        add(k, "omega_T", wto, "meV", S, L, "C: 141 here vs 148 in 2008.08560 Table I" if k == "C" else "")
    add(k, "omega_L", wlo, "meV", S, L)
    add(k, "c_avg", cs / 1000, "km/s", S, L)
    add(k, "phonon_mfp", mfp, "cm", S, L, "Callaway fit, mm-scale crystal, <~30 mK, boundary-normalised")
    add(k, "phonon_lifetime", tau, "us", S, L, "tau = l/c_s, their Eq.(4) p.4")
add("C", "isotopes_radioactive", "14C", "-", S, L, "'Natural radioactive isotopes' row")
add("Si", "isotopes_radioactive", "32Si", "-", S, L, "'Natural radioactive isotopes' row")
add("Ge", "isotopes_radioactive", "76Ge", "-", S, L, "'Natural radioactive isotopes' row (2-nu double beta)")
add("C", "radio_note", "14C/C ~1e-18 from underground methane; ~10 events/kg-yr below 100 eV", "-", S,
    "p.9 l.548-562", "otherwise 14C limits diamond to gram-day exposures")
add("Ge", "isotope_scattering", "phonon lifetime in Ge limited by isotopic scattering (Tamura)", "-", S,
    "p.4-5 l.310-313", "")
add("C", "isotope_scattering", "15x 12C enrichment doubles thermal conductivity / mfp", "-", S, "p.5 l.322-323", "")
add("C", "C2_evidence", "typical CVD single crystal 4 mm x 4 mm x 0.5 mm", "-", S, "p.4 l.225-226", "")

# ---------------------------------------------------------------------------------------------------------------
# 2004.10709 (Ramanathan, Kurinsky, "Ionization yield in silicon for eV-scale ER") Table I p.5
S = "arXiv:2004.10709"; L = "Table I p.5"
add("Si", "F_eh", "0.118 (110-240 K, 5.9 keV); 0.119 (123 K, 5.9 keV); 0.128 (130 K)", "-", S, L, "")
add("Si", "eps_eh", "3.72 (5 K, 5.5 MeV alpha); 3.72 (6-70 K, 480 keV gamma); 3.749 (123 K)", "eV", S, L,
    "high-energy limit")
add("Si", "E_g_T", "1.169 (0 K); 1.164 (110 K); 1.127 (290 K)", "eV", S, L, "photoabsorption, indirect")
add("Si", "omega_pl_meas", 16.6, "eV", S, L, "EELS, 16.6 +- 0.1 eV")

# ---------------------------------------------------------------------------------------------------------------
# 2310.05815 (CRESST, "Light DM search using a diamond cryogenic detector") p.1-2
S = "arXiv:2310.05815"
add("C", "C3_evidence", "two 0.175 g CVD diamonds each with a W-TES; 16.8 eV threshold", "-", S, "p.1 l.55-58",
    "demonstrated TES on diamond at mK")

# ---------------------------------------------------------------------------------------------------------------
# 1905.13744 (Trickle, Zhang, Zurek, "Detecting light DM with magnons") p.3-4: YIG
S = "arXiv:1905.13744"
add("YIG", "spins", "20 Fe3+ per unit cell, S_j = 5/2; 12 tetrahedral vs 8 octahedral antiparallel", "-", S,
    "p.3 l.204-207")
add("YIG", "a_exp", 12.56, "Angstrom", S, "p.4 l.261", "'a ~ 12.56 A'; cell volume Omega = a^3/2")
add("YIG", "spin_density", "S_cell = 10 per a^3/2; n_s = 20/a^3 ~ (4.6 A)^-3", "-", S, "p.4 l.261")
add("YIG", "J_eff", -0.35, "meV", S, "p.4 l.263", "effective exchange, J_eff ~ -4 K")
add("YIG", "magnon_dispersion", "omega = |J_eff| S_cell (a k)^2 ~ k^2/(7 MeV) (gapless branch)", "-", S,
    "p.4 l.264", "magnon gap: GAP (not given; anisotropy neglected)")

# 2210.13516 (Esposito, Pavaskar, "Optimal antiferromagnets for light DM detection") Table I p.3
S = "arXiv:2210.13516"; L = "Table I p.3"
for k, (vt, c1, lam, rho) in {"NiO": (1.3e-4, 0.5, 0.6, 6.6), "MnO": (2.5e-5, 4.2, 0.5, 5.2),
                              "Cr2O3": (3.5e-5, 0.3, 0.9, 4.9)}.items():
    add(k, "magnon_speed", vt, "c", S, L, "v_theta (gapless AFM magnon speed)")
    add(k, "c1_spin", c1, "MeV/Angstrom", S, L, "EFT spin-density coefficient c1 (from neutron data)")
    add(k, "Lambda_UV", lam, "keV", S, L, "EFT cutoff")
    add(k, "rho_T", rho, "g/cm3", S, L, "from their Ref.[85]")
add("NiO", "magnon_gap", "'tiny gap' from small anisotropy, neglected (footnote 5)", "-", S, "p.7 l.547", "value GAP")

# 1910.02091 (Geilhufe, Kahlhoefer, Winkler, "Dirac materials for sub-MeV DM") ZrTe5
S = "arXiv:1910.02091"
add("ZrTe5", "rho_T", 6.089, "g/cm3", S, "Fig.3(d) table p.11, 'Exp. [47]'")
add("ZrTe5", "a_exp", "3.987, 14.53, 13.722", "Angstrom", S, "Fig.3(d) table p.11", "a, b, c (Cmcm)")
add("ZrTe5", "v_F", "1.3e-3, 6.5e-4, 1.6e-3 (exp [52]); 1.1e-3, 4.5e-4, 1.0e-3 (DFT, NR)", "c", S, "Table 1 p.12", "x,y,z")
add("ZrTe5", "Delta_D", "11.75 (exp [52]); 11.8 (DFT, NR)", "meV", S, "Table 1 p.12",
    "column 'Delta (meV)'; caption says 'band gaps' but p.13 l.730 uses Delta as half-gap -> see IF")
add("ZrTe5", "eps_tensor", "308.4, 20.75, 126.1 (xx, yy, zz)", "-", S, "Table 2 p.13", "DFPT; static vs inf not stated")
add("ZrTe5", "g_deg", 2, "-", S, "Table 2 p.13", "g = g_s g_C")

# 2109.04473 (Hochberg et al., "Directional detection of light DM in superconductors") p.2
S = "arXiv:2109.04473"
add("Al", "Delta_BCS", 0.3, "meV", S, "p.2 l.121", "'For aluminum (Al), with Delta = 0.3 meV and E_F = 11.7 eV'")
add("Al", "E_F", 11.7, "eV", S, "p.2 l.121")
