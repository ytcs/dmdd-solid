# R10 / WP7-E: reconciling the energy partition — one time-resolved energy and charge balance per event (yields, defects, delayed release)

Theory agent, brief R10/WP7-E. Architecture: returns/R8/WP0-v3.md (cited "WP0 (n.m)"); cascade and partition: returns/R8/WP5-v3.md ("WP5 (Wn)", not
re-derived); defect kinetics: returns/R10/WP7-T.md ("WP7-T (n.m)"); multiphonon hand-off WP2-v3 (3.6); nuisance types WP6-v3 (5.1)–(5.1″).
CONVENTIONS.md, NOTATION v4 + R9 rows; state/CORRECTIONS.md read first (no owed correction touches WP5-v3, WP7-T, WP0-v3 §6–§8, WP2-v3 (3.6) or WP6-v3 §5).
Checks: `code/WP7-E/checks.py` (sympy + mpmath, **35 checks, all PASS, ≈ 2 s**), cited WP7E-Cn. Tags per CONVENTIONS §12: [D], [D, sketch], [E], [C];
literature [FT] (read in full text in literature/papers-WP7-E/, PDFs deleted after use), or quoted through the WP5-v3 [FT, CONFIRMED] quotes; every arXiv ID
verified against the arXiv API (2001.06503, 2007.14289, 1803.02903, 2405.10405, 2202.05097, 2208.02790, plus the WP5-v3 IDs 2004.10709, 2209.04503, 1805.09942).
WP5-v3 is **not** edited: its changes are the §5 amendment text. Status: all content CLAIMED (one return), pending the joint WP5 + WP7 audit and R×2.

---
## 0. Results at a glance
| # | Item | Result | Tag |
|---|---|---|---|
| 1 | Balance law | (E1): ω + 𝒲_bias(t) = E_hot + E_pairs + E_trap + E_st(t) + ℋ_ph + E_esc + E_sig + E_sl, every t, event by event; E_stored ≡ E_st + E_trap | D |
| 2 | Exactness | every elementary process conserves energy (13 zero-field processes + drift, WP7E-C2); at t = t_pr (E1) is WP5 (W4) plus a prompt-trap term | D |
| 3 | Two stages | P(𝐌,t\|Λ) = Σ_𝐍 P_casc(𝐍\|Λ) 𝒫_det(𝐌,t\|𝐍) (E3): WP5 owns t < t_pr, WP7-T + detector physics own t > t_pr; coupling only through 𝐍 | D |
| 4 | E_d once | E_d is not a ledger entry: it is the parameter of P_FP (W10). The ledger has E_st; WP7-T only gives E_st(t) (E5) with the sum rule (E6) | D |
| 5 | Yields | yield models act only on E_el; E_st ⊂ E_nuc exactly in Si/Ge (electrons cannot displace, WP5 §4); Lindhard ν = E_nuc (E7) | D |
| 6 | Charge once | a trapped carrier's energy lives only in E_trap; the deficit of a doubly trapped pair is E_g − E^tr_e − E^tr_h, not E_g (WP5 (W11) overstates it, C9c) | D |
| 7 | NTL identity | 𝒲_bias = eV_b N^meas (Ramo–Shockley, two electrodes, no space charge; C5): trapping lowers charge and NTL heat by the same fraction | D |
| 8 | Measured charge | P(N^meas\|event,t): compound law (E12), F_meas = ⟨𝔵⟩F_eh + Var𝔵/⟨𝔵⟩; Hecht relation and CCD thinning are its limits (C4, C6) | D |
| 9 | Two-channel recoil scale | E_R^rec = ω − E_stored(t_win) − E_esc: trapping cancels except through E_trap; measured yield biased in numerator and denominator (C7) | D |
| 10 | mK charge release | thermal and field emission from ≳ 30 meV levels frozen (exponents 10⁴; F ≳ 10⁶ V/cm needed, C10); release is athermal and history-dependent | D / E |
| 11 | Delayed events | event criterion ϵ_coll·ε ≥ E_thr^det: single-defect releases (≤ E_st,1 ≈ eV) and non-interacting TLS (quanta ≲ 10⁻⁴ eV) are heat deficit + sub-threshold power, not LEE events; 10–100 eV events need collective (stress) release | D / E |
| 12 | Time laws | 1/t (broad λ, with cutoffs (e^{−Γ_min t} − e^{−Γ_max t})/t), t^{−3/2} (correlated Frenkel pairs), exponential (narrow); released fraction in a window (C3) | D |
| 13 | Literature | Lindhard: U = 0 ⇒ E_st = 0, 𝔵 = 1; modified Lindhard: U frozen and booked electronic; R&K: E_stored = 0, 𝔵 = 1; KP/TRIM: p_surv = 1, 𝒦^{rel} = 0, fixed E_st,1; QF data: Y_H = 1, 𝔵 = 1 within t_win | D |
| 14 | WP5 amendment | 11 text/equation changes, §5 ((W4), 𝐍, (W11), §3.2, §3.3, §4, §5, §6.1, §6.3, §6.4, §8) | D |
| 15 | Nuisances | 10 new θ in WP6-v3 types (M, A, Δ, T), §6 | D (types) |

---
## 1. The balance law

### 1.1 Reservoirs [D as definitions]
*Hypotheses.* (H-E1) Quasiparticle reservoirs: H_tot = H_C (WP0 (1.1)) + H_sens + H_hold + H_rad + H_bias(t). Between collisions (WP5 (B1)) the expectation of
H_tot in a state of definite quasiparticle content is the sum of the reservoir energies below; inter-reservoir interaction energies are O(Γ/E) and enter only
during collisions (the logic of WP5 (W4)). (H-E2) Contacts in equilibrium, no injection: a collected e–h pair returns E_g as heat at the contacts (with
asymmetric contacts the two barrier heights shift heat between the contacts; the sum is E_g). (H-E3) The bias is external; electrodes are held at fixed
potential. (H-E4) Post-prompt processes are Markov in the reservoir state (no coherence across t_pr). t is measured from the DM vertex; t_pr ≈ 10–100 ps is
WP5's prompt time (§3.2), later than the WP0 (7.1) dressing time ~1/E_g and earlier than any drift (μs) or release (≥ ms).
| Reservoir | Definition | Value at t_pr | Owner |
|---|---|---|---|
| E_hot(t) | carriers above their band edges, hot ions, core holes, undamped plasmons (𝔱 = pl): the WP5 (W3) particles | E_hot(0⁺) = ω (the prompt state Λ of WP0 (7.1)); 0 for t ≥ t_pr by WP5 (H-t) | WP5 |
| E_pairs(t) | Σ_{free e}(E_c − μ) + Σ_{free h}(μ − E_v), μ any reference | N_eh E_g | WP5 |
| E_trap(t) | Σ_j[n^e_j(E_c − E^tr_{e,j} − μ) + n^h_j(μ − E_v − E^tr_{h,j})], depths E^tr, populations n_j | E_trap^{pr} (captures before t_pr) | WP5 (t < t_pr), §2 (t > t_pr) |
| E_st(t) | E^ad_0(R̄(t)) − E^ad_0(R_I(0)): configurational energy of the basin occupied at t (defects, close pairs, pockets, TLS configurations); vibrations excluded | E_st of WP5 §3.2 | WP5 (value), WP7-T (profile) |
| ℋ_ph(t) | absorber phonon energy above the bath (athermal + thermalised) | ℋ of WP5 (W4) ≡ ℋ_pr | WP5, WP2 (3.6) |
| E_esc(t) | cumulative energy that left: photons, phonons into holder/wiring | prompt luminescence only | WP5 |
| E_sig(t), E_sl(t) | cumulative energy absorbed in sensors, split into the part converted to signal (QPs above Δ_BCS, NTD temperature) and the sensor loss (sub-gap phonons, QP trapping/recombination phonons leaving the film, film-TLS storage) | 0 | detector |
| 𝒲_bias(t) | cumulative work of the bias field | 0 | detector |

**Lemma 1 [D] (WP7E-C1).** d(E_pairs + E_trap)/dμ = N_h,tot − N_e,tot over free and trapped carriers in the crystal, so the sum is μ-independent iff the
crystal is neutral (collected carriers are carried by the contact terms of (H-E2)). Only the sum is physical: the E_g share of a trapped carrier sits in
E_trap and nowhere else. With all carriers free and paired, E_pairs = N_eh E_g (C1c).
*Names.* The brief's E_dep is ω (energy given to the target, CONVENTIONS §3); its "Q_prompt" is ℋ_pr (Q is the phonon wavevector, NOTATION §C); its
"E_stored(t)" is **E_stored(t) ≡ E_st(t) + E_trap(t)**; its "E_sensor-loss" is E_sl. For superconducting absorbers E_pairs → N_qpΔ_BCS (WP5 (W13)).

### 1.2 Statement and proof
  ω + 𝒲_bias(t) = E_hot(t) + E_pairs(t) + E_trap(t) + E_st(t) + ℋ_ph(t) + E_esc(t) + E_sig(t) + E_sl(t)     (all t ≥ 0, event by event),          (E1)

  dE_r/dt = Σ_{r′} J_{r′→r}(t),  J_{r′→r} = −J_{r→r′};   d𝒲_bias/dt = Σ_{drifting carriers} e|F·v_d| = (drift power into ℋ_ph, NTL emission).            (E2)

**Theorem E-0 [D under (H-E1)–(H-E4) and WP5 (B1)].** (E1) is exact. *Proof.* H_tot is conserved except for the external work 𝒲_bias. Every elementary
process is either a WP5 (W3) vertex (energy-conserving, WP5 §1.2) or one of the post-prompt processes of §1.3, each of which moves energy between
reservoirs without loss (WP7E-C2a, 13 zero-field processes) or turns bias work into NTL phonons (C2b). Summing the flux form (E2) from E_hot(0⁺) = ω gives
(E1). ∎ At t = t_pr (no drift, no sensor absorption yet) (E1) reads ω = N_eh E_g + ℋ_pr + E_st + E_esc + E_trap^{pr}: **WP5 (W4) is the case E_trap^{pr} = 0**
(C2c). "Exact" means for the expectation at every t and event by event under (B1); the WP5 (B2) caveat (dense tracks) affects which processes occur, not (E1).
*Mean ledger from the response.* At fixed (q, ω, v), every reservoir mean is the Λ-weighted cascade mean, with the WP0 (7.3) weights:

  ⟨X(t)⟩(q,ω) = Σ_Λ w_Λ ⟨X(t)⟩_Λ,   w_Λ = tr[𝔇ᵀS(q,ω;Λ)]/tr[𝔇ᵀS(q,ω)],   ⟨X(t)⟩_Λ = Σ_𝐍 P_casc(𝐍|Λ) ⟨X(t)|𝐍⟩_det.                                        (E1′)

So every term of (E1) is defined from the final-state-resolved response (WP0 (7.1)–(7.2)) and the WP5 cascade, as the brief requires: X0 seeds at
(Λ₀, Ẽ_Λ₀), X+ seeds with ω_ph → ℋ_pr once (O4-d6), GS seeds through (W9) and ρ^ph_κ (WP2-v3 (3.6), absorbed entries carrying negative heat).

### 1.3 The process ledger [D] (WP7E-C2; energies relative to μ; F the field, Δz the drift step)
| Process | From → to (energy) | Time scale | Stage |
|---|---|---|---|
| carrier relaxation to the edges | E_hot → E_pairs (E_g per pair), ℋ_ph (rest) | ≤ t_pr | WP5 (W1)–(W3) |
| capture of e (h) on level j | E_pairs → E_trap (E_c − E^tr − μ), ℋ_ph (E^tr) | ns–ms (ℓ^tr/v_d) | §2 (WP5 if < t_pr) |
| emission from level j | reverse of capture; E^tr drawn from ℋ_ph or from an athermal trigger | frozen–s (§2.1) | §2 |
| recombination at a trap | E_trap + E_pairs → ℋ_ph (non-radiative, E_g − E^tr) or E_esc / E_sig (radiative) | μs–s | §2, WP4-v3 §6 |
| band-to-band or contact recombination | E_pairs → ℋ_ph (E_g; (H-E2)) | μs (drift) | §2 |
| drift by Δz | 𝒲_bias → ℋ_ph (eFΔz, NTL phonons) | μs | §2 |
| lattice release along a path | E_st → ℋ_ph (ε_path; FC spectrum WP7-T (4.4)) or E_esc / E_sig (photon fraction) | 𝒦^{rel}, ms–years | WP7-T (5.2) |
| resonant phonon absorption by a TLS | ℋ_ph → E_st | Γ₁⁻¹ | WP7-T §2 |
| phonon into a sensor / escape | ℋ_ph → E_sig + E_sl / E_esc | μs–ms | detector |

### 1.4 Two-stage factorisation [D given (H-E4)]
Extend WP5's 𝐍 at t_pr by the information the detector stage needs: 𝐍 = (N_eh, ℋ_pr, E_st, N_FP, E_esc, N_trap^{pr}, E_trap^{pr}, c, r_ev), with c the
configuration class of WP7-T (5.1) and r_ev the event position and track geometry (including the track's own trap density). With 𝐌(t) the measured
vector (phonon energy in a window, N^meas, delayed events):

  P(𝐌, t | Λ) = Σ_𝐍 P_casc(𝐍 | Λ) 𝒫_det(𝐌, t | 𝐍),                                                                                               (E3)
  dℛ/d𝐌 = (ρ_χ/m_χρ_T) ∫d³v f_χ ∫d³q/(2π)³ Σ_Λ tr[𝔇ᵀS(q,ω_q;Λ)] P(𝐌, t | Λ)  +  dℛ_bg/d𝐌   (WP0 (7.3) with P_casc → (E3); dℛ_bg from §3.3).       (E4)

*Proof.* Markov property at the deterministic time t_pr: condition on the reservoir state at t_pr. ∎ Each process is assigned to exactly one stage by its
time, so nothing is counted twice; the stages are **not** independent (𝒫_det depends on c, E_st and r_ev), which is how the yield and the detector response
share trapping without double counting (Theorem E-3).

### 1.5 The three consistency conditions
**Theorem E-1 (E_d is counted once) [D].** (i) E_d does not appear in (E1). It enters only as the parameter of P_FP (W10), i.e. through the probability that
the basin at t_pr differs from 𝔅₀, hence through the distribution of (E_st, N_FP, c). The kinetic energy spent above the final configuration energy,
E_d − E_st in the step model, is already inside ℋ_pr (WP5 §3.2). (ii) WP7-T fixes only the time profile:

  E_st(t) = E_st − ∫_{t_pr}^{t}dt′ ∫dE E 𝒦^{rel}(E, t′ − t_pr | c, E_st, T),                                                                       (E5)
  ∫_0^∞dt ∫dE E 𝒦^{rel}(E,t | c, E_st, T) = E_st − E_st^{frz}(c, E_st, T) ≡ E_st^{rel},                                                              (E6)

with E_st^{frz} the configurational energy of the end state reached at temperature T on the observation time (λ > 24 classes, WP7-T §4.2). For the
WP7-T (5.2) kernel, ∫dt Γe^{−Γt} = 1 (C3a), so (E6) is the condition Σ_path 𝒫_path ε_path = E_st^{rel}: **a constraint on WP7-T's path tables, not an
identity** (flag IF-E2). For a broad-λ ensemble the kernel is normalised (C3b, C3c). (iii) Released energy enters ℋ_ph (phonon branch) or E_esc / E_sig
(photon branch) and no other term. *Proof.* (E1) with (E5): the t-axis is partitioned once (C9b). ∎ **Forbidden combinations:** (a) subtracting E_d, or
TRIM's per-displacement "energy to defects", from the heat and also adding the delayed release; (b) adding release that occurs inside the sensor's
integration window to a heat yield measured with that window; (c) writing N_FP·E_d for the stored energy (E_st ≠ E_d, WP5 §3.2).

**Theorem E-2 (yield models act on the electronic share only) [D given WP5 §3–§4].** Define, per event, E_el as the sum of all electronic excitation energies
deposited by the cascade: the X-sector ω_e at the vertex (Theorem D (6.1)), the slow-ion electronic losses (WP5 §3.3: momentum-tail and Landau–Zener channels)
and the electronic losses of fast secondaries; E_nuc ≡ ω − E_el. (i) The electronic sub-cascade cannot displace atoms (4m_eE/M_κ ≤ 0.78 meV ≪ E_d at
10 eV in Si, WP5 §4, WP5v3-C11), so it adds nothing to E_st; (ii) the ion branch makes pairs only through E_el, by definition. Hence at t_pr

  E_el = N_eh E_g + ℋ_el + E_esc^{el} + E_trap^{pr},    E_nuc = ℋ_nuc + E_st,    ℋ_pr = ℋ_el + ℋ_nuc,                                                 (E7)

and Lindhard's ν = E_nuc is WP5's corrected observable ℋ_nuc + E_st (§6.1). A yield model is a map from the electronic seed spectrum dP/dω_e to P(N_eh)
(WP5 §3.3: N̄_eh = Σ(dP/dω_e)n̄(ω_e)). It must not be applied to E_R and then corrected by E_st (a second subtraction of what ν already holds), and E_st must
not be booked in E_el (the 2209.04503 secondary-U complement, WP5 §6.1(5)). Scope: Si, Ge and every target where electronic excitation cannot break bonds;
ionic targets with excitation-driven defect creation (self-trapped excitons, colour centres; WP5 §4, WP4) break (i) (gap G-E1).

**Theorem E-3 (trapped charge is counted once) [D].** (i) *Energy:* capture moves E^tr into ℋ_ph, emission takes it back, recombination at the trap
releases E_g − E^tr (C2a). A pair trapped on two levels and never recombined leaves the deficit E_g − E^tr_e − E^tr_h, not E_g; WP5 (W11)'s ⟨N_trap⟩E_g
overstates it by N_trap(E^tr_e + E^tr_h) (C9c) and is the shallow-level limit. (ii) *Charge:* a trap removes the carrier's remaining Ramo fraction from
N^meas and, in NTL mode, the same fraction from 𝒲_bias (E11), so both channels see one loss. (iii) *Yield vs response:* P_casc counts pairs reaching the band
edges plus captures before t_pr (N_trap^{pr}, E_trap^{pr}); every later capture belongs to 𝒫_det. Track traps (created by the same recoil) couple the stages
through (c, r_ev) in (E3), with no second count.

### 1.6 Time windows and thresholds [D]
A detector integrates its sensor signal over [0, t_win] after the trigger and has a threshold E_thr^det. Each released quantum of E_st^{rel} belongs to exactly
one class: **in-pulse** (t < t_win: it reduces the prompt heat deficit), **delayed event** (t > t_win and collected energy ≥ E_thr^det), **sub-threshold
continuum** (t > t_win, below threshold: heat load, noise, QP poisoning), or **frozen** (E_st^{frz}). With P_rel(t_win) the released fraction (C3):
single path 1 − e^{−Γt_win}; broad λ [ln(Γ_max t_win) + γ_E]/ln(Γ_max/Γ_min) for Γ_max⁻¹ ≪ t_win ≪ Γ_min⁻¹ (C3d); correlated Frenkel-pair recombination
erfc(d/√(4D t_win)) (C3e). The windowed heat quenching, relative to an ER calibration at equal ω, is

  Y_H(t_win) = 1 − [⟨E_st^{frz}⟩ + ⟨E_st^{rel}⟩(1 − P_rel(t_win)) + ⟨E_trap(t_win)⟩ + ⟨ΔE_esc⟩ + ⟨ΔE_sl⟩]/E_R   (+ eV_b⟨ΔN^meas(t_win)⟩/E_R in NTL mode),   (E8)

Δ = NR minus ER at equal ω (calibration cancels ϵ_coll and E_sl only to the extent that NR and ER phonon spectra convert equally: the WP8-R question,
flag IF-E7). Y_H rises with t_win (C9a).

---
## 2. Charge: trapping and release on defect levels, and the measured charge

### 2.1 Trap kinetics at mK [D for the structure; E for numbers]
Levels j: pre-existing (dopants, residual impurities, dislocations, surfaces) and event-created (the defects of class c along the track, density
𝓃_c^{trk}(r)). Shockley–Read–Hall-type rate equations, with drift velocity v_d and trapping lengths ℓ^tr_{e,h} = v_d/Σ_jσ_j v_th(𝓃_j − n_j):

  dn^e_j/dt = σ^e_j v_th N_e^f(𝓃_j − n^e_j)/V_loc − Γ^{em}_{e,j} n^e_j − σ^{rec}_j v_th N_h^f n^e_j/V_loc   (and e ↔ h),                              (E9)

coupled to carrier continuity in the field F (Poisson with the trapped space charge). **Emission channels at mK:**
- *Thermal*, Γ^{em} ∝ e^{−E^tr/T}: for E^tr = 45 meV (P in Si [UNVERIFIED value]) at 50 mK the exponent is 1.0×10⁴ (C10c): frozen for E^tr ≳ 30T.
- *Field (triangular barrier)*: WKB exponent (4/3)√(2m*)E^{tr 3/2}/(eF) (C10a); reaching 30 needs F ≈ 1.2×10⁶ V/cm (m* = 0.3m_e [E], C10b), far above
  detector fields (1–100 V/cm): absent.
- *Athermal*: phonons from later events and NTL phonons with energy ≥ E^tr; impact ionisation of neutral shallow centres by drifting carriers at higher
  fields [UNVERIFIED as to thresholds]; infrared flashing: 1803.02903 [FT] "By careful neutralization of ionized trapping sites within the crystal with regular
  exposure to infrared LEDs ('flashing'), the detectors were operated in a metastable state in which trapping of charge carriers in the crystal bulk was low."
- *Defect-borne traps*: a trap on a relaxing defect moves or disappears when the defect hops, so Γ^{em} includes Γ_path of WP7-T (4.2) for those levels.
**Consequence [D].** At mK, n_j(t) is a history variable (all prior events, flashing, cooldown) and emission is triggered, not thermal. The delayed-charge
rate ℛ_q^{del}(t) = Σ_j n_j(t)Γ^{em}_j is therefore correlated in time and position with prior large depositions, and the trapped space charge makes the
field (hence 𝔵 below) a slowly varying function of exposure (nuisance θ_SC).

### 2.2 Induced charge and the bias-work identity [D]
Ramo–Shockley: a charge q moving r₀ → r₁ induces q[U_R(r₁) − U_R(r₀)] on the readout electrode, U_R the weighting potential (1 on that electrode, 0 on the
others, Laplace). For one pair born at r_ev define 𝔵 ∈ [0, 1] as the induced charge in units of e after both carriers stop (trapped or collected).
Planar detector of thickness d, uniform field, depth z, exponential trapping, no emission: the mean over trapping points is the **Hecht relation**

  ⟨𝔵⟩ = (ℓ^tr_e/d)(1 − e^{−(d−z)/ℓ^tr_e}) + (ℓ^tr_h/d)(1 − e^{−z/ℓ^tr_h})   (C4a; ⟨𝔵⟩ → 1, Var 𝔵 → 0 as ℓ^tr → ∞, C4b,c).                              (E10)

If the bias field is V_b times the weighting field (two electrodes, no space charge), the work on a carrier equals V_b times its induced charge (planar and
coaxial geometries verified, C5a,b), so

  𝒲_bias(t) = eV_b N^meas(t)     (exact under these conditions; with space charge or interleaved electrodes use the actual field and each electrode's U_R).   (E11)

**NTL phonons count measured charge, not created pairs.** WP5 (W11)'s "+ N_eh eV_bias/E_R" is the complete-collection limit of (E11).

### 2.3 The measured-charge observable P(N^meas | event, t) [D under (H-E5)]
(H-E5) Given the event (r_ev, the track trap density), carriers drift independently: no mutual space charge or track recombination after t_pr (the WP5 (B2)
caveat persists inside NR tracks; gap G-E5). Then N^meas(t) = Σ_{i=1}^{N_eh}𝔵_i(t) with i.i.d. 𝔵_i, and

  E[e^{s N^meas(t)} | Λ, t] = Σ_N P_casc(N_eh = N | Λ) φ_t(s)^N = 𝔊_Λ(ϑ_N = ln φ_t(s)),   φ_t(s) ≡ E[e^{s𝔵(t)}],
  ⟨N^meas⟩ = ⟨N_eh⟩⟨𝔵⟩,   F_meas ≡ Var N^meas/⟨N^meas⟩ = ⟨𝔵⟩F_eh + Var 𝔵/⟨𝔵⟩   (C6a),                                                        (E12)

plus readout noise. Two readout classes: **(i) induced charge** (HPGe, CDMS-type, NTL phonon readout): 𝔵 continuous; **(ii) charge collection** (skipper
CCD): 𝔵 ∈ {0, 1} with probability ϵ_det(t) per carrier, so F_meas = ϵ_detF_eh + 1 − ϵ_det (C6b, = WP5v3-C2a) and a Poisson N_eh stays Poisson (C6c). 𝔵_i(t) is
non-decreasing after t_pr while emission occurs; with frozen emission N^meas(∞) is the Hecht-thinned yield. *Track self-trapping:* the recoil's own defects
trap part of its own pair cloud, so 𝔵 is correlated with E_st and the NR measured yield is lower than ⟨N_eh⟩⟨𝔵⟩_bulk; the joint law P(N^meas, E_stored | E_R)
is a computation (§7), not a yield-model parameter.
*Data bound [FT, 2405.10405].* Ge, 254 eV_nr, yield 64 ± 8 eV_ee (QF 25 ± 3%): "The data was analyzed with three trapezoidal shaping times, 2, 8, and 16 µs,
and four Gaussian shaping times, 2, 6, 12, and 18 µs … the reconstructed combined energy deposition … differed by less than 2 eV with one exception".
So the window-dependent part of N^meas for that detector is ≲ 2/64 ≈ 3% of the recoil's ionization between 2 and 18 µs [E, our reading]. (Their stated
motivation was the 700 ns nuclear-state lifetime, not trapping; the bound applies to both.)

---
## 3. The observable map

### 3.1 Prompt heat [D]
Zero field, t_win longer than recombination: E_pairs(t_win) = 0 and 𝒲_bias = 0, so by (E1) ℋ_ph(t_win) + E_sig + E_sl = ω − E_stored(t_win) − E_esc(t_win);
the calibrated heat signal is Y_H(t_win)·ω (E8). **The zero-field heat is blind to N_eh** (every recombined pair returns E_g); it sees only E_stored, escapes and
sensor-loss differences. NTL mode adds eV_bN^meas (E11). *Two-channel reconstruction* (1803.02903 Eq. (1) [FT]: "E_φ = E_R + E_Q eV_b/ε = E_R(1 + y eV_b/ε)",
y ≡ E_Q/E_R, E_Q = εN^meas): E_R^rec ≡ E_φ − eV_bN^meas = ω − E_stored(t_win) − E_esc (C7a). Trapping cancels **except through E_trap**, and the measured
yield y^meas = εN^meas/E_R^rec carries ⟨𝔵⟩ in the numerator and the stored-energy deficit in the denominator (C7b).

### 3.2 Measured charge [D]: (E12), with 𝔵-laws from (E9)–(E10) and the window t_win; delayed charge ℛ_q^{del} is §3.3 class (iv).

### 3.3 Delayed-event rate and spectrum; the low-energy-excess model [D for the structure; E for numbers; C where stated]
  dℛ_del/dE dt = Σ_c ∫dt′ 𝔰_c(t′) 𝒦^{rel}(E, t − t′ | c, T) ⊗ 𝒯_c(E → E^meas)   +   ℛ_q^{del}(t) ⊗ 𝒯_q,                                              (E13)

with sources 𝔰_c: **(i) event-seeded**, 𝔰_c^{ev}(t) = ∫dE_R ℛ_seed(E_R,t)P(c|E_R) from p_st (WP7-T (5.1)); **(ii) cooldown-seeded**, TLS and defect
populations frozen in at the temperature T₁ where relaxation falls behind cooling (WP7-T (4.5): stored excess π²P̄_STMV(T₁² − T₀²)/12); **(iii) stress-seeded**
(holder clamps, glue, film stress); and **(iv) trapped charge**, ℛ_q^{del} of §2.1. Transfers: absorber releases are phonons collected with ϵ_coll; sensor-film
releases deposit directly in the film (ϵ ≈ 1, different pulse shape); delayed charge is quantised (single carriers; eV_b each in NTL mode). Time laws from
WP7-T: 1/t (broad λ; with cutoffs (e^{−Γ_min t} − e^{−Γ_max t})/(t ln(Γ_max/Γ_min)), C3b), t^{−3/2} (correlated Frenkel-pair recombination, 1D crowdion and 3D),
exponential (narrow barrier sets), (1 + t/t₀)⁻² (uncorrelated bimolecular). Spectrum per release: one phonon at ε (TLS-like hops) or the FC multiphonon
spectrum WP7-T (4.4) (eV recombinations), then WP5 down-conversion.
**Event criterion [D].** A release is a delayed *event* only if its collected energy exceeds E_thr^det: ϵ_coll ε_path ≥ E_thr^det (absorber) or ε_path ≥ E_thr^det
(film). Consequences:
- **(a) Non-interacting TLS give power, not events.** Each release quantum is ≲ few T₁ (≈ 3×10⁻⁴ eV for T₁ = 1 K). An amorphous film of 100 nm × 1 cm² with
  a-SiO2's P̄_STM stores ≈ 1×10⁶ eV and releases ≈ 0.6 eV/s at t = 10 d (C12a,b) [E]: a sub-threshold heat load (and QP-poisoning source), never 10 eV
  events; a 10 eV event would need ≥ 10⁴ quanta released coherently (C12c), i.e. collective release (WP7-T G-T4, [C]).
- **(b) Particle-seeded single-defect releases are sub-threshold today.** ε_path ≤ E_st,1 ≈ 7–9 eV per Frenkel pair [UNVERIFIED, WP5 §3.2], so ϵ_coll ε ≈ 2.7 eV
  (ϵ_coll = 0.3 [E]) against 30.1 eV, the CRESST Det-A nuclear-recoil threshold quoted in 2202.05097 [FT] (C11b). They appear as the heat deficit (up to
  N_FP E_st,1/E_R ≈ 0.13 at 1 keV with p_surv = 1, C11a,c [E]) and a sub-threshold continuum; they become visible only for E_thr^det ≲ 1 eV. Their rate is
  bounded by ℛ_NR(E_R ≥ E_d) × (releases per seed), negligible underground. *Discriminants:* rate grows after neutron calibration and scales with the NR
  exposure; t^{−3/2} or 1/t per seed; non-ionizing unless the release is radiative or above E_g.
- **(c) 10–100 eV delayed events need collective release of stored stress energy** (dislocation avalanches, microfracture, glue and holder relaxation, film
  stress): background reservoirs (ii)–(iii), not event-attributable, entering (E4) through dℛ_bg. This agrees with three full-text observations: experiments "observe excess
  low-energy (10–100 eV scale) events of an unknown origin" from "a background source that is non-ionizing … and which also decreases with time since
  cooldown"; a glued crystal shows "a rate of low-energy phonon events that is more than two
  orders of magnitude larger than in a functionally identical crystal suspended from its holder in a low-stress state", with rates that "decreased with a
  time constant of 6–10 d" (2208.02790 [FT]); "Sudden increases were observed at times after warming-up the detectors above 10 K" (2202.05097 [FT], EDELWEISS/
  Ricochet), i.e. reservoir refilling by a T₁ cycle; and EDELWEISS RED30: "most of the events observed above 15 eV_ee (400 eV in total energy) are not
  associated with the creation of electron-hole pairs" (2202.05097 [FT]), i.e. lattice or film release, not class (iv). The avalanche size law is [C] (gap
  G-E2). The **time law** is a discriminant: a broad-λ population truncated at Γ_min ~ (10 d)⁻¹ gives (e^{−Γ_min t} − e^{−Γ_max t})/t, a 1/t rise at early times
  that a single exponential lacks; 2208.02790 [FT] fits exponentials over 5 d (and quotes CRESST fast ≈ 15 d and slow ≈ 1 yr constants), which does not
  separate the two [E].
- **(d) Delayed charge** (class (iv)) is ionizing, quantised under NTL gain and correlated with prior large depositions (§2.1): distinct from (a)–(c).

### 3.4 Which detector types see which terms [D]
| Detector type (examples) | ℋ_pr | E_g of pairs | N^meas | E_st deficit | E_trap | lattice/stress releases | delayed charge | film relaxation |
|---|---|---|---|---|---|---|---|---|
| zero-field phonon calorimeter (TES/QET on Si, Ge; CRESST CaWO₄/Al₂O₃; KID) | yes | yes (recombination heat) | no | yes, through Y_H(t_win) | yes (deficit E_g − ΣE^tr) | events if ϵε ≥ E_thr (collective); else continuum | no (only their tiny heat) | yes, direct |
| NTL / HV phonon (SuperCDMS HV, EDELWEISS-NTL) | yes | yes | ×eV_b (E11) | yes | yes, and lost NTL gain | yes, **without** NTL gain | yes, NTL-quantised | yes |
| heat + ionization (CDMS II, EDELWEISS) | yes | yes | yes | biases E_R^rec (C7) | biases E_R^rec and y | yes in heat only | yes in charge | yes |
| charge only (HPGe; skipper CCD) | no | no | yes (E12) | no | yes, through 𝔵 | only if radiative or > E_g | yes (single carriers) | no |
| scintillating calorimeter (light channel) | via heat | luminescence fraction in E_sig/E_esc | no | heat channel | radiative trap recombination = delayed light | heat channel | afterglow | yes |
| superconducting absorber / qubit (Al, Nb films) | yes | N_qpΔ_BCS (W13) | no | as calorimeter | — | yes | — | yes: dominant (QP poisoning) |

---
## 4. Literature limits, with their implicit defect assumptions [D for the limits; sources as tagged]
**L20 Lindhard (and modified Lindhard).** *Source.* 2001.06503 Eqs. (3)–(7) and 2209.04503 Eq. (2), quoted [FT, CONFIRMED] in WP5 §6.1. 2001.06503 [FT]:
Lindhard's model aims at energies "when atomic binding energies can be safely neglected"; with a constant binding u "the quenching factor for nuclear recoils
features a cut-off at an energy equal to twice the assumed binding energy"; its Table 1 lists "Dislocation 36" eV (Si) and "23" eV (Ge) next to the
average pair energy. *Implicit defect assumption.* (i) U = 0: displacing an atom costs nothing, so E_st = 0 and ν = ℋ_nuc; (ii) the QF depends only on the
E_el/E_nuc split, never on how E_nuc divides into ℋ_nuc and E_st, so Lindhard says nothing about the heat channel beyond Y_H = 1; (iii) charge N_eh = E_el/ε_eh^γ
with complete collection, 𝔵 = 1, E_trap = 0. *Limit of (E1).* t = t_pr, E_st = E_trap = 0, 𝔵 = 1, photon conversion of E_el, truncation 0 (BCA + Markov) of
WP5 §6.1. *Modified Lindhard* (U = U_FP + U_EDFT): each secondary displacement stores U permanently (𝒦^{rel} = 0) and, by complement, books it electronic
(WP5 §6.1(5)); the cut-off at 2u makes one number play both E_d (threshold) and E_st (energy). In the URF the two separate: E_d sets P_FP (W10), E_st enters the
ledger inside E_nuc (Theorem E-2).
**L21 Ramanathan–Kurinsky.** *Source* 2004.10709 Eqs. (5)–(11), [FT, CONFIRMED] in WP5 §6.2. *Implicit defect assumption:* ER seeds cannot displace (exact in
Si, WP5v3-C11), so E_st = 0; measured pairs = created pairs (𝔵 = 1, E_trap = 0, no escape). Its validation data (skipper CCD ε_eh = 3.749 eV at 123 K, 2004.11499
via WP5) are charge-collection data, so any loss is ϵ_det thinning (E12)(ii). *Limit:* (E1) with E_stored = E_esc = 0 and ϵ_det = 1, then the WP5 §6.2 chain.
**L22 Kinchin–Pease / NRT / TRIM.** *Source* 1805.09942 Eq. (4) and the TRIM sentence "TRIM predicts a monotonic, decreasing relationship between the percent
energy lost to defects … and E_d", [FT, CONFIRMED] in WP5 §6.3; NRT N_FP^{NRT} = 0.8E_dam/2E_d (Kinchin–Pease, not on arXiv). *Implicit defect assumption:*
p_surv = 1 (no prompt recombination), no annealing (𝒦^{rel} ≡ 0, everything frozen), and a stored energy per displacement E_st,1 fixed independently of E_d:
with f_DF ≈ p_surv·0.4(E_dam/E_R)E_st,1/E_d the TRIM sentence holds at fixed E_st,1 (C8a), while E_st,1 = E_d would make f_DF E_d-independent (C8b). So the
measured 6.08 ± 0.18% fixes the product p_surv E_st,1/E_d, not E_d alone, and the URF supplies E_st,1 = ⟨E_st⟩/⟨N_FP⟩ from p_st. *Limit:* (E5) with 𝒦^{rel} = 0,
E_st = N_FP^{NRT}E_st,1, p_surv = 1. A measurement integrates its own window: in the URF f_DF(t_win) = [E_st^{frz} + E_st^{rel}(1 − P_rel(t_win))]/E_R.
**Measured quenching data.** (a) *Ionization QF, two-channel (CDMS II Si, 1803.02903 [FT]):* recoil energy from E_φ − E_QeV_b/ε (Eq. (1), quoted §3.1), the
phonon scale set so that bulk electron recoils "should have unity ionization yield", and trapping suppressed by flashing (quoted §2.1). *Implicit:*
E_stored(t_win) = 0 for NR relative to ER (Y_H = 1) and 𝔵 = 1. *Limit:* (C7) with E_stored → 0 and ⟨𝔵⟩ → 1; the URF measured yield is
y^meas = ε⟨𝔵⟩⟨N_eh⟩/(ω − E_stored − E_esc). (b) *Ionization QF, charge only (Ge, 254 eV_nr, 2405.10405 [FT]):* E_ee from "the difference between this summed
energy and the energy of the final state"; QF 25 ± 3%, "greater than the 14% predicted by the Lindhard model". *Implicit:* complete collection within the
µs shaping window; URF: the measured QF is ⟨𝔵⟩·QF_created, window dependence ≲ 3% between 2 and 18 µs (§2.3). (c) *Heat quenching (SuperCDMS CPD,
2007.14289 [FT]):* "The heat quenching factor (the ratio of heat signals produced by nuclear and electron recoils of the same energy that accounts for effects
such as displacement damage) has been assumed to be unity for this work." *Implicit:* E_stored(t_win) = ΔE_esc = ΔE_sl = 0. *Limit:* (E8) with those zero;
exact for E_R below the displacement step (no E_st) up to E_trap, and wrong by up to ~13% at 1 keV if p_surv = 1 (C11c) [E].

---
## 5. Amendment to WP5-v3 (exact text; WP5-v3 itself is not edited)
**A-1. §1.2, after (W4), insert:** "(W4) is the t = t_pr case of the time-resolved balance WP7-E (E1) with no capture before t_pr. With captures before t_pr it
reads ω = N_eh E_g + ℋ + E_st + E_esc + E_trap^{pr}, where E_trap^{pr} is the energy of carriers in the absorbing state 'trapped' of (W3), defined with E_pairs as in WP7-E §1.1
(only E_pairs + E_trap is reference-independent). For t > t_pr the evolution of every term is WP7-E (E1)–(E2): trapping, emission, drift (bias work), recombination,
lattice release and sensor absorption are post-prompt processes and are not part of P_casc."
**A-2. §1.2, the definition of 𝐍, replace** "𝐍 = (N_eh, ℋ, E_st, N_FP, E_esc, …)" **by** "𝐍 = (N_eh, ℋ, E_st, N_FP, E_esc, N_trap^{pr}, E_trap^{pr}, c, r_ev): N_trap^{pr}
counts captures before t_pr only; c is the configuration class of WP7-T (5.1); r_ev the event position and track geometry (WP7-E §1.4)."
**A-3. §3.2 "Stored energy", append:** "E_st is its value at t_pr. Its later evolution is E_st(t) = E_st − ∫_{t_pr}^t dt′∫dE E𝒦^{rel}(E, t′−t_pr | c, E_st, T), with the
sum rule ∫∫E𝒦^{rel} = E_st − E_st^{frz} (WP7-E (E5)–(E6)). E_d enters only through P_FP (W10); the energy ledger contains E_st, never E_d (WP7-E Theorem E-1)."
**A-4. §3.4, replace (W11) and the sentence after it by:**
"Y_H(t_win) ≡ ⟨ℋ_meas(t_win)⟩/E_R = 1 − [⟨E_st^{frz}⟩ + ⟨E_st^{rel}⟩(1 − P_rel(t_win)) + ⟨E_trap(t_win)⟩ + ⟨ΔE_esc⟩ + ⟨ΔE_sl⟩]/E_R (zero field; NTL mode adds
eV_b⟨ΔN^meas(t_win)⟩/E_R, with N^meas the Ramo-weighted measured charge, WP7-E (E11)), (W11)
with Δ = NR minus ER at equal deposited energy. (W11) follows from WP7-E (E1). A pair trapped on two levels contributes E_g − E^tr_e − E^tr_h, not E_g; v3's
⟨N_trap⟩E_g is its shallow-level limit. Unit heat quenching (2007.14289 [FT]) is the truncation E_st = E_trap = ΔE_esc = ΔE_sl = 0 within t_win."
**A-5. §3.3 "Charge from the electronic deposit", append:** "The measured charge is N^meas = Σ_i𝔵_i (WP7-E (E12)): ⟨N^meas⟩ = ⟨N_eh⟩⟨𝔵⟩. Comparisons with QF data
use N^meas and the detector's 𝔵-law; trapping, including trapping on the recoil's own defects, is a detector-stage effect, not a yield effect. A yield model acts
on the electronic seed spectrum only (WP7-E Theorem E-2)."
**A-6. §4, replace** "ℛ_rel(E,t) = Σ_{ij} Γ_ij(T) N_i(t) δ(E − (E^{conf}_i − E^{conf}_j)) ⊗ (detector response)" **by** "… ⊗ 𝒯_c(E → E^meas), counted as an event only
if the collected energy exceeds E_thr^det (WP7-E (E13))", **and append to "Time dependence":** "Single-defect releases carry ≤ E_st,1 (eV) and non-interacting TLS
releases ≲ few T₁; both lie below present thresholds and appear as heat deficit and sub-threshold power. 10–100 eV delayed events require collective release
(WP7-E §3.3). Below T_× the rates are WP7-T (4.2)–(4.3) (WP7-T IF-T2)."
**A-7. §5, after (W13), insert:** "E_sub + E_excess + E_esc (film) is the sensor-loss term E_sl of WP7-E (E1)."
**A-8. §6.1, chain step 4, append:** "(F) Implicit defect assumptions: Lindhard U = 0 ⇒ E_st = 0; complete collection 𝔵 = 1, E_trap = 0; 2209.04503's U is frozen
stored energy booked electronic by complement (WP7-E §4)."
**A-9. §6.3, chain step 4, after the f_DF formula, append:** "The measured f_DF fixes p_surv E_st,1/E_d; with E_st,1 = E_d it would be E_d-independent, contrary to the
TRIM sentence (WP7E-C8). In the URF f_DF(t_win) = [E_st^{frz} + E_st^{rel}(1 − P_rel(t_win))]/E_R."
**A-10. §6.4 "Validity", replace** "no trapping before counting" **by** "(W14) concerns created pairs N_eh; the measured Fano factor is F_meas = ⟨𝔵⟩F_eh + Var𝔵/⟨𝔵⟩
(WP7-E (E12)), which reduces to ϵ_detF_eh + 1 − ϵ_det for charge collection".
**A-11. §8, replace the θ_esc row by** "θ_esc | escape only (E_esc, ΔE_esc) | M | per detector" **and add** "θ_tr, θ_em, θ_SC, θ_frz, θ_λ, θ_γ, θ_𝒦, θ_law, θ_coll,
θ_bg,c: WP7-E §6".

---
## 6. Uncertainty: nuisances for the new terms (WP6-v3 types)
| θ | Increment / object | Type (WP6-v3 (5.1)–(5.1″)) | Prior / size | Correlation | Source |
|---|---|---|---|---|---|
| θ_frz | relaxing vs frozen split of E_st per class (λ-class boundary 24) | Δ (boundary variants 22, 24, 26), then M on E_st^{rel} with support E_st^{rel} ≤ E_st (support restriction, as L17 in WP6) | σ_ln from the λ-spread | material, T | WP7-T §4.2, (5.1) |
| θ_λ, θ_γ | WKB exponent spread, defect deformation potential (WP7-T §4.6) | M on each Γ_path (σ_ln = 2σ_λ; 2σ_γ/γ) | from instanton vs WKB | material | WP7-T |
| θ_𝒦 | shape of 𝒦^{rel} at fixed sum rules | T (tilt with linear constraints ∫𝒦 = Σ𝒫, ∫E𝒦 = E_st^{rel}) | 𝒩(0,1) | class c | (E6) |
| θ_law | time-law choice per class {1/t, t^{−3/2}, exponential} | Δ | discrete profiling | class c | WP7-T §4.3, §4.5 |
| θ_tr | trapping lengths ℓ^tr_e, ℓ^tr_h (and track trap density) | M | per detector and flash state; HPGe window bound ≲ 3% (2405.10405) | detector | (E9)–(E10) |
| θ_em | athermal emission rates Γ^{em}_j | M | unknown at mK: wide (σ_ln ≥ 2) | detector, history | §2.1 |
| θ_SC | space charge / field map | Δ (field maps) + M | per exposure state | detector | §2.1 |
| θ_coll | ϵ_coll(NR)/ϵ_coll(ER) and ΔE_sl (mode-dependent collection) | M with support ϵ_coll ≤ 1 | until WP8-R: σ_ln 0.1 [E] | material–sensor pair | IF-E7 |
| θ_bg,c | amplitudes of background reservoirs (cooldown, stress, film) | A (positive rate increments; PSD trivially) | log-normal, per run | run | §3.3 |
| θ_esc | escape only (amended WP5 row) | M | per detector | detector | WP5 §8 |
*Exact constraints.* (E1) is linear in E_st^{rel}, E_trap, ΔE_esc, ΔE_sl: a measured Y_H(t_win) constrains their sum, and Y_H at two windows constrains
E_st^{rel}P_rel separately. Two-channel data constrain E_stored and ⟨𝔵⟩ separately, because E_R^rec does not depend on 𝔵 (C7a). (E11) ties θ_tr in the charge
and NTL channels (one parameter, not two). (E6) is enforced exactly by type T. WP5's (W4) constraints on θ_GW, θ_Z, θ_{R-k} are unchanged (they act on N_eh).

---
## 7. Computation specification
- *Track traps.* From the WP5 §3.4 partition tables (end states labelled by class c, WP7-T §5.4): DFT charge-transition levels E^tr for each class (HSE or
  GW-corrected, 216–512-atom cells), capture cross sections from the nonradiative multiphonon form (WP4-v3 §6 [6.3], Huang–Rhys inputs) → 𝓃_c^{trk}(r), σ_j.
  Cost ~10⁵ CPU-h per material.
- *Drift–trap Monte Carlo.* Carriers from the WP5 cascade (positions from the track), drift with anisotropic valley transport (Si, Ge at mK), trapping per (E9),
  athermal emission as a parametrised channel, Ramo weighting from field maps (planar, iZIP, CCD pixel). Output: the 𝔵-law, P(N^meas | E_R, r̂_R, F, t_win, T),
  and the joint table P(N^meas, E_stored(t_win) | E_R). 10⁶ events per point; cost ≲ 10³ CPU-h.
- *Windowed partition.* Combine with 𝒦^{rel} (WP7-T §5.4) to tabulate Y_H(t_win) on t_win ∈ {1 μs, 100 μs, 10 ms, 1 s} and the delayed spectrum per class
  with the event criterion for E_thr^det ∈ {0.1, 1, 10, 30} eV. Validation: two-channel data (C7), HPGe multi-shaping (§2.3), 1805.09942 f_DF.

## 8. Exact remaining gaps
- **G-E1.** Ionic targets (NaI, LiF, CaWO₄): excitation-driven defect creation moves energy from E_el to E_st and breaks Theorem E-2 (i); needs excited-state surfaces (WP4, WP5 R3).
- **G-E2.** The size distribution of collective (stress) releases is [C]; (E13) has the structure but no derived avalanche law (WP7-T G-T4, WP5 R4).
- **G-E3.** The sum rule (E6) needs WP7-T path tables built from the same end states as p_st; no code does this yet.
- **G-E4.** NR/ER differences in phonon collection and sensor loss (mode-selective transmission) are unquantified (WP8-R).
- **G-E5.** Track recombination and the e–h plasma phase in NR tracks (WP5 (B2)) decide N_eh vs E_trap^{pr}; (H-E5) fails there.
- **G-E6.** Space-charge nonlinearity of (E9) under exposure, and the athermal emission mechanisms at mK, are unquantified.

## 9. Checks (code/WP7-E/checks.py, 35/35 PASS)
C1 μ-independence of E_pairs + E_trap (neutrality); C2 energy conservation of the 13 zero-field processes and the drift step, reduction to WP5 (W4); C3 release
sum rules (single path, broad λ kernel and its normalisation, released fraction with γ_E, erfc for correlated recombination); C4 Hecht relation and its limits;
C5 bias work = V_b × induced charge (coaxial, planar); C6 compound law, thinning limit = WP5v3-C2a, Poisson thinning; C7 two-channel reconstruction; C8 KP/TRIM
f_DF monotonicity; C9 windowed Y_H, partition of unity, the (W11) trap-energy overstatement; C10 triangular-barrier exponent, field and thermal numbers;
C11 Frenkel-pair counts and the event criterion; C12 STM film power, stored excess, quanta per 10 eV.

---
## Symbols introduced/used (against NOTATION v4 + R9 rows)
| Symbol | Meaning | Status vs NOTATION |
|---|---|---|
| E_hot(t), E_pairs(t), E_trap(t), ℋ_ph(t) | hot-particle, free-pair, trapped-charge, absorber-phonon reservoir energies | **new** |
| E_st(t), E_st^{frz}, E_st^{rel} | configurational stored energy at t (E_st ≡ E_st(t_pr), NOTATION §G); frozen and relaxing parts | **new** (time argument and superscripts) |
| E_stored(t) ≡ E_st(t) + E_trap(t) | total stored energy (the brief's E_stored) | **new** |
| ℋ_pr, ℋ_el, ℋ_nuc | prompt heat (= ℋ of WP5 (W4), the brief's Q_prompt); its electronic and nuclear parts (ℋ_nuc as WP5 §6.1) | ℋ_pr, ℋ_el **new**; ℋ_nuc WP5-v3 |
| E_sig(t), E_sl(t), E_sens = E_sig + E_sl | sensor signal energy; sensor loss; sensor total | **new** |
| 𝒲_bias(t) | cumulative bias work | **new** (W^{scr}, 2W_κ taken) |
| J_{r′→r} | inter-reservoir energy flux | new (local) |
| E^tr_{e,j}, E^tr_{h,j}, n^e_j, n^h_j, 𝓃_j, 𝓃_c^{trk} | trap depths, populations, densities, track trap density | **new** (ε is the dielectric function) |
| σ^e_j, σ^{rec}_j, v_th, V_loc, Γ^{em}_{e,j}, ℓ^tr_{e,h}, v_d | capture and recombination cross sections, thermal speed, local volume, emission rate, trapping length, drift velocity | **new** (λ is the exciton label) |
| U_R(r) | Ramo weighting potential | **new** (φ is the dark photon) |
| 𝔵, 𝔵_i | induced-charge fraction of one pair | **new** (f, ζ, x taken) |
| N^meas(t) ≡ N_eh^{meas} | measured charge in units of e (Ramo-weighted) | **new** (Q is the phonon wavevector) |
| φ_t(s) | single-pair generating function of 𝔵 | new (local) |
| ℛ_q^{del}, ℛ_del, dℛ_bg | delayed-charge rate; delayed-event rate; background term of (E4) | **new** (ℛ_rel stays WP5's) |
| 𝔰_c(t), 𝒯_c, 𝒯_q | reservoir sources per class (WP5's 𝔰_i semantics); transfer maps | 𝔰 as NOTATION; 𝒯 **new** |
| t_win, E_thr^det, P_rel(t_win), ϵ_coll | integration window, detector threshold, released fraction, phonon collection efficiency | **new** (E_th, F, ε taken; ϵ as ϵ_det) |
| 𝐌(t), 𝒫_det(𝐌,t\|𝐍), r_ev | measured vector, detector-stage propagator, event position/track | **new** |
| E_el, E_nuc | event-level electronic and nuclear shares (⟨E_el⟩ = NOTATION E_el) | E_el extended to event level; E_nuc **new** |
| N_trap^{pr}, E_trap^{pr} | captures before t_pr and their energy | **new** (N_trap of NOTATION restricted to t < t_pr) |
| T₁ | freeze-in temperature of a reservoir (WP7-T (4.5)) | WP7-T (source T₁) |
| E_φ, E_Q, y, ε (source, 1803.02903) | total phonon energy, ionization energy, yield, pair energy | source-only (NOTATION §K style) |
| θ_frz, θ_λ, θ_γ, θ_𝒦, θ_law, θ_tr, θ_em, θ_SC, θ_coll, θ_bg,c | nuisances (θ_k family) | **new** (θ_λ, θ_γ as WP7-T §4.6) |
| (H-E1)–(H-E5), (E1)–(E13), (E1′), Theorems E-0…E-3, IF-E1…E8, G-E1…E6, WP7E-C1…C12 | labels (prefix WP7-E per CONVENTIONS §14) | labels |
| used unchanged | ω, q, Λ, S(q,ω;Λ), 𝔇, P_casc, 𝐍, N_eh, ℋ, E_st, E_esc, E_d, N_FP, N_trap, P_FP, 𝔅₀, t_pr, E^ad_0, R_I, E_R, ε_eh, ε_eh^γ, F_eh, F_meas, ϵ_det, Y_H, 𝔊, ϑ, V_bias (= V_b), E_g, E_c, E_v, Δ_BCS, N_qp, η_pb, E_sub, E_excess, p_st, c, 𝒦^{rel}, 𝒫_path, ε_path, Γ_path, λ_ij, P̄_STM, N_FP^{NRT}, E_dam, E_st,1, p_surv, ρ^ph_κ, μ (chemical potential reference, local) | NOTATION / WP5 / WP7-T rows |

## Interface flags
| # | Owner / user | Item | Action |
|---|---|---|---|
| IF-E1 | WP5-v3 | (W4), 𝐍, (W11), §3.2–§3.4, §4, §5, §6.1, §6.3, §6.4, §8 | apply the §5 amendment A-1…A-11 at the next WP5 revision |
| IF-E2 | WP7-T §5 | 𝒦^{rel} normalisation | impose (E6): Σ_path 𝒫_path ε_path = E_st − E_st^{frz} per (c, E_st), from the same end states as p_st (5.1) |
| IF-E3 | WP0-v3 (7.3) | rate to observables | P_casc → (E3) (cascade ⊗ detector stage); dℛ_bg added in (E4); 𝐍 extended by (N_trap^{pr}, E_trap^{pr}, c, r_ev) |
| IF-E4 | WP6-v3 §5.2 | yield/cascade row | add θ_frz, θ_λ, θ_γ, θ_𝒦 (type T), θ_law, θ_tr, θ_em, θ_SC, θ_coll, θ_bg,c; θ_esc = escape only; (E11) ties θ_tr across charge and NTL |
| IF-E5 | WP8 (FOM) | yields | WP8 must use N^meas (E12) and Y_H(t_win) (E8), not N_eh and Y_H = 1, and declare t_win and E_thr^det per detector class |
| IF-E6 | NOTATION | new rows | §Symbols "new" rows; N^meas replaces any "Q" for measured charge |
| IF-E7 | WP8-R | NR/ER collection | ΔE_sl and ϵ_coll(NR)/ϵ_coll(ER) in (E8) are the WP8-R mode-selective quantities |
| IF-E8 | coordinator: SOTA, LIMITS | rows | L20–L22 gain the implicit-defect-assumption sentence (§4); new rows below (numbers provisional) |

## Proposed LIMITS rows
| # | τ / chain (URF) | source formula [FT] | status |
|---|---|---|---|
| L33 | (E9) with frozen emission, uniform field, no space charge → (E10): Hecht charge-collection efficiency | Hecht relation (classic, not on arXiv); used as the 𝔵-law of (E12) | DERIVED (C4) |
| L34 | (E1)–(E2) drift + Ramo–Shockley → (E11): NTL gain eV_bN^meas (complete collection: N_eh eV_b) | 1803.02903 Eq. (1) (E_φ = E_R + E_QeV_b/ε) | DERIVED (C5, C7) |
| L35 | (E12) charge-collection limit: F_meas = ϵ_detF_eh + 1 − ϵ_det (corrects 2004.10709 App. A, as WP5 §6.2(4)) | 2004.10709 App. A | DERIVED (C6) |
| L36 | (E5)–(E6) with 𝒦^{rel} = 0, p_surv = 1: KP/NRT stored energy; f_DF fixes p_surv E_st,1/E_d | 1805.09942 Eq. (4) and TRIM sentence (via WP5 §6.3) | DERIVED (C8) |
| L37 | (E8) with E_stored = ΔE_esc = ΔE_sl = 0 in t_win: unit heat quenching | 2007.14289 (text quoted §4) | DERIVED (truncation stated) |
| L38 | (C7): two-channel recoil scale E_R^rec = ω − E_stored − E_esc and the measured yield | 1803.02903 Eq. (1) | DERIVED |
