# R16 / CW3-errata (ERR-CW3): verification corrections to returns/R16/CW3.md

Errata agent ERR-CW3, brief briefs/R16/ERR-CW3.md. This addendum is read together with returns/R16/CW3.md (not edited: returns are the record).
Where this file gives replacement text, the merger uses **only** this text. Where it says "unchanged", CW3.md stands as written.
*Read:* returns/R16/CW3.md, referees/R16/VER-CW3.md, CONVENTIONS.md (incl. R8, R13 amendments), NOTATION.md, returns/R8/WP4-v3.md §8 ((G5′), [8.1′]), code/CW3/
(checks.py, fork/). state/CORRECTIONS.md was searched for WP4 (G5′)/[8.1′]/OW4-1 entries before quoting WP4-v3: none. *Literature* (lit.py → literature/papers-ERR-CW3/, PDFs converted to txt and deleted): 1101.2210 [FT] (Eqs. (3)–(5)), 1306.6089 [FT] (Eq. (1) and the
sentence after it), 2501.05504 [FT] (Eqs. (6)–(8)), 2109.08168 v2 [FT] (PDF and HTML equation numbering, Eqs. (2), (3), (9), (12), (15)–(18)).
*Checks:* `python3 -I code/CW3/checks.py` → **45/45 PASS, ≈ 17 s** (28 CW3 checks, tolerances tightened; CW3-C6c and CW3-C11 were vacuous and are rewritten; 17 new checks marked
[ERR], cited CW3-Cn). *Fork inputs:* comments added to code/CW3/fork/{GaAs,Si}-LE76/epw.in (absolute-energy pitfall, V3). No heavy numerics were run.
Units HL, e² = 4πα; tags per CONVENTIONS §12. Everything new here is **CLAIMED** (one return).

---
## 1. Resolution of every non-STANDS verifier item

### 1.1 V9 (FALLS): LE-82 (G5′) "𝔥_off CLOSED [D, upper bound]": withdrawn and replaced by an exact remaining gap
*The verifier is right on both counts (a), (b).* Derivation (replaces the first paragraph of CW3 §1.5, "(G5′) with 𝔥_off computed"):

(a) **Disconnected term.** Take U_qp = 1, |FS⟩ = bare sea ⊗ phonon vacuum, |nk⟩ = c†_{nk}|FS⟩ (n empty). Then
  H_off|nk⟩ = [H_off, c†_{nk}]|FS⟩ + c†_{nk}H_off|FS⟩.
The second term contains a hole and a phonon, the first does not contain a hole, so they are orthogonal. At T = 0 (e–ph part; the e–e part is analogous),
  ‖H_off|nk⟩‖² = ‖H_off|FS⟩‖² + (1/N)Σ_{mν,Q≠0}(1 − f_m)|g_{mnν}(k,Q)|² − (1/N)Σ_{vν,Q≠0}|g_{nvν}(k−Q,Q)|²,     ‖H_off|FS⟩‖² = (1/N)Σ_{k′,Q≠0}Σ_{vc,ν}|g_{cvν}(k′,Q)|² + … ∝ N.     (E9.1)
All sums run over Q ≠ 0. The Q = 0 term (coherent/polaron-shift emission Σ_kg_{nn}(k,0)c†c b†_0) is itself disconnected and extensive. It has the same structure as the
n = m piece of the commutator, so it adds an interference term to (E9.1) without changing the conclusion. The last term of the first equation is the Pauli blocking of sea
processes that would end in (n,k). CW3-C12a checks (E9.1) to 10⁻¹² in an exact Fock-space toy (two bands, N = 3, 4, 5, with g(Q = 0) = 0). CW3-C12b shows ‖H_off|FS⟩‖² ∝ N (ratios 2.00, 2.00 for N = 4 → 8 → 16), while the connected component stays fixed (0.287, 0.287).
Hence 𝔥_off(ψ_b) ≥ ‖H_offψ_b‖/‖ψ_b‖ ~ √N. **(G5′) fails with U_qp = 1, and WP4 [8.1′] is vacuous for it.** The same holds for the true ψ_b = O_b|i⟩
whenever |i⟩ is not an H_d eigenstate: then H_off|i⟩ = (E_i − H_d)|i⟩, and its norm is the √N energy fluctuation of H_d in |i⟩.

(b) **Band mixing.** H_d (number-conserving) contains the one-body e–e correction (Σ_HF − v_xc)_{nn′}(k), so e^{−iH_ds} mixes bands at fixed k. The supremum of the
connected norm over one-QP states at k is therefore λ_max of the matrix
  M^c_{nn′}(k) = (1/N)Σ_{mνQ}(1 − f_m)(2n_{Qν} + 1) g*_{mnν}(k,Q) g_{mn′ν}(k,Q) + Σ^{(2),c}_{ee,nn′}(k)   (the T > 0 factor 2n + 1 is [E]),
not its largest diagonal entry. Since adding the occupied-m terms adds a PSD matrix, λ_max(M^c) ≤ λ_max(M^{FM}), with M^{FM} the Fan–Migdal zeroth-moment matrix
(sum over all m) [D at T = 0, e–ph; CW3-C12c checks M^c_{nn} ≤ M^{FM}_{nn}].

**Corrected statement.** "(G5′) 𝔥_off CLOSED [D, upper bound]" is **withdrawn**. What survives:
- [E] the connected size 𝔥^c_off(k)² ≡ λ_max M^c(k) ≤ λ_max M^{FM}(k). The Al number ≈ 0.2 eV [E] is unchanged (one conduction band, so λ_max = diagonal).
- [D] **Dressed-vacuum lemma** (CW3-C12d). If the reference |i⟩ is an eigenstate of H inside Ran 𝒬_{0,0}, then H_d|i⟩ = 𝒬_{0,0}H|i⟩ = E_i|i⟩, so H_off|i⟩ = 0.
  Then H_off e^{−iH_ds}O_b|i⟩ = e^{−iE_is}[H_off, O_b^d(−s)]|i⟩ with O_b^d(−s) = e^{−iH_ds}O_be^{iH_ds}. Only the connected commutator survives.
- **Exact remaining gap (G5′-c)**, added to the LE-82 exact gaps. Prove D-g (a) with 𝔥_off(ψ_b) replaced by
  𝔥^c(ψ_b) ≡ sup_s‖[H_off, O_b^d(−s)]|i⟩‖/‖O_b|i⟩‖. Three missing steps:
  (i) a dressing U_qp whose vacuum is the exact |i⟩ (this is gap (1), now needed for (a) as well);
  (ii) an N-uniform bound on 𝔥^c(ψ_b) (Lieb–Robinson-type for H_d with unbounded phonon numbers; open);
  (iii) the identification 𝔥^c ≈ λ_max^{1/2}M^c at leading order in g (perturbative, [E]).
- *Spec (replaces the CW3 `g2sum` spec).* EPW on the Wannier manifold: output the band matrix M^c_{nn′}(k) (empty m only) and M^{FM}_{nn′}(k) (all m), plus λ_max of each,
  on a 40³ (Al) fine Q grid at the k-points of interest. Converge λ_max to 5% under Q grid 30³ → 40³ and `degaussw` 0 (no δ: the zeroth moment needs no smearing).
  e–e: Σ^{(2),c} from the RPA W (BerkeleyGW/Yambo, 2p1h with the source-electron leg only). *Pitfall:* do not add the vacuum (k′-sum) term. It is the disconnected piece (E9.1).
  Cost ≈ 10² core-h. The result is [E] until (G5′-c) is proved.

Consequences: IF-CW3-7 is reissued (§2.3). LE-80 (iii) inherits the defect (§1.6). Owed correction 22 is new: WP4 OW4-1 stays open.

### 1.2 V1 (STANDS WITH CORRECTION): LE-77 Υ slip; perturbative caveat
- CW3 §2.1 "Im Υ = −½Σ_fΓ^{(f)}a^{off}_f" → "**Υ(ω) = Σ_f|g_f|²a^{off}_f/(ω − E_f + i0) = Υ^{PV}(ω) − (i/2)Σ_fΓ^{(f)}a^{off}_f**". Here
  Υ^{PV} = PV Σ_f|g_f|²a^{off}_f/(ω − E_f) is smooth at Ẽ and vanishes for a flat continuum. A nonzero Υ^{PV}(Ẽ) redefines ρ → ρ + Υ^{PV}(Ẽ) at O(g²). That shift enters c^F
  only at the next order, so (CW3.1) is unchanged. CW3-C1d checks the flat-continuum value to 8×10⁻⁴ and that the "Im Υ" form fails for complex a^{off}.
- CW3 §2.1 last sentence → "…|c_ν^F| = (Γ^{tot}/δ)(|a^{off}|δ/|ρ|)|sin φ_ν| ≲ 0.3Γ/δ (GaAs worst case; **first order in Γ/δ**, residual O(Γ²/δ²)), so |ΔP| ≲ 0.3Γ/δ.
  The sufficient condition 2max|c^F| ≤ 1 then reads Γ/δ ≲ 1.7. That value lies outside the range of the first-order estimate, so K_ν ≥ 0 is **quoted only for Γ/δ ≤ 0.5 [E]**
  (perturbative; reliable for Γ/δ ≪ 1)."
- The algebra of the bound and positivity is now tested on 2×10⁴ random kernels, including a non-phonon branch (CW3-C11a, b; the old C11 was arithmetic only).
  The bound holds, with max |ΔP|/bound = 0.70; violations of K_b ≥ 0 occur only when 2max|c^F| > 1.

### 1.3 V2 (STANDS WITH CORRECTION): LE-75, hypothesis (P5)
*Gap confirmed* (CW3-C2d). A real symmetric but non-scalar level-shift matrix Ẽ on D(Λ₀) is used, in the Θ-real basis, with the CW3 C2 data and Ẽ = s·diag(1, −1, 0.5, −0.3).
At s = 0.2 (Γ̂ eigenvalues 0.03–0.23), the per-branch Fano weights are ∓3.3×10⁻² against a generic 0.24, and the branch sum is 4×10⁻⁶. A scalar Ẽ = s𝟙 gives 10⁻¹³ (C2e).
*Mechanism, derived [D, commuting case].* If [Ẽ, Γ̂] = 0, take the common real eigenbasis (e_i, γ_i). Then
  X_ij ≡ ∫G†B_bG dω = (B_b)_ij·4π/[(γ_i + γ_j)(1 − iη_ij)],   η_ij ≡ 2(e_i − e_j)/(γ_i + γ_j),
so Im X_ij = (B_b)_ij(4π/(γ_i+γ_j))η_ij/(1 + η_ij²) is antisymmetric and nonzero for a single-branch kernel B_b. For B = Γ̂ = Σ_bB_b it is diagonal, hence real, so the branch sum vanishes. The closed form, the antisymmetry, the zero at η = 0 and the 1/η tail are checked in sympy
(residue and numerical quadrature, CW3-C2g).
The per-branch Fano weight is therefore O(max_ij|η_ij|/(1 + η_ij²)) relative to its generic size. It vanishes both for splittings ≪ Γ and for splittings ≫ Γ. In the second case the
levels are non-degenerate Θ-real seeds, and the theorem applies to each. C2f checks the non-commuting case: the weight decays ∝ 1/s (2.7×10⁻³ at s = 5, 9.5×10⁻⁴ at s = 20).

*Replacement text for CW3 §2.2.* Add after (P4):
"(P5) **the O(g²) level-shift matrix Ẽ on D(Λ₀) is scalar**. Sufficient conditions: one-body self-energies, with D(Λ₀) = D_c(k+q) ⊗ D_v(k) and each D_n an irrep of the group
of its k (a Kramers doublet at general k, or Γ₈ at k = 0), so that Schur's lemma gives Σ_n ∝ 𝟙 on D_n. More generally: [Ẽ, Γ̂] = 0 and every branch kernel diagonal in the common
eigenbasis. Γ̂ itself need not be scalar."
After "per eigen-channel of Γ̂ and in trace. ∎" add:
"Without (P5) only Σ_b𝔉_b = 0 is derived [D]. The per-branch 𝔉_b is O(max|η|/(1 + η²)), with η the level-shift splitting over Γ: [D] for [Ẽ, Γ̂] = 0, [E] (CW3-C2d–f)
otherwise. (P5) fails for e–h phonon-exchange (vertex) self-energies on D and for accidental near-degeneracies within ~Γ. **Tag: [D] under (P1)–(P5).** Si, diamond
(one-body level) [D]; Ge with SOC at one-body level [D]."
*Limits paragraph:* unchanged. The owed corrections 4, 5, 6 and the L-Fano row are reissued with (P5) (§2.2, §2.5).

### 1.4 V3 (STANDS WITH CORRECTION): LE-76, threshold shells and the absolute-energy pitfall
*Replacement for CW3 §2.3 "[E] values now", from "With δ₀ = 0.3 eV:" to the end of the sentence ending "[E]":*
"With δ₀ = 0.3 eV, Γ/δ ≈ 0.01–0.2 holds only for seeds whose ε_ck (and ε_vk) lie farther than 2Γ from every onset of Γ_n. Near an onset, δ_Λ₀ (CW3 definition, which includes the
threshold distance) → 0. For GaAs the Γ–L onset lies at ≈ 0.3 eV above the CBM, exactly where Γ jumps from ≈ 3 meV (LO only) to 20–60 meV. Hence **K_ν ≥ 0 holds for GaAs
outside the d11 shell and outside the onset shells |ε_ck − E_{L,X}| ≲ 2Γ, and the hole analogues (split-off onset at Δ_so ≈ 0.34 eV below the VBM), by the condition Γ/δ ≤ 0.5
[E, perturbative]**. Γ in the shell width is evaluated on the seed's side of the onset (3 meV below, 20–60 meV above). Outside these shells |ΔP| ≲ 0.3Γ/δ ≲ 0.06 [E]. Inside the
d11 and onset shells, only totals and P(N_eh) from the unexpanded Dyson form are quoted."
*Outputs (add):* "the onset-shell mask, built from the computed Γ_n(k) tables (every jump or kink of Γ_n as a function of ε_nk, shell ±2Γ)".
*Pitfalls (add as (6)):* "`fermi_energy` and `dis_froz_max` in fork/{GaAs,Si}-LE76/epw.in (6.0/9.5 and 6.2/9.0 eV) are **absolute** placeholders. Reset them from the
scf/nscf output of the actual pseudopotential set: `fermi_energy` = mid-gap, `dis_froz_max` = CBM + 3 eV, with no more than `nbndsub` bands inside the frozen window at any k.
Otherwise the fsthick window and the frozen manifold are wrong and elecselfen returns the wrong bands without an error." These instructions are now comments in both epw.in files.
The other inputs agree with the text, as the verifier checked.

### 1.5 V6 (STANDS WITH CORRECTION): LE-83, [D] only as q → 0
*Replacement for CW3 §3.3, from "the q → 0 form gives" to "no polarity needed)":* "the q → 0 form gives Ω²/(c_Lq)² = 1 at q* = 18 keV (Si) and 44 keV (GaAs). Both lie above q_BZ,
but the form itself is derived only asymptotically. Hence **1 − ε_e^{-1}(q,0) → ∞ as 1/q² for q → 0 in every solid [D]** (**Si counterexample derived as q → 0**; no
polarity needed). At finite q, the linear dispersion and Z^{(e)}(q) ≈ Z^{(e)}(0) both fail at relative order (qa)². In a monatomic-chain toy the dispersion factor alone gives
1 + (qa)²/12 + …, and π²/4 at the zone edge (CW3-C9e). The fall-off of Z^{(e)}(q) acts in the opposite direction, so the size at q ~ q_BZ is [E]."
*Then:* "At q = 1 keV … [E] ≳ 10²" unchanged. *Consequence (L17), replacement:* "…the GS lattice term dominates as q → 0 [D], is [E] ≳ 10² at q = 1 keV and [E] ≳ 1 for
q > q_BZ…". The owed correction 10, IF-CW3-4 and L17′ are reissued (§2.2, §2.3, §2.5). Check C9d is relabelled: the value 333 at 1 keV is an [E] extrapolation.

### 1.6 V8 (STANDS WITH CORRECTION): LE-80, Theorem D-m
*Add to the hypotheses of CW3 §1.3:* "(M5) the quadratic spin–lattice form is **positive definite**. Goldstone magnons are gapped by the infinitesimal (M2) field h > 0, with the
limit h → 0 taken after N → ∞, and the Q = 0 acoustic modes (rigid translations) are removed by centre-of-mass separation at finite N." Reason: at a zero mode the matrix JH is a
nilpotent Jordan block, so there is no oscillator and no number operator (CW3-C14).
*(ii) replacement tag:* "[D at quadratic order, under (M5)]".
*(iii) replacement:* "[D given U_b, (M5) and a connected (G5′-c) (§1.1 of ERR-CW3), which is open]. With U_b = the quadratic Bogoliubov map, cubic magnon terms a†a†a† acting on
the LSWT vacuum give an extensive disconnected norm, exactly as in §1.1. The bound needs the dressed (interacting) vacuum."
*Closure row and owed correction 8:* reissued (§2.1, §2.2).

### 1.7 V10 (STANDS WITH CORRECTION): LE-82 (3), Dirac running coupling, now derived
*Replacement for CW3 §1.5 (3), from "New [D, sketch, one-loop]" to "marginal [E]":*
"New [D, one-loop]: the Coulomb coupling α̃ = e²/(4πεv) of a 3D Dirac/Weyl semimetal is marginally irrelevant,
  dα̃/dl = −(2(N_D + 1)/3π)α̃²,   α̃(ω) = α̃₀/[1 + (2(N_D + 1)α̃₀/3π)ln(Λ_D/ω)].
The velocity part is +2α̃/3π, from the exchange self-energy (CW3-C13a). The charge part is 2N_Dα̃/3π, i.e. α̃/3π per Weyl node, from the interband static bubble (C13b).
At N_D = 1 this is 1101.2210 Eq. (4), dα/dl = α(Δ_V − 4α/3π), and Eq. (3) gives the velocity term 2α/3π [FT]. At α̃₀ = 0.91, N_D = 1, Λ_D/ω = 10³: **α̃ ≈ 0.25,
α̃² ≈ 0.06** (C13c; CW3's 0.39/0.15 used the charge part only). One loop at α̃₀ ~ 1 is [E] for the benchmark. Γ_qp/ω ~ α̃² ≈ 0.06, so the bin condition is met for
bins ≳ 0.1ω [E]: the conclusion is stronger."
"QED-like" is deleted. N_D counts four-component nodes (N_D = N_W/2).

### 1.8 V13 (STANDS WITH CORRECTION): LE-88 (d) tag
*Replacement for CW3 §4.3 (d):* "(d) For a quasi-free (Gaussian) target, Wick's theorem decomposes the four-point function of bilinears exactly into the disconnected product
S(q₁)S(q₂) plus connected loop terms [D]. The size estimate 'connected terms O(1/N_eff)' is [E] (counting: disconnected ∝ N_eff², connected ∝ N_eff)." Closure row reissued.

### 1.9 V14 (STANDS WITH CORRECTION): LE-89, 1306.6089 convention
I re-read the 1306.6089 sentence [FT, papers-ERR-CW3/1306.6089.txt l. 125–126]: "dnεSE* is the energy shift produced between spin-up and spin-down states of the nucleus".
*Replacement for CW3 §4.4, from "The two agree iff" to "stands.":*
"The two agree iff **d_nε_SE* is the per-level shift d·E (half the splitting)**. That convention is fixed by the physics (Rabi frequency Ω_a = dE, CW3-C10) and used by the
CASPEr supplement (S41), (S45). The source's own gloss calls d_nε_SE* the shift 'between spin-up and spin-down states'. Read as the splitting, the gloss is inconsistent with its
Eq. (1) by ×2. Status: Eq. (1) amplitude **CONFIRMED** with d_nε_SE* ≡ per-level shift. 1306.6089's verbal definition is misstated by ×2 (wording only). The convention is not the
source's own: CW3's Larmor-term analogy is withdrawn as evidence. The envelope correction (half as wide) stands."
Owed corrections 12, 13 and 21 are reissued (§2.2).

### 1.10 V15 (STANDS WITH CORRECTION): LE-90, typo 4 → 8; m_V² is not an error
*Replacement for CW3 §4.5, from "(a); ∫∂_zU_n" to "identical on resonance (b). The 32 = 2π × 4 × 2 × 2/π.":*
"(a) is a consistency check: M_n = ρπr_n²L₀ is printed by the source. ∫∂_zU_n d³x = [cos nπ − 1]·2πr_n²/√(M_nω_n) = −4πr_n²/√(M_nω_n) for odd n and 0 for even n (c).
|⟨n|δH₀|0⟩|² = **8**κ²ρ_Ve²cos²θM_n/(ε₀²ρ²L₀²ω_n) (CW3-C3d). With δ(m − ω) → (2γω²/π)/((m² − ω²)² + ω²γ²), P_s = 32κ²(ρ_V/ρ²)(e_pt²/ε₀²)(M_n/L₀²)·m_Vω_nγcos²θ/((m_V² − ω_n²)² + (ω_nγ)²).
On resonance this equals Eq. (7) and Eq. (8) (b), with 32 = 2π × 8 × 2/π. **Eq. (7)'s numerator m_V² is correct**: it is the exact steady-state power
F²γm_V²/(2M[(ω_n² − m_V²)² + γ²m_V²]) of the velocity-damped mode driven at m_V, and its integral over m_V equals the golden rule πF²/(4M) (CW3-C3e). Off resonance the
numerator depends on the smearing prescription; the δ-smeared golden rule fixes only the resonant value."
"m_V² ≡ m_Vω_n" and "is m_Vω_n" are deleted everywhere. Closure row and owed correction 15 are reissued.

### 1.11 V20 (STANDS WITH CORRECTION): LE-95, NR bracket; C6c
*Replacement in CW3 §4.10:* "in the NR limit (γ → 1, W_max = 2m_ev²) the bracket is ln(2m_ev²/I) − v² (C6c)" → "in the NR limit (W_max = 2m_eβ²γ²) the bracket
½ln(2m_eβ²γ²W_max/I²) − β² = **ln(2m_ev²/I) + v⁴/2 + O(v⁶)**: the ln γ² = v² + … cancels the −β² (CW3-C6c, now a sympy series; the CW3 C6c was a hard-coded True)."
PDG [FT] remains CW3's reading. VER-CW3 did not verify it and neither did ERR-CW3 (it is not on arXiv). L-D11′ is reissued.

### 1.12 STANDS items with wording notes from the verifier (V5, V12, V19)
- **V5** (LE-78 pitfall (3)): "mis-states the shift by ≈ 27%" → "mis-states the shift by ≈ 27% of δ_mv (δ_oo ≈ 0.27δ_mv [E], WP0-v3 (4.6″)), i.e. ≈ 21% of δ_rel".
- **V12** (LE-87): append to CW3 §4.2: "The factor m_χ/m_ν̃ assumes 𝔇^{NR} built with the NR vertex normalisation of CONVENTIONS §7 (DM-side 1/(2m_χ)² in |𝒱|²), against the
  relativistic 1/(4E_χE_ν̃) → 1/(4m_χm_ν̃)." Owed correction 20 is reissued.
- **V19** (LE-94 labels): append to CW3 §4.9: "Equation numbers of 2109.08168 are arXiv-HTML v2 numbers. In the PDF v2 [FT, checked]: |M|²_ALP = PDF (15) = HTML (16);
  dR/dcosθ = PDF (16) = HTML (17); R = PDF (17) = HTML (18) = main-text Eq. (3); the small/large-m_a limits = PDF (18) (in HTML they continue (18)). Side note (VER-CW3,
  confirmed): PDF (16) has 4m_e²(ω − ω′)² where (15) has 4m_e²ω², a second internal inconsistency of the source." L-D13 and owed correction 21 carry the note.

### 1.13 Scope-4 items (CLOSED-AS-EXACT-GAP rows)
**LE-73: doubtful "single missing step".** *Replacement for CW3 §1.1 "Single missing step" heading and the first sentence:* "**Missing steps** (four, plus one routine step):
(S1) a per-fibre conjugate operator A_K (dilation in the relative e–h momentum) and a Mourre estimate 1_I(H_K)[H_K, iA_K]1_I(H_K) ≥ c1_I + compact on intervals I that avoid
the threshold set 𝒯_K;
(S2) control of 𝒯_K. With the IR definition of X+ (ω_Q > ε_res), at most W/ε_res phonons fit in the window, so 𝒯_K is a finite union of critical-value sets of
E_Λ(K − ΣQ_j) + Σω_ν(Q_j) on compact tori. It is discrete if these functions are Morse [C]. Without ε_res the thresholds can be dense, and the hypothesis is then empty;
(S3) uniformity of the Mourre constants in g ∈ [0, g₀], K and N (the quasi-locality issue of §1.2);
(S4) the threshold behaviour: either test functions supported away from 𝒯 (the theorem then holds on C^{1,θ}_c(ℝ∖𝒯)), or a threshold-uniform LAP (weighted estimates, Hölder θ ≤ 1/2
at 3D van Hove points; open);
(S5) the passage from the fibres to H by the direct integral over K (routine given (S3)) [D, sketch]."
The rest of §1.1 is unchanged. The LE-82 bin condition shares (S1)–(S4) by analogy (next item).

**LE-82 bin (c).** "the same fibred LAP as §1.1" → "**an analogous LAP for H_d on the sectors**: H_d is not a fibre Hamiltonian H_K, so the conjugate operator must be built
sector by sector; steps (S1)–(S4) of §1.1 with H_K → 𝒬H_d𝒬". After V9, (G5′-c) joins the list of exact gaps (§1.1).

**LE-81: missing pitfall.** *Add to the CW3 §1.4 spec:* "*Pitfalls.* (1) **Double counting of the phonon-mediated interaction.** It may enter either the electronic kernel
Γ_{HF+ph} or the dressed phonon D^{-1} = D₀^{-1} − |g|²Π_CDW, but not both. Either take Γ = Γ_HF and assemble R = R_el + R_el g D g† R_el with Π_CDW = the Γ_HF-GRPA bubble, or put
the full phonon-mediated term into Γ and use the bare D₀ only for the external phonon vertex. (2) TiSe₂'s CDW is commensurate, so the phason is gapped. The Goldstone check uses the
artificially incommensurate Q only. (3) The self-consistent distortion and Δ_CDW must come from the same functional (PBE+U or hybrid) as the GRPA kernel, or the Ward identity is
violated by O(ΔU)."

**LE-86: spec completed.** *Replacement for CW3 §4.1 "Spec.":*
"*Spec.* **What:** Γ^{CC}(m_χ) per isotope for χ + (A,Z) → (A,Z+1)^{(*)} + e⁻ (continuum), plus bound-state capture e⁻ → atomic orbital of the daughter, for m_χ from threshold
Q_f to Q_f + 10 MeV.
**Level:** nuclear transitions in the allowed approximation (Fermi + GT, k_eR_N ≪ 1) [D at that order], with first-forbidden operators (r, σ·r, σ×r, the relativistic
γ₅ term) added wherever k_eR_N ≳ 0.1 or the allowed matrix element is suppressed. Shell-model nuclear states. Lepton: Dirac–Coulomb continuum with finite size and
atomic screening.
**Method:** KSHELL/NuShellX in a stated valence space (e.g. fp for A ≈ 70, jj45 for Xe/Te) for B(F), B(GT) and q-dependent one-body transition densities. Behrens–Bühring
shape factors with the radial lepton functions evaluated in the same nuclear radius convention. Bound capture with daughter Dirac–Fock orbitals.
**Convergence:** (i) total B(GT) against the Ikeda sum rule 3(N − Z) (times q_A²) to 5%, and the cumulative B(GT) inside the Q window to 1% in the number of final states (Lanczos
iterations); (ii) one valence-space enlargement (one major shell, truncated) changes Γ^{CC} by < 20% [E target], else report the spread; (iii) lepton partial waves |κ| ≤ 2,
with the |κ| = 2 terms < 5% for an allowed-dominated row; (iv) E_e grid of 200 points, Simpson to 10⁻³.
**Pitfalls:** (1) **g_A quenching**: GT strengths need g_A^{eff} = q_A·1.27, with q_A ≈ 0.7–0.8 (or explicit two-body currents), stated per valence space;
(2) **first-forbidden terms** at Q ~ MeV, where k_eR_N ~ 0.1 and suppressed GT transitions are forbidden-dominated;
(3) **Fermi-function conventions**: e⁻ emission uses the *daughter* charge Z + 1 and η = +(Z+1)αE/p (attractive). F(Z,E) as written (1905.12635) is F₀ at r = R_N; the
tabulated F₀L₀ includes finite size. Do not combine F₀L₀ with a separate finite-size correction, and do not use the parent Z (an O(1/Z) error);
(4) atomic exchange and overlap corrections at E_e ≲ 10 keV;
(5) recoil and the target-isotope abundance;
(6) the bound-capture channel is not optional near threshold (it can dominate when E_e → 0).
**Cost:** ≲ 10 core-h per isotope (shell model dominates)."

**LE-88 (c): spec completed.** *Replacement for CW3 §4.3 (c) "spec: …":*
"*Spec.* **What:** the quadratic density response R^{(2)}_{nnn}(q₁, q₂; ω₁, ω₂) (and the mixed rows needed by 𝒯_eff), with LFE (G-matrix), for ω₁, ω₂ up to the window
edge and ω₁ + ω₂ up to the sum-frequency range of the interference term.
**Level:** clamped nuclei, T = 0, adiabatic quadratic TDDFT (𝒳 = TDDFT, ALDA): R^{(2)} = [1 − χ_sK]^{-1}(ω₁+ω₂)·{χ_s^{(2)}(ω₁, ω₂) + χ_s(ω₁+ω₂)k^{(2)}_{xc}χ_s(ω₁)χ_s(ω₂)}·[1 + KR](ω₁)[1 + KR](ω₂),
with K = v_C + f_xc and k^{(2)}_{xc} = δ³E_xc/δn³ (ALDA). The RPA-quadratic level is K = v_C, k^{(2)} = 0; both are reported.
**Method:** static part from 2n+1 DFPT third derivatives (Gonze–Vigneron) as a check at ω → 0. Dynamic part by sum over states of the KS three-point function χ_s^{(2)}
on Wannier-interpolated bands, then the Dyson-like closure above.
**Convergence:** k grid 12³ → 16³ → 20³ to 3% (the quadratic response converges more slowly than R); bands to 2% (both denominators); N_G of the LFE matrices to 2%;
broadening η → 0 extrapolation (three values).
**Checks:** the HEG quadratic Lindhard function at the valence r_s (analytic) to 10⁻³; intrinsic permutation symmetry of R^{(2)} to 10⁻⁶; the static limit against DFPT d³E.
**Pitfalls:** (1) the xc kernel enters R^{(2)} twice (through K in every leg and through k^{(2)}_{xc}); dropping k^{(2)} while keeping f_xc is inconsistent;
(2) **sum-frequency poles**: ω₁ + ω₂ can exceed E_g while each ω_i < E_g, so the retarded prescriptions (ω_i + i0, ω₁ + ω₂ + 2i0) must be kept;
(3) three-point matrix elements ρ_{mn}ρ_{nl}ρ_{lm} need one gauge U(k) (CONVENTIONS §4), and PAW augmentation is needed at all three momenta;
(4) metals: intraband (Drude-like) divergences of χ_s^{(2)} at q → 0.
**Cost:** ≈ 10³ core-h."

**LE-93 Eq. (9) quantitative: spec completed.** *Replacement for the CW3 §4.8 sentence "a Dirac–Hartree–Fock evaluation of (F.4) with S_{J_TJ_T} for Xe at m_χ = 56.5–100 keV
(D §2.6 inputs)":*
"a relativistic evaluation of (F.4) with S_{J_TJ_T} for Xe at m_χ = 56.5–100 keV (D §2.6 inputs). **What:** the ratio of the conserved-current rate (F.4) to the Eq. (9) ansatz,
per shell (1s, 2s, 2p), on a (q, E_R) grid.
**Level:** bound and continuum states in **one local** potential: Dirac–Fock–Slater or a DHF-optimised local potential. A nonlocal exchange term violates the continuity
equation for the local current, so if DHF is used the exchange current must be added.
**Method:** a radial Dirac solver (GRASP/JAC or custom); continuum normalised as 1108.5383 Eq. (6), ⟨ψ̃_{k′l′m′}|ψ̃_{klm}⟩ = (2π)³δδk^{-2}δ(k′ − k).
**Convergence:** (i) partial waves κ up to |κ_max| where the shell rate changes < 1% (expect |κ_max| ~ 20–30 at these q); (ii) continuum normalisation by matching to
asymptotic Coulomb functions, amplitude error < 10⁻⁴, stable under r_max → 2r_max; (iii) radial grid.
**Check:** current conservation q·J_fi = ω n_fi to 10⁻³ for every transition.
**Pitfalls:** (1) J_T must be computed in the same gauge and potential as n (continuity), or the 'defect' is an artefact; (2) ω must use the orbital energies of the same
potential (mixing in experimental binding energies breaks continuity at O(Δε/ω)); (3) the transverse photon gauge (Coulomb) for J_T."

**LE-76 spec:** see §1.4 (pitfall (6), onset mask).

### 1.14 Scope-5 rows
L-D10′, L-O2, L9b′: unchanged. L-D13 (version note), L-D11′ ("− v²"), L17′ (validity), L-Fano ((P5), perturbative): reissued in §2.5.

---
## 2. Replacement texts for the merger

### 2.1 Closure table (rows changed; all other rows unchanged)
| Row | Item (short) | Status | Where |
|---|---|---|---|
| LE-73 | rigorous (H5)-free X0/X+ labels | CLOSED-AS-EXACT-GAP (missing steps (S1)–(S4): per-fibre Mourre estimate off thresholds, threshold-set control, g/K/N uniformity, threshold behaviour; (S5) routine) | CW3 §1.1 + ERR §1.13 |
| LE-75 | 𝔉 = 0 in Ge with SOC (and Si) | CLOSED [D] under (P1)–(P5) (pair-space PT reality, N_e even, scalar level shift on D(Λ₀)); without (P5) only Σ_b𝔉_b = 0 [D] | CW3 §2.2 + ERR §1.3 |
| LE-76 | 𝔉 size, Γ/δ map GaAs; K_ν ≥ 0 GaAs; Si d11 map | CLOSED (quantity derived + full spec; K_ν ≥ 0 [E, perturbative] outside the d11 and onset shells) | CW3 §2.3 + ERR §1.4 |
| LE-80 | Theorem D for magnetic insulators | CLOSED as theorem (i)–(ii) under (M1)–(M5); (iii) conditional on the open (G5′-c); bin condition [C] | CW3 §1.3 + ERR §1.6 |
| LE-82 | D-g beyond conjecture | (G5′) with U_qp = 1 **WITHDRAWN** (FALLS); connected (G5′-c), U_qp, bin (c) (analogous LAP for H_d), Dirac α̃ (coefficient 2(N_D+1)/3π) CLOSED-AS-EXACT-GAP; size [E] | CW3 §1.5 + ERR §1.1, §1.7, §1.13 |
| LE-83 | relaxed electron channel ε_e | CLOSED [D] (exact Lehmann formula (CW3.4); divergence as q → 0 and Si counterexample as q → 0 derived; [E] ≳ 10² at 1 keV) + spec | CW3 §3.3 + ERR §1.5 |
| LE-88 | two-insertion reductions | (b) CLOSED [D]; (d) Wick structure [D], size [E]; (c) CLOSED-AS-EXACT-GAP (full spec) | CW3 §4.3 + ERR §1.8, §1.13 |
| LE-89 | 1306.6089 factor 2; 2101.01241 u | CLOSED: amplitude CONFIRMED with d_nε_SE* = per-level shift (fixed by the Rabi frequency; the source's gloss is misstated ×2) [FT]; u derived | CW3 §4.4 + ERR §1.9 |
| LE-90 | 2501.05504 prefactor 32, M_n | CLOSED: 32 derived [D]; M_n consistency [FT]; Eq. (7) correct (damped-oscillator form) | CW3 §4.5 + ERR §1.10 |
| LE-95 | Bethe log constant; L-D12 | CLOSED: derived [D] (NR bracket ln(2m_ev²/I) + O(v⁴)) + PDG [FT, CW3's reading]; L-D12 tag kept | CW3 §4.10 + ERR §1.11 |

### 2.2 Owed corrections (complete list; the merger uses this list)
1. *unchanged.*
2. **WP5-v4 (W15)** (S) → "|ΔP(N|Λ₀)| ≤ (Γ^{ph}/Γ^{tot})max_ν|c_ν^F|·max_{b,b′}|P_b(N) − P_b′(N)| ≤ max_ν|c_ν^F|". Positivity line → "K_b ≥ 0 iff 1 + c̄^F − c_b^F ≥ 0,
   sufficient 2max|c^F| ≤ 1". GaAs [E] "2π max|c^F| ≲ 0.3Γ/δ" → "max|c^F| ≲ 0.3Γ/δ (first order in Γ/δ); K_ν ≥ 0 quoted for Γ/δ ≤ 0.5 [E, perturbative], outside the d11
   and onset shells (CW3 §2.3, ERR-CW3 §1.4)".
3. **WP5-v4 §8 θ_𝔉 row; WP6 θ_𝔉 prior** (S) → bound "|ΔP| ≤ max|c^F|" (not 2π max|c^F|); value "[E] ≲ 0.3Γ/δ, first order in Γ/δ, valid for Γ/δ ≪ 1; seeds in the d11
   or onset shells use the unexpanded Dyson form".
4. **NOTATION row 𝔉_{Λ₀,ν}, c_ν^F** (N) → "𝔉_b = Γ^{(b)}(c̄^F − c_b^F) (rate units; O4 (O4.7) is the spectral-weight form 2π|ρ|²𝔉_b/Γ^{tot});
   c_b^F = Γ^{tot}_Λ₀ Im(ρ*a^{off}_b)/|ρ_Λ₀|², dimensionless; b includes non-phonon branches; vanishes for PT-symmetric targets with N_e even and a scalar O(g²) level-shift
   matrix on D(Λ₀) (CW3 §2.2 (P1)–(P5)); without (P5) only Σ_b𝔉_b = 0".
5. **WP0-v3 §6.2 (iv″b)** (S) → "… includes the Fano term 𝔉_{Λ₀,b} (CW3 (CW3.1)); 𝔉 = 0 for PT-symmetric targets with an even electron number and a scalar level-shift matrix on
   the degenerate X0 manifold (one-body self-energies on Kramers or irrep manifolds), with or without SOC (Si, Ge, diamond) [D] (Θ-real pair basis, CW3 §2.2 (P1)–(P5));
   otherwise only the branch sum vanishes; generically ≠ 0 in GaAs [C]".
6. **WP3-v3 §M4 (iv″b) sentence** (S) → "Fano term 𝔉_{Λ₀,b} = Γ^{(b)}(c̄^F − c_b^F) with c^F of CW3 (CW3.1); 𝔉 = 0 for PT-symmetric Si, Ge, diamond at the one-body
   self-energy level [D, (P1)–(P5)]; e–h vertex level shifts leave only Σ_b𝔉_b = 0".
7. *unchanged.*
8. **WP0-v3 §6.2 Scope of (H2)** (S) → "Magnetic insulators with a charge gap Δ_ch ≫ ω_ph, J are covered by Theorem D-m (CW3 §1.3, ERR-CW3 §1.6): GS-m = spin–lattice
   manifold [D given PST]; quasi-boson sectors [D at quadratic order, with the Goldstone and Q = 0 acoustic zero modes gapped by the reference field or removed]; the cross-term
   bound is conditional on the open connected (G5′-c); itinerant magnets and fractionalised references remain open".
9. *unchanged.*
10. **LIMITS L17 (and WP0-v3 §9.2 (iii) relaxed ch = e, G6)** (S) → "ch = e, lattice relaxed: 1 − ε_e^{-1}(q,0) = [1 − ε_cl^{-1}(q)] + 𝒢_GS(q),
    𝒢_GS = (e²/q²Ω)Σ_ν|Σ_κq·Z^{(e)}_κ·e_κν e^{iq·τ_κ}/√M_κ|²/ω_ν(q_r)² (CW3 (CW3.4)), → Ω²_{P,e}/(c_Lq)² → ∞ as q → 0 in every solid, Si included [D]; [E] ≳ 10² at
    q = 1 keV; [E] ≳ 1 for q > q_BZ pending Z^{(e)}(q); step (iii) is not a usable bound; use (iv) or (9.4) with (CW3.4). The two-fluid 2.30 is the optical-only toy."
    Target row: the L17 of the bounds table (step (iii) / (9.5)), **not** the second "L17" in the OPEN ELF list (LIMITS.md l. 172).
11. *unchanged.*
12. **LIMITS L-D1** (S) → status "DERIVED, envelope ✎; amplitude CONFIRMED with d_nε_SE* ≡ per-level shift d·E (half the splitting), fixed by the Rabi frequency Ω_a = dE
    (CW3-C10) and used by 2101.01241 Supp. (S41), (S45) [FT]; 1306.6089's gloss 'energy shift between spin-up and spin-down states', read as the splitting, is misstated by ×2
    (amplitude unaffected)"; note "u = 2101.01241 (S23), absorptive overlap with the inhomogeneous line only [D]".
13. **WP7-D-v2 §1.5** (W) → "u … is the overlap of the inhomogeneous spin line with the absorptive Lorentzian (2101.01241 (S23)); the DM line is treated separately
    (Supp. §VII)"; amplitude sentence → "CONFIRMED with d_nε_SE* = per-level shift (2101.01241 convention, fixed by the Rabi frequency); 1306.6089's verbal gloss calls it the
    splitting (×2 misstatement of the source's wording)".
14. *unchanged.*
15. **LIMITS L-D4; WP7-D §1.7, IF-D12** (S) → "prefactor 32 derived (CW3 §4.5 with |⟨n|δH₀|0⟩|² = 8κ²…, ERR-CW3 §1.10); M_n = ρπr_n²L₀ printed by the source, consistent with
    ∫U_n² = (2ρω_n)^{-1}; Eq. (7)'s numerator m_V² is correct (exact steady-state power of the velocity-damped mode; equal to the smeared golden rule on resonance, Eq. (8));
    odd n only".
16. *unchanged.*
17. *unchanged.*
18. *unchanged.*
19. *unchanged.*
20. **WP7-D §2.5 massive ν̃** (W) → "ω^F = ω^{(2.1)} + (Δ_χ/m_ν̃)k²/2m_χ, 𝔇^F = 𝔇^{NR}(m_χ/m_ν̃)(1 + O(v²)) [D], with 𝔇^{NR} in the CONVENTIONS §7 vertex normalisation
    (DM-side 1/(2m_χ)²) and the relativistic 1/(4E_χE_ν̃) → 1/(4m_χm_ν̃)".
21. **SOTA ratings (WP7-D)** (W) → add "2109.08168 Eq. (3) (= HTML v2 Eq. (18) = PDF Eq. (17)): REFUTED by (m_a+2m_e)/(m_a+m_e) (CW3; VER-CW3 CONFIRMED); PDF Eq. (16)
    (dR/dcosθ) inconsistent with its (15) (4m_e²(ω−ω′)² vs 4m_e²ω²)"; "1306.6089 Eq. (1) amplitude: CONFIRMED with the per-level convention; source gloss misstated ×2";
    "2501.05504 Eq. (7): CONFIRMED (32 derived; m_V² numerator is the damped-oscillator form)"; "2011.01940 Eq. (9): not current-conserving (CONFIRMED); paper-error verdict =
    exact gap".
22. **New. WP4-v3 OW4-1, §8 Status, I1** (S) → keep open, adding: "(G5′) with U_qp = 1 fails: the disconnected term c†H_off|FS⟩ makes 𝔥_off extensive (ERR-CW3 §1.1, CW3-C12).
    The open item is the connected (G5′-c), which needs a dressed vacuum (U_qp) and an N-uniform commutator bound. Connected size [E] ≈ 0.2 eV (Al), ≤ λ_max of the Fan–Migdal
    zeroth-moment band matrix."
23. **New. WP4-v3 §8 (c) Dirac sentence** (W) → append "one-loop running α̃(ω) = α̃₀/[1 + (2(N_D+1)α̃₀/3π)ln(Λ_D/ω)] (ERR-CW3 §1.7; 1101.2210 Eq. (4) at N_D = 1 [FT]);
    α̃ ≈ 0.25 at Λ_D/ω = 10³ from α̃₀ = 0.91 [E]".

### 2.3 Interface flags (rows changed; IF-CW3-5, -8, -9, -10, -11 unchanged)
| # | Owner | Quantity | This return (replacement) |
|---|---|---|---|
| IF-CW3-1 | WP5 (W15)/(W17), K_ν; WP6 θ_𝔉; WP3 §M4 F8; O4-d7 export | Fano kernel | 𝔉_b = Γ^{(b)}(c̄^F − c_b^F), prefactor 1, c^F with Γ^{tot}; Υ = Υ^{PV} − (i/2)ΣΓa; K_x = (Γ^x/Γ^{tot})(1 + c̄^F); bound \|ΔP\| ≤ (Γ^{ph}/Γ^{tot})max\|c^F\|·spread; [E] numbers first order in Γ/δ, K_ν ≥ 0 quoted for Γ/δ ≤ 0.5 |
| IF-CW3-2 | WP0 §6.2 (iv″b), WP3, WP5, O4 | 𝔉 = 0 | [D] for PT-symmetric, N_e even, scalar level-shift matrix on D(Λ₀) (P5), with or without SOC (Si, Ge, diamond at one-body level); without (P5) only Σ_b𝔉_b = 0 |
| IF-CW3-3 | WP3 (R-code), WP5 (C-code); COMP queue | GaAs/Si Γ/δ map, c^F | fork inputs code/CW3/fork/ (reset the absolute fermi_energy, dis_froz_max); [E] K_ν ≥ 0 for GaAs off the d11 and onset shells; onset mask is an output |
| IF-CW3-4 | LIMITS L17, WP6 (θ support), WP0 §9.2 (iii), G6 | electron-only static step | (CW3.4): GS lattice term → Ω²_{P,e}/(c_Lq)² → ∞ as q → 0 in every solid [D]; [E] ≳ 10² at 1 keV; [E] ≳ 1 beyond q_BZ pending Z^{(e)}(q); step (iii) not a usable bound for relaxed ch = e |
| IF-CW3-6 | WP0 §6.2, OW0-17, WP4 OW4-4, WP7-B2 IF-B2-11, WP7-B1 G-E8 | magnetic/CDW sectors | Theorem D-m (i)–(ii) under (M1)–(M5); (iii) conditional on (G5′-c); CDW GRPA formula with the double-counting rule; metadata `ref=CDW` proposed |
| IF-CW3-7 | WP4 OW4-1, I1 | 𝔥_off | (G5′) with U_qp = 1 WITHDRAWN (extensive disconnected term); connected size ≤ λ_max M^{FM}(k) [E] with EPW matrix spec; exact gap (G5′-c); bin condition by an analogous LAP for H_d |

### 2.4 Symbols introduced by this errata (proposed NOTATION rows; collisions checked against NOTATION v4 and CW3)
| Symbol | Meaning | Where |
|---|---|---|
| (P5) | scalar O(g²) level-shift matrix on D(Λ₀) | §1.3 |
| η_ij | 2(e_i − e_j)/(γ_i + γ_j), level-shift splitting over width | §1.3 |
| Υ^{PV} | principal-value part of the off-shell self-energy Υ | §1.2 |
| 𝔥^c_off, M^c(k), M^{FM}(k) | connected off-diagonal norm; connected and Fan–Migdal zeroth-moment band matrices | §1.1 |
| (G5′-c) | connected restatement of WP4 (G5′) | §1.1 |
| (M5) | positive-definite quadratic spin–lattice form | §1.6 |
| 𝒯_K | threshold set of the fibre Hamiltonian H_K | §1.13 |

### 2.5 Proposed LIMITS rows (rows changed; L-D10′, L-O2, L9b′ unchanged)
| # | τ / chain (URF) | Source formula | Status |
|---|---|---|---|
| L-D13 | ALP dark Compton, exact Born QED (CW3.5); NR seagull H_sg | 2109.08168 Eq. (3) = HTML v2 (18) = PDF (17) (limits PDF (18)) | ✎ REFUTED by (m_a+2m_e)/(m_a+m_e) (CLAIMED, three routes; VER-CW3 CONFIRMED). Leading correction: none at tree level; in-medium negligible at m_a ≳ 100 keV per the source |
| L-D11′ | (S.1) → (S.2) Bethe with ln Ī from L(0,ω); Born, v ≫ shell velocities | PDG RPP 2024 Eq. (34.5) [FT, CW3's reading] | DERIVED; NR bracket ln(2m_ev²/I) + O(v⁴); shell/Barkas/Bloch corrections named |
| L17′ | ch = e relaxed: (CW3.4), GS lattice term | 2110.01587 §VII warning [per WP0, FT] | DERIVED (CLAIMED): step ≤ 1 false for every solid as q → 0 [D]; ≳ 10² at 1 keV and up to q_BZ [E]; [E] ≳ 1 beyond |
| L-Fano | DC first-emission kernel (CW3.1) incl. non-phonon branch | O4 (O4.7) | ✎ prefactor 1 in rate units; perturbative in Γ/δ; 𝔉 = 0 for PT, N_e even, scalar level shift on D(Λ₀) (P5) [D]; otherwise branch sum only |

---
## 3. Rebuttals (verifier claims that are wrong or too strong)
**R1. V9: "The FM zeroth moment is a defensible [E] for the linked part": wrong as stated for the subtracted linked part; right only for the orthogonal component.**
"Linked part" usually means ‖H_off|nk⟩‖² − ‖H_off|FS⟩‖². By (E9.1) that quantity is (1/N)Σ(1 − f_m)|g_{mn}|² − (1/N)Σ_v|g_{nv}(k−Q,Q)|², which is **sign-indefinite**.
In the exact Fock-space check (a counting identity, numerical) it takes the values −0.14, −1.05, +0.22 for N = 3, 4, 5 (CW3-C12c). It is not a norm, so it cannot replace 𝔥_off in the Duhamel bound [8.1′], and it is
not the FM zeroth moment (which has no f_m and no blocking term). The object that can enter is the norm of the orthogonal connected component [H_off, c†_{nk}]|FS⟩,
(1/N)Σ(1 − f_m)|g|². That is ≤ the FM zeroth moment [D at T = 0; C12a, c]. The verifier's sentence is therefore correct only with "linked part" ≡ this component. §1.1 states it so.

**R2. V2: "otherwise only Σ_b𝔉_b = 0 is derived": too pessimistic.**
In the commuting case the per-branch Fano weight is derived in closed form (§1.3; sympy residue, CW3-C2g): it is ∝ η_ij/(1 + η_ij²) with η_ij = 2(e_i − e_j)/(γ_i + γ_j). It therefore also vanishes, as
O(Γ/ΔẼ), when the level-shift splitting is ≫ Γ. In that case the levels are non-degenerate Θ-real seeds, each covered by the theorem. Numerically the same 1/s decay holds
without commutation (CW3-C2f: ratio 2.8 for s = 5 → 20). So (P5) is sufficient but not necessary. The derived statement is
"𝔉_b = O(min(ΔẼ/Γ, Γ/ΔẼ)) [D commuting, E general]". Only splittings ~ Γ give a Fano term of generic size, and the verifier's counterexample (s ~ Γ) sits exactly there.

**R3. V1: the corrected "Υ = −(i/2)Σ_fΓ^{(f)}a^{off}_f" is exact only for a flat continuum.**
In general Υ = Υ^{PV} − (i/2)ΣΓa, with Υ^{PV} the principal-value part. Υ^{PV} is absorbed in ρ at the order kept, so (CW3.1) is unaffected (§1.2). This is a precision note on
the verifier's replacement, not a disagreement with its conclusion.

**R4. V10: "The general form 2(N_D+1)/3π is my inference … not a quote": now derived.**
Velocity part 2α/3π (exchange self-energy) and charge part α/3π per Weyl node (interband bubble), sympy CW3-C13a, b. N_D = 1 reproduces 1101.2210 Eq. (4) exactly [FT].
The coefficient is [D, one-loop], not an inference.

**R5. V3: "δ → 0 exactly where Γ is 20–60 meV": true above the onset only.**
Just below the Γ–L onset Γ ≈ 3 meV (LO emission only), so the exclusion shell is asymmetric: Γ/δ ≤ 0.5 needs ≈ 6 meV below the onset and ≈ 40–120 meV above it. §1.4
evaluates the shell width with Γ on the seed's side. The verifier's symmetric "≲ 2Γ" with the above-onset Γ over-excludes the region below the onset.

No other verifier claim was found wrong. V4, V5, V7, V11, V12, V16–V19, V21 and V22 STAND, and their wording notes are applied (§1.12).

---
## 4. Changes to code/CW3/checks.py (45/45 PASS, ≈ 17 s)
- *Tightened:* CW3-C1a |ΔK| < 3×10⁻⁵ (was 5×10⁻⁴; observed 9×10⁻⁶) and the WP5 form > 300× worse; CW3-C1b 3×10⁻⁵; CW3-C1c ratio 3.8–4.2 (was 2.5–6; observed 4.00), with c computed
  for general ρ; CW3-C2a < 10⁻¹⁰ of generic (was 10⁻³); CW3-C5c ratio = (1 + m_a/m_e)² to 10⁻⁹ (was |ratio − 1| < 3×10⁻³); CW3-C9d 330–336 (was 200–500); CW3-C10 5×10⁻⁴ (was 2×10⁻³);
  CW3-C10b against the closed form (2/ΓT₂)arctan(ΓT₂/2) to 10⁻⁶ and the S25 interval.
- *Circular or vacuous checks removed:* CW3-C6c (hard-coded `True`) → sympy series of the PDG bracket; CW3-C11 (arithmetic 1/(2·0.3)) → random-kernel tests CW3-C11a, b; the unused
  `num = … + 1 − 1` line in CW3-C9 deleted.
- *New, one or more per correction:* CW3-C1d (V1 Υ), CW3-C2d–g (V2 (P5); R2 decay and closed form), CW3-C3d (V15 factor 8), CW3-C3e (V15 m_V²), CW3-C6c (V20), CW3-C9e (V6 q → 0 only), CW3-C11a, b
  (owed corrections 2, 3), CW3-C12a–d (V9, R1), CW3-C13a–c (V10, R4), CW3-C14 (V8 (M5)). V3, V13, V14 (wording, spec, tags) need no numeric check. V14's physics is CW3-C10.
- *Fork:* comments in code/CW3/fork/{GaAs,Si}-LE76/epw.in on resetting fermi_energy and dis_froz_max (V3).

---
## 5. Closing table: verifier item → resolution → location
| Verifier item | Resolution | Location |
|---|---|---|
| V1 LE-77 Υ slip; Γ/δ ≲ 1.7 outside expansion | applied; Υ^{PV} refinement; K_ν ≥ 0 quoted for Γ/δ ≤ 0.5 [E] | ERR-CW3 §1.2; owed 2, 3; IF-CW3-1; L-Fano; R3; CW3-C1d, CW3-C11a, b |
| V2 LE-75 needs (P5) | applied; closed-form η/(1+η²) mechanism; (P5) shown sufficient, not necessary | ERR-CW3 §1.3; owed 4, 5, 6; IF-CW3-2; L-Fano; R2; CW3-C2d–g |
| V3 LE-76 onset shells; epw.in absolute energies | applied (asymmetric shells, mask output, pitfall (6), file comments) | ERR-CW3 §1.4; owed 2; IF-CW3-3; R5; fork/*/epw.in |
| V4 LE-79 | STANDS: no change | — |
| V5 LE-78 "27%" | wording applied | ERR-CW3 §1.12 |
| V6 LE-83 [D] only q → 0 | applied | ERR-CW3 §1.5; owed 10; IF-CW3-4; L17′; CW3-C9d, CW3-C9e |
| V7 LE-74 | STANDS: no change | — |
| V8 LE-80 (M5); (iii) inherits V9 | applied | ERR-CW3 §1.6; owed 8; IF-CW3-6; CW3-C14 |
| V9 LE-82 (G5′) FALLS | withdrawn; re-derived ERR-CW3 (E9.1); connected size [E]; lemma [D]; exact gap (G5′-c); new spec | ERR-CW3 §1.1; owed 22; IF-CW3-7; R1; CW3-C12a–d |
| V10 Dirac coefficient | applied and derived: 2(N_D+1)/3π, α̃ ≈ 0.25 | ERR-CW3 §1.7; owed 23; R4; CW3-C13a–c |
| V11 LE-85 | STANDS: no change | — |
| V12 LE-87 normalisation | wording applied | ERR-CW3 §1.12; owed 20 |
| V13 LE-88 (d) tag | applied ([D] structure, [E] size) | ERR-CW3 §1.8; closure row |
| V14 LE-89 convention | applied (source gloss ×2; Larmor analogy withdrawn) | ERR-CW3 §1.9; owed 12, 13, 21; CW3-C10 |
| V15 LE-90 typo 4 → 8; m_V² | applied; m_V² shown exact for the damped mode | ERR-CW3 §1.10; owed 15, 21; CW3-C3d, CW3-C3e |
| V16–V18, V21, V22 | STAND: no change | — |
| V19 LE-94 labels | version note applied (PDF/HTML map checked [FT]) | ERR-CW3 §1.12; owed 21; L-D13 |
| V20 LE-95 "− v²"; CW3-C6c vacuous | applied; CW3-C6c rewritten | ERR-CW3 §1.11; L-D11′; CW3-C6c |
| §4 LE-73 doubtful single step | all missing steps (S1)–(S5) stated | ERR-CW3 §1.13 |
| §4 LE-81 double-counting pitfall | applied (+2 pitfalls) | ERR-CW3 §1.13 |
| §4 LE-82 "same" LAP; (G5′) open | "analogous LAP for H_d"; (G5′-c) added | ERR-CW3 §1.13, ERR-CW3 §1.1 |
| §4 LE-86 spec insufficient | full spec (what/level/method/convergence/pitfalls incl. g_A, forbidden, Fermi-function conventions) | ERR-CW3 §1.13 |
| §4 LE-88 (c) spec insufficient | full spec (quadratic TDDFT, dynamic level, convergence, HEG check, xc kernel, sum-frequency poles) | ERR-CW3 §1.13 |
| §4 LE-93 spec thin | full spec (local potential, partial waves, continuum normalisation, continuity gauge) | ERR-CW3 §1.13 |
| §4 LE-76/78/83 compute specs | complete apart from V3: applied | ERR-CW3 §1.4 |
| §5 L-D10′, L-O2, L9b′ | correct: unchanged | ERR-CW3 §1.14 |
| §5 L-D13, L-D11′, L17′, L-Fano | reissued | ERR-CW3 §2.5 |
| §6.7 LIMITS target rows; duplicate L17 | target named (bounds-table L17, not the OPEN ELF list l. 172) | owed 10 |
| §6.8 minor (Υ, − v², LE-88 (d), specs, LE-73 caveat) | all applied | ERR-CW3 §1.2, ERR-CW3 §1.8, ERR-CW3 §1.11, ERR-CW3 §1.13 |
| §3 CW3-C6c vacuous, CW3-C11 arithmetic, CW3-C2 blind to V2 | replaced / extended | ERR-CW3 §4; CW3-C6c, CW3-C11a, b, CW3-C2d–g |
