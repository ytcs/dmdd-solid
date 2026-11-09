# Ch10 part 1: derivation review (isolated): ch10.tex, s10-1 to s10-5, App. D.29, D.30, plus the PRIORITY items of 10.8 and 10.9
Reviewer: derivation verifier (long-form-writing SKILL §5). Date 2026-11-02. No tex edited, no QE run, nothing committed.
Sources were fetched to sources/review-ch10/ (1509.01598, 2101.08275, 2105.02233, 2105.05253, 2003.12077, 2002.06937, 2110.01587,
2608.05282, 2501.18261, 2510.25835, 2109.08168, 2101.08263, 2210.14917). The PDFs are deleted; the .txt/.html extracts are kept.
Independent check scripts are in ledgers/REVIEWS/ch10/derivation-1-checks/ (run from that folder; not committed): algebra.py (sympy:
D.30 collection, 10.9 ratio, Elliott matching, R_n1, 10.5-res, 10.5-coupling, Hölder, pole slope, band roots), ser.py (10.8 series),
compton.py, w5.py, tcorr.py, boost.py, we101.py, fc.py, elf.py, elf2.py, lind.py, lind2.py, kk.py, bound.py, ac.py, band.py. They use only the cached tables (si_fcrys.load, si_elf_binned.npz, fig10_4_data.npz,
si_jresp_NK10_NC36.npz, abs10_7.eps_si) and their own η, Lindhard, KK and Dirac-trace code. They do not call the authors' rate functions.
Legend: CHECKED = I redid the result and it agrees · WRONG = needs a correction (given) · GAP = correct but under-stated, or not reproducible as written.

## A. PRIORITY verdicts

### A1. 10.4(a): screening class of each row against Table 8.3 (s8-4.tex l.77–92). Verdict: 10.4 is RIGHT and Table 8.3 is WRONG in its last row.
- Spin current 𝒥^{αβ}_e: its spin index makes it a vector under spin rotations. Without SOC or magnetic order, R̃_{𝒥Z} = 0 at every G
  (the same argument that 8.4's own text gives for s_e), so the row is unscreened, as 10.4 says. Table 8.3 lumps it with
  "local fields (G≠0)", which contradicts 8.4's spin paragraph (l.54).
- 𝒯_e: a scalar under spin rotations and under the point group, so it correlates with n_e(q) already at G = 0. Check (tcorr.py): in a
  free Fermi gas, which has no local fields at all, Σ_pairs (vertex n)(vertex 𝒯) = 0.11, 0.29, 0.30 (units k_F²/2m) at q/k_F = 0.3, 1, 2.5,
  so the cross term is nonzero. 𝒯_e is head-screened (10.4 and D.30 l.83 are right). Table 8.3 "local fields only" is wrong.
- Transverse current: on symmetry axes the screening comes through local fields only, with weak head mixing off-axis. 8.4 and 10.4 agree.
  The model numbers in 10.4 are CHECKED against si_jresp_lf.log: head < 1e-3 (6e-4), LF −15 %/−11 %/−8 to −9 %, [100] −4 %, S_nn 0.216, head 3.94.
- Fix for Table 8.3: split its last row into three.
  (i) "Transverse current j_T | O5, O8 (part across q) | local fields (G≠0) on symmetry axes; at G=0 only through L–T mixing off axes | no".
  (ii) "Spin current 𝒥_e | O3, O7, O12–O15; ALP absorption | none without SOC or magnetic order (triplet), as s_e | no".
  (iii) "Kinetic-energy density 𝒯_e | O2 (v⊥² part); scalar absorption | head and local fields (scalar under spin and point group) | no".
  The "ALP and scalar absorption" example also has to be split: ALP absorption is a spin row (unscreened) and scalar absorption is n_e/𝒯_e (head).

### A2. 10.4(b) and D.30 l.62, l.73: W̄5 vanishes exactly under PT. Verdict: CHECKED. The book is right, and Catena et al.'s nonzero W̄5 is numerical.
- Operator algebra: Θ = PK maps e^{iq·r} to e^{iq·r} and i∇ to i∇. Hence Σ_deg f f⃗* is real, so Σ f⃗×f⃗* is both real and imaginary, and is zero.
  The same argument gives Im W̄2 = 0. It holds for nonlocal (real, inversion-symmetric) pseudopotentials, and with SOC after summing over
  Kramers pairs. It holds per k, because PT maps k to k.
- Numerical check (w5.py): a 125-plane-wave 3D model with a real even V(G), so P and T both hold, has real eigenvectors (the PT gauge), so W5(k,q) = 0 identically.
  A complex V with V(−G) = V(G)* (T only, no P) gives W5 = −0.22 ≠ 0, with W5(k,q) = W5(−k,−q). So W̄5 ≠ 0 is allowed in GaAs but not in Si or Ge.
- Source: 2105.02233 §III (text after Figs. 2–3) reports that "Im W̄2 and W̄5 are not exactly zero" and attributes this to departures
  from axial symmetry. PT symmetry rules that out for Si and Ge. A plausible numerical cause is a band cutoff (52 bands) that cuts through
  a degenerate multiplet at k+q.
  GAP (text): 10.4 l.35 should add that Im W̄2 = 0 as well, and should name Catena's attribution and the reason it fails, in one clause.
- D.30 l.73 cites "[Eq. (81)] catena2021crystal" for W̄1 = (8ωαm_e²/q³)|f_crys|². In arXiv:2105.02233 this is App. D Eq. (D2). GAP: check the
  journal numbering or cite (D2). The relation itself is CHECKED: (2Ωω/π)S̄ with S̄ = 4παm²|f|²/(q³Ω) gives 8ωαm²|f|²/q³.

### A3. 10.8(a): ALP dark-Compton factor. Verdict: CONFIRMED.
- compton.py computes the Dirac traces numerically (pseudoscalar vertex γ⁵, photon sum −g; for the vector, the 3 massive polarizations
  averaged) at x = 0.01, 0.1957, 1, 5. The vector |M̄|² equals the book's (4/3)e⁴ζ²(m²+2m m_e+2m_e²)/[m_e(m+m_e)].
  With Γ = n_e|M̄|²ω_γ/[16π m m_e(m+m_e)] (∫dΦ₂ = |p*|/(4π√s), flux 4m m_e), the vector rate equals eq:10.8-compton and the ALP rate
  equals eq:10.8-alpC exactly, at every x.
- The published Eq. (3)/(17) of 2109.08168 (read from the source) divided by tree level is exactly (x+2)/(x+1): 1.990, 1.836, 1.5, 1.167.
- Their printed squared amplitudes Eqs. (9) and (15) equal my traces up to one common factor 4, the same for V and A. The error therefore
  enters at the integration step, as the text says.
- sympy (ser.py): the series of 10.8-compton, of 10.8-thomson (−35/8 x³), of the exact-ω_γ seagull (−17/4 x³) and of alpC/(2x²) = 1 − 5/2x + 9/2x²
  are all CHECKED. Seagull/exact at 100 keV = 0.9971; 1 % at 164.8 keV; 10 % at 516 keV (text 517, rounding). alpNR is 10 % high at 49.0 keV
  and 21 % high at 100 keV.
- WE 10.8: x = 0.1957, ω_γ = 91.82 keV, factor 1.836, 1.34e-25, 2.46e-25, 1.62e-25 cm². All CHECKED.

### A4. 10.8(b): pseudoscalar pair absorption is not velocity-suppressed. Verdict: CONFIRMED.
On the pair, φ†φ ∝ e^{−i(E+Ē)t+i(p+p̄)·x}. So ∂_t gives −2i m_φ and ∇ gives i q with |q| ~ m_φ v. The spin-current term of eq:1.4-alp
(coefficient ∝ ∂_t) therefore survives at v → 0, while the spin-density (gradient) term is O(v). With the replacement g_aee → m_e G_P and
m_φ → 2m_φ, the coefficient is 2m_φ G_P, as the text has it. S_𝒥𝒥 = ¾ S_jj (per Cartesian component) follows from D.30-quarter summed over 3 components.

### A5. 10.9(a): boosted-DM density row. Verdict: CONFIRMED independently.
- Algebra: q_μJ^μ = 0 on both sides gives J_L = (ω/𝒬)J⁰ and j_L = (ω/𝒬)n_e. Then J·j = (ω²/𝒬²)J⁰n_e + J_T·j_T, so the density term carries
  (1 − ω²/𝒬²). For m_V = 0 this gives (1−ω²/𝒬²)/(𝒬²−ω²) = 1/𝒬², which is Coulomb. The ratio to the published row is (1−ω²/𝒬²)² for any m_V.
  Since ω ≤ v𝒬 (convex E(p)), the ratio lies in [(1−v²)², 1].
- Numbers (boost.py, own integrator on si_elf_binned.npz): light mediator 0.9969 (v=0.1), 0.9399 (0.5), 0.6477 (0.9), 0.1712 (0.99);
  heavy mediator 0.9999 at all v. CHECKED against the text: 0.997, 0.94, 0.65, 0.17, 1e-4. "Lowers by a third at 0.9, by six at 0.99" is CHECKED.
- Caveat to state: for the light mediator the ratio depends on L being held at its 493 eV value for 𝒬 < 493 eV (the 𝒬 ≥ ω/v region), and on
  the 22.5 keV cut. The text says this in the caption only.

### A6. 10.9(b): fermionic absorption at bound kinematics. Verdict: CONFIRMED.
- The free vertex has longitudinal current (q/2m_e)n_e, and continuity requires (ω/q)n_e. They agree only on the free shell ω = q²/2m_e.
- For the Xe 1s shell at m_χ = 56.5 keV (ω ≥ 33.3 keV, q = m_χ − ω ≤ 23.2 keV): ω/q ≥ 1.44 against q/2m_e ≤ 0.023, so the free vertex
  violates current conservation by a factor > 60.
- eq:10.9-ratio is CHECKED with sympy (algebra.py): O(m_e⁰) gives 1 − ω²/m², O(1/m_e) gives ω(m−ω)(2m−ω)/(m_e m²).
- The vector contraction (1 + ω/q)² = (m_χ/q)² is CHECKED. The Xe numbers 0.587 and 0.890 (fermi10_9.log) are consistent with
  1 − ⟨ω²/m²⟩ + O(1/m_e) = 0.554 + 0.03.

### A7. 10.9(c): Cherenkov-like transverse dominance. Verdict: CONFIRMED numerically. The novelty claim needs a modest scope.
- The transverse weight per d𝒬 is (v² − ω²/𝒬²) Im[−𝒬²/(ω²ε_T − 𝒬²)]/𝒬, the density weight is L/𝒬, both with the same prefactor.
  I re-derived this from the dissipated power (J_T·E_T against ρφ), with |J_T|²/|J⁰|² = v_T².
- Below 2 eV, an independent analytic antiderivative of the pole integral gives transverse/density = 48.5 (v = 0.3) and 527 (v = 0.5).
  Integrated over the spectrum: 2.70e-5, 1.04e-2, 5.50e-2. In 10–20 eV: 6.8e-4, 7.2e-3. All CHECKED against "49, 530, 2.7e-5, 1 %, 5.5 %, 7e-4, 7e-3".
- Normalization cross-check: the pole term → (π/2)(v² − 1/ε₁), which is Frank–Tamm and is independent of ε₂. Against the Allison–Cobb (PAI)
  form, where the θ-term is π(β² − ε₁/|ε|²) and the log is ln(Q²max/Q²min), the relative weight matches mine.
- Scope to state (for 21.5 and E.16): the term itself is the textbook transverse term of Fermi's energy-loss formula (Fermi 1940;
  Allison & Cobb 1980, PAI model). What is new is only its use in boosted-DM electron-recoil rates in a semiconductor with a massless
  mediator. Four limits apply: it vanishes for a heavy mediator; it uses 300 K ε (Cherenkov threshold 1/√ε₁); it counts the emitted
  photons as deposited energy; it mixes the scissor-gap tables (L) with measured ε. The text has the last two; add "standard Fermi/PAI term".
- Observed, not in the PRIORITY list: s10-9 l.85 still has no citation for the solar-core temperature 1.5×10⁷ K (editor note). (3T/m_e)^{1/2} = 0.087 is CHECKED.

## B. ch10.tex
- l.2: 1 MeV gives m v_max²/2 = 3.51 eV and the Si gap is 1.17 eV. CHECKED.

## C. s10-1 and App. D.29
- eq:10.1-S0 / D.29-S0: the 4π = 2π·2 (spin), the k-sum → VΩ⁻¹… and the cancellation are CHECKED. Dimension eV² is CHECKED.
  "−2Im R⁰₀₀" with Im(1/(x−iη)) is CHECKED.
- eq:10.1-rate, eq:10.1-rateiso: from A.8-rate with |Ṽ|² = πσ̄F²/μ² and the kernel q dq η/4π² this gives ρσ/(4π m ρ_T μ²) ∫q dq F² η S̄. CHECKED.
- eq:10.1-fcrys / A.8-fcrys: both forms CHECKED, the second with ε₂ = e²S/2q² = 2παS̄/q². Knapen Eq. (16), k⁵V_cell Im ε/(8π²α²m²), is CHECKED from the source.
- Limit box 10.1: substituting gives ρσαm²/(m M_cell μ²) ∫dq/q² ηF²|f|², and ×ω gives the d ln ω form. Essig Eq. (3.13) per N_cell M_cell is CHECKED.
- D.29 l.25: the f-sum first moment 4π·4/Ω·q²/2m = πn_e q²/m with n_e = 8/Ω is CHECKED. The valence–valence cancellation by q ↔ −q (pairs are each
  other's reverse) with S(q) = S(−q) is CHECKED. The zeroth-moment bound is CHECKED.
- D.29-fcrys: the angle average via δ(q − |q′|), ∫d³q′ = Σ_G′∫_BZ, (2π)³/4π = 2π², and the identification with Essig (3.17)/(3.16)
  (spin 2 absorbed, cf. their (A.29)) are CHECKED. 2π²/(αm_e²Ω) = 1.987 eV (Ω = 40.05 Å³) is CHECKED (Essig: 2.0 eV).
- D.29 conversions: Griffin (3.12) gives (2π/V)Σ|f_{i→f}|²δ = S⁰/2, CHECKED from the source (their g includes 2π). Essig (4.2): weights summing to 2,
  ∫Ωd³k/(2π)³ → ½Σw, CHECKED. Essig (4.1) is the bin average, CHECKED. Essig Sects. 4.1/4.2 (PBE, scissor 1.11, 4+52 bands, 70 Ry) and Sect. 6
  (ρ = 0.4, v₀ = 230, v_esc = 600, v_E = 240) are CHECKED.
- l.3: q_max = 2m v_max = 53.0 keV and ω_max = 35.1 eV, CHECKED. l.74: 2π/a = 0.612 q₀ and |G₁₁₁| = 1.06 q₀ = 3.95 keV, CHECKED.
  l.72: free recoil 13.6, 31, 54 eV, CHECKED. l.76: 2m v_max(1 MeV) = 1.42 q₀, CHECKED.
- l.59 / limit box: WRONG (minor). "At the kinematic edge, q = 0.55 q₀": at 5 eV the edge is q_min = m(v_max − √(v_max² − 2ω/m)) = 0.525 q₀
  (0.51 q₀ without the recoil term, as limit10_1a log prints). 0.55 q₀ is the first sampled point.
  Correction: "Just above the kinematic edge (0.53 q₀), at q = 0.55 q₀, screening cuts…".
  The other ratios (0.05, 0.22, 0.54–0.61, 0.47, macroscopic within 10 % above 2.2 q₀ = 8.2 keV) are CHECKED against limit10_1a_NK12_531.log.
  The "≈10 % from the G set" is supported by the union run (0.528 vs 0.581 at 2.4 q₀).
- l.72 f-sum test: 1.03 (q₀), 0.83 (1.5 q₀), 0.33 (2 q₀) and 1.12/1.21 at 0.3–0.5/0.5–0.7 q₀ are CHECKED (fc.py, same 0.2 q₀ windows).
  GAP (wording): below 0.5 q₀ the value is a window mean with the empty (white) k-grid bins counted as zero. That is the right estimator,
  because the weight is concentrated in the reachable bins, but the text should say "window mean, empty bins included".
  Say "empty bins counted as zero" or drop the 0.3–0.5 window.
- l.74: peak of |f|² at 1.66–1.76 q₀ (3, 5, 10 eV); ratio (2q₀)/(q₀) 2.06–2.50; (3q₀)/(q₀) 0.23–0.26 ("a quarter of that value" means the value at q₀;
  make that explicit); q^4.84 over 0.3–0.75 q₀; q^−4.95 over 2–4 q₀; q S̄ peak 1.06–1.36 q₀. All CHECKED.
- WE 10.1 (we101.py, own η by quadrature): μ = 486.16 keV, m_e²/μ² = 1.1048, ⟨1/v⟩ = 1041.4, prefactor 2.453e5, integrals 0.6519/0.1927,
  R = 1.60e5 and 4.73e4, 438 and 129/day, peaks 6.5/3.3 eV, means 6.01/4.46 eV, q < q₀ shares 0.049/0.441, q > 2q₀ shares 0.269/0.033. All CHECKED.
  GAP: "38 % (66 %) deposit less than 4.9 eV" counts the 4.9 eV bin (ω ≤ 4.95). Strictly below 4.9 eV the shares are 0.36 and 0.65; write "at most 4.9 eV".
  GAP: "q integrand largest at 1.9 q₀ = 7.2 keV" (0.60 q₀ light) comes from a 5-bin running mean. The raw argmax is 1.74 q₀ = 6.5 keV (0.64 q₀),
  because the integrand is flat. Say "near 1.7–1.9 q₀".
- l.100: "a quarter of the heavy rate from q > 2q₀" matches 0.27. CHECKED.

## D. s10-2
- eq:10.2-rate: |Ṽ|²S = σ̄F²q²L/(2αμ²) (Knapen Eq. (13) read: (σπ/μ²α)k²Im(−1/ε)·dω/2π) and q dq η/4π² give 1/(8π²α). CHECKED.
  The IP rung via S^IP = (2q²/e²)ε₂^IP is CHECKED.
- Rates (elf.py, own η and integrator): IP/RPA/LF at 10 MeV heavy 1.358e5/8.62e4/5.89e4; ratios 2.30 and 3.73; at 1 MeV 9.3 and 13.3; LF factors
  1.46/1.27 (10 MeV), 1.10/1.09 (1 MeV); KKL-convention ratios 1.563/2.729 (10 MeV) and 1.453/2.536 (100 MeV); IP/LF above 10 MeV 2.17–2.30
  and 3.46–3.73; LF share from q > 6.7 keV 0.51, from q > 2q₀ 0.29, from q > 15 keV 1.8 %; mean ω 6.23 → 6.59 eV; head factor 13.1 (2 keV),
  4.24 (q₀), 1.18 (8 keV); LF factor 1.17/1.67/1.83; static ε 2.87/1.76, 1/ε² 0.12/0.32, 0.87 at 8 keV; ε₂^IP/L at q₀ 4.73/5.17/4.45;
  peaks 14.3/26.4 eV; f-sum share below 89 eV at 10 keV 0.171; step 0.87/0.43/0.29; ε₀₀(1 keV, 0) = 6.34; ε(0,0) 10.21/9.14. All CHECKED.
- Cappellini model at k_TF = 4.12 keV, ε∞ = 11.7, λ = 1.563, ω_p = 16.6: 1/ε² = 0.116 and 0.451. CHECKED.
- eq:10.2-moments, eq:10.2-Kn (Hölder exponents), eq:10.2-bound (= Barker (9) with 4e² = 16πα, read from the source): CHECKED.
  The RPA eigenvalue argument λ/(1−λ) ∈ (−1, 0] and the diagonal-element bound are CHECKED.
- WE 10.2 (bound.py): 0.42 ≤ q ≤ 5.30 keV, ω ≤ 3.51 eV; bounds 7.3e7 (n = 1, ω_p = 31.1), 2.08e7 (16.6), 2.0e6 (n = 0), 5.54e4 (n = −1, ×3400),
  9.3e4 (unit step); at 10 MeV n = −1 gives ×16.3. All CHECKED.
  GAP l.90: "the f-sum bound 8.5×10⁵ times" at 10 MeV is computed with q ≤ 22.5 keV, which is valid because the bound holds pointwise in q
  and the rate is truncated the same way. The text does not say so: add "(q ≤ 22.5 keV)". Over all q ≤ 53 keV the figure is 2.3×10⁶.
- WE 10.2 vs 10.3 table: the LF rate at 1 MeV heavy is 16.8 in WE 10.2 and 16.7 in the 10.3 table (16.25 in my trapezoid; the threshold
  interpolation of the 0.2 eV grid moves it by 3 %). GAP: use one value in both places.
- Relaxed lattice: |M|² = N(n_eΩ)²q²/(2M_cell ω_q), S^ac = πn_e²Ωq²/(M ω_q)δ, first moment share n_eΩ m_e/M_cell = 2.734e-4, inverse moment e²n_e²Ω/(M ω_q²)
  → 𝒢 = Ω_{P,e}²/(c q)². All CHECKED. Ω_{P,e} = 0.513 eV, 1 at 18.25 keV, 333 at 1 keV: CHECKED. Dimensionless: CHECKED.
- fig:10-sumrule-limit caption: "acoustic peak over clamped bound 120, 42, 21 at 0.5, 1, 2 keV" is CHECKED (ac.py: 120.2, 41.8, 20.7).
- ω_p = 31.05 (28 e/cell) and 16.60 (8 e/cell): CHECKED. n_e = 6.99e23 cm⁻³: CHECKED. E_g/ω_max = 17: CHECKED (17.3).
- l.7: WRONG (editor gap ruling). "An electron–hole pair in silicon costs at least E_g = 1.11 eV" is a physical statement, so it should read
  1.17 eV (18 times the phonon band). 1.11 eV stays only where the tables' threshold is meant.

## E. s10-3
- Constants: k_F = 3.569 keV, v_F = 6.984e-3, ω_p = 16.60 eV, r_s = 2.005, k_TF² = 3ω_p²/v_F² (from 2e²N_F = e²m k_F/π²). All CHECKED.
  Low-ω L ≃ e²m²qω/(2πk_TF⁴) equals πmqω/(2k_F k_TF²): CHECKED.
- Table (lind2.py, own Lindhard ε₁+iε₂, own Si integrator): Lindhard 746, 6306, 8.35e4, 2.53e4, 1.31e4, 3.43e3, giving ratios 45.9, 72.4, 1.42, 2.59,
  1.07, 2.11 against my Si, or the text's 45, 70, 1.42, 2.6, 1.07, 2.1 against its Si. CHECKED. Mermin 10–35 %: CHECKED from gas10_3.log (11–34 %).
  Band 4.2–9.5 eV holds 0.64 of the Si rate (text 0.62; grid edges): CHECKED.
- 2m_e(v_F + v_max) = 9.85 keV, k_F v_max = 9.46 eV, 20 eV → q ≥ 7.55 keV: CHECKED.
- Pole: ∂ε₁/∂ω = (2ω_p²/ω³)(1+2x) → (2/ω_pl)(1+2x)/(1+x); Z_L = (1+x)/(1+2x) ≈ 1 − x; first moment (π/2)ω_p²(1 + O(x²)). All CHECKED (to the stated order).
  Kozaczuk Eqs. (5), (7) read from the source: CHECKED.
- l.70: GAP. "agrees with the exact residue to 1e-4 at 0.1 k_F and 8e-3 at 0.3 k_F" holds for ω_pl^quad with Z_L ≃ 1 − (3/5)q²v_F²/ω_p²
  (my check: −1.1e-4, −7.7e-3), the limit-box form. With Z_L = (1+x)/(1+2x) as written in eq:10.3-plrate it is 4.3e-4 and 2.9e-2.
  State which form is meant, or put the expanded Z_L in the keyresult.
- Line weight 0.991 (q_c/2) and 0.767 (0.9 q_c): CHECKED. q_c = 2.604 keV, ω₊ = 24.82 eV; quadratic 2.240 keV and 20.55 eV; ω_p-fixed 1.881 keV;
  ω_p/v_F = 2.377 keV; 2π/a = 2.283 keV; 0.533: all CHECKED.
  Phase-velocity minimum at 0.989 q_c (within 1e-3): CHECKED. v_th 9.53e-3 (2860 km/s), 9.18e-3 (2752 km/s), 3.6 and 3.46 × v_max: CHECKED.
  6.27 keV: CHECKED.
- Kurinsky: ln ratios 1.237 and 1.309, (5/2.6)² = 3.7, q_min = 166 eV, 2.48 Å: CHECKED. Kurinsky Eqs. (4), (7), (13), (14) read from the source: CHECKED.
- l.107: GAP (minor). The untruncated lab-frame Maxwellian tail with v_E^ref = 250.5 km/s and v₀ = 238 (closed form, checked P(0) = 1)
  gives 3.7×10⁻⁴⁹ (> 2750 km/s) and 1.8×10⁻⁵³ (> 2860 km/s). gas10_3.log has 3.23e-49 and 2.07e-53. The text's "3×10⁻⁴⁹" fits neither
  rounding well; recompute with the stated v_E, or write "~10⁻⁴⁹" and "~10⁻⁵³".
- WE 10.3: 5.94 and 6.90 eV, 20.6 and 24.8 eV, closest approach 14.72 eV at 1.337 keV (exact Lindhard): CHECKED. q_c/2m at 100 MeV is +0.14 %:
  CHECKED. Table bins 22.3 eV, 6.9 %, 1.7e-3; 8.5 %, 4.0e-3; 4.9e-4, 9.6e-5, 2.5 %: CHECKED from the log.
  Ridge widths: CHECKED from the log. N_eh = 5: CHECKED. 260 phonons: CHECKED.
- eq:10.3-branch: the factor |ε|² cancels in the ratio. CHECKED (the estimate 1e-3 to 1e-2 is a known item).

## F. s10-4 and App. D.30
- D.30-O8 (𝔇 elements, spin trace ¼), D.30-continuity, the longitudinal collection (v_L − ω/q)² = (Δ_χ/q)², D.30-O8T: CHECKED.
  D.30-kernel: v_T² = v² − v_min², η₂ by Fubini, CHECKED. eq:10.4-O8 prefactor ρ/(16π²mρ_T) and "η → η₂/4": CHECKED.
- D.30-quarter: singlet Σδ = 2, triplet Σ|σ^z|²/4 = ½, ratio ¼. CHECKED. PT parities: n, j, 𝒯 even; s, 𝒥 odd. Products real: CHECKED.
- D.30-catena: f⃗ = (q/2m)f − j⃗ (plane-wave check), q·f⃗ = −(ω − q²/2m)f, W̄2 and W̄4 relations, W̄3 − (m²/q²)W̄4 = Σ|j_T|²: CHECKED.
  B1–B5 against Catena Eqs. (38)–(42) read from the source: CHECKED.
- D.30-optical: per component S_TT = (2ω²/e²)Im ε_T, Tr = 4ω²Im ε_T/e², ratio 2ω²|ε|²/q², IP 2ω²/q²: CHECKED (from ε^{αβ} = δ − (e²/ω²)(n/m + R̃_jj)).
- D.30-band and eq:10.4-band: CHECKED. "(√20 − 1)² = 12.1": CHECKED. "lower edge > 1 for r > 4": CHECKED.
- s10-4 l.95: WRONG. "2√r/(1+r) below 10 % only for r < 2.4×10⁻³ or r > 4.0×10²". Solving 2√r = 0.1(1+r) gives r = 2.51×10⁻³ and 398.
  Correction: 2.5×10⁻³, as D.30 l.101 already has. The 2.4×10⁻³ of the limit-box caption is a different criterion, (√r + 1)² ≤ 1.1
  (r ≤ 2.38×10⁻³), and is right there. limit10_4a.log prints 2.38e-3 for both criteria, which is a script bug.
- WE 10.4: √25.3 = 5.030, so (5.03 − 1)² = 16.24. WRONG (minor): the text has 16.3 (the log uses the unrounded r). Write 16.2, or quote r_IP = 25.33.
  36.4, 26.3, r_med 41–76, lower edge 29–60, 42–77: CHECKED. r_IP at 30/5/3/2 MeV = 22.2/33.1/56.5/147.5: CHECKED from limit10_4a.log.
  Scissor −1.9 %: CHECKED. Screening 2.31/2.30 (η₂/η): CHECKED; my η-weighted LF rate ratio is 2.30.
- l.84: η₂/η = 1.13e-6 (0), 1.00e-6 (1e-3) from the log, and my η gives the same. (2/5)v_F² = 1.95e-5: CHECKED. 3.2e-5/2.1e-5 and 4.1e-4 vs 4.4e-4: CHECKED.
  Cross block ≤ 0.0116 up to 2.4 q₀ on (5,3,1) (npz): CHECKED. It rises to 0.096 at 2.8 q₀, and the text's "up to 2.4 q₀" is correct.
- l.3: v_F/v₀ = 8.8, "nine times": CHECKED. Hochberg 2510.25835 Eq. (6), dΓ₈/d³q = (v⊥²/4)dΓ₁/d³q, read from the source: CHECKED.
  Catena–Iglicki: (4.16)–(4.21), the anapole j_Mj_M combination negative at 15 keV, and the j₅j₅ (spin, j₅ = σe^{−iq·r}) static bound broken by ~20
  at 500 eV, read from the source: CHECKED.

## G. s10-5
- eq:10.5-rate: L = 4π²αg/(Vq²)Σ…/|ε|², which gives ρσg/(2ρ_T mμ²)∫q…. CHECKED. Dimensions: CHECKED.
- eq:10.5-lines: |F_ns(0)|² = 1/(πa³n³); free-pair density (2μ)^{3/2}Δ^{1/2}/4π²; ξ_C = (E_b/Δ)^{1/2}; matching 1/(2πa³E_b) on both sides;
  ζ(3)/(πa³); (6πζ(3))^{2/3} = 8.006. All CHECKED. Fermi factor 6.29 at Δ = E_b: CHECKED.
- l.47: WRONG. "falls to 2.6 at 10 E_x^b". With ξ = 0.316, 2πξ/(1 − e^{−2πξ}) = 2.30. Correction: "2.3 at 10 E_x^b".
  The 2.6 belongs to Δ = 0.10 eV = 6.8 E_x^b and is used correctly in WE 10.5.
- WE 10.5: 1.155 and 1.166 eV; 4.3e-6 Å⁻³; 1/ζ(3) = 0.83; (6π)^{2/3} = 7.08 → 0.104 eV; 2.6 at 1.27 eV (2.65); 0.333 → 0.329 MeV (1.3 %). All CHECKED.
- Second class: R_{n1} → (2/3)[(n²−1)/n⁵]^{1/2}r/a^{5/2} (from the general small-r form), R₂₁ = 1/(2√6), |g·∇F|² = |g|²(n²−1)/(3πa⁵n⁵),
  the ratio (|∇ρ|/|ρ|)²/(32a²) = 1.4e-3 at 9 Å (tenth of the zone = 8.6 Å), Σ_k A_k k·g = −iV^{1/2}g·∇F(0), and |Γ(2+iξ)|² = (1+ξ²)|Γ(1+iξ)|². All CHECKED.
  Selection rule: Γ₂₅′ → Δ₂′ + Δ₅ (no Δ₁), and for Ge → Λ₁ + Λ₃. CHECKED by compatibility tables.
- eq:10.5-kk and eq:10.5-res: single oscillator ratio (E₀+ω)/2E₀ and [2ε₁/(ε₁+1)]² = 3.40: CHECKED. E₀ = 9.12 eV gives 2.23: CHECKED.
  KK of the tables (kk.py): static to ≤ 0.9 % (493 eV: 7.55 against 7.61); at 1.39 keV ε₁ = 4.45, res 3.05, factor 2.12; 2.21 at 0.49 keV; 1.53 at q₀;
  1.15 at 6.7 keV; 1.07 at 8 keV. All CHECKED.
- eq:10.5-coupling: Ω² = Δ(Δ+2K), expansion, χ(0) = −2|ρ|²/(Δ+2K) against −2|ρ|²/(Δ+K): CHECKED.
- Model numbers (fig10_4_data.npz/log): ε₂ peak 16.46 → 27.48 at 5.26 → 4.52 eV; static 6.557 → 7.799; L ratios 1.27–1.30 (onset to 3.5 eV),
  1.49 (4 eV), ~1.3 above; first moment −11.4 %; coupling block 2.55 %; triplet 2.18 (< 3 eV), 5.32 (2.5–4 eV), 1.036 (> 4 eV). All CHECKED.
  GAP (minor) l.24: "weight between the onset and 3 eV grows by 2.2". From the onset (1.69 eV) the factor is 2.30; it is 2.21 only when integrated
  from 0, which includes the broadening tails. Write 2.3, or "below 3 eV".
- (a/a_x)³ = 2.2e-3: CHECKED. |k_c| = 1.94 keV: CHECKED. 0.4·2π/a = 0.913 keV: CHECKED.

## H. Convention and notation drift (against NOTATION.md and STYLE.md)
1. WRONG: eq:10.2-relaxed names the lattice term 𝒢_GS. "GS" is a banned research label (NOTATION clash entry 51: use the 𝒫_ad,
   "electron-following" vocabulary). Rename it (e.g. 𝒢_ad) and add a row.
2. WRONG: s10-5 eq:10.5-coupling and the text above it use χ⁰(0), χ(0), χ^TD for responses. NOTATION reserves χ for the dark-matter particle
   "(only)". Use R⁰, R, R^TD.
3. GAP: \varOmega appears with two new meanings, the coupled-pair pole energy in s10-5 l.88 and Ω_{P,e} in s10-2. Neither has a NOTATION row,
   and the bare Ω row says "the only meaning" (cell volume). Rename the pole to E_± or ω_±, and add a row for Ω_{P,e}.
4. GAP: ω_p means 31.1 eV (all electrons) in 10.2 and 16.6 eV (valence) in 10.2 WE, 10.3 and 10.5 (E₀ formula). NOTATION has ω_p^val
   (first use 17.5). Use ω_p^val for 16.6 eV in 10.2–10.5 and move its first use to 10.2. The electron-gas ω_p of 10.3 may stay ω_p if
   "of the gas at the valence density" is said once.
5. GAP: new symbols without rows: K_n, Z_L, v_th, r (bare; it clashes with the radial r of 10.5 l.59), r_med, δ^j_LF, η_n^max, B^+_pl, ε₂^+, w_λ, C (10.5).
6. GAP: s10-5 l.64 writes Euler's gamma function as \varGamma. STYLE reserves italic \varGamma for rates and widths and upright Γ for the
   zone centre, so the gamma function has no assigned form. Editor to rule.
7. Coverage: I did not open taufertshofer2026excitonic or dreyer2026all (not fetched). I did not check these cited equations or sections:
   lasenby (8)/(9)/§VII, knapen (6)/(17)–(19)/App. C, griffin §1, hochberg2021 (1)/(S.9), trickle2023exceed (11)/(17)/(23)/(B16)–(B17),
   trickle2022effective Table III, cappellini1993, elliott1957. They are GAP (unverified), not CHECKED.
8. No factor-of-2, π or sign drift was found in: S normalization 2π/V; f-sum π n q²/m; ε₂ = e²S^prop/2q²; e² = 4πα; L = Im[−(ε⁻¹)₀₀];
   the spin factor in f_crys; QE weights; the Griffin ½; 𝔇 contraction order (real responses under PT).
