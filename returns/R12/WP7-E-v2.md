# R12 / WP7-E-v2: one time-resolved energy and charge balance per event (yields, defects, delayed release), corrected after R11

Revision agent, coordinator R12 correction round. Supersedes returns/R10/WP7-E.md (v1, historical record); this version reads without it. Inputs:
referees/R11/REF-WP7-E-A.md (cited **A-n**, its verdict rows; **A§k.m** its sections) and REF-WP7-E-B.md (**B-n**, **B1–B11**, **C1–C8**, **D1–D4**,
**E**, **F**, **G**). Architecture: returns/R8/WP0-v3.md ("WP0 (n.m)"); cascade: returns/R8/WP5-v3.md ("WP5 (Wn)"); defect kinetics: returns/R10/WP7-T.md
("WP7-T (n.m)"). **returns/R12/WP7-T-v2.md does not exist at the time of writing**, so the λ convention is WP7-T's (Δ_ij = ω₀e^{−λ_ij}, Γ ∝ e^{−2λ}) and the
release sum rule is (E6) below, flagged to WP7-T-v2 (IF-E2). CONVENTIONS.md, NOTATION v4 + R9 rows; state/CORRECTIONS.md read (no owed item touches the sites used).
Checks: `code/WP7-E-v2/checks.py` (sympy + mpmath, **36 checks, all PASS, ≈ 2.3 s**), cited Ev2-Cn. v1's identity checks are removed. Each new check
compares two independent routes to the same quantity: field energy against a Green's-function pair sum, battery work against field energy plus
dissipation, order statistics against the Ramo current, an exact mixture variance against the formula, exact calibration algebra against its series,
and a 3D diffusion PDE against the capture law. Tags per CONVENTIONS §12. Literature [FT] = re-read in full text for R12 in literature/papers-WP7-E-v2/
(1803.02903, 1805.09942, 2007.14289, 2202.05097, 2208.02790; PDFs deleted after use) or quoted through WP5-v3's [FT, CONFIRMED] quotes; arXiv IDs verified
against the API in R10 and re-fetched. WP5-v3 is not edited (§5 is the amendment text). Status: CLAIMED, refereed R×2 (R11), corrected here.
**Novelty (B, rubric f).** (E1) is a bookkeeping synthesis of WP5 (W4), WP7-T and standard detector physics, not a new result. The collective-stress reading
of the low-energy excess and the time-law discriminant are the authors' own in 2208.02790; they are credited there.

---
## 0. Results at a glance
| # | Item | Result | Tag |
|---|---|---|---|
| 1 | Balance law | (E1): ω + 𝒲_bias = E_hot + E_pairs + E_x + E_trap + E_es + E_st(t) + ℋ_ph + E_esc + E_sig + E_sl; μ = μ_F (contact Fermi level); E_st includes ΔZPE | D given (H-E1)–(H-E3) |
| 2 | Completeness | the space-charge/image reservoir E_es is the Green's-function energy of the uncollected charges (C2a). Battery work = ΔE_es + NTL heat holds exactly with space charge (C2b) | D |
| 3 | Two stages | (E3) holds given the sufficiency hypothesis (H-E6); 𝔠, r_ev, the t_pr phonon spectrum and the carrier-cloud geometry are **marks**, not additive components of 𝐍 | D given (H-E6) |
| 4 | E_d once | E_d is not a ledger entry (it is the median of P_FP, (W10)); WP7-T gives E_st(t), (E5); sum rule (E6) cut at t_obs | D |
| 5 | Yields | yield models act on E_el. E_st ⊂ E_nuc **for defect creation**; carrier-driven defect reactions are a post-prompt cross-channel E_el → ΔE_st | D (creation) / E (reactions) |
| 6 | Charge once | doubly trapped pair stores E_g − E^tr_e − E^tr_h; a singly trapped carrier whose partner is collected stores μ_F − E_v − E^tr_h (or E_c − E^tr_e − μ_F), plus its image energy (C1c, C2e) | D |
| 7 | NTL | 𝒲_bias = eV_bN^meas (Ramo, exact even with space charge, C2c); NTL heat = 𝒲_bias − ΔE_es (C2d). Multi-electrode (ZIP/iZIP): sum over electrode pairs | D |
| 8 | Measured charge | (E12) conditional on r_ev; the reported F_meas adds ⟨N_eh⟩Var_r⟨𝔵\|r⟩/⟨𝔵⟩, which grows with N_eh (C6a,b) | D |
| 9 | Calibrated observables | every QF, Y_H and η^φ is an NR/ER ratio: η^φ_NR = 1 − d_NR + κd_ER + O(d²), κ = (1 + y g)/(1 + g), g = eV_b/ε (C7a); Y_H in ratio form with ΔE_trap (E8) | D |
| 10 | Data constraints on E_st | 1803.02903 (Si): η^φ_NR = 95.2^{+0.9}_{−0.7}% ⇒ d_NR − 0.64 d_ER = 0.048; 1805.09942 (Ge, ²⁰⁶Pb): f_DF = 6.08 ± 0.18%. With everything attributed to E_st: p_surv E_st,1/E_d ≤ 0.18 (Si), 0.19 (Ge) | D (algebra) / E (inputs) |
| 11 | mK charge release | thermal frozen (exponent 10⁴); field emission needs ≈ 1.2×10⁴ V/cm (corrected from 10⁶), i.e. 10²–10⁴ above detector fields; Poole–Frenkel 2 meV at 100 V/cm (C10) | D / E |
| 12 | Delayed events | one visibility criterion ϵ_coll ε ≥ E_thr^det. Single Frenkel-pair releases need E_thr ≤ 2.7 eV. Pocket recrystallisation (event-seeded, collective) is visible for N_a ≳ 270 atoms at a 16 eV threshold. TLS give power: total = per-λ excess × Δλ ≈ 1.4×10⁷ eV (C11, C12) | D / E |
| 13 | LEE data | stress-dependence (2208.02790) **and** a stress null (2202.05097); the single exponential is rejected in the best bin (χ²/dof = 4192/68). Collective-release reading stays [C] | C |
| 14 | Literature limits | Lindhard (U = 0), modified Lindhard (secondary U frozen, booked electronic), R&K (E_stored = 0, 𝔵 = 1), KP (E_dam/2E_d) vs NRT (0.8), TRIM (inference UNRESOLVED), QF data as **NR/ER ratio** measurements | D |
| 15 | WP5 amendment | A-1…A-16 (§5): eleven rewritten or kept, plus the four missing sites and (W6) | D |
| 16 | Nuisances | 12 θ in WP6 types (M, A, Δ, T; type T on a two-point measure = logit for fractions); priors stated | D (types) |

---
## 1. The balance law

### 1.1 Hypotheses and reservoirs
(H-E1) *Reservoirs.* H_tot = H_C (WP0 (1.1)) + H_sens + H_hold + H_rad + H_bias. Between collisions (WP5 (B1)) ⟨H_tot⟩ for a state of definite quasiparticle
content equals the sum of the reservoir energies below, which include the pair-binding (E_x) and long-range Coulomb (E_es) parts of V_ee among excited
carriers. Short-range inter-reservoir interaction energies are O(Γ/E) and act only during collisions. (H-E2) *Contacts* are in equilibrium at Fermi level μ_F
(band-aligned gauge, A§1.1, B4), with no injection. 1803.02903 [FT]: carriers "relax to the Fermi level at the electrodes". (H-E3) The bias is external and the
electrodes are held at fixed potential. (H-E4) Post-prompt processes are Markov in the full reservoir microstate. (H-E6) is in §1.4; (H-E5) in §2.3.
| Reservoir | Definition | Value at t_pr | Owner |
|---|---|---|---|
| E_hot(t) | carriers above band edges, hot ions, core holes, undamped plasmons (𝔱 = pl) | E_hot(0⁺) = ω − ω_ph(Λ) (X+ seeds put ω_ph in ℋ_ph at the vertex; GS regime (i) seeds are pure phonons; B11); 0 for t ≥ t_pr (WP5 (H-t)) | WP5 |
| E_pairs(t) | Σ_{free e}(E_c − μ_F) + Σ_{free h}(μ_F − E_v) | unbound free carriers | WP5 / §2 |
| E_x(t) | −Σ_{bound pairs} E_x^b (free/bound excitons), −Σφ_EHD (electron–hole-droplet condensation per pair, Ge/Si) | where excitons form before t_pr | WP5 R6 / §2 |
| E_trap(t) | Σ_j[n^e_j(E_c − E^tr_{e,j} − μ_F) + n^h_j(μ_F − E_v − E^tr_{h,j})] | E_trap^{pr} | WP5 (< t_pr), §2 |
| E_es(t) | electrostatic energy of uncollected charge (pair Coulomb, image, space charge): ½Σ_{ij}q_iq_jG(r_i,r_j), G the Green's function of the grounded electrodes | ≈ 0 (pairs unseparated) | §2 |
| E_st(t) | vibrational ground-state energy of the occupied basin minus that of 𝔅₀: E^ad_0(R̄) − E^ad_0(R_I(0)) + ΔZPE (B1) | E_st of WP5 §3.2 (+ ΔZPE) | WP5, WP7-T |
| ℋ_ph(t) | absorber phonon energy above the bath | ℋ_pr (= WP5 (W4) ℋ; the brief's "Q_prompt") | WP5, WP2 (3.6) |
| E_esc(t), E_sig(t), E_sl(t) | cumulative escaped energy; sensor energy converted to signal; sensor loss | prompt luminescence; 0; 0 | WP5; detector |
| 𝒲_bias(t) | cumulative work of the bias source = Σ_electrodes V_k ΔQ_k | 0 | detector |
**Lemma 1 [D] (C1a,b).** d(E_pairs + E_trap)/dμ = N_h,tot − N_e,tot over uncollected carriers, so "any μ" holds only for a neutral crystal. Once one carrier of a
pair has been collected, only μ = μ_F makes the ledger physical. A singly trapped hole stores μ_F − E_v − E^tr_h (C1c): this is contact-dependent,
O(E_g/2), and differs from the doubly trapped E_g − E^tr_e − E^tr_h (C1d). It also carries the image energy of its own charge, which for a planar sheet is
σ²z′(d − z′)/2d and vanishes at the contacts (C2e).
**Truncation statement.** E_x and φ_EHD are meV per pair (Si E_x^b ≈ 15 meV, WP5) and ΔZPE is ~0.1 eV per point defect [E, B1]; all three are kept in (E1).
A ledger that drops them is accurate to O(E_x^b/E_g) and O(ΔZPE/E_st,1).
*Names.* The brief's E_dep is ω; E_stored(t) ≡ E_st(t) + E_trap(t) + E_es^{trap}(t) (the image/space-charge energy of trapped charge); E_sensor-loss ≡ E_sl.

### 1.2 Statement and proof
  ω + 𝒲_bias(t) = E_hot + E_pairs + E_x + E_trap + E_es + E_st(t) + ℋ_ph + E_esc + E_sig + E_sl    (all t ≥ 0, event by event).                        (E1)

  dE_r/dt = Σ_{r′}J_{r′→r}, J antisymmetric;   d𝒲_bias/dt = Σ_k V_k dQ_k/dt = (NTL power into ℋ_ph) + dE_es/dt.                                    (E2)

**Theorem E-0 [D given (H-E1)–(H-E4), WP5 (B1)].** (E1) is exact. *Proof.* H_tot is conserved apart from the external work. The only external work is
𝒲_bias = Σ_kV_kΔQ_k. The electrostatic part is an exact theorem (C2a–b): for charges between electrodes at fixed potentials, the field energy equals the
Green's-function pair energy, self-image terms included, plus V²C/2. This is checked against an independent Gauss-law solution, so E_es is the complete
long-range Coulomb reservoir. Moving a charge quasi-statically, the battery work equals ΔE_es plus the work done on the charge, which a carrier at
terminal velocity dissipates as NTL phonons. The remaining processes (§1.3) are short-range quantum transitions that conserve energy vertex by vertex
(WP5 §1.2 for t < t_pr; §1.3 for t > t_pr). Summing (E2) from E_hot(0⁺) + ℋ_ph(0⁺) = ω gives (E1). ∎ What is not trivial is the completeness of the reservoir
list. That is the content of (H-E1), and C2 tests it in the electrostatic sector.
*At t_pr* (no drift, no sensor absorption): ω = N_eh E_g + E_pairs^{unp} + E_x + E_trap^{pr} + E_es + ℋ_pr + E_st + E_esc. Here N_eh is the number of **fully
free pairs**, E_pairs^{unp} is the band energy of free carriers whose partner was captured (μ_F-referenced, A§1.3, B4), and E_trap^{pr} + E_pairs^{unp} is the
μ-independent combination. **WP5 (W4) is the case with no capture and no exciton before t_pr** (E_pairs^{unp} = E_trap^{pr} = E_x = 0).
*Mean ledger from the response.* ⟨X(t)⟩(q,ω) = Σ_Λ w_Λ⟨X(t)⟩_Λ with w_Λ = tr[𝔇ᵀS(q,ω;Λ)]/tr[𝔇ᵀS(q,ω)] (WP0 (7.3)), and
⟨X⟩_Λ = Σ_𝐍∫d(marks) P_casc(𝐍, marks|Λ)⟨X(t)|𝐍, marks⟩_det.                                                                                   (E1′)

### 1.3 Process ledger (energies relative to μ_F; ℰ_b the bias field)
| Process | From → to | Time scale | Stage |
|---|---|---|---|
| relaxation to band edges | E_hot → E_pairs (E_g per pair) + ℋ_ph | ≤ t_pr | WP5 (W1)–(W3) |
| exciton / EHD formation; exciton recombination | E_pairs → E_x + ℋ_ph (E_x^b); E_pairs + E_x → ℋ_ph or E_esc (E_g − E_x^b) | ns–μs | §2 |
| capture on level j (deep: multiphonon; shallow Coulombic: cascade capture) | E_pairs → E_trap + ℋ_ph (E^tr) | ns–ms | §2 (WP5 if < t_pr) |
| emission (athermal at mK) / recombination at a trap | reverse of capture / E_trap + E_pairs → ℋ_ph or E_esc (E_g − E^tr) | frozen–s | §2 |
| drift / separation | 𝒲_bias → ℋ_ph (NTL) + E_es | μs | §2 (E2) |
| collection at a contact | E_pairs → ℋ_ph (contact) (E_c − μ_F or μ_F − E_v) | μs | §2 |
| lattice release along a path; carrier- or phonon-stimulated defect reaction | E_st → ℋ_ph (ε_path, FC spectrum WP7-T (4.4)) or E_esc / E_sig; E_trap/E_pairs → ΔE_st (either sign) | 𝒦^{rel}; stimulated | WP7-T (5.2); §1.5 |
| TLS resonant absorption; phonon into sensor / escape | ℋ_ph → E_st; ℋ_ph → E_sig + E_sl / E_esc | Γ₁⁻¹; μs–ms | WP7-T §2; detector |

### 1.4 Two-stage factorisation [D given (H-E4), (H-E6)]
Markov at t_pr is exact for the full microstate (A§2.1, B5). Write the t_pr state as additive deposits 𝐍 = (N_eh, ℋ_pr, E_st, N_FP, E_esc, N_trap^{pr},
E_trap^{pr}, E_x, E_pairs^{unp}) and **marks** 𝔪 = (𝔠, r_ev, dℋ_pr/dω_ph(r), cloud geometry), where 𝔠 ≡ WP7-T's configuration class c, renamed because c is a
band subscript and 𝒦_c a channel (A§7, D4). Additive deposits enter e^{ϑ·𝐍} of (W3); marks ride along as a marked law P_casc(𝐍, 𝔪 | Λ).
(H-E6) *Sufficiency:* 𝒫_det depends on the t_pr microstate only through (𝐍, 𝔪). This holds to the extent that the trapping of carrier i on track defects
depends on the cloud and the track only through the cloud geometry and the defect density profile. It is an approximation, and G-E9 records the
residual (B5).

  P(𝐌, t | Λ) = Σ_𝐍∫d𝔪 P_casc(𝐍, 𝔪 | Λ) 𝒫_det(𝐌, t | 𝐍, 𝔪);   dℛ/d𝐌 = (ρ_χ/m_χρ_T)∫d³v f_χ∫d³q/(2π)³ Σ_Λ tr[𝔇ᵀS(q,ω_q;Λ)]P(𝐌,t|Λ) + dℛ_bg/d𝐌.     (E3)–(E4)

Each process belongs to one stage by its time, so nothing is counted twice. The stages are coupled through 𝔪, which is how yield and response share
trapping. The phonon spectrum dℋ_pr/dω_ph(r) is needed because ϵ_coll and E_sl depend on it (IF-E7).

### 1.5 Consistency conditions
**Theorem E-1 (E_d once) [D] (A-3, B-4 STAND).** E_d is absent from (E1). It enters only as the median of P_FP(E_R, r̂_R) (W10), i.e. through the law of
(E_st, N_FP, 𝔠). E_d − E_st (step model) is MD heat inside ℋ_pr. WP7-T fixes the profile

  E_st(t) = E_st − ∫_{t_pr}^{t}dt′∫dE E𝒦^{rel}(E, t′ − t_pr | 𝔠, E_st, T; Φ_ph, n_car),   ∫_0^{t_obs}dt∫dE E𝒦^{rel} = E_st − E_st^{frz}(t_obs) ≡ E_st^{rel},   (E5)–(E6)

with E_st^{frz}(t_obs) the configurational energy still stored at the observation time t_obs, which cures the "on the observation time" versus ∫^∞ mismatch
(A§2.2(i)). 𝒦^{rel} now depends on the local phonon flux Φ_ph (later events, NTL phonons, TLS absorption) and on the carrier density n_car (recombination-
enhanced reactions), so that every ledger process of §1.3 is covered (A§2.2(ii)). For the spontaneous part of WP7-T (5.2), ∫Γe^{−Γt}dt = 1, and (E6) is the
constraint Σ_path𝒫_path ε_path = E_st^{rel}: a condition on WP7-T(-v2)'s path tables (IF-E2). Forbidden: (a) subtracting E_d, or a per-displacement "energy to
defects", from the heat while also adding the release; (b) adding release that falls inside t_win to a heat yield measured with that window; (c) N_FP·E_d as a
stored energy.
**Theorem E-2 (yields act on the electronic share) [D for creation; E for the reaction channel] (A-4, B-5).** Define E_el per event (X-sector ω_e at the
vertex, slow-ion electronic losses of WP5 §3.3, electronic losses of fast secondaries) and E_nuc ≡ ω − E_el. (i) *Creation:* knock-on kinematics forbids
electron-driven Frenkel-pair creation. The maximum transfer 2E(E + 2m_e)/M_κ equals E_d ≈ 20 eV only at E ≈ 0.2 MeV in Si, far above the keV-scale secondaries
of DM recoils, and is 0.78 meV at 10 eV (WP5v3-C11). So at t_pr

  E_el = N_eh E_g + E_pairs^{unp} + E_x + ℋ_el + E_esc^{el} + E_trap^{pr} + E_es,   E_nuc = ℋ_nuc + E_st + E_esc^{nuc} (E_esc^{nuc} = 0 by t_pr).              (E7)

(ii) *Reactions:* recombination-enhanced defect reactions and ionization-driven athermal interstitial migration in Si [UNVERIFIED, from the referees' and
standard references: Kimerling; Watkins; Bourgoin–Corbett] move electronic energy (E_g − E^tr per recombination at a defect) into ΔE_st, mostly annealing
close pairs. They are a **post-prompt cross-channel** inside 𝒦^{rel}(…; n_car) (gap G-E7). If such a reaction occurred before t_pr, (E7) would need an
E_el → E_st transfer term. Lindhard's ν = E_nuc (WP5 §6.1). A yield model maps the electronic seed spectrum dP/dω_e to P(N_eh). It must not be applied to
E_R and then corrected by E_st, and E_st must not be booked in E_el (the **secondary**-U complement of 2209.04503, WP5 §6.1(5)). Ionic targets break (i) (G-E1).
**Theorem E-3 (trapped charge once) [D] (A-5, B-6).** (i) Doubly trapped pair: deficit E_g − E^tr_e − E^tr_h. Singly trapped hole with the electron
collected: μ_F − E_v − E^tr_h + E_es^{img}. Singly trapped electron: E_c − E^tr_e − μ_F + E_es^{img}. WP5 (W11)'s ⟨N_trap⟩E_g is right for neither case. Only
in the doubly trapped, shallow-level limit is it exact. (ii) A trap removes the carrier's remaining Ramo fraction from N^meas and the same fraction from
𝒲_bias (E11). (iii) P_casc counts free pairs plus captures before t_pr; later captures belong to 𝒫_det; track traps couple the stages through 𝔪.

### 1.6 Windows, thresholds and the windowed heat quenching [D]
A detector integrates over [0, t_win] and has threshold E_thr^det. Each quantum of E_st^{rel} is in-pulse, a delayed event, sub-threshold continuum, or frozen
(at t_obs). Released fractions P_rel(t_win): single path 1 − e^{−Γt_win}. Broad λ: [ln(Γ_max t_win) + γ_E]/ln(Γ_max/Γ_min) in the intermediate range (C3a,b).
1D (crowdion) correlated recombination: erfc(d/√(4D_diff t_win)) → 1 (C3c). **3D: (r_c/d)erfc((d − r_c)/√(4D_diff t_win)) → r_c/d < 1**, with the remainder
going to the bimolecular or sink channel (C3d,e; A-12, B10). Every measured heat quantity is an NR/ER ratio at equal ω (2007.14289 [FT] defines the heat
quenching factor as "the ratio of heat signals produced by nuclear and electron recoils of the same energy"). With deficits D ≡ E_stored(t_win) + E_esc + E_sl:

  Y_H(t_win) = (ω − D_NR)/(ω − D_ER) = 1 − [⟨E_st^{frz}⟩ + ⟨E_st^{rel}⟩(1 − P_rel) + ⟨ΔE_trap⟩ + ⟨ΔE_es^{trap}⟩ + ⟨ΔE_esc⟩ + ⟨ΔE_sl⟩]/ω + O(D_ER ΔD/ω²)   (zero field),   (E8)

with Δ = NR − ER, ER being free of E_st. The linear form is first order: the ratio minus the linear form is −ΔD·D_ER/ω² (C9a). ΔE_trap can be negative:
at equal ω an ER has more pairs, so with equal trapped fractions ΔE_trap < 0 (C9b; A-9, B-G). E_trap uses μ_F (Theorem E-3). *NTL mode:* the ER reference is
ω(1 + g), g = eV_b/ε, so the NR/ER phonon ratio is (ω − D_NR + gyω)/(ω − D_ER + gω), equal to (1 + yg)/(1 + g) at D = 0 (C9c). v1's "+eV_b⟨ΔN^meas⟩/E_R"
was mis-normalised. Monotonicity: Y_H rises with t_win **in the E_st^{rel} term only**. E_trap(t_win), E_esc(t_win) and E_sl(t_win) also depend on t_win.

---
## 2. Charge: trapping, release, measured charge

### 2.1 Trap kinetics at mK [D for structure; E for numbers]
With carrier speed u_car (the actual, in general hot, drift-plus-thermal speed; v_th is meaningless at mK, A§2.4) and density per local volume,

  dn^e_j/dt = σ^e_j(u_car) u_car n_e^f(𝓃_j − n^e_j) − Γ^{em}_{e,j}n^e_j − σ^{rec}_j u_car n_h^f n^e_j   (and e ↔ h),                                          (E9)

coupled to carrier continuity in ℰ_b, and to Poisson with trapped charge (this is E_es). Capture mechanisms: deep levels by nonradiative multiphonon emission
(WP4-v3 §6 [6.3]). **Shallow hydrogenic/Coulombic centres, which dominate detector-grade Si/Ge, by cascade (Lax/Abakumov-type) capture through
sequential phonon emission**, with σ strongly speed-dependent [UNVERIFIED as to the numerical forms] (A-16, B-F). **Emission at mK:** thermal ∝ e^{−E^tr/T},
exponent 1.0×10⁴ for 45 meV at 50 mK (C10d), frozen. Field emission (triangular barrier, exponent (4/3)√(2m*)E^{tr 3/2}/(eℰ_b), C10a) needs
ℰ_b ≈ **1.2×10⁴ V/cm** for exponent 30 (m* = 0.3m_e [E]; C10b). v1's 1.2×10⁶ V/cm came from an ħc error of ×100 (A-10, B8). The margin over detector fields
(1–100 V/cm) is therefore 10²–10⁴. For charged centres the triangular barrier is the wrong model; the Poole–Frenkel lowering, √(e³ℰ_b/πε), is 2.2 meV at
100 V/cm in Si (C10c), ≪ 45 meV. Athermal emission (phonons from later events and NTL phonons, impact ionisation of neutral shallow centres [UNVERIFIED
thresholds], IR flashing, 1803.02903 [FT]: "By careful neutralization of ionized trapping sites … with regular exposure to infrared LEDs ('flashing')") and
defect-borne traps (Γ^{em} ⊃ Γ_path) remain. **Consequence:** at mK n_j(t) is a history variable, and delayed charge ℛ_q^{del} = Σn_jΓ^{em}_j is correlated with prior
large depositions.

### 2.2 Induced charge and bias work [D]
Ramo–Shockley with weighting potential U_R. For one pair, 𝔵 ∈ [0,1] is the induced charge in units of e. Planar detector, uniform field, exponential
trapping, no emission, diffusion or space charge:

  ⟨𝔵|z⟩ = (ℓ^tr_e/d)(1 − e^{−(d−z)/ℓ^tr_e}) + (ℓ^tr_h/d)(1 − e^{−z/ℓ^tr_h})   (Hecht; order-statistics and Ramo-current routes agree, C4a).                    (E10)

  𝒲_bias = Σ_k V_k ΔQ_k = eV_bN^meas (two electrodes);   NTL heat = 𝒲_bias − ΔE_es.                                                                       (E11)

The Ramo charge on an electrode is exact with any other static charge present (C2c), so 𝒲_bias = eV_bN^meas survives space charge. The dissipated NTL heat is
what changes, by −ΔE_es (C2d). Over full collection of a pair born neutral, ΔE_es = 0. For a coax geometry the work also equals V_b times the Ramo charge (C5).
For ZIP/iZIP detectors (charge electrodes interleaved with grounded phonon electrodes) 𝒲_bias = Σ_kV_kΔQ_k with each electrode's own U_R, and N^meas of one
readout channel is not 𝒲_bias/eV_b (A-6).

### 2.3 The measured-charge observable [D under (H-E5)]
(H-E5) Given (r_ev, 𝔪), carriers drift independently after t_pr (the WP5 (B2) caveat persists in NR tracks, G-E5). Then N^meas = Σ_{i≤N_eh}𝔵_i and

  E[e^{sN^meas}|Λ, 𝔪, t] = Σ_N P_casc(N|Λ, 𝔪)φ_t(s|r_ev)^N;   F_meas^{obs} = [F_eh⟨m²⟩_r + ⟨Var(𝔵|r)⟩_r]/⟨𝔵⟩ + ⟨N_eh⟩Var_r(⟨𝔵|r⟩)/⟨𝔵⟩,   m(r) ≡ ⟨𝔵|r⟩.     (E12)

C6a checks this against an exact two-position mixture. Conditional on r (one position) it reduces to ⟨𝔵⟩F_eh + Var𝔵/⟨𝔵⟩. The position term grows with
N_eh: non-Fano scaling for depth-distributed events (calibration lines, DM) (A-7, B7). Charge-collection readout (CCD), single position:
F_meas = ϵ_detF_eh + 1 − ϵ_det (C6c, = WP5v3-C2a). Track self-trapping correlates 𝔵 with E_st.
*Data.* (a) 1803.02903 [FT], Si ZIP at ~4 V/cm: "the ionization collection efficiency for CDMS II silicon detectors operated at ∼4 V/cm is consistent
with 100% for nuclear recoils below 20 keV and gradually decreases for larger energies to ∼75% at 100 keV". In URF terms ⟨𝔵⟩_NR/⟨𝔵⟩_ER = 1 below 20 keV,
falling to 0.75 at 100 keV: a direct constraint on θ_tr for NR tracks at that field. (b) 2405.10405 [FT, via v1]: shaping 2–18 µs changes the γ+NR combined
energy by < 2 eV for 6 of 7 filters, at 77 K. This bounds the NR-minus-ER window dependence there [E]. It does not bound absolute or permanent trapping, nor
mK behaviour, so it is no longer used as a θ_tr prior (A§3.4, B-C4, D3).

---
## 3. The observable map

### 3.1 Prompt heat and two-channel reconstruction [D]
Zero field: the heat signal is (E8) × ω. It is blind to N_eh, since every recombined pair returns E_g, and it sees E_stored, escapes and sensor-loss
differences. NTL mode adds 𝒲_bias − ΔE_es. **Two-channel reconstruction with ER calibration** (1803.02903 Eq. (1) [FT], E_φ = E_R + E_QeV_b/ε; phonon scale
set on "bulk electron recoils, which should have unity ionization yield"; the source then fits "an overall phonon collection efficiency for nuclear recoils
η^φ_NR = 95.2^{+0.9}_{−0.7}% relative to electron recoils of the same deposited energy" [FT]). Exact algebra (C7a) with E_Q calibrated to ω on ERs and
y ≡ E_Q/ω for the NR:

  η^φ_NR ≡ E_R^rec/ω = 1 − d_NR + κ d_ER + O(d²),   κ = (1 + yg)/(1 + g),   d ≡ D/ω,   D = E_stored(t_win) + E_esc + E_sl,                                 (E13)

and y^meas = [⟨𝔵⟩_NR⟨N_eh⟩_NR/(⟨𝔵⟩_ER⟨N_eh⟩_ER)]/η^φ_NR (per unit ω). η^φ_NR does not depend on ⟨𝔵⟩ at d = 0 (C7b). Trapping enters only through E_trap ∈ D.
**v1's reading "1803.02903 implies Y_H = 1" is REFUTED (B-C2) and withdrawn.** The paper measures η^φ_NR. The source attributes the deviation to collection:
"the phonon collection efficiency … for nuclear and electron recoils of a given energy need not be identical" [FT]. In the URF it is the combination
d_NR − κd_ER. With g ≈ 1.05 (4 V across ≈ 1 cm [E, thickness UNVERIFIED]) and y ≈ 0.3 [E], κ ≈ 0.64 and **d_NR − 0.64 d_ER = 0.048 (+0.007/−0.009)** (C7c).

### 3.2 Data constraints on E_st [D for the algebra; E for inputs]
| Data | Measured combination (URF) | Constraint if everything is attributed to E_st (upper bound) |
|---|---|---|
| 1803.02903, Si ZIP, ~4 V/cm, η^φ_NR = 95.2^{+0.9}_{−0.7}% at the ²⁵²Cf-resonance energies (tens of keV) | d_NR − κd_ER = ⟨E_st + ΔE_trap + ΔE_es^{trap} + ΔE_esc + ΔE_sl⟩/ω (to O(d²)) | ⟨E_st⟩/E_R ≤ 0.055 (95%); with NRT, p_surv E_st,1/E_d ≤ 0.18 (E_dam/E_R = 0.65 [E]) |
| 1805.09942, Ge iZIP at ~50 mK, ²⁰⁶Pb surface recoils near 103 keV: f_DF = 1 − (1 − f)/(1 − f_sur) = 6.08 ± 0.18% (surface-ER-corrected) | the same NR/ER deficit at the surface (phonon − Luke, iZIP), including surface ΔE_esc and the polarity-dependent charge collection the paper notes [FT] | ⟨E_st⟩/E_R ≤ 0.065; p_surv E_st,1/E_d ≤ 0.19 (E_dam/E_R = 0.8 [E]) |
The bounds assume the non-E_st terms are ≥ 0; a negative ΔE_trap (§1.6) would loosen them. The two papers attribute similar ~5–6% deficits to opposite causes: collection (Si) and defects (Ge) (B-C6). The URF shows both measure the same combination
and cannot separate E_st from ΔE_sl or ΔE_trap without IF-E7 (G-E4). Both bounds imply p_surv ≲ 0.4 (Si, E_st,1/E_d = 9/20) and ≲ 0.6 (Ge, 6/19.7) (C8b,c),
so v1's "up to ~13% at 1 keV with p_surv = 1" is excluded as a central value (A-L37). 1805.09942 [FT] also reports that its two detectors "differ by 2.06
standard deviations" and that they "were biased with opposite polarities" (charge carriers of opposite sign collected): a hint of ΔE_trap at the surface.

### 3.3 Delayed events and the low-energy-excess model [D for structure; E for numbers; C where stated]
  dℛ_del/dE dt = Σ_𝔠∫dt′𝔰_𝔠(t′)𝒦^{rel}(E, t − t′ | 𝔠, T; Φ_ph, n_car) ⊗ 𝒯_𝔠 + ℛ_q^{del} ⊗ 𝒯_q,                                                                  (E14)

with sources (i) event-seeded (p_st of WP7-T (5.1)); (ii) cooldown-seeded (populations frozen in at T₁); (iii) stress-seeded; (iv) trapped charge. Time laws:
1/t (broad λ, (e^{−Γ_min t} − e^{−Γ_max t})/t), t^{−3/2} (correlated recombination; 1D eventual probability 1, 3D r_c/d), exponential, (1 + t/t₀)⁻².
**One visibility criterion [D]:** a release is an event iff ϵ_coll ε ≥ E_thr^det (absorber) or ε ≥ E_thr^det (film). Comparator, for the Si/Ge case: the Si CPD of
2007.14289, σ_E = 3.86 eV [FT]. Its threshold of ≈ 4.2σ ≈ 16 eV is the referee's reading [E]. (A§4.3, B9.)
- **(a) TLS give power.** WP7-T (4.5) is **per unit λ**. The total stored excess is (π²/12)P̄_STMVT₁² × Δλ with Δλ = ½ln(Γ_max/Γ_min) ≈ 14. For a 100 nm × 1 cm²
  a-SiO2-like film at T₁ = 1 K that is ≈ 1.4×10⁷ eV, and integrating Q̇ reproduces it (C12a). Power ≈ 0.6 eV/s at 10 d. Quanta are ≲ 3T₁ ≈ 3×10⁻⁴ eV, so a 10 eV
  event needs ≥ 10⁴ coherent quanta (C12b): sub-threshold power and QP poisoning, never events, unless collective (WP7-T G-T4, [C]).
- **(b) Single Frenkel-pair releases** carry ε ≤ E_st,1 ≈ 7–9 eV [UNVERIFIED]. They are visible iff E_thr^det ≤ ϵ_coll E_st,1 ≈ 2.7 eV (ϵ_coll = 0.3 [E]), so
  invisible at 16 eV (C11a). This is a single threshold: v1's "≲ 1 eV" is withdrawn (B9).
- **(b′) Event-seeded amorphous-pocket recrystallisation** (WP5 §3.2 R_final, L22(c)) releases ~N_a × (0.1–0.2 eV) [E] in one cooperative transition. It is
  visible at 16 eV for N_a ≳ 270 atoms (C11b). The bound "particle-seeded releases ≤ E_st,1" therefore does **not** hold for keV recoils with pockets. These are
  "collective but event-seeded" (gap G-E8). Their rate is ≤ ℛ_NR(E_R ≳ keV) × (pockets per recoil): negligible underground, testable after neutron calibration.
- **(c) 10–100 eV delayed events** need collective release from reservoirs (ii)–(iii) or (b′). The data are mixed and are reported in full. For a stress
  origin: 2208.02790 [FT], a glued crystal shows "more than two orders of magnitude larger" rates than a suspended one, with "a time constant of 6–10 d" in the
  "3–38 and 30–85 eV" bins. Against: 2202.05097 [FT, EDELWEISS/Ricochet] tested holders "with adjustable stress on the crystal … However, none of these tests
  have shown a significant effect on the magnitude and shape of this low-energy excess"; its leading hypothesis is "the cracking of the epoxy used to glue the
  Ge-NTD on the crystal" (also "Sudden increases were observed at times after warming-up the detectors above 10 K"). RED30: "most of the events observed above
  15 eV_ee (400 eV in total energy) are not associated with the creation of electron-hole pairs", i.e. not class (iv). Time law: 2208.02790 [FT] states that "In
  the lowest-energy bin in the HS calorimeter, a single exponential does not sufficiently describe the time-dependent rate (χ²/(dof) = 4192/68)" and that "A
  sum of exponentials or a power law … may be a more appropriate fit". **v1's "does not separate the two" misstated this and is withdrawn** (A§4.4, B-C5). The
  rejection of a single exponential is consistent with the broad-λ form (E14)(1/t with cutoffs), but it does not establish it. The reading as collective release
  stays [C] (G-E2).
- **(d) Delayed charge** is ionizing, quantised under NTL gain, and history-correlated (§2.1).

### 3.4 Which detector types see which terms [D]
| Type | ℋ_pr | E_g of pairs | N^meas | E_st deficit | E_trap (μ_F) | E_es | lattice/stress releases | delayed charge | film relaxation |
|---|---|---|---|---|---|---|---|---|---|
| zero-field phonon calorimeter (Si/Ge CPD, CRESST, KID) | yes | recombination heat (E_g − E_x^b + E_x^b) | no | via (E8) | ΔE_trap (doubly trapped dominant at zero field) | small | events iff ϵε ≥ E_thr | no | direct |
| NTL / HV phonon | yes | yes | ×eV_b (E11) | yes | ΔE_trap incl. singly trapped (μ_F) + lost NTL | 𝒲 − ΔE_es | without NTL gain | NTL-quantised | yes |
| heat + ionization (CDMS II, EDELWEISS) | yes | yes | yes | in η^φ_NR (E13) | in η^φ_NR and y^meas | yes | heat only | charge | yes |
| charge only (HPGe, skipper CCD) | no | no | yes (E12) | no | through 𝔵 | through field | only radiative or > E_g | single carriers | no |
| scintillating (light channel) | via heat | luminescence in E_sig/E_esc | no | heat channel | radiative trap recombination = afterglow | — | heat | afterglow | yes |
| SC absorber / qubit | yes | N_qpΔ_BCS ((W13), absorber case) | no | as calorimeter | — | — | yes | — | dominant (QP poisoning) |

---
## 4. Literature limits and implicit defect assumptions [D for limits]
**L20 Lindhard / modified Lindhard.** Sources: 2001.06503 Eqs. (3)–(7), 2209.04503 Eq. (2) [FT, CONFIRMED in WP5 §6.1]; 2001.06503 [FT]: "when atomic binding
energies can be safely neglected"; with constant binding "the quenching factor … features a cut-off at an energy equal to twice the assumed binding energy";
Table I "Dislocation 36" (Si) and "23" (Ge) eV. *Implicit:* U = 0 ⇒ E_st = 0, ν = ℋ_nuc. The QF is blind to the ℋ_nuc/E_st split, so it implies nothing about heat
beyond Y_H = 1. Charge E_el/ε_eh^γ with 𝔵 = 1 and E_trap = 0. *Limit:* t_pr, those truncations, BCA (WP5 truncation 0). *Modified:* each **secondary**
displacement stores U permanently (𝒦^{rel} = 0), and by complement that secondary U is booked electronic; the primary's u is in ν̄ (WP5 §6.1(5); B-C8). The 2u
cut-off makes one number act as both E_d (threshold) and E_st (energy); the URF separates them.
**L21 R&K** (2004.10709, WP5 §6.2 [FT, CONFIRMED]; App. A misprint CONFIRMED by A and B). *Implicit:* ER (E_st = 0 for creation), measured = created pairs
(𝔵 = 1). Validation data from a CCD (thinning ϵ_det). *Limit:* (E1) with E_stored = E_esc = 0, ϵ_det = 1.
**L22 Kinchin–Pease / NRT / TRIM.** Kinchin–Pease N_FP = E_dam/2E_d. **NRT adds the 0.8** (Norgett–Robinson–Torrens; A§5); both not on arXiv, both cited in
1805.09942. *Implicit:* p_surv = 1, 𝒦^{rel} ≡ 0, and a stored energy E_st,1 per displacement. Under NRT, f_DF ≈ p_surv·0.4(E_dam/E_R)E_st,1/E_d decreases with
E_d at fixed E_st,1 (C8a). *TRIM's internal per-displacement energy is not stated in 1805.09942*, which notes that its "systematic error does not include
modeling imperfections in Geant4 and TRIM" [FT]. So v1's statement that TRIM fixes E_st,1 independently of E_d is an **inference, UNRESOLVED** (A rubric (c)),
and E_d extracted from f_DF inherits it. *Limit:* (E5) with 𝒦^{rel} = 0, E_st = N_FPE_st,1. In a dense 103 keV Pb cascade, NRT and p_surv are ill-defined
[E, A-L36]: there the URF uses ⟨E_st⟩ from MD directly. The measured f_DF is the (E8)/(E13)-type NR/ER deficit at the surface (§3.2), not E_st alone.
**Measured quenching data.** (a) *Two-channel, Si* (1803.02903 [FT]): measures η^φ_NR = 95.2% and ⟨𝔵⟩_NR/⟨𝔵⟩_ER (1 → 0.75 between 20 and 100 keV). *Implicit:*
none hidden for the heat channel, since it fits the deficit. The ionization yield assumes the flashing-neutralised trap state. *Limit:* (E13) and y^meas of
§3.1. (b) *Charge only, Ge 254 eV_nr* (2405.10405 [FT, via v1]: yield 64 ± 8 eV_ee, "greater than the 14% predicted by the Lindhard model"; calibration on γ/X
lines). *Implicit:* the measured QF is (⟨𝔵⟩_NR/⟨𝔵⟩_ER)·QF_created at 77 K in µs windows (A§3.2). (c) *Heat quenching assumed unity* (2007.14289 [FT]): "has been
assumed to be unity for this work. Though measurements of the heat quenching factor have not been made for Si, similar work has been undertaken for Ge, where
the heat quenching factor was shown to be very close to unity". *Implicit:* E_stored = ΔE_trap = ΔE_esc = ΔE_sl = 0 in t_win. *Limit:* (E8) with those zero.
1803.02903's η^φ_NR = 0.952, an Si measurement of the related two-channel ratio, now constrains it at 4.8% (B-E).

---
## 5. Amendment to WP5-v3 (exact text; WP5-v3 not edited)
**A-1. §1.2 (W3) and (W4).** In (W3), add to the cascade types "trapped on level j" and "bound exciton", with kernels 𝒦_cap (capture, from WP7-E (E9) for
t < t_pr; cascade capture for shallow Coulombic levels, multiphonon for deep ones) and 𝒦_x (exciton formation). Their absorbing-state deposits are
δ𝐍 = (N_trap^{pr} += 1, E_trap^{pr} += E_c − E^tr − μ_F or μ_F − E_v − E^tr) and (E_x −= E_x^b). After (W4) insert: "(W4) holds when no carrier is captured and no
exciton forms before t_pr. In general ω = N_eh E_g + E_pairs^{unp} + E_x + E_trap^{pr} + E_es + ℋ + E_st + E_esc, with N_eh the number of fully free pairs,
energies referenced to the contact Fermi level μ_F, and E_pairs^{unp} + E_trap^{pr} μ-independent (WP7-E-v2 (E1), §1.2). Drift, post-prompt trapping, emission,
recombination, lattice release and sensor absorption are post-prompt processes outside P_casc."
**A-2. §1.2 definition of 𝐍:** "𝐍 = (N_eh, ℋ, E_st, N_FP, E_esc, N_trap^{pr}, E_trap^{pr}, E_x, E_pairs^{unp}) (additive). The class 𝔠, the event position r_ev,
the t_pr phonon spectrum dℋ/dω_ph(r) and the carrier-cloud geometry are marks of a marked law P_casc(𝐍, 𝔪|Λ), not components of ϑ·𝐍 (WP7-E-v2 §1.4, (H-E6))."
**A-3. §3.2 "Stored energy", replace the definition by:** "E_st = [E^ad_0(R_final) − E^ad_0(R_I(0))] + ΔZPE, the difference of vibrational ground-state energies
of the final basin and 𝔅₀, at t_pr", **and append:** "Its evolution is E_st(t) = E_st − ∫E𝒦^{rel}, with ∫_0^{t_obs}∫E𝒦^{rel} = E_st − E_st^{frz}(t_obs)
(WP7-E-v2 (E5)–(E6)). E_d enters only through P_FP (W10); the ledger never contains E_d."
**A-4. §3.4, replace (W11) and the sentence after it by:** "Y_H(t_win) ≡ (NR heat signal)/(ER heat signal) at equal deposited energy
= (ω − D_NR)/(ω − D_ER), D ≡ E_st(t_win) + E_trap(t_win) + E_es^{trap} + E_esc + E_sl; to first order Y_H = 1 − [⟨E_st^{frz}⟩ + ⟨E_st^{rel}⟩(1 − P_rel(t_win))
+ ⟨ΔE_trap⟩ + ⟨ΔE_es^{trap}⟩ + ⟨ΔE_esc⟩ + ⟨ΔE_sl⟩]/ω, Δ = NR − ER (W11). E_trap is referenced to μ_F: a doubly trapped pair contributes E_g − E^tr_e − E^tr_h, a
singly trapped carrier μ_F − E_v − E^tr_h or E_c − E^tr_e − μ_F; ΔE_trap may be negative. NTL mode: the ratio is (ω − D_NR + gyω)/(ω − D_ER + gω), g = eV_b/ε.
Unit heat quenching (2007.14289) is the truncation D_NR = D_ER; the Si two-channel measurement (1803.02903) gives η^φ_NR = 0.952 (WP7-E-v2 (E13))."
**A-5. §3.3 "Charge from the electronic deposit", append:** "The measured charge is N^meas = Σ_i𝔵_i (WP7-E-v2 (E12)). Comparisons with QF data use
⟨𝔵⟩_NR/⟨𝔵⟩_ER, because QFs are calibrated on ERs. Trapping **after t_pr**, including on the recoil's own defects, is a detector-stage effect; captures before t_pr
are in P_casc (A-1)."
**A-6. §4, (W12):** "⊗ (detector response)" → "⊗ 𝒯_𝔠(E → E^meas), an event iff ϵ_coll ε ≥ E_thr^det (WP7-E-v2 (E14))". Append to "Time dependence": "Single
Frenkel-pair releases (≤ E_st,1) and TLS quanta (≲ few T₁) are sub-threshold for E_thr^det > 3 eV; amorphous-pocket recrystallisation is collective and
event-seeded and can exceed 10 eV. Below T_× use WP7-T (4.2)–(4.3)."
**A-7. §5, after (W13), insert:** "(i) Superconducting absorber (this section): E_sub and E_excess are absorber phonon energy (ℋ_ph) and E_esc is E_esc of
WP7-E-v2 (E1). (ii) The same bookkeeping applied to a sensor film, with ω replaced by the phonon energy entering the film, gives E_sig = Δ_BCSN_qp and
E_sl = E_sub + E_excess + E_esc(film)."
**A-8. §6.1 chain step 4, append:** "(F) Implicit defect assumptions: Lindhard U = 0 ⇒ E_st = 0; 𝔵 = 1, E_trap = 0; in 2209.04503 the U spent in **secondary**
displacements is frozen stored energy booked electronic by complement, while the primary's u is in ν̄."
**A-9. §6.3 chain step 4, after the f_DF formula, append:** "N_FP^{NRT} carries the NRT factor 0.8 (Kinchin–Pease: E_dam/2E_d). The measured f_DF (1805.09942)
is a phonon-minus-Luke NR/ER deficit at the surface. It contains E_st, ΔE_trap (polarity-dependent collection), surface ΔE_esc and ΔE_sl (WP7-E-v2 §3.2), and
fixes p_surv E_st,1/E_d only if those vanish. Whether TRIM's stored energy per displacement is E_d-independent is not stated in the source (UNRESOLVED)."
**A-10. §6.4 "Validity", replace** "carriers to thermalise at the band edges with no trapping before counting, no photon escape, and E_st = 0 (ER)" **by**
"carriers to thermalise at the band edges with no capture and no exciton formation before t_pr (E_trap^{pr} = E_x = 0; otherwise (W14) uses
ℋ + E_trap^{pr} − E_x in place of ℋ), no photon escape, and E_st = 0 (ER). (W14) concerns created pairs. The reported Fano factor is
F_meas^{obs} = [F_eh⟨m²⟩ + ⟨Var𝔵⟩]/⟨𝔵⟩ + ⟨N_eh⟩Var_r⟨𝔵|r⟩/⟨𝔵⟩ (WP7-E-v2 (E12)), which reduces to ϵ_detF_eh + 1 − ϵ_det for single-position charge collection".
**A-11. §8:** replace the θ_esc row by "θ_esc | escape only | M | per detector" and add "θ_tr^{pr} | prompt capture (N_trap^{pr}, E_trap^{pr}) | T on the two-point
(captured/free) measure | per material and field", plus the WP7-E-v2 §6 rows.
**A-12 (missing site 1). §1.2 (B3), replace** "An NTL drift field adds a deterministic drift term." **by** "A drift field acts after t_pr (drift times are μs).
It enters the detector stage (WP7-E-v2 (E2), (E11)), not P_casc."
**A-13 (missing site 2). §6.4 "Leading URF corrections", replace** "then trapping (N_trap) and exciton or luminescence escape via (W4)" **by** "then prompt
capture and excitons via (W4) as amended (A-1), and post-prompt trapping, induced charge and luminescence escape via WP7-E-v2 (E8), (E12)".
**A-14 (missing site 3). §9 R6, replace** "enter (W4) and (W11)" **by** "enter (W4) (prompt capture, excitons), (W11) and WP7-E-v2 (E1), (E8), (E12)".
**A-15 (missing site 4). §14 symbol rows and NOTATION §G row "N_trap":** "N_trap → N_trap^{pr} (captures before t_pr); post-prompt trap populations are
n^{e,h}_j (WP7-E-v2)".
**A-16. (W6):** "P_casc(𝐍|Λ)" → "P(𝐌, t|Λ) of WP7-E-v2 (E3), plus dℛ_bg" (the WP5 copy of WP0 (7.3); A§6).

---
## 6. Uncertainty: nuisances for the new terms (WP6-v3 types; priors stated)
Fractions in [0, 1] use **type T on a two-point measure**: tilting the measure {f, 1 − f} with the normalisation constraint gives
f(θ) = f₀e^{θψ}/(f₀e^{θψ} + 1 − f₀), the logistic (logit-normal for θ ~ 𝒩(0,1)). This is a WP6-v3 (5.1″) object, positive and exact on its constraint (D2).
| θ | Object | Type | Prior | Correlation | Source |
|---|---|---|---|---|---|
| θ_frz | E_st^{rel}/E_st per class | T (two-point) | central from WP7-T λ-classes (boundary 24); ψ = 1 per unit of σ_λ (σ_λ = 2 [E]) | class, T | WP7-T §4.2 |
| θ_λ, θ_γ | Γ_path | M | σ_ln = 2σ_λ (σ_λ = 2 [E]); σ_ln = 2σ_γ/γ (σ_γ/γ = 0.3 [E]) | material | WP7-T §4.6 |
| θ_𝒦 | shape of 𝒦^{rel} at fixed (E6) | T (constraints ∫𝒦 = Σ𝒫, ∫E𝒦 = E_st^{rel}) | 𝒩(0,1) | class | (E6) |
| θ_law | {1/t, t^{−3/2} (1D/3D), exp} | Δ | discrete profiling | class | WP7-T §4.3 |
| θ_st | ⟨E_st⟩/E_R scale (MLIP) | M | central MD; **data envelope**: d_NR − 0.64 d_ER = 0.048 (Si), f_DF = 0.061 (Ge, Pb) as one-sided bounds on ⟨E_st⟩/E_R | material | §3.2 |
| θ_tr^{pr} | prompt capture fraction | T (two-point) | central 0 (no prompt capture) with ψ giving 1% at θ = 1 [E] | material, field | A-11 |
| θ_tr | ℓ^tr_{e,h}, track trap density | M | NR: ⟨𝔵⟩_NR/⟨𝔵⟩_ER = 1 (< 20 keV), 0.75 (100 keV) at 4 V/cm Si (1803.02903) sets central and σ_ln = 0.1; other detectors from their calibration | detector, flash state | §2.3 |
| θ_em | athermal Γ^{em}_j | M | σ_ln = 2.3 (×10) [E, unknown at mK] | detector, history | §2.1 |
| θ_SC | field map / space charge (E_es) | Δ (maps) + M | per exposure state | detector | §2.1 |
| θ_coll | ϵ_coll(NR)/ϵ_coll(ER) and ΔE_sl | M | median 1, σ_ln 0.05: **constrained jointly with θ_st by η^φ_NR** (one combination measured) | material–sensor | §3.1, IF-E7 |
| θ_bg,𝔠 | background reservoir amplitudes | A | log-normal per run, σ_ln 1 | run | §3.3 |
| θ_esc | escape only | M | per detector | detector | WP5 §8 |
*Exact constraints.* η^φ_NR fixes d_NR − κd_ER, a linear combination of θ_st, θ_tr, θ_coll, θ_esc, so these must be profiled together. Two windows in Y_H
separate E_st^{rel}P_rel. (E11) ties θ_tr across charge and NTL. (E6) is exact under type T.

---
## 7. Computation specification
- *Traps.* Deep levels: DFT charge-transition levels and multiphonon capture (WP4-v3 §6 [6.3]). **Shallow Coulombic levels: cascade capture** (sequential
  acoustic-phonon emission in the bound ladder, with speed-dependent σ(u_car) at mK). Track levels per class 𝔠. Cost ~10⁵ CPU-h per material.
- *Drift–trap transport.* Start from **G4CMP** (Geant4 condensed-matter package: anisotropic valley transport, NTL emission, trapping, impact ionisation,
  Ramo readout) and add track traps, history-dependent n_j(t), athermal emission as a parameterised channel, μ_F-referenced E_trap, the E_es field energy,
  and depth-resolved 𝔵 for the (E12) position term. Output the joint table P(N^meas, E_stored(t_win) | E_R, r̂_R, ℰ_b, t_win, T). ≲ 10³ CPU-h per point set.
- *Windowed partition.* With 𝒦^{rel} (WP7-T §5.4), tabulate Y_H(t_win) and η^φ_NR for t_win ∈ {1 μs, 100 μs, 10 ms, 1 s}, and the delayed spectrum for
  E_thr^det ∈ {0.3, 1, 3, 16} eV. Validation: 1803.02903 (η^φ_NR, ⟨𝔵⟩ ratio), 1805.09942 (f_DF). *Sufficiency:* these tables are computable only together with
  the declared gaps G-E4 (ΔE_sl) and G-E6 (athermal emission) (B-F).

## 8. Exact remaining gaps
- **G-E1** Ionic targets: excitation-driven defect creation (E_el → E_st).
- **G-E2** Size law of collective releases; the stress-versus-epoxy question (2208.02790 vs 2202.05097) is open in data.
- **G-E3** (E6) needs WP7-T-v2 path tables built from the same end states as p_st.
- **G-E4** ΔE_sl, Δϵ_coll (WP8-R). Without it the §3.2 constraint cannot separate E_st from collection.
- **G-E5** Track recombination and plasma phase in NR tracks ((H-E5) fails there).
- **G-E6** Athermal emission at mK and space-charge nonlinearity.
- **G-E7** Carrier-driven defect reactions in Si/Ge tracks (rates, sign of ΔE_st).
- **G-E8** Pocket-recrystallisation size distribution (N_a) and rate.
- **G-E9** The residual of (H-E6): carrier–defect distance correlations beyond the cloud geometry and the density profile.

## 9. Checks (code/WP7-E-v2/checks.py, 36/36 PASS)
C1 μ-dependence and the singly trapped energy; C2 planar electrostatics with sheet charges: field energy vs Green's-function sum (completeness of E_es),
battery work = ΔE_es + dissipation, Ramo exact with space charge, NTL heat ≠ 𝒲 with charge present, image energy; C3 broad-λ kernel, 1D erfc, 3D image solution
of the diffusion equation and capture law (r_c/d); C4 Hecht by two routes; C5 coax Ramo; C6 exact position-mixture variance; C7 calibration algebra vs series
for η^φ_NR, data κ; C8 NRT monotonicity and data inversion; C9 ratio vs linear Y_H, sign of ΔE_trap, NTL normalisation; C10 FN exponent, corrected field
(1.19×10⁴ V/cm), Poole–Frenkel, thermal; C11 visibility thresholds (FP, pockets); C12 STM per-λ vs total, power.

---
## R12 closing table (one row per referee item)
Status: **applied**, **applied + dropped** (claim withdrawn), **stands** (no change), **rebutted** (with derivation).
| Item | Verdict | Status | Where |
|---|---|---|---|
| A-1, B-1, B-2, B1–B4 | (E1) reference μ; missing reservoirs; t_pr split; C2 tautological | applied | §1.1 (μ_F, E_x, E_es, ΔZPE), §1.2, Theorem E-3; C1, C2 |
| A-2, B-3, B5 | (E3) sufficiency; marks | applied | §1.4 (H-E6), 𝔪; A-2; G-E9 |
| A-3, B-4 | E_d once: E_st^{frz} vs ∞; stimulated channels | stands + applied (minor) | (E5)–(E6) cut at t_obs; 𝒦^{rel}(…; Φ_ph, n_car) |
| A-4, B-5, B6 | E_st ⊂ E_nuc "exactly" | applied + dropped ("exactly") | Theorem E-2 (creation only; reactions post-prompt; E_esc^{nuc}); G-E7 |
| A-5, B-6 | singly trapped case | applied | Theorem E-3, Table 3.4, A-4; C1c |
| A-6, B-7 | (E11) | stands; multi-electrode form added | §2.2; L34 |
| A-7, B-8, B7 | F_meas position mixture | applied | (E12); A-10; C6 |
| A-8, B-9 | C7 tautology; ER calibration; η^φ_NR omitted | applied | (E13), §3.1–§3.2; C7 |
| A-9 | (E8) ΔE_trap, normalisation, monotonicity | applied | (E8), §1.6; A-4; C9 |
| A-10, B-10, B8 | ħc ×100 | applied (number corrected) | §2.1, §0; C10b; Poole–Frenkel C10c |
| A-11, B-11, B9 | TLS per λ; pockets; selective quotation; threshold | applied + dropped ("does not separate", "≲ 1 eV") | §3.3 (a)–(c); C11, C12 |
| A-12, B10 | 3D correlated recombination | applied | §1.6; C3d,e |
| A-13, B-13, C2, C6 | literature limits: 1803.02903 REFUTED reading; NRT label; f_DF content; 2007.14289 next sentence; QF as ratios | applied + dropped (Y_H = 1 reading) | §3.1, §3.2, §4; L37, L38 |
| A-14, B-14, G | amendment | applied | §5 A-1…A-16 |
| A-15, B-15, D2, D3 | nuisances: prompt trapping, ⟨𝔵⟩ ratio, types, 77 K prior | applied + dropped (77 K prior) | §6 (type T two-point, θ_tr^{pr}, θ_st) |
| A-16, F | computation spec: cascade capture; G4CMP; excitons | applied | §7; §1.3 |
| A rubric (c): 1805.09942 TRIM inference UNRESOLVED | | applied (marked UNRESOLVED) | §4 L22, A-9 |
| A rubric (c): 2004.10709 App. A CONFIRMED; (W11) overstatement CONFIRMED | | stands | §4 L21; Theorem E-3 |
| A§7, D4 | symbol clashes (c, μ, F, D) | applied | 𝔠, μ_F, ℰ_b, D_diff (Symbols) |
| B-C1, C3, C7, C8 | quotes CONFIRMED; C8 "secondary" | stands; A-8 fixed | §4, A-8 |
| B-C4 | 2405.10405 bound misapplied | applied + dropped (as θ_tr prior) | §2.3(b) |
| B-C5 | 2208.02790/2202.05097 selective | applied | §3.3(c) |
| B11 | E_hot(0⁺); WP5 (B3) drift | applied | §1.1; A-12 |
| B-E, A-L33…L38 | LIMITS validity and leading correction; Hecht source | applied | Proposed LIMITS rows |
| B rubric (f), A rubric (f) | no novelty; credit 2208.02790 | applied | header |
No item is rebutted: every verdict was accepted, and two claims were withdrawn outright (the 1803.02903 "Y_H = 1" reading, and "≲ 1 eV").

---
## Symbols introduced/used (against NOTATION v4 + R9 rows)
| Symbol | Meaning | Status |
|---|---|---|
| E_hot, E_pairs, E_pairs^{unp}, E_x, E_trap, E_es, ℋ_ph, ℋ_pr, ℋ_el | reservoirs (§1.1); E_es^{trap}, E_es^{img} its trapped-charge and image parts | **new** |
| E_st(t), ΔZPE, E_st^{frz}(t_obs), E_st^{rel}, E_stored | stored energy incl. zero-point change; frozen and relaxing parts; total stored | **new** (E_st redefined with ΔZPE; flag) |
| φ_EHD | electron–hole-droplet condensation energy per pair | **new** |
| μ_F | contact Fermi level (energy reference) | **new** (bare μ collides with μ_χe, μ*) |
| ℰ_b | bias field | **new** (F is the Fano/form-factor family) |
| D_diff, r_c, d | diffusion constant, capture radius, pair separation | **new** (𝔇 is the DM tensor) |
| 𝔠 | configuration class (= WP7-T c) | **new** (c is a band subscript; 𝒦_c a channel) |
| 𝔪 = (𝔠, r_ev, dℋ_pr/dω_ph(r), cloud geometry) | marks of the cascade law | **new** |
| E_sig, E_sl, 𝒲_bias, V_k, Q_k | sensor signal, sensor loss, bias work, electrode potentials and charges | **new** |
| E^tr_{e,j}, n^{e,h}_j, 𝓃_j, σ^e_j(u_car), σ^{rec}_j, u_car, Γ^{em}_{e,j}, ℓ^tr_{e,h} | trap depth, populations, densities, cross sections, carrier speed, emission rate, trapping length | **new** |
| U_R, 𝔵, m(r) ≡ ⟨𝔵\|r⟩, N^meas, φ_t(s\|r) | weighting potential, induced fraction, its conditional mean, measured charge, single-pair MGF | **new** |
| F_meas^{obs} | position-averaged measured Fano factor | **new** |
| η^φ_NR, g ≡ eV_b/ε, κ, y, d ≡ D/ω, D | NR/ER phonon factor (source symbol 1803.02903), NTL ratio, calibration weight, measured yield, fractional deficit | η^φ_NR, y, ε source (NOTATION §K); g, κ, d **new** |
| f_DF, f, f_sur | source symbols of 1805.09942 | source-only |
| t_win, t_obs, E_thr^det, P_rel, ϵ_coll | window, observation time, threshold, released fraction, phonon collection efficiency | **new** |
| ℛ_q^{del}, ℛ_del, dℛ_bg, 𝔰_𝔠, 𝒯_𝔠, 𝒯_q, 𝐌, 𝒫_det | delayed rates, background, sources, transfers, measured vector, detector propagator | **new** |
| N_trap^{pr}, E_trap^{pr}, θ_frz, θ_λ, θ_γ, θ_𝒦, θ_law, θ_st, θ_tr^{pr}, θ_tr, θ_em, θ_SC, θ_coll, θ_bg,𝔠 | prompt captures; nuisances | **new** (N_trap restricted, A-15) |
| (H-E1)–(H-E6), (E1)–(E14), (E1′), Theorems E-0…E-3, A-1…A-16, IF-E1…E9, G-E1…E9, Ev2-C1…C12 | labels (prefix WP7-E-v2) | labels |
| used unchanged | ω, Λ, S(q,ω;Λ), 𝔇, P_casc, 𝐍, N_eh, ℋ, E_esc, E_d, N_FP, P_FP, 𝔅₀, t_pr, E^ad_0, E_R, ε_eh, F_eh, ϵ_det, Y_H, E_x^b, E_g, E_c, E_v, Δ_BCS, N_qp, p_st, 𝒦^{rel}, 𝒫_path, ε_path, Γ_path, λ_ij, P̄_STM, T₁, N_FP^{NRT}, E_dam, E_st,1, p_surv, V_bias (= V_b) | NOTATION / WP5 / WP7-T |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-E1 | WP5-v3 | amendment | apply A-1…A-16 |
| IF-E2 | WP7-T-v2 | release sum rule; marks | impose (E6) cut at t_obs; 𝒦^{rel} gains Φ_ph, n_car dependence (stimulated, carrier-driven channels); class → 𝔠 |
| IF-E3 | WP0-v3 (7.3) | rate to observables | P_casc → (E3) marked law ⊗ 𝒫_det; dℛ_bg |
| IF-E4 | WP6-v3 §5.2 | nuisances | §6 rows; type T on a two-point measure for fractions; θ_st, θ_tr, θ_coll profiled jointly with η^φ_NR |
| IF-E5 | WP8 | yields | use N^meas, F_meas^{obs} (with position term), Y_H(t_win) as NR/ER ratios, and η^φ_NR data; declare t_win and E_thr^det |
| IF-E6 | NOTATION | rows | §Symbols "new"; N_trap → N_trap^{pr}; E_st with ΔZPE |
| IF-E7 | WP8-R | ΔE_sl, ϵ_coll(NR)/ϵ_coll(ER) | the quantity that separates E_st from collection in η^φ_NR and f_DF |
| IF-E8 | coordinator: LIMITS, SOTA | rows; L20–L22 sentences | rows below; SOTA: "1803.02903 measures η^φ_NR = 0.952" |
| IF-E9 | WP4-v3 §6 | capture | the shallow-level cascade capture is outside [6.3]; WP4 or WP7 to own it |

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L33 | (E9), frozen emission → (E10) Hecht ⟨𝔵\|z⟩ | K. Hecht, Z. Phys. 77, 235 (1932) [UNVERIFIED, classic; not on arXiv; equation not checked against the original] | exponential trapping, uniform field, no emission, no diffusion, no space charge | athermal emission, diffusion, the depth term of (E12), E_es | DERIVED (C4a) |
| L34 | (E1)–(E2) + Ramo → (E11): 𝒲 = eV_bN^meas; NTL heat 𝒲 − ΔE_es | 1803.02903 Eq. (1) [FT] | two electrodes (else Σ_kV_kΔQ_k), terminal-velocity drift | space charge (ΔE_es), mode-dependent phonon collection ("need not be identical" [FT]) | DERIVED (C2, C5) |
| L35 | (E12) charge collection: F_meas = ϵ_detF_eh + 1 − ϵ_det (corrects 2004.10709 App. A) | 2004.10709 (A6)–(A7) [FT, CONFIRMED by A, B] | single position, Bernoulli collection | position term ⟨N⟩Var_r⟨𝔵⟩/⟨𝔵⟩ | DERIVED (C6) |
| L36 | (E5)–(E6), 𝒦^{rel} = 0, NRT: f_DF ≈ p_surv·0.4(E_dam/E_R)E_st,1/E_d | 1805.09942 Eq. (4), 6.08 ± 0.18% [FT] | dilute cascades, ΔE_trap = ΔE_esc = ΔE_sl = 0, iZIP window | ΔE_trap (polarity), surface ΔE_esc, ΔE_sl; MD ⟨E_st⟩ instead of NRT for dense Pb cascades; TRIM internals UNRESOLVED | DERIVED (C8) |
| L37 | (E8) with D_NR = D_ER: unit heat quenching | 2007.14289 [FT] | E_R below displacement and negligible trapping differences | the Si two-channel datum η^φ_NR = 0.952 (1803.02903): a 4.8% combination d_NR − κd_ER | DERIVED (truncation) |
| L38 | (E13): η^φ_NR = 1 − d_NR + κd_ER + O(d²), y^meas with ⟨𝔵⟩_NR/⟨𝔵⟩_ER | 1803.02903 Eq. (1) and η^φ_NR = 95.2^{+0.9}_{−0.7}% [FT] | ER calibration at the same field, first order in d | O(d²); κ depends on V_b, ε and y; ΔE_sl vs E_st degeneracy (IF-E7) | DERIVED (C7) |
