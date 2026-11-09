# Chapter 11 mock-reader review: personas (b) and (c)

Read: tex/ch11/ch11.tex, s11-1 … s11-9, tex/appD/D-31.tex, D-32.tex (build/main.pdf predates the sources).
Halo recovered from the text: v0 = 238, vesc = 544, vE = 250.5 km/s (vmax = 794.5; vrms 379).
Reproduced numerically (numpy/scipy, my own code), all matching the text to the quoted digits:
654 /kg/yr heavy plateau; c̄_LA = 9.017, 1/⟨1/c⟩ = 9.011, ⟨Σw/c⟩⁻¹ = 8.956 km/s, ratio 1.0067 (Ge 5.36/5.313/1.0092);
S4/S0 = 0.028; κ_η = 3.147 (3.10 at c_Si); I0 = 5.32e-7; Υ2/Υ0, Υ4/Υ0 at 0–700 km/s, zeros 196/138/435;
Q_DM = 1.34e6 at 256 km/s; Z*_GaAs = 2.108, Z*/ε∞ = 0.194; I_pol 0.822/0.759 meV; GaAs table 0.170, LiF 19.0;
Poisson tails 4.0e-5/2.0e-2/0.21, 47 % above n = 2; j_BZ(bond) = 0.443; ∫d³Q/(Q²|k−Q|²) = π³/k; TDS prefactor 1/16;
σ_ω = 88.4 meV, onsets 92.5/113 keV and 17.5/21.3/26.2/32.0 MeV; 1−e^{−2W} = 0.061/0.43/0.90;
toy model: ⟨1|X³|2⟩ = 6√2, E_kin factor, n = 2 ratio 1.50 and n = 4 ratio 27 at q_BZ; MK nodes 59.8/191.1/371.3,
weights 0.191/0.670/0.139; σ_b²/b̄² = 1.88e-4, ⟨δ^M⟩_b = −0.054, Γ_iso/g² = 1.37e-2 eV, Γ_EM/g² = 2.96e-6 eV;
d = −1.21e-3 /u, bracket 0.226, rigid ×8.2, PBE d = −7.6e-5 (×250); eq 11.8-shift identity; P_n prefactor 32;
bar coefficient π²/24 and mode shares 4/π²n⁴; band 30 MeV: 159 keV, x_R = 11.8, σ_lnR = 2.4e-3.
These are the "can I do it" tests cited below as [✓ header].

---

## Persona (b): particle physicist, QFT yes, no solid state

### 11.1 Acoustic phonons
- [lost, minor; notation clash] Eq. 11.1-master: δ(ω − ω_q) carries the DM energy loss ω_q (from §1.3/§8.2, not
  restated here) on the same line as S_A, which contains δ(ω − ω_{Qν}). Two "ω with a wavevector subscript" in one line.
  Fix: restate ω_q = q·v − q²/2m_χ in 11.1, or rename one of them.
- [lost, minor] Light mediator: "each branch and direction contributes q0⁴c_ν η(c_ν)/ω_th to the brackets" — the brackets
  contain the weight 1/c_ν, so read literally the c_ν does not cancel. Means "the q-integral contributes". Reword.
- [fast] Christoffel problem, quasi-transverse branches, Voigt shear-row ordering: I needed App. C.18 to follow;
  the section is terse but self-consistent and nothing downstream needs more than the result.
- [outcome: yes] Derive S_A per mass, edge (6.1 keV), light-mediator limit and its 1+κ_η correction, heavy plateau. [✓ header]

### 11.2 Optical phonons in polar crystals
- [outcome: yes] Sherman–Morrison step and the line formula for L reproduced; S_ZZ = (2q²/e²)L → eq 11.2-SZZ;
  one-branch form, eq 11.2-rate (factor 1/2π), Γ(v) and the e'² ↔ σ_e map all check.
- [lost, minor] Γ(v) is called "the rate per particle" without saying it is the scattering rate of one DM particle
  moving through the medium (dimension energy). One clause would do.
- [UBD, notation] p (Born-charge vector/√M) vs p (momentum) vs p_φ; fine in context but heavy.
- Own field: the millicharge and dark-photon vertices, and ζ, are stated correctly. No condescension.

### 11.3 Multiphonon response
- [outcome: yes] eq 11.3-exact from the pair sum (D.31), n-phonon term with 1/n!, zero first moment of distinct terms,
  Poisson tail bound. [✓ header]
- [UBD/clash] "q_0² = 2M_κω_0" in the Kahn–Krnjaic–Mandava quote, two paragraphs after q_0 = αm_e is used in rates.
  Rename (e.g. q_osc).
- [fast] Certified band eq 11.3-band: the "|_{vertex at q}" average is hard to parse from the keyresult alone; D.31's
  pointwise-band subsection makes it clear. Suggest one sentence in the main text: "shift q only in the Kronecker delta".
- [lost, minor] Intro says free recoil takes over "about 140 keV"; 11.4 says "about 90 keV". Both are right once the two
  criteria (x_R = 4, 9) appear in 11.4, but at 11.3 the reader has no way to know which.

### 11.4 Impulse limit and free nuclear recoil
- [outcome: yes] Width, Gaussian, cumulants, free-recoil rate (D.32), fermionic absorption slope 1+q/M and 1−e^{−2W}.
- [not re-derived here] Scalar fermionic operator "weights the density by q²/m_χ²" and vector "continuity … (m_χ/q)²"
  are quoted from 10.9. I accept them (they follow from ū_ν P_L u_χ traces) but a one-line pointer to the spinor trace
  would help a QFT reader verify 1−2m_χ/M vs 1−m_χ/M here.
- Own field: Dror–Elor–McGehee mapping, σ_F = m_χ²/4πΛ⁴, recoil 1/4v² enhancement — all correct.

### 11.5 Anharmonic and quantum-crystal corrections
- [outcome: yes] Moments µ̄2, µ̄3, µ̄4 (including the cancellation of the mixed terms for a real ground state);
  toy-model amplitudes and 16λ3²/k², 108λ3²/k². [✓ header]
- [not reproduced from text] "The first three hold at any temperature": D.32 derives c3 only at T = 0. It does hold —
  ∫ω³S = ⟨D³⟩ + ⟨D[H,D]⟩ in any stationary state, and ⟨pV′+V′p⟩ = 0 — but the reader must supply this. Add one line to D.32.
- [fast] Markov–Krein band: "canonical representation through ξ", "node passes through infinity", the half-line
  windows — impossible to reproduce without App. C.10. I could check the three-node solution at ξ = E_R, nothing more.
- [UBD/clash] η (halo mean inverse speed) vs η_anh; κ (species) vs κ_η. Tolerable, flagged for the notation pass.

### 11.6 Nuclear-spin and isotope couplings
- [UBD] Forward references to §11.8 on a linear read: the intro ("couplings of sec 11.1, 11.2, 11.8"),
  "the coupling-to-mass cancellation of sec:11.8-single", "unlike the zone-center absorption of sec:11.8".
  The cancellation is in fact proved right there (orthogonality to the translation mode); point back to
  we:8-nucleon / 11.2 instead, or say "derived here; used again in 11.8".
- [outcome: yes] eq 11.6-alp from eq 11.6-random with Γ_abs = S/2ω (I reproduced the π/6), B−L numbers. [✓ header]
- Own field: NR reduction of g φ ψ̄iγ⁵ψ, g_aNN = 2m_N g_N on shell, B−L split into neutron-number and EM currents,
  ζ = g_{B−L}/e — all correct.

### 11.7 Anisotropy and daily modulation
- [outcome: yes] Radon transform, Legendre/addition-theorem pairing, Υ_0 = η, all Υ ratios and zeros, A_day = 1.83 R4/R0.
- [minor numeric] "q = 1.79 q_BZ, at the shell |G_111| = 3.95 keV": 3.95/2.25 = 1.76.
- Evenness argument (dipole–quadrupole interference, O(q³)) is clean; no condescension.

### 11.8 Absorption on phonons and acoustic modes
- [outcome: yes] eq 11.8-shift (I verified the λ-shift identity and the leftover real constant v χχ/ε∞), site couplings,
  d, GaAs cancellation, resonator power (prefactor 32), Q_DM, free bar. [✓ header]
- [lost, minor] "Their GaAs projection takes the electron numbers 28 and 36" vs the worked example's 30.724/33.276:
  the bridge is the one clause "rigid ions … give the same structure with Q in place of Z*". State explicitly that
  28/36 are zero-field counts which the rank-one screening turns into Z − Q/ε∞.
- [minor] Sapphire band integral 36.3 meV (11.2, ordinary axis) vs 35.9 meV here, with no stated averaging
  (presumably ⅔ o + ⅓ e). Say which.
- Own field: |E′| = √(2ρ_χ), t_coh, de Broglie numbers, sign of δm_e = −gφ (convention of eq 8.1-scalar, not restated) fine.

### 11.9 Nuisance parameters
- [outcome: yes] σ_lnR in quadrature, kinematics of the 30 MeV example. The table is a good index. Leans on §8.8
  classes (normalization/tilt/…) without recap; acceptable since I read ch8.

### D.31, D.32
- Every step reproduced (pair sum, crystal-momentum delta, first moments, j_BZ for a sphere, Fourier transforms,
  π³/k, slope 1+q/M). Only gap: the finite-T statement for c3 noted above.

**Overall (b).** I would keep reading. The chapter is unusually checkable: every number I tested reproduces. My losses
were notational (ω_q, q_0, η/κ reuse), one forward reference block in 11.6, and two places where a single missing
sentence costs time (28/36 electrons; finite-T third moment). None blocks later material.
**Verdict (b): MINOR GAPS.**

---

## Persona (c): condensed-matter theorist (DFT, many-body), no dark-matter physics

### 11.1
- [outcome: yes] DM side is learnable from ch1 recap: v_min, η, F_DM, σ_p normalisation, edge. Rate prefactor 1/4 reproduced.
- [slow] Christoffel/Voigt pitfall, Hill average, Anderson Debye convention: standard for me, but short and
  correctly stated (Rayleigh bound q̂·M·q̂ ≥ B for cubic: true, needs only C11 ≥ C12, C44 ≥ 0). Not condescending.
- Own field: Voigt order yz,xz,xy correct; Zener ratios 1.56/1.66/1.21 correct; q_BZ vs Q_D distinction correct.

### 11.2
- Own field checks: LST generalisation and ω_L,max ≤ ω_T,max(ε0/ε∞)^{1/2} via interlacing — correct; Fröhlich analogy
  correct; "semilocal ε∞ 26 % high → rate 37 % low" correct.
- [query] GaAs Ω = 44.80 Å³ and ρ_T = 5.361 g/cm³ imply a = 5.638 Å, below every measured value (5.653 RT, ≈5.648 low T;
  ρ ≈ 5.32). Source not traceable inside ch11 (presumably we:5-lst). Z* scales as Ω^{1/2}, so +0.4 % in Z*, +0.8 % in rate.
  Please state the origin or switch to the measured cell.
- [query] Dielectric data (ε∞ = 10.88, ε0 = 12.9, ω_T/ω_L = 33.62/36.35 meV) are room-temperature values; the text
  notes the percent-level change on cooling. Fine, but a 10 mK detector would want the low-T set (ω_L ≈ 36.7–36.8 meV).
- [outcome: yes] Band integral, splitting route, LiF/GaAs factorisation (29 × 40 × 0.21 × 0.45 ≈ 110).

### 11.3
- Own field: coherent/incoherent in neutron sense vs DM sense is explained well; Warren 1/|q−G| law for second-order TDS
  correct; real-space divergence of B at T > 0 (falls as T/r) correct.
- [fast] Same as (b): certified band notation.
- [outcome: yes] Poisson weights, first-moment shares, tails. [✓ header]

### 11.4
- [outcome: yes] Impulse/Doppler width, x_R criteria, free-recoil rate and its domain of validity.
- DM-side terms (Helm, Lewin–Smith, σ_N) lean on ch2 without recap; fine for me after ch2.
- Own field: neutron Compton analogy correct; "zero-point broadening ≈ classical gas at 237 K" correct.

### 11.5
- Own field: SCHA rationale for helium, Kubo-transform obstruction of RPMD/CMD at T ≪ ω, M^{-1/4} zero-point scaling,
  time-reversal selection rule killing O(Φ³) — all correct.
- [minor] E_kin change "−0.14 to +0.08 %": endpoints pair (λ3, λ4) = (0.01, 2.5e-4) and (0.006, 2e-4); the quoted
  ranges also allow (0.01, 2e-4), giving −0.20 %. Say the range is for the two fitted sets.
- [fast] Markov–Krein subsection (as b).

### 11.6
- Own field: Lifshitz single-defect formula, first-order h_iso, local-mode condition (light defect, above band), Tamura
  width (π/2)g ω² g_ph/3 — all correct and signs right.
- [UBD] Forward references to §11.8 (also b).
- [query] "Measured optical phonon 64.1 meV" (in we:11-tail; reused for the 0.6 % PBE error): Raman gives
  520.7 cm⁻¹ = 64.56 meV at RT and ≈524 cm⁻¹ = 64.97 meV at low T. Which datum? It changes the 0.6 % to 1.3–2 %.
- [outcome: yes] Isotope channel numbers. [✓ header]

### 11.7
- DM side (Cygnus, wind direction, Υ_ℓ filter) learnable; the halo-as-filter picture is the clearest DM explanation in the
  chapter for a CM reader.
- Own field: cubic-site isotropy of B_κ and projected DOS → incoherent response isotropic: correct and nicely stated as exact.
- [minor numeric] 1.79 vs 1.76 q_BZ (also b).

### 11.8
- Own field: "a longitudinal phonon carries Z − Z*/ε∞ electrons" — correct within the rank-one form; polariton crossover
  √ε0 ω_T ≈ 0.12 eV, depolarisation factors, plano-convex trapped-mode normalisation all correct.
- [lost, minor] 28/36 vs 30.724/33.276 (also b).
- [minor] Core-electron kinetic term estimated as "binding energy/m_e ≈ 0.1": correct order (Ga ≈ 52 keV total), flagged
  as uncomputed in the text — good.

### 11.9
- [outcome: yes] I can read the table and redo the 30 MeV band. DM-side "reach", "three events per kg-yr" learned from captions.

**Overall (c).** I would keep reading. Condensed-matter content is correct everywhere I could test it; my queries are
about provenance of two input numbers (GaAs cell, Si optical frequency) and the room-temperature dielectric set. The DM
side is reachable from ch1–2 and ch8. Fast spots: certified band (11.3) and Markov–Krein (11.5, needs App C.10).
No condescension in my field.
**Verdict (c): MINOR GAPS.**

---

## Shared fix list (priority order)
1. 11.6: remove/redirect forward references to §11.8.
2. Notation: ω_q in eq 11.1-master; q_0 reuse in 11.3; η/η_anh, κ/κ_η, d (11.5 vs 11.8), N (cells/depolarisation/neutrons).
3. D.32: one line proving the finite-T third moment, or drop "any temperature" for µ̄3 in eq 11.5-moments.
4. 11.8: make the 28/36 → Z − Q/ε∞ step explicit; state the sapphire 35.9 vs 36.3 meV averaging.
5. Small numerics/provenance: 1.79→1.76 q_BZ; GaAs Ω = 44.80 Å³; Si "measured 64.1 meV"; E_kin range pairing.
6. 11.3 intro "140 keV" — forward-point to the two criteria of 11.4.
