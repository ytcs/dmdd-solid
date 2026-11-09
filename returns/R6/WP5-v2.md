# R6 / WP5-v2: energy partition and measured quanta (corrected standalone version)

Revision agent, brief R6/REV-WP5. Supersedes returns/R5/WP5.md (v1), which stays as the historical record; this version reads without it.
Conventions: CONVENTIONS.md; symbols: NOTATION v4; architecture: returns/R6/WP0-v2.md, cited **WP0-v2 (s.n)** with v2 numbers. Owed
corrections: state/CORRECTIONS.md §0, §11, WP0-v2 flags F2, F3, F6, F8, F11; closing table §12. Checks: `code/WP5-v2/checks.py` (sympy only,
exact arithmetic, 37 checks, all PASS, ~3 s), cited **WP5v2-Cn** (v1's C1–C10 keep their content; C11–C20 are new). Tags: **[D]** DERIVED
(hypotheses stated), **[D, sketch]**, **[E]** ESTIMATED, **[C]** CONJECTURED; literature **[FT]** full text, **[ABS]** abstract,
**[UNVERIFIED]** quoted from memory. This return's equations are **WP5 (W1)…(W15)**; (W1)–(W14) keep v1's objects and numbers, (W15) is new.
Units: ħ = c = k_B = 1, e² = 4πα, v_C(k) = e²/k². Status: CLAIMED (v1 R5 content), pending R×2.

---
## 1. The partition-transport stage of the URF

### 1.1 Theorem C: every cascade kernel is a master-formula rate with a target-internal projectile [D]
*Hypotheses.* First order in the screened interaction W^{scr} (GW level). The projectile is a quasiparticle of the target (a Bloch electron
or hole in state nk, or a moving ion), distinguishable from the medium's response (exchange: item (d)).
*Statement.* Use WP0-v2 (3.3) with the DM replaced by the projectile. A Bloch carrier couples to the **total** charge, so its coupling vector
is |c⟩ ∝ |z⟩ (CONVENTIONS §7) and its response is S_cc (written S_zz in WP0-v2 (5.4)). Its vertex is 𝒱(p) = v_C(p) ρ_{n′n}(k,−p), where
p = q_r + G is an unrestricted loop momentum (NOTATION §B) and the carrier goes nk → n′, k−p. WP0-v2 (5.4) then gives

  Γ_{nk→n′,k−p} = ∫d³p/(2π)³ |v_C(p) ρ_{n′n}(k,−p)|² S_cc(p, ω) [1 − f_{n′,k−p}],   ω = ε_{nk} − ε_{n′,k−p},
  ⇒ Γ_{nk} = Σ_{n′} ∫d³p/(2π)³ 2 v_C(p) |ρ_{n′n}(k,−p)|² Im[−(ε^{-1})_{00}(p,ω)] [1 − f_{n′,k−p}]/(1 − e^{−βω}).               (W1)

(W1) is 2|Im Σ^{GW}_{nk}| in head-only form, since S_cc = (2p²/e²)L/(1 − e^{−βω}) gives |𝒱|²S_cc = 2v_C(p)|ρ|²L/(1 − e^{−βω}) (WP5v2-C13).
With local fields it becomes Σ_{GG′}ρ*_G v_C(p+G) Im(−ε^{-1}_{GG′}) ρ_{G′}, which is 0812.2923 Eqs. (1)–(2) [FT], τ^{-1} = (2Z/ħ)|ImΣ| (source
notation: Z = quasiparticle residue, Gaussian units).
**Consequences:**
- (a) **Impact ionization, plasmon emission and plasmon decay are a single channel**, the e–h part of Im[−1/ε]. The plasmon is a pole of
  ε^{-1} (L11), not a separate cascade species. In RPA its decay products are the cvk pairs of WP0-v2 (7.2) at (p, ω). (Adopted by WP0-v2
  (7.1) and CONVENTIONS §13 item 21.)
- (b) **The secondary-pair distribution is the WP0-v2 final-state-resolved response.** A generation-n_gen carrier creates the pair
  Λ′ = (c′v′k′) with weight S(p,ω;Λ′)/S(p,ω) from WP0-v2 (7.2), with the **retarded out-state** weight (ε̃^{-1})_{G0} in (3.2) order (WP0-v2
  §10, CC-1; required in non-centrosymmetric targets such as GaAs). The cascade is the iterate of the WP0-v2 interface (7.1)–(7.2).
- (c) **Polar materials and the Coulomb-line classes (WP0-v2 (5.5), flag F2).** Apply WP0-v2's four-class topological classification to the
  carrier diagram. *External class* (p+G, ω): resummed once into ε^{-1}(p,ω), including local fields; (W1). *Ionic class*: the ionic part of
  the **total** ε at (p, ω) gives LO-phonon (Fröhlich) emission through (W1) itself. *DFPT class* (Q+G): the screened g. The long-range
  (Fröhlich) part g^L of the DFPT vertex is the same Coulomb line as the ionic class at p = Q + G, so the separate e–ph kernel must use only
  g^S = g − g^L (the EPW split) to avoid double counting. *Pair class*: enters only phonon-assisted ii, O(g²W^{scr}), beyond the first-order
  kernels (W1)+(W2); listed as a truncation (τ: n_g = 0 in the ii kernel). The argument (every line at momentum p resummed exactly once) is
  v1's; only the citation changes from v1's "three channels" to the four classes.
- (d) **Exchange.** Replace |M^{ii}_{dir}|² by |M|² = ½(|M^{ii}_{dir}|² + |M^{ii}_{xch}|² + |M^{ii}_{dir} − M^{ii}_{xch}|²) (0812.2923 Eq. (5) [FT], source "M_D, M_E").
  The correction is O(|M^{ii}_{xch}/M^{ii}_{dir}|) and matters only near threshold, where the final momenta are comparable. 0812.2923 also states that
  the BTE rate definition is ambiguous: its Eq. (1) and Eq. (5) differ through Z_{kn} and W versus W_R (its Eq. (7); source notation for the
  residue and the screened/reducible interaction). This is a genuine quasiparticle-picture uncertainty of the size of the difference between
  its Eqs. (1) and (8); gap R1 (§9).
- (e) **Slow ions.** An ion of charge form factor Z_κ(k) moving with velocity v_N has no recoil, so ω = k·v_N, and (W1) becomes Lindhard's
  dielectric stopping −dE/dx = (2Z_κ²α/πv_N²)∫dk/k ∫_0^{kv_N}dω ω L(k,ω) (Gaussian e_G² = α in the prefactor). This holds only in Born; the
  Born condition Z_κα/v_N ≪ 1 fails badly for keV recoils (Si at 1 keV: Z_κα/v_N ≈ 3.7×10², WP5v2-C6) [E]. See §3.3.

The phonon kernel is the EPW golden rule in campaign conventions (CONVENTIONS §5) [D, at O(g²)]:

  Γ^{ph}_{nk→m,k+Q} = (2π/N) Σ_ν |g^S_{mnν}(k,Q)|² [(n_{Qν}+1)δ(ε_{nk}−ε_{m,k+Q}−ω_{Qν}) + n_{Qν}δ(ε_{nk}−ε_{m,k+Q}+ω_{Qν})].           (W2)

g^S is DFPT-screened at ν = 0 (static); its error is O(ω_Q²/E_g²) ≈ 3×10⁻³ (X2; WP0-v2 (5.5); flag F11), not O(ω_Q/E_g). For GaAs, g^S
excludes g^L by (c); Si quadrupole corrections are included (SOTA R2).

### 1.2 The branching generating functional [D]
*Hypotheses.*
- (B1) Markov: collision durations ≪ time between collisions (Γ ≪ carrier energy scale); no inter-collision coherence. (Distinct from O4's
  (B1)/(B2), which are cited as O4-B1, O4-B2 in §1.5.)
- (B2) Siblings evolve independently: dilute limit, no Pauli blocking or Coulomb interaction between cascade particles. A 1 keV deposit
  makes ~300 pairs within ~10 nm, so the pair density is ≲ 10¹⁹ cm⁻³ ≪ 𝓃_e [E].
- (B3) Homogeneous medium, no applied field. An NTL drift field adds a deterministic drift term.

*Statement.* A particle state x (cascade type 𝔱 ∈ {e, h, phonon, ion, core hole}, band n, k, or ion energy and direction) evolves through
channels c with kernels 𝒦_c(x → x′_1…x′_m); each channel deposits δ𝐍_c, with 𝐍 = (N_eh, ℋ, E_st, N_FP, E_esc, …) (ℋ = heat). The generating
functional 𝔊_x(ϑ) = E[e^{ϑ·𝐍} | x] obeys the backward equation

  Γ_x 𝔊_x(ϑ) = Σ_c ∫dx′ 𝒦_c(x→x′_1..x′_m) e^{ϑ·δ𝐍_c} Π_j 𝔊_{x′_j}(ϑ),   Γ_x = Σ_c ∫dx′ 𝒦_c,   𝔊_x = e^{ϑ·𝐍_term(x)} on absorbing states.   (W3)

Proof: first-step analysis of a Markov branching process; condition on the first collision and factorise with (B2). Kernels: (W1) for e–e,
(W2) for e–ph, §3 for ions. A carrier is absorbing when its energy E above its band edge is below the ii threshold E_th^{ii}; its remaining
kinetic energy then goes to ℋ.
*Moments.* With m_x ≡ ∂_ϑ𝔊_x|₀, Γ_x m_x = Σ_c∫𝒦_c[δ𝐍_c + Σ_j m_{x′_j}] (linear). Second moments follow from ∂²_ϑ; for one channel step this
is the law of total variance (WP5v2-C9). **Lindhard's integral equation (L20), the R&K mean yield (L21) and Kinchin–Pease defect counts (L22)
are first moments of (W3); F_eh and F_NR (L23) are second moments** (§6).
*Exact energy bookkeeping [D].* Each vertex conserves energy. Assume terminal carriers relax to their band edges and pairs are counted at
E_g (with an exciton, E_g → E_g − E_x^b; Si E_x^b ≈ 15 meV). Then

  ω = N_eh E_g + ℋ + E_st + E_esc   (event by event),                                                                               (W4)

where E_esc covers photons and phonons that leave the target. Hence N_eh = (ω − ℋ − E_st − E_esc)/E_g: **all ionization statistics are
heat-partition statistics** (§6, L23).

### 1.3 Seeding and the measured spectrum [D given WP0-v2 (7.1)]
The prompt state Λ of WP0-v2 (7.1) is a set of particles {x′_j}: e at (n_e, k_e, E_e), h at (n_h, k_h, E_h) (carrier energies, NOTATION), phonons with total ω_ph, a recoiling ion with momentum, a core hole. Then

  P_casc(𝐍|Λ) = [coefficient of e^{ϑ·𝐍} in] e^{ϑ·𝐍_prompt(Λ)} Π_{j∈Λ} 𝔊_{x′_j}(ϑ),                                                    (W5)

  dℛ/d𝐍 = (ρ_χ/m_χρ_T) ∫d³v f_χ(v) ∫d³q/(2π)³ Σ_Λ tr[𝔇(q,v) S(q, ω_q; Λ)] P_casc(𝐍|Λ)   (= WP0-v2 (7.3)).                          (W6)

For an e–h seed, (B2) gives 𝔊_Λ = e^{ϑ_N} 𝔊_e(E_e,k_e) 𝔊_h(E_h,k_h) (ϑ_N = the N_eh component of ϑ): the generating form of R&K Eq. (5).
The DM tensor is traced **inside** the Λ sum, because different operators (density, spin, current) populate (E_e, E_h, k_e, k_h)
differently; the same holds for the q integral. At fixed (q, ω, v): P(N_eh|q,ω) = Σ_Λ tr[𝔇S(q,ω;Λ)]P_casc(N_eh|Λ)/tr[𝔇S(q,ω)]. These were
v1's WP0 defects WP5-1, WP5-2; WP0-v2 (7.3) has adopted them. **Pair-resolved weights** are WP0-v2 (7.2) with the retarded out-state
(ε̃^{-1})_{G0}; WP1-v2 [E2] uses the same out-state form (flag F1; I3 closed). **X+ seeds** carry
n_ph and ω_ph from WP3's joint response WP3 (W.1); ω_ph goes to ℋ once (O4-d6). **GS (NR) seeds** carry E_R and direction from S^{GS}_κκ and
ρ^{ph}_κ (WP2 (3.6); §3.1).

### 1.4 Controlled reductions
- **(R-k) Energy-only reduction [D under the hypothesis; error stated].** Suppose momentum randomisation is faster than energy loss,
  Γ_k ≫ Γ_E. This holds for e–ph above ~1 eV, where intervalley and acoustic scattering are quasi-elastic. Then 𝔊_{nk}(ϑ) → 𝔊_𝔱(E_car; ϑ) after
  the first collision, and the kernels are iso-energy averages
  𝒦̄_𝔱(E_car→E′_car) = Σ_{nk}δ(E_car − ε_{nk})𝒦(nk→…)/Σ_{nk}δ(E_car − ε_{nk}). The error is O(Γ_E/Γ_k) per generation. **Only the first generation keeps
  the k (hence q) memory**; that is where the DM-versus-photon seed difference enters.                                                (W7)
- **(CSDA) Near-threshold ii probability [D].** If ii events are rare per unit energy loss and ω_{Qν} ≪ E_car − E_th^{ii}, a carrier at E₀ that has
  not yet impact-ionised loses energy at the rate dE/dt|_ph = Σ_ν⟨ω_{Qν}Γ^{ph}_ν(E_car)⟩ (iso-energy average), and

  p_no-ii(E₀) = exp[ −∫_{E_th^{ii}}^{E₀} dE_car Γ_ii(E_car)/(dE/dt|_ph)(E_car) ]   (WP5v2-C16).                                                     (W8)

  This controls the 1e⁻/2e⁻ boundary. R&K's single ratio Γ^{ph}/Γ_ii (their Eq. (8)) is the free-particle evaluation of the integrand.

### 1.5 Response/cascade consistency: the C-code side of O4, and the Fano term in GaAs [D; E for the size]
WP0-v2 §6.2 (iv″b) makes P(N_eh|q,ω) convention-independent at O(g²) only if the cascade satisfies O4's hypotheses and code-pair conditions.
The WP5 cascade (the "C-code" of O4) must implement:
- **O4-B1** Markov in the prompt label (this is (B1)–(B2) above) and **O4-B2** the first-emission kernel
  𝒦_{Λ₀→Λ₊} = [2π|g_{Λ₊Λ₀}|²δ(Ẽ_Λ₀ − E_Λ₊) + 𝔉_{Λ₀,Λ₊}]/Γ^{tot}_Λ₀, Γ^{tot} = Γ^{ph} + Γ^x (Γ^x = ii, Auger, radiative; supplied by WP5 only);
- **O4-d2** the same g^S, gauge U(k), ω_{Qν} and eigenvectors as the response code; Γ^{ph}_Λ₀ = −2 Im Σ^{FM} branch by branch;
- **O4-d3** the X0 seed starts at the response code's Ẽ_Λ₀ (ZPR included); a bare-band cascade shifts the seed by the same Re Σ;
- **O4-d6** X0 seeds at (Λ₀, Ẽ_Λ₀, n_ph = 0) and the cascade emits first; X+ seeds at (Λ₊, n_ph = 1, ω_ph = ω_Q) with no re-applied first
  emission, ω_ph to ℋ once;
- **O4-d8, d9, d10** the same δ-smearing σ (level spacing ≪ σ ≪ δ), the same T (n_Q, n_Q + 1), and all non-phonon channels in the cascade only.
Violating d2/d3 by 10–20% gives an O(1) error in P(N_eh) (O4 toy T4); this is a hard requirement, not a nuisance.

**The Fano term (WP0-v2 flag F8; O4 (O4.7)).** For an X0 seed Λ₀ the first-emission branching to phonon branch ν is
K_ν = (Γ^{(ν)} + 𝔉_ν)/Γ^{tot}, with 𝔉_ν ≡ 𝔉_{Λ₀,ν} = 2πΓ^{(ν)}(c̄^F − c_ν^F), c_ν^F = Im(ρ*_Λ₀ a^{off}_ν), c̄^F = Σ_νΓ^{(ν)}c_ν^F/Γ^{ph}, so Σ_ν𝔉_ν = 0
(WP5v2-C14a). In a PT-symmetric crystal ρ and a^{off} are simultaneously real, so 𝔉 = 0 (Si, Ge, diamond; WP5v2-C14b) [D, sketch, O4].
*Bound [D].* Let P_ν(N) ≡ P_casc(N_eh = N | first emission into ν). The 𝔉-induced change is ΔP(N|Λ₀) = Σ_ν(𝔉_ν/Γ^{tot})P_ν(N). Because
Σ_ν𝔉_ν = 0, ΔP = Σ_ν(𝔉_ν/Γ^{tot})(P_ν − P̄) for any constant P̄ (WP5v2-C14c); choosing P̄ at the midpoint of {P_ν},

  |ΔP(N|Λ₀)| ≤ ½ (Σ_ν|𝔉_ν|/Γ^{tot}) · max_{ν,ν′}|P_ν(N) − P_ν′(N)| ≤ 2π (Γ^{ph}/Γ^{tot}) max_ν|c_ν^F| · max_{ν,ν′}|P_ν(N) − P_ν′(N)|.       (W15)

*Estimate for GaAs [E].* O4 gives 2π|c_ν^F| = O(Γ_Λ₀|a^{off}_ν|/|ρ_Λ₀|) × |sin φ_ν| = O(Γ_Λ₀/δ)|sin φ_ν|, with φ_ν the relative phase of a^{off}_ν and
ρ_Λ₀. That phase exists only through the inversion-odd part of the crystal potential; its ratio to the even part in GaAs is ~0.2–0.3
(Cohen–Bergstresser antisymmetric/symmetric form factors [UNVERIFIED]), so 2π max|c_ν^F| ≲ 0.3 Γ_Λ₀/δ. The branches differ by the first
phonon energy (≤ ω_LO ≈ 36 meV [UNVERIFIED]) and by Q; near the ii onset P_ν(N) varies on an energy scale ≳ 0.1 eV, so the spread is
≲ 0.36 (worst case, at the 1e⁻/2e⁻ boundary) and much smaller elsewhere. Hence |ΔP| ≲ 0.11 Γ_Λ₀/δ (WP5v2-C14e): ≲ 2×10⁻³ for Γ/δ ≈ 0.02,
≲ 7×10⁻² for Γ/δ ≈ 0.6 (the O4-d11 edge shell, where only totals and the unexpanded-Dyson P(N_eh) are quoted anyway). 𝔉 only redistributes
first emissions among branches (it changes no rate). Status: the exact number needs the response code's 𝔉 export (O4-d7; WP3); until then
(W15) with Γ/δ from the O4 map is the GaAs nuisance θ_𝔉 (§8).

---
## 2. Hot carriers: closure of G1

**Formula.** (W1)+(W2) inside (W3), seeded by (W5)–(W6) from the DM S(q,ω;Λ), under the §1.5 conditions. Temperature enters in three places:
the Bose factors in (W2), the (1 − e^{−βω})^{-1} in (W1), and the T-renormalised bands (ZPR, L12). It does **not** enter only through E_g(T)
(§6.2). Output: P_n(q,ω,T) ≡ P(N_eh = n | q, ω, T), with moments ε_eh(q,ω,T) = ω/n̄ and F_eh(q,ω,T).
**Computation specification (per material: Si, Ge, GaAs).**
- *Bands.* QE (PBE, norm-conserving or PAW) plus G0W0 (BerkeleyGW or Yambo). QP corrections Wannier-interpolated up to ~15 eV above the CBM.
  Si needs 16–20 disentangled sp³d WFs; Ge and GaAs similar, with SOC. Above ~15 eV use free-electron-like states with GW lifetimes; this is
  where R&K's free-particle model is accurate (§6.2) and provides a matching check.
- *W^{scr}(p,ω).* BerkeleyGW full-frequency ε^{-1}_{GG′}(p,ω), ω ∈ [0, 60] eV (N_ω ≈ 200, denser below 20 eV), p-mesh 10³–12³ plus G-shifts,
  N_G ≈ 200–300 (cutoff 8–10 Ry), ≥ 200 empty bands. Converge Im ε^{-1} at the plasmon (Si ~16.7 eV) to 2%. Total ε for GaAs (ionic part via
  DFPT Z*_κ, ε_∞). Cost: 10⁴–10⁵ core-h per material [E].
- *ii kernel.* (W1) with LFE and exchange per (d). Store 𝒦̄(E → E′; E_e′, E_h′), the pair split resolved via WP0-v2 (7.2) (retarded out-state
  weight) at (p, ω). Sample iso-energy surfaces with ~10³ k-points per 50 meV bin. Cost ∝ N_E × N_kiso × N_p × N_b′ ≈ 10³×10³×10⁴×20 matrix
  elements via FFT: 10⁴–10⁵ core-h [E].
- *e–ph kernel.* EPW, coarse 8³/8³ grid, Wannier interpolation, fine k 80³–100³ plus Q 50³ by MC sampling. Bands up to the WF window,
  T ∈ {0, 50, 100, 150, 300} K, g^S only for GaAs, quadrupole corrections (SOTA R2). Same g^S and ω_{Qν} as the response code (O4-d2).
  Cost ~10⁴ core-h [E].
- *Cascade solve.* (R-k) for n_gen ≥ 2: a 1D recursion in E on a 10 meV grid, by event sampling or deterministic moment equations (cost
  negligible). n_gen = 1 is fully k-resolved from S(q,ω;cvk), using WP1 outputs (RPA+LFE) and, for X+ seeds, the WP3 PAER pair distribution
  with ω_ph removed to ℋ (O4-d6); for GaAs the 𝔉 correction (W15).
- *Grid of outputs.* ω ∈ [E_g, 50 eV] in 50 meV steps; |q| ∈ [0, 25 αm_e] with 3 directions plus the angular average; 5 temperatures.
  50 eV–keV: match to the asymptotics (n̄ = ω/ε_eh + b_N, Var = F_ehω/ε_eh) (§6.4).
- *Validation (not fit parameters).* Si quantum yield at 3–8 eV and 50–1500 eV (photon seeds, q ≈ 0; data cited in 2004.10709);
  ε_eh = 3.749 ± 0.001 eV and F_eh = 0.119 ± 0.002 at 5.9 keV and 123 K (2004.11499 [FT]); Ge ε_eh(77 K). A photon seed (q ≈ 0) and a DM
  seed (q ~ 1–10 keV) from the same code give the G1 q-dependence directly.
- *Nuisances for WP6:* §8.

---
## 3. Nuclear recoil: the heat / defect / charge partition (closure of G3)

### 3.1 Hand-over from S^{GS}_κκ [D]
The regimes are set by E_R = q²/2M_κ and x_R (WP0-v2 Table 6.1); K labels per CONVENTIONS §11.
- **(i)** x_R ≲ 1 (E_R ≲ ω_max ≈ 60 meV in Si; K = 1ph-coh/1ph-inc/multi-…). Final states are few-phonon states in the GS sector (WP2). The
  partition is trivial: P = δ(ℋ − ω)δ_{N_eh,0}, E_st = 0. The phonon content is ρ^{ph}_κ(ω′|q,ω) of WP2 (3.6), used as recorded (flag F6; WP2-v2 IF-2). **Sign of ω′ [D]:** entries at ω′ < 0 are
  **absorbed** thermal phonons (s^ph = −1, weight n_B), not created ones: created number ∫_{ω′>0}ρ^{ph}_κ, absorbed number ∫_{ω′<0}ρ^{ph}_κ,
  and ∫ω′ρ^{ph}_κ dω′ = ω is the **net** lattice energy, so ℋ = ω (not ∫|ω′|ρ^{ph}_κ). The NR/phonon seed is the created set minus the absorbed
  set; absorption entries seed no cascade particle and carry negative heat (WP5v2-C20a).
- **(ii)** x_R ≫ 1 (K = imp). The impulse approximation of WP2 (5.3), S_IA(q,ω) = (2π/Ω)Σ_κ|c_κ|²∫d³P₀ 𝔫_κ(P₀)δ(ω − q²/2M_κ − q·P₀/M_κ)
  (c_κ the species coupling, = A_κF^M_κ for nucleon coupling; one atom κ per cell), resolved in the struck-nucleus momentum P_I = P₀ + q:

  S^{GS,IA}_κκ(q,ω; P_I) = (2π/Ω)|c_κ|² 𝔫_κ(P_I − q) δ(ω − P_I²/2M_κ + (P_I − q)²/2M_κ),   σ_ω² = 4E_R E^kin_q̂,   E^kin_q̂ = ⟨(q̂·P₀)²⟩/2M_κ.   (W9)

  This is the saddle point of the incoherent multiphonon sum (L5 → L6). Its Doppler width σ_ω (WP5v2-C7a) is the leading 1/x_R correction;
  E^kin_q̂ is the **true** (zero-point plus anharmonic, T-dependent) kinetic energy of WP2 (5.3) (v1 used the harmonic
  ⟨P²⟩ = (M_κ/2)∫dω′D_κ(ω′)ω′coth(βω′/2), its harmonic limit; interface flag I2). Harmonic T = 0 gives E^kin_q̂ = ⟨ω⟩/4, σ_ω² = E_R⟨ω⟩
  (WP5v2-C7b). The skewness is 𝔨₃^{GS} from the BO curvature (WP2 (5.2), L6 ✎). **The MD initial condition is fixed by the response:** one
  atom of species κ at a site, lattice positions {R_I(0)} from the harmonic (or PIMD) Wigner distribution at T, momentum P_I = P₀ + q,
  P₀ ~ 𝔫_κ. This reproduces S_κκ's energy distribution to O(1/x_R); the correction is the quantum/classical difference of the final
  vibrational state.
- *Size.* Si, E_R = 10 eV (20 eV): σ_ω ≈ 0.67 eV (0.95 eV) with ⟨ω⟩ = 45 meV (WP5v2-C7c) [E]. The struck atom's kinetic energy is smeared
  by ~1 eV around E_d: predicted, not tuned.
- *No double counting with Migdal.* WP0-v2 Theorem D (6.1) splits the DM vertex: GS seeds (no electronic excitation) go to (W9); X-sector
  (Migdal) seeds add prompt e–h pairs (WP3) and a recoil. The WP5 transport starts **after** the vertex. A "U" that "effectively
  incorporates the Migdal effect" (2209.04503 [FT]) double counts if a WP3 Migdal rate is also added. Neutron-calibrated yields contain
  Migdal: fit Y_tot = Y_casc[S^{GS}] + ∫dω_e P_casc(N|ω_e)dP_Mig/dω_e, never Y_casc plus Migdal (WP3 N3; WP0-v2 double-counting rule (e)). **Drag-mass subtraction [D] (WP2-v2 (3.4), §5.2′, IF-2; WP3 J3;
  WP0-v2 §6.2 (iii) and rule (a)):** when Migdal (X-sector) seeds are added separately, the GS seed must not be normalised to the full
  nuclear f-sum. Per nucleus the GS first moment is q²/2M_κ − E^{Mig}_1(q), E^{Mig}_1(q) = q·δM_κ·q/(2M_κ²), the remainder being the
  X-sector (Migdal) energy moment; its zeroth moment is depleted by P_Mig(q). A harmonic WP2 S^{GS}_κκ (which saturates q²/2M_κ exactly)
  is rescaled in its first moment by 1 − 2M_κE^{Mig}_1/q² (δM_κ/M_κ ≤ 2.7×10⁻⁴ in Si [E]) before seeding (WP5v2-C20b).

### 3.2 Dynamics on the BO surface [D for the regime boundaries; E for the numbers]
- **(iii)** E_R ≈ 0.3 eV–E_d. The trajectory runs on the BO surface E^ad_0(R). It is anharmonic: the displacement amplitude in Si is
  u_I ≈ √(2E_R/M_κ⟨ω⟩²) ≈ 0.38 Å at 1 eV against a 2.35 Å bond (WP5v2-C17) [E]. It is classical: λ_dB(20 eV, Si) ≈ 0.012 Å. It is adiabatic:
  the Massey parameter ξ_Mas = E_g ℓ_int/v_N ≈ 15 at 20 eV (ℓ_int = 1 Å; WP5v2-C6), so non-adiabatic loss is ~e^{−ξ_Mas}.
  **BO-MD is controlled here.** Everything goes to ℋ, except a stored energy when E_R ≥ E_d.
- **Displacement threshold (definition).** Let 𝔅₀ be the basin of the perfect crystal on E^ad_0 and 𝒰_t the dissipative flow (dynamics plus
  bath). For recoil direction r̂_R:

  P_FP(E_R, r̂_R) = Pr_{R_I(0)∼Wigner}[ lim_{t→∞} 𝒰_t(R_I(0), √(2M_κE_R) r̂_R) ∉ 𝔅₀ ],   E_d(r̂_R) ≡ E_R such that P_FP = ½.                   (W10)

  A smooth step whose width comes from the zero-point and thermal R_I(0) and from (W9); the step model is its zero-width limit.
- **Stored energy.** E_st = E^ad_0(R_final) − E^ad_0(R_I(0)) at t_pr ≈ 10–100 ps, after prompt recombination and before thermally activated
  annealing (§4). R_final holds a vacancy–interstitial pair, a close pair or an amorphous pocket. **E_st ≠ E_d.** E_d is a dynamical (kinetic)
  threshold; E_st is a thermodynamic formation energy, ~E^{form}_V + E^{form}_I for a separated pair (Si ≈ 7–9 eV, Ge ≈ 5–7 eV
  [UNVERIFIED, DFT literature from memory]). The rest, E_d − E_st, is heat.

### 3.3 Electronic excitation by the recoil (the charge channel) [D for the threshold logic; E for the numbers]
- **Kinematic threshold.** A binary collision between a slow ion (v_N ≪ v_F) and a valence electron transfers at most 2m_ev_N(v_N + v_F). A
  pair needs E_g, so v_th ≈ E_g/(2m_ev_F). With free-electron v_F (WP5v2-C5): **E_R,th ≈ 375 eV (Si), 465 eV (Ge)** [E]. The band-structure
  version replaces the Fermi sphere by the support of L(k,ω) (Theorem C(e)). Below E_R,th the linear-response electronic stopping in a gapped
  crystal vanishes. A friction model F = −S^{stop}_e(E)v̂ (2506.03810 Eq. (3) [FT], SRIM S_e) assigns electronic loss with no final state there.
- **What creates pairs below E_R,th.** Non-adiabatic transitions in close collisions, where the local gap of the distorted configuration
  closes (quasi-molecular promotion): the X-sector couplings of Theorem D at strong coupling. Per crossing they follow Landau–Zener,
  P_LZ = exp(−2πh_LZ²/(v_N|ΔF_LZ|)) (h_LZ the diabatic coupling, ΔF_LZ the slope difference). Both ξ_Mas ≈ 2 at 1 keV and Z_κα/v_N ≫ 1 say
  that **linear-response (Lindhard–Scharff) stopping is not a derived limit at E_R ≲ few keV**; it is a fit.
- *Data.* The Ge measurement QF = 25 ± 3% at 254 eV_nr (2405.10405 [ABS]) lies below the binary threshold; if confirmed, this channel must
  dominate there [E].
- **Charge from the electronic deposit.** The electronic excitation spectrum dP/dω_e produced along the trajectory seeds the §2 cascade.
  Slow-ion excitations are near-gap, so **N̄_eh ≠ E_el/ε_eh^γ**: the conversion uses P_n at the NR seed spectrum, not the photon asymptote
  (§6.1, L20 correction).

### 3.4 Computation specification for G3
- **PES.** DFT (QE or VASP; PBE and SCAN for spread) joined to ZBL/DMol at r < 1 Å. Train an MLIP (ACE, MACE or NequIP) on ~10⁴
  configurations: dimers down to 0.5 Å, point defects, close pairs, amorphous and liquid, plus recoil snapshots. Force error ≤ 50 meV/Å;
  energy ≤ 3 meV/atom.
- **E_d(r̂_R) and P_FP.** ~300 directions in the irreducible wedge × 20 Wigner R_I(0) samples, bisection to 0.5 eV, cells of 4096–8000 atoms
  for 3–5 ps, 0.1 fs step near close approach, boundary thermostat: ~3×10⁴ MLIP runs, ~10³ GPU-h. Check 20 directions with BO-DFT-MD
  (512 atoms, ~10⁵ core-h).
- **Partition tables.** E_R ∈ [1 eV, 10 keV] (40 log points) × 100 directions × 100 seeds from (W9). Cells from 10³ atoms (< 100 eV) to
  10⁵ atoms (10 keV), 1–10 ps. Record ℋ, E_st (quench to 0 K at t_pr) and defect labels. Cost 10⁴–10⁵ GPU-h.
- **Electronic channel.** Real-time TDDFT Ehrenfest or surface hopping (Qb@ll, Octopus, SALMON) for Si–Si and Ge–Ge close collisions,
  E_coll = 50 eV–5 keV, impact parameters b_imp = 0–1.5 Å, 64–216-atom cells, 20–50 trajectories per energy. Output the **distribution**
  dP/dω_e(b_imp, E_coll), not only S^{stop}_e. Cost ~10⁶ core-h. Attach it to the MLIP-MD as stochastic excitation events feeding §2.
- **Outputs.** P(ℋ, E_st, N_eh | E_R, r̂_R, T) and moments, the anisotropic E_d surface and the heat quenching Y_H(E_R, r̂_R):

  Y_H ≡ ⟨ℋ_meas⟩/E_R = 1 − ⟨E_st⟩/E_R − ⟨E_esc⟩/E_R − ⟨N_trap⟩E_g/E_R   (zero field; + N_eh eV_bias/E_R in NTL mode).                    (W11)

  (W11) follows from (W4). Unit heat quenching (2007.14289 [ABS]) is the truncation E_st = E_esc = N_trap = 0.

---
## 4. Defects, annealing and stored energy as a background model (G12)
**Formula [D, under harmonic TST and Markov hopping].** Defect configurations i have energies E^{conf}_i ≡ E^ad_0(R_i) and hop rates Γ_ij(T).
Populations N_i(t) are seeded by recoils (§3: DM, radiogenic, cosmogenic; source 𝔰_i(t)) and by the post-cooldown state:

  dN_i/dt = 𝔰_i(t) + Σ_j [Γ_ji N_j − Γ_ij N_i],   ℛ_rel(E,t) = Σ_{ij} Γ_ij(T) N_i(t) δ(E − (E^{conf}_i − E^{conf}_j)) ⊗ (detector response).   (W12)

Rates:
- above the crossover T_× = ω_bar/2π: Γ_ij = (Πω_i^{(min)}/Πω^{(TS)}) e^{−E_bar/T}/(2π) (Vineyard; ω_bar the barrier-top curvature frequency);
- below T_×: instanton tunnelling Γ_ij ∝ e^{−𝒮_inst}.
For an Si interstitial-like barrier with ω_bar ~ 2π×10 THz, T_× ≈ 76 K (WP5v2-C17) [E]. **At mK, annealing is tunnelling or triggered
(avalanche: 2408.07518 [ABS] finds that crossing low barriers triggers larger releases). Classical TST predicts no events there.**
- **Time dependence [D].** For a barrier density 𝒩_b(E_bar) flat over the active range and Γ = Γ_att e^{−E_bar/T},
  Σ Γe^{−Γt} → 𝒩_b T(1 − e^{−Γ_att t})/t ∝ 1/t (WP5v2-C8): a generic 1/t decay after cooldown or irradiation. Exponential decays need a narrow
  barrier set. The 1/t law is also proposed for dislocation relaxation (2406.15425 [ABS]), so the time law alone does not discriminate.
- **Energy spectrum [C].** The observed ∝ e^{−E/E_slope} (2408.07518 reports that simulations reproduce it) is not derived here. A
  maximum-entropy release distribution at fixed mean ⟨E^{conf}_i − E^{conf}_j⟩ would give it; conjecture.
- **Computation specification.** *Barriers:* climbing-image NEB on the §3.4 MLIP from the quenched §3 end states; validate 50 barriers
  against DFT. *Kinetics:* rate catalogue by on-the-fly kinetic MC; instanton (ring-polymer) rates for the 10² most frequent hops below T_×.
  *Seeds:* E_R spectra of cosmogenic neutrons and radiogenic recoils as 𝔰_i. *Output:* ℛ_rel(E, t, T) with nuisances for the barrier spread
  and the MLIP error. *Cost:* ~10⁴ GPU-h.
- **Exact remaining gap (G12).** Triggered-avalanche statistics at T ≪ T_× need a non-Markov treatment of strain and phonon pulses (R4, §9).
- **DFT-level defect creation by ER (catalog gap 5).** The §2 carriers cannot displace atoms: the maximum transfer from a 10 eV electron to Si
  is 4m_eE/M_κ ≈ **0.78 meV** ≪ E_d (WP5v2-C11; v1's 1.5 meV was 2× too large; the conclusion is unchanged). ER defect creation therefore
  needs electronic-excitation-driven bond breaking (self-trapped excitons or core-hole Auger). In Si this is absent at eV scale [E]. It is
  candidate-dependent for ionic targets (NaI, LiF: colour centres; WP4).

---
## 5. Quasiparticle yield in superconductors
**Formula [D under (B1)–(B3)].** (W3) with types {hot e (ω ≫ Δ_BCS), QP(E), phonon ω′ > 2Δ_BCS, phonon ω′ < 2Δ_BCS (loss), escaping phonon}.
Scope: Theorem D does not apply (WP0-v2 §6.2 (H2) scope); the sectors are quasiparticle-number sectors (WP4, flag F5).
- *Seed.* S(q,ω;Λ) on the BCS reference state with the conserving GRPA vertex (L15, WP4). For ω ≫ Δ_BCS (every m_χ ≳ 100 keV) the seed is a
  normal-state hot e–h pair and (W1) applies unchanged, including the Al plasmon (~15 eV). For ω ≈ 2Δ_BCS–few Δ_BCS the seed is WP4 [4.6]:
  Λ = (E₁, E₂), E₁ + E₂ = ω, P(E₁|ω) = [E₁E₂ + Δ_BCS²]/[√(E₁² − Δ_BCS²)√(E₂² − Δ_BCS²)]/[ω𝔤_I(ω/Δ_BCS)], used as recorded.
- *Kernels.* Near Δ_BCS: Eliashberg α²F(ω′) with coherence factors. Phonons are case I (density-like): QP scattering carries (1 − Δ_BCS²/E₁E₂),
  pair breaking and recombination carry (1 + Δ_BCS²/E₁E₂). Photon (case II) pair breaking carries (1 − Δ_BCS²/E₁E₂) (1401.1937 Eq. (1) [FT]).
  **The DM density vertex is case I** (WP4 [4.6] numerator E₁E₂ + Δ_BCS²), so for ω ≈ 2Δ_BCS–3Δ_BCS the DM seed's (E₁,E₂) split differs
  from the photon calibration: a q-independent but probe-dependent analogue of G1 [D for the sign structure]. v1's open item (R5) on the
  screened vertex is closed at the seed level by WP4 [4.6] and L15 (GRPA); its size at q ≲ 1/ξ_coh stays with WP4.
- *Exact bookkeeping (as W4).* ω = N_qpΔ_BCS + E_sub + E_excess + E_esc, so

  η_pb ≡ Δ_BCS⟨N_qp⟩/ω = 1 − ⟨E_sub + E_excess + E_esc⟩/ω,   F_qp = Var(E_sub + E_excess + E_esc)/(Δ_BCS²⟨N_qp⟩),                    (W13)

  N_qp the quasiparticle number (NOTATION); WP4-v2 §4.6 uses the same normalisation (WP5v2-C15; I1 closed).
- *Limits.* For ω < 3Δ_BCS there is no cascade: N_qp = 2, η_pb = 2Δ_BCS/ω. For ω ≫ ω_D in a bulk absorber, η_pb → 0.57–0.6 (infinite-volume
  results quoted in 1401.1937 [FT]). The late-time Rothwarf–Taylor stage (1401.1937 Eqs. (2)–(5) [FT]) is the coarse-grained two-type
  version of (W3); its phonon-trapping factor 1/(Γ_pb/Γ_esc + 1) (pair-breaking rate Γ_pb, escape rate Γ_esc; source "τ_l/τ_pb") is the E_esc
  term of (W13).
- *Specification.* Inputs: DFPT α²F (QE/EPW) for Al, Nb, Ta, plus measured α²F as a check; Δ_BCS(T); film thickness d_film and Γ_esc(d_film),
  or the transmission t_esc (WP4). Solve: Chang–Scalapino kinetic equations as the mean-field closure of (W3), plus event sampling for F_qp.
  Grids: E on a 1 μeV grid near Δ_BCS, 0.1 meV up to ω_D, (W1) above. Output: η_pb(ω, d_film, T) and F_qp.

---
## 6. LIMITS entries derived (L20–L23)

### 6.1 L20: Lindhard quenching (and the modified Lindhard 2209.04503)
- **Source [FT] (source notation: ε = reduced energy 𝓔_red, ν̄ = nuclear energy ν̄_L, k = k_L, W = σ²_strag, U = U_bind, S_e = S^{stop}_e).**
  2001.06503 Eq. (3): ∫dσ_{n,e}[ν̄(E−T_n−ΣT_ei) + ν̄(T_n−U) − ν̄(E) + Σ_iν̄_e(T_ei−U_ei)] = 0. With approximations (A)–(E) this becomes Eq. (5):
  k ε^{1/2} ν̄′(ε) = ∫_0^{ε²}dt f(t^{1/2})/(2t^{3/2}) [ν̄(ε−t/ε) + ν̄(t/ε) − ν̄(ε)], with S_e = kε^{1/2}, k = 0.133Z^{2/3}A^{-1/2} (Eq. (4)). The
  solution is Eq. (7): ν̄_L = ε/(1+kg(ε)), g = 3ε^{0.15} + 0.7ε^{0.6} + ε, and f_n = (ε − ν̄)/ε (Eq. (6)). 2209.04503 adds the binding U(E),
  the second-order term and electronic straggling W(ε) in Eq. (2): −½εS_e(1 + W/(S_eε))ν̄″ + S_eν̄′ = ∫_{εu}^{ε²}dt f(t^{1/2})/(2t^{3/2})
  [ν̄(ε−t/ε) + ν̄(t/ε−u) − ν̄(ε)], with U = U_FP + U_EDFT(E) (Eq. (3)).
- **URF chain.**
  1. WP0-v2 (3.4), GS sector, K = imp → recoil seed (W9).
  2. (W3), ion type, observable ν = ℋ + E_st (+ the internal excitation energy U_bind).
  3. First moment = 2001.06503 Eq. (3) exactly, with dσ_n = classical scattering on E^ad_0 and dσ_e = the §3.3 non-adiabatic excitation kernel [D].
  4. Truncations: (I/A) drop recoils generated by electrons (exact below the §4 4m_eE/M_κ bound); (II–IV/C–E) small fractional transfers;
     (D) nuclear and electronic channels independent; E^ad_0 → a universal screened pair potential (TF or ZBL; amorphous random medium: no
     channeling, no anisotropy); dσ_e → Born free-electron-gas stopping ∝ v_N (Theorem C(e)) times Lindhard's hand-inserted Z^{1/6}
     (2209.04503 [FT] states this); (B/V) U_bind = 0 (Lindhard) or U_FP + U_EDFT (2209.04503); charge yield N_eh = E_el/ε_eh^γ.
- **Validity.** Born stopping needs Z_κα/v_N ≪ 1, which fails for all keV recoils (≈ 3.7×10² at 1 keV Si) [E], so S^{stop}_e ∝ v_N is an
  empirical scaling there. Binary electronic excitation needs E_R ≳ 375 eV (Si) or 465 eV (Ge) [E, WP5v2-C5]. The amorphous-medium step needs
  ranges ≫ the lattice constant and no channeling. Quoted empirical validity: 𝓔_red ≳ 0.1 (≈ 4 keV) for Si and ≳ 0.00088 (≈ 250 eV) for Ge
  (2001.06503 [FT]). The modified model fits 680 eV–3 MeV Si data with χ²/dof = 1870/101 (2209.04503 [FT]).
- **Leading URF corrections.** (a) **The gap threshold:** below E_R,th the electronic deposit comes only from close-collision (Landau–Zener)
  promotion, so a non-zero QF below ~0.4 keV measures that channel; sign-definite (the binary channel switches off). (b) **Seed-spectrum
  conversion:** N̄_eh = Σ_{ω_e}(dP/dω_e) n̄(ω_e) ≠ E_el/ε_eh^γ; near-gap excitations give n̄ ≈ 1 per excitation, against ω_e/3.75 eV for the
  photon conversion. (c) Crystal anisotropy and channeling: directional QF. (d) U_bind computed as ⟨E_st⟩ (§3.2) instead of fitted.
- **Discrepancies.** (1) *Reduced energy.* 2001.06503 uses Lindhard's a = 0.8853a₀/(√2 Z^{1/3}) (𝓔_red/E = 0.0243 keV⁻¹ for Si); 2209.04503
  uses ZBL a with C = 16.2616/(Z Z_1Z_2) and Z_1 = 12 for a stripped Si ion (0.0268 keV⁻¹). The same E maps to a 𝓔_red 10% different
  (WP5v2-C10): fitted parameters cannot be transferred. (2) 2001.06503 notes an internal inconsistency of Lindhard's boundary condition:
  ν̄′(0) → 1 is imposed, while Eq. (5) implies ν̄′(0) → 0. (3) The second-order coefficient ½εS_e of 2209.04503 Eq. (2) requires
  ∫dσ_{n,e}T_nΣT_e → ½εS_e; not derived in the text and not reproduced here. The straggling coefficient ½W is consistent with the stated
  expansion. (4) 2506.03810 (MD) stops at 10 eV_nr "as no ionization occurs below this threshold" while using SRIM friction above it; the
  binary threshold (~375 eV) is 40× higher, so their sub-keV ionization is a property of the friction model, not of a final-state channel [E].

### 6.2 L21: Ramanathan–Kurinsky ionization model; step model
- **Source [FT, 2004.10709] (source notation: E_r = deposited energy, → ω; "E_r" in Eqs. (15)–(16) = phonon losses).**
  Eq. (5): n(E_r) = 1 + ∫_0^{E_r−E_g}dE P(E,E_r)⟨N(E)⟩. Eq. (6): e/h symmetry P(E,E_r) = P(E_r−E_g−E, E_r). Eq. (7): a Beta P(x|α) fitted to
  photon ε_eh data at 3–8 eV. Eq. (8): Γ_ph/Γ_eh = A(105/2π)(E−ω_0)^{1/2}/(E−E_g)^{7/2}. Eq. (9): A = (|M_ph|/|M_eh|)(4π⁴/VΔ)(ħ²/2m)³, with
  A = 5.2 "eV²". Eq. (10): p_eh = [1 + Γ_ph/Γ_eh]^{-1}. Eq. (11): E_g(T) = E_g(0) − aT²/(T+b) as the only T dependence. Plasmons:
  n_pl = ⌊(E_r−E_g)/ω_pl⌋. The step model N_eh^{step} = 1 + ⌊(ω−E_g)/ε_eh⌋ (ε_eh = 3.6–3.8 eV Si, 2.9 eV Ge) appears in the survey
  (2105.05253, 2603.12326) as "Q".
- **URF chain.** (W6) → (W5) with an e–h seed → (W3) first moment. Then:
  1. q-marginalise the seed **and** replace S(q,ω;cvk) by a photon (q ≈ 0) fit. This is not the marginal of the DM seed (WP0-v2 (7.3); §7).
  2. (R-k) (W7) from generation 1.
  3. Impose e/h symmetry N̄_e = N̄_h. The URF keeps them separate; the hole bandwidth (B_h ≈ 12 eV) emerges from the band structure.
  4. (W1) → constant |M_eh|² with momentum conservation dropped ("random-k"), free parabolic DOS ∝ √E, vacuum mass. The three-body phase
     space is Γ(3/2)³/Γ(9/2)(E−E_g)^{7/2} = (2π/105)(E−E_g)^{7/2} (WP5v2-C1a,b): the origin of 105/2π. The threshold moves from
     E_th^{ii} ≈ 1.1–1.5E_g to E_g.
  5. (W2) → one Einstein mode ω₀ = 63 meV with constant |g|², T = 0: Γ^{ph} ∝ (E−ω₀)^{1/2}. The ratio is R&K Eq. (8) [D].
  6. Plasmons: an explicit fixed-energy plasmon channel on top of (4) double counts with the RPA ii channel (Theorem C(a)); R&K find no
     effect, consistent with this.
  7. The step model is the deterministic limit P_casc(N|Λ) → δ_{N,N_eh^{step}(ω)}, so F_eh = 0.
- **Validity.** Steps (4)–(5) need E − E_g ≫ the band-structure scale (E_dir − E_g ≈ 2.2 eV Si; L/X valley spacing in Ge), in practice
  E ≳ 10–15 eV [E]. The Beta seed is valid only for photon kinematics. The step model fails whenever √(F_ehn̄) ≳ ½, i.e. n̄ ≳ 1/(4F_eh) ≈ 2 for Si,
  so it is never accurate beyond the forced region ω < 2E_g [E]. Its mean averaged over the fractional part is (ω−E_g)/ε_eh + ½; the
  asymptotic URF mean is ω/ε_eh + b_N; they agree only if b_N = ½ − E_g/ε_eh ≈ 0.19 (Si) (WP5v2-C18) [E].
- **Leading URF corrections.** (a) **q-dependence of the seed:** the first generation is k-resolved; the size is bounded by R&K's own envelope
  between α = 0 and α → ∞ (source Beta parameter; up to ~50% in p_2 at 4–8 eV, 2004.10709 [FT]). (b) Temperature beyond E_g(T): phonon
  absorption n_{Qν}, T-dependent ZPR band shapes, and (1−e^{−βω})^{-1} in (W1); the ii threshold region is where Γ^{ph}(T) matters, via (W8).
  (c) X+ (PAER) seeds remove ω_ph into ℋ at the vertex (O4-d6). (d) Exchange (Theorem C(d)).
- **Discrepancies.** (1) *Units of A:* Eq. (8) is dimensionless only if [A] = energy³, so "5.2 eV²" is inconsistent (WP5v2-C1c). (2) *Golden
  rule:* Eq. (9) has |M_ph|/|M_eh|; the golden rule gives |M_ph|²/|M_eh|²; Δ is undefined as a real- or k-space volume. (3) *Symbol collision:*
  E_r means "recoil energy" in Eqs. (2)–(5) and "phonon losses" in Eqs. (15)–(16). (4) *App. A, Eqs. (22)–(23)* write Var = Fn + η(1−η)n
  (source η = detection efficiency ϵ_det). Binomial thinning gives Var = ϵ_det²F_ehn + ϵ_det(1−ϵ_det)n exactly, so
  **F_meas = ϵ_detF_eh + 1 − ϵ_det, not F_eh/ϵ_det + 1 − ϵ_det** (WP5v2-C2a). The text's 0.130/0.160 at ϵ_det = 0.98/0.95 are close to the exact
  0.133/0.159; Eq. (23) gives 0.137/0.171 (WP5v2-C2b). F_meas − F_eh = (1 − ϵ_det)(1 − F_eh) ≥ 0 (WP5v2-C2d), so the stated "lower bound" has
  the inequality the wrong way round.

### 6.3 L22: displacement threshold and defect energy loss
- **Source [FT].** 1805.09942 Eq. (1): Ê = E(1 − f). Eq. (4): f_DF = 1 − (1−f)/(1−f_sur) = (6.08 ± 0.18)% at 103 keV ²⁰⁶Pb in Ge. TRIM maps
  this to E_d = 19.7^{+0.6}_{−0.5} eV, with "TRIM predicts a monotonic, decreasing relationship between the percent energy lost to defects …
  and E_d". 2301.06592 Eq. (8): R(t) = ∫_{4π}∫_{E_th(θ,φ)} d²R/dE_rdΩ_r, with E_th(θ,φ) from the MD E_d surface (17.5–77.5 eV in Si).
- **URF chain.** 1. Seed (W9). 2. (W3), ion type, first moment of E_st and N_FP. 3. E_d from (W10) on E^ad_0. 4. Truncations: E^ad_0 → empirical
  potentials (SW, Tersoff; the source of the reported 7–30 eV Ge spread); drop the R_I(0) sampling (zero-point/thermal) and the IA Doppler
  spread, which makes the step sharp; NRT/Kinchin–Pease counting N_FP^{NRT} ≈ 0.8E_dam/2E_d (E_dam the damage energy) with stored energy per
  defect E_st,1, so f_DF ≈ p_surv·0.4(E_dam/E_R)E_st,1/E_d (p_surv the survival fraction) [E]; this reproduces TRIM's decreasing f_DF(E_d) at
  fixed E_st,1. 5. 2301.06592's additional assumption, ionization threshold = E_d, is **not** a URF limit: the ionization threshold is the
  §3.3 kinematic or Landau–Zener threshold. In a calorimeter E_d produces a heat **deficit** E_st, not a threshold (W11).
- **Validity.** BO-MD is controlled at E_R ~ E_d: ξ_Mas ≈ 15, λ_dB ≈ 0.01 Å (WP5v2-C6, C17), no electronic excitation (C5). The empirical
  potential is the dominant error. The thermal and zero-point step width is ~1 eV (WP5v2-C7).
- **Leading URF corrections.** (a) A smooth P_FP(E_R, r̂_R) with width σ ≈ √(E_d⟨ω⟩) ≈ 1 eV (Si). (b) Anisotropic E_st(E_R, r̂_R): a daily
  modulation of the **heat** response near E_d, in addition to that of the ionization threshold. (c) Amorphous-pocket stored energy beyond
  isolated Frenkel pairs (2408.07518), which also seeds §4. (d) Post-cascade annealing makes f_DF time-dependent.
- **Discrepancies.** (1) 1805.09942's E_d depends on TRIM's internal stored energy per displacement, not stated. The measured quantity is
  ⟨E_st⟩/E, and its physical carrier is the formation energy, not E_d. (2) 2301.06592 Eq. (6) writes v_min = √(2m_nE_r)/(2μ_{m_D−N}); m_n must
  be the nucleus mass, while the same symbol labels the nucleon in μ_{m_D−n} (Eq. (5)). (3) Ionization threshold = E_d (2301.06592) conflicts
  with Si QF data non-zero down to ~0.7 keV but not with a threshold at E_d; in the URF the two thresholds are physically distinct.

### 6.4 L23: Fano factor F_eh and ε_eh
- **Source [FT].** 2004.10709 Eq. (3): F = σ²/n_eh = σ²ε_eh/E_r (Fano's definition). Eq. (16): ε_eh = C·E_g + E_r, C ≈ 2.2–2.9 (the Klein form;
  here E_r = phonon losses). Measurements at 5.9 keV, 123 K: F = 0.119 ± 0.002, ε_eh = 3.749 eV (2004.11499 [FT]). Model value F_∞ = 0.115
  (2004.10709 [FT]).
- **URF chain.** Second moment of (W3) with an e–h seed. With (W4) and E_st = E_esc = 0:

  F_eh = Var(ℋ)/(E_g² n̄) = (ε_eh/E_g − 1)·𝔡_H,   𝔡_H ≡ Var(ℋ)/(E_g⟨ℋ⟩),   ε_eh = E_g + ⟨ℋ⟩/n̄   [D, exact given (W4); WP5v2-C3].      (W14)

  **F_eh and ε_eh are the first two moments of the heat partition.** Truncations:
  - (i) Klein limit: no phonon loss during ii; residual KE uniform in k with √E DOS below E_th^{ii} = (3/2)E_g (parabolic, equal masses).
    Then ε_eh = E_g + 2·(3/5)E_th^{ii} = (14/5)E_g (WP5v2-C4a): Eq. (16) with C = 2.8; the phonon term rω₀ is Eq. (16)'s "E_r".
  - (ii) Independent residuals would give F_eh = 54/175 ≈ 0.31 (WP5v2-C4b), 2.6× the data. **The energy constraint and the anti-correlation
    between sibling residuals are the leading physics of F_eh**, not a small correction.
  - (iii) Phonon shot noise, Var(ℋ) ≈ ω₀⟨ℋ⟩, gives F_eh ≈ (ε_eh/E_g − 1)ω₀/E_g = 0.121 for Si (ω₀ = 63 meV, E_g = 1.16 eV at 123 K) and 0.155
    for Ge (ω₀ = 37 meV) (WP5v2-C19) [E]. The Si agreement may be accidental. Ge reference values ~0.11–0.13 [UNVERIFIED].
- **Asymptotics: F_eh is a moment, not a parameter [D, renewal theorem for (W3) with (R-k)].** n̄(ω) = ω/ε_eh + b_N + o(1), Var N_eh =
  F_ehω/ε_eh + O(1); ε_eh and F_eh are computable functionals of (W1)–(W2). Near threshold F_eh(ω) is not constant: 0 for ω < 2E_g, with
  structure set by (W8).
- **Nuclear-recoil Fano [D under conditional independence of the cascade given E_el].** F_NR = F_eh + Var(E_el)/(ε_eh⟨E_el⟩) (WP5v2-C12b;
  with the §3.3 caveat that ε_eh must be the NR-seed conversion, not ε_eh^γ). At 25 keV in Si, Lindhard gives ⟨E_el⟩ ≈ 9.1 keV (WP5v2-C12a).
  F_NR ≈ 24 (2206.13639 [ABS]) then requires σ(E_el)/⟨E_el⟩ ≈ 10% (WP5v2-C12c) [E]: the second moment of the Lindhard partition, a computable
  target for §3.4.
- **Validity.** (W14) needs carriers to thermalise at the band edges with no trapping before counting, no photon escape, and E_st = 0 (ER).
  The asymptotics need ω ≳ 50 eV.
- **Leading URF corrections.** The finite-ω structure F_eh(ω) from (W8); then measurement thinning F_meas = ϵ_detF_eh + 1 − ϵ_det (WP5v2-C2),
  which corrects R&K App. A; then trapping (N_trap) and exciton or luminescence escape via (W4).
- **Discrepancies.** As §6.2(4). Also the R&K model F ≈ 0.115 sits below the skipper-CCD 0.119 ± 0.002; with exact thinning ϵ_det ≈ 0.995
  would reconcile them (WP5v2-C2c) [E].

---
## 7. Status of the WP0 defects found in v1 (now adopted in WP0-v2; flag F3)
| v1 ID | Defect | WP0-v2 status |
|---|---|---|
| WP5-1 | v1 WP0 (7.3) second formula integrated q out before seeding | adopted: WP0-v2 (7.3) = (W6) |
| WP5-2 | v1 WP0 (7.3) single-operator weight | adopted: tr[𝔇S(q,ω;Λ)]/tr[𝔇S(q,ω)] in WP0-v2 (7.3) |
| WP5-3 | v1 WP0 (7.1) plasmon label next to RPA cvk pairs double counts | adopted: WP0-v2 (7.1), L11; CONVENTIONS §13 item 21 |
| WP5-4 | R&K called the Λ-marginal kernel | adopted: WP0-v2 (7.3), L21 (photon-seed fit; θ_seed) |
No new WP0-v2 defect is found. WP0-v2 is consistent with this return on (7.1)–(7.3), (5.5), Theorem D sectors and the L20–L23 pointers
(WP0-v2 (9.7) lists L20–L23 with the source equations quoted in §6 here).

---
## 8. Uncertainty hand-over (WP6)
Nuisances are increments Δ^τ_k entered with WP6's positivity-preserving types (WP0-v2 (8.1); CONVENTIONS §11), not v1's additive increments.
They act on P_casc(N_eh|Λ; θ) (the continuous yield model WP6 O6-3 asks for), one θ per physics item, shared across targets where the physics is:
| θ | Increment | Type | Size / prior |
|---|---|---|---|
| θ_seed | photon (q ≈ 0) vs DM seed, computed as a difference at n_gen = 1 | Δ (until computed), then M | R&K envelope, ≤ 50% in p_2 at 4–8 eV [E] |
| θ_{R-k} | (R-k) vs k-resolved n_gen = 2 on a subset (gap R2) | M | computed |
| θ_GW | GW vs vertex-corrected ii rate in (W1) | M | ±20% [E] |
| θ_exch | exchange on/off (Theorem C(d)) | M | computed |
| θ_Eg | ZPR band edge (L12) | E (energy shift) | σ_E from the ZPR uncertainty |
| θ_𝔉 | Fano term in non-PT targets (W15) | A on P (sign-free, Σ_ν𝔉_ν = 0) | |ΔP| ≤ 0.11 Γ/δ (GaAs) [E]; 0 for Si, Ge |
| θ_PES | MLIP vs empirical vs DFT E_d, E_st | Δ / M | spread of the three |
| θ_LZ | TDDFT functional for the Landau–Zener channel (gap R3) | M | functional spread |
| θ_esc | escape and trapping (E_esc, N_trap) | M | per detector |
Two exact constraints restrict them. (W4) ties θ_GW and θ_{R-k} to ε_eh and F_eh: the measured ε_eh and F_eh at 5.9 keV constrain a linear
combination of the two. (W13) does the same for η_pb. WP6's discrete yield-model choice {step, R&K, URF} (WP6 table, type Δ) is kept until
the URF cascade is computed; then it is replaced by the θ above (I4 closed: WP6-v2 writes ε_eh).

---
## 9. Exact remaining gaps
- **R1.** The quasiparticle (BTE) definition of the ii rate near threshold, where 0812.2923 Eqs. (1) and (5) differ. An NEGF/Kadanoff–Baym
  treatment of the three-QP final state would settle it. Size: |Eq.(1) − Eq.(8)|/Eq.(1) of 0812.2923, through Z_{kn} and W versus W_R.
- **R2.** The (R-k) error O(Γ_E/Γ_k) has no proven bound below ~1 eV above threshold, which is where p_2 is decided.
- **R3.** The close-collision excitation kernel dP/dω_e(b_imp, E_coll) relies on adiabatic-XC TDDFT, whose gap and level-crossing errors are
  uncontrolled. G3's charge channel below E_R,th rests on it.
- **R4.** Triggered (avalanche) annealing at T ≪ T_× and the e^{−E/E_slope} spectrum are [C].
- **R5.** (Narrowed.) The case-I seed for ω ≈ 2Δ_BCS–3Δ_BCS is WP4 [4.6]; what remains is its GRPA-vertex size at q ≲ 1/ξ_coh (WP4).
- **R6.** Excitons (E_x^b), shallow-dopant trapping and indirect-gap luminescence escape enter (W4) and (W11); not computed here.
- **R7 (new).** The exact 𝔉_{Λ₀,ν} in GaAs needs the response code's export (O4-d7, WP3); (W15) is a bound with an [E] phase.

---
## 10. Interface flags
| # | Owner | Quantity | Recorded form | Mismatch / action |
|---|---|---|---|---|
| I1 | WP4 | pair-breaking efficiency | WP4-v2 §4.6 η_pb = Δ_BCS⟨N_qp⟩/ω | **CLOSED** (audit A11): WP4-v2 dropped the factor 2; equals (W13) |
| I2 | WP2 | IA width for the MD seed; GS f-sum; ρ^{ph}_κ sign | WP2 (5.3), σ_ω² = 4E_RE^kin_q̂; WP2-v2 IF-2 | adopted in (W9); v1's harmonic ⟨P²⟩ is its harmonic limit. IF-2 (drag-mass subtraction, ω′ < 0 = absorption) applied in §3.1; GS rename done in WP2-v2 |
| I3 | WP1 (via WP0-v2 F1) | pair-resolved external weight | WP1-v2 [E2] out-state form | **CLOSED** (audit A11): WP1-v2 adopted the retarded out-state weight = WP0-v2 (7.2) |
| I4 | WP6 | yield model | WP6-v2, ε_eh | **CLOSED** (audit A11): WP6-v2 writes ε_eh; replace the discrete yield models by the §8 θ's once the cascade exists (WP6 O6-3) |
| I5 | WP3 | X+ joint seed | WP3-v2 §8 joint density of (E_e, E_h) | **CLOSED** (audit A11): renamed in WP3-v2; used as recorded via WP3 (W.1) |
| I6 | WP3, O4 | 𝔉 export | O4-d7 | needed for any GaAs pair-resolved P(N_eh) outside the window; bound (W15) meanwhile (F8) |
| I7 | NOTATION | E_e, E_h | NOTATION row "E_e, E_h" (from WP0-v2 F10) | **CLOSED** (audit A11): row added |
| I8 | CONVENTIONS / WP0-v2 | total-charge response | CONVENTIONS §6 S_chch (ch = c); WP0-v2 (5.4) S_zz | same object (|c⟩ ∝ |z⟩); this return writes S_cc. No content mismatch |

---
## 11. Contested corrections
None. Every owed correction to WP5 (CORRECTIONS §0, §11; WP0-v2 F2, F3, F6, F8, F11) is applied as stated.

---
## 12. Corrections applied (closing table)
| # | Correction (ID / source) | Where applied | How |
|---|---|---|---|
| 1 | Missing "Symbols introduced/used" table (CORRECTIONS §11 row 1; NOTATION-APPLY D8) | §14 | table added; no deviations |
| 2 | W → W^{scr}; v_p → v_C(p) (CORRECTIONS §11 row 2, §0) | (W1), §1.1(c)–(d), §2 | renamed; S_zz → S_cc per CONVENTIONS §6 (I8) |
| 3 | G_x(s), s → 𝔊_x(ϑ), ϑ; K_c → 𝒦_c; g → n_gen; H → ℋ (§11 row 3) | (W3)–(W5), §1.1(b), §2 | renamed |
| 4 | P(E) → dE/dt|_ph; g_κ(ω′) → D_κ(ω′); σ_ω kept (§11 row 4) | (W8), (W9) | renamed; (W9) now uses WP2's E^kin_q̂, D_κ only in its harmonic limit |
| 5 | Q_h → Y_H; E_b, g(E_b), k_ij, T_c, n_i, S_i, S_inst → E_bar, 𝒩_b, Γ_ij, T_×, N_i, 𝔰_i, 𝒮_inst (§11 row 5) | (W11), (W12), §4 | renamed |
| 6 | η → η_pb / ϵ_det; η̄ → E_el; ε → ε_eh; ε_γ → ε_eh^γ; D → 𝔡_H; F → F_eh; b → b_N; ε (Lindhard) → 𝓔_red; k → k_L; W(ε) → σ²_strag; W ≈ 12 eV → B_h; ξ → ξ_Mas; S_e → S^{stop}_e; p_n → P_n; Φ_t → 𝒰_t; labels → WP5-… (§11 row 6) | (W13), (W14), §3, §5, §6 | renamed; source quotes keep source symbols with a dictionary line |
| 7 | G (Theorem D sector) → GS (CORRECTIONS §0; CONVENTIONS §10, §13 item 18) | §3.1, L20 | GS, S^{GS}_κκ |
| 8 | Carrier energies ε_e, ε_h → E_e, E_h (CORRECTIONS §0) | §1.3, §2, (W5) | renamed; NOTATION row now present (I7 closed) |
| 9 | Δ (SC gap) → Δ_BCS (CORRECTIONS §0) | §5, (W13) | renamed |
| 10 | Theorem C(c) must cite the four Coulomb-line classes (WP0-v2 F2) | §1.1(c) | external/ionic/DFPT/pair classes applied to the carrier diagram; pair class = phonon-assisted ii, a stated truncation |
| 11 | Size of the Fano term 𝔉 in GaAs (WP0-v2 F8) | §1.5, (W15), §8 θ_𝔉, R7 | rigorous TV bound [D] + GaAs estimate |ΔP| ≲ 0.11 Γ/δ [E]; WP5v2-C14 |
| 12 | Static DFPT error O(ω_Q²/E_g²), not O(ω_Q/E_g) (WP0-v2 F11) | (W2) | stated |
| 13 | Final-state labels consistent with WP0-v2 (F3) | §1.1(a), §7 | stated; v1 WP0 defects marked adopted |
| 14 | Multiphonon S^{GS}_κκ and ρ^{ph}_κ used as recorded (WP0-v2 F6) | §1.3, §3.1, (W9) | WP2 (3.6), (5.3) forms adopted; I2 |
| 15 | Pair-resolved seeding with the retarded out-state weight (WP0-v2 §10 CC-1, F1) | §1.1(b), §1.3, §2 | (7.2) in (3.2) order; I3 |
| 16 | Nuisances by WP6 types, not additive (CONVENTIONS §11, §13 item 13; WP6-W2) | §8 | M/A/E/Δ per θ; θ_k → θ_Rk, θ_W → θ_GW, θ_X → θ_exch (label clashes) |
| 17 | O4 hand-on to WP5: C-code conditions B1, B2, d2, d3, d6, d8–d10 (WP0-v2 (7.3) hand-over; O4 §6) | §1.5, §2 | listed as hard requirements |
| 18 | Literature tag [UNVERIFIED] for from-memory values (CONVENTIONS §12) | §3.2, §6.4, §1.5 | formation energies, Ge Fano, GaAs form factors, ω_LO |
| 19 | Label prefixes (CONVENTIONS §14) | throughout | WP5 (Wn), WP5v2-Cn, WP0-v2 (s.n), O4-dn, WP3 (W.n) |
| 20 | v1 WP0 equation numbers → WP0-v2 (x_R: Table 6.1; (5.5) classes; (6.1) Theorem D; (7.1)–(7.3); (8.1)) | throughout | re-cited |
| 21 | NOTATION compliance beyond CORRECTIONS §11: v (ion) → v_N; Z_1 → Z_κ; M → M_κ; p_I, p_0 → P_I, P₀; n_κ(p) → 𝔫_κ; N_κ/V → 1/Ω (WP2 (5.3)); Ω (SC phonon) → ω′, Ω_D → ω_D; Ω̂ → r̂_R; V_BO, V_i → E_BO, E^{conf}_i; E_f(V) → E^{form}_V; α (spectrum slope) → 1/E_slope; τ_l/τ_pb → Γ_pb/Γ_esc; d → d_film; T_dam, N_d, ε_st, ξ_surv → E_dam, N_FP^{NRT}, E_st,1, p_surv; M_D, M_E → M^{dir}, M^{exc}; E_x → E_x^b; y_j → x′_j | §1–§6 | renamed (each old symbol collided with a v3 row) |
| 22 | WP3 N3 calibration rule (Y_tot) not cited in v1 | §3.1 | added |
| 23 | Seed for ω ≈ 2–3Δ_BCS now given by WP4 [4.6]; conserving GRPA (L15) | §5, R5 | adopted; R5 narrowed; I1 |
| 24 | Self-found: electron → Si maximum transfer at 10 eV is 0.78 meV, not 1.5 meV | §4 | corrected (WP5v2-C11); conclusion unchanged |
| 25 | Self-found: checks used scipy (dblquad), against the sympy-only rule | code/WP5-v2/checks.py C1b | exact Dirichlet integral (π/8 × 16/105) |
| 26 | Self-found: 2007.14289 was tagged [FT] in v1 §3.4 but listed abstract-only in v1 §10 | (W11) | tag [ABS] |
| 27 | WP2-v2 IF-2 (coordinator relay): (a) subtract the Migdal drag-mass energy E^{Mig}_1 from the GS f-sum when Migdal is seeded separately; (b) ω′ < 0 in ρ^{ph}_κ = absorbed phonons | §3.1 (i), (ii) | (a) GS first moment q²/2M_κ − E^{Mig}_1, zeroth depleted by P_Mig; (b) created/absorbed split, ℋ = net ω; WP5v2-C20a,b |
| 28 | Audit A11 (coordinator): flags I1, I3, I4, I5, I7 stale after WP4-v2, WP1-v2, WP3-v2, WP6-v2 and NOTATION updates | §1.3, §5, §8, §10, §14 | marked CLOSED; the WP4 [4.6] factor-2 sentence deleted; WP5v2-C15b relabelled as a closed-flag record |
| 29 | NOTATION v4 renames (CORRECTIONS §17) | §1.1(d), §1.4 (W7)–(W8), §3.2, §4, §5, §6.1, §6.3, §8, §9 R5, §14 | M^{dir}, M^{exc} → M^{ii}_{dir}, M^{ii}_{xch}; E_BO → E^ad_0; ξ_BCS → ξ_coh; E (local carrier energy) → E_car (E′ → E′_car); θ_Rk → θ_{R-k}; rows 16, 21 keep the old names as history; §14 updated to v4. Notational only |

**Count:** 28 corrections applied (18 owed by CORRECTIONS/WP0-v2 flags/CONVENTIONS/WP2-v2 IF-2/audit A11, 7 consistency or interface items, 3 self-found);
0 contested. Interface flags: 8 (I1–I8); I1, I3, I4, I5, I7 CLOSED (audit A11); open: I2 (applied here), I6 (𝔉 export), I8 (S_cc ≡ S_zz);
none is a content mismatch. Row 29 (NOTATION v4 renames) is notational and outside this count.

---
## 13. Literature (IDs verified against the arXiv API in v1, 2026-10-31; not re-read here)
- Full text read (v1): 2004.10709 (R&K, Eqs. (1)–(23)); 2209.04503 (Eqs. (1)–(4)); 2001.06503 (Eqs. (1)–(22)); 1805.09942 (Eqs. (1)–(4), §V);
  2301.06592 (Eqs. (1)–(8)); 0812.2923 (Eqs. (1)–(9)); 1401.1937 (Eqs. (1)–(5)); 2506.03810 (Eqs. (3)–(4)); 2004.11499 (results).
- Abstract or title only: 2408.07518, 1703.05371, 2603.16702, 2405.10405, 2206.13639, 2112.14495, 2210.01557, 2007.14289, 2503.03683,
  2406.15425, 2104.01811, 2101.08263, 2002.06937, 2003.12077, 2306.14944.
- Campaign sources used as recorded: WP0-v2; WP2 (3.6), (5.2), (5.3); WP3 (W.1), N3; WP4 [4.6], L15; WP6 §5–§7, O6-3; O4 (O4.7), d1–d11.
- Not on arXiv (cited by content): Lindhard et al. 1963; Fano 1947; Klein 1968; Kaplan et al. 1976; Chang–Scalapino; Cohen–Bergstresser 1966
  [UNVERIFIED values]. Text extracts from v1 remain in literature/papers-WP5/ (extractor code/WP5/html2txt.py).

---
## 14. Symbols introduced/used
All symbols follow NOTATION v4 and CONVENTIONS; **no deviations** (v4 renames: CORRECTIONS §17, closing-table row 29). Source formulas in §1.1(d), §6 keep their own symbols, with the campaign
translation stated in each source line (NOTATION §K).
*Used as defined in NOTATION v4:* q, ω, ω_q, v, ρ_χ, f_χ, m_χ, ρ_T, Ω, N, V, 𝔇, ℛ, α, e, v_C, k, k′, n, m, v, c (band subscripts), ε_{nk},
ψ_{nk}, f_{nk}, E_g, E_dir, E_th, ρ_{mn}, ρ̃, Q, ν, ω_{Qν}, n_{Qν}, g_{mnν}, g^S, g^L, ω₀, ⟨ω⟩, ω_max, D_κ, 𝔫_κ, E^kin_q̂, 𝔨₃^{GS}, x_R, M_κ,
Z_κ, A_κ, F^M_κ, c_s (c_κ), z_s, 𝓃_e, P_I, R_I, I, κ, v_N, U_κ/Z_κ(p), S, S_ab, S_cc (= S_chch, ch = c), S(q,ω;Λ), R, ε, ε̃, ε^{-1}_{GG′}, ε_∞,
L, W^{scr}, Z*_κ, ω_p, ω_pl, E_x^b, GS, X0, X+, X, Λ, Λ₀, Λ₊, Ẽ_Λ₀, Γ_Λ₀, Γ^{ph}, Γ^x, Γ^{tot}, Γ^{(f)} (as Γ^{(ν)}), Σ^{FM},
a^{off}, 𝔉_{Λ₀,ν}, c_ν^F (O4's Im(ρ*a^{off}); c̄^F its Γ-weighted mean), 𝒦_{Λ₀→Λ₊}, δ, δ₀, DC, fp, τ, 𝒳, K, n_g, θ_k, Δ^τ_k, σ_E;
N_eh, N_eh^{step}, P_casc, P(N_eh|q,ω), P_n, 𝐍, ℋ, E_st, E_esc, E_d, N_FP, N_trap, 𝔊_x(ϑ), ϑ, 𝒦_c, Γ_ii, Γ_E, Γ_k, dE/dt|_ph, p_no-ii, ε_eh,
ε_eh^γ, F_eh, F_NR, F_qp, F_meas, 𝔡_H, ϵ_det, b_N, E_el, 𝓔_red, k_L, ν̄_L, σ²_strag, U_bind, Y_H, Y_tot, Y_casc, E_R, E_R,th, σ_ω, ξ_Mas, B_h,
E_bar, 𝒩_b, Γ_ij, T_×, N_i, 𝔰_i, 𝒮_inst, S^{stop}_e, 𝔅₀, 𝒰_t, P_FP, N_qp, η_pb, t_esc, E_sub, E_excess, n_gen, Δ_BCS, 𝔤_I, v_F, k_F, ω_e,
ω_ph, n_ph, s^ph, δM_κ, E^{Mig}_1, E_e, E_h (NOTATION §G, added after WP0-v2 F10), P_Mig, ρ^{ph}_κ, T, β.
*Introduced here (new names, no collision; now NOTATION v4 §M rows):*
| Symbol | Meaning | Where |
|---|---|---|
| 𝔱 | cascade particle type (e, h, phonon, ion, core hole) | (W3), (W7) |
| x′_j | child states of a cascade vertex | (W3), (W5) |
| E_car | carrier energy above its band edge (local variable; v3 name E) | (W7), (W8) |
| E_th^{ii} | impact-ionization threshold | §1.2, (W8), §6 |
| 𝒦̄_𝔱 | iso-energy-averaged kernel | (W7) |
| M^{ii}_{dir}, M^{ii}_{xch} | direct and exchange ii amplitudes (0812.2923 "M_D, M_E"; v3 names M^{dir}, M^{exc}) | §1.1(d) |
| E^ad_0(R), E^{conf}_i | BO ground-surface energy (v3 name E_BO, = WP2-v2 E^ad_0); energy of defect configuration i | §3.2, §4, (W12) |
| r̂_R | recoil direction | (W10), (W11) |
| λ_dB, ℓ_int | de Broglie wavelength; interaction length in ξ_Mas | §3.2 |
| t_pr | prompt (pre-annealing) time for E_st | §3.2 |
| E^{form}_V, E^{form}_I | vacancy, interstitial formation energies | §3.2 |
| h_LZ, ΔF_LZ, P_LZ | Landau–Zener coupling, slope difference, transition probability | §3.3 |
| b_imp, E_coll | impact parameter, collision energy (TDDFT) | §3.4 |
| V_bias | NTL bias voltage | (W11) |
| ℛ_rel | relaxation-event rate (decorated ℛ) | (W12) |
| ω_bar, Γ_att | barrier-top curvature frequency; attempt rate | §4 |
| E_slope | slope of the release spectrum e^{−E/E_slope} | §4 |
| α²F(ω′) | Eliashberg function (one symbol; not the bare α) | §5 |
| E₁, E₂ | quasiparticle energies of a BCS pair seed (WP4 [4.6]) | §5 |
| Γ_pb, Γ_esc, d_film, ω_D, ξ_coh | pair-breaking rate, phonon escape rate, film thickness, Debye energy, coherence length | §5, R5 |
| N_FP^{NRT}, E_dam, E_st,1, p_surv | NRT displacement count, damage energy, stored energy per FP, survival fraction | §6.3 |
| θ_seed, θ_{R-k}, θ_GW, θ_exch, θ_Eg, θ_𝔉, θ_PES, θ_LZ, θ_esc | WP5 nuisances (θ_k family) | §8 |
| a₀ | Bohr radius (source quote 2001.06503) | §6.1 |
Labels: WP5 (W1)–(W15), WP5v2-C1…C20, R1–R7 (as WP5-R1…), I1–I8 (interface flags), (R-k), (CSDA), (B1)–(B3) (as WP5-B1…; O4's are O4-B1, O4-B2).
