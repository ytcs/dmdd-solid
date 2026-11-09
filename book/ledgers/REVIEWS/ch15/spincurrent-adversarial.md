# Adversarial review: direct spin-current pair breaking and ALP absorption (s15-4, D-40)

Scope: tex/ch15/s15-4.tex (Sect. 15.4-spin and Sect. 15.4 intro), tex/appD/D-40.tex (first two subsections),
tex/ch10/s10-7.tex (Sect. 10.7-alp), tex/ch08/s8-1.tex (Eq. 8.1-alp), figscripts/ch15/abs15.py, we15_4.py, fig15_3.log.
No tex edited, nothing committed. Scratch scripts: session scratchpad calc/f1a.py and calc/num.py.
I started from the assumption that the claim is wrong. The derivations below did not let me keep that assumption.

## Verdict: STANDS WITH CORRECTIONS

The mechanism is real. It is not a mean-field artifact, it is not removed by any equivalence theorem, and the published
projections leave it out because of an explicit spin-trace assumption that does not hold for paired electrons.
Required corrections:
- C1 (false statement). "In the clean normal metal the spin current commutes with the Hamiltonian" (s15-4 l.124,
  D-40 l.36) holds only for a one-body band Hamiltonian. Spin-independent, Galilean-invariant e-e interactions do NOT
  conserve the spin current (spin Coulomb drag). Normal phonon processes relax it too. The normal metal therefore already
  absorbs through this channel.
- C2 (overclaim). "The weight itself is fixed beyond mean field" (s15-4 l.124, D-40 l.38) is true only of the TOTAL
  weight over all frequencies. The weight that sits near 2Delta is the coherent quasiparticle part,
  ~ (pi/2) wp^2 (1+F1a/3)/(1+lambda). The remainder sits at omega ~ omega_D and at the scale of E_F.
  The factor 1/(1+lambda) = 0.70 follows from the sum rule and must be applied, not left as an optional caveat. The
  headline becomes g_aee ~ 6.1e-13 (not 5.1e-13). D-40's "Only interactions in the l = 1 channel ... correct the line
  shape" should also name the self-energy (lambda, and F1s through m*).
- C3 (line shape). The F1a dressing has the Leggett form below. For |F1a/3| <= 0.1 it changes sigma^J(4Delta) by a
  factor 0.75-1.3, which moves g by +-15%. For F1a < 0 a bound S = 1, l = 1 mode forms below 2Delta and takes weight.
  The book says this qualitatively, which is acceptable. The formula should be given.
- C4 (attribution). The "5.6e-9" is the book's own recomputation (Debye alpha^2F_tr, its sigma_1^S = 7.9e-4 eV in
  Eq. 10.7-alp). It is not a number read off the published curves, and the text should say so. The reason the published
  works omit the channel is identified below (Mitridate et al. Eq. 28). The book's diagnosis of that omission is right.
None of C1-C4 touches the existence or the order of magnitude of the effect. Relative to phonon-only projections the gain
in g stays at ~1e4. Relative to a correct normal-state spin baseline that includes spin drag, it is ~30-150.

## 1. Which operator

The relativistic coupling is L = (g/2m) d_mu a psibar gamma^mu gamma5 psi. Its nonrelativistic reduction (FW, or Mitridate
et al. Table 1, or Berlin et al. 2312.11601 Eq. 19) is
  H = -(g/2m) [ grad(a).sigma + adot sigma.(p+p')/(2m) ] + O(1/m^2).
Book Eq. 8.1-alp has (g/m)[grad(a).s + adot sum_alpha s^alpha v^alpha] with s = sigma/2. These are the same expression,
so the normalisation of g_aee is the standard one. Its rate formula, Gamma = (3 m^2 g^2/(4 m_e^2 e^2)) sigma_1, matches
Hochberg-Lin-Zurek 1608.01994 Eq. 10, Mitridate Eq. 47 and Berlin Eq. 54 (unpolarized).
- Wind term, at amplitude level. |grad a| = m v_DM a, while the axioelectric term carries m a v_F. The wind term couples
  to the spin density S(q), which is T-odd. Its pair amplitude has the case-II factor (xi'-xi)Delta/(2EE') ~ q v_F/Delta.
  The ratio of wind to axioelectric amplitude is therefore (v_DM/v_F)(q v_F/Delta) ~ 0.15 x 2.7e-5 ~ 4e-6. The wind term
  is negligible, and the book's statement on this is right.
- Pseudoscalar versus derivative form. psi -> exp(i g a gamma5/2m) psi maps one form to the other, up to an anomaly term
  ~ alpha g a F Ftilde/m and terms of O(g^2). On shell, and in a medium without spin order, the two give the same
  amplitudes.
- No equivalence theorem removes the term. For any spin-independent H (exact, or H_MF with local s-wave pairing),
  sum sigma.p/m = i[H, D], with D = sum_i sigma_i.x_i. The unitary transformation U = exp(i lambda(t) D), with
  lambda = g adot/2m, cancels the velocity-form coupling. It leaves -lambdadot D, the length form, with
  |lambdadot D_fi| = m_a lambda |D_fi| = lambda |omega_fi D_fi|. The rate is identical. Only a STATIC a can be gauged
  away; this is the Schiff-type statement of Berlin et al. Sect. V, Eq. 92, which concerns level shifts.
- Conclusion. Absorption at q -> 0 is controlled by O = sum_i sigma_i.v_i, the trace of the spin current. The book uses
  this operator.

## 2. Commutator and conservation (the crux)

- Two-body commutator. [p1 sigma1z + p2 sigma2z, V(r1-r2)] = -i grad V(r12) (sigma1z - sigma2z). This is nonzero for
  antiparallel spins. For the charge current (sigma -> 1) the forces cancel by Newton's third law.
- So Galilean invariance protects the charge current, but NOT the spin current. A contact interaction U delta(r12) does
  not protect it either: it acts only in the singlet, s-wave channel, where it randomises the relative momentum.
- The EXACT interacting H (lattice + Coulomb + phonons, without SOC) does not conserve J_s. No Ward identity forces the
  q = 0 absorption to vanish. The non-commutation of the mean-field theory, [tau3, xi tau3 - Delta tau1] = 2i Delta tau2,
  is therefore not an artifact of breaking a conservation law. It mirrors a non-conservation that is already in H.
- What H does conserve is the LOCAL spin density, with or without interactions, because there is no SOC. Local s-wave
  pairing psi_up^dag psi_dn^dag commutes with s_z(x). So H_MF obeys spin continuity with the bare current, J_s = i[H_MF, D_s].
  The bare BCS bubble is conserving in the spin channel. This is unlike charge, where the phase mode (Anderson) is needed.
  The s-wave ladder does not dress the vertex v^z_k, which is odd in k.
- No spin Drude weight survives at T = 0. A uniform static spin vector potential (up +A, down -A) is a pure gauge
  transformation of any spin-independent H, U = exp(i A sum x_i sigma_i^z). It leaves the singlet order parameter
  psi_up psi_dn invariant. The ground-state energy therefore does not depend on the spin twist, and the spin stiffness
  vanishes exactly, beyond mean field. Mean field reproduces this: (2/pi) int sigma^J = wp^2 equals the diamagnetic term.
- The exact f-sum rule [[H,D_s],D_s] = N/(4m) involves only the kinetic term, because D_s commutes with every
  spin-independent term. Its total therefore lies at omega > 0. The lowest q = 0, S = 1 states are two-quasiparticle
  states at energies >= 2Delta, or a bound triplet mode just below 2Delta (Sect. 3).
- Physical check. The relabelled state U(delta)|BCS> = prod (u_{k-delta} + v_{k-delta} c^dag_{k up} c^dag_{-k dn})|0>
  has ↑ and ↓ Fermi seas shifted in opposite directions. In the normal metal that state is stationary under a one-body
  H. In the BCS state it is not an eigenstate, and it decays into pairs at 2E_k.
- Conclusion. The crux resolves in the book's favour, but for a different reason from the one D-40 gives. D-40 argues
  from H_MF only. The decisive fact is that the exact H does not conserve J_s either, so mean field breaks no symmetry
  that H has.

## 3. Vertex corrections, sum rule, normal state

Normal Fermi liquid (Leggett; Galilean invariant):
- The quasiparticle spin current is j_s = (1 + F1a/3) v*.
- The coherent spin Drude weight is D_s = (n/m*)(1 + F1a/3) = (n/m)(1 + F1a/3)/(1 + F1s/3). Compare D_c = n/m, which is
  exact.
- The rest of the sum rule, (n/m)[1 - D_s m/n], is incoherent multi-pair weight at the scale of E_F.
- The spin current relaxes by collisions, through spin drag or spin diffusion, at a rate 1/tau_sd ~ beta(omega^2 + pi^2 T^2).
  The book's statement that it commutes with H is false (C1).

Normal Al, T -> 0, omega = 0.72 meV:
- I take beta ~ 0.03-0.3 /eV (Quinn-Ferrell scale), so Gamma_sd ~ 1.6e-8 to 1.6e-7 eV.
- This gives sigma^J_N ~ wp^2 Gamma_sd/omega^2 ~ 5-45 eV. The phonon-assisted normal-metal value is sigma_1^N = 4.9e-3 eV
  (fig15_3.log). So even the normal metal absorbs ALPs through spin drag far more than the published sigma^J = sigma_1
  mapping allows. The mapping misses this because Galilean invariance kills only the charge drag.
- The corresponding g_aee(3/kg-yr) is 2-7e-11. The superconducting direct term is still 5e-13: 1e3 to 1e5 larger in
  sigma. It is not an incremental reshuffle. The same sum-rule weight moves from a Lorentzian of width ~1e-8 eV centred at
  zero into a window of width ~Delta at the absorption frequency, so sigma ~ wp^2/Delta.

Superconductor with F1a, Leggett form, dynamic. Let f(omega) be the normalised bare BCS spin-current bubble, with
f(0) = 1 and Im f = 2pi Delta^2/(omega sqrt(omega^2 - 4Delta^2)). Then
  K_s(omega) = (n/m*)(1 + F)(1 - f)/(1 + F f),  F = F1a/3,  sigma^J = Im K_s/omega.
- Check at omega -> 0: K_s -> 0, so there is no spin stiffness. In the normal limit, f -> 0 and K_s -> D_s.
- By Kramers-Kronig the weight above 2Delta is (pi/2) D_s, not (pi/2) n/m. My numerics confirm
  (2/pi) int Im f/omega = 1.000.
- sigma^J(4Delta)/bare = 1.145 (F = +0.05), 1.305 (+0.1), 0.869 (-0.05), 0.750 (-0.1).
- For F < 0 the denominator 1 + F Re f = 0 has a root below 2Delta, because Re f diverges as (2Delta - omega)^{-1/2}. It
  is a bound S = 1, l = 1 mode. Its binding is 5.6e-3 Delta at F = -0.05, 2.1e-2 Delta at -0.1, and 7.4e-2 Delta at -0.2.
- For F > 0 the inverse-square-root edge is softened to (omega - 2Delta)^{1/2}.

Electron-phonon (Eliashberg):
- The phonon f-function is spin-independent, so it adds nothing to F1a. It does give m* = m_b(1 + lambda).
- The coherent normal-state spin Drude weight is therefore wp^2/(1 + lambda), the same reduction as for the charge Drude
  weight at omega << omega_D. The remainder is the spin analogue of the Holstein band at omega ~ omega_D.
- In the superconductor the weight within a few Delta of the edge is (pi/2) wp^2/(1 + lambda). With lambda = 0.43,
  sigma^J falls by 0.70 and g rises by 1.196, to 6.1e-13. This factor is mandatory (C2). The book now presents it as
  "would raise".

Summary of this section: the bare BCS bubble gives the right structure (threshold 2Delta, coherence factor Delta^2/E^2,
odd-k vertex with no s-wave dressing). The prefactor needs Z_s ~ (1 + F1a/3)/(1 + lambda) and the F1a denominator above.
Neither cancels the effect.

## 4. Literature

Searches: INSPIRE free text and titles; arXiv abstract queries through lit.py. Queries included: axion superconductor
absorption, spin current, axioelectric superconductor, Cooper pair, spin Coulomb drag dark matter, in-medium spin
response. I found no paper that computes direct, third-body-free pair breaking by the ALP spin current, or the
spin-current correlator of a superconductor for dark matter. Candidates checked and excluded: 2412.20850 (transmon
quasiparticles: phonon-mediated, sigma_1 based), 2610.27764, 2510.19918.

Published Al-SC ALP projections:
- Hochberg-Lin-Zurek 1604.06800, 1608.01994.
- Mitridate-Trickle-Zhang-Zurek 2106.12586, Sect. III B and Sect. V.
- Chen et al. 2202.11716, which shows the Al-SC curve.
- Berlin-Millar-Trickle-Zhou 2312.11601, Eq. 54 and footnote 3: "a + e -> e + phonon in non-spin-ordered
  superconductors [84, 87]".

Why the published projections drop the channel. They drop it BY ASSUMPTION, and the assumption is invalid here:
- Mitridate et al., Eq. 28: "we have simplified the spin trace assuming the electron loop does not involve non-trivial
  spin structures; Pi_{Sigma_i, Sigma_j} = tr(sigma_i sigma_j)/tr 1 Pi_{1,1} ... In the superconductor calculation in
  Sec. V ... the electron-phonon coupling is spin-independent, so the same simplification applies."
- Their Sect. V computes normal-state cut diagrams and then multiplies by a BCS coherence factor (Eq. 103).
- With Nambu propagators the anomalous part is F ~ i sigma_y. Then tr[sigma_z F sigma_z^T F^dag] = -tr[F F^dag], and
  with v(-k) = -v(k) the FF term adds for sigma.v and cancels for v. This is the direct term. It has no phonon line, so it
  cannot appear in a two-loop phonon calculation.
- Berlin et al. Sect. IV.2.1 assume a per-electron susceptibility chi_ei that does not depend on that electron's spin
  ("electrons respond incoherently"). That is the independent-electron premise that pairing violates.

Related known physics, consistent with the book:
- Vanishing Pauli susceptibility (Yosida) and the Knight shift; residual Knight shift through SOC (Ferrell 1959,
  Anderson 1959). This is the q-space analogue of the transfer of spin weight above 2Delta.
- Leggett 1965 Fermi-liquid theory of superfluids, the source of the Sect. 3 form.
- Spin Coulomb drag (D'Amico-Vignale 2000), which supports C1.
None of this prior work applies the effect to dark-matter absorption.

## 5. Numbers (own formula, calc/num.py)

Inputs: wp_intra = 12.29 eV, Delta = 0.18 meV, rho_chi = 0.3 GeV/cm^3, rho_T = 2.70 g/cm^3,
R = (rho_chi/(rho_T m))(3 m^2 g^2/(4 m_e^2 e^2)) sigma^J.

| case at m_a = 0.72 meV = 4 Delta | sigma^J (eV) | g_aee for 3 /kg-yr |
|---|---|---|
| bare BCS (book) | 9.51e4 | 5.12e-13 (0.114 events at 1e-13) |
| x 1/(1+lambda), lambda = 0.43 (required, C2) | 6.65e4 | 6.1e-13 |
| also F1a/3 = +0.1 / -0.1 | | 5.4e-13 / 7.1e-13 |
| normal Al, T -> 0, spin drag only | 5-45 | 7e-11 to 2e-11 |
| book's phonon-assisted sigma_1^S in Eq. 10.7-alp | 7.9e-4 | 5.6e-9 |

The book's numbers (fig15_3.log: 5.1e-13, 5.6e-9; 87% of the weight below 4Delta) reproduce. Corrected headline:
g_aee ~ (5-7) x 1e-13 for clean bulk Al, roughly 1e4 below the phonon-only mapping.

## Points the book should add (text-level)

1. Replace "the spin current commutes with the Hamiltonian" in the normal state with: "commutes with the one-body band
   Hamiltonian. Electron-electron collisions (spin drag) and normal phonon processes relax it, so the normal-state weight
   is a narrow Drude peak, not a delta function."
2. State the exact weight statement as "total, all frequencies". Put Z_s = (1+F1a/3)/(1+lambda) into Eq. 15.4-sJ, or
   carry it in the headline number.
3. Give the F1a-dressed form in D-40 and note the possible bound S = 1 mode for F1a < 0.
4. Label 5.6e-9 as "published method, our sigma_1^S" and cite Mitridate Eq. 28 as the precise point of omission.
5. Point out that the published normal-metal mapping also omits spin drag, as a side remark.

## Applied

Numbers: figscripts/ch15/spin15.py -> spin15.log (uses abs15.py; reproduces calc/f1a.py and calc/num.py).
- C1. s15-4 (paragraph after Eq. 15.4-sJ) and D-40 (after the weight integral): the spin current commutes with the
  one-body band Hamiltonian only; two-body forces enter with (sigma1 - sigma2), Galilean invariance protects only the
  charge current; e-e collisions (spin Coulomb drag) and normal phonon processes give a narrow normal-state Drude peak.
  Estimate in s15-4, summary and F row: sigma^J_N ~ 5-45 eV at 0.72 meV (beta = 0.03-0.3 /eV) vs phonon-assisted
  4.9e-3 eV; direct term (with Z_s) 1.5e3-1.5e4 larger (log; the brief's "1e3-1e5" is not what the numbers give, the
  bare form gives 2.1e3-2.1e4). Correct conserving argument stated: local s-wave pairing commutes with the local spin
  density; zero spin stiffness via the spin-twist gauge argument. D-40 notes D_s commutes with interactions, so the
  total-weight sum rule holds although J_s is not conserved.
- C2. "Weight fixed beyond mean field" -> total weight over all frequencies. Coherent weight near 2Delta =
  (pi/2) wp^2 (1+F1a/3)/(1+lambda_ep), stated as required by the sum rule (s15-4, D-40, summary, nuisance row, F row).
  Headline g_aee = 6.1e-13 (6.13e-13; bare 5.12e-13); 0.080 events at 1e-13; 1 meV: sigma^J = 2.31e4 eV, 4e6 x
  sigma_1^S; crossing with normal Holstein 10.9 meV (bare 11.5 meV, as plotted in Fig. 15.3b; caption says bare
  form and the 0.70 factor). ch17/s17-2 l.18 g value updated to 6.1e-13.
- C3. Leggett form K_s = wp^2/(1+lambda) (1+F)(1-f)/(1+Ff), sigma^J = -Im K_s/omega, in D-40 with ratios
  1.31/1.15/0.87/0.75 and bound S=1, l=1 mode bindings 5.6e-3/2.1e-2/7.4e-2 Delta; in s15-4 third caveat:
  g_aee -12 % to +15 % for |F1a/3| <= 0.1, range 5.4e-13 to 7.1e-13; nuisance row and F row updated.
- C4. s15-4, summary, F row: 5.6e-9 labelled as the book's recomputation with its phonon-assisted sigma_1^S = 7.9e-4 eV.
- Literature: s15-4 cites mitridate2021dark Eq. (28) and berlin2024physical Sect. IV.2.1 neutrally as using the same
  independent-electron spin trace. arXiv API: 2106.12586 (JHEP09(2021)123) and 2312.11601 (JHEP05(2024)314) verified;
  bib entry berlin2024physical added.
- Not changed: ch17 Fig./text "up to 11.5 meV" (tied to its plotted bare form of Eq. 15.4-sJ); fig15_3.py/log
  (bare form; their "if ... quasiparticle factor" line is superseded by spin15.log).
- Build: latexmk main.tex -outdir=/tmp/claude-0/build-spin, 0 LaTeX errors; no undefined citations; remaining
  undefined references are to unwritten chapters 18-21.
