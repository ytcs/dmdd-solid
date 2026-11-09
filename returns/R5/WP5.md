# R5 / WP5: energy partition and measured quanta

Isolated theory agent. Read scope as in the brief. Theory only. The identity and estimate checks are in `code/WP5/checks.py`
(sympy and arithmetic, 10 checks, all PASS, < 10 s). `code/WP5/html2txt.py` extracts the full text from arXiv HTML. All 24 arXiv IDs
cited here were verified against the arXiv API (§10). Tags: **[D]** DERIVED (hypotheses stated), **[E]** ESTIMATED, **[C]** CONJECTURED.
WP0 equations are cited as WP0 (s.n). This return's own equations are numbered (W1)…(W24) to avoid collisions. Units follow NOTATION:
ħ = c = k_B = 1, e² = 4πα, v_p = e²/p². The ionization yield is N_eh (WP0 §10). Source formulas are quoted from full text [FT].

---
## 1. The partition-transport stage of the URF

### 1.1 Theorem C: every cascade kernel is a master-formula rate with a target-internal projectile [D]
*Hypotheses.* First order in the screened interaction W (GW level). The projectile is a quasiparticle of the target (a Bloch electron or
hole in state nk, or a moving ion), and it is distinguishable from the medium's response (exchange is treated separately below).
*Statement.* Put WP0 (3.3) to work with the DM replaced by the projectile. A Bloch carrier couples to the **total** charge, so its
coupling vector is |c⟩ = |z⟩. Its vertex is 𝒱(p) = v_p ρ_{n′n}(k, −p), where p = q + G is unrestricted and the carrier goes nk → n′, k−p.
WP0 (5.4) then gives

  Γ_{nk→n′,k−p} = ∫d³p/(2π)³ |v_p ρ_{n′n}(k,−p)|² S_zz(p, ω) [1 − f_{n′,k−p}],   ω = ε_{nk} − ε_{n′,k−p},
  ⇒ Γ_{nk} = Σ_{n′} ∫ d³p/(2π)³ 2 v_p |ρ_{n′n}(k,−p)|² Im[−(ε^{-1})_{00}(p,ω)] [1 − f] /(1 − e^{−βω}).                      (W1)

(W1) is 2|Im Σ^{GW}_{nk}| in the head-only form. With local fields it becomes Σ_{GG′} ρ*_G v_{p+G} Im(−ε^{-1}_{GG′}) ρ_{G′}, which is
0812.2923 Eqs. (1)–(2) [FT], τ^{-1} = (2Z/ħ)|ImΣ|. The chain is checked as follows: S_zz = (2p²/e²)L, so |𝒱|²S = 2v_p|ρ|²L.
**Consequences:**
- (a) **Impact ionization, plasmon emission and plasmon decay are a single channel.** They are the e–h part of Im[−1/ε]. The plasmon
  is a pole of ε^{-1} (L11), so it is not a separate particle species in the cascade. In RPA, its decay products are the cvk pairs of
  WP0 (7.2), evaluated at (p, ω).
- (b) **The secondary-pair distribution is the WP0 final-state-resolved response.** A generation-g carrier creates the pair
  Λ′ = (c′v′k′) with weight S^{RPA}(p,ω;Λ′)/S(p,ω), which is WP0 (7.2). The cascade is therefore the iterate of the WP0 interface (7.1)–(7.2).
- (c) **Polar materials.** The ionic part of the total ε gives LO-phonon emission (Fröhlich) through the same formula. To avoid double
  counting, the separate e–ph kernel must use only the short-range part g^S = g − g^L of the DFPT vertex. This is the EPW long-range
  split. The proof is WP0's three-channel argument (5.5): every Coulomb line at momentum transfer p is already resummed in ε^{-1}(p,ω).
- (d) **Exchange.** Replace |M_D|² by |M|² = ½(|M_D|² + |M_E|² + |M_D − M_E|²) (0812.2923 Eq. (5) [FT]). This correction is
  O(|M_E/M_D|) and matters only near threshold, where the final momenta are comparable. 0812.2923 also states that the BTE rate
  definition is ambiguous: its Eq. (1) and its Eq. (5) differ through Z_{kn} and W versus W_R (its Eq. (7)). That ambiguity is a genuine
  quasiparticle-picture uncertainty, of order the difference between Eqs. (1) and (8) of 0812.2923; it is listed as R1 in §9.
- (e) **Slow ions.** Take an ion of charge form factor Z_1(k) moving with velocity v. It has no recoil, so ω = k·v, and (W1) becomes
  Lindhard's dielectric stopping −dE/dx = (2Z_1²α/πv²) ∫dk/k ∫_0^{kv}dω ω L(k,ω). This holds only in Born, and the Born
  condition Z_1α/v ≪ 1 fails badly for keV recoils (Si at 1 keV: Z_1α/v ≈ 3×10²) [E]. See §3.3.

The phonon kernel is the EPW golden rule written in NOTATION conventions [D, at O(g²)]:

  Γ^{ph}_{nk→m,k+Q} = (2π/N_Q) Σ_ν |g^S_{mnν}(k,Q)|² [(n_{Qν}+1)δ(ε_{nk}−ε_{m,k+Q}−ω_{Qν}) + n_{Qν}δ(ε_{nk}−ε_{m,k+Q}+ω_{Qν})].        (W2)

### 1.2 The branching generating functional [D]
*Hypotheses.*
- (B1) Markov: collision durations are much shorter than the time between collisions (Γ ≪ the carrier energy scale); no inter-collision coherence.
- (B2) Siblings evolve independently. This is the dilute limit: no Pauli blocking or Coulomb interaction between cascade
  particles. A 1 keV deposit makes ~300 pairs within ~10 nm, so the pair density is ≲ 10¹⁹ cm⁻³ ≪ n_e [E].
- (B3) Homogeneous medium with no applied field. An NTL drift field adds a deterministic drift term.

*Statement.* A particle state x = (species a, band n, k, or ion energy and direction) evolves through channels c with kernels K_c(x → y_1…y_m), and
each channel deposits the observables δ𝐍_c, where 𝐍 = (N_eh, H = heat, E_st = stored defect energy, N_FP, E_esc, …). The generating functional is
G_x(s) = E[e^{s·𝐍} | x]. It obeys the backward equation

  Γ_x G_x(s) = Σ_c ∫dy K_c(x→y_1..y_m) e^{s·δ𝐍_c} Π_j G_{y_j}(s),   Γ_x = Σ_c ∫dy K_c,   G_x = e^{s·𝐍_term(x)} on absorbing states.     (W3)

The proof is first-step analysis of a Markov branching process: condition on the first collision and use (B2) to factorise. The kernels are
(W1) for e–e, (W2) for e–ph, and §3 for ions. A carrier is absorbing when it can no longer impact-ionize, i.e. its excess energy above
its band edge is below the ii threshold. Its remaining kinetic energy then goes to H.

*Moments.* With m_x ≡ ∂_sG_x|₀, the first moment obeys the linear equation Γ_x m_x = Σ_c∫K_c[δ𝐍_c + Σ_j m_{y_j}]. Second moments follow from
∂²_s. For one channel step this is the law of total variance (check C9). **Lindhard's integral equation (L20), the R&K mean yield
(L21) and Kinchin–Pease defect counts (L22) are first moments of (W3). F and F_NR (L23) are second moments** (§6).

*Exact energy bookkeeping [D].* Each vertex conserves energy. Assume terminal carriers relax to their band edges and pairs are counted at E_g (with an exciton, E_g → E_g − E_x; Si E_x ≈ 15 meV). Then

  ω = N_eh E_g + H + E_st + E_esc   (event by event),                                                                              (W4)

where E_esc covers photons and phonons that leave the target. Hence N_eh = (ω − H − E_st − E_esc)/E_g. **All ionization statistics are
heat-partition statistics** (§6, L23).

### 1.3 Seeding and the measured spectrum [D given WP0 (7.1)]
The prompt state Λ of WP0 (7.1) is a set of particles {y_j}: e, h, phonons with E_ph, a recoiling ion with momentum, a core hole. Then

  P_casc(𝐍|Λ) = [coefficient of e^{s·𝐍} in] e^{s·𝐍_prompt(Λ)} Π_{j∈Λ} G_{y_j}(s),                                                  (W5)

  dR/d𝐍 = (ρ_χ/m_χρ_T) ∫d³v f_χ(v) ∫d³q/(2π)³ Σ_Λ tr[𝔇(q,v) S(q, ω_q; Λ)] P_casc(𝐍|Λ).                                            (W6)

For an e–h seed, (B2) gives G_Λ = z G_{e}(ε_e,k_e) G_{h}(ε_h,k_h). This is the generating form of R&K Eq. (5). The DM tensor must be
traced **inside** the Λ sum, because different operators (density, spin, current) produce different (ε_e, ε_h, k_e, k_h) distributions.
The same holds for the q integral. This corrects WP0 (7.3); see §7.

### 1.4 Controlled reductions
- **(R-k) Energy-only reduction [D under the hypothesis; error stated].** Suppose momentum randomization is faster than energy loss,
  Γ_k ≫ Γ_E. This holds for e–ph above ~1 eV, where intervalley and acoustic scattering are quasi-elastic. Then G_{nk}(s) → G_a(ε; s) after the first
  collision, and the kernels average over iso-energy surfaces:
  K̄_a(ε→ε′) = D_a(ε)^{-1} Σ_{nk} δ(ε−ε_{nk}) K(nk→…). The error is O(Γ_E/Γ_k) per generation. **Only the first generation keeps the k (and
  hence q) memory.** That is where the DM-versus-photon seed difference enters.                                                     (W7)
- **(CSDA) Near-threshold ii probability [D].** Suppose the ii events are rare per unit energy loss and ω_ph ≪ E − E_th. Then a carrier at E_0 that has not yet impact-ionized loses energy at the rate
  P(E) = Σ_ν ω_ν Γ^{ph}_ν(E), and

  p_{no-ii}(E_0) = exp[ −∫_{E_th}^{E_0} dE Γ_ii(E)/P(E) ].                                                                        (W8)

  This is the controlling quantity for the 1e⁻/2e⁻ boundary. R&K's single ratio Γ_ph/Γ_eh (their Eq. (8)) is the free-particle evaluation of
  the integrand.

---
## 2. Hot carriers: closure of G1

**Formula.** (W1)+(W2) inside (W3), seeded by (W5)–(W6) from the DM S(q,ω;Λ). Temperature enters in three places: the Bose factors in (W2), the
(1−e^{−βω})^{-1} in (W1), and the T-renormalised bands (ZPR, L12). It does **not** enter only through E_g(T) (§6.2). Output: p_n(q,ω,T) ≡ P(N_eh = n | q, ω, T),
together with its moments ε_eh(q,ω,T) = ω/n̄ and F(q,ω,T).

**Computation specification (per material: Si, Ge, GaAs).**
- *Bands.* QE (PBE, norm-conserving or PAW) plus G0W0 (BerkeleyGW or Yambo). QP corrections are Wannier-interpolated up to ~15 eV above the CBM.
  Si needs 16–20 disentangled sp³d WFs; Ge and GaAs are similar, with SOC. Above ~15 eV use free-electron-like states with GW lifetimes. This is the
  regime where R&K's free-particle model is accurate (§6.2) and provides a matching check.
- *W(p,ω).* BerkeleyGW full-frequency ε^{-1}_{GG′}(p,ω), with ω ∈ [0, 60] eV (N_ω ≈ 200, denser below 20 eV), a p-mesh of 10³–12³ plus
  G-shifts, N_G ≈ 200–300 (cutoff 8–10 Ry), and ≥ 200 empty bands. Converge Im ε^{-1} at the plasmon (Si ~16.7 eV) to 2%.
  Use the total ε for GaAs (ionic part via DFPT Z*, ε_∞). Cost: 10⁴–10⁵ core-h per material [E].
- *ii kernel.* Evaluate (W1) with LFE and exchange per (d). Store it as K̄(ε → ε′; ε_e′, ε_h′), with the pair split resolved via WP0 (7.2) at
  (p, ω). Sample iso-energy surfaces with ~10³ k-points per 50 meV bin. Cost scales as N_ε × N_kiso × N_p × N_b′ ≈ 10³×10³×10⁴×20 matrix elements
  via FFT. That is 10⁴–10⁵ core-h [E].
- *e–ph kernel.* EPW with a coarse 8³/8³ grid, Wannier interpolation, and fine k 80³–100³ plus q 50³ by MC sampling. Use bands up to the WF
  window, T ∈ {0, 50, 100, 150, 300} K, g^S only for GaAs, and include quadrupole corrections (SOTA R2). Cost: ~10⁴ core-h [E].
- *Cascade solve.* Use (R-k) for generation ≥ 2: a 1D recursion in ε on a 10 meV grid, either by MC event generation or by deterministic moment
  equations. Cost is negligible. Generation 1 is fully k-resolved from S(q,ω;cvk), using WP1 outputs (RPA+LFE) and, for X+ seeds, the WP3 PAER
  pair distribution, with E_ph removed to H.
- *Grid of outputs.* ω ∈ [E_g, 50 eV] in 50 meV steps; |q| ∈ [0, 25 αm_e] with 3 directions plus the angular average; 5 temperatures.
  The 50 eV–keV range is handled by matching to the asymptotic (n̄ = ω/ε + b, Var = Fω/ε) (§6.4).
- *Validation (these are not fit parameters).*
  - Si quantum yield at 3–8 eV and 50–1500 eV (photon seeds, q ≈ 0; the data are cited in 2004.10709);
  - ε_eh = 3.749 ± 0.001 eV and F = 0.119 ± 0.002 at 5.9 keV and 123 K (2004.11499 [FT]);
  - Ge ε_eh(77 K).
  A photon seed (q ≈ 0) and a DM seed (q ~ 1–10 keV) from the same code give the G1 q-dependence directly.
- *Nuisances for WP6.* θ_W (the GW versus GW+vertex ii rate, ±20% [E]); θ_k (the error of the (R-k) reduction); θ_X (exchange on/off); θ_{Eg}
  (the ZPR band edge, from L12).

---
## 3. Nuclear recoil: the heat / defect / charge partition (closure of G3)

### 3.1 Hand-over from S_κκ [D]
The regimes are set by E_R = q²/2M_κ and x_R (WP0 (6.1)):
- **(i)** x_R ≲ 1 (E_R ≲ ω_max ≈ 60 meV in Si). The final states are few-phonon states in the G sector (WP2). The partition is trivial:
  P = δ(H − ω)δ_{N_eh,0}, with E_st = 0.
- **(ii)** x_R ≫ 1. In the impulse approximation (IA) the final-state-resolved response is

  S_κκ^{IA}(q,ω; p_I) = (2πN_κ/V) |F^M_κ|² n_κ(p_I − q) δ(ω − p_I²/2M_κ + (p_I − q)²/2M_κ),   ⟨p_x²⟩ = (M_κ/2)∫dω′ g_κ(ω′) ω′ coth(βω′/2).      (W9)

  This is the saddle point of the incoherent multiphonon sum (L5 → L6). Its Gaussian Doppler width σ_ω² = q²⟨p_x²⟩/M² = E_R⟨ω⟩ (T = 0,
  Einstein average; check C7) is the leading 1/x_R correction. **The MD initial condition is therefore fixed by the response:** one
  atom of species κ at a site, with lattice positions drawn from the harmonic Wigner distribution at T and momentum p_I = p_0 + q, p_0 ~ n_κ.
  This reproduces S_κκ's energy distribution to O(1/x_R). Its correction is the quantum/classical difference of the final vibrational state.
- *Size.* For Si at E_R = 10 eV (20 eV), the Doppler spread is σ_ω ≈ 0.67 eV (0.95 eV) [E]. So the struck atom's kinetic energy is smeared by ~1 eV
  around E_d. This smearing is predicted, not tuned.
- *No double counting with Migdal.* WP0 Theorem D splits the DM vertex: G-sector seeds (no electronic excitation) go to (W9). X-sector
  (Migdal) seeds add prompt e–h pairs (WP3) and a recoil. The WP5 transport starts **after** the vertex. A "U" that "effectively incorporates
  the Migdal effect" (2209.04503 [FT]) double counts if a WP3 Migdal rate is also added.

### 3.2 Dynamics on the BO surface [D for the regime boundaries; E for the numbers]
- **(iii)** E_R ≈ 0.3 eV–E_d. The trajectory runs on V_BO. It is anharmonic: the displacement amplitude in Si is u ≈ √(2E_R/Mω²) ≈ 0.38 Å at 1 eV against a 2.35 Å bond [E].
  The motion is classical: λ_dB(20 eV, Si) ≈ 0.012 Å. It is adiabatic: the Massey parameter ξ = E_g a/v ≈ 15 at 20 eV (check C6), so
  non-adiabatic loss is ~e^{−ξ}. **BO-MD is controlled here.** Everything goes to H, except a stored energy when E_R ≥ E_d.
- **Displacement threshold (definition).** Let 𝔅₀ be the basin of the perfect crystal on V_BO and Φ_t the dissipative flow (dynamics plus bath). Then

  P_FP(E,Ω̂) = Pr_{R_0∼Wigner}[ lim_{t→∞} Φ_t(R_0, √(2ME)Ω̂) ∉ 𝔅₀ ],   E_d(Ω̂) ≡ E such that P_FP = ½.                                   (W10)

  It is a smooth step whose width comes from the zero-point and thermal R_0 and from (W9). The step model is its zero-width limit.
- **Stored energy.** E_st = V_BO(R_final) − V_BO(R_0), evaluated at t_pr ≈ 10–100 ps, after prompt recombination and before thermally activated annealing (§4).
  The defect content of R_final is a vacancy–interstitial pair, a close pair or an amorphous pocket. **E_st ≠ E_d.** E_d is a dynamical
  (kinetic) threshold. E_st is a thermodynamic formation energy, ~E_f(V) + E_f(I) for a separated pair (Si ≈ 7–9 eV, Ge ≈ 5–7 eV from
  DFT literature values quoted from memory [E]). The rest, E_d − E_st, is heat.

### 3.3 Electronic excitation by the recoil (the charge channel) [D for the threshold logic; E for the numbers]
- **Kinematic threshold.** A binary collision between a slow ion (v ≪ v_F) and a valence electron transfers at most 2m_ev(v + v_F). A
  pair needs E_g, so v_th ≈ E_g/(2m_ev_F). With free-electron v_F (check C5): **E_R,th ≈ 375 eV (Si), 465 eV (Ge)** [E]. The
  band-structure version replaces the Fermi sphere by the support of L(k,ω) (Theorem C(e)). Below E_R,th the linear-response
  electronic stopping in a gapped crystal vanishes. A friction model F = −S_e(E)v̂ (2506.03810 Eq. (3) [FT], SRIM S_e) assigns electronic
  energy loss that has no final state there.
- **What creates pairs below E_R,th.** Non-adiabatic transitions in close collisions, where the local gap of the distorted configuration closes
  (quasi-molecular promotion). These are the X-sector couplings of Theorem D at strong coupling. Per crossing they follow Landau–Zener,
  P = exp(−2πH_12²/(v|ΔF|)). Both the Massey parameter (ξ ≈ 2 at 1 keV) and Z_1α/v ≫ 1 say that **linear-response (Lindhard–Scharff)
  stopping is not a derived limit at E_R ≲ few keV**. It is a fit.
- *Data.* The Ge measurement of QF = 25 ± 3% at 254 eV_nr (2405.10405 [ABS]) lies below the binary threshold. If it is confirmed, this channel must
  dominate there [E].
- **Charge from the electronic deposit.** The electronic excitation spectrum dP/dω_e produced along the trajectory seeds the §2 cascade. Slow-ion
  excitations are near-gap, so **N̄_eh ≠ η̄/ε_γ**: the conversion uses p_n at the NR seed spectrum, not the photon asymptote (§6.1, L20 correction).

### 3.4 Computation specification for G3
- **PES.** DFT (QE or VASP; PBE and SCAN for spread), joined to ZBL/DMol at r < 1 Å. Train an MLIP (ACE, MACE or NequIP) on ~10⁴ configurations: dimers down to
  0.5 Å, point defects, close pairs, amorphous and liquid, plus the recoil snapshots. Force error ≤ 50 meV/Å; energy ≤ 3 meV/atom.
- **E_d(Ω̂) and P_FP.** Use ~300 directions in the irreducible wedge × 20 Wigner R_0 samples, bisecting to 0.5 eV, in cells of 4096–8000 atoms
  for 3–5 ps with a 0.1 fs step near close approach and a boundary thermostat. That is ~3×10⁴ MLIP runs, ~10³ GPU-h. Check 20 directions with
  BO-DFT-MD (512 atoms, ~10⁵ core-h).
- **Partition tables.** E_R ∈ [1 eV, 10 keV] (40 log points) × 100 directions × 100 seeds from (W9). Cells range from 10³ atoms (< 100 eV) to 10⁵ atoms (10 keV),
  run for 1–10 ps. Record H, E_st (by quench to 0 K at t_pr), and defect labels. Cost: 10⁴–10⁵ GPU-h.
- **Electronic channel.** Real-time TDDFT Ehrenfest or surface hopping (Qb@ll, Octopus, SALMON) for Si–Si and Ge–Ge close collisions.
  Use E_rel = 50 eV–5 keV, impact parameters 0–1.5 Å, 64–216-atom cells and 20–50 trajectories per energy. Output the **distribution** dP/dω_e(b, E_rel),
  not only S_e. Cost ~10⁶ core-h. Attach it to the MLIP-MD as stochastic excitation events, and feed the excitations into §2.
- **Outputs.** P(H, E_st, N_eh | E_R, Ω̂, T) and its moments, the anisotropic E_d surface and the heat-quenching Q_h(E_R, Ω̂) of (W11).

  Q_h ≡ ⟨H_meas⟩/E_R = 1 − ⟨E_st⟩/E_R − ⟨E_esc⟩/E_R − ⟨N_trap⟩E_g/E_R   (zero field; + N_eh eV_b/E_R in NTL mode).                        (W11)

  (W11) follows from (W4). Unit heat quenching (2007.14289 [FT]) is the truncation E_st = E_esc = N_trap = 0.

---
## 4. Defects, annealing and stored energy as a background model (G12)

**Formula [D, under harmonic TST and Markov hopping].** Defect configurations i have energies V_i on V_BO and transition rates k_ij(T). The
populations n_i(t) are seeded by recoils (§3: DM, radiogenic, cosmogenic; source S_i(t)) and by the post-cooldown state, and obey

  dn_i/dt = S_i(t) + Σ_j [k_ji n_j − k_ij n_i],   R_rel(E,t) = Σ_{ij} k_ij(T) n_i(t) δ(E − (V_i − V_j)) ⊗ (detector response).      (W12)

The rates are:
- above the crossover T_c = ω_b/2π: k_ij = (Π ω_i^{(min)}/Π ω^{(TS)}) e^{−E_b/T}/(2π) (Vineyard);
- below T_c: instanton tunnelling k ∝ e^{−S_inst}.
For an Si interstitial-like barrier with ω_b ~ 2π×10 THz, T_c ≈ 75 K [E]. **At mK, annealing is tunnelling or triggered
(avalanche: 2408.07518 [ABS] finds that crossing low barriers triggers larger releases). Classical TST predicts no events there.**
- **Time dependence [D].** For a barrier density g(E_b) that is flat over the active range, Σ k e^{−kt} → g T (1−e^{−νt})/t ∝ 1/t (check C8).
  This gives a generic 1/t decay after cooldown or irradiation. Exponential decays need a narrow barrier set. The 1/t law has also been
  proposed for dislocation relaxation (2406.15425 [ABS]), so the time law alone does not discriminate between the two.
- **Energy spectrum [C].** The observed ∝ e^{−αE} (2408.07518 reports that simulations reproduce it) is not derived here. A maximum-entropy
  release distribution at fixed mean ⟨V_i − V_j⟩ would give it, but that is a conjecture.
- **Computation specification.**
  - *Barriers.* Climbing-image NEB on the §3.4 MLIP, starting from the quenched §3 end states; validate 50 barriers against DFT.
  - *Kinetics.* Rate catalogue by on-the-fly kinetic MC; instanton rates (ring-polymer) for the 10² most frequent hops below T_c.
  - *Seeds.* E_R spectra of cosmogenic neutrons and radiogenic recoils as S_i.
  - *Output.* R_rel(E, t, T) with nuisances for the barrier spread and the MLIP error.
  - *Cost.* ~10⁴ GPU-h.
- **Exact remaining gap (G12).** The triggered-avalanche statistics at T ≪ T_c needs a non-Markov treatment of strain and phonon pulses. This is R4 (§9).
- **DFT-level defect creation by ER (catalog gap 5).** The carriers of §2 are not energetic enough to displace atoms: the maximum transfer from a
  10 eV electron to Si is 4m_eE/M ≈ 1.5 meV ≪ E_d. ER defect creation therefore needs electronic-excitation-driven bond breaking
  (self-trapped excitons or core-hole Auger). In Si this is absent at eV scale [E]. It is candidate-dependent for ionic targets (NaI, LiF: colour centres; WP4).

---
## 5. Quasiparticle yield in superconductors
**Formula [D under (B1)–(B3)].** (W3) with species {hot e (ω ≫ Δ), QP(E), phonon Ω > 2Δ, phonon Ω < 2Δ (loss), escaping phonon}.
- *Seed.* S(q,ω;Λ) on the BCS reference state (L15, WP4). For ω ≫ Δ (every m_χ ≳ 100 keV) the seed is a normal-state hot e–h pair, and
  (W1) applies unchanged. That includes the Al plasmon (~15 eV).
- *Kernels.* Near Δ: Eliashberg α²F(Ω) with coherence factors. Phonons are case I (density-like), so QP scattering carries
  (1 − Δ²/EE′) and pair breaking or recombination carries (1 + Δ²/EE′). Photon pair breaking carries (1 − Δ²/EE′) (1401.1937 Eq. (1) [FT]).
  **The DM density vertex is case I.** So for ω ≈ 2Δ–3Δ the DM seed's (E,E′) split differs from the photon calibration. This is a
  q-dependence analogous to G1 [D for the sign structure; the screened density vertex at q ≲ 1/ξ goes to WP4].
- *Exact bookkeeping (as W4).* ω = N_qp Δ + E_sub + E_excess + E_esc, so

  η ≡ Δ⟨N_qp⟩/ω = 1 − ⟨E_sub + E_excess + E_esc⟩/ω,   F_qp = Var(E_sub + E_excess + E_esc)/(Δ²⟨N_qp⟩).                             (W13)

- *Limits.*
  - For ω < 3Δ there is no cascade: N_qp = 2 and η = 2Δ/ω.
  - For ω ≫ Ω_D in a bulk absorber, η → 0.57–0.6 (the infinite-volume results quoted in 1401.1937 [FT]).
  - The late-time Rothwarf–Taylor stage (1401.1937 Eqs. (2)–(5) [FT]) is the coarse-grained two-species version of (W3). Its
    phonon-trapping factor 1/(τ_l/τ_pb + 1) is the E_esc term of (W13).
- *Specification.*
  - *Inputs.* DFPT α²F (QE/EPW) for Al, Nb, Ta, plus measured α²F as a check; Δ(T); film thickness d and the phonon escape time τ_l(d).
  - *Solve.* Chang–Scalapino kinetic equations as the mean-field closure of (W3), plus event MC for F_qp.
  - *Grids.* E on a 1 μeV grid near Δ, 0.1 meV up to Ω_D, (W1) above.
  - *Output.* η(ω, d, T) and F_qp.

---
## 6. LIMITS entries derived

### 6.1 L20: Lindhard quenching (and the modified Lindhard 2209.04503)
- **Source [FT].** 2001.06503 Eq. (3): ∫dσ_{n,e}[φ̄(E−T_n−ΣT_ei) + φ̄(T_n−U) − φ̄(E) + Σ_iφ̄_e(T_ei−U_ei)] = 0. With approximations (A)–(E),
  this becomes Eq. (5): k ε^{1/2} ν̄′(ε) = ∫_0^{ε²}dt f(t^{1/2})/(2t^{3/2}) [ν̄(ε−t/ε) + ν̄(t/ε) − ν̄(ε)], with S_e = kε^{1/2}, k = 0.133Z^{2/3}A^{-1/2}
  (Eq. (4)). The solution is Eq. (7): ν̄_L = ε/(1+kg(ε)), g = 3ε^{0.15} + 0.7ε^{0.6} + ε, and f_n = (ε − ν̄)/ε (Eq. (6)).
  2209.04503 adds the binding U(E), the second-order term and electronic straggling W(ε) in Eq. (2):
  −½εS_e(1 + W/(S_eε))ν̄″ + S_eν̄′ = ∫_{εu}^{ε²}dt f(t^{1/2})/(2t^{3/2})[ν̄(ε−t/ε) + ν̄(t/ε−u) − ν̄(ε)], with U = U_FP + U_EDFT(E) (Eq. (3)).
- **URF chain.**
  1. WP0 (3.4), G sector, K = imp → recoil seed (W9).
  2. (W3), ion species, observable ν = H + E_st (+ the internal excitation energy U).
  3. First moment = 2001.06503 Eq. (3) exactly, with dσ_n = classical scattering on V_BO and dσ_e = the §3.3 non-adiabatic excitation kernel [D].
  4. Truncations:
     - (I/A) drop recoils generated by electrons (exact below the §4 4m_eE/M bound);
     - (II–IV/C–E) small fractional transfers;
     - (D) nuclear and electronic channels independent;
     - V_BO → a universal screened pair potential (TF or ZBL; the crystal becomes an amorphous random medium: no channeling, no anisotropy);
     - dσ_e → Born free-electron-gas stopping ∝ v (Theorem C(e)), times Lindhard's hand-inserted Z^{1/6} (2209.04503 [FT] states this);
     - (B/V) U = 0 (Lindhard), or U = U_FP + U_EDFT (2209.04503);
     - charge yield N_eh = η̄/ε_γ.
- **Validity.**
  - Born stopping needs Z_1α/v ≪ 1. That fails for all keV recoils (≈ 3×10² at 1 keV Si) [E], so S_e ∝ v is an empirical scaling there.
  - Binary electronic excitation needs E_R ≳ 375 eV (Si) or 465 eV (Ge) [E, C5].
  - The amorphous-medium step needs recoil ranges ≫ the lattice constant and no channeling.
  - The quoted empirical validity is ε ≳ 0.1 (≈ 4 keV) for Si and ε ≳ 0.00088 (≈ 250 eV) for Ge (2001.06503 [FT]).
  - The modified model fits 680 eV–3 MeV Si data with χ²/dof = 1870/101 (2209.04503 [FT]).
- **Leading URF corrections.**
  - (a) **The gap threshold.** Below E_R,th the electronic deposit comes only from close-collision (Landau–Zener) promotion, so a non-zero QF
    below ~0.4 keV measures that channel. This is a sign-definite modification: the binary channel switches off.
  - (b) **Seed-spectrum conversion.** N̄_eh = Σ_ω_e (dP/dω_e) n̄(ω_e) ≠ η̄/ε_γ. Near-gap excitations give n̄ ≈ 1 per excitation, against ω_e/3.75 eV
    for the photon conversion.
  - (c) Crystal anisotropy and channeling: directional QF.
  - (d) U computed as ⟨E_st⟩ (§3.2) instead of fitted.
- **Discrepancies.**
  - (1) *Reduced energy.* 2001.06503 uses Lindhard's a = 0.8853a₀/(√2 Z^{1/3}) (ε/E = 0.0243 keV⁻¹ for Si). 2209.04503 uses ZBL a with
    C = 16.2616/(Z Z_1Z_2) and Z_1 = 12 for a stripped Si ion (0.0268 keV⁻¹). The same E therefore maps to an ε that differs by 10% (check C10).
    Fitted parameters cannot be transferred between the two papers.
  - (2) 2001.06503 notes an internal inconsistency of Lindhard's boundary condition: ν̄′(0) → 1 is imposed, while Eq. (5) implies ν̄′(0) → 0.
  - (3) The second-order coefficient ½εS_e of 2209.04503 Eq. (2) requires ∫dσ_{n,e}T_nΣT_e → ½εS_e. That identification is not derived in the text, and
    we could not reproduce it. The straggling coefficient ½W is consistent with the stated expansion.
  - (4) 2506.03810 (MD) stops at 10 eV_nr "as no ionization occurs below this threshold" while using SRIM friction above it. Our C5 threshold,
    ~375 eV, is 40× higher for binary excitation. So their sub-keV ionization is a property of the friction model, not of a final-state channel [E].

### 6.2 L21: Ramanathan–Kurinsky ionization model; step model
- **Source [FT, 2004.10709].**
  - Eq. (5): n(E_r) = 1 + ∫_0^{E_r−E_g}dE P(E,E_r)⟨N(E)⟩.
  - Eq. (6): the e/h symmetry P(E,E_r) = P(E_r−E_g−E, E_r).
  - Eq. (7): a Beta P(x|α), fitted to photon ε_eh data at 3–8 eV.
  - Eq. (8): Γ_ph/Γ_eh = A(105/2π)(E−ω_0)^{1/2}/(E−E_g)^{7/2}.
  - Eq. (9): A = (|M_ph|/|M_eh|)(4π⁴/VΔ)(ħ²/2m)³, with A = 5.2 "eV²".
  - Eq. (10): p_eh = [1 + Γ_ph/Γ_eh]^{-1}.
  - Eq. (11): E_g(T) = E_g(0) − aT²/(T+b) as the only T dependence.
  - Plasmons: n_pl = ⌊(E_r−E_g)/ω_pl⌋.
  - The step model Q = 1 + ⌊(ω−E_g)/ε⌋ (with ε = 3.6–3.8 eV for Si and 2.9 eV for Ge) appears in the survey (2105.05253, 2603.12326).
- **URF chain.** (W6) → (W5) with an e–h seed → (W3) first moment. Then:
  1. q-marginalise the seed **and** replace S(q,ω;cvk) by a photon (q ≈ 0) fit. This is not a marginalisation of the DM seed; see §7.
  2. Use (R-k) (W7) from generation 1.
  3. Impose e/h symmetry: N̄_e = N̄_h. The URF keeps them separate, and the hole bandwidth (W ≈ 12 eV) emerges from the band structure.
  4. (W1) → constant |M_eh|² with momentum conservation dropped ("random-k"), free parabolic DOS ∝ √E, vacuum mass. The three-body phase space is then
     Γ(3/2)³/Γ(9/2)(E−E_g)^{7/2} = (2π/105)(E−E_g)^{7/2} (check C1). This is the origin of 105/2π. The threshold moves from E_th ≈ 1.1–1.5E_g to E_g.
  5. (W2) → one Einstein mode ω_0 = 63 meV with constant |g|², at T = 0. This gives Γ_ph ∝ (E−ω_0)^{1/2}. The ratio is R&K Eq. (8) [D].
  6. Plasmons: an explicit fixed-energy plasmon channel added on top of (4) double counts with the RPA ii channel (Theorem C(a)). R&K find no effect,
     which is consistent with this.
  7. The step model is the deterministic limit P_casc(N|Λ) → δ_{N,N_step(ω)}, so F = 0.
- **Validity.**
  - The free-particle steps (4)–(5) need E − E_g ≫ the band-structure scale (E_dir − E_g ≈ 2.2 eV in Si; the L/X valley spacing in Ge). In practice that is E ≳ 10–15 eV [E].
  - The Beta seed is valid only for photon kinematics, by construction.
  - The step model fails whenever √(F n̄) ≳ ½, i.e. n̄ ≳ 1/(4F) ≈ 2 for Si (F ≈ 0.12). So it is never accurate beyond the forced region ω < 2E_g [E].
  - The step model's mean, averaged over the fractional part, is (ω−E_g)/ε + ½. The asymptotic URF mean is ω/ε + b. They agree only if
    b = ½ − E_g/ε ≈ 0.19 (Si) [E].
- **Leading URF corrections.**
  - (a) **q-dependence of the seed.** The first generation is k-resolved. The size is bounded by R&K's own envelope between α = 0 and α → ∞
    (up to ~50% in p_2 at 4–8 eV, 2004.10709 [FT]).
  - (b) Temperature beyond E_g(T): phonon absorption n_Q, T-dependent ZPR band shapes, and the factor (1−e^{−βω})^{-1} in (W1).
    The ii threshold region is where Γ_ph(T) matters, through (W8).
  - (c) X+ (PAER) seeds remove E_ph into H at the vertex.
  - (d) Exchange (Theorem C(d)).
- **Discrepancies.**
  - (1) *Units of A.* Eq. (8) is dimensionless only if [A] = energy³. A = 5.2 "eV²" is therefore inconsistent with Eq. (8) as written (check C1c).
  - (2) *Golden rule.* Eq. (9) has |M_ph|/|M_eh|; the golden rule gives |M_ph|²/|M_eh|². Δ is undefined as a real- or k-space volume.
  - (3) *Symbol collision.* E_r means "recoil energy" in Eqs. (2)–(5) and "phonon losses" in Eqs. (15)–(16).
  - (4) *App. A, Eqs. (22)–(23).* These write Var = Fn + η(1−η)n. Binomial thinning gives Var = η²Fn + η(1−η)n exactly, so
    **F_meas = ηF + 1 − η, not F/η + 1 − η** (check C2). The text's 0.130/0.160 at η = 0.98/0.95 are close to the exact 0.133/0.159.
    Eq. (23) gives 0.137/0.171. The stated "lower bound" claim has the inequality the wrong way round.

### 6.3 L22: displacement threshold and defect energy loss
- **Source [FT].**
  - 1805.09942 Eq. (1): Ê = E(1 − f). Eq. (4): f_DF = 1 − (1−f)/(1−f_sur) = (6.08 ± 0.18)% at 103 keV ²⁰⁶Pb in Ge. TRIM maps this to E_d = 19.7^{+0.6}_{−0.5} eV,
    with "TRIM predicts a monotonic, decreasing relationship between the percent energy lost to defects … and E_d".
  - 2301.06592 Eq. (8): R(t) = ∫_{4π}∫_{E_th(θ,φ)} d²R/dE_rdΩ_r, with E_th(θ,φ) taken from the MD E_d surface (17.5–77.5 eV in Si).
- **URF chain.**
  1. Seed (W9).
  2. (W3), ion species, first moment of E_st and N_FP.
  3. E_d from (W10) on V_BO.
  4. Truncations:
     - V_BO → empirical potentials (SW, Tersoff; the source of the reported 7–30 eV Ge spread);
     - drop the R_0 sampling (zero-point/thermal) and the IA Doppler spread, which turns the step sharp;
     - NRT/Kinchin–Pease counting N_d ≈ 0.8T_dam/2E_d, with stored energy per defect ε_st, so f ≈ ξ_surv·0.4(T_dam/E_R)ε_st/E_d [E].
       This reproduces TRIM's decreasing f(E_d) at fixed ε_st.
  5. 2301.06592's additional assumption, ionization threshold = E_d, is **not** a URF limit. The ionization threshold is the §3.3 kinematic or
     Landau–Zener threshold. In a calorimeter E_d produces a heat **deficit** E_st, not a threshold (W11).
- **Validity.** The BO-MD step is controlled at E_R ~ E_d: Massey ξ ≈ 15, λ_dB ≈ 0.01 Å (C6), with no electronic excitation (C5). The empirical potential is
  the dominant error. The thermal and zero-point step width is ~1 eV (C7).
- **Leading URF corrections.**
  - (a) A smooth P_FP(E,Ω̂) with width σ ≈ √(E_d⟨ω⟩) ≈ 1 eV (Si).
  - (b) Anisotropic E_st(E_R,Ω̂). This gives a daily modulation of the **heat** response near E_d, in addition to the modulation of the ionization threshold.
  - (c) Amorphous-pocket stored energy beyond isolated Frenkel pairs (2408.07518), which also seeds §4.
  - (d) Post-cascade annealing makes f time-dependent.
- **Discrepancies.**
  - (1) 1805.09942's E_d depends on TRIM's internal stored energy per displacement, which is not stated. The measured quantity is ⟨E_st⟩/E,
    and its physical carrier is the formation energy, not E_d.
  - (2) 2301.06592 Eq. (6) writes v_min = √(2m_nE_r)/(2μ_{m_D−N}). Here m_n must be the nucleus mass, while the same symbol labels the nucleon in μ_{m_D−n} (Eq. (5)).
  - (3) Taking the ionization threshold equal to E_d (2301.06592) conflicts with Si QF data that are non-zero down to ~0.7 keV but not with a
    threshold at E_d. In the URF the two thresholds are physically distinct.

### 6.4 L23: Fano factor F and ε_eh
- **Source [FT].** 2004.10709 Eq. (3): F = σ²/n_eh = σ²ε_eh/E_r (Fano's definition). Eq. (16): ε_eh = C·E_g + E_r, with C ≈ 2.2–2.9
  (the Klein form). Measurements at 5.9 keV and 123 K: F = 0.119 ± 0.002, ε_eh = 3.749 eV (2004.11499 [FT]). The model value is F_∞ = 0.115 (2004.10709 [FT]).
- **URF chain.** Second moment of (W3) with an e–h seed. With (W4) and E_st = E_esc = 0:

  F = Var(H)/(E_g² n̄) = (ε/E_g − 1)·D,   D ≡ Var(H)/(E_g⟨H⟩),   ε = E_g + ⟨H⟩/n̄   [D, exact given (W4); check C3].            (W14)

  **F and ε are the first two moments of the heat partition.** Truncations:
  - (i) The Klein limit: no phonon loss during ii, and residual KE uniform in k with a √E DOS below E_th = (3/2)E_g (parabolic, equal masses).
    This gives ε = E_g + 2·(3/5)E_th = (14/5)E_g (C4), i.e. Eq. (16) with C = 2.8. The phonon term rω_0 is the "E_r" of Eq. (16).
  - (ii) Independent residuals would give F = 54/175 ≈ 0.31 (C4), 2.6× the data. **The energy constraint and the anti-correlation between
    sibling residuals are the leading physics of F.** They are not a small correction.
  - (iii) A phonon shot-noise estimate, Var(H) ≈ ω_0⟨H⟩, gives F ≈ (ε/E_g − 1)ω_0/E_g. This is 0.121 for Si (ω_0 = 63 meV, E_g = 1.16 eV at 123 K)
    and 0.155 for Ge (ω_0 = 37 meV) [E]. The Si agreement may be accidental. The Ge reference values, ~0.11–0.13, are quoted from memory and not verified here.
- **The asymptotics, and why F is a moment rather than a parameter [D, renewal theorem for (W3) with (R-k)].** n̄(ω) = ω/ε + b + o(1) and Var N =
  Fω/ε + O(1). Both ε and F are computable functionals of the kernels (W1)–(W2). Near threshold F(ω) is not constant: it is 0 for ω < 2E_g,
  and its structure is set by (W8).
- **Nuclear-recoil Fano [D under conditional independence of the cascade given η].** F_NR = F_ER(η̄) + Var(η)/(ε η̄). At 25 keV in Si,
  Lindhard gives η̄ ≈ 9.1 keV. F_NR ≈ 24 (2206.13639 [ABS]) then requires σ_η/η̄ ≈ 10% [E]. That is the second moment of the Lindhard
  partition, a computable target for §3.4.
- **Validity.** (W14) needs carriers to thermalise at the band edges with no trapping before counting, no photon escape, and E_st = 0 (ER). The
  asymptotics need ω ≳ 50 eV.
- **Leading URF correction.** The finite-ω structure F(ω) from (W8). Then measurement thinning, F_meas = ηF + 1 − η (C2), which corrects R&K App. A.
  Then trapping (N_trap) and exciton or luminescence escape via (W4).
- **Discrepancies.** As in §6.2(4). Also, the R&K model F ≈ 0.115 sits below the skipper-CCD value of 0.119 ± 0.002. With exact thinning, η ≈ 0.995
  would reconcile them [E].

---
## 7. WP0 defects
1. **WP0 (7.3), second formula.** dR/dN_eh = ∫dω (dR/dω) P(N_eh|q,ω) integrates out q before seeding. That loses the q-dependence that (7.2) was
   introduced to keep, and it is ill-defined because P depends on q. Replace it by (W6), with the q integral and the 𝔇 trace inside the Λ sum.
2. **WP0 (7.3), first formula.** P(N_eh|q,ω) = Σ_Λ S(q,ω;Λ)P_casc/S holds for a single operator only. For several operators the weight must be
   tr[𝔇S(q,ω;Λ)]/tr[𝔇S(q,ω)], because spin and current operators populate (ε_e, ε_h, k) differently.
3. **WP0 (7.1).** It lists "plasmon/collective" as a prompt final state with branching B(Λ_eh|pl), next to e–h states drawn from S^{RPA}(q,ω;cvk), (7.2).
   In RPA the plasmon's decay products are already the cvk pairs, because the screened vertex includes the pole. Feeding both into the
   cascade double counts. Within RPA, Λ must be cvk only. A separate plasmon label is needed only beyond RPA, or when the collective mode can
   escape or convert to non-pair channels (films, WP4).
4. **WP0 (7.3), last sentence.** It calls R&K the Λ-marginalised kernel. R&K's seed is a photon (q ≈ 0) fit, not the marginal of the DM
   S(q,ω;Λ) (§6.2, step 1).

---
## 8. Uncertainty hand-over (WP6)
These follow the WP0 (8.1) increments:
- θ_seed: photon versus DM seed, computed as a difference;
- θ_k: (R-k) against a k-resolved generation 2 on a subset;
- θ_W: the GW versus vertex-corrected ii rate;
- θ_X: exchange;
- θ_PES: the spread between MLIP, empirical and DFT E_d and E_st;
- θ_LZ: the TDDFT functional for the Landau–Zener channel;
- θ_esc: escape and trapping.

Two exact constraints restrict them. (W4) ties θ_W, θ_k to ε and F: the measured ε and F at 5.9 keV constrain the linear combination of
θ_W and θ_k. (W13) does the same for η.

---
## 9. Exact remaining gaps
- **R1.** The quasiparticle (BTE) definition of the ii rate near threshold, where 0812.2923 Eq. (1) and Eq. (5) differ. An NEGF/Kadanoff–Baym treatment of the
  three-QP final state would settle it. The size is |Eq.(1) − Eq.(8)|/Eq.(1) of 0812.2923, through Z_{kn} and W versus W_R.
- **R2.** The (R-k) error O(Γ_E/Γ_k) has no proven bound below ~1 eV above threshold, which is where p_2 is decided.
- **R3.** The close-collision excitation kernel dP/dω_e(b, E_rel) relies on adiabatic-XC TDDFT, whose gap and level-crossing errors are uncontrolled. G3's charge channel
  below E_R,th rests on it.
- **R4.** Triggered (avalanche) annealing at T ≪ T_c, and the e^{−αE} spectrum, are [C].
- **R5.** The case-I DM density vertex for ω ≈ 2Δ–3Δ at q ≲ 1/ξ needs WP4's gauge-invariant screened BCS response.
- **R6.** Excitons (E_x), shallow-dopant trapping and indirect-gap luminescence escape enter (W4) and (W11). They are not computed here.

## 10. Literature (all IDs verified against the arXiv API, 2026-10-31)
- Full text read: 2004.10709 (R&K, Eqs. (1)–(23)); 2209.04503 (Eqs. (1)–(4)); 2001.06503 (Eqs. (1)–(22)); 1805.09942 (Eqs. (1)–(4), §V);
  2301.06592 (Eqs. (1)–(8)); 0812.2923 (Eqs. (1)–(9)); 1401.1937 (Eqs. (1)–(5)); 2506.03810 (Eqs. (3)–(4)); 2004.11499 (results).
- Abstract or title check only: 2408.07518, 1703.05371, 2603.16702, 2405.10405, 2206.13639, 2112.14495, 2210.01557, 2007.14289, 2503.03683,
  2406.15425, 2104.01811, 2101.08263, 2002.06937, 2003.12077, 2306.14944.
- Not on arXiv (cited by content only): Lindhard et al. 1963; Fano 1947; Klein 1968; Kaplan et al. 1976; Chang–Scalapino.
- PDFs deleted after reading (brief). The HTML and text extracts are kept in literature/papers-WP5/.
