# R12 / WP7-D-v2: extensions beyond single-vertex golden-rule rates (coherent fields, fermionic absorption, two insertions, out-of-scope interfaces), corrected standalone version

Revision agent, R12 correction round. Supersedes returns/R10/WP7-D.md (v1, kept as the record). Applies every verdict of the R11 referees
referees/R11/REF-WP7-D-A.md (items "A-n" for claims, "A-Cn" for corrections) and REF-WP7-D-B.md ("B-Vn", "B-An"); closing table §9.
Architecture: returns/R8/WP0-v3.md, cited "WP0 (n)", read through state/CORRECTIONS.md. Conventions: CONVENTIONS.md (HL units e² = 4πα,
campaign signs of q, ω and Fourier transforms (§2–§3), tr[𝔇ᵀS]); symbols: NOTATION v4 + R9 rows; new symbols §6.
Checks: `code/WP7-D-v2/checks.py` (v1 checks C1–C15 kept, C3 now a plain integrand identity; N1–N13 new), sympy + mpmath, **49/49 PASS,
≈ 5 s**, cited WP7D-Cn / WP7D-Nn. Tags: [D] derived (hypotheses stated), [D, sketch], [E], [C]; literature [FT] (whole text read), [ABS]
(abstract, or abstract plus a named section), [UNVERIFIED]. Full texts were fetched with lit.py (literature/papers-WP7-D/ in R10,
literature/papers-WP7-D-v2/ in R12; PDFs deleted). Every arXiv ID was verified against the arXiv API. Status of all content: CLAIMED.
Halo: every source rate quoted at ρ = 0.39 or 0.4 GeV/cm³ is rescaled to CONVENTIONS §8 (ρ_χ = 0.3) whenever it enters a LIMITS row.
**Displayed equations of this return:** (D.1)–(D.9), (F.1)–(F.7), (T.1)–(T.4), (S.1)–(S.2). No other label is cited.

## 0. What changed (v1 → v2; one line per substantive change, details in §9)
| v1 | v2 | change (referee item) |
|---|---|---|
| §1.4(i) mean power = golden rule "for any t_int" | §1.4(i) | only for t_int ≫ min(t_coh, 1/Γ_T) and a stationary coupling; otherwise Fejér-windowed (A-C1, B-V3) |
| (D.1) weight at k = +m_φv | (D.1), (D.3) | weight at k = −m_φv (CONVENTIONS §2); (D.3) pairs 𝒮_φ(k,ω) with R(−k,ω) (B-A1) |
| R_{I⁺I⁻}, sign of ⟨I^z⟩ unstated | (D.4) | R_{I⁺I⁺} in (3.2) order, ⟨I^z⟩ < 0 for absorption; spin temperature for prepolarised samples (B-A2, A-C4) |
| 1306.6089 "resonant growth agrees" | §1.5 | factor-2 amplitude UNRESOLVED (B-A2) |
| crossover (3/2)t_coh; Rayleigh "O(1)" | §1.6 | crossover O(1)·t_coh; random-amplitude penalty 3–10 (1905.13650) for fixed-amplitude analyses, already inside (D.6) (A-C2, A-C3, B-A3) |
| "1/ε₀ is the slab case" | §1.3, §1.7 | withdrawn (REFUTED as exclusive): bulk also gives 1/ε₀; geometry factors 1 / 3ε₀/(ε₀+2) / ε₀ (A-C7, B-A4) |
| (D.7) P_abs | (D.7) | P_abs/V (A-C5); Q_DM^eff frequency and annual dependence (A-C6) |
| §1.8 citation, "0.045 for Cu" | (D.8) | "Eq. (7) and following text"; correction 2δ_rel^a [E], (Zα)² only an upper bound (A-C8, B-A5) |
| §1.9 LSWT computes the source regime | (D.9), §1.10 | LSWT only for T ≪ T_CM; near-T_CM response is an exact remaining gap (B-A6) |
| 2011.01940 "exact"; "−5%, < 10⁻³"; "the source flags (Zα)²" | §2.4(b) | spin convention derived (N5); sizes −11% (Xe K, 100 keV) and −34% to −41% (56.5 keV), valence +0.7–2%; paper-error status UNRESOLVED; source statement corrected (A-C10, A-C11, B-A7) |
| L-D8 without 2308.00309 | (F.7) | 2308.00309 read in full: light scalar mediator, t = 2m_χω − m_χ² (A-(f)) |
| (T.1) (S†S)ψ̄γ^μγ₅ψ | (T.1)–(T.2) | Lorentz-invariant i(S†∂↔S) for V, A with velocity-dependent pair tensor; per unit volume; identical-boson ½ (A-C12, B-A8) |
| dark Compton "first order in e"; "O(x²) relativistic" | (T.4) | amplitude O(e²κ_mix); NR seagull = 2109.08168 Eq. (2) through O(x²), first difference at O(x³), attribution UNRESOLVED (B-V13) |
| I2 radiative part ∝ Re n_r | §4.2 | M1: ∝ n_r³ (E1 would be ∝ n_r) (A-C13, B-A9) |
| X readout, ε polarisation | §6 | renamed X_rd, e_λ/e′_λ′ (B-A10) |

---
## 1. The coherent classical-field regime (S4, S9, A9, §10(ii))

### 1.0 Regime and scales [D for definitions, E for numbers]
A bosonic DM field φ of mass m_φ is classical when N_dB ≡ (ρ_χ/m_φ)(2π/(m_φv₀))³ ≫ 1: N_dB(1 eV) = 1.1×10⁶, N_dB = 1 at m_φ ≈ 33 eV (WP7D-C7).
Reference scalars: **t_coh ≡ 2π/(m_φv₀²)** (6.6 ms at 1 μeV), **ℓ_coh ≡ 2π/(m_φv₀)** (1.6 km at 1 μeV). The DM line is one-sided,
(ω − m_φ)/m_φ ∈ [0, v_max²/2] = [0, 3.51×10⁻⁶] for v_max = 794.5 km/s (WP7D-N11). Time scales: 1/m_φ, t_coh, the target response time
1/Γ_T (T₂ for spins, Q_mode/ω_n for a resonator), t_int. Length scales: ℓ_coh and the sample size L_s; for L_s ≪ ℓ_coh the field is uniform over
the sample and k_φ = m_φv is replaced by the body's mode structure (§1.3).

### 1.1 Field model [D; Gaussian stationary field, NR halo, no self-interaction]
⟨φ(x,t)φ(x′,t′)⟩ = (ρ_χ/m_φ²)∫d³v f_χ(v)cos[ω_v(t−t′) − m_φv·(x−x′)], ω_v = m_φ(1 + v²/2). With the inverse transform of CONVENTIONS §2,
⟨φφ⟩ = ∫d³k/(2π)³∫(dω/2π)𝒮_φ(k,ω)e^{−ik·(x−x′)−iω(t−t′)}, the positive-frequency weight sits at **k = −m_φv** (WP7D-N2):

  𝒮_φ(k,ω) = (ρ_χ/2m_φ²)(2π)⁴∫d³v f_χ(v)[δ³(k + m_φv)δ(ω − ω_v) + δ³(k − m_φv)δ(ω + ω_v)],   ∫(dω/2π)𝒮_φ(ω) = ρ_χ/m_φ².          (D.1)

k-integrated: 𝒮_φ(ω>0) = (πρ_χ/m_φ²)F_φ(ω), F_φ(ω) ≡ f_sp(v)/(m_φv)|_{v=√(2(ω−m_φ)/m_φ)}, ∫F_φdω = 1 (WP7D-C2a). The plane-wave component
∝ e^{i(m_φv·x − ω_vt)} couples through y_φ∫φO to O(+m_φv) (O(q) = ∫e^{+iq·r}O(r)). The sign is immaterial for P,T-invariant targets but
binding (CONVENTIONS §3) for §1.9. *Literature limit.* 1711.10489 Eq. (10) [FT] (Rayleigh-amplitude, random-phase field) and Eq. (24)
(exponential law with mean λ(ω) = Aπf(v)/(m_av)) follow from (D.1) through their flux map Eqs. (12)–(15) (WP7D-C2b).

### 1.2 Couplings and operator rows (truncation chain) [D]
H_int(t) = y_φ∫d³x φ(x,t)O(x) (WP0 (3.3)), with O per coupling: dark photon, κ_mixeJ^μ_em with WP0 (3.6); g_aγγ in B₀, WP0 (2.9); ALP–electron,
NLO 2 tr J_e(k) (WP0 §2, 2106.12586 Eq. (18)); ALP–nucleon gradient, the nuclear-spin row I_κ^β with vertex ∝ g_aNN k_φ^β; nucleon EDM,
Σ_I d_EDM E*_I·𝐈_I (site-resolved spin row, E*_I a DFT material constant); scalar moduli (1508.01798 Eq. (1)), δm_e/m_e couples to
∂H/∂ln m_e = −T_e (row 𝒯_e at k → 0, exact for H_C) and δα/α to ∂H/∂ln α = the Coulomb energy, **a new row a = (C, 𝔘), 𝔘_C(k)** (IF-D2).
Chain: WP0 (3.3)/(3.5) single vertex, first order in y_φ, linear response, any sector (GS for phonons/BAR/strain, X for dark-photon absorption,
spin rows with the (1.2) Zeeman option, B₀ ≠ 0); 𝒳 per platform; n_T enters through detailed balance and noise (D.6). No new τ slot; new
metadata geom ∈ {bulk, body} (IF-D3).

### 1.3 Coherent signal amplitude [D, Kubo; linear response, stationary state before the drive, (3.2) index order]
For a drive component φ_k(t) and any readout O_rd,

  δ⟨O_rd(k)†⟩(t)/V = y_φ∫_{t₀}^{t}dt′ R_{rd,O}(k; t−t′)φ_k(t′),   R_ab(k;t) ≡ −(i/V)θ(t)⟨[O_a(k,t)†, O_b(k,0)]⟩,                           (D.2)

and in steady state (t − t₀ ≫ 1/Γ_T), for φ = Re[φ_c e^{i(k·x−ωt)}], δ⟨O_rd†⟩/V = (y_φ/2)φ_c e^{−iωt}R_{rd,O}(k,ω). The coherent signal is the
**off-diagonal retarded response R_{rd,O}** at (k,ω) ≈ (m_φv, m_φ), an element of the matrix whose diagonal gives the rates. The Kubo sign is
tested on a quantum two-level system against the golden rule (WP7D-N1).
- *Finite body (L_s ≪ ℓ_coh):* k → 0 and R_{rd,O}(ω) = Σ_n ⟨0|O_rd†|n⟩⟨n|O|0⟩/(V(ω − ω_n + iΓ_n/2)) − (n, −ω)*, over the body's normal modes.
- *Photon-mediated couplings:* for a non-relativistic dark photon (k_φ ≪ ω) the bulk in-medium mixing of WP0 (3.6) already gives E′ ∝ κ_mix/ε(ω).
  For L_s ≪ 2π/m_φ the sample shape multiplies this bulk field by an orientation factor: **1 for E′ normal to a slab, 3ε₀/(ε₀+2) for a sphere,
  ε₀ for E′ parallel to a slab** (WP7D-N10) [D, sketch: electrostatic boundary conditions]. v1's "the 1/ε₀ of 2501.05504 Eq. (5) is the slab case"
  is **withdrawn**: the source attributes it to bulk screening ("Since the BAR is also dielectric"), and bulk and slab-normal coincide.

### 1.4 Absorbed power; the golden rule as the incoherent, long-record limit [D]
Time-averaging ⟨φ∂_tH_int⟩ with (D.2), (D.1), for a stationary (always-on) coupling and t_int ≫ min(t_coh, 1/Γ_T):

  P_abs/V = −2y_φ²∫d³k/(2π)³∫₀^∞(dω/2π) ω 𝒮_φ(k,ω) Im R_OO(−k,ω) = −y_φ²ρ_χ∫d³v f_χ(v)(ω_v/m_φ²) Im R_OO(m_φv, ω_v).           (D.3)

Monochromatic case: −(y_φ²ωφ_c²/2)Im R = ω n_φ Γ_net with WP0 (3.5) (WP7D-C1a; sign on a classical mode C1b and a quantum two-level system N1).
- **(i)** For **t_int ≫ min(t_coh, 1/Γ_T)** (the record resolves the wider of the DM line and the target line) the mean absorbed power and the mean
  number of events P_abs t_int/ω equal the f_χ-averaged golden rule (3.5). For shorter records the mean energy absorbed is (D.3) with
  𝒮_φ convolved with the Fejér window (t/2π)sinc²(ωt/2) and need not be linear in t. Example: (D.4) at δω_L = 0, t ≪ T₂, t_coh gives M_⊥ ∝ t
  and absorbed energy ∝ t² (no rate). Coherence never changes a mean linear in ⟨φφ⟩; the relevant mean is the windowed one.
- **(ii)** Statistics: absorption events from a Gaussian field are Bose-bunched, Var N = N̄ + N̄²/𝒩_c over 𝒩_c coherence cells (chaotic-light
  result) [D, sketch]; Poisson is the incoherent limit 𝒩_c ≫ N̄ (IF-D7).
- **(iii)** A mean-field readout ⟨O_rd⟩ is ∝ y_φ (|R_{rd,O}|); a calorimetric/counting readout is ∝ y_φ² (Im R_OO).

### 1.5 Spin precession (S4: CASPEr-electric, -gradient) [D]
Nuclear spins in B₀ ∥ z, H = +ω_LI^z (ω_L > 0), transverse relaxation T₂. In the (3.2) order with a = b = I⁺ (O_a† = I⁻),
⟨[I⁻(t), I⁺]⟩ = −2⟨I^z⟩e^{−iω_Lt}, so **R_{I⁺I⁺}(0,ω) = −(2⟨I^z⟩/V)/(ω − ω_L + i/T₂)**; −Im R > 0 (absorption) requires ⟨I^z⟩ < 0, the
polarisation of the lower Zeeman level (WP7D-N3). With the rotating-frame Rabi frequency Ω_a and δω_L ≡ ω_L − m_φ, (D.2) is the
linearised Bloch equation, m(t) = iΩ_aM₀(1 − e^{−(iδω_L+1/T₂)t})/(iδω_L + 1/T₂) (WP7D-C5a):

  |M_⊥(t)| = M₀Ω_a·2|sin(δω_Lt/2)|/|δω_L|  (t ≪ T₂),     |M_⊥| = M₀Ω_aT₂/√(1 + δω_L²T₂²)  (t ≫ T₂).                                 (D.4)

*Literature limits.* 1306.6089 Eq. (1) [FT], M(t) ≈ npμE*ε_Sd_n sin[(2μB_ext − m_a)t/ħ]/(2μB_ext − m_a)·sin(2μB_ext t). (a) Envelope: the exact form is
sin(δω_Lt/2)/(δω_L/2) (WP7D-C5b), the printed resonance is half as wide (first zeros π/t vs 2π/t); both referees CONFIRMED this; the carrier
is also approximate ((ω_L+m_a)/2 exact vs ω_L). (b) **Amplitude: UNRESOLVED by a factor 2.** The source defines d_nε_SE* as "the energy shift
produced between spin-up and spin-down states", i.e. the splitting; the rotating-frame Rabi frequency is then Ω_a = d_nε_SE*/2 and Eq. (1) is 2×
the linear response at δω_L = 0. The two agree if d_nε_SE* is read as half the splitting (the H = −dσ·E convention). (IF-D11.)
2101.01241 Eq. (1) [FT], M_a = uM₀Ω_aT₂cos(ω_at), is the second form at δω_L = 0 (WP7D-C5c). Their spectral factor u (defined in their
supplement, ref. [53], not read) is the overlap of the inhomogeneous spin line, the DM line and the Lorentzian of (D.4) [D, sketch].
*Corrections.* (a) T₂ > t_coh: the drive is a line; use |R|²𝒮_φ in (D.5) (1306.6089's T_b = min(τ, T₂), Eq. (3) HTML = (A2) PDF).
(b) Inhomogeneous broadening enters as the site sum in R_{I⁺I⁺} (GIPAW shielding/EFG). (c) **Noise of prepolarised samples.** CASPEr samples are
prepolarised and out of equilibrium (T₁ of hours). The FDT noise of (D.5) then holds at a **spin temperature β_s defined by tanh(β_sω_L/2) = p**
(polarisation p), not at the lattice β: coth(β_sω_L/2)·⟨I^z⟩ is independent of p, matching 1306.6089 §A.3 ("unaffected by the polarization"),
Eq. (2) HTML = (A1) PDF. At the lattice β the noise would wrongly scale as p/p_eq.

### 1.6 Signal-to-noise ratio versus t_int/t_coh [D; Gaussian signal and noise, periodogram/likelihood analysis]
Readout X_rd ≡ O_rd(k→0) of the whole sample. Two-sided PSDs:

  𝒮^{sig}(ω) = y_φ²V²|R_{rd,O}(0,ω)|²𝒮_φ(ω),     𝒮^{int}(ω) = −V coth(β_sω/2) Im R_{rd,rd}(0,ω)   (FDT, WP0 (4.1), at the spin/system temperature),     (D.5)

plus detector noise 𝒮^{det}; 𝒮_n = 𝒮^{int} + 𝒮^{det}. The weak-signal Asimov statistic of the exponential-bin likelihood is

  TS_A = t_int∫₀^∞(dω/2π)[𝒮̃^{sig}_{t_int}(ω)/𝒮_n(ω)]²,   𝒮̃^{sig}_{t} = 𝒮^{sig} ∗ (t/2π)sinc²(ωt/2),                                       (D.6)

- **t_int ≫ t_coh, 1/Γ_T:** TS_A = t_int∫(dω/2π)(𝒮^{sig}/𝒮_n)²; threshold amplitude ∝ **𝒮_n^{1/2}(t_coh t_int)^{−1/4}**.
- **t_int ≪ t_coh:** one (Fejér-broadened) bin carries the signal; threshold amplitude ∝ **𝒮_n^{1/2}t_int^{−1/2}**.
- **Crossover at t_int = O(1)·t_coh.** v1's "(3/2)t_coh" holds only for a box line, the bin-offset-averaged bin, and the weak-signal form: at
  TS = 2.71 a single bin needs s/b = 2.65 with the exact statistic 2[s/b − ln(1 + s/b)] but 1.65 (2.02 offset-averaged) with Σ(s/b)²
  (WP7D-N4, C4a–c). The constant is not used in any LIMITS row.
- **Random amplitude.** For t_int ≲ t_coh the amplitude is a single Rayleigh draw. The exponential-bin likelihood behind (D.6) (complex Gaussian
  signal plus noise) already contains it. Analyses that treat the amplitude as deterministic overestimate limits by factors **3–10**
  (1905.13650 [ABS]). Apply one or the other, never both.
*Literature limits.* 1306.6089 Eqs. (8)–(9) (HTML numbering; (A7)–(A8) in the PDF) [FT], B_s = √S_n T^{−1/2} (T < τ) and √S_n(τT)^{−1/4} (T > τ):
the two scalings. 1711.10489 Eq. (54) [FT], Ã_95% = √(2.71[(Tπ/2m_a)∫dv f²/(vλ_B²)]^{−1}): (D.6) in the long-record limit (integrand identity,
WP7D-C3). Eq. (63), S/N = |Φ|(Tτ)^{1/4}/√λ_B, and Eq. (69), S/N ≈ 1.8 TS^{1/4}: the same limit.

### 1.7 Acoustic resonators (A9: piezoelectric BAR/hBAR) [D for the structure; source prefactor not re-derived]
O = −E′·P, P^i = e^{ijk}_pt∇^ju^k (GS sector). For mode n with width γ_n, (D.3) with the halo line gives

  P_abs/V = −y_φ²(ρ_χ/m_φ)∫dω F_φ(ω) Im R_mode(ω),   R_mode(ω) = (|⟨n|O|0⟩|²/V)[1/(ω − ω_n + iγ_n/2) − 1/(ω + ω_n + iγ_n/2)].         (D.7)

*Literature limit.* 2501.05504 Eq. (7) [FT], P_s = 32κ²(ρ_V/ρ²)(e_pt²/ε₀²)(M_n/L₀²)m_V²γ_ncos²θ_V/((m_V² − ω_n²)² + (ω_nγ_n)²) with γ_n = ω_n/Q_s,
Q_s = min{Q_p, Q_DM}, is (D.7) in the monochromatic limit γ_n ≫ 2π/t_coh; on resonance 1/γ_n = Q_s/m (their Eq. (8), WP7D-C6b). For their
stated regime Q_p ≫ Q_DM the narrow Lorentzian integrates to (π/2)δ (WP7D-C6a) and Q_s → **Q_DM^eff ≡ (π/2)m_φF_φ(ω_n)**, maximum 1.3×10⁶ (boosted
SHM), 2.4×10⁶ (rest-frame Maxwellian) (WP7D-C6c). Their "Q_DM ∼ 10⁶" is the peak value, not an error (both referees: a consistent
reinterpretation). Q_DM^eff depends on the operating point through F_φ(ω_n) and carries the annual modulation of v_E(t). This is the standard
narrow-resonator haloscope result, not a new one. The prefactor 32 and M_n are not re-derived (IF-D12). Geometry factor: §1.3.

### 1.8 Oscillating constants, resonant-mass detectors and clocks (§10(ii)) [D for the scaling; D, sketch for the drive; E for corrections]
H_C (WP0 (1.1)) with M_κ → ∞ is unitarily equivalent to α²m_eH̃ with lengths in units of 1/(αm_e) (WP7D-C15), so

  h_mod ≡ δa/a = −δα/α − δm_e/m_e = −(d_{m_e} + d_α)√(4πG_N)φ,   O = −(δm_e/m_e)𝒯_e(0) + (δα/α)𝔘_C(0).                                    (D.8)

*Literature limit.* 1508.01798 Eq. (7) [FT] (ℛ^eff_{i0j0} = δ_ijḧ) **and the definition of h in the text after it**; their Eq. (8),
F_mod,n = −ḧM°RJ_n, is the mode force. At k → 0 a static modulus only moves the equilibrium (comoving coordinates; uniform-dilation analogue of
the WP0 (4.8) Ward identity), so the drive is ∝ ω² [D, sketch]. *Corrections [E].* (a) Finite nuclear mass: O(κ_BO⁴) times the ZPR fraction
(~10⁻³). (b) Relativistic terms: writing a = a_nr(1 + δ_rel^a(α)) with δ_rel^a ∝ α², dln a/dln α = −1 + 2δ_rel^a, twice the fractional
scalar-relativistic lattice shift; for Cu this is |2δ_rel^a| ≈ 0.01–0.02, negative [E, typical DFT scalar-relativistic shifts, UNVERIFIED].
v1's 0.045 is the nuclear (Zα)², a core-electron number; it is kept only as an upper bound. (c) Clocks (1405.2925, [ABS]): static k = 0
responses to the same operator.

### 1.9 Multiferroic / magnetoelectric axion coupling (S9) [D, sketch]
2102.10171 Eq. (5) [FT, PDF], δE_ae ≈ −iħg_ae(∂_ta/2m_e²c)⟨Ψ|σ·∇|Ψ⟩, is the row 2 tr J_e of WP0 §2. The magnetisation readout is

  δM(ω) = y_φV R_{s^z,trJ_e}(0, ω)a(ω),   R_{s^z,trJ_e} ≠ 0 only if P and T are both broken (WP0 (4.3)).                                   (D.9)

Their Eq. (10), |δM/θ₀| = |χαM₀/2α_M − cP₀/2m_P²|/√((ω_a² − ω_M²)² + η_M²ω_a²), comes from Ginzburg–Landau equations for the **longitudinal**
M dynamics with damping η_M added by hand, in the regime T ≈ T_CM with critical slowing down τ ∼ |T − T_CM|^{−νz} (their Eq. (9)). Reading it
as a single-pole approximation of (D.9) is a sketch. **Computability:** LSWT on a T = 0 DFT+SOC magnetic structure (ref = LSWT, conserving as
WP0 (1.2) requires) gives (D.9) only for T ≪ T_CM; it has no pole that softens at T_CM. **Exact remaining gap:** the near-T_CM (critical)
response, the regime the source targets, needs a finite-T spin-dynamics method (e.g. stochastic LLG or quantum Monte Carlo plus analytic
continuation on a DFT-derived spin model with the tr J_e vertex). It is not computed by any URF route (IF-D13).

### 1.10 Computation specification (item 1)
- **Regime test first:** t_int ≫ min(t_coh, 1/Γ_T) for rate-type use of (D.3); otherwise the windowed form (§1.4(i)).
- **Inputs.** Halo F_φ (CONVENTIONS §8, v_E(t)). NMR: B₀, g_I, shielding/EFG (GIPAW in QE or CASTEP), E*_I (DFT), T₂ and T₁ from data;
  **noise at the spin temperature β_s from the prepolarisation p**. BAR: elastic and piezoelectric tensors (DFPT), FEM modes and the
  orientation factor, Q_p from data. Moduli: dln a/dln α, dln a/dln m_e from DFT with scaled constants plus scalar-relativistic and ZPR
  corrections; J_n by FEM. Multiferroic: LSWT/TDDFT+SOC for T ≪ T_CM only (new module, ~10³ core-h); near T_CM, gap (§1.9).
- **Grids.** ω ∈ [m_φ, (1 + 3.6×10⁻⁶)m_φ] (the one-sided line, WP7D-N11), ≥ 3000 points; t_int from 10⁻²t_coh to 10³t_coh.
- **Convergence.** TS_A to 1% under halving δω; FEM ω_n to 0.1%. **Cost.** Seconds per (m_φ, t_int) once R is tabulated; DFT 10²–10⁴ core-h.
- **Outputs.** 𝒮^{sig}, 𝒮^{int}, TS_A(t_int), P_abs, 𝒩_c, with τ string + geom.

---
## 2. Fermionic absorption (A10: χ + target → ν̃ + target excitation)

### 2.1 The missing operator class [D]
H_int = Λ_F^{−2}Σ∫d³x [ν̃̄Γχ][ψ̄Γ′ψ] + h.c., with a relativistic outgoing light fermion ν̃ (mass m_ν̃, k_ν̃ = p_χ − q, E_ν̃ = √(k_ν̃² + m_ν̃²)).
Target bilinears map onto existing rows as in WP0 §2 (ψ̄γ⁰ψ → n; ψ̄γψ → j + magnetisation current; ψ̄ψ → n + 𝒯-type; ψ̄γγ₅ψ → 2s;
ψ̄γ⁰γ₅ψ → 2 tr J). The new class is DM-side: 𝔏^{ab}(q,v) ≡ (2j_χ+1)^{−1}Σ_spins(Λ_F^{−2}ū_ν̃Γ_au_χ)*(Λ_F^{−2}ū_ν̃Γ_bu_χ) and

  𝔇^F_ab(q,v) ≡ 𝔏_ab/(4E_χE_ν̃),     ω^F_q(v) ≡ E_χ(v) − E_ν̃(|m_χv − q|).                                                                 (F.1)

### 2.2 Master formula [D; first Born; DM plane waves; ν̃ free and neutral; Gibbs target; relativistic normalisation of χ, ν̃]

  Γ^F_χ(v) = ∫d³q/(2π)³ tr[𝔇^{Fᵀ}S(q, ω^F_q(v))],     dℛ/dω = (ρ_χ/m_χρ_T)∫d³v f_χ∫d³q/(2π)³ tr[𝔇^{Fᵀ}S(q,ω)]δ(ω − ω^F_q(v)).         (F.2)

Only the existing S_ab is needed, on the curve ω = m_χ − q (v → 0, m_ν̃ → 0), at q ≈ m_χ. Isotropic S̄, unpolarised DM:

  dΓ^F_χ/dω = q𝔏(q)S̄(q,ω)/(8π²m_χ),   q = m_χ − ω.                                                                                     (F.3)

### 2.3 Vector and scalar operators [D; (L) of WP0 (4.6)]
*Vector* Λ_F^{−2}(ν̃̄γ_μP_Rχ)(ψ̄γ^μψ): 𝔏^{μν} = Λ_F^{−4}[k^μp^ν + k^νp^μ − g^{μν}k·p ∓ iε^{μναβ}k_αp_β]; with continuity J_L = (ω/q)n (WP7D-C8a–c):

  Γ^F_V = ∫d³q/(2π)³(1/4Λ_F⁴)[(m_χ²/q²)S_nn(q, m_χ−q) + S_{J_TJ_T}(q, m_χ−q) + P-odd S^A_{J_TJ_T} term],   (q + ω) = m_χ at v = 0.       (F.4)

The density coefficient is exact for bound or free targets under (L). The ε-term pairs with the P-odd S^A_{J_TJ_T} (chiral targets; WP4 [3.3]; needs
the tr[𝔇ᵀS] order). *Scalar* Λ_F^{−2}(ν̃̄P_Lχ)(ψ̄ψ): 𝔏_S = E_ν̃m_χ/Λ_F⁴ (C8d), so

  Γ^F_S = ∫d³q/(2π)³(1/4Λ_F⁴)S_nn(q, m_χ−q) + O(𝒯-row).                                                                                (F.5)

### 2.4 Literature limits [D]
**(a) Neutral current on nuclei.** Free nucleus, S_NN = 2π𝓃_κA_κ²|F^M_κ|²δ(ω − q²/2M_κ); (F.4) gives (WP7D-C9)

  Γ^F = 𝓃_κA_κ²|F^M_κ|²σ_NC/(1 + q₀/M_κ),   m_χ = q₀ + q₀²/2M_κ,   σ_NC ≡ m_χ²/(4πΛ_F⁴);   Γ^F = 𝓃_κA_κ²|F^M_κ|²σ_NC(1 − m_χ/M_κ + …).   (F.6)

1905.12635 Eq. (4) [FT], R = (ρ_χ/m_χ)σ_NC Σ_jN_{T,j}A_j²F_j²Θ(E⁰_{R,j} − E_th), σ_NC = m_χ²/(4πΛ⁴) (operator Eq. (1)), is (F.6) at M_κ → ∞
(source ρ_χ ≃ 0.4, rescale to 0.3). Wording (A-C9): the density row alone gives q₀²/(1 + q₀/M) = m_χ²(1 − 2m_χ/M + …); the longitudinal
current (continuity) changes only the O(m_χ/M) term to −m_χ/M. **Corrections:** (i) −m_χ/M_κ; (ii) crystal line shape at K = imp (WP0 L6),
σ_ω/E⁰_R = 2√(⟨p²_κ⟩/3)/m_χ ≈ 4×10⁻³ (Si, 10 MeV) [E], plus ±m_χv (1905.12635: "ΔE_R/E_R ∼ 10⁻³"); (iii) nuclear internal excitation for
q ≳ 1/r_N (outside; 2405.05728 [ABS]).
**(b) Electrons (atoms).** *Spin convention, derived (A-C10, B-L-D8).* From (3.1) per atom, with the continuum normalisation of 1509.01598
Eq. (49) (⟨k′l′m′|klm⟩ = (2π)³δδδ(k−k′)/k²), 𝒮̄_at = 2π(m_ek′/(2π)³)Σ_{occ}Σ_{l′m′}|⟨k′l′m′|e^{iq·x}|i⟩|², the occupied sum over spin-orbitals.
1509.01598 Eq. (51) [ABS + App. A.3 read], |f_ion|² = (2k′³/(2π)³)Σ_occΣ_{l′m′}|…|², then gives **𝒮̄_at = π|f_ion|²/(2E_R) iff "occupied states" counts
both spins** (WP7D-N5a). Consistency with their Eq. (52), dR/dlnE_R = (ρ_χ/m_χ)(σ̄_e/8μ²)∫q dq|F_DM|²|f_ion|²η, and WP0 (9.2) requires exactly this
(C10a), so the spin count is fixed. 2011.01940 Eq. (8) [FT] writes (4k′³/(2π)³)Σ_{l′L}(2l+1)(2l′+1)(2L+1)[3j]²|∫r²R_{k′l′}R_{nl}j_L|²; the Gaunt sum
Σ_{m,l′m′}|…|² equals the bracketed sum (WP7D-N5b), so its 4k′³ is 2 spins × 2k′³ and the two definitions agree, **provided R_{k′l′} carries the
Eq. (49) normalisation**, which 2011.01940 does not print (it cites "[3, 12]"; its Eq. (30) is mapped from 1509.01598, which supports the
same convention). Residual status of that last point: UNRESOLVED-minor.
With 𝔏 = |ℳ|²/(4m_e²), (F.3) gives dσv/dE_R = |ℳ|²q|f_ion|²/(64πm_χm_e²E_R) = **2011.01940 Eq. (7)** (equivalently its Eq. (30)) (C10b); the scalar
(F.5) gives **its Eq. (10)**, dσv_S/dE_R ≃ σ_eq²|f_ion|²/(4E_Rm_χ²), σ_e = m_χ²/(4πΛ⁴), identically (C10c), both modulo the convention above.
*Vector, their Eq. (9).* It multiplies |f_ion|² by the free-electron |ℳ|² at q = m_χ + E_B − E_R; (F.4) uses continuity. The ratio Eq. (9)/(F.4) is
1 + O(m_χ²/m_e²) at free kinematics (C10d, C11) and 1 − ω²/m_χ² + ω(m_χ−ω)(2m_χ−ω)/(m_χ²m_e) + O(m_e^{−2}) at bound kinematics (C10e).
**Sizes (exact coded ratio, WP7D-N6):** valence shells 1.007 (m_χ = 100 keV), 1.021 (200 keV), i.e. of the same O(m_χ²/m_e²) as the S_{J_TJ_T} term
the URF itself drops; **Xe K shell −11%** at m_χ = 100 keV, ω ≈ 43 keV, and **−34% to −41%** at the source's best fit m_χ = 56.5 keV
(ω = 34.6–37.5 keV). The O(1) piece −ω²/m_χ² is a real continuity defect of the free-vertex ansatz (at K-shell kinematics J_L = (ω/q)n ≈ 0.5n
versus (q/2m_e)n ≈ 0.05n). But the dropped J_T term is O(⟨p_e²⟩/m_e²) ≈ (Zα)² ≈ 0.16 for the Xe K shell, and Dirac corrections are of similar size, so
a quantitative comparison needs both. What the source says (corrected, A-C11): relativistic wavefunction corrections "increase the total
cross-section", by "a factor of a few to several orders of magnitude for q ∼ O(MeV)", and it draws m_χ ≳ 100 keV dashed. **Status of "Eq. (9) is
wrong": UNRESOLVED** (algebra CONFIRMED by both referees). Priority of the continuity remark: UNRESOLVED (2201.11905, a bound-electron and
nucleus treatment with a dark dipole, [ABS] only; later treatments not searched).
**(c) Scalar operator with a light mediator (2308.00309, read in full) [D].** 2308.00309 Eq. (1) is the scalar operator (χ̄P_{L,R}ν)(ēe)/Λ²;
Eq. (14) σ_e ≡ m_χ²/(4πΛ⁴); Eq. (15) σ_e = m_χ²Y_ee²Y_χν²/(4πm_φ⁴), "valid provided m_φ ≫ m_χ, with corrections of order (m_χ/m_φ)²"; its direct-detection
rates are those of 2011.01940 (it cites the erratum PRD 105, 119903). In URF the mediator is not contact: Λ_F^{−2} → Y_eeY_χν/(m_φ² − t) with the
four-momentum transfer at v = 0

  t = ω² − q² = 2m_χω − m_χ²  (q = m_χ − ω),     Γ^F_S(m_φ) = ∫d³q/(2π)³ (Y_ee²Y_χν²/4)(m_φ² − 2m_χω + m_χ²)^{−2} S_nn(q, m_χ−q),            (F.7)

so the rate factor is 1 − 2m_χ²/m_φ² + … (WP7D-N7a,b), the source's O((m_χ/m_φ)²), with an ω dependence that tilts the ionisation spectrum.
t is set by the relativistic ν̃ leg, not by −q², unlike WP0's F_DM (2.2).

### 2.5 What remains outside [exact gaps]
- **Charged current** (χ + n → p + e⁻, 1905.12635 Eqs. (6)–(13)): species-changing nuclear transition operator plus the Coulomb-distorted e⁻
  (Fermi function, their Eq. (12)); neither is in the 16-row basis with a free final lepton. Gap: nuclear transition row + distorted waves.
- **Massive ν̃ with m_ν̃ ≈ m_χ:** (F.1) reduces to WP0 (2.1) with Δ_χ = m_ν̃ − m_χ up to replacing q²/2m_χ by q²/2m_ν̃, a relative O(Δ_χ/m_χ)
  difference [D, sketch].

### 2.6 Computation specification (item 2)
- **Inputs.** Electrons: all-electron S_nn, S_{J_TJ_T} along ω = m_χ − q for m_χ ∈ [E_g, 1 MeV], **with the spin-orbital (both spins) convention of
  §2.4(b) fixed in the code and stated in the table header**; DHF orbitals for q ≳ m_e/3; crystals: high-q all-electron PAW (IF-D5). Light
  mediators: the (F.7) factor. Nuclei: S^{GS}_κκ at K = imp (WP2 L6), ⟨p²_κ⟩ from DFPT.
- **Grids.** 1D in q per m_χ (≈ 200 points); m_χ, 40 per decade. **Convergence.** width to 1% in ⟨p²_κ⟩; electron spectra 2% in PAW augmentation.
- **Cost.** Nuclei negligible; electrons 10⁴–10⁵ core-h per crystal. **Outputs.** dℛ/dω per operator (V, S, A), peaks, widths, τ string.

---
## 3. Two-insertion processes (A11, §11.9)

### 3.1 Classification [D for the list; D, sketch for the reductions]
T = H_int + H_intG₀(E_i + ω_in)H_int + …. Target objects: (a) one target operator times a DM-side operator quadratic in the DM fields (contact pair
absorption): two-point S; (b) two target operators joined by a target propagator, 𝒯^{(2)}_{ab}(k₁,k₂;ω₁) = Σ_mO_b(k₂)|m⟩⟨m|O_a(k₁)/(E_i + ω₁ − E_m
+ i0) + (1 ↔ 2): four-point S_{𝒯𝒯}; (c) interference of (a) and (b): three-point quadratic response R^{(2)}_{abc}; (d) a DM propagator between two
target insertions (double scattering): ⟨O†O†OO⟩. Reductions [D, sketch]: (b) → a two-point function of an effective seagull + polarisability operator by
closure when all intermediate states are far off shell; (d) → products S(q₁)S(q₂) for a Gaussian (RPA, Wick) target with uncorrelated momenta
(the kinetic limit of §4.1); (c) only through one-loop expressions of R^{(2)} (e.g. the Lindhard quadratic response).

### 3.2 Contact pair absorption [D]
2507.14287 Eq. (3) [FT]: ℋ_S = m_e(S†S)(ψ̄_e[G_{S,S} + iG_{S,P}γ⁵]ψ_e) + i(S†∂↔_μS)(ψ̄_eγ^μ[G_{S,V} + G_{S,A}γ⁵]ψ_e). The vector and axial electron currents
come with the **derivative DM current**, not with S†S (v1's (S†S)ψ̄γ^μγ₅ψ was not Lorentz invariant; withdrawn). Annihilating (p, p̄) gives the DM
factor 1 for S†S and (p − p̄)^μ for i(S†∂↔S) (WP7D-N8). Hence a pair tensor and the rate **per unit target volume**:

  Γ_pair/V = ∫d³p d³p̄/(2π)⁶ g_DM²f_DM(p)f_DM(p̄) tr[𝔇^{pairᵀ}(p,p̄)S(p + p̄, E_p + E_p̄)],   𝔇^{pair}_ab = 𝒢_a*𝒢_b/(4E_pE_p̄),                    (T.1)

  S, P: 𝒢 = m_eG_{S,S}, m_eG_{S,P} against n (P: O((p+p̄)·s/m_e)-suppressed);   V, A: 𝒢^μ = G_{S,V/A}(p − p̄)^μ against (n, j) or (2 tr J, 2s).   (T.2)

For V the time component E_p − E_p̄ = O(m_χv²) and the space part (p − p̄) = O(m_χv), so V and A are velocity-suppressed; the A rate ∝ |p − p̄|_⊥²
against the spin rows reproduces the 𝒫[(u − v)_⊥²] weighting printed after their Eq. (10). Only existing two-point S at (k ≈ 0, ω ≈ 2m_χ) enter:
pair absorption is single absorption at 2m_χ with the operator's row and a velocity-dependent DM tensor. *Literature limit.* 2507.14287 Eqs. (5)–(7)
[FT], dΓ_p = 2π|ℳ_fi|²δ(ΔE_fi − E − Ē)dρ_p, dρ_p = d³p d³p̄ g²_DMf f/(2π)⁶, is (T.1) for a discrete transition. Their Eq. (8) with ξ ≃ 44.8 gives each of S
and S† the density ρ_DM/(2m_DM) (escape cut at 2.5β_c; WP7D-C13; CONFIRMED by both referees). Their ρ_DM = 0.39 GeV/cm³ must be rescaled to 0.3.
*Corrections.* Quantum statistics (their S_Q), the Tremaine–Gunn cap (their Eq. (10)), the k = p + p̄ dependence of S in solids.

### 3.3 Pair absorption through two linear couplings [D, structure]
y_φφO at second order: amplitude ⟨f|𝒯^{(2)}(k₁,k₂;m_φ)|i⟩, rate ∝ y_φ⁴ **(n_φ²/2)** S_{𝒯𝒯}(k₁ + k₂, 2m_φ) for a real field (identical bosons: n_φ²/2
unordered pairs, WP7D-N13); four-point, reducing by closure to a two-point polarisability response when m_φ and 2m_φ are off-resonant; with a contact
term the interference needs R^{(2)}.

### 3.4 Dark Compton scattering (V + e → γ + e) [D for the Thomson limit]
The amplitude is O(e²κ_mix): one e from the photon vertex and one e κ_mix from the dark-photon vertex (v1's "first order in e" withdrawn). With
polarisation vectors e_λ (dark photon) and e′_λ′ (photon), q = k_V − k′, the transition operator is

  𝒯^C(q) = κ_mix(e²/m_e)(e_λ·e′*_λ′)n_e(q) + κ_mix e²Σ_m[(e′*·j)|m⟩⟨m|(e·j)/(E_i + m_V − E_m) + (e·j)|m⟩⟨m|(e′*·j)/(E_i − ω′ − E_m)],    (T.3)

Γ = ∫d³k′/((2π)³2ω′)(1/2m_V)Σ_pol S_{𝒯^C𝒯^C}(q, m_V − ω′). For a free electron at rest the resonant terms vanish (e·p_i = 0, e′·k′ = 0; checked by
hand by A), and with ⟨Σ|e·e′|²⟩ = 2/3 (C12a):

  Γ = 𝓃_eκ_mix²σ_Th·ω′/(m_V(1 + ω′/m_e)),   ω′ + ω′²/2m_e = m_V,   σ_Th = e⁴/(6πm_e²).                                                      (T.4)

*Literature limit.* 2109.08168 Eq. (2) [FT], R = (n_e/ρ_T)(ρ_DM/m_V)(e⁴ε²/24πm_e²)(m_V + 2m_e)(m_V² + 2m_em_V + 2m_e²)/(m_V + m_e)³: (T.4) equals it **through
O(x²)**, x = m_V/m_e (both 1 − 3x/2 + 5x²/2), and the first difference is at O(x³) (−35/8 vs −15/4) (WP7D-C12b, N12). Which physics fixes the x³ term
(spin, Klein–Nishina structure, relativistic recoil) is not computed: UNRESOLVED. URF content: (i) bound targets with m_V ≫ |E_B|: S_nn from the shell
Compton profiles J^{(sh)}(p_z) (WP6 tables); binding corrections are the resonant terms of (T.3); (ii) in-medium photon phase space n_r(ω′), → 1 at
ω′ ≫ ω_p (consistent with the source neglecting in-medium effects); (iii) the ALP case (their Eq. (3)) needs the spin row and the pseudoscalar-form
seagull (e g_aee/2m_e)aσ·A; not re-derived (IF-D12).

### 3.5 Scattering plus mediator absorption (§11.9; 2501.09642 [ABS + §3.4]) [D]
Two independent single-vertex processes (WP0 L0 with a light-mediator F_DM, and WP0 L9b for solar dark photons), different initial states, incoherent sum,
shared κ_mix. A combined amplitude would need the t-channel mediator on shell; for NR halo DM ω ≤ qv < q, so it is always spacelike. §11.9 is closed.

### 3.6 Second Born and the Barkas term [D, structure]
Re⟨T₁†T₂⟩, case (c): linear in R^{(2)}. This is WP0 §9.1 correction (β) and, for stopping, the Z³ Barkas term; for the electron gas R^{(2)} is the Lindhard
quadratic response.

### 3.7 Computation specification (item 3)
- **Inputs.** Pair absorption: S_OO(k ≈ 0, 2m_χ) from L9b tables (charge-like rows) or WP4 (spin rows), **with 𝔇^{pair} of (T.1)–(T.2) for V, A
  (velocity moments ⟨(p − p̄)_i(p − p̄)_j⟩ over f_DM⊗f_DM)**, ρ_χ = 0.3; dark Compton: J^{(sh)}(p_z) or high-q S_nn, n_r(ω′); Barkas: HEG R^{(2)} with an
  LDA map (new module). **Grids.** dark Compton ω′ ∈ m_V(1 ± 0.1), 100 points, 32 angles; pair: as L9b plus a 3D velocity quadrature (20³).
- **Cost.** Minutes; R^{(2)} 10² core-h. **Outputs.** rates, spectra, τ string.

---
## 4. Out of scope, with the interfaces

### 4.1 Damage tracks and paleo-detectors (D3, D4): the stopping-power interface
**Stopping as a limit of (3.3) [D].** Projectile of charge Z_κ, velocity v_N, no recoil (ω_q = q·v_N), coupled to total charge ((5.4)), weighted by ω:

  −dE/dx = v_N^{−1}∫d³k/(2π)³ ω|Z_κe²/k²|²S_zz(k, k·v_N) = (2Z_κ²α/πv_N²)∫(dk/k)∫₀^{kv_N}dω ω L(k,ω)   (T = 0),                             (S.1)

the Lindhard dielectric stopping (prefactor WP7D-C14a; = WP5-v3 §1.1(e)). **Bethe [D, sketch]:** for kv_N ≫ ω_max the inner integral saturates the f-sum
(9.5), (π/2)ω_p², between a lower cutoff k_min and the Bethe-ridge 2m_ev_N:

  −dE/dx = (4πZ_κ²α²𝓃_e/m_ev_N²) ln(2m_ev_N²/Ī),                                                                                          (S.2)

(WP7D-C14b). The prefactor is derived; the constant inside the log (k_min ≈ Ī/v_N, ln Ī = (2/πω_p²)∫ω L(0,ω)ln ω dω) is the standard heuristic, not derived
here, and its literature form is [UNVERIFIED]. **Why tracks are outside:** (i) Born parameter Z_κα/v_F ≈ 15 (Si), 35 (Ge) for keV recoils (WP5-v3
§1.1(e), §3.3); (ii) a track is 10²–10⁴ correlated collisions on a target damaged by earlier ones (case (d) of §3.1 at all orders) plus thermal-spike and
Coulomb-explosion dynamics; (iii) the readout is a defect configuration, not an excitation spectrum. **Hand-off:** per recoil seed, the prompt seed (7.3)
and the loss kernels dP/dω_e(k; v_N) from (S.1) at fixed k (Born, valid only where Z_κα/v_rel ≪ 1); WP5 transports (Markov ion transport truncation 0 /
MLIP-MD); CSDA length ∫dE/(S_n + S_e) and the damage map are WP5 outputs (IF-D6).

### 4.2 DM-side radiative de-excitation (I2) [D for the split; D, sketch for the medium factor]
2006.13918 Eq. (2) [FT], τ^{−1} ∼ πδ³/Λ_d², is the vacuum decay χ* → χγ through the σ^{μν}F_{μν} transition dipole of their Eq. (1), i.e. **magnetic dipole
(M1)** at NR. No target operator appears in the amplitude, so no S_ab enters. The medium enters only through 𝒟^γ of WP0 (3.6), via Γ_med = −2 Im Σ_χ*(δ):
- transverse on-shell part: in a transparent non-magnetic medium the photon density of states scales as n_r³ and the per-photon |B|² is independent of
  n_r, so **Γ_M1 ∝ n_r³(δ)** (an E1 decay would scale as n_r, its per-photon |E|² ∝ 1/n_r²) (WP7D-N9), local-field factors aside; numerically irrelevant at
  δ ≫ ω_p, where n_r → 1;
- absorptive part (ε₂(δ) > 0): non-radiative transfer χ* + target → χ + excitation through a virtual photon. This is inside URF: WP0 (3.3) with Δ_χ = −δ
  (exothermic, (2.1)) and the dipole vertex in 𝔇 (|μ_χ × q|²/q⁴ against S_{J_TJ_T}), i.e. the I1/I4 machinery.

---
## 5. Claims, tags and checks
| Claim | Tag | Check / source |
|---|---|---|
| (D.1) spectrum, weight at k = −m_φv; 1711.10489 Eq. (24) | D | C2a,b, N2 |
| (D.2) coherent amplitude = off-diagonal R; Kubo sign | D; finite body, orientation factors D, sketch | N1, N10 |
| (D.3) mean power = golden rule for t_int ≫ min(t_coh, 1/Γ_T), stationary coupling; windowed otherwise; bunching | D; bunching D, sketch | C1a,b, N1 |
| (D.4) Bloch limits, R_{I⁺I⁺} sign; 1306.6089 envelope (CONFIRMED by A, B), amplitude factor 2 UNRESOLVED; 2101.01241 Eq. (1); u | D; u D, sketch | C5a–d, N3 |
| (D.5)–(D.6) SNR scalings; crossover O(1)·t_coh; random-amplitude penalty inside (D.6); spin temperature | D | C3, C4a–c, N4 |
| (D.7) BAR, Q_DM^eff ≤ 1.3×10⁶ (SHM); prefactor 32 open | D | C6a–c |
| (D.8) H_C scaling h_mod; drive ∝ ω²; relativistic 2δ_rel^a | D; drive D, sketch; size E | C15 |
| (D.9) multiferroic cross-response; LSWT only T ≪ T_CM; near-T_CM gap | D, sketch | — |
| (F.1)–(F.5) class, master formula, contractions | D | C8a–d, C11 |
| (F.6) 1905.12635 Eq. (4), −m_χ/M, width | D; width E | C9 |
| §2.4(b) spin convention; Eqs. (7), (10) identities; Eq. (9) ratio and sizes; paper-error status UNRESOLVED | D; sizes D (exact ratio) | C10a–e, N5a,b, N6 |
| (F.7) light scalar mediator (2308.00309) | D | N7a,b |
| (T.1)–(T.2) pair absorption with 𝔇^{pair}; ξ = 44.8 ↔ ρ/2m per species | D | C13, N8 |
| §3.3 identical-boson ½ | D | N13 |
| (T.3)–(T.4) dark Compton = Eq. (2) through O(x²) | D; x³ attribution UNRESOLVED | C12a–c, N12 |
| §3.5 §11.9 closed | D | — |
| §3.1 reductions | D, sketch | — |
| (S.1) Lindhard; (S.2) Bethe prefactor | D; log constant D, sketch / UNVERIFIED | C14a,b |
| §4.2 I2: M1 ∝ n_r³; non-radiative part in (3.3) | D, sketch | N9 |

---
## 6. Symbols introduced/used (against NOTATION v4 + R9 rows)
**Used as defined:** q, ω, ω_q, Δ_χ, v, v₀, v_E, v_max, f_χ, η, ρ_χ, ρ_T, m_χ, j_χ, 𝐒_χ, 𝔇_ab, 𝒱_a, S_ab, S̄, R_ab, R̃, ε (total dielectric only), ε₀, L,
v_C, 𝒟^γ_{μν}, y_φ, φ, k_φ, Γ_abs, Γ_net, Γ_χ, ℛ, κ_mix, g_aee, g_aγγ, B₀, O_a, n_e, s_e, j_e, J_e, 𝒯_e, T_e, I_κ^β, F^M_κ, A_κ, Z_κ, M_κ, 𝓃_e, 𝓃_κ, ω_p,
K (= imp), τ, 𝒳, n_T, GS, X, X0, X+ (sectors only), κ_BO, J^{(sh)}(p_z), n_r, σ₁, E_R, E_B (quoted), m_e, μ_χe, σ̄_e, F_DM, T, β, V.
**Introduced (proposed NOTATION rows; collisions re-checked after B-A10):**
| Symbol | Meaning | Where |
|---|---|---|
| t_coh, ℓ_coh, t_int, N_dB, 𝒩_c, Γ_T | coherence time/length (not τ_c: τ is the truncation index); integration time; occupation per de Broglie volume; coherence cells; target width | §1.0, §1.4 |
| 𝒮_φ(k,ω), F_φ(ω), f_sp(v) | field spectral density; normalised line; speed distribution | (D.1) |
| O_rd, **X_rd** | readout operator; its sample total (v1 "X" collided with the sector X) | (D.2), (D.5) |
| 𝒮^{sig}, 𝒮^{int}, 𝒮^{det}, 𝒮_n, TS_A | PSDs and Asimov statistic | (D.5)–(D.6) |
| β_s | spin temperature, tanh(β_sω_L/2) = p | §1.5, (D.5) |
| ω_L, δω_L, T₂, T₁, M₀, Ω_a, p | Larmor frequency, detuning, spin times, magnetisation, rotating-frame Rabi frequency, polarisation | (D.4) |
| d_EDM, E*_I | nucleon EDM; effective field at site I | §1.2 |
| γ_n, Q_mode, Q_DM^eff | mode width, mode quality factor, effective DM quality factor | (D.7) |
| 𝔘_C(k) | Coulomb-energy density row (∂H/∂ln α) | (D.8) |
| h_mod, d_{m_e}, d_α, δ_rel^a | modulus strain; modulus couplings (source "d_e" renamed); fractional relativistic lattice shift | (D.8) |
| geom ∈ {bulk, body} | τ metadata | §1.2 |
| ν̃, m_ν̃, E_ν̃, 𝐤_ν̃, Λ_F, 𝔏, 𝔇^F, ω^F_q, σ_NC | fermionic absorption objects (ν is the phonon branch) | (F.1)–(F.6) |
| Y_ee, Y_χν, m_φ (mediator), t | 2308.00309 couplings (quoted); mediator mass; four-momentum transfer squared | (F.7) |
| 𝒮̄_at, f_ion | per-atom S̄; sources' ionisation form factor (quoted) | §2.4(b) |
| G_{S,i}, 𝒢_a, 𝔇^{pair}, f_DM, g_DM, ξ | pair couplings (quoted), DM-side pair vertex, pair tensor, occupation, dof, normalisation | (T.1)–(T.2) |
| 𝒯^{(2)}, 𝒯^C, R^{(2)}_{abc} | second-order and Compton operators; three-point response (not χ^{(2)}) | §3.1, (T.3) |
| **e_λ, e′_λ′** | dark-boson and photon polarisation vectors (v1 "ε" collided with the dielectric ε) | (T.3) |
| ω′, σ_Th | emitted photon energy; Thomson cross-section (σ_T is WP6's) | (T.4) |
| Ī, Γ_med, Σ_χ* | Bethe mean excitation energy; in-medium width; DM self-energy | (S.2), §4.2 |

---
## 7. Interface flags
| # | Owner | Quantity | This return |
|---|---|---|---|
| IF-D1 | NOTATION | new symbols | rows of §6 |
| IF-D2 | WP0 §2, CONVENTIONS §7 | basis | add row 𝔘_C; DM-side class 𝔇^F with relativistic ω^F_q; pair tensor 𝔇^{pair} for derivative DM currents |
| IF-D3 | CONVENTIONS §11 | metadata | geom ∈ {bulk, body} |
| IF-D4 | WP2 (L6) | NC line shape | S^{GS}_κκ at q = m_χ, true ⟨p²_κ⟩ |
| IF-D5 | WP1 | high-q all-electron S_nn, S_{J_TJ_T} | q ∼ 10 keV–1 MeV; spin-orbital convention; Dirac bilinears for cores |
| IF-D6 | WP5 | stopping kernels | (S.1) hand-off; Barkas = R^{(2)} |
| IF-D7 | WP6 | likelihood | exponential bins (D.6); bunching; fixed-amplitude analyses overestimate by 3–10 (1905.13650 [ABS]); no double counting |
| IF-D8 | WP4 ([3.3], L19) | chiral targets | P-odd S^A_{J_TJ_T} in (F.4) |
| IF-D9 | LIMITS L9b, WP3 §4 | finite bodies | orientation factor relative to bulk 1/ε₀: 1, 3ε₀/(ε₀+2), ε₀ (up to ε₀² in power); BAR Q_DM^eff |
| IF-D10 | LIMITS (L-D8) | 2011.01940 Eq. (9) | O(1) −ω²/m_χ² continuity defect of the free-vertex ansatz; quantitative comparison needs J_T and Dirac terms; paper-error status UNRESOLVED |
| IF-D11 | LIMITS (L-D1) | 1306.6089 Eq. (1) | envelope width CONFIRMED (factor 2); amplitude factor 2 UNRESOLVED (splitting vs half-splitting) |
| IF-D12 | open | 2501.05504 prefactor 32 and M_n; 2109.08168 Eq. (3) (ALP seagull); dark-Compton x³ attribution | not derived |
| IF-D13 | WP4 / new | multiferroic near T_CM | exact remaining gap: finite-T spin dynamics with tr J_e vertex |
| IF-D14 | LIMITS (all new rows) | source halo | rescale ρ = 0.39/0.4 → 0.3 GeV/cm³ (CONVENTIONS §8) |

---
## 8. Proposed LIMITS rows (provisional labels; numbers assigned by the coordinator)
| # | τ / chain (URF) | Source formula | Status |
|---|---|---|---|
| L-D1 | (D.2) k → 0, spin row with B₀, R_{I⁺I⁺}, rotating wave; transient/steady (D.4); spin-temperature noise | 1306.6089 Eq. (1); 2101.01241 Eq. (1) | D; ✎ envelope (CONFIRMED), amplitude factor 2 UNRESOLVED (IF-D11) |
| L-D2 | (D.1) Gaussian field, k = −m_φv weight; signal PSD (D.5) | 1711.10489 Eqs. (8), (10), (24) | D |
| L-D3 | (D.6) exponential-bin likelihood; scalings t^{−1/2}, (t t_coh)^{−1/4}; crossover O(1)·t_coh (no constant); random amplitude included, fixed-amplitude penalty 3–10 (1905.13650 [ABS]) | 1306.6089 Eqs. (8)–(9) HTML = (A7)–(A8) PDF; 1711.10489 Eqs. (54), (63), (69) | D ✎ |
| L-D4 | (D.7) P_abs/V, GS finite-body mode, piezo vertex; monochromatic limit; Q_p ≫ Q_DM gives Q_DM^eff(ω_n, t); orientation factor (IF-D9) | 2501.05504 Eqs. (5), (7), (8) | D (structure; prefactor open) ✎ |
| L-D5 | (D.8) H_C scaling, k → 0, drive ∝ ω² (sketch); correction 2δ_rel^a [E] | 1508.01798 Eq. (7) and following text (h), Eq. (8) | D ✎ |
| L-D6 | (D.9) R_{s^z,trJ_e}, P,T-broken reference; T ≪ T_CM by LSWT; near-T_CM gap | 2102.10171 Eqs. (5), (10) | D, sketch; gap IF-D13 |
| L-D7 | (F.2)/(F.4) vector NC, nuclear density row + continuity, M_κ → ∞; K = imp line shape; ρ → 0.3 | 1905.12635 Eqs. (1), (3), (4) | D |
| L-D8 | (F.3)–(F.5), (F.7): electron density row; 𝒮̄_at = π\|f_ion\|²/2E_R with spin-orbital convention (N5); light scalar mediator; ρ → 0.3 | 2011.01940 Eqs. (7), (8), (9), (10), (30); 1509.01598 Eqs. (49), (51), (52); 2308.00309 Eqs. (1), (14), (15) | D ((7), (10) identities, modulo R_{k′l′} normalisation); (9) ✎ ratio at bound kinematics, paper-error UNRESOLVED (IF-D10) |
| L-D9 | (T.1)–(T.2) pair absorption: S, P with \|𝒢\|²; V, A with velocity-dependent 𝔇^{pair}; per unit volume; ρ → 0.3 (from 0.39) | 2507.14287 Eqs. (3), (5)–(8) | D ✎ |
| L-D10 | (T.3)–(T.4) seagull, free S_nn, NR kinematics: equal through O(x²) | 2109.08168 Eq. (2) (Eq. (3) open) | D |
| L-D11 | (S.1) Lindhard (Born); (S.2) Bethe | WP5-v3 §1.1(e) (owner WP5); Bethe [UNVERIFIED] | D (Lindhard), D, sketch (Bethe log) |
| L-D12 | interface: I2 M1 decay, in-medium Γ ∝ n_r³; non-radiative part = (3.3) with Δ_χ = −δ | 2006.13918 Eqs. (1), (2) | D, sketch (out of scope) ✎ |

**Ratings of claims about published papers (after R11).**
| Paper / item | v2 rating |
|---|---|
| 1306.6089 Eq. (1) envelope half as wide | CONFIRMED (A, B) |
| 1306.6089 Eq. (1) resonant amplitude | UNRESOLVED (factor 2, convention of d_nε_SE*) |
| 2011.01940 Eq. (9) not current-conserving at bound kinematics | algebra CONFIRMED; "paper wrong" UNRESOLVED |
| 2507.14287 Eq. (8), ξ = 44.8 ↔ ρ/2m per species | CONFIRMED (A, B) |
| 2501.05504 Q_s → Q_DM^eff for Q_p ≫ Q_DM | CONFIRMED as a reinterpretation (not an error) |
| 2501.05504 "1/ε₀ is the slab case" (v1) | REFUTED (B); withdrawn |
| 2109.08168 Eq. (2) agreement | CONFIRMED through O(x²); x³ attribution UNRESOLVED |

---
## 9. Closing table (one row per referee item; status: applied / rebutted / dropped / no change)
| Item | Verdict | Status | Where |
|---|---|---|---|
| A-1, A-2, A-4, A-5, A-9, A-10, A-11, A-14, A-15, A-16, A-18 | STANDS | no change (A-18: C3 made a plain integrand identity, N1 added as independent Kubo test) | §1, §2, §3, §4; checks |
| A-3 / A-C1 golden-rule mean for short records | SWC | applied: t_int ≫ min(t_coh, 1/Γ_T), windowed otherwise, counterexample | §1.4(i), §1.10 |
| A-6 / A-C2 crossover 3/2 | SWC | applied: O(1)·t_coh; dropped from LIMITS | §1.6, L-D3; N4 |
| A-C3 Rayleigh penalty | — | applied: 3–10 from 1905.13650 [ABS]; built into (D.6) | §1.6, IF-D7 |
| A-C4 spin temperature | — | applied | §1.5(c), (D.5), §1.10 |
| A-7 / A-C5 (D.7) per volume | SWC | applied: P_abs/V | (D.7) |
| A-C6 Q_DM^eff dependences | — | applied | §1.7 |
| A-C7 slab wording | — | applied: orientation factors relative to bulk | §1.3, IF-D9; N10 |
| A-8 / A-C8 citation, (Zα)² size | SWC | applied: "Eq. (7) and text"; 2δ_rel^a, 0.045 upper bound | (D.8), L-D5 |
| A-C9 J_L wording | — | applied | §2.4(a) |
| A-12a / A-C10 spin convention | SWC | applied: derived from (3.1) with explicit spin; Gaunt identity; residual R_{k′l′} normalisation UNRESOLVED-minor | §2.4(b); N5a,b |
| A-12b / A-C11 what the source flags; paper-error status | SWC | applied: source quote corrected; UNRESOLVED | §2.4(b), IF-D10 |
| A-13 / A-C12 pair operators, per volume, ρ, identical bosons | SWC | applied: (T.1)–(T.2), ½ in §3.3, ρ rescaling | §3.2, §3.3, IF-D14; N8, N13 |
| A-17 / A-C13 n_r³ | SWC | applied | §4.2, L-D12; N9 |
| A-C14 tags | — | applied: 2501.09642 and 1509.01598 now [ABS + named section] | §2.4(b), §3.5 |
| A-C15 checks | — | applied: N1 (quantum Kubo), N2 (k sign), N3 (R sign) are independent tests | checks |
| A-(f) read 2308.00309 before L-D8 | — | applied: read in full, (F.7) | §2.4(c), L-D8; N7 |
| A-(f) Q_DM^eff not new | — | applied | §1.7 |
| B-V1 / B-A1 k sign | SWC | applied | (D.1), (D.3); N2 |
| B-V2, B-V9, B-V10, B-V15 | STANDS | no change | — |
| B-V3 stationary coupling | STANDS | applied (stated) | §1.4 |
| B-V4 / B-A2 R label and sign; amplitude; u tag | SWC | applied: R_{I⁺I⁺}, ⟨I^z⟩ < 0; amplitude UNRESOLVED; u [D, sketch] | §1.5, IF-D11; N3 |
| B-V5 / B-A3 crossover artefact; double counting | SWC | applied | §1.6; N4 |
| B-V6 / B-A4 slab REFUTED; grid | SWC | applied: claim withdrawn; grid [m, (1+3.6×10⁻⁶)m] | §1.3, §1.7, §1.10; N10, N11 |
| B-V7 / B-A5 missing (D.8); Cu number; tag alignment | SWC | applied: (D.8) displayed; 2δ_rel^a; drive [D, sketch] in text and table | §1.8, §5 |
| B-V8 / B-A6 multiferroic near T_CM | SWC | applied: exact remaining gap | §1.9, §1.10, IF-D13 |
| B-V11 / B-A7 sizes | SWC | applied: valence 1.007/1.021, Xe K −11% and −34% to −41%; J_T and Dirac needed | §2.4(b); N6 |
| B-V12 / B-A8 pair operators, per volume | SWC | applied | §3.2 |
| B-V13 O(e²) amplitude; "relativistic" O(x²) | SWC | applied: O(e²κ); agreement through O(x²), x³ attribution UNRESOLVED | §3.4; N12 |
| B-V14 reductions are sketches | SWC | applied: [D, sketch] | §3.1 |
| B-V16 Bethe log constant | SWC | applied: [D, sketch]/UNVERIFIED; L-D11 tag | §4.1 |
| B-V17 / B-A9 n_r³ | SWC | applied | §4.2 |
| B-V18 / B-A10 undefined labels; X, ε collisions; "first order in e"; unused symbols | SWC | applied: only (D.1)–(D.9), (F.1)–(F.7), (T.1)–(T.4), (S.1)–(S.2) exist and are displayed; X_rd, e_λ; h_mod, d_α now used in (D.8) | throughout, §6 |
| B-(a) massive-ν̃ reduction | — | applied: O(Δ_χ/m_χ) difference stated, [D, sketch] | §2.5 |
| B-(b) PDF numbering of 1306.6089; L-D8 equivalence; L-D11 tag | — | applied | §1.5, §1.6, L-D3, L-D8, L-D11 |
| B-(f) priority of the continuity remark | — | applied: UNRESOLVED; 2201.11905 [ABS] | §2.4(b) |
| Coordinator: "2501.05504 slab claim REFUTED" | — | applied (withdrawn) | §1.3, ratings table |

**Count.** Referee A: 18 claims (10 STANDS, 8 SWC) and 15 corrections, all applied; no rebuttals; one claim withdrawn (none of A's). Referee B: 18 verdicts
(4 STANDS, 14 SWC) and 10 corrections, all applied; one claim dropped (the exclusive slab attribution, B-A4/V6). Checks 49/49 PASS (v1's 34 + 15 new).
**Literature:** read in full (R10 or R12): 1306.6089, 1711.10489, 2101.01241, 2501.05504, 1508.01798, 2102.10171 (PDF), 1905.12635, 2011.01940, 2507.14287,
2109.08168, 2006.13918, 2308.00309 (R12). [ABS + named section]: 1509.01598 (App. A.3), 2501.09642 (§3.4). [ABS]: 1306.6088, 1905.13650, 2201.11905, 2609.07908,
2410.17308, 2405.05728, 1405.2925. All IDs verified against the arXiv API.
