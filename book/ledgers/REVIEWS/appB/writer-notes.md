# Appendix B writer notes: NOTATION defects (2026-11-07)

Found while generating B.1 from NOTATION.md (figscripts/appB/gen_B1.py; full lists in figscripts/appB/gen_B1.log). NOTATION.md was
not edited. Line numbers refer to NOTATION.md as read on 2026-11-07 (it changed during the run: the Ch9 revision added rows).

## 1. Same symbol, different meanings (two or more rows)

Each pair below lists the same symbol spelling in two rows with different meanings. Some may be intended local reuse; none is
listed in the clash entries as a deliberate split as far as I could tell. Clear clashes first.

| Symbol | Row A | Row B |
|---|---|---|
| E_p | l.145 relativistic energy of momentum p (2.2) | l.305 on-site p energy in tight binding (3.2) |
| G_V | l.831 vector pair-operator coupling (10.8) | l.874 Voigt shear modulus (11.1) |
| s | l.183 spin projection (2.3) | l.1354 modulus of the complete elliptic integrals (C.8); B.2 lists this s |
| ω_p | l.361 electron plasma frequency | l.1048 phonon energy at a magnon–phonon crossing (14.2) |
| v_T | l.706 dark-matter velocity transverse to q (8.1) | l.874 transverse sound speed of a polycrystal (11.1) |
| v₀ | l.39 halo circular-speed parameter | l.416 (row with v̄; v₀ appears as the G = 0 head of the Coulomb matrix) |
| e | l.15 elementary charge | l.1345 electron Dirac field of the charged current (22.3) |
| φ | l.88 absorbed bosonic dark-matter field | l.1342 charge-density-wave row (22.3) |
| ψ | l.105 Dirac electron field | l.768 log-template row (8.8) |
| ϵ | l.335 energy E − m_e of the two-component state (3.5) | l.1274 phonon collection efficiency (19.5) |
| Φ | l.335 two-component state (3.5) | l.1088 field-line row (14.6) |
| θ_s | l.157 scattering angle (2.2) | l.1265 Lindhard–Scharff row (19.3) |
| L_e | l.245 electron-channel loss function | l.877 loss function of the extraordinary ray (11.2) |
| c_L | l.901 resonator mode quantity (11.8) | l.1265 Lindhard reduced-energy constant (19.3) |
| ω_max | l.1262 largest energy a slow ion gives one electron | l.1484 highest phonon frequency (E.9) |
| Γ_abs | l.708 absorption rate per quantum of a bosonic field | l.1317 absorption rate of the mean-field phonon solve (20.5) |
| Γ_0 | l.1283 bath row (19.6) | l.1500 barrier row (E.11) |
| T_d | l.669 tetrahedral point group | l.1072 temperature of a neutron measurement (14.4); l.1157 Lindhard row (16.6) |
| U | l.1083 molecular-magnet row (14.5) | l.1266 damage-energy row (19.3) |
| N_X | l.1180 color-center row (16.6) | l.1251 number of bound pairs at readout (18.5) |
| Ξ | l.584 deformation constant | l.1371 velocity measure domain (C.12) |
| ξ | l.135 energy mismatch (2.1) | l.1244 rate exponent (D.44) |
| ν | l.427 Lindhard reduced frequency (4.5) | l.480 phonon branch index |
| σ_ω | l.883 impulse width (11.4) | l.1155 Doppler width (16.6) |
| Θ_D | l.485 Debye temperature | l.1164 infrared-row (16.7) |
| α_M | l.1085 magnetoelectric row (14.5) | l.1489 supercell row (E.10) |
| γ_n | l.912 full width of mode n (11.8) | l.1394 neutron magnetic moment |
| ℓ₀ | l.887 anharmonic row (11.5) | l.1356 zero-point length of an oscillator (C.20) |
| ω_k, d_k | l.1403 spin–boson bath | l.1490 / l.1409 vibronic mode and chain rows |
| z_p | l.220 pole position (D.3) | l.392 complex frequency (4.1) |
| 𝗍 | l.1098 test statistic (14.6) | l.1375 likelihood statistic (C.14) |
| j_L | l.800 longitudinal current component (D.30) | l.1426 radial-solution row (E.2) |

## 2. Duplicate rows with the same meaning

The same symbol has two rows with the same meaning; one row should go (B.1 lists both, under their own first-use sections).

- M_cell (l.475, cell mass; l.1049, mass per cell)
- N_at (l.402, number of atoms; l.1414, atoms per supercell)
- V_b (l.1166; l.1500, barrier height, renamed twice)
- V_bias (l.123; l.1276, Luke gain row repeats it)
- c_k (l.732; l.884, cumulants of the self response)
- m_h (l.311; l.458, hole mass)
- E_el (l.526; l.1264, electronic energy)
- b_br, N_casc (l.1168, l.1285, l.1513), 𝗀_λ (l.1324, l.1372), ϵ_Luke (l.1274, l.1316), Δ_w (l.151, l.217), Ω_at (l.891, l.1502)

## 3. Rows lacking units

None: every kept row has a Units entry. Some are not units: "as quoted" (E_G, B_SI), "model-dependent", "as f", "as S_ab". B.1 prints
them as text.

## 4. First-use sections that do not exist

None. Every section number in every First-use cell has a label in tex/ (checked against tex/**/*.tex).

## 5. Other defects met while converting

- l.335 (Φ, ϵ): the Meaning cell contains the typography note "(\epsilon)", a LaTeX command in the table text.
- l.778 (○, tab:9-atlas): a table mark with an internal label in the Symbol cell; B.1 prints it as $\circ$ without the label.
- l.20 (ρ_crit, h): mixed first use ("ρ_crit: —; h: 1.1"); B.1 drops ρ_crit and its meaning and unit clause.
- Meanings with internal labels outside parentheses (eq:…, tab:…, "WE 8-sectors", "Table 8.1", "App. C.20 derives …",
  "cond-mat/9409105"): B.1 strips them, but they should leave NOTATION too.
- l.1477 (μ*): a pointer row for literature notation; dropped from B.1 (μ* → μ*_C is in B.2).
- Many symbol spellings in NOTATION drop bold where the tex prints bold (ψ_nk vs ψ_{n𝐤}); B.1 takes typography from the tex.

## 6. Acronyms (B.3; full list in figscripts/appB/gen_B3.log)

47 acronyms are used but never expanded in the text, among them RPA (85 uses, first 8.5), BCS (47, first 1.5), DFT (46, first 7.1),
CDMS (17), GPU (14), LF (14), FFT (12), EPW (11), CPU (8), HSE06, SOC, QED, CCD, HOMO/LUMO. Ten more are expanded only after their
first use: BSE, DFPT, HSE, PBE, LO, TO, SCF, SCHA, TDDFT, YIG. B.3 takes their expansions from a hand-edited list in gen_B3.py.
