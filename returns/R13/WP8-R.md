# R13 / WP8-R: mode-selective phonon collection as an NR/ER discriminant (go/no-go screen)

Agent WP8-R, brief briefs/R13/WP8-R.md. Inputs: returns/R8/WP5-v3.md read through **returns/R12/WP7-E-v3.md §5 (A-1…A-16)**, since WP5-v4 does not
exist yet (state/CORRECTIONS.md row "WP7-E-v3 §5"). Also returns/R8/WP2-v3.md, CONVENTIONS.md and NOTATION v4 with the R9/WP7 rows; CORRECTIONS §11 and §17 were read.
None of the owed renames touch the objects used here: (W4), (W11)→A-4, (W13), §3.1–3.4, L20.
**Checks:** `code/WP8-R/checks.py` uses numpy, scipy and sympy. It is deterministic and has no Monte Carlo: **48/48 PASS in ≈ 1 s**, cited as **WP8R-Cn**. The "cascade" check
WP8R-C3 is a toy linear rate equation on a frequency grid [E], not a transport simulation.
**Literature:** sources marked [FT] were read in full text in literature/papers-WP8-R/: 1109.1193, 1109.4343, 1805.02495, 2012.12430, 2301.08699, 2302.05998
and 2408.04732. Their arXiv IDs and titles were verified against the arXiv API, as were those of the inherited citations 1401.1937 and 2004.11499 (via WP5-v3), and the PDFs have been deleted. 2303.02067, 1305.2405 and 1405.4215 are [ABS]; they come from an INSPIRE citation walk on
1109.4343, which has 7 citing records. Kaplan, JLTP 37, 343 (1979), Tamura PRB 31, 2574 (1985) and Maris are not on arXiv and were **not accessed**. Their content enters only
through the [FT] papers above, which quote it. Tags follow CONVENTIONS §12. Rate laws are quoted in their source form (Γ = Aν⁵, Γ = Bν⁴, with ν in Hz) as source-only notation
(NOTATION §K). Campaign formulas use 𝒜_anh, 𝒜_iso and f ≡ ω_{Qν}/2π (Symbols). **No directionality claims.**

---
## 0. Verdict at a glance
| # | Question | Result | Tag |
|---|---|---|---|
| 1 | Do NR and ER prompt phonon populations differ at birth? | Yes, in branch mix (both are dominated by optical/zone-boundary phonons at f ≈ 8–15 THz) and by an ER-only **soft fraction** f_s ≈ ω_op/ε_eh = 1.7% (Si), 1.2% (Ge) | E |
| 2 | Memory time and length | the hard-part spectral distance falls below 10⁻³ by **t_mem ≈ 10 ns (Si), ≈ 30–100 ns (Ge)**; polarisation is erased after more than 650 (Si) and 5000 (Ge) mode-mixing events by 1 µs. The cloud spreads ≲ 80 µm (Si) and ≲ 16 µm (Ge) by 100 ns. This is ≪ 1 cm and ≪ τ_ph = 20–100 µs | D (scaling) / E |
| 3 | Interface transmission | In the primary band (f ≳ 0.7 THz, λ ≪ d_film) AMM is frequency-independent. Below that (sub-THz NTL phonons, thin films) λ ~ d_film and d_film/L_pb(Ω) bring in Ω dependence, which is a lever for ζ_O and not an NR/ER primary signature. L/T contrast at normal incidence is t^{AMM}_L/t^{AMM}_T = 0.95–1.10 for Si/Al, Si/W, Si/Ti, Si/Ir, Ge/Al and Al₂O₃/Al. η_pb(Ω) is flat above 4Δ_BCS(Al) = 0.17 THz | E |
| 4 | **(a) Mode/frequency/angle-selective collection of the primary populations** | **NO-GO.** Only (1 − 𝔶)f_s survives, and it does not depend on mode. Even at perfect contrast and zero position spread, 𝔖 = 0.38 at 100 eV and 1.15 at 300 eV, with 2σ first reached at E_R = 0.52 keV. With a 2% residual position spread, 𝔖 < 1 at every energy | D given §2 / E |
| 5 | (b) Zero-field gap-energy channel | Δf_g = (1 − 𝔶)E_g/ε_eh = 0.26 (Si), 0.22 (Ge). The gap phonons are born at high frequency, so the mode contrast is ζ_O = 0. It can be read only through the **timing** of E_g release (E_X, E_trap; WP7-E-v3), which falls outside this screen. Flagged | D / C |
| 6 | (c) HV/NTL mode (≥ 100 V) | **NO-GO at any contrast for E_R ≤ 300 eV.** The pair-number ceiling is 𝔖_int = 0.53 (100 eV) and 0.91 (300 eV) at F_NR = 1. With F_NR = F_eh = 0.15 it is still 1.0 and 1.72 (WP8R-C7l). At 1 keV, 𝔖_int = 1.67–3.15 depending on F_NR | D (algebra) / E |
| 7 | (d) Low-bias, phonon-only readout of NTL vs primary phonons (the CDMS-PSD mechanism) | **CONDITIONAL (a measurement proposal, not a GO).** This is charge-mediated, not mode selection. 𝔖 ≥ 2 at E_R = 100 eV in Si (V_b ≈ 6–10 V, σ_ph = 2.65 eV) needs ζ_O ≥ 0.15 / 0.28 / 0.53 at σ_pos = 0.02 / 0.05 / 0.10. Carrying over the precedent's implied ζ_O/σ_pos ≈ 9 gives 𝔖(100 eV) ≈ 2.7 | E |
| 8 | IF-E7 (δ, r) | δ_prim ≤ 0.007: memory loss leaves only f_s, so δ cannot carry the 0.048 deficit of 1803.02903. r ≠ 1 is physically expected (NTL phonons skip quasidiffusion), but its sign is model-dependent | E |

**Overall: NO-GO for the brief's target.** Interfaces whose transmission depends on mode, frequency or angle cannot separate NR from ER, because the populations
lose their frequency and polarisation memory within ~10–100 ns and ≲ 0.1 mm. The only phonon-borne NR/ER information that survives to the sensor comes through charge
(Luke/NTL, carrier-relaxation and gap-energy phonons). That channel is ionization yield read out with phonons, which is exactly the mechanism of the CDMS precedent
(§5). An interface can at most raise its contrast ζ_O. **Mapping onto the brief's GO rule:** (d) reaches ≳ 2σ at sub-keV only on an [E] extrapolation whose two
inputs (ζ_O, σ_pos) have not been measured, and it is not an interface effect. The brief's question therefore gets NO-GO, and (d) goes to WP8 as a measurement proposal (IF-R4).

---
## 1. Initial phonon populations at equal total phonon energy
**1.1 Inputs [FT/DB/E]** (Table 1.1). In WP5 (W4) as amended by A-1, an ER deposits ω = N_e^f(E_c − μ_F) + N_h^f(μ_F − E_v) + E_X + E_trap^{pr} + E_es + ℋ + E_st + E_esc. At t_pr the
**prompt phonon part** is ℋ ≈ ω(1 − E_g/ε_eh). The gap part E_g/ε_eh is carried by pairs, excitons or traps (WP7-E-v3 (E1)).

| Quantity | Si | Ge | Source / tag |
|---|---|---|---|
| E_g, ε_eh (eV) | 1.17, 3.75 (3.81 in source) | 0.75, 2.96 | 1109.1193 Table I p.16 [FT]; ε_eh(Si) = 3.749 from WP5-v3 §2 (2004.11499 [FT]) |
| prompt-phonon fraction of ER, 1 − E_g/ε_eh | 0.688 | 0.747 | WP5 (W4) [D] |
| Debye frequency f_D (THz) | 15 | 8.64 | 1109.1193 Table I p.16 [FT]; 1805.02495 Table I p.2 ("15 THz") [FT] |
| ω_op proxy (meV) | ≈ 62 | ≈ 36 (h f_D) | 1805.02495 p.6 "Debye energy (∼62 meV in Si)" [FT]; Ge [E] |
| ER soft fraction f_s ≈ ω_op/ε_eh | 0.017 | 0.012 | [E] (§1.2) |
| NR yield 𝔶 at E_R = 100 eV (Lindhard) | 0.153 | 0.126 | WP5 L20 Eq. (7) form, WP8R-C6 [E]. Below E_R,th = 352/395 eV the yield is **not derived** (WP5 §3.3) |
| NTL phonon frequency (Ge, near-surface field) | – | ≈ 300 GHz (e), ≈ 700 GHz (h); lower and ballistic in the bulk field | 1109.4343 p.2–3 [FT] |
| steady mode mix L/FT/ST after isotope scattering | 9.3/37.6/53.1% | 9.8/36.7/53.5% | 2302.05998 p.4 [FT] |

**1.2 ER (zero field) [E].** Hot carriers relax first by intervalley and optical emission at f ≈ 11–15 THz (Si), then by intravalley acoustic emission once E_car < ω_op.
Each such phonon has energy ≤ 2c_ν√(2m*E_car): ≈ 5.7 meV ≈ 1.4 THz at E_car = 30 meV, m* = 0.3m_e, c_ν = 9 km/s. These phonons are born at or below the
ballistic threshold (§2). The residual carrier energy is uniform on [0, ω_op], which gives ≈ ω_op per pair and f_s ≈ ω_op/ε_eh. NOTATION has the e–ph kernel (WP5 §2) but no
output of the **created-phonon spectrum**, so f_s is an estimate (IF-R1). **Gap energy:** at zero field, E_g per pair goes to E_X (excitons, ≳ ns), E_trap or
recombination. Its release time is not known at mK [UNVERIFIED], and its phonons are born hard (multiphonon/Auger), so they lose memory as in §2.
**In HV mode** it is released at the electrodes as relaxation phonons in the Al. 1109.4343 p.3 [FT] calls these "initially ballistic … a minimal contribution to pulse shape".
NTL phonons add the energy fraction g/(1 + g), with g ≡ eV_b/ε_eh (WP7-E-v3 symbol).

**1.3 NR [E].** For E_R ≲ ω_max (x_R ≲ 1), WP2 (3.6) gives ρ^ph_κ, and its branch-projected form gives the LA/TA/LO/TO content exactly [D]. **For E_R ≳ eV**, the
WP5 §3.4 MD partition tables specify ℋ and E_st but **not the created-phonon spectrum** (IF-R1). Here a DOS-weighted thermal spike is assumed: every branch is
populated with f ≲ f_D, the optical share is of order the optical DOS weight (~½), and the energy below 1.4 THz is ≈ (1.4/15)⁴ ≈ 10⁻⁴. The "athermal LO/optical
share" therefore differs between NR and ER by O(0.1–0.3) in branch mix, but both populations are hard. At sub-keV energies an NR deposits ≈ (1 − 𝔶E_g/ε_eh) of E_R promptly
as phonons, against 0.69 for an ER (Si).

---
## 2. Propagation: down-conversion, isotope scattering, focusing
**2.1 Rates [FT] (source form).** Γ_anh = A ν⁵ acts on L phonons only. G4CMP p.4 [FT]: "down-conversion events from the other polarization states are negligible … not
implemented", with branches L → L′T and L → TT. Γ_iso = B ν⁴ mixes polarisations according to the DOS (same page).

| | B = 𝒜_iso (s³) | A = 𝒜_anh (s⁴) | v_L, v_T (m/s), ρ (g/cm³) |
|---|---|---|---|
| Si | 2.43×10⁻⁴² (1109.1193 Table I p.16; 2408.04732 Table 4 p.7: 2.33 calc, 2.42–2.56 meas) [FT] | 7.41×10⁻⁵⁶ (1109.1193 Table I; 2408.04732 Table 3 p.6: 1.15×10⁻⁵⁵ calc) [FT] | 9000, 5400, 2.33 (1109.1193 Table I) [FT] |
| Ge | 3.67×10⁻⁴¹ (1109.1193 Table I; 1109.4343 p.2 "36.7×10⁻⁴²") [FT] | 1.61×10⁻⁵⁵ (1109.4343 p.2) / 6.43×10⁻⁵⁵ (1109.1193) / 6.8 and 16.5 ×10⁻⁵⁵ (2408.04732 Table 3) [FT]: **range ×10** | 5310, 3250, 5.32 (1109.1193 Table I) [FT] |

**2.2 Scaling result [D given the ν⁵, ν⁴ laws and isotope mixing faster than L decay].** In Si, mixing outruns decay below f_eq = B/A = 33 THz. In Ge the same holds
below 228 THz (WP8R-C1a), although at 10 THz in Si it is only 3.3× faster. The mixed population therefore decays at the effective rate x_L𝒜_anh f⁵, with x_L the steady L fraction. By time t all
energy sits below **f_*(t) = (x_L𝒜_anh t)^{−1/5}**:

| t | 1 ns | 100 ns | 1 µs | 10 µs | 100 µs |
|---|---|---|---|---|---|
| f_* Si (THz) | 10.8 | 4.3 | 2.7 | 1.7 | 1.1 |
| f_* Ge (THz) | 9.1 | 3.6 | 2.3 | 1.45 | 0.91 |

In Ge the ×10 spread in A shifts f_* by (A_max/A_min)^{1/5} ≤ 1.6 (WP8R-C1c). The 1-cm ballistic thresholds are ℓ_iso = 1 cm at f_b = 0.72 THz (Si) and 0.32 THz (Ge). One decay per crossing occurs at 2.5 THz (Si)
and 1.9 THz (Ge) (WP8R-C2a). This agrees with the absorbed spectrum peaking at 0.7–0.9 THz in Si/Al KIDs (1805.02495 p.7 [FT]) and with "ballistic … 755 µs" in Ge (1109.4343 p.2 [FT]).

**2.3 Loss of frequency memory [E, WP8R-C3].** The toy linear cascade uses daughter energy fractions x ~ Beta(3,3), symmetric and broad like 1109.1193 Fig. 8 [FT]. It conserves energy exactly (WP8R-C3a, b).
Initial spectra: NR = Debye energy density to f_D. ER = (1 − f_s)·(hard line at 0.95 f_D) + f_s·(flat 0.3–1.4 THz). The total-variation distance between the
normalised spectra evolves as:

| t | 0 | 0.1 ns | 1 ns | 10 ns | 100 ns | 1 µs | 10 µs |
|---|---|---|---|---|---|---|---|
| Si, full (hard part only) | 0.54 (0.54) | 0.36 (0.35) | 0.043 (0.039) | 0.017 (0.001) | 0.016 (<10⁻³) | 0.012 | 0.008 |
| Ge, full (hard part only) | 0.54 | 0.50 | 0.29 | 0.024 (0.022) | 0.011 (<10⁻³) | 0.008 | 0.005 |

The reason is that the ν⁵ law makes the late spectrum a scaling function of f/f_*(t), independent of where it started. Once f_* ≪ f_0 the start is forgotten, and
the hard part's distance decreases monotonically (WP8R-C3c, d). **What remains is ≤ f_s**, and even that shrinks as the hard cascade fills the soft band (WP8R-C3e).
1805.02495 p.6 [FT] states that the primordial distribution "is unknown, nevertheless their effects are wiped out after the quasidiffusion stage". The source assumes this;
here it is derived.

**2.4 Polarisation, space and focusing [D/E].** The number of isotope (mode-mixing) events integrated along f_*(t) reaches 652 (Si) and 5072 (Ge) by 1 µs (WP8R-C2b), so polarisation memory goes as e^{−N_mix}. The diffusive
spread is r_rms = 77 µm (Si) and 16 µm (Ge) at 100 ns, and 0.61 mm and 0.13 mm at 1 µs (WP8R-C2c). An NR deposit (~nm) and a sub-keV ER track (≲ µm) are both point sources on this scale.
Focusing and caustics (2302.05998 Fig. 2 [FT]) act only on phonons below f_b. Those phonons are the same population for NR and ER, so caustics enter the **spread**
(σ_pos) and not the separation. The higher local phonon density of a dense NR cascade can only speed up the decay [E]. **Times against crystal size:** t_mem ≈ 10–100 ns and
ℓ_mem ≲ 0.1 mm, against L = 1 cm and τ_ph ≈ 20 µs rise (2012.12430 p.5 [FT]), 30–160 µs fall (2012.12430 Table I p.7 [FT]) and 755 µs (CDMS Ge, 1109.4343 [FT]).

---
## 3. Interface transmission and quasiparticle trapping
**3.1 Material inputs.** Si and Ge: 1109.1193 Table I [FT]. Al₂O₃: λ = 139.8, µ = 166.24 GPa from 2408.04732 Table 3 p.6 [FT], with ρ = 3.866 g/cm³ from AFLOW
aflow:0725f687e8b52e3f (PBE, ICSD 31548) [DB]. W: AFLOW aflow:b36865785bd06095 (bcc), ρ = 18.56, K = 297.7, G = 150.5 GPa [DB]. Ti: aflow:ece991e1e336aa44 (hcp),
ρ = 4.265, K = 113.5, G = 63.5 [DB]. Al: ρ = 2.720 from aflow:c2c7b894cd35ec8a [DB], with K = 76, G = 26 GPa [UNVERIFIED]. Ir: ρ = 21.98 from aflow:bbfb2cb08928c327 [DB],
with K = 320, G = 210 GPa [UNVERIFIED]. AFLOW has no AEL entry for Al or Ir. The JARVIS OPTIMADE endpoint returned HTTP 500, and the JARVIS bulk download was not attempted.
Cross-check: the Si (µ, λ) of 2408.04732 reproduce 9000/5400 m/s to 1% (WP8R-C4a).

**3.2 AMM/DMM [E, WP8R-C4].** The table gives the isotropic AMM: normal incidence t^{AMM} = 4Z^{ac}₁Z^{ac}₂/(Z^{ac}₁+Z^{ac}₂)², and a flux-averaged SH (transverse) wave with Snell refraction and
critical angles. It also gives the Debye DMM, t^{DMM}_{12} = Σc₂⁻²/(Σc₁⁻² + Σc₂⁻²). Checks: t + 𝔯 = 1, reciprocity and DMM detailed balance (WP8R-C4b–d).

| substrate/film | AMM L ⊥ | AMM T ⊥ | AMM SH ⟨flux⟩ | DMM | t^{AMM}_L/t^{AMM}_T |
|---|---|---|---|---|---|
| Si/Al | 0.991 | 0.960 | 0.960 | 0.743 | 1.03 |
| Si/W | 0.588 | 0.621 | 0.482 | 0.778 | 0.95 |
| Si/Ti | 0.974 | 0.982 | 0.896 | 0.658 | 0.99 |
| Si/Ir | 0.522 | 0.527 | 0.406 | 0.752 | 0.99 |
| Ge/Al | 0.943 | 0.881 | 0.905 | 0.510 | 1.07 |
| Al₂O₃/Al | 0.822 | 0.748 | 0.858 | 0.810 | 1.10 |

- **Frequency.** The AMM between half-spaces has no frequency dependence, and the Debye DMM is frequency-independent below both cutoffs. Film interference sets in at
  λ ≳ d_film. λ(1 THz, Al) = v_L/f ≈ 6 nm ≪ 40–600 nm, so the primary band is safe. At 0.1–0.3 THz, however, λ ≈ 20–60 nm, which is comparable to 40–60 nm films. Scope: the
  thick-film limit holds for primaries; for sub-THz NTL phonons in thin films it is a ζ_O lever, not an NR/ER primary signature.
- **Measured.** The effective Si→Al transmission is **0.3–0.55**, and specular (AMM) reflection is favoured over DMM (1805.02495 p.1 [FT]). The ideal-interface AMM above is
  an upper bound. Leman tunes the aSi–Al interaction to "∼33%" (1109.1193 p.14 [FT]). Kaplan's tabulated values were not accessed.
- **Mode and angle.** The best L/T contrast is 10% (Al₂O₃/Al). It multiplies an NR/ER difference in L fraction that is ∝ e^{−N_mix} → 0 (WP8R-C4f). The arrival angle distribution depends on
  geometry and position, not on event type. **Mode- and angle-selective transmission therefore carries no NR/ER information** [D given §2].

**3.3 Pair-breaking and trapping vs frequency [D for the limits, WP8R-C5].** WP5 (W13) gives η_pb = 2Δ_BCS/Ω for 2Δ_BCS ≤ Ω < 4Δ_BCS, with N_qp = 2. The asymptote is
0.57–0.6 (1401.1937 [FT], via WP5-v3 §5), and 1805.02495 Table I uses 0.57 [FT]. With Δ_BCS(Al) ≈ 0.18 meV [UNVERIFIED], 2Δ_BCS = 87 GHz and 4Δ_BCS = 174 GHz.
**Every arriving primary or NTL phonon (≳ 0.3 THz) sits on the flat η_pb branch.** Absorption per transit is ≈ d_film/L_pb(Ω) for d_film < L_pb (L₀ ∼ 720 nm,
1109.1193 p.17 [FT]), and L_pb(Ω) falls with Ω [UNVERIFIED form]. That makes thin films mildly frequency-selective, which again is a ζ_O lever between sub-THz NTL
phonons and ≥ 0.7 THz primaries; it does not apply to NR vs ER primaries, which share one spectrum. The other links of ϵ_prim (QP collection, trapping, the W TES; 2012.12430 App. p.15 [FT]; ϵ_prim ≈ 13–29%, 2301.08699 p.77 and 2012.12430
Table I [FT]) are energy-independent. W, Ti and Ir TES have smaller gaps still, so none of the listed sensors is frequency-selective in the arriving band. A frequency
cut inside that band needs 2Δ_BCS ≈ 3 meV (Nb-like [UNVERIFIED]; 0.73 THz, WP8R-C5c). Such a film rejects bulk-field NTL phonons and accepts part of the primary arrival.

**3.4 Observables.** Use either a fast/slow ratio O = E_fast/E_tot or a two-film ratio O = E_film1/(E_film1 + E_film2). With channel fractions a_pop per population and energy fractions φ_pop,
**O = Σ_pop a_pop φ_pop** (WP8R-C7a). The contrast between two populations is ζ_O ≡ a_L − a_p, and so on.

---
## 4. Figure of merit
**4.1 Definition [D].** 𝔖 ≡ |⟨O⟩_NR − ⟨O⟩_ER| / [½(σ²_NR + σ²_ER)]^{1/2} at equal total phonon energy E_tot, where
σ² = (σ_ph/E_tot)² + σ²_pos + ζ_O²σ²_φ + σ²_Nph.
- σ_ph = 2.65 eV, the baseline of the Si CPD (2012.12430 p.1 [FT]).
- σ_pos is the residual position and caustic dependence of a_pop after any position correction [E].
- σ_φ is the pair-number spread of φ_L: F_eh = 0.15 (ER), F_NR = 1 [E].
- σ_Nph is the phonon-number term: ≲ 0.9% at 100 eV, for f ≈ 1 THz and ϵ_prim = 0.13 (WP8R-C9b).

**4.2 (a) Primary route (zero field, mode selection) [WP8R-C7d, e].** Here ΔO ≤ ζ_O(1 − 𝔶)f_s.

| E_R (eV) | 50 | 100 | 300 | 1000 | 3000 |
|---|---|---|---|---|---|
| 𝔖 (Si, ζ_O = 1, σ_pos = 0) | 0.19 | 0.38 | 1.15 | 3.84 | 11.5 |

2σ is first reached at **0.52 keV (ζ_O = 1)** and **1.7 keV (ζ_O = 0.3)**, both with zero position spread. Any σ_pos ≥ ζ_O(1 − 𝔶)f_s/2 ≈ 0.7%·ζ_O caps 𝔖 below 2 at
every energy. For σ_pos = 0.02, 𝔖 < 1 everywhere (WP8R-C7e). CDMS pulses show position variations of order unity across the crystal (1109.4343 Figs. 1–2 [FT]).
**⇒ NO-GO, quantified.**

**4.3 (b) Gap-energy channel at zero field [WP8R-C9a].** Δf_g = 0.26 (Si) and 0.22 (Ge) is large, but §2 forces ζ_O = 0 under mode selection. Under timing, ζ_g depends on
τ_gap/τ_ph and on the bulk vs surface location of the release, and both are unknown at mK. This is a timing discriminant and is flagged (G-R2, IF-R2).

**4.4 (c, d) NTL route [WP8R-C7b, c, f–k].** ΔO = ζ_O·g(1 − 𝔶)/[(1 + g)(1 + 𝔶g)]. It is largest at **g = 𝔶^{−1/2}** with value (1 − √𝔶)/(1 + √𝔶), which for Si at 100 eV means
V_b ≈ 9.6 V. Results for Si, σ_ph = 2.65 eV:

| V_b | ζ_O = 0.3, σ_pos = 0.05: 𝔖 at 50/100/300/1000 eV | ζ_O = 0.5, σ_pos = 0.02 | ceiling 𝔖_int (ζ_O = 1, no noise, no position term) |
|---|---|---|---|
| 2 V | 1.14 / 1.44 / 1.60 / 1.63 | 2.34 / 3.79 / 5.73 / 6.53 | 5.6 / 7.9 / 13.7 / 25.1 |
| 4 V | 1.56 / 1.95 / 2.18 / 2.24 | 2.85 / 4.36 / 6.78 / 8.42 | 4.4 / 6.2 / 10.6 / 19.4 |
| 10 V | 1.63 / 2.04 / 2.41 / 2.56 | 2.32 / 3.34 / 5.44 / 7.95 | 2.6 / 3.7 / 6.4 / 11.6 |
| 100 V | 0.35 / 0.46 / 0.66 / 0.83 | 0.37 / 0.52 / 0.89 / 1.54 | 0.37 / 0.53 / 0.91 / 1.67 |

- **HV mode is NO-GO at any ζ_O for E_R ≤ 300 eV (WP8R-C7g, WP8R-C7l; the latter also holds at F_NR = 0.15).** When NTL energy dominates both populations, the observable becomes φ_L ≈ 1 − E_prim/(N_eh eV_b), with E_prim the primary phonon energy. The pair-number spread then
  swamps the 1 − 𝔶 difference.
- **Low bias (d).** At 100 eV the minimum contrast for 2σ is **ζ_O,min = 0.15 / 0.28 / 0.53 at σ_pos = 0.02 / 0.05 / 0.10** (best V_b = 7.5–10 V; WP8R-C7j). For ζ_O = 0.1 it
  fails at every bias (WP8R-C7f).
- Caveats [E]:
  - ε_eh, F_eh and 𝔶 at a few pairs;
  - charge trapping at low field at mK (θ_tr, WP7-E-v3);
  - σ_ph counted once for two channels;
  - 𝔶(100 eV) is a Lindhard truncation below the binary threshold.

---
## 5. Comparison with the precedent (CDMS phonon pulse-shape discrimination)
- **1109.4343 [FT].** SuperCDMS Soudan Ge iZIP, ±2 V, 7–20 keV_nr. One 40–70% risetime parameter rejects bulk ER against bulk NR at "1:10³ (limited by the statistics)".
  The authors attribute the information to charge: "Much of the essential information content of the charge measurement is duplicated in the phonon
  measurement, through the production of secondary phonon populations as charges propagate" (p.2). Primary phonons are treated as one quasidiffusive population whose
  shape depends only on position (p.2–3), and relaxation phonons are dropped (p.3). **This is mechanism (d), not (a).** The precedent supports §2: it finds no
  primary-population NR/ER signature.
- **Calibration (WP8R-C7k).** Read as a ≈ 3.1σ one-sided separation, it implies ζ_O/σ_pos ≈ 9.3 (Ge, g = 1.35, 𝔶(10 keV) = 0.23). Carried to a σ_ph = 2.65 eV Si device
  at 2–10 V with ζ_O = 0.3, this gives 𝔖 = 1.96 / 2.73 / 3.48 / 3.86 at 50 / 100 / 300 / 1000 eV.
  - Caveats: the iZIP contrast came mostly from **near-surface high-field** NTL (300/700 GHz, p.2–3), which a uniform low-field phonon-only device lacks; and a 10³
    leakage bound read as Gaussian 3.1σ is an assumption [E].
- **Other precedents (all charge-mediated).**
  - 2303.02067 [ABS] (EDELWEISS, NbSi athermal sensors) tags ionizing events through NTL phonons, with heat-only rejection "by more than a factor 5" above 3 keV.
  - 1405.4215 [ABS] gives phonon-only surface rejection of 4.5×10⁻⁴ at 46% NR acceptance, which is position information.
  - 1305.2405 [ABS] is charge plus phonon.
  - 1109.1193 p.17 [FT]: in CDMS Ge ER at ±3 V, NTL phonons are 56% of the signal and surface-recombination phonons 13%, the latter "in a low frequency, ballistic regime that is used to provide a surface-event discriminator".
- **What would be new.** Running (d) at sub-keV without charge readout, with a frequency-cut film (§3.3) supplying ζ_O. The decisive inputs are ζ_O and σ_pos, measured on an
  NR/ER calibration at V_b ≈ 5–10 V. **None is mode selection of primaries.**

---
## 6. IF-E7: the collection quantities δ and r (WP7-E-v3 (E8), (E13))
- **δ [E, WP8R-C8a].** NR and ER prompt phonons reach the sensors with one spectrum and one polarisation mix, apart from the ER soft excess. So
  δ_prim ≡ (ϵ_prim^ER − ϵ_prim^NR)/ϵ_prim^ER ≈ (1 − 𝔶)f_s(ϵ_soft/ϵ_hard − 1), and |δ_prim| ≤ 0.007 for |ϵ_soft/ϵ_hard − 1| ≤ ½. The memory-loss argument forces
  any larger δ to come from **non-spectral** differences: surface ΔE_esc, position distribution, or detector loss channels.
  - **⇒ δ cannot carry the 0.048 Si deficit of 1803.02903.** The deficit has to come from the r-term and/or stored energy (and ΔE_trap), as allowed by WP7-E-v3 (Ev3-C7e, h).
- **r [E].** NTL phonons are born at 0.3–0.7 THz (Ge, near-surface) or lower (bulk), so they skip the quasidiffusive stage. Primaries go through it. In CDMS geometry the
  two are absorbed with different time constants (1109.4343 p.2–3). r ≠ 1 is therefore expected, and r = 1.14 (WP7-E-v3) is physically admissible. Its **sign** depends on the
  window and geometry: ballistic phonons are absorbed slowly but avoid sub-gap down-conversion in the films. It cannot be fixed without a transport calculation
  (G-R1). Bound: |r − 1| ≲ 0.2 [E].

---
## 7. Exact remaining gaps
| # | Gap | Closing object |
|---|---|---|
| G-R1 | ζ_O, σ_pos and r for a concrete geometry | G4CMP-type transport (owner WP8; not run here by rule); or a measurement: NR/ER calibration at V_b = 5–10 V with fast/slow and Al/Nb two-film readout |
| G-R2 | release-time law of the gap energy at zero field, mK (excitons, traps, surface recombination) | WP7-E-v3 E_X, E_trap kinetics; measured τ_gap |
| G-R3 | created-phonon spectra of NR (E_R ≳ eV) and ER | WP5 §3.4 MD tables and the §2 e–ph kernel should record dℋ/dω (WP7-E-v3 mark dℋ/dω_ph) |
| G-R4 | 𝔶 and F_NR at E_R ≲ 350 eV | WP5 §3.3 non-adiabatic channel |
| G-R5 | Al, Ir elastic moduli [UNVERIFIED]; Kaplan 1979 not accessed | DB entry (JARVIS once reachable) or [FT] |

## 8. Checks (code/WP8-R/checks.py, 48/48 PASS)
| Group | Content |
|---|---|
| C1a–c | f_eq = B/A; f_*(1 µs) = 2.71 (Si) and 2.29 (Ge) THz; the Ge A spread moves f_* by ≤ (A_max/A_min)^{1/5} |
| C2a–c | ballistic thresholds; N_mix by 1 µs; diffusive r_rms |
| C3a–e | toy cascade: energy conservation (kernel and evolution); monotone loss of hard-part memory; TV < 0.05 by 100 ns; full TV ≤ 0.02 at 10 µs |
| C4a–f | sound speeds cross-checked; AMM t + 𝔯 = 1 (sympy); SH reciprocity; DMM detailed balance; transmission range; mode-contrast bound |
| C5a–c | η_pb limits; 4Δ_BCS(Al) < 0.2 THz; Nb-like cut at 0.73 THz |
| C6a, b | Lindhard 𝔶(100 eV); monotonicity |
| C7a–l | O algebra; Δφ_L closed form, optimum g = 𝔶^{−1/2} (sympy); primary-route 𝔖 table and E_2σ; NTL grid; HV ceiling and its F_NR sensitivity; ζ_O,min; CDMS calibration |
| C8a, b | δ_prim bound; η(r = 1) = 1 |
| C9a, b | gap-fraction difference; phonon-number term |

## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| f ≡ ω_{Qν}/2π; f_*(t) = (x_L𝒜_anh t)^{−1/5}; f_b; f_eq = 𝒜_iso/𝒜_anh; f_D | phonon frequency (Hz); quasidiffusive frequency at time t; 1-cm ballistic threshold; mixing/decay crossover; Debye frequency | **new** (f_D = source ν_D) |
| 𝒜_anh, 𝒜_iso | coefficients of Γ_anh = 𝒜_anh f⁵ (L only), Γ_iso = 𝒜_iso f⁴ (source "A", "B"; 1109.4343 and 2302.05998 use the same letters) | **new** (source A, B → source-only) |
| x_L | steady longitudinal fraction after isotope mixing | **new** |
| N_mix, r_rms, t_mem, ℓ_mem | integrated mode-mixing events; diffusive spread; memory time and length | **new** |
| f_s, Δf_g | ER soft (born-ballistic) energy fraction; NR/ER gap-energy fraction difference | **new** |
| 𝔶 | energy-equivalent NR ionization yield ⟨N_eh⟩ε_eh/E_R (Lindhard f_n under WP5 L20 truncation; ≠ source y of 1803.02903) | **new** |
| O, a_pop, φ_pop, φ_L, E_prim, ζ_O, σ_pos, σ_φ, σ_Nph, σ_ph, 𝔖, 𝔖_int | mode-ratio observable; channel fraction (not α); energy fraction (not a Fano factor); NTL fraction; primary phonon energy; contrast; position spread; pair-number and phonon-number spreads; sensor baseline; separation; pair-number ceiling | **new** |
| t^{AMM}_L, t^{AMM}_T, t^{AMM}_{SH}, t^{DMM}_{12}, 𝔯, Z^{ac} = ρc_ν, L_pb(Ω) | AMM and DMM transmissions (the t-family of NOTATION §G t_esc); reflection; acoustic impedance; pair-breaking length | **new** |
| δ_prim, ϵ_soft, ϵ_hard, τ_gap | spectral part of δ; collection of soft and hard phonons; gap-energy release time | **new** |
| used unchanged | ω, ω_{Qν}, ν (branch), c_ν, E_R, x_R, ρ^ph_κ, ℋ, E_g, ε_eh, F_eh, N_eh, N_qp, η_pb, Δ_BCS, E_st, E_X, E_trap, E_esc, E_car, t_pr, ϵ_prim, ϵ_NTL, δ, r, g, V_b, Y_H, η^φ_NR, θ_tr, d_film | NOTATION / WP5 / WP7-E-v3 |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-R1 | WP5 (v4) §2, §3.4 | created-phonon spectra | record dℋ/dω_{Qν} (branch-resolved) for ER relaxation and NR MD tables; f_s and the NR optical share are [E] until then |
| IF-R2 | WP7-E-v3 / WP8 | gap-energy release time | τ_gap at mK zero field enters any timing discriminant (Δf_g = 0.26 Si); add θ_gap (type T) if WP8 uses timing |
| IF-R3 | WP7-E-v3 IF-E7 | δ, r | δ_prim ≤ 0.007 (spectral part); the 0.048 deficit must be r and/or E_st, ΔE_trap and non-spectral δ; r ≠ 1 expected, sign open (G-R1) |
| IF-R4 | WP8 | discrimination menu | drop mode/frequency/angle selection of primaries (NO-GO, §4.2) and HV-mode phonon PSD at E_R ≤ 300 eV (𝔖_int < 2 for F_NR ≥ 0.15). Keep low-bias phonon-only NTL PSD as CONDITIONAL with requirement ζ_O ≥ 0.28 at σ_pos = 0.05 (Si, 100 eV) |
| IF-R5 | WP6 | nuisances | if (d) is used: θ_ζ (contrast, M), θ_pos (σ_pos, M), F_NR (A) |
| IF-R6 | coordinator: SOTA | statement | "Phonon NR/ER information at the sensors is charge-mediated; prompt populations lose frequency/polarisation memory in ≈ 10–100 ns, ≲ 0.1 mm (WP8-R §2)" |

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L39 | WP5 (W4) prompt ℋ → down-conversion Γ = 𝒜_anh f⁵ (L), mixing 𝒜_iso f⁴ → scaling spectrum in f/f_*(t) | 1109.1193 Table I; 2302.05998 §2.2.2; 2408.04732 Tables 3–4 [FT] | isotropic Debye-like solid; f ≪ f_D; mixing faster than decay (f < f_eq); no surfaces | anisotropic rates, surface down-conversion (∼0.1%/bounce, 1109.1193 p.14), film-induced down-conversion | DERIVED (scaling) / E (WP8R-C3) |
| L40 | AMM (isotropic, welded) and Debye DMM at substrate/film | Kaplan 1979 [UNVERIFIED, not accessed]; measured Si→Al 0.3–0.55 (1805.02495 [FT]) | λ ≪ d_film; clean interface; isotropic media | oxide/aSi layers, anisotropy, partial specularity | ESTIMATED (WP8R-C4) |
| L41 | WP5 (W13) η_pb(Ω) flat above 4Δ_BCS → no frequency selectivity in Al/W/Ti/Ir sensors | WP5-v3 §5; 1401.1937 via WP5-v3 [FT]; 1805.02495 η_pb = 0.57 [FT] | Ω ≥ 4Δ_BCS; uniform film | film escape (L₀ ≈ 720 nm), QP trapping geometry | DERIVED (limits; WP8R-C5) |
| L42 | NTL-route separation 𝔖 = ζ_O g(1−𝔶)/[(1+g)(1+𝔶g)]/σ, optimum g = 𝔶^{−1/2}; HV ceiling 𝔖_int | 1109.4343 [FT] (precedent), 2303.02067 [ABS] | equal E_tot; Gaussian spreads; ε_eh constant at few pairs | F_eh, F_NR at few pairs; low-field trapping; σ_pos | DERIVED (algebra, WP8R-C7b, c) / E (numbers) |
