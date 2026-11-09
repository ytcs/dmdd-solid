# Ch12 post-acceptance check: off-diagonal G != G' estimate and the struck-atom phase

Isolated re-derivation, 2026-11-03. Scope: figscripts/ch12/offdiag12.py (+ .log, npz), tex/ch12 s12-1, s12-3,
s12-4, s12-5, s12-6 (tab:12-nuisances, Summary), appD/D-33, sources/12.3/2011.13352 (Liang et al.).
Reruns (scratchpad, no npz written, no QE): NK=4 GM=11 ECUT=21 ETA=0.15, once as shipped and once with the EPM
origin moved from the bond centre onto the atom at +tau (U_GG' -> U_GG' e^{i(G-G').tau}). Verdict: no WRONG item;
two GAPs (wording/caveats), not applied to the tex. No rebuild needed.

## (1) Off-diagonal estimate "about 1.2 to 1.4"

| item | verdict | note |
|---|---|---|
| chi0_GG' (Adler-Wiser, res + antires, retarded signs, spin 2, rho_G = <c k+q| e^{i(q+G)r} |v k>, umklapp GU when k+q leaves the mesh) | CHECKED | R0_ab ~ rho_a^* rho_b, i.e. <0|n(p_a)^+|j><j|n(p_b)|0>: same index order as S^ee_GG' of eq:12.1-Skk. |
| v(q+G) and inversion | CHECKED | eps~ = 1 - v^1/2 R0 v^1/2 with v = 4pi/|q+G|^2 (a.u.); full NG x NG inverse per w; Sp = -(E - E^+)/2i is the anti-Hermitian part defined after eq:12.3-FL. Diagonal of eps~ = diagonal of eps, so (iii) Im[-1/eps_GG] is the scalar form of lim:12.3a. |
| Weight W_GG' = Z(p)Z(p') p^.p'^ e^{i(G-G').X} e^{-<u_x^2>|G-G'|^2/2} | CHECKED | boost (q.p)(q.p') -> q^2 p.p'/3; vertex Z Z' e^4/(p^2 p'^2); S^ee ~ |p||p'| Sp: product Z Z' cos(p,p') Sp, as coded. Diagonal of (i) is exactly (ii). |
| Three variants consistent with eq:12.3-LMig / -FL / -rate | CHECKED | same Q_Mig = L_Mig/(3w^4), same rate_free kernel, same mesh and w grid; only the G-sum differs, so ratios are clean. |
| Umklapp channel of the nuclear kick | CHECKED | soft limit: int dw_l S^ad between n_k(Q-G) and n_k(Q-G') = <e^{i(G-G').X}> (one site, position components commute), = phase x exp(-<u_x^2>|G-G'|^2/2), independent of Q. DW changes the ratio by ~1 % (cutoff |dG| ~ 17 (2pi/a) >> GM). Distinct-site (Bragg) terms are dropped in (i) and (ii) alike, as in the book's impulse treatment. |
| Struck-atom phase and its sign | CHECKED | from eq:A.3-space (O(q) = int e^{+iqr}) and eq:12.1-force: a_G ~ e^{-iG.tau}, a_G^* a_G' = e^{+i(G-G').tau}, as coded (sympy, phase_check below). +tau and -tau agree per q to 1e-15 (inversion + time reversal), so the 2-atom average is exact. |
| Gauge test (new) | CHECKED | origin on atom, no phase: 1.5508 = bond centre with phase: 1.5508 (log 1.5508); (ii), (iii), P(ii) identical in both frames; rate at 100 MeV 1.5555 vs 1.5555. Bond-centre no-phase (2.0645) is the wrong number, as the log says. |
| Reproducibility | CHECKED | shipped run reproduces the log NK=4 GM=11 line to all printed digits (1.5508 / 1.5666 / 2.0645 / 1.2162). |
| "flat in m_chi" | CHECKED | NK=8 GM=19: 1.409 (10 MeV) to 1.378 (1 GeV), 3 %. |
| Printed band "about 1.2 to 1.4", "not converged in G" | GAP | The band is [extrapolated central, raw], not a bracket. 1.4 = raw NK=8 GM=19 (1.378 total, 1.38-1.41 in rate); 1.2 = the log's hand extrapolation (NK->inf at GM=19: 1.31, minus 0.06 for GM 19->27 and ~0.05 for 27->35). The G drift at NK=4 is -0.056 (19->27) then -0.078 (27->35): not decelerating, and the log says the trend beyond GM=35 is not established. Same drift with ZFIX=4 (1.572 -> 1.490), so it is not a Z_ion artefact. Hence the direction of non-convergence is downward and the lower end is not a bound; "raises the rate" holds at every computed point (min 1.465) but is not established in the limit. Suggested wording (s12-3 l.88 and the tab:12-nuisances row; optionally s12-1 l.124): after "not converged in the sum over reciprocal-lattice vectors" add "; the lower end is an extrapolation, and larger reciprocal-lattice sets still lower it". Reported, not applied (6 places, judgement call for the editor). |
| Model fidelity | GAP | model (iii)/(ii) = 1.19-1.27 against 1.35 of lim:12.3a: about 2/3 of the diagonal local-field effect, so the off-diagonal size has no bound from the model in either direction; P(ii)/KKL 1.13 (NK=10) to 1.67 (NK=4, and ETA=0.3): only ratios are usable. The tex calls it "a model" and "open" everywhere it appears, which is adequate. |
| Constant Z vs Z_ion(p) | note | eq:12.3-FL is printed for constant Z_ion; the band comes from Z_ion(p)Z_ion(p') runs. ZFIX=4 runs give the same ratios within 0.03, so harmless. |

## (2) Phase e^{i(G-G').tau_kappa} in eq:12.3-FL and Liang et al. Eqs. (12)-(13)

| item | verdict | note |
|---|---|---|
| Phase is required and transforms correctly | CHECKED | origin shift r = r' + d: n'(p) = e^{-ip.d} n(p), so S'_GG' = e^{i(G-G').d} S_GG', eps~' = D eps~ D^+ (D = diag e^{iG.d}); inverse and anti-Hermitian part transform alike. Hence sum c_GG' Sp'_GG' (origin on atom, no phase) = sum c_GG' e^{i(G-G').tau} Sp_GG' (any origin); diagonal origin-free. Numeric check, random absorbing 7x7 eps~: difference 9e-16 (no-phase off-atom differs by 26 %). Confirmed on the real model by the gauge test above. |
| Liang Eqs. (12)-(13) = eq:12.3-FL with the origin on the struck atom | CHECKED | Eq. (12) is FL with the phase = 1; Eq. (13) uses the same symmetrized eps~ (1/(|k+G||k+G'|)). Their derivation (App. A.2.3, Eq. (39) second line) drops k from the nuclear momentum balance, i.e. evaluates the ion's e^{-ik.X} at X = 0; no origin is stated, as the book says. With an exact plane-wave nucleus the G != G' terms would connect orthogonal final states and vanish, so the off-diagonal terms exist only for a nucleus localized at a site, which is where the phase lives. |
| Sign convention | note | the sign of the phase is tied to the index order of R0_GG' (which slot carries n(k+G)^+); eq:12.3-FL does not state it, and a transposed convention flips tau -> -tau. Moot for Si (inversion about the bond centre; Liang's eps~ is symmetric there), but it matters for GaAs. Optional: state "R0_GG' with n(k+G)^+ on the left, as S^ee of eq:12.1-Skk" after eq:12.3-FL. |

Scripts (scratchpad, not part of the book): /tmp/claude-0/-home-user/364f612b-be7d-56fd-924b-36b7d0d3bbab/scratchpad/pac/
run_gauge.py, phase_check.py, bc.log (shipped), atom.log (origin on atom).
