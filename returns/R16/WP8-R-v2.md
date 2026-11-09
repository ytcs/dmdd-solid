# R16 / WP8-R-v2: phonon collection as an NR/ER discriminant (revised go/no-go screen)

Revision by CW6 (brief briefs/R16/CW6.md, row LE-20), 2026-11-01. **Standalone: it replaces returns/R13/WP8-R.md.** It absorbs referees/R14/REF-WP8-R-A.md ("A")
and REF-WP8-R-B.md ("B"), the WP8-R rulings of returns/R14/WP5-AUD.md §5.1 ("AUD", R-a…R-i, D-7…D-10), their reconciliation in returns/R16/CW5.md §1 (LE-22,
OC-7, OC-8) and §2.5 ((CW5-3), (CW5-4)), and the CMPMC flags IF-AUD-2…4 of returns/R15/CMPMC-AUD.md. The closing table (§9) has one row per referee item.
**Checks:** `code/CW6/checks.py`, **44/44 PASS in ≈ 17 s** (numpy, scipy, sympy; deterministic, no Monte Carlo), cited **CW6-Kn**. Stage K1 reproduces
v1's published numbers with v1's own conventions; K2–K8 apply the corrections. v1's checks (code/WP8-R, WP8R-Cn) remain valid for the quantities that are
unchanged here, and they are re-derived in K1.
**Literature [FT]**, read in literature/papers-CW6/ (arXiv IDs and titles verified against the arXiv API; PDFs deleted): 1109.1193, 1109.4343, 1401.1937,
1805.02495, 2012.12430, 2303.02196, 2408.04732, 1901.07569. Page numbers are PDF pages. Kaplan (1979), Little (1959), Swartz–Pohl (1989) and Tamura (1983)
are not on arXiv and were **not accessed**. The AMM formulas they would supply are **derived here** (§3.2, [D]), so no LIMITS row rests on them.
**Symbols (renames against v1, per NOTATION and A N1–N4, B §C):** g → g_Luke, r → r_coll, δ → δ_coll, δ_prim → δ_coll^{prim}; 𝔖 → 𝒮_sep, 𝔖_int → 𝒮_int
(𝔖 is NOTATION's Ward generator); O → O_obs; Ω (phonon energy) → ω_{Qν}; f_D ≡ ω_D/2π (ħ = 1 energies in meV are quoted as hf). 𝔶 is kept, with the
WP5-AUD definition 𝔶(E_R) ≡ ⟨N_eh⟩ε_eh/E_R (created-charge yield) and **y_ion = 𝔶⟨𝔮⟩_NR/⟨𝔮⟩_ER** (A-5); numerically the measured Y of 2303.02196 is used for 𝔶
(it is a created-pair yield there up to ⟨𝔮⟩ and the ε = 3.8 eV convention). 𝒜_anh, 𝒜_iso are kept with ⚠ (bare 𝒜 is a halo index; subscripted forms
do not collide). [DB] is the CONVENTIONS R13 amendment rank ("[DB] below [FT]").
**Status:** CLAIMED (revision). The yield-dependent sites inherit WP5-AUD's status, now REFEREED once CW5 OC-1…OC-8 are applied.

---
## 0. Verdict at a glance
| # | Question | Result (v2) | Tag |
|---|---|---|---|
| 1 | Do NR and ER prompt populations differ at birth? | Yes: in branch mix (both hard: optical/zone-boundary, f ≈ 8–15 THz in Si, ≤ f_D = 8.64 THz in Ge) and by an ER-only **soft fraction** f_s ≈ ω_op/ε_eh = 1.7% (Si), 1.2% (Ge). f_s uses a uniform residual on [0, ω_op] and 1805.02495's "Debye energy" 62 meV as ω_op proxy. **Plus the gap-energy population** (§1.2): (1 − 𝔶)𝒢_gap = 0.28 of E_R (Si, 𝒢_gap ≡ E_g/ε_eh = 0.312), released later and at a site set by the kinetics | E |
| 2 | Memory time and length | Hard-part spectral distance < 10⁻³ by **t_mem ≈ 10 ns (Si), 30–100 ns (Ge)** (Ge TV 0.022 / 2.5×10⁻³ / 4×10⁻⁴ at 10 / 30 / 100 ns, CW6-K4a); ≥ 650 (Si) / 5000 (Ge) mode-mixing events by 1 µs; r_rms ≲ 80 µm (Si), 16 µm (Ge) at 100 ns. **Scope:** bulk Si/Ge (not Al₂O₃, §2.5), prompt populations only, events farther than r_rms(t) from an instrumented face (≥ 96% of a 4-mm device at 100 ns, CW6-K4b) | D (f_*(t) scaling, N_mix, r_rms) / E (toy cascade) |
| 3 | Interface and sensor selectivity | Isotropic AMM is frequency-independent for λ ≪ d_film; flux-averaged L/T contrast **1.06 (Si/Al), 0.75 (Ge/Al)** (normal incidence 1.03/1.07; Ge/Al L critical angle 56.4°) (CW6-K5e). η_pb(ω_{Qν}) is **not** flat above 4Δ_BCS: it rises to 0.59 near 6Δ in the no-loss limit and falls with ω in thin films (1401.1937 p.5; CMPMC-AUD T8). The detector's main frequency selector is **mean free path × coverage** (1109.4343 p.2), not the interface | D (AMM) / FT / E |
| 4 | (a) Mode/frequency/angle selection of the primaries | **NO-GO**, conditional on σ_pos ≳ 1% and on ζ_O ≪ 1 for any soft-vs-hard selector (the soft band 0.3–1.4 THz overlaps the arrival band 0.7–2.7 THz). With σ_pos = 0 and ζ_O = 1 the §4.1 convention gives 2σ at **0.36 keV** (0.44 keV with σ_Nph), 1.2 keV at ζ_O = 0.3 (CW6-K2) | D given §2 / E |
| 5 | (b) Zero-field gap-energy channel | **UNRESOLVED** (not NO-GO). Readable as a two-window (timing) or fast/slow observable: ΔO_b = 𝒢_gap(r_g^{ER} − 𝔶r_g^{NR}) (CW6-K3k, from (CW5-3)); 𝒮_b(100 eV) = 8.2ζ_gap-scale at σ_pos = 0, 4.6 at σ_pos = 0.05 (ζ_gap = 1), ζ_gap,min = 0.42 at σ_pos = 0.05. Its sign can flip with a bimolecular NR tail (CW6-K3l). Decisive input: r_g^{NR,ER}(t) and release site (G-R2) | D (algebra) / E |
| 6 | (c) HV/NTL mode (≥ 100 V) | **CONDITIONAL NO-GO** at E_R ≤ 300 eV: firm at the central measured Y, F_NR (2303.02196) and at E_R ≲ 220 eV (1σ); at the 1σ corner the pair-number ceiling is 2.014 with the source's ε = 3.8 eV (1.999 with 3.75) (CW6-K3f, K3j; CW5 OC-7) | D (algebra) / E (inputs) |
| 7 | (d) Low-bias phonon-read NTL route | **CONDITIONAL, not GO.** It is the ionization-yield discriminant read out with phonons, bounded by the yield's own pair-number ceiling, with 𝔶 underived below 352 eV. ζ_O,min(100 eV) = **0.13/0.24/0.44** at σ_pos = 0.02/0.05/0.10 (measured Y, F_NR, F_ER = F_meas^{obs}, σ_Nph, ζ_gap = 0); ζ_gap = ∓ζ_O moves the middle value to 0.27/0.21 (CW6-K3c, K3d). The CDMS calibration transfer is withdrawn ([C], no physical support) | E |
| 8 | IF-E7 (δ_coll, r_coll) | **δ_coll^{prim} ≤ 0.007–0.012** only. The gap-release part δ_coll^{gap} = (1 − y_ion)𝒢_gap(ρ_g − 1)/[1 + 𝒢_gap(ρ_g − 1)] (exact, CW6-K8a) gives the whole 0.048 for a 24% gap/hard collection contrast ρ_g − 1 (K8b): **δ_coll can carry the deficit.** r_coll ≠ 1 expected, sign open; a mean-field toy gives r_coll = 0.87–0.98 (K7c), so WP8-R **does not support (B-b) r_coll ≥ 1**. A bias scan of η^φ_NR breaks the r_coll/(δ_coll + E_st) degeneracy (K8c) | D (algebra) / E |

**Overall.** **NO-GO for mode/frequency/angle selection of prompt populations in bulk Si/Ge** (rows 4, 6). The zero-field gap-energy channel (row 5) is
**UNRESOLVED** pending the release law and site. (d) is a phonon-readout variant of yield discrimination, CONDITIONAL on ζ_O, σ_pos, ζ_gap and 𝔶(< 352 eV).
The reason for excluding (d) from "GO" is **not** that it lacks an interface effect (its ζ_O comes from a frequency-cut film); it is that its intrinsic limit is
the yield's pair-number ceiling, so it does not work "where yield fails" (A F9, B B4).

---
## 1. Initial populations at equal deposited energy
**1.1 Ledger.** WP5 (W4) as amended by A-1: **ω + 𝒲_bias(t_pr)** = N_e^f(E_c − μ_F) + N_h^f(μ_F − E_v) + E_X + E_trap^{pr} + E_es + ℋ + E_st + E_esc (AUD R-a; 𝒲_bias(t_pr) = 0 at
zero field). Prompt phonon part: ℋ ≈ ω(1 − 𝒢_gap) for an ER; ℋ ≈ E_R(1 − 𝔶𝒢_gap) − E_st − E_esc for an NR (AUD R-b; E_st/E_R ≤ 0.055, L36).
Inputs (Table 1.1 of v1, unchanged and [FT] as there): E_g = 1.17/0.75 eV, ε_eh = 3.75 (Si; 3.81 in 1109.1193 Table I p.16; 3.749 from 2004.11499)/2.96 eV, f_D = 15/8.64 THz
(1109.1193 Table I), steady mode mix L/FT/ST 9.3/37.6/53.1% (Si), 9.8/36.7/53.5% (Ge) (2302.05998 p.4). **Yield:** 𝔶(E_R) is the measured Si Y of 2303.02196
Table II p.5 [FT]: 0.102^{+0.034}_{−0.030} (100 eV), 0.108^{+0.009}_{−0.010} (220 eV), 0.136^{+0.009}_{−0.008} (460 eV), with F_NR = 0.9^{+0.7}_{−0.4}, 0.5^{+0.2}_{−0.1}, 1.8^{+0.6}_{−0.5};
log-linear interpolation [E] between, flat outside. Lindhard (0.153 at 100 eV, L20 truncation, rejected by WP5 §6.1(b) for near-gap seeds) is the comparison
column only. Below E_R,th = 352/395 eV 𝔶 is **not derived** (WP5 §3.3; B-2 of WP5-AUD is the spec), so every (c)/(d) number at 50–300 eV is [E] on a measured, not derived, input.
**1.2 ER, zero field [E].** Hot carriers relax by intervalley/optical emission (11–15 THz in Si), then intravalley acoustic emission below ω_op; each such phonon
has hf ≤ 2c_ν√(2m*E_car) (5.7 meV ≈ 1.4 THz at 30 meV). Residual uniform on [0, ω_op] gives f_s ≈ ω_op/ε_eh. **Gap energy.** E_g per pair stays in E_pairs + E_X
until it is released as heat, trapped or emitted as light. Its release fraction r_g(t) obeys (CW5-4): r_g(t) = Σ_kw_ke^{−γ_k t} for linear kinetics, and
1/(1 + t/t₀) for bimolecular formation in dense tracks, so **r_g^{NR} ≠ r_g^{ER}** (CW5 §2.5). Its spectrum at birth is **not known**: bulk multiphonon/Auger
release is hard (then it loses memory as in §2), but release at surfaces or electrodes is soft and ballistic, "in a low frequency, ballistic regime that is
used to provide a surface-event discriminator" (1109.1193 p.17 [FT]: 13% of the signal), or goes straight into Al quasiparticles plus "a population of initially
high energy phonons" that become ballistic (1109.4343 p.3 [FT]). v1's "born hard" was untagged and is withdrawn (A F2, B B1).
**1.3 NR [E].** For x_R ≲ 1, WP2 (3.6) gives the branch-projected ρ^{ph}_κ [D]. Above ~eV the created-phonon spectrum is the WP5 mark dℋ_pr/dω_ph of WP5-AUD B-1 (as
corrected by CW5 OC-3: end-state zero-point level ω_s/2 subtracted, ΔZPE excluded, [ω_op, E_th^{ii}] and ℋ_nuc assigned). Until it is computed, a DOS-weighted
thermal spike is assumed (optical share ~½; energy below 1.4 THz ≈ 10⁻⁴). IF-R1 is re-pointed to returns/R13/WP5-v4.md (dℋ/dω_ph mark, l.145) and WP5-AUD B-1.

## 2. Propagation: down-conversion, isotope mixing, memory
**2.1 Rates [FT].** Γ_anh = 𝒜_anh f⁵ on L only; Γ_iso = 𝒜_iso f⁴ for all modes, DOS-weighted mixing (2302.05998 p.4: "negligible … not implemented" for T
decay). Si 𝒜_iso = 2.43×10⁻⁴² s³, 𝒜_anh = 7.41×10⁻⁵⁶ s⁴ (1109.1193 Table I p.16; 2408.04732 Tables 3–4 p.6: 2.33 calc, 2.42–2.56 meas; 1.15×10⁻⁵⁵ calc);
Ge 3.67×10⁻⁴¹; 𝒜_anh(Ge) spans 1.61–16.5×10⁻⁵⁵ (×10). v1 used 1.61 (1109.4343 p.2, credited there to Msall & Wolfe, not Tamura), the slowest decay, which is
conservative for memory loss. These are the CMPMC presets (include/cmpmc/materials/presets.hpp:36–37 Si; crystal_config.hpp:65–66 Ge, commit cd56e1b).
**2.2 Scaling [D given the f⁵, f⁴ laws, isotope mixing faster than L decay, and t ≫ (x_L𝒜_anh f_D⁵)⁻¹ ≈ 0.2 ns (Si)].** The mixed population decays at
x_L𝒜_anh f⁵, so by time t the energy sits below **f_*(t) = (x_L𝒜_anh t)^{−1/5}**: 10.8/4.3/2.7/1.7/1.1 THz (Si) and 9.1/3.6/2.3/1.45/0.91 THz (Ge) at
1 ns/100 ns/1 µs/10 µs/100 µs (CW6-K1a). Γ_iso/Γ_anh,L = 3.3 at 10 THz in Si: mixing outruns decay only marginally at the start (stated, A).
The hypothesis "f ≪ f_D" of v1 is replaced by the time condition above (B §D).
**2.3 Loss of frequency memory [E (toy) + D (scaling)].** A linear cascade with a Beta(3,3) daughter kernel (self-similar), one scalar rate x_L𝒜_anh f⁵ for
every phonon and no surfaces shows the hard-part TV distance falling below 10⁻³ by 10 ns (Si; 6.4×10⁻⁴) and between 30 and 100 ns (Ge) (WP8R-C3; CW6-K4a).
This is a scaling argument plus toy numerics, **not a derivation**: the real two-species L/T kernel with non-decaying T phonons is not shown to satisfy the
homogeneous-fragmentation hypotheses. The statement itself is not new: "details of the distribution will rapidly be lost" (1109.1193 p.6 [FT]); "wiped out after
the quasidiffusion stage" (1805.02495 p.6 [FT]). v1's "here it is derived" is withdrawn (A §2.3, B A1). Agreement with the 0.7–0.9 THz absorbed peak of
1805.02495 p.7 is circular (that MC starts from the Debye energy) and is no longer cited as support (A).
**2.4 Polarisation, space, focusing [D/E].** N_mix(1 µs) = 5𝒜_iso(x_L𝒜_anh)^{−0.8}t^{0.2} = 652 (Si), 5072 (Ge); r_rms = 77/16 µm (100 ns), 0.61/0.13 mm (1 µs)
(CW6-K1a). **Near-face scope (A F1, corrected):** events within r_rms(t) of an instrumented face reach a film before t_mem. For the device behind σ_ph = 2.65 eV,
**1 cm × 1 cm × 0.4 cm** Si (2012.12430 p.4 [FT]; A's "1 mm" is wrong, B's 4 mm stands), that shell is 0.5% of the volume at 10 ns and 3.9% at 100 ns (CW6-K4b).
It is a position class with residual memory, not an NR/ER discriminant at that volume fraction. Caustics act on phonons below f_b (0.72/0.32 THz for 1 cm),
which are a common population: they enter σ_pos, not the separation.
**2.5 Al₂O₃ is outside §2.2 (B A2).** 𝒜_iso = 0.025×10⁻⁴² s³, 𝒜_anh = 1.88–12.7×10⁻⁵⁵ s⁴ (2408.04732 Tables 3–4 [FT]; CMPMC presets.hpp:89–90) give
f_eq = 0.020–0.13 THz, and 𝒜_iso f⁴ × 1 µs = 0.025/0.4/16 at 1/2/5 THz (CW6-K4c). Mixing is slower than decay over the primary band, T phonons born in sapphire
neither mix nor decay, and the e^{−N_mix} argument fails. **All memory-loss statements are restricted to Si/Ge.** Sapphire is an exact gap (G-R6: needs T-decay
beyond the isotropic L-only channel, CMPMC-AUD §6 item 8, and the NR/ER birth polarisation, IF-R1).

## 3. Interfaces, films and sensors
**3.1 Inputs.** Si, Ge: 1109.1193 Table I [FT]. Al₂O₃: (λ, µ) = (139.8, 166.24) GPa, 2408.04732 Table 3 [FT], ρ AFLOW [DB]. W, Ti: AFLOW AEL moduli [DB] (IDs as v1).
Al: ρ = 2720 [DB], K = 76, G = 26 GPa [UNVERIFIED] (v_L/v_T = 6379/3092 m/s); cross-check, CMPMC presets.hpp:281–288 (C_ij from the G4CMP Al config; Voigt λ = 58.63,
µ = 26.16 GPa, ρ = 2700) gives 6410/3113 m/s and changes every Al number below by ≤ 0.6% (CW6-K5). Ir: K = 320, G = 210 GPa [UNVERIFIED] (G-R5 → LE-10).
**3.2 Isotropic AMM, derived [D].** Welded plane interface between isotropic solids, incident plane wave of slowness p = sinθ/c₁. Continuity of u_x, u_z,
σ_zz = iω[λp d_x + (λ + 2µ)s d_z], σ_xz = iωµ(s d_x + p d_z) for the four outgoing waves (P, SV reflected and transmitted; polarisations d_P = c_L(p, s),
d_SV = c_T(s, −p), s the signed vertical slowness, evanescent branches decaying away from z = 0) gives a 4×4 linear system; energy coefficients are
ρc²s|A|²/(ρ₁c₁²s₁) for propagating waves. SH decouples: t_SH = 4Z₁Z₂/(Z₁ + Z₂)², Z = ρc_T cosθ. **Checks:** flux conservation to 3×10⁻¹⁵ at every angle in
both directions (CW6-K5b); normal incidence reproduces v1 (Si/Al 0.991/0.960, K5a); SH flux averages reproduce v1 (K5c). **Reciprocity theorem [D]:** for any
reciprocal interface in equilibrium, Σ_νc_{1ν}⁻²⟨t_{12,ν}⟩ = Σ_νc_{2ν}⁻²⟨t_{21,ν}⟩ (flux-weighted ⟨·⟩ = ∫t(θ)2sinθcosθdθ); verified to 6×10⁻⁶ (K5d). It holds for DMM
by construction, t^{DMM}_{12} = Σ₂/(Σ₁ + Σ₂), Σ = c_L⁻² + 2c_T⁻² (K5g). This replaces the unread Kaplan/Little/Swartz–Pohl sources for L40 (A F10, B §D).

| Flux-averaged AMM | P | SV | SH | mode+angle t̄ | DMM | L/T (flux) | L/T (normal) |
|---|---|---|---|---|---|---|---|
| Si → Al | 0.977 | 0.892 | 0.960 | 0.934 | 0.743 | 1.06 | 1.03 |
| Al → Si | 0.603 | 0.266 | 0.315 | 0.323 | 0.257 | — | — |
| Ge → Al | 0.629 | 0.781 | 0.905 | 0.809 | 0.510 | **0.75** | 1.07 |
| Al → Ge | 0.874 | 0.715 | 0.819 | 0.778 | — | — | — |
Normal-incidence values for Si/W, Si/Ti, Si/Ir, Al₂O₃/Al are unchanged from v1 (0.588/0.621, 0.974/0.982, 0.522/0.527, 0.822/0.748); their flux averages are G-R5/§6 item 2
of CMPMC-AUD (anisotropic Christoffel-matched AMM). **Measured.** 1805.02495 p.1 [FT]: "transmission coefficients Si-Al in the range [0.3 - 0.55]" for "an aluminum film of
60 nm and a silicon substrate of 380 µm", fitted data-vs-MC with specular reflection, i.e. an **effective** substrate→film coefficient, not a measured AMM t̄; the AMM t̄ = 0.934 is an upper
bound. By the reciprocity theorem the matching film→substrate value is 0.10–0.19 (Σ_Si/Σ_Al = 0.346, K5f), against 0.32 (AMM) and 0.26 (DMM).
**Mode and angle.** The L/T contrast multiplies an NR/ER L-fraction difference ∝ e^{−N_mix}, so no NR/ER information follows in Si/Ge. The Ge/Al flux contrast
0.75 is larger than v1's "best 10%" but changes nothing for the same reason (A F5 closed). Not established for Al₂O₃ (§2.5).
**3.3 Pair breaking and trapping [FT/E].** WP5 (W13) gives η_pb = 2Δ_BCS/ω for 2Δ ≤ ω < 4Δ and an asymptote 0.57–0.6 "for infinite superconducting volumes"
(1401.1937 p.2 [FT]). Between, it is not flat: "For 2∆ ≤ hνs ≤ 4∆, ηs reduces monotonically" and for 4Δ ≤ hν ≤ 6Δ it "tends to increase", with "the overall
effect … a reduction in ηs as hνs increases" for finite phonon-loss time (1401.1937 p.5 [FT]). CMPMC-AUD T8: no loss 0.569 (4.5Δ), 0.595 (6Δ), 0.590 (≥ 10Δ);
with the 600 nm escape law 0.53 (5Δ) → 0.46 (40Δ) (IF-AUD-2). The film loss time is τ_l = 4d_film/(v_film t̄_esc) (CW6.md LE-123, CW6-K6). **Δ_BCS(Al):** v1 used 0.18 meV
[UNVERIFIED]; 1109.4343 p.3 [FT] writes "2∆Al = 200 µeV"; the CMPMC preset has Δ = 173.715 µeV (presets.hpp:298). 4Δ = 97–174 GHz in all three readings, so every
arriving primary or NTL phonon (≳ 0.3 THz) lies above 4Δ; it does **not** lie on a flat branch. A residual ω dependence of η_pb is a further ζ_O lever (NTL or gap vs
primary), never an NR/ER primary contrast, because NR and ER primaries share one spectrum.
**3.4 The real selector (A F3, B B2).** "A phonon's timescale of surface absorption … is therefor highly dependent on mean free path" (1109.4343 p.2 [FT], 6.1% Al
coverage). Absorption time ∝ [c t̄ v̄/(2d)]⁻¹ in the ballistic limit (1901.07569 Eq. (5), p.6 [FT]: τ_collection = 4V/(Σ A c_s f)) and longer when the mean free
path ∝ f⁻⁴ is short. Collection is therefore frequency-selective through geometry. This sets ζ_O of (b) and (d); it does not reopen (a).
**3.5 Observables (link to WP0, A N6).** O_obs = E[Σ_pop a_pop φ_pop(𝐍, 𝔪) | Λ] under the cascade map P_casc(𝐍, 𝔪|Λ) of WP0-v3 (7.3) / WP7-E-v3 (E3), with a_pop the
channel fraction (fast/slow, or film 1/(film 1 + film 2)) and φ_pop the energy fraction of population pop ∈ {primary, NTL, gap}. Contrasts ζ_O ≡ a_NTL − a_prim, ζ_gap ≡ a_gap − a_prim.

## 4. Figure of merit
**4.1 Definition [D] (one convention everywhere).** 𝒮_sep ≡ |⟨O_obs⟩_NR − ⟨O_obs⟩_ER|/[½(σ²_NR + σ²_ER)]^{1/2} at equal E_tot,
σ² = (σ_ph/E_tot)² + σ²_pos + σ²_Nph + w²F N_eh, with w = (ζ_O eV_b⟨𝔮⟩ + ζ_gap E_g)/E_tot the O shift per pair; σ_ph = 2.65 eV (the 1×1×0.4 cm Si device of 2012.12430,
p.1/p.4 [FT]); σ_Nph = [¼hf/(ϵ_prim E_tot)]^{1/2} (f = 1 THz, ϵ_prim = 0.13; 0.9% at 100 eV); F = F_meas^{obs} = 0.119 (ER, A-10 form, ϵ_det → 1) and measured F_NR.
v1's primary route used √2σ_ph/E_R; the √2 is removed (A F6.1, B A4).
**4.2 (a) primary route.** ΔO ≤ ζ_O(1 − 𝔶)f_s. E_2σ at ζ_O = 1, σ_pos = 0: **357 eV** (measured Y), 382 (Lindhard(E), = A), 369 (frozen 𝔶, = B's 368), 442 with σ_Nph; 1.2 keV at
ζ_O = 0.3 (CW6-K2a, b). Any σ_pos ≥ ζ_O(1 − 𝔶)f_s/2 = 0.76%·ζ_O caps 𝒮 < 2 at every energy (K2c); CDMS pulses vary at order unity with position (1109.4343 Figs. 1–2).
ζ_O ≈ 1 between soft and hard primaries is unphysical (band overlap, K2d). **NO-GO, conditional on σ_pos ≳ 1% and ζ_O ≪ 1.**
**4.3 (b) gap channel.** With (CW5-3) to first order and a late window t₂ at which r_g = 0, the two-window ratio O_b ≡ E_sig(t₁)/E_sig(t₂) gives
ΔO_b = 𝒢_gap[r_g^{ER}(t₁) − 𝔶r_g^{NR}(t₁)] (CW6-K3k). If r_g^{NR} = r_g^{ER} this is ζ_gapΔf_g with ζ_gap = r_g(t₁) and Δf_g = (1 − 𝔶)𝒢_gap = 0.28 (Y = 0.102).
𝒮_b(100 eV) = 8.2 (ζ_gap = 1, σ_pos = 0), 4.6 (σ_pos = 0.05), 1.46 (ζ_gap = 0.3, σ_pos = 0.05); ζ_gap,min = 0.42 at σ_pos = 0.05 (K3h, K3i). A fast/slow O_obs (§3.5) reads the same
channel through the release site (ζ_gap from §3.4). The bimolecular NR tail 1/(1 + t/t₀) against an exponential ER release changes the sign of ΔO_b at t₁ = 3.86t₀ (K3l): the
channel is real but its sign and size are kinetic. **UNRESOLVED; decisive input G-R2 (r_g^{NR,ER}(t), site, spectrum).** It is charge-borne (∝ 1 − 𝔶), so it is a yield/timing
discriminant, not a mode-selection one.
**4.4 (c, d) NTL route.** ΔO = ζ_OΔφ_L + ζ_gapΔφ_gap, Δφ_L = g(1 − 𝔶)/[(1 + g)(1 + 𝔶g)], Δφ_gap = 𝒢_gap(1 − 𝔶)/[(1 + g)(1 + 𝔶g)], g ≡ g_Luke⟨𝔮⟩ (WP8R-C7b, c; CW6-K3a).
Δφ_L is largest at g = 𝔶^{−1/2}, where Δφ_gap = 0.053 (Lindhard) (A F7). Si, σ_ph = 2.65 eV, measured Y(E), ζ_gap = 0:

| | 50 eV | 100 eV | 300 eV | 1000 eV |
|---|---|---|---|---|
| 10 V, ζ_O = 0.3, σ_pos = 0.05 (v2) | 1.94 | 2.44 | 2.70 | 2.70 |
| same, v1 (frozen Lindhard 𝔶, F_ER 0.15, F_NR 1, no σ_Nph) | 1.63 | 2.04 | 2.41 | 2.56 |
- **HV (100 V), conditional NO-GO (CW5 OC-7).** The pair-number ceiling with energy-matched measured bands is 1.9986 (ε 3.75, ⟨𝔮⟩ 0.873) and **2.014** with the source definition
  ⟨n_eh⟩ = YE_r/3.8 (2303.02196 Eq. (1)) (CW6-K3f, K3j); 1.763 at ⟨𝔮⟩ = 1; the joint 2σ corner exceeds 2 from 220 eV. Threshold F_NR* = 0.28/0.41/0.51 at ⟨𝔮⟩ = 1/0.873/0.8.
  v1's "robust at F_NR = 0.15" (C7l) is marginal: 1.99–2.01 with Y(300 eV) = 0.12 (2.18 at Y = 0.102, WP5-AUD AUD-C7c′; > 2 checked in CW6-K3g). The gap term does not change the ceiling (both scale with N_eh).
- **Low bias (d).** ζ_O,min(100 eV) = 0.13/0.24/0.44 at σ_pos = 0.02/0.05/0.10 (K3c; with v1's inputs 0.15/0.28/0.53). With ζ_gap/ζ_O = −1, −0.5, 0, +0.5, +1 the σ_pos = 0.05 value is
  0.27/0.25/0.24/0.22/0.21 (K3d). ζ_O = 0.1 fails at every bias. A mean-field two-film toy (4-mm Si, 5% Nb-like + 5% Al coverage) gives ζ_O = 0.11–0.42 for ⟨E_Luke⟩ = 4.7–0.75 meV
  (K7b; CW6.md LE-118): the requirement is not unreasonable, but it is geometry-model output [E], not a measurement.
- **Precedent transfer withdrawn.** 1109.4343's "1:10³ (limited by the statistics of the data)" (p.1 [FT]) is a floor: ζ_O/σ_pos ≥ 9.3, or 12–13 at 80–90% NR acceptance. Its
  contrast came from near-surface high-field NTL; in a uniform low-field device NTL phonons are "emitted with low energies and correspondingly ballistic free paths" (p.2). The
  transfer to a Si 4-mm device is [C]; v1's "𝒮(100 eV) ≈ 2.7" is removed from §0.
- Caveats [E]: ε_eh, F at few pairs and pair quantisation at 0.03-pair resolution; low-field trapping at mK (θ_tr; 2303.02196 p.4: trapping 12.7%, impact ionization 0.6%);
  σ_ph counted once for two channels.

## 5. The CDMS precedent
1109.4343 [FT] (Ge iZIP, ±2 V, 7–20 keV_nr): bulk ER/NR rejection "1:10³ (limited by the statistics of the data)" (p.1) from one risetime parameter. The information is
charge-borne: "Much of the essential information content of the charge measurement is duplicated in the phonon measurement" (p.2). The selector is mean free path ×
coverage (p.2); relaxation phonons are ignored "since they are initially ballistic" (p.3). The precedent is **consistent with** §2 (it does not test for a primary NR/ER
signature; it assumes the same memory loss, 1109.1193 p.13) and uses phonon frequency only for clock, position and surface tagging (1109.1193 p.17). Other precedents
(2303.02067 [ABS], 1405.4215 [ABS], 1305.2405 [ABS]) are charge-mediated or position information. What would be new: (d) or (b) at sub-keV without charge readout.

## 6. IF-E7: δ_coll and r_coll (WP7-E-v3 (E7), (E13); WP5-AUD (AUD-1))
- **Decomposition [D, first order].** δ_coll = δ_coll^{prim} + δ_coll^{gap} + δ_coll^{pos} + δ_coll^{esc} (spectral, gap-release, position, surface escape). δ_coll^{prim} ≈ (1 − 𝔶)f_s(ϵ_soft/ϵ_hard − 1),
  |δ_coll^{prim}| ≤ 0.007 for |ϵ_soft/ϵ_hard − 1| ≤ ½ [E] and ≤ 0.012 at ϵ_soft = 0. δ_coll^{gap} = (1 − y_ion)𝒢_gap(ρ_g − 1)/[1 + 𝒢_gap(ρ_g − 1)], ρ_g ≡ ϵ_gap/ϵ_hard, **exact** at fixed
  populations (CW6-K8a). With y_ion = 0.3, ρ_g − 1 = 0.24 gives 0.048 (K8b). **⇒ δ_coll^{prim} cannot carry the 0.048 deficit of 1803.02903; δ_coll can** (B B3 corrected v1's §6).
- **r_coll.** NTL phonons skip quasidiffusion, so r_coll ≠ 1 is expected; sign open. Mean-field toy: r_coll = 0.87 (⟨E_Luke⟩ 0.75 meV), 0.96 (2 meV), 0.98 (4.7 meV) (K7c): soft NTL
  phonons lose more to sub-gap and bare-surface channels. **WP8-R does not support (B-b) r_coll ≥ 1; if r_coll < 1 the WP7-E-v3 bounds (L36) are void until G-R1 closes** (A F8).
  Prior: σ_ln = 0.1, median 1, sign open in the profiled object; the conditional bound on the r_coll ≥ 1 branch only (CW5 OC-8; v1's "|r − 1| ≲ 0.2" read as 2σ).
- **Breaking the degeneracy [D].** From (AUD-1), ∂(1 − η^φ_NR)/∂r_coll = g_Luke(1 − y_ion)/(1 + g_Luke) at r_coll = 1 (rises with V_b) while the coefficient of
  X ≡ δ_coll + (D′_NR − κ_cal(r_coll)D′_ER)/ω is 1; the Jacobian at two biases (g_Luke = 1.05 and 10.5) has rank 2 (CW6-K8c, d). An η^φ_NR measurement at two biases on one
  detector separates r_coll from (δ_coll + E_st). Two windows separate E_st^{rel}P_rel and r_g (CW5 §2.5).

## 7. Exact remaining gaps
| # | Gap | Closing object |
|---|---|---|
| G-R1 | ζ_O, ζ_gap, σ_pos, r_coll for a concrete geometry | CMPMC run, spec in CW6.md LE-118/LE-121 (gated modules and SOTA items listed there); or an NR/ER calibration at V_b = 5–10 V with fast/slow and two-film readout |
| G-R2 | r_g^{NR,ER}(t), release site and spectrum of the gap energy at zero field, mK | (CW5-4) with rates (CW5 §2.5 spec); CW6.md LE-119 transport part |
| G-R3 | created-phonon spectra (NR ≳ eV, ER) | WP5-AUD B-1 as corrected by CW5 OC-3; propagation spec CW6.md LE-120 |
| G-R4 | 𝔶 and F_NR below 352 eV | WP5-AUD B-2 (CW5 OC-4); data 2303.02196 until then |
| G-R5 | Al, Ir moduli; anisotropic and thin-film AMM for W, Ti, Ir, Al₂O₃ | LE-10 (data); CMPMC-AUD §6 item 2 |
| G-R6 | Al₂O₃ memory loss (mixing hypothesis fails) | T-mode decay beyond the ICA (CMPMC-AUD §6 item 8); birth polarisation (IF-R1) |

## 8. Checks (code/CW6/checks.py)
| Group | Content |
|---|---|
| K1 | reproduction of v1: f_*, N_mix, r_rms; 𝒮_prim, 𝒮_int, ζ_O,min with v1 conventions |
| K2 | §4.1 convention; E_2σ under three yield inputs; σ_pos cap; band overlap |
| K3 | NTL route with gap population, measured Y/F, σ_Nph; HV ceiling 1.9986/2.014; (b) channel 𝒮_b, ζ_gap,min, two-window algebra, bimolecular sign flip |
| K4 | Ge TV window; near-face shell (4 mm); Al₂O₃ f_eq, N_mix |
| K5 | P–SV AMM solver: flux conservation, normal incidence, SH, reciprocity, Ge/Al critical angle and contrast, measured → reverse map, DMM |
| K6–K8 | film escape with t_esc; mean-field two-film ζ_O, r_coll; δ_coll^{gap}, bias-scan Jacobian |

## 9. Closing table (one row per referee and audit item)
| Item | Source | Disposition in v2 | Where |
|---|---|---|---|
| V1 / row 1 (f_s assumptions; "8–15 THz" Si only) | A | applied: assumptions tagged, Ge f_D stated | §0 r1, §1.2 |
| V2 / F1 (bulk scope; [D] → [E]) | A | applied; device thickness corrected to 4 mm (A's 1 mm wrong, B right; 2012.12430 p.4) | §2.3–2.4, K4b |
| V3 / F4 (η_pb not flat) | A, B A3, IF-AUD-2 | applied with 1401.1937 p.5 quote and CMPMC T8 numbers | §3.3 |
| F5 (L/T normal incidence only) | A | closed: full P–SV flux averages; Ge/Al 0.75 | §3.2, K5e |
| V4 / F6.1 / A4 (√2 convention) | A, B | applied: one convention; E_2σ 357 eV (measured Y), 382/369 reproduce A/B | §4.1–4.2, K2a,b |
| F6.2 (frozen 𝔶) | A | applied: measured Y(E) primary, Lindhard comparison | §1.1, §4.4, K3e |
| F6.3 (σ_Nph omitted) | A | applied in all routes | §4.1, K3c |
| V5 / F2 / B1 / row 5 ((b) ζ_O = 0) | A, B | withdrawn: (b) UNRESOLVED; quantified with (CW5-3)/(CW5-4) | §0 r5, §1.2, §4.3, K3h–l |
| V6 / row 6 (HV NO-GO) | A, B | becomes CONDITIONAL per AUD D-7 and CW5 OC-7 | §4.4, K3f,g,j |
| V7 / F7 (missing gap population in O) | A | applied: ζ_gapΔφ_gap term; ζ_O,min range | §4.4, K3a,d |
| CDMS calibration transfer | A, B B2 | withdrawn ([C]); 10³ read as floor 9.3 (12–13 at 80–90% acceptance) | §4.4, §5 |
| V8 / F8 / B3 (δ, (B-a), (B-b)) | A, B | applied: δ_coll^{prim} vs δ_coll^{gap} (exact); (B-b) unsupported flag; "|r−1| ≲ 0.2" replaced by OC-8 prior | §6, K7c, K8a,b |
| V9 / F9 / B4 (verdict reason) | A, B | applied: yield-ceiling reason; overall wording of B4 | §0 overall |
| V10 / F10 / B §D L39–L42 | A, B | new rows below: L39 ESTIMATED with time condition and scope; L40 sourced by in-return derivation; L41 ESTIMATED; L42 conditional | LIMITS rows |
| F3 / B2 (frequency selector) | A, B | applied: mean free path × coverage | §3.4 |
| §(e) Si ω_op proxy is the Debye energy | A | tagged [E] | §0 r1 |
| f_s(Ge) 0.012 vs 0.0125 in code | A | text 0.012 (rounded 0.0125); no number depends on it | §0 r1 |
| 1805.02495 0.7–0.9 THz circular; 0.3–0.55 device and fitted | A, B §D | applied | §2.3, §3.2 |
| N1 / B §C (g, r, δ, y renames) / AUD D-8 | A, B, AUD | applied | header |
| N2 (𝔖 collision) | A, B §C | 𝒮_sep, 𝒮_int | header |
| N3 (𝔶 vs y_ion) / AUD R-c, D-9 | A, B, AUD | kept 𝔶 with the WP5-AUD definition and the y_ion relation; measured Y used | header, §1.1 |
| N4 (O) | A | O_obs | §3.5 |
| N5 (WP5-v4 exists) | A | IF-R1 re-pointed | §1.3 |
| N6 (link to WP0 (7.3)) | A | O_obs as a functional of P_casc | §3.5 |
| Ω, f_D, 𝒜 notation | B §C | ω_{Qν}; f_D ≡ ω_D/2π; 𝒜 kept with ⚠ | header |
| [DB] tag | B §C | CONVENTIONS R13 amendment ranks [DB] | header |
| 2012.12430 "Si CPD" label | B §C | relabelled: 1×1×0.4 cm Si, 0 V | §4.1 |
| A1 (derivation overclaim; credit 1109.1193 p.6) | B | applied | §2.3 |
| A2 (Al₂O₃) | B | applied: excluded; G-R6 | §2.5, K4c |
| A5 (verified items; 94-event overcount) | B | noted: N_mix integration from t = 0 overcounts by ≈ 94 of 652, immaterial | §2.4 |
| weak checks C4f, C5c, C8a | B | C4f replaced by the e^{−N_mix} argument with computed N_mix; C5c: 0.7 THz hole NTL sits on the 0.73 THz cut (stated); C8a range stated | §3.2–3.3, §6 |
| row 9 pair quantisation | B | caveat added | §4.4 |
| L40 Kaplan unread | A, B | replaced by derived AMM + reciprocity; Kaplan stays not accessed | §3.2 |
| Δ_Al 200 µeV (1109.4343 p.3) | A, B A3 | all three values stated; conclusion unchanged | §3.3 |
| "born hard" untagged; ×½ in δ bound | B §E | withdrawn / tagged [E] | §1.2, §6 |
| AFLOW IDs not re-queried | B §E | kept [DB] as v1; not re-queried here | §3.1 |
| R-a (ledger LHS 𝒲_bias) | AUD | applied | §1.1 |
| R-b (NR form omits E_st, E_esc) | AUD | applied | §1.1 |
| R-d (primary NO-GO with yield range) | AUD | consistent (K2b) | §4.2 |
| R-e (Δf_g 0.28) | AUD | applied | §0 r5 |
| R-f / D-7 (HV robustness) | AUD, CW5 OC-7 | applied | §4.4 |
| R-g (ζ_O,min 0.13/0.24/0.44) | AUD | reproduced with v2 inputs (K3b, K3c) | §4.4 |
| R-h / D-10 (F_ER → F_meas^{obs}; g_Luke⟨𝔮⟩) | AUD | applied | §4.1 |
| R-i (r_coll prior) | AUD, CW5 OC-8 | σ_ln 0.1 | §6 |
| D-1 (E_pairs + E_X in D′) | AUD, CW5 OC-1 | used: (CW5-3) is the (b) channel | §4.3 |
| IF-AUD-3 (Luke rate typo) | CMPMC-AUD | Γ_Luke = (v_L/3ℓ₀)(𝔐 − 1)³/𝔐 is the form to quote (not 1109.1193 (21)); not used numerically here | — |
| IF-AUD-4 (G4CMP surface coefficients are demo values) | CMPMC-AUD | any G-R1 run supplies p_spec, p_diff, p_anh (CW6.md LE-118) | §7 |

## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| f, f_*(t), f_b, f_eq, f_D ≡ ω_D/2π; 𝒜_anh, 𝒜_iso ⚠; x_L; N_mix, r_rms, t_mem, ℓ_mem; f_s | as v1 | v1 (NOTATION owed, LE-164) |
| O_obs, a_pop, φ_pop, ζ_O, ζ_gap, σ_pos, σ_Nph, σ_ph, 𝒮_sep, 𝒮_int, 𝒮_b, O_b | observable; channel and energy fractions; contrasts; spreads; separations; two-window ratio | renamed (v1 O, 𝔖) / new (ζ_gap, 𝒮_b, O_b) |
| Δφ_L, Δφ_gap, Δf_g; 𝒢_gap ≡ E_g/ε_eh (CW5) | NR/ER energy-fraction differences | v1 / new (Δφ_gap) |
| δ_coll^{prim}, δ_coll^{gap}, δ_coll^{pos}, δ_coll^{esc}; ρ_g ≡ ϵ_gap/ϵ_hard; ϵ_soft, ϵ_hard, ϵ_gap | parts of δ_coll; gap/hard collection ratio | new (renamed δ_prim) |
| t^{AMM}_{P,SV,SH}(θ), t̄_{12}, Σ ≡ c_L⁻² + 2c_T⁻², Z, 𝔯 | AMM coefficients; mode+angle average; DMM/reciprocity weight | v1 t-family + new t̄, Σ |
| used | 𝔶 (WP5-AUD), y_ion, g_Luke, ⟨𝔮⟩, r_coll, δ_coll, κ_cal(r_coll), r_g, P_g (CW5), F_meas^{obs}, F_NR, η_pb, Δ_BCS, t_esc, d_film, ℋ, E_st, 𝒲_bias, ϵ_prim, ϵ_NTL | NOTATION / WP5-AUD / CW5 |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-R1 | WP5 | created-phonon spectra | WP5-AUD B-1 + CW5 OC-3 (unchanged need) |
| IF-R2 | WP6, WP7-E | (b) channel | θ_X type T on r_g^{NR}, r_g^{ER} (CW5 IF-CW5-2); add θ_gap (ζ_gap, M) if (b) or (d) is used |
| IF-R3 | WP7-E (IF-E7), LIMITS L36 | δ_coll, r_coll | δ_coll^{gap} can carry 0.048; (B-b) not supported by WP8-R; bias scan breaks the degeneracy |
| IF-R4 | WP8-F/S | menu | drop (a); (c) CONDITIONAL NO-GO (OC-7); (d) CONDITIONAL yield-readout variant (ζ_O ≥ 0.24 at σ_pos = 0.05); (b) UNRESOLVED |
| IF-R5 | WP6 | nuisances | θ_ζ, θ_ζg (M), θ_pos (M), F_NR (A → measured band) — row text in CW6.md LE-125 |
| IF-R6 | SOTA | statement | text in CW6.md LE-126 |

## Proposed LIMITS rows (replace v1's L39–L42; numbers by the coordinator)
| # | Chain | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L39 | (W4) prompt ℋ → Γ = 𝒜_anh f⁵ (L), 𝒜_iso f⁴ mixing → scaling spectrum in f/f_*(t) | 1109.1193 Table I, p.6 ("rapidly be lost"); 2302.05998 §2.2.2; 2408.04732 Tables 3–4 [FT] | Si/Ge (f_eq ≫ f; fails for Al₂O₃); t ≫ (x_L𝒜_anh f_D⁵)⁻¹; bulk events beyond r_rms(t) of a face; self-similar kernel | anisotropic rates; "a loss of ∼0.1% for each phonon-surface interaction" (1109.1193 p.14); film down-conversion | ESTIMATED (scaling D, toy E) |
| L40 | isotropic welded AMM (P–SV + SH) and DMM; reciprocity Σ₁t̄₁₂ = Σ₂t̄₂₁ | derived here (CW6-K5); measured effective Si→Al 0.3–0.55 for 380 µm/60 nm (1805.02495 p.1 [FT]) | λ ≪ d_film; isotropic media; clean interface | anisotropy (Christoffel AMM); oxide/aSi layers; partial specularity | DERIVED (formulas) / E (numbers) |
| L41 | WP5 (W13) η_pb(ω_{Qν}): 2Δ/ω below 4Δ; thin-film fall above | 1401.1937 pp.2, 5 [FT]; CMPMC-AUD T8 | lumped film, isotropic escape | τ_l/τ_0φ dependence; Chang–Scalapino solution | DERIVED (< 4Δ) / ESTIMATED (above) |
| L42 | NTL route ΔO = ζ_OΔφ_L + ζ_gapΔφ_gap; g_opt = 𝔶^{−1/2}; ceiling 𝒮_int | WP8R-C7b, c; CW6-K3; 2303.02196 Table II [FT] (inputs); 1109.4343 calibration only | equal E_tot; Gaussian spreads; §4.1 convention | F, 𝔶 at few pairs (G-R4); ⟨𝔮⟩; low-field trapping; HV ceiling CONDITIONAL (OC-7) | DERIVED (algebra) / E (numbers) |
