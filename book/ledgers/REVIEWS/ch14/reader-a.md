# Chapter 14: mock reader (a), first-year PhD student
Read from the .tex sources (ch14/s14-1 to s14-6, appD/D-38), linearly, with Ch. 7.1, 8.1-8.2, 4.2, A.8 and C.19 reread for the equations they cite. I checked derivations by hand and numerics in Python (scratchpad scripts: NiO grid sums, the one-magnon rate integral with an SHM halo of v0 = 238, vE = 250.5, vesc = 544 km/s, Mn12 levels, YIG hybrid, F_phi line statistics, Weiss mean field).

**Verdict: MINOR GAPS.** No step blocks the material that follows. Every headline number I tried came out the same (list at the end). The gaps are presentation problems: a few cross-references and terms, one overstated "bound", and a few numbers that the text gives me no way to reproduce.

## 14.1 Magnon scattering (with D.38)
**Lost points**
- Para. 1 of "Zero-point spin reduction" / "The three weights violate the sum rule": the text says $\Delta S/|S|$ is a *lower* estimate of the one-magnon error, and Tab. 14-nuisances labels it "bound", and the summary says "at least". But D.38 admits that "the change of the ground state at the same order, and the shift of the magnon energies ... are not part of it". The argument also holds $\langle S^z\rangle$ and $W_\parallel$ at their linear-spin-wave values, and those values carry next-order corrections too. So as derived, "at least" is not rigorous. It should be called an estimate of the leading correction, or the text should say why the omitted ground-state change cannot reduce it. I was unsure what to believe until I read D.38.
- Para. 4 of "One-magnon response": "twice the distance from $\Gamma$ to the ordering wavevector" is fine. But "carried automatically if $A_k$, $B_k$ are evaluated at the full momentum transfer" only became clear after D.38 showed $B_{q} = \epsilon_G B_{q_r}$. One sentence in the main text ("$J_{AB}$ changes sign under a sublattice reciprocal vector that maps A onto B") would have saved me the detour.

**Steps I could not reproduce**: none that I tried.
- Checked: eq. 14.1-Safm from the D.38 amplitudes (both branches, $\Vol = 2N_s\Omega$); D.38-weight ($\cosh 2\theta - \epsilon\sinh 2\theta$); the near-$\Gamma$/near-$Q$ forms; $2|S|J_{AB}(0) = 211.7$ meV, $w = 0.024$ and 42; $\langle|S_\chi\cdot S_e|^2\rangle = 3/16$; eq. 14.1-sigma; the prefactor $2/3$ of eq. 14.1-rate; eq. 14.1-inc via $\int du\,u\,\eta = \langle v\rangle/2$; eq. 14.1-mmin and 7.2 keV; Wick's theorem for $\langle n^2\rangle$; the HP half-sum giving D.38-sumrule.
- Numbers: $\Delta S = 0.07843$ on a $100^3$ grid (0.07827 with $J_1 = 0$); zone average of $w$ = $1 + 2\Delta S$ exactly; $W_\perp$, $W_\parallel$, the ratio 0.0731, 1.066 and 0.995; the limit box values for $|S| = 1/2$ and $5/2$; $\Omega$, $\rho_T$; $|F|^2 = 0.84$ and 0.49.
- Full rate integral: 10.3, 285, 434, 2.60e3, 3.19e3 and 1.52e3 events/kg/yr at 0.01, 0.03, 0.1, 1, 3 and 10 MeV. Ratio to eq. 14.1-inc 0.955 and 0.987. Edges near 30 and 85 keV for the 20 and 50 meV thresholds. Anisotropy factors 29.2, 1.35 and 1.03. $\langle v\rangle = 354$ km/s.
- Small: $K = 0.097$ meV gives a gap of 4.53 meV, not 4.54 (rounding of $K$).

**Used before defined**: none blocking. "Energy-mapping, spin-spiral or Green's-function routes" are only names with a pointer (E.9). Acceptable.

**Too slow / too fast**
- Too fast: the sum-rule paragraph packs three claims (overcount, the HP fix, weight moved into the two-magnon continuum) into one paragraph. It reads fine only with D.38 open.
- Last paragraph: "fixed by its anisotropy" for $m_\chi < 50$ keV is stated after one easy-axis model. The caveat ("only imitates") comes two sentences later. Fine, but it could come first.

**Outcomes**
- Write the AFM one-magnon $S_{ab}$ at any $q$: yes. I rederived it.
- Evaluate $w$ near $\Gamma$/$Q$: yes.
- Assemble the $\mathcal{O}_4$ rate and its heavy-mass limit: yes. I reproduced the figure numbers.
- Compute $\Delta S$ and the sum-rule defect: yes.

## 14.2 Two-magnon continua and magnon-phonon modes
**Lost points**
- First sentence: the 7% longitudinal weight is attributed to "(\cref{sec:7.1})". Sec. 7.1 only says that $S^z$ creates pairs. The 7% (0.073) comes from Sec. 14.1 / we:14-nio. I went back to 7.1 looking for it.
- Sec. 14.2-nuis: "$\delta_k'$", "$\vartheta_k$" and "\cref{eq:8.8-open}" are used with no reminder of what they mean. I had to reopen 8.8 to parse "Only the small parameter is known, so $\delta_k'$ is an estimate of that size".
- Para. after eq. 14.2-amp: "$\mathcal{A}^{2m} \simeq q\cdot\nabla\theta$". My expansion gives $\sinh(\theta_{k-q} - \theta_k) \simeq -q\cdot\nabla\theta$. The sign is irrelevant for the weight, but it should be written correctly or as $|\cdot|$.

**Steps I could not reproduce**: none. Checked:
- The A and B terms of $S^z(q)|0\rangle$, the relabelling, eq. 14.2-S2m normalization, and the zone averages $W_\parallel$, $W_\perp$.
- Numerics: $w_\perp \simeq 0.289\,qa$; $w_\parallel \simeq 0.0147\,(qa)^2$; at $(\frac14,\frac14,\frac14)$, $w_\perp = 1.000$, $w_\parallel = 0.0816$, $\omega = 105.84$ meV; $w_\parallel \to 0.25$ at $Q$; ratio peak 0.082 near 1.3-1.5 keV and < 0.05 below 0.5 keV; continuum top 236.3 meV at both $q$; eq. 14.2-mratio 5.03, 1.43 keV and 0.285 keV.
- The $-\mathrm{Im}\,G$ form of S2m; the single-ion pair energies $4D(S-1)$ vs $2D(2S-1)$.
- The magnetoelastic vertex eq. 14.2-gmp, which I rederived from $(2/S)^{1/2}B_{me}[\dots]$ and the phonon field: $g = B_{me}k/\sqrt{2SM\omega_p}$.
- YIG worked example: $|S| = 14.23$, $D_{sw}$, $M_{cell}$, $B_{me}$, $k_\times = 4.63\times10^{-3}$ nm$^{-1}$, $g = 0.176$ µeV, 3.0%, 85 MHz, 0.146 and 0.010 contents, 3.1% window, upper root 0.418 nm$^{-1}$ / 1.06 meV / 0.32%, phonon content $3\times10^{-12}$.

**Used before defined**: "Colpa's diagonalization" (given only a one-clause gloss, which suffices).

**Too slow / too fast**
- Too fast: the ladder sum rule paragraph is fine.
- The bound-pair paragraph (Wortis, Silberglitt) is a literature survey that I cannot check. It was acceptable as context.

**Outcomes**
- Derive the two-magnon amplitude and response: yes.
- Find the kinematic edges and the mass gain: yes.
- Explain why final-state interactions conserve the integrated weight: yes.
- Compute a hybridization gap: yes.
- Size the nuisances: yes, given 8.8.

## 14.3 Absorption into magnons
**Lost points**
- Para. "\Cref{eq:14.3-rate} has a delta function": "the Kittel mode of YIG" is used before Sec. 14.3-kittel defines it.
- First paragraph: the Compton wavelength uses $2\pi/m$ (12 cm), while the de Broglie wavelength uses the reduced $1/mv$ (24 m). The mixed conventions made me recompute both.

**Steps I could not reproduce**
- The eight-site XXZ cluster results (0.85, 0.91, 5-23%): not attempted. This needs exact diagonalization, and the text gives the model but no procedure.
- $\omega_M/\omega_E = 1.3\times10^{-3}$ for MnF$_2$: the sublattice magnetization is not given.
- Everything else checked:
  - $\lambda_S$ table (all five rows); the first-order $\langle L\rangle$ and $g$ shift; the $1.44$.
  - Larmor line weight via commutator plus detailed balance; eq. 14.3-rate; eq. 14.3-peak (the mass drops out); 0.47 modulation; $t_{coh} = 0.10$ ms.
  - Kittel: $H_u$ from Zeeman plus demagnetization; elliptic weights; film 3.16 µeV / 27.3 mT / 1.74.
  - YIG: $\Omega$, 2951.8 u, 0.246 T, 37.8 emu/g, $\omega_M = 28.5$ µeV, 86.4/82.0 mT, 9.49 µeV, thermal factor, 24 kHz, 6.6 µs, $\mathcal{R}_{peak} = 3.64$ s$^{-1}$kg$^{-1}$ = $1.15\times10^8$/yr, 35 per hour.
  - AFMR amplitude $(u_0 - v_0)$; eq. 14.3-afmrweight; MnF$_2$ values 5.447 / 0.0949 / 1.021 meV / 247 GHz / 0.0929 / 0.0933 / 0.74 / $7.2\times10^{-3}$ / 8.75 T / 0.01 meV.
  - Limit box gray $B_0 \ge 4.8\,\mu_0 M_s$.

**Too slow**: the Landé derivation is undergraduate material. It is short, so this is no harm.

**Outcomes**
- Show that the Larmor line is exact for isotropic exchange: yes.
- Use $\lambda_S$ correctly for $J$ multiplets vs quenched ions: yes.
- Compute the Kittel shift and reweighting for an ellipsoid: yes.
- Compute AFMR frequency and weight: yes.

## 14.4 Spin responses from neutron data
**Lost points**
- "$q_{1BZ} = 987$ eV": I could not get this from $a = 12.375$ Å for bcc YIG. The nearest zone face is at $\sqrt2\pi/a$ = 708 eV, the H point at $2\pi/a$ = 1002 eV, and the equal-volume sphere radius is 783 eV. The text should say what "edge of the first zone" means here (presumably Berlin et al.'s definition). The 186 keV that follows is consistent with 987 eV.

**Steps I could not reproduce**: none besides the above. Checked:
- Eq. 14.4-PT from C.19-cross; $(\gamma_n r_{cl})^2 = 0.2906$ b; Berlin's constant equals $r_{cl}^2/4\pi$.
- $F_g$ and $C_{sn}$; 0.83 and 1.19; Ni$^{2+}$ $\langle j_2\rangle/\langle j_0\rangle$ = 0.035 and 0.152; $C(q)/C(0)$ = 0.994 and 0.973; $g = 2.34$ gives 0.73; gray $g - 2 \le 0.094$.
- 15.0 keV and 20 eV; the phonon $(q/30\ \mathrm{keV})^2$.
- The $\mathfrak{D}$ tensors of $\mathcal{O}_{4,6,9,10}$; eq. 14.4-uniax; eq. 14.4-invert; every number in we:14-paramagnet (0.050, 0.112, 3.7%, 0.141, 0.32).

**Used before defined**: none. "Full polarimetry" is cited, which is acceptable.

**Too fast**: the point-group half of the no-go keyresult is brisk but correct. I would add one sentence on why $q$ and $q + G$, which can point in different directions, are not related either (they are different operators).

**Outcomes**
- Convert $S^{neu}$ to $\mathrm{Tr}[P_T S]$ with the orbital correction: yes.
- State which operators the data calibrate, bound or miss: yes.
- Perform the two-angle inversion with errors: yes.

## 14.5 Chiral and nonreciprocal targets
**Lost points**
- Para. after fig. 14-cd: "at 1 keV the quartz value of $g_{33}$ gives $q g_{33} = 0.034$". The sentence before speaks of energy $\omega$, so I first read 1 keV as an energy, which gives $q \ge 377$ keV and $q g \approx 13$. The 0.034 holds for $q$ = 1 keV, that is, an energy near 2.65 eV. It should say "at $q$ = 1 keV".
- Eq. 14.5-GL: $\chi$, $\alpha$, $\alpha_M$, $c$, $m_P$ and $\omega_a$ are never defined. $\theta_0$ is "times its photon coupling", while the coupling derived just above is $g_{aee}$, and the text does not reconcile the two. I cannot evaluate or check this equation.
- "The density rows of $\mathcal{O}_5$ and $\mathcal{O}_8$ meet the current rows through $S_{nj}$, whose enantiomer-odd part is a vector even in $q$ ... averages to zero": asserted with no step. I could not verify it.
- Terms: "hexaferrite" (for hexagonal LuFeO$_3$, where the usual meaning differs); "pseudo-angular momentum"; "phonon Hall effect"; $T_{CM}$ is never expanded.

**Steps I could not reproduce**
- GaAs band averages (0.124, 0.112, 2.2 MeV, 0.015 $\mu_N$): these need the Ch. 5 force constants. Not attempted.
- The spin-wave curve of lim:14.5b (1.4 and 4.5): not attempted.
- Checked:
  - Eq. 14.5-recip signs; eq. 14.5-gyr via the FDT; eq. 14.5-helicity; $n_\pm$; eq. 14.5-rot gives 21.6°/mm at 2.105 eV; $q g_{33} = 7\times10^{-5}$.
  - The $\mathcal{O}_5$-$\mathcal{O}_8$ interference $\mathfrak{D}$ and its contraction $(1/m_e)\mathrm{Re}(c_5^* c_8)\,q\cdot\mathcal{G}$; the factor $2\pi^2$ in eq. 14.5-enant.
  - $D_3$ character counts (0, 1, 2); $-0.0057$ bohr and $-0.045$; the $[H, L_z]$ commutator; $Z^* m_p/M_{Ga} = 0.030$.
  - Mn$_{12}$: $D$ = 0.0563 meV, 1.07, 1.21, 1.098 meV, 12.7 K, next line 0.18 meV lower, barrier top at $m = -1$ with 4.59 meV / 53 K; eq. 14.5-smm, weight $2|S|$, net weight $2|\langle S_z\rangle|$.
  - Alves conversion factor $n_r/|\varepsilon|^2$; $\mathcal{J}(0) = -i\sum\sigma\cdot\nabla/2m_e$.
  - Weiss vs Landau: the ratio is 1.105 at $0.94\,T_{CM}$, so the stated threshold is borderline but correct if read as Weiss/Landau within 10%.

**Too fast**: the whole section moves at survey pace (three detector concepts in about 4 pages). Chiral phonons and multiferroics are mostly literature statements I take on trust.

**Outcomes**
- Use reciprocity to decide which blocks can be odd in $q$: yes.
- Count invariants for a point group: yes.
- Write the enantiomer difference: yes.
- Compute SMM line positions and weights: yes.
- Multiferroic cross response: only qualitatively, because eq. 14.5-GL is opaque.

## 14.6 Coherent fields and precessing nuclear spins
**Lost points**
- Lim. 14.6c and the paragraph after it: the "exact Neyman construction ... with $N_{eff}$ equal bins" is described only in a figure caption. So 1.99, 1.76, 1.5%, 3.46, 2.24, 23 and 5.4 $t_{coh}$, and 136 / 8.7 cannot be reproduced from the text. One displayed sentence giving the statistic and its distribution under each hypothesis would make them checkable.
- "Schiff moment" and "PMN-PT" are used with no gloss (the moment's role is explained, so this is minor).

**Steps I could not reproduce**: the Neyman-construction numbers above. Checked:
- 241.8 kHz; 26.8 mT; $4.6\times10^{39}$ quanta; $t_{coh} = 1.044$ s; 249 km; top of line $3.5\times10^{-6}$.
- From an SHM sample, the $F_\phi$ peak / mean / equivalent width / half-correlation come out 0.578 / 1.267 / 2.673 / 1.47 (book: 0.58 / 1.27 / 2.67 / 1.47).
- Fejér normalization; the $\min(t_{coh}, 1/\Gamma_T)$ criterion; geometric variance; $3.4\times10^7$.
- Heisenberg precession; $p_{pol} = 2.27\times10^{-4}$; $\mu_0 M_0 = 2.9$ nT; $b_\phi$; $\Omega_{Rabi}$ (both couplings); the rotating-frame ODE and eq. 14.6-mperp (all three forms); the Budker envelope factor 2; $u_{sp} = 3.84\times10^{-4}$; the three regimes of eq. 14.6-ms; saturation 0.387 for $T_2 = 10\,t_{coh}$ (book 0.39); $(\Omega t)^2/6$; $M_z = M_0/(1 + \Omega^2 T_1 T_2)$; noise independent of $p_{pol}$.
- $\mathsf{t} \simeq \sum x^2$; both scalings of eq. 14.6-scaling, with $\mathsf{t} = 2\pi t\sigma^4/(\Delta\omega_{eq} S_n^2)$; 0.41 Hz; 63; 3447 and 82,730; $24^{1/4}$.

**Too slow**: the Bloch-equation setup is familiar NMR material, but it is needed for the notation. No harm.

**Outcomes**
- Decide when the golden rule applies vs the coherent regime: yes.
- Solve the linearized Bloch equations for a driven ensemble: yes.
- Explain the exponential-bin likelihood and derive the two sensitivity laws: yes.
- Quantify the fixed-amplitude bias: only by quoting the book's numbers.

## Chapter-level remarks
- Summary para. 2: "lower by $v_{max}/4c_M$, a factor 5.0". $v_{max}/4c_M$ is 4.77. The 5.0 is the exact eq. 14.2-mratio. Quote the exact form or give 4.8.
- Summary para. 2: "0.073 ..., the fraction that the sum rule moves out of the one-magnon line". The sum rule moves $\Delta S/|S| = 0.078$, and 0.073 is what arrives in the continuum (they differ by $\Delta S^2$). The wording conflates them; Sec. 14.6-nuisances gets it right.
- Tab. 14-nuisances: the basis "bound" on the one-magnon weight row should become "est." unless the 14.1 argument is tightened (see 14.1).
- Pace overall: 14.1-14.4 are at the right speed for me, with D.38 a real help. 14.5 is much faster and more descriptive. 14.6 is clear until the Neyman numbers.

**Would I keep reading?** Yes. The magnon chapters are the strongest stretch since Ch. 7: I could rebuild the NiO rate curve from the printed formulas to within a percent. My residual doubts are the strength of the "at least 7.8%" claim, the opaque Ginzburg-Landau formula of 14.5, and statistical factors in 14.6 that I must take on trust.
