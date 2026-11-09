"""Full-text values added by WP8-U-TOP. Locators: arXiv = PDF page of the pdftotext extract in
literature/papers-WP8-U-TOP/ (extracts kept, PDFs deleted); Europe PMC = JATS full-text XML (PMCID, table/section).
Row: (material, property, value, unit, source, locator, note). Tag is [FT] for every row here.
Sources not on arXiv (tag [FT], full text read via Europe PMC):
  DS09  = Del Sordo et al., Sensors 9, 3491 (2009), doi:10.3390/s90503491, PMC3297127
  WBG24 = Wide-Bandgap Semiconductors for Radiation Detection: A Review, Materials 17, 1147 (2024), doi:10.3390/ma17051147, PMC10934017
  GAN20 = Vertical GaN-on-GaN Schottky Diodes as alpha-Particle Radiation Sensors, Micromachines 11, 519 (2020), doi:10.3390/mi11050519, PMC7281217
  CZT23 = Advances in High-Energy-Resolution CdZnTe Linear Array Pixel Detectors..., Sensors 23, 2167 (2023), doi:10.3390/s23042167, PMC9960822
  SEL26 = SELUN photon-counting detector, J. Synchrotron Rad. (2026), doi:10.1107/s1600577525009026, PMC12809242
  BV25  = Optimal Selection ... Wide-Bandgap Semiconductor for Betavoltaic Battery, Nanomaterials 15, 635 (2025), doi:10.3390/nano15090635, PMC12073746
"""
DS09 = "Del Sordo 2009 Sensors 9:3491 (PMC3297127)"
WBG24 = "Materials 17:1147 (2024) (PMC10934017)"
GAN20 = "Micromachines 11:519 (2020) (PMC7281217)"
CZT23 = "Sensors 23:2167 (2023) (PMC9960822)"
SEL26 = "J Synchrotron Rad 2026 SELUN (PMC12809242)"
BV25 = "Nanomaterials 15:635 (2025) (PMC12073746)"
T1DS = 'Table 1 "Physical properties of the principal compound semiconductors at T = 25 C", row "Pair creation energy (eV)"'

ROWS = [
 # ---------------- eps_eh (pair-creation energy) ----------------
 ("Si", "eps_eh", 3.62, "eV", DS09, T1DS, "25 C; compilation value"),
 ("Si", "eps_eh", 3.62, "eV", "arXiv:2311.03902", "Table 1 p.2 (col. eps_i,Si used for comparison)", "reference value used by the SiC comparison method, 25 C"),
 ("Ge", "eps_eh", 2.96, "eV", DS09, T1DS, "table header says 25 C, but Ge spectrometers are operated at ~77 K; read as the 77 K value [C]"),
 ("Ge", "eps_eh", 3.37, "eV", "arXiv:1602.08005", "p.12 Sec. 2.1.4", "50 mK; '(3.37+-0.01) eV' fit of EDELWEISS Ep/EQ vs bias; model-dependent (Luke-phonon efficiency 0.85 free)"),
 ("Ge", "eps_eh", "3.32 (+0.84 -0.97)", "eV", "arXiv:1602.08005", "p.11 Sec. 2.1.3", "50 mK, from CDMSlite resolution + Fano model; method-limited"),
 ("Ge", "eps_eh", "~3", "eV", "arXiv:1602.08005", "p.9 Sec. 2.1.1", "77 K: 'eps is almost a constant, ~3 eV [14-19]'"),
 ("Ge", "F_eh", 0.13, "-", "arXiv:1602.08005", "p.9 Sec. 2.1.1", "77 K, 'F = 0.13 [17]' (Klein review); secondary quote"),
 ("Ge", "F_eh", "0.14 (+0.02 -0.03)", "-", "arXiv:1602.08005", "p.11 Sec. 2.1.3", "50 mK, model-dependent inference, not a direct measurement"),
 ("C", "eps_eh", "13.1 +- 0.2", "eV", "arXiv:2311.05011", "PDF p.30 (final section)", "alpha particles, refs 53,54; room T"),
 ("C", "eps_eh", "13.25 +- 0.50", "eV", "arXiv:2311.05011", "PDF p.30", "continuous X-ray beam, ref 55"),
 ("C", "eps_eh", "13.05 +- 0.20", "eV", "arXiv:2311.05011", "PDF p.30", "continuous X-ray beam, ref 56"),
 ("C", "eps_eh", "12.82 +- 0.13", "eV", "arXiv:2311.05011", "PDF p.30", "transmission X-ray detector, ref 57"),
 ("C", "eps_eh", 13, "eV", GAN20, 'Table 1 row "e-h pair creation (eV)"', "compilation"),
 ("SiC-3C", "eps_eh", 6.90, "eV", "arXiv:2610.16949", "Table II PDF p.23", "Expt. column, Makarov 1975 refs [22,23]; electrons"),
 ("SiC-4H", "eps_eh", "7.83 +- 0.02", "eV", "arXiv:2311.03902", "Table 1 p.2; abstract", "alpha 4.2-5.6 MeV, comparison to Si (3.62 eV), 25 C (p.4 'All measurements were performed at room temperature (25 C)')"),
 ("SiC-4H", "eps_eh", "7.82 +- 0.02", "eV", "arXiv:2311.03902", "Table 1 p.2", "2013, alpha, charge injection (Garcia et al., = arXiv:1308.2886), 23 C"),
 ("SiC-4H", "eps_eh", "7.28 / 7.6 / 7.71 / 7.78 / 7.79 / 7.8 / 8.6 / 5.05", "eV", "arXiv:2311.03902", "Table 1 p.2", "earlier literature 2003-2013; 5.05 (DC e-beam current, 2006) is an outlier; 7.6 from 241Am X-rays"),
 ("SiC-4H", "deps_eh_dT", "-0.27 over 23->500 C", "eV", "arXiv:1308.2886", "p.10", "'measured decrease in eps over the same temperature range is nearly twice as large [as Eg], about 0.27 eV'"),
 ("SiC-4H", "F_eh", 0.100, "-", "arXiv:2311.03902", "Table 2 p.2", "X-rays, 'Calculated from linewidth' (Bertuccio 2011); room T"),
 ("SiC-4H", "F_eh", "<= 0.04", "-", "arXiv:2311.03902", "Table 2 p.2", "X-rays, upper limit from linewidth (Phlips 2005); in tension with 0.100"),
 ("SiC-4H", "F_eh", 0.128, "-", "arXiv:2311.03902", "Table 2 p.2", "Klein model, not a measurement"),
 ("GaAs", "eps_eh", 4.2, "eV", DS09, T1DS, "25 C"),
 ("GaAs", "eps_eh", 4.2, "eV", WBG24, 'Table 1 row "e-h pair creation energy (eV)"', "compilation"),
 ("GaAs", "eps_eh", 4.3, "eV", GAN20, 'Table 1 row "e-h pair creation (eV)"', "compilation; spread 4.2-4.3"),
 ("GaN", "eps_eh", 8.9, "eV", WBG24, 'Table 1 row "e-h pair creation energy (eV)"', "compilation (ref. Sellin & Vaitkus 2006 per 2610.16949 Fig. 6 caption)"),
 ("GaN", "eps_eh", 8.9, "eV", GAN20, 'Table 1 row "e-h pair creation (eV)"', "compilation"),
 ("AlN", "eps_eh_calc", 12.2, "eV", "arXiv:2610.16949", "Table II PDF p.23", "first-principles DFT+full-band MC (theory), Expt. column is '-': no measurement"),
 ("AlN", "eps_eh_empirical", 14.4, "eV", BV25, "Table 2 footnote *", "'estimated based on the relation (2.15Eg+1.23)'; not a measurement"),
 ("SiO2-a", "eps_eh", 18.0, "eV", "arXiv:2610.16949", "Table II PDF p.23-24; text p.24", "Ausman & McLean 1975 (amorphous SiO2 films, recombination-model fit); one sample 16.4 eV"),
 ("CdTe", "eps_eh", 4.43, "eV", DS09, T1DS, "25 C"),
 ("CdTe", "eps_eh", 4.43, "eV", WBG24, "Table 1", "compilation"),
 ("CZT", "eps_eh", 4.6, "eV", DS09, T1DS, "Cd0.9Zn0.1Te, 25 C"),
 ("CZT", "eps_eh", 4.46, "eV", CZT23, "Table 1 caption", "+20 C; cited to Cornet et al. 1970"),
 ("CZT", "F_eh", 0.1, "-", CZT23, "Table 1 caption; Sec. 3", "'Fano factor of 0.1 [33]', ref 33 = Redus et al. 1997 'Fano factor determination for CZT'"),
 ("CZT", "F_eh", 0.089, "-", SEL26, "footnote 5", "assumed value (with eps 4.5 eV) for the CZT sensor; not a measurement"),
 ("HgI2", "eps_eh", 4.2, "eV", DS09, T1DS, "25 C"),
 ("TlBr", "eps_eh", 6.5, "eV", DS09, T1DS, "25 C"),
 ("ALL-SEMI", "F_eh_range", "0.06-0.14", "-", DS09, "Sec. 2 after Eq. (5)", "'In semiconductors, the Fano factor F is much smaller than unity (0.06-0.14) [14]'"),
 # ---------------- empirical eps_eh(E_g) laws (used for [E] brackets) ----------------
 ("ALL", "eps_eh_law_Klein", "(14/5)Eg + 0.5", "eV", "arXiv:2610.16949", "PDF p.4 Sec. II", "Klein 1968"),
 ("ALL", "eps_eh_law_wide", "1.54Eg + 1.89", "eV", "arXiv:2610.16949", "PDF p.4 Sec. II", "recent fit dominated by wide-gap data"),
 # ---------------- displacement energies ----------------
 ("Si", "E_d", 13, "eV", GAN20, 'Table 1 row "Displacement Energy, E d (eV)"', "compilation"),
 ("GaAs", "E_d", 10, "eV", GAN20, "Table 1", "compilation"),
 ("SiC-4H", "E_d", "C 20, Si 35", "eV", GAN20, "Table 1", "compilation, per sublattice"),
 ("GaN", "E_d", "Ga 45, N 109", "eV", GAN20, "Table 1", "compilation, per sublattice"),
 ("C", "E_d", 35, "eV", GAN20, "Table 1", "compilation; 2008.08560 Table I gives 38-48 (R13 row)"),
 # ---------------- dielectric / phonon (GaAs, sapphire) ----------------
 ("GaAs", "eps_0", 12.9, "-", "arXiv:1807.10291", "Table I p.11", "fills R13 GAP:eps_0"),
 ("GaAs", "eps_inf", 10.89, "-", "arXiv:1807.10291", "Table I p.11", ""),
 ("Al2O3", "eps_0_par", 11.5, "-", "arXiv:1807.10291", "Table I p.11", "parallel to c"),
 ("Al2O3", "eps_0_perp", 9.3, "-", "arXiv:1807.10291", "Table I p.11", "perpendicular to c"),
 ("Al2O3", "eps_inf", 3.2, "-", "arXiv:1807.10291", "Table I p.11", ""),
 ("Al2O3", "omega_TO_LO_o", "TO 633.6/569/439.1/385; LO 906.6/629.5/481.7/387.6", "cm-1", "arXiv:1807.10291", "Table II p.31", "ordinary ray, error < 0.5 %"),
 ("Al2O3", "omega_TO_LO_e", "TO 582.4/397.5; LO 881.1/510.9", "cm-1", "arXiv:1807.10291", "Table II p.31", "extraordinary ray"),
 # ---------------- cosmogenic 3H ----------------
 ("Si", "cosmo_3H_rate", 124, "atoms/kg/day", "arXiv:2506.06568", "p.1", "sea level, 'roughly 124 atoms/kg/day'"),
 ("Si", "cosmo_3H_bg_per_day", 0.002, "/(kg keV day) per day exposure", "arXiv:2506.06568", "p.1", "0-5 keV"),
 ("Ge", "cosmo_3H_rate", "75 +- 26", "atoms/kg/day", "arXiv:1706.05818", "Table 1 p.12", "natGe, calculated; measured 82 +- 21 and 76 +- 6 (Table 2 p.14)"),
 ("NaI", "cosmo_3H_rate", "83 +- 27", "atoms/kg/day", "arXiv:1706.05818", "Table 1 caption p.12", "Na + I"),
 ("Ge", "cosmo_3H_sat_bg", 7.2, "/(kg keV day)", "arXiv:1706.05818", "p.20", "saturation, 1-7 keV raw rate (NaI 7.9)"),
 ("NaI", "cosmo_3H_sat_bg", 7.9, "/(kg keV day)", "arXiv:1706.05818", "p.20", "saturation, 1-7 keV"),
 ("ALL", "3H_decay", "T1/2 12.3 y, beta endpoint 18.6 keV", "-", "arXiv:2506.06568", "p.1", ""),
 # ---------------- magnets ----------------
 ("YIG", "omega_max_mag", "~90 (predicted); modes observed to nearly 100", "meV", "arXiv:1705.06594", "p.2", "INS full magnon spectrum"),
 ("YIG", "Delta_mag_optical", "~30", "meV", "arXiv:1705.06594", "p.2", "zone-centre gap between the acoustic ('ferromagnetic') and first optical magnon"),
 ("YIG", "Delta_mag", "gapless acoustic branch (Kittel: tunable by B0)", "-", "arXiv:1705.06594", "p.2", "no zero-field gap resolved (energy resolution 5.4 meV at the elastic line, methods p.5)"),
 ("YIG", "J_ex", "J1 6.8(2), J2 0.52(4), J3a 0.0(1), J3b 1.1(3), J4 -0.07(2), J5 0.47(8), J6 -0.09(5)", "meV", "arXiv:1705.06594", "Table p.3", "fit to INS"),
 ("NiO", "Delta_mag", "1.15 (mode B), 1.29 (mode A); further modes < 0.5", "THz", "arXiv:1806.07968", "pp.3-4 (Fig. 5 caption)", "low-T AFMR; 1 THz = 4.136 meV"),
 ("MnO", "Delta_mag", 0.82, "THz", "arXiv:2609.20122", "p.1", "high-frequency AFMR branch at low T; low branch 'in the microwave regime'"),
 ("Cr2O3", "Delta_mag", 0.696, "meV", "arXiv:2010.08926", "p.2", "zone-centre magnon energy"),
 # ---------------- many-atom oxides ----------------
 ("Li2MoO4", "rho_T", 3.04, "g/cm3", "arXiv:1704.01758", "p.22", "'lower density (3.04 g/cm3 vs. 4.18 g/cm3)'; fills R13 GAP"),
 # ---------------- source-defect resolutions ----------------
 ("ALL", "c_LA_def_1910", "average of omega_LA/q over a 20x20 grid on a sphere |q| ~ 10 eV", "-", "arXiv:1910.10716", "p.13 App. A3", "phonopy frozen-phonon (p.13 App. A2)"),
]
