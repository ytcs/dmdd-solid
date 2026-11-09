# R13 / WP5-v4: energy partition and measured quanta (WP5-v3 with the WP7-E-v3 amendment A-1…A-16 applied)

Revision agent, brief R13/WP5-ERR. Supersedes returns/R8/WP5-v3.md (v3), which stays as the historical record; this version reads without it.
**Change source.** The "Amendment to WP5-v3" A-1…A-16 of returns/R12/WP7-E-v3.md §5 (refereed R×2 in R11, verified R12 VER ×2 and VER2 ×2), applied
in place, in the order of the v3 text. Where an A-item conflicts with v3 text, WP7-E-v3 wins; every such conflict is listed in **§R13.1**, the
A-item → location map is **§R13.2**, the consistency checks against WP7-T-v2 Theorem T-1 (conditions (i)–(v)) and WP6-v3 (nuisance types) are
**§R13.3**, and the new checks are **§R13.4**. **Energy convention** (coordinator, CONVENTIONS §13 row 23): stored energies are configurational,
E^{conf}_i ≡ E^ad_0(R_i), and the zero-point change ΔZPE is carried inside the phonon reservoir ℋ_ph = ℋ_ph^{avail} + ΔZPE. **Names.** WP7-E-v3's
local symbols are written in their NOTATION names ("Rows added WP7-E"; state/CORRECTIONS.md §18): κ → κ_cal, X → X^{oth}, g → g_Luke, y → y_ion,
δ → δ_coll, r → r_coll, r_c → r_cap, σ(u_car) → σ_cap, 𝔵 → 𝔮, m(r) → m_ind(r), E_x ≡ −N_XE_x^b → ΔE_X^b, ε (1803.02903 pair energy) → ε_eh; WP7-T-v2's
ε_ij → ε^{hop}_ij. Borrowed labels carry their return prefix (CONVENTIONS §14): "WP7-E-v3 (E1)", "WP7-T-v2 (5.3)". Text inserted from the
amendment is marked **[A-n]** (in the §R13 tables and closing sections "A-n" always means the amendment item of WP7-E-v3 §5; in the
kept v3 text and §R8 tables a bare "A-n"/"B-n" is still an R7 referee verdict); v4 annotations that go beyond the amendment text are marked **[v4]** and are listed in §R13.1/§R13.3.
**Checks.** `code/WP5-v4/checks.py`: code/WP5-v3/checks.py with C1–C30 unchanged (cited WP5v3-Cn as before) plus **WP5v4-C31…C43** for the changed
equations (sympy + mpmath; **75/75 PASS, ≈ 55 s**). **Literature.** Every arXiv ID the amendment touches (1803.02903, 1805.09942, 2007.14289,
2202.05097, 2208.02790, 2209.04503, 2405.10405) and the main v3 sources (2004.10709, 2001.06503, 2004.11499, 1401.1937, 2301.06592, 0812.2923,
2506.03810, 2408.07518), and the remaining v3 abstract-level citations (1703.05371, 2603.16702, 2206.13639, 2112.14495, 2210.01557,
2503.03683, 2406.15425, 2104.01811, 2101.08263, 2002.06937, 2003.12077, 2306.14944, 2105.05253, 2603.12326), 29 IDs in all, verified against the
arXiv API (literature/papers-WP5-v4/arxiv-*.json; all exist with matching titles). 1803.02903, 1805.09942 and 2007.14289 re-read in
full text for R13 (page numbers = PDF pages; PDFs deleted). Status: CLAIMED; v3 REFEREED (R7) and the amendment REFEREED with WP7-E; the merged
text awaits the R13 joint audit (WP5-AUD). The v3 §10 (interface flags) and §14 (symbols) now sit in the closing sections "Interface flags" and "Symbols
introduced/used", which, with "Proposed LIMITS rows", end the return.

**v3 preamble (kept).** Revision agent, brief R8/REV3-WP5. Supersedes returns/R6/WP5-v2.md (v2) and returns/R5/WP5.md (v1), which stay as the historical record;
this version reads without them. Inputs applied: referees/R7/REF-WP5-A.md (cited **A-n** = its verdict V*n*) and REF-WP5-B.md (**B-n**);
state/SOTA.md "R7 referee reports" cross-package notes (cited **SOTA-R7**). Conventions: CONVENTIONS.md; symbols: NOTATION v4;
architecture: returns/R6/WP0-v2.md, cited **WP0-v2 (s.n)**. Checks: `code/WP5-v3/checks.py` (sympy only, exact arithmetic, **55 checks,
all PASS, ~3.5 s**), cited **WP5v3-Cn**. C1–C20 keep their v2 subject; the checks the referees called vacuous or wrong are replaced
(C1c, C2d, C5, C6, C7b, C14e, C18, C20b, C20c; v2 C14e's bare arithmetic is dropped); C21–C30 check the new R8 derivations. Tags: **[D]** DERIVED
(hypotheses stated), **[D, sketch]**, **[E]** ESTIMATED, **[C]** CONJECTURED; literature **[FT]** full text, **[ABS]** abstract,
**[UNVERIFIED]** quoted from memory; rubric-(c) literature claims carry the R7 rating **CONFIRMED / UNRESOLVED** (REFUTED ones are
dropped, §13.1). Equations **WP5 (W1)…(W15)** keep their v2 objects; (W1), (W7), (W15) are restated with the R7 corrections and (W3) gains
the hypotheses (H-t), (H-m); (W1′), (W16), (W17) are new. Units: ħ = c = k_B = 1, e² = 4πα, v_C(k) = e²/k². Status: CLAIMED, refereed R×2 (R7), corrected here. **§10** holds the interface flags; **§R8.1–R8.3** at the end hold the referee-disagreement settlements, the rebuttals and
the closing table (one row per referee item); **§R9** at the very end is the R9 clean-up table (VER-WP5-A/B new items, AUDIT-2 rows).

---
## 1. The partition-transport stage of the URF

### 1.1 Theorem C: every cascade kernel is a master-formula rate with a target-internal projectile [D]
*Hypotheses.* First order in the screened interaction W^{scr} (GW level), quasiparticle residue Z_qp → 1 (item (d)). The projectile is a
quasiparticle of the target (a Bloch electron or hole in state nk, or a moving ion), distinguishable from the medium's response (exchange
lies beyond these hypotheses: item (d)).
*Statement.* Use WP0-v2 (3.3) with the DM replaced by the projectile. A Bloch carrier couples to the **total** charge, so its coupling vector
is |c⟩ ∝ |z⟩ (CONVENTIONS §7) and its response is S_cc (written S_zz in WP0-v2 (5.4)). Its vertex is 𝒱(p) = v_C(p) ρ_{n′n}(k,−p), where
p = q_r + G is an unrestricted loop momentum (NOTATION §B) and the carrier goes nk → n′, k−p. WP0-v2 (5.4) then gives

  dΓ_{nk→n′}(p)/d³p = (2π)^{-3} |v_C(p) ρ_{n′n}(k,−p)|² S_cc(p, ω) [1 − f_{n′,k−p}],   ω = ε_{nk} − ε_{n′,k−p}   (final state n′, k−p),
  ⇒ Γ^{out}_{nk} = Σ_{n′} ∫d³p/(2π)³ 2 v_C(p) |ρ_{n′n}(k,−p)|² Im[−(ε^{-1})_{00}(p,ω)] [1 − f_{n′,k−p}][1 + n_B(ω)].                 (W1)

(1/(1 − e^{−βω}) = 1 + n_B(ω), WP5v3-C22.) The first line is the **differential** rate into the final state labelled by p (B-1(iii)); the
total is its integral. S_cc = (2p²/e²)L/(1 − e^{−βω}) gives |𝒱|²S_cc = 2v_C(p)|ρ|²L/(1 − e^{−βω}) (WP5v3-C13).
**(W1) is the out-scattering rate Γ^{out}, which is the cascade kernel [D] (A-1, B-1).** The GW self-energy has the thermal factor
1 − f + n_B = (1 − f)(1 + n_B) + f·n_B (WP5v3-C22), so

  2|Im Σ^{GW}_{nk}| = Γ^{out}_{nk} + Γ^{in}_{nk},   Γ^{in}_{nk} = (W1) with [1 − f][1 + n_B] → f_{n′,k−p} n_B(ω).                         (W16)

The identification "(W1) = 2|ImΣ|" of v2 holds only for f·n_B → 0 (hot carriers at T ≪ E_g, where it is harmless). Holes are written with
hole occupations, so for them f → 1 − f_h before applying (W16).
**Local fields and non-centrosymmetric targets (B-1(ii)) [D].** With WP0-v2's ε⁻¹_{GG′} = δ_{GG′} + v_C(p+G)R_{GG′}, the screened interaction is
W_{GG′} = ε⁻¹_{GG′} v_C(p+G′) (right index), not v_C(p+G)ε⁻¹_{GG′} (WP5v3-C21a). The absorptive kernel is the **anti-Hermitian part**:

  2v_C|ρ|²Im[−ε⁻¹_{00}] → −2 Σ_{GG′} ρ*_G [(W − W†)/2i]_{GG′} ρ_{G′} = −2 Im(ρ†Wρ),   ρ_G ≡ ρ_{n′n}(k,−p−G),                       (W1′)

which is real for any W; the element-wise Im W differs from it when W_{GG′} ≠ W_{G′G}, as in GaAs (WP5v3-C21b; the same issue as WP0-v2 CC-1).
v2's "Σρ*_G v_C(p+G) Im(−ε⁻¹_{GG′}) ρ_{G′}" had both defects and is withdrawn.
**Relation to the GW lifetime (A-1).** 0812.2923 Eq. (1) [FT; CONFIRMED by REF-A] is τ⁻¹ = (2Z/ħ)|ImΣ| with the quasiparticle residue
Z (= Z_qp here) ≈ 0.8 (its item (a) under Eq. (8)). So (W1) equals the GW lifetime only at Z_qp = 1, which is consistent with the first-order
hypothesis but is numerically a **global ~20% factor**, not a near-threshold effect: it is carried by a separate nuisance θ_Z (§8).
**Consequences:**
- (a) **Where the plasmon lies inside the e–h continuum, impact ionization, plasmon emission and plasmon decay are a single channel**, the
  e–h part of Im[−1/ε] = ε₂/|ε|² (B-3). The plasmon is then a peak of ε^{-1} (L11) carried by e–h weight (ε₂(ω_pl) > 0: Si, Ge, GaAs, where
  ω_pl ≈ 16 eV lies in the interband continuum), not a separate cascade species; its decay products are the cvk pairs of WP0-v2 (7.2) at
  (p, ω). (Adopted by WP0-v2 (7.1) and CONVENTIONS §13 item 21.) **Restriction [D]:** for an *undamped* pole (nearly-free-electron metal,
  RPA, q < q_c, e.g. Al) the pole carries no e–h weight at ω = ω_pl at that order; as q → 0, Im[−1/ε] = (πω_p/2)δ(ω − ω_p) carries the whole
  f-sum (WP5v3-C27), while at finite q < q_c the Lindhard continuum below qv_F shares it (VER-WP5-B N4). The plasmon is then a
  genuine final state, cascade type 𝔱 = pl, with its own decay kernel (interband ε₂ at (q, ω_p), Landau damping beyond q_c, or two-pair
  decay); §5 treats Al this way. Interface flag IF-R8-3.
- (b) **The secondary-pair distribution is the WP0-v2 final-state-resolved response.** A generation-n_gen carrier creates the pair
  Λ′ = (c′v′k′) with weight S(p,ω;Λ′)/S(p,ω) from WP0-v2 (7.2), with the **retarded out-state** weight (ε̃^{-1})_{G0} in (3.2) order (WP0-v2
  §10, CC-1; required in non-centrosymmetric targets such as GaAs). The cascade is the iterate of the WP0-v2 interface (7.1)–(7.2).
- (c) **Polar materials and the Coulomb-line classes (WP0-v2 (5.5), flag F2).** Apply WP0-v2's four-class topological classification to the
  carrier diagram. *External class* (p+G, ω): resummed once into ε^{-1}(p,ω), including local fields; (W1). *Ionic class*: the ionic part of
  the **total** ε at (p, ω) gives LO-phonon (Fröhlich) emission through (W1) itself. *DFPT class* (Q+G): the screened g. The long-range
  (Fröhlich) part g^L of the DFPT vertex is the same Coulomb line as the ionic class at p = Q + G, so the separate e–ph kernel must use only
  g^S = g − g^L (the EPW split) to avoid double counting. *Pair class*: enters only phonon-assisted ii, O(g²W^{scr}), beyond the first-order
  kernels (W1)+(W2); listed as a truncation (τ: n_g = 0 in the ii kernel). The argument (every line at momentum p resummed exactly once) is
  v1's; only the citation changes from v1's "three channels" to the four classes. (The ionic class is a phonon line at the external
  momentum, SOTA-R7 REF-WP0-A/B; in the carrier diagram that line is the phonon-pole part of ε_tot at (p, ω).) **Caveat (R9, AUDIT-2 m20):**
  WP0-v3 G14 restates the classification as **three** Coulomb-line classes (external, DFPT, pair) plus ionic phonon-bridge insertions; the
  "ionic class" above is that bridge insertion. The counting argument and WP5-cp1–cp3 are unchanged by the relabelling.
  **Code-pair conditions for "counted once" (A-2, B-2) [D: the subtraction is exact only if these hold].** ε_ion(p, ω) in (W1) and g^L
  subtracted in (W2) must be the **same object**:
  - **WP5-cp1** the same Z*_κ, ε_∞ (tensor) and ω_LO, from one response/DFPT run;
  - **WP5-cp2** the same multipole content: if g^L carries dipoles + quadrupoles Q_κ (EPW), ε_ion must include Q_κ too; otherwise subtract the
    dipole g^L only. GaAs must not subtract a quadrupolar g^L that ε_ion lacks;
  - **WP5-cp3** the same range separation: EPW's g^L carries a Gaussian (Ewald) cutoff over G, while (W1) sums the ionic head over all
    p = Q + G. Use the same cutoff in both, or the residual ∝ e^{−|Q+G|²/4α_E} at p = Q + G ≠ Q is double counted.

  These are O4-d2-type requirements on the e–e/e–ph code pair (§1.5, §2).
- (d) **Exchange [beyond the hypotheses of Theorem C] (A-1).** (W1) has no |M_dir|² to correct: it is written with Im W. Exchange needs
  0812.2923's Eq. (7), Im W ≈ W_R Im χ₀ W_R, which replaces Im W by explicit pair amplitudes with W_R and so goes beyond first order in W.
  In that form |M^{ii}_{dir}|² → ½(|M^{ii}_{dir}|² + |M^{ii}_{xch}|² + |M^{ii}_{dir} − M^{ii}_{xch}|²) (0812.2923 Eq. (5) [FT], source "M_D, M_E"; its item (b): Eqs. (1)/(8)
  contain no M_E term). This is an alternative rate definition, not a term "added to (W1)"; it is tagged [beyond hypothesis] and enters
  only through θ_exch (§8). The Eq. (1)/(5) ambiguity (Z_kn, W vs W_R) is gap R1 (§9); the Z factor itself is the global θ_Z above.
- (e) **Slow ions.** An ion of charge form factor Z_κ(k) moving with velocity v_N has no recoil, so ω = k·v_N, and (W1) becomes Lindhard's
  dielectric stopping −dE/dx = (2Z_κ²α/πv_N²)∫dk/k ∫_0^{kv_N}dω ω L(k,ω) (Gaussian e_G² = α in the prefactor; T = 0, ω > 0). This holds
  only in Born. **For v_N ≪ v_F the electrons meet the ion at relative speed ≈ v_F, so the linearity (Born) parameter is Z_κα/v_F, not
  Z_κα/v_N (A-3, B-4)**: Z_κα/v_F ≈ 15 (Si), 35 (Ge) with free-electron v_F (WP5v3-C6b) [E]. It is ≫ 1, so linear-response stopping is not a
  derived limit for keV recoils (the conclusion of v2 stands; v2's number 3.7×10² used the wrong velocity and is withdrawn). The standard
  remedy is nonlinear (DFT) stopping (Echenique–Nieminen–Ritchie [UNVERIFIED]). See §3.3.

The phonon kernel is the EPW golden rule in campaign conventions (CONVENTIONS §5) [D, at O(g²)]:

  Γ^{ph}_{nk→m,k+Q} = (2π/N) Σ_ν |g^S_{mnν}(k,Q)|² [(n_{Qν}+1)δ(ε_{nk}−ε_{m,k+Q}−ω_{Qν}) + n_{Qν}δ(ε_{nk}−ε_{m,k+Q}+ω_{Qν})].           (W2)

g^S is DFPT-screened at ν = 0 (static); its error is O(ω_Q²/E_g²) ≈ 3×10⁻³ (X2; WP0-v2 (5.5); flag F11), not O(ω_Q/E_g). For GaAs, g^S
excludes g^L by (c), under WP5-cp1–cp3; Si quadrupole corrections are included (SOTA R2).

### 1.2 The branching generating functional [D]
*Hypotheses.*
- (B1) Markov: collision durations ≪ time between collisions (Γ ≪ carrier energy scale); no inter-collision coherence. (Distinct from O4's
  (B1)/(B2), which are cited as O4-B1, O4-B2 in §1.5.)
- (B2) Siblings evolve independently: no Pauli blocking and no Coulomb (carrier–carrier, Auger) interaction between cascade particles.
  **This is an assumption whose error is estimated only for small seeds (A-5, B-6).** Two separate conditions [E] (WP5v3-C25):
  - (B2a) Pauli: final-state occupation ≪ 1, i.e. n_pair ≪ (density of states in the ~eV loss window) ~ 10²² cm⁻³ eV⁻¹ × 1 eV. A 1 keV
    deposit (~300 pairs) in a 10 nm-radius sphere gives n_pair = 7×10¹⁹ cm⁻³ (3×10²⁰ cm⁻³ in a 10 nm cube): occupation ≲ 3%. Satisfied.
  - (B2b) Coulomb: n_pair a_X³ ≪ 1 (a_X ≈ 4 nm the Si exciton radius [UNVERIFIED]; the e–h-plasma (Mott) density is ~10¹⁸–10¹⁹ cm⁻³ [E]).
    At 1 keV n_pair a_X³ ≈ 5–19: **violated**. v2's "≲ 10¹⁹ cm⁻³ ≪ 𝓃_e" was numerically wrong (by 7–30×) and used the wrong criterion
    (the valence density 𝓃_e tests neither condition) and is withdrawn.

  Scope: (B2) is used for the eV–100 eV DM-electron seeds of G1 (≲ 30 pairs), where n_pair a_X³ ≲ 0.5 for a 10 nm cloud, a marginal [E]
  rather than a controlled value; for ≳ keV electron deposits and for all NR tracks it is **[C]**, with an unestimated error (nuisance θ_dense, §8).
- (H-t) Almost-sure termination (A-4): every particle reaches an absorbing state in finite time with probability 1. Sufficient: every
  non-absorbing state has a positive net energy-loss rate (true for carriers above E_th^{ii} at T ≪ E_g and for ions above the
  thermal energy).
- (H-m) Minimal solution (A-4): (W3) is solved by the minimal non-negative solution, obtained by iteration from the terminal data. Without
  (H-t) the fixed-point equation has spurious solutions: for a toy branching law f(s) = (1 − p) + ps² the roots are 1 and (1 − p)/p, and the
  termination probability is the minimal one, (1 − p)/p < 1 for p > ½ (WP5v3-C23). Under (H-t) the minimal solution at ϑ = 0 is 𝔊 = 1.
- (B3) Homogeneous medium, no applied field **in the cascade kernels**. **[A-12]** A drift field does work e ℰ_b v_d t_pr per carrier before t_pr
  (≲ 0.25 eV at 250 V/cm, saturated [E]; WP5v4-C40). This is booked in 𝒲_bias and ℋ; the drift is otherwise post-prompt (WP7-E-v3 (E1-pr), (E2),
  (E11)). **[v4]** "No applied field" is read as "the kernels 𝒦_c are field-free" (§R13.1 K5).

*Statement.* A particle state x (cascade type 𝔱 ∈ {e, h, phonon, ion, core hole, **trapped on level j** [A-1]}, band n, k, or ion energy and
direction) evolves through channels c with kernels 𝒦_c(x → x′_1…x′_m); each channel deposits δ𝐍_c, with **[A-2]** "𝐍 = (N_e^f, N_h^f, N_e^{tr},
N_h^{tr}, E_trap^{pr}, ℋ, E_st, N_FP, E_esc, N_X, E_X) (additive). The class 𝔠, r_ev, dℋ/dω_ph(r) and the cloud geometry are marks of
P_casc(𝐍, 𝔪|Λ) (WP7-E-v3 §1.4, (H-E6))." (ℋ = heat.) **[v4]** N_eh ≡ N_e^f + N_X (band electrons, bound or not) is a derived, non-additive
function of 𝐍 (WP7-E-v3 (E1-W4)); P_casc(N_eh|Λ) everywhere below is the corresponding marginal (§R13.1 K4). The generating
functional 𝔊_x(ϑ) = E[e^{ϑ·𝐍} | x] obeys the backward equation

  Γ_x 𝔊_x(ϑ) = Σ_c ∫dx′ 𝒦_c(x→x′_1..x′_m) e^{ϑ·δ𝐍_c} Π_j 𝔊_{x′_j}(ϑ),   Γ_x = Σ_c ∫dx′ 𝒦_c,   𝔊_x = e^{ϑ·𝐍_term(x)} on absorbing states.   (W3)

Proof: first-step analysis of a Markov branching process; condition on the first collision and factorise with (B2); (H-t), (H-m) select
the solution. Kernels: (W1) (= Γ^{out}) for e–e,
(W2) for e–ph, §3 for ions. A carrier whose energy E above its band edge is below the ii threshold E_th^{ii} no longer branches; its remaining
kinetic energy goes to ℋ as it relaxes to the edge. **[A-1]** In (W3) the cascade type "trapped on level j" is reached through the capture
kernel 𝒦_cap (WP7-E-v3 (E9) for t < t_pr: cascade capture for shallow Coulombic levels, multiphonon for deep ones). Deposits are **per carrier**
and additive, each carrier deposited **once**, by its state at t_pr. A carrier at the band edge is non-absorbing until t_pr. If still free at t_pr
it deposits (N_e^f += 1, energy E_c − μ_F) or (N_h^f += 1, μ_F − E_v). If captured before t_pr it deposits only (N_e^{tr} += 1,
E_trap^{pr} += E_c − E^tr_e − μ_F, ℋ += E^tr_e), and likewise for holes, with no N_e^f deposit and no E_g or exciton term for that carrier (WP5v4-C31).
Exciton and droplet formation are two-body processes outside (B2). They are post-prompt (formation times ≳ ns > t_pr) and enter the explicit
reservoir E_X = Σ(E_g − E_x^b) of WP7-E-v3 (E1). **[v4]** So "absorbing" in (H-t) means "at t_pr" for edge carriers (§R13.1 K3).
*Moments.* With m_x ≡ ∂_ϑ𝔊_x|₀, Γ_x m_x = Σ_c∫𝒦_c[δ𝐍_c + Σ_j m_{x′_j}] (linear). Second moments follow from ∂²_ϑ; for one channel step this
is the law of total variance (WP5v3-C9). **The R&K mean yield (L21) and Kinchin–Pease defect counts (L22) are first moments of (W3); F_eh and
F_NR (L23) are second moments; Lindhard's integral equation (L20) is the first moment after the additional binary-collision (BCA) and
Markov-ion-transport truncation 0** (A-6; §6.1).
*Exact energy bookkeeping [D].* Each vertex conserves energy. Assume terminal carriers relax to their band edges and pairs are counted at
E_g, with no capture, no exciton and negligible bias work before t_pr. (v3's exciton rule "E_g → E_g − E_x^b" is withdrawn: excitons are
post-prompt and sit in E_X, A-1; Si E_x^b ≈ 15 meV [UNVERIFIED]. WP5v3-C30 stays as algebra only; §R13.1 K1.) Then

  ω = N_eh E_g + ℋ + E_st + E_esc   (event by event),                                                                               (W4)

where E_esc covers photons and phonons that leave the target. **[A-1]** "(W4) holds with no capture, no exciton and negligible bias work before
t_pr. In general ω + 𝒲_bias(t_pr) = N_e^f(E_c − μ_F) + N_h^f(μ_F − E_v) + E_X + E_trap^{pr} + E_es + ℋ + E_st + E_esc (WP7-E-v3 (E1-pr));
N_eh = N_e^f = N_h^f only without capture." Equivalently (WP7-E-v3 (E1-W4); WP5v4-C31), with N_eh ≡ N_e^f + N_X, ΔE_X^b ≡ −N_XE_x^b and
E_pairs^{unp} ≡ (N_h^f − N_e^f)(μ_F − E_v),

  ω − N_eh E_g − E_st − E_esc = ℋ + E_trap^{pr} + E_es + E_pairs^{unp} + ΔE_X^b − 𝒲_bias(t_pr) ≡ ℋ_eff,   E_pairs^{unp} + E_trap^{pr} μ_F-independent.   (W4′)

Hence N_eh = (ω − ℋ − E_st − E_esc)/E_g under (W4)'s conditions, and N_eh = (ω − ℋ_eff − E_st − E_esc)/E_g in general: **all ionization statistics
are heat-partition statistics** (§6, L23) **[v4: of ℋ_eff when capture, excitons or bias work are present; §R13.1 K2]**.

### 1.3 Seeding and the measured spectrum [D given WP0-v2 (7.1)]
The prompt state Λ of WP0-v2 (7.1) is a set of particles {x′_j}: e at (n_e, k_e, E_e), h at (n_h, k_h, E_h) (carrier energies, NOTATION), phonons with total ω_ph, a recoiling ion with momentum, a core hole. Then

  P_casc(𝐍|Λ) = [coefficient of e^{ϑ·𝐍} in] e^{ϑ·𝐍_prompt(Λ)} Π_{j∈Λ} 𝔊_{x′_j}(ϑ),                                                    (W5)

**[v4]** (W5) is the 𝔪-marginal of P_casc(𝐍, 𝔪|Λ); the marks are read off the same cascade sample (A-2).

  dℛ/d𝐌 = (ρ_χ/m_χρ_T) ∫d³v f_χ(v) ∫d³q/(2π)³ Σ_Λ Σ_ab 𝔇_ab(q,v) S_ab(q, ω_q; Λ) P(𝐌, t|Λ) + dℛ_bg/d𝐌,
  P(𝐌, t|Λ) = Σ_𝐍∫d𝔪 P_casc(𝐍, 𝔪|Λ) 𝒫_det(𝐌, t|𝐍, 𝔪)   (WP7-E-v3 (E3)–(E4)).                                                              (W6)

**[A-16]** (W6) is the observable-level rate. The cascade-level rate dℛ/d𝐍 = (ρ_χ/m_χρ_T)∫d³v f_χ∫d³q/(2π)³ Σ_Λ Σ_ab 𝔇_ab S_ab(q, ω_q; Λ)
P_casc(𝐍|Λ) (= WP0-v2 (7.3), v3's (W6)) is kept as its t = t_pr marginal (𝒫_det(𝐌, t_pr|𝐍, 𝔪) = δ_{𝐌𝐍}; WP5v4-C43).

(Index order: Σ_ab𝔇_abS_ab = tr[𝔇ᵀS], which differs from tr[𝔇S] when S has antisymmetric imaginary parts. WP0-v3 (3.4), (7.3) and
CONVENTIONS §8 now use tr[𝔇ᵀS] (AUDIT-2 G1, m21); this return writes tr[𝔇ᵀS] throughout; IF-R8-9.)

For an e–h seed, (B2) gives 𝔊_Λ = e^{ϑ_N} 𝔊_e(E_e,k_e) 𝔊_h(E_h,k_h) (ϑ_N = the N_eh component of ϑ): the generating form of R&K Eq. (5).
The DM tensor is traced **inside** the Λ sum, because different operators (density, spin, current) populate (E_e, E_h, k_e, k_h)
differently; the same holds for the q integral. At fixed (q, ω, v): P(N_eh|q,ω) = Σ_Λ tr[𝔇ᵀS(q,ω;Λ)]P_casc(N_eh|Λ)/tr[𝔇ᵀS(q,ω)]. These were
v1's WP0 defects WP5-1, WP5-2; WP0-v2 (7.3) has adopted them. **Pair-resolved weights** are WP0-v2 (7.2) with the retarded out-state
(ε̃^{-1})_{G0}; WP1-v2 [E2] uses the same out-state form (flag F1; I3 closed). **X+ seeds** carry
n_ph and ω_ph from WP3's joint response WP3 (W.1); ω_ph goes to ℋ once (O4-d6). **GS (NR) seeds** carry E_R and direction from S^{GS}_κκ and
ρ^{ph}_κ (WP2 (3.6); §3.1).

### 1.4 Controlled reductions
- **(R-k) Energy-only reduction [D under (R-k) or (R-k′); error [E]].** Let Γ_E = Γ^{ph}_E + Γ_ii be the **total** energy-changing rate
  (A-10: v2 omitted Γ_ii). Hypothesis (R-k): momentum randomisation is faster than energy change, Γ_k ≫ Γ_E. The e–ph part holds above
  ~1 eV (intervalley and acoustic scattering are quasi-elastic), but in Si above ~3–5 eV Γ_ii ≳ Γ^{ph}, so (R-k) **fails** exactly where
  (W8) and p_2 are decided. Hypothesis (R-k′): the ii final states are themselves iso-energy distributed, independent of the parent's k
  (large unrestricted p in (W1)). Under (R-k) **or** (R-k′), 𝔊_{nk}(ϑ) → 𝔊_𝔱(E_car; ϑ) after the first collision, with iso-energy kernels
  𝒦̄_𝔱(E_car→E′_car) = Σ_{nk}δ(E_car − ε_{nk})𝒦(nk→…)/Σ_{nk}δ(E_car − ε_{nk}). The error O(Γ_E/Γ_k) per generation is an estimate [E], not derived
  (A, rubric (a)); (R-k′) is unproven and is part of gap R2. **Only the first generation keeps the k (hence q) memory**; that is where the
  DM-versus-photon seed difference enters.                                                                                              (W7)
- **(CSDA) Near-threshold ii probability [D].** If ii events are rare per unit energy loss and ω_{Qν} ≪ E_car − E_th^{ii}, a carrier at E₀ that has
  not yet impact-ionised loses energy at the rate dE/dt|_ph = Σ_ν⟨ω_{Qν}Γ^{ph}_ν(E_car)⟩ (iso-energy average), and

  p_no-ii(E₀) = exp[ −∫_{E_th^{ii}}^{E₀} dE_car Γ_ii(E_car)/(dE/dt|_ph)(E_car) ]   (WP5v3-C16).                                                     (W8)

  This controls the 1e⁻/2e⁻ boundary. R&K's single ratio Γ^{ph}/Γ_ii (their Eq. (8)) is the free-particle evaluation of the integrand.

### 1.5 Response/cascade consistency: the C-code side of O4, and the Fano term in GaAs [D; E for the size]
WP0-v2 §6.2 (iv″b) makes P(N_eh|q,ω) convention-independent at O(g²) only if the cascade satisfies O4's hypotheses and code-pair conditions.
The WP5 cascade (the "C-code" of O4) must implement:
- **O4-B1** Markov in the prompt label (this is (B1)–(B2) above) and **O4-B2** the first-emission kernel
  𝒦_{Λ₀→Λ₊} = [2π|g_{Λ₊Λ₀}|²δ(Ẽ_Λ₀ − E_Λ₊) + 𝔉_{Λ₀,Λ₊}]/Γ^{tot}_Λ₀, Γ^{tot} = Γ^{ph} + Γ^x (Γ^x = ii, Auger, radiative; supplied by WP5 only);
- **O4-d2** the same g^S, gauge U(k), ω_{Qν} and eigenvectors as the response code; Γ^{ph}_Λ₀ = −2 Im Σ^{FM} branch by branch; plus the
  e–e/e–ph pair conditions **WP5-cp1–cp3** of §1.1(c);
- **O4-d3** the X0 seed starts at the response code's Ẽ_Λ₀ (ZPR included); a bare-band cascade shifts the seed by the same Re Σ;
- **O4-d6** X0 seeds at (Λ₀, Ẽ_Λ₀, n_ph = 0) and the cascade emits first; X+ seeds at (Λ₊, n_ph = 1, ω_ph = ω_Q) with no re-applied first
  emission, ω_ph to ℋ once;
- **O4-d8, d9, d10** the same δ-smearing σ (level spacing ≪ σ ≪ δ), the same T (n_Q, n_Q + 1), and all non-phonon channels in the cascade only.
Violating d2/d3 by 10–20% gives an O(1) error in P(N_eh) (O4 toy T4); this is a hard requirement, not a nuisance.

**The Fano term (WP0-v2 flag F8; O4 (O4.7)).** For an X0 seed Λ₀ the first-emission branching to phonon branch ν is
K_ν = (Γ^{(ν)} + 𝔉_ν)/Γ^{tot}, with 𝔉_ν ≡ 𝔉_{Λ₀,ν} = 2πΓ^{(ν)}(c̄^F − c_ν^F), c̄^F = Σ_νΓ^{(ν)}c_ν^F/Γ^{ph}, so Σ_ν𝔉_ν = 0 and Σ_νK_ν = Γ^{ph}/Γ^{tot}
(WP5v3-C14a, C29). **Dimensions (A-17(a)).** With a^{off} ~ ρ/energy (WP0-v2 (6.3)), the raw Im(ρ*a^{off}) has dimension |ρ|²/energy, so
𝔉_ν = 2πΓ^{(ν)}(c̄ − c_ν) would not be a rate. The dimensionless coefficient is

  c_ν^F ≡ Γ_Λ₀ Im(Σ_Kramers ρ*_Λ₀ a^{off}_ν) / |ρ_Λ₀|²,                                                                                      (W17)

which reproduces O4's scaling 2π|c_ν^F| = O(Γ_Λ₀|a^{off}_ν|/|ρ_Λ₀|)|sin φ_ν| (WP5v3-C14g). The O(1) prefactor follows from O4 §3 step (iii) and
must be fixed there (interface flag IF-R8-4). **𝔉 = 0 for PT-symmetric crystals [D, sketch, O4]:** spinless, ρ and a^{off} are simultaneously
real (Si, diamond). **With SOC (Ge) (A-17(c))** (PT)² = −1, ρ and a^{off} are quaternion-real 2×2 Kramers blocks; element-wise Im(ρ*a^{off}) ≠ 0,
and only the Kramers-pair trace vanishes (WP5v3-C14f). Hence the Σ_Kramers in (W17): Λ₀ is Kramers-summed, as O4 (O4.7) states.
**Positivity of K_ν (B-10, "not addressed").** Since |c̄^F − c_ν^F| ≤ 2 max|c^F|, K_ν ≥ Γ^{(ν)}(1 − 4π max_ν|c_ν^F|)/Γ^{tot} ≥ 0 whenever
4π max|c^F| ≤ 1 (WP5v3-C14e); with the [E] phase estimate below this holds wherever Γ/δ ≲ 1.7. Whether GaAs satisfies it awaits a GaAs
Γ/δ map (the O4-d11 map is Si's and is not applied to GaAs; VER-WP5-B N2). Where it fails, the
sampler uses signed weights: draw ν from |K_ν|/Σ|K| and carry the weight sign(K_ν)Σ_ν|K_ν|.
*Bound [D].* Let P_ν(N) ≡ P_casc(N_eh = N | first emission into ν). The 𝔉-induced change is ΔP(N|Λ₀) = Σ_ν(𝔉_ν/Γ^{tot})P_ν(N). Because
Σ_ν𝔉_ν = 0, ΔP = Σ_ν(𝔉_ν/Γ^{tot})(P_ν − P̄) for any constant P̄ (WP5v3-C14c); choosing P̄ at the midpoint of {P_ν},

  |ΔP(N|Λ₀)| ≤ ½ (Σ_ν|𝔉_ν|/Γ^{tot}) · max_{ν,ν′}|P_ν(N) − P_ν′(N)| ≤ 2π (Γ^{ph}/Γ^{tot}) max_ν|c_ν^F| · max_{ν,ν′}|P_ν(N) − P_ν′(N)|.       (W15)

The bound (W15) is rigorous [D] once c^F is defined by (W17) (A-17, B-10; WP5v3-C14d, C14e). Since spreads of probabilities are ≤ 1,
**|ΔP| ≤ 2π(Γ^{ph}/Γ^{tot}) max_ν|c_ν^F| ≤ 2π max_ν|c_ν^F|** holds with no further input.
*Estimate for GaAs [E] (corrected, A-17(b), B-10).* O4 gives 2π|c_ν^F| = O(Γ_Λ₀/δ)|sin φ_ν|, φ_ν the relative phase of a^{off}_ν and ρ_Λ₀, which
exists only through the inversion-odd crystal potential; with an odd/even form-factor ratio ~0.2–0.3 (Cohen–Bergstresser [UNVERIFIED]),
2π max|c_ν^F| ≲ 0.3 Γ_Λ₀/δ. The spread max|P_ν − P_ν′| is **not** bounded by the phonon-energy difference alone: the first phonons differ in Q,
intervalley (Γ → L, X) and intravalley emission send the carrier to valleys with different ii thresholds, and near the 1e⁻/2e⁻ boundary
(and below 1 eV above threshold, where (R-k) has no bound, gap R2) the spread can be O(1). Hence the defensible statement is
**|ΔP| ≲ 0.3 Γ_Λ₀/δ (worst case, spread ≤ 1)**, with v2's 0.11 Γ_Λ₀/δ (spread 0.36) as an optimistic central value only. Two caveats remain:
Γ/δ for GaAs is **unknown** (the O4-d11 map is a **Si** map: WP3-v3 §M4 gives 0.007–0.2 at δ₀ = 0.3 eV, superseding WP0-v2's 0.02–0.6 at
δ₀ = 0.1 eV, which violated δ₀ ≫ ω_max; AUDIT-2 m5; B-10, B rubric (d)), and the phase is [UNVERIFIED].
𝔉 only redistributes first emissions among branches (it changes no rate). Status: the exact number needs the response code's 𝔉 export
(O4-d7; WP3) and a GaAs Γ/δ map; until then the GaAs nuisance θ_𝔉 (§8) carries the bound 2π max|c^F| with the [E] value 0.3 Γ/δ.

---
## 2. Hot carriers: closure of G1

**Formula.** (W1) (Γ^{out}, with (W1′) for local fields) + (W2) inside (W3), seeded by (W5)–(W6) from the DM S(q,ω;Λ), under the §1.5
conditions and WP5-cp1–cp3. **Rate definition fixed in the spec (A-19):** the ii kernel is (W1′) at Z_qp = 1 (0812.2923 Eq. (1) with Z → 1);
the Z factor and the Eq. (5) exchange form are varied only through θ_Z and θ_exch (§8), not left to R1. Temperature enters in three places:
the Bose factors in (W2), the 1 + n_B in (W1), and the T-renormalised bands (ZPR, L12). It does **not** enter only through E_g(T)
(§6.2; WP5v3-C28). Output: P_n(q,ω,T) ≡ P(N_eh = n | q, ω, T), with moments ε_eh(q,ω,T) = ω/n̄ and F_eh(q,ω,T).
**Computation specification (per material: Si, Ge, GaAs).**
- *Bands.* QE (PBE, norm-conserving or PAW) plus G0W0 (BerkeleyGW or Yambo). QP corrections Wannier-interpolated up to ~15 eV above the CBM.
  Si needs 16–20 disentangled sp³d WFs; Ge and GaAs similar, with SOC. Above ~15 eV use free-electron-like states with GW lifetimes; this is
  where R&K's free-particle model is accurate (§6.2) and provides a matching check.
- *W^{scr}(p,ω).* BerkeleyGW full-frequency ε^{-1}_{GG′}(p,ω), ω ∈ [0, 60] eV (N_ω ≈ 200, denser below 20 eV), p-mesh 10³–12³ plus G-shifts,
  N_G ≈ 200–300 (cutoff 8–10 Ry), ≥ 200 empty bands. Converge Im ε^{-1} at the plasmon (Si ~16.7 eV) to 2%. Total ε for GaAs (ionic part via
  DFPT Z*_κ, ε_∞). Cost: 10⁴–10⁵ core-h per material [E].
- *ii kernel.* (W1′) with LFE in the right Coulomb index and the anti-Hermitian part (GaAs); exchange (d) as a separate θ_exch run.
  Store 𝒦̄(E → E′; E_e′, E_h′), the pair split resolved via WP0-v2 (7.2) (retarded out-state
  weight) at (p, ω). Sample iso-energy surfaces with ~10³ k-points per 50 meV bin. Cost ∝ N_E × N_kiso × N_p × N_b′ ≈ 10³×10³×10⁴×20 matrix
  elements via FFT: 10⁴–10⁵ core-h [E].
- *e–ph kernel.* EPW, coarse 8³/8³ grid, Wannier interpolation, fine k 80³–100³ plus Q 50³ by MC sampling. Bands up to the WF window,
  T ∈ {0, 50, 100, 150, 300} K, g^S only for GaAs, quadrupole corrections (SOTA R2). Same g^S and ω_{Qν} as the response code (O4-d2);
  g^L and ε_ion built from one DFPT run with matched multipoles and Ewald cutoff (WP5-cp1–cp3).
  Cost ~10⁴ core-h [E].
- *Cascade solve.* (R-k)/(R-k′) for n_gen ≥ 2 (θ_{R-k} tests it on a subset): a 1D recursion in E on a 10 meV grid, by event sampling or deterministic moment equations (cost
  negligible). n_gen = 1 is fully k-resolved from S(q,ω;cvk), using WP1 outputs (RPA+LFE) and, for X+ seeds, the WP3 PAER pair distribution
  with ω_ph removed to ℋ (O4-d6); for GaAs the 𝔉 correction (W15).
- *Grid of outputs.* ω ∈ [E_g, 50 eV] in 50 meV steps; |q| ∈ [0, 25 αm_e] with 3 directions plus the angular average; 5 temperatures.
  50 eV–keV: match to the asymptotics (n̄ = ω/ε_eh + b_N, Var = F_ehω/ε_eh) (§6.4, [D, sketch] under its stated hypotheses); for ≳ keV
  the (B2) density caveat applies (θ_dense).
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
  set; absorption entries seed no cascade particle and carry negative heat (WP5v3-C20a).
- **(ii)** x_R ≫ 1 (K = imp). The impulse approximation of WP2 (5.3), S_IA(q,ω) = (2π/Ω)Σ_κ|c_κ|²∫d³P₀ 𝔫_κ(P₀)δ(ω − q²/2M_κ − q·P₀/M_κ)
  (c_κ the species coupling, = A_κF^M_κ for nucleon coupling; one atom κ per cell), resolved in the struck-nucleus momentum P_I = P₀ + q:

  S^{GS,IA}_κκ(q,ω; P_I) = (2π/Ω)|c_κ|² 𝔫_κ(P_I − q) δ(ω − P_I²/2M_κ + (P_I − q)²/2M_κ),   σ_ω² = 4E_R E^kin_q̂,   E^kin_q̂ = ⟨(q̂·P₀)²⟩/2M_κ.   (W9)

  This is the saddle point of the incoherent multiphonon sum (L5 → L6). Its Doppler width σ_ω (WP5v3-C7a) is the leading 1/x_R correction;
  E^kin_q̂ is the **true** (zero-point plus anharmonic, T-dependent) kinetic energy of WP2 (5.3) (v1 used the harmonic
  ⟨P²⟩ = (M_κ/2)∫dω′D_κ(ω′)ω′coth(βω′/2), its harmonic limit; interface flag I2). Harmonic T = 0 gives E^kin_q̂ = ⟨ω⟩/4, σ_ω² = E_R⟨ω⟩
  (WP5v3-C7b). The skewness is 𝔨₃^{GS} from the BO curvature (WP2 (5.2), L6 ✎). **The MD initial condition is fixed by the response:** one
  atom of species κ at a site, lattice positions {R_I(0)} from the harmonic (or PIMD) Wigner distribution at T, momentum P_I = P₀ + q,
  P₀ ~ 𝔫_κ. This reproduces S_κκ's energy distribution to O(1/x_R); the correction is the quantum/classical difference of the final
  vibrational state.
- *Size.* Si, E_R = 10 eV (20 eV): σ_ω ≈ 0.67 eV (0.95 eV) with ⟨ω⟩ = 45 meV (WP5v3-C7c) [E]. The struck atom's kinetic energy is smeared
  by ≳ 1 eV around E_d: predicted, not tuned (the Doppler part only, so a lower bound on the P_FP step width; §6.3, B L22).
- *No double counting with Migdal.* WP0-v2 Theorem D (6.1) splits the DM vertex: GS seeds (no electronic excitation) go to (W9); X-sector
  (Migdal) seeds add prompt e–h pairs (WP3) and a recoil. The WP5 transport starts **after** the vertex. A "U" that "effectively
  incorporates the Migdal effect" (2209.04503 [FT]) double counts if a WP3 Migdal rate is also added. Neutron-calibrated yields contain
  Migdal: fit Y_tot = Y_casc[S^{GS}] + ∫dω_e P_casc(N|ω_e)dP_Mig/dω_e, never Y_casc plus Migdal (WP3 N3; WP0-v2 double-counting rule (e)).
  **GS/Migdal moment bookkeeping [D in the impulse regime] (corrected, A-18, B-11; WP2-v2 (3.4), §5.2′, IF-2; WP3 J3; WP0-v2 §6.2 (iii)).**
  The nuclear f-sum is exact with the bare mass, ∫dω ω S_κκ = q²/2M_κ per nucleus, and splits into GS + X. In the impulse regime a Migdal
  (X) event carries its electronic energy ω_e **and** the nuclear recoil ≈ q²/2M_κ, so 𝓜¹_X = E^{Mig}_1 + P_Mig q²/2M_κ, with
  E^{Mig}_1(q) = ∫ω_e dP_Mig = q·δM_κ·q/(2M_κ²). Hence

    𝓜⁰_GS = 1 − P_Mig(q),   𝓜¹_GS = (1 − P_Mig)q²/2M_κ − E^{Mig}_1(q) = (1 − P_Mig) q²/2(M_κ + δM_κ) + O(P_Mig δM/M, (δM/M)²)   (WP5v3-C20b).

  v2's "GS first moment q²/2M_κ − E^{Mig}_1" with "zeroth moment depleted by P_Mig" was inconsistent unless X events carried no recoil, and
  "rescale the first moment by 1 − δM/M" is not an operation on S (a multiplicative rescaling changes the zeroth moment by the same factor,
  while P_Mig ∝ q² and δM/M is q-independent). **Prescription:** use M_κ + δM_κ in the (W9) δ-function and multiply S^{GS} by (1 − P_Mig(q)).
  **Size [E] (WP5v3-C20c):** δM_κ/M_κ = 2.7×10⁻⁴ (Si, all electrons); P_Mig ~ 2m_e(m_e/M_κ)E_R⟨r²⟩ ≈ 5×10⁻³ at E_R = 1 keV (⟨r²⟩ = 1 Å²,
  REF-A's order-of-magnitude input, not a computed value; to be replaced by WP3's P_Mig(q) when available), growing ∝ E_R: ≈ 0.5% at 1 keV
  and ≈ 5% at 10 keV, the upper end of the §3.4 NR grid, where the soft-limit form itself degrades [E] (WP5v3-C20c; VER-WP5-A N4). The P_Mig
  term dominates above E_R ≈ 50 eV. The correction is ≈ 0.5% at 1 keV, below every listed nuisance, but reaches ~5% at 10 keV,
  but not the "≤ 2.7×10⁻⁴" of v2. The referees agree on the prescription and differ on the size; settled in §R8.1 (D3).

### 3.2 Dynamics on the BO surface [D for the regime boundaries; E for the numbers]
- **(iii)** E_R ≈ 0.3 eV–E_d. The trajectory runs on the BO surface E^ad_0(R). It is anharmonic: the displacement amplitude in Si is
  u_I ≈ √(2E_R/M_κ⟨ω⟩²) ≈ 0.38 Å at 1 eV against a 2.35 Å bond (WP5v3-C17) [E]. It is classical: λ_dB(20 eV, Si) ≈ 0.012 Å. It is adiabatic:
  the Massey parameter ξ_Mas = E_g ℓ_int/v_N ≈ 15 at 20 eV (ℓ_int = 1 Å; WP5v3-C6), so non-adiabatic loss is ~e^{−ξ_Mas}.
  **BO-MD is controlled here.** Everything goes to ℋ, except a stored energy when E_R ≥ E_d.
- **Displacement threshold (definition).** Let 𝔅₀ be the basin of the perfect crystal on E^ad_0 and 𝒰_t the dissipative flow (dynamics plus
  bath). For recoil direction r̂_R:

  P_FP(E_R, r̂_R) = Pr_{R_I(0)∼Wigner}[ lim_{t→∞} 𝒰_t(R_I(0), √(2M_κE_R) r̂_R) ∉ 𝔅₀ ],   E_d(r̂_R) ≡ E_R such that P_FP = ½.                   (W10)

  A smooth step whose width comes from the zero-point and thermal R_I(0) and from (W9); the step model is its zero-width limit.
- **Stored energy.** E_st = E^ad_0(R_final) − E^ad_0(R_I(0)) at t_pr ≈ 10–100 ps, after prompt recombination and before thermally activated
  annealing (§4). R_final holds a vacancy–interstitial pair, a close pair or an amorphous pocket. **E_st ≠ E_d.** E_d is a dynamical (kinetic)
  threshold; E_st is a thermodynamic formation energy, ~E^{form}_V + E^{form}_I for a separated pair (Si ≈ 7–9 eV, Ge ≈ 5–7 eV
  [UNVERIFIED, DFT literature from memory]). The rest, E_d − E_st, is heat. **[A-3]** "The zero-point shift ΔZPE of the final basin is a
  correction inside the phonon reservoir, not part of E_st; hop i → j releases ε^{hop}_ij + ΔZPE_i − ΔZPE_j to phonons. The mean evolution is
  ⟨E_st(t)⟩ = E_st − ∫E𝒦^{rel}, with ∫_0^{t_obs}∫E𝒦^{rel} = E_st − ⟨E_st^{unrel}(t_obs)⟩ and ∫∫𝒦^{rel} = ⟨N_hop⟩ (Theorem T-1; WP7-E-v3
  (E5)–(E6)). E_d enters only through P_FP (W10)." **[v4] Reading required by T-1 condition (ii).** E_st is an E^{conf} difference only if
  **both** arguments are basin minima: R_final the quenched end state (as §3.4 already specifies) **and** R_I(0) replaced by the minimum of 𝔅₀. The
  Wigner-sampled R_I(0) of §3.1 lies above that minimum by the initial-state potential energy, ≈ 3⟨ω⟩/4 ≈ 34 meV per atom at T = 0 (harmonic [E],
  ⟨ω⟩ = 45 meV), i.e. ≈ 138 eV in a 4096-atom cell (WP5v4-C39), which would swamp E_st. So E_st ≡ E^{conf}(R_final^{min}) − E^{conf}(𝔅₀^{min}), the same
  table as (W12) and as p_st of WP7-T-v2 (5.1) (§R13.3; IF-R13-3).

### 3.3 Electronic excitation by the recoil (the charge channel) [D for the threshold logic; E for the numbers]
- **Kinematic threshold.** A binary collision between a slow ion (v_N ≪ v_F) and a valence electron transfers at most 2m_ev_N(v_N + v_F). A
  pair needs E_g, so v_th ≈ E_g/(2m_ev_F). With the free-electron k_F for 4 valence e/atom, n = 32/a³ (k_F = 1.808 Å⁻¹ Si, 1.736 Å⁻¹ Ge;
  WP5v3-C5a): **E_R,th ≈ 352 eV (Si), 395 eV (Ge)** [E] (336/382 eV keeping v_N²; WP5v3-C5b,c). v2's 375/465 eV used unsourced k_F = 1.75/1.60 Å⁻¹
  (A-11, B-9) and are withdrawn. **The threshold is soft (A-11, B-9) [D for the logic].** For gapped jellium, L(k,ω) is supported in
  |ω − k²/2m| ≤ kv_F, which with ω ≤ kv_N gives the sharp bound. In a crystal, L(k, ω ≥ E_g) at k ≳ E_g/v_N ≈ 2k_F is the low-ω tail of the
  Bethe ridge, fed by the high-momentum tail of the valence momentum density (Umklapp, core orthogonalisation): small but non-zero. Below
  E_R,th the linear-response electronic stopping is therefore **strongly suppressed, not zero**. A friction model F = −S^{stop}_e(E)v̂
  (2506.03810 Eq. (3) [FT, CONFIRMED]; SRIM S_e) assigns electronic loss there with no final-state suppression.
- **What creates pairs below E_R,th.** Non-adiabatic transitions in close collisions, where the local gap of the distorted configuration
  closes (quasi-molecular promotion): the X-sector couplings of Theorem D at strong coupling. Per crossing they follow Landau–Zener,
  P_LZ = exp(−2πh_LZ²/(v_N|ΔF_LZ|)) (h_LZ the diabatic coupling, ΔF_LZ the slope difference). Both ξ_Mas ≈ 2 at 1 keV and Z_κα/v_F ≈ 15 ≫ 1 say
  that **linear-response (Lindhard–Scharff) stopping is not a derived limit at E_R ≲ few keV**; it is a fit.
- *Data.* The Ge measurement QF = 25 ± 3% at 254 eV_nr (2405.10405 [ABS]; 64 ± 8 eV_ee [FT per WP7-E-v3 §4(b), not re-read here]) lies below the binary threshold (395 eV); if confirmed, this
  channel or the momentum-tail stopping must dominate there [E].
- **Charge from the electronic deposit.** The electronic excitation spectrum dP/dω_e produced along the trajectory seeds the §2 cascade.
  Slow-ion excitations are near-gap, so **N̄_eh ≠ E_el/ε_eh^γ**: the conversion uses P_n at the NR seed spectrum, not the photon asymptote
  (§6.1, L20 correction).
- **[A-5]** "N^meas = Σ_i𝔮_i (WP7-E-v3 (E12)). QF comparisons use ⟨𝔮⟩_NR/⟨𝔮⟩_ER. Trapping after t_pr is a detector-stage effect; captures before t_pr
  are in P_casc (A-1). 1803.02903's 'ionization collection efficiency' is a ratio to a higher-field yield model, not ⟨𝔮⟩_NR/⟨𝔮⟩_ER." (Source [FT],
  1803.02903 PDF p. 3: "consistent with 100% for nuclear recoils below 20 keV"; the yield-model dependence is WP7-E-v3 §2.3(a) [FT].) The Ge datum
  above is accordingly (⟨𝔮⟩_NR/⟨𝔮⟩_ER)·QF_created at 77 K (WP7-E-v3 §4(b)).

### 3.4 Computation specification for G3
- **PES.** DFT (QE or VASP; PBE and SCAN for spread) joined to ZBL/DMol at r < 1 Å. Train an MLIP (ACE, MACE or NequIP) on ~10⁴
  configurations: dimers down to 0.5 Å, point defects, close pairs, amorphous and liquid, plus recoil snapshots. Force error ≤ 50 meV/Å;
  energy ≤ 3 meV/atom.
- **E_d(r̂_R) and P_FP.** ~300 directions in the irreducible wedge × 20 Wigner R_I(0) samples, bisection to 0.5 eV, cells of 4096–8000 atoms
  for 3–5 ps, 0.1 fs step near close approach, boundary thermostat: ~3×10⁴ MLIP runs, ~10³ GPU-h. Check 20 directions with BO-DFT-MD
  (512 atoms, ~10⁵ core-h).
- **Partition tables.** E_R ∈ [1 eV, 10 keV] (40 log points) × 100 directions × 100 seeds from (W9). Cells from 10³ atoms (< 100 eV) to
  10⁵ atoms (10 keV), 1–10 ps. Record ℋ, E_st (quench to 0 K at t_pr; **[v4]** E_st referenced to the 𝔅₀ minimum,
  §3.2) and defect labels. Cost 10⁴–10⁵ GPU-h.
- **Electronic channel.** Real-time TDDFT Ehrenfest or surface hopping (Qb@ll, Octopus, SALMON) for Si–Si and Ge–Ge close collisions,
  E_coll = 50 eV–5 keV, impact parameters b_imp = 0–1.5 Å, 64–216-atom cells, 20–50 trajectories per energy. Output the **distribution**
  dP/dω_e(b_imp, E_coll), not only S^{stop}_e. Cost ~10⁶ core-h. Attach it to the MLIP-MD as stochastic excitation events feeding §2.
- **Outputs.** P(ℋ, E_st, N_eh | E_R, r̂_R, T) and moments, the anisotropic E_d surface and the heat quenching Y_H(E_R, r̂_R; t_win)
  (the windowed NR/ER signal ratio of (W11); ℋ_meas of v3 is withdrawn, §R13.1 K7):

  **[A-4]** "Y_H(t_win) ≡ (NR heat signal)/(ER heat signal) at equal deposited energy. With multiplicative collection
  E_sig = ϵ_prim(ω − D′) + ϵ_NTL·(NTL heat), where D′ ≡ E_st(t_win) + E_trap(t_win) + E_es^{trap} + ΔZPE(t_win) + E_esc is the pre-sensor deficit
  (ΔZPE in ℋ_ph but not sensor-absorbable; ΔZPE^{ER} = 0) and δ_coll ≡ (ϵ_prim^{ER} − ϵ_prim^{NR})/ϵ_prim^{ER}:

  Y_H = (1 − δ_coll)(ω − D′_NR)/(ω − D′_ER) = 1 − δ_coll − [⟨E_st^{unrel}(t_obs)⟩ + ⟨E_st^{rel}⟩(1 − P_rel(t_win)) + ⟨ΔE_trap⟩ + ⟨ΔE_es^{trap}⟩
        + ⟨ΔZPE(t_win)⟩ + ⟨ΔE_esc⟩]/ω   (W11)

  The absolute sensor loss cancels; E_trap is μ_F-referenced (doubly trapped E_g − E^tr_e − E^tr_h; singly trapped μ_F − E_v − E^tr_h or
  E_c − E^tr_e − μ_F); ΔE_trap may be negative. NTL mode: [(1 − δ_coll)(ω − D′_NR) + r_collg_Luke y_ion ω]/[(ω − D′_ER) + r_collg_Luke ω],
  r_coll = ϵ_NTL/ϵ_prim^{ER}, g_Luke = eV_b/ε_eh. Unit heat quenching (2007.14289) is δ_coll = 0, D′_NR = D′_ER; the Si two-channel datum
  η^φ_NR = 0.952 (1803.02903) constrains δ_coll + g_Luke(r_coll − 1)(1 − y_ion)/(1 + r_collg_Luke) + (D′_NR − κ_calD′_ER)/ω = 0.048."
  **[v4] Remainders and checks.** The second equality of (W11) holds to O(d′², δ_colld′, δ_coll²), d′ ≡ D′/ω (WP7-E-v3 (E8); WP5v4-C33a); the
  bracket uses ⟨E_st(t_win)⟩ = E_st^{unrel}(t_obs) + E_st^{rel}(1 − P_rel(t_win)) with ⟨E_st⟩^{ER} = 0 (WP5v4-C33c); ϵ_prim cancels in both modes and
  the NTL ratio reduces to (1 + y_iong_Luke)/(1 + g_Luke) at zero deficits and r_coll = 1 (WP5v4-C33b). The κ_cal combination in the last sentence is
  WP7-E-v3 (E13), derived at r_coll = 1. Re-derived from the calibration procedure (ER-calibrated phonon and charge scales, 1803.02903 Eq. (1);
  WP5v4-C34), the exact first-order form at general r_coll is

  1 − η^φ_NR = g_Luke(r_coll − 1)(1 − y_ion)/(1 + r_collg_Luke) + [(1 + g_Luke)/(1 + r_collg_Luke)](δ_coll + d′_NR)
             − [(1 + g_Luke)(1 + r_collg_Luke y_ion)/(1 + r_collg_Luke)²] d′_ER + O(d′², δ_colld′, δ_coll²),                                       (W11′)

  which equals A-4's combination at r_coll = 1 (κ_cal = (1 + y_iong_Luke)/(1 + g_Luke) = 0.642 at y_ion = 0.3 [E], g_Luke = 4/3.82 = 1.047 [FT]). At
  the degenerate point r_coll = 1.144 the two weights are 0.931 and 0.576 (against 1 and 0.642), so A-4's combination carries an
  O((r_coll − 1)δ_coll, (r_coll − 1)d′) remainder of 7–10% of the deficit terms (WP5v4-C34b,c). The E_st bounds of §6.3 are unaffected: they rest
  on WP7-E-v3 (C7g), 1 − η − E_st/ω = g_Luke(r_coll − 1)[(1 − y_ion) − E_st/ω]/(1 + r_collg_Luke) + (non-negative terms), which (W11′) reproduces at
  general r_coll (WP5v4-C34e). IF-R13-2. Source quotes [FT, 1803.02903]: phonon scale calibrated on "bulk electron recoils, which should have unity
  ionization yield" (PDF p. 8); "gives ηNR = 95.2+0.9 −0.7 % at 95% C.L." (p. 17, as extracted; the PDF typesets η^φ_NR = 95.2^{+0.9}_{−0.7}%); "For silicon, ε = 3.82 eV above 77 K" (p. 5, footnote 2); bias 4 V,
  4 V/cm (p. 5). 2007.14289 [FT, PDF p. 4]: the heat quenching factor is assumed unity, as for Ge, "where the heat quenching factor was shown to
  be very close to unity".

---
## 4. Defects, annealing and stored energy as a background model (G12)
**Formula [D, under harmonic TST and Markov hopping].** Defect configurations i have energies E^{conf}_i ≡ E^ad_0(R_i) and hop rates Γ_ij(T).
Populations N_i(t) are seeded by recoils (§3: DM, radiogenic, cosmogenic; source 𝔰_i(t)) and by the post-cooldown state:

  dN_i/dt = 𝔰_i(t) + Σ_j [Γ_ji N_j − Γ_ij N_i],   ℛ_rel(E,t) = Σ_{ij} Γ_ij(T) N_i(t) δ(E − (E^{conf}_i − E^{conf}_j)) ⊗ 𝒯_𝔠(E → E^meas).        (W12)

**[A-6]** "⊗ 𝒯_𝔠(E → E^meas), an event iff ϵ_coll ε ≥ E_thr^det, ε = ε^{hop}_ij + ΔZPE_ij (WP7-E-v3 (E14))", with ΔZPE_ij = ΔZPE_i − ΔZPE_j (WP7-T-v2 §4.1: ZPE_i − ZPE_j of the local modes, the released amount; WP7-E-v3's per-hop δZPE) and
ε^{hop}_ij = E^{conf}_i − E^{conf}_j the δ-argument of (W12). "Single Frenkel-pair releases and TLS quanta are sub-threshold for E_thr^det > 3 eV
(ϵ_coll E_st,1 ≈ 0.3 × 9 eV = 2.7 eV [E]; WP5v4-C41). Pocket recrystallisation is collective, event-seeded and can exceed 10 eV. Below T_× use
WP7-T-v2 rates." **[v4]** The δ-argument of (W12) stays configurational (T-1 (v)); δZPE enters only the observable argument of 𝒯_𝔠. The sourced
(W12) obeys T-1 by linearity provided its index set contains the recombined state 𝔅₀ and the separated-pair states (§R13.3; WP5v4-C38).

Rates:
- above the crossover T_× = ω_bar/2π: Γ_ij = (Πω_i^{(min)}/Πω^{(TS)}) e^{−E_bar/T}/(2π) (Vineyard; ω_bar the barrier-top curvature frequency);
- below T_×: instanton tunnelling Γ_ij ∝ e^{−𝒮_inst}. **[A-6, v4]** Below T_× the rates are those of WP7-T-v2 (its (4.2) with J_ph + J_el + J_loc
  and the window (4.3), WP7-T-v2 IF-T2), which supersede this line for mK use (§R13.1 K9).
For an Si interstitial-like barrier with ω_bar ~ 2π×10 THz, T_× ≈ 76 K (WP5v3-C17) [E]. **At mK, annealing is tunnelling or triggered
(avalanche: 2408.07518 [ABS] finds that crossing low barriers triggers larger releases). Classical TST predicts no events there.**
- **Time dependence [D].** For a barrier density 𝒩_b(E_bar) flat over the active range and Γ = Γ_att e^{−E_bar/T},
  Σ Γe^{−Γt} → 𝒩_b T(1 − e^{−Γ_att t})/t ∝ 1/t (WP5v3-C8): a generic 1/t decay after cooldown or irradiation. Exponential decays need a narrow
  barrier set. The 1/t law is also proposed for dislocation relaxation (2406.15425 [ABS]), so the time law alone does not discriminate.
- **Energy spectrum [C].** The observed ∝ e^{−E/E_slope} (2408.07518 reports that simulations reproduce it) is not derived here. A
  maximum-entropy release distribution at fixed mean ⟨E^{conf}_i − E^{conf}_j⟩ would give it; conjecture.
- **Computation specification.** *Barriers:* climbing-image NEB on the §3.4 MLIP from the quenched §3 end states; validate 50 barriers
  against DFT. *Kinetics:* rate catalogue by on-the-fly kinetic MC; instanton (ring-polymer) rates for the 10² most frequent hops below T_×.
  *Seeds:* E_R spectra of cosmogenic neutrons and radiogenic recoils as 𝔰_i. *Output:* ℛ_rel(E, t, T) with nuisances for the barrier spread
  and the MLIP error. *Cost:* ~10⁴ GPU-h.
- **Exact remaining gap (G12).** Triggered-avalanche statistics at T ≪ T_× need a non-Markov treatment of strain and phonon pulses (R4, §9).
- **DFT-level defect creation by ER (catalog gap 5).** The §2 carriers cannot displace atoms: the maximum transfer from a 10 eV electron to Si
  is 4m_eE/M_κ ≈ **0.78 meV** ≪ E_d (WP5v3-C11; v1's 1.5 meV was 2× too large; the conclusion is unchanged). ER defect creation therefore
  needs electronic-excitation-driven bond breaking (self-trapped excitons or core-hole Auger). In Si this is absent at eV scale [E]. It is
  candidate-dependent for ionic targets (NaI, LiF: colour centres; WP4).

---
## 5. Quasiparticle yield in superconductors
**Formula [D under (B1)–(B3)].** (W3) with types {hot e (ω ≫ Δ_BCS), QP(E), phonon ω′ > 2Δ_BCS, phonon ω′ < 2Δ_BCS (loss), escaping phonon}.
Scope: Theorem D does not apply (WP0-v2 §6.2 (H2) scope); the sectors are quasiparticle-number sectors (WP4, flag F5).
- *Seed.* S(q,ω;Λ) on the BCS reference state with the conserving GRPA vertex (L15, WP4). For ω ≫ Δ_BCS (every m_χ ≳ 100 keV) the seed is a
  normal-state hot e–h pair and (W1) applies. **The Al plasmon (~15 eV) is an undamped RPA pole for q < q_c (§1.1(a) restriction; B-3):**
  it enters (W3) as a separate type 𝔱 = pl, created by (W1) with weight (πω_p/2)δ(ω − ω_p) and destroyed by its own damping rate Γ_pl
  (interband ε₂(q, ω_p) for q < q_c, Landau damping into e–h pairs for q > q_c, two-pair decay beyond RPA), with children e–h pairs at total
  energy ω_p. Bulk plasmons are longitudinal and do not radiate, so every decay channel puts ω_p into the electron system; (W13)'s bookkeeping,
  and hence η_pb, is unchanged at leading order, and only the (E₁, E₂) split of the plasmon's children depends on which channel dominates
  [D for the bookkeeping, E for the irrelevance of the channel]. For ω ≈ 2Δ_BCS–few Δ_BCS the seed is WP4 [4.6]:
  Λ = (E₁, E₂), E₁ + E₂ = ω, P(E₁|ω) = [E₁E₂ + Δ_BCS²]/[√(E₁² − Δ_BCS²)√(E₂² − Δ_BCS²)]/[ω𝔤_I(ω/Δ_BCS)], used as recorded.
- *Kernels.* Near Δ_BCS: Eliashberg α²F(ω′) with coherence factors. Phonons are case I (density-like): QP scattering carries (1 − Δ_BCS²/E₁E₂),
  pair breaking and recombination carry (1 + Δ_BCS²/E₁E₂). Photon (case II) pair breaking carries (1 − Δ_BCS²/E₁E₂) (1401.1937 Eq. (1) [FT]).
  **The DM density vertex is case I** (WP4 [4.6] numerator E₁E₂ + Δ_BCS²), so for ω ≈ 2Δ_BCS–4Δ_BCS (the no-cascade region) the DM seed's (E₁,E₂) split differs
  from the photon calibration: a q-independent but probe-dependent analogue of G1 [D for the sign structure]. v1's open item (R5) on the
  screened vertex is closed at the seed level by WP4 [4.6] and L15 (GRPA); its size at q ≲ 1/ξ_coh stays with WP4.
- *Exact bookkeeping (as W4).* ω = N_qpΔ_BCS + E_sub + E_excess + E_esc, so

  η_pb ≡ Δ_BCS⟨N_qp⟩/ω = 1 − ⟨E_sub + E_excess + E_esc⟩/ω,   F_qp = Var(E_sub + E_excess + E_esc)/(Δ_BCS²⟨N_qp⟩),                    (W13)

  N_qp the quasiparticle number (NOTATION); WP4-v2 §4.6 uses the same normalisation (WP5v3-C15; I1 closed).
- **[A-7]** "(i) Superconducting absorber: E_sub, E_excess are absorber ℋ_ph and E_esc is E_esc of WP7-E-v3 (E1). (ii) A sensor film (ω → phonon
  energy entering the film): E_sig = Δ_BCSN_qp, E_sl = E_sub + E_excess + E_esc(film); the film's 1 − η_pb is part of the multiplicative ϵ of
  (E7)" (WP7-E-v3 (E7); the ϵ_prim, ϵ_NTL of (W11)).
- *Limits.* For ω < 4Δ_BCS there is no cascade: N_qp = 2, η_pb = 2Δ_BCS/ω ∈ [½, 1] (WP5v3-C15a). [Corrected from v2's 3Δ_BCS (SOTA-R7,
  REF-WP4-A/B: "N_qp = 2 holds up to ω < 4Δ"). Derivation: a QP at E can emit a pair-breaking phonon (ω′ ≥ 2Δ_BCS) only if E − Δ_BCS ≥ 2Δ_BCS;
  the hotter QP of the seed pair has at most E = ω − Δ_BCS, so a third QP needs ω ≥ 4Δ_BCS.] For ω ≫ ω_D in a bulk absorber, η_pb → 0.57–0.6 (infinite-volume
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
  [ν̄(ε−t/ε) + ν̄(t/ε−u) − ν̄(ε)], with U = U_FP + U_EDFT(E) (stated in the text; Eq. (3) gives U_EDFT; A rubric (c) minor misquote corrected).
- **URF chain (corrected: A-6, B-12).**
  1. WP0-v2 (3.4), GS sector, K = imp → recoil seed (W9).
  2. (W3), ion type, observable **ν = ℋ_nuc + E_st**, where ℋ_nuc is the heat reaching atomic motion through the ion branch (nuclear
     collisions), **excluding** the heat of the electronic sub-cascade. (v2's ν = ℋ + E_st was wrong: (W4) puts all carrier-relaxation heat,
     ≈ (ε_eh − E_g)/ε_eh ≈ 70% of E_el, into ℋ, while Lindhard's ν̄ counts only energy delivered to atoms by nuclear collisions.)
     **U assignment (URF):** U_FP (the Frenkel-pair creation energy) → E_st, which is lattice stored energy and belongs to ν, not to the
     ionization; U_EDFT (inner-shell excitation) → electronic. v2's "(+ U_bind) in ν" is withdrawn.
  3. **Truncation 0: binary-collision approximation (uncorrelated targets at rest, a pair potential) + Markov ion transport.** Given truncation
     0, the first moment of (W3) is 2001.06503 Eq. (3), with dσ_n = binary scattering on the pair potential and dσ_e = the §3.3 non-adiabatic
     excitation kernel [D given BCA + Markov]. A cross-section "on E^ad_0" is defined only after this step (A-6). Truncation 0 fails in
     E_R ≲ few keV dense cascades in Ge (thermal spikes) [E].
  4. Truncations: (I/A) drop the electrons' contribution Σϕ̄_e to ν (exact **by definition** of ν; **not** justified by the §4 4m_eE/M_κ bound,
     which excludes displacements by electrons, not phonon emission by electrons, the dominant electron→lattice channel; B-12);
     (II–IV/C–E) small fractional transfers;
     (D) nuclear and electronic channels independent; E^ad_0 → a universal screened pair potential (TF or ZBL; amorphous random medium: no
     channeling, no anisotropy); dσ_e → Born free-electron-gas stopping ∝ v_N (Theorem C(e)) times Lindhard's hand-inserted Z^{1/6}
     (2209.04503 [FT, CONFIRMED] states this); (B/V) U_bind = 0 (Lindhard) or U_FP + U_EDFT (2209.04503); charge yield N_eh = E_el/ε_eh^γ.
     **[A-8]** "(F) Implicit: Lindhard U = 0 ⇒ E_st = 0; 𝔮 = 1, E_trap = 0; in 2209.04503 the **secondary** U is frozen stored energy booked
     electronic by complement; the primary's u is in ν̄." (Consistent with Discrepancy (5) below; no conflict.)
- **Validity.** Born stopping needs Z_κα/v_F ≪ 1; Z_κα/v_F ≈ 15 (Si), 35 (Ge) [E, WP5v3-C6b], so S^{stop}_e ∝ v_N is an empirical scaling at
  keV. Binary electronic excitation needs E_R ≳ 352 eV (Si) or 395 eV (Ge), a soft threshold [E, WP5v3-C5]. The amorphous-medium step needs
  ranges ≫ the lattice constant and no channeling. Quoted empirical validity: 𝓔_red ≳ 0.1 (≈ 4 keV) for Si and ≳ 0.00088 (≈ 250 eV) for Ge
  (2001.06503 [FT, CONFIRMED]). The modified model fits 680 eV–3 MeV Si data with χ²/dof = 1870/101 (2209.04503 [FT, CONFIRMED]).
- **Leading URF corrections.** (a) **The gap threshold:** below E_R,th the binary electronic deposit is strongly suppressed (not zero:
  momentum-density tail, §3.3), so a non-zero QF below ~0.35–0.4 keV measures close-collision (Landau–Zener) promotion plus that tail;
  a strong suppression, not a sign-definite switch-off. (b) **Seed-spectrum
  conversion:** N̄_eh = Σ_{ω_e}(dP/dω_e) n̄(ω_e) ≠ E_el/ε_eh^γ; near-gap excitations give n̄ ≈ 1 per excitation, against ω_e/3.75 eV for the
  photon conversion. (c) Crystal anisotropy and channeling: directional QF. (d) U_bind computed as ⟨E_st⟩ (§3.2) instead of fitted.
- **Discrepancies.** (1) *Reduced energy [CONFIRMED; referee disagreement settled in §R8.1 (D1)].* 2001.06503 uses Lindhard's
  a = 0.8853a₀/(√2 Z^{1/3}) (𝓔_red/E = 0.0243 keV⁻¹ for Si). 2209.04503 uses the ZBL length a = 0.8853a₀/Z, Z = Z₁^{0.23} + Z₂^{0.23}, "with
  suitable values of the effective atomic numbers of the incident ion and the target atom Z1 and Z2", C = 16.2616/(ZZ₁Z₂) keV⁻¹, and later
  "the effective number of valence electrons in the incident ion is Z1 = 12, while Z2 = 14" (Bohr-stripped effective Z₁, following its
  ref. [40]) [FT, re-read for R8]. That gives 0.0268 keV⁻¹, 10% above Lindhard's (WP5v3-C10a); with Z₁ = 14 it would be 0.0226 (−7%,
  WP5v3-C10b). Either way the same E maps to a 𝓔_red at least 7% different: fitted parameters cannot be transferred. (2) 2001.06503 notes an
  internal inconsistency of Lindhard's boundary condition: ν̄′(0) → 1 is imposed, while Eq. (5) implies ν̄′(0) → 0 [CONFIRMED; their own
  remark]. (3) *The second-order coefficient ½εS_e of 2209.04503 Eq. (2).* v2's "not derived in the text" is **REFUTED and withdrawn**
  (2209.04503 follows "the arguments in [5]" = 2001.06503, App. B Eqs. (28)–(29): mean-value theorem with t̄_n ≈ ⟨ε sin²(θ/2)⟩ = ε/2). The
  objection that survives is ours [D]: under approximation (D)/(III) ("nuclear and electronic collisions separately") each event has
  T_n = 0 or T_e = 0, so the cross term ∫dσ_{n,e}T_nΣT_e vanishes identically, and a ½εS_e term contradicts the approximation used to get
  S_e (WP5v3-C26). (R9, VER-WP5-A N1: v3's second half, "ε/2 is unweighted while dσ_n is forward-peaked", is **withdrawn**. In
  2001.06503 Eq. (29) the mean-value average t̄_n is weighted by the electronic loss ΣT_e in the same collision, which grows toward small
  impact parameter where T_n is large; the dσ_n-only average is the wrong weight, and t̄_n ≳ ε/2 is possible.) The straggling coefficient ½W is
  consistent with the expansion (+½ν̄″(ΣT_e)² → −½Wν̄″ on the LHS). (4) 2506.03810 (MD) stops at 10 eV_nr "as no ionization occurs below this
  threshold" while using SRIM friction above it [quote CONFIRMED by both referees]; the binary threshold (~352 eV Si) is 35× higher, so
  [E, our physics inference, not a literature claim] their sub-keV ionization is a property of the friction model, not of a final-state
  channel (up to the momentum-tail suppression of §3.3). (5) *U in secondary displacements booked as electronic [restated in R9, VER-WP5-A N3].*
  2209.04503 (and 2001.06503, per REF-B) write ε_R = η̄ + ν̄ and f_n = η̄/ε_R = (ε + u − ν̄)/(ε + u), with the sub-threshold boundary
  ν̄ = ε + u = ε_R (its Eq. (4), s ≤ u). So the **primary's** u is counted in ν̄ (atomic), and f_n = 0 below threshold: no inconsistency there.
  The U spent in **secondary** collisions enters the recursion as ν̄(T_n − U), is absent from ν̄, and therefore falls into η̄ = ε_R − ν̄ by
  complement: U lost in secondary displacements (identified at low E with U_FP, a lattice stored energy) is booked as electronic. In the URF
  (E_st ≠ charge) this is a source inconsistency; its size is not derived here [E]. (v3's "u counted in the electronic fraction … up to
  u/(ε + u)" overstated it and is withdrawn.)

### 6.2 L21: Ramanathan–Kurinsky ionization model; step model
- **Source [FT, 2004.10709] (source notation: E_r = deposited energy, → ω; "E_r" in Eqs. (15)–(16) = phonon losses).**
  Eq. (5): n(E_r) = 1 + ∫_0^{E_r−E_g}dE P(E,E_r)⟨N(E)⟩. Eq. (6): e/h symmetry P(E,E_r) = P(E_r−E_g−E, E_r). Eq. (7): a Beta P(x|α) fitted to
  photon ε_eh data at 3–8 eV. Eq. (8): Γ_ph/Γ_eh = A(105/2π)(E−ω_0)^{1/2}/(E−E_g)^{7/2}. Eq. (9): A = (|M_ph|/|M_eh|)(4π⁴/VΔ)(ħ²/2m)³, with
  A = 5.2 "eV²". Eq. (10): p_eh = [1 + Γ_ph/Γ_eh]^{-1}. Eq. (11): E_g(T) = E_g(0) − aT²/(T+b) as the only T dependence ("purely through
  the variation of the gap energy" [CONFIRMED, REF-B]). Plasmons:
  n_pl = ⌊(E_r−E_g)/ω_pl⌋. The step model N_eh^{step} = 1 + ⌊(ω−E_g)/ε_eh⌋ (ε_eh = 3.6–3.8 eV Si, 2.9 eV Ge) appears in the survey
  (2105.05253, 2603.12326) as "Q".
- **URF chain.** (W6) → (W5) with an e–h seed → (W3) first moment. Then:
  1. q-marginalise the seed **and** replace S(q,ω;cvk) by a photon (q ≈ 0) fit. This is not the marginal of the DM seed (WP0-v2 (7.3); §7).
  2. (R-k) (W7) from generation 1 (needs (R-k′) where Γ_ii ≳ Γ^{ph}; §1.4).
  3. Impose e/h symmetry N̄_e = N̄_h. The URF keeps them separate; the hole bandwidth (B_h ≈ 12 eV) emerges from the band structure.
  4. (W1) → constant |M_eh|² with momentum conservation dropped ("random-k"), free parabolic DOS ∝ √E, vacuum mass. The three-body phase
     space is Γ(3/2)³/Γ(9/2)(E−E_g)^{7/2} = (2π/105)(E−E_g)^{7/2} (WP5v3-C1a,b): the origin of 105/2π. The threshold moves from
     E_th^{ii} ≈ 1.1–1.5E_g to E_g.
  5. (W2) → one Einstein mode ω₀ = 63 meV with constant |g|², T = 0: Γ^{ph} ∝ (E−ω₀)^{1/2}. The ratio is R&K Eq. (8) [D].
  6. Plasmons: an explicit fixed-energy plasmon channel on top of (4) double counts with the RPA ii channel (Theorem C(a)); R&K find no
     effect, consistent with this.
  7. The step model is the deterministic limit P_casc(N|Λ) → δ_{N,N_eh^{step}(ω)}, so F_eh = 0.
- **Validity.** Steps (4)–(5) need E − E_g ≫ the band-structure scale (E_dir − E_g ≈ 2.2 eV Si; L/X valley spacing in Ge), in practice
  E ≳ 10–15 eV [E]. The Beta seed is valid only for photon kinematics. **Step model (corrected, B-13):** it is exact in the forced region
  (N_eh = 1 below the ii onset). As a heuristic [E, not a derived failure point], its δ-distribution misassigns N at O(1) probability once
  σ_N = √(F_ehn̄) ≳ ½, i.e. n̄ ≳ 1/(4F_eh) ≈ 2.1, which with the asymptotic mean is ω ≳ ε_eh(2.1 − b_N). The URF b_N is not computed (0.19 is
  only the value at which the step-model mean would match; VER-WP5-A N2), so for |b_N| ≲ 0.3 this is ω ≈ 7–9 eV in Si [E] (WP5v3-C18). (v2's "so never
  accurate beyond ω < 2E_g" did not follow from n̄ ≳ 2 and is withdrawn.) Its mean averaged over the fractional part is (ω−E_g)/ε_eh + ½; the
  asymptotic URF mean is ω/ε_eh + b_N; they agree only if b_N = ½ − E_g/ε_eh ≈ 0.19 (Si) (WP5v3-C18) [E].
- **Leading URF corrections.** (a) **q-dependence of the seed:** the first generation is k-resolved. **No prior bound is available (A-20,
  B-13):** R&K's α family (their Eq. (6)–(7)) imposes e/h symmetry, while a q ≠ 0 DM seed is e/h-asymmetric and electrons and holes have
  different thresholds, so the photon-Beta envelope cannot bound the DM seed. The size is a computed difference at n_gen = 1 (θ_seed, §8); the
  α-envelope spread may be shown as an illustration [E] only. v2's "up to ~50% in p_2 at 4–8 eV, 2004.10709 [FT]" is **UNRESOLVED /
  misattributed** (REF-A: the text has "~50% in limits" and "systematics on the order of 50%") and is not used. (b) Temperature beyond E_g(T): phonon
  absorption n_{Qν}, T-dependent ZPR band shapes, and (1−e^{−βω})^{-1} in (W1); the ii threshold region is where Γ^{ph}(T) matters, via (W8).
  (c) X+ (PAER) seeds remove ω_ph into ℋ at the vertex (O4-d6). (d) Exchange (Theorem C(d)).
- **Discrepancies (all CONFIRMED by both referees against the full text unless stated).** (1) *Units of A:* Eq. (8) is dimensionless only
  if [A] = energy³, so "5.2 eV²" is inconsistent; Eq. (9) with a dimensionless amplitude ratio and Δ a real-space volume does give E³, so the
  "eV²" is the error, not Eq. (9) (WP5v3-C1c). (2) *Golden rule:* Eq. (9) has |M_ph|/|M_eh|; the golden rule gives |M_ph|²/|M_eh|². (v2's
  "Δ is undefined" is **REFUTED and withdrawn**: the paper defines it as "the volume per electronic state", and dimensional consistency of
  Eq. (8) forces the real-space reading, WP5v3-C1c.) (3) *Symbol collision:* E_r means "recoil energy" in Eqs. (2)–(5) and "phonon losses" in
  Eqs. (15)–(16); also C ≈ 2.2–2.9 is quoted in "eV" although Eq. (16) makes it dimensionless [CONFIRMED, REF-B]. (4) *App. A* (HTML
  Eqs. (22)–(23) = PDF (A6)–(A7)) writes Var = Fn + η(1−η)n (source η = detection efficiency ϵ_det). Binomial thinning gives
  Var = ϵ_det²F_ehn + ϵ_det(1−ϵ_det)n exactly, so **F_meas = ϵ_detF_eh + 1 − ϵ_det, not F_eh/ϵ_det + 1 − ϵ_det** (WP5v3-C2a). The text's 0.130/0.160 at
  ϵ_det = 0.98/0.95 are close to the exact 0.133/0.159 (0.130 is the exact value at F = 0.112, the low end of their band; WP5v3-C2e); Eq. (23)
  gives 0.137/0.171 (WP5v3-C2b). **Bound direction (corrected reason, A-14, B-14):** R&K call their approximation "a lower bound on the
  measured Fano factor". The relevant comparison is R&K's formula against the exact one: (F/ϵ + 1 − ϵ) − (ϵF + 1 − ϵ) = F(1 − ϵ²)/ϵ =
  F(1/ϵ − ϵ) ≥ 0 (WP5v3-C2d), so their expression is an **upper** bound on the exact F_meas and the "lower bound" is wrong. v2's reason,
  F_meas − F_eh = (1 − ϵ)(1 − F_eh) ≥ 0, compares measured with intrinsic and says nothing about the direction of R&K's approximation; withdrawn.

### 6.3 L22: displacement threshold and defect energy loss
- **Source [FT].** 1805.09942 Eq. (1): Ê = E(1 − f). Eq. (4): f_DF = 1 − (1−f)/(1−f_sur) = (6.08 ± 0.18)% at 103 keV ²⁰⁶Pb in Ge. TRIM maps
  this to E_d = 19.7^{+0.6}_{−0.5} eV, with "TRIM predicts a monotonic, decreasing relationship between the percent energy lost to defects …
  and E_d". 2301.06592 Eq. (8): R(t) = ∫_{4π}∫_{E_th(θ,φ)} d²R/dE_rdΩ_r, with E_th(θ,φ) from the MD E_d surface (17.5–77.5 eV in Si).
- **URF chain.** 1. Seed (W9). 2. (W3), ion type, first moment of E_st and N_FP. 3. E_d from (W10) on E^ad_0. 4. Truncations: E^ad_0 → empirical
  potentials (SW, Tersoff; the source of the reported 7–30 eV Ge spread); drop the R_I(0) sampling (zero-point/thermal) and the IA Doppler
  spread, which makes the step sharp; NRT/Kinchin–Pease counting N_FP^{NRT} ≈ 0.8E_dam/2E_d (E_dam the damage energy) with stored energy per
  defect E_st,1, so f_DF ≈ p_surv·0.4(E_dam/E_R)E_st,1/E_d (p_surv the survival fraction) [E]; this reproduces TRIM's decreasing f_DF(E_d) at
  fixed E_st,1. **[A-9]** "N_FP^{NRT} carries NRT's 0.8 (Kinchin–Pease: E_dam/2E_d). The measured f_DF (1805.09942) is an NR/ER
  phonon-minus-Luke deficit at the surface: δ_coll + (r_coll-term) + (D′_NR − κ_calD′_ER)/ω, containing E_st, ΔE_trap (polarity-dependent), surface
  ΔE_esc and the collection terms. It bounds p_surv E_st,1/E_d ≤ 0.20 (95% C.L.) only under Δϵ ≥ 0, r_coll ≥ 1, X^{oth}_NR ≥ κ_calX^{oth}_ER
  (X^{oth} including ΔZPE) and E_st/ω ≤ 1 − y_ion. TRIM's per-displacement energy is not stated (UNRESOLVED)." **[v4] Numbers** (WP7-E-v3 §3.2;
  WP5v4-C35): the 95% C.L. bounds on ⟨E_st⟩/E_R are **0.055 (Si, 1803.02903) and 0.064 (Ge, 1805.09942)** without ΔZPE (WP7-E-v3 table), and
  **0.056 / 0.065** if a ΔZPE of ≤ 1% of E_st [E] is not cancelled (the values quoted in SOTA, IF-E8); p_surv E_st,1/E_d ≤ 0.21 (Si) / 0.20 (Ge);
  p_surv ≲ 0.47 / 0.66 (0.48 / 0.67 with ΔZPE), with E_dam/E_R = 0.65 / 0.8 [E] and E_st,1/E_d = 9/20 / 6/19.7 [E]. Inputs [FT, 1805.09942]:
  "(6.08 ± 0.18) %" (PDF p. 1 abstract, p. 5); the weighted mean "(6.08 ± 0.08) %", the detectors "differ by 2.06 standard deviations" and "were
  biased with opposite polarities" (p. 5). 5. 2301.06592's additional assumption, ionization threshold = E_d, is **not** a URF limit: the
  ionization threshold is the §3.3 kinematic or Landau–Zener threshold. In a calorimeter, crossing E_d (through P_FP, (W10)) produces a heat
  **deficit** E_st, not a threshold ((W11); E_d is not itself an energy entry, WP7-E-v3 Theorem E-1; §R13.1 K11).
- **Validity.** BO-MD is controlled at E_R ~ E_d: ξ_Mas ≈ 15, λ_dB ≈ 0.01 Å (WP5v3-C6a, C17), no electronic excitation (WP5v3-C5). The empirical
  potential is the dominant error. The IA Doppler width of the seed is ~1 eV (WP5v3-C7); this is a **lower bound** on the step width (B, L22).
- **Leading URF corrections.** (a) A smooth P_FP(E_R, r̂_R) with width σ ≳ √(E_d⟨ω⟩) ≈ 1 eV (Si): the Doppler width of the seed energy only;
  the PES-intrinsic (direction-averaged, thermal-lattice R_I(0)) contribution is not estimated, so "~1 eV, predicted, not tuned" (§3.1) is
  a lower bound [E]. (b) Anisotropic E_st(E_R, r̂_R): a daily
  modulation of the **heat** response near E_d, in addition to that of the ionization threshold. (c) Amorphous-pocket stored energy beyond
  isolated Frenkel pairs (2408.07518), which also seeds §4. (d) Post-cascade annealing makes f_DF time-dependent.
- **Discrepancies.** (Source quotes CONFIRMED in FT by REF-A: 1805.09942 Eq. (4), 6.08 ± 0.18%, 19.7 eV, the TRIM sentence; 2301.06592
  Eqs. (5)–(6) and "E_th … assumed to be correlated with the threshold displacement energy", REF-B.) (1) 1805.09942's E_d depends on TRIM's
  internal stored energy per displacement, not stated. The measured quantity is the NR/ER deficit combination of A-9 above, which
  **bounds** ⟨E_st⟩/E under (B-a)–(B-d) of WP7-E-v3 §3.2 (v3's "the measured quantity is ⟨E_st⟩/E" is withdrawn, §R13.1 K10); the physical
  carrier of E_st is the formation energy, not E_d. (2) 2301.06592 Eq. (6) writes v_min = √(2m_nE_r)/(2μ_{m_D−N}); m_n must
  be the nucleus mass, while the same symbol labels the nucleon in μ_{m_D−n} (Eq. (5)). (3) Ionization threshold = E_d (2301.06592) conflicts
  with Si QF data non-zero down to ~0.7 keV but not with a threshold at E_d; in the URF the two thresholds are physically distinct.

### 6.4 L23: Fano factor F_eh and ε_eh
- **Source [FT].** 2004.10709 Eq. (3): F = σ²/n_eh = σ²ε_eh/E_r (Fano's definition). Eq. (16): ε_eh = C·E_g + E_r, C ≈ 2.2–2.9 (the Klein form;
  here E_r = phonon losses). Measurements at 5.9 keV, 123 K: F = 0.119 ± 0.002, ε_eh = 3.749 eV (2004.11499 [FT]). Model value F_∞ = 0.115
  (2004.10709 [FT]).
- **URF chain.** Second moment of (W3) with an e–h seed. With (W4) and E_st = E_esc = 0:

  F_eh = Var(ℋ)/(E_g² n̄) = (ε_eh/E_g − 1)·𝔡_H,   𝔡_H ≡ Var(ℋ)/(E_g⟨ℋ⟩),   ε_eh = E_g + ⟨ℋ⟩/n̄   [D, exact given (W4); WP5v3-C3].      (W14)

  **F_eh and ε_eh are the first two moments of the heat partition.** Truncations:
  - (i) Klein limit: no phonon loss during ii; residual KE uniform in k with √E DOS below E_th^{ii} = (3/2)E_g (parabolic, equal masses).
    Then ε_eh = E_g + 2·(3/5)E_th^{ii} = (14/5)E_g (WP5v3-C4a): Eq. (16) with C = 2.8; the phonon term rω₀ is Eq. (16)'s "E_r".
  - (ii) Independent residuals would give F_eh = 54/175 ≈ 0.31 (WP5v3-C4b), 2.6× the data. **The energy constraint and the anti-correlation
    between sibling residuals are the leading physics of F_eh**, not a small correction.
  - (iii) **[E, inconsistent model; no evidential weight] (A-9, B-8).** Phonon shot noise alone, Var(ℋ) ≈ ω₀⟨ℋ⟩, gives
    F_eh ≈ (ε_eh/E_g − 1)ω₀/E_g = 0.121 for Si (ω₀ = 63 meV, E_g = 1.16 eV at 123 K) and 0.155 for Ge (ω₀ = 37 meV) (WP5v3-C19). This truncation
    drops the residual-KE variance entirely, although that variance (0.21 eV² per carrier in the Klein model) exceeds the shot-noise variance ω₀ × (phonon heat per
    carrier) ≈ 63 meV × (0.25–0.5 eV) ≈ 0.016–0.03 eV² (Eq. (16)'s E_r ≈ 0.5–1 eV per pair; R9, VER-WP5-B N1 corrected v3's comparator ω₀⟨E_res⟩;
    WP5v3-C19) is what (ii) identifies as the leading physics. (ii) and (iii) cannot both be leading; the consistent statement is
    F_eh = [Var(Σ residuals, with the energy-constraint anti-correlation) + Var(phonon)]/(E_g²n̄), whose first term is not computed here.
    The Si agreement of (iii) with data is **not** evidence for it, and the number is not cited as support anywhere in this return.
    Ge reference values ~0.11–0.13 [UNVERIFIED].
- **Asymptotics: F_eh is a moment, not a parameter [D, sketch] (A-8, B-18).** n̄(ω) = ω/ε_eh + b_N + o(1) and Var N_eh = F_ehω/ε_eh + O(1)
  follow from the key renewal theorem for a reduction of (W3) of convolution form m(E) = ∫m(E − x)F_loss(dx) + …, **under the hypotheses**:
  (r1) a stationary (E-independent) loss law F_loss at large E; (r2) F_loss non-lattice (non-arithmetic); (r3) F_loss has a finite second
  moment. Each can fail: (r2) fails for the (R-k) one-mode truncation (losses on the lattice generated by {ω₀, E_g}), which leaves a periodic
  term in n̄(ω) − ω/ε_eh (toy: deterministic loss d gives m(E) − E/d = −{E/d}, WP5v3-C24); full band-structure kernels satisfy (r2)
  generically. (r1), (r3) fail for a fast primary with a knock-on tail ∝ W⁻² up to E/2: ∫W²F(dW) ∝ E (WP5v3-C24), so corrections can be O(ln ω),
  not o(1). What holds **without** the theorem: ε_eh and F_eh are computable functionals of (W1)–(W2) (moments of (W3)). Near threshold
  F_eh(ω) is not constant: 0 in the forced region, with structure set by (W8).
- **Nuclear-recoil Fano [D under conditional independence of the cascade given E_el].** F_NR = F_eh + Var(E_el)/(ε_eh⟨E_el⟩) (WP5v3-C12b;
  with the §3.3 caveat that ε_eh must be the NR-seed conversion, not ε_eh^γ). At 25 keV in Si, Lindhard gives ⟨E_el⟩ ≈ 9.1 keV (WP5v3-C12a).
  F_NR ≈ 24 (2206.13639 [ABS]) then requires σ(E_el)/⟨E_el⟩ ≈ 10% (WP5v3-C12c) [E]: the second moment of the Lindhard partition, a computable
  target for §3.4.
- **Validity.** **[A-10]** (W14) needs "carriers to thermalise at the band edges, with no capture, no exciton formation and negligible bias work
  before t_pr, no photon escape, and E_st = 0 (ER); otherwise (W14) uses ℋ_eff = ℋ + E_trap^{pr} + E_es + E_pairs^{unp} + ΔE_X^b − 𝒲_bias(t_pr) in
  place of ℋ, with N_eh = N_e^f + N_X, ΔE_X^b = −N_XE_x^b ≤ 0 and E_pairs^{unp} = (N_h^f − N_e^f)(μ_F − E_v) (WP7-E-v3 (E1-W4), C13a). (W14)
  concerns created pairs. The reported Fano factor is F_meas^{obs} = [F_eh⟨m_ind²⟩ + ⟨Var𝔮⟩]/⟨𝔮⟩ + ⟨N_eh⟩Var_r m_ind/⟨𝔮⟩ (WP7-E-v3 (E12)), with
  m_ind(r) ≡ ⟨𝔮|r⟩, which reduces to ϵ_detF_eh + 1 − ϵ_det for single-position charge collection" ((W4′); WP5v4-C32 for (W14) with ℋ_eff,
  WP5v4-C36 for F_meas^{obs} by exact enumeration).
  The asymptotics need ω ≳ 50 eV and (r1)–(r3); at ≳ keV the (B2) Coulomb caveat applies.
- **Leading URF corrections.** The finite-ω structure F_eh(ω) from (W8); then measurement thinning F_meas = ϵ_detF_eh + 1 − ϵ_det (WP5v3-C2),
  which corrects R&K App. A; **[A-13]** then prompt capture via (W4) as amended (A-1), and post-prompt trapping, excitons (E_X), induced
  charge and luminescence escape via WP7-E-v3 (E1), (E8), (E12).
- **Discrepancies.** As §6.2(4) (with the corrected bound-direction reason). Also the R&K model F ≈ 0.115 sits below the skipper-CCD
  0.119 ± 0.002; with exact thinning ϵ_det ≈ 0.995 would reconcile them (WP5v3-C2c) [E]. Source quotes (Eq. (3), Eq. (16) with
  C ≈ 2.2–2.9, F_∞ = 0.115) CONFIRMED by REF-B.

---
## 7. Status of the WP0 defects found in v1 (now adopted in WP0-v2; flag F3)
| v1 ID | Defect | WP0-v2 status |
|---|---|---|
| WP5-1 | v1 WP0 (7.3) second formula integrated q out before seeding | adopted: WP0-v2 (7.3) = (W6) |
| WP5-2 | v1 WP0 (7.3) single-operator weight | adopted: tr[𝔇S(q,ω;Λ)]/tr[𝔇S(q,ω)] in WP0-v2 (7.3) |
| WP5-3 | v1 WP0 (7.1) plasmon label next to RPA cvk pairs double counts | adopted: WP0-v2 (7.1), L11; CONVENTIONS §13 item 21 |
| WP5-4 | R&K called the Λ-marginal kernel | adopted: WP0-v2 (7.3), L21 (photon-seed fit; θ_seed) |
WP0-v2 is consistent with this return on (7.2)–(7.3), (5.5), Theorem D sectors and the L20–L23 pointers (WP0-v2 (9.7)), with four R8
items flagged to WP0 (§10): (i) WP0-v2 §6.2(iii)'s "𝓜¹^{(e)}" wording for the X share invites the misreading corrected in §3.1 (X events
carry the recoil; A-18, A rubric (d)); (ii) the plasmon-label rule of (7.1) / CONVENTIONS §13 item 21 needs the undamped-pole exception
(§1.1(a)); (iii) the O4-d11 Γ/δ map is Si-only (B rubric (d)); (iv) the tr[𝔇ᵀS] index order (SOTA-R7; adopted in WP0-v3, AUDIT-2 m21).

---
## 8. Uncertainty hand-over (WP6)
Nuisances are increments Δ^τ_k entered with WP6's positivity-preserving types (WP0-v2 (8.1); CONVENTIONS §11), not v1's additive increments.
They act on P_casc(N_eh|Λ; θ) (the continuous yield model WP6 O6-3 asks for), one θ per physics item, shared across targets where the physics is:
| θ | Increment | Type | Size / prior |
|---|---|---|---|
| θ_seed | photon (q ≈ 0) vs DM seed, computed as a difference at n_gen = 1 | Δ (until computed), then M | **no prior bound** (R&K's α family is e/h-symmetric; A-20, B-13); computed |
| θ_{R-k} | (R-k)/(R-k′) vs k-resolved n_gen = 2 on a subset (gap R2) | M | computed |
| θ_GW | GW vs vertex-corrected ii rate in (W1) | M | ±20% [E] |
| θ_Z | quasiparticle residue: (W1) at Z_qp = 1 vs 2Z_qp\|ImΣ\| (0812.2923 Eq. (1), Z ≈ 0.8) — global, not near-threshold (A-1) | M | 0.8–1 [E] |
| θ_exch | exchange (0812.2923 Eq. (5) form, Theorem C(d); beyond the first-order hypothesis) | M | computed |
| θ_Eg | ZPR band edge (L12) | E (energy shift) | σ_E from the ZPR uncertainty |
| θ_𝔉 | Fano term in non-PT targets (W15), c^F per (W17) | A on P (sign-free, Σ_ν𝔉_ν = 0) | bound \|ΔP\| ≤ 2π max\|c^F\|; [E] ≲ 0.3 Γ/δ worst case (0.11 Γ/δ optimistic central) (GaAs; Γ/δ map for GaAs unknown); 0 for Si, Ge (Ge Kramers-summed) |
| θ_dense | (B2) violation (carrier–carrier Coulomb, n_pair a_X³ ≳ 1) in ≳ keV ER and all NR tracks | M | [C], unestimated |
| θ_PES | MLIP vs empirical vs DFT E_d, E_st | Δ / M | spread of the three |
| θ_LZ | TDDFT functional for the Landau–Zener channel (gap R3) | M | functional spread |
| θ_esc | **[A-11]** escape only | M | per detector |
| θ_tr^{pr} | **[A-11]** prompt capture fraction | T on the two-point measure, f₀ = 10⁻³, ψ = ln 10.09 (1% at θ = 1) | per material and field |
| θ_unrel | [A-11, WP7-E-v3 §6] E_st^{rel}/E_st per class | T (two-point) | central from WP7-T-v2 computed Γ on t_obs; ψ per σ_λ = 2 [E]; class, T |
| θ_λ, θ_γ | [A-11, WP7-E-v3 §6] Γ_path | M | σ_ln = 2σ_λ (σ_λ = 2 [E]); 2σ_γ/γ (0.3 [E]); material |
| θ_𝒦 | [A-11, WP7-E-v3 §6] shape of 𝒦^{rel} at fixed sum rules | T (constraints ∫∫𝒦^{rel} = ⟨N_hop⟩, ∫∫E𝒦^{rel} = E_st^{rel}) | 𝒩(0,1); class |
| θ_law | [A-11, WP7-E-v3 §6] {1/t, t^{−3/2} 1D/3D, exp} | Δ | discrete profiling; class |
| θ_st | [A-11, WP7-E-v3 §6] ⟨E_st⟩/E_R scale | M | central MD; one-sided data bounds 0.055 (Si), 0.064 (Ge) at 95% C.L. under (B-a)–(B-d) (≤ 1% wider with ΔZPE); material |
| θ_tr | [A-11, WP7-E-v3 §6] ℓ^tr_{e,h}, track trap density | M | per-detector calibration; σ_ln = 0.5 [E]; 1803.02903's collection efficiency only as a one-sided, model-flagged product ≥ 0.75 (100 keV); detector, flash state |
| θ_em | [A-11, WP7-E-v3 §6] athermal Γ^{em}_j | M | σ_ln = 2.3 [E]; detector, history |
| θ_SC | [A-11, WP7-E-v3 §6] field map, E_es | Δ + M | per exposure state; detector |
| θ_coll | [A-11, WP7-E-v3 §6] δ_coll = Δϵ/ϵ_prim and r_coll = ϵ_NTL/ϵ_prim | M on (1 − δ_coll) and on r_coll | median 1, σ_ln 0.05 each; profiled jointly with θ_st through η^φ_NR (the degenerate direction); material–sensor |
| θ_X | [A-11, WP7-E-v3 §6] exciton formation and recombination fractions | T (two-point) | central from WP7-E-v3 §7 kinetics; f₀ ≥ 10⁻³; material, field, T |
| θ_bg,𝔠 | [A-11, WP7-E-v3 §6] background reservoir amplitudes | A | log-normal per run, σ_ln 1; run |
**[v4]** The WP7-E-v3 rows add one exact constraint: η^φ_NR ties θ_coll, θ_st, θ_tr and θ_esc, and must be imposed in the exact form (W11′)
(the procedure of WP5v4-C34), not the r_coll = 1 combination (§R13.3 for the WP6-v3 type checks). Two exact constraints restrict the v3 rows. (W4) ties θ_GW, θ_Z and θ_{R-k} to ε_eh and F_eh: the two measured numbers ε_eh and F_eh at 5.9 keV
constrain two combinations of these three nuisances, leaving one direction free. θ_Z (a global factor 0.8–1 on Γ_ii) and θ_GW (±20% on the
same rate) are largely degenerate: WP6 must treat them as correlated (or merge them into one M-type factor on Γ_ii) (VER-WP5-B N3). (W13) does the same for η_pb. WP6's discrete yield-model choice {step, R&K, URF} (WP6 table, type Δ) is kept until
the URF cascade is computed; then it is replaced by the θ above (I4 closed: WP6-v2 writes ε_eh).

---
## 9. Exact remaining gaps
- **R1.** The quasiparticle (BTE) definition of the ii rate beyond first order in W (the Z factor itself is θ_Z), where 0812.2923 Eqs. (1) and (5) differ. An NEGF/Kadanoff–Baym
  treatment of the three-QP final state would settle it. Size: |Eq.(1) − Eq.(8)|/Eq.(1) of 0812.2923, through Z_{kn} and W versus W_R.
- **R2.** (Extended, A-10.) The (R-k) error O(Γ_E/Γ_k) is an estimate with no proven bound below ~1 eV above threshold, and (R-k) itself
  fails above ~3–5 eV in Si where Γ_ii ≳ Γ^{ph}; there the reduction rests on the unproven (R-k′) (ii final states iso-energy random). Both
  regions are where p_2 is decided.
- **R3.** The close-collision excitation kernel dP/dω_e(b_imp, E_coll) relies on adiabatic-XC TDDFT, whose gap and level-crossing errors are
  uncontrolled. G3's charge channel below E_R,th rests on it.
- **R4.** Triggered (avalanche) annealing at T ≪ T_× and the e^{−E/E_slope} spectrum are [C].
- **R5.** (Narrowed.) The case-I seed for ω ≈ 2Δ_BCS–4Δ_BCS (the no-cascade region, §5) is WP4 [4.6]; what remains is its GRPA-vertex size at
  q ≲ 1/ξ_coh (WP4).
- **R6.** Excitons (E_x^b), shallow-dopant trapping and indirect-gap luminescence escape **[A-14]** enter (W4) (prompt capture), (W11) and
  WP7-E-v3 (E1) (E_X), (E8), (E12); not computed here (exciton kinetics: WP7-E-v3 §7, G-E10).
- **R7.** The exact 𝔉_{Λ₀,ν} in GaAs needs the response code's export (O4-d7, WP3), the O(1) prefactor of (W17) from O4, and a GaAs Γ/δ map;
  (W15) is a bound with an [E] phase.
- **R7′ (R9, AUDIT-2 IF-R8-10).** No package supplies a GaAs Γ/δ map (OW0-10, O-WP3-6): it is recorded as an exact remaining gap. Until it
  exists, the GaAs θ_𝔉 uses only the rigorous bound |ΔP| ≤ 2π max|c^F| and the K_ν ≥ 0 condition is unverified for GaAs.
- **R8 (new).** (B2) at ≳ keV: carrier–carrier Coulomb/Auger scattering in dense tracks (θ_dense); and truncation 0 (BCA + Markov) for dense
  NR cascades (thermal spikes in Ge).

---
## 10. Interface flags
Moved to the closing section "Interface flags" (v3 flags I1–I8, IF-R8-1…10 unchanged there, plus the R13 flags).

---
## 11. Status summary after R7
Gaps R1–R8 are in §9. Status of the WP5 [D] claims after R7: Theorem C (W1) [D] as the out-rate under the stated hypotheses (Z_qp = 1, first
order in W); (W3) [D] under (B1), (B2), (B3), (H-t), (H-m) with (B2) [E]/[C] by scope; (W4), (W14) [D] exact; (W7) [D] under (R-k) or (R-k′),
error [E]; (W8) [D]; (W15) [D] with (W17); the asymptotics [D, sketch]; thresholds, Born parameter, (B2) densities, GaAs 𝔉 size [E].
**After R13 (v4).** (W4) [D] under its stated conditions, (W4′) [D] in general (WP7-E-v3 (E1-pr), Theorem E-0); (W6) [D] given WP7-E-v3 (H-E6);
(W11) [D] for the algebra with multiplicative collection (first order in d′, δ_coll), (W11′) [D]; (W12) obeys T-1 [D] under §R13.3 (i)–(v); the
E_st bounds [D] for the algebra, [E] for inputs; (W14) [D] with ℋ_eff.

---
## R8.1 Referee disagreements and how they are settled
- **(D1) 2209.04503's reduced-energy constant: is Z₁ = 12 used in C? REF-A: UNRESOLVED; REF-B: CONFIRMED. B is right.** Settled by
  re-reading the full text for R8 (fetched, read at the cited passage, deleted). Page 1 defines a = 0.8853a₀/Z, Z = Z₁^{0.23} + Z₂^{0.23}, "with
  suitable values of the effective atomic numbers of the incident ion and the target atom Z1 and Z2", and C = 16.2616/(ZZ₁Z₂) keV⁻¹; page 4
  states "the effective number of valence electrons in the incident ion is Z1 = 12, while Z2 = 14". The same symbols, explicitly the
  *effective* numbers, enter C. The arithmetic (WP5v3-C10a,b) gives 0.0268 keV⁻¹ (+10% vs Lindhard's 0.0243) with Z₁ = 12 and 0.0226 (−7%) with
  Z₁ = 14; the paper's own prescription selects the first. The non-transferability conclusion holds under either reading (|Δ| ≥ 7%), which
  REF-A also notes. Wording changed to "Bohr-stripped effective Z₁" (B).
- **(D2) Renewal asymptotics. REF-B: add "non-lattice"; REF-A: also stationarity and a finite second moment, which fail for a W⁻² knock-on
  tail, so downgrade to [D, sketch]. A's is the complete statement; both are adopted.** Derivation (WP5v3-C24): a lattice loss law leaves a
  periodic remainder (B's point), and a W⁻² tail has ∫W²dF ∝ E, violating the finite-second-moment hypothesis of the key renewal theorem
  (A's point); B's fix alone does not cover the second failure, so the tag is [D, sketch] with (r1)–(r3) stated (§6.4).
- **(D3) Migdal/GS bookkeeping: size. REF-B: "negligible, δM/M ≤ 2.7×10⁻⁴"; REF-A: the omitted P_Mig·E_R term dominates at keV. Both are right
  on different points; A is right on which term dominates, B is right that it is negligible against the listed nuisances.** The two
  prescriptions are the same: (1 − P_Mig)S^{GS} with M_κ + δM_κ reproduces the exact split f-sum − E^{Mig}_1 − P_Mig q²/2M_κ through first order,
  the residual being O(P_Mig δM/M, (δM/M)²) (WP5v3-C20b). Sizes (WP5v3-C20c): P_Mig ≈ 5×10⁻³ at 1 keV against δM/M = 2.7×10⁻⁴; crossover at
  E_R ≈ 53 eV. So the correction is P_Mig-dominated above ~50 eV (A), and ≈ 0.5% at 1 keV, below every listed nuisance (B); it grows ∝ E_R to
  ~5% at 10 keV (R9, VER-WP5-A N4), where it is no longer negligible against the NR nuisances.
- **(D4) GaAs Fano-term estimate. REF-A: use spread ≤ 1, so ≲ 0.3Γ/δ; REF-B: quote the rigorous bound 2π max|c|·spread and keep 0.11Γ/δ at most as a
  central value. Compatible; both adopted:** bound 2π max|c^F| (spread ≤ 1 is exact for probabilities), [E] worst case 0.3Γ/δ (A), 0.11Γ/δ as
  the optimistic central value (B).
- **(D5) (B2) scope. REF-A: holds for the ≲ 100 eV seeds, [C] at keV; REF-B: error unestimated at ≳ keV.** Agree at keV. On the small seeds
  my estimate (§1.2, WP5v3-C25) gives n_pair a_X³ ≈ 0.5 for 30 pairs in a 10 nm-radius cloud, so (B2) there is marginal [E], not established;
  see rebuttal R8.2-(b).
- **(D6) 2506.03810 inference. REF-A: the "friction-model property" judgement is UNRESOLVED (not checkable in the text); REF-B: fair.** It is
  not a literature claim: the quote is CONFIRMED by both, and the inference is our physics [E], derived from the binary threshold (§3.3),
  now with the soft-threshold caveat. Marked so in §6.1(4).
- **(D7) Mott density. REF-B: ~4×10¹⁸ cm⁻³; REF-A: 10¹⁸–10¹⁹.** Consistent; quoted as ~10¹⁸–10¹⁹ cm⁻³ [E]. The argument does not depend on the
  value: n_pair at 1 keV is ≥ 7×10¹⁹.
Items raised by one referee only (B-3 plasmon; A-1 Z factor and exchange; A-10 (R-k); A-17(a),(c); B-12 L20 observable; B-15 item 7) are not
disagreements; each is applied (§R8.3).

## R8.2 Rebuttals (these go back to the named referee)
- **(a) To REF-A, V4/§2 (applied with a refinement).** REF-A writes that "𝔊 ≡ const spuriously solves (W3) at ϑ = 0". At ϑ = 0, under (H-t),
  𝔊 = E[1] = 1 **is** the true solution. Spurious solutions arise when (H-t) fails: with 𝔊 defined as E[e^{ϑ·𝐍}; termination], 𝔊(0) is the
  termination probability, the minimal non-negative root, while 1 is a second root. Example (WP5v3-C23): f(s) = (1 − p) + ps² has roots 1 and
  (1 − p)/p; for p = ¾ the minimal root is ⅓. (H-t) and (H-m) are both adopted (§1.2), with this statement of why (H-m) matters.
- **(b) To REF-A, V5 (scope of (B2), applied with a restriction).** REF-A says (B2) "holds for the eV–100 eV DM-electron seeds (≲ 30 pairs)".
  With REF-A's own criterion n_pair a_X³ ≪ 1 and a_X ≈ 4 nm: 30 pairs within a 10 nm-radius sphere give n_pair = 7×10¹⁸ cm⁻³ and
  n_pair a_X³ ≈ 0.46 (WP5v3-C25 scaled by 30/300); a smaller cloud (a 100 eV electron's range is a few nm) gives more. So (B2) for those seeds
  is marginal, not controlled. §1.2 states it as [E] there and [C] at keV; the Pauli part (B2a) is satisfied in both.
- **(c) To REF-A, V16 / §5 table (rating of the Z₁ = 12 claim).** UNRESOLVED → CONFIRMED, by the full-text passages quoted in (D1): the paper
  prescribes the effective Z₁, Z₂ in C and sets Z₁ = 12, Z₂ = 14. The −7% alternative applies only if the paper's own prescription is ignored.

## R8.3 Closing table (one row per referee item)
Status key: **applied** (correction made), **applied + dropped** (a claim removed or marked UNRESOLVED), **stands** (verdict STANDS; kept,
no change needed), **rebutted (part)** (applied, but one point rebutted in §R8.2).
| Item | Verdict | Status | Where |
|---|---|---|---|
| A-1 | (W1) out-rate; Z factor; exchange beyond hypothesis | applied | §1.1 (W1), (W16), "Relation to the GW lifetime", (d); §2; §8 θ_Z, θ_exch; WP5v3-C22 |
| A-2 | ε_ion ↔ g^L code-pair conditions | applied | §1.1(c) WP5-cp1–cp3; §1.5 O4-d2; §2 |
| A-3 | Born parameter Z_κα/v_F ≈ 15 | applied | §1.1(e); §3.3; §6.1 Validity; WP5v3-C6b |
| A-4 | (H-t), (H-m); (B2) density | rebutted (part) | §1.2 (H-t), (H-m); §R8.2(a); WP5v3-C23 |
| A-5 | (B2) density and criterion | rebutted (part) | §1.2 (B2a,b); §8 θ_dense; R8; §R8.2(b); WP5v3-C25 |
| A-6 | Lindhard needs BCA + Markov | applied | §1.2 moments; §6.1 chain step 3 (truncation 0) |
| A-7 | R&K/KP/F_NR moments | stands | §1.2, §6.2–§6.4 unchanged |
| A-8 | renewal asymptotics → [D, sketch] | applied | §6.4 (r1)–(r3); §2 grid; WP5v3-C24 |
| A-9 | (W14) stands; (iii) inconsistent | applied | §6.4 (iii) [E, inconsistent model]; WP5v3-C19 |
| A-10 | (R-k): Γ_ii in Γ_E; (R-k′); R2 | applied | §1.4 (W7); §6.2 step 2; §9 R2 |
| A-11 | thresholds 352/395 eV; soft | applied | §3.3; §6.1; WP5v3-C5a–c |
| A-12 | R&K [A] = E³ | stands | §6.2(1) kept; C1c made a real dimensional check |
| A-13 | \|M\|² CONFIRMED; "Δ undefined" REFUTED | applied + dropped | §6.2(2): "Δ undefined" withdrawn |
| A-14 | App. A: reason for the bound | applied | §6.2(4); §6.4; WP5v3-C2d |
| A-15 | 2001.06503 claims | stands | §6.1(1)–(2) kept |
| A-16 | ½εS_e REFUTED; Z₁ UNRESOLVED | applied + dropped; rebutted (part) | §6.1(3) withdrawn and replaced (WP5v3-C26); Z₁: §R8.1(D1), §R8.2(c) |
| A-17 | (W15): c^F dimensions; spread ≤ 1 → 0.3Γ/δ; Ge Kramers | applied | §1.5 (W17), estimate; §8; WP5v3-C14e–g; IF-R8-4, -5 |
| A-18 | Migdal/GS bookkeeping; C20b,c | applied | §3.1; WP5v3-C20b,c; IF-R8-1; §R8.1(D3) |
| A-19 | spec: fix Z/rate definition and code-pair conditions | applied | §2 Formula and kernels |
| A-20 | θ_seed: 50% misattributed; α family cannot bound | applied + dropped | §6.2(a) claim UNRESOLVED, not used; §8 θ_seed; IF-R8-6 |
| A-(a) | (R-k) error tag; 𝔉 = 0 in Ge needs SOC caveat | applied | §1.4 [E]; §1.5 |
| A-(c) | 2209.04503 Eq. (3) is U_EDFT | applied | §6.1 source line |
| A-(d) | flag WP0-v2 §6.2(iii) 𝓜¹^{(e)} wording | applied | §7; IF-R8-1 |
| A-(f) | "rigorous" (W15) needs dimensional c^F | applied | §1.5 (W15) + (W17) |
| B-1 | (W1) = Γ_out; LFE index; anti-Hermitian; differential rate | applied | §1.1 (W1), (W1′), (W16); WP5v3-C21a,b, C22; IF-R8-2 |
| B-2 | ε_ion ↔ g^L condition | applied | §1.1(c) WP5-cp1–cp3 |
| B-3 | plasmon = e–h channel only inside the continuum; Al | applied | §1.1(a); §5; WP5v3-C27; IF-R8-3 |
| B-4 | Born parameter | applied | as A-3 |
| B-5 | (W3), moments | stands | §1.2 (L20 observable: B-12) |
| B-6 | (B2) density; Mott criterion | applied | §1.2 (B2a,b); §R8.1(D5), (D7) |
| B-7 | (W4), (W14) exact | stands | §1.2, §6.4 |
| B-8 | Klein numbers; (ii) vs (iii) | applied | §6.4 (iii) |
| B-9 | thresholds 352/395 eV; "vanishes" → suppressed | applied | §3.3; §6.1 Validity and correction (a); WP5v3-C5 |
| B-10 | (W15) bound stands; estimate imports Si Γ/δ; negative K_ν | applied | §1.5 (estimate, K_ν ≥ 0 condition, signed sampler); WP5v3-C14e; IF-R8-5, -10 |
| B-11 | Migdal: not an operation on S; negligible; C20b,c vacuous | applied | §3.1; WP5v3-C20b,c; §R8.1(D3) |
| B-12 | L20: ν = ℋ_nuc + E_st; truncation (A); U | applied | §6.1 chain steps 2–4; §6.1 discrepancy (5) |
| B-13 | L21: step-model region; seed envelope [E] | applied | §6.2 Validity; §6.2(a); WP5v3-C18 |
| B-14 | R&K claims: units, \|M\|² CONFIRMED; Δ REFUTED; App. A reason; C in "eV"; T only via E_g | applied + dropped | §6.2 source line and Discrepancies (1)–(4); WP5v3-C1c, C2d, C2e |
| B-15 | 2001.06503/2209.04503 claims; ½εS_e REFUTED; u in f_n missed | applied + dropped | §6.1 Discrepancies (1)–(5); WP5v3-C26 |
| B-16 | 2506.03810, 2301.06592 CONFIRMED | stands | §6.1(4); §6.3 |
| B-17 | (W8), (W9) | stands | §1.4, §3.1 |
| B-18 | renewal: non-lattice | applied | §6.4 (r2); WP5v3-C24 |
| B-19 | C1c, C7b, C14e, C20b, C20c not checks | applied | code/WP5-v3/checks.py: all five replaced |
| B-20 | contested corrections: none | n/a | rebuttals now in §R8.2 |
| B-L22 | step width √(E_d⟨ω⟩) is a lower bound | applied | §3.1; §6.3 |
| B-(d) | §1.5 uses Si Γ/δ for GaAs | applied | §1.5; IF-R8-10 |
| B-(e) | G1 spec inherits V1(ii) and V2 | applied | §2 |
**Counts (40 numbered items A-1…A-20, B-1…B-20):** applied 27 (A-4, A-5 included), applied + dropped 5 (A-13, A-16, A-20, B-14, B-15), stands 7 (A-7, A-12, A-15,
B-5, B-7, B-16, B-17), n/a 1 (B-20); rebutted in part 3 (A-4, A-5, A-16, all applied otherwise; A-16 counted under applied + dropped).
Claims dropped: "Δ undefined" (R&K), "½εS_e not derived" (2209.04503), "~50% in p_2" (marked UNRESOLVED, not used), plus the withdrawn numbers
375/465 eV, 3.7×10², ≲ 10¹⁹ cm⁻³ and the identities "(W1) = 2|ImΣ|" and "never accurate beyond ω < 2E_g". The seven unnumbered sub-items (A-(a),
(c), (d), (f), B-L22, B-(d), B-(e)) are all applied. **Self-found (from SOTA-R7 cross-package notes):** the 3Δ_BCS → 4Δ_BCS no-cascade
limit (§5; IF-R8-7) and the tr[𝔇ᵀS] index order in (W6) (IF-R8-9).
The v2 closing table (R6 corrections 1–29: renames, owed WP0-v2 flags F2, F3, F6, F8, F11, audit A11, NOTATION v4) remains applied in this
text; rows 11 (𝔉 size) and 27 (drag-mass subtraction) are superseded by A-17/B-10 and A-18/B-11 above.

---
## 13. Literature
**13.1 Rubric-(c) claims after R7 (claims about what published papers say or get wrong).** Kept only if CONFIRMED; REFUTED ones dropped;
UNRESOLVED marked. Other citations (data, methods) keep their v2 tags.
| Paper | Claim | Rating | Kept? |
|---|---|---|---|
| 2004.10709 | [A] must be energy³ ("5.2 eV²" inconsistent) | CONFIRMED (A, B) | yes, §6.2(1) |
| 2004.10709 | Eq. (9) unsquared \|M_ph\|/\|M_eh\| | CONFIRMED (A, B) | yes, §6.2(2) |
| 2004.10709 | "Δ undefined" | REFUTED (A, B) | **dropped** |
| 2004.10709 | E_r symbol collision | CONFIRMED (A, B) | yes, §6.2(3) |
| 2004.10709 | C ≈ 2.2–2.9 quoted in "eV" for a dimensionless C | CONFIRMED (B) | yes, §6.2(3) |
| 2004.10709 | App. A: F/η + 1 − η wrong; exact ηF + 1 − η; numbers | CONFIRMED (A, B) | yes, §6.2(4) |
| 2004.10709 | "lower bound" has the wrong direction | CONFIRMED (A, B), with the corrected reason | yes, §6.2(4) |
| 2004.10709 | T dependence only through E_g(T) | CONFIRMED (B) | yes, §6.2 source |
| 2004.10709 | "~50% in p_2 at 4–8 eV" | UNRESOLVED / misattributed (A) | marked, not used |
| 2001.06503 | boundary-condition inconsistency (their own remark) | CONFIRMED (A, B) | yes, §6.1(2) |
| 2001.06503 / 2209.04503 | reduced energies 0.0243 vs 0.0268 keV⁻¹ (Z₁ = 12 in C) | CONFIRMED (B; re-read for R8; A's UNRESOLVED rebutted) | yes, §6.1(1) |
| 2209.04503 | ½εS_e "not derived" | REFUTED (A, B) | **dropped**; replaced by our (D)-inconsistency objection |
| 2209.04503 | Lindhard's Z^{1/6} by hand; U "effectively incorporates the Migdal effect"; χ²/dof 1870/101, 680 eV–3 MeV | CONFIRMED (A, B) | yes, §3.1, §6.1 |
| 2209.04503 (2001.06503 per B) | u counted in the electronic fraction f_n = (ε + u − ν̄)/(ε + u) | CONFIRMED (B; re-read for R8) | yes, §6.1(5) |
| 2001.06503 | validity ranges 𝓔_red ≳ 0.1 (Si), ≳ 0.00088 (Ge) | CONFIRMED (B) | yes, §6.1 |
| 2506.03810 | "halted … below 10 eV_nr, as no ionization occurs below this threshold"; Eq. (3) friction | CONFIRMED (A, B); inference is ours [E] | yes, §6.1(4) |
| 2301.06592 | Eq. (6) m_n vs nucleon μ (Eq. (5)); E_th = E_d assumption | CONFIRMED (A, B) | yes, §6.3 |
| 1805.09942 | Eq. (4), 6.08 ± 0.18%, 19.7 eV, TRIM sentence | CONFIRMED (A) | yes, §6.3 |
| 0812.2923 | Eq. (1) τ⁻¹ = (2Z/ħ)\|ImΣ\|, Z ≈ 0.8; Eq. (5) exchange; Eqs. (1)/(8) contain no M_E | CONFIRMED (A) | yes, §1.1 |
**13.2 Sources.** **R13:** full text re-read for the amendment: 1803.02903 (PDF pp. 3, 5, 6, 8, 17), 1805.09942 (pp. 1, 5), 2007.14289 (pp. 2, 4,
6), PDFs deleted; [FT] via WP7-E-v3 (not re-read here): 2202.05097, 2208.02790, 2405.10405 (§4(b) of WP7-E-v3), 2209.04503 (also v3 R8 re-read).
arXiv IDs verified against the API: literature/papers-WP5-v4/arxiv-*.json (all 29 arXiv IDs cited in this return). 2007.14289 moves from "abstract only" to full text.
Full text read (v1): 2004.10709; 2209.04503 (re-read at pp. 1, 4 for R8, then deleted); 2001.06503; 1805.09942; 2301.06592;
0812.2923; 1401.1937; 2506.03810; 2004.11499 (results). Abstract or title only: 2408.07518, 1703.05371, 2603.16702, 2405.10405, 2206.13639,
2112.14495, 2210.01557, 2503.03683, 2406.15425, 2104.01811, 2101.08263, 2002.06937, 2003.12077, 2306.14944. Campaign sources used
as recorded: WP0-v2; WP2 (3.6), (5.2), (5.3); WP3 (W.1), N3; WP4 [4.6], L15; WP6 §5–§7, O6-3; O4 (O4.7), d1–d11; R7 referee reports and
SOTA-R7. Not on arXiv (cited by content): Lindhard et al. 1963; Fano 1947; Klein 1968; Kaplan et al. 1976; Chang–Scalapino;
Cohen–Bergstresser 1966; Echenique–Nieminen–Ritchie [UNVERIFIED values].

---
## 14. Symbols introduced/used
Moved to the closing section "Symbols introduced/used" (v3 table unchanged there, plus the R13 rows).

---
## R9 clean-up (VER-WP5-A, VER-WP5-B new items; returns/R8/AUDIT-2.md rows addressed to WP5)
Checks re-run after the edits: code/WP5-v3/checks.py **55/55 PASS** (C18, C19, C20c, C26, C27 revised).
| Item | Defect | Action | Where |
|---|---|---|---|
| VER-A N1 | L20 Discrepancy (3): the forward-peaking (dσ_n-weighted ⟨T_n⟩) argument uses the wrong weight; 2001.06503 Eq. (29) weights T_n by the electronic loss | second half withdrawn; the cross-term-vanishes-under-(D) half kept [D]; C26 now checks only that half | §6.1(3); WP5v3-C26 |
| VER-A N2 | circular b_N in the step-model failure point | ω ≳ ε_eh(2.1 − b_N) with b_N not computed: ≈ 7–9 eV for \|b_N\| ≲ 0.3 [E] | §6.2 Validity; WP5v3-C18 |
| VER-A N3 | "u booked electronic" overstated | restated: only U spent in secondary displacements is booked electronic (by complement); primary u is in ν̄; bound u/(ε+u) withdrawn, size [E] | §6.1(5) |
| VER-A N4 | P_Mig size needs a range | ≈ 0.5% at 1 keV, ≈ 5% at 10 keV, ∝ E_R, soft-limit [E]; ⟨r²⟩ = 1 Å² flagged as an input pending WP3's P_Mig(q) | §3.1; §R8.1 (D3); IF-R8-1; WP5v3-C20c |
| VER-B N1 | §6.4(iii)/C19 comparator | ω₀ × phonon heat per carrier ≈ 0.016–0.03 eV² (not ω₀⟨E_res⟩); conclusion strengthened | §6.4(iii); WP5v3-C19 |
| VER-B N2 | §1.5 K_ν ≥ 0 sentence reapplied the Si Γ/δ map to GaAs | "holds wherever Γ/δ ≲ 1.7; GaAs awaits its own map" | §1.5 |
| VER-B N3 | §8 "two" nuisances (now three); θ_Z/θ_GW degenerate | two constraints on three nuisances, one direction free; WP6 to treat θ_Z and θ_GW as correlated or merge them | §8 |
| VER-B N4 | C27 "whole f-sum" holds only as q → 0 | restricted to q → 0; at finite q < q_c the continuum below qv_F shares the f-sum, no e–h weight at ω_pl | §1.1(a); WP5v3-C27 |
| AUDIT-2 m20 | §1.1(c) "four-class" vs WP0-v3 G14 "three classes + ionic phonon-bridge insertions" | caveat sentence added (wording only) | §1.1(c) |
| AUDIT-2 m21 | (W6) note / §1.3 kept "tr[𝔇S]" meaning Σ𝔇_abS_ab | written tr[𝔇ᵀS] throughout; IF-R8-9 closed | §1.3; §7; §10 |
| AUDIT-2 m5 | Si Γ/δ map is 0.007–0.2 at δ₀ = 0.3 eV (WP3-v3 §M4), not 0.02–0.6 | quoted values updated; still Si-only, not used for GaAs | §1.5; IF-R8-5, IF-R8-10 |
| AUDIT-2 §8 IF-R8-10 | nobody supplies a GaAs Γ/δ map | recorded as exact remaining gap R7′ | §9 R7′; IF-R8-10 |
| AUDIT-2 B3 | WP0/WP3 omit the X-sector recoil (WP5 §3.1 is the reference) | no WP5 change needed: WP5 §3.1 already states 𝓜¹_X = E^{Mig}_1 + P_Mig q²/2M_κ; action is WP0/WP3's | §3.1; IF-R8-1 |
| AUDIT-2 m6, m15; §8 IF-R8-3/4/5/8 | owners WP0, WP3, NOTATION, coordinator | no WP5 change; flags stand as raised | §10 |
| AUDIT-2 §8 N-entries for WP5 (G8, G10, WP1 IF-17, WP3 IF-12, WP4 I12–I15) | marked "not needed" for WP5 | none | — |

---
## R13.1 Conflicts between the amendment and the v3 text (WP7-E-v3 wins in every row)
| # | v3 site and text | Amendment | Resolution in v4 |
|---\|---\|---\|---|
| K1 | §1.2: "(with an exciton, E_g → E_g − E_x^b; Si E_x^b ≈ 15 meV; (W14) keeps its form, WP5v3-C30)" | A-1, A-10: exciton and droplet formation are two-body, outside (B2), post-prompt (≳ ns > t_pr); they sit in the reservoir E_X; (W14) uses ℋ_eff with N_eh = N_e^f + N_X and ΔE_X^b | v3 rule withdrawn; C30 kept as algebra only; replaced by (W4′) (C31, C32) |
| K2 | §1.2: (W4) "event by event" as the general law; "all ionization statistics are heat-partition statistics" | A-1: (W4) holds only with no capture, no exciton, negligible pre-t_pr bias work; general law is WP7-E-v3 (E1-pr) | (W4) scoped; (W4′) added; the corollary now refers to ℋ_eff in general |
| K3 | §1.2: "A carrier is absorbing when E < E_th^{ii}; its remaining kinetic energy then goes to ℋ" | A-1: "A carrier at the band edge is non-absorbing until t_pr" | below E_th^{ii} the carrier stops branching and its kinetic energy goes to ℋ (v3 kept); it stays a live state for 𝒦_cap and is absorbed only at t_pr, where it is deposited once by its state; (H-t) read accordingly |
| K4 | §1.2: 𝐍 = (N_eh, ℋ, E_st, N_FP, E_esc, …); NOTATION §G row of the same form | A-2: 𝐍 = (N_e^f, N_h^f, N_e^{tr}, N_h^{tr}, E_trap^{pr}, ℋ, E_st, N_FP, E_esc, N_X, E_X), class and geometry as marks 𝔪 | replaced; N_eh is a derived function of 𝐍 and P_casc(N_eh\|Λ) its marginal; NOTATION row → IF-R13-1 |
| K5 | §1.2 (B3): "no applied field. An NTL drift field adds a deterministic drift term" | A-12: pre-t_pr bias work e ℰ_b v_d t_pr, booked in 𝒲_bias and ℋ; drift otherwise post-prompt | sentence replaced; "no applied field" read as "field-free kernels" |
| K6 | §1.3 (W6): dℛ/d𝐍 with P_casc(𝐍\|Λ) as the observable rate | A-16: dℛ/d𝐌 with P(𝐌, t\|Λ) of WP7-E-v3 (E3), + dℛ_bg/d𝐌 | replaced; v3 form kept as the t = t_pr marginal (C43) |
| K7 | §3.4 (W11): Y_H ≡ ⟨ℋ_meas⟩/E_R; additive deficits; ⟨N_trap⟩E_g; "+ N_eh eV_bias/E_R" in NTL mode; "(W11) follows from (W4)"; unit quenching = "E_st = E_esc = N_trap = 0" | A-4: NR/ER signal ratio at equal ω; multiplicative collection; μ_F-referenced E_trap (⟨N_trap⟩E_g exact only for doubly trapped shallow levels, WP7-E-v3 Theorem E-3); NTL ratio with r_coll; follows from WP7-E-v3 (E1), (E7); unit quenching = δ_coll = 0, D′_NR = D′_ER | replaced (W11); (W11′) added for general r_coll; NOTATION §G row "Y_H ⚠ heat quenching ⟨ℋ_meas⟩/E_R" → IF-R13-1 |
| K8 | §4 (W12): "⊗ (detector response)" | A-6: ⊗ 𝒯_𝔠, visibility ϵ_coll(ε^{hop}_ij + ΔZPE_ij) ≥ E_thr^det | replaced; the δ-argument of (W12) stays configurational |
| K9 | §4: "below T_×: instanton tunnelling Γ_ij ∝ e^{−𝒮_inst}" | A-6: "Below T_× use WP7-T-v2 rates" (WP7-T-v2 IF-T2) | line kept as v3 record, superseded for mK use by WP7-T-v2 (4.2)–(4.3) |
| K10 | §6.3 Discrepancy (1): "The measured quantity is ⟨E_st⟩/E" | A-9: f_DF is δ_coll + r_coll-term + (D′_NR − κ_calD′_ER)/ω and bounds E_st only under (B-a)–(B-d) | v3 sentence withdrawn and replaced |
| K11 | §6.3 step 5: "In a calorimeter E_d produces a heat deficit E_st" | A-3, A-9 (WP7-E-v3 Theorem E-1): E_d enters only through P_FP | reworded: crossing E_d (through P_FP) produces the deficit E_st |
| K12 | §6.4 Validity: "no trapping before counting" | A-10 | replaced |
| K13 | §6.4 Leading corrections: "trapping (N_trap) and exciton or luminescence escape via (W4)" | A-13 | replaced |
| K14 | §8 θ_esc: "escape and trapping (E_esc, N_trap)" | A-11: escape only; θ_tr^{pr} and the WP7-E-v3 §6 rows added | replaced |
| K15 | §9 R6: "enter (W4) and (W11)" | A-14 | replaced |
| K16 | §14 and NOTATION §G: N_trap as a WP5 deposit | A-15: N_e^{tr} + N_h^{tr} before t_pr; n^{e,h}_j after | applied in this return's Symbols; NOTATION row → IF-R13-1 |
| K17 | §3.4 "2007.14289 [ABS]"; §13.2 lists 2007.14289 as abstract-only | WP7-E-v3 cites it [FT] | re-read here (PDF p. 4) and retagged [FT] |
No amendment item was found to contradict a derivation of v3 (only statements of scope, definitions and tags), so no v3 equation other than
(W4) (scope), (W6), (W11) and (W12) (transfer) changes form.

## R13.2 Changelog: A-item → WP5-v4 location
| A-item | Content | WP5-v4 location | Checks |
|---\|---\|---\|---|
| A-1 | trapped type, 𝒦_cap, per-carrier deposits once, excitons post-prompt; (W4) scope and (E1-pr) | §1.2 *Statement* (type list), after "(W2) for e–ph…", *Exact energy bookkeeping*, after (W4); (W4′) | C31 |
| A-2 | additive 𝐍; marks 𝔪 | §1.2 *Statement* | C31 |
| A-3 | E_st configurational; ΔZPE in ℋ_ph; ⟨E_st(t)⟩, T-1 sum rules; E_d via P_FP | §3.2 "Stored energy" (+ [v4] quench reading) | C33c, C38, C39 |
| A-4 | (W11) replaced: multiplicative Y_H(t_win), NTL ratio, unit quenching, η^φ_NR constraint | §3.4 Outputs, (W11) (+ [v4] (W11′)) | C33a–c, C34a–e, C42 |
| A-5 | N^meas = Σ𝔮_i; QF via ⟨𝔮⟩ ratios; 1803.02903 efficiency reading | §3.3, new last bullet | C36 |
| A-6 | (W12) ⊗ 𝒯_𝔠; visibility; sub-threshold releases; WP7-T-v2 rates below T_× | §4 (W12) and the T_× bullet | C38, C41 |
| A-7 | SC absorber and sensor-film bookkeeping | §5, after (W13) | — (definitions) |
| A-8 | (F) implicit Lindhard assumptions | §6.1 URF chain step 4 | — (statement) |
| A-9 | NRT 0.8; f_DF as a deficit combination; bound 0.20 with conditions; TRIM UNRESOLVED | §6.3 URF chain step 4 (+ [v4] numbers) and Discrepancy (1) | C34e, C35 |
| A-10 | (W14) validity; ℋ_eff; F_meas^{obs} | §6.4 Validity | C31, C32, C36 |
| A-11 | θ_esc escape only; θ_tr^{pr}; WP7-E-v3 §6 rows | §8 table and the constraint sentence | C37 |
| A-12 | (B3) pre-t_pr bias work | §1.2 (B3) | C40 |
| A-13 | §6.4 Leading URF corrections | §6.4 Leading URF corrections | — |
| A-14 | §9 R6 | §9 R6 | — |
| A-15 | N_trap restriction | closing Symbols (v3 list) and IF-R13-1 | — |
| A-16 | (W6) → dℛ/d𝐌 with P(𝐌, t\|Λ); cascade-level marginal kept | §1.3 (W6) | C43 |

## R13.3 Consistency checks
**(a) WP7-T-v2 Theorem T-1, conditions (i)–(v), against the v4 text.**
| Condition | v4 text | Status |
|---\|---\|---|
| (i) every hop in 𝒦^{rel}, uphill (ε^{hop}_ij < 0) included | (W12) sums all i ≠ j; ℛ_rel carries negative arguments (heat absorbed, no event through 𝒯_𝔠) | consistent (C38 has an uphill hop) |
| (ii) one E^{conf} table for p_st and the paths | §3.2 E_st (A-3) and (W12) E^{conf}_i ≡ E^ad_0(R_i); **requires R_I(0) → the 𝔅₀ minimum** (the Wigner R_I(0) is ≈ 138 eV high in a 4096-atom cell, C39); §3.4 quench and §4 NEB end states must use one MLIP | consistent **with the [v4] reading**; residual = WP7-E-v3 G-E3 (IF-R13-3) |
| (iii) photon branch kept in E | 𝒯_𝔠 routes to E_esc/E_sig (A-6); film/absorber bookkeeping (A-7) | consistent |
| (iv) Σ_iN_i = 1, closed linear single-seed chain | the sourced (W12) is linear, so per-seed T-1 superposes: ∫_0^t∫dE E ℛ_rel = ∫_0^t Σ_i𝔰_iE^{conf}_i − Σ_iN_i(t)E^{conf}_i, **if the index set contains 𝔅₀ (E^{conf} = 0) and the separated-pair states**; a loss to an unlisted state breaks it (C38: 0.63 eV defect for the toy leak). v3 §4's 1/t law (superposed one-hop decays) is inside; bimolecular recombination, inter-seed reactions (cooldown and stress reservoirs, WP7-E-v3 (E14) (ii)–(iii)) and the triggered avalanches of R4 (non-Markov) are outside, as is the bimolecular θ_law option | consistent; scope stated |
| (v) configurational energies, ΔZPE in ℋ_ph | A-3, A-4 (ΔZPE in D′), A-6 (δZPE only in the observable argument); ZPE sum rule separately (C38) | consistent |
| time-dependent rates | (W12) with stimulated Γ_ij(t; Φ_ph, n_car) (WP7-E-v3 (E5)) is covered (WP7-T-v2 C16b) | consistent |
| E_d once (WP7-E-v3 Theorem E-1) | E_d appears only in (W10), P_FP and the NRT count N_FP^{NRT} (§6.3, multiplied by E_st,1, never as N_FP·E_d) | consistent (K11 wording fixed) |

**(b) WP6-v3 nuisance types (WP6-v3 (5.1)–(5.1″)).**
| θ | Type used | WP6-v3 definition | Status |
|---\|---\|---\|---|
| θ_esc, θ_λ, θ_γ, θ_st, θ_tr, θ_em | M | log-normal multiplicative on a positive scalar | consistent |
| θ_tr^{pr}, θ_unrel, θ_X | T on a two-point measure | (5.1″) with S_c = (1 − f₀, f₀) on {0, 1}, φ = (1) (zeroth moment only), ψ = ln(1 + Δ′/S_c) (R9 form; here Δ′ = 9.09f₀ at the "captured" point); "no new support" ⇔ f₀ > 0 (C37) | consistent |
| θ_𝒦 | T with ∫∫𝒦^{rel} = ⟨N_hop⟩, ∫∫E𝒦^{rel} = E_st^{rel} | (5.1″) on linear moment constraints; needs the constraint vector inside the moment cone of supp 𝒦^{rel} | consistent for multi-path classes; **[v4] note:** for a one-path class (single ε^{hop}) the E-support is one point, so the two constraints are trivially met but the constraint vector cannot lie strictly inside the moment cone and the (5.1″) uniqueness condition (≥ 3 support points) fails in E; θ_𝒦 then reduces to a time-shape nuisance, degenerate with θ_λ/θ_law (IF-R13-5) |
| θ_law | Δ | discrete profiling | consistent; the bimolecular (1 + t/t₀)⁻² option is excluded by T-1 (iv) |
| θ_SC | Δ + M | allowed combination | consistent |
| θ_coll | M on (1 − δ_coll) and on r_coll, median 1, σ_ln 0.05 | positive scalars | consistent as a type; **[v4] note:** the median-1 symmetric prior puts half its mass at δ_coll < 0 and r_coll < 1, outside (B-a)/(B-b). Not a contradiction (the bounds are conditional statements; the profile uses the full prior), but WP6 must report the profiled E_st constraint and the conditional bound separately (IF-R13-5) |
| θ_bg,𝔠 | A | additive, PSD (non-negative) increments | consistent (background templates are non-negative rates) |
| exact constraint η^φ_NR | ties θ_coll, θ_st, θ_tr, θ_esc | WP6-v3 §6 exact constraints | consistent if imposed through (W11′) / the C34 procedure, not the r_coll = 1 combination |
| v3 WP5 rows (θ_seed … θ_dense) | unchanged | WP6-v3 §5.2 yield row (IF6-16) | consistent; θ_esc now "escape only" (A-11) |

## R13.4 Checks (code/WP5-v4/checks.py; C1–C30 = WP5-v3, unchanged; 75/75 PASS)
| Check | Content (independent route) |
|---\|---|
| WP5v4-C31, C31b | (E1-pr) per-carrier deposit sum = N_ehE_g + E_pairs^{unp} + E_trap^{pr} + ΔE_X^b by enumeration of all capture/exciton fates (≤ 3 pairs); μ_F-independence from neutrality and its failure without it; once-per-carrier closure; the double-count is 2(E_c − μ_F) |
| C32 | (W14) with ℋ_eff by brute force over a discrete law; fails with bare ℋ when E_trap^{pr} fluctuates |
| C33a–c | multiplicative Y_H: ϵ_prim cancels; first-order bracket; NTL limit (1 + y_iong_Luke)/(1 + g_Luke); unit quenching; ⟨E_st(t_win)⟩ decomposition from an explicit two-exit master equation |
| C34a–e | η^φ_NR from the calibration procedure (not from closed forms): ϵ_prim cancels; η₀(r_coll); r_coll = 1 first order with κ_cal; general-r_coll weights (W11′); κ_cal = 0.642; r_coll = 1.144 → 0.952; y_ion 0.22–0.35 → 0.947–0.955; (B-d) relation |
| C35 | bounds 0.055/0.064, 0.21/0.20, 0.47/0.66; ΔZPE-shifted 0.056/0.065, 0.48/0.67 |
| C36 | F_meas^{obs} by exact enumeration over positions, N_eh and per-carrier marks 𝔮; single-position limit ϵ_detF_eh + 1 − ϵ_det |
| C37 | two-point type T = WP6-v3 (5.1″) with the zeroth-moment constraint; f(1) = 1.00%; f₀ = 0 cannot move |
| C38 | sourced (W12) T-1 identity (two seeds, uphill hop, 𝔅₀ listed), ZPE sum rule, and a leak counter-example (mpmath expm + quadrature) |
| C39 | harmonic ⟨V⟩ = ω/4 per mode; 3⟨ω⟩/4 per atom; 138 eV per 4096-atom cell (T-1 (ii) reading) |
| C40 | pre-t_pr bias work 4×10⁻⁴ eV and 0.25 eV |
| C41 | visibility: 0.3 × 9 eV = 2.7 eV < 3 eV; pocket N_a ≳ 272 at 16.3 eV |
| C42 | μ_F-referenced trap energies; ΔE_trap < 0 example |
| C43 | (E3) at t = t_pr is the P_casc marginal |

## R13.5 Provenance of values new in v4
Values inherited from v3 keep their v3 tags. Values the amendment brings into this return:
| Value | Tag | Source |
|---\|---\|---|
| η^φ_NR = 95.2^{+0.9}_{−0.7}% (95% C.L.), Si, 10–100 keV | [FT] | 1803.02903 PDF p. 17 ("The weighted average over all detectors of the coadded best-fit results … gives ηNR = 95.2+0.9 −0.7 % at 95% C.L.", text extraction) |
| ε_eh(Si) = 3.82 eV above 77 K | [FT] | 1803.02903 p. 5, footnote 2 |
| V_b = 4 V, 4 V/cm (CDMS II Si) | [FT] | 1803.02903 p. 5 |
| phonon scale on ER "which should have unity ionization yield" | [FT] | 1803.02903 p. 8 |
| f_DF = (6.08 ± 0.18)% (Ge, ²⁰⁶Pb); weighted mean (6.08 ± 0.08)%; 2.06σ; opposite polarities | [FT] | 1805.09942 p. 1 (abstract), p. 5 |
| E_d(Ge) = 19.7^{+0.6}_{−0.5} eV (TRIM inference) | [FT] | 1805.09942 (v3 §6.3, CONFIRMED by REF-A) |
| heat QF = 1 assumed (Si), Ge "very close to unity"; trigger threshold 16.3 eV | [FT] | 2007.14289 p. 4; p. 2 and p. 6 |
| Ge 64 ± 8 eV_ee at 254 eV_nr | [FT via WP7-E-v3] | 2405.10405 (not re-read here) |
| y_ion = 0.3 (0.22–0.35 over 10–100 keV) | [E] | WP7-E-v3 §3.1 |
| E_dam/E_R = 0.65 (Si), 0.8 (Ge); E_st,1 ≈ 9 eV (Si), 6 eV (Ge) | [E] / [UNVERIFIED] | WP7-E-v3 §3.2; v3 §3.2 (formation energies from memory) |
| ΔZPE ≈ 0.1 eV per point defect (≈ 1% of E_st,1) | [E] | WP7-E-v3 §1.1 |
| ϵ_coll = 0.3; pocket energy 0.1–0.2 eV per atom | [E] | WP7-E-v3 §3.3 |
| v_d = 10⁶–10⁷ cm/s, t_pr = 100 ps, ℰ_b = 4–250 V/cm | [E] | WP7-E-v3 C15 |
| E_x^b(Si) ≈ 15 meV | [UNVERIFIED] | v3 value, now tagged |
| ⟨ω⟩(Si) = 45 meV | [E] | WP5v3-C7c |

---
## Symbols introduced/used
**R13 (v4).** All WP7-E symbols are used in their NOTATION names ("Rows added WP7-E", "Rows added WP7"); checked against NOTATION v4 + R9 + WP7
rows for collisions.
*Used as defined in NOTATION "Rows added WP7-E" / "Rows added WP7":* E_hot, E_pairs, E_X, E_trap, E_es, E_es^{trap}, E_es^{img}, E_sig, E_sl,
ℋ_ph = ℋ_ph^{avail} + ΔZPE, ℋ_pr, ΔE_X^b ≡ −N_XE_x^b, N_X, φ_EHD, ΔZPE(t), δZPE (per-hop change; written ΔZPE_ij = ΔZPE_i − ΔZPE_j = ZPE_i − ZPE_j, the WP7-T-v2 §4.1 sign), E_st^{unrel}(t_obs),
E_st^{rel}, E_stored, ⟨N_hop⟩, N_e^f, N_h^f, N_e^{tr}, N_h^{tr}, E_pairs^{unp}, μ_F, ℰ_b, 𝔪, 𝒲_bias, V_k, Q_k, ϵ_prim^{NR}, ϵ_prim^{ER}, ϵ_NTL, Δϵ,
δ_coll, r_coll, D′, d′, X^{oth}, κ_cal, g_Luke, y_ion, η₀(r_coll), E^tr_{e,j}, E^tr_{h,j}, n^{e,h}_j, U_R, 𝔮_i, m_ind(r), N^meas, F_meas^{obs}, t_win,
t_obs, E_thr^det, P_rel, ϵ_coll, dℛ_bg, 𝒯_𝔠, 𝐌, 𝒫_det, θ_unrel, θ_λ, θ_γ, θ_𝒦, θ_law, θ_st, θ_tr^{pr}, θ_tr, θ_em, θ_SC, θ_coll, θ_X, θ_bg,𝔠;
from WP7-T rows: 𝔠, p_st, 𝒦^{rel}, ε^{hop}_ij, ΔZPE_ij; V_b (= V_bias, NOTATION §M). Source-only: 1803.02903 η^φ_NR (as quoted), y_C;
1805.09942 f_DF, f, f_sur.
*Introduced here (R13; new names, checked for collisions):*
| Symbol | Meaning | Where |
|---\|---\|---|
| 𝒦_cap | prompt (t < t_pr) capture kernel onto level j (cascade capture for shallow, multiphonon for deep levels; WP7-E-v3 (E9) at t < t_pr) | §1.2 (A-1) |
| 𝔱 = tr_j | cascade type "trapped on level j" | §1.2 (A-1) |
| ℋ_eff | effective heat of (W14): ℋ + E_trap^{pr} + E_es + E_pairs^{unp} + ΔE_X^b − 𝒲_bias(t_pr) | (W4′), §6.4 (A-10) |
| R_final^{min}, 𝔅₀^{min} | quenched (basin-minimum) end and start configurations of the E_st definition | §3.2 ([v4] reading) |
| P(𝐌, t\|Λ) | marked observable law (WP7-E-v3 (E3)) used in (W6) | (W6) (A-16) |
| (W4′), (W11′) | labels (WP5 (W4′), WP5 (W11′)) | §1.2, §3.4 |
| K1–K17, IF-R13-1…8, WP5v4-C31…C43 | labels | §R13.1, flags, §R13.4 |
**N_trap (A-15):** "N_trap → N_e^{tr} + N_h^{tr} counted before t_pr; post-prompt trap populations are n^{e,h}_j (WP7-E-v3)".

### v3 symbol record (former §14, unchanged except the A-15 entry)
All symbols follow NOTATION v4 and CONVENTIONS; source formulas keep their own symbols with the translation stated (NOTATION §K).
*Used as defined in NOTATION v4:* q, ω, ω_q, v, ρ_χ, f_χ, m_χ, ρ_T, Ω, N, V, 𝔇, ℛ, α, e, v_C, k, k′, n, m, v, c (band subscripts), ε_{nk},
ψ_{nk}, f_{nk}, E_g, E_dir, E_th, ρ_{mn}, ρ̃, Q, ν, ω_{Qν}, n_{Qν}, g_{mnν}, g^S, g^L, ω₀, ⟨ω⟩, ω_max, D_κ, 𝔫_κ, E^kin_q̂, 𝔨₃^{GS}, x_R, M_κ,
Z_κ, A_κ, F^M_κ, c_s (c_κ), z_s, 𝓃_e, P_I, R_I, I, κ, v_N, U_κ/Z_κ(p), S, S_ab, S_cc (= S_chch, ch = c), S(q,ω;Λ), R, ε, ε̃, ε^{-1}_{GG′}, ε_∞,
L, W^{scr}, Z*_κ, ω_p, ω_pl, E_x^b, GS, X0, X+, X, Λ, Λ₀, Λ₊, Ẽ_Λ₀, Γ_Λ₀, Γ^{ph}, Γ^x, Γ^{tot}, Γ^{(f)} (as Γ^{(ν)}), Σ^{FM},
a^{off}, 𝔉_{Λ₀,ν}, c_ν^F (normalised by (W17); c̄^F its Γ-weighted mean), 𝒦_{Λ₀→Λ₊}, δ, δ₀, DC, fp, τ, 𝒳, K, n_g, θ_k, Δ^τ_k, σ_E;
N_eh, N_eh^{step}, P_casc, P(N_eh|q,ω), P_n, 𝐍 (as redefined by A-2), ℋ, E_st, E_esc, E_d, N_FP, N_trap (**[A-15]** "N_trap → N_e^{tr} + N_h^{tr}
counted before t_pr; post-prompt trap populations are n^{e,h}_j (WP7-E-v3)"), 𝔊_x(ϑ), ϑ, 𝒦_c, Γ_ii, Γ_E, Γ_k, dE/dt|_ph, p_no-ii, ε_eh,
ε_eh^γ, F_eh, F_NR, F_qp, F_meas, 𝔡_H, ϵ_det, b_N, E_el, 𝓔_red, k_L, ν̄_L, σ²_strag, U_bind, Y_H, Y_tot, Y_casc, E_R, E_R,th, σ_ω, ξ_Mas, B_h,
E_bar, 𝒩_b, Γ_ij, T_×, N_i, 𝔰_i, 𝒮_inst, S^{stop}_e, 𝔅₀, 𝒰_t, P_FP, N_qp, η_pb, t_esc, E_sub, E_excess, n_gen, Δ_BCS, 𝔤_I, v_F, k_F, ω_e,
ω_ph, n_ph, s^ph, δM_κ, E^{Mig}_1, E_e, E_h (NOTATION §G, added after WP0-v2 F10), P_Mig, ρ^{ph}_κ, T, β.
*Also used (NOTATION v4), new in v3:* n_B (Bose function), q_c (Landau onset), 𝓜¹ (moment), Z_qp (QP residue; NOTATION has it from WP4-v2 §8 for the SC case;
used here for the normal-state carrier residue, the same object, **flagged**); c_ν^F is **redefined dimensionless by (W17)** (**flagged**, IF-R8-4).
*Introduced in v2 (NOTATION v4 §M rows), unchanged:* 𝔱, x′_j, E_car, E_th^{ii}, 𝒦̄_𝔱, M^{ii}_{dir}, M^{ii}_{xch}, E^ad_0, E^{conf}_i, r̂_R, λ_dB, ℓ_int, t_pr,
E^{form}_V, E^{form}_I, h_LZ, ΔF_LZ, P_LZ, b_imp, E_coll, V_bias, ℛ_rel, ω_bar, Γ_att, E_slope, α²F, E₁, E₂, Γ_pb, Γ_esc, d_film, ω_D, ξ_coh,
N_FP^{NRT}, E_dam, E_st,1, p_surv, θ_seed, θ_{R-k}, θ_GW, θ_exch, θ_Eg, θ_𝔉, θ_PES, θ_LZ, θ_esc, a₀.
*Introduced here (R8; new names, checked against NOTATION v4 for collisions):*
| Symbol | Meaning | Where |
|---\|---\|---|
| Γ^{out}_{nk}, Γ^{in}_{nk} | out- and in-scattering rates; 2\|ImΣ\| = Γ^{out} + Γ^{in} | (W1), (W16) |
| W_{GG′} (with ε⁻¹v right index) | screened interaction matrix, = W^{scr} in G-space | (W1′) |
| 𝔱 = pl, Γ_pl | plasmon cascade type for an undamped pole; its damping rate | §1.1(a), §5 |
| WP5-cp1–cp3 | e–e/e–ph code-pair conditions (labels) | §1.1(c) |
| α_E | Ewald (range-separation) parameter of g^L | §1.1(c) |
| (H-t), (H-m) | termination and minimal-solution hypotheses (labels, as WP5-H-t, WP5-H-m) | §1.2 |
| n_pair, a_X | local pair density of a track; exciton Bohr radius | §1.2 (B2) |
| (B2a), (B2b) | Pauli and Coulomb parts of (B2) | §1.2 |
| (R-k′) | iso-energy ii final-state hypothesis (label) | §1.4 |
| ℋ_nuc | heat delivered to atomic motion through the ion branch (Lindhard's ν without the electronic sub-cascade) | §6.1 |
| U_FP, U_EDFT | source symbols (2209.04503) for the Frenkel-pair and inner-shell parts of U_bind | §6.1 |
| 𝓜⁰_GS, 𝓜¹_GS, 𝓜¹_X | zeroth/first energy moments of the GS and X sectors per nucleus | §3.1 |
| F_loss, (r1)–(r3) | renewal loss law; its hypotheses (labels) | §6.4 |
| θ_Z, θ_dense | WP5 nuisances: QP residue; (B2) violation | §8 |
| IF-R8-1…10 | interface-flag labels | §10 |
Labels: WP5 (W1)–(W17) (plus (W1′)), WP5v3-C1…C30, R1–R8 (as WP5-R1…), I1–I8 and IF-R8-1…10, (R-k), (R-k′), (CSDA), (B1)–(B3),
(H-t), (H-m) (as WP5-…; O4's are O4-B1, O4-B2), WP5-cp1–cp3, A-n / B-n (R7 referee verdicts).

---
## Interface flags
**R13 flags (new).**
| # | Owner(s) | Item | Action |
|---\|---\|---\|---|
| IF-R13-1 | NOTATION §G | rows "𝐍 = (N_eh, ℋ, E_st, N_FP, E_esc, …)", "N_trap", "Y_H ⚠ heat quenching ⟨ℋ_meas⟩/E_R" are stale after A-2, A-15, A-4 | replace by the A-2 vector (N_eh derived), the A-15 restriction, and "Y_H(t_win): NR/ER heat-signal ratio at equal ω (multiplicative collection)" |
| IF-R13-2 | WP7-E-v3 (E13), A-4; LIMITS L38 | the κ_cal combination is exact to first order only at r_coll = 1; at general r_coll the weights are (1 + g_Luke)/(1 + r_collg_Luke) and (1 + g_Luke)(1 + r_collg_Luke y_ion)/(1 + r_collg_Luke)² ((W11′), WP5v4-C34b; 0.931 and 0.576 at r_coll = 1.144) | add "+ O((r_coll − 1)δ_coll, (r_coll − 1)d′)" to A-4 / L38 or quote (W11′); the E_st bounds (C7g) are unaffected |
| IF-R13-3 | WP7-E-v3 G-E3; WP7-T-v2 (5.1), T-1 (ii); WP5 §3.4, §4 spec | E_st needs both ends quenched (R_I(0) → 𝔅₀ minimum; else ≈ 34 meV per atom, C39); one MLIP and one quench protocol for E_st, p_st and the NEB end states | adopt the reading; WP5-AUD to confirm |
| IF-R13-4 | WP7-T-v2 IF-T2, IF-T9 | IF-T2 (sub-T_× rates): applied (A-6, §4). IF-T9 (signed seed weights at phonon poles, do not clip): not among A-1…A-16; v3 §1.5 already samples signed K_ν weights | noted; extend the signed sampler to defect seeds at the next WP5 revision |
| IF-R13-5 | WP6-v3 §5.2 | WP7-E-v3 rows θ_tr^{pr} … θ_bg,𝔠 and θ_esc "escape only" (A-11); η^φ_NR constraint via (W11′); θ_coll prior extends outside (B-a)/(B-b); for one-path classes θ_𝒦 is a time-shape nuisance degenerate with θ_λ/θ_law (no E-freedom; (5.1″) interior condition fails) | WP6 to add the rows, use (W11′), and report the profiled E_st constraint separately from the conditional bound |
| IF-R13-6 | coordinator: SOTA, LIMITS | bounds quoted as 0.056/0.065 (SOTA, with ΔZPE) and 0.055/0.064 (WP7-E-v3 table, without): both are now in §6.3 with their conditions | none needed beyond the LIMITS rows below |
| IF-R13-7 | coordinator: state/CORRECTIONS.md §18 last row | "applied by R13 WP5-ERR → returns/R13/WP5-v4.md" | returned; mark the row done; WP5-v3 is now read through WP5-v4 |
| IF-R13-8 | WP0-v3 (7.3) | (W6) is now the marked observable law; WP0-v3 (7.3) is its t = t_pr marginal | consistent; optional pointer in WP0 |

### v3 interface flags (former §10, unchanged)
**v2 flags (status unchanged unless stated).**
| # | Owner | Quantity | Status in v3 |
|---\|---\|---\|---|
| I1 | WP4 | η_pb = Δ_BCS⟨N_qp⟩/ω | CLOSED (audit A11); see IF-R8-7 for the no-cascade range |
| I2 | WP2 | IA width σ_ω² = 4E_RE^kin_q̂; GS f-sum; ρ^{ph}_κ sign | applied in (W9); the GS-moment part is **superseded by IF-R8-1** |
| I3 | WP1 | retarded out-state weight | CLOSED (audit A11) |
| I4 | WP6 | ε_eh; yield model | CLOSED (audit A11); new θ's in IF-R8-6 |
| I5 | WP3 | X+ joint seed | CLOSED (audit A11) |
| I6 | WP3, O4 | 𝔉 export (O4-d7) | open; see IF-R8-4, IF-R8-5 |
| I7 | NOTATION | E_e, E_h | CLOSED (audit A11) |
| I8 | CONVENTIONS / WP0-v2 | S_cc ≡ S_chch ≡ S_zz | no content mismatch (confirmed by A and B) |

**New R8 flags: every change that alters a quantity another package uses.**
| # | Owner(s) | Quantity | v2 form | v3 form | Action |
|---\|---\|---\|---\|---\|---|
| IF-R8-1 | WP0-v2 §6.2(iii) and rule (a); WP2-v2 IF-2, (3.4), §5.2′; WP3 J3 | GS seed moments when Migdal is seeded separately | 𝓜¹_GS = q²/2M_κ − E^{Mig}_1, "rescale the first moment by 1 − δM/M" | 𝓜⁰_GS = 1 − P_Mig, 𝓜¹_GS = (1 − P_Mig)q²/2M_κ − E^{Mig}_1; prescription (1 − P_Mig)S^{GS} with M_κ + δM_κ (§3.1, WP5v3-C20b); size ≈ 0.5% at 1 keV, ~5% at 10 keV [E] | WP0 to reword 𝓜¹^{(e)} (the X share carries the recoil); WP2/WP3 to adopt the prescription |
| IF-R8-2 | WP0-v2 (5.4), (7.1); WP1, X2 if they quote Theorem C | carrier rate | (W1) = 2\|ImΣ^{GW}\|; LFE kernel Σρ*_G v_C(p+G) Im(−ε⁻¹_{GG′})ρ_{G′} | (W1) = Γ^{out}; 2\|ImΣ\| = Γ^{out} + Γ^{in} (W16); LFE kernel −2Im(ρ†Wρ), W = ε⁻¹v_C(p+G′), anti-Hermitian part (W1′) | cite (W1′)/(W16); same anti-Hermitian rule as WP0-v2 CC-1 |
| IF-R8-3 | WP0-v2 (7.1); CONVENTIONS §13 item 21; WP4 (metals) | plasmon as a final state | "Λ = cvk only within RPA" (always) | holds when ε₂(ω_pl) > 0; an undamped RPA pole (metals, q < q_c) is a final state 𝔱 = pl with its own decay (§1.1(a), §5, WP5v3-C27) | add the exception to item 21 and to WP0 (7.1) |
| IF-R8-4 | O4 (O4.7); NOTATION row "𝔉_{Λ₀,ν}, c_ν^F" | Fano coefficient | c_ν^F = Im(ρ*a^{off}) (dimension \|ρ\|²/energy) | c_ν^F = Γ_Λ₀ Im(Σ_Kramers ρ*a^{off}_ν)/\|ρ_Λ₀\|² (W17), dimensionless; Kramers-summed with SOC | O4 to fix the O(1) prefactor; NOTATION row to state the normalisation |
| IF-R8-5 | WP6-v2 θ_𝔉 row (§5.2, row 31); WP3-v2 IF-4 | GaAs Fano-term size | \|ΔP\| ≲ 0.11Γ/δ (2×10⁻³ … 7×10⁻²) | rigorous \|ΔP\| ≤ 2π max\|c^F\|; [E] ≲ 0.3Γ/δ worst case, 0.11Γ/δ optimistic; GaAs Γ/δ map unknown (the O4-d11 map, 0.007–0.2 at δ₀ = 0.3 eV, is Si's) | WP6 prior and WP3 IF-4 to carry the bound and the worst case |
| IF-R8-6 | WP6-v2 §5.2, §15 | WP5 nuisances | θ_seed prior "≤ 50% in p_2"; θ_exch an M-type on/off | θ_seed: no prior bound (computed); new θ_Z (0.8–1, global), new θ_dense ([C]); θ_exch beyond the first-order hypothesis | WP6 to add θ_Z, θ_dense and drop the θ_seed prior |
| IF-R8-7 | WP4-v2 §4.6 (line "= 2Δ_BCS/ω for ω < 3Δ_BCS") | no-cascade range | N_qp = 2 for ω < 3Δ_BCS | ω < 4Δ_BCS (§5, WP5v3-C15a), consistent with REF-WP4-A/B | WP4 to correct 3Δ → 4Δ |
| IF-R8-8 | coordinator: SOTA §(line "Binary e–ion collisions … 375 eV (Si) and 465 eV (Ge)"); LIMITS rows L20, L23 | thresholds; L20/L23 status lines | 375/465 eV, sharp; "½εS_e not reproduced"; "F ≈ 0.121 [E]" | 352/395 eV, soft (suppressed, not zero); Born parameter ≈ 15/35; ½εS_e: derived in 2001.06503 App. B, objection is the (D)-inconsistency; F ≈ 0.121 has no evidential weight; L20 observable ν = ℋ_nuc + E_st with BCA as truncation 0 | coordinator to update SOTA and LIMITS |
| IF-R8-9 | WP0-v2 (3.4), (7.3); CONVENTIONS §8 (SOTA-R7 REF-WP0-A) | rate contraction | tr[𝔇S] | tr[𝔇ᵀS] = Σ_ab𝔇_abS_ab in (W6) and §1.3 | CLOSED (R9): WP0-v3 and CONVENTIONS §8 adopted it (AUDIT-2 G1, m21) |
| IF-R8-10 | WP0-v2 O4-d11; WP3 | Γ/δ map | used for GaAs in v2 §1.5 | Si only (WP3-v3 §M4: 0.007–0.2 at δ₀ = 0.3 eV); GaAs needs its own map | nobody supplies it: recorded as exact remaining gap R7′ (AUDIT-2) |

---
## Proposed LIMITS rows
No new L-numbers: the WP7-E-v3 rows L33–L38 already carry the new chains. Proposed amendments to the WP5 rows (the coordinator assigns; ✎ = corrected):
| # | Chain (URF) | Change proposed | Status |
|---\|---\|---\|---|
| L20 | (3.4) GS imp → (W9) → (W3) first moment | add to the implicit assumptions (A-8): "U = 0 ⇒ E_st = 0; 𝔮 = 1, E_trap = 0; 2209.04503's secondary U is frozen stored energy booked electronic by complement" | DERIVED (chain), REFEREED (R7) ✎ |
| L21 | (W6) → (W5) → (W3) + truncations | (W6) is now the marked observable law; R&K/step model are statements about P_casc(N_eh\|Λ), its t = t_pr marginal (A-16) | DERIVED (✎), REFEREED (R7) — wording only |
| L22 | (W9) → (W3) → (W10) | measured f_DF (1805.09942) = δ_coll + r_coll-term + (D′_NR − κ_calD′_ER)/ω (A-9); bound p_surv E_st,1/E_d ≤ 0.20 (95% C.L.) only under (B-a)–(B-d); see L36; E_st needs quenched end states (IF-R13-3) | DERIVED, REFEREED (R7) ✎ |
| L23 | second moment of (W3) with (W4) | validity per A-10: no capture, no exciton, negligible bias work before t_pr; otherwise (W14) with ℋ_eff (W4′); reported Fano factor F_meas^{obs} (L35) | DERIVED, REFEREED (R7) ✎ |
| (W11) | heat quenching | the v3 truncation "E_st = E_esc = N_trap = 0" is replaced by L37 (δ_coll = 0, D′_NR = D′_ER); the Si datum enters through L38 with the IF-R13-2 remainder | pointer to L37/L38 |
