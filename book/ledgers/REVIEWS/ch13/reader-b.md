# Chapter 13 mock-reader review: reader b (personas b and c)

What I read: the .tex sources of Chapter 13 (ch13.tex, s13-1 to s13-9) and App. D.35, D.36 and D.37, linearly. The PDF is current. I read nothing else.
How I checked: by hand and with numpy/scipy, from the book's own inputs (v_max = 794.5 km/s, so v_max^2 = 7.023e-6).
The chapter has no exercises, so the worked examples stand in for them. I redid seven of them in full.

## Checks reproduced (both personas)
- 13.1. Floors and q* values. Stationary-point derivation of eq:13.1-mPA, giving 2E/(v^2 - u^2). Parabolic Si zero-phonon minimum 0.4246 MeV at q = 1.460 keV, with a 0.480 keV shortfall and 1.359 eV. Ge 0.324 MeV at 1.104 keV. GaAs eq:13.1-mZPdir: 3.68 MeV for [111], none for [100]. The L-valley bracket 0.517-0.560. All n_B values. Bound-state shift 0.0025.
- WE 13-onset: every pass, the sensitivity of 2.8e-4 MeV/meV, and 0.3378 and 0.3384.
- 13.2. Hole-path signs. The on-shell identity C -> B(filled) and D -> A(filled). The q = 0 cancellation, eq:13.2-q0.
- WE 13-exchange, rebuilt from scratch. I reproduce the gap 1.448, E_min = 2.912, all four denominators exactly, |rho_vv|^2 = 0.643 and |rho_cv|^2 = 0.357, |M| = 0.0996, |C+D| = 0.0776, |A+B| = 0.0643 and the ratio 0.417. This needs two guesses; see item b2.
- 13.3. Prefactor of eq:13.3-near, Omega (m_d m_h)^{3/2}/(4 pi^2), from the explicit joint DOS (16 pi^4 / 64 pi^6). Cone averages C x^3/12 <1/kappa> and the LA term x^4/48. The 8.85 meV curvature term. Cost ratio 1.2e-3. Window bound |Q*| >= 0.62 keV. Tilt shift (1/2) M u^2 = 0.02 meV.
- 13.4. All epsilon factors: 0.021-0.025, 0.026-0.033, 40-48, 30-38, 1.25 and 1.31, 2.9-3.4, 3.6-4.5. Also n = 0.200 A^-3, k_F = 1.81 A^-1, the prefactor 0.05 and k_x = -(2/3) f_x/n. The factorization (eps~^-1)_G0 = (1/eps_mac)[delta + v R-bar] (D.36). Both solvable limits (D.36).
- 13.5. WE 13-TA-transfer to 5 digits: forward 1.467; inverse terms +1.19083, -0.21542, +0.02722, -0.00289, +0.00028. The 77 K factors 2.64/1.90/1.47/1.29, the factor-2 point at 23 meV, the factors times 0.88, and the series ratios 0.064, 1.7e-4, 0.49, 0.11. The Stanford factors 0.61/0.88.
- 13.6. Soft-limit bracket of WE 13-soft: deformation -0.607, velocity ~ -1e-5, intraband slopes = D + v p. At the extremum: 2.09 +- 4.9, amplitude ratio 2.5, 2 m* c_nu. The margin ratios, the 0.77 energy share, Q_min = 0.018 A^-1, m* c values.
- 13.7. Closed form of eq:13.7-sqrt and the numbers 2.0/0.4/0.8 meV. Varshni shifts. dm/dE_g = 2/(v + u)^2 = 0.283 and 2 m^2/q^2 = 0.187. All of WE 13-windowT, including the sideband onsets 0.3157, 0.3027 and 0.3278.
- 13.8. Coefficients 32 and 8/pi of eq:13.8-edge, the (32/3) E^{1/2} x^{3/2} start, the 8.0 E_x^b equivalence, the 1s fraction 0.74 at 1.200 eV, and the factor 81. The scalar compact form eq:13.8-MT, via x = h - V. Dark-photon WE: eps2 = 2.44e-4, L = 1.51e-6, R = 9.3e27 zeta^2, zeta = 1.8e-14, 7.0e-15 and 7.5e-14. The ALP ratio 7.3e-9.
- 13.9. The beta-function integrals giving p_on + 7/2; F_0 = 3.5 meV per 0.001 MeV; 0.92^6.5-0.92^7 = 0.56-0.58. The quadrature combination giving a factor of 4. m_ZP = 0.4077 from (q, E) = (1.33 keV, 1.355 eV). Exciton shift 0.0028. Glide phases w = (a/2)(1,1,0), w/2 - tau = (0,0,-a/4) and G'.w/2 = -pi.

## Persona (b): particle physicist (QFT, no solid-state physics)

### 13.1 The indirect-gap window
- Lost: none. The kinematics is that of a two-body threshold with a q-dependent "mass gap", and it reads naturally.
- Not reproduced: one number inside WE 13-onset. The bound-pair optimum q* = 0.885 keV does not follow from the formula used in the passes, q* = 2E/v_max, which gives 0.883. It does follow from q* = 2E/(v_max - u), but the free-pair passes used 2E/v_max (894 eV; with the slope it would be 897 eV). Use one convention throughout.
- Used before defined: the phonon-assisted process of sec:9.1 (Ch. 9 is outside my reading set). It is harmless, since 13.1 explains it again.
- Pace: about right. The GaAs paragraph is dense but complete.
- Outcomes: compute m_min^PA and m_min^ZP (the parabolic version) for a crystal from E_g, k_c and one phonon energy: yes, done above for Si, Ge and GaAs. Explain why fixed directions or a hole fixed at the valence-band maximum give upper values: yes.

### 13.2 The amplitude
- Lost: none. The time-ordered (old-fashioned) perturbation theory and the fermion-sign bookkeeping are familiar to me.
- One sentence would help QFT readers without talking down to persona (a). The band-sum theorem is the statement that the one-electron Feynman propagator carries both particle and hole poles (Z-graphs), so the unrestricted sum is what a covariant calculation gives automatically.
- b2. WE 13-exchange cannot be reproduced exactly as written, for two reasons.
  - The twist is called "small", but the stated gap of 1.448 eV needs theta ~ 0.31 rad, a k shift of about 0.05 rad. A twist of 0.01-0.05 gives 1.442.
  - The phonon vertex convention changes |M| and the headline factor. The displacement wave can be phased at the cell origin, e^{iQR}, or at the orbital, e^{iQx}. Cell origin with Bloch convention II reproduces every printed magnitude. Orbital phasing gives |M| = 0.107 and a rate ratio of 0.62 (a factor of 1.6, not 2.4).
  - Fix: state theta and the phase convention of the A-minus-B vertex.
- Used before defined: none.
- Outcomes: list the four paths and derive eq:13.2-M on shell: yes. Show the q = 0 cancellation: yes. State why the amplitude does not interfere with the zero-phonon line: yes; the orthogonality of the phonon Fock states is clear.

### 13.3 The rate
- Lost: the group-theory paragraph. The book asserts the Delta-line labels (Delta_1 for LA, Delta_2' for LO, Delta_5 for TA/TO, Gamma_25' -> Delta_2' + Delta_5) and cites a reference, but prints no C4v character table or compatibility relation. I can check Delta_5 x Delta_5 ∋ Delta_1, but I cannot check the assignments. Fix: a three-line table (or a pointer to App. C).
- Used before defined: delta_w and "the off-shell window" appear in the keyresult eq:13.3-SPA and in the text, but are fixed only in 13.6. The forward reference is given, but the condition enters a boxed result.
- Pace: the onset-exponent counting rule (D/2 - 1, plus one power for a vanishing |M|^2) is very good.
- Outcomes: assemble S^PA and L^PA with the right N and V counting: yes. Derive p_on = 2, 3 and 4: yes, worked through both integrals. Predict the LA kink from symmetry: only given the table.

### 13.4 Screening
- Lost: the mean-field second-order source eq:13.4-dn2 in the main text. It is followed easily only with D.36 open. D.36 is clear, and I verified it.
- Pace: fast in "The pair channel", adequate overall.
- Outcomes: show that one factor 1/eps_mac survives: yes, and I checked the algebra. Size the external factor from tabulated eps: yes. Compute the pair channel: no, but the book says it is open.

### 13.5 The optical limit
- Lost: none. The continuity Ward identity eq:13.5-ward is correct and well placed. The contact-term remark for nonlocal potentials is the right caveat; it is the same thing as seagull terms.
- Outcomes: derive eq:13.5-Mlim and eq:13.5-limit: yes. Invert absorption data in temperature: yes; reproduced to 1e-5. Explain why the inversion is ill-posed without a split by branch: yes.

### 13.6 Soft phonons and the window
- Lost in the soft limit, twice.
  - The text says the comoving intraband vertex is i l Q (D + v (x) p), but the keyresult numerator is D -+ c p. They reconcile through (D + v p)/(v +- c) = (D -+ c p)/(v +- c) + p and the bare Galilean terms -p_cc + p_vv, which appears only in D.37's last paragraph. Fix: one sentence in 13.6.
  - WE 13-soft says that setting the interband vertices to zero "halves |M|^2". That holds for one sign of Q, (4.91/7.0)^2 = 0.49. For the other sign it triples |M|^2, (4.91/2.82)^2 = 3.0.
- Too fast: the theta_ep versus delta_w/E_w paragraph. |Sigma_m| ~ <|g|^2>/E_w and the "about 0.2" are asserted, not derived.
- Outcomes: explain why the soft phonon is harmless: yes. State and apply the window theorem: yes.

### 13.7 Renormalization
- Lost: none. The ZG argument is clear enough for me. Persona (c) has a reservation, below.
- Used before defined: none.
- Outcomes: show f-sum transfer from S^0 to S^PA: yes. Explain why WL/ZG double-count the sideband: yes. Estimate the nonadiabatic correction: yes (2.0 + 0.4 + 0.8 meV).

### 13.8 Excitons and bosonic absorption
- Lost: one statement. "Excitonic edge exceeds free-pair by 81, 16, 7.3" sits right after the single-branch keyresult. The 16 and 7.3 are two-branch (TA+TO) values; for TA alone I get 12.7 and 6.5. Fix: say "two-branch".
- Own field, checked:
  - the dark-photon in-medium mixing zeta_eff = zeta/eps_1 and L = eps2/|eps|^2;
  - the ALP rate (3 m^2/4 m_e^2)(g^2/e^2) sigma_1;
  - the Sommerfeld factor 2 pi xi/(1 - e^{-2 pi xi});
  - the cancellation of rho_chi/m_phi in the absorption rate.
  All are correct.
- Outcomes: build the replica edge eq:13.8-edge: yes. Compute a dark-photon rate from a cold edge: yes. Explain why the dark photon has no new amplitude: yes.

### 13.9 The silicon window
- Not reproducible from the text: the reach numbers. Examples are 3e-29 cm^2 at 0.36 MeV and the ratios 0.24-0.56. They need the form-factor curve, the model eps and the halo integration, none of which is printed. This is acceptable for an estimate, but a one-line table of the form factor would let a reader check.
- Own field:
  - The mass power p_on + 7/2 relies on eta ~ (v_max - v_min)^2 at the escape edge, that is, on the smoothly truncated halo of tab:1-shm. A sharply truncated Maxwellian gives a linear edge and one power less. The keyresult should say "for the halo of tab:1-shm".
  - Error: the Summary says the external factor is "one inverse macroscopic dielectric function ... 1/40 to 1/48". Those are the head values. The macroscopic values in WE 13-external are 1/30-1/38.
- Inconsistency: 13.3 and 13.6 (last paragraph) say the onset exponents hold for |q| <= 1.33 keV. That is where the parabolic window closes. With the computed bands it closes at 1.27 keV (fig:13-offshell). Say which.
- Outcomes: read the edge order and the status table: yes. Derive the mass power at the onset: yes. Reproduce the joint minimum: no, it needs bands, as stated.

### Persona (b) on condescension and errors in my field
- No condescension. Ward identity, optical theorem, linked-cluster theorem and cut diagrams are used correctly.
- D.37's "Ward identity" is really on-shell invariance under a field redefinition (an equivalence-theorem argument). The name is acceptable.
- Errors: the Summary factor (above), and the halo-edge dependence of p_on + 7/2, which is left unstated.

**Persona (b) verdict: MINOR GAPS.** Nothing blocks the material that follows.

## Persona (c): condensed-matter theorist (DFT, many-body; no dark-matter physics)

### Section by section
- 13.1
  - The dark-matter kinematics (v_max, the parabola qv - q^2/2m) are introduced through Ch. 1 references, and I could follow them.
  - Used before defined, for me: eta and F_DM, which are recalled only later in 13.9.
  - Outcome (window kinematics): yes.
- 13.2
  - Correct, and the Herzberg-Teller derivation eq:13.2-HT is clean.
  - It rightly notes the filled-band part of the change of the valence state that a Sternheimer phonon run discards.
  - The error estimate eq:13.2-err is fine. D.35 gives a bound with delta_off - 2 omega.
  - Outcome: yes.
- 13.3
  - The symmetry argument treats e^{iq.r} as Delta_1 without the phases of the nonsymmorphic elements. 13.9 does this properly for m_z (w/2 - tau normal to the plane). A forward pointer, or one line that the screw/glide phases cancel for G = 0, would satisfy a careful reader.
  - The LA = Delta_1, LO = Delta_2' assignment agrees with the usual literature.
- 13.4
  - The local-field factorization is right.
  - The adiabatic-LDA k_xc source is a nice point and is standard in TDDFT second-order response.
  - The WE attributes the 13-22% deficit of RPA eps_inf (10.2/9.1 against 11.7) to "what RPA misses at long wavelength". With scissor-shifted bands the deficit is mostly the missing electron-hole attraction (the vertex/BSE), which the scissor does not compensate. Say so.
- 13.5: correct. The ill-posedness argument for the inversion by branch is a good, non-obvious point.
- 13.6
  - The soft-limit construction (comoving vertex, Galilean term absent from frozen-strain D) is correct. I confirmed it from the WE numbers.
  - Fano paragraph: the claim that PT invariance makes every amplitude real "with and without spin-orbit coupling" needs qualifying. With SOC, (PT)^2 = -1, the states come in Kramers pairs, and the amplitudes cannot all be made real. The vanishing must come from summing over Kramers partners, if it holds. The proof is in 8.6, which I did not recheck.
  - D.37-Qmin for emission: the sharp bound is delta_w/(v - c). The stated delta_w/(v + c) is valid but weaker (it is the absorption bound). This is numerically irrelevant.
- 13.7
  - The ZG paragraph says frequency-adjacent modes become degenerate "with the same sigma and the same coupling to the electrons". The second half is overstated. Neighbours in the frequency list can come from distant Q with quite different couplings. ZG's cancellation rests on the sign-alternation heuristic and the concentration of measure (which the book also gives), not on equal couplings. Soften.
  - The opening line "about 60 meV" zero-point renormalization does not match 56 (computed), 57 (8x8x8) and 71-73 (experiment), all elsewhere in the chapter. Pick one.
  - The nonadiabatic sqrt(omega) estimate and its comparison with Ponce are fair and correctly separated from differences between methods.
- 13.8
  - The exciton-phonon vertex matches Antonius-Louie.
  - The Elliott factorization with M^x held at the extrema is justified.
  - The two-pair completeness test is honest and well specified.
- 13.9
  - The glide-parity rule and the unsuppressed (2-00) vertex are correct as derived, and genuinely instructive.
  - Small mismatch: eps2 = 5.9e-4 from 11 cm^-1 at 1.25 eV implies n_r ~ 3.40. With n_r ~ 3.56 it is 6.2e-4. Negligible.
- Dark-matter material new to me (rate formula, v_min, eta, reference cross section, the mediators): I could follow 13.9's rate logic given Ch. 1 and Ch. 10. The cross-section values I take on trust.

### Notation and terminology (persona c)
- x is both the energy above onset (13.3, 13.8, 13.9) and the dark-matter vertex (13.4, D.36).
- ς is the pair source in 13.4 and the ZG signs in 13.7.
- a is the lattice constant and the Varshni coefficient (13.7).
- c is a band index, the sound speed c_nu and Stanford's c_1.
- None of these blocks reading, but the clash of x and ς inside one chapter is avoidable.

### Persona (c) on condescension and errors in my field
- No condescension. The many-body and DFT content is at research level and mostly correct.
- Points to fix: the SOC/PT reality claim (13.6); the "same coupling" ZG statement (13.7); the cause of the RPA eps deficit (13.4).
- What a computational person can do from 13.2, 13.4 and 13.6: the f-sum, the soft-limit test and the q = 0 test eq:13.2-q0 are well chosen controls.

**Persona (c) verdict: MINOR GAPS.**

## Learning outcomes, inferred (summary)
- Outcomes I can do:
  - window kinematics (13.1);
  - four-path amplitude and band-sum theorem (13.2);
  - S^PA, L^PA and onset exponents (13.3);
  - external screening factor and the 1/eps_mac factorization (13.4);
  - optical limit and temperature inversion (13.5);
  - soft limit and window theorem (13.6);
  - f-sum transfer, ZG double counting and the sqrt(omega) nonadiabatic estimate (13.7);
  - replica edge and bosonic absorption rates (13.8);
  - edge order and mass power (13.9).
- Outcomes I cannot do from the text, as the book itself says: the pair-channel size, the joint zero-phonon minimization (needs bands) and the rate estimate of 13.9 (inputs not printed).

## Overall
Both personas would keep reading. Every derivation I attempted closed, and every number I recomputed agrees, except the items below.

Must-fix:
1. The Summary's "macroscopic factor 1/40-1/48" should read 1/30-1/38; or call it the head factor.
2. WE 13-exchange: state the twist value and the phase convention of the phonon vertex, which changes the 2.4 factor.

Should-fix:
3. The 1.33 versus 1.27 keV range for the exponents.
4. "Halves |M|^2" holds for one sign only.
5. "16, 7.3" are two-branch values.
6. Halo-edge assumption in eq:13.9-medge.
7. SOC/PT reality claim.
8. ZG "same coupling".
9. "About 60 meV".
10. The bound-pair q* convention in WE 13-onset.
11. Reconcile D +- c p with D + v p in 13.6.
12. A Delta-line table in 13.3.

**Verdict: MINOR GAPS.**
