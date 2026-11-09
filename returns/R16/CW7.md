# R16 / CW7: closure of the CW7 loose ends — uncertainty, rate assembly, FOM and synthesis; WP8-U/F revisions

Agent CW7, brief briefs/R16/CW7.md; rows LE-19, 21, 152, 153, 154, 155, 156, 157, 159, 160, 176, 177 of state/LOOSE-ENDS.md §2. Read: LOOSE-ENDS §1, §1b,
§3; STATEMENT (deliverable directive 2026-11-01); CONVENTIONS (incl. R13 amendments, [CALC]); NOTATION v4 (greps for every new symbol); CONTROLS;
state/CORRECTIONS.md §0, §17 (no WP8 section); returns/R8/WP6-v3 §1–§7, §11; WP4-v3 §2, §4.3, I12; WP0-v3 G7; returns/R5/O4 §2, §5, d1–d11;
returns/R6/AUDIT §8 (G8, G11); returns/R13/WP8-U, WP8-F; returns/R14/WP8-U-top, WP8-U-table-v2.csv, WP5-AUD §5–§6, GAP-EF; referees/R14/REF-WP8-U-A, -B and
REF-WP8-F-A, -B (cited by LE-19/21). **Deliverables:** this file; returns/R16/WP8-U-v2.md, WP8-U-table-v3.csv and WP8-F-v2.md (LE-19, LE-21: standalone,
with closing tables); code/CW7/ (`checks.py` 32 checks CW7-C1…C32, all PASS, < 2 min; `cascade_gf.py`; `build_v3.py`; `rank.py`; `fetch_ids.py`; `data/`).
No heavy computation was run (no row is compute-in-box); every compute row is closed by a derivation plus a specification. Values computed in checks.py
are [E] from tagged inputs, not [CALC]. Literature: lit.py into literature/papers-CW7/ (PDFs deleted, `.txt` kept for locators); IDs verified (CW7-C32).

## Closure table
| Row | Item | Status | Location |
|---|---|---|---|
| LE-19 | R14 findings on WP8-U | **CLOSED** (WP8-U-v2 + table v3, 25-row closing table) | §1; WP8-U-v2.md §9 |
| LE-21 | R14 findings on WP8-F (+ WP5-AUD F-a…F-i) | **CLOSED** (WP8-F-v2, 43-row closing table; "(prov.)" lifted) | §2; WP8-F-v2.md §9 |
| LE-152 | G8′/OW6-1 halo-independent bound for directional responses | **CLOSED** (theorem: stream representation, dual-cone characterisation, ≤ N_bins atoms; isotropic limit = WP6-v3 (4.2)) | §3 |
| LE-153 | OW6-3 continuous P_casc(N_eh\|Λ;θ) | **CLOSED** (derivation (CW7-153a) + solver + specification) | §4 |
| LE-154 | OW6-6 size of the (P) leakage | **CLOSED** (bound λ_i ≤ (2ω_max/Δ_i)ϱ_−, exact lemma; [E] size) | §5 |
| LE-155 | G-F1 scalar-absorption FOM | **CLOSED** (closed form, sum rule, specification) | §6 |
| LE-156 | G-F4 magnon nuisance row | **CLOSED** (WP6 (5.2) row text, owed) | §7 |
| LE-157 | one-sided SC nuisance, y ≲ 3.5 exclusion | **CLOSED** (WP6 does not carry it: replacement row, owed) | §8 |
| LE-159 | WP8-S ranking synthesis | **CLOSED-AS-EXACT-GAP** (synthesis delivered; missing step: its R×2) | §12 |
| LE-160 | r_mat and profile-vs-envelope convention | **CLOSED** (decision derived; CONVENTIONS row owed) | §9 |
| LE-176 | low-T ε₀ of PbTe, PbS, PbSe, KTaO₃ | **CLOSED** (measured values [FT] for SrTiO₃, KTaO₃, PbTe; PbS, PbSe flagged unusable; FOM insensitivity derived) | §10 |
| LE-177 | cosmogenic activation, ²¹⁰Pb | **CLOSED** (rates [FT] for Si, Ge, NaI, Te; GAP rows with reason + specification; ²¹⁰Pb GAP) | §11 |

---
## 1. LE-19: WP8-U revision
returns/R16/WP8-U-v2.md is the standalone text; returns/R16/WP8-U-table-v3.csv keeps the 2997 v2 rows verbatim and adds 314 rows (CW7-C29). Substantive outcomes:
one screening rule (FAIL needs positive evidence; NiPS₃, h-BN, c-BN, PE move to SURVIVOR-COND); GaAs S2 PASS on full text (4.3 g crystal, 2507.07119 p.1); one
DB vetting rule set V1–V6 (ε₀ dropped for 13 failed-IR runs + InSb, CW7-C30); source disputes adjudicated (2008.08560 n_e CONFIRMED defect; 1910.10716 c_LA
"suspect, pending measured C_ij"; IF-U5 closed, Δ_D = half-gap); ⁷⁶Ge added; bound-only activities printed as "<"; LU3 withdrawn, LU1 merged into L4 as a data
note, LU2/LU4 corrected; renames T_D, τ_life, g_iso, ω_p^{val}, s_spin, c₁^{spin}, screen_S*. The GAP-EF ε_eh/F_eh predictions fill the survivor GAP rows [E].

## 2. LE-21: WP8-F revision
returns/R16/WP8-F-v2.md is the standalone text. Derivations that changed: (1.2′) v-dependent DM tensors use 𝒦^{kin,(2)} with ξ; the NR-1ph per-mass A-free
coefficient is restricted to the light mediator, or m_χ ≲ 0.1–1 MeV for a heavy one, and generalised to Σ_ν(q̂·ê_ν)²/c_ν(q̂); the optical-branch statement
falls and is replaced by the O(q⁴a²) intra-cell term (2205.02250 Eq. (31) [FT]); 2W uses ⟨ω⁻¹⟩; 𝓡_pol carries per-branch log weights; GaAs "≤ 0.144" becomes
0.144–0.153; compound Migdal per mass is Σ_κ𝓠_Mig,κ/A_cell with Z_κ(k) inside (CW7-C20); ALP in B₀ ∝ g²B₀²L_∥/m_φ²; FM magnon edges are quadratic; the
systematics floor carries ΔE_ROI; one C.L. The WP5-AUD rulings F-a…F-i are applied and the "(prov.)" flag is lifted. G-F1 and G-F4 are closed here (§6, §7);
G-F6 (spin-dependent nucleon class) is a new exact gap.

---
## 3. LE-152: halo-independent bounds for directional (anisotropic) responses [D]
**Item.** WP6-v3 (4.5) left G8′ open: for targets beyond hypothesis (I) (anisotropic, P,T-broken, daily modulation) the halo enters through the Radon transform
f̂^{(0)}(q̂,u,t), and a conservative bound "needs a convex characterisation of the Radon transforms of non-negative f_χ with |v| ≤ v_max: a moment problem".
**Idea.** Do not parametrise by f̂; parametrise by the velocity measure itself. Positivity of a measure on a ball is trivially characterised, the rate is linear
in it, and the Radon image of a non-negative measure is automatically admissible. The bound is then a semi-infinite linear program whose optimisers are finite
sums of streams.
**Hypotheses.** (H1) First Born, WP6-v3 (1.7): every bin count is linear in the halo, μ_i = ∫_B 𝔎_i(w)dF(w), F ≥ 0 a finite Borel measure on the compact ball
B = {|w| ≤ v_esc} in the galactic frame (or the lab ball |v| ≤ v_max), with the **stream kernel** 𝔎_i(w) = μ_i[δ_w] continuous on B. For a lab-fixed
crystal (sidereal rotation R(t), Earth velocity v_E(t)),
  𝔎_i(w) = 𝔈_i (ρ_χ/m_χρ_T)⟨∫dω∫d³q/(2π)³ Σ_Λ tr[𝔇(q, v_t)ᵀS(R(t)⁻¹q, ω; Λ)]P(i|Λ) δ(ω − q·v_t + q²/2m_χ)⟩_{t∈bin i},   v_t = w − v_E(t),   (3.1)
so time-binned (sidereal) data stay linear in F (CW7-C4). (H2) Anisotropic (P): 𝔎_i(w) ≥ 0 for all w ∈ B (per-stream positivity; §5 bounds its failure).
(H3) The bounded quantity is linear, Φ[F] = ∫φ dF with φ ≥ 0 continuous (examples below). (H4) Visibility: max_i 𝔎_i(w) > 0 on supp φ.
**Theorem G8′.** (i) *Characterisation of admissible Radon data.* The set 𝒞 = {f̂^{(0)}[F] : F ≥ 0 on B} is a weak-* closed convex cone, and a datum f̂ belongs to 𝒞
iff ⟨g, f̂⟩ ≥ 0 for every continuous g(q̂, u) whose back-projection (R*g)(w) ≡ ∫_{S²}dq̂ g(q̂, q̂·w) is non-negative on B.
(ii) *Bound.* Φ_max ≡ sup{Φ[F] : μ_i[F] ≤ N_i^{up}, i = 1…N_b} = min{Σ_iλ_iN_i^{up} : λ ≥ 0, Σ_iλ_i𝔎_i(w) ≥ φ(w) ∀w ∈ B}.
(iii) *Extreme points.* The supremum is attained by a halo of at most N_b streams, F* = Σ_{k≤N_b} c_kδ_{w_k}.
(iv) *Isotropic limit.* If 𝔎_i depends only on |w| (hypothesis (I)) and φ(w) = Θ(|w| − u₀)/|w| (so Φ = η̃(u₀) per unit normalisation), then for one bin
Φ_max = N_i^{up}/inf_{v≥u₀}𝒜_i(v), 𝒜_i(v) ≡ v𝔎_i(v): exactly the WP6-v3 (4.2) monotone-step-column statement, including its non-monotone case.
**Proof.** (i) All Radon data live on the compact set S²×[−v_esc, v_esc] (q̂·w ∈ [−|w|, |w|]), so R: M(B) → M(S²×[−v_esc, v_esc]) is weak-* continuous (it is the adjoint of g ↦ R*g, which maps continuous functions to continuous functions on compact B).
The probability measures on B form a weak-* compact convex base (Banach–Alaoglu; B compact), so its image is compact and the cone it generates is closed. The
bipolar theorem gives 𝒞 = {f̂ : ⟨g, f̂⟩ ≥ 0 ∀g ∈ 𝒞*}, and g ∈ 𝒞* iff ⟨g, R[δ_w]⟩ = (R*g)(w) ≥ 0 for every w, because the δ_w generate the cone. The
Helgason–Ludwig moment conditions (∫u^kf̂ du a homogeneous degree-k polynomial in q̂) are implied, not imposed. (ii) Weak duality: for feasible F and λ,
Φ[F] = ∫φdF ≤ ∫Σλ_i𝔎_idF ≤ Σλ_iN_i^{up}. Strong duality: restricting F to supp φ loses nothing (𝔎_i ≥ 0, so dropping mass elsewhere keeps
feasibility and Φ), and there its mass is ≤ Σ_iN_i^{up}/κ, κ ≡ min_{supp φ}max_i𝔎_i > 0 by (H4) and compactness; so the feasible set is weak-* compact, Φ
is continuous, and Slater holds (F = 0 is strictly feasible for N^{up} > 0), so the semi-infinite LP has no gap (standard conic duality). (iii) Φ is linear and the
feasible set is compact convex, so the optimum is attained at an extreme point (Bauer); an extreme point of {F ≥ 0 : ∫𝔎_idF ≤ N_i} has support on at most N_b
points (Carathéodory-type theorem for moment sets, Rogosinski 1958 / Winkler 1988 [UNVERIFIED citations]). (iv) A shell at speed v with η-coefficient
η̃_v contributes μ_i = 𝒜_i(v)η̃_v and Φ = η̃_v (CONVENTIONS §8 step decomposition); a single constraint is saturated by the best single atom,
Φ_max = N_i sup_{v≥u₀}1/𝒜_i(v). ∎ Checks: CW7-C1 (isotropic reduction, non-monotone columns), C2 (multi-bin ≤ min of single bins, 3 atoms), C3 (anisotropic
60-direction × 15-speed stream grid: primal = dual, 2 ≤ 4 atoms), C4 (time-averaged kernel linear in F).
**What can be bounded.** (a) η̃(u₀)-type halo values (isotropic or directional, φ = Θ(n̂·w − u₀)); (b) the **maximal rate of a second experiment B** given A's limits,
φ = 𝔎^{B}_j — the conservative comparison of two crystals or of two sidereal orientations; (c) a modulation amplitude (difference of two time-binned kernels,
with φ ≥ 0 replaced by a signed φ: (ii) still holds with weak duality; (iii) still holds). The ER/URF statements of WP6-v3 (4.1)–(4.3) (convexity of −ln ℒ in F,
flat directions = ker 𝒜) carry over with 𝒜 → the stream matrix 𝔎_i(w_k).
**Limits and leading correction.** (I) recovers (4.2); a cubic crystal's first anisotropy is ℓ = 4 (WP6-v3 (1.5)) and enters 𝔎_i at relative size of the ℓ = 4
coefficient of S. If (H2) fails (a truncated S with negative DC pieces), (ii) is no longer an upper bound; the leakage is bounded in §5. The theorem uses no
property of f_χ beyond F ≥ 0 and |w| ≤ v_esc; adding a known speed distribution or isotropy in the galactic frame are extra linear constraints (still an LP).
**Computation specification (G8′ library step; not run).** *What:* the stream matrix 𝔎_i(w_k) on a stream grid and the LP (ii) per m_χ. *Approximation level:* the
library S(q,ω;Λ) at the τ* string of each target (WP6-v3 §7), **q-vector resolved** (no angle average), with the Λ-resolved seeding and P(i|Λ) of §4.
*Method:* for each stream w_k and sidereal phase t, the δ fixes ω on every q-vector of the library grid, so 𝔎_i(w_k) is one sweep over q (cost N_q³ per stream and
phase); stream grid = 768 HEALPix directions × 100 speeds (10 km/s) × 24 phases ≈ 1.8×10⁶ kernel columns × N_q³ ≈ 10⁶ ⇒ ≈ 2×10¹² multiply-adds per m_χ
(a GPU job; on the CPU box only for a coarse 192-direction grid). LP with N_b constraints and ≈ 8×10⁴ variables: HiGHS, seconds. *Convergence:* refine the grid
around the ≤ N_b optimal atoms (exchange/column-generation step; the dual λ certifies optimality: Σλ_i𝔎_i ≥ φ on the refined grid), report Φ_max at two grid
levels. *Pitfalls:* frame (the support constraint |w| ≤ v_esc lives in the galactic frame); per-bin CL (Bonferroni as WP6-v3 (4.2)); (H2) must be tested on the
library (the WP6 gate, now on 𝔎_i ≥ 0); q-grid aliasing of the δ for slow streams. Inputs for the anisotropic S: COMP-PH/COMP-PAER band structures and the WP1
q-resolved ε⁻¹ (qe-rtsc fork layout: `rtsc/bench` stages scf → nscf on the full-zone k grid (no symmetry reduction, `nosym=.true.` so that S(q) is q̂-resolved)
→ response code; `@PSEUDO@` SG15 placeholders).
**Novelty.** Stream (extreme-point) methods for NR halo-independent analysis exist: Feldstein & Kahlhoefer 1403.4606 and Ibarra & Rappelt 1703.09168 [ABS];
angular discretisation for directional NR: Kavanagh 1502.04224 [ABS]. Their application to ER/URF crystal responses with the dual-cone characterisation (i)
replacing the Radon moment problem: priority search not done beyond these [ABS] reads (UNRESOLVED).

## 4. LE-153: the continuous cascade distribution P_casc(N_eh | Λ; θ) [D within GAP-EF (H-EF1)–(H-EF7)]
**Item.** WP6-v3 OW6-3 needs a continuous (not step) P_casc(N_eh|Λ;θ) for (1.7) and the halo-independent columns; GAP-EF derived the first two moments only.
**Derivation.** Under GAP-EF (H-EF1)–(H-EF7) a carrier of type t and kinetic energy x is a Markov branching process: with probability p_t(x) = 1/(1 + R_t(x))
(GAP-EF (EF2)) it impact-ionises into (t, x₁) + (t, x₂) + (t̄, x₃), x₁ + x₂ + x₃ = x − E_g, with density ρ_tρ_tρ_t̄/Φ_t; otherwise it emits ω₀; below θ_iiE_g it
stops. Let N be the number of ii events in its subtree and 𝔊_t(x;z) ≡ E[z^N | t, x]. First-step analysis with independent subtrees (H-EF2) gives

  𝔊_t(x;z) = p_t(x) z ⟨𝔊_t(x₁;z)𝔊_t(x₂;z)𝔊_t̄(x₃;z)⟩ + (1 − p_t(x)) 𝔊_t(x − ω₀;z),   𝔊_t = 1 for x < θ_iiE_g,                  (CW7-153a)

with ⟨·⟩ the (H-EF3) average, a triple convolution [(ρ_t𝔊_t)*(ρ_t𝔊_t)*(ρ_t̄𝔊_t̄)](x − E_g)/Φ_t(x − E_g). Differentiating at z = 1 gives GAP-EF (EF3) for
∂_z𝔊 = E[N] and (EF4) for ∂_z²𝔊 + ∂_z𝔊 = E[N²]. A seed Λ = (c, v, k) with carrier energies x_e = ε_ck − E_CBM, x_h = E_VBM − ε_vk (the primary pair counted once):

  P_casc(N | Λ) = [z^N] z 𝔊_e(x_e;z)𝔊_h(x_h;z),   P(N) = N_z⁻¹Σ_k z_k^{−N}·(·)(z_k),  z_k = e^{2πik/N_z}  (exact for N < N_z).                (CW7-153b)

For an X+ (phonon-assisted) seed the electronic energy is ω − ω_Q: P_casc(N|Λ₊) uses x_e + x_h = ω − ω_Q − E_g (needed by §5).
**Properties [D].** (a) Σ_NP = 1 and P ≥ 0 (𝔊 is a probability generating function on |z| ≤ 1; the recursion maps p.g.f.s to p.g.f.s). (b) Near threshold the
distribution is exactly discrete: for x_e, x_h < θ_iiE_g, P = δ_{N,1}; the first ii channel opens at ω = (1 + θ_ii)E_g on one carrier. (c) For x ≫ E_g,
mean ω/ε_eh + b_N and variance F_ehω/ε_eh (GAP-EF §1.4); [D, sketch] the cumulant generating function ln𝔊 is asymptotically linear in x (renewal), so P tends to a
discretised Gaussian with corrections O(x^{−1/2}) in the skewness — the continuous form WP6 needs. (d) The θ dependence: θ_GW, θ_Z, θ_{R-k} act as one
M-type factor on 𝒜_ph (GAP-EF IF-EF2), i.e. λ_ph → λ_ph(1 + r)^θ in (EF2); θ_𝔉 (O4 d7, GaAs only) is the A-type correction of the first step.
**Checks.** CW7-C5: Σ_NP = 1 to 10⁻¹⁶, P ≥ −2×10⁻¹⁶, and 𝔊′(1), 𝔊″(1) reproduce the moment recursion to 10⁻⁹ (λ_ph = 0 and Si's 3.55). C6: the moment solver
reproduces GAP-EF's λ_ph → 0 values (ε_eh/E_g Richardson 1.5851 vs 1.585; F 0.0811 vs 0.081). C7: Si (λ_ph = 3.55, w₀ = 0.054) F = 0.1147 vs GAP-EF 0.114.
C8: ⟨N|Λ⟩ = 1 + m(x_e) + m(x_h), P(0|Λ) = 0.
**Computation specification (formulated; CPU, code/CW7/cascade_gf.py).** *What:* tables P_casc(N | x_e, x_h; θ) and the library maps Λ ↦ (x_e, x_h) for every
Λ-sector of the response library. *Level:* energy-only reduction (H-EF1) of WP5 (W3), random-k ii (H-EF3), one phonon mode (H-EF4), universal 𝒜_ph (H-EF5) — the
"URF (energy-only)" member of the WP6 discrete yield choice; the ab initio kernels of GAP-EF §5 replace ρ_t, p_t when available (same recursion, iso-energy
kernels 𝒦̄_𝔱). *Inputs:* E_g(T_op), ω₀, a_DOS or the DOS from the band structure, B_h, 𝒜_ph and its θ factor. *Grids:* x step h = E_g/50 with ω₀ on the grid
(GAP-EF: up to 30% phonon-to-gap distortion otherwise), Richardson with h/2 (C6 shows the O(h) error: 1.682/1.634/1.609 at h = 0.04/0.02/0.01); X up to 20E_g,
then matching to the asymptotic Gaussian; N_z = 2^⌈log₂(N̄ + 8σ_N)⌉ (no wrap-around). *Cost:* O(K²N_z) per material and θ value (K = 1000, N_z = 64:
≈ 6×10⁷ complex multiply-adds, seconds); 5 θ values × 27 survivors: minutes on the box. *Pitfalls:* Φ_t = 0 at x = E_g (handled as "no ii"); grid
commensurability of ω₀; aliasing in z; seed-dependence of b_N (one-sided vs symmetric seeds differ, GAP-EF §1.4); T beyond E_g(T) and excitons (GAP-EF GE-3,
GE-4) are outside the model. qe-rtsc is used only upstream (bands, DOS, EPW kernels in the `rtsc/bench` layout of GAP-EF §5).

## 5. LE-154: size of the O(ω_Q/ε_eh) leakage of hypothesis (P) [D]
**Item.** WP6-v3 (4.2): outside the window the DC split seeds X0 (electronic energy ω) and X+ (electronic energy ω − ω_Q) with different P(i|·), and
Σ_ΛPS = P_{X0}S_tot + (P_{X+} − P_{X0})S_{X+} can be negative where the Hadamard finite part of S_{X+} is; "the affected fraction is O(ω_Q/ε_eh), sign unbounded".
**Lemma [D].** For f of bounded variation and h > 0, ∫|f(E) − f(E − h)|dE ≤ h·TV(f). (Write f(E) − f(E − h) = ∫_{E−h}^{E}df and exchange integrals.) CW7-C9.
**Hypothesis (M) stochastic monotonicity.** N_eh(E) is stochastically non-decreasing in the seed electronic energy E. Then P(i|E) = P(N ≥ a|E) − P(N > b|E) is a
difference of two non-decreasing [0,1]-valued functions and TV(P(i|·)) ≤ 2 (= 2 exactly for the step model, CW7-C10). (M) holds for the step model and for
(CW7-153a) when p_t is monotone in x [D, sketch: coupling of two cascades started at x < x′ by giving the excess to one product].
**Bound.** At fixed q, with A^{(n)} the contracted kernels of WP6-v3 (1.4) and P_{X+}(i|ω) = P(i|ω − ω_Q),
  ∫dω [Σ_ΛA^{(n)}P(i|Λ)]_− ≤ ∫dω|P(i|ω) − P(i|ω − ω_Q)|·[A^{(n)}_{X+}]_− ≤ ω_max·TV(P(i|·))·sup_ω[A^{(n)}_{X+}]_− ≤ 2ω_max sup_ω[A^{(n)}_{X+}]_−,   (CW7-154)
because P_{X0}A_tot ≥ 0. Relative to the bin signal μ_i ≃ Δ_i⟨A_tot⟩_i (Δ_i the bin width in ω): **λ_i ≤ (2ω_max/Δ_i)·ϱ_−**, ϱ_− ≡ sup[A_{X+}]_−/⟨A_tot⟩_i.
Multi-phonon X+ seeds replace ω_max by the largest net phonon energy. CW7-C11 checks (CW7-154) on a toy with a negative edge piece.
**Size [E].** Si single-electron bins (Δ_i = ε_eh = 3.749 eV, ω_max = 62.3 meV): 2ω_max/Δ_i = 3.3%, so λ_i ≤ 0.033ϱ_−. ϱ_− is the gate quantity: the negative
part of the DC X+ kernel relative to the total in the bin. By O4 (O4.4) the finite part of a Lorentzian is Γ fp(1/Δ²) with ⟨Γfp, φ⟩ = −2√πΓ for a unit Gaussian,
so ϱ_− is O(Γ/δ) times the X+ share of the bin; O4 §5 gives Γ/δ ≈ 0.02–0.6 for Si outside the edge shell. Inside the shell (Γ/δ ≳ 1) O4 d11 mandates a
Λ-independent P, i.e. sufficient condition (ii) of WP6-v3 (4.2), so (P) holds there by construction. The X+ share near the Si edge is a library output
(COMP-PAER); no number is asserted here.
**Remedy with a stated price [D].** Seeding X0 and X+ of the same pair with the common P_{X0} (sufficient condition (iii)) makes (P) exact; it changes μ_i by
∫(P_{X0} − P_{X+})A_{X+}, bounded by the same right-hand side of (CW7-154) (with |A_{X+}| in place of its negative part). It enters WP6 as an M-type nuisance θ_seedP
with r ≤ (2ω_max/Δ_i)ϱ, ϱ ≡ sup|A_{X+}|/⟨A_tot⟩_i. **Computation specification:** the gate of WP6-v3 (4.2) adds ϱ_− and ϱ per bin, model and m_χ (one extra pass
over the library cells; negligible cost); pitfalls: bins narrower than ω_max (λ_i is then O(ϱ_−), not small), and the edge shell (use d11).

## 6. LE-155: scalar-absorption FOM beyond WP0-v3 (3.5)–(3.6) [D]
**Item.** WP8-F G-F1: "no closed form for the scalar-absorption FOM beyond (3.5)–(3.6) (needs Π_φφ, Π_φA per material)".
**Hypotheses.** A scalar φ with L = −y_φφψ̄_eψ_e, non-relativistic DM-side absorption (k_φ = m_φv, |k_φ| ≈ 10⁻³m_φ), target in its electronic ground state,
first order in y_φ; WP0-v3 (3.5)–(3.6) for Γ.
**Step 1 (operator).** The Foldy–Wouthuysen reduction of ψ̄ψ for a normalised two-spinor gives ψ̄ψ → φ†(1 − p²/2m_e²)φ + O(v⁴), so the target operator is
O_φ(k) = n_e(k) − 𝒯_e(k), 𝒯_e(k) = Σ_i{p_i², e^{ik·r_i}}/(4m_e²) (NOTATION 𝒯_e row). **Step 2 (charge conservation).** On shell n_e(k) = k·j_e(k)/ω, so the n_e amplitude is O(|k|/ω) = O(v_DM ≈ 10⁻³) times a current matrix element and is
screened like a longitudinal photon, whereas the 𝒯_e amplitude, O(⟨p²⟩/m_e²), carries no v_DM suppression. As v_DM → 0 only 𝒯_e survives (WP0-v3's "n_e
suppressed by charge conservation"); the n_e row is the O(k²) correction listed under Limits. **Step 3 (mixing).** The photon-reducible part (3.6) adds
R̃_{𝒯n}v_Cε⁻¹R̃_{n𝒯}; with n = k·j/ω, R̃_{𝒯n} = (k/ω)·R̃_{𝒯j} and v_C = e²/k², so the term is (e²/ω²)k̂·R̃_{𝒯j}ε⁻¹R̃_{j𝒯}·k̂, **finite at k → 0** unless
R̃_{𝒯j}(0,ω) = 0. A scalar–vector cross response at k = 0 is an ℓ = 1 invariant of the point group, which exists only for polar groups (WP6-v3 (1.5), C28).
**Result.**
  Γ_φ = −(y_φ²/m_φ) Im R̃_{𝒯𝒯}(0, m_φ)   (every non-polar point group: Si, Ge, GaAs (T_d), sapphire (D_3d), all cubic and centrosymmetric crystals),     (CW7-155a)
plus the mixing term −(y_φ²e²/m_φ³)Im[k̂·R̃_{𝒯j}ε⁻¹R̃_{j𝒯}·k̂] for polar groups (wurtzite GaN, AlN, ZnO; LiNbO₃-type), and **FOM_φ = −Im R̃_{𝒯𝒯}(0,m_φ)/ρ_T** (> 0 for ω > 0).
In the independent-particle approximation (spin summed)
  Im R⁰_{𝒯𝒯}(0, ω) = −(2π/V) Σ_{cvk} |⟨ck|p²|vk⟩|²/(4m_e⁴) δ(ω − ε_ck + ε_vk),   ⟨c|p²|v⟩ = Σ_m p_cm·p_mv (all bands m, core included).        (CW7-155b)
Compare the ALP–electron row ∝ |p_cv|² and the dark photon ∝ |p_cv|²/ω²|ε|²: the scalar samples second-order momentum matrix elements, hence different selection
rules (𝒯 is even under inversion: c,v of equal parity at Γ, so in Si the direct Γ₂₅′ → Γ₁₅ edge is suppressed and the scalar edge differs from the optical one).
**Sum rule [D].** For eigenstates of H = Σp²/2m_e + V, ⟨i|[[p², V], p²]|i⟩ = 4m_e⟨i|(∇V)²|i⟩ (from p² = 2m_e(H − V), [[p²,V],V] = −2(∇V)², and ⟨i|[X,H]|i⟩ = 0), hence
per electron Σ_f(E_f − E_i)|⟨f|𝒯|i⟩|² = ⟨(∇V)²⟩/(2m_e³), i.e. ∫₀^∞dω ω Im R_{𝒯𝒯} is fixed by ⟨|∇V|²⟩ — **dominated by the core region**. CW7-C12 (sympy, HO
eigenstates n = 0, 1, 2) and C13 (anharmonic 1D, ratio 1.0000).
**Limits.** Free electron gas: 𝒯 is diagonal in plane waves, Im R_{𝒯𝒯}(0, ω > 0) = 0 (no absorption without a lattice, the analogue of the vanishing
Drude-free dark-photon absorption at k = 0). Leading correction: the n_e row at O(k²) with its own screening, and relativistic corrections of the target
(mass-velocity, Darwin) at the same O(v²) in the core.
**Computation specification (qe-rtsc layout; not run).** *What:* Im R⁰_{𝒯𝒯}(0,ω) and (next rung) the RPA+LFE R̃_{𝒯𝒯}. *Level:* τ = IP (then RPA+LFE), n_g = 0,
scr = {ext, LFE}; in-gap absorption needs the n_g = 2 phonon-assisted row (WP3) as for the dark photon. *Method:* `rtsc/bench` stages scf → nscf (dense
k-grid, ≥ 24³ for Si; ≥ 200 bands only if the m-sum route is used) → matrix elements by the **direct kinetic route** ⟨c|p²|v⟩ = Σ_G|k + G|²c*_{c,G}c_{v,G} plus the
PAW one-centre correction Σ_{ij}⟨c|p̃_i⟩(⟨φ_i|p²|φ_j⟩ − ⟨φ̃_i|p²|φ̃_j⟩)⟨p̃_j|v⟩ (the m-sum converges slowly and needs core states). *Key parameters:* ecut (the
kinetic matrix element converges like the total kinetic energy: ecut ≥ 80 Ry for SG15 Si), k-grid, smearing of δ (≤ 20 meV), scissor to the measured E_g(T_op).
*Pitfalls:* (1) norm-conserving pseudo-wavefunctions miss the core oscillations that dominate the sum rule — use PAW reconstruction or an all-electron cross-check
(SG15 is the campaign standard for DFPT; record the deviation); (2) the nonlocal pseudopotential: 𝒯 is the canonical kinetic operator, not m_e²v·v, so do not use
velocity matrix elements i[H,r]; (3) the f-sum is not a check here — use the (CW7-155) sum rule restricted to valence for the valence block; (4) polar targets
need R̃_{𝒯j} (current response) for the mixing term. Cost: Si-size cells, minutes on the box; 10-atom oxides ≈ 1 GPU-hour on the fork.
**Literature.** 2106.12586 (Mitridate, Trickle, Zhang, Zurek) treats scalar absorption via electronic excitations [ABS, ID verified]; its prefactors were not
compared here (structure-level agreement claimed only).

## 7. LE-156: magnon FOM nuisance — the WP6 (5.2) row [D for structure, E for widths]
**Derivation.** LSWT with Holstein–Primakoff to O(S⁰): on a sublattice S^z = S − a†a, S^+ ≈ √(2S)a. With the Bogoliubov vacuum, the local transverse
(one-magnon) weight is W_⊥ = ⟨S^xS^x + S^yS^y⟩ = S(1 + 2ΔS) and the connected longitudinal (two-magnon) weight is W_∥ = ⟨n²⟩ − ⟨n⟩² = ΔS(1 + ΔS)
(same-site ⟨aa⟩ = 0), ΔS = N⁻¹Σ_kv_k² the zero-point spin reduction. Hence the computable two-/one-magnon ratio r_2m = ΔS(1 + ΔS)/(S(1 + 2ΔS)).
Ferromagnet at T = 0: ΔS = 0 and S^{(2m)} ≡ 0 exactly (WP4-v3 [2.4](a)). Simple-cubic AFM: ΔS = 0.078, r_2m = 0.146, 0.049, 0.029 at S = ½, 3/2, 5/2
(CW7-C14) — far below the heuristic 1/(2S), which is 1 (not 0.5) at S = ½ (REF-WP8-F-A F12). The q-resolved S^{(2m)} is WP4-v3 [2.4] (computed, PSD, new support).
**Owed row for WP6-v3 §5.2 (exact text):**
| Magnon reference LSWT (ref = LSWT; HP order) | (a) S^{(2m)}_αβ of WP4-v3 [2.4] in the central value (AFM/ferri; ≡ 0 for a FM at T = 0); (b) residual magnon–magnon interaction and the one-magnon weight renormalisation; (c) magnetic form factor F^{mag}_j(q) (dipole ⟨j₀⟩ + (1 − 2/g_J)⟨j₂⟩) and ligand covalency; (d) Δ_mag, J^{ex} | (a) A (PSD); (b) M on contracted scalars; (c) M; (d) E | (a) a^A median 1, σ_ln = r_2m-weighted 0.5 [E]; (b) r^M = max(ΔS/S, r_2m/(2S)) computed from the Bogoliubov coefficients; (c) σ_ln 0.2 [E]; (d) σ_E = measured-gap error (Cr₂O₃ 0.696, MnO 3.39, NiO 4.76/5.33 meV [FT via WP8-U-TOP]) or the DFT+U spread | material (θ_mag, θ_Fmag) | WP4-v3 [2.1]–[2.4]; CW7 LE-156 |
**Specification.** ΔS, r_2m from the LSWT Bogoliubov coefficients on N_k = 40³ (C14 converged to 10⁻³); S^{(2m)} as WP4-v3 [2.4] (≈ 3×10⁷ operations per q);
F^{mag} from tabulated ⟨j₀⟩, ⟨j₂⟩ (or a DFT+U spin density, qe-rtsc `rtsc/bench` scf with Hubbard U, spin-polarised). Pitfall: YIG is a ferrimagnet with 20 Fe
per cell and gapless acoustic branch — use the full multi-sublattice Bogoliubov transform, not the two-sublattice formula.

## 8. LE-157: superconducting nuisance, one-sided and with the y ≲ 3.5 exclusion [D]
**Check of WP6.** WP6-v3 (5.2) carries "Superconducting targets … first-order screening term in the central value; residual M; ≤ 16% at y = 5, 4% at y = 10" — a
symmetric M type with no exclusion. **It does not carry I12.** **Derivation.** WP4-v3 [4.2′]: L^{BCS} = 𝔤_IL^{nor}[1 − 2(Δ_BCS/qv_F)𝔰_BCS(y)], 𝔰_BCS > 0, so the
correction **lowers** L; its size is uncertain only through the KK cutoff (|δL/L| = 0.16 to ∞ vs 0.07 cut at y = 5; 0.04/0.01 at y = 10; K34). Hence: central =
the cut value (smaller reduction), one-sided M s(θ) = s_c e^{−|θ|σ_BCS(y)}, σ_BCS = |δL/L|_∞ − |δL/L|_cut (0.09 at y = 5, 0.03 at y = 10), θ half-normal; the
profiled limit is never stronger than the θ = 0 one (CW7-C15). Where the expansion fails (2(Δ_BCS/qv_F)𝔰_BCS > 0.3, i.e. y_BCS ≲ 3.5 at q ≈ ω/v_max), the cells
are **masked**: since L ≥ 0 there, dropping a non-negative signal can only weaken a limit, so masking is conservative (C15: 20% masked weakens 2.303/s to 2.88/s).
**Ranking consequence:** the near-threshold 𝓡 of Al/WSi targets falls (the masked cells are exactly the y < 3.5 edge region where 𝔤_I's π/2 step sits).
**Owed replacement row (WP6-v3 §5.2, "Superconducting targets"):**
| Superconducting targets (Al, Nb; WSi without a quoted factor) | L^{BCS} = 𝔤_IL^{nor}[1 − 2(Δ_BCS/qv_F)𝔰_BCS] (WP4-v3 [4.2′], I12), central with the KK cut at ω′ = qv_F | **M one-sided (downward)**, θ_BCS half-normal: s = s_c e^{−\|θ\|σ_BCS(y)} | σ_BCS = 0.09 (y = 5), 0.03 (y = 10), interpolated in ln y; **cells with 2(Δ_BCS/qv_F)𝔰_BCS(y) > 0.3 (y ≲ 3.5 at the kinematic edge) masked from the signal (conservative) until RG9** | material | WP4-v3 K34; CW7 LE-157 |
Specification: tabulate 𝔰_BCS(y) once (K32 quadrature) and the mask per (q, ω) cell of the library; the full-KK route of RG9 (Im ε^{BCS} for ω′ ≳ qv_F) removes the mask.

## 9. LE-160: r_mat and the profile-vs-envelope convention [D]
**Derivation.** Two experiments (or materials) A, B with signals s_A(1 + δ)^{θ_A}, s_B(1 + δ)^{θ_B}, corr(θ_A, θ_B) = r_mat. (a) *Combined limit:* to first order
Var(s_A + s_B) = δ²(s_A² + s_B² + 2r_mats_As_B) is maximal at r_mat = 1, so r_mat = 1 is the conservative choice for any combination (the profiled limit weakens
monotonically in the variance, WP6-v3 (6.2)). (b) *Ranking:* Var ln(FOM_A/FOM_B) = 2δ²(1 − r_mat) (equal widths) is maximal at r_mat = 0, so a ranking claimed
robust must hold at r_mat = 0 (CW7-C16). (c) *Physics:* a nuisance whose template is a method error (𝒳 rung, XC principal components, interim pair-screening
factor, yield-model choice, 𝒜_ph factor) is the same random variable for every material computed with that method; a material input measured independently
(E_g(T_op), ε_eh calibration, ρ_T, c_L) is not. (d) *Profile vs envelope:* WP6-v3 (6.2): profiling costs O(δ²), the envelope O(δ); like for like at δ = 0.5,
envelope/profile ×1.35 (M) and ×1.57 (linear) (WP0-v3 G7). **Decision (owed CONVENTIONS §13 row 29, exact text in "Owed corrections"):** method nuisances
r_mat = 1 (shared θ) across materials computed with the same method and version; material-measured inputs r_mat = 0; combined limits use r_mat = 1 (conservative);
rankings report r_mat = 0 bands with the r_mat = 1 central; headline = profile (WP6-R2), band = envelope (WP6-R3); the choice is written in every library header.

## 10. LE-176: low-temperature ε₀ of the soft-mode crystals
**Data [FT].** SrTiO₃ χ⁻¹ = 5×10⁻⁵ at 0.3 K ⇒ ε₀ ≈ 2×10⁴ (0903.1445 Table 1 p.6); "εr = 23,000 at 4K" quoted, 27,400 extracted (1607.08146 p.1–2). KTaO₃ χ⁻¹ =
2×10⁻⁴ ⇒ ≈ 5×10³ (0903.1445 Table 1 p.6; KTaO₃ is EXCLUDED-RADIO by S4, so WP8-U-TOP's "oxides" scope covers it — check done). PbTe "> 1000" at low T (1003.5140
p.11). PbS, PbSe: no measured low-T value in the texts read — flagged unusable (DFPT 161, 174; soft TO). **Derivation [D].** With Σ_νΔ_ν = 1/ε_∞ − 1/ε₀,
∂ln/∂lnε₀ = ε_∞/(ε₀ − ε_∞): measured vs DFPT moves the POL weight by 2.8% (PbTe), 1.3% (KTaO₃), ≤ 10% (PbS with ε₀ → ∞), and by ×2.75 for SrTiO₃'s failed-run 9.96
(CW7-C17); by LST ε₀ω_T² = ε_∞ω_L², finite as ω_T → 0 (C18), so ω_LO, ε_∞, Z* (the (2.5b) inputs) are regular and the ER window (ω ≫ ω_LO) sees ε_∞ only.
Exception, stated: absorption at m_φ ≈ ω_TO(soft) and any static-screening use (ω < ω_TO) need measured ε(ω, T). Table rows: WP8-U-v2 §4.3 (v3 CSV `eps_0_lowT`).

## 11. LE-177: cosmogenic activation and ²¹⁰Pb
**Derivation [D].** Production at rate R(t) (atoms /(kg·d)) and decay λ: dN/dt = R − λN, so after a history of exposures (R_k for t_k, then cooling t_c)
A = Σ_kR_k(1 − e^{−λt_k})e^{−λ(t_c + later exposures)}; saturation A = R. The sub-keV rate density is 𝓇^{cos}_{<1} = A·f_{<1}/(1 keV) for β emitters (f from the
WP8-U-TOP shape machinery) plus EC lines: "L- and M-shell captures will produce weaker lines at approximately 1 and 0.1 keV" [FT 1607.04560 p.3] (⁶⁵Zn, ⁶⁸Ge
L-lines 1.1–1.3 keV, p.10), i.e. EC nuclides land in the sub-keV ROI through their L/M fractions. Check: Si ³H, R = 124: 0.169 /(kg·d·keV) after 100 d, 11.06 at
saturation (CW7-C19 = WP8-U-TOP). **Data [FT]:** Si ³H/⁷Be/²²Na (2007.10584 p.1); Ge ³H, ⁴⁹V, ⁵⁵Fe, ⁶⁵Zn, ⁶⁸Ge ≥ 74 (1607.04560 p.2, p.21, p.28); NaI eight nuclides
(1411.0106 Table 6 p.15); natTe ACTIVIA saturation activities (1411.5947 Table 4 p.10, calc.); CaWO₄ ¹⁷⁹Ta, ¹⁸¹W, ³H identified (1908.06755 p.4, p.15), rate GAP.
All other survivors: explicit `GAP:cosmo_production` rows; ²¹⁰Pb/U/Th: `GAP:Pb210_U_Th` (process and surface contamination, not a material property; WP8-F §2.8(iii)).
**Computation specification (formulated; not a qe-rtsc quantity).** *What:* R per nuclide at sea level for each survivor composition. *Method:* (i) ACTIVIA
(semi-empirical Silberberg–Tsao cross sections, measured data where present) × the sea-level neutron and proton spectra; (ii) Geant4 (Shielding list) or TALYS
cross sections convolved with the same spectra, for the light nuclides (³H, ⁷Be) where (i) is unreliable. *Inputs:* composition and isotopic abundances (v3
CSV), spectra parameterisation, exposure history. *Validation:* reproduce Si (2007.10584) and Ge (1607.04560) measured rates within their errors before use.
*Cost:* ACTIVIA seconds per material; Geant4 10⁸ primaries ≈ 1–3 CPU-h per material (fits the box; formulated only). *Pitfalls:* ³H and ⁷Be from ACTIVIA can be
off by factors (1607.04560 p.19: models span 27.7–210 nuclei/kg/day for ³H in Ge); ³H out-diffusion in Si (2506.06568) makes the in-crystal activity
history-dependent; EC line fractions (K:L:M) per nuclide are needed for the sub-keV rate.

## 12. LE-159: WP8-S ranking synthesis (after WP8-F-v2, WP8-U-v2, R14, WP5-AUD)
**Method [D for the functionals, E for numbers].** One scalar per channel from WP8-F-v2 §5.1, inputs from WP8-U-table-v3 with the V6 provenance ranking;
pool = SURVIVOR + SURVIVOR-COND after the WP8-U-v2 one-rule change (so NiPS₃, h-BN, c-BN, PE are in; EXCLUDED-RADIO dropped); tiers with δ_rank = 0.2 in ln FOM (ties inside a tier); robust = same tier at r_mat = 0 (§9).
Script code/CW7/rank.py → code/CW7/data/ranking.json (CW7-C31: sapphire ε-route 9.15 vs the FT mode sum 9.40; GaAs 0.147 vs Z* route 0.170).
| Channel (validity) | Scalar | Leading tiers (value) | SURVIVOR leaders | Robustness / caveat |
|---|---|---|---|---|
| ER low-mass edge | m_floor = 2E_g/v_max² (room-T E_g) | PbSe 0.048, PbTe 0.054 MeV; PbS 0.083; Ge 0.19, GaSb 0.21; Si 0.32 (0.333 at low T); GaAs 0.40 | Ge, Si, GaAs | Pb salts: ε_eh ≈ 1.5–1.9 eV [E, outside GAP-EF's validated range], PbTe S4-COND, ε₀ soft (§10) |
| ER rate ceiling | Z/A (f-sum per mass) | 0.40–0.50 for all inorganic survivors (×1.24) | – | not a ranking variable: w_acc⟨1/ω⟩ needs L(q,ω) data (GAP) |
| ER threshold in quanta | ε_eh (measured, else GAP-EF) | Pb salts 1.5–1.9 [E]; GaSb 2.7 [E]; Ge 2.96–3.37; Si 3.75; GaAs 4.2 | Ge, Si, GaAs | near threshold use P(N\|q,ω) (§4) |
| NR-1ph (light mediator; heavy only m_χ ≲ 0.1–1 MeV) | ∝ 1/c_LA (rel. Si) | CsI 6.4; NaI 3.0, Bi₂Se₃ 2.9, PbTe 2.6, PbSe 2.5; PbS, GaSb, TeO₂, CaWO₄ 2.1–2.3 | TeO₂ 2.2, CaWO₄ 2.1, Ge, GaAs 1.8 | DB c_L +20% (GaAs) ≈ one tier; soft lattices pay at the edge (CsI m_min^{ac} 41 keV at 1 meV vs C 3.2) |
| NR-1ph edge | m_min^{ac}(1 meV) | C 3.2; SiC 4.6–4.7; Al₂O₃, AlN 5.3 keV | Al₂O₃ 5.3, Si 6.5 | opposite to the rate ranking (WP8-F-v2 §2.3) |
| POL (A′-mediated) | 𝓘_pol/ρ_T [E, multi-branch] | LiF 19 (Z* route), α-SiO₂ 18.5 (ε route, upper), MgF₂ 11.9, NaF 9.9–10, Al₂O₃ 9.2 (FT 9.4), CaF₂ 8.5, MgO 7.2–7.6 meV cm³/g | LiF, NaF, Al₂O₃ | Z* DFT (10% ⇒ ≈ one tier); weakly polar need ε to 3%; GaAs 0.15 is ×60 below sapphire |
| Migdal (nuclear factor only) | Σ_κZ_ion,κ²/A_cell | LiF 1.93, NiO 1.82, MgF₂ 1.64; α-SiO₂, C, CaF₂, LiAlO₂, Al₂O₃ 1.2–1.5 | LiF, LiAlO₂, Al₂O₃ | × 𝓠_Mig (needs L(k,ω): GAP); Si 0.57, Ge 0.22, GaAs 0.24 |
| MAG | 𝓈_λ⟨\|F^{mag}\|²⟩/ρ_T; Δ_mag | YIG (gapless acoustic, 𝓈 from S_cell/Ω), NiO, MnO, Cr₂O₃ (gaps 0.70–5.3 meV) | none (all COND) | F^{mag} GAP; YIG a_exp GAP |
| Background (S4) | intrinsic sub-keV rate | KTaO₃, InSb excluded; TeO₂, PbTe, ZrTe₅, Cr₂O₃ COND; ³H reducible column | – | cosmogenic GAP outside Si, Ge, NaI, Te (§11) |
**Reading.** (1) No material leads every channel: the ER edge favours narrow gaps (Ge, then Si, GaAs among survivors), the POL and Migdal factors favour light
ionic fluorides and oxides (LiF, NaF, Al₂O₃), the NR-1ph rate favours soft heavy lattices (TeO₂, CaWO₄ among survivors) while its edge favours stiff light ones
(C, SiC, Al₂O₃). (2) Sapphire and LiF are the only survivors in the leading tiers of two channels (POL + Migdal; Al₂O₃ also NR edge). (3) Every Pb-salt lead is
conditional on ε_eh outside the validated cascade range and on soft-mode inputs. (4) Ties: adjacent tiers swap under one DB-accuracy step (c_L 20%, Z* 10%), so
only tier membership two apart is claimed robust.
**Exact remaining gap.** The synthesis is delivered here; the single missing step is its R×2 (hostile referees on this §12 and rank.py), outside CW7's remit.
Secondary inputs that would change tiers: L(q,ω)/ε₂ data pointers (ER w_acc, Migdal 𝓠_Mig), measured C_ij (NR-1ph), measured ω_LO/Z* for oxides (POL), F^{mag} (MAG).

## 13. Checks (code/CW7/checks.py; 32 checks, all PASS)
C1–C4 LE-152; C5–C8 LE-153; C9–C11 LE-154; C12–C13 LE-155; C14 LE-156; C15 LE-157; C16 LE-160; C17–C18 LE-176; C19 LE-177; C20–C27 WP8-F-v2 corrections;
C28–C30 WP8-U-v2 table; C31 LE-159 ranking; C32 arXiv IDs (record written by fetch_ids.py from the arXiv API).

## 14. Literature (all IDs API-verified; PDFs deleted; [FT] = read here)
[FT] 2007.10584, 1607.04560, 1411.0106, 1411.5947, 1908.06755 (cosmogenics); 0903.1445, 1607.08146, 1003.5140 (soft-mode ε₀); 2507.07119 (GaAs mass); 2205.02250
(Eqs. (24)–(33)). Fetched, not used for values: 1503.02095, 2605.16534, 2412.11577, 0902.1497, 1903.09674. [ABS] 1403.4606, 1703.09168, 1502.04224, 2106.12586,
1111.0292. Classic, [UNVERIFIED]: Rogosinski (1958), Winkler (1988), Lyddane–Sachs–Teller (1941).

---
## Symbols introduced/used
| Symbol | Meaning | Status |
|---|---|---|
| 𝔎_i(w) | stream kernel: bin-i count of a unit-density stream at galactic-frame velocity w (3.1) | new (𝔎 free in NOTATION) |
| F, B, Φ, φ, Φ_max, λ_i, N_i^{up}, N_b | halo measure on the ball B; bounded functional and weight; its maximum; dual weights; upper counts; number of bins | new (LE-152 only) |
| 𝒞, R*, g | cone of admissible Radon data; back-projection; test function | new (LE-152 only) |
| 𝔊_t(x;z) | probability generating function of the ii count of a carrier (CW7-153a) | new (G avoided: reciprocal vectors) |
| λ_i, ϱ_−, ϱ, Δ_i, TV(·), θ_seedP | (P) leakage fraction; negative-part and absolute X+ ratios; bin width; total variation; seeding nuisance | new (LE-154); λ_i here ≠ λ_ph |
| O_φ, Γ_φ (scalar), FOM_φ | scalar target operator n_e − 𝒯_e; scalar absorption rate; per-mass FOM | new (Γ_φ is NOTATION's absorbed-boson subscript) |
| ΔS, r_2m, W_⊥, W_∥ | zero-point spin reduction; two-/one-magnon local weight ratio; local weights | new |
| θ_mag, θ_Fmag, θ_BCS, σ_BCS(y) | magnon, form-factor and SC nuisances; SC one-sided width | new (θ_SC is taken by WP7-E) |
| WP8-F-v2 / WP8-U-v2 renames | 𝒦^{kin,(n)}, C_χ, 𝓠_Mig,κ, 𝓈_λ, w^{pol}_ν, T_D, τ_life, g_iso, ω_p^{val}, s_spin, c₁^{spin} | their Symbols sections |
| used | S, R̃, 𝒯_e, 𝔇^{(n)}, A^{(n)}, η, ξ, η̃, 𝒜_ij, f̂^{(n)}, P(i\|Λ), P_casc, Λ, ε_eh, F_eh, λ_ph, 𝒜_ph, ω₀, θ_ii, ρ_t, Φ_t, p_t, b_N, ω_Q, ω_max, Γ, δ, 𝔤_I, 𝔰_BCS, y_BCS, Δ_BCS, r_mat, ε₀, ε_∞, χ (source), ρ_T | NOTATION v4 + R9/WP7 rows |

## Interface flags
| # | Owner | Item | Action |
|---|---|---|---|
| IF-CW7-1 | WP6 | Theorem G8′ (§3), the stream-kernel library step, (H2) gate on 𝔎_i ≥ 0 | adopt as WP6 §4.5 replacement; OW6-1 closed |
| IF-CW7-2 | WP6 / WP5 | (CW7-153a,b) as the continuous P_casc; X+ seeds at ω − ω_Q | adopt; OW6-3 closed at formula + spec level |
| IF-CW7-3 | WP6 | (CW7-154), ϱ_−, ϱ in the gate; θ_seedP | adopt; OW6-6 closed |
| IF-CW7-4 | WP8-F, WP0 | scalar FOM (CW7-155a,b), polar-group mixing | WP0-v3 (3.5)–(3.6) pointer; G-F1 closed |
| IF-CW7-5 | WP6 | magnon row and SC replacement row (§7, §8) | apply to §5.2 |
| IF-CW7-6 | WP4 | 1/(2\|𝐒\|) = 1 at \|𝐒\| = ½ (WP4-v3 §2.1(c), [2.2](b)); r_2m as the computed size | correction |
| IF-CW7-7 | coordinator | CONVENTIONS row 29 (r_mat, profile/envelope); [DB] tag; V1–V6 | apply |
| IF-CW7-8 | referees (R17) | R×2 of WP8-S §12, WP8-U-v2, WP8-F-v2 | launch |
| IF-CW7-9 | COMP-PAER / WP1 | q-vector-resolved S for the stream kernel (no angle average) | library output |

## Owed corrections (target → exact text; no file other than the R16 deliverables was edited)
- **WP6-v3 §4.5 (G8′)** → "G8′ is closed by CW7 Theorem G8′ (returns/R16/CW7.md §3): in the galactic-frame velocity measure F ≥ 0 the counts are linear with stream
  kernels 𝔎_i(w); admissible Radon data form the weak-* closed cone dual to {g : R*g ≥ 0 on B}; the conservative bound is the semi-infinite LP
  sup{∫φdF : ∫𝔎_idF ≤ N_i^{up}} = min{Σλ_iN_i^{up} : Σλ_i𝔎_i ≥ φ}, attained by ≤ N_bins streams; under (I) it reduces to (4.2). Hypothesis: 𝔎_i ≥ 0 (anisotropic (P))."
- **WP6-v3 §11 OW6-1, OW6-3, OW6-6** → append "CLOSED (CW7 §3; §4 (CW7-153a,b); §5 (CW7-154))".
- **WP6-v3 §4.2, sentence "The affected fraction is O(ω_Q/ε_eh) ≈ 1–2% of pairs in Si …, sign unbounded"** → "The negative part is bounded by (CW7-154):
  λ_i ≤ (2ω_max/Δ_i)ϱ_−, ϱ_− ≡ sup[A_{X+}]_−/⟨A_tot⟩_i (stochastic monotonicity of N in E); 3.3%·ϱ_− for Si single-electron bins."
- **WP6-v3 §5.2** → add the magnon row of §7 and replace the "Superconducting targets" row by the row of §8 (texts above); add row "Seeding (P) | P_{X0} for X0 and X+ of the
  same pair | M | r ≤ (2ω_max/Δ_i)ϱ | material | CW7 LE-154".
- **WP4-v3 §2.1(c) and [2.2](b)** → "1/(2|𝐒_j|) ≪ 1: 0.2 for YIG, **1** for |𝐒| = ½ (LSWT qualitative only); the computed local two-/one-magnon ratio is
  r_2m = ΔS(1 + ΔS)/(S(1 + 2ΔS)) (0.146 at S = ½, simple-cubic AFM)".
- **WP0-v3 (3.5)–(3.6), scalar row** → add "closed form: Γ_φ = −(y_φ²/m_φ)Im R̃_{𝒯𝒯}(0,m_φ) for non-polar point groups, plus the R̃_{𝒯j} mixing term for polar groups (CW7-155a,b)".
- **CONVENTIONS §13 new row 29** → "| 29 | r_mat and profile/envelope (2026-11-01) | WP6-v3 default r_mat = 0 (1 as a variant); OW6-4 | **method nuisances (𝒳 rung, XC PCs, pair-screening factor,
  yield model, 𝒜_ph) r_mat = 1 across materials computed with the same method and version; independently measured inputs r_mat = 0; combined limits r_mat = 1;
  rankings r_mat = 0 bands around the r_mat = 1 central; headline = profile (WP6-R2), band = envelope (WP6-R3), declared in the library header.** *Why:* r_mat = 1 maximises
  the variance of a sum (conservative for combination), r_mat = 0 that of a ratio (conservative for ranking) (CW7 §9) |".
- **CONVENTIONS §12 provenance** → add "[DB] database entry with ID and field (JARVIS-DFT `JVASP-n`, MP/Alexandria OPTIMADE, NIST, IAEA); ranks below [FT] and
  [CALC]; DB fields obey the vetting rules V1–V6 of returns/R16/WP8-U-v2.md §1.3".
- **LIMITS L4** → Note/action: "✔ data cross-check (WP8-U-v2): LST on 2008.08560 SiC, ≤ 1.2% with A₁ = ∥, E₁ = ⊥ (CW7-C28)".
- **NOTATION** → rows for the Symbols table above and the WP8 renames (𝒦^{kin,(n)}, C_χ, 𝓠_Mig,κ, 𝓈_λ, w^{pol}_ν, T_D, τ_life, g_iso, ω_p^{val}, s_spin, c₁^{spin}).
- **SOTA (WP8 block)** → "WP8-U/F revised (R16 CW7): WP8-U-v2, table v3, WP8-F-v2 supersede R13; yield rows released; WP8-S synthesis in CW7 §12 (pending R×2)".

## Proposed LIMITS rows (numbers provisional; the coordinator assigns)
| # | Chain (URF) | Source | Validity | Leading correction | Status |
|---|---|---|---|---|---|
| L-H1 | WP6-v3 (1.7) linear in F ≥ 0 → stream kernels → semi-infinite LP; (I) → WP6-v3 (4.2) | 1403.4606, 1703.09168 (NR stream method) [ABS] | first Born; 𝔎_i ≥ 0; compact velocity support | (P) leakage (CW7-154); grid refinement of the atoms | DERIVED (C1–C4) |
| L-H2 | (CW7-153a) p.g.f. recursion → z-derivatives = GAP-EF (EF3)–(EF4); → P_casc(N\|Λ) | GAP-EF §1.3; R&K 2004.10709 (moments) | (H-EF1)–(H-EF7) | θ_{R-k}; T beyond E_g(T); excitons | DERIVED (C5–C8) |
| L-H3 | ψ̄ψ → n_e − 𝒯_e; charge conservation; ℓ = 1 selection → Γ_φ = −(y²/m_φ)Im R̃_{𝒯𝒯}(0,m_φ); sum rule ⟨(∇V)²⟩/(2m_e³) | 2106.12586 (structure) [ABS] | non-polar point groups; first order in y_φ; NR DM | n_e row at O(k²); target relativistic corrections; polar mixing | DERIVED (C12, C13) |
| L-H4 | LSWT/HP to O(S⁰) → W_∥/W_⊥ = ΔS(1 + ΔS)/(S(1 + 2ΔS)) | WP4-v3 [2.4] | T ≪ T_N; two-sublattice AFM | magnon–magnon interaction O(1/S²) | DERIVED (C14) |
