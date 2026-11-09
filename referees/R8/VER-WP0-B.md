# R8 / VER-WP0-B: verification of returns/R8/WP0-v3.md against REF-WP0-B (R7)

Read: WP0-v3 §0, §2, §4, §5.3–5.7, §6.2, §9.2, §16–§18, and code/WP0-v3/checks.py (re-run: **76/76 PASS**). Same isolation as R7.
My own sympy checks (scratchpad `ver.py`, under 1 min):
- the general moment identity of (4.5) for k = 0–3 (residual 0);
- the equality of the two 𝓜³ commutator forms;
- ∫₀^∞ j₂(x)/x dx = 1/3.

I re-fetched 2110.01587 to check the corrected citation, then deleted it.

## 1. Item-by-item verdicts
| R7 item | v3 action | Verdict | Note |
|---|---|---|---|
| V1 J-row transversality needs [H, s_i] = 0 | §2, §9.1(α), C21 | RESOLVED | wording exact |
| V2 master formulas | none | RESOLVED (STANDS) | — |
| V3a R^∞ | (4.2): R^∞ ≡ 0; R^{phys} = R + 𝓃/m; R^L(q,0) = −𝓃/m | RESOLVED | consistent with CONVENTIONS Π^γ_T |
| V3b nonreciprocity order | (4.3) per operator; densities O(q³) + O(q⁵) | RESOLVED | — |
| V4 (4.5) off-diagonal | S_ab[O] + S_ba[O†]; general ∫ω^k[S_ab − (−1)^kS_ba[O†]] | RESOLVED | k = 0–3 verified (REF-B-S3) |
| V5 f-sum, (4.6′) | unchanged; (4.6″) orbit–orbit added (REF-A's item) | RESOLVED | spot check below |
| V6 (4.7) qualifier, O(q⁴) | rebutted; (4.7′) | **rebuttal ACCEPTED** (§2) | new scope error N1 in (4.7′) |
| V7 (4.9) import tag | [D in X1]; C12 "algebra only" | RESOLVED | — |
| V8 Bohm–Staver; L–T mixing | clamped ε(q,0); G = 0 mixing stated | RESOLVED | — |
| V9 (5.5) bridge case | Case 1 / Case 2 (ionic insertion); [D, sketch] | RESOLVED | TR evenness R(−ν) = R(ν)† = R(ν) below the gap is correct |
| V10 retarded W^{scr}(P,ω_f) | (5.7), §16.3, flag G8 | RESOLVED | — |
| V11 CC-1 tag; C10g | two-level tag (§16.2); C10g now run pair by pair | RESOLVED | — |
| V12 Theorem D | magnetic insulators removed; κ_BO²; smeared nuclei (H1); essential support; N-uniformity; FT tags | RESOLVED, with one residual (N2) | — |
| V13 (iv′)/(iv″) definitions, (6.3) normalisation | 𝒞_adm, w₀, b_λ defined; (4π/V) | RESOLVED | bound check: (5/2π + 1/π)Γ/δ + b_λΓ/δ = (1.11 + b_λ)Γ/δ at ℓ_win = δ ✔ |
| V14 L0 | none | RESOLVED (STANDS) | — |
| V15 L17 electron channel; citation | (9.4′), (iii) split, (iv), status narrowed | RESOLVED | (9.4′) re-derived: ε_e^{-1} = (1 + b − ab)/(1 + a + b) ✔; 2110.01587 Eq. (8) is the weighted-integral bound and Eq. (9) the rate bound ✔ |
| V16 hyperfine; "only coupling of 𝐈" | remark applied | RESOLVED | — |
| minor items 1–4 | applied / no change | RESOLVED | — |

Spot check of (4.6″), REF-A's item (no verdict owed by me):
- The double commutator of a p_i·K·p_j bilinear is 2q·K·q cos(q·r_ij). ✔
- FT[(𝟙 + r̂r̂)/r] = (4π/k²)[𝟙 + (𝟙 − 2k̂k̂)] = (8π/k²)(𝟙 − k̂k̂). ✔ So the uniform pair-density part vanishes at k = ∓q. ✔
- Thomas–Fermi gives V_ee = T/3, hence δ_oo/δ_mv = (4/9)/(5/3) = 4/15. ✔ It uses the neutral-atom E_ee, which is not E′_ee, but this is acceptable as [E].

## 2. Rebuttal §17.2 (to B-V6): ACCEPT
My R7 claim was that the finite-q correction to 𝓜³_eκ at cubic sites is O(q⁴ ∫ y ρ_e dy) and vanishes as q → 0. That is wrong for the uniform
part of the conditional density, where ∫ y ρ_e dy diverges. I also mislabelled T_d sites as O(q⁴).

**Derivation, momentum space.** Write the conditional density as ρ_e(y) = Σ_G 𝓃_G e^{iG·y} and use FT[(q·∇)²U](k) = −(q·k)²Ze²/k². In (4.7),
∫ d³y ρ_e e^{−iq·y}(…) forces k = q − G, which gives the v3 G-sum.
- The G = 0 term is 𝓃_e q⁴/q² = 𝓃_e q² at every q ≠ 0.
- For |G| ≫ q the G ≠ 0 terms give (q·Ĝ)² 𝓃_G, which a cubic star average turns into (q²/3)(𝓃_e(R) − 𝓃_e).
- Total: −(q²/3) Z e² 𝓃_κ [𝓃_e(R) + 2𝓃_e]/(mM). ✔

**Real space.** The uniform part against the ℓ = 2 kernel 2Zα q² P₂/y³, together with the ℓ = 2 component −5 j₂(qy) P₂ of e^{−iq·y}, gives
−(2/3) q² Z e² 𝓃_e · 3∫j₂(x)/x dx = −(2/3) q² Z e² 𝓃_e, independent of q. ✔ (∫ j₂(x)/x dx = 1/3, verified.)

**Independent route (my own).**
- At large ω, (4.2) with (4.3) gives R_eκ → 𝓜³_eκ/ω⁴, using ∫(1 − e^{−βω})ω³S_eκ = ∫ω³[S_eκ + S_κe[O†]].
- With two uncorrelated species, (5.3) gives R_eκ = R̃_e(z_e v_C z_κ)R̃_κ.
- With R̃_e = 𝓃_e q²/(m ω²) and R̃_κ = 𝓃_κ q²/(M ω²) this is −Z e² 𝓃_e 𝓃_κ q²/(mM ω⁴), i.e. (4.7′) at 𝓃_e(R) = 𝓃_e. ✔

**Order of limits.** qL ≫ 1 holds for every DM transfer, so (4.7′) is the physical result. My form is the qL ≪ 1 limit (∫P₂ dΩ = 0). The
"contact term q-exact" point stands and is credited.

**T_d sites.** The q³ terms Σ_G 𝓃_G (q·G)³/G⁴ survive because 𝓃_G − 𝓃_{−G} = 2i Im 𝓃_G ≠ 0. The cubic odd invariant is xyz, so the term is
∝ i q_x q_y q_z. The vector term Σ_G 𝓃_G (q·G)/G² vanishes by T_d symmetry. ✔

**Size.** 2𝓃_e/𝓃_e(R): with 𝓃_e(R) ≈ 2Z³/π a₀⁻³ ≈ 1.7×10³ a₀⁻³ and 𝓃_e ≈ 0.104 a₀⁻³ for Si, this is ≈ 1.2×10⁻⁴. ✔

## 3. New errors in the changed sections
**N1 (4.7′) validity window is misstated (NEW ERROR, minor; numerically ~10⁻⁴).** v3 gives the range "1/L ≪ q ≪ 1/a_core". The expansion
(q·(q−G))²/|q−G|² → (q·Ĝ)² needs q ≪ |G| for every star that carries weight, so the range must start from q ≪ G_min ≈ 2π/a (≈ 2.3 keV in Si),
not from 1/a_core.
- For G_min ≲ q ≪ 1/a_core, the valence stars with |G| ≲ q contribute ≈ 𝓃_G q² (G = 0-like) rather than 𝓃_G q²/3.
- That changes the coefficient of the 𝓃_e-size term by O(𝓃_val/𝓃_e(R)). This is the same order as the 2𝓃_e correction being claimed.
- The remainder "O(q³)" is O(q³/G_min) relative, which says the same thing.

Correction: state (4.7′) for 1/L ≪ q ≪ G_min. For G_min ≲ q ≪ 1/a_core, write
𝓜³_eκ = −(q²Ze²𝓃_κ/mM)[𝓃_e(R)/3 + Σ_{G≠0} 𝓃_G((q·(q−G))²/(q²|q−G|²) − 1/3) + 𝓃_e].
The bracket lies between 𝓃_e(R)/3 + 2𝓃_e/3 and 𝓃_e(R)/3 + O(𝓃_val). Only the contact term is universal across the DM range of q (keV to tens
of keV). The conclusion ("fixed by contact densities up to ~10⁻⁴") is unaffected.

**N2 (6.1) remainder order applies to a regime the theorem is not used in (NOT RESOLVED as a statement; v3 is now honest but incomplete).**
- O(κ_BO^{2(n+1)}) is stated "in the semiclassical scaling (nuclear momenta O(1))".
- Every application of Theorem D (ZPL, phonon sidebands, Migdal at small q) concerns low-lying vibrational states, where that scaling does
  not hold.
- v3 drops the re-indexing ("not used") but leaves (6.1) without an order for the regime it is used in.

Correction: add "for low-lying vibrational states the order of the remainder is not derived [C]; O(κ_BO^{2(n+1)}) holds in the semiclassical
regime". OW0-13/14 should carry it.

No other new errors found:
- (4.2), (4.3), (4.5) and the general k formula, (5.3), (5.5) Case 2, (5.7), (6.3), (9.4′) and §9.2 (iii)/(iv) were re-derived or spot-checked
  and are correct.
- Closing-table bookkeeping (32 + 8 + 1 + 1 = 42) is consistent with the 20 B rows (16 main + 4 minor) as listed.
