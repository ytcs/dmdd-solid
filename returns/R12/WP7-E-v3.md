# R12 / WP7-E-v3: one time-resolved energy and charge balance per event (yields, defects, delayed release), fix round after the R12 verification

Revision agent, coordinator WP7-E v3 fix round. Supersedes returns/R12/WP7-E-v2.md and returns/R10/WP7-E.md (historical record); this version reads without
them. Inputs: referees/R11/REF-WP7-E-A.md and REF-WP7-E-B.md (cited **R11-A-n**, **R11-B-n**), and the verification reports referees/R12/VER-WP7-E-A.md
(**VA §n**) and VER-WP7-E-B.md (**VB N1–N5**). Architecture: returns/R8/WP0-v3.md ("WP0 (n.m)"); cascade: returns/R8/WP5-v3.md ("WP5 (Wn)"); defect kinetics:
**returns/R12/WP7-T-v2.md** ("WP7-T-v2 (n.m)"; λ convention Δ_ij = ω₀e^{−λ_ij}, Γ ∝ e^{−2λ}; **Theorem T-1** = its (5.3)). CONVENTIONS.md, NOTATION v4 + R9 rows;
state/CORRECTIONS.md read (no owed item touches the sites used).
**Coordinator decision applied (ZPE convention).** Stored energies are **configurational** (E^{conf}_i ≡ E^ad_0(R_i)), as in WP5 (W12) and Theorem T-1. The
zero-point change of occupied basins, ΔZPE, is carried as an explicit correction inside the phonon reservoir ℋ_ph (§1.1).
Checks: `code/WP7-E-v3/checks.py` (sympy + mpmath, **50 checks, all PASS, ≈ 3 s**), cited Ev3-Cn. Each check compares two independent routes: field energy
against a Green's-function pair sum; battery work against field energy plus dissipation; order statistics against the Ramo current; an exact mixture
variance; exact calibration algebra against its series; a 3D diffusion PDE against the capture law; and a master-equation integral against its
telescoped form. Tags per CONVENTIONS §12. Literature [FT] = re-read in full text in literature/papers-WP7-E-v2/ (1803.02903, 1805.09942, 2007.14289,
2202.05097, 2208.02790; PDFs deleted) or quoted through WP5-v3's [FT, CONFIRMED] quotes; arXiv IDs verified against the API. WP5-v3 is not edited (§5 is the
amendment text). **Novelty:** (E1) is a bookkeeping synthesis of WP5 (W4), WP7-T-v2 and standard detector physics, not a new result. The collective-stress
reading of the low-energy excess and the time-law discriminant are credited to 2208.02790. Status: CLAIMED, refereed R×2 (R11), verified (R12), fixed here.

---
## 0. Results at a glance
| # | Item | Result | Tag |
|---|---|---|---|
| 1 | Balance law | (E1): ω + 𝒲_bias = E_hot + E_pairs + E_X + E_trap + E_es + E_st(t) + ℋ_ph + E_esc + E_sig + E_sl; μ = μ_F; **E_X = Σ_excitons(E_g − E_x^b)** is an explicit reservoir; E_st configurational, ΔZPE inside ℋ_ph | D given (H-E1)–(H-E3) |
| 2 | Completeness | E_es = Green's-function energy of uncollected charge (C2a); battery work = ΔE_es + NTL heat with space charge (C2b–d) | D |
| 3 | Two stages | (E3) given (H-E6); additive **per-carrier** deposits plus marks 𝔪 | D given (H-E6) |
| 4 | E_d once | not a ledger entry; ⟨E_st(t)⟩ from (E5); (E6) is an **identity** (Theorem T-1), with ∫∫𝒦^{rel} = ⟨N_hop⟩ | D |
| 5 | Yields | yield models act on E_el; E_st ⊂ E_nuc for creation; carrier-driven reactions are post-prompt | D / E |
| 6 | Charge once | doubly trapped pair: E_g − E^tr_e − E^tr_h; singly trapped: μ_F − E_v − E^tr_h (or E_c − E^tr_e − μ_F) + image | D |
| 7 | NTL | 𝒲_bias = Σ_kV_kΔQ_k (= eV_bN^meas, two electrodes); NTL heat = 𝒲 − ΔE_es. Bias work before t_pr is e ℰ_b v_d t_pr ≈ 4×10⁻⁴–0.25 eV per carrier (C15) | D |
| 8 | Measured charge | F_meas^{obs} = [F_eh⟨m²⟩ + ⟨Var𝔵⟩]/⟨𝔵⟩ + ⟨N_eh⟩Var_r m/⟨𝔵⟩ (C6) | D |
| 9 | **Multiplicative collection** | E_sig = ϵ_prim(ω − D′) + ϵ_NTL·(NTL heat). The O(1) absolute loss cancels in every NR/ER ratio (C7a). η^φ_NR = 1 − δ − d′_NR + κd′_ER, with δ = Δϵ/ϵ and r = ϵ_NTL/ϵ_prim = 1 (C7c). r alone shifts η by g(1−r)(1−y)/(1+rg) (C7b) | D |
| 10 | E_st data bounds (95% C.L.) | ⟨E_st⟩/E_R ≤ 0.055 (Si, 1803.02903); ≤ 0.064 (Ge, 1805.09942); p_surv E_st,1/E_d ≤ 0.21 / 0.20; p_surv ≲ 0.47 / 0.66 (≤ 1% wider with ΔZPE). Conditions: **Δϵ ≥ 0**, r ≥ 1, X_NR ≥ κX_ER, **E_st/ω ≤ 1 − y** | D (algebra) / E (inputs) |
| 11 | Degeneracy | r = 1.14 (NTL phonons collected 14% better than primary phonons) alone reproduces η^φ_NR = 0.952 (C7e); over y = 0.22–0.35 it gives 0.947–0.955 (C7h), inside the band, so current data cannot distinguish r-only from stored energy | D / E |
| 12 | mK charge release | thermal frozen; field emission needs ≈ 1.2×10⁴ V/cm; Poole–Frenkel 2.2 meV at 100 V/cm | D / E |
| 13 | Delayed events | one criterion ϵ_coll ε ≥ E_thr^det; single Frenkel pair needs E_thr ≤ 2.7 eV; pockets visible at 16.3 eV for N_a ≳ 270; TLS give power (total = per-λ × Δλ ≈ 1.4×10⁷ eV) | D / E |
| 14 | LEE data | stress dependence (2208.02790), stress null (2202.05097), single exponential rejected (χ²/dof = 4192/68). Collective reading [C] | C |
| 15 | Literature limits | Lindhard, modified Lindhard (secondary U), R&K, KP (E_dam/2E_d) vs NRT (0.8), TRIM inference UNRESOLVED, QF data as NR/ER ratios; 1803.02903 collection efficiency = a field/model ratio | D |
| 16 | WP5 amendment | A-1…A-16 (§5) | D |
| 17 | Nuisances | 12 θ in WP6 types; θ_tr^{pr} with f₀ = 10⁻³ so the tilt can move (C14) | D (types) |

---
## 1. The balance law

### 1.1 Hypotheses and reservoirs
(H-E1) *Reservoirs.* H_tot = H_C (WP0 (1.1)) + H_sens + H_hold + H_rad + H_bias. Between collisions (WP5 (B1)) ⟨H_tot⟩ for a state of definite quasiparticle
content equals the sum of the reservoir energies below. These include the pair-binding (in E_X) and long-range Coulomb (E_es) parts of V_ee among excited
carriers. Short-range interaction energies are O(Γ/E) and act only during collisions. (H-E2) Contacts are in equilibrium at Fermi level μ_F (band-aligned
gauge), with no injection. 1803.02903 [FT]: carriers "relax to the Fermi level at the electrodes". (H-E3) The bias is external; electrodes are at fixed
potential. (H-E4) Post-prompt processes are Markov in the full microstate. (H-E5) is in §2.3, (H-E6) in §1.4.
| Reservoir | Definition | Value at t_pr | Owner |
|---|---|---|---|
| E_hot(t) | carriers above band edges, hot ions, core holes, undamped plasmons | E_hot(0⁺) = ω − ω_ph(Λ); 0 for t ≥ t_pr (WP5 (H-t)) | WP5 |
| E_pairs(t) | **unbound** free carriers: N_e^f(E_c − μ_F) + N_h^f(μ_F − E_v) | per-carrier sums | WP5 / §2 |
| **E_X(t)** | **excitons and droplets, an explicit reservoir: Σ_{free+bound excitons}(E_g − E_x^b) + Σ_{EHD pairs}(E_g − φ_EHD)** | normally 0 (formation ~ns > t_pr; C13) | §2 |
| E_trap(t) | Σ_j[n^e_j(E_c − E^tr_{e,j} − μ_F) + n^h_j(μ_F − E_v − E^tr_{h,j})] | E_trap^{pr} | WP5 (< t_pr), §2 |
| E_es(t) | ½Σ_{ij}q_iq_jG(r_i, r_j): pair Coulomb, image, space charge; G the Green's function of the grounded electrodes | ≈ 0 | §2 |
| E_st(t) | **configurational**: E^ad_0(R̄(t)) − E^ad_0(R_I(0)) = E^{conf} difference (WP5 (W12), Theorem T-1) | E_st of WP5 §3.2 | WP5, WP7-T-v2 |
| ℋ_ph(t) | phonon energy above the bath, **including the explicit correction ΔZPE(t)**, the zero-point shift of the occupied basins relative to 𝔅₀: ℋ_ph = ℋ_ph^{avail} + ΔZPE(t). Only ℋ_ph^{avail} can reach a sensor | ℋ_pr (WP5 (W4) ℋ; the brief's "Q_prompt") | WP5, WP2 (3.6) |
| E_esc, E_sig, E_sl | escaped; sensor signal; sensor loss | prompt luminescence; 0; 0 | WP5; detector |
| 𝒲_bias(t) | Σ_kV_kΔQ_k | 𝒲_bias(t_pr) = O(N·eℰ_b v_d t_pr) | detector |
**Exciton convention (VB N3, VA §3.1).** E_pairs counts unbound carriers only. A carrier bound in an exciton or droplet carries its full band energy in E_X.
Formation moves (E_c − μ_F) + (μ_F − E_v) = E_g from E_pairs into E_X as E_g − E_x^b, and puts E_x^b into ℋ_ph (C13c). The binding correction appears in
derived formulas as **E_x ≡ −N_XE_x^b ≤ 0** (with N_X the number of bound pairs, droplets counted with φ_EHD), since E_X = N_XE_g + E_x.
**ZPE convention.** ΔZPE (~0.1 eV per point defect [E], i.e. ~1% of E_st,1) is energy of the vibrational ground state, not available to sensors. A hop
i → j releases ε^{conf}_ij + (ΔZPE_i − ΔZPE_j) into ℋ_ph^{avail}. The ZPE terms telescope exactly like the configurational ones (C16). So the observable release
energy is ε_obs = ε^{conf} + δZPE, and (E6) holds for E^{conf} with a separate ZPE sum rule.
**Lemma 1 [D] (C1a,b).** d(E_pairs + E_trap)/dμ = N_h,tot − N_e,tot over uncollected carriers, so only μ = μ_F is physical once a carrier is collected. A
singly trapped hole stores μ_F − E_v − E^tr_h (C1c,d) plus its image energy σ²z′(d − z′)/2d for a planar sheet (C2e).
*Names.* E_dep ≡ ω; E_stored ≡ E_st + E_trap + E_es^{trap}; E_sensor-loss ≡ E_sl.

### 1.2 Statement and proof
  ω + 𝒲_bias(t) = E_hot + E_pairs + E_X + E_trap + E_es + E_st(t) + ℋ_ph + E_esc + E_sig + E_sl     (all t ≥ 0).                                         (E1)

  dE_r/dt = Σ_{r′}J_{r′→r}, J antisymmetric;   d𝒲_bias/dt = Σ_kV_k dQ_k/dt = (NTL power into ℋ_ph) + dE_es/dt.                                         (E2)

**Theorem E-0 [D given (H-E1)–(H-E4), WP5 (B1)].** (E1) holds in expectation at every t. Event by event it holds for the sampled microstate history,
i.e. for every realisation of the stochastic hop and capture sequence. *Proof.* H_tot is conserved apart from 𝒲_bias = Σ_kV_kΔQ_k. In the electrostatic
sector, field energy = Green's-function pair energy (self-image included) + V²C/2, so E_es is complete there (C2a, against an independent Gauss-law
solution). Under a quasi-static move, battery work = ΔE_es + work on the charge, and at terminal velocity that work is NTL heat (C2b–d). The remaining
processes (§1.3) are short-range quantum transitions, each energy-conserving per vertex. Summing (E2) from E_hot(0⁺) + ℋ_ph(0⁺) = ω gives (E1). ∎ The
substantive content is completeness of the reservoir list, i.e. (H-E1).
*At t_pr, per-carrier form (VA §4 A-1).*

  ω + 𝒲_bias(t_pr) = N_e^f(E_c − μ_F) + N_h^f(μ_F − E_v) + E_X + E_trap^{pr} + E_es + ℋ_pr + E_st + E_esc.                                                    (E1-pr)

Neutrality gives N_e^f + N_e^{tr} = N_h^f + N_h^{tr} (excitons are neutral). With N_eh ≡ N_e^f + N_X (band electrons, bound or not), E_x = −N_XE_x^b and
E_pairs^{unp} ≡ (N_h^f − N_e^f)(μ_F − E_v) (C13a):

  ω − N_eh E_g − E_st − E_esc = ℋ_pr + E_trap^{pr} + E_es + E_pairs^{unp} + E_x − 𝒲_bias(t_pr),   E_pairs^{unp} + E_trap^{pr} μ_F-independent (C13b).          (E1-W4)

**WP5 (W4) is the case with no capture, no exciton, and negligible pre-t_pr bias work.** Pre-t_pr bias work is e ℰ_b v_d t_pr per carrier: 4×10⁻⁴ eV at
4 V/cm and 10⁶ cm/s, up to 0.25 eV at 250 V/cm and saturated 10⁷ cm/s (C15) [E, t_pr = 100 ps]. It is negligible for N_eh but not zero in HV detectors, and is
booked in 𝒲_bias and ℋ_pr (VA §3.5).
*Mean ledger.* ⟨X(t)⟩(q,ω) = Σ_Λw_Λ⟨X(t)⟩_Λ, w_Λ = tr[𝔇ᵀS(q,ω;Λ)]/tr[𝔇ᵀS(q,ω)] (WP0 (7.3)), ⟨X⟩_Λ = Σ_𝐍∫d𝔪 P_casc(𝐍, 𝔪|Λ)⟨X(t)|𝐍, 𝔪⟩_det.   (E1′)

### 1.3 Process ledger (energies relative to μ_F; ℰ_b the bias field)
| Process | From → to | Time scale | Stage |
|---|---|---|---|
| relaxation to band edges | E_hot → E_pairs (per carrier) + ℋ_ph | ≤ t_pr | WP5 (W1)–(W3) |
| exciton / droplet formation | E_pairs (E_g per pair) → E_X (E_g − E_x^b or E_g − φ_EHD) + ℋ_ph (E_x^b or φ_EHD) | ns–μs (zero/low field) | §2 (post-prompt; two-body, outside WP5 (B2)) |
| exciton recombination / dissociation | E_X → ℋ_ph or E_esc (E_g − E_x^b); dissociation reverses formation | ns–μs | §2 |
| capture on level j (deep: multiphonon; shallow: cascade capture) | E_pairs → E_trap + ℋ_ph (E^tr) | ns–ms | §2 (WP5 if < t_pr) |
| emission (athermal at mK) / recombination at a trap | reverse / E_trap + E_pairs → ℋ_ph or E_esc (E_g − E^tr) | frozen–s | §2 |
| drift (also before t_pr) | 𝒲_bias → ℋ_ph (NTL) + E_es | ≥ ps | §2 (E2) |
| collection | E_pairs → ℋ_ph at contact (E_c − μ_F or μ_F − E_v) | μs | §2 |
| lattice hop i → j; stimulated reactions | E_st → ℋ_ph^{avail} (ε^{conf} + δZPE) or E_esc/E_sig; E_trap/E_pairs → ΔE_st (either sign) | 𝒦^{rel}; stimulated | WP7-T-v2 (5.2); §1.5 |
| TLS absorption; phonon into sensor / escape | ℋ_ph → E_st; ℋ_ph^{avail} → E_sig + E_sl / E_esc | Γ₁⁻¹; μs–ms | WP7-T-v2 §2; detector |

### 1.4 Two-stage factorisation [D given (H-E4), (H-E6)]
Additive **per-carrier** deposits (VA §4 A-1): 𝐍 = (N_e^f, N_h^f, N_e^{tr}, N_h^{tr}, E_trap^{pr}, ℋ_pr, E_st, N_FP, E_esc, N_X, E_X). These have energies
(E_c − μ_F), (μ_F − E_v), (E_c − E^tr − μ_F), (μ_F − E_v − E^tr), capture heat E^tr → ℋ, and exciton energy (E_g − E_x^b). "Fully free pair" is not a
per-particle property, since it depends on both siblings' fates, so it is not a deposit. N_eh = N_e^f = N_h^f only without capture. Marks 𝔪 = (𝔠, r_ev,
dℋ_pr/dω_ph(r), cloud geometry); 𝔠 ≡ WP7-T-v2's class c, renamed. (H-E6) *Sufficiency:* 𝒫_det depends on the t_pr microstate only through (𝐍, 𝔪) (residual: G-E9).

  P(𝐌, t | Λ) = Σ_𝐍∫d𝔪 P_casc(𝐍, 𝔪 | Λ) 𝒫_det(𝐌, t | 𝐍, 𝔪);   dℛ/d𝐌 = (ρ_χ/m_χρ_T)∫d³v f_χ∫d³q/(2π)³ Σ_Λ tr[𝔇ᵀS(q,ω_q;Λ)]P(𝐌,t|Λ) + dℛ_bg/d𝐌.   (E3)–(E4)

### 1.5 Consistency conditions
**Theorem E-1 (E_d once) [D].** E_d is absent from (E1). It enters only as the median of P_FP (W10). For the mean (VA §2):

  ⟨E_st(t)⟩ = E_st − ∫_{t_pr}^{t}dt′∫dE E𝒦^{rel}(E, t′ − t_pr | 𝔠, T; Φ_ph, n_car),   ∫_0^{t_obs}dt∫dE E𝒦^{rel} = E_st − ⟨E_st^{unrel}(t_obs)⟩ ≡ E_st^{rel},     (E5)–(E6)

with 𝒦^{rel} the expected hop-event density per seed of WP7-T-v2 (5.2), normalised to **∫∫𝒦^{rel} = ⟨N_hop⟩**, not 1. The single-path Σ𝒫Γe^{−Γt} form is the
one-hop case. **(E6) is an identity, Theorem T-1**, under its conditions: (i) uphill hops included; (ii) one E^{conf} table shared by p_st and the paths;
(iii) photon branch kept in E; **(iv) Σ_iN_i(t) = 1, a closed, linear, single-seed chain**; (v) configurational energies, ΔZPE in ℋ_ph. Consequences of (iv):
in the 3D correlated case the separated-pair state reached with probability 1 − r_c/d must be listed in the chain; uncorrelated (bimolecular) recombination
and the inter-seed reactions of the cooldown and stress reservoirs ((E14) sources (ii)–(iii)) lie outside the per-seed (E6); hence the bimolecular law
(1 + t/t₀)⁻² is not a θ_law option. E_st^{unrel}(t_obs) is the energy unreleased by t_obs (WP7-T-v2 naming; "frozen" means t_obs → ∞). Event by event, E_st(t) is a sampled hop sequence with mean (E5). T-1's telescoping proof holds for time-dependent rates
Γ_ij(t; Φ_ph, n_car), which carry the stimulated channels (stated in WP7-T-v2 (C16b)). Forbidden: (a) subtracting E_d or a per-displacement "energy to
defects" from the heat while also adding the release; (b) adding in-window release to a windowed heat yield; (c) N_FP·E_d as stored energy.
**Theorem E-2 (yields act on the electronic share).** [D] for creation, [E] for the reaction channel. Electron-driven Frenkel-pair creation needs
2E(E + 2m_e)/M_κ ≥ E_d, i.e. E ≈ 0.2 MeV in Si, far above DM secondaries (WP5v3-C11: 0.78 meV transfer at 10 eV). At t_pr,
E_el = (E1-pr electronic terms) and E_nuc = ℋ_nuc + E_st + E_esc^{nuc} (E_esc^{nuc} = 0 by t_pr). Recombination-enhanced and ionization-driven defect
reactions (Kimerling; Watkins; Bourgoin–Corbett [UNVERIFIED]) are a post-prompt cross-channel E_el → ΔE_st inside 𝒦^{rel}(…; n_car) (G-E7). A yield model
maps the electronic seed spectrum to P(N_eh). It is never applied to E_R and then corrected by E_st, and the **secondary**-U complement of 2209.04503 is not
booked in E_el (WP5 §6.1(5)). Ionic targets: G-E1.
**Theorem E-3 (trapped charge once) [D].** Doubly trapped pair: E_g − E^tr_e − E^tr_h. Singly trapped hole (electron collected): μ_F − E_v − E^tr_h + E_es^{img}. Singly
trapped electron: E_c − E^tr_e − μ_F + E_es^{img}. WP5 (W11)'s ⟨N_trap⟩E_g is exact only in the doubly trapped shallow-level limit. A trap removes its
remaining Ramo fraction from N^meas and from 𝒲_bias (E11). Captures before t_pr are in P_casc, later ones in 𝒫_det.

### 1.6 Windows, collection and the windowed heat quenching [D]
Released fractions P_rel(t_win): single path 1 − e^{−Γt}; broad λ [ln(Γ_max t) + γ_E]/ln(Γ_max/Γ_min) (C3a,b); 1D correlated recombination erfc(d/√(4D_diff t))
→ 1 (C3c); 3D (r_c/d)erfc((d − r_c)/√(4D_diff t)) → r_c/d (C3d,e).
**Multiplicative collection (VB N1).** The sensor sees phonons, not deficits. With D′ ≡ E_stored(t_win) + ΔZPE(t_win) + E_esc the **pre-sensor** deficit (small;
ΔZPE^{ER} = 0, and ΔZPE is the part of ℋ_ph that no sensor can absorb, §1.1) and
ϵ_prim, ϵ_NTL the fractions of primary and NTL phonon energy that become signal (O(0.1–0.3): the 70–90% absolute loss lives here, not in D′):

  E_sig = ϵ_prim^{(NR/ER)}(ω − D′) + ϵ_NTL·(NTL heat),   ϵ_prim^{NR} ≡ ϵ_prim^{ER}(1 − δ),  δ ≡ Δϵ/ϵ ≡ (ϵ_prim^{ER} − ϵ_prim^{NR})/ϵ_prim^{ER},  r ≡ ϵ_NTL/ϵ_prim^{ER}.    (E7)

The quantity in E_sl is the absolute loss (1 − ϵ)·(phonon energy). It cancels in every NR/ER ratio (C7a). Zero field:

  Y_H(t_win) = (1 − δ)(ω − D′_NR)/(ω − D′_ER) = 1 − δ − [⟨E_st^{unrel}(t_obs)⟩ + ⟨E_st^{rel}⟩(1 − P_rel) + ⟨ΔE_trap⟩ + ⟨ΔE_es^{trap}⟩ + ⟨ΔZPE(t_win)⟩ + ⟨ΔE_esc⟩]/ω + O(d′², δd′, δ²),   (E8)

with d′ ≡ D′/ω small, so the first-order form is controlled (C9a). Δ = NR − ER. ΔE_trap may be negative: an ER has more pairs at equal ω (C9b). NTL mode:
Y_H^{NTL} = [(1 − δ)(ω − D′_NR) + rgyω]/[(ω − D′_ER) + rgω], g = eV_b/ε, which equals (1 + yg)/(1 + g) at zero deficits and r = 1 (C9c). Y_H rises with t_win
in the E_st^{rel} term only.

---
## 2. Charge: trapping, release, measured charge

### 2.1 Trap kinetics at mK [D for structure; E for numbers]
  dn^e_j/dt = σ^e_j(u_car)u_car n_e^f(𝓃_j − n^e_j) − Γ^{em}_{e,j}n^e_j − σ^{rec}_j u_car n_h^f n^e_j   (and e ↔ h),                                              (E9)

with u_car the actual carrier speed, coupled to drift in ℰ_b and to Poisson with the trapped charge (this is E_es). Capture: deep levels by multiphonon
emission (WP4-v3 §6 [6.3]); shallow Coulombic centres by cascade (Lax/Abakumov-type) capture with speed-dependent σ [UNVERIFIED forms]. Emission at mK:
thermal exponent 1.0×10⁴ (45 meV, 50 mK; C10d), frozen. Field emission needs ℰ_b ≈ 1.2×10⁴ V/cm for exponent 30 (C10a,b), a margin of 10²–10⁴ over
detector fields. Poole–Frenkel lowering is 2.2 meV at 100 V/cm (C10c). What remains is athermal: later-event and NTL phonons, impact ionisation of neutral
centres [UNVERIFIED thresholds], IR flashing (1803.02903 [FT]: "By careful neutralization of ionized trapping sites … with regular exposure to infrared LEDs
('flashing')"), and defect-borne traps. n_j(t) is a history variable, and delayed charge ℛ_q^{del} = Σn_jΓ^{em}_j correlates with prior large depositions.
*Excitons.* At zero or low field, unbound pairs at the edges form free excitons, bind to impurities (bound excitons) or condense into droplets, then
recombine (heat or light) or dissociate. The field-ionisation scale E_x^b/(ea_X) ≈ 4×10⁴ V/cm (C17) far exceeds detector fields. In biased detectors exciton
formation is suppressed instead by drift separation of the pair before binding. Kinetics: §7.

### 2.2 Induced charge and bias work [D]
  ⟨𝔵|z⟩ = (ℓ^tr_e/d)(1 − e^{−(d−z)/ℓ^tr_e}) + (ℓ^tr_h/d)(1 − e^{−z/ℓ^tr_h})   (Hecht; two routes, C4a);   𝒲_bias = Σ_kV_kΔQ_k = eV_bN^meas (two electrodes);   NTL heat = 𝒲_bias − ΔE_es.   (E10)–(E11)

Ramo is exact with space charge (C2c). The dissipated heat differs from 𝒲 by −ΔE_es (C2d), and ΔE_es = 0 over full collection of a pair born neutral. Coax:
C5. For ZIP/iZIP use Σ_kV_kΔQ_k with each electrode's U_R.

### 2.3 The measured-charge observable [D under (H-E5)]
(H-E5) Given (r_ev, 𝔪), carriers drift independently after t_pr (the WP5 (B2) caveat persists in NR tracks, G-E5).

  E[e^{sN^meas}|Λ, 𝔪, t] = Σ_N P_casc(N|Λ, 𝔪)φ_t(s|r_ev)^N;   F_meas^{obs} = [F_eh⟨m²⟩_r + ⟨Var(𝔵|r)⟩_r]/⟨𝔵⟩ + ⟨N_eh⟩Var_r(m)/⟨𝔵⟩,   m(r) ≡ ⟨𝔵|r⟩.            (E12)

C6a checks this against an exact mixture. The last term grows with N_eh. CCD, single position: ϵ_detF_eh + 1 − ϵ_det (C6c).
*Data.* (a) 1803.02903 [FT]: "the ionization collection efficiency for CDMS II silicon detectors operated at ∼4 V/cm is consistent with 100% for nuclear
recoils below 20 keV and gradually decreases for larger energies to ∼75% at 100 keV". The source defines it against a yield parameterisation: "The
ionization collection efficiency assumes the parameterization for y_C from Ref. [30]", built from data "at higher electric fields". **It is therefore
(⟨𝔵⟩_NR(4 V/cm)/⟨𝔵⟩_NR(high field))·(y_true/y_C), a field- and model-dependent ratio, not ⟨𝔵⟩_NR/⟨𝔵⟩_ER** (VB N4, VA §3.3). v2's reading is withdrawn. Its use
here is a one-sided, model-flagged constraint: that product ≥ 0.75 at 100 keV. (b) 2405.10405 [FT, via v1]: window 2–18 µs changes the γ+NR energy by < 2 eV
for 6 of 7 filters at 77 K. This bounds only the NR-minus-ER window dependence there [E].

---
## 3. The observable map

### 3.1 Two-channel reconstruction with multiplicative collection [D]
1803.02903 Eq. (1) [FT]: E_φ = E_R + E_QeV_b/ε. The phonon scale is calibrated on "bulk electron recoils, which should have unity ionization yield". The
paper then fits "an overall phonon collection efficiency for nuclear recoils η^φ_NR = 95.2^{+0.9}_{−0.7}% relative to electron recoils of the same deposited
energy", quoted "at 95% C.L.", over "the 10–100 keV energy range considered here" (²⁵²Cf neutron calibration) [FT]. With (E7), ER calibration of both
channels, and y ≡ E_Q/ω for the NR, the exact algebra (C7) gives:
- η^φ_NR is **independent of the absolute ϵ_prim** (C7a);
- at zero deficit, η₀ = 1 + g(1 − r)(1 − y)/(1 + rg) (C7b);
- at r = 1,

  η^φ_NR = 1 − δ − d′_NR + κd′_ER + O(d′², δ²),   κ = (1 + yg)/(1 + g);   d′_NR − κd′_ER = [E_st + ΔX + (1 − κ)X_ER]/ω   (C7c,d),                       (E13)

where X ≡ E_trap + E_es^{trap} + ΔZPE + E_esc are the non-E_st pre-sensor deficits (ΔZPE^{ER} = 0) and ΔX = X_NR − X_ER. **The (1 − κ)X_ER ≈ 0.36X_ER term was missing in v2** (VA §3.2,
VB N1). y^meas = [⟨𝔵⟩_NR⟨N_eh⟩_NR/(⟨𝔵⟩_ER⟨N_eh⟩_ER)]/η^φ_NR. With g = eV_b/ε = 4/3.82 = 1.047, sourced from 1803.02903 [FT] ("The ionization electrodes were biased to 4 V with respect to the phonon electrodes, creating
an electric field of 4 V/cm"), and y = 0.3 [E], κ = 0.642 (C7f).
**Degeneracy.** r = 1.144 alone, with no stored energy, gives η^φ_NR = 0.952 (C7e). This is the effect the source raises ("may depend … even on the relative
fractions of primary and NTL phonons" [FT]). The datum constrains the combination 1 − η = δ + g(r − 1)(1 − y)/(1 + rg) + d′_NR − κd′_ER, not E_st alone. **Current data cannot distinguish the r-only
explanation (r = 1.144) from stored energy.** At fixed r = 1.144 the shift scales as (1 − y). Over 10–100 keV (y ≈ 0.22–0.35 [E]) it gives η₀ = 0.947–0.955 (C7h),
inside the quoted +0.9/−0.7% band, so the energy dependence does not break the degeneracy at present precision. A sharper η^φ_NR(E_R) measurement would.

### 3.2 Data bounds on E_st [D for the algebra; E for inputs]
**Conditions (stated):** (B-a) Δϵ ≥ 0, i.e. NR primary phonons are collected no better than ER ones; (B-b) r ≥ 1, i.e. NTL phonons are collected no worse
than ER primary phonons; (B-c) X_NR ≥ κX_ER (ΔX + (1 − κ)X_ER ≥ 0), e.g. negligible ER trapping after flashing (X includes ΔZPE, of either sign);
**(B-d) E_st/ω ≤ 1 − y.** (B-d) is needed because, for r ≥ 1 at first order in the deficit, 1 − η − E_st/ω = g(r − 1)[(1 − y) − E_st/ω]/(1 + rg) + (δ, ΔX
terms ≥ 0) (C7g); it is trivially met here (E_st/ω ≲ 0.06 against 1 − y ≈ 0.7). Under (B-a)–(B-d), E_st/ω ≤ 1 − η.
**ΔZPE shift.** If ΔZPE is not cancelled by other X terms, |ΔZPE| ≲ 0.01E_st [E] (~0.1 eV per defect) rescales the bound by ≤ 1%: 0.055 → ≤ 0.056 (Si),
0.064 → ≤ 0.065 (Ge); p_surv E_st,1/E_d ≤ 0.21 / 0.20 (unchanged at two digits); p_surv ≲ 0.48 / 0.67 (C8d). The table quotes the ΔZPE-free values.
| Data | Measured combination | 95% C.L. bound on ⟨E_st⟩/E_R | NRT reading (C8) |
|---|---|---|---|
| 1803.02903, Si ZIP, ~4 V/cm, 10–100 keV: η^φ_NR = 95.2^{+0.9}_{−0.7}% (95% C.L.) | 1 − η as above | ≤ 0.048 + 0.007 = **0.055** | p_surv E_st,1/E_d ≤ 0.055/(0.4·0.65) = **0.21**; p_surv ≲ **0.47** (E_st,1/E_d = 9/20 [E]) |
| 1805.09942, Ge iZIP ~50 mK, ²⁰⁶Pb near 103 keV: f_DF = 1 − (1 − f)/(1 − f_sur) = 6.08 ± 0.18% (surface-ER corrected; uncertainty already inflated ×2.06) | the same NR/ER structure (phonon − Luke), κ ≈ 0.6 [E] | ≤ 0.0608 + 2(0.0018) = **0.064** | ≤ 0.064/(0.4·0.8) = **0.20**; p_surv ≲ **0.66** (6/19.7 [E]) |
The central values (0.048, 0.061) give 0.18/0.19. v2 labelled those as bounds, which was wrong (VB N2) and is corrected here. The two papers attribute
similar deficits to opposite causes, collection (Si) and defects (Ge). The URF shows that both measure δ + (r-term) + d′_NR − κd′_ER and cannot separate them
without IF-E7 (G-E4). 1805.09942 [FT]: its detectors "differ by 2.06 standard deviations" and "were biased with opposite polarities", a hint of ΔX ≠ 0.

### 3.3 Delayed events and the low-energy-excess model
  dℛ_del/dE dt = Σ_𝔠∫dt′𝔰_𝔠(t′)𝒦^{rel}(E, t − t′ | 𝔠, T; Φ_ph, n_car) ⊗ 𝒯_𝔠 + ℛ_q^{del} ⊗ 𝒯_q,                                                                (E14)

with sources (i) event-seeded (p_st of WP7-T-v2 (5.1)), (ii) cooldown-seeded, (iii) stress-seeded, and (iv) trapped charge. Released energies are
ε^{conf} + δZPE. **One visibility criterion:** ϵ_coll ε ≥ E_thr^det (absorber) or ε ≥ E_thr^det (film). Comparator: the Si CPD of 2007.14289 [FT], σ_E = 3.86 eV,
with "The trigger threshold was set at 4.2 σ above the normally-distributed baseline noise level, corresponding to 16.3 eV after calibration" (stated in the
source; v2 wrongly called it a referee reading).
- **(a) TLS give power.** WP7-T (4.5) is per unit λ. The total is (π²/12)P̄_STMVT₁² × Δλ, Δλ = ½ln(Γ_max/Γ_min) ≈ 14, i.e. ≈ 1.4×10⁷ eV for a 100 nm × 1 cm² film
  at T₁ = 1 K (C12a). Power ≈ 0.6 eV/s at 10 d. Quanta ≲ 3×10⁻⁴ eV, so a 10 eV event needs ≥ 10⁴ coherent quanta (C12b).
- **(b) Single Frenkel-pair releases** (≤ E_st,1 ≈ 7–9 eV [UNVERIFIED]) are visible iff E_thr^det ≤ ϵ_coll E_st,1 ≈ 2.7 eV (ϵ_coll = 0.3 [E]); invisible at
  16.3 eV (C11a).
- **(b′) Pocket recrystallisation** (event-seeded, collective; ~N_a × 0.1–0.2 eV [E]) is visible at 16.3 eV for N_a ≳ 270 (C11b), with rate
  ≤ ℛ_NR(keV) × pockets per recoil (G-E8).
- **(c) 10–100 eV events** need collective release. The data are mixed. For a stress origin, 2208.02790 [FT]: "more than two orders of magnitude larger"
  in a glued crystal, "time constant of 6–10 d" in the "3–38 and 30–85 eV" bins. Against, 2202.05097 [FT]: holders "with adjustable stress on the crystal …
  However, none of these tests have shown a significant effect on the magnitude and shape of this low-energy excess", with "the cracking of the epoxy used to
  glue the Ge-NTD on the crystal" as a leading hypothesis; also "Sudden increases were observed at times after warming-up the detectors above 10 K", and RED30
  events "not associated with the creation of electron-hole pairs". Time law, 2208.02790 [FT]: "In the lowest-energy bin in the HS calorimeter, a single
  exponential does not sufficiently describe the time-dependent rate (χ²/(dof) = 4192/68)", and "A sum of exponentials or a power law … may be a more
  appropriate fit". This is consistent with the broad-λ form of (E14), but does not establish it. The reading stays [C] (G-E2).
- **(d) Delayed charge** is ionizing, NTL-quantised and history-correlated.

### 3.4 Which detector types see which terms [D]
| Type | ℋ_pr | E_g of pairs | E_X | N^meas | E_st deficit | E_trap (μ_F) | E_es | releases | delayed charge | film |
|---|---|---|---|---|---|---|---|---|---|---|
| zero-field phonon calorimeter (Si/Ge CPD, CRESST, KID) | yes | recombination heat | excitons form, E_g − E_x^b returned as heat or light | no | (E8) | ΔE_trap (doubly trapped) | small | events iff ϵε ≥ E_thr | no | direct |
| NTL / HV phonon | yes | yes | suppressed by drift | ×eV_b | yes | ΔE_trap incl. singly trapped + lost NTL | 𝒲 − ΔE_es | no NTL gain | NTL-quantised | yes |
| heat + ionization (CDMS II, EDELWEISS) | yes | yes | low | yes | in (E13) | in (E13), y^meas | yes | heat only | charge | yes |
| charge only (HPGe, skipper CCD) | no | no | lost to the charge if not dissociated | yes | no | through 𝔵 | via field | radiative or > E_g only | single carriers | no |
| scintillating (light) | via heat | luminescence in E_sig/E_esc | exciton luminescence | no | heat | afterglow | — | heat | afterglow | yes |
| SC absorber / qubit | yes | N_qpΔ_BCS ((W13), absorber case) | — | no | as calorimeter | — | — | yes | — | dominant |

---
## 4. Literature limits and implicit defect assumptions [D for limits]
**L20 Lindhard / modified Lindhard.** 2001.06503 Eqs. (3)–(7), 2209.04503 Eq. (2) [FT, CONFIRMED in WP5 §6.1]. 2001.06503 [FT]: "when atomic binding energies
can be safely neglected"; "a cut-off at an energy equal to twice the assumed binding energy"; Table I "Dislocation 36" / "23" eV. *Implicit:* U = 0 ⇒ E_st = 0;
QF blind to the ℋ_nuc/E_st split; 𝔵 = 1, E_trap = 0. *Modified:* each **secondary** displacement stores U permanently (𝒦^{rel} = 0) and, by complement, books it
electronic; the primary's u is in ν̄. The 2u cut-off merges E_d (threshold) and E_st (energy).
**L21 R&K** (2004.10709 [FT, CONFIRMED]; App. A misprint CONFIRMED). *Implicit:* E_st = 0 (ER creation), 𝔵 = 1, CCD thinning.
**L22 Kinchin–Pease / NRT / TRIM.** Kinchin–Pease N_FP = E_dam/2E_d; NRT adds 0.8 (Norgett–Robinson–Torrens). *Implicit:* p_surv = 1, 𝒦^{rel} ≡ 0, fixed E_st,1.
NRT f_DF ≈ p_surv·0.4(E_dam/E_R)E_st,1/E_d decreases with E_d at fixed E_st,1 (C8a). TRIM's per-displacement energy is not stated in 1805.09942 ("systematic
error does not include modeling imperfections in Geant4 and TRIM" [FT]), so that inference is **UNRESOLVED**. In dense Pb cascades NRT and p_surv are
ill-defined, and the URF uses MD ⟨E_st⟩. The measured f_DF is the (E13)-type NR/ER deficit (§3.2).
**Measured quenching data.** (a) Si two-channel (1803.02903): measures η^φ_NR (§3.1–§3.2). Its "ionization collection efficiency" is a field/model ratio
(§2.3a). (b) Ge charge-only 254 eV_nr (2405.10405 [FT, via v1]: 64 ± 8 eV_ee, "greater than the 14% predicted by the Lindhard model"; γ/X-line calibration):
the measured QF is (⟨𝔵⟩_NR/⟨𝔵⟩_ER)·QF_created at 77 K. (c) 2007.14289 [FT]: heat QF "assumed to be unity for this work. Though measurements … have not been made
for Si, similar work has been undertaken for Ge, where the heat quenching factor was shown to be very close to unity". *Implicit:* δ = 0, D′_NR = D′_ER (and
r = 1 in NTL mode). The Si two-channel datum constrains the corresponding combination at 4.8%.

---
## 5. Amendment to WP5-v3 (exact text; WP5-v3 not edited)
**A-1. §1.2 (W3), (W4).** In (W3) add the cascade type "trapped on level j", with capture kernel 𝒦_cap (WP7-E-v3 (E9) for t < t_pr: cascade capture for
shallow Coulombic levels, multiphonon for deep ones). Use **per-carrier** additive deposits, each carrier deposited **once**, by its state at t_pr. A
carrier at the band edge is non-absorbing until t_pr. If still free at t_pr it deposits (N_e^f += 1, energy E_c − μ_F) or (N_h^f += 1, μ_F − E_v). If captured
before t_pr it deposits only (N_e^{tr} += 1, E_trap^{pr} += E_c − E^tr_e − μ_F, ℋ += E^tr_e), and likewise for holes, with no N_e^f deposit and no E_g or exciton
term for that carrier. Exciton and droplet
formation are two-body processes outside (B2). They are post-prompt (formation times ≳ ns > t_pr) and enter the explicit reservoir E_X = Σ(E_g − E_x^b) of
WP7-E-v3 (E1). After (W4) insert: "(W4) holds with no capture, no exciton and negligible bias work before t_pr. In general ω + 𝒲_bias(t_pr) =
N_e^f(E_c − μ_F) + N_h^f(μ_F − E_v) + E_X + E_trap^{pr} + E_es + ℋ + E_st + E_esc (WP7-E-v3 (E1-pr)); N_eh = N_e^f = N_h^f only without capture."
**A-2. §1.2, 𝐍:** "𝐍 = (N_e^f, N_h^f, N_e^{tr}, N_h^{tr}, E_trap^{pr}, ℋ, E_st, N_FP, E_esc, N_X, E_X) (additive). The class 𝔠, r_ev, dℋ/dω_ph(r) and the cloud
geometry are marks of P_casc(𝐍, 𝔪|Λ) (WP7-E-v3 §1.4, (H-E6))."
**A-3. §3.2 "Stored energy", keep** "E_st = E^ad_0(R_final) − E^ad_0(R_I(0))" (configurational, = E^{conf} difference, as (W12)) **and append:** "The zero-point shift
ΔZPE of the final basin is a correction inside the phonon reservoir, not part of E_st; hop i → j releases ε^{conf}_ij + ΔZPE_i − ΔZPE_j to phonons. The mean
evolution is ⟨E_st(t)⟩ = E_st − ∫E𝒦^{rel}, with ∫_0^{t_obs}∫E𝒦^{rel} = E_st − ⟨E_st^{unrel}(t_obs)⟩ and ∫∫𝒦^{rel} = ⟨N_hop⟩ (Theorem T-1; WP7-E-v3 (E5)–(E6)). E_d
enters only through P_FP (W10)."
**A-4. §3.4, replace (W11) and the sentence after it by:** "Y_H(t_win) ≡ (NR heat signal)/(ER heat signal) at equal deposited energy. With multiplicative
collection E_sig = ϵ_prim(ω − D′) + ϵ_NTL·(NTL heat), where D′ ≡ E_st(t_win) + E_trap(t_win) + E_es^{trap} + ΔZPE(t_win) + E_esc is the pre-sensor deficit (ΔZPE in ℋ_ph but not sensor-absorbable; ΔZPE^{ER} = 0) and
δ ≡ (ϵ_prim^{ER} − ϵ_prim^{NR})/ϵ_prim^{ER}: Y_H = (1 − δ)(ω − D′_NR)/(ω − D′_ER) = 1 − δ − [⟨E_st^{unrel}(t_obs)⟩ + ⟨E_st^{rel}⟩(1 − P_rel(t_win)) + ⟨ΔE_trap⟩ + ⟨ΔE_es^{trap}⟩
+ ⟨ΔZPE(t_win)⟩ + ⟨ΔE_esc⟩]/ω (W11). The absolute sensor loss cancels; E_trap is μ_F-referenced (doubly trapped E_g − E^tr_e − E^tr_h; singly trapped μ_F − E_v − E^tr_h or
E_c − E^tr_e − μ_F); ΔE_trap may be negative. NTL mode: [(1 − δ)(ω − D′_NR) + rgyω]/[(ω − D′_ER) + rgω], r = ϵ_NTL/ϵ_prim^{ER}, g = eV_b/ε. Unit heat quenching
(2007.14289) is δ = 0, D′_NR = D′_ER; the Si two-channel datum η^φ_NR = 0.952 (1803.02903) constrains δ + g(r − 1)(1 − y)/(1 + rg) + (D′_NR − κD′_ER)/ω = 0.048."
**A-5. §3.3, append:** "N^meas = Σ_i𝔵_i (WP7-E-v3 (E12)). QF comparisons use ⟨𝔵⟩_NR/⟨𝔵⟩_ER. Trapping after t_pr is a detector-stage effect; captures before t_pr are in
P_casc (A-1). 1803.02903's 'ionization collection efficiency' is a ratio to a higher-field yield model, not ⟨𝔵⟩_NR/⟨𝔵⟩_ER."
**A-6. §4, (W12):** "⊗ (detector response)" → "⊗ 𝒯_𝔠(E → E^meas), an event iff ϵ_coll ε ≥ E_thr^det, ε = ε^{conf} + δZPE (WP7-E-v3 (E14))". Append: "Single
Frenkel-pair releases and TLS quanta are sub-threshold for E_thr^det > 3 eV. Pocket recrystallisation is collective, event-seeded and can exceed 10 eV. Below
T_× use WP7-T-v2 rates."
**A-7. §5, after (W13):** "(i) Superconducting absorber: E_sub, E_excess are absorber ℋ_ph and E_esc is E_esc of WP7-E-v3 (E1). (ii) A sensor film (ω → phonon
energy entering the film): E_sig = Δ_BCSN_qp, E_sl = E_sub + E_excess + E_esc(film); the film's 1 − η_pb is part of the multiplicative ϵ of (E7)."
**A-8. §6.1 step 4, append:** "(F) Implicit: Lindhard U = 0 ⇒ E_st = 0; 𝔵 = 1, E_trap = 0; in 2209.04503 the **secondary** U is frozen stored energy booked electronic
by complement; the primary's u is in ν̄."
**A-9. §6.3 step 4, append:** "N_FP^{NRT} carries NRT's 0.8 (Kinchin–Pease: E_dam/2E_d). The measured f_DF (1805.09942) is an NR/ER phonon-minus-Luke deficit at the
surface: δ + (r-term) + (D′_NR − κD′_ER)/ω, containing E_st, ΔE_trap (polarity-dependent), surface ΔE_esc and the collection terms. It bounds p_surv E_st,1/E_d ≤ 0.20
(95% C.L.) only under Δϵ ≥ 0, r ≥ 1, X_NR ≥ κX_ER (X including ΔZPE) and E_st/ω ≤ 1 − y. TRIM's per-displacement energy is not stated (UNRESOLVED)."
**A-10. §6.4 "Validity", replace** "carriers to thermalise at the band edges with no trapping before counting, no photon escape, and E_st = 0 (ER)" **by**
"carriers to thermalise at the band edges, with no capture, no exciton formation and negligible bias work before t_pr, no photon escape, and E_st = 0 (ER);
otherwise (W14) uses ℋ_eff = ℋ + E_trap^{pr} + E_es + E_pairs^{unp} + E_x − 𝒲_bias(t_pr) in place of ℋ, with N_eh = N_e^f + N_X, E_x = −N_XE_x^b ≤ 0 and
E_pairs^{unp} = (N_h^f − N_e^f)(μ_F − E_v) (WP7-E-v3 (E1-W4), C13a). (W14) concerns created pairs. The reported Fano factor is
F_meas^{obs} = [F_eh⟨m²⟩ + ⟨Var𝔵⟩]/⟨𝔵⟩ + ⟨N_eh⟩Var_r⟨𝔵|r⟩/⟨𝔵⟩ (WP7-E-v3 (E12)), which reduces to ϵ_detF_eh + 1 − ϵ_det for single-position charge collection".
**A-11. §8:** replace the θ_esc row by "θ_esc | escape only | M | per detector" and add "θ_tr^{pr} | prompt capture fraction | T on the two-point measure,
f₀ = 10⁻³, ψ = ln 10.09 (1% at θ = 1) | per material and field", plus the WP7-E-v3 §6 rows.
**A-12. §1.2 (B3), replace** "An NTL drift field adds a deterministic drift term." **by** "A drift field does work e ℰ_b v_d t_pr per carrier before t_pr
(≲ 0.25 eV at 250 V/cm, saturated). This is booked in 𝒲_bias and ℋ; the drift is otherwise post-prompt (WP7-E-v3 (E1-pr), (E2), (E11))."
**A-13. §6.4 "Leading URF corrections":** "then trapping (N_trap) and exciton or luminescence escape via (W4)" → "then prompt capture via (W4) as amended (A-1),
and post-prompt trapping, excitons (E_X), induced charge and luminescence escape via WP7-E-v3 (E1), (E8), (E12)".
**A-14. §9 R6:** "enter (W4) and (W11)" → "enter (W4) (prompt capture), (W11) and WP7-E-v3 (E1) (E_X), (E8), (E12)".
**A-15. §14 symbol rows and NOTATION §G "N_trap":** "N_trap → N_e^{tr} + N_h^{tr} counted before t_pr; post-prompt trap populations are n^{e,h}_j (WP7-E-v3)".
**A-16. (W6), replace** "dℛ/d𝐍 = … P_casc(𝐍|Λ)" **by** "dℛ/d𝐌 = … P(𝐌, t|Λ) of WP7-E-v3 (E3), + dℛ_bg/d𝐌", keeping the cascade-level dℛ/d𝐍 with
P_casc(𝐍|Λ) as its t = t_pr marginal (VB minor).

---
## 6. Uncertainty: nuisances (WP6-v3 types; priors stated)
Fractions use **type T on a two-point measure**, f(θ) = f₀e^{θψ}/(f₀e^{θψ} + 1 − f₀) (logistic). It requires f₀ > 0: a tilt cannot move mass onto an empty
point (C14b).
| θ | Object | Type | Prior | Correlation | Source |
|---|---|---|---|---|---|
| θ_unrel | E_st^{rel}/E_st per class | T (two-point) | central from WP7-T-v2 computed Γ on t_obs; ψ per σ_λ = 2 [E] | class, T | WP7-T-v2 §5.2 |
| θ_λ, θ_γ | Γ_path | M | σ_ln = 2σ_λ (σ_λ = 2 [E]); 2σ_γ/γ (0.3 [E]) | material | WP7-T-v2 §4.6 |
| θ_𝒦 | shape of 𝒦^{rel} at fixed sum rules | T (constraints ∫∫𝒦 = ⟨N_hop⟩, ∫∫E𝒦 = E_st^{rel}) | 𝒩(0,1) | class | (E6), T-1 |
| θ_law | {1/t, t^{−3/2} 1D/3D, exp} | Δ | discrete profiling | class | WP7-T-v2 |
| θ_st | ⟨E_st⟩/E_R scale | M | central MD; one-sided data bounds 0.055 (Si), 0.064 (Ge) at 95% C.L. under (B-a)–(B-d) (≤ 1% wider with ΔZPE) | material | §3.2 |
| θ_tr^{pr} | prompt capture fraction | T (two-point) | **f₀ = 10⁻³, ψ = ln 10.09 = 2.31** (1% at θ = 1) [E] (C14a) | material, field | A-11 |
| θ_tr | ℓ^tr_{e,h}, track trap density | M | per-detector calibration; wide σ_ln = 0.5 [E]. 1803.02903's collection efficiency enters only as a one-sided, model-flagged product ≥ 0.75 (100 keV) | detector, flash state | §2.3 |
| θ_em | athermal Γ^{em}_j | M | σ_ln = 2.3 [E] | detector, history | §2.1 |
| θ_SC | field map, E_es | Δ + M | per exposure state | detector | §2.1 |
| θ_coll | δ = Δϵ/ϵ and r = ϵ_NTL/ϵ_prim | M on (1 − δ) and on r | median 1, σ_ln 0.05 each; profiled jointly with θ_st through η^φ_NR (the degenerate direction, C7e) | material–sensor | §3.1, IF-E7 |
| θ_X | exciton formation and recombination fractions | T (two-point) | central from §7 kinetics; f₀ ≥ 10⁻³ | material, field, T | §2.1, §7 |
| θ_bg,𝔠 | background reservoir amplitudes | A | log-normal per run, σ_ln 1 | run | §3.3 |
*Exact constraints.* η^φ_NR fixes δ + g(r − 1)(1 − y)/(1 + rg) + d′_NR − κd′_ER, which ties θ_coll, θ_st, θ_tr and θ_esc. Two windows in Y_H separate E_st^{rel}P_rel.
(E11) ties θ_tr across channels. (E6) is exact under type T and T-1.

---
## 7. Computation specification
- *Traps.* Deep levels: DFT charge-transition levels plus multiphonon capture (WP4-v3 §6 [6.3]). Shallow Coulombic levels: cascade capture with σ(u_car) at mK.
  Track levels per class 𝔠. ~10⁵ CPU-h per material.
- **Exciton/EHD kinetics (VA item 16).** Rate equations for unbound pairs n_eh, free excitons n_X, bound excitons n_BX (per impurity species) and droplets:
  formation dn_X/dt = C_X n_e n_h − n_X/τ_X − (binding to impurities, rate ∝ 𝓃_imp σ_BX) − (dissociation), droplet nucleation above the critical
  density/temperature (Ge, Si phase diagrams [UNVERIFIED values]), Auger recombination of bound excitons, luminescence branching (→ E_esc/E_sig). Field
  dependence: pairs separated by drift faster than the binding time do not form excitons; field ionisation at ≳ 4×10⁴ V/cm (C17). Inputs: capture coefficient
  C_X(T), τ_X, E_x^b, φ_EHD from literature or ab initio exciton calculations (WP1 BSE). G4CMP does not model excitons, so this module is new. Output: the E_X(t)
  and luminescence fraction per event class.
- *Drift–trap transport.* Start from G4CMP (anisotropic valleys, NTL, trapping, impact ionisation, Ramo). Add track traps, history-dependent n_j(t),
  athermal emission, μ_F-referenced E_trap, E_es, the exciton module, depth-resolved 𝔵, and pre-t_pr drift. Output P(N^meas, E_stored(t_win) | E_R, r̂_R, ℰ_b,
  t_win, T). ≲ 10³ CPU-h per set.
- *Collection.* ϵ_prim^{NR/ER} and ϵ_NTL from phonon transport (WP8-R) with the t_pr phonon spectrum (a mark), giving δ and r of (E7).
- *Windowed partition.* With 𝒦^{rel} (WP7-T-v2 §5.5) tabulate Y_H(t_win) and η^φ_NR for t_win ∈ {1 μs, 100 μs, 10 ms, 1 s} and E_thr^det ∈ {0.3, 1, 3, 16} eV.
  Validation: 1803.02903 and 1805.09942. Computable only together with G-E4 and G-E6.

## 8. Exact remaining gaps
- **G-E1** ionic targets (E_el → E_st).
- **G-E2** collective-release size law; stress versus epoxy (2208.02790 vs 2202.05097).
- **G-E3** (now narrowed) T-1 condition (ii): one shared E^{conf} table for p_st and the paths; the ZPE sum rule alongside.
- **G-E4** δ and r (collection) separate E_st from collection in η^φ_NR and f_DF.
- **G-E5** track recombination and the plasma phase.
- **G-E6** athermal emission and the space-charge nonlinearity.
- **G-E7** carrier-driven defect reactions.
- **G-E8** pocket size distribution.
- **G-E9** the (H-E6) residual.
- **G-E10** exciton capture coefficients and droplet thresholds at mK for Si/Ge.

## 9. Checks (code/WP7-E-v3/checks.py, 50/50 PASS)
| Checks | Content |
|---|---|
| C1 | μ_F and singly trapped energy |
| C2 | electrostatics: completeness of E_es, energy theorem with space charge, Ramo, NTL heat ≠ 𝒲, image |
| C3 | release kernels: broad λ, 1D erfc, 3D image solution and r_c/d |
| C4 | Hecht by two routes |
| C5 | coax Ramo |
| C6 | position-mixture variance |
| C7 | multiplicative two-channel algebra: ϵ_prim cancels, η₀(r), first-order (E13), the (1 − κ)X_ER term, r-degeneracy, κ, condition E_st/ω ≤ 1 − y (C7g), y-range of the degeneracy (C7h) |
| C8 | NRT, the 95% C.L. bounds, ΔZPE shift (C8d) |
| C9 | multiplicative Y_H, ΔE_trap sign, NTL ratio |
| C10 | emission numbers |
| C11 | visibility (16.3 eV FT threshold) |
| C12 | STM per-λ vs total |
| C13 | exciton reservoir, (W14) substitution, μ_F independence, formation deposit |
| C14 | θ_tr^{pr} tilt |
| C15 | pre-t_pr bias work |
| C16 | ZPE telescoping on a master equation |
| C17 | exciton field-ionisation scale |

---
## v3 closing table (one row per R12 verification item; R11 items were RESOLVED in v2 per VA §1 and VB §1)
| Item | Defect | Status | Where |
|---|---|---|---|
| VB N1 | additive O(1) sensor loss invalidates the first-order forms and the bound sign | applied: multiplicative (E7); (E8), (E13), A-4 rewritten; Δϵ ≥ 0 (and r ≥ 1, X_NR ≥ κX_ER) stated | §1.6, §3.1–§3.2; C7, C9 |
| VB N2, VA §3.2 | central values labelled as bounds; (1 − κ)D_ER term missing | applied: 0.055/0.064 → 0.21/0.20, p_surv ≲ 0.47/0.66; (1 − κ)X_ER in (E13) | §0, §3.2, §6, A-9, L36–L38; C7d, C8 |
| VB N3, VA §3.1, VA A-1 | exciton E_g unbooked; non-additive N_eh | applied: explicit E_X reservoir; per-carrier deposits; consistent in table, (E1-pr), ledger, A-1 | §1.1–§1.4, A-1, A-2; C13 |
| VB N4, VA §3.3 | 1803.02903 collection efficiency misread | applied + dropped (as θ_tr central value): field/model ratio, one-sided constraint | §2.3a, §4, §6, A-5 |
| VA §3.4, VA A-11 | θ_tr^{pr} with f₀ = 0 cannot move | applied: f₀ = 10⁻³, ψ = ln 10.09 | §6, A-11; C14 |
| VB N5, VA A-10 | (W14) E_x sign, missing E_pairs^{unp}, E_es | applied | A-10, (E1-W4); C13a |
| VA §3.5, A-12 | pre-t_pr bias work not zero | applied | (E1-pr), A-1, A-12; C15 |
| VA §2 (E6 vs T-1) | identity, ⟨N_hop⟩ normalisation, mean, time-dependent rates | applied | §1.5, §6 θ_𝒦, IF-E2, G-E3 |
| VA §2 ΔZPE / coordinator ZPE decision | ΔZPE vs E^{conf} | applied: E_st configurational, ΔZPE inside ℋ_ph, ZPE telescoping | §1.1, A-3, (E14); C16 |
| VA item 16 | excitons absent from §7 | applied | §7, G-E10, θ_X; C17 |
| VB A-16 (minor) | (W6) left-hand side | applied | A-16 |
| VB minor | "²⁵²Cf-resonance" wording | applied: "10–100 keV (²⁵²Cf neutron calibration)" | §3.1–§3.2 |
| VB minor | CPD threshold attribution | applied: 4.2σ = 16.3 eV quoted from 2007.14289 [FT] | §3.3; C11 |
| VA C2e (harmless) | image check only endpoints | stands (the energy itself is checked through C2a) | C2 |
| VER2-A §2 | T-1 condition (iv) not cited | applied: (iv) Σ_iN_i = 1 and its consequences (3D escape state, bimolecular and inter-seed excluded) | §1.5 |
| VER2-A §2 | naming E_st^{frz}(t_obs) | applied: renamed E_st^{unrel}(t_obs); θ_frz → θ_unrel | §1.5, §1.6, A-3, A-4, §6, Symbols |
| VER2-A §2 | IF-E2 time-dependent-rate sub-item | applied: closed (WP7-T-v2 C16b) | §1.5, IF-E2 |
| VER2-A §3.1, VER2-B M1 | ΔZPE missing from D′ | applied: in (E7), (E8), (E13) X, A-4, A-9; ≤ 1% shift on the bounds | §1.6, §3.1–§3.2; C8d |
| VER2-A A-1 | edge carrier double-booked | applied: each carrier deposited once by its t_pr state | A-1 |
| VER2-B | condition E_st/ω ≤ 1 − y | applied as (B-d) | §0, §3.2, A-9, §6, L36, L38; C7g |
| VER2-B | g tag; y-range of the degeneracy | applied: g sourced [FT]; η₀ = 0.947–0.955 for y = 0.22–0.35 | §3.1; C7h |

---
## Symbols introduced/used (against NOTATION v4 + R9 rows)
| Symbol | Meaning | Status |
|---|---|---|
| E_hot, E_pairs, E_X, E_trap, E_es, ℋ_ph, ℋ_ph^{avail}, ℋ_pr, ℋ_el | reservoirs (§1.1); E_es^{trap}, E_es^{img} | **new** |
| E_x ≡ −N_XE_x^b, N_X, φ_EHD | exciton binding correction, bound-pair number, droplet energy per pair | **new** |
| ΔZPE(t), δZPE | zero-point shift of occupied basins (inside ℋ_ph); per-hop change | **new** |
| E_st(t) (configurational), E_st^{unrel}(t_obs), E_st^{rel}, E_stored, ⟨N_hop⟩ | stored energies (unreleased by t_obs, as WP7-T-v2 §5.3; "frozen" E_st^{frz} only for t_obs → ∞); expected hop number | E_st as NOTATION; others **new** / WP7-T-v2 |
| N_e^f, N_h^f, N_e^{tr}, N_h^{tr}, E_pairs^{unp} | per-carrier counts; unpaired free-carrier energy | **new** |
| μ_F, ℰ_b, D_diff, r_c, 𝔠, 𝔪 | contact Fermi level, bias field, diffusion constant, capture radius, class, marks | **new** |
| E_sig, E_sl, 𝒲_bias, V_k, Q_k | signal, sensor loss, bias work, electrode potentials and charges | **new** |
| ϵ_prim^{NR,ER}, ϵ_NTL, δ ≡ Δϵ/ϵ, r, D′, d′, X | multiplicative collection efficiencies, NR/ER difference, NTL/primary ratio, pre-sensor deficit, fraction, non-E_st deficits | **new** |
| E^tr_{e,j}, n^{e,h}_j, 𝓃_j, σ(u_car), u_car, Γ^{em}, ℓ^tr | trap quantities | **new** |
| U_R, 𝔵, m(r), N^meas, φ_t, F_meas^{obs} | induced-charge quantities | **new** |
| η^φ_NR, y, ε, y_C (1803.02903); f_DF, f, f_sur (1805.09942); g ≡ eV_b/ε, κ | source symbols; calibration ratios | source-only / **new** |
| t_win, t_obs, E_thr^det, P_rel, ϵ_coll, ℛ_q^{del}, ℛ_del, dℛ_bg, 𝔰_𝔠, 𝒯_𝔠, 𝒯_q, 𝐌, 𝒫_det | windows, thresholds, delayed rates, transfers, detector stage | **new** |
| C_X, τ_X, n_X, n_BX, σ_BX | exciton kinetics (§7) | **new** |
| θ_unrel, θ_λ, θ_γ, θ_𝒦, θ_law, θ_st, θ_tr^{pr}, θ_tr, θ_em, θ_SC, θ_coll, θ_X, θ_bg,𝔠 | nuisances | **new** |
| (H-E1)–(H-E6), (E1)–(E14), (E1-pr), (E1-W4), (E1′), (B-a)–(B-c), Theorems E-0…E-3, A-1…A-16, IF-E1…E9, G-E1…E10, Ev3-C1…C17 | labels (prefix WP7-E-v3) | labels |
| used unchanged | ω, Λ, S(q,ω;Λ), 𝔇, P_casc, 𝐍, N_eh, ℋ, E_esc, E_d, N_FP, P_FP, 𝔅₀, t_pr, E^ad_0, E^{conf}, E_R, ε_eh, F_eh, ϵ_det, Y_H, E_x^b, E_g, E_c, E_v, Δ_BCS, N_qp, η_pb, p_st, 𝒦^{rel}, Γ_ij, λ_ij, P̄_STM, T₁, N_FP^{NRT}, E_dam, E_st,1, p_surv, V_bias (= V_b) | NOTATION / WP5 / WP7-T-v2 |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-E1 | WP5-v3 | amendment | apply A-1…A-16 |
| IF-E2 | WP7-T-v2 | T-1 | (E6) is an identity under T-1 (i)–(v); time-dependent rates are covered (WP7-T-v2 C16b): closed. Remaining: condition (ii) (one E^{conf} table) and the ZPE sum rule alongside |
| IF-E3 | WP0-v3 (7.3) | rate to observables | (E3) marked law ⊗ 𝒫_det; dℛ_bg |
| IF-E4 | WP6-v3 §5.2 | nuisances | §6 rows; type T two-point with f₀ > 0; θ_coll, θ_st, θ_tr, θ_esc profiled jointly through η^φ_NR |
| IF-E5 | WP8 | yields | N^meas, F_meas^{obs}, Y_H(t_win) and η^φ_NR as NR/ER ratios with multiplicative collection; declare t_win, E_thr^det |
| IF-E6 | NOTATION | rows | §Symbols "new"; N_trap restriction; E_st configurational, ΔZPE in ℋ_ph |
| IF-E7 | WP8-R | δ, r | the collection quantities that separate E_st from collection in η^φ_NR and f_DF |
| IF-E8 | coordinator: LIMITS, SOTA | rows; SOTA | rows below. SOTA: "1803.02903 measures η^φ_NR = 0.952 (95% C.L. band), degenerate between E_st and collection (δ, r)" |
| IF-E9 | WP4-v3 §6 / WP1 | shallow-level cascade capture; exciton parameters (BSE) | owner to be assigned |

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L33 | (E9) frozen emission → (E10) Hecht | K. Hecht, Z. Phys. 77, 235 (1932) [UNVERIFIED, classic] | exponential trapping, uniform field, no emission/diffusion/space charge | athermal emission, diffusion, the (E12) depth term, E_es | DERIVED (C4a) |
| L34 | (E1)–(E2) + Ramo → (E11) | 1803.02903 Eq. (1) [FT] | two electrodes (else Σ_kV_kΔQ_k), terminal drift | space charge (ΔE_es); r ≠ 1 ("need not be identical" [FT]) | DERIVED (C2, C5) |
| L35 | (E12) charge collection: ϵ_detF_eh + 1 − ϵ_det | 2004.10709 (A6)–(A7) [FT, CONFIRMED] | single position, Bernoulli | position term | DERIVED (C6) |
| L36 | (E5)–(E6), 𝒦^{rel} = 0, NRT: f_DF ≈ p_surv·0.4(E_dam/E_R)E_st,1/E_d | 1805.09942 Eq. (4) [FT] | Δϵ ≥ 0, r ≥ 1, X_NR ≥ κX_ER (incl. ΔZPE), E_st/ω ≤ 1 − y; dilute cascades | collection (δ, r), ΔE_trap, surface ΔE_esc; MD ⟨E_st⟩ for dense cascades; bound ≤ 0.20 (95%) | DERIVED (C8) |
| L37 | (E8) with δ = 0, D′_NR = D′_ER: unit heat quenching | 2007.14289 [FT] | E_R below displacement; negligible trapping and collection differences | Si datum: 1 − η^φ_NR = 0.048 (combination of δ, r, E_st, X) | DERIVED (truncation) |
| L38 | (E13): η^φ_NR = 1 − δ − d′_NR + κd′_ER (r = 1); η₀(r) = 1 + g(1−r)(1−y)/(1+rg) | 1803.02903 Eq. (1), η^φ_NR = 95.2^{+0.9}_{−0.7}% (95% C.L.) [FT] | ER calibration at the same field; first order in d′, δ (multiplicative collection); bounds need E_st/ω ≤ 1 − y | r-degeneracy (r = 1.14 alone fits); O(d′²); κ depends on V_b, ε, y | DERIVED (C7) |
