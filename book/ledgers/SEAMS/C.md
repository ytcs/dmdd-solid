# SEAM: Appendix C.1–C.8 (Mathematical tools)

Length (wc on .tex, math included): total 12,930 for C-1 … C-8
(spine 15,500 for C.1–C.8; nothing padded, every step written out). appC.tex now inputs C-1 … C-8 before C-9; the `\setcounter{section}{8}`
line and its comment are removed.
Build: full main.tex in /tmp/build-C: 0 LaTeX errors, 0 overfull boxes in C-1 … C-8, no undefined citations from C (the only undefined
citation in the build, kubo1957statistical, comes from ch04/s4-1.tex, another writer's section).
Lint: remaining hits are false positives (LONG-SENT merges across a display that ends a sentence; EQ-PUNCT on a `cases` display whose
period is inside `cases`, C-2 l. 31).
Figures: none (spine lists none). Bib appended (DOIs checked against Crossref, 2026-11-02): olver2010nist (DLMF; equation numbers read
from dlmf.nist.gov, extracts in sources/C/), monkhorst1976special, blochl1994improved, vonderlage1947method, toll1956causality,
kronig1926theory, baym1961determination, colpa1978diagonalization, mermin1966short (DOI 10.1063/1.1704995), wilcox1967exponential,
isserlis1918formula, lindhard1954properties (no DOI; for 4.5). No arXiv entries added.
Numbers checked by script (scratchpad checks.py, bog.py): erf(2.286) = 0.99877, erf(1.0525) = 0.86338 (series, 9 terms), erfc asymptotic
1.329e-3 → 1.238e-3 vs exact 1.227e-3; central lobe 90.3%; Y^c_4 normalization and its Y_4m form; ∫r³e^{−βr}j_1 = 8βq/(β²+q²)³;
Lorentzian test 1/(1+Γ/2); Matsubara sum (2n_B+1)/(2ω₀); elliptic reductions (μ₀ = 2, μ₁ = 1.3); K log limit; boson Bogoliubov
(ω₀ = 1, g₀ = 0.6: E_b = 0.8, ground −0.2, sinh²θ = 0.125, truncated Fock space) and fermion Bogoliubov (4×4 Fock matrices, exact).

## The reader now knows
- C.1: δ as a distribution; squeezed families t f(tx) → δ (Gaussian, Lorentzian, golden-rule function); Gaussian corrections O(1/t²) vs
  slow-tail corrections O(1/t). Dirichlet integral; ∫sin²u/u² = π (eq:C.1-sinsq) and its Parseval reading (area 2πt); the golden-rule
  limit with its correction ½ fp∫w/ξ² (eq:C.1-sincorr, proves eq:2.1-deltalimit and the 1/(tδ_w) estimate of 2.1); sin(ξt)/ξ → πδ
  (eq:C.1-sinc); δ(g(x)) (eq:C.1-deltag) and the surface form (eq:C.1-surface); completeness (eq:C.1-complete), Parseval
  (eq:C.1-parseval), convolution theorem (eq:C.1-conv, used by Helm in 2.2); origin of +i0⁺ (eq:C.1-causal).
- C.2: Dirac comb and Poisson summation (eq:C.2-comb, -poisson): sum → integral error = image terms g̃(mL); exponential vs power-law
  convergence; δ needs broadening first; density of states (eq:C.2-dos), van Hove singularities; Bravais/reciprocal working definitions;
  lattice sum Σ_R e^{ik·R} = NΣ_G δ_{kG} (eq:C.2-latticesum) **derived here** (3.1 should point back, not rederive); k-point counting,
  zone volume; unfolding Σ_q = Σ_k Σ_G (eq:C.2-unfold); grid-average error = Fourier components at supercell vectors (eq:C.2-grid);
  insulators exponential, metals slow; Monkhorst–Pack (named); broadening σ_br vs grid; Gaussian preferred to Lorentzian; tetrahedron
  method (named); N/V bookkeeping.
- C.3: eq:C.3-j0, eq:C.3-j1 (the two integrals of 2.2), Laplace-transform radial integrals (1s→2p check); angular moments
  (eq:C.3-moments) and the general formula ⟨(n^x)^{2a}(n^y)^{2b}(n^z)^{2c}⟩; Y_lm (Condon–Shortley), orthonormality, Legendre, addition
  theorem, Unsöld (eq:C.3-unsold, closed shells of 2.2); Rayleigh plane-wave expansion **derived** via Rodrigues + recursion
  (eq:C.3-planewave); j_l limits and the multipole picture (q r_orb ~ 1 at q ≈ 2 keV); cubic harmonics: why l = 1, 2, 3 are absent,
  Y^c_4 normalized (eq:C.3-cubic), counts at l = 6, 8, 10, 12; second-rank tensors of cubic crystals are isotropic; anisotropy starts at
  l = 4 (→ 10.7).
- C.4: PV with the subtraction form (eq:C.4-PV); general proof of Sokhotski–Plemelj for Lipschitz w (eq:C.4-SP); Cauchy integral and
  Plemelj jump relations (eq:C.4-cauchy, -jump); rules: xδ = 0, x PV(1/x) = 1, boundary-value difference (eq:C.4-difference),
  d ln|x|/dx = PV, d PV(1/x)/dx = −fp(1/x²) (eq:C.4-dPV), 1/(x ± i0)² = fp(1/x²) ± iπδ′ (eq:C.4-square); pinch vs one-sided double pole;
  normalized Lorentzian δ_Γ(x) (eq:C.4-lorentz) with corrections linear in Γ_w (eq:C.4-lorentzcorr) and the 1/(1+x²) test; widths add
  under convolution; Voigt keeps the tails; summary of the folded (numerically finite) forms.
- C.5: causality ⇒ analyticity for Im z > 0 (eq:C.5-Rz), poles below the axis (A.3/A.7 conventions); spectral form with ϱ_R = −Im R/π
  (eq:C.5-spectral); large-z expansion, R ≃ 𝓃_e q²/(m_e z²) from the f-sum (eq:C.5-highfreq); KK derivation (eq:C.5-KK) and half-axis
  forms (eq:C.5-KKhalf); which functions obey KK: ε⁻¹ − 1 always (static form eq:C.5-screening, perfect-screening sum rule ∫L/ω = π/2);
  ε − 1 only without zeros in Im z > 0 and with a gap (eq:C.5-KKeps, ε_∞ from ε₂), metallic pole subtracted; KK + large-ω ⇒ ∫ωε₂ = πω_p²/2;
  Matsubara residues, frequency-sum formulas (eq:C.5-matsum) with the oscillator example (2n_B + 1)/(2ω₀); analytic continuation,
  non-uniqueness (e^{βz} − 1)h(z) and its removal by decay (Baym–Mermin); Padé caveat (→ E.3).
- C.6: Gaussian integral with complex parameters (eq:C.6-gauss), Fresnel, Gaussian transform e^{−q²s²/2}; moments (eq:C.6-moments);
  generating function (eq:C.6-generating); n-dim (eq:C.6-gaussn); Isserlis/Wick (eq:C.6-isserlis); Hadamard lemma (eq:C.6-hadamard);
  BCH for central commutator (eq:C.6-BCH); displacement operator D̂(α_d) (eq:C.6-D), kick e^{iqx} = D̂(iqℓ₀); coherent state and Poisson
  distribution (eq:C.6-coherent), mean deposit q²/2M, Si 60 meV mode: q²ℓ₀² = 1 at q = 56 keV; Huang–Rhys (→ 5.6); normal ordering
  (eq:C.6-normal); Bloch identity ⟨e^Â⟩ = e^{⟨Â²⟩/2} **stated** (eq:C.6-bloch; proof D.15); ⟨x²⟩ = ℓ₀²(2n_B + 1); product formula
  (eq:C.6-product) as the generating formula of 5.6 (e^{−2W} e^{⟨(q·u(t))(q·u(0))⟩}).
- C.7: PSD equivalences (incl. the "all principal minors" caveat), Cauchy–Schwarz (eq:C.7-CS); S_ab is PSD (Gram form) and the
  interference bound; block LDU factorization, inverse and determinant (eq:C.7-block); head formula 1/(M⁻¹)₀₀ (eq:C.7-head) for
  ε_mac (→ 4.4, D.7); Löwdin/Feshbach partitioning (eq:C.7-partition; 2.4 level shift as its second order; → 8.6); Dyson-type equation
  (eq:C.7-dyson), series vs closed form, collective modes at det(1 − X₀K) = 0; R = R̃/ε, TDDFT, 𝖦⁻¹ = 𝖦₀⁻¹ − Σ; Woodbury
  (eq:C.7-woodbury); boson Bogoliubov (eq:C.7-Hboson, -Eboson): tanh 2θ_b = g₀/ω₀, E_b = (ω₀² − g₀²)^{1/2}, zero-point occupation
  sinh²θ_b, instability for |g₀| ≥ ω₀; para-unitary matrix form ηh, Colpa's positivity condition; fermion Bogoliubov (eq:C.7-Hfermion,
  -Efermion): tan 2θ_f = g₀/ξ₀, E_f = (ξ₀² + g₀²)^{1/2}, gap; mapping to u^B, v^B (7.2) and u^M, v^M (7.1).
- C.8: erf/erfc (eq:C.8-erf), finite interval (eq:C.8-interval = eq:D.1-erf), ∫y²e^{−y²} (eq:C.8-y2 → eq:1.2-nesc); Taylor series
  (eq:C.8-series) and asymptotic series (eq:C.8-asymptotic) with the 1.2 numbers; K(s), E(s) (eq:C.8-KE) with modulus s, series
  (eq:C.8-KEseries), log limit (eq:C.8-Klog), reduction of ∫₀^π(μ₀ + μ₁ cos φ)^{∓1/2} (eq:C.8-reduce) and its link to eq:1.2-angle (daily
  averages); Lindhard static function F_L(y) (eq:C.8-FL) and limits (1 − y²/3, ½ with log-divergent slope at y = 1, 1/(3y²)); branch
  rule ln[(u+1+i0)/(u−1+i0)] = ln|…| − iπΘ(1−|u|) (eq:C.8-branch), also from Sokhotski–Plemelj.

## Pointing sentences checked (grep of ch01, ch02, appA, appD)
- s2-1 l.35, l.40 (C.1: ∫sin²u/u² = π; proof of eq:2.1-deltalimit) → eq:C.1-sinsq, eq:C.1-sincorr; the derivative limit → eq:C.1-sinc.
- s2-1 l.124 (C.2: continuum limit incl. BZ sums) → C.2 throughout.
- s2-2 l.12 (C.1: δ(g(x)) for a simple root) → eq:C.1-deltag with the 2.2 example.
- s2-2 l.77, 84, 96, 203 (C.3: Unsöld; 4π sin(qr)/qr; 4πi j₁; 4π sin/qr for Helm) → eq:C.3-unsold, -j0, -j1.
- s2-4 l.127, 150 (C.4: general SP proof; collects definitions) → eq:C.4-SP and the summary subsection.
- s1-2 l.31, s1-3 l.174, D-1 l.10 (C.8: error function) → eq:C.8-erf, -interval, -y2.

## Symbols introduced (proposed below)
w(x) test function (extends 2.4's local use to App. C); δ_Γ(x) normalized Lorentzian; dΩ_n̂ solid angle of direction n̂; n^α
components of a unit vector; Y_lm, P_l, j_l (already used in 2.2), Y^c_l cubic harmonics; ℱ generic function in C.2 and Cauchy integral
ℱ(z) in C.4; σ_br broadening width; ϱ_R spectral density; X_c, x_c cut-offs; K(s), E(s), s, s′ elliptic; F_L(y) static Lindhard
function; ω₀, ℓ₀ oscillator (2.5 already uses ω₀); D̂(α_d), α_d; μ, η Gaussian parameters (C.6 only); μ₀, μ₁ coefficients of μ₀ + μ₁cos φ (C.8); Â, B̂, X̂, Ŷ
generic operators; bold upright matrices 𝐌, 𝐀, 𝐁, 𝐂, 𝐃, 𝐍, 𝐔, 𝐖, 𝐊, 𝐗, 𝐓, 𝐡, 𝛈; ω₀, g₀, ξ₀, E_b, E_f, θ_b, θ_f, u^b, v^b, u^f, v^f,
d̃_j, c̃_j (C.7).

## Promises made to later sections
- 3.1: use eq:C.2-latticesum (derived here) and the counting; define 𝐛_i, BZ, BvK fully (C.2 gives one-line working definitions).
- 4.1/4.3: analyticity and KK are in C.5 (eq:C.5-KK, -KKhalf); 4.3 may cite them instead of rederiving. 4.4: ε_∞ − 1 from ε₂ and
  ∫ωε₂ = πω_p²/2 via eq:C.5-KKeps. 4.5: eq:C.8-FL, -branch; perfect screening eq:C.5-screening.
- 4.7/4.8/D.10: Matsubara sums eq:C.5-matsum; continuation conditions. 4.4/D.7: eq:C.7-head. 4.6, 4.7: eq:C.7-dyson.
- 5.3/5.6/D.15: eq:C.6-bloch is stated here and must be proved in D.15; 5.6 uses eq:C.6-product and eq:C.6-coherent (S_HR).
- 7.1/7.2: eq:C.7-Eboson, -Efermion; 7.1's antiferromagnet uses the para-unitary form. 8.6: eq:C.7-partition.
- 10.7: cubic harmonics eq:C.3-cubic (S_ℓ uses the same index; the book writes l in 2.2 and C.3, ℓ in NOTATION's S_ℓ row).
- E.1: k-point grids and smearing (C.2 names them). E.3: Padé continuation caveat.

## Undefined references from C.1–C.8 (all to unwritten targets)
app:D.7, app:D.10, app:D.15, app:E.1, app:E.3, sec:3.1, 3.3, 3.6, 4.1, 4.2, 4.4, 4.5, 4.6, 4.7, 4.8, 5.3, 5.6, 6.1, 7.1, 7.2, 8.6, 10.7,
11.4.

## Open questions / for the editor
1. **Elliptic integrals.** The brief says C.8 must deliver "the elliptic integrals that 1.2 and 1.3 use", but no sentence in 1.2 or 1.3
   uses or points to them (only erf is cited, s1-2 l.31, s1-3 l.174). C.8 gives K, E as the spine specifies and ties them to
   eq:1.2-angle (daily averages of |v_E − v n̂|^{±1}) without inventing a Chapter-1 use. Either 1.2 adds such a use or the spine entry
   drops "1.2, 1.3" for the elliptic part.
2. Notation choices to confirm: K(s), E(s) upright with modulus s (k is a crystal momentum; italic K is unused in Part I, E is energy);
   cubic harmonics Y^c_l (italic K_ℓ avoided); δ_Γ(x) for the normalized Lorentzian (script L would clash with C.9's Lagrangian);
   bare μ and η as Gaussian parameters in C.6 and μ₀, μ₁ in C.8 (bare a, b are reserved; C.8 avoids η because η(v_min) appears there); ℱ for generic functions (bare F is not used).
   C.1 keeps bare f(u), g(x) as generic functions, as A.3 does with f(t).
3. Bloch identity: stated in C.6 with Mermin 1966 cited; the proof is deferred to D.15 per spine. The citation of Monkhorst–Pack,
   Blöchl et al. and Colpa is by paper, without an equation number (closed access, not fetched).
4. A.3 writes Ω for a transition energy (l.33), which clashes with bare Ω = cell volume; C.1 uses ΔE = E_f − E_i instead.
5. C.6 uses M = 26.06 GeV for the silicon nucleus, the value of we:1-nuclear.
6. C.4's section title is "Singular denominators" (the spine title "Principal value, …, Lorentzian limits" fails the noun-phrase
   rule); all four topics are covered.

## Proposed ledger rows (the editor merges them)
NOTATION:
| w(x) | test function in distribution identities (2.4, App. C) | — | 2.4 |
| δ_Γ(x) | normalized Lorentzian (Γ_w/2π)/(x² + Γ_w²/4) | eV⁻¹ | C.4 |
| dΩ_n̂, n^α | solid-angle element of the direction n̂; Cartesian components of a unit vector (superscript index) | sr; 1 | C.3 |
| Y_lm, P_l, j_l | spherical harmonics (Condon–Shortley), Legendre polynomials, spherical Bessel functions | 1 | 2.2 |
| Y^c_l(n̂) | cubic harmonic of order l (superscript c mandatory) | 1 | C.3 |
| ℱ | generic function in a sum or Cauchy integral (C.2, C.4 only; script F) | — | C.2 |
| σ_br | broadening width of a delta function on a grid (subscript mandatory) | eV | C.2 |
| ϱ_R(ω) | spectral density −Im R/π of a response (subscript mandatory; ϱ̂ is the density matrix) | as R/eV | C.5 |
| K(s), E(s), s, s′ | complete elliptic integrals (upright, argument mandatory), modulus and complementary modulus | 1 | C.8 |
| F_L(y) | static Lindhard function, y = q/2k_F | 1 | C.8 |
| ω₀, ℓ₀ | single-oscillator energy; its zero-point length (2Mω₀)^{-1/2} | eV; Å | 2.5 |
| D̂(α_d), α_d | displacement operator and its complex amplitude (subscript d mandatory; α is the fine-structure constant) | 1 | C.6 |
| Â, B̂, X̂, Ŷ | generic operators in exponential identities (hats mandatory) | — | C.6 |
| μ, η (bare) | parameters of a Gaussian e^{−μx² + ηx} (C.6 only) | — | C.6 |
| μ₀, μ₁ | coefficients of μ₀ + μ₁ cos φ in elliptic reductions (C.8 only) | — | C.8 |
| 𝐌, 𝐀, … (bold upright) | generic matrices; 𝐍 = (𝐌/𝐃)⁻¹; 𝐌/𝐃 Schur complement | — | C.7 |
| ω₀, g₀, ξ₀ | diagonal energy and pairing amplitude of a two-mode quadratic Hamiltonian (C.7 only) | eV | C.7 |
| E_b, E_f, θ_b, θ_f, u^b, v^b, u^f, v^f | boson/fermion Bogoliubov energies, angles and coefficients (upright b, f mandatory) | eV; 1 | C.7 |
| d̃_j, c̃_j | Bogoliubov-transformed boson and fermion operators | — | C.7 |
Clash notes: δ_Γ vs δ(x) (decorated δ, as δ_w in 2.4); Y^c vs Y_q, Y_ph, Y_qp (yields; superscript c only here); E(s) vs energies
(upright, argument); s vs s_e(q), s_κ(q), s_skin (bare s only as the modulus in C.8 and a Gaussian width in C.6); μ bare vs reduced
masses (decorated); η bare vs η(v_min) (argument) and η_anh; σ_br joins the decorated σ family (entry 32); u^b/u^f join entry 35.
GLOSSARY:
| distribution | linear rule assigning a number to each test function; δ, PV, fp are distributions | C.1 |
| Poisson summation formula | Σ_n F(n) = Σ_m ∫F(y)e^{2πimy}dy; sum-to-integral error as image terms | C.2 |
| van Hove singularity | divergence of 1/|∇ε| at a stationary point of a band; kink (3D) or log (2D) in the DOS | C.2 |
| Monkhorst–Pack grid | uniform (possibly shifted) k-point grid | C.2 |
| tetrahedron method | BZ integration with linear interpolation of bands in tetrahedra | C.2 |
| Unsöld's theorem | Σ_m|Y_lm|² = (2l+1)/4π | C.3 |
| Rayleigh expansion | e^{iq·r} = Σ(2l+1)i^l j_l(qr)P_l(q̂·r̂) | C.3 |
| cubic harmonics | functions of direction invariant under the cubic group (l = 0, 4, 6, …) | C.3 |
| Plemelj jump relations | F(x+i0) − F(x−i0) = w, sum = PV transform / πi | C.4 |
| Kramers–Kronig relations | Re R = π⁻¹ PV∫Im R/(ω′−ω), and conversely | C.5 |
| spectral representation | R(z) = ∫ϱ_R(ω′)/(z − ω′) | C.5 |
| analytic continuation (Matsubara) | iω_j → ω + i0⁺ under decay at infinity (Baym–Mermin) | C.5 |
| Baker–Campbell–Hausdorff formula | e^X e^Y = e^{X+Y}e^{[X,Y]/2} for central [X,Y] | C.6 |
| displacement operator, coherent state | D̂ = exp(α_d d† − α_d* d); D̂|0⟩, Poisson number distribution | C.6 |
| Bloch identity | ⟨e^Â⟩ = e^{⟨Â²⟩/2} for Â linear in harmonic variables | C.6 (proof D.15) |
| Isserlis (Wick) theorem for Gaussians | higher moments = sum over pairings | C.6 |
| positive semidefinite matrix | x†Mx ≥ 0 ∀x | C.7 |
| Schur complement | M/D = A − BD⁻¹C | C.7 |
| Löwdin partitioning | effective Hamiltonian H_PP + H_PQ(E − H_QQ)⁻¹H_QP | C.7 |
| Bogoliubov transformation | mixing of creation and annihilation operators; para-unitary (bosons), unitary (fermions) | C.7 |
| error function | erf x = (2/√π)∫₀^x e^{−y²}dy | C.8 |
| complete elliptic integrals | K(s), E(s) | C.8 |
CONCEPTS: "Golden-rule delta limit and its correction" | C.1 | match `eq:C.1-sincorr`. "Sum-to-integral and k-grid errors" | C.2 |
`Poisson`, `eq:C.2-grid`. "Plane-wave expansion and cubic harmonics" | C.3 | `Rayleigh`, `Y^{\mathrm{c}}`. "Distributions of singular
denominators" | C.4 | `eq:C.4-SP`, `eq:C.4-square`. "Causality and Kramers–Kronig" | C.5 | `eq:C.5-KK`. "Matsubara sums" | C.5 |
`eq:C.5-matsum`. "Gaussian/BCH/Bloch identities" | C.6 | `eq:C.6-bloch`. "Schur complement and Dyson equations" | C.7 |
`eq:C.7-block`, `eq:C.7-dyson`. "Bogoliubov transformations" | C.7 | `eq:C.7-Eboson`. "Error function and elliptic integrals" | C.8.
CLAIMS:
- ∫sin²(ξt/2)w/ξ² = (πt/2)w(0) + ½fp∫w/ξ² + o(1) | C.1 | derived.
- Σ_R e^{ik·R} = NΣ_G δ_{kG}; grid error = Σ F_R over supercell vectors | C.2 | derived.
- Rayleigh expansion | C.3 | derived; DLMF 10.60.7. Y^c_4 = (5/8)(21/π)^{1/2}(Σn⁴ − 3/5) = (7/12)^{1/2}Y₄₀ + (5/24)^{1/2}(Y₄₄ + Y₄₋₄) | C.3 |
  derived/checked numerically; Von der Lage–Bethe 1947.
- Sokhotski–Plemelj for Lipschitz w; d PV/dx = −fp; 1/(x+i0)² = fp + iπδ′ | C.4 | derived.
- Lorentzian correction linear in Γ_w (eq:C.4-lorentzcorr) | C.4 | derived (from eq:2.4-split), test case exact.
- KK, half-axis forms, ε⁻¹ − 1 always, ε − 1 for stable gapped media | C.5 | derived; Kronig 1926, Toll 1956.
- Matsubara sum formulas; continuation unique under decay | C.5 | derived; Baym–Mermin 1961.
- Gaussian, Isserlis, BCH, coherent-state Poisson law | C.6 | derived. Bloch identity | C.6 | stated; Mermin 1966; proof D.15.
- Block inverse, Woodbury, partitioning | C.7 | derived. Boson/fermion Bogoliubov spectra | C.7 | derived, checked numerically; Colpa 1978.
- erf series/asymptotics and 1.2 numbers; K/E series, log limit, reductions; Lindhard limits and branch | C.8 | derived/DLMF; checked.
INDEX: distribution; test function; nascent delta function; Dirichlet integral; Riemann–Lebesgue lemma; Parseval's theorem; convolution
theorem; Poisson summation formula; Dirac comb; image terms; density of states; van Hove singularity; Born–von Karman conditions;
lattice sum; Brillouin zone (volume); unfolding; zone average; k-point grid; Monkhorst–Pack grid; smearing; tetrahedron method; solid
angle; angular moments; spherical harmonics; Condon–Shortley phase; Legendre polynomials; Rodrigues' formula; addition theorem; Unsöld's
theorem; Rayleigh expansion; spherical Bessel functions; multipole expansion; cubic harmonics; principal value; Sokhotski–Plemelj
formula; Cauchy integral; Plemelj jump relations; Hadamard finite part; Lorentzian; Voigt profile; causality; analyticity;
Kramers–Kronig relations; spectral representation; perfect-screening sum rule; Matsubara frequency sum; analytic continuation; Padé
approximant; Gaussian integral; Fresnel integral; Isserlis theorem; Hadamard lemma; Baker–Campbell–Hausdorff formula; displacement
operator; coherent state; Poisson distribution; normal ordering; Bloch identity; positive semidefinite matrix; Cauchy–Schwarz
inequality; Schur complement; Löwdin partitioning; Dyson equation; Woodbury identity; Bogoliubov transformation; para-unitary matrix;
error function; asymptotic series; complete elliptic integrals; Lindhard function; Kohn anomaly; branch cut.
