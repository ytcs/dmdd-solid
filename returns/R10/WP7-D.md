# R10 / WP7-D: extensions beyond single-vertex golden-rule rates (coherent fields, fermionic absorption, two insertions, and the out-of-scope interfaces)

Theory agent, brief briefs/R10/WP7-D.md. Architecture: returns/R8/WP0-v3.md, cited "WP0 (n)" (read through state/CORRECTIONS.md; WP0-v3 has
no open owed corrections that touch the equations used here). Conventions: CONVENTIONS.md (HL units e² = 4πα, campaign signs of q and ω,
tr[𝔇ᵀS] contraction); symbols: NOTATION v4 + R9 rows; new symbols in §6. Checks: `code/WP7-D/checks.py`, sympy (+ mpmath for three numbers),
**34/34 PASS, ≈ 5 s**, cited WP7D-Cn. Tags: [D] derived (hypotheses stated), [D, sketch], [E] estimated, [C] conjectured; literature [FT] read
in full text in this return (arXiv HTML/PDF fetched with lit.py into literature/papers-WP7-D/, PDFs deleted at the end), [ABS], [UNVERIFIED].
Every arXiv ID below was verified against the arXiv API (export.arxiv.org, id_list query) on 2026-11-01. Status of all new content: CLAIMED.
Equations are numbered (D.n) coherent regime, (F.n) fermionic absorption, (T.n) two insertions, (S.n) stopping / out of scope.

---
## 0. Summary

| Item | Catalog rows | What URF needs | Truncation chain (WP0) | Status |
|---|---|---|---|---|
| Coherent classical field | S4, S9, A9, §10(ii) | nothing new for the physics: the same retarded R of (3.2), driven by a stochastic field; new: field statistics, finite-body geometry metadata, one operator row 𝔘_C (Coulomb-energy density) | (3.3)/(3.5) single vertex, first order in y_φ, linear response; GS (phonons/BAR/strain), spin rows with B₀ (NMR), tr J_e in a P,T-broken reference (multiferroic); 𝒳 per platform; metadata geom | [D] (D.1)–(D.9); limits 6 papers [FT] |
| Fermionic absorption | A10 | one new **DM-side** class: fermion-number-changing bilinear ν̃̄Γχ, relativistic final-state kinematics ω^F_q, tensor 𝔇^F; target side unchanged (rows n, j, s, J, 𝒯) | (3.3) with 𝔇 → 𝔇^F, ω_q → ω^F_q; nuclei: S^{GS}_κκ at K = imp; electrons: X sector, all-electron, Dirac bilinears for q ≳ m_e | [D] (F.1)–(F.7); 1905.12635, 2011.01940 recovered |
| Two insertions | A11, §11.9 | classification by correlator order; pair absorption (contact) and Thomson-limit dark Compton reduce to two-point S; second-order (resonant) parts need four-point functions, interference needs three-point R^{(2)} | (3.3) at second order in H_int (O(y²) amplitude) | [D] (T.1)–(T.6); 2507.14287, 2109.08168 recovered; §11.9 trivial |
| Out of scope | D3, D4, I2 | stopping power as the m_χ → ∞, first-ω-moment limit of (3.3) and its hand-off to transport; I2 has no target vertex | (3.3), K = imp, Born; WP5 truncation 0 | [D] for the interfaces (S.1)–(S.4); exact reasons |

---
## 1. The coherent classical-field regime (S4, S9, A9, §10(ii))

### 1.0 Regime and scales [D for the definitions, E for the numbers]
A bosonic DM field φ of mass m_φ is a classical field when the occupation per de Broglie volume is large,
N_dB ≡ (ρ_χ/m_φ)(2π/(m_φv₀))³ ≫ 1: N_dB(1 eV) = 1.1×10⁶, N_dB = 1 at **m_φ ≈ 33 eV** (WP7D-C7; ρ_χ = 0.3 GeV/cm³, v₀ = 238 km/s, CONVENTIONS §8).
Coherence time and length (reference scalars; the exact objects are the autocorrelation (D.1)): **t_coh ≡ 2π/(m_φv₀²)** ≈ 1.6×10⁶·(2π/m_φ)
(6.6 ms at 1 μeV) and **ℓ_coh ≡ 2π/(m_φv₀)** (1.6 km at 1 μeV). Four time scales decide which formula applies: the DM period 1/m_φ, t_coh,
the target response time 1/Γ_T (T₂ for spins, Q_mode/ω_n for a resonator), and the integration time t_int. Two length scales: ℓ_coh and the
sample size L_s. For L_s ≪ ℓ_coh (every laboratory sample below ~meV) the field is uniform over the sample and the bulk momentum
**k_φ = m_φv must be replaced by the body's own mode structure** (§1.3).

### 1.1 Field model [D, hypotheses: Gaussian stationary field, non-relativistic halo, no self-interaction]
With the halo velocity distribution f_χ (CONVENTIONS §8), the field is a Gaussian random process with
⟨φ(x,t)φ(x′,t′)⟩ = (ρ_χ/m_φ²)∫d³v f_χ(v) cos[ω_v(t−t′) − m_φv·(x−x′)], ω_v = m_φ(1 + v²/2). Its spectral density, defined by
⟨φφ⟩ = ∫d³k/(2π)³∫(dω/2π)𝒮_φ(k,ω)e^{−ik·(x−x′)−iω(t−t′)}, is

  𝒮_φ(k,ω) = (ρ_χ/2m_φ²)(2π)⁴∫d³v f_χ(v)[δ³(k − m_φv)δ(ω − ω_v) + δ³(k + m_φv)δ(ω + ω_v)],   ∫(dω/2π)𝒮_φ(ω) = ρ_χ/m_φ²,          (D.1)

with k-integrated line 𝒮_φ(ω>0) = (πρ_χ/m_φ²)F_φ(ω), **F_φ(ω) ≡ f_sp(v)/(m_φv)|_{v=√(2(ω−m_φ)/m_φ)}**, f_sp the speed distribution, ∫F_φdω = 1
(WP7D-C2a). *Literature limit.* 1711.10489 Eq. (10) [FT] builds the same field as a sum of Rayleigh-amplitude, random-phase components;
its Eq. (24), ⟨S_ΦΦ(ω)⟩ = Aπf(v)/(m_av), with exponentially distributed periodogram bins, is (D.1) pushed through the ABRACADABRA flux map
(their Eqs. (12)–(15)) (WP7D-C2b). The sign of k under the campaign Fourier convention (O(q) = ∫e^{+iq·r}) matters only for P,T-broken
targets (WP0 (4.3), L19).

### 1.2 Couplings and operator rows (truncation chain) [D]
H_int(t) = y_φ∫d³x φ(x,t)O(x) (WP0 (3.3)), with O per coupling:
- **dark photon:** κ_mixeJ^μ_em with the in-medium mixing of WP0 (3.6) (photon-reducible part); **g_aγγ in B₀:** WP0 (2.9);
- **ALP–electron (S9, magnon absorption):** NLO 2 tr J_e(k) (WP0 §2; 2106.12586 Eq. (18)); LO s_e(k) is O(k)-suppressed;
- **ALP–nucleon gradient (CASPEr-gradient/wind):** the nuclear-spin row I_κ^β(k_φ) with vertex ∝ g_aNN k_φ^β; **nucleon EDM (CASPEr-electric):**
  Σ_I d_EDM E*_I·𝐈_I, a spin row with a site-resolved vertex E*_I (Schiff-screened effective field; a material constant from DFT);
- **scalar moduli (§10(ii), 1508.01798 Eq. (1)):** δm_e/m_e couples to ∂H/∂ln m_e = −T_e (the kinetic-energy density row 𝒯_e of WP0 §2 at k → 0,
  exact for H_C: T_e ∝ 1/m_e), and δα/α to ∂H/∂ln α = the Coulomb potential energy. The latter is **not in the 16-row basis**: new row
  a = (C, 𝔘), 𝔘_C(k) ≡ Fourier density of the Coulomb energy (Interface flag IF-D2). Nuclear masses fixed: corrections O(κ_BO⁴) (§1.8).
Chain: WP0 (3.3)/(3.5) single vertex, first order in y_φ, linear response, any sector (GS for phonons, BAR modes, strain; the electronic X
sector for dark-photon absorption; spin rows need the (1.2) Zeeman/hyperfine options with B₀ ≠ 0); kernel rung per platform;
n_T enters only through detailed balance and the noise (D.6). **No new τ slot.** New metadata: geom ∈ {bulk, body} (finite-body response, §1.3).

### 1.3 Coherent signal amplitude [D, Kubo; hypotheses: linear response, target in a stationary state before the drive, (3.2) index order]
For φ = Re[φ_c e^{i(k·x−ωt)}] and any readout operator O_rd (an extensive observable: transverse magnetisation, displacement, polarisation),
first-order time-dependent perturbation theory with WP0 (3.2) gives

  δ⟨O_rd(k)†⟩(t)/V = y_φ∫_{t₀}^{t}dt′ R_{rd,O}(k; t−t′)φ_k(t′),   R_{ab}(k;t) ≡ −(i/V)θ(t)⟨[O_a(k,t)†, O_b(k,0)]⟩,                       (D.2)

and in steady state (t − t₀ ≫ 1/Γ_T) δ⟨O_rd†⟩/V = (y_φ/2)φ_c e^{−iωt}R_{rd,O}(k,ω): **the coherent signal is the off-diagonal retarded response
R_{rd,O} at (k, ω) ≈ (m_φv, m_φ)**, an element of the same R matrix whose diagonal gives the rates. Two refinements:
- *Finite body (L_s ≪ ℓ_coh):* k → 0 and R is the response of the finite sample, R_{rd,O}(ω) = Σ_n ⟨0|O_rd†|n⟩⟨n|O|0⟩/(V(ω − ω_n + iΓ_n/2)) − (n ↔ −ω)*,
  summed over the body's normal modes n (mode functions with free/clamped boundary conditions), not the bulk R(q,ω) at q = m_φv.
- *Photon-mediated couplings:* the photon-reducible part of WP0 (3.6) must be evaluated with the sample's electrostatic boundary conditions
  (depolarisation tensor) when L_s ≪ 2π/m_φ; the bulk 𝒟^γ is the L_s ≫ 2π/m_φ limit [D, sketch]. The 1/ε₀ in 2501.05504 Eq. (5) is the
  slab case (field normal to the plates, D continuous).

### 1.4 Absorbed power, and the golden rule as the incoherent limit [D]
Time-averaging ⟨φ ∂_tH_int⟩ with (D.2) and (D.1):

  P_abs/V = −2y_φ²∫d³k/(2π)³∫₀^∞(dω/2π) ω 𝒮_φ(k,ω) Im R_OO(k,ω) = −y_φ²ρ_χ∫d³v f_χ(v)(ω_v/m_φ²) Im R_OO(m_φv, ω_v).               (D.3)

For a monochromatic field (D.3) is −(y_φ²ωφ_c²/2)Im R, and this equals ω·n_φ·Γ_net with n_φ = ρ_χ/ω and Γ_net of WP0 (3.5) (WP7D-C1a; sign
checked on a damped mode, −Im R = Im χ_mode > 0, WP7D-C1b). Hence:
- **(i) The mean absorbed power and the mean number of absorption events, P_abs t_int/ω, are given exactly by the golden-rule rate (3.5)
  averaged over f_χ, for any t_int and any t_coh.** Coherence never changes a mean that is linear in the field two-point function. If the target
  response is narrower than the DM line (Γ_T ≪ 2π/t_coh), (3.5) at a single ω is replaced by the line average ∫dω F_φ(ω)Im R(ω), i.e. (D.3).
- **(ii) Coherence changes the statistics.** Absorption events from a classical Gaussian field are Bose-bunched: for N̄ expected events
  collected over 𝒩_c independent coherence cells (≈ t_int/t_coh × (L_s/ℓ_coh)³, at least 1), Var N = N̄ + N̄²/𝒩_c [D, sketch: Gaussian field
  moments ⟨I²⟩ = 2⟨I⟩² per cell]. The Poisson golden-rule likelihood is the **incoherent limit 𝒩_c ≫ N̄**. For meV–eV absorbers counting
  quanta (WP0 L9b) 𝒩_c ≫ N̄ always; for resonant single-mode readouts (qubits, BAR phonon counting) at t_int ≲ t_coh it fails (Interface flag IF-D7).
- **(iii) Coherent amplitude vs power.** A readout that measures ⟨O_rd⟩ (a mean field, (D.2)) gains coherently, ∝ y_φ; a calorimetric or
  counting readout measures (D.3), ∝ y_φ². They are different observables of the same R: Im R_OO (power) versus |R_{rd,O}| (amplitude).

### 1.5 Spin precession (S4: CASPEr-electric, -gradient) [D]
For nuclear spins of a species κ in B₀ ∥ z (Larmor ω_L, transverse relaxation T₂), the spin row gives, after the rotating-wave step,
R_{I⁺I⁻}(0,ω) ≃ −(2⟨I^z⟩/V)/(ω − ω_L + i/T₂). With the rotating-frame Rabi frequency Ω_a ≡ (vertex × field amplitude)/2 and detuning
δω_L ≡ ω_L − m_φ, (D.2) is the linearised Bloch equation, solved by m(t) = iΩ_aM₀(1 − e^{−(iδω_L+1/T₂)t})/(iδω_L + 1/T₂) (WP7D-C5a), so

  |M_⊥(t)| = M₀Ω_a·2|sin(δω_Lt/2)|/|δω_L|  (t ≪ T₂),     |M_⊥| = M₀Ω_aT₂/√(1 + δω_L²T₂²)  (t ≫ T₂).                                 (D.4)

*Literature limits.* 1306.6089 Eq. (1) [FT]: M(t) ≈ npμE*ε_Sd_n sin[(2μB_ext − m_a)t]/(2μB_ext − m_a)·sin(2μB_ext t) is the first form at
δω_L → 0 (resonant growth M₀Ω_at, WP7D-C5d) with M₀ = npμ, Ω_a = E*ε_Sd_n. Off resonance the exact envelope is sin(δω_Lt/2)/(δω_L/2)
(WP7D-C5b), whereas the source prints sin(δω_Lt)/δω_L ("≈"): the resonance as printed is half as wide (Interface flag IF-D11).
2101.01241 Eq. (1) [FT], M_a = uM₀Ω_aT₂cos(ω_at), is the second form at δω_L = 0 (WP7D-C5c), with their spectral factor u = the overlap of the
inhomogeneous spin line and the DM line, i.e. u = ∫dω F_φ(ω)𝔤_inh(ω)·(Lorentzian of (D.4)) normalised to its δω_L = 0, T₂ value [D].
*Leading corrections.* (a) t_coh vs T₂: when T₂ > t_coh the drive is not monochromatic; the response is |R|²𝒮_φ in (D.6) (CASPEr's
T_b = min(t_coh, T₂), 1306.6089 Eq. (3)). (b) Inhomogeneous broadening (chemical shift, quadrupole splitting) enters as the sum over sites in
R_{I⁺I⁻}; it is computable (GIPAW EFG/shielding) rather than fitted. (c) Spin noise: by FDT (D.6), −coth(βω/2)Im R_{I⁺I⁻}, the Lorentzian of
1306.6089 Eq. (2) ("consistent with the fluctuation-dissipation theorem", their §A.3).

### 1.6 Signal-to-noise ratio versus t_int/t_coh [D, hypotheses: Gaussian signal and noise, weak signal, periodogram/likelihood analysis]
Readout X ≡ O_rd(k→0) of the whole sample. Signal PSD and intrinsic noise PSD (two-sided, ∫(dω/2π)):

  𝒮_X^{sig}(ω) = y_φ²V²|R_{rd,O}(0,ω)|²𝒮_φ(ω),     𝒮_X^{int}(ω) = −V coth(βω/2) Im R_{rd,rd}(0,ω)   (FDT, WP0 (4.1)),                       (D.5)

both from one response matrix; detector noise 𝒮^{det} is added. The Asimov test statistic of the exponential-bin likelihood is

  TS_A = t_int∫₀^∞(dω/2π)[𝒮̃^{sig}_{t_int}(ω)/𝒮_n(ω)]²,   𝒮_n = 𝒮^{int} + 𝒮^{det},   𝒮̃^{sig}_{t} = 𝒮^{sig} ∗ (t/2π)sinc²(ωt/2),                 (D.6)

the convolution being the finite-record (Fejér) window. Limits [D]:
- **t_int ≫ t_coh, 1/Γ_T** (window negligible): TS_A = t_int∫(dω/2π)(𝒮^{sig}/𝒮_n)²; for a line of width 2π/t_coh, TS_A = t_int t_coh(P_s/𝒮_n)², with
  P_s the positive-frequency signal power, so the threshold amplitude scales as **𝒮_n^{1/2}(t_coh t_int)^{−1/4}**.
- **t_int ≪ t_coh:** all signal power in one bin, TS_A = (2/3)(P_s t_int/𝒮_n)² (∫sinc⁴ = 4π/3, WP7D-C4a,b), threshold **𝒮_n^{1/2}t_int^{−1/2}**.
- The crossover is at **t_int = (3/2)t_coh** (WP7D-C4c).
*Literature limits.* 1306.6089 Eqs. (8)–(9) [FT]: B_s = √S_n T^{−1/2} (T < τ) and √S_n(τT)^{−1/4} (T > τ), "ignoring factors of order unity": the
two limits above. 1711.10489 Eq. (54) [FT], Ã_95% = √(2.71[(Tπ/2m_a)∫dv f²/(vλ_B²)]^{−1}): (D.6) with 𝒮^{sig} of (D.1)–(D.5) (WP7D-C3, the
integrand identity); their Eq. (63), S/N = |Φ|(Tτ)^{1/4}/√λ_B, is the t_int ≫ t_coh limit with S/N ≈ 1.8 TS^{1/4} (their Eq. (69)).
*Leading corrections.* (a) For t_int ≲ t_coh the amplitude is a single Rayleigh draw (1711.10489 Eq. (8)); the expected-limit factor must be
marginalised over it (an O(1) weakening at 95%) [E]. (b) Narrow targets (Γ_T < 2π/t_coh) make |R|² the line shape. (c) Annual/daily modulation
of f_χ (CONVENTIONS §8) enters 𝒮_φ.

### 1.7 Acoustic resonators (A9: piezoelectric BAR/hBAR) [D for the structure; source prefactor not re-derived]
The dark-photon E′ couples to the piezoelectric polarisation P^i = e^{ijk}_pt∇^ju^k, i.e. O = −E′·P (a displacement-gradient operator of the
GS sector); a resonator mode n with damping γ_n has R_{nn}(ω) ∝ −1/(ω_n² − ω² − iωγ_n), and (D.3) gives

  P_abs = −y_φ²(ρ_χ/m_φ)∫dω F_φ(ω) Im R_mode(ω),   R_mode(ω) = (|⟨n|O|0⟩|²/V)[1/(ω − ω_n + iγ_n/2) − 1/(ω + ω_n + iγ_n/2)].           (D.7)

*Literature limit.* 2501.05504 Eq. (7) [FT], P_s ∝ m_V²γ_n cos²θ_V/((m_V² − ω_n²)² + (ω_nγ_n)²) with "the delta function smeared by the larger of
the linewidths" (γ_n = ω_n/Q_s, Q_s = min{Q_p, Q_DM}), is (D.7) in the monochromatic limit γ_n ≫ 2π/t_coh (F_φ → δ(ω − m_V)); on resonance
it gives 1/γ_n = Q_s/m (their Eq. (8), WP7D-C6b). **In the opposite, relevant limit Q_p ≫ Q_DM** (their stated regime, Q_p = 10⁶–10¹⁰) the
Lorentzian integrates to (π/2)δ (WP7D-C6a) and (D.7) replaces Q_s by **Q_DM^eff ≡ (π/2)m_V F_φ(ω_n)**, whose maximum is **1.3×10⁶ for the
boosted SHM** (2.4×10⁶ for a rest-frame Maxwellian) (WP7D-C6c): their "Q_DM ∼ 10⁶" holds at the line peak, and (D.7) supplies the line shape
(the signal at ω_n tracks F_φ(ω_n)). The prefactor 32 and the mode normalisation M_n of their Eqs. (2), (7) are not re-derived here (open).
The 1/ε₀ in their Eq. (5) is the slab depolarisation of §1.3.

### 1.8 Oscillating constants, resonant-mass detectors and clocks (§10(ii)) [D for the scaling; E for the corrections]
H_C (WP0 (1.1)) with M_κ → ∞ is unitarily equivalent to α²m_e H̃ with all lengths in units of 1/(αm_e). Hence every equilibrium length scales
as a ∝ (αm_e)^{−1} and a uniform modulus produces the monopole strain **h = −δα/α − δm_e/m_e** (hydrogenic check WP7D-C15).
*Literature limit.* 1508.01798 Eq. (7) [FT], h ≡ −δα/α − δm_e/m_e, is this scaling; their Eq. (8), F_mod,n = −ḧM°RJ_n, is the force on mode n.
In URF the operator is O = −(δm_e/m_e)𝒯_e(0) + (δα/α)𝔘_C(0); at k → 0 a static change only moves the equilibrium (no force in comoving
coordinates, the uniform-dilation analogue of the WP0 (4.8) Ward identity), so the mode drive is ∝ ω² (the ḧ of Eq. (8)) [D, sketch].
*Leading corrections [E].* (a) Finite nuclear mass: zero-point lattice expansion depends on m_e/M_κ, relative O(κ_BO⁴)·(ZPR fraction ~10⁻³).
(b) Relativistic terms (WP0 (1.2) H_rel scale as α⁴m_e, not α²m_e): dln a/dln α = −1 + O((Zα)²), e.g. 0.045 for Cu, the dominant
correction for heavy-element resonators. (c) Clocks (1405.2925, [ABS] here): transition frequencies are static responses (k = 0, ω → 0) to the
same operator; no new object.

### 1.9 Multiferroic / magnetoelectric axion coupling (S9) [D, sketch]
2102.10171 Eq. (5) [FT, PDF], δE_ae ≈ −iħg_ae(∂_ta/2m_e²c)⟨Ψ|σ·∇|Ψ⟩, is the ALP–electron NLO row 2 tr J_e of WP0 §2. Its expectation value
in the ground state is nonzero only in a P- and T-broken reference (the P·M term), and the magnetisation readout is the cross-response
R_{s^z, trJ_e}(0, m_a), which vanishes unless P and T are both broken (P,T selection rule of WP0 (4.3)). Their Eq. (10) (a Lorentzian
1/√((ω_a² − ω_M²)² + η_M²ω_a²) times static Ginzburg–Landau factors) is R_{s^z,trJ_e} in a single-magnon-pole approximation; the "critical
slowing down" is the pole approaching ω → 0 at T_CM. Computable by LSWT on a DFT+SOC magnetic structure (WP4 reference ref = LSWT) with the
tr J_e vertex; the conserving-approximation requirement of WP0 (1.2) applies (a bare bubble in the broken-symmetry basis violates (4.6)).

### 1.10 Computation specification (item 1)
- **Inputs.** Halo: F_φ(ω) from CONVENTIONS §8 (SHM, v_E(t)); 𝒮_φ by (D.1). Platform responses at k → 0: NMR, spin Hamiltonian (B₀, g_I, chemical
  shift and EFG from GIPAW in QE or CASTEP; E*_I from DFT Schiff-screened fields), T₂ and T₁ from data; BAR, elastic and piezoelectric tensors
  (DFPT: QE ph.x, ABINIT), mode shapes and depolarisation by FEM (FEniCS/COMSOL), Q_p from data; moduli, dln a/dln α and dln a/dln m_e by DFT
  with scaled constants plus a scalar-relativistic and ZPR correction, modal overlaps J_n by FEM; multiferroic, R_{s,trJ} by LSWT/TDDFT+SOC
  (new module, ~10³ core-h).
- **Grids.** ω resolution ≤ 10⁻⁷m_φ across the DM line (≥ 3000 points over (1 ± 2×10⁻⁶)m_φ); t_int scan from 10⁻²t_coh to 10³t_coh.
- **Convergence.** TS_A stable to 1% under halving δω; FEM modes to 0.1% in ω_n.
- **Cost.** Seconds per (m_φ, t_int) once R is tabulated; DFT inputs 10²–10⁴ core-h per material.
- **Outputs.** 𝒮^{sig}(ω), 𝒮^{int}(ω), TS_A(t_int), P_abs, the bunching factor 𝒩_c, with the τ string plus geom metadata.

---
## 2. Fermionic absorption (A10: χ + target → ν̃ + target excitation)

### 2.1 The missing operator class [D]
WP0 §2 assumes the DM keeps its identity up to a small splitting Δ_χ and is non-relativistic on both legs. Fermionic absorption needs a
**fermion-number-changing DM-side bilinear**, H_int = Λ_F^{−2}Σ_{Γ,Γ′}∫d³x [ν̃̄Γχ](x)[ψ̄Γ′ψ](x) + h.c., with a relativistic outgoing light
fermion ν̃ (mass m_ν̃, momentum k_ν̃ = p_χ − q, energy E_ν̃ = √(k_ν̃² + m_ν̃²)). The target bilinears ψ̄Γ′ψ map onto the existing rows exactly as in
WP0 §2: ψ̄γ⁰ψ → n; ψ̄γψ → j + (i/2m_s)q × (2s) (Gordon); ψ̄ψ → n − 𝒯-type correction; ψ̄γγ₅ψ → 2s; ψ̄γ⁰γ₅ψ → 2 tr J (O(v)). So the new
class lives entirely on the DM side: the **lepton tensor** 𝔏^{ab}(q,v) ≡ (2j_χ+1)^{−1}Σ_spins (Λ_F^{−2}ū_ν̃Γ_au_χ)*(Λ_F^{−2}ū_ν̃Γ_bu_χ) and

  𝔇^F_ab(q,v) ≡ 𝔏_ab/(4E_χE_ν̃),     ω^F_q(v) ≡ E_χ(v) − E_ν̃(|m_χv − q|)   (relativistic final leg; replaces (2.1)).                       (F.1)

𝔇^F is Hermitian PSD (sum of rank-one projectors, as 𝔇). No field-theoretic matching factor 1/(4m_χm_s) of (2.2) appears on the target side,
because the target operators are field bilinears with non-relativistic normalisation (n = ψ†ψ).

### 2.2 Master formula [D; hypotheses: first Born in H_int; DM plane waves; ν̃ a free plane wave (neutral, non-interacting with the target);
Gibbs target; relativistic normalisation ⟨p|p′⟩ = 2EVδ for χ and ν̃]
Golden rule with Σ_{k_ν̃} → V∫d³q/(2π)³ at fixed p_χ, and the (2π/V) of (3.1):

  Γ^F_χ(v) = ∫d³q/(2π)³ tr[𝔇^{Fᵀ}(q,v) S(q, ω^F_q(v))],     dℛ/dω = (ρ_χ/m_χρ_T)∫d³v f_χ(v)∫d³q/(2π)³ tr[𝔇^{Fᵀ}S(q,ω)] δ(ω − ω^F_q(v)).   (F.2)

This is WP0 (3.3)–(3.4) with 𝔇 → 𝔇^F and ω_q → ω^F_q: **the target side needs only the existing S_ab, evaluated on the one-dimensional curve
ω = m_χ − q (v → 0, m_ν̃ → 0)**, at q ≈ m_χ (no v_min, no η; the velocity integral is trivial at leading order, as in 2011.01940 Eq. (28)). The
1/(4E_χE_ν̃) is the relativistic final-state phase space. For isotropic S̄ and unpolarised DM, v → 0, m_ν̃ = 0:

  dΓ^F_χ/dω = q 𝔏(q) S̄(q,ω)/(8π²m_χ),   q = m_χ − ω.                                                                                   (F.3)

### 2.3 Vector and scalar operators [D; (L) of WP0 (4.6) for current conservation]
*Vector*, Λ_F^{−2}(ν̃̄γ_μP_Rχ)(ψ̄γ^μψ). The traces give 𝔏^{μν} = Λ_F^{−4}[k^μp^ν + k^νp^μ − g^{μν}k·p ∓ iε^{μναβ}k_αp_β] (k = k_ν̃, p = p_χ). The
target current is conserved, q·J_fi = ω_fi n_fi (WP0 (4.6), under (L)), so J_L = (ω/q)n and the contraction is (WP7D-C8a,b,c)

  𝔏^{μν}J*_μJ_ν = (m_χ/Λ_F⁴)[((q+ω)²/q)|n|² + q|J_T|² + P-odd ε-term],   (q + ω) = m_χ at v = 0, so
  Γ^F_V = ∫d³q/(2π)³ (1/4Λ_F⁴)[(m_χ²/q²)S_nn(q, m_χ−q) + S_{J_TJ_T}(q, m_χ−q) + S^A-term],                                                (F.4)

with J the full NR vector current (paramagnetic + magnetisation (i/2m_s)q × 2s). The density coefficient m_χ²/q² is **exact for any target**
(bound or free) once the longitudinal current is eliminated by continuity. The ε-term pairs with the antisymmetric part S^A_{J_TJ_T} ∝ ε q̂,
which is P-odd and vanishes for P-invariant targets; in chiral targets it is the fermionic analogue of the 𝒪₅×𝒪₈ enantiomer term of WP4 [3.3]
and requires the tr[𝔇ᵀS] order (WP0 §3.2).
*Scalar*, Λ_F^{−2}(ν̃̄P_Lχ)(ψ̄ψ): 𝔏_S = E_ν̃m_χ/Λ_F⁴ (WP7D-C8d), so Γ^F_S = ∫d³q/(2π)³ (1/4Λ_F⁴)S_nn(q, m_χ−q) + O(𝒯-row).                       (F.5)

### 2.4 Literature limits [D]
**(a) Neutral current on nuclei.** For a free nucleus of species κ, S_NN = 2π𝓃_κA_κ²|F^M_κ|²δ(ω − q²/2M_κ). Then (F.4) gives (WP7D-C9)

  Γ^F = 𝓃_κA_κ²|F^M_κ|²σ_NC/(1 + q₀/M_κ),   m_χ = q₀ + q₀²/2M_κ,   σ_NC ≡ m_χ²/(4πΛ_F⁴);   Γ^F = 𝓃_κA_κ²|F^M_κ|²σ_NC(1 − m_χ/M_κ + …).        (F.6)

1905.12635 Eq. (4) [FT], R = (ρ_χ/m_χ)σ_NC Σ_j N_{T,j}A_j²F_j²Θ(E⁰_{R,j} − E_th) with σ_NC = m_χ²/(4πΛ⁴) (vector NC operator, their Eq. (1)), is
(F.6) at M_κ → ∞. Note the full m_χ² (not E_ν̃m_χ) needs the nuclear longitudinal current, eliminated by continuity. **Leading corrections.**
(i) −m_χ/M_κ (recoil Jacobian, WP7D-C9). (ii) **Crystal line shape**: at q ≈ m_χ ≫ q_BZ the nucleus is in the impulse regime (K = imp, WP0 L6):
the δ at E⁰_R = m_χ²/2M becomes a Gaussian of width σ_ω = q√(⟨p²_κ⟩/3)/M_κ with the true ⟨p²_κ⟩ (zero-point included), i.e.
σ_ω/E⁰_R = 2√(⟨p²_κ⟩/3)/m_χ ≈ 4×10⁻³ for Si at m_χ = 10 MeV [E] (√(⟨p_x²⟩) ≈ 21 keV); the DM velocity adds ±m_χv relative 2×10⁻³
(1905.12635's "ΔE_R/E_R ∼ 10⁻³"). Both are now computable (WP2 L6 skewness from the BO curvature included). (iii) Nuclear internal excitation:
for q ≳ 1/r_N or ω ≳ 100 keV the frozen-internal-state assumption of WP0 §2 fails (outside this framework; 2405.05728 treats nucleon Fermi
motion [ABS here]).
**(b) Electrons (atoms).** Dictionary [D]: 1509.01598 Eq. (52) [FT], dR/dlnE_R = (ρ_χ/m_χ)(σ̄_e/8μ²)∫q dq|F_DM|²|f_ion|²η, compared with WP0 (9.2)
per atom gives **𝒮̄_at(q,ω) = π|f_ion(k′,q)|²/(2E_R)** (ω = E_R + |E_B|; f_ion as in their Eq. (51), spin-summed occupied states) (WP7D-C10a).
Then (F.3) with the density row, 𝔏 = |ℳ|²/(4m_e²) (|ℳ|² averaged over initial, summed over final spins; Σ over both target-electron spins
sits in S), gives dσv/dE_R = |ℳ|²q|f_ion|²/(64πm_χm_e²E_R) = **2011.01940 Eq. (7) [FT], equivalently its appendix Eq. (30)** (WP7D-C10b).
The scalar case (F.5) reproduces **their Eq. (10)**, dσv_S/dE_R ≃ σ_eq²|f_ion|²/(4E_Rm_χ²), σ_e = m_χ²/(4πΛ⁴), **exactly** (WP7D-C10c). The vector
case: their Eq. (9) multiplies |f_ion|² by the free-electron |ℳ|² evaluated at q = m_χ + E_B − E_R; (F.4) instead gives m_χ²/q² from
continuity. The two agree to O(m_χ²/m_e²) at free kinematics (WP7D-C10d, free 2 → 2 kinematics exact: WP7D-C11) and differ at bound
kinematics by the factor **1 − ω²/m_χ² + ω(m_χ−ω)(2m_χ−ω)/(m_χ²m_e) + O(m_e^{−2})** (WP7D-C10e). The free-vertex factorisation is not
current-conserving off the free shell; (F.4) is (under (L), at the NR-operator level). Size [E]: Xe K shell (ω ≥ 34.6 keV) at m_χ = 100 keV,
−12% + 7% ≈ −5%, comparable to the (Zα)² ≈ 0.16 relativistic correction the source itself flags ("once q ≳ m_e … relativistic corrections");
for valence shells < 10⁻³ (Interface flag IF-D10). **Leading corrections:** (i) S_{J_TJ_T} term of (F.4), relative O(⟨p_e²⟩/m_e² + m_χ²/m_e²);
(ii) Dirac bilinears for core shells (WP0 (1.2) "relativistic cores"; O((Zα)²)); (iii) in crystals use the all-electron S_nn of WP1 at
q ∼ m_χ (10–500 keV), which is above QEdark/DarkELF cutoffs (L-D8).

### 2.5 What remains outside [exact gaps]
- **Charged current** (χ + n → p + e⁻, 1905.12635 Eqs. (6)–(13)): the target operator changes the nuclear species (isospin-raising β-decay matrix
  element) and the outgoing e⁻ is charged, so its Coulomb distortion (the Fermi function 𝓕(Z+1,E_e), their Eq. (12)) is a final-state
  interaction with the target. Neither is a matrix element of the 16-row basis with a free final lepton. Gap: a nuclear transition-operator row
  plus distorted lepton waves; nuclear-physics input, not solid-state response.
- **Massive ν̃ with m_ν̃ ≈ m_χ** (inelastic-like): covered by (F.1) (ω^F_q → q·v − q²/2m_ν̃ − Δ_χ with Δ_χ = m_ν̃ − m_χ, i.e. WP0 (2.1) at O(v²)).

### 2.6 Computation specification (item 2)
- **Inputs.** Electrons: all-electron S_nn(q,ω), S_{J_TJ_T}(q,ω) along ω = m_χ − q for m_χ ∈ [E_g, 1 MeV]; atoms with DHF orbitals (GRASP-class) for
  q ≳ m_e/3; crystals with QCDark2-type all-electron PAW extended to q ≤ 1 MeV (WP1 interface IF-D5). Nuclei: S^{GS}_κκ at K = imp (WP2 L6) with
  ⟨p²_κ⟩ from DFPT phonon DOS; Helm F^M_κ.
- **Grids.** One-dimensional in q per m_χ (≈ 200 points across the ionisation/impulse support); m_χ log grid 40 points per decade.
- **Convergence.** Line width converged to 1% in ⟨p²_κ⟩; electron spectra to 2% in PAW augmentation at q ≤ 1 MeV.
- **Cost.** Nuclei: negligible. Electrons: 10⁴–10⁵ core-h per crystal for the high-q all-electron table.
- **Outputs.** dℛ/dω per operator (V, S, A), peak positions and widths, the τ string with K = imp (nuclei) or n_D/𝒳 (electrons).

---
## 3. Two-insertion processes (A11, §11.9)

### 3.1 Classification [D]
At second order the transition operator is T = H_int + H_int G₀(E_i + ω_in) H_int + …; for the target the relevant objects are:
(a) a **single target operator** multiplying a DM-side operator quadratic in the DM fields (contact pair absorption): two-point S_OO;
(b) **two target operators** joined by a target propagator, 𝒯^{(2)}_{ab}(k₁,k₂;ω₁) ≡ Σ_m O_b(k₂)|m⟩⟨m|O_a(k₁)/(E_i + ω₁ − E_m + i0) + (1 ↔ 2):
the rate needs S_{𝒯𝒯}, a **four-point** function of the O's;
(c) interference of (a) and (b) to the same final state: Re⟨T_a†T_b⟩, a **three-point** function, i.e. the quadratic retarded response
R^{(2)}_{abc}(k₁,ω₁;k₂,ω₂) (the second-order Kubo kernel);
(d) a DM propagator between two target insertions (double scattering): ⟨O†O†OO⟩ at two momenta.
**Reductions to two-point functions [D]:** (b) reduces to S of an effective one-body operator when every intermediate state is far off shell
(|E_i + ω₁ − E_m| ≫ the spread of E_m − E_i): closure gives 𝒯^{(2)} → [O_b,[H,·]]-type seagull plus a polarisability operator; (d) reduces to
products S(q₁)S(q₂) when the target is Gaussian (RPA, Wick factorisation) and the two momenta are uncorrelated, which is the kinetic
(transport) limit used in §4.1; (c) has no two-point reduction except through a one-loop RPA expression of R^{(2)} (e.g. the Lindhard quadratic
response of the electron gas).

### 3.2 Contact pair absorption [D]
H_int = G_pair∫d³x (S†S)(x)O(x) (2507.14287 Eq. (3), scalar DM, O = m_eψ̄ψ → m_e n, or ψ̄γ^μγ₅ψ → spin rows). The DM pair (p, p̄) is annihilated
at one point, so with DM occupation numbers f_DM (∫d³p/(2π)³g f = n per species) the rate per DM pair density is

  Γ_pair = ∫d³p d³p̄/(2π)⁶ g² f(p)f(p̄) |G_pair|²/(4E_pE_p̄) S_OO(p + p̄, E_p + E_p̄)   → ≈ n_χn_χ̄|G_pair|²S_OO(≈0, 2m_χ)/(4m_χ²).            (T.1)

Only the existing two-point S at (k ≈ 0, ω ≈ 2m_χ) enters: **pair absorption is single absorption at 2m_χ with the quadratic operator's row**,
so the L9b machinery (and its in-medium screening (3.6) for charge-like rows) applies unchanged. *Literature limit.* 2507.14287 Eqs. (5)–(7)
[FT], dΓ_p = 2π|ℳ_fi|²δ(ΔE_fi − E − Ē)dρ_p with dρ_p = d³p d³p̄ g²f f/(2π)⁶, is (T.1) for a discrete atomic transition (S_OO a δ at ΔE_fi, with
the relativistic normalisation inside their |ℳ_fi|²). Their Eq. (8) normalisation with ξ = 44.8 gives each of χ and χ̄ the density
ρ_DM/(2m_DM) (escape cut at 2.5β_c included; WP7D-C13), which fixes how ρ_χ is split between particle and antiparticle in (T.1).
*Leading corrections.* Quantum statistics (their S_Q terms), the Tremaine–Gunn cap (their Eq. (10)) for fermions, and for a solid target the
k = p + p̄ ≈ 2m_χv dependence of S (negligible for k ≪ 1/a_lat).

### 3.3 Pair absorption through two linear couplings [D, structure]
If the DM couples linearly (y_φφO, (3.3)) the pair φφ → target is second order: amplitude ⟨f|𝒯^{(2)}(k₁,k₂;m_φ)|i⟩ and rate ∝ y_φ⁴n_φ²S_{𝒯𝒯}(k₁+k₂, 2m_φ),
a four-point function. When 2m_φ and m_φ are both off-resonant for the target's spectrum (e.g. m_φ < E_g < 2m_φ, or both below the gap),
closure turns 𝒯^{(2)} into the static or dynamic polarisability operator and S_{𝒯𝒯} into a two-point function of it (a two-photon-absorption
type response). If a contact term (§3.2) is also present, the interference needs R^{(2)} (three-point). Not otherwise needed by any catalog row.

### 3.4 Dark Compton scattering (V or a + e → γ + e) [D for the Thomson limit]
First order in κ_mix, first order in e. In Coulomb gauge the NR target couples to (A + κ_mixA′) through j·A and the seagull (e²/2m_e)n(A + κ_mixA′)²,
so the transition operator is

  𝒯^C(q) = κ_mix(e²/m_e)(ε·ε′*)n_e(q) + κ_mix e²Σ_m[(ε′*·j)|m⟩⟨m|(ε·j)/(E_i + m_V − E_m) + (ε·j)|m⟩⟨m|(ε′*·j)/(E_i − ω′ − E_m)],   q = k_V − k′,  (T.2)

and Γ = ∫d³k′/((2π)³2ω′)(1/2m_V)Σ_pol S_{𝒯^C𝒯^C}(q, m_V − ω′). For a free electron at rest the resonant terms vanish at O(m_V/m_e) (ε·p_i = 0;
intermediate momentum −k′ ⟂ ε′) and the seagull gives, with S_nn = 2π𝓃_eδ(ω − q²/2m_e) and ⟨Σ_λ′|ε·ε′|²⟩ = 2/3 (WP7D-C12a),

  Γ = 𝓃_eκ_mix²σ_Th·ω′/(m_V(1 + ω′/m_e)),   ω′ + ω′²/2m_e = m_V,   σ_Th = e⁴/(6πm_e²) = 8πα²/3m_e²,                                       (T.3)

i.e. κ_mix²σ_Th(1 − (3/2)m_V/m_e + …). *Literature limit.* 2109.08168 Eq. (2) [FT], R = (n_e/ρ_T)(ρ_DM/m_V)(e⁴ε²/24πm_e²)(m_V + 2m_e)(m_V² + 2m_em_V +
2m_e²)/(m_V + m_e)³, equals (T.3) **through O(m_V/m_e)**, both giving 1 − 3x/2 (WP7D-C12b,c); the O(x²) difference is relativistic (spin and
Klein–Nishina terms) and needs Dirac bilinears. **URF content.** (i) In a bound target (T.2) with ω′ ≈ m_V ≫ binding is the Compton impulse
approximation: S_nn(q, m_V − ω′) is fixed by the shell Compton profiles J^{(sh)}(p_z) already tabulated for WP6 (NOTATION §M); binding
corrections are the resonant terms of (T.2) (four-point, reducing to two-point by closure when m_V ≫ |E_B|). (ii) The final photon is emitted
into the medium: its phase space carries n_r(ω′) and the photon-reducible screening of (3.6) [D, sketch]; the source neglects in-medium effects
"insignificant in the high DM mass regime", consistent with n_r → 1 at ω′ ≫ ω_p. (iii) The ALP case (their Eq. (3)) needs the spin row with
the pseudoscalar-form seagull (e g_aee/2m_e)aσ·A; not re-derived here (open).

### 3.5 Scattering plus mediator absorption (§11.9; 2501.09642) [D]
2501.09642 [FT, Abstract and §3.4] combines halo-DM scattering through a light dark photon with absorption of solar dark photons in the same
detector. These are **two independent single-vertex processes** (WP0 L0 with F_DM of the light mediator, and WP0 L9b), with different initial
states, so they add incoherently and share only κ_mix (and the target S). A combined "scattering-into-absorption" amplitude would need the
t-channel mediator on shell, q² = ω² − |q|² = m_d²; for NR halo DM ω ≤ |q|v ≪ |q|, so the exchanged mediator is always spacelike and never
on shell. **No new response object; §11.9 is closed** by L0 + L9b with shared parameters.

### 3.6 Second Born and the Barkas term [D, structure]
The interference of first and second Born amplitudes for a charged or light-mediator projectile is case (c) of §3.1: Γ^{(3)} ∝ Re⟨T₁†T₂⟩, linear in
R^{(2)}. This is the WP0 §9.1 correction (β) ∼ μ_χ|Ṽ|q/4π and, for stopping, the Z³ Barkas term. It is the only place a three-point
function enters any catalog row; for the electron gas R^{(2)} is the Lindhard quadratic response (one-loop RPA).

### 3.7 Computation specification (item 3)
- **Inputs.** Pair absorption: S_OO(k ≈ 0, 2m_χ) from the L9b tables (σ₁(2m_χ) for charge-like rows; spin rows from WP4); dark Compton: J^{(sh)}(p_z)
  (WP6 tables) or S_nn at q ≈ m_V from WP1 high-q tables, plus n_r(ω′); Barkas: R^{(2)} of the HEG plus a local-density map (new module).
- **Grids.** Dark Compton: ω′ ∈ m_V(1 ± 0.1), 100 points, angles 32; pair absorption: as L9b.
- **Cost.** Minutes, except R^{(2)} (10² core-h for an LDA map).
- **Outputs.** Rates and spectra with the τ string; the dark-Compton spectrum (a line at T = m_V²/2(m_e + m_V) broadened by J^{(sh)}).

---
## 4. Out of scope, with the interfaces

### 4.1 Damage tracks and paleo-detectors (D3, D4): the stopping-power interface [D]
**Stopping power as a limit of the master formula.** Take (3.3) for a projectile of charge form factor Z_κ(k) and velocity v_N with no recoil
(m → ∞, so ω_q = q·v_N), coupled to the total target charge ((5.4), total ε), and weight by the energy loss ω:

  −dE/dx = v_N^{−1}∫d³k/(2π)³ ω |Z_κ(k)e²/k²|² S_zz(k, k·v_N) = (2Z_κ²α/πv_N²)∫(dk/k)∫₀^{kv_N}dω ω L(k,ω)   (T = 0, Z_κ const),        (S.1)

the Lindhard dielectric stopping in campaign units (prefactor WP7D-C14a; = WP5-v3 §1.1(e), Gaussian e_G² = α, same number). For
k v_N ≫ ω_max the inner integral saturates the f-sum (9.5), (π/2)ω_p², between k_min ≈ Ī/v_N and the Bethe-ridge cutoff 2m_ev_N:

  −dE/dx = (4πZ_κ²α²𝓃_e/m_ev_N²) ln(2m_ev_N²/Ī),   ln Ī ≡ (2/πω_p²)∫₀^∞dω ω L(0,ω) ln ω,                                                 (S.2)

the non-relativistic Bethe formula (WP7D-C14b; the defining integral for Ī is [D] at this level, its use in the literature [UNVERIFIED] here).
Nuclear stopping is the same construction on S^{GS}_κκ (K = imp, WP0 L6). **Why tracks are outside.** (i) For keV–MeV recoils v_N ≪ v_F and the
Born parameter is Z_κα/v_F ≈ 15 (Si), 35 (Ge) (WP5-v3 §1.1(e)): (S.1) is not a derived limit there, only a fit (WP5-v3 §3.3). (ii) A track is a
sequence of ~10²–10⁴ correlated collisions whose targets are damaged by earlier ones: case (d) of §3.1 at all orders, plus thermal-spike and
Coulomb-explosion dynamics; there is no finite-order response expansion. (iii) The readout (etching, NV strain spectroscopy, X-ray) measures a
defect configuration, not an excitation spectrum. **Hand-off.** The URF delivers, per recoil seed, the prompt joint seed (7.3) and the
differential electronic and nuclear loss kernels dP/dω_e(k; v_N) from (S.1) at fixed k (Born, valid only where
Z_κα/v_rel ≪ 1), and WP5 transports with its Markov ion-transport truncation 0 / MLIP-MD (WP5-v3 §1.1, §3.4). Track length (CSDA) = ∫dE/(S_n + S_e)
and the damage map are WP5 outputs. Interface flag IF-D6.

### 4.2 DM-side radiative de-excitation (I2) [D for the split]
2006.13918 Eq. (2) [FT], τ^{−1} ∼ πδ³/Λ_d², is the vacuum magnetic-dipole decay χ* → χγ. **It has no target vertex**: the target operators O_a
never appear in the amplitude, so no S_ab enters. The medium enters only through the photon propagator 𝒟^γ of WP0 (3.6), via
Γ_med = −2 Im Σ_χ*(δ) with the in-medium photon:
- the transverse on-shell part gives emission with photon density of states ∝ Re n_r(δ) (transparent, non-magnetic medium; local-field factors
  aside) [D, sketch];
- the absorptive part (ε₂(δ) > 0) is **non-radiative transfer to the target**, χ* + target → χ + target excitation through a virtual photon. That
  *is* inside URF: WP0 (3.3) with Δ_χ = −δ (exothermic, (2.1)), the dipole vertex in 𝔇 (∝ |μ_χ × q|²/q⁴ against S_{J_TJ_T}, or |d·q|²/q⁴ against
  S_zz = (2q²/e²)L), i.e. catalog row I1/I4 machinery.
So I2 stays out (its signal is a DM-internal decay followed by ordinary photon absorption, L9b with a photon), and its only target-dependent
corrections are n_r(δ) and the non-radiative channel, which belongs to (3.3).

---
## 5. Claims, tags and checks
| Claim | Tag | Check / source |
|---|---|---|
| (D.1) field spectrum; 1711.10489 Eq. (24) as a limit | D | C2a,b |
| (D.2) coherent amplitude = off-diagonal retarded R; finite-body replacement of k_φ | D; finite-body and depolarisation D, sketch | — |
| (D.3) mean power and mean counts = f_χ-averaged (3.5) at any t_int; Bose bunching Var N = N̄ + N̄²/𝒩_c | D; bunching D, sketch | C1a,b |
| (D.4) Bloch transient/steady limits; 1306.6089 Eq. (1), 2101.01241 Eq. (1); envelope sin(δω_Lt/2)/(δω_L/2) | D | C5a–d |
| (D.5)–(D.6) SNR; t^{−1/2} vs (t t_coh)^{−1/4}; crossover (3/2)t_coh; 1306.6089 Eqs. (8)–(9), 1711.10489 Eqs. (54), (63) | D (weak signal, Gaussian) | C3, C4a–c |
| (D.7) BAR: Q_s → (π/2)m F_φ(ω_n) ≤ 1.3×10⁶ (SHM) for Q_p ≫ Q_DM | D; prefactor 32 not re-derived | C6a–c |
| (D.8) h = −δα/α − δm_e/m_e from H_C scaling; drive ∝ ω²; corrections (Zα)², κ_BO⁴ | D; corrections E | C15 |
| (D.9) multiferroic = R_{s,trJ_e} in P,T-broken reference | D, sketch | — |
| (F.1)–(F.2) fermion-number-changing class, 𝔇^F, ω^F_q, master formula | D | C11 |
| (F.4)–(F.5) vector/scalar contractions; m_χ²/q² exact by continuity; P-odd J_T×J_T term | D | C8a–d |
| (F.6) 1905.12635 Eq. (4) + (1 − m_χ/M) + impulse line width | D; width E | C9 |
| 2011.01940 Eqs. (7), (10) exact; Eq. (9) agrees at free kinematics, differs by 1 − ω²/m² + … at bound kinematics | D; size E | C10a–e |
| (T.1) contact pair absorption = two-point S at (≈0, 2m_χ); 2507.14287 Eqs. (5)–(8), ξ = 44.8 ↔ ρ/2m per species | D | C13 |
| (T.2)–(T.3) dark Compton Thomson limit; 2109.08168 Eq. (2) through O(m_V/m_e) | D | C12a–c |
| §3.5 scattering + mediator absorption are independent; mediator never on shell | D | — |
| (S.1)–(S.2) Lindhard and Bethe stopping as limits of (3.3); tracks outside (Born parameter, multiple scattering) | D; Ī usage UNVERIFIED | C14a,b |
| §4.2 I2 split (radiative: n_r only; non-radiative: inside (3.3)) | D, sketch | — |

---
## 6. Symbols introduced/used (against NOTATION v4 + R9 rows)
**Used as defined in NOTATION/CONVENTIONS:** q, ω, ω_q, Δ_χ, v, v₀, v_E, f_χ, η, ρ_χ, ρ_T, m_χ, j_χ, 𝐒_χ, 𝔇_ab, 𝒱_a, S_ab, S̄, R_ab, R̃, ε, ε₀, ε_∞, L,
v_C, Π^γ_T, 𝒟^γ_{μν}, y_φ, φ, k_φ, a^φ_k, Γ_abs, Γ_net, Γ_χ, ℛ, κ_mix, g_aee, g_aγγ, B₀, O_a, n_e, s_e, j_e, J_e, tr J_e, 𝒯_e, T_e, I_κ^β, F^M_κ,
F^Σ_κ, A_κ, Z_κ, M_κ, 𝓃_e, 𝓃_κ, ω_p, 𝓜¹, K (τ label, K = imp), τ, 𝒳, n_T, GS, X0, X+, κ_BO, q_BZ, G_min, a_lat, J^{(sh)}(p_z), S^{stop}_e, n_r(ω),
σ₁, E_R, E_B (as the sources' binding energy, quoted), α, e, m_e, μ_χe, σ̄_e, F_DM, T (temperature), β, V, Ω, H_C, H_rel, L19, L6, L9b.
**Introduced here (proposed NOTATION rows; no collision found):**
| Symbol | Meaning | Where |
|---|---|---|
| t_coh ≡ 2π/(m_φv₀²), ℓ_coh ≡ 2π/(m_φv₀) | DM-field coherence time and length (reference scalars; τ is the truncation index, so not τ_c) | §1.0 |
| t_int | integration time | §1.0, (D.6) |
| N_dB | DM occupation per de Broglie volume | §1.0 |
| 𝒮_φ(k,ω), 𝒮_φ(ω), F_φ(ω), f_sp(v) | classical-field spectral density; k-integrated line; normalised line shape; DM speed distribution | (D.1) |
| O_rd, X | readout operator; its sample total O_rd(k→0) | (D.2), (D.5) |
| 𝒮_X^{sig}, 𝒮_X^{int}, 𝒮^{det}, 𝒮_n, P_s | signal, intrinsic (FDT) and detector noise PSDs; total noise; signal power | (D.5)–(D.6) |
| TS_A | Asimov test statistic | (D.6) |
| 𝒩_c | number of independent coherence cells in an exposure | §1.4 |
| Γ_T | target response width (1/T₂, ω_n/Q_mode) | §1.0 |
| ω_L, δω_L ≡ ω_L − m_φ, T₂, T₁, M₀, Ω_a | Larmor frequency, detuning, spin relaxation times, equilibrium magnetisation, rotating-frame Rabi frequency | (D.4) |
| d_EDM, E*_I | nucleon EDM; Schiff-screened effective field at site I | §1.2 |
| γ_n, Q_mode, Q_DM^eff ≡ (π/2)m_φF_φ(ω_n) | mode width; mode quality factor; effective DM quality factor | (D.7) |
| 𝔘_C(k) | Coulomb-energy density operator (new row a = (C, 𝔘); ∂H/∂ln α) | §1.2, (D.8) |
| h_mod, d_{m_e}, d_α | modulus strain; modulus couplings (1508.01798 "d_{m_e}, d_e"; d_e renamed to avoid the electron subscript) | (D.8) |
| geom ∈ {bulk, body} | τ metadata: bulk response vs finite-body (mode-resolved, depolarised) response | §1.2 |
| ν̃, m_ν̃, E_ν̃, 𝐤_ν̃ | outgoing light fermion of fermionic absorption (ν is the phonon branch label) | (F.1) |
| Λ_F | contact scale of the fermion-number-changing operator (sources' Λ) | (F.1) |
| 𝔏^{ab}, 𝔏^{μν} | lepton (χ→ν̃) tensor | (F.1), (F.4) |
| 𝔇^F_ab, ω^F_q(v) | DM tensor and kinematic energy transfer of fermionic absorption | (F.1)–(F.2) |
| σ_NC | per-nucleon NC absorption cross-section m_χ²/(4πΛ_F⁴) (1905.12635) | (F.6) |
| 𝒮̄_at, f_ion | per-atom angle-averaged S; sources' ionisation form factor (quoted) | §2.4(b) |
| G_pair, f_DM, g_DM, ξ | pair-contact coupling; DM occupation; DM degrees of freedom; 2507.14287 normalisation (quoted) | (T.1) |
| 𝒯^{(2)}_{ab}, 𝒯^C | second-order transition operator; dark-Compton (Raman) operator | §3.1, (T.2) |
| R^{(2)}_{abc} | quadratic (three-point) retarded response (χ is the DM, so not χ^{(2)}) | §3.1, §3.6 |
| σ_Th | Thomson cross-section (σ_T is WP6's sensor width) | (T.3) |
| ω′, ε, ε′ | emitted photon energy; dark-boson and photon polarisation vectors | (T.2) |
| Ī | mean excitation energy of the Bethe formula | (S.2) |
| Γ_med, Σ_χ* | in-medium decay width, DM self-energy | §4.2 |

---
## 7. Interface flags
| # | Owner / user | Quantity | Recorded form | This return |
|---|---|---|---|---|
| IF-D1 | NOTATION (coordinator) | new symbols | — | rows of §6 |
| IF-D2 | WP0 §2, CONVENTIONS §7 (operator basis) | rows and DM-side classes | 16 rows + 𝒯_e; DM keeps identity (Δ_χ small) | add the Coulomb-energy row 𝔘_C (moduli, d_α) and the fermion-number-changing DM-side class 𝔇^F with relativistic ω^F_q (F.1)–(F.2) |
| IF-D3 | CONVENTIONS §11 (τ metadata) | finite-body response | bulk only | add metadata geom ∈ {bulk, body}; coherent-regime entries carry it |
| IF-D4 | WP2 (L6, K = imp) | NC fermionic-absorption line shape | — | S^{GS}_κκ at q = m_χ with the true ⟨p²_κ⟩ gives the line width (≈ 4×10⁻³ relative, Si at 10 MeV [E]) |
| IF-D5 | WP1 (all-electron S, high q) | S_nn, S_{J_TJ_T} at q ∼ 10 keV–1 MeV along ω = m_χ − q | QEdark/DarkELF cutoffs | needed for electron fermionic absorption in crystals; Dirac bilinears for cores (WP0 (1.2)) |
| IF-D6 | WP5 (transport) | stopping kernels | WP5-v3 §1.1(e) Lindhard | (S.1) is the m → ∞, ω-weighted limit of (3.3); Barkas = three-point R^{(2)} (§3.6), beyond WP5's Born kernels |
| IF-D7 | WP6 (likelihood) | absorption statistics | Poisson | coherent regime: exponential periodogram bins (D.6); counting with 𝒩_c ≲ N̄ is super-Poissonian, Var N = N̄ + N̄²/𝒩_c |
| IF-D8 | WP4 ([3.3], L19) | chiral targets | 𝒪₅×𝒪₈ interference | fermionic absorption with chiral (P_R) operators has a P-odd S^A_{J_TJ_T} term (F.4) |
| IF-D9 | LIMITS L9b, WP3 §4 | absorption in finite bodies | bulk (3.6) | depolarisation for L_s ≪ 2π/m_φ; BAR Q_s → Q_DM^eff (D.7) |
| IF-D10 | LIMITS (new L-D8), source 2011.01940 | vector-operator bound-electron factor | free-vertex |ℳ|² at bound q | continuity gives m_χ²/q² (F.4); difference 1 − ω²/m_χ² + … (C10e); CLAIMED, size comparable to the relativistic correction the source flags; not a REFUTED rating |
| IF-D11 | LIMITS (new L-D1), source 1306.6089 Eq. (1) | off-resonance envelope | sin(δω_Lt)/δω_L ("≈") | exact small-tilt envelope sin(δω_Lt/2)/(δω_L/2) (C5b); resonant growth agrees |
| IF-D12 | open | 2501.05504 prefactor 32, mode normalisation M_n; 2109.08168 Eq. (3) (ALP seagull) | — | not re-derived here |

---
## 8. Proposed LIMITS rows (provisional labels L-D1…L-D12; numbers to be assigned by the coordinator)
| # | τ / chain (URF) | Source formula [this return, FT] | Status |
|---|---|---|---|
| L-D1 | (D.2) at k → 0, spin row with B₀, linear response, rotating wave; transient t ≪ T₂ and steady state t ≫ T₂ (D.4) | 1306.6089 Eq. (1); 2101.01241 Eq. (1) | D (envelope ✎, IF-D11) |
| L-D2 | (D.1) Gaussian field from f_χ; signal PSD (D.5) | 1711.10489 Eqs. (10), (24) | D |
| L-D3 | (D.6) weak signal, t_int ≪ t_coh and t_int ≫ t_coh | 1306.6089 Eqs. (8)–(9); 1711.10489 Eqs. (54), (63), (69) | D |
| L-D4 | (D.3)/(D.7) GS sector, finite-body mode, piezo vertex, monochromatic limit; Q_p ≫ Q_DM gives Q_DM^eff | 2501.05504 Eqs. (5), (7), (8) | D (structure; prefactor open) ✎ |
| L-D5 | (D.8) H_C scaling, k → 0, mode drive ∝ ω² | 1508.01798 Eqs. (7)–(8) | D |
| L-D6 | (D.2) cross-response R_{s^z,trJ_e}, P,T-broken reference, single magnon pole | 2102.10171 Eqs. (5), (10) | D, sketch |
| L-D7 | (F.2)/(F.4) vector NC, nuclear density row, free nucleus, M_κ → ∞; crystal: K = imp line shape | 1905.12635 Eqs. (3)–(4) | D |
| L-D8 | (F.3)–(F.5) electron density row, per-atom 𝒮̄_at = π\|f_ion\|²/2E_R (1509.01598 Eq. (52)) | 2011.01940 Eqs. (7), (9), (10), (30) | D ((10) exact; (9) ✎ at bound kinematics, IF-D10) |
| L-D9 | (T.1) contact pair absorption, two-point S at (≈0, 2m_χ) | 2507.14287 Eqs. (5)–(8) | D |
| L-D10 | (T.2)–(T.3) seagull row, free S_nn, NR; O(m_V/m_e) recoil exact | 2109.08168 Eq. (2) (and Eq. (3), open) | D through O(m_V/m_e) |
| L-D11 | (S.1)–(S.2) (3.3) with m → ∞, ω-weighted, total ε, Born | WP5-v3 §1.1(e) (Lindhard, owner WP5); Bethe [UNVERIFIED here] | D (Born only; tracks out of scope) |
| L-D12 | interface only: I2 radiative decay, in-medium n_r factor; non-radiative part = (3.3) with Δ_χ = −δ | 2006.13918 Eq. (2) | D, sketch (out of scope) |

**Literature read in full text in this return (arXiv IDs verified against the API):** 1306.6088 (title/abstract level only, [ABS]), 1306.6089,
1711.10489, 2101.01241, 2501.05504, 1508.01798, 2102.10171 (PDF), 1905.12635, 2011.01940, 1509.01598 (appendix A.3), 2507.14287, 2109.08168,
2501.09642 (abstract and §3.4), 2006.13918. Verified but not read: 2609.07908, 2410.17308, 2308.00309, 2405.05728, 1405.2925 ([ABS]).
