# Ch12 derivation review, part 1 (12.1–12.3, D.33)

Reviewer: derivation verifier (isolated). Date 2026-11-02. Files: tex/ch12/ch12.tex, s12-1.tex, s12-2.tex, s12-3.tex, tex/appD/D-33.tex.
Sources fetched to sources/review-ch12/d1/ (PDFs deleted, text kept): 2011.09496 (KKL), 1707.07258 (Ibe), 2210.06490 and 2603.13052 (Berghaus),
2205.03395, 2011.13352, 1912.13484 (Liang), 2208.12222 (Cox), 2604.26773 (Kahlhoefer). NIST He I from sources/12.2.
Scripts (scratchpad, not in the book): r9.py (sympy, bracket), r9num.py (rate with the corrected bracket, reuses limit12_3b/mig12 data),
nums.py (independent re-integration of the Si tables), misc.py (sympy: H atom, CM separation). No QE run.
Verdicts: CHECKED = redone and agrees; WRONG = error, correction given; GAP = missing step/statement or wording that misleads.

## PRIORITY R9: 12.3 free-recoil bracket: CONFIRMED (WRONG in 12.3)

- Independent derivation (r9.py, sympy). Free nucleus, kick q, electrons take p, nucleus leaves with q − p, a = p²/2M, b = q·p/M.
  Ordering 1 (kick first): denominator ω_e + (q−p)²/2M − q²/2M = ω_e − b + a. Ordering 2 (Coulomb first): −(ω_e + a).
  Sum = b/[(ω_e − b + a)(ω_e + a)] exactly (sympy: difference 0). Numerator is q·p/M, the soft-limit numerator, with no p²/M.
- The book's eq:12.3-bracket, 1/(ω_e − y) − 1/ω_e with y = (q−p)·p/M = b − 2a, keeps the −p²/M of y but drops the +a in both
  denominators. The two are not separable orders: the dropped a's cancel the −2a of the numerator exactly. "Recoil energy below
  1e-2 of ω_e" is true but irrelevant; a must be compared with y, not with ω_e.
- Angle averages (sympy series in 1/M), normalized to v_N²p²/(3ω_e⁴):
  book form: 1 + 3p²/q² + (9/5)v_N²p²/ω_e² − 6p²/(Mω_e) + …  (the displayed equation of 12.3 l.99 is algebraically right for the book form);
  exact:     1 + (9/5)v_N²p²/ω_e² − 2p²/(Mω_e) + (5/2)p⁴/(M²ω_e²) + …   No p²/q² term. The 9/5 term stands.
- Sources: Liang et al. 2011.13352 Eq. (1) keeps the recoil k²/2m_N in BOTH denominators (exact form above). KKL 2011.09496 Eq. (3)
  as printed is [1/(ω − q_N·(k+K)/m_N) − 1/ω] with q_N the FINAL ion momentum, i.e. the book's bracket, omitting k²/2m_N in both
  denominators; KKL use it in the soft limit, where the omission is harmless. The error is the book's use of it beyond the soft
  limit. The book cites both as "the exact energy denominators" (l.92); only Liang Eq. (1) is.
- Numerical (r9num.py: limit12_3b machinery, same tables, same kinematics, bracket replaced): soft/exact =
  1.0011 (3 MeV), 1.0010 (5), 1.0008 (12), 1.0008 (16.5), 1.0006 (50), 0.9994 (150 MeV). Book bracket reproduces the log
  (0.275, 0.499, 0.844, 0.911, 0.991, 1.000). osc12_4.log check 2 agrees (free exact/lead = 0.99944; book bracket/lead 25.4 at q = 2 keV).
- Artefacts to remove (all O(p/q)):
  - s12-3 l.3 "it holds down to about 16 MeV, below which the electrons take a sizable part of the nuclear momentum".
  - l.92 "The soft limit fails first. Its parameter is p/q …" and l.101 "The first, 3p²/q², is the soft limit proper … falls short by 1.2 at 12 MeV and 2 at 5 MeV".
  - l.94–99: eq:12.3-bracket and the averaged display; replace by b/[(ω_e−b+a)(ω_e+a)] (align with eq:12.4-corr) and the exact average above.
  - lim:12.3b: solid curve, gray band "≥ 0.89 E_onset (m_χ ≥ 16.5 MeV)", box sentence "Below about 16 MeV …", and l.113/l.115
    ("the soft limit fails before the lattice does"; "above 16 MeV"). Rebuilt result: within the free recoil the soft limit holds to
    ≤ 1.1×10⁻³ for 3–150 MeV; the high-mass correction (9/5)v_N²p²/ω_e² (0.04/0.13/0.42 at 100/300/1000 eV, CHECKED) is what remains.
    limit12_3b.py l.52 must use the exact form (and its docstring l.10–12 claim "relative size < 1e-2" is the same error).
  - s12-1 l.87 "sec:12.3, sec:12.4 write out the exact denominators for a free … nucleus": point to the corrected 12.3 form.
  - D-33 l.64 "together with the exact energy denominator for a free recoil that sec:12.3 derives": KKL Eq. (3) is not exact; say
    their bracket drops p²/2M in both denominators, which is consistent only in the soft limit.
- Content of the rebuilt lim:12.3b: on the present mass axis the ratio is flat (≤ 1.1e-3), so the box has nothing to show there.
  What controls the soft limit is the Doppler term (9/5)v_N²p²/ω_e² at large E_R (0.13 at 300 eV, 0.42 at 1 keV). Near 1 keV
  v_Np = 1.6 eV at the median p exceeds the gap, the exact bracket's pole ω_e − b + a = 0 lies inside the integration range, and the
  expansion fails; plot soft/exact against E_R (or m_χ up to 1 GeV) and state the breakdown there, or stop below it.
- Consequence for KKL's soft-limit condition k ≪ q_N: not needed by the amplitude; it enters only through the lattice factor frame and
  kinematics (R12 nuisance row).

## R13 (12.6 sum rule, bremsstrahlung, scalar absorption)
Out of the files under review (12.6 is in derivation-2's brief, which carries the same R13 line). Not verified here.

## Known items (editor-notes) concerning these files
- R1, WRONG premise (substantive). Limit 12.3a does NOT measure the G ≠ G′ elements: its caption says "The elements G ≠ G′ are in
  neither curve". The 1.35 is scalar ε (head inverted as a number) vs the diagonal of the inverted full matrix, i.e. local fields on the
  diagonal. The off-diagonal terms of eq:12.3-FL (the E.18 vs Berghaus dispute) remain unsized; KKL (2011.09496, main text) say only
  "do not contribute more than an O(1) amount", Berghaus 2210.06490 call off-diagonal ELF elements "small". The R1 book wording
  "≈35 % effect … concentrated at p ≳ q_BZ, \cref{lim:12.3a}" must not be attached to G ≠ G′. Correct form: "local fields lower the
  diagonal-form probability by 1.35 (lim:12.3a); the G ≠ G′ terms of eq:12.3-FL are not computed (App. E.18)". Editor to re-rule.
- R2 (energy axis): fig12_2 caption still per E_ej; fig12_3 already on ω_e (8.15 eV added). Pending reviser. Not a derivation error.
- R5: s12-2 l.143 still "where the binding is smaller still" (Ge 4.15 meV pending).
- R6: superseded by R9 (the box is rebuilt). The <10⁻⁵ bound-nucleus statement is CHECKED (limit12_3b.log: max 8.1e-6, 3–111 MeV).
- R7: s12-1 l.78 has the model label; the cross-reference to the full 12.3 number (6.1e-3 at E_R = 100 eV) is not yet there.
- R8: the value 5e-3 is not used in 12.1–12.3 or D.33. CHECKED. 12.3's 6.1e-3 at 100 eV scales to 6.1e-2 at 1 keV, consistent.
- R10: no 2210.06490 misattribution in these files (only Eqs. (3.6), (3.8), both verified in 2210.06490). CHECKED.
- R11: 5.6 keV is labelled by its model in 12.1 (fig12_1.log 5.57 keV). CHECKED.
- R15: s12-1 l.138 "both corrections below 10⁻³" still unrestricted. Numbers CHECKED: P_Mig = 6.1e-5 × E_R/eV → 10⁻³ at 16.4 eV, 3.05 % at 500 eV.
- 12.2-writer cross-check (12.3 vs 12.2): atom 2.09e-3 at 1 keV ↔ 2.09e-4 at 100 eV (fig12_3.log 2.088e-4): consistent. CHECKED.

## Campaign returns (CORRECTIONS.md, SOTA.md)
- Boost mass m_A (CORRECTIONS §6 row "boost mass"): used. CHECKED. P_Mig ≤ E_R(δM/M)/E_g (CW2.14): 12.1's estimate is consistent
  (Si 100 eV: bound 0.025 ≥ 6.1e-3). 1BZ domain of KKL Eq. (6) (CORRECTIONS §20 row WP8-errata §15): the book states it (12.3 l.68). CHECKED.
- (1 − P_Mig)S with M + δM (SOTA B3): s12-1 l.138. CHECKED. No superseded campaign value found in these files.

## 12.1 The joint electron–lattice response
- l.3 E_R = 47.8 meV, 2W = 1.57, e^{−2W} = 0.21, "two in a million": CHECKED (fig12_1.log 47.78 meV, 1.571, 0.208, 1.864e-6).
- eq:12.1-joint, -marginal, positivity (with D-33 l.7–11): CHECKED (delta-function product; contraction is a sum of |·|²).
- eq:12.1-sectors / D-33 l.13: GAP (minor). l.9 puts "any change of the zero-point energy" in ω_l, while E^el_f is the zero-phonon
  energy, which already contains the ZPE change; D-33 l.13 then needs E_f − E_i = E^el_f for P_0. Delete "and any change of the
  zero-point energy" or define E^el_f as the vertical-plus-relaxation energy without ZPE. As written the P_0 line would sit at ω_l = ΔZPE.
- eq:12.1-force (with D-33 l.17–22): CHECKED (v(r) = ∫e^{−ip·r}v(p), n_e(p) = Σe^{ip·r}, p → −p with even v; gradient −ip).
- eq:12.1-amp: CHECKED. Sign: −i q·d/(MΔE), d = −F/ΔE, q·F = −i∫(q·p)v n e^{−ip·X}: i·(−i) = 1; phase e^{i(q−p)·X}. Dimensionless.
- eq:12.1-Skk: CHECKED. Normalization (2π/V)(V/2π)²V⁻²·V = 1/2π (D-33 l.48); units eV = S(q,ω) per energy; G/G′ ordering matches |A|².
- l.72–76 estimate: CHECKED. δM/M = 14 m_e/M = 2.735e-4; (0.0478/6)(2.735e-4) = 2.2e-6; ratio 6/0.0478 = 125 ("120").
- l.78, fig:12-plane: CHECKED against fig12_1.log (1.86e-6, 4.44 eV, 88.9 %, 5.93 eV, 21.1 %, 48.37 meV, 5.57 keV). ⟨p²⟩/2M = 0.60 meV CHECKED.
- l.87: v_Np/ω_e = 2.4e-3, (ω_l/ω_e)² = 1.2e-4. CHECKED ("2e-3, 1e-4"). See R9 for the pointer to 12.3.
- WE 12-oscillator: ℓ_0 = (M_Si·ω_0)^{−1/2} = 0.0482 Å, q = 1/ℓ_0 = 41.1 keV, E_R = ω_0: CHECKED. Poisson(1) 0.368/0.368/0.184/0.061,
  Poisson(3) via |iqℓ_0 − √S|² = 3, S ω_0 = 0.128 eV, 1.234 eV, 0.12 eV split, 12 % excess (3.939/3.508): CHECKED. All exact/Condon/
  non-Condon fractions, 3.94/3.52/4.00e-6, 0.153/0.148 eV, 1.199 eV: CHECKED (we12_1.py rerun, 2 s; N = 140 and 200 identical).
  GAP (l.98): "3ω_0 = 0.192 eV" then "1.0463 + 0.188 = 1.234 on the computed surfaces": 0.188 is the Condon excited-surface mean
  (we12_1.log (a) 0.1884), not 3ω_0. Say "0.188 eV on the computed surfaces (quanta 63.4 and 65.5 meV)".
- l.107 and tab:12-truncations. Ibe Eqs. (55)–(58), KKL Eqs. (3), (6), Liang 2205.03395 Eqs. (3.1)–(3.4) (propagator
  i/[(ε_i−ε_j)² − ω²], reduction (3.2)): CHECKED. Berghaus Eq. (3.8): GAP. Eq. (3.8) keeps the off-diagonal ELF elements
  Im[−ε⁻¹_KQ] and sets Q ≃ K only in the lattice factor; the diagonal ELF is their numerical choice (their Sect. 5, "we drop the
  off-diagonal terms … in Eq. (3.8)"). Table cell "diagonal in the loss function" and l.107/l.129 "the three crystal formulas drop
  the off-diagonal elements" should say "diagonal in the lattice factor; ELF diagonal in the evaluation".
- l.129 "local fields change the Si electron-recoil rate by 1.5 at 10 MeV": CHECKED (s10-2 l.38: 8.6e4/5.9e4 = 1.46).
- l.133–138 zeroth and first moments: CHECKED (eq:12.1-zeroth from the f-sum split; prescription = SOTA B3). R15 pending.
- l.150 metal ∫dω ω·ω⁻⁴ divergence: CHECKED.

## 12.2 The atomic limit
- eq:12.2-mA/-Hint: CHECKED (sympy chain-rule Jacobian, misc.py: R block 1/m_A, no R–ρ cross terms, ρ diagonal 1/m_e + 1/M,
  off-diagonal 1/M ⇒ mass polarization −M⁻¹Σ_{e<e′}∇·∇).
- eq:12.2-cm: CHECKED (X = R_cm − (m_e/m_A)Σρ). eq:12.2-joint dims (eV): CHECKED.
- l.35 sources: Ibe Eqs. (55), (57) (phase e^{−i q_e·Σx}), (73) q_e = m_e v_F ≃ (m_e/m_A)q_A; Kahlhoefer Eq. (1) phase e^{+i q_e·Σr}: CHECKED.
- l.37 2N_e m_e/m_A = 5.47e-4 (Si), 4.83e-4 (Ge): CHECKED.
- eq:12.2-rate: CHECKED (v_min = q/2μ_χN + ω_e/q from ω = q²/2m_A + ω_e; per-mass prefactor). ½m_χv²_max = 35 eV / 3.5 keV
  (v_max = 794.5 km/s): CHECKED.
- l.48 q_e = 88 eV, ξ_D = 0.068 (4p, 2.90 a_0) and 0.017 (3d): CHECKED ("0.07", "0.02").
- l.53 H: q_e²⟨z²⟩ = q_e²a_0²; limit-box correction 1 − (5/8)ξ_D²: CHECKED (sympy).
- eq:12.2-sums: CHECKED. Double commutator N_e/m_e + N_e²/M = N_e m_A/(m_e M); × q_e²/2 with q_e = m_e q/m_A gives (N_e m_e/M)E_R
  with E_R = q²/2m_A. 0.27/0.24/0.23 eV: CHECKED (0.2735, 0.2417, 0.2256).
- eq:12.2-shell, eq:12.2-dipole dims: CHECKED. Ibe Eqs. (86)–(90): CHECKED.
- lim:12.2a numbers (0.127, 0.188, 14.4/9.2 GeV, endpoints 0.027/0.011, < 7 % below 0.1): CHECKED (limit12_2a.log).
  WRONG (minor), l.81 "offset of 2 to 3 %": a/a_dip = 0.9845 (Si), 0.9776 (Ge) → 1.5 and 2.2 %. Write "about 2 %".
  Cox Sect. II C (dipole valid for v ≪ αZ_n; corrections (v/αZ_n)²): CHECKED.
- fig:12-atoms and l.83 (Cox values from the paper's public ancillary tables via fig12_2.py; the paper prints no per-shell total to compare): Si 2.09e-3, cores 7.95e-4, Ge 1.63e-3 / 1.73e-3, Xe 1.98e-3, 0.5 % (3d 0.44, 3p 0.13), 13 % (4p), 6 %: CHECKED (fig12_2.log, we12_2.log).
- WE 12-germanium: m_A = 67.654 GeV, q = 11.63 MeV, v_A = 1.72e-4 = 51.5 km/s, q_e = 87.9 eV, 0.024, 0.0296, m_χ ≥ 2.27 GeV (own
  root-find 2.268): CHECKED. Shell values vs Ibe Table II (Ge: 3d 2.8e-2, 4p 2.6e-2, E_3d = 35 eV, 4s→4p 4.0e-2): CHECKED.
  1/580, 9.3e-4, 2.59e-3, 1.18e-3, 4.3e-3, 1/230, 8.18 eV, 7.28 + 0.63, 96.8 %, 0.242 eV, 124 eV, 135 eV: CHECKED.
  GAP, l.97 "Since only one event in 580 ionizes, such an event carries 124 eV": 0.242 eV × 580 = 140 eV. The 124 eV is the
  ionization part of the tabulated moment (7.28 eV × 0.0296 / 1.73e-3). Say so; the exact 0.242 eV includes bound transitions.
- l.106–112 core shells in a crystal: q = 92.5 keV/164 meV (Si), 113 keV/94 meV (Ge), x_R^{−1/2} = 4.9e-3, pull-back 3.3e-6 and
  8.3e-7, ΔEτ 2.7e-4 and 6.7e-4, radii 0.28/0.39/1.48 Å: CHECKED.
  WRONG (minor), l.110 Si 2p "99.6 eV": s3-5 l.101 gives 99.4 (2p_{3/2}) and 99.8 (2p_{1/2}), centroid 99.5. Use 99.4 or "99.5 (centroid)".
- eq:12.2-exc, eq:12.2-bound: CHECKED (f = 2m_eΔE|D|²; ΔE < I for lines, > I for continuum).
- He numbers: f = 0.27625 and 0.07346 at 21.218/23.087 eV (NIST tsv); 13.606·f/ΔE = 0.1771, +0.0433 = 0.2204, all 0.263, 84 %;
  v_A/α = 0.0100 at 10 eV, P = 2.65e-5 ("2.7e-5"), 52.2 MeV: CHECKED. Kahlhoefer Eq. (6): CHECKED.
- H shares 0.565 / 0.717 / 0.555 / 0.644 (sympy: |z|²_2p = 2¹⁵/3¹⁰ = 0.5549, |z|²_3p = 0.0890): CHECKED. lim:12.2b 0.239, 1/5 at ξ = 1
  (0.144/0.717 = 0.20), ξ ≤ 0.154 → 4 %: CHECKED.
- l.143 Ge 8.75e-2 vs 5.86e-2: CHECKED.

## 12.3 Crystals at large momentum
- l.3: q = 1.57 MeV, E_R = 47.1 eV, q/q_BZ = 698, E_R/⟨ω⟩ = 1150, "thirty times": CHECKED. "holds down to about 16 MeV": WRONG (R9).
- eq:12.3-See: CHECKED (S = (2π/V)Σ|n|²δ = 2(−Im χ), L = v_C(−Im χ), v_C = e²/p²).
- unnumbered combination l.27 and eq:12.3-soft: CHECKED ((1/2π)·2·Z²e²(v_N·p)²L/(ω⁴p²) per 2πn_κ → e²/π = 4α). Dims eV⁻¹.
  KKL Eq. (6) and "valid only for k in the first BZ" (text after Eq. (6)): CHECKED.
- l.23 Z_ion: 4.20 (2.4 keV), 4.40 (3.4 keV), 4.84, 6.78: CHECKED (mig12 core form factor, PBE free atom).
- l.46: q = 2.287 MeV, v_N = 8.74e-5 = 26.2 km/s; own re-integration of the KKL-LF table: P = 6.11e-3 (script 6.07e-3), median 4.56 eV,
  88.7 % below 10 eV, mean 5.94 eV; point ion 3.89e-3, ratio 1.572; median p 5.68 keV = 2.52 q_BZ; 96.8 % above q_BZ; plasmon 4.3 %;
  3.9e-5/eV ↔ fig12_1 1.864e-6/47.78 meV: CHECKED. KKL "1.6 for Si" with momentum-dependent charges (Sect. D text near Fig. 7): CHECKED.
  KKL plasmon cut at 2.5 keV is in Fig. 6 (main text) and App. C: CHECKED.
- WE 12-fsum: CHECKED (fifth moment ↔ f-sum gives c = e²/π). n_e = 2.00e23 cm⁻³, ω_p^val = 16.60 eV, 0.94/0.93/0.92/0.90/0.62/0.17,
  2.3 % above 10 keV (own 2.26 %), tail bound 1.6 % (own 1.61 %): CHECKED.
- lim:12.3a: 1.3 q_BZ = 2.93 keV, 8 % (0.078), 1.24 at 2q_BZ, 1.35 at 3q_BZ, total 1.35 (8.194/6.068), peak 2.96 q_BZ: CHECKED. See R1.
- eq:12.3-FL: CHECKED. Off-diagonal normalization redone: dP/dω = (4αv²/3ω⁴)Z²Σ_GG′∫_BZ d³k/(2π)³ cos θ_GG′ Im[−ε̃⁻¹], so
  L_Mig = Z²𝓕_L/Ω. Liang 2011.13352 Eqs. (11)–(13) (prefactor 2A²σZ²αN_T/(3μ²Ωm_N²), symmetrized ε̃): CHECKED; lim:12.3b formula matches Eq. (11).
- l.88 "Knapen … at most a factor of order one": CHECKED against KKL ("do not contribute more than an O(1) amount").
- l.90 KKL cut 4ω̄ → 9ω̄ (App. C), 0.16 eV at onset, < 10⁻⁵ bound vs free: CHECKED.
- l.92–115: WRONG (R9). The 9/5 term and its values 0.04/0.13/0.42, E_R^max(1 GeV) = 496 eV, ≈ 20 % at 0.5 keV: CHECKED.
- l.117 Si 2p atom 7.1e-5 = 1.17 % of 6.07e-3: CHECKED.
- l.121, fig:12-crystal-atom: 2.09e-4, 1.29e-4, 29.1, 46.9; 3p 1.2e-4, 3s 1.0e-5, cores 7.95e-5: CHECKED (fig12_3.log).
- l.130: 84 % between gap and 8.15 eV (own 83.4 %), ×5.9 at 10 eV, ×64 at 20 eV ("sixty"), q_e = 44.7 eV, 3–9 keV: CHECKED.
- eq:12.3-rate: CHECKED (dE_R = q dq/M; v_min; prefactor 2αρσ_N/(3m_χμ²M³)). Dims eV⁻¹.
- l.144 ∫dq q³η = 4μ⁴⟨v³⟩ (∫u³Θ(v−u) = v⁴/4): CHECKED. ⟨v³⟩^{1/3} = 400.5 km/s: CHECKED.
- eq:12.3-permass: CHECKED (per nucleus the rate is A-independent: A²/M_κ² = 1/m_u²; per unit mass ΣN_κ/(A_cell m_u)).
- l.149 local exponents 1.01 / 1.24 / 2.07: the numbers are CHECKED, but WRONG attribution. They are the exponents of the coupling
  factor μ_χN⁴/(m_χμ_χn²) (analytic: 1.014 at 7 MeV, 1.24 at 141 MeV, 2.08 at 4.2 GeV), not of "the computed silicon rate": with the
  q ≥ 92.5 keV cut the computed rate vanishes below ≈ 17 MeV, and limit12_3c.log gives 7.67 between 20 and 40 MeV. Replace
  "The computed silicon rate has the local exponents" by "This factor has the local exponents".
- l.149 Ni factor 25–81, f-sum bound (π/2)ω_p²/E_g⁵: CHECKED.
- lim:12.3c: 66 MeV, 1.25 at 30 MeV, 1.85 at 20 MeV: CHECKED. l.164 rates 1.9/30/970 kg⁻¹yr⁻¹ (1.879, 29.6, 968): CHECKED.
  KKL ρ = 0.4 GeV/cm³, v_esc = 500 km/s (factor 4/3): CHECKED.
- eq:12.3-HW, -AW, -AWbound: CHECKED (Σ∇_iV = −i[H,P] = m_e[H,[H,R]]; ⟨c|F|v′⟩ = m_e(ε_c−ε_v′)²r_cv′; weight bound |(1±x)²−1| ≤ 2x + x²).
  Bound values 1.56/0.54/0.25 ("1.6"): CHECKED. Acoustic-sum-rule ordering and the factor ½ of the Hermitian ordering (⟨c|P̂_I = 0): CHECKED.
  lim:12.3d: 0.025, 0.38, 0.76, 1.5e-15 ("2e-15"), 2.5e-16 ("3e-16"): CHECKED. Liang 1912.13484 Eqs. (2.7), (2.8) (boost on struck site only)
  and 2011.13352 Fig. 4 (loss-function rate above Wannier near the gap): CHECKED.
- l.170 amplitude reduces to the dipole boost "up to a phase": CHECKED.

## Appendix D.33
- D.33-labels: CHECKED (see 12.1; ZPE GAP applies to l.13).
- D.33-F and the amplitude A_fj: CHECKED (sign, phase, Condon step). Atom frame l.36: CHECKED (phase cancellation e^{ip·X}).
- D.33-square: CHECKED (normalization 1/2π; crystal-momentum reduction; units).
- eq:D.33-diag, eq:D.33-4alpha: CHECKED ((2π)⁻¹·Z²e⁴p⁻⁴·2p²e⁻² = Z²e²/(πp²), e²/π = 4α). l.64: WRONG pointer (R9).
- D.33-atom: CHECKED (d_j0 = m_eΔE⟨Σr⟩ from F = −m_eΔE²⟨Σr⟩; amplitude −i m_e v_N·⟨Σr⟩; Ibe Eq. (58)).
- eq:D.33-virtual: CHECKED. The (1/N)Σ_Q is the site-diagonal phonon Green function (kick and force on the same nucleus), leading
  term by completeness; correction (64.1 meV/1.17 eV)² = 3.0e-3, probability 1.006. Berghaus Eq. (3.6) ∇H_χL·∇H_eL/(m_Nω²) and the
  lattice factor at q − k_e − K: CHECKED. Liang Eqs. (3.1)–(3.4): CHECKED.

## NOTATION drift
- H_int (12.2 internal Hamiltonian) clashes with NOTATION rows "H′, H_int: dark-matter–target interaction" (2.1) and the 4.7
  interaction part. Rename (e.g. H_rel or H^int with a row).
- s_κ(Q, ω) (D.33, fig:12-plane caption "s") clashes with s_κ(q) = nuclear spin density (NOTATION row 677). Rename or decorate.
- 𝓕_L (eq:12.3-FL) vs F_L = static Lindhard function (NOTATION 429): different glyph but same letter and subscript; no row for 𝓕_L.
  Suggest 𝓕_loss or 𝓕_Mig and add a row.
- Bare bold F (eq:12.3-HW, total force on the electrons) vs NOTATION 899 "bare F is not used"; F^I_j0 (force matrix element) and
  F_exc, F_ion (12.2 oscillator-strength sums) have no rows.
- D_q̂ (12.2 dipole operator) vs D, δD = kick operator (11.4, NOTATION 873). Decorated, but add a row or rename.
- No rows: L_Mig, P̂^W_I, A^W_cv, W_v (W is the Debye–Waller exponent), P_exc, P_ion, F_exc. R_cm, 𝛒 are marked "6.1 only" but reused in 12.2 with m_A.
- No factor-2, π or sign drift found in the Fourier, f-sum, FDT (S = 2L/v_C) or loss-function conventions; e² = 4πα throughout.

## Summary of corrections (by priority)
1. R9 confirmed: replace eq:12.3-bracket by the exact b/[(ω_e−b+a)(ω_e+a)]; delete the 3p²/q² term, the 16.5 MeV boundary, 0.495 at
   5 MeV and the "soft limit fails first" narrative (12.3 l.3, 92–115, lim:12.3b; 12.1 l.87; D-33 l.64); fix limit12_3b.py l.52.
   Corrected soft/exact ratio is 1.000–1.001 at 3–150 MeV.
2. R1 conflates local fields on the diagonal (lim:12.3a, ×1.35) with the G ≠ G′ terms (unsized). Editor to re-rule the wording.
3. 12.3 l.149 exponent attribution; 12.1 Berghaus "diagonal" attribution; 12.1/D-33 ZPE labelling; WE-germanium 124 eV logic.
4. Minor numbers: 12.2 l.81 "2 to 3 %" → about 2 %; 12.2 l.110 Si 2p 99.6 → 99.4 (or 99.5 centroid); WE 12-oscillator 0.188 eV source.
5. NOTATION rows/renames as listed.
