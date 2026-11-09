# Independent check: direct spin-current pair breaking and ALP absorption (s15-4, D-40)

Scope: tex/ch15/s15-4.tex Sect. "Spin-current absorption", tex/appD/D-40.tex, figscripts/ch15/abs15.py,
fig15_3.py/.log, we15_4.py/.log. No tex edited. Scratch: num.py and sym.py in the session scratchpad.

## Verdict: CORRECT WITH CAVEATS

The direct term is real and the formula, the sum rule and the numbers check out. In a singlet BCS state the uniform spin
current does not commute with H_MF and creates zero-momentum triplet pairs above 2Delta. Published Al-SC ALP projections
leave this channel out. They do so through a spin-trace step that does not hold with anomalous propagators, not for a
physical reason the book missed. The caveats (end of file) concern the clean-limit regime, the line shape and the framing of
the 10^4 comparison, not whether the term exists.

## 1. Derivation from scratch

Operator. L = (g/2m)(d_mu a) psibar gamma^mu gamma5 psi. Its NR reduction (Mitridate et al. 2106.12586 Eq. L_int_eff;
Berlin et al. 2312.11601 Eq. HamDeriv) is H = -(g/2m) grad(a).sigma - (g/2m) adot sigma.v, with v = p/m (symmetrised).
- Wind term: at q -> 0 it is the total spin, conserved by H_MF (and full H without SOC); at q = m_a v_DM its pair amplitude
  is O(q v_F Delta/E^2), about v_DM^2 ~ 1e-6 below the axioelectric term. Negligible.
- So the controlling operator is O = sum_i sigma_i.v_i: a scalar contraction, with no polarisation vector. The ALP carries
  no spin index to project.

Nambu form. Psi_k = (c_k_up, c^dag_{-k,down}). With v_{-k} = -v_k, the relabelling k -> -k in the down term gives:
- O_z = sum_k v^z_k (n_k_up - n_k_dn) = sum_k v^z_k Psi^dag tau3 Psi (spin and odd-v signs cancel); charge current: Psi^dag 1 Psi.

Commutators (sympy):
- [tau3, xi tau3 - Delta tau1] = 2i Delta tau2 != 0, and [1, h] = 0.
- Directly: [O_z, c^dag_{k up} c^dag_{-k dn}] = 2 v_k c^dag c^dag: a Cooper pair carries spin current, not charge current.

Spectrum. In the quasiparticle basis the off-diagonal element of tau3 is Delta/E (sympy: (M01)^2 - Delta^2/E^2 = 0). This
is the pair-creation amplitude v^z Delta/E into gamma^dag_k1 gamma^dag_k2, with coherence factor (uv'+vu')^2 -> Delta^2/E^2
at q = 0. With S_OO = 3 S_{O_z O_z} and sigma^J := (pi e^2/(omega V)) S_OO/3 (normalised so sigma^J = sigma_1 in the normal
metal):
  sigma^J = (pi e^2/omega) N_1 <v_z^2> int dxi (Delta^2/E^2) delta(omega-2E) = 2 pi omega_p^2 Delta^2 /[omega^2 sqrt(omega^2-4Delta^2)]
using omega_p^2 = 2 e^2 N_1 <v_z^2>. This is identical to Eq. 15.4-sJ / D.40-sJ, with threshold 2Delta and an inverse
square-root edge.
- Total weight: int_1^inf dx/(x^2 sqrt(x^2-1)) = 1 (sympy) -> (pi/2) omega_p^2. Fractions 0.866 < 4Delta, 0.995 < 20Delta: match.

Charge current comparison. Its vertex is the unit matrix, which is diagonal in the quasiparticles. Pairing leaves its weight
in the delta(omega) supercurrent, so a clean sample has no absorption from it. This is consistent with D.40.

Spin-trace check. In the FF (anomalous) part of the bubble, F ~ i sigma_y:
- tr[sigma_z F sigma_z^T F^dag] = -2 vs tr[F F^dag] = +2; the odd velocity v(k)v(-k) = -v^2 flips it again. So FF adds for
  the spin current and cancels for charge. A normal-state spin-trace factorisation loses exactly this sign.

Conserving-approximation check (this point is not in the book and strengthens it):
- A contact s-wave singlet pairing term psi_up^dag(x) psi_dn^dag(x) commutes with the local s_z(x). H_MF therefore keeps
  local spin continuity with the bare spin current sum sigma v. This differs from charge, where the Anderson problem arises.
- Hence J_s = i[H_MF, D_s], with D_s = sum sigma_z x. The spin f-sum <[[H,D_s],D_s]> = n/m holds exactly in mean field.
- s-wave ladder corrections vanish for the odd-parity vertex v^z(k). So BCS is gauge-consistent for spin; only l = 1
  interactions correct it (Landau F_1^a, triplet p-wave pairing).

## 2. Normal-state limit and the sum rule

- Clean normal metal without SOC: intraband sigma.p is conserved, weight is delta(omega). Published projections absorb
  through momentum relaxation (phonons, impurities), as for charge.
- Independent sum rule. For any spin-independent H (lattice plus Coulomb), J_s = i[H, D_s] exactly, so
  int_0^inf sigma^J domega = (pi/2) omega_p^2 holds independently of interactions. The intraband part uses the band
  omega_p^2.
- A singlet ground state has zero spin stiffness at T = 0: the Yosida function vanishes and there is no spin superfluid.
  From the mean-field numbers, the static paramagnetic spin-current response (2/pi) int sigma^J domega = omega_p^2 exactly
  cancels the diamagnetic term, so the spin Drude weight D_s = 0.
- The lowest S = 1 excitations at zero momentum are two-quasiparticle states at >= 2Delta. The exact weight therefore has
  to sit above about 2Delta, or in a triplet collective mode just below it.
- This is the same physics as the vanishing Pauli susceptibility (Knight shift) of a BCS superconductor: the small-q
  spin-density weight n q^2/m moves from omega < q v_F to omega >= 2Delta. So the claimed weight transfer is physical.

Mixed and transverse components:
- sigma_x v_x and sigma_y v_y create m = +-1 triplet pairs with the same amplitude, by SU(2) of the singlet.
- Cross terms i != j vanish (a pi spin rotation about z flips sigma_x, not sigma_z). sigma_z v_x would respond like
  sigma_z v_z (cubic), but the scalar sigma.v does not contain it. So S_OO = 3 S_zz; the s15-4 statement holds.

## 3. Spin-orbit coupling in Al

- SOC does not create the effect, and in Al it barely changes it. Pairing is between Kramers partners, so the pseudospin
  current keeps the tau3 Nambu structure and the pair-breaking matrix element survives.
- Elliott-Yafet spin-flip rates in Al are about 1e-4 of the momentum rate. Meservey-Tedrow tunnelling in Al films gives
  hbar/tau_so ~ (0.03-0.15) Delta, and much less in clean bulk.
- Only a fraction of order hbar/(tau_so Delta) of the weight stays at low frequency, as in the residual-Knight-shift
  analogue (Ferrell, Anderson 1959). The direct term is not a Drude response already contained in published sigma_1.
  The normal-state relaxation sigma_1 encodes is momentum relaxation; SOC adds a negligible spin-flip channel.
- Dirty limit: impurity-assisted absorption is the normal-state analogue (book: case-I factor). In strong-SOC metals
  (Sn, Pb films) with 1/tau_so >~ Delta the conclusion would weaken substantially. Not Al.

## 4. Literature (INSPIRE citations of 2106.12586; arXiv sources read, then deleted)

- Hochberg, Lin, Zurek 1604.06800 Eq. (rateAxion): |M|^2 = 3(g/2m)^2(omega/e)^2 |M_gamma|^2 from free-electron
  e + a -> e + phonon with normal-state spinors; superconductivity only via the photon's coherence factor (their Eq. 17).
  No direct pair-breaking term.
- Mitridate, Trickle, Zhang, Zurek 2106.12586:
  - Eq. (spin_tr) sets Pi_{Sigma^i,Sigma^j} = delta^{ij} Pi_{1,1}, "obviously valid for one-loop"; for the SC: "the
    electron-phonon coupling is spin-independent, so the same simplification applies".
  - Sect. V treats Al-SC electrons as free quasiparticles, with Re Pi taken from the normal metal ("carry over to the
    superconductor case").
  - This step drops the FF sign flip above: omitted by assumption, not excluded for a stated physical reason. Their
    field-redefinition footnote concerns operator coefficients only.
- Berlin, Millar, Trickle, Zhou 2312.11601:
  - The axioelectric term acts as a spin-directed effective field. For unpolarised targets they relate the rate to Im eps
    through a single-electron mapping (j_i = chi_ei E), warning "care must be taken in understanding the individual
    electronic response". Paired electrons break that mapping.
  - Their Sect. on spurious EDMs gives sigma.Pi/m = i[H0, sigma.x] for spin-independent H0.
- Bloch, Knapen 2411.10542: same commutator trick (sigma.p -> omega sigma.x) for nuclear spins; conceptual analogue.
- Chen et al. 2202.11716: without spin degeneracy the ALP rate is not a photon self-energy. Gelmini et al. 2006.13909:
  scalar screening only, not relevant.
- No paper found that treats direct spin-current/spin-dipole pair breaking of ALPs in superconductors. Searches covered
  INSPIRE (refersto 2106.12586, 1604.06800 topics) and arXiv/lit.py queries on axion, superconductor, spin current,
  axioelectric and pair breaking.

Field-redefinition objection:
- The pseudoscalar and derivative forms agree on shell. With spin-independent H0, the term adot sigma.v equals, by a
  unitary transformation, (g/2m) addot sum_i sigma_i.x_i: a uniform spin-dependent "electric" field.
- This maps the rate onto the q -> 0 spin-dipole (spin-density) response, with S_JJ = omega^2 S_DD. It does not remove the
  channel. It re-expresses it as the gapped long-wavelength spin susceptibility of the singlet state. The objection fails.

## 5. Numbers (independent script; rho_chi = 0.3 GeV/cm^3, rho_T = 2.70 g/cm^3, omega_p = 12.29 eV, Delta = 0.18 meV)

Rate formula used: R = 3 g^2 rho_chi m_a sigma / (4 m_e^2 e^2 rho_T). I re-derived it by golden rule and it matches HLZ.

| quantity at m_a = 0.72 meV | mine | book/log |
|---|---|---|
| sigma^J_dir | 9.513e4 eV | 9.51e4 |
| R_dir | 1.143e25 g^2 /kg/yr | 1.14e25 |
| g_aee for 3 /kg-yr (direct) | 5.12e-13 | 5.1e-13 |
| sigma_1^S (Holstein, Debye a2F, lam_tr 0.39, omega_D 37 meV) | 7.86e-4 eV | 7.86e-4 |
| g_aee (phonon-assisted sigma_1^S) | 5.64e-9 | 5.6e-9 |
| g_aee (normal-metal Holstein sigma_1^N) | 2.25e-9 | (not quoted) |
| events at g = 1e-13 (direct) | 0.114 | 0.11 |
| g_aee with a 1/(1+lambda_ep = 0.43) Z factor | 6.1e-13 | (n/a) |
| 50 nm film, Mattis-Bardeen sigma_1 = sigma_n g_II | g = 1.98e-12 | (n/a) |
| 50 nm film, spin channel sigma_n g_I | g = 1.48e-12 | (n/a) |

The 5.6e-9 is the book's own recomputation, using the published method (sigma_1 -> rate) with its Holstein model. It is
not a value read off the published curves. Mitridate et al. use 2Delta = 0.6 meV, which puts 0.72 meV almost at their
threshold.

## Caveats the text should state

1. Clean limit means mean free path >> xi_0 ~ 1.6 um: bulk high-purity Al. In films (the usual detector) the dirty form
   applies, and the published sigma_1 mapping on the film's own Mattis-Bardeen sigma_1 already gives g ~ 2e-12, against
   1.5e-12 for the spin channel.
   - The 10^4 gain is over phonon-only clean-Al projections, not over every sigma_1-based estimate. s15-4 should say so in
     one sentence.
2. The line shape at a given m_a depends on several corrections; the integrated weight is protected by the exact sum rule.
   F_1^a backflow, a possible triplet p-wave exciton near 2Delta (l = 1 vertex), strong-coupling Z ~ 1/(1+lambda) (g x1.2).
   The text names the FL factor but not the triplet-pairing vertex or a possible sub-gap triplet mode.
3. SOC: negligible for Al (hbar/tau_so << Delta). It is the controlling caveat for heavy-element superconductors.
4. Published treatments also apply the photon coherence factor to the ALP in the impurity- and phonon-assisted channels.
   s15-4 already flags the phonon case as open.
5. Optional strengthening: add the conserving-approximation remark and the Knight-shift (Yosida) analogy. They show the
   result follows from an exact sum rule plus the singlet gap, not from a mean-field artefact.
