# SEAM: Appendix C.10–C.17 (Mathematical tools, second block)

Length (wc on .tex, math included): C-10 2,067; C-11 2,223; C-12 1,299; C-13 1,009; C-14 1,315; C-15 1,724; C-16 1,303; C-17 2,156;
total 13,096 (spine 12,500 for C.10–C.17). appC.tex inputs C-10 … C-17 after C-9, before \printbibliography.
Build: full main.tex in /tmp/build-C-b: 0 LaTeX errors, 0 undefined citations, one overfull box in C-10 … C-17 (0.17 pt, C-13 l. 35).
Lint: three LONG-SENT hits remain, all false positives where the linter merges a sentence across a display that ends it (C-16
matrix element; C-17 after eq:C.17-ninv and before eq:C.17-gyration). No banned terms.
Figures: none (spine lists none). Sources: sources/C-b/1007.1727.txt (Cowan et al., equation numbers (6), (7), (8), (14) read from the
full text; PDF deleted).
Bib appended (DOIs checked against Crossref, arXiv IDs against the arXiv API, 2026-11-02): krein1977markov (10.1090/mmono/050),
akhiezer1965classical (SIAM reprint DOI 10.1137/1.9781611976397), harris1963theory, feller1971introduction (no DOI), rogosinski1958moments,
shapiro2009semi, fishburn1970intransitive, cowan2011asymptotic (1007.1727), wilks1938large, feldman1998unified (physics/9711021),
foldy1950dirac, bjorken1964relativistic (no DOI), glauber1991quantum, dresselhaus2008group. Chapter or equation pointers only where read or certain (Feller XI.1, Harris I, Dresselhaus 3, Cowan Eqs. (6)–(8), (14), Sect. 3.1);
Krein–Nudel'man, Akhiezer, Shapiro, Rogosinski, Fishburn, Foldy–Wouthuysen, Bjorken–Drell, Glauber–Lewenstein cited without pointers.
Numbers checked by script (scratchpad mk.py, checks.py, ren.py, grp.py):
- C.10: Gaussian H⁻¹, ϱ_MK(0) = 2/3, ϱ_MK(ξ) = 2/(3 + ξ⁴) at ξ = 1, 2, 3, 4, 6, 10; canonical representations at ξ = 0, 0.5, 1.5, 2, 3
  (moments μ₃, μ₄ reproduced to 10⁻¹⁵); band at ξ = 0: [1/6, 5/6]; at ξ = 3: 1 − F ∈ [0, 0.0238] vs true 1.35e−3 (×18); ξ = 4: ×240;
  tail formula on gamma(3): +4.1% at 58σ, +1.3% at 173σ. Degenerate ξ (leading coefficient of 𝖪 zero) at ξ = ±1 for the Gaussian.
- C.11: extinction of 1 − p + ps² (p = 0.3, 0.5, 0.6, 0.75) by iteration; renewal equation for U[0,1] losses solved numerically
  (offset −1/3 to 10⁻⁶ at E = 20); MC (2×10⁵ chains, E = 50): ⟨E_res⟩ = 0.3331, Var N/E = 0.670, Fano 0.336.
- C.14: χ²₁ quantiles 1.000, 2.706, 3.841; one-sided z² 1.642, 2.706; n = 0 asymptotic 0.82 vs exact 2.303; P(A ≻ B) = 0.826;
  MC error 0.0035.
- C.15: q²/8m_e² = 4.8e−5 at 10 keV; Darwin 1s m(Zα)⁴/2 = 0.72 meV, 27.8 eV, 0.760 keV for Z = 1, 14, 32; γ_D − 1 = −0.0052 (Si),
  −0.0276 (Ge). FW commutator algebra checked by hand twice (coefficients 1/2, −1/8, −1/3; double commutator sign).
- C.16: H 2p→1s lifetime 1.595 ns from eq:C.16-dipole; 2α/3π = 1.55e−3.
- C.17: group enumeration: N_gyr = 2 (32), 0 (4̄3m), 0 (m3̄m), 1 (432), 1 (23); rank-3 polar invariants 4, 1, 0, 1, 2; l = 3 invariants
  1, 1, 0, 0, 1. Diamond glide {m_x|τ₂} maps 0 → τ₂, τ₂ → a₁; w = a₁; phases e^{iG·τ₂} for (020), (022), (040).

## The reader now knows
- C.10: Hamburger and Stieltjes problems (truncated, μ₀…μ₄); Hankel matrix 𝐇 PSD (eq:C.10-hankel), shifted 𝐇₁ on the half line;
  reproducing kernel 𝖪(x, ξ) (eq:C.10-kernel, -reproduce); Christoffel function ϱ_MK(ξ) = 1/𝖪(ξ,ξ) (eq:C.10-rho) as the maximal point
  mass; canonical representation through ξ: three real nodes, positive weights, quadrature exact to degree 4 (eq:C.10-quadrature),
  w_ξ = ϱ_MK, **proved**; Markov–Krein band (eq:C.10-band) **proved** by the polynomial-majorant argument (all three node positions);
  Gaussian ϱ_MK = 2/(3 + ξ⁴) (eq:C.10-gauss), 2/3 at the mean; tail ϱ ≃ (μ̄₄ − μ̄₂² − μ̄₃²/μ̄₂)/(ξ − μ₁)⁴ (eq:C.10-tail) = det𝐇/(μ̄₂ξ⁴);
  absolute vs relative (×18 at 3σ, ×240 at 4σ); Stieltjes point-mass bound (eq:C.10-stieltjes).
- C.11: PGF, factorial moments, variance (eq:C.11-pgf, -var); Poisson Fano 1; extinction dichotomy in m̄ proved by convexity; binomial thinning (eq:C.11-thin) and
  F_k = fF + 1 − f (eq:C.11-thinfano) = the F_meas rule of 20.1; Galton–Watson recursion (eq:C.11-gw); extinction = smallest root
  (keyresult), toy (1 − p)/p; minimal solution; type-and-deposit branching functional (eq:C.11-functional) with mean and second-moment
  recursions (eq:C.11-mean, -second) solved by an upward sweep; renewal equation (eq:C.11-renewal); key renewal theorem stated
  (eq:C.11-key, Feller); undershoot law (1 − F)/⟨X⟩ and mean ⟨X²⟩/2⟨X⟩ (eq:C.11-undershoot) **derived**; overshoot same law;
  Wald → N̄ = E/⟨X⟩ + ⟨X²⟩/2⟨X⟩² − 1 (eq:C.11-linear); CLT → Var N ≃ σ_X²E/⟨X⟩³ and renewal Fano σ_X²/⟨X⟩² (eq:C.11-fano); the three
  hypotheses (stationary, non-lattice, finite second moment) with the lattice counterexample −{E/d} and the x⁻² knock-on tail.
- C.12: finite LP, weak duality (eq:C.12-weak), ≤ n positive components (proved); semi-infinite program and dual (eq:C.12-sip);
  dual certificate (eq:C.12-certificate); strong duality hypotheses (compactness, continuity, visibility κ_v, Slater; Shapiro);
  mass bound (eq:C.12-mass); ≤ n streams (Rogosinski) and complementary slackness; one-bin closed form (eq:C.12-onebin);
  discretization bracket with Lipschitz leakage (eq:C.12-leak); role of kernel positivity.
- C.13: strict partial order; interval order (eq:C.13-order) and transitivity; non-transitive incomparability (example); 2+2
  property and Fishburn's representation theorem; semiorders; height (eq:C.13-height) and tiers; tiers are antichains (proved);
  each tier-k member lies below some tier-(k−1) member (proved); sorting algorithm; four-interval example; what a tier does and
  does not assert.
- C.14: Poisson likelihood (eq:C.14-poisson), binned product; Gaussian likelihood (eq:C.14-gauss) and its large-count origin;
  likelihood ratio 𝗍 (eq:C.14-ratio); Wilks; thresholds 1.00, 2.71, 3.84 (eq:C.14-thresholds); one-sided limits (z = 1.282, 1.645);
  small-count failure (0.82 vs 2.303) and Feldman–Cousins named; nuisance ϑ and profile ratio (eq:C.14-profile); Gaussian profiling
  ⇒ widths in quadrature (eq:C.14-quadrature) **derived**; MC propagation, 16/84 percentiles; P(A ≻ B) for lognormals with
  correlation r (eq:C.14-pairwise); MC error.
- C.15: Dirac representation (eq:C.15-gamma), H_D with electron charge −e (eq:C.15-HD), free spinors and normalization
  (eq:C.15-spinor), r^{γ_D−1} behaviour; NR limits of scalar, vector, axial, pseudoscalar bilinears (eq:C.15-bilinears), link to 1.4's
  ALP and scalar couplings, Gordon decomposition; FW transformation with every commutator (eq:C.15-split, -Hprime), power counting and
  second transformation; double commutator (eq:C.15-double); H_FW with mass–velocity, Darwin, spin–orbit (eq:C.15-HFW); Darwin contact
  term and |ψ_ns(0)|² (eq:C.15-darwin), sizes (Zα)²; FW image of e^{iq·r} (eq:C.15-vertex).
- C.16: Coulomb-gauge mode expansion and quantization (eq:C.16-A), number states, n + 1 emission; minimal coupling with e_c
  (eq:C.16-minimal); one-photon rate (eq:C.16-rate); dipole limit and 4αω³|r_fi|²/3 (eq:C.16-dipole), H 2p check; emission by a
  classical current (eq:C.16-classical); sudden-kick soft spectrum (2α/3π)v²/ω (eq:C.16-soft); medium: mode density n_r²n_grp, energy
  n_rn_grp, rate ×n_r (eq:C.16-medium) with transparency and no-local-field hypotheses.
- C.17: {R|t}, composition (eq:C.17-compose); point group, proper/improper, θ_R; symmorphic vs nonsymmorphic, glide, screw; HM and
  Schoenflies names for m3̄m, 4̄3m, 432, 32; representations, characters, orthogonality (eq:C.17-orth); invariant count via projector
  (eq:C.17-ninv) **proved**; D₃ character table; polar/axial characters (eq:C.17-polar); centrosymmetric ⇒ no odd-q response; scalar
  odd-q needs broken inversion and TR (A.4); reciprocity χ_ij(q) = χ_ji(−q) ⇒ only the gyration tensor at linear q; N_gyr formula
  (eq:C.17-gyration); worked example (we:C-gyration): GaAs N_gyr = 0 but one rank-3 invariant, 432 N_gyr = 1; Fd3̄m, F4̄3m symmorphic;
  diamond glide (eq:C.17-glide), g² = a₁; extinction of (200)-class components for every invariant function (eq:C.17-extinct); glide
  parity (eq:C.17-parity) and selection rule with Umklapp (eq:C.17-selection); twofold degeneracy at X (named).

## Symbols introduced (proposed below)
μ_k, μ̄_k; F_P(ξ); 𝐇, 𝐇₁, 𝐯(x), 𝐮(ξ), 𝐜, 𝐚 (bold upright, as C.7); 𝖪(x, ξ); y_i, w_i (nodes and weights, C.10 only); U(x) (C.10
local majorant); 𝔊_N(s), 𝔤(s), N_n, P_ext, m̄ (offspring mean), N_k, f (keep probability), Y, Ȳ(x), \overline{Y²}(x), p_c(x), d_c;
F_loss, ⟨X⟩, σ_X, N(E), N̄(E), S_n, E_res, Z(E), z(E); Ξ, 𝓑, 𝗄_i, 𝖿, 𝗀_λ, λ_i, N_i^up, N_tot, κ_v, Φ_max, Φ_h, h, L_h; ≻, I_a = [ℓ_a, u_a],
h(a) (C.13 local); 𝖫, 𝗍, 𝗍_p, σ_N, σ_ϑ, N̂, N_MC, Φ(z) (standard normal CDF), P(A ≻ B); β_D, 𝛂_D, γ_D, 𝚺, ψ_A, ψ_B, u(p,s), ξ_s, 𝖤, 𝖮,
X, 𝛑, H_D, H_FW, H_Dar; 𝛜_kj, d_kj, H_rad, e_c, M_fi, r_fi, N_γ, J̃(k, ω), n_grp; {𝖱|t}, 𝒫, 𝖣(𝖱), c^{(a)}(𝖱), c_V, c_A, θ_𝖱, 𝖰, n_inv,
χ_ij(q, ω), γ_ijl, g_ml, N_gyr (gyration count), g = {m_x|τ₂}, 𝐰, η (glide parity).

## Promises made to later sections
- 11.5: eq:C.10-band with eq:C.10-rho; Gaussian 2/3 (the spine's worked example 11.6 uses it); tail eq:C.10-tail (the corrected
  coefficient μ̄₄ − μ̄₂² − μ̄₃²/μ̄₂, equal to κ₄ + 2κ₂² − κ₃²/κ₂ in cumulants); Stieltjes refinement only stated at the point-mass level.
- 18.1: eq:C.11-functional, -mean, -second; minimal solution; 18.2: eq:C.11-linear (linear yield, D.44), eq:C.11-fano (renewal Fano
  estimate), eq:C.11-undershoot; the three hypotheses. 20.1: eq:C.11-thinfano.
- 21.2: eq:C.12-certificate, -onebin, -leak; D.46 should cite eq:C.12-mass for the leakage bound.
- 17.6: eq:C.13-order, -height and the antichain/tier facts; eq:C.14-pairwise, 16/84 percentiles.
- 8.8, 21.4, 21.5, 14.6, 19.4: eq:C.14-poisson, -ratio, -thresholds, -profile, -quadrature; the small-count caveat.
- 10.6, 10.9, 12.5: eq:C.15-HFW, -darwin, -vertex, -bilinears.
- 12.6: eq:C.16-rate, -dipole, -classical, -soft, -medium.
- 13.9: eq:C.17-glide, -extinct, -parity, -selection (the tool only; no silicon verdict is stated). 14.5: eq:C.17-gyration,
  we:C-gyration (GaAs, 432; α-quartz is left to 14.5's worked example).

## Undefined references from C.10–C.17 (all to unwritten targets)
sec:8.8, 10.6, 10.9, 11.5, 12.5, 12.6, 13.9, 14.5, 17.6, 18.1, 18.2, 20.1, 21.2, 21.4, 21.5.

## Open questions / for the editor
1. **3.1 vs C.17 on (200).** s3-1.tex (worked example we:3-diamond, second paragraph) says an electron in silicon feels the (200) and
   (222) components of the potential "only through the part that is not of this form, such as the charge that piles up in the bonds".
   The diamond glide makes the (200)-class components of every space-group-invariant function vanish exactly (eq:C.17-extinct); only
   (222) is restored by the bond charge. 3.1 should drop "(200) and" from that sentence (or point to eq:C.17-extinct).
2. **Likelihood symbol.** 𝖫 (sans-serif L) proposed, since ℒ is the Lagrangian density (C.9), L the loss function and Λ the final-state
   class; 𝗍 (sans-serif t) for −2 ln of the ratio (t is time, q momentum, Cowan's q_μ not adopted).
3. **Characters.** c^{(a)}(𝖱), c_V, c_A instead of the usual χ, because χ is the dark matter; irreducible representations labeled by
   (a), not Γ, because upright Γ is the zone center (STYLE). Mulliken labels A₁, A₂, E appear only in the D₃ illustration.
4. **Dirac matrices.** 𝛂_D, β_D (subscript D) to avoid α (fine-structure) and β (1/T); the 1.4 row "ψ, ψ̄, γ^μ, γ⁵ (1.4 only)" must
   be widened to "1.4, C.15, 10.6, 10.9, 12.5". Even/odd operators 𝖤, 𝖮 (sans-serif; ℰ is the macroscopic field).
5. **Photon operators.** d_kj (generic bosons of 2.3) and polarization 𝛜_kj with index j (λ is the exciton label, e_κν(Q) the phonon
   polarization). Charge of the radiating particle e_c (the withdrawn z_e, z_κ are not revived).
6. **Generating-function variable s** in C.11 (local; s is already a spin label, an elliptic modulus in C.8 and a Gaussian width in C.6).
   𝔊 (fraktur) follows the research notation for the branching functional; 18.1 should use the same letter.
7. **C.14 scope.** Budget 1,500; written at 1,300 without padding. The Monte Carlo part covers what 17.6 lists (propagation, 68%
   intervals, P(A ≻ B)); the optimum-interval method of 21.5 is not recapped here (21.5 states it).
8. **Stieltjes band.** The sharp Stieltjes band is stated by reference (Krein–Nudel'man Chap. III) and only its point-mass form
   (eq:C.10-stieltjes) is derived; if 11.5 uses the T = 0 refinement numerically, it needs the full construction (D-item).
9. Section titles shortened to pass the title rule: C.15 "Dirac equation and Foldy–Wouthuysen reduction"; C.11 "Generating functions,
   branching and renewal" (spine: "…, branching processes and renewal theory").

## Proposed ledger rows (the editor merges them)
NOTATION:
| μ_k, μ̄_k | k-th moment and central moment of a normalized distribution (C.10 only; bare μ stays the C.6 Gaussian parameter) | as x^k | C.10 |
| F_P(ξ) | cumulative distribution of P (decorated F family) | 1 | C.10 |
| 𝐇, 𝐇₁ | Hankel matrix μ_{i+j} and shifted Hankel matrix μ_{i+j+1} (bold upright, C.7 convention) | — | C.10 |
| 𝖪(x, ξ) | reproducing kernel 𝐯(x)ᵀ𝐇⁻¹𝐯(ξ) (sans-serif; K(s) is the elliptic integral) | — | C.10 |
| 𝔊_N(s), 𝔤(s) | probability generating function of N; offspring generating function (s local, 0 ≤ s ≤ 1) | 1 | C.11 |
| P_ext | extinction probability | 1 | C.11 |
| F_loss, ⟨X⟩, σ_X | loss distribution of a renewal chain, its mean and width | —; eV | C.11 |
| E_res | undershoot (residual energy) of a renewal chain | eV | C.11 |
| Ξ, 𝓑 | nonnegative velocity measure; its compact domain (C.12) | — | C.12 |
| 𝗄_i(𝐰), 𝖿(𝐰), 𝗀_λ | stream kernel of bin i; bounded functional's kernel; dual function Σλ_i𝗄_i − 𝖿 (sans-serif) | — | C.12 |
| λ_i, N_i^up, κ_v | dual variables; count bounds; visibility constant (C.12 only; λ elsewhere is the exciton label) | 1 | C.12 |
| ≻, h(a) | resolved-above relation of an interval order; height (tier index) | — | C.13 |
| 𝖫, 𝗍, 𝗍_p | likelihood; −2 ln likelihood ratio; its profiled form (sans-serif) | 1 | C.14 |
| N̂, σ_N, σ_ϑ | Gaussian estimate of N_sig and its width; constraint width of a nuisance | 1 | C.14 |
| Φ(z) | standard normal distribution function (C.14, C.11; Φ_max in C.12 is decorated) | 1 | C.14 |
| 𝛂_D, β_D, γ_D | Dirac matrices (subscript D mandatory); γ_D = [1 − (Zα)²]^{1/2} | 1 | C.15 |
| ψ_A, ψ_B | large and small two-component parts of a Dirac spinor | eV^{3/2} | C.15 |
| 𝖤, 𝖮 | even and odd parts of H_D (sans-serif) | eV | C.15 |
| H_FW, H_Dar | Foldy–Wouthuysen Hamiltonian to O(m_ev⁴); Darwin contact term | eV | C.15 |
| d_kj, 𝛜_kj | photon annihilation operator and polarization vector of mode (k, j), j = 1, 2 | 1 | C.16 |
| e_c | charge of a radiating particle (−e for an electron, Z_κe for a bare nucleus) | 1 | C.16 |
| n_grp | group index dk/dω of a medium (n_g is the electron–phonon order of 8.5) | 1 | C.16 |
| {𝖱\|𝐭}, 𝒫 | space-group operation; point group (𝖱 sans-serif; bold 𝐑 is a lattice vector) | — | C.17 |
| c^{(a)}(𝖱), c_V, c_A | irreducible, polar-vector and axial-vector characters (χ is the dark matter) | 1 | C.17 |
| γ_ijl, g_ml, N_gyr | linear-q coefficient of the current response; gyration tensor; number of gyration invariants | — | C.17 |
| η (glide parity) | eigenvalue sign of a glide on Bloch states (C.17 only; η(v_min) has an argument) | 1 | C.17 |
Clash notes: n_g of 8.5 is avoided (group index n_grp, gyration count N_gyr). Φ(z) vs Φ_max (C.12)
vs the force-constant Φ^{(3)} (5.7): decorated or with argument. h(a) (height) vs h_E, Planck h: argument mandatory. 𝖫 joins the
sans-serif family with 𝖦. d_kj joins d_γ (2.3). s (C.11) joins the list of local uses of bare s. η (glide parity, C.17) and η(v_min).
GLOSSARY:
| Hamburger / Stieltjes moment problem | which moment sequences belong to a distribution on ℝ / on [0, ∞) | C.10 |
| Hankel matrix | matrix μ_{i+j} of moments; PSD for any distribution | C.10 |
| Christoffel function | 1/𝐯ᵀ𝐇⁻¹𝐯, the largest mass a distribution with given moments can put at a point | C.10 |
| canonical representation | three-point distribution with the given moments and a node at ξ | C.10 |
| Markov–Krein band | moment bounds on a cumulative distribution, width ϱ_MK(ξ) | C.10 |
| probability generating function | ⟨s^N⟩ | C.11 |
| Galton–Watson process | branching process with independent identically distributed offspring | C.11 |
| extinction probability | smallest root of 𝔤(s) = s | C.11 |
| renewal equation, key renewal theorem | Z = z + Z * F; Z → ∫z/⟨X⟩ for non-lattice F | C.11 |
| undershoot | residual E − S_N(E) of a renewal chain; limit density (1 − F)/⟨X⟩ | C.11 |
| semi-infinite linear program | finitely many constraints on a measure (or infinitely many in the dual) | C.12 |
| dual certificate | dual-feasible λ; proves an upper bound by weak duality | C.12 |
| complementary slackness | optimal streams at zeros of 𝗀_λ; λ_i > 0 only on saturated bins | C.12 |
| interval order | a ≻ b iff ℓ_a > u_b | C.13 |
| antichain, height | set of mutually incomparable elements; 1 + longest chain above | C.13 |
| likelihood, likelihood ratio | probability of the data as a function of parameters; −2 ln ratio to the maximum | C.14 |
| Wilks' theorem | −2 ln λ → χ² with one degree of freedom per parameter of interest | C.14 |
| profile likelihood | likelihood maximized over nuisances at fixed parameter of interest | C.14 |
| Foldy–Wouthuysen transformation | unitary decoupling of large and small Dirac components order by order in 1/m | C.15 |
| mass–velocity, Darwin, spin–orbit terms | O(1/m²) terms of H_FW | C.15 |
| contact density | \|ψ(0)\|², the electron density at a nucleus | C.15 |
| minimal coupling | p → p − e_cA | C.16 |
| dipole approximation | e^{−ik·r} → 1 for kr ≪ 1 | C.16 |
| group index | n_grp = dk/dω | C.16 |
| point group, space group | rotations (and reflections) of a crystal; all symmetry operations including translations | C.17 |
| symmorphic, nonsymmorphic | space group with or without irreducible fractional translations | C.17 |
| glide, screw | reflection or rotation combined with a fractional translation | C.17 |
| character | trace of a representation matrix | C.17 |
| polar and axial vectors | transform with 𝖱 or with det(𝖱)𝖱 | C.17 |
| gyration tensor | axial–polar tensor g_ml of natural optical activity | C.17 |
| glide parity | sign η of the glide eigenvalue of a Bloch state in the mirror plane | C.17 |
CONCEPTS: "Moment bounds (Markov–Krein)" | C.10 | `eq:C.10-band`. "Branching and generating functions" | C.11 | `eq:C.11-gw`,
`eq:C.11-functional`. "Renewal asymptotics" | C.11 | `eq:C.11-linear`, `eq:C.11-fano`. "Semi-infinite LP and dual certificate" | C.12 |
`eq:C.12-certificate`. "Interval orders and tiers" | C.13 | `eq:C.13-order`. "Likelihoods and profiling" | C.14 | `eq:C.14-profile`.
"Foldy–Wouthuysen reduction" | C.15 | `eq:C.15-HFW`. "Quantized radiation field" | C.16 | `eq:C.16-A`. "Point groups and glides" | C.17 |
`eq:C.17-ninv`, `eq:C.17-selection`.
CLAIMS:
- Canonical representation exists (three real nodes, positive weights, exact to degree 4), w_ξ = 1/𝖪(ξ,ξ); band eq:C.10-band | C.10 |
  derived; Krein–Nudel'man, Akhiezer. Gaussian 2/(3 + ξ⁴); tail eq:C.10-tail | C.10 | derived, checked numerically.
- Extinction = smallest fixed point; thinning Fano rule; moment recursions | C.11 | derived. Key renewal theorem | C.11 | stated, Feller.
  Undershoot law, linear yield with constant ⟨X²⟩/2⟨X⟩² − 1, renewal Fano σ²/⟨X⟩² | C.11 | derived; checked numerically.
- Weak duality, ≤ n support (finite), discretization bracket eq:C.12-leak | C.12 | derived. Strong duality | C.12 | stated, Shapiro 2009.
  ≤ n atoms on the continuum | C.12 | stated, Rogosinski 1958.
- Interval-order transitivity, 2+2 property, tiers are antichains | C.13 | derived. Representation theorem | C.13 | stated, Fishburn 1970.
- Profiled Gaussian widths add in quadrature | C.14 | derived. Wilks | C.14 | stated, Wilks 1938, Cowan et al. Sect. 3.1.
- H_FW to O(m_ev⁴) and the FW vertex eq:C.15-vertex | C.15 | derived (Foldy–Wouthuysen 1950). Darwin 1s shift m(Zα)⁴/2 | C.15 | derived.
- Mode quantization, rate, dipole 4αω³|r|²/3 (H 2p 1.60 ns), soft spectrum (2α/3π)v²/ω | C.16 | derived. Medium factor n_r with group
  index cancelling | C.16 | derived (energy density of a dispersive medium from Jackson; nondispersive case Glauber–Lewenstein 1991).
- Invariant count eq:C.17-ninv | C.17 | derived. N_gyr values for 4̄3m, 432, m3̄m | C.17 | derived, checked by enumeration. Reciprocity
  restricts linear-q current response to the gyration tensor | C.17 | derived (sketch from A.4's argument). Diamond (200)-class
  extinction for any invariant function; glide-parity selection rule eq:C.17-selection | C.17 | derived. Twofold degeneracy at X | C.17 |
  stated, Dresselhaus et al.
INDEX: moment problem; Hamburger moment problem; Stieltjes moment problem; Hankel matrix; Carleman's condition; Christoffel function;
reproducing kernel; canonical representation; Gaussian quadrature; Markov–Krein band; Chebyshev–Markov–Stieltjes inequalities;
probability generating function; factorial moment; Fano factor; binomial thinning; Galton–Watson process; extinction probability;
minimal solution; first-step analysis; renewal equation; key renewal theorem; elementary renewal theorem; undershoot; overshoot;
Wald's identity; lattice distribution; linear programming; duality (weak, strong); semi-infinite program; dual certificate; Slater
condition; extreme point; complementary slackness; discretization error; partial order; interval order; semiorder; antichain; height;
tier; likelihood; likelihood ratio; Wilks' theorem; confidence interval (one- and two-sided); nuisance parameter; profile likelihood;
Monte Carlo propagation; Dirac equation; Dirac matrices; spinor; bilinear; Gordon decomposition; Foldy–Wouthuysen transformation;
mass–velocity term; Darwin term; spin–orbit coupling; contact density; Coulomb gauge; photon number state; minimal coupling; dipole
approximation; spontaneous emission; bremsstrahlung (soft); refractive index; group index; symmetry operation; point group; space group;
symmorphic; nonsymmorphic; glide plane; screw axis; character; character orthogonality; polar vector; axial vector; gyration tensor;
optical activity; reciprocity; diamond space group (Fd3̄m); systematic absence; glide parity.
