# Ch20 part 1 (20.1–20.3): derivation check (isolated)
Reviewer: derivation verifier (SKILL §5). Date 2026-11-06. Files: tex/ch20/ch20.tex, s20-1.tex, s20-2.tex, s20-3.tex.
Method: independent sympy/numpy scripts (scratchpad a201–a206.py; an independent AMM solver; an independent fragmentation
solver), not the figscripts. Sources read in sources/review-ch20/ (1109.1193, 2302.05998, 2004.10709, 2303.02196,
1803.02903, 2408.04732, 1109.4343, 1805.02495, 2109.13551, 1401.1937, 1701.03459, 2012.12430); PDFs deleted.
Verdicts: CHECKED / WRONG / GAP. No tex edited. Nothing heavy run.

## Summary of rulings asked for
1. **Luke rate, 20.1 vs E.12: 20.1 is right.** Golden rule with Leman's own vertex (Eq. 20) gives
   Γ_L = (c_LA/3l_0)(k/k_s)²(1 − k_s/k)³ (sympy, exact). Leman Eq. (22) and G4CMP Eq. (9), integrated over θ, give the same
   (ratio 1, sympy). Leman Eq. (21) = G4CMP Eq. (8) = eq:E.12-luke is smaller by k_s/k (sympy). **E.12 is WRONG**: replace by
   eq:20.1-luke, and its sentence "grows linearly at large k" → "grows as k² at large k".
2. **Al elastic constants: change quantified (table §20.3-Al).** The 0 K Voigt set moves t̄_esc 0.327 → 0.368 (+12.5 %),
   t_l(60 nm) 0.223 → 0.187 ns (−16 %), t_l/t₀ 0.86–1.08 → 0.72–0.94, the lumped-film factor 3.06 → 2.72, the trapped-flux
   angle 35.2° → 37.7°, the fitted 𝔩_f/d_f range ≈6–26 → ≈5–23. **Caution:** Ch15's "c_LA 6.47, c_TA 3.40 km/s" are the
   **[100]** speeds √(C11/ρ), √(C44/ρ) at ρ = 2.73 (s15-1 l.7, s15-4 l.38), not isotropic averages. 20.3 must not import
   them into the isotropic AMM; use the Voigt 0 K speeds (6.63/3.30 at ρ 2.70, or 6.59/3.28 at ρ 2.73).
3. **WE 20.1 numbers all reproduced** (0.158/0.170/0.125/0.136/0.165/0.324), and the general F_meas formula is CHECKED.
4. **Memory-loss times reproduced exactly** by an independent solver (6.81/46.8 ns; 151.7/1037 ns). **20.5 l.89 is
   inconsistent with them** (still says "within about 10 ns and 30 to 100 ns"); SOTA l.540, l.581 likewise superseded.

## 20.1 Charge transport
| location | verdict | note / correction |
|---|---|---|
| l.7 Green reciprocity, Q_s^ind = −qφ_s | CHECKED | Standard; sign consistent with eq:20.1-ramo. |
| eq:20.1-ramo, current I_s | CHECKED | |
| eq:20.1-qpair, worked 2/3 | CHECKED | Electron (−e) +s_e and hole (+e) −s_h both give +e s/d. ½ + ⅙ = ⅔. |
| l.12 "as quoted by Lachish" | GAP (minor) | Lachish 1701.03459 states only the planar form dh = (dx/d)q (Eq. 2), not the weighting-potential theorem. Say "planar form as quoted by", or cite Shockley/Ramo directly. |
| eq:20.1-work, planar eV𝔮 per pair | CHECKED | Σ_k V_kΔQ_k = q[φ_bias(start) − φ_bias(end)]. |
| l.26 Coulomb 1.3e-5 eV, bias work 4 meV | CHECKED | 1.26e-5 eV (ε₀ = 11.4, NOTATION-consistent at mK); 4 V·10 µm/1 cm = 4 meV. |
| l.28 3.82 eV (CDMS) | CHECKED | 1803.02903 footnote 2. |
| l.32 ⟨min(s,L)⟩ | CHECKED | sympy. |
| eq:20.1-hecht, limits | CHECKED | Large-λ: 1 − d/2λ_d. Lachish Eqs. (3)–(4) are images in the PDF; the form is standard. |
| eq:20.1-hecht2, eq:20.1-qavg | CHECKED | sympy: per carrier ½ − X/6 + X²/24 − …, X = d/λ_d. |
| l.49 "a third", L²/2λd, ⟨L²⟩ = d²/3 | CHECKED | |
| l.49 0.632/0.736/0.787; 0.952/0.968 | CHECKED | 2e⁻¹ = 0.7358; 2(1 − e^{−½}) = 0.7869; 0.9516; 0.9675. |
| l.58 Leman Eqs. (24)–(25), k_max ∝ ℰ^{1/3} | CHECKED | |
| lim:20.1a saturation 0.787, deficit 8.9 % at μℰ = 0.1v_sat | CHECKED | 2(1 − e^{−1/2}); 0.1987 vs 0.1811 → 8.85 %. |
| l.71 first-order deficit μℰ/v_sat | CHECKED | |
| lim:20.1b 0.030 / 0.015 | CHECKED | 2X/6 = 0.01; 4X/6 = 0.01. |
| l.88 second order +X²/24, relative X/4 | CHECKED | |
| eq:20.1-Fpos (general measured-charge Fano) | CHECKED | Law of total variance with Var(N_ind given r) = N̄σ_q² + q̄²F N̄, N_eh independent of r. Binomial reduction gives fF + 1 − f (sympy). The assumption "N_eh independent of position" is stated, good. |
| l.99 Bhatia–Davis σ² ≤ q̄(1 − q̄) | CHECKED | |
| lim:20.1c published form, Ramanathan Eqs. (A6)–(A7) | CHECKED | Source: (F n + ηn(1 − η))/(ηn) = F/η + 1 − η, the Fano term unthinned, as the book says. Note: the source calls its form a lower bound; it is an upper bound on exact thinning (book is right). |
| lim:20.1c excess F(1/f − f) ≈ 2F(1 − f); gray f ≥ 0.923 | CHECKED | 0.92342. |
| WE 20.1 binomial 0.158, published 0.170, diff 0.012 | CHECKED | 0.1583, 0.1700, 0.0117. |
| WE 20.1 midplane λ = 4.83d, σ² = 0.0156, F = 0.125 | CHECKED | ⟨min(s,L)²⟩ = 2λ²[1 − e^{−L/λ}(1 + L/λ)] (sympy); 4.8319, 0.01556, 0.1247. |
| WE 20.1 uniform λ = 6.41d; ⟨q̄²⟩ 0.9026; ⟨σ²⟩ 0.0230; Var_z 1.16e-4; 0.1325 | CHECKED | 6.4147, 0.90262, 0.02296, 1.156e-4, 0.13248. |
| WE 20.1 position 1.22e-4 N̄: 0.003/0.033/0.19; totals 0.136/0.165/0.324 | CHECKED | 0.1357, 0.1649, 0.3240. |
| WE 20.1 0.01 at 82 pairs ≈ 0.3 keV; 6e-6 | CHECKED | 82.2 pairs = 308 eV; 6.04e-6. |
| WE 20.1 F_eh = 0.114 | CHECKED (convention) | Consistent with the validated cascade (DC-67 Si F 0.11398; quote DC-67 only via REF-DC-67's textbook list). Editor item stands: 20.5 uses 0.119 (measured); state the convention once in 20.1. |
| l.128 e^{−1.04e4}; Poole–Frenkel 0.45 / 2.25 meV | CHECKED | 2(αeℰ/ε₀)^{1/2} = 0.4496, 2.248 meV. |
| l.128 flashing, Agnese Sect. 2 | CHECKED | 1803.02903 Sect. 2. |
| eq:20.1-dE, sheet changes | CHECKED | sympy: below −σ(d − z₀)/(ε₀d), above +σz₀/(ε₀d). |
| eq:20.1-sheet "which a sheet at a face attains"; l.142 "lower value for a sheet at a face" | GAP | The bound is reached only as z₀ → 0, and then the whole jump sits in the vanishing slab 0 < z < z₀ while the bulk field is unchanged (the charge just images onto the electrode). So 6.3e4 cm⁻² gives a 1 % distortion in no finite volume. Correction: say the bound is approached in a thin slab between a near-face sheet and its electrode. For a distortion over a finite part of the drift region, a sheet at depth z₀ needs 6.3e4·d/(d − z₀) cm⁻² (1.26e5 at the midplane, distorted over the whole crystal). Recast the 5–10 h estimate accordingly (the midplane 10 h is the bulk-relevant value). |
| l.142 1.59e-7 V/cm per e/cm²; 6.3–12.6e4; ×4 at 4 V/cm | CHECKED | 1.5873e-7. |
| l.142 0.127 trapping probability | GAP (minor) | 2303.02196 says "charge trapping (12.7 % probability)" citing its ref. [28], without saying per carrier; "per-carrier … of the dominant sign" is the book's reading. Cite the primary (HVeV CT/II paper) or say "a trapping probability of 12.7 %". Arithmetic 5.2 h / 10.3 h, 19 s / 37 s at ×1000: CHECKED. |
| l.148–eq:20.1-luke derivation (root Q*, |∂/∂Q| = Q*/2m, prefactor (D^n)²m/2πρc, angle integral) | CHECKED | sympy, each step. |
| l.161 claim about Leman Eq. (21)/G4CMP Eq. (8) | CHECKED | Both sources read: Eq. (21) has (k/k_L)¹, Eq. (22) has (k/k_L)² as a rate density. See Summary 1. |
| eq:20.1-Eluke, ⟨u⟩ = ¾(1 − k_s/k) | CHECKED | sympy. |
| l.168 mc² 0.230 meV, l₀ 7.5 µm, c/3l₀ 4.0e8, 2.0e8 s⁻¹, 0.35/0.46 meV | CHECKED | 0.2303 meV; l₀ 7.47 (ρ 2.33) / 7.48 µm (ρ 2.335, Leman Table II lists 7.5); 4.01e8; 2.01e8; 0.345/0.461. |
| l.172 balance (M − 1)⁴/M² = 2eℰl₀/mc² | CHECKED | sympy. |
| l.174 holes 4.3/7.0, 1.2/2.1 meV; electrons 1.1/2.1 meV (mc² 0.120) | CHECKED | 4.32/6.95; 1.15/2.06; e: 1.09/2.05 meV (l₀ 16.4 µm; Leman lists 16.9). |
| l.174 (E_c/E_max)⁴, 0.3 % | CHECKED | 0.0031. |
| l.174 vs DC-83 (VALIDATED, quotable) | NOTE | DC-83 MC: Si e⁻ ⟨E_Luke⟩ = 0.840 meV at 1 V/cm (Si rows within 1.1 % of the earlier run); the book's balance value 1.09 meV is 30 % higher, consistent with its "overestimates" wording. DC-83 quoted ranges 0.75–4.7 (e⁻), 1.1–6.4 (h⁺) meV are consistent. Optional: add the MC value. |
| l.180 "published normalizations differ by k/k_s" | CHECKED | |

## 20.2 Athermal phonons
| location | verdict | note / correction |
|---|---|---|
| l.3, l.7 69 eV, 2300 phonons, 6e11 modes, 4e-9, 0.86 µeV | CHECKED | 2293; 6.28e11; 3.7e-9. |
| l.9 cap 2c_LA k: 8.7 / 6.0 meV | CHECKED | 8.70, 5.96 meV (m_dos 0.321). |
| eq:20.2-fs and l.9 "below about 6 meV" | GAP (minor) | Carriers near ω_opt emit up to 8.7 meV; 6 meV is the cap at mean KE. Say "below about 6 to 9 meV" (fig 20.2 puts f_s on 0.2–6 meV, a model choice). 1.7 %/1.3 %: CHECKED (1.71/1.27). |
| l.14 citation [Table I] of Leman for ω_opt and ε_eh | WRONG (citation) | Leman Table I lists ε_eh 3.81 (Si), 2.96 (Ge) and no optical-phonon energies. 64.1/37.6 meV and 3.75 eV need the book's own sources (Ch5/Ch18). Keep Leman only for Ge 2.96 eV. |
| l.14 N_eh E_g = 31 % | CHECKED | 26.7 × 1.17 = 31.2 eV. |
| eq:20.2-V3 scaling, ω³y(1 − y) | CHECKED | eq:5.7-V3 carries 1/√(8ω₁ω₂ω₃); Q₁Q₂Q₃ ∝ ω³ → ω^{3/2}. |
| l.25 angle integral Q₂/(c₂QQ₁), phase space ∝ ω² | CHECKED | dQ₂/dcosθ = −QQ₁/Q₂. |
| eq:20.2-anh (E⁵ law, priority) | CHECKED | eq:5.7-gamma at T = 0 has no further ω factors: ω³ × ω² = ω⁵. |
| l.32 transverse cannot decay (isotropic) | CHECKED | Triangle inequality argument is correct. |
| l.32 A values: 7.41e-56, 1.15e-55, 1.61e-55, 6.8e-55, 6.43e-55, 1.65e-54 | CHECKED | Leman Table I; Hernandez Table 3 (A, Ac,l); Hertel–Pyle l.82 (credits Msall–Wolfe). Ge 6.43e-55 vs 1.65e-54, both "Tamura": UNRESOLVED without Tamura (closed). The ratio is 2.57, not a 2π-power or a c⁵ conversion I can identify. (The editor note calls this the "Ge isotope constant"; it is the anharmonic constant, s⁴. The book text is right.) |
| l.32 18 ps at 15 THz, 14 µs at 1 THz | CHECKED | 17.8 ps; 13.5 µs. |
| eq:20.2-isoborn (π/6) | CHECKED | Golden rule with N⁻¹Σe e*δ = δ_βγ g_κ/3, ∫g_κ = 3. Matches Tamura. |
| eq:20.2-rayleigh B = 4π³g_md Ω_at⟨c⁻³⟩ | CHECKED | Debye g_κ = 3Ω_atω²⟨c⁻³⟩/2π², ω = 2πν. Hernandez Eq. (4) ✓. |
| l.53 x_L 9.3 % / 9.8 % | CHECKED | Kelsey Sect. 2.2.2. |
| WE 20.2 M̄, g_md 2.007e-4, contributions, 70 % | CHECKED | 28.0855; 1.378e-5, 4.715e-5, 1.398e-4; 69.6 %. |
| WE 20.2 "deviate by −0.39, +3.17, +6.72 %" | GAP (sign convention) | These are (M − M̄)/M̄ = −δ^M; the text (and NOTATION l.883) defines δ^M = 1 − M/M̄. Write "masses deviate from M̄ by …" or give δ^M = +0.39, −3.17, −6.72 %. Harmless (squared). |
| WE 20.2 ⟨c⁻³⟩ 4.90e-12 (C.18 tensor), 4.69e-12 (code), Ω_at 20.02 | CHECKED | Independent Christoffel average 4.9031e-12. |
| WE 20.2 B_iso 2.44e-42 (priority) | CHECKED | 2.4439e-42; inside Tamura et al. measured 2.42–2.56 (Hernandez Table 4 ✓). |
| WE 20.2 Γ 2.44e6, 0.41 µs, 3.9e-7, v_rms 5.85, mfp 2.4 mm, 4e5 λ | CHECKED | |
| WE 20.2 Ge g_md 5.87e-4, B 3.67e-41, ×15 | CHECKED | Hernandez 5.88e-4; Leman Table I. |
| l.63 / lim:20.2b 5.6 meV, 9.6, factor 8.1 at 17.6 meV, PBE ⟨c⁻³⟩ +22 % | CHECKED (vs log) | DOS not recomputed. Internally consistent: 9.57 fit → 10 % at 5.68 meV; at 1 THz +5 %. |
| l.78 B/A 33 / 228 THz; ×3.3 at 10 THz | CHECKED | 32.8; 228.0. |
| eq:20.2-frag (P_d energy-weighted) | CHECKED | Number density 2·30y²(1 − y)², energy-weighted 60y³(1 − y)², ∫ = 1. |
| eq:20.2-Estar, keyresult eq:20.2-scaling (E_* ∝ t^{−1/5}, priority) | CHECKED | sympy substitution reproduces each term with the common factor E_prompt/tE_*. Energy check ✓. |
| l.103 settling 0.19 / 1.3 ns; E_* 44.6/28.1/17.7/11.2 and 37.8/23.8/15.0/9.5 meV; 0.63, 0.92 | CHECKED | 0.191, 1.316 ns; all E_*; 0.628, 0.916. |
| l.105 mean 0.667E_*, median 0.66, 80 % in 0.36–0.97 | CHECKED | Independent solver: 0.6671, 0.664, 0.364/0.971. |
| l.105, lim:20.2a all within 10 % after 0.46 ns | CHECKED | Independent: 0.019, 0.063, 0.48 ns (grid). |
| lim:20.2a Leman Eqs. (6), (8), A, B | CHECKED | |
| l.120 threshold E_* = 0.51–0.53 E_mem | CHECKED | 0.515 (near-top), 0.526–0.527 (band). |
| fig:20-spectrum, l.129 6.8 ns / 47 ns; 0.15 / 1.0 µs (priority) | CHECKED | Independent: 6.81, 46.8 ns; 151.7, 1037 ns. |
| l.129 22 meV TA forgotten near 1 µs | CHECKED | E_* = 0.52 × 22 = 11.4 meV at 0.90 µs. |
| l.129 "times … usually quoted" | GAP (minor) | Uncited; cite or drop "usually quoted". |
| l.129 TV 0.13/0.026/0.015/0.012; 6e-4 above 6 meV | CHECKED, GAP in caption | Reproduced only with LA:TA energy shares 42/64 : 22/64 and Gaussians per ln E (phon20_2.birth_er_si); with equal shares TV(10 ns) = 0.18. State the shares in the fig:20-spectrum caption. |
| l.129 0.01 % below 6 meV (cubic) | CHECKED | 8.6e-5. |
| eq:20.2-Nmix, 164/650; 1300/5100 | CHECKED | Integral ✓; 164, 652; 1274, 5072. |
| l.138 r² = (10/9)v²(xA)^{4/5}t^{9/5}/B; 8.6/68/540 µm; 1.8/15/120 µm | CHECKED | |
| l.138 45 meV: 0.95 ns, 1.4 µm; shell 0.21/1.7/13.5 %; 36 % at 3 µs | CHECKED | Ren et al. 4 mm ✓. |
| l.140 sapphire B, A, B/A 0.02–0.21 THz, 0.025/0.4/16 | CHECKED | Hernandez Tables 3–4 and the "fifth power" remark (p. 6) ✓. |
| keyresult eq:20.2-bound and its proof | CHECKED | Midpoint R₀ ∈ [0, 1]; above-E_mem term ≤ (Δ_h/2)·2. |
| l.156 E_mem 21.6 meV, bound 0.15 vs 0.012; 17.7 meV, 0.026 vs 0.009; 36 % | CHECKED (vs log) | Consistent with the 0.52 rule (11.19/0.517). Priority: the bound reduces to f_s only if every hard birth lies above E_mem; the text says so. |
| Cross-check 20.5 l.89 | WRONG (outside my files; flagged per brief) | It says memory is lost "within about 10 ns and 30 to 100 ns". By 20.2 that holds only for near-top births; for the upper factor-two band it is 0.15/1.0 µs, and for ER's 22 meV TA ≈1 µs. 20.5 also writes f_soft, ω_op where 20.2 has f_s, ω_opt (notation drift). Align 20.5 and the discrimination verdict (l.153). |
| SOTA l.540, l.581 ("≈10 ns / 30–100 ns, ≲ 0.1 mm") | SUPERSEDED | By 20.2: 0.15–1 µs, r_rms 0.54 mm at 1 µs. Campaign "IF-E7 δ_prim ≤ 0.007" (SOTA l.540) and CORRECTIONS l.441 δ_coll^prim ≤ 0.012 differ from 20.2's bound (f_s = 0.017 if the E_mem condition holds, 0.15 for the model births at 1 µs). Log in CORRECTIONS. |

## 20.3 Phonons into films
| location | verdict | note / correction |
|---|---|---|
| l.7 anisotropy 1.56 / 1.22; Voigt Si 9.00/5.40, Al 6.41/3.11 | CHECKED | 1.563, 1.223; 8.995/5.404; 6.409/3.112 (room-T C.18/Kittel Al). |
| eq:20.3-Qz, eq:20.3-SH, critical angle | CHECKED | Independent SH solution agrees. |
| l.25 σ_zz, σ_xz, eq:20.3-b | CHECKED | |
| eq:20.3-flux; flux closure ≤ 3e-11 | CHECKED | My solver: ≤ 5e-15 at 500 angles. |
| l.37 0.99; > 0.98 to 70°; < 0.9 beyond 78°; SV 0.036 at 30°, max 0.19 near 76°; 0.96 | CHECKED | 0.9909; 0.990 at 70°; 0.900 at 78.28°; 0.0356; 0.193. |
| l.37, fig:20-amm critical angles 36.9, 57.5; 20.2, 29.0, 35.2, 45.4; 0.30 at 45.4° | CHECKED | 0.3018. |
| l.46 8.0/3.9 nm at 0.8 THz; 0.107 THz; 0.087 THz | CHECKED | Martinez Sect. V 0.7–0.9 THz ✓. |
| eq:20.3-count, eq:20.3-avg weights | CHECKED | d²Q_∥ = (2πω²/c²) sinθ cosθ dθ. |
| S-matrix argument, keyresult eq:20.3-recip (priority) | CHECKED | Independent averages satisfy it to 4e-14 (all Al sets). |
| l.78 𝔫 0.0808/0.231, 0.350, t̄ 0.934/0.327; 2.9; 0.669, 0.895, 0.598; 0.977/0.892/0.960; 1.06 | CHECKED | 0.9338/0.3269; 2.856; 0.6685, 0.8946, 0.5980; 1.055. |
| eq:20.3-dmm 0.741/0.259 | CHECKED | |
| lim:20.3a 1.175–1.273; 7.1 %; ×3.03 (priority) | CHECKED | t(0)/t̄_esc = 3.031. |
| l.99 6 % above 0.934; 0.347 within 6 % | CHECKED | 1.061; 0.3469. |
| eq:20.3-pabs-theta, 2E₃, eq:20.3-pabs, thin limit 4d/(𝔩t̄) | CHECKED | 2E₃(y) = 1 − 2y + O(y² ln y). |
| escape-rate derivation, keyresult eq:20.3-tl (priority) | CHECKED | Nc/4 flux; N_ν ∝ c⁻³ → Σc⁻²⟨t_ν⟩ = 𝔫_f t̄_esc. |
| l.132 P_abs ≃ t_l/t_pb | CHECKED | |
| l.134 lumped form, G4CMP Eq. (17); 10 % for d/𝔩 < 0.074; up to 14 % | CHECKED | Source: exp(−2·2d/λ), escape on first return. 0.0738; 13.5 % at 0.235. |
| l.134 "a thin film absorbs 1/t̄_esc = 3.06 times more" (priority) | CHECKED, GAP | Exact only as d_f/𝔩_f → 0 (3.054 at 1e-4). At the WE's 𝔩_f = v_s t₀ (d/𝔩 = 0.070) the factor is 1.91; at the fitted 𝔩_f/d_f = 26 → 9 it is 2.24 → 1.65. With 0 K Al: 2.72 thin, 1.79 at the WE. Add "in the thin-film limit" and give the factor ≈1.9 at 60 nm. |
| WE 20.3 Σc⁻² 0.2309, Σc⁻³ 0.0702, v_s 3.29; 0.606/0.270/0.318; t_l 0.223/0.281 ns; 1.26; 0.86/1.08; 0.855 µm, y_f 0.140, 0.467 vs 0.462 | CHECKED | All reproduced. |
| WE 20.3 t₀ 0.26 ns, Guruswamy p. 2 | CHECKED | 1401.1937 p. 2: τ₀φ = 0.26 ns (its ref. 10). |
| l.148 Martinez setup | CHECKED with nit | 380 µm is P1; P4 sits on 300 µm (Sect. III). T is absorption on crossing, no film propagation (Sect. IV ✓). |
| eq:20.3-Tfit inversion: P_abs 0.321–0.589; 𝔩_f/d_f 25.8–9.1; 1.55–0.54 µm; t_pb 0.47–0.17 ns; specular 1.43–0.50; DMM 1.36–0.36; 0.105–0.193 | CHECKED | All reproduced (DMM specular low end 5.6 d_f). |
| l.153 "constrains 𝔩_f/d_f ≈ 6–26, says little about the interface" (priority) | CHECKED, refine | Sound, for a reason worth stating: in the thin limit T_fit → t̄_SiAl·4d/(𝔩t̄_esc) = (𝔫_Al/𝔫_Si)·4d_f/𝔩_f for any energy-conserving interface, by eq:20.3-recip. At the fitted P_abs (0.3–0.6) finite-y corrections leave an AMM/DMM spread of 12 % (T = 0.30) to 33 % (T = 0.55). The constraint depends on the film speeds through 𝔫_Al: with the 0 K set the range becomes 5.1–23.1 (diffuse), 4.8–21.5 (specular), so ≈5–23. |
| l.153 Leman 33 % a-Si/Al, Sect. III G | CHECKED | 1109.1193 l.676. |
| l.157 Si [100]/[111] speeds; t̄_esc 0.291/0.360; t_l 0.251/0.203 ns; t̄_SiAl 0.925–0.937 | CHECKED | 0.2911/0.3594; 0.2506/0.2030. |
| l.157 texture ≤ 3 % (6.29–6.49) | CHECKED | |
| l.157 0 K Al: Malica–Dal Corso Table 2 (114.3, 61.9, 31.6) | CHECKED | Row "Expt.m", Kamm–Alers extrapolated to 0 K. |
| l.157 0 K → 6.63/3.30, t̄_esc 0.368, t_l 0.187 ns, −16 % | CHECKED | At ρ = 2.70. See §20.3-Al for the ruling. |
| l.159–163 quarter-wave t_min, SiO₂ 5.80 km/s, 12.8e6; 0.855 at 0.72 THz (2 nm); 0.907 (1 nm, 0.8 THz) | CHECKED | Full transfer matrix: 0.8553, 0.9073. |
| l.163 "spread 0.259–0.327, factor 1.26" | CHECKED (room-T); update | 0 K Voigt: 0.282–0.368, factor 1.31. |

### §20.3-Al: room-temperature vs 0 K aluminum (ruling R, CORRECTIONS §19.13(g), l.638–640)
Independent AMM; Si Voigt (9.00/5.40, 2.33) throughout; d_f = 60 nm; t₀ = 0.26 ns.
| Al set | c_LA/c_T (km/s), ρ | t̄_Si→Al | t̄_esc AMM / DMM | v_s | t_l AMM / DMM (ns) | t_l/t₀ | 1/t̄_esc | T crit. angle, trapped flux |
|---|---|---|---|---|---|---|---|---|
| C.18 room T (now in text) | 6.41/3.11, 2.70 | 0.934 | 0.327 / 0.259 | 3.29 | 0.223 / 0.281 | 0.86–1.08 | 3.06 | 35.2°, 0.598 |
| 0 K Voigt (recommended) | 6.63/3.30, 2.70 | 0.938 | 0.368 / 0.282 | 3.50 | 0.187 / 0.244 | 0.72–0.94 | 2.72 | 37.7°, 0.557 |
| 0 K Voigt, ρ(0 K) | 6.59/3.28, 2.73 | 0.938 | 0.364 / 0.279 | 3.48 | 0.190 / 0.247 | 0.73–0.95 | 2.75 | 37.4°, 0.561 |
| Ch15 [100] speeds (do not use in an isotropic AMM) | 6.47/3.40, 2.73 | 0.942 | 0.387 / 0.291 | 3.61 | 0.172 / 0.229 | 0.66–0.88 | 2.58 | 39.0°, 0.531 |
Changes, room T → 0 K Voigt: t̄_esc +12.5 % (AMM), +8.6 % (DMM); t_l −16 % (AMM), −13 % (DMM); AMM/DMM t_l ratio 1.26 → 1.31;
the fitted 𝔩_f/d_f 6–26 → 5–23. ρ (2.70 vs 2.73) moves everything by ≤ 1.6 %. Recommendation: rewrite 20.3 with the 0 K Voigt set
as primary (ρ_T = 2.70 for the impedances, consistent with "rates keep 2.70", CORRECTIONS l.640). Keep room T as the
sensitivity. Propagate t_l/t₀ 0.72–0.94 to 20.4/20.5, and 37.7° (trapped share 0.557, i.e. "56 %") to E.25 (its 34.9° and the
"60 %" in 20.3 l.132, l.159). In the WE, 𝔩_f = v_s t₀ becomes 0.909 µm, y_f 0.132, P_abs 0.422 against t_l/(t_l + t₀) = 0.418.

## Notation / convention drift (against NOTATION)
- t_pb, 𝔮 (with q̄, σ_𝔮²), ξ_SC, y_f, T_fit, P_abs(θ), 𝔫_f, n_sh, ρ_tr, p_tr have no NOTATION rows (20.1/20.3 first uses). Add them.
- x_L (20.2, longitudinal share) also appears in the 19.3 row (Lindhard continuation coefficient): two meanings of one glyph. Flag.
- ε₀ = 11.4 (mK) in 20.1: consistent with NOTATION l.493 (mK use is listed for 18.5; extend the row to 20.1).
- δ^M sign in WE 20.2 (above).
- 20.5 f_soft, ω_op vs 20.2 f_s, ω_opt (NOTATION row f_s, l.1288).
- No factor-of-2, π or sign drift found in the 20.1–20.3 formulas themselves. h vs ħ (E_ath/h as a frequency in Hz) is used
  consistently with E.12. Γ_L vs g_Luke is distinct, per NOTATION l.1458.

## Campaign returns / corrections
- CORRECTIONS l.345 (CW6): AMM 0.32, DMM 0.26, ×1.26, "constrains λ_pb/d": consistent with 20.3 (room T). The campaign's
  "a_opt ≈ 0.14–0.38 at 60 nm" (in-film optical depth) does not map onto the book's numbers: 4d_f/𝔩_f = 0.155–0.44 (AMM),
  0.18–0.66 (DMM); y_f = half of these. Do not quote a_opt. With 0 K Al all of these shift (above).
- CORRECTIONS l.656, l.657 (𝔯_coll) concern 20.5: not checked here.
- DC-RESULTS: DC-83 (Luke energies) compared above; DC-67 F_eh consistent (quote only via REF-DC-67). No other DC row bears on 20.1–20.3.
