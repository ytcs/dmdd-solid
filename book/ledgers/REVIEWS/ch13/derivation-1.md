# Ch13 part 1: derivation check (isolated), 13.1–13.4, D.35, D.36
Reviewer: derivation verifier (long-form-writing SKILL §5). Date 2026-11-06. No tex edited, nothing committed, no QE run.
Scripts (independent, not the figscripts): `/tmp/claude-0/-home-user-breakthrough-maths/30a63adb-c597-5cb8-b46c-4c5645c8b7d4/scratchpad/rev/`
  `kin.py` (kinematics, every 13.1/13.3/13.4 number), `chain.py` (own Fock-space brute force of WE 13.2), `ph.py`, `ph2.py`
  (phonon numbers from `figscripts/ch05/si_ifc.py`, bands from `ch03/qe_si_pbe.npz`), `sym.py` (sympy algebra), Knapen data
  from `figscripts/ch13/eps13_4.npz`. Sources fetched with lit.py into `sources/review-ch13/` (2108.03239, 1603.06965,
  2101.08275, 2601.11177; the PDFs I fetched have been deleted. 1202.3454 was already there and was read, not deleted).
Verdicts: CHECKED (redone, agrees) / WRONG (with correction) / GAP (missing step, unsupported number or label).

## Summary
- PRIORITY items. The four-path amplitude, its fermion signs and the Pauli/exchange band sum all hold: algebra redone,
  and my own 924-determinant brute force reproduces every printed number of WE 13.2. The onset exponents
  (3 / 4 / 2 / 3/2 / 5/2) and their cone averages are CHECKED with sympy and the computed dispersion. Screening:
  the 1/ε_mac factorisation (exact), the two solvable limits, k_x and all numbers in WE 13.4 are CHECKED against the
  Knapen/DarkELF data. The interim factor [0.4, 1.8] is a GAP: it is inconsistent with what 13.4 now derives (item S5).
- WRONG: four small errors (D.35 intermediate denominator; 0.62 → 0.61 keV; 44.3 → 44.1 meV; "4 to 5 %" → 3.7–4.8 %).
- NOTATION drift: four items, all clashes (M^± means two things, ς has three meanings, W^scr without its R, ω_TA without an argument).
  No factor-2, π or sign error was found.

## 13.1 The indirect-gap window
| location | verdict | note / correction |
|---|---|---|
| l.3: 0.35 MeV → ½mv² = 1.23 eV, q = 0.93 keV; E_min(0.93 keV) ≈ 1.9 eV | CHECKED | 1.229 eV, 927.5 eV; PBE+scissor [100] gives 1.855 eV |
| l.7: k_c/2v_max = 0.366 MeV; floor 0.333 at q = 0.88 keV; 0.474 MeV at q = k_c | CHECKED | 0.3661, 0.3332 (q = 883 eV), 0.4740 |
| eq:13.1-mZP (both forms), "restricting q or k only raises it" | CHECKED | m ≥ q²/2(qv−E) from qv−q²/2m ≥ E; monotone in E; min over a subset ≥ min |
| l.21: M_eh = 0.916+0.277 = 1.19; parabola m_ZP = 0.425 MeV at 1.46 keV; shortfall 0.48 keV, 0.19 eV, total 1.36 eV | CHECKED | 0.42468 MeV at q = 1460 eV; 480 eV; 0.189 eV |
| l.21: PBE bands, [100] 0.420 MeV at 1.43 keV; [110] 0.548; [111] 0.615 | CHECKED | qe_si_pbe.npz +0.613 eV scissor: 0.4200 at 1427 eV; 0.5476; 0.6152 (spline 0.4199 at 1410 eV) |
| l.23: exciton shift ∂m/∂E = m/(qv−E); 0.0025 MeV, 0.6 % | CHECKED | 0.00249 MeV, 0.59 % |
| eq:13.1-EPA; relaxation off the extrema < 0.02 meV | CHECKED | ½M_eh u² at Q*: u_TA = 2.06 km/s → 0.014 meV |
| l.36: n_B(14.8 meV) = 0.12 (77 K), 2e−19 (4 K), 3e−75 (1 K); absorption sideband 0.329 MeV | CHECKED | 0.121, 2.3e−19, 2.9e−75; 0.32900 |
| eq:13.1-mPAdef → eq:13.1-mPA (q* = 2E/(v+E′), m = 2E/(v²−E′²)) | CHECKED | sympy: exact at the stationary point (not only to O(u²)) |
| keyresult "Window kinematics" | CHECKED | — |
| l.56: ω_TA(Q*) = 14.8 meV at 0.46 (2π/a); tilt 0.3 rad raises it by 0.7 meV; LA, TO onsets 0.341, 0.350 MeV; q* = 0.90 keV | CHECKED | si_ifc: 14.79 meV; +0.68 meV; LA 0.34097, TO 0.35006; TA optimum 0.33743 at q = 896.5 eV |
| l.56: TA 18.27 meV of the optical edge [macfarlane1958fine] | CHECKED | = 212 K phonon temperature of Macfarlane et al. (paywalled; 6.5/NOTATION value; not refetched) |
| Fig 13.1 caption: 0.3374 / 0.3332 / 0.3378 MeV, 8 % soft at X, scissor 0.613 eV | CHECKED | TA(X) PBE 17.05 vs 18.57 meV (−8.2 %) |
| WE 13.1: k_c = 1940 eV; pass 1: q* 883, Q* 1057 eV = 0.463, ω 14.86; pass 2: E 1.1849, q* 894, Q* 0.458 = 0.53 Å⁻¹, ω 14.79; u = 2.1 km/s, u²/v² = 7e−6 | CHECKED | 1940.5; 1057.4 = 0.4632, 14.868; 894.2, 0.4583 = 0.5302 Å⁻¹, 14.792; slope 13.6 meV·Å = 2.06 km/s, 6.7e−6 |
| WE 13.1: onset 0.3374, +1.3 %; sensitivity 2.8e−4 MeV/meV; scaled TA 16.1 → 0.3378; 18.27 → 0.3384; bound 1.1553, q* 0.885, ω 14.85, 0.3332 | CHECKED | 0.33743 (+1.26 %); 2.85e−4; 16.11 → 0.33780; 0.33842; 0.33326 |
| l.79 Ge: ΓL = 1.90 keV; floor 0.212 at 0.56 keV; 1.34 keV = 0.70 ΓL; TA(L) 1.9 THz = 7.9 meV; onset 0.2119–0.2141 | CHECKED | 1.8977 keV; 0.21189, 561.5 eV; 0.704; 7.86 meV; 0.21414. Source: Haxhijaj 2601.11177 Table 4, Ge L_TA = 1.9 THz (Expt−ZPE) ✓ |
| l.79 Ge: M_eh = 1.59+0.469 = 2.06; m_ZP = 0.32 MeV at 1.10 keV | CHECKED | 0.3238 MeV at 1103 eV |
| l.81 GaAs: floor 0.433; q* 1.15 keV; M_eh 0.42 / 0.96 → 3.1 / 1.3 eV | CHECKED | 0.43289; 1147 eV; 0.067+0.350 / 0.067+0.893 (Luttinger 6.98, 2.06, 2.93); 3.07 / 1.34 eV |
| eq:13.1-mZPdir | CHECKED | sympy: max_q (qv − q²/2μ) = ½μv² ⇒ μ ≥ m_g ⇒ m ≥ m_gM/(M−m_g) |
| l.93 GaAs: m_g = 0.847 m_e; [100] never; [111] 3.7 MeV; onset 0.433–0.436 MeV (TA ≤ 10.5 meV at X) | CHECKED / GAP | 0.8472; 3.68 MeV; 0.43588. GAP: 10.5 meV is the PBE value (dagger in tab:5-phonons), not measured (≈9.8 meV). It still bounds the onset from above, but say "computed" |
| l.93 GaAs L valleys: 0.517 / 0.560 MeV (editor item, 13.1 writer) | CHECKED | 0.51691; ΓL(5.653 Å) = 1899.4 eV → 0.56048. Window 0.433 → 0.517–0.560 confirmed |
| 13.9 l.108 (editor VERIFY, 1.71 eV) | CHECKED (numerics only) | Varshni with the recalled Vurgaftman L parameters (1.815 eV, 0.605 meV/K, 204 K) gives 1.707 eV at 300 K; floor 0.4870 MeV ✓. Locator not checkable (not open access) |
| l.99: Si onset moves 3e−4 MeV per meV; Ge confined to 0.002 MeV | CHECKED | 2.85e−4; 0.2141 − 0.2119 |
| Editor item: Q* 14.72 @ 0.510 Å⁻¹ (E.14) vs 14.79 @ 0.53 (13.1) | CHECKED | 13.1 matches si_ifc at the measured a (14.79 at 0.530 Å⁻¹); E.14 already aligned (App E pass 2) |

## 13.2 The phonon-assisted amplitude (PRIORITY)
| location | verdict | note / correction |
|---|---|---|
| eq:13.2-final, momentum bookkeeping k′ = k+q+Q | CHECKED | — |
| eq:13.2-T (E_m includes the phonon energy) | CHECKED | consistent with D.35-T, where ∓ω_Q is written out |
| eq:13.2-paths A–D: vertices, crystal momenta, denominators | CHECKED | redone term by term: A (p, k+q), B (p, k+Q), C (hole p, k+Q), D (hole p, k+q); each denominator = E_i + (energy supplied) − E_m |
| l.51 fermion sign of C (and D) | CHECKED | c†_p c_v c†_c c_p = −c†_c n_p c_v (three transpositions), redone by hand and in my Fock code |
| l.55 on-shell C → B(filled p), D → A(filled p); keyresult eq:13.2-M | CHECKED | denominators: ω−ε_c′+ε_p = −(ε_v−ε_p∓ω_Q), ε_p−ε_c′∓ω_Q = −(ω−ε_p+ε_v) |
| l.67 M dimensionless, O(1) in N; N^{−1/2} removed by Σ_Q | CHECKED | g [eV] ρ [1] / [eV] |
| l.71 / eq:13.2-q0: A(p=v) → g/ω, B(p=c) → −g/ω, M(q=0) = 0 | CHECKED | — |
| WE 13.2 (two-band chain): gap 1.448 eV, ω 1.508, E_min(q) 2.912, margin 1.40; table denominators −1.552, −3.060, −1.492, −3.120; terms A–D; blocked forms +1.492, +3.120 equal to C, D; |ρ_vv|² 0.642, |ρ_cv|² 0.358; |C+D| 0.077, |A+B| 0.065, |M| 0.100; brute force = band sum; only four intermediate states; empty-only |M|² = 0.42 → ×2.4; off shell by 0.10 eV: C → 0.0066−0.0406i, 3.7 % | CHECKED | own implementation (Φ = 0.3 twist from the script docstring): all reproduced. Brute force − band sum = 7e−17. Complex values agree up to an overall gauge sign (−1 on every entry, as it must be for a phase of ψ_c, ψ_v). Off shell: 3.70 % |
| l.104–106 no interference at O(g²); order-g² self-energies belong to ZPL | CHECKED | orthogonality of phonon occupations; the thermal ρ is diagonal |
| eq:13.2-doff | CHECKED | four cases redone; for B/D the bound is E_g ± ω_Q, so E_g − ω_Q covers absorption |
| l.115: 1.17−0.064 = 1.11 eV; margin ≈ 0.7 eV at onset | CHECKED | — |
| eq:13.2-Mad, frozen-phonon derivation, eq:13.2-HT | CHECKED | bra term from b* in the ket: ⟨ψ_p,k′−Q|V_Q†|ψ_c⟩* = g_cp(k′−Q,Q) ✓ |
| eq:13.2-err signs | CHECKED | 1/(D_A ± ω) and 1/(D_B ∓ ω) expansions |
| l.135: ω/δ_off = 1.6 % (TA 18.27), 5.2 % (TO 57.73); 10 % needs 0.18 / 0.58 eV; chain: 1.9 % at 1.40 eV, 6.2 % at 0.62 eV | CHECKED | 1.65 %, 5.20 %; 0.183, 0.577; chain: 1.94 % (q = 2 steps), 6.20 % (q = 1 step, margin 0.624 eV), both below ω/δ_off (4.3 %, 9.7 %) |
| l.51 citations: Giustino Eq. (200); Noffsinger Eqs. (2), (3) | CHECKED / GAP | Both are the two-term form summed over all p (the combined result), not four separate paths. Reword: "Their combined form is the two-term amplitude of …" |
| l.3 Kahn & Lin Sect. VI | CHECKED | 2108.03239 Sect. VI (Migdal) intro names the 2→3 electron+phonon process near the gap |
| Editor item (13.8 note): E.15 "two-pair intermediate states" | CHECKED | 13.2 and D.35 are right: one pair per intermediate state (proved in D.35; brute force finds exactly four). E.15 must be reworded as the note says |

## 13.3 The phonon-assisted rate (PRIORITY: onset exponents)
| location | verdict | note / correction |
|---|---|---|
| eq:13.3-SPA prefactor 4π/Ω; N cancels | CHECKED | (2π/𝒱)·2·N⁻¹·N²⟨⟨⟩⟩ = 4π/Ω; dims eV² (= NOTATION S) |
| eq:13.3-LPA = (e²/2q²)(1−e^{−βω})S; 8π²α/(Ωq²) | CHECKED | e² = 4πα; matches eq:4.4-SL |
| w_± = rate − inverse (D.35 detailed balance) | CHECKED | sympy, emission and absorption |
| l.46 zero-phonon limit = eq:10.1-S0; f_crys normalisation q³ΩS̄/(4παm_e²) | CHECKED | agrees with CORRECTIONS l.37 (4πα, not 2πα) |
| q → 0 consistency with eq:6.5-eps2PA (g_deg πe²/ω²Ω) | CHECKED | ρ_cv ≈ q·v/ω gives 8π²α|M_opt|²/(Ωω²) = 2πe²/(Ωω²) |
| l.3: 0.35 MeV at 1 keV → 1.22 eV; E_min(1 keV) 1.77 eV; TA 14 meV, 0.94 keV | CHECKED | 1.221; 1.767; 13.98 meV; k_c − q = 940 eV |
| l.58 completing the square −½M_eh u²; 0.02 meV (TA), 0.18 meV (LA) at 1 keV | CHECKED | κ_e = −m u, κ_h = +m u; u_TA 16.9 meV·Å = 2.57 km/s → 0.022 meV; u_LA 48.3 meV·Å → 0.18 meV |
| eq:13.3-near (x², prefactor Ω(m_d m_h)^{3/2}/4π²) | CHECKED | sympy convolution of two pocket DOS × 4πΩ; m*_d = (0.916·0.191²)^{1/3} = 0.322 |
| eq:13.3-Eth (|Q*|², θ_Q, κ_ν) | CHECKED | expansion redone |
| D-counting rule; D = 6 → x², D = 8 → x³, forbidden +1 → x⁴; exciton x^{1/2}, x^{3/2}; ring 5/2 | CHECKED | — |
| l.75 C_4v selection rules: Γ25′ → Δ2′ ⊕ Δ5; LA Δ1, LO Δ2′, T Δ5; LA forbidden, TA/TO/LO allowed | CHECKED | standard compatibility. Consistency: Δ5⊗Δ5 ∌ Δ5, so the TA splitting off axis is quadratic, which matches κ > 0 for both TA branches |
| l.77 SOC part "below 10⁻⁴" | GAP | number not derived or sourced (cf. CW1-errata "SOC-lifted 1.3×10⁻⁴" for a different vertex). Cite the source or say "estimated as small" |
| l.77 (2̄00) class: vertex picks up the glide phase and becomes Δ2′; LA allowed | GAP (unverified) | plausible: e^{−iG·τ} = −1 on the operations with a fractional translation, but which C4v classes carry τ was not checked here. Same open item as the editor's 13.9 glide-parity VERIFY |
| l.79 TA on axis for |q| < 1.34 keV; optical min 44 meV vs 60 on axis at 1 keV; Ge Λ reps; Ge TA split linear | CHECKED | si_ifc: on axis at 1.30/1.34 keV, off axis at 1.38; optical min 44.14 meV (θ = 1.92 rad), axis 59.51 |
| keyresult eq:13.3-pon | CHECKED | Agrees with SOTA l.363 (Si TA 3, LA 4, TO/LO 3; Ge 3) |
| l.93 fit ranges (x³ within 10 % to 1.3 meV, 3.3 at 10 meV, x⁴ to 2.4 meV); 1.2e−3 at 0.1 meV | CHECKED (last) / not re-run | 0.1/24·(0.240+0.047) = 1.196e−3; ranges need fig13_3.py, not re-run |
| Fig 13.3 caption: optical onset "44.3 meV" | WRONG | the minimum over all directions is 44.14 meV (Nelder–Mead from 40 starts; a grid gives the same). Print 44.1 meV. The edges at 13.98 and 25.00 meV and X 17.06 vs 18.57 are ✓ |
| l.104–106 window bound |Q*| ≥ M c + (M²c² + 2Mδ_w)^{1/2}; c = 5.0 km/s; 0.31 Å⁻¹ "or 0.62 keV"; 1.33 keV | WRONG (rounding) / GAP | Phase velocity at 0.31 Å⁻¹ is 5.02 km/s ✓. Bound: 614 eV = 0.311 Å⁻¹ with M = 1.19 m_e (617 eV with 1.2). Print **0.61 keV** (1.94 − 0.61 = 1.33 is then consistent; 1.94 − 0.62 = 1.32 is not). GAP (13.6-writer item): label 1.33 keV as the parabolic value and add 1.27 keV from the computed bands (13.6 l.73/82 already does) |
| WE 13.3: 0.48 Å⁻¹ = 0.41 X; ω 13.98 / 25.00; onset 1.184 eV, 0.341 MeV; ZP edge 0.60 (parabola 0.73); window to 0.30 eV | CHECKED | 0.4766 Å⁻¹ = 0.412; 0.34106 MeV; 0.727 eV |
| WE 13.3: slope 16.9 meV·Å; κ₁ = 8.85 meV | CHECKED | 16.93; 8.84 (8.85 with the rounded inputs) |
| WE 13.3: κ on θ = 0.02: lower TA 2.3–8.5, upper 18–24, LA 16.8; ⟨1/κ⟩ 0.240, 0.047 | CHECKED | 2.30–8.48, 18.2–24.4, 16.78; 0.2399, 0.0468 |
| WE 13.3: Cx³/12⟨1/κ⟩, Cx⁴/48 (q/(k_c−q))²⟨1/κ²⟩, cone πx/κ, fraction x/4κ | CHECKED | sympy |
| l.21 θ_ep = 0.010–0.016 | not re-derived | cross-reference to eq:8.5-theta |
| Editor items 13.3 writer (δ_w = 0.3; 0.60 vs 0.73 both labelled; 1.19 vs 1.2) | CHECKED | 13.3 states 1.19 m_e; both edge values are labelled |

## 13.4 Screening (PRIORITY)
| location | verdict | note / correction |
|---|---|---|
| l.3, l.7: ε ≈ 6; ×30–50; (ω_Q/E_g)² ≈ 3e−3 | CHECKED | (0.064/1.17)² = 2.99e−3 (bound with the top phonon; 1.4e−4 for TA) |
| eq:13.4-rhoscr, eq:13.4-rhoLF (exact 1/ε_mac factorisation) | CHECKED | algebra of D.36 redone, plus a numerical test with random 6×6 R⁰, v: column error 1e−16, 1/(ε⁻¹)_00 = 1 − v₀R̄₀₀ to 2e−16 |
| l.36–40 first-order ϱ^F, source ς, ς_cv = M^±[ρ^scr] | CHECKED | occupation factors redone for m empty/filled; on-shell denominators match D.35 |
| eq:13.4-dn2 (trace with e^{−iKr} → ρ_ab*; denominator ω_f + ε_b − ε_a) | CHECKED | — |
| keyresult eq:13.4-Mscr; dimensions | CHECKED | ρ·W^scr[eV⁻²]·δn^(2)[eV²] dimensionless |
| l.74 coherent-potential limit → M/ε(q+Q, ω_f) | CHECKED | 1 + ε̃⁻¹f_Hxc R⁰ = ε̃⁻¹ |
| l.74 / D.36 rigid translation: c_A = iℓ ê·q; four-path → ρ/ε(q,ω); pair term → 1/ε(q,ω_f) − 1/ε(q,ω) | CHECKED | commutators and the v_C R⁰ = 1 − ε identity verified with sympy |
| l.74 / WE "<10⁻³", "2×10⁻³" sized with ω_TA = 14 meV | GAP (wording) | at Q = 0 an acoustic ω_Q → 0, so in the strict rigid limit ω_f = ω and the pair term vanishes. The 2e−3 is the frequency-shift size at the zone-interior ω_TA, not a property of the rigid limit; say so |
| eq:13.4-Lscr; |ε_mac|⁻² = (ε₁⁰)⁻²[1+O(g²)] | CHECKED | — |
| eq:13.4-kxc; k_x = −(2/3) f_x/n; f_x = −e²/4k_F²; ratio (2/3)(k_c/2k_F)² | CHECKED | sympy; HL e² = 4πα; n = 0.1998 Å⁻³, k_F = 1.8085 Å⁻¹, 0.0739 × 2/3 = 0.049 |
| l.122 static ε: 10.2 (q → 0), 6.1–6.6 at 1 keV, 3.2–3.7 near 2 keV | CHECKED | eps13_4.npz: 10.21; 6.07/6.63; 3.24–3.75 (1866–2032 eV) |
| l.124 macroscopic LF +25 to 31 % | CHECKED | (6.31/5.52)² = 1.307, (6.93/6.20)² = 1.249 |
| l.126 four mesh points 1.87–2.03 keV; ε₁(1.2 eV) 3.3–3.8 / 2.9–3.5; factor 0.07–0.12; Im ≈ 1e−3 | CHECKED | 1866, 1888, 1972, 2032 eV; 3.30–3.84 / 2.91–3.51; 0.068–0.118; ε₂ = 1.1e−3 at 2032 eV |
| WE 13.4: mesh 0.944, 0.986 keV; ε₀₀ 6.31–6.93, ε_mac 5.52–6.20; 1/ε² 0.021–0.025, 0.026–0.033; ×40–48, ×30–38; 0.0073, ×2.9–3.4, ×3.6–4.5; 13 %, 22 % | CHECKED | 6.312/6.929, 5.521/6.202; all ratios reproduced |
| WE 13.4 "Across the window … 4 to 5 % at both points" | WRONG (minor) | head: 4.2 / 4.8 %; macroscopic: 3.7 / 4.4 %. Print "4 to 5 % with the head, 4 % with local fields" or "less than 5 %" (l.122 is fine) |
| WE 13.4 log slope 0.07–0.08 | CHECKED | 0.073, 0.083 |
| Citation knapen2021dark | CHECKED / GAP | 2101.08275 Sect. III: GPAW RPA with and without LFE ✓. The mesh files are those of the DarkELF package (2104.12786); cite it for the data, as we13_4.py does |
| l.150 "13.9 carries the external local fields and the pair channel together" vs 13.9 l.87 "local-field wings of the vertex and the pair channel" | GAP | the two descriptions differ: "external local fields" includes the macroscopic +25–31 %, while the "wings" do not. Align, and state whether 13.9's model ε₁ includes the macroscopic LF |

### S5. The interim factor [0.4, 1.8] (13.9 l.87, l.163, l.190; E.14 l.13; E.16 l.19): GAP
- Source: WP3-v3 C28 (returns/R8/WP3-v3.md l.262–263, l.649–650): (1+δ_ω)(1+δ_LF)(1+δ_pair) with δ_ω = ±2 %,
  δ_LF ∈ [−0.2, 0.2] and δ_pair ∈ [−0.5, 0.5] gives 0.98·0.8·0.5 = 0.392 and 1.02·1.2·1.5 = 1.836, i.e. [0.4, 1.8]. The arithmetic is CHECKED.
  It is the current campaign value: SOTA l.65 records [0.5, 1.2] as superseded by [0.4, 1.8], and LIMITS L8 and DC-17 use [0.4, 1.8].
  CORRECTIONS l.82 still says "interim factor [0.5, 1.2] stands". That entry is stale and should be marked superseded. The book uses no superseded value.
- 13.4 now contradicts the inputs of the envelope. (i) The coherent-potential limit gives a factor 0.07–0.12, i.e.
  δ_pair ≈ −0.9, outside [−0.5, 0.5]. (ii) 13.4 derives a definite, signed macroscopic LF change of +25–31 % (head → ε_mac),
  outside |δ_LF| ≤ 0.2 and not "sign not derived".
  13.9 itself says "the two limits span a factor of ten", which makes a ×4.5-wide envelope look arbitrary.
- The range can be defended, but the text has to say how. 13.9's estimate is calibrated on the measured optical edge, which already
  contains the pair channel at q = 0, and the pair momentum is pinned at k_c (13.4 l.72). The factor then multiplies only the
  ratio (1+δ_pair(q))/(1+δ_pair(0)) times the wing terms, not 1+δ_pair itself. Applying 0.07–0.12 on top of the measured
  edge would double count. Correction: in 13.9 (and E.16 l.19, E.14 l.13) say that the factor covers the q-dependence of the
  pair channel beyond the optical calibration plus the vertex wings, and do not justify it by the span of the two limits.
  State whether ε₁(q,ω) of the estimate includes the macroscopic LF (otherwise the +25–31 % is a known factor, not part of the envelope).
  Also check that the "factor two from screening at finite q beyond the optical limit" in 13.9's error budget is this same item and is not counted twice.
  The envelope's geometric centre is 0.85 (WP8-F median 0.85), not 1.

## D.35
| location | verdict | note / correction |
|---|---|---|
| eq:D.35-T; intermediate-state classification; momentum placement | CHECKED | — |
| hole-path sign display (l.30) | CHECKED | — |
| l.34 diagonal terms: "⟨Φ_f|X|Φ_f⟩ y_cv/(E₀ − E_f ∓ ω_Q) with E_m = E_f ∓ ω_Q" | WRONG | the denominator is E₀ − E_m ∓ ω_Q = E₀ − E_f = −ω on the shell. As printed (E₀ − E_f ∓ ω_Q) it would be −ω ∓ ω_Q. Replace with "y_cv/(E₀ − E_m ∓ ω_Q) = −y_cv/ω". The conclusion −(⟨X⟩₀ + x_cc − x_vv)y_cv/ω and the linked-cluster cancellation are right |
| eq:D.35-theorem (resolvent form) | CHECKED | — |
| off-shell statement | CHECKED | — |
| adiabatic form, eq:D.35-drho (b* terms reach k ± 2Q) | CHECKED | — |
| error series and bound ω/(δ_off − 2ω) | CHECKED | geometric series r/(1−r), r = ω/(δ−ω) |
| thermal averages, detailed balance, w_± f_v(1−f_c) | CHECKED | sympy |
| Editor item: overfull boxes l.34–38, 74–75 | not checked | layout, no build run |

## D.36
| location | verdict | note / correction |
|---|---|---|
| eq:D.36-second, band-sum theorem via ϱ (both m classes, on-shell denominators) | CHECKED | — |
| ε̃⁻¹ f_Hxc elimination, retarded | CHECKED | (1 − R⁰f)⁻¹ and (1 − fR⁰)⁻¹ push-through identity |
| macroscopic factor R = R̄ + R̄v₀R ⇒ (ε̃⁻¹)_G0 = (1+v₀R₀₀)[δ + (f̄R̄)_G0] | CHECKED | numerically (above) |
| optical theorem: Im W = W†(Im R⁰)W | CHECKED | RPA, Hermitian v |
| two solvable limits | CHECKED | (see 13.4) |
| ALDA source: cross term coefficient 1 (not ½); ratio formula | CHECKED | agrees with VER-WP3-B note (2) (SOTA l.372) |

## NOTATION / convention drift
| item | verdict | correction |
|---|---|---|
| M^±_cvν: NOTATION l.596 defines M^±_cvν(k,Q) "1 (a velocity)" (6.5). 13.2/13.3 use M^±_cvν(k,q,Q), dimensionless | GAP (one symbol, two meanings) | add a row for the 3-argument dimensionless density amplitude (13.2), or decorate one of the two (e.g. M^{γ±} for light). Also add M^ad, M̃^± (13.2, 13.4) |
| ς (13.4/D.36 second-order source) | GAP (clash) | NOTATION l.465 ς = Σ_kδϱ_k (D.9 only), l.1153 ς_Qν = ZG signs (E.8). The 13.4 note calls ς a "new glyph", which it is not. Pick another glyph (e.g. 𝔰^(2) or σ^(2)) or register it with a scope note |
| W^scr "retarded" in 13.4 keyresult and D.36 | GAP (convention) | NOTATION l.387: retarded is W^{scr,R}; bare W^scr with a real argument is time-ordered. Write W^{scr,R}(q+Q, ω_f) in eq:13.4-Mscr, D.36-amp and the fig 13.4 caption |
| ω_TA without an argument (13.3 WE "ω_TA = 13.98", 13.4 WE "ω_TA = 14.0 meV") | GAP (minor) | NOTATION l.592/598: bare ω_TA is the 6.5 value at k_c (18.27 meV). Write ω_TA(Q*) |
| ϱ (no hat) for the KS one-body density matrix in 13.4/D.36 | CHECKED (acceptable) | consistent with ϱ(x,x′) of D.4; ϱ̂ is the operator |
| L^PA screened from 13.4 on; δ_LF, δ_pair first defined in 13.4 (NOTATION l.799 says 13.9/E.16) | GAP (known, editor) | update NOTATION at the merge |
| ⟨⟨·⟩⟩, n_Qν, ε_mac = 1 − v_C R̄₀₀, ε̃⁻¹, f_crys normalisation, S [eV²], L [1], m*_d 0.322, v_max 794.5 km/s, m_min^{ZP,PA} | CHECKED | no factor-2, π or sign drift found |

## Campaign cross-check (CORRECTIONS / SOTA)
- Onsets 0.3374 (continuum) / 0.3332 (replica), ZP-edge bracket 0.40–0.42 (13.1 l.23 upper value 0.420–0.425): consistent with
  CORRECTIONS l.314/335/568 (0.405–0.408, 1s 0.402–0.405) and LIMITS L8. M_eh = 1.19 m_e and Q_w = 0.31 Å⁻¹ at δ_w = 0.3 eV agree with CORRECTIONS l.571.
  The superseded 1.41 m_e is not used.
- Exponents agree with SOTA l.363. The sign of the ALDA cross term agrees with SOTA l.372. Interim factor: see S5 (current value used; CORRECTIONS l.82 stale).
- Static-DFPT error O(ω_Q²/E_g²) (13.4 l.7) agrees with CORRECTIONS l.215 (not O(ω_Q/E_g)).
