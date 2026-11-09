# CORRECTIONS: index of owed corrections, per return and per site (NOTATION-APPLY, 2026-10-31)

**Read this before quoting any return.** Returns are the historical record and are never edited. Each item below is owed, not
executed. Types: **S** substantive (a formula, factor or claim changes), **N** notation rename (CONVENTIONS/NOTATION v3), **W** wording
or scope. "Found by" names the return or referee that found it. Status of substantive claims stays in state/SOTA.md; this file only routes.
Label citations use the return prefix (CONVENTIONS §14).

## 0. Global renames (apply to every return where the left-hand symbol appears)
| Old (in returns) | New (v3) | Where it occurs |
|---|---|---|
| χ, χ⁰, χ_ee, χ_KS (response); Π (D2 density polarisation) | R, R⁰, R_ee, R⁰; R̃ | D1, D2, X2 |
| Q (ionization yield), P(Q\|q,ω) | N_eh, P(N_eh\|q,ω) | L21 sources, SOTA (O4 entry, coordinator note), O4 §6 d11 |
| G (Theorem D ground sector), S^G | GS, S^{GS} | W0, W2, W3, W5 |
| X (ladder rung), Δ_X | 𝒳, Δ^τ_𝒳 | W0, W1, W6 |
| "Debye–Waller" for the Allen–Heine tadpole; H_DW, Σ^{DW}, g^{DW} | AH tadpole; H_AH, Σ^{AH}, g^{AH} | D1 §5.3, D2 §1–§3, W3 §5 (source quotes) |
| c, c_s (sound speed) | c_ν | X1, W0 (4.9), RA, RB |
| v_n, v_c, v_v (band group velocities); P_n | v^g_n; p_{nn} | X1, D2 C7, RA, RB, W3 |
| A (translation generator) | 𝔄 | D1, X1, X2, RA, RB |
| v_k, v_q, v_p, v(P) (Coulomb) | v_C(k) | W0, W4, W5, X2, D2 |
| a_{Qν} (phonon), A_{Qν} = b + b† | b_{Qν}, B_{Qν} | D1, W2; D2 |
| κ (Sommerfeld arg., background dielectric, mixing, cumulants) | ζ_S, ε_bg, κ_mix, 𝔨_m | W1, W4, W0/W3, W2 |
| Λ (Dirac cutoff), Λ_f (X2 pair correction) | Λ_D, r^{pair}_f | W4, X2 |
| W (screened interaction), W_e(q), W(ε), W ≈ 12 eV | W^{scr}, E^{Mig}_1(q), σ²_strag, B_h | X2, W5; W3; W5; W5 |
| ε_M (macroscopic / Mermin), ε_L (Lindhard) | ε_mac / ε_Mer, ε_Lin | W1 / W4 |
| Δ (SC gap, Dirac gap, scissor, charge gap, detuning, denominators, Δ_κ(q), Δ₀, Doppler) | Δ_BCS, Δ_D, Δ_scis, Δ_Mott, δω, d_{A,m}, δρ_κ, δ_v,0, σ_ω | W4, W1, O4, D1/D2, W2, W6 |
| M¹_ab, M³_ab, M₁^{SB} (moments) | 𝓜¹_ab, 𝓜³_ab, 𝓜₁^{SB} | W0, D2, W3 |
| ε_e, ε_h (carrier energies, WP0 §7.1) | E_e, E_h (ε_e stays the electron-channel dielectric) | W0 §7, W5 |
| n_s, n_e (number densities) | 𝓃_s, 𝓃_e | W0, W3 |
| τ_e; τ_ph, τ_g | 𝒯_e; t_ph, t_g | W0, W3 |
| O_i, O₁…O₁₅ (Fitzpatrick) | 𝒪_i | W0, W1, W4 |
| C1 (O4 convention) | DC (Dyson convention) | O4, SOTA O4 entry |

## 1. R1 / D1
| Site | Correction | Type | Found by |
|---|---|---|---|
| §2 eq. (3) isotropic reduction | 𝒢 = η(v_min)/(2q), not η/q; prefactor ρ_χσ̄_e/(4πm_χρ_Tμ²), not 1/(2π) | S | RA §1; WP0 (9.1); audit A1–A2 |
| §2 crystal form factor | |f_cr|² prefactor 2π²/(αm_e²Ω), i.e. |f_crys|² = Ωq³S̄/(4παm_e²) (not 2πα); the Essig comparison was contaminated by the factor 2 | S | RA §1; WP1 [E12]; audit A5 |
| §5.1 resonance bound | |d| ≥ min(E_min(q) − ω, E_g − ω_max), not E_min(q) − ω | S | RA §2, RB 2b |
| §4 adiabatic error scale | δ = min(E_min(q) − ω, E_g − ω_Q); "standard DFPT gives only path B" holds for the Sternheimer output only (∂V_SCF gives all g) | S/W | RA §6, RB §6 |
| §5.2 linewidth split | Hadamard finite part fp(1/Δ²), not a principal value | S | RA §7, RB §7 |
| §5.3, §6.2(b) | "sideband weight compensated" → first moment only; "DW" = e^{−2W} only; the AH shift is not DW | W | RA §3, RB 3c |
| §6.1 C1 | derivation divides by zero on intraband m = v, c terms (result right); restore i[g, q·r] in step 3 | S | RA §9, RB §9 |
| §6.2 C7 | iℓ_Q(û·q)ρ_cv is wrong; superseded by X1 C7a–e | S | RA §4, RB §4, X1 |
| §3 screening | "every Coulomb line carries q or Q" is false (pair channel); use X2 (2.2); H2 redundant in the window | S | RA §5, RB §5, X2 |
| §7 recipe | Bethe-ridge out-of-manifold remainder for ρ and g with redone cost; PAW augmentation at all q; Si quadrupoles in g; one gauge U(k) for g and F; nonlocal f-sum for C4 | S | RA §10, RB §10 |
| N4–N6, §3 | χ → R; Δ_{A,m} → d_{A,m}; a → b; D(λ) → ρ_cv(λ_fd); 𝒢 keeps its name (= f̂^{(0)}/q) | N | v3 |

## 2. R1 / D2
| Site | Correction | Type | Found by |
|---|---|---|---|
| code/D2/identities.py check (3) docstring | spin factor 2 missing (πe²/q²V → 2πe²/q²V) | W | RA §1, RB §1 |
| §2b window criterion | misses the hole-path (B, m occupied) resonance, a generic first-order transition; use D1's E_min(q) | S | RA §7, RB §7 |
| §2c item 4 | unrestricted band sum in the third-order δρ^V is unproven → [C] or Kubo form | S | RA §2, RB 2c |
| §3 "cutting pair" | per-diagram claim unproven; only SE-p + SE-h + V together are first-moment neutral; "mainly g_cc − g_vv" is [E] | S | RA §3, RB 3b |
| §4b two-class screening | pair channel omitted; use X2 (2.2) | S | RA §5, RB §5, X2 |
| §6 C7 | iu^{zp}·(q − m_eΔv)ρ_cv holds only at Q ≡ 0 (= X1 C7e); physical limit is X1 | S | RA §4, RB §4, X1 |
| §6 C8 | flag restricted to m_χ ≈ 0.4–0.9 MeV with folded q (Umklapp ZPL at q ≈ G₁₁₁) | S | RA §8, RB §8 |
| §6 C1 | nonlocal caveat wrong in kind: exact with the generalised current incl. [g^{NL}, q·r]; write q̂ before the cubic ε^L = ε^T step | S/W | RA §9, RB §9 |
| §6 C5 | absorption threshold E_g − max_ν ω_{Q*ν} at the connecting Q* | W | RB §10 |
| §0, §2 | state e_{κν}(−Q) = e_{κν}(Q)*; non-degeneracy hypothesis unnecessary for orthogonality | W | RB §1, §7 |
| §5 | GaAs ε_ion ≈ 10⁻³ absolute (≈ 10⁻⁴ relative), not 10⁻³–10⁻² | W | RB §5 |
| §0–§2 | χ → R, Π → R̃; A_Qν → B_Qν; b stays; M^{(2)} carries 1/√N (= M_D1/√N); H_DW, Σ^{DW} → H_AH, Σ^{AH} | N | v3 |

## 3. R2 / REF-A and REF-B
| Site | Correction | Type | Found by |
|---|---|---|---|
| REF-B §1 last paragraph, "D1's η/q angular average … verified ✓" | wrong: the correct factor is η/(2q) (REF-A §1) | S | this pass, audit A1 |
| REF-A §5 proposal ε(q, ω∓ω_Q) | exact only for the convective (rigid) component; general screening is X2 (2.2) | S | X2 §5 |
| REF-A/REF-B §4 sympy notation | c, c_s, c_ν → c_ν; A → 𝔄; v_n → v^g_n | N | v3 |

## 4. R3 / X1
| Site | Correction | Type | Found by |
|---|---|---|---|
| §9 "screening aside" | resolved by X2 (pair channel) | W | X2 |
| §5 C7, (X1) | adopt verbatim with ℓ_Q N-outside, index order Q̂·Ξ·ê, upper sign = emission of −Q | W | WP3 §3 |
| throughout | η (|Q| scale) → |Q|; c → c_ν; v_n → v^g_n; P_n → p_{nn}; S, s → 𝔖, s^W; K_± → K^{soft}_±; R1–R3 → X1-R1…R3; "(W)" → X1 (W) | N | v3 |

## 5. R3 / X2
| Site | Correction | Type | Found by |
|---|---|---|---|
| (2.2) external weight Σ_G(ε̃^{-1})_{G0}ρ(q+G) | equals WP1 [E2]'s (1+Rv)_{0G} only for R_{GG′} = R_{G′G} (TR + inversion); in GaAs the index/conjugation convention must be reconciled with WP0 (3.2) ordering | S (open) | this pass, from WP1 D6 |
| §6 δ_pair sign, coherence bound, q-independence | remain [C]; interim factor [0.5, 1.2] stands until X2-N2/N3 [SUPERSEDED: [0.4, 1.8] (WP3-v3, R8); under rebuild in the book Ch13 review, ruling R2] | W | X2, W3 |
| throughout | χ_KS, χ → R⁰, R; W → W^{scr}; Λ → r^{pair}; η → c_coh; T_G → 𝔗_G; D_f → δM^{intra}_f; K → f_Hxc; τ_κ → r_κ | N | v3 |

## 6. R4 / WP0 (the owed erratum; all CLAIMED pending R×2)
| Site | Correction | Type | Found by |
|---|---|---|---|
| (1.2) hyperfine | H_FC = +(2/3)g_eμ_Bg_Iμ_N s·𝐈δ³ = +(1/3)…σ·𝐈δ³; WP0 is 2× too large; sign + with g_I signed | S | WP4-D1, audit A18 |
| (1.2) relativistic f-sum | SOC and Darwin give zero; only mass-velocity: −(5/3)⟨T⟩/m (WP1 [E11]); sizes (Zα)² = 0.055 Ge 1s, ~10⁻³ Ge 3d | S | WP1-D2, D3 |
| (4.6), (5.3) commutator | [T, n] = q·j exactly; drop "(q²/2m_s)n_s" (no effect on the f-sum) | S | WP1-D1, audit A13 |
| (4.9) soft limit | incomplete (misses Galilean p_{nn} terms; equals X1 only at band extrema); ℓ_Q has N inside (M_WP0 = M_X1/√N); replace by X1 | S/N | WP3-1 |
| (5.3) screening of non-density operators | j_T is screened through local fields; spins at SOC = 0 are xc-renormalised by f_xc^T | S | WP1-D4, D5 |
| (5.3) "Z*/ε∞ vertex for LO phonons" | for nucleon coupling the external vertex stays A_κ; Z*/ε∞ belongs to charge coupling | W | WP2-C1 |
| (5.6) uses D2-normalised M; (5.7) | (5.7) is X2 (2.2) truncated (G = G′ = 0, resonant pairs, off-shell M); use X2 | S | WP3-2 |
| Table 6.1 x_coh, K label, 2W | x_coh is not the coherence control (use n_ph and the shell parameter); "coherent 1-ph (x_R ≪ 1)" conflates; 2W = q·B·q in general (isotropic only for cubic sites); new K labels in CONVENTIONS §11 | S | WP2-D1, D2, D3 |
| Table 6.1 row "1/S, Δ/E_F" | controlling parameters for SC and magnets listed in WP4-D4 | W | WP4-D4 |
| §6.2 (H2) | fails for every gapless target (metals, SC, semimetals); state the scope | S | WP4-D2 |
| §6.2 (i) | per-sector PSD only inside the window or for bins ≳ δ; Z may exceed 1 | S | O4 §9 |
| §6.2 (iv) | replace [C] by O4 (iv′)/(iv″) with the DC convention and conditions d1–d11 | S | O4 |
| §6.2 (ii)/L7a boost mass | M vs m_A: the difference is the drag mass δM_κ | W | WP3-5 |
| sector dictionary S_eκ X+ | "dark photon only" → any 𝔇 with c_ec_κ ≠ 0; X-sector ω_e moment fixed and negative (WP3 J7) | S | WP3-4 |
| §7.1 plasmon label | within RPA Λ = cvk only (plasmon decay products are already the pairs) | S | WP5-3 |
| §7.3 first formula | multi-operator weight tr[𝔇S(Λ)]/tr[𝔇S] | S | WP5-2 |
| §7.3 second formula | q integrated before seeding; replace by WP5 (W6) (𝔇 trace and q integral inside the Λ sum) | S | WP5-1 |
| §7.3 last sentence | R&K is a photon-seed fit, not the Λ-marginal of the DM seed | W | WP5-4 |
| §7.2 weight (ε^{-1})_{G0} | general weight (1+Rv)_{0G} (non-centrosymmetric targets) | S | WP1-D6 |
| (8.1) additive Gaussian | violates positivity; use WP6 M/A/E/Δ types | S | WP6-W2 |
| (8.2) f-sum constraint | ∫_ℝ ωS = π𝓃_eq²/m_e (not 2π…), integral over negative ω at T > 0; vacuous for conserving truncations | S | WP6-W1, W3; audit A12 |
| (8.3) theory band | envelope vs profile differ at O(δ) vs O(δ²); report WP6's three objects | S | WP6-W4 |
| (9.1) hypothesis | "isotropic f_χ" → angle-averaged S (hypothesis (I)); formula right | W | WP6-W5 |
| (9.3) L7d | "it is X0, not X+" → n = 0 term X0, n ≥ 1 terms X+ | S | WP3-3 |
| (9.3) L12 | "ZG = stochastic evaluation" → deterministic one-shot quadrature of Williams–Lax | W | WP3-6 |
| (9.3) L15, L16 pointers | conserving GRPA, not "RPA with coherence factors"; include the remote-band background ε_bg in the total ε | S | WP4-D3, D5 |
| (9.3)/(4.3) "L odd in ω with inversion or TR" | flag the converse: P- and T-broken targets have nonreciprocal S and a v-odd rate (add to L19) | W | WP4-D6 |
| §10 | symbols superseded by NOTATION v3 (G → GS, X → 𝒳, ψ (species) → s, a/b Cartesian → α/β, v_k → v_C, τ_e → 𝒯_e, M¹ → 𝓜¹, ε_e/ε_h carriers → E_e/E_h, c_s sound → c_ν) | N | v3 |

## 7. R5 / WP1
| Site | Correction | Type | Found by |
|---|---|---|---|
| [E1], [E2] | (ε^{-1})_{G_qG_q}(q_r,ω) ≡ WP0's (ε^{-1})_{00}(q,ω) (CONVENTIONS §2) | W | v3 |
| §12 table | κ (Sommerfeld) → ζ_S; W̄_l → 𝒲̄_l (per spin); ε_M → ε_mac; E_b → E_x^b; S_F → 𝒮_F; T_ℓm → S_ℓm; F(q) → w_pl(q); K_ℓ → K^cub_ℓ; Ξ (BSE kernel) → Ξ^{BSE}; Δ_sc → Δ_scis; C1–C8 → WP1-C1…C8 | N | v3 |
| §3.4, §12 v_max | 544 + 250 = 794 km/s: valid as v_max^ref (CONVENTIONS §8) | W | v3 |
| §6.2 2607.06005 "dipole" claim | needs the full-text double check at referee stage (SOTA) | W | SOTA |

## 8. R5 / WP2
| Site | Correction | Type | Found by |
|---|---|---|---|
| §14 flag "NOTATION ρ_χ = 0.4" | resolved: NOTATION v2/v3 have 0.3 | W | v3 |
| §5.2 G/X split of κ₃ | needs WP3 confirmation against its Migdal spectra (WP2 gap 7): OPEN | W | WP2 |
| throughout | k_i (phonon) → Q_i; ℓ (cell) → R; L → ΔR; κ_m → 𝔨_m; n_κ(p) → 𝔫_κ(p); K_q̂ → E^kin_q̂; μ_κ → w_κ; ρ_κ(ω′\|…) → ρ^{ph}_κ; Σ_ν → Π^{ph}_ν; J_κ (spin q.n.) → 𝒥_κ; c_κ → x_κ; g_κ → h^I_κ; σ_ℓκ → o_{Rκ}; s_i → s^{ph}_i; Q_κ → 𝒬_κ; Δ_κ → δρ_κ; D_A, D_NA → D^{dyn}; ω_L (Larmor) → ω_Lar; g(q,ω;x) → 𝒢; S^G → S^{GS}; Q_χ → e_χ; f_κ(q) ≡ c_κ; Δ (Doppler) → σ_ω; K₃, K₄ → 𝒞₃, 𝒞₄; C1–C9, D1–D4 → WP2-… | N | v3 |

## 9. R5 / WP3
| Site | Correction | Type | Found by |
|---|---|---|---|
| (W.4c) "S^{X+} = (2q²/e²)L^{PA}" | at T > 0 divide by (1 − e^{−βω}) (immaterial for T ≪ E_g) | W | v3 |
| (W.5) | inherits the X2/WP1 external-weight caveat for non-centrosymmetric targets (§5 above) | S (open) | this pass |
| throughout | S (exciton), Ω_S, A^S → λ, E_λ, A^λ; 𝒢_{SS′ν} → g^x_{λλ′ν}; χ_f → Ψ^{vib}_f; W_e(q) → E^{Mig}_1(q); n(ω) → n_r(ω); A_f → A^{Mig}_f / A^{PAER}_f; α(ω) → α_pol(ω); k (W.5 loop) → p; U_κ(p) keeps its name; C1–C10, N1–N5, T0–T6, (W.n) → WP3-…; τ_e → 𝒯_e; n_e → 𝓃_e | N | v3 |

## 10. R5 / WP4
| Site | Correction | Type | Found by |
|---|---|---|---|
| §2.1 halo values quoted from 1905.13744 | source conventions, not campaign (§8 of CONVENTIONS) | W | WP4 |
| §5 L16 κ² claim against 1708.08929/1910.02091 | HIGH-PRIORITY referee check against full text before any claim (SOTA) | W | SOTA |
| throughout | Δ → Δ_BCS / Δ_D; Δ_c → Δ_Mott; u_k, v_k → u^B_k, v^B_k; U, V → U^B, V^B; λ (hybrid) → h; g_I, g_II → 𝔤_I, 𝔤_II; E^b_ν → ℰ^α_ν; F_j → F^{mag}_j; J_ij → J^{ex}_ij; κ → ε_bg; Λ → Λ_D; g (Dirac) → g_deg; s → 𝓈; 𝐠, γ(ω) → 𝐛_NR, γ_OA; γ, ℓ, D → γ_rel, ℓ_mfp, D_diff; ε_M, ε_L → ε_Mer, ε_Lin; E_b (donor) → E_b^D; S_k → S_HR,k; S_C, ζ → 𝒮_F, ζ_S; η (Dirac Sommerfeld) → ζ_S; η_esc → t_esc; μ_e → 𝛍_e; W (quoted ELF) → L; K1–K10, D1–D6, RG1–RG8 → WP4-… | N | v3 |

## 11. R5 / WP5 (no symbol table in the return; renames listed here)
| Site | Correction | Type | Found by |
|---|---|---|---|
| — | add the mandatory "Symbols introduced/used" table at the next revision (RULES) | W | this pass |
| (W1), §1.1(d) | W → W^{scr}; v_p → v_C(p) | N | v3 |
| (W3)–(W5) | G_x(s), s → 𝔊_x(ϑ), ϑ; K_c → 𝒦_c; generation g → n_gen; H (heat) → ℋ | N | v3 |
| (W8), (W9) | P(E) → dE/dt\|_ph; g_κ(ω′) → D_κ(ω′); σ_ω kept | N | v3 |
| (W11), (W12) | Q_h → Y_H; E_b, g(E_b), k_ij, T_c, n_i, S_i, S_inst → E_bar, 𝒩_b, Γ_ij, T_×, N_i, 𝔰_i, 𝒮_inst | N | v3 |
| (W13), (W14), §6 | η (pair-breaking) → η_pb; η (detection) → ϵ_det; η̄ → E_el; ε → ε_eh; ε_γ → ε_eh^γ; D → 𝔡_H; F → F_eh; b → b_N; ε (Lindhard) → 𝓔_red; k → k_L; W(ε) → σ²_strag; W ≈ 12 eV → B_h; ξ (Massey) → ξ_Mas; S_e → S^{stop}_e; p_n → P_n; Φ_t → 𝒰_t; C1–C10, R1–R6, (W1)–(W24) → WP5-… | N | v3 |

## 12. R5 / WP6 (no symbol table in the return; renames listed here)
| Site | Correction | Type | Found by |
|---|---|---|---|
| — | add the mandatory "Symbols introduced/used" table at the next revision (RULES) | W | this pass |
| §7.3 τ string `nT=130K` | n_T is a thermal order; temperature goes to metadata: `nT=0` + `T=130K` (CONVENTIONS §11) | S (format) | this pass |
| §2.3 (V4), §2.5 D3, §9 N1 | v_E: integrals use v_E(t); reference scalar v_E^ref = |v_⊙| = 250.5 km/s; 252.1 km/s (annual mean) enters the halo band | W | this pass |
| §9 N1 ρ_χ flag | resolved: 0.3 | W | v3 |
| throughout | v_⊥ → v_T; u_∥ → v_∥; δ, Δ₀ → δ_v, δ_v,0; K → N_esc; A₀, A₂ → A^{(0)}, A^{(2)}; p → p_on; ν_e → θ^{det}_ex; ρ_mat → r_mat; r_k → r^M_k; k (tail) → k_tail; ε → ε_eh; X → 𝒳; C1–C12, D1–D6, W1–W5, N1 → WP6-… | N | v3 |

## 13. R5 / O4
| Site | Correction | Type | Found by |
|---|---|---|---|
| §3 (vi) "each m keeps its weight" | scope: holds for the Fan Z-part per pair; the vertex term Re Υ changes \|ρ^{ren}\|², so there is no global zeroth-moment rule for n_e (REF-B, WP3 J4) | W | this pass |
| §5, §6 d11 "P(Q)" | P(N_eh\|q,ω) | N | v3 |
| throughout | C1 → DC; m, f → Λ₀, Λ₊; λ_f, Υ_m → a^{off}_f, Υ_Λ₀; ρ̃ → ρ^{ren}; Δ → δω; φ → w_test; 𝒜(ℓ), ℓ → 𝒞_adm(ℓ_win), ℓ_win; K_{m→f} → 𝒦; \|s⟩ → \|src⟩; V → V_ep; P → PV; T0–T5, S1–S4, d1–d11 → O4-… | N | v3 |

## 14. literature/L1.md
| Site | Correction | Type | Found by |
|---|---|---|---|
| §2(c), §3 | "Q" step model → N_eh^{step}; EPW "q" (phonon) → Q | N | v3 |
| §2 context computation, v_max ≈ 794 | consistent with v_max^ref = 794.5 | W | v3 |

## 15. state/SOTA.md (owed edits; the coordinator applies them)
| Site | Correction | Type |
|---|---|---|
| coordinator note on O4 and O4 entry: "P(Q\|q,ω)", "P(Q)" | P(N_eh\|q,ω) | N |
| R5 O4 entry "(iv′) Convention C1" | DC (Dyson convention) | N |
| Theory row 11 (C7) | SUPERSEDED by X1 C7a–e (R3) | W |
| Amendments owed: "NOTATION S provisional" | confirmed (WP0 (3.1), v3) | W |
| Amendments owed: "CONTROLS C7 … AMENDED" | SUPERSEDED (REF verdict FALLS, then X1) | W |
| Amendments owed: "C1 prefactor from memory" | closed in full text (WP3) | W |
| R5 WP6 "Convention flags" and WP2 flag on ρ_χ | resolved (CONVENTIONS §8) | W |
| new | add pointer: "Read state/CORRECTIONS.md before quoting a return" | W |

## 16. Campaign files (owed edits by the coordinator)
| File / site | Correction | Type |
|---|---|---|
| CONTROLS.md C7, last sentence "A uniform rigid shift … M^{(2)} → 0 as Q → 0 for acoustic branches" | contradicts C7a–e (the limit is the X1 soft factor, not 0); delete | S |
| CONTROLS.md C4 "compensated by Debye–Waller / renormalisation of the zero-phonon weight" | "first moment compensated by the Fan + vertex non-phonon cuts; DW = FC e^{−2W}" | W |
| LIMITS.md L2, L3, L6, L7d, L8, L9, L12, L15, L16 | apply the WP0 §9.3 ✎ pointers as amended in §6 above (L7d split, L12 ZG deterministic, L15 GRPA, L16 ε_bg) | W |
| LIMITS.md L1, L4, L5, L6, L9, L13, L15, L16, L17, L18, L19, L20–L24, L7a–d | status OPEN → DERIVED/CLAIMED per the R5 returns (pending R×2) | W |
| README.md | add CONVENTIONS.md and state/CORRECTIONS.md to the table | W |

## Coordinator additions after NOTATION-APPLY (2026-10-31)
- CONTROLS C7: the leftover sentence "M^{(2)} → 0 as Q → 0" was DELETED (it contradicted C7a–e). APPLIED.
- REF-B (R2) §1 wrongly verified D1's η/q. The correct factor is η/(2q) (REF-A, WP0 9.2, WP6). Readers of REF-B route here.
- OPEN, must be resolved in REV-WP1 and REV-WP3 (and checked again in R7): in non-centrosymmetric targets (GaAs), X2's external weight (ε⁻¹)_{G0} and WP1's (1+Rv)_{0G} disagree. Decide whether the difference is physical or a convention, with a derivation.
- O4: narrow the zeroth-moment statement's scope to the Fan part (REV-WP0).
- WP6: the library string puts nT=130K (a temperature) in the thermal-order slot of τ. Fix the slot semantics per CONVENTIONS §11 (REV-WP6).
- Halo reference CONFIRMED by the coordinator: v_E^ref = |v_⊙| = 250.5 km/s, v_max = 794.5 km/s. The 252.1 km/s annual mean enters only the halo-uncertainty band (WP6).
- The audit script is copied to code/NOTATION-APPLY/audit.py (26/26 PASS on rerun).

## WP0-v2 interface flags (2026-10-31): to be applied in REV-WP1..WP6
- F1 → REV-WP1, REV-WP3. WP1 [E2] misses the total in non-centrosymmetric targets unless ρ → ρ*. WP0-v2 CC-1: the physical out-state weight is the retarded (ε̃⁻¹)_{G0}, in WP0 (3.2) order (v1 (7.2), X2). WP1's (1+Rv)_{0G} is the in-state labelling and enters conjugated. Both give the same total; they coincide in the PAER window. This settles the GaAs item, pending R7.
- F2 → REV-WP5. Theorem C must cite the four Coulomb-line classes of WP0-v2 §5, not the v1 "three-channel" (5.5).
- F4 → REV-WP2, REV-WP3. Compare WP2's κ₃ split with WP0-v2 (4.7) and WP3's Migdal spectra explicitly.
- F5 → REV-WP4. The replacement of Theorem D for gapless targets (metals, SC, semimetals) is owned by WP4: state it as a theorem or a conjecture.
- F8 → REV-WP5, REV-WP3. Estimate (or bound) the size of the Fano term 𝔉 in GaAs.
- F9 → REV-WP6. Fix the τ string (nT slot = thermal order, not a temperature).
- F11 → all REV agents. The static-DFPT screening error is O(ω_Q²/E_g²) (X2), not O(ω_Q/E_g).
- F3, F6, F7: consistency notes (WP0-v2 §12), including WP2's owed G → GS rename.

## 17. R6 v2 returns: renames owed for NOTATION v4 (audit A14, A20; to be applied at the R7 errata)
| Return / site | Old → new | Type |
|---|---|---|
| WP0-v2 (8.1), (8.3) | a_k (A-type amplitude) → a^A_k; "c = 2.71" → the number 2.71 (bare c is a band subscript); ℒ, π_k now have rows; s_{ex,i}, b_{ex,i} as in NOTATION §E | N |
| WP0-v2 §6.2 (ii), (4.8) | V (potential energy) → V_pot (V_ee, V_eN, V_NN); adiabatic energies → E^ad_n | N |
| WP1-v2 §15 | none owed; IF-9 rows added (a_lat, n_H, α_χ, k_v, ψ̂, α_LRC, p_T, E_min,0, δq̂) | — |
| WP2-v2 (5.1′), §17 | y (= ω − E_R) → y_R; a_A → a^A_{n_A} | N |
| WP3-v2 §4, §16 | 𝒜_ν(ω;T) → 𝒜^{PA}_ν(ω;T) | N |
| WP4-v2 [2.4], §15 | 𝒜^α (two-magnon amplitude) → 𝒜^{2m}_α | N |
| WP4-v2 [2.2], §15 | 𝒜̄^α_ν → 𝒜̄^{1m}_{α,ν} | N |
| WP4-v2 [4.2], §15 | y, y′ (= ω/Δ_BCS) → y_BCS, y′_BCS | N |
| WP4-v2 §5.4 correction (ii) | 𝒮_F = πζ_S/(1 − e^{−πζ_S}), ζ_S = α/(ε_bg v_F b_D) → 𝒮_F^D, ζ_S^D ([6.2] keeps 𝒮_F, ζ_S) | N |
| WP4-v2 §6, [6.1], §15, flag I6 | n_D (defect density) → 𝓃_D; n_NV → 𝓃_NV | N |
| WP4-v2 §8, §15 | 𝒬_{n,m} → 𝒬^{D-g}_{n,m} (𝒬_κ is the dynamical quadrupole) | N |
| WP4-v2 §1–§4 | ξ₀ (coherence length) → ξ_coh | N |
| WP5-v2 §1.1(d), §14 | M^{dir}, M^{exc} (ii amplitudes) → M^{ii}_{dir}, M^{ii}_{xch} (M^{exc}_{λ±} is WP3's exciton replica) | N |
| WP5-v2 §3.2, §4, §14 | E_BO(R) → E^ad_0(R) (WP2-v2 name for the same object) | N |
| WP5-v2 §5, R5, §14 | ξ_BCS → ξ_coh (ξ^{BCS}_k is the normal-state energy) | N |
| WP5-v2 (W7), (W8) | E (local carrier energy) → E_car | N |
| WP5-v2 §8, §14 (IF6-1) | θ_Rk → θ_{R-k}; θ_GW, θ_exch kept | N |
| WP6-v2 (5.1′), §15 | y → y_R; Π[·] → Π_mom[·] | N |
| WP6-v2 (6.2), §15 | W (Lambert-W value) → W_Lam | N |
| WP6-v2 §15 (IF6-2) | a_k → a^A_k | N |
| WP6-v2 §15 | θ_W, θ_X (WP5 nuisances) → θ_GW, θ_exch (WP5-v2 names); θ_{R-k} kept | N |
| WP6-v2 (5.2), §15 | J^{(sh)}(p_z) kept; WP6 v1 "J_s" → J^{(sh)} | N |

## 18. WP7 returns: renames owed (R13 merge, 2026-11-01; returns/R12/WP7-*-v2.md, WP7-E-v3.md not edited)
Read each WP7 return through this table and NOTATION "Rows added WP7" / "Rows added WP7-E". Source: the two clash tables there.
| Return / site | Old → new | Type |
|---|---|---|
| WP7-D-v2 | ω_L (Larmor frequency) → ω_Lar, δω_Lar (as B2 already does) | N |
| WP7-D-v2 | γ_n (mode width) → γ^{mode}_n; B2's γ_n source-only | N |
| WP7-D-v2 | Q_mode, Q_DM^eff, source Q_s, Q_p (quality factors) → 𝔔_mode, 𝔔^{eff}_DM, 𝔔_s, 𝔔_p | N |
| WP7-D-v2 | Ω_a (Rabi frequency) → Ω_Rabi | N |
| WP7-D-v2 | p (spin polarisation) → p_pol | N |
| WP7-D-v2 | ξ (2507.14287 pair normalisation) → source-only, cited as ξ_pair | N |
| WP7-D-v2 | m_φ in (F.7) (scalar mediator mass) → m_φ^{med} | N |
| WP7-D-v2 | m_V in §3.4 (dark-photon DM mass), x = m_V/m_e → m_φ; x = m_φ/m_e | N |
| WP7-D-v2 | t in (F.7) (Mandelstam t) → t_M | N |
| WP7-D-v2 | ω′ (emitted photon energy) → ω′_γ | N |
| WP7-D-v2 | T₁, T₂ (spin times) vs T §4.5 / 1610.03974 T₁, T₀ (temperatures) → spin times keep T₁, T₂; heat-release temperatures T_hi, T_lo | N |
| WP7-B2-v2 | v_κ, v̄, δv, v^{LO} (absorption vertices) → 𝔳_κ, 𝔳̄, δ𝔳, 𝔳^{LO} | N |
| WP7-B2-v2 | A, B (Taraskin IR coefficients) → A^{IR}, B^{IR} | N |
| WP7-B2-v2 | r_c (ionic-core radius) → r^{ion}_core; T's r^{def}_core | N |
| WP7-T-v2 | c (defect class) → 𝔠 (WP7-E-v3 already writes 𝔠) | N |
| WP7-T-v2 | η (local pole width ωΓ_ph) → η_pole | N |
| WP7-T-v2 | G(q,ω) (local acoustic propagator) → G^{ac}(q,ω) | N |
| WP7-T-v2 | ε_ij (hop release energy) → ε^{hop}_ij | N |
| WP7-T-v2 | ε_D(k), ϖ(k) (defecton dispersion, shape) → ε^{dfn}(k), ϖ^{dfn}(k) | N |
| WP7-T-v2 | 𝒬(t) (overlap exponent) → 𝒬^{sb}(t) | N |
| WP7-T-v2 | Γ_φ (pure dephasing) → Γ_dph | N |
| WP7-T-v2 | w_e, w_N, w_c (acoustic weights) → w^{ac}_s | N |
| WP7-T-v2 | d (tunnelling distance) → d_tun | N |
| WP7-B1-v2 IF-B1-9, WP7-D-v2 IF-D3 | geom value sets → one key geom ∈ {bulk, body, 1D, 2D, stack} (CONVENTIONS §13 row 25) | W |
| WP7-E-v3 | κ (calibration ratio) → κ_cal | N |
| WP7-E-v3 | X, ΔX (non-E_st deficits) → X^{oth}, ΔX^{oth} | N |
| WP7-E-v3 | g ≡ eV_b/ε (Luke gain) → g_Luke | N |
| WP7-E-v3 | y (ionization yield) → y_ion | N |
| WP7-E-v3 | ε (1803.02903 pair energy) → ε_eh (same object, NOTATION §G) | N |
| WP7-E-v3 | δ ≡ Δϵ/ϵ → δ_coll | N |
| WP7-E-v3 | r ≡ ϵ_NTL/ϵ_prim → r_coll | N |
| WP7-E-v3 | r_c (capture radius) → r_cap | N |
| WP7-E-v3 | σ(u_car) (capture cross-section) → σ_cap | N |
| WP7-E-v3 | 𝔵, 𝔵_i (induced-charge mark) → 𝔮, 𝔮_i | N |
| WP7-E-v3 | m(r) (position-mean mark) → m_ind(r) | N |
| WP7-E-v3 | E_x ≡ −N_XE_x^b (binding correction) → ΔE_X^b | N |
| WP7-B1-v2 §17, WP7-D-v2 §8 | the R12 verifier minors (VER-WP7-B1-A/B, VER-WP7-D-A/B) were applied in the LIMITS rows only (✎ in LIMITS "WP7 (R12, REFEREED)"); the returns' own row text is superseded by LIMITS | W |
| WP7-E-v3 §5 (Amendment A-1…A-16 to WP5-v3) | applied by R13 WP5-ERR → returns/R13/WP5-v4.md; until it returns, WP5-v3 is read with §5 of WP7-E-v3. **DONE (R16 CW8-A merge):** WP5-v4 returned and was audited (returns/R14/WP5-AUD.md, IF-AUD-8: "WP5-v4 audited (R14 WP5-AUD)"; A-1…A-16 applied faithfully; IF-R13-2, -3, -5 resolved there; IF-R13-4, -8 stand as noted, §19.5). WP5-v3 is no longer read with E §5; read WP5-v4 through §19.5 | S |

## 19. R14–R16 owed corrections targeting returns (CW8-A merge, 2026-11-01; returns not edited)
Sources, in the merge order of authority (later overrides earlier): returns/R14/WP5-AUD.md with referees/R14/REF-WP5-AUD-{A,B}.md as settled in returns/R16/CW5.md §1 (LE-22)
and CW5-errata.md §B; returns/R16/GAP-EF-v2.md + GAP-EF-v2-errata.md §3 (superseding R14 GAP-EF); returns/R16/CWn.md read through referees/R16/VER-CWn.md and
CWn-errata.md (errata re-issued text where re-issued, CWn.md where "unchanged"); returns/R16/WP8-R-v2.md (with CW6-errata §B4), WP8-U-v3.md, WP8-U-table-v4.csv,
WP8-F-v3.md; returns/R15/CMPMC-AUD.md, returns/R16/CMPMC-DEV.md, returns/R15/COMP-PAER.md. Type per CONVENTIONS §12 (S substantive, N rename, W wording/scope).
"Exact text" is quoted from the source item named in the last column; where the source gives a long replacement, the cell names the site and the source item
whose text is to be used verbatim (never paraphrase it when quoting the return). Corrections whose target is a coordinator file (LIMITS, NOTATION, CONVENTIONS,
SOTA, LOOSE-ENDS) were applied in the CW8-A merge (returns/R16/CW8-A-merge-log.md) and are listed here only as pointers. **Label clash:** returns/R14/WP5-AUD.md
and returns/R15/CMPMC-AUD.md both use IF-AUD-n; always cite them as "WP5-AUD IF-AUD-n" and "CMPMC-AUD IF-AUD-n" (CONVENTIONS §14).

### 19.1 WP0-v3 (returns/R8/WP0-v3.md)
| Site | Exact text (or source item holding it verbatim) | Type | Source |
|---|---|---|---|
| §6.2 (iv″b) | "… includes the Fano term 𝔉_{Λ₀,b} (CW3 (CW3.1)); 𝔉 = 0 for PT-symmetric targets with an even electron number and a scalar level-shift matrix on the degenerate X0 manifold (one-body self-energies on Kramers or irrep manifolds), with or without SOC (Si, Ge, diamond) [D] (Θ-real pair basis, CW3 §2.2 (P1)–(P5)); otherwise only the branch sum vanishes; generically ≠ 0 in GaAs [C]" | S | CW3-errata §2.2 item 5 |
| §6.2 rigour paragraph | delete "and the crystal has a gapless acoustic branch"; add "the PST gap condition concerns the electronic spectrum only; acoustic softness is the IR issue of the X+ definition (O4 §8.4)". "For low-lying vibrational states … the order of the remainder is not derived [C]" → "holds with the same order on energy-cutoff states (math-ph/0201055, 'Energy cutoff') [D given PST]" | W | CW3 OC-7 (unchanged) |
| §6.2 Scope of (H2) | "Magnetic insulators with a charge gap Δ_ch ≫ ω_ph, J are covered by Theorem D-m (CW3 §1.3, ERR-CW3 §1.6): GS-m = spin–lattice manifold [D given PST]; quasi-boson sectors [D at quadratic order, with the Goldstone and Q = 0 acoustic zero modes gapped by the reference field or removed]; the cross-term bound is conditional on the open connected (G5′-c); itinerant magnets and fractionalised references remain open" | S | CW3-errata §2.2 item 8 |
| §9.2 (iii) relaxed ch = e, G6 | as LIMITS L17 (CW3-errata §2.2 item 10, applied in LIMITS): step (iii) is not a usable bound for the relaxed electron channel; use (iv) or (9.4) with (CW3.4) | S | CW3-errata §2.2 item 10 |
| (2.9) and L9b note | "Γ_abs = g²_aγγB₀² B̂₀·Im[−ε^{-1}(m_φ)]·B̂₀/m_φ (= 2305.05681 Eq. (6), CONFIRMED [FT]); valid for samples ≫ skin depth"; §12 O6 → "closed (CW3 §3.4)" | W | CW3 OC-11 (unchanged) |
| (2.9) ALP-in-B₀ prefactor | check the 1/m_φ² dependence of the ALP-in-B₀ absorption against WP8-F-v3 §2.2 (g²B₀²L_∥/(ρ_Tm_φ²)) | W | WP8-F-v3 IF-F9 |
| (3.5)–(3.6), scalar row | "closed form: Γ_φ = −(y_φ²/m_φ)Im R̃_{𝒯𝒯}(0, m_φ) for non-polar point groups; polar groups add −(y_φ²e²/m_φ³)Im[R̃_{𝒯i}(ε⁻¹)_{ij}R̃_{j𝒯}](0, m_φ) (longitudinal + transverse parts of 𝒟^γ, full optical ε tensor) (CW7-155a,b; errata §1.6). The per-electron sum rule Σ_f(E_f − E_i)\|𝒯_fi\|² = ⟨(∇V)²⟩/(2m_e³) holds for a one-body regular V only and diverges for the Coulomb nucleus; the matrix-element check is ⟨c\|p²\|v⟩ = −2m_e⟨c\|V\|v⟩." | S | CW7-errata §2.1 |
| (7.3) | optional pointer: "(W6) of WP5-v4 is the marked observable law; (7.3) is its t = t_pr marginal" (consistent; no change of content) | W | WP5-v4 IF-R13-8, stands per WP5-AUD IF-AUD-8 (closes LE-166) |
| §2 operator basis | 𝒪₂ → v_χ²n_s − 2v_χ·j_s + 𝔳²_s with the 17th row 𝔳²_s (applied in CONVENTIONS §7, R16 amendment) | S | CW3 OC-9 (unchanged), IF-CW3-5 |

### 19.1′ WP1-v3 (returns/R8/WP1-v3.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| [E11] (δ_rel), with WP6 and LIMITS L17 (9.5) | the complete O(α²) list for the relativistic f-sum shift is mass-velocity + orbit–orbit only; (CW3.3) all-electron 𝒮_st(k) spec | W | IF-CW3-8 (unchanged) |
| [E13] Si zero-phonon thresholds; window numbers 0.42/0.54 MeV | replace by the [CALC] values: PAER-only 0.333 (replica) / 0.3374 (continuum) – 0.405–0.408 MeV; forbidden ZPL from 0.405–0.408; allowed ZPL from 0.547 MeV (the 0.42 (0.40–0.44) and ≈ 0.54 MeV estimates are confirmed at their low end) | S | COMP-PAER IF-CP-1 (CLAIMED, unrefereed) |
| GaAs inputs (with CW1) | GaAs low-T ε_∞, ω_L, ω_T [FT] are needed to 1% for the A4 near-cancellation (CW2 §20); collect measured values | W | IF-CW2-5 (unchanged) |

### 19.2 WP2-v3 (returns/R8/WP2-v3.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| §5.2″ (Core part), sentence "The L shell roughly doubles the O(q²) coefficient [E] (its 8 electrons at ≈ 4× the radius), so the hydrogenic numbers are a lower bound on the deviation." | replace by the four bullets of CW2-errata §2 item 3 verbatim ("All-electron atomic densities (NR, PBE; R16 CW2 §9, CW2-errata E-2, E-7, [CALC]): 𝔯 − 1 = 0.59, 4.21, 9.98, 28.7, 92.0% (Si) at 10, 30, 51.1, 102, 300 keV. The L shell raises the O(q²) coefficient by ≈ 1.6× and is negligible above ≈ 100 keV … Correct 𝓃_e(R_κ) and Δ𝓃_κ separately.") | S | CW2-errata §2 item 3 (OC-3) |
| §12 item 8 | → "spherical part [CALC, NR, CW2 §9]; crystal valence anisotropy and the relativistic finite-nucleus 𝓃_e(R_κ) open (CW2-errata E-7)" | W | CW2-errata §2 item 3 |
| §12 gaps 1–3, IF-10, IF-13 | append: "exact ω-integrated coherent weight (R16 CW2 (CW2.3)–(CW2.4)), certified pointwise band (CW2.5)–(CW2.6), T > 0 resummed form (CW2.7) (second-order TDS 1/\|q − G\|). The ≈ 0.16 [E] stands until ℛ₂ (CW2.4) is computed for the crystal (only a 1D illustration, ℛ₂ = −0.34, exists)" | W | CW2-errata §2 item 10 (OC-10) |
| §10 L4 add-on; finite-q charge vertices | "every finite-q charge vertex or Δ𝓃 above q_c ≈ 10 keV uses AE densities, and every 𝓃_e(R_κ) uses ∫𝓃_eρ^{nuc}; PAW frozen-core and spherical-core LAPW give no core polarisation" | W | CW2-errata §2 item 13 (IF-CW2-9) |
| G3 tables (validity columns) | adopt f_coh = 𝔓^{(n)}/S_inc (exact for Bravais), computed S_coh/S_inc in flagged cells and ℛ^{coh}_n (CW2.4) as the G3 coherence-validity columns | W | IF-CW2-1 (unchanged) |
| G13 / anharmonic template | first-order Φ³ is absent from S_κκ (CW2.18); the increment is O((Φ³)², Φ⁴); template structure fixed, no M type | W | IF-CW2-4 (unchanged) |

### 19.3 WP3-v3 (returns/R8/WP3-v3.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| §M4 (iv″b) sentence | "Fano term 𝔉_{Λ₀,b} = Γ^{(b)}(c̄^F − c_b^F) with c^F of CW3 (CW3.1); 𝔉 = 0 for PT-symmetric Si, Ge, diamond at the one-body self-energy level [D, (P1)–(P5)]; e–h vertex level shifts leave only Σ_b𝔉_b = 0" | S | CW3-errata §2.2 item 6 |
| J8, (4.7′) (E^{Mig}_3, 𝔨₃^X) | quote (CW2.13) E^{Mig}_3 = (q²/2M²)[Ze²⟨𝓃_e⟩_{ρ^{nuc}}/3 − ∂²E^ad]; NR coefficients at r = 0: 1501 (Si), 16867 (Ge), 15445 (Ga), 18527 (As) eV² × E_R, low against the relativistic finite-nucleus value by ≈ 8% (Si) and ≈ 37–45% (Ge/Ga/As) [E]; only the relativistic finite-nucleus density is owed | S | CW2-errata §2 item 12 (IF-CW2-2) |
| IF-13 / J3 | append: "P_Mig ≤ E_R(δM_κ/M_κ)/E_g (R16 CW2 (CW2.14)); δM_κ = ω² slope of the dynamical on-site force constant" | W | CW2 OC-11 (unchanged) |
| N1 (validity range) | add the P_Mig validity range P_Mig ≤ E_R(δM/M)/E_g (CW2.14) to J3/N1 | W | IF-CW2-6 (unchanged) |
| (W.6), Migdal–PAER interference | A^{Mig} = −i × boost amplitude: carry the −i in Migdal–PAER interference | S | IF-CW4-4 (unchanged) |
| §M9 / WP1-v3 [E13] Si window | replace the parabolic [E] window by the [CALC] values: PAER-only 0.333 (replica) / 0.3374 (continuum) – 0.405–0.408 MeV; forbidden ZPL from 0.405–0.408; allowed ZPL from 0.547 MeV; the 0.42 (0.40–0.44) and ≈ 0.54 MeV estimates are confirmed at their low end | S | COMP-PAER IF-CP-1 (CLAIMED, unrefereed) |
| §M7 / X2 data-calibrated PAER | "the dipole extrapolation of the optical ε₂ to q ≈ 0.3–0.9 Å⁻¹ overstates S̄ by ×10–40 (ℱ_ρ); any data-calibrated PAER estimate must carry a finite-q vertex form factor" | W | COMP-PAER IF-CP-3 |

### 19.4 WP4-v3 (returns/R8/WP4-v3.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| OW4-1, §8 Status, I1 | keep open, adding: "(G5′) with U_qp = 1 fails: the disconnected term c†H_off\|FS⟩ makes 𝔥_off extensive (ERR-CW3 §1.1, CW3-C12). The open item is the connected (G5′-c), which needs a dressed vacuum (U_qp) and an N-uniform commutator bound. Connected size [E] ≈ 0.2 eV (Al), ≤ λ_max of the Fan–Migdal zeroth-moment band matrix." | S | CW3-errata §2.2 item 22 (new) |
| §8 (c) Dirac sentence | append "one-loop running α̃(ω) = α̃₀/[1 + (2(N_D+1)α̃₀/3π)ln(Λ_D/ω)] (ERR-CW3 §1.7; 1101.2210 Eq. (4) at N_D = 1 [FT]); α̃ ≈ 0.25 at Λ_D/ω = 10³ from α̃₀ = 0.91 [E]" | W | CW3-errata §2.2 item 23 (new) |
| I12; §4.3 validity table; L15 nuisance wording | "L^{BCS} = 𝔤_IL^{nor}(1 + 𝔯_ε²)/[(1 + δ_𝔰)² + 𝔤_I²𝔯_ε²] (CW4 (8.1)); at the Al edge 0.33–0.40 (y = 2.2) … 0.94–0.96 (y = 10)"; use (8.1) and the CW4 §8 table instead of [4.2′] + "exclude y ≲ 3.5"; type-Δ nuisance from the KK-∞/cut spread; WP4-K34's Re ε^{nor} = k_TF²/q² is 19% above the edge value 0.839k_TF²/q² | S | CW4 OC-12 (unchanged); CW4-errata §B IF-CW4-1 |
| §2.1(c) and [2.2](b) | "1/(2\|𝐒_j\|) is the LSWT expansion parameter: 0.2 for YIG (\|𝐒\| = 5/2); = 1 at \|𝐒\| = ½, where LSWT is qualitative only. The computed sizes are r_2m = ΔS(1 + ΔS)/(S(1 + 2ΔS)) (local two-/one-magnon ratio; 0.146 at S = ½, simple-cubic AFM) and the one-magnon weight defect ΔS/S (0.156 at S = ½; CW7-errata §1.7)." | W | CW7-errata §2.1; WP8-F-v3 IF-F8 |
| §6 RG7, l.329, l.551 | "t_esc is the flux- and mode-averaged film→substrate transmission t̄_esc: AMM 0.32, DMM 0.26 (Al/Si; CW6 §7). It enters τ_l = 4d/(v_film t̄_esc) for an isotropised film population and the per-entry absorption (CW6-4). The fitted Si→Al 0.3–0.55 of 1805.02495 is t̄_{Si→Al}·P_abs and constrains λ_pb/d (a_opt ≈ 0.14–0.38 at 60 nm), not t_esc. RG7 closed as a nuisance θ_esc^{film} over AMM/DMM (×1.26 in τ_l)." | W | CW6-errata §B2 OC-CW6-7 (re-issued) |
| IF-U7 (YIG experimental a) | open: s_spin ∝ a⁻³ needs the experimental lattice constant [FT] (GAP) | W | WP8-U-v3 IF-U7 |
| (W13)-type η_pb use (with WP5) | η_pb(Ω, τ_l/τ₀^φ) for 4Δ < Ω ≤ 10Δ from 1401.1937 Fig. 4 [FT], reproduced by CMPMC to ≤ 0.011 (τ_l/τ₀^φ ≤ 4); it falls with Ω in thin films | W | CMPMC-DEV IF-DEV-1 (CLAIMED) |

### 19.5 WP5-v4 (returns/R13/WP5-v4.md) and the WP5 specifications (§2, §3.3, §3.4, §4)
WP5-v4 is **REFEREED** once read through this table (CW5 IF-CW5-9: after WP5-AUD IF-AUD-1…8 and CW5 OC-1…OC-8).
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| A-4/(W11) (and WP5-AUD §1.2 D-1 bullet, D-1 row, AUD-C3d label, R-e; WP7-E-v3 (E7)–(E8)) | CW5-errata §B OC-1 verbatim ("D′ ≡ E_st(t_win) + E_pairs(t_win) + E_X(t_win) + E_trap(t_win) + E_es^{trap} + ΔZPE(t_win) + E_esc, used only in the exact ratio Y_H = (1 − δ_coll)(ω − D′_NR)/(ω − D′_ER). … 'L36–L38 numbers unaffected' → '[E]: drift ≈ 1 µs (Si, 4 V/cm) and ≈ 2.5–25 µs (Ge iZIP, ±2 V, ≈ 1.6 V/cm [E: 25.4 mm thickness assumed, not stated in 1805.09942]) against ≳ 100 µs windows'.") | S | CW5-errata §B OC-1 (supersedes WP5-AUD D-1) |
| A-4 last sentence; E §6 "Exact constraints" (WP7-E-v3) | "η^φ_NR = 0.952 constrains g_Luke(r_coll − 1)(1 − y_ion)/(1 + r_collg_Luke) + [(1 + g_Luke)/(1 + r_collg_Luke)](δ_coll + (D′_NR − κ_cal(r_coll)D′_ER)/ω) = 0.048." (the A-4 mixed sentence is off by O((r_coll − 1)d′)) | S | WP5-AUD §2, D-3 |
| A-12 (and WP5-AUD D-2) | D-2 reclassified as clarification. Append to A-12: "(E7) counts 𝒲_bias(t_pr) once, inside NTL heat; never weight ℋ_pr (which contains it) by ϵ_prim. Its collection efficiency lies between ϵ_prim and ϵ_NTL [E]; ≤ 0.25 eV per carrier at 250 V/cm, saturated drift, t_pr = 100 ps [E] (WP7-E-v3 C15)." | N | CW5-errata §B OC-2 |
| §8 θ_coll; E §6 θ_coll; WP6 θ_coll row (and WP5-AUD §3.2(b), D-4) | "r_coll: median 1, σ_ln 0.1 [E] (WP8-R's \|r_coll − 1\| ≲ 0.2 read as 2σ), sign open in the profiled object (i); the conditional bound (ii) E_st/ω ≤ 1 − η is reported on the r_coll ≥ 1 branch only. The C8b illustration assumes r_coll ≥ 1, a flat E_st/ω prior on [0, 0.1] and δ_coll = X^{oth} = 0." (WP5-AUD's σ_ln 0.2 is withdrawn) | S | CW5 OC-8 (unchanged by errata) |
| §R13.3(b) θ_𝒦 note; IF-R13-5 | "≥ 3 support points" → "moment matrix of (1, E) singular for one ε^{hop}; interior condition ε_min < E_st^{rel}/⟨N_hop⟩ < ε_max with ≥ 2 distinct ε^{hop}" | W | WP5-AUD D-5 (STANDS, CW5 §1.1) |
| §3.4 (Partition tables), §4 (Barriers) | quench protocol (1)–(5) of WP5-AUD §3.1 verbatim ("(1) E^{conf}(𝔅₀^{min}) is the relaxed perfect cell … (5) The MLIP-versus-DFT spread of E^{conf} differences is θ_PES."); G-E3 closed as a specification, open as a computation | S | WP5-AUD D-14 (IF-R13-3 CONFIRMED) |
| §2, §3.4 (created-phonon spectrum, B-1) | "(i) carrier relaxation from creation down to ω_op; (ii) residual kinetic energy below ω_op; (iii) capture heat; (iv) pre-t_pr NTL heat; (v) lattice heat ℋ_nuc from the §3.4 MD projection (with anharmonic residual and thermostat energy). Σ_{(i)–(v)} = ℋ_pr − ΔZPE; ΔZPE is excluded from the spectrum. E_s^{(0)} = ω_s/2 per end-state mode (not the projection of R_I(0)). The ≤ 10% anharmonic acceptance is [E]." | S | CW5 OC-3 (unchanged); WP5-AUD D-16; WP8-R-v2 IF-R1 |
| §3.3 (B-2, 2303.02196 NR yield) | "N_eh ≤ ⟨N_eh⟩ + 6σ (≥ 100 at 1 keV); trajectories per point ≥ 1112 for 6% on the variance at κ_ex = 2 (error √(2/(n − 1) + κ_ex/n); 8.9% at n = 500); 2303.02196's sub-keV E_r is set by neutron kinematics; its Eq. (1) books the non-NTL phonon energy as E_r (unit heat quenching), which is the L37 truncation; ⟨𝔮⟩ = 0.873 is a worst case from detector-model trapping probabilities [E]." | W | CW5-errata §B OC-4 |
| A-6/C41 | "N_a ≳ 270" → "N_a ≳ 272–543 (0.2–0.1 eV/atom)"; "E_thr ≤ 2.7 eV" → "≤ 2.1–2.7 eV" | W | CW5 OC-6 (unchanged; WP5-AUD D-12) |
| §6.3, C35 | p_surv(Si, ΔZPE) "≲ 0.48" → "≲ 0.47 (unrounded 0.4748)" | W | CW5 OC-6 (unchanged; supersedes WP5-AUD D-13 "0.475") |
| §1.5 (sampler), §3.1 | CW5-errata §B OC-9 verbatim ("Defect seeds exported at phonon poles (WP7-T-v2 (1.3), IF-T9) carry the signed weight (π\|B\|²/η_pole)δ − 2πIm(a*B)δ. … report min_{N_eh} of the class sum and treat a negative value as a cascade-consistency failure.") (closes IF-R13-4) | S | CW5-errata §B OC-9 |
| §1.5, (W17) and the K_ν line | "K_b = (Γ^{(b)} + 𝔉_b)/Γ^{tot}, 𝔉_b ≡ Γ^{(b)}(c̄^F − c_b^F), c_b^F ≡ Γ^{tot}Im(Σ_{f∈b}Γ^{(f)}ρ*_Λ₀a^{off}_f/Γ^{(b)})/\|ρ_Λ₀\|², c̄^F = Σ_bΓ^{(b)}c_b^F/Γ^{tot}, b ∈ {ν, x}, a^{off}_x = 0 at O(g²); Σ_b𝔉_b = 0 (Σ_ν𝔉_ν = −Γ^xc̄^F)." | S | CW3 OC-1 (unchanged) |
| (W15) | "\|ΔP(N\|Λ₀)\| ≤ (Γ^{ph}/Γ^{tot})max_ν\|c_ν^F\|·max_{b,b′}\|P_b(N) − P_b′(N)\| ≤ max_ν\|c_ν^F\|". Positivity line → "K_b ≥ 0 iff 1 + c̄^F − c_b^F ≥ 0, sufficient 2max\|c^F\| ≤ 1". GaAs [E] "2π max\|c^F\| ≲ 0.3Γ/δ" → "max\|c^F\| ≲ 0.3Γ/δ (first order in Γ/δ); K_ν ≥ 0 quoted for Γ/δ ≤ 0.5 [E, perturbative], outside the d11 and onset shells (CW3 §2.3, ERR-CW3 §1.4)" | S | CW3-errata §2.2 item 2 |
| §8 θ_𝔉 row (and WP6 θ_𝔉 prior) | bound "\|ΔP\| ≤ max\|c^F\|" (not 2π max\|c^F\|); value "[E] ≲ 0.3Γ/δ, first order in Γ/δ, valid for Γ/δ ≪ 1; seeds in the d11 or onset shells use the unexpanded Dyson form" | S | CW3-errata §2.2 item 3 |
| §6.4 "Asymptotics" | CW5-errata §B OC-10 verbatim ("n̄(ω) = ω/ε_eh + o(ω) is DERIVED (CW5 §2.7 with CW5-errata §A12 … under (r1′)–(r5′) …). The constant b_N and Var N_eh = F_ehω/ε_eh + O(1) remain [D, sketch] (second-order renewal). CW5-C5 tests toy identities only.") | W | CW5-errata §B OC-10 |
| §6.4(ii)–(iii); WP5v3-C4b | rewrite §6.4(ii)–(iii) per GAP-EF-v2-errata §3 IF-EF1 verbatim ("(ii) 54/175 ≈ 0.31 is the variance with N held fixed. With the energy constraint, the same independent-residual model gives 27/686 = 0.0394, 3× below the data … (iii) Phonon shot noise is not the leading term either: 𝒱_> is 7× Poisson. Replace (ii)–(iii) by (EF6), (EF6′), (EF7) with the §1.6 table (errata R-6 for row 2)"); relabel WP5v3-C4b "N fixed"; L23 note (applied in LIMITS) | S | GAP-EF-v2-errata §3 IF-EF1 |
| §1.5 / R5 Holstein seeds in SC | (12.1) confirms B1 §9 WP4-consistency (i)–(ii): QP energy ω − ω_ph, case-I P(E₁) | W | IF-CW4-5 (unchanged) |
| readout (QD films) | Förster transfer ∝ J_F² is a WP5 readout input; S unaffected | W | IF-CW4-7 (unchanged) |
| §2.5-type exciton/gap release (R6 / G-E10) | adopt (CW5-4) for r_g(t) with the CW5-errata (E.3)–(E.6) bimolecular-loss forms; the missing input is the rate set {k_FX, k_FT, k_XB,j, k_B↓,j, η_X, η_B,j, C_X} and, for dense tracks, γ_XX and C_A(mK) (CW5-errata §C LE-141) | S | IF-CW5-1; CW5-errata §A0, §C |
| §8 (yield row) | (EF3)–(EF4) of GAP-EF-v2 serve as the "URF (energy-only)" member of {step, R&K, URF}; ε_eh prior 𝒩(3.75, 0.05) unchanged; θ_GW and θ_Z on Γ_ii are equivalent to one M-type factor on 𝒜_ph; the F prior comes from the structural spread (−10%), not from 𝒜_ph | W | GAP-EF-v2 IF-EF2 (unchanged) |
| Si ε_eh, F presets | the CMPMC presets carry 3.749 eV / 0.119; T dependence at mK is not modelled | W | CMPMC-AUD IF-AUD-6 |
| Symbols (R8 table), §1.2 (B2) | n_pair (track pair density) → 𝓃_pair; a_X → a_x; W_{GG′} of (W1′) read as W^{scr}_{GG′} with the (W1′) index order (R17 CW8-B, LE-164) | N | NOTATION "Rows added R17" |
| §5 Limits (no-cascade range) | none owed: N_qp = 2, η_pb = 2Δ_BCS/ω for ω < 4Δ_BCS is already in WP5-v4 §5 and WP4-v3 §4.6 K27, I2 (IF-R8-7 applied both sides; re-checked R17 CW8-B) | — | WP5-v4 IF-R8-7; WP4-v3 I2 |

### 19.6 WP6-v3 (returns/R8/WP6-v3.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| §5.2 "Yield / cascade", "Fano factor F_eh" rows; rows after "Cascade band edge θ_Eg" | replace/append the WP5-AUD §3.2 table rows verbatim, **with two changes**: θ_coll "r_coll: median 1, σ_ln **0.1** [E] …" (CW5 OC-8; WP5-AUD's 0.2 withdrawn), and the row θ_X written **θ_exc** (rename, §19.16), type T **on r_g^{NR} and r_g^{ER} separately** (CW5 IF-CW5-2, WP8-R-v2 IF-R2) | S | WP5-AUD D-6, §3.2; CW5 OC-8, IF-CW5-2 |
| §6 Exact constraints | add: "η^φ_NR (1803.02903) fixes (AUD-1), the general-r_coll form of WP5-v4 (W11′), and ties θ_coll, θ_st, θ_tr and θ_esc. Report (i) the profiled E_st constraint under the full priors and (ii) the conditional bound E_st/ω ≤ 1 − η under (B-a)–(B-d) separately." | S | WP5-AUD §3.2 (D-6) |
| §5.2 rows θ_U, θ_τ (LEE model), θ_{R-k} | θ_U (M on U_rel), θ_τ (Δ on τ_av) for the LEE model; θ_{R-k} bounded by (CW5-1) (conditional on (H-BGK), CW5-errata §A0) | S | IF-CW5-2 |
| §5.2 rows θ_ζ, θ_ζg, θ_pos, F_NR, θ_Ssurf | CW6-errata §B2 OC-CW6-5 verbatim (θ_ζ "contrast ζ_O ≡ a_NTL − a_prim … uniform [0, 0.5] [E] …"; θ_ζg "… uniform [−0.5, 0.5] [E] (sign open) …"; θ_pos, F_NR rows as CW6 §9; θ_Ssurf "surface recombination velocity S_surf (enters through S/(S + D_X/L_X)) \| M \| σ_ln 2.3 [E] …") | S | CW6-errata §B2 OC-CW6-5 |
| §5.2 θ_esc^{film} | add θ_esc^{film} (AMM/DMM, ×1.26 in τ_l) as the RG7 nuisance | W | CW6-errata OC-CW6-7 |
| §5.2 magnon row, SC row, seeding row | the three rows of CW7-errata §2.1 verbatim (magnon reference LSWT row with r^M_mag = ΔS/S; superconducting row "M one-sided (downward) … masked … y < 3.8 …"; seeding (P) row) | S | CW7-errata §2.1 (LE-156, LE-157, LE-154) |
| §4.5 (G8′) | CW7-errata §2.1 text verbatim ("G8′ is closed by CW7 Theorem G8′ (returns/R16/CW7.md §3, corrected by CW7-errata §1.3): … under (I) **in the lab frame** it reduces to (4.2); signed φ (modulation amplitudes) need visibility on {φ > 0}.") | S | CW7-errata §2.1 |
| §11 OW6-1, OW6-3, OW6-6 | "OW6-1 CLOSED (CW7 §3 with errata §1.3); OW6-3 CLOSED (CW7 §4 (CW7-153a), (CW7-153b) as reworded in errata §1.4; solver code/CW7/cascade_gf.py as fixed for θ_ii > 1); OW6-6 CLOSED (errata §1.5 (CW7-154′); the R16 (CW7-154) fell)." | W | CW7-errata §2.1 |
| §4.2, sentence "The affected fraction is O(ω_Q/ε_eh) ≈ 1–2% of pairs in Si …, sign unbounded" | "The negative part is bounded by (CW7-154′): λ^P_i ≤ (2ω_max/Δ_i)ϱ_−, ϱ_− ≡ sup_ω max([A_X+]_−, [A_X0]_−)/⟨A_tot⟩_i (stochastic monotonicity of N in E; both pieces are needed because P_X+ − P_X0 takes both signs in an interior bin); 3.3%·ϱ_− for Si single-electron bins." | S | CW7-errata §2.1 |
| r_mat default (OW6-4) | read through CONVENTIONS §13 row 29 (signed-elasticity rule) | S | CW7-errata §2.1 (applied in CONVENTIONS) |
| §5.2 Dirac (L16) | multiply source curves by ε_bg² (σ̄) and √ε_bg (κ); never also by 0.55–0.62 | W | IF-CW4-6 (unchanged) |
| §5.2 SC (L^{BCS}) | type-Δ nuisance from the KK-∞/cut spread of CW4 (8.1) | W | CW4-errata IF-CW4-1 |
| §5.2 θ_𝔉 | as §19.5 (CW3-errata item 3) | S | CW3-errata §2.2 item 3 |
| library output | q-vector-resolved S for the stream kernel (no angle average) | W | IF-CW7-9 |
| IF6-10 (Si window) | as §19.1′ [E13] (COMP-PAER [CALC] window) | S | COMP-PAER IF-CP-1 |
| §5.2 yield row (URF member) | as §19.5 "§8 (yield row)": (EF3)–(EF4) as the URF (energy-only) member; one M-type factor on 𝒜_ph; F prior from the structural spread | W | GAP-EF-v2 IF-EF2 (unchanged) |

### 19.7 WP7-B1-v2 (returns/R12/WP7-B1-v2.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| §13 G-A2 | "CLOSED (R16 CW4 §12); Eliashberg form [D, sketch], computation specified" | W | CW4 OC-2 (unchanged) |
| §13 G-X6, G-E10b, G-A6, G-I5, G-E12, G-E5, G-E10a | read through LIMITS LB1-8, LB1-5, LB1-11, LB1-13, LB1-6 (CW4-errata §B OC-3…OC-7, applied there) and the CW4 closure table (LE-108…LE-115) | W | CW4-errata §B |
| §12 / (W.6) Migdal phase | as §19.3 (IF-CW4-4) | S | IF-CW4-4 |

### 19.8 WP7-B2-v2 (returns/R12/WP7-B2-v2.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| §2.2 (i) and §2.1 scope "O(ΔM/M) (²⁹Si ≈ 3.5%) [E]" | → "O(σ_M/M̄): exact first-order form (R16 CW2 (CW2.22)), +9% at 50 meV [E for D(ω)]" | S | CW2 OC-8 (unchanged) |
| §11.1–§11.11 gaps | read through LIMITS B2-L1, B2-L3, B2-L4, B2-L5, B2-L6, B2-L7 and "Numbers carried" (CW2-errata §2 items 2, 4–7; CW4 OC-8, OC-9; applied there) | W | CW2-errata §2; CW4 |
| IF-B2-11 / §11.12 magnetic sectors | Theorem D-m (CW3 §1.3 with ERR-CW3 §1.6) | W | IF-CW3-6 |

### 19.9 WP7-D-v2 (returns/R12/WP7-D-v2.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| §1.5 | "u … is the overlap of the inhomogeneous spin line with the absorptive Lorentzian (2101.01241 (S23)); the DM line is treated separately (Supp. §VII)"; amplitude sentence → "CONFIRMED with d_nε_SE* = per-level shift (2101.01241 convention, fixed by the Rabi frequency); 1306.6089's verbal gloss calls it the splitting (×2 misstatement of the source's wording)" | W | CW3-errata §2.2 item 13 |
| §1.7, IF-D12 | as LIMITS L-D4 (CW3-errata §2.2 item 15): "prefactor 32 derived …; M_n = ρπr_n²L₀ printed by the source, consistent with ∫U_n² = (2ρω_n)^{-1}; Eq. (7)'s numerator m_V² is correct …; odd n only" | S | CW3-errata §2.2 item 15 |
| §1.8 | "drive ∝ ω² [D] (body force −ρḧξ); 2δ_rel^a = −1.97×10⁻² (Cu), 1809.02863 Table II [FT]" | S | CW3 OC-16 (unchanged) |
| IF-D10 | as LIMITS L-D8 (CW3 OC-17, unchanged) | S | CW3 OC-17 |
| §3.4, IF-D12 | status "DERIVED: 2109.08168 Eq. (2) is the exact tree-level Dirac result (CW3-C4a); (T.4) agrees through O(x²); x³: exact −15/4, (T.4) −35/8; 1/8 kinematic, 1/2 Dirac amplitude"; §3.4(iii) seagull → "H_sg = −(eg_aee/2m_e²)(∂_ta)σ·A"; "Eq. (3) open" → "Eq. (3) REFUTED by (m_a+2m_e)/(m_a+m_e) (CW3 (CW3.5))" | S | CW3 OC-18 (unchanged) |
| §4.1 | "(S.2) DERIVED with ln Ī = (2/πω_p²)∫ωL(0,ω)ln ω dω; PDG RPP 2024 Eq. (34.5) [FT]"; NR bracket ln(2m_ev²/I) + O(v⁴) (CW3-errata L-D11′) | S | CW3 OC-19 (unchanged); CW3-errata §2.5 |
| §2.5 massive ν̃ | "ω^F = ω^{(2.1)} + (Δ_χ/m_ν̃)k²/2m_χ, 𝔇^F = 𝔇^{NR}(m_χ/m_ν̃)(1 + O(v²)) [D], with 𝔇^{NR} in the CONVENTIONS §7 vertex normalisation (DM-side 1/(2m_χ)²) and the relativistic 1/(4E_χE_ν̃) → 1/(4m_χm_ν̃)" | W | CW3-errata §2.2 item 20 |
| §2.5 charged current | exact-gap closure: row + distorted-wave spec of CW3 §4.1 with ERR-CW3 §1.13 (LE-86) | W | CW3-errata §1.13 |

### 19.10 WP7-T-v2 (returns/R12/WP7-T-v2.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| G-T5 (and LIMITS L30 source cell) | "Andreev–Lifshitz, Zh. Eksp. Teor. Fiz. 56, 2057 (1969) [UNVERIFIED, original not read; via cond-mat/0310283 ref. [11]]; review: Usp. Fiz. Nauk 102, 323 (1970) = Sov. Phys. Usp. 13, 670 (1971) (Crossref). T⁻⁹: cond-mat/0310283 Eqs. (12), (49)–(61) [FT], credited there to Pushkarov (its refs [16, 17])." | W | CW5 OC-11 (unchanged) |
| G-T1 | (CW5-6) replaces the [UNVERIFIED] Yamada formula; Born limit α_ohm = 4K with K = (N_σVΩ)² per spin (with a both-spin K: α_ohm = K, factor 1; CW5-errata §A21) | S | IF-CW5-6; CW5-errata §B "new (α_ohm)" |
| G-T2, §4.2 "frozen" verdicts | the CW5 §3.3 conditional verdict table (Al row "≥ 5.6%", CW5-errata §A23); single missing number per CW5 §3.3 | S | IF-CW5-6; CW5-errata §A23 |
| L30 status | exponent DERIVED (T⁻⁹), prefactor [FT] Eq. (61); T < Δ_dfn source law D_B ∝ (θ_p/T)⁷ Eq. (64) (not derived) | W | CW5-errata §B L30 row |
| IF-T9 (signed seeds) | answered by CW5-errata OC-9 (§19.5) | — | CW5-errata OC-9 |

### 19.11 WP7-E-v3 (returns/R12/WP7-E-v3.md)
| Site | Exact text (or source item) | Type | Source |
|---|---|---|---|
| (E7)–(E8) D′ | CW5-errata §B OC-1 (as §19.5) | S | CW5-errata OC-1 |
| (E13) remark; §6 "Exact constraints" | as §19.5 (WP5-AUD §2 constraint sentence with κ_cal(r_coll)) | S | WP5-AUD D-3 |
| §6 θ_coll | σ_ln 0.1 (CW5 OC-8) | S | CW5 OC-8 |
| §6 θ_X | rename θ_X → θ_exc (it reused WP6-v2's local name for θ_exch) | N | SOTA R13 pending item; LE-164 |
| §0 row 13, §3.3(b′) | "N_a ≳ 270" → "N_a ≳ 272–543 (0.2–0.1 eV/atom)"; "E_thr ≤ 2.7 eV" → "≤ 2.1–2.7 eV" | W | CW5 OC-6 |
| §3.2 | p_surv(Si, ΔZPE) "≲ 0.48" → "≲ 0.47 (unrounded 0.4748)" | W | CW5 OC-6 |
| §8 G-E4 and IF-E7 | CW6-errata §B2 OC-CW6-3 verbatim ("δ_coll = δ_coll^{prim} + δ_coll^{gap} + δ_coll^{pos} + δ_coll^{esc}; δ_coll^{prim} ≤ 0.012; δ_coll^{gap} = 𝒢_gap(ρ_g − 1)(x_ER − x_NR)/[1 + 𝒢_gapx_ER(ρ_g − 1)] … provided r_coll, y_ion (⟨𝔮⟩ measured at both biases) and X are bias-independent over the scan (CW6 §5, CW6-errata A7)") | W | CW6-errata OC-CW6-3 |
| (B-b) r_coll ≥ 1 | WP8-R-v2 does not support r_coll ≥ 1 (toy 0.87–0.98 [E], from sub-2Δ_Al NTL energy counted as lost); on r_coll < 1 the E_st/ω bound widens by g_Luke(1 − r_coll)(η^φ_NR − y_ion)/(1 + g_Luke) (exact at δ_coll = X^{oth} = 0) | S | CW6-errata IF-CW6-2 |
| Theorem E-2; G-E2; G-E9 | ionic exception (prompt E_el → E_st via STE, (CW5-8)); G-E2 → (CW5-9) (two missing steps: U_rel with (Γ_min, Γ_max), b_br; CW5-errata §A0); G-E9 → (CW5-12) (TV bound; exact **if** the marks are sufficient, CW5-errata §A32) | S | IF-CW5-7; CW5-errata §A0, §A32 |
| IF-E9 | "(EF12) holds only under (H-cap); otherwise use (EF12′). In both, each captured electron raises ℋ_eff by exactly E_g, split among ℋ, E_trap^{pr} and E_pairs^{unp} (errata R-12, GAP-EF-v2-C26). (EF13) is in the (W4′)-consistent form; §4.3 spec." Close IF-E9 at the formula level; numbers stay open (GE-4) | S | GAP-EF-v2-errata §3 IF-EF4 |
| NTL phonon spectrum (§1–§2) | NTL phonon energies at 1–100 V/cm (paer-sota, 1 mm, Ge/Si): ⟨E_Luke⟩ = 0.75–4.7 meV (e⁻), 1.1–6.4 meV (h⁺) ([CALC] pending CMPMC-AUD IF-AUD-1); the legacy 921db93 values are 5–45% too hard | W | CMPMC-AUD IF-AUD-5 |
| gap channel (collection row of the §1.3 ledger) | collected-carrier energy E^{coll}_rel routed through a 600 nm Al electrode re-enters Ge as soft phonons: 49–51% of E^{coll}_rel, mean 1.0 Δ_Al, 90–93% below 2Δ_Al (mechanism for the "soft, ballistic" surface-recombination population, 1109.1193 p.17 [FT]) | W | CMPMC-DEV IF-DEV-3 (CLAIMED) |

### 19.12 WP8-R v1 (returns/R13/WP8-R.md)
| Site | Exact text | Type | Source |
|---|---|---|---|
| whole return | "SUPERSEDED (R16, CW6/LE-20) by WP8-R-v2" (returns/R16/WP8-R-v2.md, read with CW6-errata §B4). WP5-AUD D-7…D-10 (R-a, R-c, R-f, R-h; renames δ, r, g → δ_coll, r_coll, g_Luke), CMPMC-AUD IF-AUD-2…4 and REF-WP8-R-A/B are applied in v2 | S | CW6 OC-CW6-1 (unchanged); WP5-AUD D-7…D-10 |
| WP8-R-v2 (R16) | read with the CW6-errata §B4 replacement passages (header checks line 62/62; §0 rows 2, 6, 8; §2.1, §2.4, §3.2 "Fitted.", §3.3, §3.5, §4.4, §6, §8, §9, IF-R3, L40) | S | CW6-errata §B4 |

### 19.13 WP8-U (returns/R13/WP8-U.md, R14/WP8-U-top.md, R16/WP8-U-v2.md → WP8-U-v3.md and WP8-U-table-v4.csv)
WP8-U-v3 and table v4 supersede R13 WP8-U, R14 WP8-U-top, R16 WP8-U-v2 and tables v1–v3 (WP8-U-v3 header). Owed against v4:
| Site | Exact text | Type | Source |
|---|---|---|---|
| v4 row 1543 (ZrTe5 Delta_D), note | "half-gap per 1910.02091 Eq. (1.1) and p.12 (gap 23.6 meV ↔ Δ = 11.8 meV); 'Exp. [52]' = 1603.05351, which reports no gap (massless-Dirac SdH paper) [attribution UNVERIFIED]; its Table I v_F (plane-resolved, 4.03/1.94/4.89 ×10⁵ m/s) are the 'Exp.' velocities; use 11.8 (DFT, NR)" | S | CW4-errata §B OC-11(a) (**conflict with WP8-U-v3 §5 "Δ_D = 11.75 meV"; listed for the coordinator, merge log §C**) |
| v4 row 3182 (`Delta_D_definition`, v3 l.3195), note | replace "Delta_D = 11.75 meV is the half-gap" by "the Table 1 Δ column is the half-gap; documented value 11.8 meV (DFT, NR); 11.75 meV attributed to [52] but not found there (CW4 §10)" | S | CW4-errata §B OC-11(a) (same conflict) |
| v4 row 1619 (Al Delta_BCS 0.3 meV), note; add row Al `Delta_BCS_bulk_E` 0.18 meV | CW4-errata §B OC-11(b) verbatim (note "source working value: 2109.04473 p.2 '∆ is half of the superconducting gap', ∆ = 0.3 meV; ≈ 1.7× bulk (film-like)"; new row `Al,Al,superconductor,SURVIVOR-COND,Delta_BCS_bulk_E,0.18,meV,E,arXiv:2305.06084,…`); v4 row 3181 (`flag_Delta_BCS`, v3 l.3194) → tag E, source "arXiv:2305.06084 T_c; CW4 §11" | S | CW4-errata §B OC-11(b); IF-CW4-2 |
| v4 Nb rows (row 2395 kept) | add row `Nb,Nb,superconductor,SURVIVOR-COND,Delta_BCS_FT,1.50-1.61,meV,FT,arXiv:1805.06359,p.3,"secondary (review-level) quote, orientation-dependent; 2Δ/k_BT_c = 3.74-4.04 with T_c 9.25-9.3 K (p.5)"` | S | CW4-errata §B OC-11(c) |
| U7, IF-U10, LU3 (R13 WP8-U) | U7 text of CW6-errata §B2 OC-CW6-4 ("A_iso is ordered Ge > Si > C as 1901.07569 p.6 states qualitatively; the Si value 1.65×10⁻⁴⁵ s³ is this return's closed form [E], consistent with 2408.04732 Eq. (4) (p.4) and Table 4 (p.7) [FT] …"). **LU3 itself is withdrawn** by WP8-U-v3 §10 (later authority); its content enters LIMITS as CW6-L4 (2408.04732 [FT]); the OC-CW6-4 status change of LU3 is therefore void | W | CW6-errata OC-CW6-4; WP8-U-v3 §10 |
| R14–R16 non-cubic elastic tensors | every non-cubic C_ij, Christoffel speed and NR edge of R14–R16 was built with C₄₄ ↔ C₆₆ swapped and C₁₄ misplaced (JARVIS shear order (xy, yz, zx)); read v4 rows `C_ij_Voigt_DFT_v4`, `c_LA_Christoffel_avg`, `c_dir_100_001`, `c_NR1_heavy`, `c_LA_max_dir`; R14 WP8-U-top LT1 non-cubic values and R16 v3 values are superseded | S | WP8-U-v3 §0 row 10, §1.3 V5′, §4.1′ (CLAIMED; R×2 owed, IF-ERR7-6) |
| reading rule | for any (material, property) with several rows, the last row whose note says "supersedes" wins; screening keys and the `verdict` column are unique/final | W | WP8-U-v3 header |

### 19.14 WP8-F (returns/R13/WP8-F.md → R16/WP8-F-v2.md → WP8-F-v3.md)
| Site | Exact text | Type | Source |
|---|---|---|---|
| whole return | WP8-F-v3 supersedes R13 WP8-F and R16 WP8-F-v2; WP5-AUD F-a, F-c, F-e, F-h, F-i, D-11, D-12, D-13, D-17 are applied there ("(prov.)" lifted, IF-F3 answered) | S | WP8-F-v3 header; WP5-AUD §5.2 |
| (4.2) "tanδ₀ of a-SiO₂ not quoted" | CW5-errata §B OC-12 verbatim ("tanδ₀ (low power, mK, ~6 GHz): thermal SiO₂ 3.0–3.3×10⁻⁴ and PECVD SiO₂ 2.7–2.9×10⁻³ (0802.2404 Table I [FT]); PECVD a-SiO₂ (SiH₄ + O₂) ≈ 5×10⁻³ at 25 mK (cond-mat/0507622 PDF pp. 3, 7 [FT]); … bulk fused-silica mK value GAP.") | W | CW5-errata §B OC-12 |
| §2.8(d) | E_st caps valid at the calibration energies only (Si 10–100 keV; Ge 103 keV ²⁰⁶Pb, surface); release power ≤ 𝓟_st (T-1); p_surv ≲ 0.47 (0.4748) | W | WP5-AUD D-17; CW5 OC-6 |
| v3 additions | the ERR-CW7 changes absorbed from REF-WP8-S-A/B (light-mediator target independence L-F4; heavy-mediator window; polar ε-route bound; 𝓠_Mig plasmon pole; uniaxial C_ij; ²¹⁰Pb) are CLAIMED pending their R×2 (IF-ERR7-6) | W | CW7-errata §5 |

### 19.15 R14 and R16 returns themselves (WP5-AUD, GAP-EF, CW returns)
| Return / site | Exact text | Type | Source |
|---|---|---|---|
| returns/R14/WP5-AUD.md §1.2 D-1, §5.1 R-f, D-7, §0 row 5, IF-AUD-6, AUD-C7c/C7c′ | read through CW5-errata §B OC-1 (D-1) and CW5 OC-7 (HV verdict CONDITIONAL; "robust at F_NR = 0.15" → marginal) | S | CW5 §1.3, OC-7 |
| WP5-AUD D-2, §3.2(b), D-4, D-12, D-13, §7, C3c/C3e | read through CW5-errata §B OC-2, CW5 OC-8, CW5 OC-6 ("N_a ≳ 272–543"; "p_surv ≲ 0.47 (unrounded 0.4748)"; tags g_Luke [FT], y_ion [E], κ_cal, r_coll [D on E]; "[FT via X]" → "[FT] (source, as read by X)"; 300 eV bracket [E]; C3c, C3e "consistency identities") | N | CW5 OC-2, OC-6, OC-8 |
| WP5-AUD B-1, B-2 | read through CW5 OC-3 and CW5-errata §B OC-4 | S/W | CW5 |
| WP5-AUD status | REFEREED (R×2 R14, settled in CW5 §1; CW5-errata) | — | CW5 §1 "Status" |
| returns/R14/GAP-EF.md (v1) | superseded by returns/R16/GAP-EF-v2.md read with GAP-EF-v2-errata.md §2–§3; v1's "derived" ε_eh ≈ 1.61E_g + k₂ is withdrawn (observed fit); v1 labels L39–L43 withdrawn (now L-EF1…L-EF5); v1 CsI ε_eh 11.46 → 11.21 eV | S | GAP-EF-v2 header, IF-EF6, IF-EF7, §0 row 10 |
| returns/R16/CW2.md … CW7.md, GAP-EF-v2.md | each is read through its R16 errata file (errata re-issued text wins; "unchanged" items from the CW file) | — | the errata headers |
| returns/R16/CW7.md §12 (WP8-S synthesis) | not merged: WP8-S is not final (REF-WP8-S-A/B; revision by a separate agent; rank.py must read table v4, IF-ERR7-1) | — | CW7-errata §5 |

### 19.16 Renames owed inside R14–R16 returns (read each return through NOTATION "Rows added R14–R16" and this table)
| Return / site | Old → new | Type |
|---|---|---|
| WP7-E-v3 §6; WP5-AUD §3.2 θ_X row | θ_X (exciton/gap-release nuisance) → θ_exc | N |
| CW2-errata (CW2.28) | P_g (ground-doublet projector) → P^{gd} (P_g is the gap-energy release fraction 1 − r_g, CW5) | N |
| CW2-errata (CW2.12′) | b, τ (pair tensors) → b^{pr}, τ^{pr} (b phonon operator; τ truncation index) | N |
| CW2 (CW2.27); CW2-errata (CW2.27′) | b_λ (chiral-stable probability) → b^{ch}_λ; 𝒞 (chiral-stable terminal set) → 𝒞_chi | N |
| CW2 (CW2.4) | ℛ_n → ℛ^{coh}_n (ℛ is the physical rate, WP8-F-v3) | N |
| CW2 (CW2.11) | ϱ(ξ) (Christoffel/Markov–Krein mass) → ϱ_MK(ξ) | N |
| CW3 §2.2 | Θ (antiunitary PT) → Θ_PT (Θ is the Heaviside step) | N |
| CW3 §1.3 | U_b (symplectic magnon–phonon map) → U^{sl}_b (U^B Bogoliubov, U_qp) | N |
| CW3 §4.1 | F(Z,E) (Fermi function) → F_Fermi(Z,E) | N |
| CW3-errata §1.3 | η_ij (level-shift ratio) → η^{ls}_ij | N |
| CW3-errata §1.13 | 𝒯_K (threshold set) → 𝒯^{thr}_K (𝒯_e kinetic operator, 𝒯^{(2)} two-insertion) | N |
| CW4 §1, §12 | M_i (Nambu amplitude) → M^N_i | N |
| CW4 §8 | 𝔯 (Im ε^{nor}/Re ε^{nor}) → 𝔯_ε | N |
| CW4 §15 | 𝐝 (transition dipole) → 𝐝_tr | N |
| CW4 §21 | c ≡ q̂·m̂ → cos θ_qm (c only as a band subscript, CONVENTIONS §4); CW4's u, v are u^B_k, v^B_k | N |
| CW5 (CW5-4) | w_k (weights of r_g) → w^g_k (w_κ one-phonon measure) | N |
| CW5 (CW5-8) | ε_X (energy per exciton) → 𝓔_X (ε dielectric family; E_X reservoir) | N |
| CW5 (CW5-10) | λ_L, r₀, D_a (track line density, radius, ambipolar diffusion) → λ_trk, r_trk, D_amb (GAP-EF r₀ thermalisation distance) | N |
| CW5 (CW5-11) | p_R, ω_R, S_HR,R → p_rxn, ω_rxn, S_HR,rxn (E_R recoil energy) | N |
| CW5 §3.8 | W_eff, W_r → W^{hop}_eff, W^{hop}_r (W_κ Debye–Waller) | N |
| CW5-errata §A12 | K_x, K_∞, ξ, κ (lineage kernel, scale-free limit, log decrement, approach exponent) → K^{lin}_x, K^{lin}_∞, ξ_ren, κ_ren (CW3 K_x branch weight; ξ halo; κ species) | N |
| CW5 / CMPMC-DEV | E_rel: CW5 keeps E_rel (TLS/LEE release energy); CMPMC-DEV E_rel (energy a collected carrier releases at the contact) → E^{coll}_rel | N |
| CW6, WP8-R-v2 | Σ ≡ c_L⁻² + 2c_T⁻² → Σ_c (Σ self-energy); Z (acoustic impedance) → Z_ac; 𝔯 (AMM ratio) → 𝔯_ac | N |
| CW6 §7 / CW6-errata A4 | a (in-film optical depth) → a_opt; a (channel fraction, errata A4) → a_pop (WP8-R-v2 name) | N |
| CW6 §6 | n_s (trapped areal charge) → n^{tr}_s (𝓃_s species density) | N |
| CW7 §3 (LE-152) | F, B, Φ, φ, g, 𝒞, R* → F_w, 𝔹_v, Φ_ℓ, φ_ℓ, g_test, 𝒞_R, R*_v; λ_i (dual weights) → λ^{dual}_i | N |
| CW7 §5 (LE-154), CW7-errata §1.5 | λ_i (leakage fraction) → λ^P_i | N |
| CW7-errata, WP8-F-v3 | K_ν(m_χ) (per-branch light-mediator weight) → K^{lm}_ν (K_ν is the WP5 Fano class weight) | N |
| CW7-errata, WP8-F-v3 | r^M (magnon residual width) → r^M_mag (row r^M_k of NOTATION §E) | N |
| WP8-F-v3 §2.6 | 𝔇_sw (FM spin-wave stiffness) → D_sw (𝔇 DM tensor family) | N |
| GAP-EF-v2 §4 | T_c (carrier temperature) → T_car (T_c critical temperature); κ_i (capture indicator) → 𝟙^{cap}_i; p_esc (exciton escape fraction) → p_esc^X (WP7-B2 p_esc) | N |
| CMPMC-AUD | 𝔐 (carrier Mach number) → 𝔐_c (𝔐 ∈ {ad, sud} is the Migdal-regime slot of τ, CONVENTIONS §11) | N |
| COMP-PAER | 𝔉_ρ(q) (finite-q form-factor proxy) → ℱ_ρ(q) (𝔉 Fano term) | N |
| CMPMC-AUD LIMITS labels | AUD-L1…AUD-L5 → CMPMC-AUD-L1…L5; DEV-L1…DEV-L4 → CMPMC-DEV-L1…L4 (WP5-AUD AUD-n labels) | N |
| GAP-EF v1 LIMITS labels | L39–L43 → withdrawn; v2 L-EF1…L-EF5 (WP8-R keeps L39–L42; CONVENTIONS §13 row 30) | N |
| table v4 (returns/R16/WP8-U-table-v4.csv) Al Δ_BCS | bulk row 0.18 meV [E] to be added; 0.3 meV relabelled film (CONVENTIONS §13 row 33) | W |

### 19.17 WP7/WP8 "owner to cite/adopt" flags addressed to frozen packages (R17, CW8-B; LE-174; returns not edited)
Routing table (flag → frozen site → adoption text or reason none is owed). The frozen packages (WP1–WP4, WP6 at v3; WP5 at v4; WP7-D at v2) are read through this
table exactly as through §19.1–§19.11. The adoption text restates the flag cell of the named return (its "Interface flags" table) with the equation labels it cites. It
is the reading rule for the frozen site and is quoted from the flag, not newly derived. "None owed" rows give the reason.
| Flag | Frozen site | Adoption text / reading rule | Type | Status |
|---|---|---|---|---|
| WP7-D IF-D4 | WP2-v3 §5 (L6 impulse NR) | "For the neutral-current (fermionic-absorption) line shape use S^{GS}_κκ at q = m_χ with the true ⟨p²_κ⟩ (not the Debye estimate) (WP7-D §2.4(a), (F.2)/(F.4); LIMITS L-D7)" | W | adoption text |
| WP7-D IF-D5 | WP1-v3 §5 (cores), §2 | "High-q all-electron S_nn and S_{J_TJ_T} at q ∼ 10 keV–1 MeV are inputs of WP7-D (F.4); spin-orbital convention as WP1; Dirac bilinears for cores (WP0-v3 (1.2) relativistic-cores option)" | W | adoption text; computation not owed by the frozen package (no WP1 revision; tables are a data input of L-D7) |
| WP7-D IF-D6 | WP5-v4 §1.1(e), §3.3 | "(S.1) is the stopping-kernel hand-off (LIMITS L-D11/L-D11′); the Barkas term is the second-order response R^{(2)}" | W | adoption text (WP5 track physics stays WP5's; Cat. D3/D4 class C) |
| WP7-D IF-D7 | WP6-v3 §2–§5 (likelihood) | "Coherent-regime (classical-field) signals use the exponential-bin likelihood (D.6) with bunching; fixed-amplitude analyses overestimate the reach by ×3–10 (1905.13650, LIMITS L-D3; CW3 §4.11 [FT]); one likelihood per signal, no double counting between the coherent and golden-rule rows" | S | adoption text |
| WP7-D IF-D8 | WP4-v3 [3.3], L19 (chiral targets) | "The P-odd antisymmetric response S^A_{J_TJ_T} enters (F.4) for chiral targets; WP4's chiral S^A rows are its input" | W | adoption text |
| WP7-D IF-D9 | WP3-v3 §4 (L9b), LIMITS L9b | "Finite bodies: orientation factor relative to bulk 1/ε₀ of 1 (slab, normal), 3ε₀/(ε₀+2) (sphere), ε₀ (slab, parallel), up to ε₀² in power; BAR Q_DM^eff" | W | none owed beyond the reading rule: already in LIMITS L-D4 (leading-correction cell) |
| WP7-B1 IF-B1-2 | WP4-v3 [4.5] (film S_surf "[C with images]") | "For films with d_film ≪ 1/q use the exact sheet stack (E9.1) and the finite-N_lay matrix [D]; thicker films unchanged" | S | adoption text |
| WP7-B1 IF-B1-3 | WP4-v3 L16 (and LIMITS L16) | "2D Dirac targets: the substrate enters only through v_C^{2D} = e²/(q(ε₁+ε₂)), remote bands only through r_K; never rescale the vertex (the 3D ε_bg rule is 3D only)" | S | adoption text |
| WP7-B1 IF-B1-4 | WP3-v3 (W.5); WP6-v3 nuisance typing | "Bound lines in S^{ee}_{GG′} are part of X Migdal (WP7-B1 (X8.1)), nuisance type A; the δ(ω_ph) part is X0" | W | adoption text |
| WP7-B1 IF-B1-5 | WP4-v3 [7.2]; WP6-v3 | "WP4's O(v/v*) concerns line positions (Doppler); for ω-integrated or smooth-S rates the correction is O(v²/v*²) (WP7-B1 C11); the light-mediator edge (I3.3) is halo-dependent within m_χv²/2" | W | adoption text (LIMITS LB1-12 carries it) |
| WP7-B1 IF-B1-7 | WP5-v4 §1.3 seeding (WP0-v3 (7.3)) | "New seed classes Λ: Frenkel (𝔬, 𝔵) with radiative yield; QD (e, h envelopes, MEG); Holstein (E₁, E₂, ω_ph); layer-resolved pairs; bound-Migdal (λ, p). Each is seeded by (W6) with its own P(𝐌, t\|Λ)" | S | adoption text |
| WP7-B1 IF-B1-9 | WP6-v3 §7 library | "τ strings: E8/E9/E12 `X=RPA` with `geom=1D\|2D\|stack`, rates converted from per length/area to per target mass; E5 `X=BSE;basis=molecular`; A2 sector `(2,1)`, `ref=BCS`" | N | none owed: geom key already CONVENTIONS §13 row 25 and R13 amendment (basis ∈ {crystal, molecular}); this row is the WP6 reading rule |
| WP7-B2 IF-B2-1 | WP2-v3 §4, WP3-v3 §4 | "Single-phonon absorption is LIMITS B2-L1 ((B2.1.1)–(B2.1.4)); the electron-scalar LO residue is Z − Z*/ε_∞" | W | none owed beyond the cross-reference: B2-L1 is in LIMITS |
| WP7-B2 IF-B2-5 | WP4-v3 §2, L13 | "Uniform-mode spin weight: cite the Larmor statement, the Polder factor and the λ_S rules of WP7-B2 §5 ((B2.5.1)–(B2.5.2), C7–C8; Larmor citation [FT] per CW4)" | W | adoption text |
| WP7-B2 IF-B2-6 | WP5-v4 §4; WP7-E-v3 | "SMM avalanche and chiral-band collection are detector-response functions outside S (metastable-well line); they enter through 𝒯_𝔠/𝒫_det, not the rate" | W | adoption text |
| WP7-B2 IF-B2-7 | WP5-v4 §4 | "ER colour-centre channel: WP7-B2 (B2.9.1)(b); aggregates have f_opt ≈ 0 at sub-GeV" | W | adoption text (yields: LE-151 exact gap) |
| WP7-B2 IF-B2-8 | WP3-v3 §2, §4; WP0-v3 §6.2(ii) | "Migdal-type absorption: crystal identity (B2.8.1)–(B2.8.2); medium factor +1.2×10⁻³ at 1 keV" | W | adoption text |
| WP7-B2 IF-B2-12 | WP6-v3 §7 library | "B−L in Si: isotope one-phonon term + EM-like two-phonon term, additive ((B2.4.1)–(B2.4.2)); library key per term" | N | adoption text; numbers in LIMITS "Numbers carried" (isotope B−L) |
| WP7-T IF-T2 | WP5-v4 §4, (W12) | — | — | none owed: applied in WP5-v4 (A-6, §R13.1 K9; IF-R13-4) |
| WP7-T IF-T5 | WP2-v3 (1.2); WP4-v3 §6 | "Defect vertices: host term with the corrected sign +2w_s(q̂·γ^{def}·q̂)q²/[ρ(c_l²q² − (ω+i0)²)] (WP7-T (1.2)); pole rule (1.3) for the WP4 [6.1] responses" | S | adoption text |
| WP7-T IF-T6 | WP7-D-v2 (dark photon on TLS) | "WP7-T (2.3) is the incoherent limit of dark-photon absorption on TLS; tanδ₀ inputs as LIMITS L32 (CW5-errata OC-12)" | W | adoption text |
| WP7-T IF-T7 | WP4-v3 §4.5 (films) | "Film phonon budget: include the TLS phonon mean free path ℓ_TLS⁻¹ = πP̄γ²ω tanh(ω/2T)/(ρc³) (WP7-T §2.3(a)) and the delayed release (WP7-T §5, Theorem T-1) in the film loss" | W | adoption text (CW6 film rows carry the transport side) |
| WP8-F IF-F2 | WP8-U (revised to v3) | — | — | none owed: not a frozen package; WP8-U-v3 and WP8-F-v3 rank on 𝓩_B and report both 𝓡 and m_min |
| WP8-F IF-F5 | WP8-R (revised to v2) | — | — | none owed: not a frozen package; shared property table = WP8-U-table-v4.csv |
| WP8-U IF-U2 | WP8-F (revised to v3) | — | — | none owed: superseded by IF-U2′, adopted in WP8-F-v3 §5 |

## 20. R17 final owed corrections targeting returns (CW8-FINAL merge, 2026-11-01; returns not edited)
Sources (later overrides earlier): returns/R16/CW1.md read through referees/R16/VER-CW1.md and returns/R16/CW1-errata.md §2 (the errata's re-issued text wins; "unchanged" =
CW1.md); returns/R17/WP8-errata.md §17.3 read through referees/R17/VER-ERR-WP8.md (0 FALLS; its corrections C1–C12 are folded into the text below and are themselves owed
corrections to WP8-errata); returns/R17/GAP-EF-v3-errata.md §5–§7. Type per CONVENTIONS §12: S substantive, N rename, W wording/scope. Corrections whose target is a
coordinator file were applied in this merge and are listed as pointers only: CW1 OC-1 (LIMITS L8), OC-10 (L9b), OC-11 (L3: withdrawn, text unchanged), OC-12 (SOTA C8);
WP8-errata §17.1 (LIMITS L-F1 with VER C6, L-F2, L-F4, L-H2, L-H4, L-S1–L-S3, L-EW1 with VER C3), §17.2 (NOTATION); GAP-EF-v3 E3-11, R3-4 (LIMITS L-EF4, L-EF5).
Record: returns/R17/CW8-FINAL-log.md.

### 20.1 CW1 targets: WP1-v3, WP3-v3, COMP-PH, COMP-PAER, WP8-F-v3, CONTROLS (returns/R16/CW1-errata.md §2)
| Site | Exact text | Type | Source |
|---|---|---|---|
| WP1-v3 §3.4 "Summary for WP3/WP6" and IF-6 v3 cell | "Si zero-phonon line opens at 0.405–0.408 MeV (continuum; best 0.407; 1s 0.402–0.405) [CALC, PBE+SOC, a_exp; CW1 §1, errata E-1]. It lies off the valley axis (ϑ_ZP = 0.18 rad, {001} plane, hole off Γ) and is second class by the σ_z mirror. An allowed-size zero-phonon channel ((2̄00) class, X face, \|ρ\|² ≈ 0.01–0.04 for c₁, 0.028 for c₁ + c₂) opens at ≈ 0.50 MeV and leads from ≈ 0.51 MeV. The (2̄00) vertex is not small (Σ_v\|ρ\|² = 0.150 at its extremum, light hole) [CALC, CW1 §2]. Ge: formulated (CW1 §1.4, errata E-4)." Delete "it leads only if \|ρ_cv^{(2̄00)}\| ≳ η_PA^{1/2}\|ρ_cv^{ref}\| [E, open …], otherwise the reliably allowed class starts at ≈ 0.62 MeV ((1̄11))" in §3.4, §3.7, IF-6 and R9 N1 | S | CW1-errata §2 OC-2 (VER-CW1 V2, V8) |
| WP1-v3 §3.7 table [E14] and IF-6b | replace the ϖ_II table by "ϖ̄_II (angle-averaged, (CW1.4′) of ERR-CW1, relaxed-pair vertex, SOC edge) = 0.020 / 0.16 / 0.34 at ε_ex = E_x^b / 50 / 100 meV, i.e. ≤ 0.34 at 100 meV; first heavy hole only, the cone model valid for all three (min-of-cones). Second (mirror-even) heavy hole open from 0.415–0.420 MeV, (CW1.4b), upper estimate. Pointwise at the optimum 0.01–0.04 (k_rel) + 0.03–0.10 (SOC) [vertex CALC, PAER E ×/÷10]"; the interim sentence by "PAER leads the integrated electronic rate at least to ≈ 0.42 MeV, centrally to ≈ 0.43 MeV; two-channel ≈ 0.43–0.51 (the second heavy hole dominates the ZPL side above 0.43); allowed-size ZPL opens at ≈ 0.50 and leads from ≈ 0.51 MeV (CW1 §3.3, errata E-7)" | S | CW1-errata §2 OC-3 (V10, V11) |
| WP3-v3 §M9 window bullets (1)–(3) and IF-8 v3 cell | (1) "m_χ^{PA} ≲ m_χ < 0.405–0.408 MeV [CALC, PBE+SOC]"; (2) "0.405–0.51 MeV: PAER coexisting with the forbidden-class (mirror) ZPL and, from 0.415–0.420 MeV, the second heavy-hole channel. PAER leads to ≈ 0.42–0.43, ϖ̄ per CW1 §3.2 / ERR-CW1 E-7; the allowed-size ZPL opens at ≈ 0.50, comparable"; (3) "above ≈ 0.51 MeV the allowed-size ZPL ((2̄00) class) leads; PAER/ZPL ≲ 0.1 pointwise there, 10⁻²–10⁻⁵ on the axis" | S | CW1-errata §2 OC-4 |
| WP3-v3 §M3(c) | "Si (M_x = m_l + m_hh[100] = 1.19 m_e [CALC, PBE, no SOC, CW1 §1.3]; 1.41 m_e (source not stated in WP3) is withdrawn): Q_w = 0.31 Å⁻¹ at δ₀ = 0.3 eV" | S | CW1-errata §2 OC-5 (V4) |
| WP3-v3 §M3(e), §R1 and the p̄_on table | "crossover \|q\| ≈ 1.35 keV [CALC, COMP-PH §4]; the window low-mass end is on axis"; table row "(2̄00) class: LO minimum off axis [CALC, CW1 §4] → p̄_on = 3 (TA, TO, LA, LO)"; LA kink: "SOC admixture ≲ 10⁻⁴ (on-axis geometry) and ≈ 2×10⁻³ (off-axis mirror-plane geometry) relative weight [E, transfer of the CALC ZPL-vertex lift, CW1 §13 / ERR-CW1 E-9]" (replaces "~2×10⁻³ [E]") | S | CW1-errata §2 OC-6 (V12, V13) |
| WP1-v3 §3.2(c) last bullet and §10 item 6 | "SOC lifts the Si on-axis zero to \|ρ\|² ≈ 3.6×10⁻⁶ at the extremum (Γ₈ quartet sum, gauge invariant) and 2.6×10⁻⁶ at the on-axis pair (0.4–0.5% amplitude), and the mirror-plane zero to 1.3×10⁻⁴ [CALC, CW1 §13, ERR-CW1 E-12]; Ge ≲ 10% [E] (formulated)" | S | CW1-errata §2 OC-7 (V21; R-1) |
| COMP-PH §0 row "ZPL kinematic edge" and §4 "m_ZPL = 0.4154 MeV" | "0.4154 MeV is the on-axis local optimum; the joint (q,k) minimum is 0.405–0.408 MeV off axis (best 0.407, PBE+SOC, a_exp; CW1 §1.2, ERR-CW1 E-1)"; and "the allowed/forbidden split … not computed here" → "computed in CW1 §2" | S | CW1-errata §2 OC-8 |
| COMP-PAER §0 item 1, §4 table, IF-CP-1 | COMP-PAER's "first zero-phonon final state 0.405–0.408 MeV (continuum)" is **kept** (now [CALC, CW1/ERR-CW1: 0.407 with SOC, re-minimised]). Add: "allowed class (2̄00): 0.547 MeV is the nearest-pocket assignment; the allowed-size channel opens at ≈ 0.50 MeV on the X face (CW1 §2.3)" | W | CW1-errata §2 OC-9 (V3) |
| WP8-F-v3 §2.7(b) (window FOM Δm/m) and COMP-PH §0 row "window FOM" | use E^{ZPL}_min(q* = 0.90 keV) = 1.727 eV (DFT, PBE+SOC, a_exp; not re-minimised, ≲ −1 meV expected; 1.697 eV Wannier a_PBE scalar at ϑ = 0.34 rad, not 1.715 from five directions) and recompute Δm/m | S | CW1-errata §2 IF-CW1-3 (V32) |
| COMP-PAER tier H (owner of DC-1), stage-6 output grid | "the stage-6 output grid must include the {001} mirror-plane cones (§3.3), the **second heavy-hole cone on the axis** (E-7c), and the X-face (2̄00) edge with c₁ and c₂. ZPL vertices with the hole at k_v(q), pair relaxed; bands with SOC" | S | CW1-errata §2 IF-CW1-4 |
| WP6-v3 nuisances (WP1 IF-3) | IF-CW1-5 text verbatim (relaxed-pair q coefficient \|∂_{q_z}ρ\|_rel\| = 1.57 Å, \|∂_{k_z}ρ\| = 0.32 Å, SOC-lifted 1.3×10⁻⁴; second heavy hole, on-axis edge 0.415–0.420 MeV, g_⊥ = 2.21 Å; the on-axis (n_H² − 1)/(3πa_x⁵n_H⁵) form is the on-axis special case) | S | CW1-errata §2 IF-CW1-5 |
| COMP-PH Ge §6.2 (DC-2 owner) | "Ge thresholds must use the joint (q,k) minimisation (CW1.1) (scripts/emin_fast.py) and check the σ_d mirror rule at the optimum; the parabolic 0.32–0.36 MeV is not a reliable bracket", plus "SOC in the bands and the DFT re-minimisation of ERR-CW1 E-1; no anisotropy-based lowering is transferred from Si (E-4)" | S | CW1 IF-CW1-2 + CW1-errata §2 |
| CONTROLS.md C8 bracket (coordinator copy outside the write set of this merge) | "PAER-leading GaAs only at m_χ ≈ 0.43–0.51 MeV [E, parabolic; CW1 §24], full q integral; band-structure check formulated" (SOTA copy applied) | S | CW1 OC-12 |
| CW1.md §0 counts line | "Counts: CLOSED 15, CLOSED-AS-EXACT-GAP 11" → "CLOSED 14, CLOSED-AS-EXACT-GAP 12" (the per-row cells of §0 / errata §2) | W | this merge (LOOSE-ENDS §4) |

### 20.2 WP8 targets: WP8-U-v3 / table v4, WP8-F-v3, CW7-errata, WP8-S-v2, WP8-errata itself (returns/R17/WP8-errata.md §17.3 with VER-ERR-WP8)
| Site | Exact text | Type | Source |
|---|---|---|---|
| §19.13 (WP8-U) row (a): v4 `screen_S1` rows | "dropped non-[E] rows are GaAs S1 and SiO₂-q S1 (not 'two GaAs rename rows')" | W | WP8-errata §2, §17.3(a); VER #2 |
| §19.13 row (b): §0 row 10 / build_v4.py | cyclic shear mis-indexing text of WP8-errata §1; CW7-C33 tolerance 0.11 → 0.05 (VER #1: the 0.05 equals the observed maximum, not a margin) | W | §17.3(b) |
| §19.13 row (c): v4 `cosmo_EC_lines_subkeV` (Ge); CW7-errata §1.11; WP8-U-v3 §4.4 l.163–164 | "K lines ≈ 5–11 keV; the dominant ⁶⁵Zn, ⁶⁸Ga, ⁶⁸Ge, ⁷¹Ge L-lines (1.10–1.30 keV) lie above 1 keV; the L-lines of the lighter-daughter EC nuclides (⁴⁴Ti/⁴⁴Sc (Sc/Ca daughters, lower still), ⁴⁹V, ⁵¹Cr, ⁵⁴Mn, ⁵⁵Fe, ⁵⁶⁻⁵⁸Co; ≤ 0.61–0.87 keV for the Ti…Fe daughters from the E_L/E_K trend of 1607.04560 Table 1, an extrapolation [E]) and all M-lines (~0.1 keV) are inside the sub-keV ROI; ⁴⁴Ti/⁴⁴Sc production in Ge is not given in the paper (unquantified)" | S | §10, §17.3(c) + VER C7 |
| §19.13 row (d): WP8-U-v3 §0 row 7, §5 | "1910.10716 Table I c_LA: GaN, AlN, ZnO and CsI CONFIRMED inconsistent with measured elasticity (GaN, AlN, ZnO above every Christoffel LA speed [FT 1110.1346 p.2, cond-mat/0507217 p.7]; CsI below √(B/ρ) with measured B [FT cond-mat/9408044 p.18]); **CaWO₄ 8.4% below the measured sphere-averaged LA speed and below the slowest LA direction: CONFIRMED inconsistent**; α-SiO₂, NaCl pending" (replaces "CaWO₄ 2.3% below its measured LA range (marginal)") | S | §12, §17.3(d) + VER C9 |
| §19.13 row (e): CaWO₄, CsI `c_LA` rows; new rows | CaWO₄, CsI `c_LA` rows superseded for ranking by WP8-errata §3–§4; add `C_ij_exp` CaWO₄ [FT 2508.08858 p.16, quoting its ref. [73] (Farley & Saunders 1972, ultrasonic, 1.5–300 K; the temperature of the quoted set is not stated; also used by its ref. [63], Malkin et al. 2017)] and `B_exp` CsI 13.5 GPa [FT cond-mat/9408044 Table I p.18, isothermal room-T EOS fit, its ref. [11]; ρ_T 4.529 g/cm³ from a = 4.567 Å]; CsI elastic constants owed data = DEFERRED-COMPUTE DC-93 | S | §17.3(e) + VER C1, C3 |
| §19.13 row (f): C (diamond) | `screen_S2` PASS and `verdict` SURVIVOR under CONVENTIONS row 38 [FT 2310.05815]; array caveat row | S | §13.1, §17.3(f); VER #13 |
| §19.13 row (g): Al, Ir, YIG | state/DATA-ADDENDA.csv supersedes v4 Al tensor-derived rows (`c_L_iso`, `c_T_iso`), ρ-derived rows (`n_e_val`, free-electron rows), christoffel_v4 Al/Ir entries, YIG `a_exp`, `rho_T_from_a_exp`, `n_e_val`, 𝓃_spin (×1.045) (VER #14: 0 K C_ij with room-T a, −0.6% in c, negligible) | S | §17.3(g) |
| §19.14 (WP8-F) heavy window: §0 NR-1ph row, §2.3(a″), §5.1 | the LIMITS L-F1 text of this merge (pairwise W_AB as the contiguous range where \|(R_A/R_B)(c_A/c_B) − 1\| < 0.1, capped at min(m_hi,A, m_hi,B); per-material onset 4.7–5.7 m_min^{ac}, ≈ 4.2 against Si for the softer material; u₋ ≈ 0.21 v_max; first-order η(c + u) shift, diamond/Si −7%); replaces both the WP8-F-v3 "0.1 ≲ m_χ ≲ q_BZ/(2v_max)" and the WP8-errata §6 "m_on ≈ 4.2 m_min^{ac}(c_NR1) (4.0–4.5 over the survivors)" and its W_AB = [max(m_on), min(…)] definition | S | WP8-errata §6 + VER C6(a)–(c) |
| §19.14 light mediator: §0, §2.3(a″), §5.1 | WP8-errata §7 replacement texts verbatim ((EW-7.1), κ_η = 3.14; "target-independent for m_χ ≫ (1 + κ_η)m_min^{ac} of every compared material; material factor spread ×1.08 at large m_χ") | S | §7; VER #7 |
| §19.14 ε-route: §2.5, IF-ERR7-1, IF-F1′ | WP8-errata §8 text (interlacing hypothesis; (8.1) interval for ε-only materials; sapphire σ 3%) | S | §8; VER #8 |
| §19.14 r^M status: §2.6, §4 | "[D] as the LSWT transverse sum-rule defect ΔS/S; [E] (lower estimate) as the one-magnon width" | W | §9; VER #9 |
| §19.15 / CW7-errata §1.12 (G-F6 spec) | WP8-errata §11 text with "Σ_ν over the 3N modes and e_κν normalised on the κ sublattice" → "e_ν normalised over the cell (Σ_κ\|e_κν\|² = 1); completeness then gives Σ_ν\|e_κν\|² = 3 per k, i.e. ∫D_κdω = 3"; state the k-average (1/N_k)Σ_k and the per-cell count of κ atoms | S | §11 + VER C8 |
| §19.15 / CW7-errata §1.1, §1.4, §1.7, §1.11 | dropped rows (§2); commensurate-grid pitfall (§5); r^M (§9); EC lines (row (c) above) | S/W | §17.3 |
| WP8-S-v2 (new §19.18 of WP8-errata §17.3) | "read through WP8-errata: §0 rows 3–5, 8; §1.3 (r_mat wording, Si ε_eh, sapphire width); §1.4 (117 tiers); §2.3 (window per LIMITS L-F1 of this merge, CaWO₄, CsI, R10, R13); §2.4 (NR edge: C leads S, Al₂O₃ second); §4 ER-quanta row; §5 (readings replaced by WP8-errata §16.3; statement (ii)); §6 item 1 (spec §15 as corrected below), item 2; L-S1–L-S3. code/REV-WP8-S/data/ranking_v3.json supersedes ranking_v2.json." | S | §17.3 |
| WP8-errata §15 (L(k, ω) spec) | add: the k-domain of 𝓠_Mig is the 1BZ Wigner–Seitz cell (2011.09496 Eq. (6) valid for k ∈ 1BZ; not a sphere of 5 keV; the 0–5 keV range is for ER only), with "WS cell vs inscribed sphere" as a convergence item; pitfall (e) "the BSE rung bounds it" → "the BSE rung computes it". With these the gap is CLOSED-AS-EXACT-GAP (run = DEFERRED-COMPUTE DC-28) | S | VER C10 |
| WP8-errata §16.4 (next-target guide) | PbSe and PbS "Missing demonstration": add "mK operation (S1 COND) and phonon readout (S3 COND)"; PbTe: add "S3 readout"; h-BN: "S2 FAIL rests on an [UNVERIFIED] v4 row"; relabel the diamond C_ij, LiF ε₀, GaSb low-T gap, TeO₂ C_ij and CsI C_ij cells "literature read (IF-EW-3)", not measurements | W | VER C12 |
| WP8-errata §0 header, §3, §17.3(e) (CaWO₄ source) | "quoting J. M. Farley & G. A. Saunders … via its ref. [63]" → "quoting its ref. [73] (Farley & Saunders 1972, ultrasonic, 1.5–300 K; the temperature of the quoted set is not stated; also used by its ref. [63], Malkin et al. 2017)" | W | VER C1 |
| WP8-errata §4, L-EW1 (CsI B₀) | B₀ is an isothermal room-T EOS fit (not the adiabatic B_S); L-EW1 leading correction: append "B_T (EOS fit) vs B_S (adiabatic) and T-dependence: ±7% in B, ±4% in the floor" (σ_ln(B) 0.07 covers it); cite a = 4.567 Å for ρ_T 4.529 | W | VER C3 |
| WP8-errata §0 header, §18; code/CW7/cascade_gf.py docstring; checks.py header | docstring "biased by −1.7% at h = 0.02" → "−1.61% (CW7-C5c)"; restate the runtime as measured (VER-ERR-WP8: 574 s; CW8-FINAL rerun: 16.6 s, 41/41 PASS) | W | VER C4 |
| WP8-errata §5 and IF-EW-1; its rows at l.454 and l.518 | "GAP-EF-v2 did not use h = 0.02: model.grid held \|w_eff/w_ph − 1\| < 1% (and θ_ii = 3/2 was rounded on odd N). Rerun on the commensurate solver (code/GAP-EF-v3, returns/R17/GAP-EF-v3-errata.md): ε_eh moves by ≤ 0.06% (V0), ≤ 0.19% (V1), F_eh by ≤ 0.13%; Si F = 0.114 and its 2.6σ [book: 2.5σ at E_g = 1.160 eV, consistent with the DC-67 referee] stand." Rows "Si +1.3% in ε_eh" → "**closed**: ≤ 0.19% (GAP-EF-v3)" | S | GAP-EF-v3-errata §7 |
| code/REV-WP8-S rank.py / ranking_v3.json | drop `runtime_s` from the JSON so that S2-C15 can pin v3 by md5 (rank.py rewrites ranking_v3.json with a different md5, content-equivalent) | W | VER C11 |
| status of the chain | WP8-U-v3, WP8-F-v3, table v4 + WP8-errata, WP8-S-v2 + ranking_v3: **VERIFIED** (VER-ERR-CW7, VER-ERR-WP8; CONVENTIONS §13 row 36 condition met); IF-EW-6 (R×2 of WP8-errata) answered by VER-ERR-WP8 for this merge | W | brief CW8-FINAL; VER-ERR-WP8 |

### 20.3 GAP-EF-v2 → GAP-EF-v3 (returns/R16/GAP-EF-v2.md, GAP-EF-v2-errata.md)
| Site | Exact text | Type | Source |
|---|---|---|---|
| GAP-EF-v2.md, every printed model number | read through returns/R17/GAP-EF-v3-errata.md §5 (R3-1…R3-18): its grid-commensurate numbers supersede GAP-EF-v2's last digits (𝒜_ph 5.588 eV³; residual max +24.7%; (EF9) 2.329, 0.965; (EF10) coefficients; predictions table, 18 rows); F_Si 0.114, 2.6σ [book: 2.5σ at E_g = 1.160 eV, consistent with the DC-67 referee], rms 12.3% stand | S | GAP-EF-v3 §4–§5 |
| GAP-EF-v2-errata.md | read through GAP-EF-v3-errata §6 (E3-1…E3-12); code/GAP-EF-v3/data/results.json supersedes code/GAP-EF-v2/data/results.json | S | GAP-EF-v3 §6 |
| GAP-EF-v2 (EF11) check and errata C15 | "solver FD dε/dE_g = 1.777, (EF11) 4.6% low" → "FD 1.699 at the true ω₀; (EF11) 1.694, 0.3% low" (v2's FD was an ω₀-grid artefact) | S | GAP-EF-v3 §0 item 8 |
| GAP-EF-v2 discretisation wording | "≤ 0.05% (Si), 0.12% (C)" → errors at the production grid Si ε +0.064%, F −0.071%; C ε +0.19% (quadrature O(h^{3/2}) with phonons, O(h) at λ_ph = 0) | W | GAP-EF-v3 R3-1 |
| code/GAP-EF/cascade.py (v1) | carries the same rounding; v1 is superseded, no rerun owed | W | GAP-EF-v3 §7 |
| CW1.md §25 (CW1-L9) and every quote of the Si nonadiabatic ZPR correction | "≲ 2 meV (own estimate, 0.12 eV vertex)" → 8 meV (Poncé et al. 1504.05992 Table VI: −64.3 meV adiabatic vs −56.2 meV nonadiabatic, one calculation); the window bound ≤ 0.002 MeV is unchanged because the window uses the measured gap | S | book 13.7 (2026-11-06) |
| l.314, l.335 "allowed ZPL from 0.547 MeV" | read through l.575: 0.547 MeV is the nearest-pocket assignment; the allowed (2̄00)-class line opens at ≈ 0.50 MeV (book 13.9, Table 13.1) | S | book Ch13 review (2026-11-06) |
| CONTROLS C8, SOTA GaAs window "0.43–0.51 MeV" | GaAs PAER-leading band 0.43 → 0.52–0.56 MeV with E_L = 1.815 eV (low-T); the earlier 0.51 used E_L ≈ 1.71 eV | S | book 13.9 (2026-11-06) |
| interim local-field/pair factor [0.4, 1.8] | its inputs (pair ≤ ±0.5, unsigned LF ≤ ±0.2) conflict with book 13.4 (pair-channel limit 0.07–0.12; signed LF +25–31 %); being rebuilt relative to the measured optical edge (book Ch13 ruling R2); the result is entered here when the revision returns | S (open) | book Ch13 review |
| interim factor [0.4, 1.8] (resolves the open row above) | → screening correction relative to the optical calibration: external factor 0.60–1.45 × local-field wings 0.55–1.77 = 0.3–2.6 [E] (book figscripts/ch13/interim13.log, verified postrev-check). The pair channel cancels at pinned momentum (≤ 4×10⁻³); the residual from the 0.2 keV pair-momentum spread above onset is unsized | S | book Ch13 R2 |
| COMP-PAER rate-estimate reach (Macfarlane 20 K cold edge) | the book's primary cold edge is the Stanford et al. 0.5 K fit: σ̄_e (3 ev, 1 kg yr) heavy 3e-30 (0.36 MeV, quoted as band 3e-30–3e-29, ×15: 55 % of the rate lies below Stanford's lowest diode energy 1.206 eV) and 4e-32 cm² (0.40); light 1.4e-32 and 2e-34. Old values (3.1e-29, 7e-32, 1.3e-31, 3.9e-34) are the spread. ZP/PA ratios and lead masses unchanged | S | book Ch13 R5 + postrev F1 |
| Si nonadiabatic ZPR split | 6.1 meV VBM / 1.9 meV CBM (Poncé Table VI: 40.87 → 34.75; −23.28 → −21.43), not 6.0/2.1 | W | book Ch13 R7 |
| Si cold excitonic edge | 1.1728 eV with E_g(0) = 1.1692 eV book-wide; 1.1736 retired | W | book Ch13 R5 |
| WP4-v3 §2.3 magnon–phonon hybrids | built from exchange striction (∂J/∂u); about a collinear state that term has no part linear in the bosons, so it couples a phonon to magnon PAIRS only. One-magnon–one-phonon mixing comes from the magnetoelastic (spin–orbit) term (Kittel 1958; Rückriegel et al. 2014 Eqs. (3.23), (3.25)) | S | book 14.2 (2026-11-06) |
| WP4/campaign MnF₂ ω_M/ω_E (shape shift) | 1.6e-2, not 1.3e-3 (Vaidya's M_s = 47.7 kA/m is M/4π; SI μ₀M = 0.74–0.75 T). Reference values: measured AFMR 1.1 meV, spin flop ~9.4 T; the fitted fields (1.021 meV, 8.75 T) are 7 % low | S | book Ch14 review |
| YIG zone boundary 987 eV | uses the superseded a = 12.56 Å; with a = 12.375 Å: 2π/a = 1002 eV, inscribed radius 708 eV; every q inside the zone below 134 keV (not 186) | W | book Ch14 |
| NiO magnon speed c_M = 1.39e-4 | the J₂-only value; J₁+J₂ gives 1.29–1.36e-4, edge 7.3 keV, two-magnon gain 5.1 | W | book Ch14 |
| Aybas et al. μ₀M₀ | 2.9 nT is the equilibrium (computed) value; measured 1.9 nT | W | book Ch14 |
| ΔS/|S| "lower bound" on the one-magnon defect | an estimate at leading order (the ground-state change at the same order is excluded) | S | book Ch14 R1 |
| Neutron no-go for q̂·S·q̂ | holds model-independently only; within localized moments, transverse data at several q+G fix the full tensor | S | book Ch14 R2 |
| t_coh convention | 1/(m v₀²) = 1.04 ms at 1 µeV (App. E.26 had the 2π form, 6.6 ms) | W | book Ch14 R4 |
| YIG uniform-mode exchange mass | 3.25 MeV from the book's D_sw (Chigusa et al. ~3.5 MeV) | W | book Ch14 |
| CW4 (8.1)/SPINE superconducting edge table (0.33–0.40 … 0.94–0.96) and the type-Δ "KK spread" nuisance (l.343, l.391) | these are bare-bubble values, so not physical. Use the conserving response (DC-41): clean 0.867/0.999/1.069/1.067/1.023 at y = 2.2…10 (book v_F); impurity range 1.008–1.091 for y ≥ 3; edge remainder two-sided −2 % to +9 % for y ≥ 3 | S | book Ch15 |
| Al free-electron constants (v_F = 6.67e-3 / 6.8e-3 in SPINE, SOTA, DC-41 𝔩_e labels) | one set, m* = m_e: v_F = 6.753e-3, E_F = 11.65 eV, ω_p = 15.78 eV, k_TF = 4.05 keV. DC-41's Γ → 𝔩_e conversion used 6.8e-3 (labels change by 0.6 %) | W | book Ch15 R1 |
| SC exclusion mask y < 3.8 (bare first-order term) | y < 3 (≤ 10 % variation of the conserving edge value over 𝔩_e = 30 nm–100 µm) | S | book Ch15 R2 |
| CW4 thresholds 9.4/8.2/6.5/2.3/0.049 | grid artefacts → 9.1/7.9/6.3/2.25/0.050 (book v_F) | W | book Ch15 |
| Al elastic constants (room temperature) in book s6-4 (a2F force-constant fit) and C-18 l.106 | superseded by DATA-ADDENDA (C11 114.3, C44 31.6 GPa; §19.13(g)); refit owed at the next Ch6/App. C pass | S (open) | book Ch15 |
| Zhang et al. (1607.07854) Table I N₀ for x = 0.85 | inconsistent with their R_s and D (Einstein relation 3.3e47/3.0e47 vs 4.1/3.8) | W | book Ch15 |
| §19.13(g) Al 0 K elastic constants convention | sound speeds from the 0 K constants (Malica–Dal Corso) with ρ(0 K) = 2.73 g cm⁻³: c_LA = 6.47, c_TA = 3.40 km/s; rates keep ρ = 2.70 g cm⁻³ | W | book Ch15 post-check |
| Campaign return (molecular crystals, binned-sum corrections) | mixing with other manifolds changes the binned |f|² sum at FIRST order in 𝔍/ΔE (intensity borrowing), not second order | S | book 16.4 (2026-11-06) |
| v4 rows 1543/3182 (ZrTe₅ Δ_D) | book adopts 11.8 meV (NR half-gap) central, with 15.6 (ISIF7) and 17.5 meV (Ref. [21] row) as the computed range; conflict resolved for the book | S | book Ch16 R1 |
| Campaign DM–TLS rate 3.7e-2 (WP7-T) | book: 2.3e-2 /(kg·day·meV) with Golding's C_l = 1.9e-4 (3.1e-2 with the averaged C = 2.6e-4; 3.6e-2 with C = 3e-4 and the book halo); the remaining difference is the halo escape cut | S | book Ch16 R2 |
| Graphene Dirac velocity | book-wide v_D = 3.02e-3 (t = 2.8 eV) | W | book Ch16 R4 |
| LiF exciton-route F–H threshold | 4.0 MeV is an upper bound (from the gap); the exciton-energy value is unsourced | W | book Ch16 R6 |
| book 12.3/12.4/D.33 diagonal self-lattice Migdal form (eq:12.3-soft, eq:12.4-harm, eq:D.33-diag) | valid for the incoherent/impulse regime (q ≳ 2 q_BZ). For the coherent zero-phonon response at q ≪ q_BZ the Ch8 boost identity binds; the diagonal form is high by ~15 as q → 0 (screening, the head of ε⁻¹; the dropped terms are the I ≠ I′ coherence), with the wrong spectrum (median 4.5 vs 17.4 eV). The identity is quantitative only below ~0.75 keV. No printed number changes (< 0.75 keV carries ≤ 0.2 % of the Si Migdal rate). The ×1.2–1.4 off-diagonal estimate stands in its regime | S | book Ch12 erratum review (2026-11-06) |
| NiO magnon edge (Ch17 draft 7.16/8.05/317 keV, J₂-only c_M) | 7.31/8.20/316 keV with c_M = 1.36e-4 | W | book Ch17 |
| ZrTe₅ absorption in Ch17 | measured-structure row: ζ(100 meV) 1.25e-15, factor 6.3–6.4, cone end 0.38 eV, dark-photon gap 0.38–1.17 eV | W | book Ch17 |
| Griffin et al. Table I CsI | bulk-modulus floor 25 % above the tabulated speed (not 20 %); ZnO ratio 2.05 | W | book Ch17 |
| GaAs interference (book WE 17.4) | 403×/521× without the cross cell; 216/245 are vs bare nuclear charges | W | book Ch17 |
| book 12.3/12.6 σ_n (per-nucleon) | clashes with 15.4 σ_n (conductivity); Ch17 uses σ_p; fix 12.3/12.6 at their next pass | N | book Ch17 |
| Si carrier-cascade calibration (research A_AB 5.588; Ch18 draft 5.674) | one continuum-calibrated set A_AB = 5.703 eV³ at E_g = 1.160 eV (R&K's eV² unit is a misprint); F_eh 0.114 at 2.4σ below 0.119 | W | book Ch18 R1 |
| Klein relation | Shockley balance + two assumptions; the uniform-population assumption overstates the phonon-free ε by 36–39 %; within 10 % of the cascade only for λ_AB 0.65–84 | S | book 18.4 |
| Step model near threshold | overcounts the two-pair probability ~10× at 5 eV (≥ 6× robust; full-band R19) | S | book 18.3 / R19 |
| casc18_3.py above ~55 eV | Gat extrapolation beyond the grid top + NZ aliasing; guards added; printed ≤ 51 eV values unchanged | W | book Ch18 |
| WP-campaign toy 𝔯_coll 0.87–0.98 (transport sign) | an artefact of cutting the Luke spectrum at its energy-grid edge (sub-gap share 0.118 vs 0.017–0.058); book 20.5 (final): 𝔯_coll 0.81–1.02 with energy conserved (0.82–1.01 at 0.84 meV); the sign is not fixed | S | book 20.5 |
| WP7-E calibration chain (CDMS phonon-yield ratio) | depends on ε_eh: the reconstruction uses 3.82 eV while Luke phonons follow the true 3.75 eV (book). Stored-only 0.042 (95 % edge 0.049); collection-only 𝔯_coll 1.128 [1.099, 1.152] (Lindhard 1.134; yield from the source's fit y_C = 0.324 at 20 keV); 40 V: 0.919/0.947/0.932; bound 0.055 under (a)–(e) with (e) ε_eh ≤ 3.82 eV, 0.049 with the book ε. Collection alone (1.128) is not reached by the 20.5 transport estimate (0.81–1.02, energy conserved) but not excluded until computed real-detector kernels; the two-bias measurement decides | S | book Ch19 R1/R2 |
| Lindhard yield soft-collision "13 % band" | a sensitivity to the cross-section continuation exponent (−11/+13/+39 % at 1 keV for 0.30/0.363/0.40), not an uncertainty; the ε^{1/6} law follows from the x^{1/3} continuation | W | book 19.3 |
| Si mean excitation "L shell 2/3" | withdrawn (unit-dependent normalisation); the data give 161 eV | W | book 19.3 |
| Displacement count (NRT 0.8) | 0.70 with the screened cross-section; NRT 11–14 % high for T_d ≥ 10 E_d | W | book 19.4 |
| book Ch19 "collection alone disfavoured (transport ≤ ~1.09)" and the WP7-E calibration row | FINAL (Ch20 R1 rework): mean-field 𝔯_coll with energy conserved (every phonon a film emits returned, both films; one Al film or Nb-like + Al; 60 nm to thick; sub-gap lost or absorbed) is 0.81–1.02 over ⟨E_L⟩ 0.75–4.7 meV and 0.82–1.01 at 0.84 meV (Si electrons, 1 V/cm); one Al film 0.96–1.02, two films 0.81–1.01; ε_prim 0.684 (two thick films); a uniform signal-free sink (bare loss up to 0.3/hit) keeps it ≤ 1.023. Only a selective sink (lumped film: phonons emitted after the first pair break deleted) gives 1.05–1.10 (≈300 nm) and 1.30–1.53 (60 nm), an upper envelope with no physical sink identified. Collection alone (1.128) is not reached by the transport estimate; not excluded until computed real-detector kernels (E.25); the two-bias measurement decides. Ch19 (19.4, 19.5, summary, F row) amended | S | book Ch20 R1 rework; Ch19 amendment |
| Ch20 first-pass film-escape 𝔯_coll (values above ~1.05: 1.05–1.13 one Al film, 1.30–1.53 at 60 nm; two-film 0.91–1.09, ε_prim 0.610) | non-conserving: the escaped phonons (and all phonons a film emits after its first pair break) were deleted instead of returned to the crystal, and the second (Nb-like) film's relaxation phonons were dropped. With both returned, no mean-field case exceeds 1.02 (uniform sink ≤ 1.023); the deleted-phonon values are kept only as a selective-sink upper envelope | S | book Ch20 postrev-check / R1 rework |
