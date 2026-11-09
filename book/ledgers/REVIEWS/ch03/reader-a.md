# Chapter 3 mock-reader review: persona (a), first-year PhD student
Scope: Ch. 3 (intro, 3.1–3.6, summary) and App. C.1–C.8, D.4, D.5, read linearly. `build/main.pdf` (Nov 1 23:46) predates every
ch03/appC/appD source, so I read the .tex. I redid each derivation by hand and checked every number I could with numpy/scipy
(1D nearly-free-electron model, two-band chain, intrinsic carriers, Luttinger, Kane, cutoffs, Lindhard and erf numerics).
I judged Figs. 3.6–3.8 for pedagogy only. I read no briefs, ledgers or notation files.

## 3.1 Lattices and reciprocal space
- **Lost points.** None that block. WE "diamond structure factor": "the glide symmetry ... forces (200) to vanish (C.17)".
  I do not know what a glide is, and C.17 is outside my reading. Fix: one clause ("a reflection combined with a translation by a
  quarter cube diagonal") or drop the reason and keep only the claim.
- **Not reproduced.** Nothing. b_i, the (h,k,l) parity rule, |ΓL|,|ΓX|,|ΓK|,|ΓW|, the 0.985 sphere radius, k_F = 3.57 keV, the
  densities, and the WE numbers (0.42/0.46/4.84/52.6 keV; count 1.31e4) all check.
- **Used before defined.** "glide symmetry"; "Born–Oppenheimer" (forward reference to 5.1 given, which is fine).
- **Too slow / fast.** The sign remark after (u×v)×(u×w) is fiddly but correct. The lattice sum is derived here and again,
  word for word, in C.2 (see Appendices).
- **Outcomes.** Build the fcc reciprocal lattice and BZ: yes. Reduce a q: (2.2,0.5,0)·2π/a gives G_q = (2,0,0) and
  q_r = (0.2,0.5,0), |q| = 5.15 keV, |q_r| = 1.23 keV. Find extinctions: yes, S_bas(200) = 1 + e^{iπ} = 0 and GaAs gives 31−33 = −2.
  Count states and bands: yes, 8 e⁻/cell gives 4 bands.

## 3.2 Bloch states and band structure
- **Lost point 1.** WE "vertex between the two lowest nearly-free bands": "This value of q marks a scale: from this particular
  k the transition deposits 1.6 eV, which needs q ≥ 0.61 keV." I had to compute ε₂(k+q) myself (1.62 eV) before I saw that the
  q = 377 eV point is not kinematically reachable from this k. The previous sentence calls 377 eV "the smallest momentum transfer
  with which dark matter can deposit the 1 eV gap", which suggests the opposite. Fix: say outright that at q = 377 eV the final
  state has moved up to 1.6 eV, so the pair at this q is a reference scale, not an allowed event.
- **Lost point 2 (small).** The occupation is said to be accurate "to e^{−E_g/2T}" before 3.3 explains where that exponent comes
  from. A pointer to Eq. (3.3-ni) would help.
- **Not reproduced.** Nothing. My 25-plane-wave diagonalization gives the edges 0.7515/1.7491 eV, gap 0.9976, second gap
  0.0964 eV, |v21| = 2.244e-3, |ρ21| = 0.0225/0.2098/0.4962 at q = 10/100/377 eV (optical limit 0.0224/0.224/0.849), and
  |ρ_m1|² = 0.298/0.251/0.226/0.225 at q = G1 with closure ≈ 1. The 2-wave slope 448 eV, tight-binding K = 3.66 t,
  m* = 1/(2ta²), Eqs. (3.2-r), (3.2-dHk), (3.2-dudk) and the optical limit all follow as written.
- **Used before defined.** None that matter (μ_ch, n_F, v_C come from Ch. 2).
- **Too slow / fast.** Well paced. The validity condition (3.2-validity) together with the 1D example is the best part of the chapter.
- **Outcomes.** Bloch theorem and the central equation: yes. NFE gap = 2|U_G|, and its failure under extinction (96 meV at
  second order): yes. TB fcc band: yes. Density vertex with G_U kept, plus closure: yes. Optical limit and when it fails: yes,
  |v21| = 0.85 v_max puts DM at the edge.

## 3.3 Silicon, germanium and gallium arsenide
- **Lost points.** None that block. In the k·p/SO subsection, the step "the crystal SO operator reduces to ξ_eff L·S with
  w_κ the p weight" is asserted. I accept it but cannot derive it. One sentence on why the cross-site terms drop out would help.
- **Not reproduced, input missing (not errors).** m_dv = 0.50 m_e "from spherically averaged heavy and light holes": no recipe
  is given. (m_hh^{3/2}+m_lh^{3/2})^{2/3} with direction-geometric means gives 0.51. Single-band share of m_e/m⊥: I get 2.30 with
  v = 2.9e-3 against the stated 2.27 (v is rounded). Kane: 1/(1+18.3/1.42) = 0.0720 against the stated 0.0718 (E_P is rounded).
  E_min values read off Fig. 3.6(b) (1.26 eV, 2.2 eV, "about 2.0 eV" at 0.88 keV) are figure numbers and excluded.
- **Reproduced.** m_dc = 1.064; n_i = 6.1e9 cm⁻³ (300 K), 1.0e-20 (77 K), 10^{-720.7} (4 K); valley aspect ratios 2.2 and 4.4;
  hydrogen 2p splitting α⁴m/32 = 4.53e-5 eV = 0.365 cm⁻¹; the SO ratios; Δ_SO/3 = 15 meV and 0.10 eV; the j=3/2 projector;
  Kane+SO 0.0660 (also 0.025 and 0.075); every hh/lh entry of Tab. 3.1 from the γ's; Eq. (3.3-Eminpar) and its 0.35 keV;
  WE kc 0.486–4.814 keV, 3.26 eV, 0.474 MeV, 0.333 MeV at 0.88 keV; WE mmin 0.968/0.253/0.212 MeV, Ge |ΓL| = 1.898 keV, 0.420 MeV.
- **Used before defined.** "semilocal functional" and "quasiparticle correction" (both before 3.4); "cyclotron resonance";
  "electron–nuclear double resonance" (harmless).
- **Inconsistency noticed.** WE 3-scales (3.1) uses E_g = 1.11 eV without comment. Only here do I learn the book uses 1.17 eV.
  A half-sentence in 3.1 would save a double-take.
- **Too slow / fast.** The Luttinger 4×4 is quoted, not derived. That is acceptable, since the formula lets me rebuild the table.
- **Outcomes.** Locate band edges and valleys: yes. Compute a mass by k·p: yes (Kane 0.066). Estimate Δ_SO from the ion: yes.
  Use E_min(q) against the DM reach to see why 0.333 MeV cannot reach the valley without a phonon: yes (0.474 MeV bound).
- **Fig. 3.6 (pedagogy).** Panel (b) is the most useful figure in the chapter: E_min against the 1 MeV reach makes the
  phonon-window argument visible. Suggest marking |G200|−k_c = 2.63 keV, where the text says the [100] curve leaves E_g.
  **Fig. 3.7:** clear, and the Ge Γ/L ordering is spelled out in the caption.

## 3.4 Many electrons and density-functional theory
- **Lost point 1 (conceptual).** The derivative discontinuity is asserted ("the exact xc potential jumps by a constant").
  Neither 3.4 nor D.5 says *why* it must exist. The ingredients are already on the page: E(N) is piecewise linear, so the
  chemical potential jumps from −I to −A at N_e. The KS kinetic part jumps only by E_g^KS, so the remainder must sit in E_xc.
  That one sentence turns Eq. (3.4-gap) from a fact into an argument.
- **Lost point 2.** Fig. 3.8 caption: "Goedecker–Teter–Hutter pseudopotential, double-zeta Gaussian basis with polarization
  functions". The text has just said plane waves are the standard basis, and I cannot tell whether a Gaussian basis matters
  for the gap. Fix: one clause saying the basis choice moves the gap by tens of meV (the caption's own ±25/−36 meV), plus a pointer.
- **Lost point 3 (small).** The text above Fig. 3.8 compares the LDA bands with G0W0 squares from a *different* calculation.
  The caption says so, but the body text should too, or I read the 0.53–0.64 eV spread as the scatter of one correction.
- **Not reproduced.** Nothing. The scissor velocity rescaling, the factors 1.22 and 1.50, the shifts 0.568/0.613 eV, the WE
  masses 0.148/0.171/0.313–0.367/0.333 MeV and 0.407 MeV, and 8.5 % all check.
- **Used before defined.** G0W0 and W^scr (forward reference to 4.8); "norm-conserving" and "SG15" (before 3.5); "Coulomb-hole
  term" (E.3); "Lagrange multipliers" in the KS sense (D.5 explains it).
- **Too slow / fast.** "LDA works because the xc hole obeys the same sum rule" goes a little fast. Only the exchange hole is
  shown (D.4) to hold one electron. The LDA lattice constant (5.401 Å) is stated in both 3.1 and 3.4.
- **Outcomes.** Write HF and KS equations and say what each eigenvalue means: yes. Explain the band-gap problem: mostly. I can
  state it, and I can argue Δ_xc myself only after supplying the sentence above. Apply a scissor to energies, vertex and
  velocities: yes (v_cv × 3.12/2.55 = 1.22). Propagate the gap error to m_min: yes (0.148 against 0.333 MeV).
- **Fig. 3.8 (pedagogy).** (a) shows "right shape, wrong position" well. (b) with the m_min right axis is an excellent link back to Ch. 1.

## 3.5 Plane waves, pseudopotentials and core states
- **Lost point 1.** "the silicon 2p shell opens at m_χ = 29 MeV and needs q ≥ 38 keV". This reads as if both hold at once. At
  the threshold mass the only usable q is (2m_χω)^{1/2} ≈ 76 keV; 38 keV is the heavy-mass floor ω/v_max. The same applies to
  2s (43 MeV / 57 keV) and Ge 3d (8.5 MeV / 11 keV), and to the dotted lines of Fig. 3.10. Fix: "needs q ≥ 38 keV for any mass
  (76 keV at threshold)".
- **Lost point 2 (small).** "Spin–orbit coupling is added, when needed, with fully relativistic potentials (Sec. 3.3)". Sec. 3.3
  does not discuss fully relativistic potentials, so the pointer misleads.
- **Not reproduced, input missing.** "3 % of [2p] weight above 38 keV", "three quarters [of Ge 3d] above 11 keV", the core radial
  peaks, and the 0.662/0.767 charges all need the atomic calculation, which is fine. Si 1s shift: (1785.9−1781.2)/1781.2 = 0.264 %,
  stated as 0.27 % (a rounding nit).
- **Reproduced.** 1s FT and the p⁻⁸ tail; k_cut = 28.9 keV at 60 Ry; 2121 and ~5500 plane waves; p_f = 9.7 keV; 113 Ry; ~80 bands;
  the log-derivative identity (3.5-logder); the PAW cross-term algebra; core thresholds 28.6/43/524/8.5 MeV; the full
  Pauli reduction to H_mv + H_Dar + H_SO (I redid every commutator); ⟨H_mv⟩ = −5/8 and Darwin = +1/2 in (Zα)⁴m; (Zα)²;
  (Zα)⁴m/32 = 1.74/47.4 eV; Z_eff = 14.2.
- **Used before defined.** "Ry" (defined only in D.4, reached via 3.4) and "bohr" in the WE. Dirac matrices α_D, β_D (C.15,
  outside my reading). The Dirac equation sits at the edge of my assumed background, but the derivation is self-contained once
  it is granted. "Troullier–Martins", "single-projector", "Dirac–Kohn–Sham" appear in captions. "scalar-relativistic" appears in
  the Fig. 3.9 caption before the text defines it.
- **Too slow / fast.** The PAW Δ size estimate ("dipole difference, weighted by the fraction inside the sphere") is quick but
  plausible. Otherwise well paced, and the cutoff estimate (3.5-Ecut) is very clear.
- **Outcomes.** Pick E_cut for a target q_max: yes (30 keV gives 113 Ry). Explain norm conservation: yes. Write the
  all-electron vertex: yes, as a formula, though I could not implement it from this alone. Decide when core shells matter:
  yes. Size relativistic corrections: yes ((Zα)²/4 = 0.26 %/1.36 %).

## 3.6 Wannier functions
- **Lost point 1.** "Both sets are real, as the functions at a minimum must be ..., so that this test does not tell them apart".
  No test has been mentioned. Fix: "so reality, a common check that a minimization has converged, does not tell them apart".
- **Lost point 2.** The PBE CBM is at 0.840 (2π/a) in 3.4 but "0.85 (2π/a)" in the Fig. 3.12 caption with the same 0.557 eV gap.
  It is probably a different grid or cutoff, but as written the two look contradictory.
- **Not reproduced.** Eq. (3.6-stationary) and the discrete forms (3.6-discrete) are quoted. I cannot derive them, and I don't
  think I am expected to. The spreads 16.2/19.8/14.0/7.58 Å² need the calculation.
- **Reproduced.** The orthonormality of the WFs, the Blount r-matrix (3.6-blount) by parts, the Ω_I/Ω̃ split, aliasing
  (3.6-alias) and the exactness result. The whole chain WE, numerically: band edges ±1.118/±3.041 eV; |H^W(R)| = 2.192/0.468/
  0.0525/0.0120 eV; a/ξ_W = 0.771; error 51/4.75/0.64 meV and 2.4 µeV for n_k = 4/8/12/24; two-band error 0.24 eV at n_k = 2,
  ~1e-15 for n_k ≥ 3.
- **Used before defined.** "Chern invariants" (never defined; "a topological invariant that vanishes with time-reversal
  symmetry" would do), "Berry connection" (defined only by formula), "Löwdin", "Foster–Boys" (names only, harmless).
- **Too slow / fast.** Eq. (3.6-stationary), with its superoperators 𝒜 and 𝒮, is the one opaque block of the chapter. It
  could go to App. E.5 with a sentence left here ("codes follow the gradient of Ω_W from the projected gauge").
- **Outcomes.** Build WFs from a smooth gauge and explain why the gauge matters: yes. Explain disentanglement and frozen
  windows: yes, conceptually. Predict interpolation error from the range of H^W: yes (chain, factor e^{−a/2ξ} = 0.68 per point).
  Explain why one gauge must be used throughout: yes, and the WE's gauge-mismatch test made it concrete. Run a maximal
  localization by hand: no, and the text does not expect it.

## Appendices read (C.1–C.8, D.4, D.5)
All derivations reproduced: the golden-rule limit with its finite-part correction (C.1; the central lobe holds 90.3 %);
Poisson/grid aliasing and the lattice sum (C.2); the Rayleigh expansion via I_l, ∫r³e^{−βr}j₁, and the Y^c_4 normalization
41/105 → 16/525 (C.3); Sokhotski–Plemelj, d PV/dx = −fp and the Lorentzian test 1−Γ/2+Γ²/4 against the Gaussian 0.7 % (C.4);
KK, the Matsubara oscillator sum and the high-frequency moment (C.5); BCH, coherent states and q = 56 keV for 60 meV in Si (C.6);
Schur/Woodbury and both Bogoliubov cases (E_b = 0.8, sinh²θ = 0.125) (C.7); erf(1.0525) = 0.86337 and erf(2.286) = 0.99877
(C.8: a stated erfc of 1.227e-3 matches x = 2.2857 rather than 2.286), K(s) log limit, F_L limits, and the branch of the
Lindhard logarithm (C.8). D.4: Σ_x(k) via the stated antiderivative, F_L(1) = ½, widening 8.29 eV, ⟨F_L⟩ = ¾, E_x = −6.22 eV at
r_s = 2.0. D.5: the HK contradiction, Levy two-step minimum, KS by chain rule, E_0 double counting, Janak, v_x = Σ_x(k_F) =
−8.29 eV, Slater −12.4 eV.
- **Used before defined in appendices.** D.4 cites E_F from Sec. 4.2 although Sec. 2.5 already has it; C.8 mentions "Kohn
  anomaly" and "Friedel oscillations" (harmless).
- **Too slow.** C.2 repeats the reciprocal-lattice definitions and the lattice-sum derivation of 3.1 nearly verbatim. Either
  could point to the other.

## Overall
I would keep reading, with confidence. The chapter is honest about what it derives and what it quotes, and every derived step
I attempted reproduced, usually to the stated digit. The 1D nearly-free-electron worked examples (gap, vertex, Umklapp) and the
two-band Wannier chain are the best teaching in the book so far: I rebuilt both numerically and matched every number. The thread
from bands to E_min(q) to "0.333 MeV cannot reach the valley without a phonon" is clear and motivating. **No item in the lost
points or the non-reproduced lists blocks the material that follows.** The non-reproduced items are rounding or missing inputs
(m_dv recipe, atomic-calculation weights, figure readings), not errors. Fixes that would make it CLEAR, in order of value:
(1) one sentence motivating Δ_xc from the piecewise-linear E(N) (3.4/D.5);
(2) say that the q = 377 eV point in WE 3-vertex is not kinematically reachable from that k;
(3) separate "q ≥ ω/v_max for any mass" from "q at threshold mass" for the core shells (3.5, Fig. 3.10);
(4) define or drop "glide symmetry" (3.1) and "Chern invariant" (3.6), and gloss the Gaussian-basis jargon in the Fig. 3.8 caption;
(5) reconcile 0.840 against 0.85 for the PBE CBM (3.4 / Fig. 3.12), and flag the 1.11 eV against 1.17 eV choice in WE 3-scales;
(6) fix the pointer to Sec. 3.3 for "fully relativistic potentials" (3.5), and the unclear "this test" (3.6).

**Verdict: MINOR GAPS**
