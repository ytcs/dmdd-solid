# R7 / REF-WP0-B: hostile referee of returns/R6/WP0-v2.md (isolated)

Read: WP0-v2.md, code/WP0-v2/checks.py, CONVENTIONS, NOTATION (grep only), CONTROLS, DONE, LIMITS. Not read: referees/ (other files),
state/, AUDIT, other returns, other briefs. `python3 -I checks.py` reproduces **44/44 PASS** (13 s). My own sympy checks (≤ 1 min,
scratchpad `ref.py`) are cited as REF-B-Sn. Full texts fetched with lit.py, read, then deleted: 2101.08263, 2101.08275, 2110.01587,
2608.05282, math-ph/0104024 (Spohn–Teufel), math-ph/0201055 (PST).

## Verdict table
| # | Claim (WP0-v2 location) | Verdict | One-line reason |
|---|---|---|---|
| V1 | 16-operator basis, matching, anchor (2.2)–(2.3) | STANDS WITH CORRECTION | the on-shell reduction to j_T, J_T needs [H, s_i] = 0 (SOC = 0, no H_hf, no Zeeman); (L) alone is not enough for the J rows |
| V2 | Master formulas (3.1)–(3.6), bookkeeping, absorption | STANDS | Lehmann, golden rule, (2ωV)^{-1/2} quantisation re-derived; factors agree |
| V3 | FDT, KK, detailed balance, positivity (4.1)–(4.4) | STANDS WITH CORRECTION | R^∞_{jj} = +𝓃/m contradicts (3.2) and the gauge identity stated in the same line; the nonreciprocal part of S_ee is O(q³), not 2q·𝐛 |
| V4 | First-moment matrix (4.5) | STANDS WITH CORRECTION | as written (S_ab[O] + S_ab[O†]) it is false off the diagonal (REF-B-S1); it must be S_ab[O] + S_ba[O†] |
| V5 | f-sum (4.6), (4.6a–e), mass-velocity (4.6′) | STANDS | re-derived; −0.18% Si, −0.58% Ge reproduced from virial ⟨T⟩ |
| V6 | Mixed third moment (4.7), q → 0 qualifier | STANDS | the contact term is exact at all q; the finite-q correction is the ℓ = 2 term, O(q⁴) at cubic sites; the qualifier is right (sharpening below) |
| V7 | C7 soft limit (4.9), Q_min | STANDS (as an import) | lab ⇔ comoving algebra and the v1 offset check out; Q_min with (v_max + c_ν) is the correct weaker (absorption) bound. Not derived in this package: the tag should be "[D in X1]" |
| V8 | Screening (5.1)–(5.4), species coupling vectors | STANDS WITH CORRECTION | Dyson and LFE algebra exact (re-derived); the Bohm–Staver line uses ε_e, which by (5.5) contains the ions; it must be the clamped electronic ε |
| V9 | Four Coulomb-line classes, topological proof (5.5) | STANDS WITH CORRECTION | the proof ("the phonon line closes exactly one cycle") excludes the ionic class, where the phonon line is a bridge; the classes are not a partition of Coulomb lines by momentum |
| V10 | (5.6)–(5.7), (5.7′) | STANDS WITH CORRECTION | W^{scr}(P,ω_f) sits where pairs are open, so the in/out labelling matters there; (5.7) is right only with retarded W in (3.2) order. CC-1's "(5.7) unaffected because R is Hermitian" holds for the external factor only |
| V11 | CC-1, (7.2) out-state weight | STANDS WITH CORRECTION | factorisation algebra exact (re-derived); retarded ⇒ out-state is [D, sketch]; C10g's label claims a pair-by-pair test it does not run; the pair-channel extension (V10) is missing |
| V12 | Theorem D: hypotheses, scope, PST basis | **FALLS in part** | "applies to magnetic insulators" contradicts (H2): gapless or degenerate spin sector. Remainder O(κ_BO^{n+1}) is mis-indexed (PST's parameter is ε = κ_BO²). PST is cited [ABS] in support of a [D]. Point-nucleus Coulomb fails PST's H_k by Spohn–Teufel's own statement; finite nuclear size cures it; N-uniformity is the real gap |
| V13 | Theorem D (iv′)/(iv″), Γ/δ bound, d1–d11 | STANDS (as an import) | internally consistent (11 conditions; the d6/d7/d11 cross-references in (7.3) and §12 match); the bound content is O4's and cannot be verified inside this brief |
| V14 | L0 (§9.1) | STANDS | chain re-derived; source quotes verified in full text (2101.08263 Eq. (1), (S.9)) |
| V15 | L17 (§9.2) | STANDS WITH CORRECTION | (9.4)–(9.6) verified against 2110.01587 and 2608.05282 in full text, but (iii) is proven only for ε_c and the clamped ε; for the electron channel with relaxed lattice, 1 − ε_e^{-1}(q,0) > 1 is possible (REF-B-S2), as 2110.01587 §VII itself warns |
| V16 | Hyperfine sign and factor (1.2), (2.9) ALP map | STANDS | −𝛍_e·B_contact with HL B = (2/3)𝛍δ³ re-derived; κ_mix m² → g_aγγB₀m gives g²B₀²Im(−1/ε_∥)/m |

Literature claims (rubric c): WP0-v2 claims **no** published paper is wrong. The KKL n_{−k} remark is a sign convention (checked
in 2101.08275); 2305.05681 is honestly left open (O6). There is nothing to rate CONFIRMED/REFUTED. One citation slip: §9.2 says (9.6) "gives
… 2110.01587 Eq. (4)", but Eq. (4) there is the partial-range inequality ∫dω/ω Im(−1/ε_L) ≤ (π/2)(1 − ε_L^{-1}(0,k)), not a rate formula.

---
## Arguments

**V1. On-shell transversality for the spin-current row.** q·v^⊥ = q·v_χ − q·v_s. Elastic DM gives q·v_χ = ω. For the density row,
⟨f|q·j|i⟩ = ⟨f|[H,n]|i⟩ = ω⟨f|n|i⟩ under (L), so q·v^⊥ → 0. For the J row one needs q_αJ^{αβ}(q) = [H, Σ_i e^{iq·r_i}s_i^β]. Write H = T + V.
Then [T, e^{iq·r}s^β] = q_αJ^{αβ}, but [V, e^{iq·r}s^β] = e^{iq·r}[V, s^β]. This vanishes only if V commutes with every s_i. The Fermi contact
term (1.2) (s·𝐈δ³ is multiplicative in r, so it satisfies (L)), Zeeman g_eμ_B B₀·s and SOC all violate it. Correction: add "SU(2)-invariant
H (SOC = 0, H_hf and B₀ off)" to the hypothesis of the J_T statement in (2.2) and in L0 (α). The matching examples (𝒪₃, 𝒪₇, 𝒪₈) and the count
1 + 3 + 3 + 9 = 16 per species are correct. The symmetrised ½{p/m, e^{iq·r}} acting on |k⟩ gives (k + k′)/2m = v_s. ✔

**V2.** Γ = 2πΣ_{p′}|V^{-1}Σ_a𝒱_a⟨f|O_a|i⟩|²δ = ∫d³q/(2π)³ Σ_ab 𝒱_a*𝒱_b (2π/V)Σ⟨i|O_a†|f⟩⟨f|O_b|i⟩δ, so 𝔇_ab = 𝒱_a*𝒱_b matches the index
order of (3.1). Absorption: Γ_abs = 2π(y²/2ωV)Σ|⟨f|O(k)|i⟩|²δ = (y²/2ω)S. Γ_net uses (1 − e^{−βω})S = −2 Im R. ✔ Per unit target mass:
n_χΓ_χ/ρ_T. ✔

**V3a. R^∞ for currents.** By (3.2), R_ab is the Lehmann sum Σ(p_i − p_f)(…)/(ω − E_fi + i0), so R_ab → 0 as ω → ∞ for every a, b. Hence
R^∞ ≡ 0, including for paramagnetic currents. Moreover, at T = 0, using ⟨f|q·j|0⟩ = (E_f − E_0)⟨f|n|0⟩:
R_{j_Lj_L}(q,0) = −2Σ_f|⟨f|j_L|0⟩|²/(V(E_f − E_0)) = −(2/q²V)Σ_f(E_f − E_0)|⟨f|n|0⟩|² = −𝓃/m exactly. So the stated gauge identity
R^L_jj(q,0) + 𝓃/m = 0 holds for the spectral R alone. It would be violated if R contained R^∞ = +𝓃/m. Correction: "R^∞ = 0 for all
operators of §2. The diamagnetic contact term belongs to the physical current kernel K^{αβ} = R_{j^αj^β} + δ_{αβ}𝓃_s/m_s, not to R."
**V3b. Nonreciprocity order.** For O = n_e and an insulator, S_ee(q,ω) = q_αq_βA_αβ(ω) + q_αq_βq_γB_αβγ(ω) + O(q⁴). The q² coefficient
is even, so S(q) − S(−q) = 2q_αq_βq_γB_αβγ + O(q⁵). "2q·𝐛_NR + O(q³)" holds only for operators with O(1) matrix elements (the spin rows),
or if 𝐛 ∝ q². Restate it per operator.

**V4. (4.5) off-diagonal.** ∫(dω/2π)ω S_ab[O] = V^{-1}⟨O_a†[H,O_b]⟩. Stationarity gives ⟨[O_a†,[H,O_b]]⟩ = ⟨O_a†[H,O_b]⟩ + ⟨O_b[H,O_a†]⟩.
The second term is the moment of S_ba[O†] (operators O_b†, O_a†), not of S_ab[O†] (operators O_a†, O_b†). The two are complex conjugates,
so they differ off the diagonal. REF-B-S1 (4-level system, random complex O_a ≠ O_b, T = 0): the residual of (4.5) as written is −25i;
with S_ab[O] + S_ba[O†] it is 0; the diagonal is fine. This is consistent with (4.3), which already pairs S_ab[O] with S_ba[O†].
(4.6c) 𝓜¹_eκ = 0 is unaffected (the commutator vanishes), but the spectral statement must be ∫ω[S_eκ + S_κe[O†]]dω = 0.

**V5.** For F = −p⁴/8m³: F(p+q) + F(p−q) − 2F(p) = −[p²q²/2 + q⁴/4 + (p·q)²]/m³. With the cubic/closed-shell average
⟨(p·q)²⟩ = q²⟨p²⟩/3 this gives (4.6′). From the virial theorem, ⟨T⟩ ≈ |E_tot|/N_e: 562 eV (Si) and ≈ 1.77 keV (Ge), so δ_rel = −1.8×10⁻³ and
−5.8×10⁻³. ✔ The Dirac remark (α·p is linear in p, so the double commutator vanishes) ✔. (4.6d): 14·m_e/(28·1836 m_e) = 2.7×10⁻⁴ ✔.

**V6. (4.7).** C4d (1D, full two-body H) gives −(q²/mM)e^{iq(X−x)}V″; with V = −U the sign is that of (4.7). ✔ V_NN and V_ee drop out
because they commute with the electron or nuclear momenta, respectively. ✔ Decompose (q·∇)²U = (q²/3)∇²U + [ℓ = 2 part]. With U = Zα/r,
∇²U = −Ze²δ³ (HL), and **the phase e^{iq·(R−r)} equals 1 on the δ support, so the contact term is q-exact.** The ℓ = 2 part ∝ q²P₂(q̂·ŷ)/y³
picks up the ℓ = 2 component of e^{−iq·y}, which is −5j₂(qy)P₂(q̂·ŷ) ∝ (qy)². Its average over the conditional electron density at a cubic site is
therefore O(q⁴∫y ρ_e(y)dy), nonzero at finite q and zero as q → 0. At non-cubic sites it is O(q²) (the field gradient at the nucleus).
The text's qualifier and parenthesis are correct. Sharpening: "𝓜³_eκ = −q²Z_κe²𝓃_κ𝓃_e(R_κ)/(3m_eM_κ) + O(q⁴) (cubic); + q_αq_β×EFG
term (non-cubic)". 𝓜³ is not given a stated ω normalisation (the analogue of (4.5)); add one.

**V7. (4.9) and Q_min.** C12a/b check only that the two printed forms are equivalent and that v1 is offset by ê·(p_cc − p_vv). Nothing in
WP0-v2 derives (X1). The package is "standalone", so the tag should read [D in X1; algebra WP0v2-C12]. Dimensions: ℓ_Q × momentum is
dimensionless ✔. |D|/c_ν = 10 eV/(3×10⁻⁵) ≈ 330 keV ✔. Q_min: on shell, Δε_c ≡ ε_{c,k+q+Q} − ε_{c,k+q} = ω ∓ ω_Q − (ε_{c,k+q} − ε_{vk}).
For emission this gives |Q| ≥ (E_min − ω)/(v_max − c_ν); for absorption, |Q| ≥ (E_min − ω)/(v_max + c_ν). The printed bound is the weaker,
valid for both. ✔ Soft bremsstrahlung: |M|² ∝ ℓ_Q² ∝ 1/|Q| (deformation), so ∫Q²dQ is finite; piezo gives M ∝ ℓ_Q/|Q|, |M|² ∝ |Q|^{-3}, a
log. ✔

**V8. Screening.** From R = R̃ + R̃vR in super-space: R_cb = (1 − R̃_ccv)^{-1}R̃_cb, so R_ab = R̃_ab + R̃_ac(1 − vR̃_cc)^{-1}vR̃_cb
(push-through). This is (5.3) with ε = 1 − vR̃_cc. ✔ (5.4), (5.5) signs ✔. j_L: S_{nj_L} = (ω/q)S_nn needs only [H,n] = q·j (full H, (L)). ✔
Two corrections:
(a) Bohm–Staver ω² = Ω²_{p,ion}/ε_e(q,0). By (5.5), ε_e^{-1} ≡ 1 + v_CR_ee contains the ionic response, and hence the acoustic pole itself.
The correct object is the clamped-nucleus electronic ε (= ε at clamped nuclei).
(b) j_T: besides LFE (G ≠ 0), in non-cubic targets, or at finite q off high-symmetry directions, R̃_{j_T(q),n(q)} ≠ 0 already at G = 0
(longitudinal–transverse mixing). (5.3) covers this; the prose names only the LFE mechanism.

**V9. Four classes.** The proof treats the Coulomb-proper O(g²) polarisation diagram as a graph (loops = nodes; Coulomb and phonon lines =
edges) and argues that the phonon line closes one cycle. This is right when the phonon momentum is integrated (Q free): DFPT segments at Q+G,
pair segment at P = q+Q, bridges at q. In the ionic ("X") class, however, the phonon line carries q mod G and is a **bridge**: removing it
disconnects the diagram, contrary to "the phonon line closes exactly one cycle". Its Coulomb lines also carry q+G, the external-class
momentum. So the statement "every Coulomb line is in exactly one class" is not a momentum partition. Correct statement: the phonon line is
either a bridge (ionic class = ionic part of ε_tot in the external chain, and of ε(P) in the pair chain) or closes one cycle (DFPT, pair,
external). The proof should be given for both cases. Box diagrams (both external vertices on one loop) have no pair segment; harmless, but
"the middle one is the pair channel" assumes there is one. Ring-level restriction and excitonic exclusion are stated. ✔ DFPT order
O(ω_Q²/E_g²): with TR, R(Q,−ν)* = R(Q,ν)ᵀ, and below the gap R is Hermitian, so R(−ν) = R(ν): even in ν. ✔ (Inversion is not needed.)
(0.06/1.12)² = 2.9×10⁻³ ✔.

**V10/V11. CC-1 and the pair channel.** Re-derived: R = R⁰(1 + fR) = (1 + Rf)R⁰ gives R − R† = (1 + R†f)(R⁰ − R⁰†)(1 + fR) =
(1 + Rf)(R⁰ − R⁰†)(1 + fR†) (f real diagonal). With R⁰_{GG′} = Σ_pair ρ_G*ρ_{G′}g, the 00 element is Σ_pair|Σ_Gρ_G(1 + fR)_{G0}|²Im g.
This is (7.2). ✔ The "out-state ⇔ retarded" identification (causal induced potential acting on bare KS pairs, as in time-dependent
mean-field theory) is physically sound, but it is an argument, not a theorem: in RPA, pair labels are not eigenstates of the interacting H.
Tag it [D, sketch].
**The overclaim.** §7.2/§10 say the out/in choice is immaterial for X2 (2.2)/(5.7) because "R(q,ω) is Hermitian in the PAER window". That covers
only the external factor (ε̃^{-1})_{G0}(q,ω), Hermitian to O(g²) there. The pair-channel factor W^{scr}(P,ω_f) is evaluated at the energy and
momentum of the final pair itself, where pairs are open by construction, so R(P,ω_f) is not Hermitian. Pair-resolved |M̃|² then depends on
retarded vs advanced W, exactly as in (7.2) (the totals agree, cf. C7a). Correction: state that (5.7) requires W^{scr}_{GG′}(P,ω_f)
retarded, with the final-pair index first (as printed), and that WP5 pair-resolved seeding inherits this choice. C10g's label "pair by pair"
is not what it tests (it compares totals only). The claim is nonetheless true, since R_{GG′} = R_{G′G} under TR + inversion makes the weights
equal; fix the label.

**V12. Theorem D.**
(a) **Magnetic insulators are outside (H2).** (H2) needs a non-degenerate adiabatic electronic ground state with gap Δ_ad ≥ E_g. In a magnetic
insulator, magnons are electronic excitations at clamped nuclei. With a continuous broken symmetry they are gapless (Goldstone), and a
ferromagnet's ground manifold is (2S+1)-fold degenerate. Anisotropy gaps (≲ meV) are generally below ω_ph, and magnon–phonon crossings
(NOTATION's g_mp) are exactly where adiabatic decoupling fails. Remove "magnetic insulators" from the scope. Alternatively, restrict to
magnon gap ≫ ω_ph, or move them to F5 (the gapless-target theorem, [C]) together with metals and superconductors.
(b) **Order counting.** PST's small parameter is ε = (m_e/M)^{1/2} = κ_BO² (math-ph/0104024 Eq. (4), math-ph/0201055), with errors O(ε^{n+1})
in the semiclassical scaling (nuclear momenta O(1)). Writing O(κ_BO^{n+1}) assumes a re-indexing for low-lying vibrational states
(∇_R ~ ε^{-1/2}). That re-indexing is plausible but not derived. State it, or write O(ε^{n+1}) with the scaling hypothesis.
(c) **Evidence.** math-ph/0201055 is tagged [ABS] yet underpins a [D] statement. (I read it: the symbol class assumes bounded-operator-valued
H(q,p) and a gap uniform in phase space.)
(d) **Coulomb.** Spohn–Teufel (math-ph/0104024, after condition H_k): the conditions "put constraints only on … the smoothness and decay of the
charge distribution of the nuclei. **For point nuclei H_k fails**", and a Hunziker-distortion generalisation (Klein–Martinez–Seiler–Wang)
would be needed. Hence "PST rigorous for smooth potentials; Coulomb assumed harmless [C]" is accurate, but it misses the cheap fix: the
framework already carries finite nuclear size (F^M_κ). With extended rigid nuclear charges, H_k holds. Then the electron–electron Coulomb
term is X-independent and does not enter H_k, so it is not the obstruction.
(e) **The real gap.** PST constants depend on the number n = 3N_nuc of slow coordinates (C_b^k bounds and a gap uniform over Λ ⊂ ℝⁿ), so (6.1)
is not N-uniform. The thermodynamic limit is listed only under (iv″)'s rigour items. Tag (6.1) itself "[D for finite systems with smeared
nuclei; C for the crystal limit]".
(f) "On the support of the vibrational state" should read "on the essential support (up to exponentially small tails)": harmonic
wavefunctions have full support.
The (ii) algebra is checked: ⟨n|Σ_i∇_iV_eN|0⟩ = m(E_n − E_0)²⟨n|Σr_i|0⟩ (via [H,p] = i∇V, p = im[H,r]). The amplitude is
(q/M)·⟨Φ_n|∇_RΦ₀⟩/(E_n − E_0) = (m q/M)·⟨n|Σr|0⟩. δM_atom = 2m²Σ(E_a − E_0)|⟨a|Σx|0⟩|² = N_e m (TRK). (iii) X-sector 𝓜¹_κκ = 𝓃_κq·δM·q/M². ✔

**V13. (iv′)/(iv″), d1–d11.** (6.3) is consistent with CONVENTIONS §10 (δ → X0; fp, PV → X+). C13a (fp(1/x²) against a Gaussian gives −2√π)
and C13b ✔. The list in (iv″d) has exactly 11 items, and the in-text uses d6 (first emission once), d7 (𝔉 export) and d11 (edge shell)
match their positions. The bound |Δw₀|/w₀ ≲ (1.1 + b_λ)Γ/δ is meaningful only for Γ/δ ≪ 1. With Si Γ/δ up to 0.6 (quoted) it is O(1), and
the text accordingly restricts that region to totals and P(N_eh). Consistent. b_λ and 𝒞_adm(ℓ_win) are used without definition in this
package (O4's objects); the standalone claim needs them defined. The normalisation of (6.3) (1/V, spin) is not stated.

**V14. L0.** ∫dΩ_q δ(ω − qv cosθ + q²/2m_χ) = (2π/qv)Θ(v − v_min), so dℛ/dω = (ρ_χ/m_χρ_T)∫q dq/(4π²)|Ṽ|²ηS̄, which is (9.2). With
S = (2q²/e²)W this equals 2101.08263 (S.9), ρ_χ/(2π²e²ρ_Tm_χ)∫q³|V|²Wη (FT ✔). Eq. (1) there is Γ = ∫d³q/(2π)³|V|²(2q²/e²)Im(−1/ε(q,ω_q))
(FT ✔). 2608.05282 Eq. (4) also matches. ✔

**V15. L17.** (9.4) = 2110.01587 Eq. (1) = 2608.05282 Eq. (1) ✔. (9.5) = 2608.05282 Eq. (2) ✔. (9.6) = 2608.05282 Eq. (8) with
(ε − 1)/ε = 1 − ε^{-1} ✔. Hölder log-convexity re-derived ✔. Lehmann gives −v_CR_chch(q,0) ≥ 0 for any channel, so the issue is only the
upper step "≤ 1", i.e. ε_ch^{-1}(q,0) ≥ 0. For ch = c this is the stability (Dolgov–Kirzhnits–Maksimov) question, proven at RPA+LFE. ✔
**For ch = e with relaxed lattice, which (ii) requires, it is not covered and can fail.** REF-B-S2, inside the package's own (5.3), with two
species, no LFE, diagonal static R̃, a ≡ −v_CR̃_e ≥ 0 and b ≡ −v_CZ²R̃_κ ≥ 0: 1 − ε_c^{-1} = (a + b)/(1 + a + b) < 1, but
**1 − ε_e^{-1}(q,0) = a(1 + b)/(1 + a + b)**, which exceeds 1 whenever ab > 1 + b. A GaAs-like q → 0 case (a = ε_∞ − 1 = 9.9, b = ε₀ − ε_∞ = 2)
gives **2.30**. At finite q in Si the static ionic b is O(1) (GS inverse-moment weight ~ κ⁴/κ⁴), and a = 10.7, b = 0.5 gives 1.32. No
theorem bounds ε_e, because it is not the response to a charge probe. 2110.01587 §VII states that electron-only (leptophilic) couplings
with nuclear motion can exceed these bounds. Corrections: (iii) "PROVEN at RPA+LFE" applies to ch = c and to clamped ε (= ε_e at clamped
nuclei). For electron-only coupling the usable bound is (iv) with ω_th above the phonon band and ε_∞ the physical above-phonon value: the
error is O(κ_BO⁴) only if ε_∞ includes zero-point renormalisation, and O(κ_BO²) if it is the clamped DFT value. The O5 closure (§12) is
overstated accordingly. Mark the electron-channel static bound [C]/false in general, and drop "strictly tighter for polar targets" as the
only case where (iv) matters.

**V16.** HL: B_G = (8π/3)μ_Gδ³ becomes B_HL = (2/3)μ_HLδ³. H = −𝛍_e·B = +(2/3)g_eμ_Bg_Iμ_N s·𝐈δ³ ✔. Minor: nuclear Zeeman −g_Iμ_N𝐈·B₀
and N–N dipolar terms also couple 𝐈 ("the only coupling" is false with B₀ on). (2.9): Γ_A′ = κ²m Im(−1/ε) with κ → g_aγγB₀/m ✔.

## Minor
- (4.8) "each term is O(q)" depends on B. For B = n_e, every S_{Bs} is O(q²), and the identity gives O(q³).
- (5.6) "otherwise divide L^{PA} by (1 − e^{−βω})": say "divide the right-hand side". At T > 0 the band occupation factors are also dropped.
- §9.2 citation slip (2110.01587 Eq. (4)), see above.
- C3c, C5 and C4d are single-instance sanity checks (rank-one Gram, 4-δ measure, 1D). They are fine as checks, not proofs. The text uses them
  correctly except C10g.

## Gap-closure (rubric e)
- F1/OW0-7: the algebra is closed; the pair-channel extension (V10) is a new remaining item.
- O5 (L17 iii): closed for ch = c only (V15).
- F4/OW0-8: rests on WP2-v2 and WP3-v2, which I may not read. (4.7) itself is now correct, so it cannot obstruct closure.
- Theorem D rigour: the exact remaining gap is the N-uniform PST bound for the crystal (point-nucleus Coulomb is avoidable, V12d), plus
  (H2) for magnetic targets.

## Required corrections (summary)
R1 (2.2): add the SU(2) hypothesis for J_T transversality. R2 (4.2): R^∞ ≡ 0; diamagnetic term goes into K. R3 (4.3): odd part of S_ee is O(q³).
R4 (4.5): use S_ba[O†]. R5 (5.3): Bohm–Staver with clamped ε. R6 (5.5): treat the bridge (ionic) case in the proof. R7 (5.7), §10: require
retarded W^{scr}(P,ω_f); drop "unaffected because Hermitian". R8 Theorem D: remove magnetic insulators; ε vs κ order; FT for PST; smeared
nuclei; N-uniformity tag on (6.1). R9 (9.2)(iii): electron channel not proven and false in general; restrict the claim. R10: C10g label;
§9.2 citation; (4.7) sharpened remainder.
