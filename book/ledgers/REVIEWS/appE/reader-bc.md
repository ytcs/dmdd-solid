# Appendix E mock-reader review: personas (b) and (c)

Scope. I read E-1 to E-13 in order, and ch03 (s3-1, s3-2) and ch04 (s4-1, s4-2, s4-7) where Appendix E points to them. Those are the only drafted sections. References to sec 3.3-3.6, 4.3-4.6, 4.8-4.9, 8.5, 8.8, chapters 1, 2, 5-7 and 10-20, and Appendices A, C and D could not be followed.
Below, "UBD" means the item is undefined anywhere I could read. "Deferred" means it is defined in an undrafted chapter. Deferred items are listed once in the shared ledger and not repeated per section.

## Shared ledger: steps I recomputed (Python/by hand)

Reproduced (my value in brackets):
- E.1: N_PW at 60 Ry [2121]; m_max [17.9]; Omega in bohr^3 [270.3]; LDA/PBE lattice-constant percent errors from Table E-functionals [Si -0.24/+0.92, Ge -0.30/+2.11, GaAs -0.59/+1.92]; hybrid cost factor [2048]; Sommerfeld E, F_sm, S_sm (eq E.1-sommerfeld); mixing recursion (eq E.1-mixing) and the bound beta < 2(2pi/k_TF L)^2; FD truncation h^2 eps''''/12 and noise 4 delta/h^2; SOC cost x8; Ge cutoff ratio [1.54]; 49% gap error, 0.85% expansion.
- E.2: 1s cutoff [1764 Ry, 3.4e5 PW, x159]; q_opt^2 [26, 12, 40 Ry]; 1/r_c [1.55, 1.05 keV]; q_opt [19.0, 13.0 keV]; 2k_cut at 60 Ry [57.8 keV]; Griffin 2 keV -> 45 keV; double commutator eq E.2-dc and kinetic term q^2/2m_e; Hamann B_0 [1.34%].
- E.3: scissor [0.568/0.613 eV]; SOC VBM mean and Delta_SO/3 [14.7 meV, 97 meV]; omega_p [16.6 eV]; G-vector counts at 10/15 Ry [144, 265]; velocity rescaling eq E.3-vrescale and its optical-limit invariance.
- E.4: LO-TO algebra eq E.4-LOTO (the bracket squares to 1/mu_red); Berry phase equals Wannier centres; KK sign; Q_c [0.1424 /A]; Delta B at 300 K [3.56e-4 A^2] and at T=0 [1.94e-5 A^2]; c Q_c [65 K]; storage [9.6 MB]; 35 Ry -> 22 keV and |G_111| [3.95 keV]; 29 q-points x 6 + 3 [177].
- E.5: 64,000^2 pairs; 270 TB; 4 GB; 3 GB; 1.9e8 and 8.8e5 multiply-adds; 3e16 flops; /48; window fractions [5.28e-3, 1.62e-2] and points [338, 1039]; 120^3 counts [1.8e3, 5.4e3, 2e7 pairs]; 1.3e5 multiply-adds per pair; scalings delta^3 and N_f^6.
- E.6: 70 bands -> k = 4.70 /A, 84 eV; k_cut at 500 eV [22.6 keV]; scissor first moment; spurious factor [(omega-Delta)/omega]^2; Wannier-Mott mu_x [0.106] and a_x [6.0 nm]; |b_i| [2.00 /A]; BSE dimension [1.6e4]; f-sum [433 eV^2]; q_r resolution [0.49 keV].
- E.7: N_FFT/N_pw = 48/pi; 70 Ry -> 31.2 keV, 15.8 /A, N_pw [2672]; storage [2.42 GB]; zone volume [47.6 keV^3]; N_G [2376]; vertex count [5.0e11]; flops [6.4e14, ~1.8 h at 1e11/s]; core kinematics from the quoted depths [33.4 MeV, 44.2 keV; Ge 8.2 MeV, 10.8 keV]; scissor factor [1.288, |v|^2 +66%]; (Z alpha)^2 [1.0%, 5.5%, 15.5%]; f-sum eq E.7-fsum including the q.v_g term.
- E.8: Fan term normalisation; classical/quantum ratio 2T/omega [1.7e-4 at 10 meV]; 64.3 - 56.2 = 8.1 meV; 35 + 22 = 57 meV; omega/T at 1 K [116].
- E.9: Heisenberg energies eq E.9-map and inversion eq E.9-J12; conversion J -> -J/2 [17.3, 19.0 meV]; spiral energy eq E.9-spiral; Matsubara counts [748, 7480]; Allen-Dynes T_c [1.225 K]; d ln T_c/d mu* [-23.1]; Delta_BCS [0.179 meV].
- E.10: E_corr for n = 2, 3, 4 [0.161, 0.107, 0.080 eV]; Born limit of eq E.10-ohm [4K_b].
- E.11: a_U [0.128 A]; V_ZBL at 1.0 and 1.5 A [50.9, 9.6 eV]; r_min table, solved numerically [1.487, 1.201, 1.005, 0.828, 0.489, 0.179 A]; v at 100 eV and 1 keV [26.2 km/s, 0.83 A/fs]; time steps [0.19, 0.06 fs]; equipartition [0.53 eV]; binomial error [0.016]; cost [410 s, 2.3e3 core-h, 4.6e7 core-h]; Boltzmann factor at 10 mK [e^-1.16e5].
- E.12: B_iso [2.35e-42 s^3]; every entry of Table E.12-rates; A/B crossover [32.8 THz]; lifetimes [0.135 ns, 55 ns, >13.5 us]; incoherence ratios [4e-7 at 1 THz, 1.3e-3 at 15 THz]; lambda/mfp [4.1e5]; 2.4e6 phonons.
- E.13: band counts at 20/50/100 eV [8.1, 32.1, 90.8]; hbar Gamma [0.066 eV]; Alig-Bloom probabilities at 3, 5, 8, 10 eV [0.053, 0.363, 0.773, 0.882]; the linear fits [3.709 eV, 0.1153]; N_casc [7.1e3]; N_G [257, 727]; storage [6.3 GB]; N_k^2 N_b^2 [2.7e9]; 1333 pairs and ~5.5e4 phonon events.

Not reproduced or inconsistent (detail under the persona sections):
- N1 (E.5, cost of a phonon-assisted recoil run): 1e16 operations at 1e13 /s is 1.0e3 s, about 17 minutes, not "hours". The few-core figure (2.3 days) is right.
- N2 (E.9, frozen-magnon relation): Holstein-Primakoff on eq E.9-heis gives omega(Q) = |S|[J(Q) - J(0)]. Check: for an NN chain with H = -J sum S_i.S_{i+1}, the standard result is omega = 2JS(1 - cos ka) = S[J(0) - J(Q)]. The text has 2|S|[...] and hence omega = 4 Delta E/(|S| sin^2 theta). Both are a factor 2 too large. The correct relation is omega = 2 Delta E/(|S| sin^2 theta), which matches Halilov's 4 Delta E/(M sin^2 theta) with M = 2|S|.
- N3 (E.9, Allen-Dynes sensitivity): the exact values are T_c(0.14) = 0.738 K and T_c(0.10) = 1.872 K, ratios 0.60 and 1.53. The quoted "0.63 or 1.59" are the linearised e^{-/+0.46}, yet they sit in the same sentence as the exact T_c values.
- N4 (E.4, frozen-phonon versus DFPT scaling): a supercell of R^3 primitive cells holds N_at R^3 atoms, so the frozen-phonon cost is about 3 N_at^4 R^9, not 3 N_at R^9. As printed, the N_at powers of the two routes cannot be compared.
- N5 (E.7, binning): "0.02 q_0" uses q_0, which is never defined. With q_0 = alpha m_e, 30 keV needs about 402 bins, not the 900 in "500 x 900".
- N6 (E.8, worked example): the +9 meV zero-point lattice expansion is quoted but not applied. If experiment (-62/-64 meV) includes it, the electron-phonon part is about -71/-73 meV, and AHC-NA/ZG (-56/-57) underestimate by about 20%, not "about ten percent". The section's own Pitfalls paragraph says both terms must be included.
- N7 (E.13): A_AB is "fitted to hot-electron injection data between 2 and 5 eV". Two paragraphs later "the pair energy agrees to 1% because A_AB was chosen to make it agree". These cannot both be true as written.
- N8 (E.1 versus E.7): E.1's FFT estimate (at least 37, rounded to 40^3 = 6.4e4 points at 60 Ry) and E.7's N_FFT = 15 N_pw (about 3.2e4 at 60 Ry) differ by a factor 2, because E.7 assumes a cube while the fcc box is a parallelepiped. Also, |m_i| <= 17.9 needs 35 points, not 37.

Deferred (undrafted chapters). The truncation label T, T_0, n_B, n_T, n_A, n_g, rung X, lattice label K, xi_D (E.7), eta_anh (E.8), delta_off (E.4), F_DM, v_min, theta_ii, the seed class Lambda, the "off-shell parameter" (E.13), C_kk'(t), B_Qnu, the Hecht relation, the Lyddane-Sachs-Teller relation, and the Kohn-Sham, PAW and Wannier derivations of sec 3.4-3.6.

## Persona (b): particle physicist, QFT yes, solid state no

Overall. This is the page I wanted: every method comes with its inputs, the parameters to converge, the cost, the checks and a silicon number. The units (hbar = 1, Heaviside-Lorentz, e^2 = 4 pi alpha) are natural to me. I saw no condescension. In places the text talks to me in code-user jargon (Miller indices, Voigt rows) without a gloss, which is the opposite fault and a mild one.
The one structural obstacle is the label T, with its components n_B, n_T, n_A, n_g and X. It is invoked in every section and defined only in sec 8.5, which I do not have. From context, n_T means three different things: "static lattice, no phonons" in E.1, "DFPT phonon at n_T = 0" in E.4 and "phonon-assisted absorption is n_T = 1" in E.5. One sentence per use saying what the number means, or a half-page glossary at the head of E, would fix it.

E.1 DFT in practice.
- Lost: "error ... is the set of real-space Fourier components of the integrand at the size of the fictitious block" is hard to parse; "components at the superlattice vectors R of the n1 x n2 x n3 block" would be clearer. Two "measured" Si lattice constants appear (5.416 A in the table, 5.431 A in the worked example) with only the caption to bridge them. A doubled phrase: "a set of 40 semiconductors ... over some forty semiconductors".
- Not reproduced: none. UBD: "Pulay stress" is named before it is explained (the next sentence explains it; fine). The occupation function f-tilde is introduced well.
- Pace: right. The cost paragraph is a useful scaling lesson.
- Judge a published DFT number: yes. I would now ask for the functional, the lattice constant, E_cut, the k-grid per quantity, the occupations and the SOC treatment.

E.2 Pseudopotentials.
- Lost: in eq E.2-rhoPAW the kappa sum "runs over every atom of the crystal; ... the atoms of all cells contribute equally". Is kappa a cell index or a crystal index? State the normalisation. The f-sum test ("0.81 with 16 bands ...") does not say which n is used, or whether the result is summed over the four valence bands.
- Not reproduced: none. UBD: "logarithmic derivative" and "ghost" are defined in place (good). "Gaunt coefficients" is not glossed.
- Pace: the PAW algebra is slightly fast for me ("completeness ... lets the smooth part be replaced"). One displayed line of the cross-term cancellation would help.
- Judge: yes for the form factor at large q. This is the section I would cite to a colleague.

E.3 Quasiparticle corrections.
- Lost: Table E-gw gives GaAs LDA = 0.67 eV, while Table E-functionals gives 0.43 eV, with no comment. For Ge the table lacks a measured Gamma gap, so "within 0.04 eV of experiment" for Gamma cannot be checked.
- Not reproduced: none. UBD: "COHSEX", "head and wings" and "Coulomb-hole / screened-exchange" are named but only half explained.
- Pace: the plasmon-pole paragraph is dense but complete.
- Judge a published GW gap: mostly. I know to ask about the starting point, the band/cutoff convergence pair, the PPM versus full frequency, SOC, ZPR and the core treatment.

E.4 DFPT.
- Lost: "valid to relative order omega/delta_off": delta_off is undefined here. In the convergence paragraph, "frequencies depend on the square root of second derivatives and small errors ... show up as frequency noise" reads backwards, since a square root halves relative errors. The real point (near-zero acoustic modes, or imaginary frequencies from noise) should be stated.
- Not reproduced: N4.
- Pace: the Delta B estimate at Gamma is excellent. The finite-frequency Sternheimer paragraph is fast.
- Judge: yes for phonons, Z* and eps_inf. The LO-TO check against measured frequencies is a concrete tool.

E.5 Wannier.
- Lost: no gloss on the spread functional Omega_W, which is deferred to sec 3.6. The interpolated density-vertex route ("for each q the real-space matrix must be built anew") would be clearer with one sentence on what is periodic in R and what is not.
- Not reproduced: N1. Everything else in Worked Example E-counts reproduces.
- Pace: the counting example is the best in the appendix.
- Judge: yes. I would check the gauge consistency of g, rho and v, the off-grid tests, the dipole and quadrupole subtraction, and the window.

E.6 Dielectric response.
- Lost: the X-rung assignments ("RPA for the diagonal of eps_GG'") presuppose sec 4.6.
- Not reproduced: none. UBD: "Tamm-Dancoff", "Lanczos-Haydock" and "resolution of the identity" are named and not explained (acceptable as pointers).
- Pace: good. The 70-band free-electron count is the right level for me.
- Judge a published loss function: yes. Check the f-sum moment, G_q rather than G = 0, local fields, the band count and the scissor treatment.

E.7 Form factors.
- Lost: N5 (q_0). The "heavy mediator" and "light mediator" weights depend on F_DM and eq A.8-rateiso, which are deferred.
- Not reproduced: N5.
- Pace: right. The worked example is clean and reproducible.
- Judge: yes, and this is the most directly useful section for my field.

E.8 Finite temperature.
- Lost: the hierarchy paragraph is opaque without sec 8.5 (n_A, n_T). The SCHA "auxiliary versus physical" warning is clear.
- Not reproduced: N6.
- Pace: fine.
- Judge a published ZPR: mostly. I now know about adiabatic versus non-adiabatic, the delta -> 0 extrapolation, residual Z* and the double counting with a measured gap.

E.9 Magnetic and superconducting parameters.
- Lost: none beyond conventions, which the text handles explicitly and well.
- Not reproduced: N2, N3.
- Pace: fine.
- Judge: yes for T_c and Delta (mu* sensitivity). For J, I would compare conventions, and the factor 2 in N2 would mislead me.

E.10 Defects.
- Lost: none. UBD: "Delta SCF" and "inherent structure" (E.11) are explained in place.
- Not reproduced: none.
- Pace: good.
- Judge: yes. The E_corr example makes the charged-cell problem concrete.

E.11 MD and learned potentials.
- Lost: none.
- Not reproduced: none. The r_min table reproduces to 0.01 A.
- Pace: good.
- Judge a published E_d or E_st: yes. Check the potential, the splice, the quench, the number of directions and recombination.

E.12 Transport Monte Carlo.
- Lost: none. UBD: "Herring-Vogt" is explained; "Hecht" and "Ramo" are deferred or given.
- Not reproduced: none.
- Pace: good.
- Judge: yes for collection kernels, including the warning that down-sampling breaks the variance.

E.13 Hot-carrier cascades.
- Lost: N7. "Omitting exchange alone reduces the rate by at most 0.75" does not say whether 0.75 is a factor or a fraction.
- Not reproduced: N7 (logic, not arithmetic).
- Pace: good.
- Judge a published epsilon_eh/F: yes. The statistics paragraph tells me how many cascades a claimed F needs.

Verdict (b): MINOR GAPS. Nothing blocks the following material. The deferred T label is the main friction, and N1 to N8 are local.

## Persona (c): condensed-matter theorist (DFT and MBPT)

Overall. The physics is correct almost throughout, the numbers are traceable, and the "converge on the quantity, not the energy" theme is exactly right. Tone: no condescension. The explicit DFT basics in E.1 (Sommerfeld smearing, Kerker) are pitched at a level I skimmed but did not resent. The errors below are mostly prefactors and internal consistency. The main topic where practice looks dated is GW.

E.1.
- "Apart from the highest occupied level, [KS eigenvalues] have no exact physical meaning": fine. It is worth adding that the KS gap differs from the fundamental gap by the derivative discontinuity, which is the reason the error is systematic.
- "the change between successive cutoffs is a reliable error estimate": the Ge column contradicts this. The 50 -> 60 Ry change is 1.3 meV, while the error at 60 Ry is 3.1 meV. Soften the claim.
- Cold smearing (eq E.1-cold) is correctly reproduced. The claim of no sigma^2 term in forces and stresses is a fair reading of Marzari-Vanderbilt.
- The SCF argument uses eps = 1 - v R^0 on densities. Strictly, the density-space operator is 1 - R^0 v, with the same spectrum. Fine.
- N8.

E.2.
- "core bound by more than 100 eV" (Si 2p) and E.7's "2p ... about 116 eV below the VBM": the measured Si L_2,3 edge is about 99-100 eV. If 116 eV is a computed (KS or atomic) level, say so, because it drives the 33 MeV and 44 keV thresholds in E.7. With 99 eV these become about 28 MeV and 38 keV.
- The ghost discussion, the Delta gauge and the nonlocal f-sum (eq E.2-fsumNL) are correct and well placed.
- Statement of note: the Ismail-Beigi result that the density vertex needs no nonlocal correction is correct and often misunderstood. Good to have it explicit.

E.3.
- GW practice. The section rests on Hybertsen-Louie (1986), Godby (1988) and Aryasetiawan-Gunnarsson (1998). Two points should be checked against the current literature.
  - Si G0W0@LDA "1.24-1.29 eV" comes from older, less converged calculations. Modern, carefully converged G0W0@LDA/PBE values for Si cluster nearer 1.1-1.2 eV.
  - Current practice includes band/cutoff extrapolation or static-remainder schemes (Bruneval-Gonze), full-frequency contour deformation, and QSGW with ladder vertices in W (QSGW-hat), which largely removes the QSGW overestimate attributed to missing e-h attraction in W.
  One or two sentences, with a citation, would bring this up to date.
- The GaAs LDA gap discrepancy between the two tables (0.67 versus 0.43 eV) needs a note (lattice constant, Ga 3d, SOC).
- The ZPR "0.3 eV in diamond, below 0.1 eV in heavier" is attributed to van Schilfgaarde 2006, an odd source for ZPR. Check it.
- The velocity rescaling and the scissor f-sum are correct. The point that a scissor-RPA eps_inf "moves toward the measurement" may overshoot (IP + scissor without LF tends to undershoot 11.7). "Closer" is not guaranteed.

E.4.
- N4.
- "phonons are computed at the theoretical equilibrium ... so that the forces vanish": in diamond and zincblende the forces vanish by symmetry at any a. What is nonzero away from equilibrium is the stress. The reason to use the theoretical a is consistency of the second derivative, not forces.
- Frequency-noise argument (see b).
- Born-charge symmetry argument, the dipole subtraction, ASR caveats, and the warning against zeroing g at Q -> 0: all correct and nicely done.

E.5.
- N1.
- Dynamical quadrupoles in Si, with the 10% mobility effect from Brunin: correct and current.
- "eight sp^3 hybrids ... lowest conduction bands" plus disentanglement: standard. The four checks are sound.

E.6.
- Reining's long-range kernel with alpha = 0.2 is fine. Note that alpha is material dependent (scaling roughly as 1/eps_inf), and mention newer kernels (bootstrap, JGM) at least by name.
- The BSE cost and the Albrecht lessons are correct. The Wannier-Mott numbers reproduce. Si E_b(exp) is 14.7 meV against the "~10 meV" used; harmless here.

E.7.
- N5, plus the 2p depth (see E.2).
- The f-sum eq E.7-fsum is cleaner than E.2's symmetric version, because it keeps q.v_g and says why it cancels. Consider cross-referencing the two so a reader does not think they disagree.
- Griffin: E.2 says the reconstruction matters "above energy deposits of about 15 eV", while E.7 says "even for thresholds as low as about 10 eV". Reconcile.

E.8.
- N6. Also "the residual underestimate is attributed to overscreening by the small KS gap" is plausible, but after N6 the size of the residual changes.
- QHA, SCHA (auxiliary versus physical frequencies), TDEP's classical-sampling warning and the ZG brackets: correct and current.

E.9.
- N2 (a factor-2 error in a formula that people will use) and N3.
- DFT+U projector dependence, the J conventions table and the LKAG-versus-mapping discussion are good.
- Calling Eliashberg "n_g = 2 ... summed to all orders in Nambu space" is fine.

E.10.
- Makov-Payne is presented as "the correction". A sentence should say that the bare point-charge term often overcorrects (the Lany-Zunger ~2/3 scaling), which is why FNV and Kumagai-Oba are preferred. The text gets there, but the worked example applies the full Madelung term as if it were the correction.
- Inconsistency with E.11: "trajectory followed for about 10 ps" here versus 20 ps runs for the same Sassi study in E.11.

E.11. Correct. The ZBL table reproduces. The quench protocol and the equipartition estimate are a good catch for stored-energy work. The GAP-18 cost of 100 ms/atom/core is plausible for that model. Saying that ACE or MACE are one to two orders cheaper would justify the "faster descriptor families" remark quantitatively.

E.12. Correct (Tamura rates reproduce exactly). Minor: G4CMP's Luke emission is LA-only, while carriers above c_TA also emit TA. Worth one clause, since the text says "faster than the longitudinal sound speed".

E.13.
- N7, and the "0.75" ambiguity.
- The statement that eq E.13-imsigma already contains plasmon emission, so no separate channel should be added, is correct and important.
- In the "Double counting" pitfall the plasmon and phonon clauses are run together; split them.

Verdict (c): MINOR GAPS. N2 is the only outright formula error. N6 and N7 are internal contradictions that a referee would flag. The GW section needs a post-2010 update. None of these blocks the following material.

## Can I now judge a published calculation? (summary)
| Section | (b) | (c) |
|---|---|---|
| E.1 DFT | yes | yes |
| E.2 PP/PAW, large-q vertex | yes | yes |
| E.3 GW | mostly (core and GaAs table) | yes, with the modern-practice caveat |
| E.4 DFPT | yes | yes |
| E.5 Wannier/EPW | yes | yes |
| E.6 response/BSE | yes | yes |
| E.7 form factors | yes | yes (check 2p depth) |
| E.8 ZPR/anharmonic | mostly | yes (fix N6) |
| E.9 J, Eliashberg | T_c yes; J misled by N2 | yes (fix N2) |
| E.10 defects | yes | yes |
| E.11 MD/MLIP | yes | yes |
| E.12 transport | yes | yes |
| E.13 cascades | yes | yes (fix N7) |

## Priority fixes
1. N2: frozen-magnon/LSWT prefactor in E.9.
2. N6: apply the +9 meV in Worked Example E-zpr, or explain why not.
3. N7: say what A_AB was fitted to.
4. N1, N3, N4, N5, N8: prefactor and count slips.
5. The GaAs gap discrepancy between the tables; the Si 2p depth (116 eV versus about 99 eV measured); E.2/E.7 Griffin thresholds (15 versus 10 eV); E.10/E.11 run length (10 versus 20 ps).
6. A short glossary of the label T (n_B, n_T, n_A, n_g, X, K) at the head of Appendix E, consistent across sections.
7. GW modern-practice sentences in E.3; Makov-Payne overcorrection caveat in E.10.
