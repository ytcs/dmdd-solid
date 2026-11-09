# App. C.15–C.20 acceptance review, part 2: derivation check (isolated)

Reviewer: derivation verifier (long-form-writing SKILL.md §5). Date 2026-11-07.
Scope: tex/appC/C-15.tex, C-16.tex, C-17.tex, C-19.tex, C-20.tex (C.18 already accepted, skipped); NOTATION.md; STYLE.md;
SPINE App. C rows C.15–C.20 ("Used by").
Method: every non-definitional step redone by hand and with sympy/numpy/scipy (scripts in the session scratchpad, not in the book):
Dirac-matrix identities and the FW transform as exact 4×4 algebra with a velocity-counting parameter; the double commutator and the
vertex as differential operators on a generic spinor; point-group counts by enumeration of the 48 signed permutation matrices; the
ohmic rate against a direct numerical time integral; the Frenkel–Kontorova chain relaxed numerically. Dimensions checked on every
displayed result; every number recomputed; every use of `app:C.n` / `eq:C.n-…` / `we:C-gyration` grepped in tex/ch*, appD, appE,
appF and compared in form and convention. Sources fetched with lit.py into sources/review-appC2/: Berlin et al. 2504.02927,
Qureshi cond-mat/9409105, Fitzgerald 1806.11002 (PDFs deleted after the check). Books (Bjorken–Drell, Jackson, Dresselhaus, Squires,
Lovesey, Braun–Kivshar) and the non-arXiv papers (Foldy–Wouthuysen, Glauber–Lewenstein, Blume, Moon et al., Leggett et al.) are not
open; checked against the standard statements.

Summary: 1 WRONG (wording that contradicts the result, C.17), 0 WRONG in mathematics, 5 GAP (minor: one notation clash, one
mis-pointed reference, two missing source remarks, the SPINE "Used by" lists). All else CHECKED. Every chapter citation of a
C.15–C.20 result finds it here in the form, sign and normalization used.

## C.15 Dirac equation and Foldy–Wouthuysen reduction

| Location | Verdict | Note / correction |
|---|---|---|
| Opening: Ge 1s at Zα = 0.23; corrections a few % of binding | CHECKED | 32/137.036 = 0.2335; relative shift 1.4–5.5 %. |
| eq:C.15-gamma; γ⁵ = iγ⁰γ¹γ²γ³ = offdiag(1,1); α², β² = 1, anticommutation | CHECKED | sympy. |
| Lagrangian → field equation → eq:C.15-HD (π = p + eA, V = −eA⁰) | CHECKED | Signs follow eq:C.9-mix (J_em = −ψ̄γψ) and A_μ = (A⁰, −A). V = −Zα/r with e² = 4πα. |
| eq:C.15-spinor: u†u = 2E, ūu = 2m_e; small/large ≈ v/2 | CHECKED | sympy. |
| γ_D − 1 = −0.005 (Si), −0.028 (Ge) | CHECKED | −0.00523, −0.02765. |
| γ⁰γⁱγ⁵ = diag(σⁱ,σⁱ), γ⁰iγ⁵ = i[[0,1],[−1,0]] | CHECKED | sympy. |
| eq:C.15-bilinears (four limits) and the pseudoscalar step | CHECKED | Reproduced; ψ̄iγ⁵ψ → ∇·(ψ_A†σψ_A)/2m_e. Integration by parts gives −(g/2m_e)∇φ·spin, same sign as eq. of sec:1.4 (L_aee). |
| Scalar − density = −2ψ_B†ψ_B = −T/m_e ("kinetic-energy term") | CHECKED | Matches eq:10.6-scalar and D.24 (1 − K²/8m²). |
| Gordon decomposition (convection + (2m_e)⁻¹∇×spin) | CHECKED | By hand with σⁱσʲ = δ + iεσ. |
| FW commutators [βO,β] = −2O, [βO,O] = 2βO², intermediate commutators, coefficients ½, −⅛, −⅓ | CHECKED | Exact BCH series to 7 terms with random Hermitian blocks, O→λO, E→λ²E: difference from eq:C.15-Hprime vanishes through λ⁴. |
| eq:C.15-Hprime | CHECKED | = Bjorken–Drell (4.3) at Ȯ = 0. |
| Power counting; second transformation adds O(m v⁶), leaves odd O(m v⁵) | CHECKED | |
| eq:C.15-double [O,[O,V]] = −∇²V − 2Σ·(∇V×p) | CHECKED | sympy on a generic 4-spinor with V(x,y,z). |
| eq:C.15-HFW; spin–orbit = (2m_e²)⁻¹(r⁻¹V′)S·L | CHECKED | Standard (Thomas factor included); dimensions eV. |
| eq:C.15-darwin: H_Dar = πZαδ³/2m_e² | CHECKED | ∇²V = 4πZαδ³. |
| \|ψ_ns(0)\|² = (Zαm_e)³/πn³; 1s Darwin shift m_e(Zα)⁴/2 | CHECKED | |
| 0.72 meV, 5.3e-5 (H); 28 eV, 0.010 (Z=14); 0.76 keV, 0.055 (Z=32) | CHECKED | 0.7245 meV; 27.8 eV; 759.7 eV; (Zα)² = 5.33e-5, 0.0104, 0.0545. |
| Mass–velocity −⅝m_e(Zα)⁴; net ¼(Zα)² of binding; 0.26 % Si, 1.46 % Ge "in all-electron calculations" | CHECKED | Hydrogenic ¼(Zα)² gives 0.26 / 1.36 %, exact Dirac 1s 0.262 / 1.40 %; the 1.46 % is the all-electron atom of we:3-Zalpha, correctly attributed. |
| Vertex transform e^X f e^{−X} = f + β[O,f]/2m − [O,[O,f]]/8m² | CHECKED | Same algebra as for E. |
| eq:C.15-vertex (ordering e^{iq·r} to the left of σ·(q×p)) | CHECKED | sympy with f = e^{iq·r}. Between plane waves equals the D.24 time component, iS·(q×K)/4m² with K = 2k + q. |
| q²/8m_e² = 4.8e-5 at 10 keV | CHECKED | 4.79e-5. |

Chapter uses: 10.6 (vertex, |ρ|² change −q²/4m², bilinears, r^{γ_D−1}, Ge 1s 0.055), 10.9 (time component → 1, J^μ → (n, j)),
12.5 (darwin, contact density), 3.5 (H_D, FW), 7.3 (α_D, β_D), 8.1 (bilinears, vertex factor 1.3e-3 at 53 keV, Zα ≈ 0.10 for Si 1s),
D.24 (spinor, gamma, vertex), D.34 (H_D): all present in the form used. CHECKED.

## C.16 The quantized radiation field

| Location | Verdict | Note / correction |
|---|---|---|
| Mode energy Σ2Vω²\|c\|²; c = α/(2Vω)^{1/2}; eq:C.16-A | CHECKED | Cross terms cancel since (k×ε)·(k×ε′) = k²ε·ε′. Standard HL normalization. |
| n + 1 enhancement; n_B negligible for ω ≫ T | CHECKED | |
| eq:C.16-minimal; p·A = A·p in Coulomb gauge | CHECKED | |
| One-photon matrix element; eq:C.16-rate prefactor e_c²ω/(8π²m²) | CHECKED | 2π · ω²/(2π)³ · 1/(2ω). |
| p_fi = −imω r_fi; polarization sum; ∫ = 4π\|d\|²·⅔ | CHECKED | |
| eq:C.16-dipole Γ = e_c²ω³\|r\|²/3π = (4/3)αω³\|r\|² | CHECKED | Dimensions eV. |
| H 2p→1s: \|r_fi\|² = 2¹⁵/3¹⁰ a₀² per m; τ = 1.60 ns | CHECKED | sympy radial/angular integral 32768/59049; τ = 1.595 ns (measured 1.596 ns). |
| k(10 eV) = 5.1e-3 Å⁻¹ | CHECKED | 5.07e-3. |
| Classical-current amplitude c = i(2Vω)^{−1/2}ε*·J̃; eq:C.16-classical ω/16π³ | CHECKED | J̃ convention e^{iωt − ik·r} as in A.3. |
| Sudden kick J̃ = iе_c v/(ω − k·v + i0); eq:C.16-soft = (2α/3π)v²/ω | CHECKED | Standard soft (Larmor) spectrum; ω dN/dω flat. |
| Medium: k = n_rω, DOS ∝ n_r²n_grp; ⟨u⟩ = ¼[d(ωε)/dω\|E₀\|² + \|B₀\|²] → factor n_r n_grp | CHECKED | Bracket = 2n_r n_grp ω²\|A₀\|². |
| eq:C.16-medium Γ_med = n_r Γ_vac (n_grp cancels) | CHECKED | Conditions (transparency, local field = 1) stated. |
| C.16, ¶ "The field as oscillators": classical amplitude α_kj | GAP (notation) | α_kj clashes with the fine-structure constant α, used two paragraphs later in eq:C.16-dipole, and is in no NOTATION row or local list. Rename (e.g. a_kj or 𝔞_kj) or write c_kj(2Vω_k)^{1/2} directly. |

Chapter use: 12.6 (eq:12.6-classical = n_r·eq:C.16-soft with e_c²/e²; "classical result of C.16 for a sudden kick"; medium mode
normalization) CHECKED.

## C.17 Point and space groups

| Location | Verdict | Note / correction |
|---|---|---|
| eq:C.17-compose (product and inverse) | CHECKED | |
| Improper R = (−1)(−R), θ_R of −R; mirror = inversion × C₂ about normal | CHECKED | |
| 32 point groups; Si/Ge m3̄m, GaAs 4̄3m, 432, quartz/Te 32 | CHECKED | |
| eq:C.17-orth; multiplicity n_a | CHECKED | Standard. |
| eq:C.17-ninv proof (projector Q) | CHECKED | |
| D₃ characters and the two orthogonality checks | CHECKED | (4+2+0)/6 = 1; (2−2+0)/6 = 0. |
| eq:C.17-polar c_V = det·(1+2cosθ), c_A = 1+2cosθ; Y_l character ×(−1)^l for improper | CHECKED | |
| Centrosymmetric ⇒ no odd-rank polar invariant; TR removes odd part of scalar S(q,ω) | CHECKED | |
| Reciprocity χ_ij(q) = χ_ji(−q) ⇒ γ_ijl antisymmetric in ij ⇒ ε_ijm g_ml | CHECKED | |
| eq:C.17-gyration (key result) | CHECKED | |
| we:C-gyration: Td class values 9,0,1,−1,−1 → N_gyr = 0; c_V³ 27,0,−1,−1,1 → 1 (\|ε_ijl\|); 432 → 1; m3̄m → 0 | CHECKED | Enumeration of the 48 matrices reproduces all four counts; D₃ gives 2 (as used in 14.5). |
| Fd3̄m: origin on atom, Td ops with t = 0, others with τ₂; {−1\|τ₂} = inversion through τ₂/2; F4̄3m symmorphic | CHECKED | |
| eq:C.17-glide: fixed plane x = a/8, glide vector (0,a/4,a/4); τ₂ → a₁ = (a/2)(0,1,1); g² = {1\|a₁} | CHECKED | numpy; a₁ as in eq:3.1-fcc. |
| Extinctions: f_G = e^{iG·τ₂}f_{m_xG}; eq:C.17-extinct (k+l ≡ 2 mod 4); (222) not in an m_x-type plane | CHECKED | Sign convention e^{+iG·r} as in sec:3.1 / A.3. (222) lies in the σ_d plane x = y, which is in 4̄3m with t = 0, so no extinction: consistent. |
| "with components f_G (eq:3.1-fG)" | GAP (pointer) | eq:3.1-fG is the sum-of-atoms formula, not the definition of f_G for an arbitrary periodic function. Point to eq:A.3-periodic (the general definition, which the next sentence uses). |
| Bloch label of gψ is m_x k; eq:C.17-parity λ = ηe^{−ik·w/2}; relabel k → k−G gives ηe^{−iG·w/2} | CHECKED | |
| Vertex conjugation e^{−iq·τ₂}; phase e^{iq·(w/2−τ₂)}, w/2 − τ₂ = (a/4)(−1,0,0) | CHECKED | |
| eq:C.17-selection | CHECKED | Same rule as eq:13.9-glide (with m_z, w = (a/2)(1,1,0), −π for (2̄00)). |
| "At k = q = 0 and G = (2π/a)(0,2,0), eq:C.17-selection requires a state to have opposite parity to itself" | WRONG (wording) | With q = 0 the vertex is 1 and the reduced final momentum would be −G, not the state itself; the diagonal element is then 1, not 0. The intended case is the transfer q = G. Correction: "At k = 0 and q = G = (2π/a)(0,2,0), so that the reduced final momentum k + q − G is again 0, eq:C.17-selection requires …". |
| X-point twofold degeneracy of every band (no SOC) | CHECKED | Standard for O_h⁷. |

Chapter uses: 3.1, 3.2, 3.4 (glide extinction of (200)), 10.5 (fractional-translation phases), 13.3 (eq:C.17-orth, eq:C.17-parity),
13.9 (parity, selection, glide, extinct; its WE redoes the m_z case consistently), 14.5 (ninv, polar, gyration, WE values for D₃,
Td) all present in the form used. CHECKED.

## C.19 Magnetic neutron scattering

| Location | Verdict | Note / correction |
|---|---|---|
| γ_n = −1.913, μ_N = e/2m_p, M_e = −2μ_B s_e | CHECKED | |
| HL magnetostatics; eq:C.19-field B = P_T M | CHECKED | q×(B−M) = 0, q·B = 0. |
| Born constants (m_n/2π)·2γ_n(e/2m_p)(e/2m_e) = γ_n r_cl with m_n = m_p to 0.14 % | CHECKED | m_n/m_p − 1 = 0.138 %. |
| r_cl = 2.818 fm; (γ_n r_cl)² = 0.2906 b | CHECKED | 2.8179 fm; 0.2906 b. |
| eq:C.19-amplitude sign and Fourier convention | CHECKED | ⟨p′\|V\|p⟩ = ∫e^{iq·r}V with q = p − p′ matches s_e(q) = Σe^{iq·r_i}σ/2. |
| eq:C.19-cross with S_ab of eq:4.2-Sab (2π/V, O_a† left) | CHECKED | Σ_a s_⊥a†s_⊥a = Σ s_a†P_ab s_b; V/2π restores extensivity; dimensions area/energy. |
| Equivalence to Berlin et al. Eq. (26) | CHECKED | Their prefactor γ²e⁴Ω_c/(8m_e²(2π)³N_f) = (γr_cl)²Ω_c/(4πN_f); with χ″ = 2(1 − e^{−βω})S_ab it is eq:14.4-PT. |
| Sentence citing Eq. (26) "per formula unit and with σ in place of σ/2" | GAP (minor) | Omits the second convention difference that 14.4 and F-rows state (their π/V against 2π/V, and χ″ = 2(1−e^{−βω})S). Either add "and with their susceptibility χ″_ab = 2(1 − e^{−βω})S_ab" or drop the convention clause and leave the comparison to 14.4. |
| eq:C.19-spinonly; l = 0 only; ⟨j_l⟩ integrals | CHECKED | |
| Dipole form factor: 2S⟨j₀⟩ + L(⟨j₀⟩+⟨j₂⟩) = g_J[⟨j₀⟩ + (2/g_J − 1)⟨j₂⟩]J | CHECKED | With S = (g−1)J, L = (2−g)J. 14.4's quenched-ion form ⟨j₀⟩ + (1 − 2/g)⟨j₂⟩ (L = (g−2)S) is a different, also correct case; 14.4 uses eq:C.19-dipole only for J multiplets. Consistent. |
| (g_J/2)J = S + L/2; spin probe sees (g_J − 1)J | CHECKED | |
| eq:C.19-polar matrix elements | CHECKED | ⟨−\|σ·s\|+⟩ = s₁ + is₂. |
| Spin-flip channels: P∥x → S_yy+S_zz, P∥y → S_zz, P∥z → S_yy; chiral difference; S_xx in no channel | CHECKED | |

Chapter uses: 7.1 (form factor, falls off at a few Å⁻¹), 14.1 (spinonly), 14.3 (moment (g_J/2)J), 14.4 (cross, field, amplitude,
polar, dipole, DW inside S_ab) present in the form used. CHECKED.

## C.20 Dissipative two-level systems and kinks

| Location | Verdict | Note / correction |
|---|---|---|
| eq:C.20-H; Δ_tl; eq:C.20-J; eq:C.20-ohmic J_s = 2πα_ohm ω e^{−ω/ω_cut} | CHECKED | Maps onto Leggett et al.: λ = q₀C/(2mω)^{1/2} gives πΣλ²δ = q₀²J_Leggett, α = q₀²η/2π. Qureshi's K is the same α (his Γ(1−2K)cos πK factors). |
| Superohmic ω³ for strain coupling | CHECKED | λ² ∝ Q²/ω ∝ ω, DOS ω². |
| Completed square; δ_k = λ_k/ω_k; H_R = D H_L D† | CHECKED | |
| [X,Y] = −2iδ² sin ωt; BCH; Bloch identity; eq:C.20-Q | CHECKED | By hand with eq:C.6-BCH, eq:C.6-bloch. |
| T = 0 one-mode Poisson series; energy-release sign | CHECKED | ∫e^{iΔ_as t}C(t) → δ(Δ_as − nω), L higher by Δ_as. |
| Ohmic imaginary part → πα sgn t; log integral ½ln(1+Ω²t²); sinh product | CHECKED | Numerical quadrature and product to 2e5 terms. |
| eq:C.20-Qohm; linear growth beyond 1/T; \|C\| = (ω_cut\|t\|)^{−2α} at T = 0; static overlap diverges | CHECKED | |
| eq:C.20-rate via eq:2.5-corr at zero probe energy | CHECKED | ⟨O†(t)O⟩ = e^{iΔ_as t}C(t). |
| Phases e^{∓iπα} for t ≷ 0; strip analyticity; contour t = x − i/2T | CHECKED | |
| sech^{2α} Fourier transform = 2^{2α−1}\|Γ(α+iν/2)\|²/Γ(2α) | CHECKED | Quadrature, two (α, ν) pairs, 1e-15 agreement. |
| eq:C.20-ohmrate (key result) and detailed balance | CHECKED | Against the direct time integral with the full ω_cut-regularized 𝒬(t) at ω_cut = 10⁴T: agreement to 1e-4 for α = 0.2, 0.35, Δ_as = 0, 1.5T. Dimensions eV. |
| Symmetric form √πΓ(α)/Γ(α+½)(πT/ω_cut)^{2α−1}; scales as T^{2α−1} | CHECKED | Duplication formula; numerical. |
| α ≪ 1 limit Δ̃₀²/γ₀ of Qureshi Eq. (10) | CHECKED | Source: γ₀ = KΘ = 2πKT, Δ̃₀ = Δ₀(Θ/ω_c)^K[Γ(1−2K)cos πK]^{1/2}; C.20 sum → Δ₀²/(2παT). |
| eq:C.20-Dr (Leggett's Δ_r); dependence on Δ₀²ω_cut^{−2α} only | CHECKED | Also checked: 2Γ_LR with eq:C.20-Dr equals eq:16.8-scaling exactly (reflection formula), as 16.8 claims. |
| Adiabatic argument exponent α/(1−α); coherent below T ~ Δ_r for α < ½; localization α ≥ 1 | CHECKED | Standard (Leggett et al.). |
| eq:C.20-FK; eq:C.20-discrete | CHECKED | ∂/∂u_n of V_s sin² gives (πV_s/a)sin(2πu/a). |
| eq:C.20-sG: c_ch, ω_s² = 2π²V_s/M_κa² (single-atom frequency) | CHECKED | |
| First integral; d_kink = a²[K/2π²V]^{1/2}; eq:C.20-kink | CHECKED | Matches Fitzgerald Eq. (2), μ = 1/d_kink. |
| sin²(2 arctan e^{−s}) = sech²s; local equality of spring and substrate energy | CHECKED | |
| eq:C.20-Ekink = 4V_s d/a = (2a/π)(2V_sK)^{1/2} | CHECKED | = Fitzgerald Eq. (3), β = K_ch, V₀ = V_s. |
| Lorentz invariance; eq:C.20-mass (2/π²)(a/d)M_κ; 7 % at d = 3a | CHECKED | 0.0675. |
| sech² transform πkd²/sinh(πkd/2); Poisson form vs eq:C.2-poisson | CHECKED | Quadrature; C.2 convention maps with spacing a, sign of exponent irrelevant (±m summed). |
| eq:C.20-PN coefficient 8π²V_s d²/a² · m cosech(π²md/a); m = 0 → E_kink | CHECKED | Direct lattice sum E(0) − E(a/2) equals the m = 1 peak-to-peak value. |
| eq:C.20-EPN; 3e-6 V_s at d = 2a; min at z₀ = a/2 | CHECKED | 3.38e-6. |
| Discrete relaxation: barrier 22 % lower at d = a, 17 % at 1.23a, gap closes | CHECKED | Relaxed chain (241 atoms): −22.4 %, −17.3 %; also −10.0 % at 1.74a and −7.5 % at 2a, as 19.6 and fig:19-limit-crowdion state. |
| Citation of Fitzgerald for the barrier (Eq. (4) only) | GAP (source remark) | Fitzgerald's own series, Eq. (5), carries 2π²V₀/(μ²a²), a factor 4 below eq:C.20-PN, and his Eq. (6) is a factor 2 below eq:C.20-EPN (the F-row of lim:19.6b records the factor 2). C.20 is right (lattice sum and relaxed chain confirm). Since C.20 cites the source at this step, one clause would prevent a reader's mismatch: "… Eq. (4); the series of that reference, Eq. (5), is smaller by 4." No novelty wording needed. |

Chapter uses: 16.7 (H without bath, Pauli matrices), 16.8 (J, ohmic, rate, ohmrate, Dr, NIBA = Qureshi, γ₀ = 2παT), 19.6 (FK, kink,
Ekink, mass = M_cr, EPN, discrete deviations; tungsten d_kink 1.59–2.25a, E_kink 6.4–9.0 eV, barrier 1.2e-4–3.6e-7 eV recomputed),
D.42 (J_s, 2J_s spectral function, ohmic normalization), E.22, F-rows: present in the form used. CHECKED.

## Notation drift (against NOTATION.md)

All C.15–C.20 symbols have rows (lines 336–337, 603–604, 1014, 1030–1031, 1378–1410) or appear in the locals of clash entry 74;
upright Γ(z) and italic \varGamma are used as STYLE requires; 𝒬(t) is distinguished from 10.9's 𝒬. Exceptions:
- C.16 α_kj (classical mode amplitude): clash with α, no row (GAP above).
- C.20 uses p for "a number of order one" in the adiabatic argument and s = (z − z₀)/d_kink in the energy integral, both
  undeclared locals (p is momentum, s_e the spin density); harmless but could be listed in entry 74's C.20 locals. (Note only.)
- d_kink: ignored per brief (parallel rename).

## SPINE "Used by" lists

| Row | Verdict | Note |
|---|---|---|
| C.15 "10.6, 10.9, 12.5" | GAP | Also cited by 3.5, 7.3, 8.1, D.24, D.34. |
| C.16 "12.6" | CHECKED | |
| C.17 "13.9, 14.5" | GAP | Also 3.1, 3.2, 3.4, 10.5, 13.3 (and C.18). |
| C.19 "14.4" | GAP | Also 7.1, 14.1, 14.3. |
| C.20 "16.8, 19.6" | GAP | Also 16.7, D.42, E.22. |

Each extra user cites a result that exists here in the form used; only the SPINE rows are incomplete.
