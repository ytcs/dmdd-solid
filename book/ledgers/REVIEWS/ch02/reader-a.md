# Chapter 2 mock-reader review: persona (a), first-year PhD student

Read: Chapter 2 (Sects. 2.1-2.5 and Summary) linearly, from tex/ch02/*.tex with the built PDF for
cross-references; Appendix A.1-A.9, D.2, D.3 where Chapter 2 pointed to them; Chapter 1 reread for
the definitions it supplies (sigma_e, F_DM, eta, Eq. 1.5-rate, lattice vocabulary). Every derived
step was redone by hand, and checked with sympy or numpy where that was quicker (including a 2001-level
diagonalization for WE 2-continuum and the broadband averages of WE 2-twophoton).

**Verdict: MINOR GAPS.** Nothing blocks the material that follows. One sign slip in an intermediate
display of 2.4, a few small numerical mismatches, and missing appendix targets cost me time, but every
boxed result I tested is correct.

## Global observations
- **Unresolved references in the PDF.** The Chapter 2 pages of main.pdf show "??" 67 times (32 more
  in Appendix A). Most point forward to chapters not yet written, which is fine. The ones I wanted to
  follow are the proofs I am sent to: App. C.1 (delta limit, int sin^2u/u^2 = pi, delta(g(x)) rule),
  C.2 (continuum limit of sums), C.3 (angular integrals, sum_m |Y_lm|^2, j_1), C.4 (Sokhotski-Plemelj,
  finite part), C.9 (Yukawa transform, Eq. C.9-Gq, used in 2.3 and A.2). I could do each step myself,
  so this is a gap in what I could check, not a flaw in the argument.
- **Notation clashes I noticed.** V is both the box volume and the potential, often on the same line
  (Eq. 2.1-Vbox: V(x_chi - x_e) and 1/V^2). beta is 1/T in 2.5 and a radial decay constant in the
  2.2 hydrogen example. xi is the energy mismatch (2.1), the Coulomb parameter xi_C (2.2) and a speed
  moment (A.8). Omega is both solid angle and cell volume. "w" marks both E_w (continuum width) and
  Gamma_w (decay width). None of these confused me for long, but each made me stop.

## 2.1 Fermi's golden rule
1. Lost points: none. The derivative argument (d/dt of Eq. 2.1-Pstatic -> 2|M|^2 sin(xi t)/xi -> pi delta)
   is the clearest version of this derivation I have read.
2. Steps I could not reproduce: none. Checked: central-peak fraction 0.9028 ("90.3%"); Eq. 2.1-WEP by
   parts; short-time bracket E_w t/4 -> N_f|O|^2 t^2; long-time bracket pi/2 - 2/(E_w t) and the delay
   4/(pi E_w); Gamma = 2pi(0.892 meV)^2(2000/eV) = 10.0 meV; 2pi D_f = 8.27 ps. My own diagonalization
   gives first order 10% above exact at t = 21.92 eV^-1, P1 = 0.987 vs exact 0.630 at 1/Gamma, and
   agreement with 1 - e^{-Gamma t} to 0.36% at 1/Gamma, all as stated. Box algebra (Eq. 2.1-Vbox,
   2.1-sigma), relativistic dictionary and |M|^2 = 16 m_chi^2 m_e^2 |V~|^2 all check.
3. Used before defined: "Dyson series of the interaction picture" (forward ref to 2.4; fine for me).
   "Counter-rotating term" and "frame rotating with the perturbation" (Fig. 2-1 caption, WE): I had to
   work out myself that, with emission dropped, c~_f = c_f e^{i xi_f t} gives constant coefficients.
   One sentence would fix it.
4. Too slow / too fast: the paragraph on relativistic normalization and <f|iT|i> = i(2pi)^4 delta^4 M
   is fast for someone without QFT (which the book does not assume). I followed the algebra, but the
   T-matrix and Peskin conventions arrive with no preparation. Labelling it "for readers comparing
   with particle-physics papers" would tell me I can skim it.
5. Outcomes. Derive the golden rule and its window: yes. Track V through a two-body rate to sigma_T:
   yes (1/V^2 from |M|^2, V from the sum, V/v from the flux). Explain why absorption scales with rho_chi:
   yes, O = (phi_0/2) x operator, phi_0^2 = 2 rho_chi/m_phi^2.

## 2.2 Born approximation and form factors
1. Lost points: none blocking.
   - Para. on kinematic matching: "q >~ 0.4 keV" to cross 1.1 eV uses v_max = 2.65e-3, but the previous
     sentence set v ~ 1e-3 (which would give 1.1 keV). It matches Ch. 1's 0.42 keV; the text just needs to
     say "at v_max".
   - d Omega_q is the solid angle of p', not of q. The parenthesis explains this, but the subscript
     still misled me on first reading.
2. Not reproduced / mismatches:
   - WE 2-free: at m_V = 30 MeV I get sigma_T/sigma_e - 1 = 2.3e-8, not 3e-8. The other values (1.015,
     2.63, 192, q_max = 2.69 keV = 0.72 q_0) check.
   - WE 2-coherent: sigma_N/sigma_p = 953 "the values quoted in Sect. 1.4", but 1.4 quotes 950
     (from rounding 1.22 x 784). Harmless, but the two chapters should quote the same number.
   - Limit box (0.46 and 0.036 of the exact rate; 30% agreement): not attempted. These are figure-script
     outputs that need Coulomb continuum partial waves, so I take them on trust.
   - Everything else checks: Born radial integral, Rutherford, dsigma/dq and sigma_T = sigma_e, the
     sigma_e form of Eq. 2.2-bound, the angle average 1/(2qv) giving Eq. 2.2-spectrum, the f_ion phase-space
     factor 1/4 and prefactor sigma_e/(8 mu^2), the plane-wave Eq. 2.2-fion-pw (both spins), Helm
     small-q <r^2> = 3R^2/5 + 3s^2, R_nuc = 3.465/4.774 fm, first zeros 256/186 MeV, Born parameters
     1.2e-8 and 7.2e-4 for the dark-photon benchmark.
3. Used before defined: j_1 appears in the 1s->2p calculation ("4 pi i j_1(qr)") but is named "the
   spherical Bessel function" only in the Helm paragraph. Hartree-Fock orbitals are used here before
   2.3 sketches the idea. "Roothaan-Hartree-Fock" and "Woods-Saxon" are used with citations only, which
   is fine. "Bragg-like elastic response at reciprocal-lattice vectors" is a forward pointer; Ch. 1
   defined G, so I could follow it.
4. Too fast: the f_ion normalization step ("the sum over final states at fixed omega is |f_ion|^2/4
   per unit ln E_ej") hides the delta-function Jacobian (delta in omega -> 1/E_ej, then x E_ej back
   for d/d ln E). I reconstructed it, but one line would save the next reader ten minutes. Not too slow
   anywhere; the hydrogen example is very well judged.
5. Outcomes. Derive dsigma/dOmega and sigma = sigma_e for a heavy mediator: yes. Write the bound rate
   with f_{i->f}: yes. Hydrogen: F_1s = 16/(4+x^2)^2, F_1s(q_0) = 0.64, inelastic 1 - 0.41 = 0.59;
   |f_1s->2p|^2 = 72x^2/(9/4+x^2)^6 confirmed symbolically, peak 0.0836 at qa_0 = 0.671, 0.061 at q_0,
   small-q slope 2^15/3^10 = 0.555. Nuclei: F^2_Helm(q_max) = 0.998 (1 GeV), 0.886 (10 GeV), 0.356
   (100 GeV) for Si; 0.0019 for Ge at 100 GeV, q_max = 214 MeV. All as stated.

## 2.3 Second quantization
1. Lost points: none. The opening ("the two states differ in two entries") motivates the topic well.
2. Steps not reproduced: none, but Eq. 2.3-direct-exchange was terse ("reordering gives one sign per
   mismatch"). Doing it out: the two annihilation orders give +1 and -1, each pairs with two creation
   matchings, the four terms give 2[v_C(k) - delta_ss' v_C(|p'-p-k|)], and the 1/2 cancels the 2. Stating
   that the 1/2 is cancelled by the two equivalent labellings would close it. Checked: bilinear
   commutators Eq. 2.3-bilinear; normal ordering Eq. 2.3-normal; jellium k = 0 bookkeeping
   (N^2 v/2V - N^2 v/V + (N^2-N)v/2V = -N v/2V); the cross term factor 2 in Eq. 2.3-HC (k -> -k);
   the electron-nucleus matrix element; Si estimate d = 1.71 A = 3.2 a_0, 8.4 eV vs 1.3 eV, ratio 2d/a_0.
3. Used before defined: Bloch states, Wannier orbitals, magnons, spin-orbit coupling appear with forward
   refs only. Acceptable as signposts; none is needed to follow the algebra.
4. Pace: about right for someone without many-body theory. The two-orbital bond example is excellent.
   Slight overlap: the self-interaction removal is shown twice (field operators and plane waves); both
   are useful, so I would keep both.
5. Outcomes. Act with c, c^dagger and derive the anticommutators: yes. Write one- and two-body operators
   and n_e(q) = sum c^dagger_{k+q} c_k: yes. Write the Coulomb Hamiltonian with k = 0 removed by neutrality:
   yes. Get direct minus exchange: yes (above). D.2 proofs (lemma, two-body via the one-body result twice,
   basis change) all follow.

## 2.4 Second-order processes
1. Lost point (strongest finding). The unnumbered display of the inner time integral in "Second-order
   golden rule" has the wrong overall sign. With t_0 -> -inf and switching e^{t/tau_s},
   int_{-inf}^{t_1} dt_2 e^{[i(E_m-E_i)+1/tau_s]t_2} = +i e^{...t_1}/(E_i - E_m + i/tau_s)
   (equivalently -i e^{...}/(E_m - E_i - i/tau_s)). The text writes -i/(E_i - E_m + i/tau_s); sympy
   confirms the mismatch. The next display (c_f with A_2 entering like A_1), the key result Eq. 2.4-golden2,
   and the independent derivation in Eq. D.3-cm are all consistent with the *corrected* sign. So the
   slip is confined to that one line and nothing downstream changes. But a careful reader who
   multiplies through by (-i)^2 gets c^(2) with the opposite sign and stalls. Fix: flip the sign on that line.
2. Steps not reproduced: none besides the above. Checked: first-order Lorentzian area 2pi; cross-term
   contour integral 2pi i (3/tau)/(3i/tau) = 2pi, imaginary part odd; Rayleigh combination
   2(E_m-E_a)|O|^2/(omega^2 - (E_m-E_a)^2); Lorentzian normalization D|H|^2 2pi/Gamma = 1; finite-part
   identity and the -pi Gamma_w w''(0)/4 correction in Eq. 2.4-split; D.3 kernel, Markov integral,
   flat-continuum R(z), R'(0) = 2Gamma/(pi E_w) = 0.0064, survival excess 0.0023 (0.4%).
3. Used before defined: "direct gap", "vertical transition", "conduction-band minimum / valence-band
   maximum" carry forward refs to 3.3; Ch. 1 gave me enough to follow. "Dynamic polarizability" is
   undefined but standard.
4. Pace: the finite-part subsection is dense but complete; I needed the worked example to believe the
   sign claim (finite part negative for a peaked spectrum). The time-orderings discussion of Pauli-blocked
   intermediate states (last paragraph of "Time orderings") goes fast, but it is explicitly deferred to 6.5.
5. Outcomes. Second-order amplitude and T-matrix: yes. Two orderings and their denominators: yes. Width
   at resonance: yes. PV / delta / finite-part split: yes. WE 2-twophoton reproduced: A = -0.833 eV^-1,
   rate 6.9e-13 eV = 1.05e3 s^-1, factor 16; on resonance |A|^2 = 4.0e6, 4.0e-6 eV, cascade agreement
   4.7 parts in 1e6 once Gamma_w/2 is kept in the off-resonant denominator, P_m = 0.04. Broadband: exact
   2.410e5, delta 2.507e5 (+4.0%), fp -1.00e4, sum within 0.13%; at 30 meV off: delta 2785, fp 1795, PV
   197, off 6, sum within 0.6% of 4753, delta alone -41%. All as stated.

## 2.5 Thermal states and detailed balance
1. Lost points: none.
2. Steps not reproduced: none. Checked: relabelling proof of Eq. 2.5-db; thermal golden rule ->
   Eq. 1.5-rate term by term (q dq/(2pi)^2 measure and sigma_e/(4pi mu^2) prefactor, also = A.8-rateiso);
   S = 2pi n_T sum |f|^2 delta for the gas of 2.2 is consistent with Eq. 2.5-golden; n_F(1-n_F) identity;
   oscillator moments (2n_B+1 = 1.22 at 300 K; first moment |lambda|^2 omega_0); n_B values 0.109,
   2.5e-76, 9.1e-6, 1e-252, 1.27; lens volume and blocking fraction 3q/4k_F - q^3/16k_F^3.
3. Used before defined: none that matter; "f-sum rule", "Lindhard" and "fluctuation-dissipation" are
   forward-labelled.
4. Too slow: the Gibbs-state subsection and the derivation of n_F, n_B restate statistical mechanics
   that the persona is assumed to know. It is short, so it does no harm, but it could be cut to a
   reminder. The free-electron-gas numbers for silicon are well placed.
5. Outcomes. Average the golden rule over a thermal state and identify S(q, omega): yes. Derive and apply
   detailed balance: yes (e^{2.32} = 10.2 for the 60 meV phonon). Free electron gas: k_F = 3.57 keV =
   0.96 q_0, E_F = 12.5 eV, v_F = 7.0e-3, N_F = 9.2e7 eV^2; 7.8% of the sea active at q = 0.1 q_0.

## Overall
I would keep reading. The chapter does what its opening promises. Every rate is built from one formula,
the volume is tracked to the end, and each tool (form factors, occupation numbers, second order,
thermal averages) is tested on a worked example whose numbers I could reproduce. The derivations are
at the right level for me: I never needed an outside text, only paper and an hour per section. What
would make it CLEAR: fix the sign of the inner-integral display in 2.4; resolve or temporarily inline
the App. C targets that 2.1-2.4 send me to; add one line each for the rotating-frame trick (2.1), the
f_ion Jacobian (2.2) and the factor 1/2 in the direct-exchange count (2.3); align 953/950 and the
3e-8 value; and say "at v_max" for the 0.4 keV transfer.
