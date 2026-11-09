# Ch16 part 1 derivation check (ch16.tex, s16-1, s16-2, s16-3, appD/D-41)
Reviewer: isolated derivation verifier, 2026-11-06. Sources fetched with lit.py into sources/review-ch16/ (1708.08929, 1910.02091,
2110.01587; PDFs deleted, text/HTML kept); already on disk and read: sources/16.2 (2312.00866, 2607.15338, 2507.07164, 2110.01587),
sources/16.3 (1606.08849, 1706.02487, 0709.1163, 2208.05967, rii_*.yml). Not read: Pines 1956 (closed), hechster2017 (closed).
Independent scratch checks (scratchpad, not in the repo): stack.py (sympy, layered stack), par.py (parabolic channel, demon),
n162.py (16.2 numbers), opw.py (independent OPW/PW graphene rate), halo_test.py (ZrTe₅ published-rule normalization vs halo).
Cached logs re-read: we16_1, limit16_1a, zrte5_16, fig16_1, kern16_2, fig16_2, limit16_2a–c, we16_2, limit16_3a–b, nt16_3, qd16_3,
we16_3. No QE, nothing heavy. State checked: CORRECTIONS, SOTA, DC-RESULTS, returns/R18/DC-49 and REF-DC-49-54-36 §2, §4.
Verdict summary: 2 WRONG (scope/wording), 7 GAP, all PRIORITY derivations CHECKED; one recommendation (graphene v_D).

## PRIORITY items (editor notes 16.1–16.3, partII notes)
P1. D.41 / eq:16.1-ratio, ε_bg² (scattering) and ε_bg (absorption): CHECKED.
  L_pub = Im ε_D/|1+ε_D/ε_bg|² = ε_bg² Im ε_D/|ε_bg+ε_D|² and Γ_pub = ζ²m(Im ε_D/ε_bg)ε_bg²/|ε|² = ε_bg Γ are identities (sympy; also
  limit16_1a.log: ratio 1.000000 of ε_bg², absorption deviation 7e-16). Source side verified in full text:
  1708.08929 v2 Eq. (2.5) α̃ = αg/(κv_F) (includes g; the book's α̃ excludes g_deg, NOTATION row 647, so g_degα̃ = 0.91 ✓),
  Eq. (2.6)/(2.7) ε_r = 1 + (e²g/24π²κv)[…] (charge e²/κ in the loop), footnote 5 (e₀² = 4πα/κ at the cutoff), Eq. (3.7) |M|² ∝ 1/|ε_r|²,
  Eq. (3.11) F_med = 1/ε_r with vacuum σ̄_e, Eqs. (4.4)–(4.5) ε_eff² = ε²m⁴/|m²−Π|², R ∝ ε_eff² Im ε_r, Eq. (A.8) ε_r with 1/κ;
  1910.02091 Eqs. (2.2)–(2.7), (2.24)–(2.28), (3.8)–(3.14) the same construction. Eq. (3.13) prefactor 288π⁴κ²v²/(e⁴g²) =
  ½(6πκv/gα)² ✓ (e⁴ = 16π²α²); Λ′ = Λexp(12π²κv/ge²) = Λexp(3π/(g_deg α̃)) ✓ (eq:D.41-lprime). RPA chain of the "Dirac-only mediator"
  (D.41 l.43): R_DD = R⁰/ε_pub, Im(R⁰ε*_pub) = Im R⁰ ✓. Absorption D.41-abs: ζ_eff² = ζ²/|ε|², −Im Π/ω = m Im ε ✓.
  Reach shifts eq:D.41-reach (σ ∝ 1/N, ζ ∝ N^{-1/2}) ✓. Matches SOTA (REFEREED, WP4-v3) and CORRECTIONS l.390 ("never also ×0.55–0.62";
  D.41 last paragraph says exactly this) ✓.
P2. Lower bound (α/v_max)² = 7.6 (s16-1 l.35): CHECKED. v_max = (544+250.5)/c = 2.6502e-3; α/v_max = 2.754, square 7.582.
  Premise v_D < v_max is the source's own kinematic statement (1708.08929 Eq. (3.15)–(3.16)), and holds with a gap too (ω ≥ v_D q).
  For an anisotropic cone read v_D as the smallest v_i and ε_bg as ε_bg,ii (add "isotropic" or "along a principal axis": GAP-minor).
P3. Reversed design rule (s16-1 l.37): CHECKED. d/dx[x/((x+a)²+b²)] = 0 ⇔ x² = a²+b², so the published absorption peaks at
  ε_bg = |ε_D| = |4.532+6.081i| = 7.584 ✓ (50 meV, limit16_1a.log). Total-ε rates fall monotonically for ε_bg + Re ε_D > 0, which holds
  everywhere in the model (Re ε_D > 0 inside the cutoff for |s| < 4v²Λ²); published scattering rises monotonically for Re ε_D > 0 ✓.
  Source: 1708.08929 Sect. 4.2 "optimal κ/g is O(10) for v_F = 1e-4" ✓. (Their Fig. 5 is at m_A′ = 10, 100 eV, above 2v_FΛ = 0.04 eV;
  "a maximum of this kind underlies" is fair as worded; do not strengthen it.)
P4. ZrTe₅ ×4800–6600 (s16-1 l.64): CHECKED as the book's own calculation, with a flag. zrte5_16.log: 4814 (20.7 keV) to 6562; independent
  rerun with the same tables 4715–6562 (book halo). REF-DC-49-54-36 §4 item 5 (the only quotable wording, DC-RESULTS) gives "×(4–6)×10³ (th.)
  … accuracy about ±10–15 % from unstated inputs" over 30 keV–1 MeV; the book's upper end 6600 lies 10 % above it. The factor itself depends
  on the halo: halo_test.py gives 4190–6100 (v0 220, v_esc 544, v_E 232), 4900–6160 (220/600/232), 5170–6420 (230/600/240).
  → Keep 4800–6600 but label it "with the book's halo", and add "(the compute referee's (4–6)×10³ with the source's inferred halo)" or
  round to "about 5×10³ to 6.6×10³". The harmonic-mean 2550, and the isotropic-model overstatement 2.3–2.7 (iso/aniso reach 0.37–0.44) ✓.
P5. 0.63–0.72 recomputation gap (fig:16-zrte5 caption): CHECKED, cause is mostly the halo. With ρ = 6.135, Λ̃ = min Λ_iv_i = 0.180 eV
  (1910.02091 Eq. (2.21) ✓) and the hard-cutoff bracket (their Eq. (3.10) with μ̃ = 2e^{−5/6}Λ̃ is ln(4Λ̃²/|q̃²|), = book bracket ✓), the
  ratio is 0.635–0.736 (book halo), 0.80–1.11 (v0 = 220, v_esc = 600, v_E = 232), 0.81–1.71 (220/544/232). DC-49 reached 0.90–1.06 with an
  inferred halo (v_esc = 600) and common density; 1910.02091 states no halo constants (DC-49 §10 item 6). → Caption: "it lies at
  0.63–0.72 of the published curve above 20 keV, a difference of halo: the source states none, and with v0 = 220, v_E = 232,
  v_esc = 600 km/s the ratio is 0.8–1.1." The absorption check (1.0050–1.0054, halo-free) is the clean input test ✓.
P6. eq:16.2-inplane and eq:16.2-corr: CHECKED exactly (stack.py, sympy). Solving ε_j(ψ″−k²ψ) = −1 with ψ, εψ′ continuous gives the book's
  C_A, C_B identically, and the period average of k²ψ equals eq:16.2-inplane identically (zero difference; numeric spot check 1e-16).
  Series in k with d_A = fa_s: k⁰ term = 1/ε_⊥, k¹ term = 0, k² coefficient / [f²(1−f)²(ε_A−ε_B)²/(12ε_∥ε_⊥²)] = 1 ✓.
  EMT form = 2110.01587 Eq. (16) at any filling (identity, sympy) ✓; the algebra ε_⊥[(1−f)ε_A+fε_B] = ε_Aε_B + f(1−f)(ε_A−ε_B)² ✓.
P7. The "real constant" vs 2110.01587 Eq. (19): CHECKED, and explained. Eq. (19) (HTML): R = [2 − kd coth(kd/2) + ε(2ε−4−kd)]/
  [kε(coth(kd/2)+ε)]. One-layer limit of the book (ε_B = 1, d_B → ∞) = d(1/ε−1) − 2(ε−1)²t/[kε(εt+1)] (sympy ✓), and
  R = −[book] − d_A exactly. Origin: Lasenby–Prabhu normalize R so that a bulk slab gives R = −d/ε (their text, k ∥ x̂), i.e. R integrates
  −1/ε over the layer without subtracting the vacuum value 1 that the layer displaces; the book's a_s(ε⁻¹−1) is the change from vacuum.
  The constant is real and ω-independent, so Im R is unchanged. → Add one clause: "the constant is the vacuum term −d_A, which their R,
  normalized to −d/ε for a bulk slab, does not subtract." Line at ε_A = −coth(kd/2), Drude ω² = ω_p²kd/(2+kd) ≈ ω_p²kd/2 = eq:16.2-2Dpl with
  n_2D = n_ed ✓.
P8. Nanotube ×4 / ×2.1 (s16-2 l.72): CHECKED. 2607.15338 Eqs. (3)–(4): S_1D = g|q|δ(ω−v|q|), one right- and one left-mover, benchmarks
  g = 0.2–0.7, v_F ≃ 0.8e6 m/s; no channel factor anywhere in Eq. (6). Their g, v with g₂ = g₄ = v_C reduce to g_c(N=1), v/g_c ✓.
  Four-channel charge mode: g_c = [1+8α ln(…)/πv]^{-1/2} (the Kane–Balents–Fisher form) ✓; S_1D weight Ng_c, first moment Nvq² ✓.
  At fixed g_c the rate is ×4 low ✓; at fixed kernel 4g_c(4)/g_c(1) = 2.15 (q = 10 eV) ✓ "2.1" (2.09 at 1 eV, 2.35 at 100 eV: say "2.1 at
  10 eV, 2.1–2.4 over 1–100 eV" if a range is wanted). Matches SOTA (R×2: "2607.15338 single-channel, CNT rate ×4").
P9. Graphene OPW ×1.44 / ×1.84 (s16-3 l.45): CHECKED by an independent code (opw.py: own momentum-space normalization, own radial
  form factor F = ⟨j₀⟩ − 2P₂⟨j₂⟩, own angular grids; only η(v_min) shared). Heavy: PW 7.16e3 / OPW 1.02e4 (10 MeV), 2.89e3 / 5.26e3
  (100 MeV), ratios 1.43, 1.83; light: 1.14, 1.18. Book: 6.9e3/1.0e4, 2.8e3/5.2e3, 1.44, 1.84, 1.14, 1.19. Agreement 1–4 % (my coarser
  E_B histogram and E-grid). K_PW = 6.014e-10, K_OPW = 2.128e-17 eV⁻³ at q = 1 eV, E = 50 eV reproduced to 4 digits; M_OPW = O(q) ✓.
  Rate prefactor σm_ep/(16π³μ²) and the 1/4π of eq:16.3-rate re-derived ✓. E_B: mean 4.409 eV, range 0–8.4 ✓.
P10. Hard-wall dots 0.70–1.03 and −9π/(8kR): the formula is CHECKED (Dirichlet Weyl N = Vk³/6π² − Sk²/16π; (S/V)(6π²/16πk) = 9π/(8kR);
  log: χ < 10 gives 46 levels vs Weyl+surface 45.7). The range is WRONG in scope, see W1.
P11. Blanco Eq. (6) too large by μ/(4ω): CHECKED. Re-derived eq:16.3-qdrate from the golden rule: (ρ_χσ/4πm_χρ_Tμ²)∫q dq ηF²S̄ with
  S̄ = (2π/Ω)⟨|f_QD|²⟩ gives ωρ_χσ/(2m_χM_cellμ²) ✓. Printed (6): N_tρ_χσ̄/(8m_χμ); with N_t per mass = 1/M_cell the ratio is μ/(4ω) =
  486.16 keV/12 eV = 4.05e4 ✓. Bulk limit 2π⟨|f_QD|²⟩ = 4παm_e²|f_crys|²/q³ reproduces Essig's crystal rate ✓. Their Eq. (12) (HTML
  numbering) sets |f_QD|² = (2π²/E_rαm_e²V_cell)Σ∫…E_rδ(…) = the dimensionless |f_crys|², so (6)+(12) has mass dimension 2 ✓ (qd16_3.log).
  Eq. (11) misprint: with 0.283d³, d = 3.3 nm gives 0.51 eV; with 0.283d, 1.24 eV ≈ the quoted 1.2 eV ✓ (the text avoids it ✓).
P12. Hochberg et al. Eq. (7) state count: ruling: the count is twice the physical one as printed. Eq. (7): R = 2Σ_i(ρ_χ/m_χ)N_C A_uc
  ∫d²ℓ/(2π)² …, "N_C ≃ 5×10²⁵ kg⁻¹ is the density of carbon atoms", "factor of two … degenerate spin states". A_uc∫_BZ d²ℓ/(2π)² = 1, so
  each band holds 2N_C electrons per kg, but a band of a two-atom cell holds 2·(N_C/2) = N_C. The rate is right only if each Ψ_π(ℓ)
  integrates to 1/2; Eq. (1) is a four-site cluster with an unstated N_ℓ, and a unit-normalized Eq. (1) carries weight 1. The book's own
  model uses N_π = 1/m_C (eject16_3.py l.49), so no book number inherits it. → s16-3 l.27 GAP: add after "per band": "which counts each
  band twice unless Ψ_π carries weight ½ (N_ℓ is not given there)"; an author query at most, not a claim of error.
P13. PbS-in-silica depolarization 6.00 (we:16-depol): CHECKED. Zemel formula at 3.5 µm: ε = 17.627; Malitson: 1.9765 (2.276 at 5 eV, 2.139
  at 2.5 eV); 9·17.63²/21.584² = 6.005; field ratio 0.275, 1/ε 0.0567; ε_in = 10 → 4.62, 25 → 6.71, 1+i → 0.566, 3+3i → 2.45 ✓. MG to first
  order, Im(−1/ε_eff) = 9φ Im ε_in/|ε_in+2ε_out|² and the criterion (2ε_in+ε_out)(ε_in−ε_out) > 0 for real ε_in ✓. Blanco Eq. (16) and
  "dielectric function obtained from Ref. [139]" (Hechster–Sarusi, a model) ✓.
P14. Graphene v_D 3.41e-3 (16.2) vs 3.02e-3 (16.3): RECOMMEND 3.02e-3 (t = 2.8 eV, Castro Neto et al., text after Eqs. (5), (7):
  v_F = 3ta/2, "≃ 1×10⁶ m/s"). Reasons: (i) 16.3 already needs t = 2.8 eV for the π-band binding energies (0–8.4 eV, mean 4.41) of the
  same model, so 3.41e-3 would make 16.3 inconsistent with itself; (ii) γ₀ = 3.16 eV of 2312.00866 is the SWMcC bilayer-graphite fit,
  appropriate inside Das et al.'s bilayer model (keep it there, "as quoted"), not as the book's graphene velocity; (iii) the nanotube
  numbers of 16.2 and 16.3 must share one velocity. Zhang–Chen's 0.8e6 m/s = 2.67e-3 is a third value; say so where 2607.15338 is used.
  Changes in 16.2 with 3.02e-3 (n162.py): N_chv_C/πv_D 31, 7 → 35, 8; g_c 0.18, 0.22, 0.36 → 0.17, 0.21, 0.34; plasmon 7.3, 5.7, 3.6 →
  6.9, 5.4, 3.4 v_max ("four to seven" → "three to seven"); 0.225/0.419 → 0.212/0.398 (ratio 2.13, unchanged); subband pairs
  2v_D/r_t 1.9 → 1.7 eV; graphene interband edge 30 eV/0.30 eV → 32 eV/0.30 eV; rerun limit16_2a (g_c range, 10 % point), fig16_2,
  map16 caption; drop the Table 16.1 clause.

## WRONG
W1. lim:16.3b box text (s16-3 l.113) "the dot carries 0.70 to 1.03 of the scissored bulk response over the PbS range". limit16_3b.log
  computes 0.702–0.965 (qR = 3) and 0.763–1.026 (qR = 8) over x = 3–11.14 only, i.e. 3.6–10 eV. The PbS range starts at x = 1.65
  (2.5 eV), where the qR = 8 cumulative ratio is 65.6 (x = 1.65) and 2.42 (x = 1.99); and the PbS range has qR ≥ 7.5, so the qR = 3 curve
  does not apply there. → "Between 3 and 11 confinement energies above the gap (3.6 to 10 eV for these dots) the dot carries 0.76 to 1.03
  of the scissored bulk response at qR = 8 (0.70 to 0.97 at qR = 3); nearer the gap the discrete levels dominate the cumulative ratio."
  The text paragraph (l.116, "15 to 30 % below … between 3 and 11 confinement energies") is consistent with this ✓.
W2. Notation: eq:16.2-inplane defines t_j = tanh(kd_j/2); NOTATION reserves t_j for the single-defect strength (11.6), and s16-3 uses t for
  the hopping (2.8 eV). → τ_j or θ_j (local), or write tanh in full. Also ε_pub (new, s16-1, D.41) has no NOTATION row (editor note
  asked for it), and B (the Dirac bracket of eq:7.3-eps, s16-1 l.7, D.41 l.18) collides with the B of NOTATION row 856 (bulk modulus,
  "bare B is never …"); s (Dirac invariant) is "local to D.22 and 7.3" in NOTATION row 657 but is used in 16.1, 16.3 and D.41: widen the scope.

## GAP
G1. we:16-factor (s16-1 l.57): the recomputed published-form reach at 100 keV is 2.8e-45 cm², the published gapped curve at 100 keV reads
  5.0e-45 (data/pub_h_gapped.csv), a factor 1.8 that the reader will notice beside "3.4e-46 read from the figure". REF-DC-49-54-36 §4 item 9
  (quotable as a footnote at most): the ideal curves of 1708.08929 lie 1.75–2 in rate below its own formula (source ρ_χ = 0.4 vs the book's
  0.3 widens it). → footnote: "the published curve lies about a factor 2 above its own formula (book halo: 1.8 at 100 keV)". The ×1600
  shift of the read minimum, 3.37e-46 → 5.39e-43, is correct either way.
G2. s16-1 l.64, Δ_D = 15.6 meV (ISIF7 row, bold in 1910.02091 Table 1, and the text below it: gap 31.2 ↔ Δ 15.6 ✓). CORRECTIONS row 458
  (v4 row 1543) and SOTA l.621 favour 11.8 meV (NR) for the campaign's ZrTe₅ row, an open coordinator conflict. Not superseded for the
  book's purpose (the reproduction must use the implemented row), but say "the implemented (ISIF7) row; the experimental-structure row has
  Δ = 11.8 meV" so the two do not look like a clash with Ch7/App. E.
G3. s16-1 l.35 lower bound: state that it is for an isotropic cone (or per principal axis with ε_bg,ii and v_i), see P2.
G4. s16-3 l.38: "the more diffuse Slater orbital of app:E.21" has exponent 1.568/a₀ (eject16_3.py BETA_ALT), which is the Clementi–Raimondi
  2p exponent for carbon; Slater's rules give 1.625/a₀. Both orbitals have the Slater form r e^{−ζr}cos θ, so "Slater" does not separate them.
  → "the Clementi–Raimondi exponent 1.568/a₀ (more diffuse)" with a citation, or Slater's 1.625/a₀ and rerun the 0.4–4.3 range.
G5. we:16-demon "ordinary sheet plasmon at 191.5 meV" is the √q term only; with the ¾v_F,l²q² term of eq:16.2-2Dpl it is 193 meV.
  → "at 191.5 meV to leading order". All other WE 16.2 numbers ✓ (below).
G6. s16-1 l.17 / D.41 l.3 cite eq:D.22-gapless and the bracket of eq:7.3-eps; the hard-cutoff vs MS-bar reading (+5/3) is stated in the WE
  ✓, but D.41-lprime uses the hard-cutoff bracket while 1708.08929 Eq. (3.13) uses the e^{−5/6}-redefined Λ. The identity (prefactor
  carries ε_bg²) is scheme independent; add "in either scheme" after "an identity" (D.41 l.45) to pre-empt the question.
G7. s16-2 l.190 "For a general direction … also approaches eq:16.2-emt as (ka_s)²": asserted, not derived. limit16_2c.log at 30° gives
  peak shifts 0.0091, 0.0282, 0.1068 at ka_s = 0.5, 1, 2 (ratios 3.1, 3.8 per doubling, against 4.06 in plane), quadratic only
  asymptotically with damping. Acceptable as "approaches … at small ka_s"; drop "as (ka_s)²" or show the expansion.

## CHECKED (location → verdict; numbers recomputed)
- ch16.tex: 0.333 MeV (Ch1/13 PAER onset, SOTA ✓); "about 10 keV" Dirac threshold (10.5 keV ZrTe₅) ✓. Map caption: not a derivation.
- s16-1 l.3: |ε|² = 55.2² = 3047 ≈ 3000, 1.195 ≈ 1.2, ratio 2551 ✓. l.7–13: ε_D = (gα/6πv)B, Im = (gα/6v)ρ(s) = 1708.08929 Eq. (2.6) at κ = 1 ✓;
  ρ(s) ✓; dimension: L dimensionless ✓. l.17: 6.081 ✓; 0.61 ✓; 0.86–0.94 (leading/total 1.157→1.063) ✓.
- s16-1 l.23: F_med, ε_pub, Π = ω²(1−ε_pub) vs 1708.08929 (2.4), (4.4) ✓; 1910.02091 (2.5)–(2.7), (2.25)–(2.27) ✓.
- s16-1 l.33: 1910.02091 Eqs. (3.13)–(3.14) print q_x²v_{F,z}² for the x term ✓ (DC-49: published curves use v_F,x ✓); footnote 5 ✓;
  "text after Eq. (3.13)" Λ′ ✓; Eq. (2.1) couples to J_EM ✓.
- lim:16.1a caption: v_D 4e-4, Δ 2.5 meV, g 2, Λ 0.2 keV (1708.08929 Sect. 2.1, Fig. 4 caption ✓); gray ε_bg ≤ 1.049 (ε_bg² = 1.1) ✓;
  α/v_D = 18.24 ✓; 0.74 at ε_bg = 40 (0.735–0.736) ✓; 0.99 at 1000 (0.987) ✓.
- we:16-factor: α̃ 0.456, gα̃ 0.912 ✓; B = ln 256 + iπ = 5.545+3.142i ✓; 1.936 ✓; ε_D 10.73+6.08i ✓; |ε|² 2611 ✓; L 2.33e-3, 0.61, 3.80e-3 ✓;
  +5/3: ∫x(1−x)ln[x(1−x)] = −5/18 (×6 = −5/3) so the MS-bar bracket is ln+5/3 ✓, 0.27 → 0.35, 0.54 ✓; 1.632, 3.73, 1600 ✓; 0.0932, ×40 ✓;
  ρ_T 10 g/cm³ (1708.08929 l.971 ✓); 3.35e30, 9.5e-16, 1.5e-16, √40 = 6.32 ✓; 1/(n_eV_uc) = 1/(5e24 kg⁻¹·60 Å³) = 3.333 g/cm³ ✓;
  4.4e-42, 2.8e-45, ×1600, 3.2 decades ✓ (we16_1.log); min 3.37e-46 at 9 keV (csv) → 5.39e-43 ✓.
- s16-1 l.62: per-axis 9.51e4, 431, 1.59e4; (308.4/20.75)² = 220.9 ✓; tensor 1910.02091 Table 2 ✓.
- s16-1 l.64: velocities, Λ̃ = min(0.23·1973.27·1.1e-3, 0.216·…·4.4e-4, 0.1·…·9.1e-4) = 0.1796 eV ✓; g = 2 ✓; thresholds 10.49/20.98 keV,
  axes 12.66/9.39/11.29 keV (independent root find) ✓; ρ 6.089 (Fig. 3(d) table, Exp.) ✓; 98.4 events ✓; 2.24e-40 at 49 keV ✓;
  harmonic mean 50.53 ✓, 2554 ✓; 25.343² = 642.3 ✓ (Hochberg tensor = 1910.02091 Table 2 "Ref. [21]" row ✓).
- fig:16-zrte5: 6.135 g/cm³ for absorption (their "this work") ✓; |ε_bg,ij| ≤ 1.2 ✓ (Table 2; dropping it < 1 %, REF 49-1).
- s16-1 l.73: 87 % (0.871) ✓; 6.2–6.3 (6.207–6.325) ✓ = REF §4 item 5 ✓; 1.22e-15 ✓; √308.4 = 17.56, √20.75 = 4.56 ✓; Yb₃PbO 42.8² = 1831.8,
  √42.8 = 6.54 ✓; "model, not material" = REF §4 item 4 caveat ✓; "sensitive to the gap size" (Sect. 4) ✓.
- s16-1 l.77–79: gα̃ ln(Λ̃/Δ) = 0.380·2.443 = 0.929 ✓; μ = Δ/2v², E_b = μ(α/ε)²/2 = Δα̃²/4 = 0.141 meV ✓; Sommerfeld x = πα̃/b with b the
  carrier speed in the pair frame (relative speed 2bv_D) ✓; x/(1−e^{−x}) = 1.5 at x = 0.874 → b = 0.683 ✓, 1/√(1−b²) = 1.368 ✓; 85/18/5 % (log) ✓.
- s16-1 l.81: k_TF² = e²𝒩/ε_bg ✓ (dimension eV²). l.83: BNQ-TTF footnote 3 "α_eff ∼ 10 … qualitative" ✓.
- D.41: eq:D.41-eps, -aniso (1910.02091 Π⁰⁰ prefactor ge²/24π²v₁v₂v₃ = gα/6πv₁v₂v₃, ×v_i²q̂_i² ✓; physical sign used, "anti-screening"
  not quoted ✓ per DC-RESULTS); Im ε_D = (πe²/q²)V⁻¹Σ|⟨f|n|0⟩|²δ ✓; eq:D.41-ratio, on-axis ε_bg,ii², ε_D → 0 limit (q̂·ε_bg·q̂)² ✓;
  large-ε_bg behaviour |𝓛′| ≈ 6π/(gα̃) ✓; unpolarized factor between min and max ε_bg,ii ✓.
- s16-2 kernels: e²/((ε_a+ε_b)q) ✓; F_th = 2/x − 2(1−e^{−x})/x² = 1 − x/3 ✓, 0.946/0.850 at 100/300 eV, 0.9 at 191 eV ✓; 1/r_t = 281.9 eV,
  v_max/r_t = 0.747 eV ✓; Keldysh form ✓; tube kernel FT of the ring average = 2I₀K₀, ×e²/4π = 2αI₀K₀ ✓; small-x ln(2/x)−γ_E ✓;
  10 % at qr = 0.383 (108 eV) ✓; large x α/(qr) = 2πα/q shared over 2πr ✓ (s16-3 l.78).
- s16-2 plasmons: D_Dr = gE_F/4π ✓; n/m ✓; ¾v_F² (disc ¼ vs sphere ⅕) ✓; ω² = 2αE_Fq ✓; 20.4, 6.4 v_max ✓; edge 30.2 eV, 0.297 eV ✓;
  v_D = 3a_CCγ₀/2 = 3.411e-3 ✓ (2312.00866 Sect. II: γ₀ 3.16, a_CC 1.42 Å ✓); Das Eqs. (13)–(19) structure ✓.
- R⁰_1D = Nvq²/π(ω²−v²q²) ✓; pole and weight Ng_c|q| ✓ (Im 1/(ω²−ω_pl²+i0) = −πδ/2ω_pl); first moment Nvq² ✓; 31.4, 6.9 ✓;
  g_c 0.176/0.225/0.357 ✓; 7.3/5.7/3.6 v_max ✓; 1.92 eV ✓; 1–2 eV for 100–200 nm spacing ✓.
- Parabolic channels: 1D Lindhard closed-form zero ✓; correction (q²/2k_F²)g_c²[¼ + g_c²/3(1−g_c²)] verified to 1e-9 at g = 0.2, 0.5, 0.8
  (par.py, mpmath) ✓; lim:16.2a 1.28/1.305 k_F, g_c 0.19–0.63 ✓.
- Demon: v_a = (n_h/2m_h𝒩_F)^{1/2} ✓; share (q²/(q²+k_TF²))² and (q/(q+q_s))² (sympy) ✓; widths (π/2)v_a/v_F and ν/√(1−ν²) ✓;
  Re f₂ = 1, Im f₂ = ν/√(1−ν²) ✓; lim:16.2b 0.157, 0.53 (0.527) ✓, 3 % at 0.02 ✓; 2507.07164: 80–800 meV along z, 1.6 eV in plane,
  HDD ~200 meV, Eqs. (1), (2) ✓.
- we:16-demon: k_F 156.4 eV ✓; v_F 1.53e-3, 7.65e-5 ✓; q_s = 2αm_l = 1.49 keV ✓; v_a 2.42e-4 = 72.5 km/s ✓; 0.158, 3.16 ✓; 0.128, 0.0134 ✓;
  41.8 → 4.81 meV ✓; 0.160, 0.77 meV ✓; 30.6 meV ✓; 1.75e-4 ✓; ¾(1/3.162)² = 0.075 ✓; 1.37 keV, 3.8 keV, 1.8 eV, ×11 ✓. (1.72e-4, the
  "check" peak 4.97 meV and 1.76e-4 taken from we16_2.log, not recomputed.)
- Stacks: Σe^{−q|n|a+iq_zna} = sinh/(cosh−cos) ✓; bulk limit e²/(ε_ba_sq²) ✓; in-phase and acoustic modes ✓; small-θ ω² = fε_∞ω_p²θ²/ε_B ✓.
- lim:16.2c: EMT peaks 0.4226/0.2754 undamped → 0.4215/0.2740 damped ✓; ε_A = −1 at 0.4767 eV ✓; ka_s < 1.94 → k = 76.7 eV, 14.5 keV ✓.
- s16-2 l.203: Hölder equality for a single line ✓.
- s16-3 ejection: m_min = 2Φ/v_max² = 1.224 MeV, q_min 1.623 keV, β = 7.514 keV ✓ (1606.08849 Eq. (2), Z_eff 4.03 ✓, Φ 4.3 eV and
  footnote 2 ✓); eq:16.3-Sej → eq:16.3-rate factor 1/4π ✓; eq:16.3-iso 1/16π³ ✓; OPW form factor ordering ⟨χ_p|e^{iq·r}|ψ_i⟩ ✓;
  ψ̃ ∝ βk_z/(β²+k²)³ (Eq. (4)) ✓; tails |p−q|⁻⁵ ✓; table 0.46–25, 0.4–4.3, 740 (736) ✓; forward ≈ 2× backward, 10 MeV–10 GeV (1606.08849
  Sect. III) ✓; Fermi factor omitted "text after Eq. (6)" ✓; 7.3/3.4/2.6 ✓; lim:16.3a 31 eV, 0.60/94 eV, 3.5, 2.1, 4.3 ✓.
- s16-3 tubes: v_D = 3ta/2 = 3.022e-3 = 9.06e5 m/s ✓; 2Δ₁(1 nm) = 0.795 eV ✓; 0.760/J₀² 0.741, 1.521/0.250 ✓; 226 keV ✓;
  eq:16.3-R1D re-derived (overlap ¼θ′²q², two roots, ε/(v²k)) ✓; ∫ = g v_D, Δ → 0 gives g v_Dδ(s) = metallic line ✓; eq:16.3-eps2 ✓.
- s16-3 dots: eq:16.3-gap = Blanco Eq. (5) ✓; 1.2 − 0.41 = 0.79 eV ✓; a_x 20 nm [129] ✓; closure Σ_e = 1 (Dirichlet completeness) ✓;
  "above about 2.5 eV" ✓; 1/(m_φv) = 0.197 mm ✓; sphere field 3ε_out/(ε_in+2ε_out) ✓.

## Campaign values and parallel compute
- CORRECTIONS/SOTA: Dirac ε_bg²/ε_bg (REFEREED) ✓; "never ×0.55–0.62" ✓; 2D rule "substrate only through v_C^2D, remote bands only through
  r_K; never rescale the vertex" (CORRECTIONS l.538) = s16-2 l.37 ✓; Luttinger g·v = v_F and CNT ×4 ✓; 2110.01587 Eq. (16) exact ✓;
  sheet screening = kd ≪ 1 limit of Eq. (19) (SOTA l.679) ✓; ZrTe₅ Δ_D conflict, see G2. No superseded value used.
- DC-RESULTS / R18: DC-49 bears on P4, P5, absorption 6.2–6.3 (✓ identical), Yb₃PbO ×1832 (✓, with the model caveat in REF wording ✓),
  ×642 for the isotropised 1708.08929 model (✓; REF 49-2: ×640 must not be applied to 1910.02091, and the book does not). Differences:
  ×4800–6600 vs (4–6)×10³ (P4); recomputation ratio 0.63–0.72 vs DC-49's 0.90–1.06 (P5, halo). Nothing withdrawn is quoted.
