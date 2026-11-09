"""Sect. 22.1 and the Chapter 22 opening: every number quoted from another section, with its source, and the few
derived from them. Run: python index22_1.py  (writes index22_1.log).

Sect. 22.1 computes nothing new except the worked example (we22_1.py) and the counts of Fig. 22.1 (fig22_1.py).
Every other number is quoted from the home named in the text; this script records each one with its source label
and the source script or log where one exists, so that the log holds every number printed in the section.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
out = []


def q(value, what, source):
    out.append(f"{value:<34s} | {what:<70s} | {source}")


out.append("QUOTED VALUES (value | quantity | source in the book)")
# Silicon window (Sect. 13.9, App. E.14, tab:21-dominant)
q("0.333-0.405 MeV", "phonon-assisted rate is the only Si electron-recoil channel; 0.405 = first zero-phonon edge (1s line 0.402-0.405, continuum 0.405-0.408)", "app:E.14 opening; sec:13.9, tab:13-window")
q("factor of ten", "phonon-assisted rate estimate (x/÷10)", "sec:13.9 (tab:13-window); fig13_9.py docstring")
q("350-450 core-hours", "plane-wave stages of the phonon-assisted calculation", "app:E.14, tab:E14-params")
q("0.42-0.43 MeV; 0.43-0.51 MeV", "end of phonon-assisted lead; two-channel band", "sec:13.9, tab:13-window")
q("0.3332 / 0.3374 MeV", "phonon-assisted onset (replica / free pair)", "sec:13.9; app:E.14")
q("0.3336 / 0.3378 MeV", "onsets with the TA branch scaled to neutron data", "app:E.14")
q("0.3 meV; 8.5e-5 MeV", "grid tolerance of omega_TA(Q*); onset shift 2*dw/vmax^2", "app:E.14 (recomputed below)")
q("a few tens of core-hours", "direct DFPT verification of omega_TA(Q*)", "app:E.14 (three core-hours per wavevector)")
q("0.3 to 2.6", "screening correction relative to the optical calibration", "app:E.14; tab:13-nuisances")
q("x20 at 1.20 eV", "two cold Si absorption datasets differ", "sec:13.9-open")
q("x9 at 0.36 MeV; factor 3", "cold data choice on the rate; finite-q form factor", "tab:21-dominant")
q("25 meV", "cold-edge measurement window above threshold", "sec:13.9-open")
q("20 K", "measured absorption edge for the optical-limit control", "app:E.14 (Macfarlane et al.)")
# Silicon zero-phonon rate (Ch10, tab:21-dominant)
q("x1.28; 3.6-10 MeV", "electron-hole attraction on the heavy-mediator rate", "tab:21-dominant")
q("1.48 at 3 MeV", "one-standard-deviation factor of the Si rate", "sec:10.10 (nuis10_10.py); figscripts/ch21/we21_4.log x1.482")
q("about 10 %", "coupling block dropped (Tamm-Dancoff)", "tab:10-nuisances")
q("39 %; 93 %", "variance share of the factor 1.48: attraction alone; attraction + tabulation spread", "sec:10.10 (beta 0.247, 0.289, 0.078, 0.064); derived below")
q("1.48 -> 1.11", "band at 3 MeV after BSE and a converged IP table", "sec:21.4 (s21-4)")
q("x3.2 at 1 MeV; x1.34 at 3 MeV", "independent-particle tabulation spread", "tab:21-dominant")
q("x1.24 at 10 MeV (above 2 q0)", "local fields at large q", "tab:21-dominant")
q("at least 16; at least 29", "velocity coupling vs static-electron formula (IP; density row screened), 10 MeV", "sec:10.4 (s10-4 l.72)")
q("1.1-1.2 vs 0.93 at 0.3-0.7 q0", "f-sum of the published IP tables at small q", "tab:10-nuisances")
q("10 keV", "range of the all-electron local-field calculation", "sec:10.10-open")
q("near 30 MeV; 0.07 vs 0.69", "Ge 3d/valence with crystal final states (bound)", "tab:21-dominant")
q("-0.76 %", "relativistic f-sum shift of Ge", "sec:10.6; Summary of Ch10")
# Germanium window
q("0.2119-0.2141 MeV", "Ge phonon-assisted onset from measured TA data", "sec:13.9; tab:13-window")
q("0.1 eV; 0.744 eV; 6^3", "band-order check; Ge L gap; phonon grid", "app:E.14")
q("0.775 eV; 0.823 eV", "hybrid functional (no SOC): Gamma-Gamma and Gamma-L gaps of Ge",
  "Abdurrazaq et al., arXiv:2512.08857, Fig. 1(a) and its text (sources/22.1/2512.08857.txt)")
q("order not restored with SOC", "hybrid (HSE06) with spin-orbit coupling: Gamma 0.64-0.69 eV below L 0.79-0.83 eV", "compute result DC-2 (state/DC-RESULTS.md); agrees with 2512.08857")
q("about 24 %; 39 %", "4s-orbital shift fitted to both Ge gaps: m_t(L) heavy, m_Gamma heavy", "compute result DC-2-alpha (state/DC-RESULTS.md); app:E.14")
q("0.89 eV; 0.0815 m_e (0.010); 0.038 m_e (0.005)", "Ge direct gap; L transverse mass and Gamma mass with check tolerances", "app:E.14 (revised)")
q("0.32 MeV", "Ge zero-phonon edge, on-axis parabolic estimate (orients, does not bound)", "sec:13.1")
# Migdal
q("0.75 keV to 2 q_BZ", "unsized coherent region of the Si Migdal response", "tab:12-nuisances; tab:17-nuisances")
q("nearly all up to 1 MeV; 33 % at 2 MeV; 7 % at 3 MeV", "share of the Si Migdal rate in that region",
  "tab:12-nuisances (figscripts/ch12/migdal_rates12.log)")
q("14.9", "diagonal form over the boost limit as q -> 0", "tab:12-nuisances; eq:8.3-boostward")
q("1.2-1.4", "off-diagonal local fields, model, lower end not bounded", "sec:12.3-validity; offdiag12.log")
q("x1.35", "diagonal local fields", "lim:12.3a")
q("14 m_e (exact, trace rule, Q = 0)", "trace value of the drag mass per Si atom, eq:12.5-trace", "sec:12.5-trace")
q("18.6 m_e (12-24 m_e); 28.7 m_e; 5.60e-4", "on-site valence drag mass (bound); on-site total; delta M_II/M", "sec:12.5; tab:12-nuisances")
q("few parts in 1e4", "delta M/M from 2.73e-4 (trace) to 5.60e-4 (on-site)", "sec:12.5")
q("1.6, 0.54, 0.25 at 20, 50, 100 eV", "absolute bound of the Wannier picture", "tab:12-nuisances")
q("0.315; 0.498", "largest P(first) of the Migdal row: survivors (NaF), full pool (NaCl)", "sec:21.7; guide21_7.log")
q("5.7e5", "pole vs gap-weighted Migdal figure of merit, Si", "sec:17.5; Ch17 Summary")
# Recoil charge and cascade
q("352 eV; 399 eV", "binary thresholds Si, Ge", "eq:19.2-Eth; yield19_2.log")
q("0.10 at 100 eV; (25 +- 3) % at 254 eV", "measured NR charge yields Si, Ge", "sec:19.2 (2303.02196 Table II; 2405.10405)")
q("15; 35", "Born parameter Z alpha/v_F of the close collision (v_F Fermi velocity) Si, Ge", "sec:19.2")
q("117 to over 1000", "Born parameter Z_1 alpha/v of the recoiling ion (v its speed), Si", "sec:19.3")
q("0.097 in [0.030, 0.173] at 5 eV", "two-pair fraction, full-band cascade", "sec:18.3-fullband")
q("0.114; 0.119", "F_eh of the calibrated model; measured Si", "sec:18.4")
q("4.15 eV [3.95, 4.73]; >= +-0.4 eV", "eps_eh of the full-band cascade without a fitted constant; class systematic", "sec:18.4; tab:18-nuisances")
q("3.749 eV; 2.96 eV (77 K)", "measured pair energies Si, Ge", "sec:18.4; sec:21.7")
q("0.83; 0.21", "P(GaSb beats Ge); conventional width outside validated range", "sec:21.7; guide21_7.log")
q("0.54 % (0.32-0.77 %)", "capture fraction that closes the Si Fano gap", "sec:18.5 (s18-5); tab:18-nuisances")
# Readout
q("0.81-1.02; 1.128", "mean-field collection ratio; ratio needed by collection alone", "sec:20.5; sec:19.5")
q("about 5 %", "required accuracy of tunneling exponent and E_reorg/eps_hop", "sec:19.6-open")
# Lattice, spin, SC, Dirac
q("20 keV; +-0.2 %", "few-phonon range; anharmonic kinetic-energy bound", "sec:11.5; tab:11-nuisances")
q("quarter of a percent above 100 meV at 30 MeV", "Si lattice rate accuracy (nucleon coupling)", "sec:11.9-open")
q("at most 3 %; -19 %", "GaAs acoustic charge; GaAs scalar rate core term (parametric)", "tab:11-nuisances")
q("7.8 %", "NiO one-magnon weight high", "sec:14.1")
q("1.25e4; 0.39", "free-electron alpha^2F_tr excess below 1 meV; lambda_tr from resistivity", "sec:15.4")
q("1.33; above 1.5", "edge multiple and Sommerfeld factor, ZrTe5", "tab:16-nuisances; sec:16.1")
q("factor 2.8", "ZrTe5 reach band from the background tensor", "we:16-band")
# Rows added in the revision (open calculations of Ch11, 14, 15, 16)
q("5.0e3 at 50 meV; 65 meV", "isotope over electromagnetic B-L absorption (lower limit); top of cold two-phonon gap in data", "sec:11.6; eq:11.6-Tbound")
q("293 K", "temperature of the measured Si absorption that bounds the cold value", "sec:11.6 (fig:11-iso)")
q("0.5; about 0.04; 30^3-40^3", "two-magnon interaction 1/2|S| in NiO; weight moved in energy; wavevector grid", "sec:14.2")
q("q g33 = 0.034 at 1 keV", "optical-activity scale in quartz", "sec:14.5")
q("0.52; 0.39", "(1 + lambda_tr)^-2 in Al; lambda_tr", "sec:15.4-strong")
q("2 %", "partial f-sum per molecule, acceptance test of the molecular-crystal BSE", "app:E.21")
q("0.28; 0.44", "alpha_ohm of the measured Al-covered resonators (acceptance test)", "app:E.22")
# Published limits
q("1/r; 1.7 at 56.5 keV", "fermionic absorption, free-electron vertex low (Xe 1s)", "sec:10.9-open")
q("1e-4; <=1e-4; R^(-1/2)", "boosted heavy mediator: density-row and transverse corrections; limit scaling",
  "compute result for the published CRDM treatment (liang2025plasmon), quotable wording")
q("< 1 % for m >= 10 keV; ~3 keV; 0.05-0.93 at 1 keV", "boosted light mediator: shift; undetermined below; ratio range",
  "same source, quotable wording")

out.append("")
out.append("DERIVED")
vmax = 2.650e-3
dw = 0.3e-3   # eV
out.append(f"onset shift 2*dw/vmax^2 = {2*dw/vmax**2/1e6:.2e} MeV for dw = 0.3 meV (vmax = {vmax})")
out.append(f"envelope ratio of the two-pair fraction 0.173/0.030 = {0.173/0.030:.2f} ('almost six')")
b = [0.247, 0.289, 0.078, 0.064]
tot = sum(x * x for x in b)
out.append(f"variance shares of the 1.48 band: attraction {b[0]**2/tot:.3f}, attraction+tabulation {(b[0]**2+b[1]**2)/tot:.3f}")
out.append(f"largest deposit of m_chi = 0.333 MeV: m v_max^2/2 = {0.333e6*vmax**2/2:.3f} eV")
out.append("channel counts of Fig. 22.1: see fig22_1.log")
out.append("worked-example numbers: see we22_1.log")

with open(os.path.join(HERE, "index22_1.log"), "w") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out[-6:]))
