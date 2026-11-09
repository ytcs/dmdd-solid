# Chapter 18 mock-reader review: reader b (personas b and c)
Source read: tex/ch18/*.tex (identical in content to the current build/main.pdf), linearly, after Chs 1-8, 10-17.
Arithmetic checked in Python (scipy): every number listed as "reproduced" below was recomputed, not just read.

## Persona (b): particle physicist, QFT yes, solid state no

### 18.1 The carrier cascade
- **Lost points.** None blocking. Two places needed a second read:
  (i) the iso-energy reduction talks about "quasi-elastic scattering by intervalley and acoustic phonons" without saying, here or in a footnote, why those collisions change the momentum but barely change the energy. Chs 6-7 define the terms, but the point that intervalley phonons are a few tens of meV against eV of kinetic energy is what makes $\Gamma_k \gg \Gamma_E$ plausible, and it is left implicit. One clause would fix it.
  (ii) The Fig. 18.1 model uses $A_{\mathrm{AB}} = 5.2$ with $\Eg = 1.17$ eV and is "chosen to reproduce the measured pair energy". From 18.2 on, the calibrated value is 5.674 at $\Eg = 1.160$. Only in 18.3 ("the calibrated constant lowers them by less than 0.03") and 18.4 (5.2 is a 300 K fit) do I learn that these are two different silicon models. A half-sentence in 18.1 would stop the double-take.
- **Steps reproduced.** Threshold (18.1-theta): eliminating $u$ gives $x(m_e+m_h)/(2m_e+m_h) = \Eg$. Correct, and 3/2 for equal masses. FDT step: $S = -2(1+n_B)\,\mathrm{AH}(R)$, $v R v = W - v$, diagonal limit $-2\Imag W_{GG} = 2 v L$. Correct. Toy cascade: $\mathfrak{G}_2 = 0.76s + 0.24$, probabilities 36/625, 228/625, 361/625, mean 2.52, variance 0.3648, ratio 0.145. All exact. Dirichlet constant $2\pi/105$: correct. Pauli and Coulomb estimate: 267 pairs, $6.4\times10^{19}$ cm$^{-3}$, $4\times10^{-3}$, $n a_x^3 = 4.7$ and 0.47. All correct. Equal rates at 5.76 eV for $A=5.2$, $\Eg=1.17$: matches "5.8 eV". 50 eV: $50 - 13.06\times1.17 = 34.7$ eV of heat: matches.
- **Could not reproduce.** None (the sampled numbers of Fig. 18.1 are numerical results, not derivations).
- **Used before defined.** "Minimal solution" and "the toy branching law $1-p+ps^2$" point to App. C.11, which the chapter's reader is not told to read. Persona (b) knows extinction fixed points, so this is fine for me, but see the global note below.
- **Pace.** The common-velocity threshold argument is undergraduate kinematics for me: slightly slow, but harmless. The 18.1-ii paragraph on $z_{\mathrm{qp}}$ and the cutting rule is the right speed.
- **Outcomes.** (1) Write impact ionization as a master-formula rate with one coupling row per $\vect{G}$: yes. (2) Derive $\theta_{\mathrm{ii}}$: yes. (3) Set up and solve a backward equation for a small cascade: yes (toy redone by hand). (4) State why the seed split matters: yes.
- **Own field.** $-2\Imag\Sigma^R = \Gamma_{\mathrm{out}} + \Gamma_{\mathrm{in}}$ (a sum for fermions) is right, as is $\Gamma_{\mathrm{qp}} = -2z\Imag\Sigma$. Calling the carrier-electron exchange a vertex correction is standard. No condescension.

### 18.2 Mean energy per pair and the Fano factor
- **Lost points.** (a) Eq. (18.2-tagged): "$x_1 = E, x_2, \dots$ are the kinetic energies of the successive carriers that hold it". The weight is attached to *ionizations*, so the sum should run over the ionization events on the unit's chain, at the energy each carrier has *when it ionizes*. As worded, it reads as one term per carrier, and $x_1 = E$ assumes that the first collision is an ionization. A carrier that emits $k$ phonons first ionizes at $E - k\omega_{\mathrm{AB}}$, not at $E$. Probably a wording issue, but I could not tell which sum is meant until I rebuilt the argument. Fix: "$x_j$ the kinetic energy at the $j$-th ionization of a carrier holding the unit".
  (b) "$\lambda_{\mathrm{AB}}$ is the strength of phonon emission relative to impact ionization a gap above threshold." At $x = 2\Eg$ the ratio (18.1-randomk) is $\lambda_{\mathrm{AB}}\sqrt{2}\cdot105/(2\pi) \approx 23.6\,\lambda_{\mathrm{AB}}$, not $\lambda_{\mathrm{AB}}$. Say "proportional to".
- **Steps reproduced.** (18.2-moments) and the decomposition: identities, fine. Poisson estimate $\mathcal V_> = 0.0543\times0.93/1.16 = 0.043$; ratio 6.7; covariance cancels 92%; 1% error moves $F$ by 2.6%. All correct. Random parking: the ODE for $\phi$, its integrating factor $e^{-2E_1}$, the small-$s$ limit and $\rho_\infty = 0.74759792$ (scipy: 0.7475979203). Gap law: $\int G = \rho_\infty$, $\int (1+g)G = 1$, $\langle g\rangle = 0.337617$, $\operatorname{Var}g = 0.079437$, $F_{\mathrm{ren}} = 0.0443977 = 0.870\,F_{\mathrm{park}}$. All reproduced. Shockley uniform population: mean $0.9\Eg$, variance $27/175$, $F = 54/175$ and $27/686$. Reproduced.
- **Could not reproduce.** The second-moment recursion is never written in the chapter: (18.2) points to (C.11-second) and (D.43-m2). So the three silicon terms 0.092/0.291/-0.269, $F_{\mathrm{park}}$ on the grid and the Fig. 18.2 curves cannot be checked from the chapter text. Writing the energy-only second-moment recursion in one display (it is short) would make 18.2 self-contained.
- **Used before defined.** $b_N$, $c_N$ appear in 18.2-heat before 18.2-linear discusses them (forward-referenced, acceptable). The key renewal theorem is used by name (App. C.11).
- **Inconsistency.** The grid step is $\Eg/74$ here and in Figs. 18.limit-moments/park, but 18.4-model says "halving the grid step from $\Eg/73$". One of them is a typo.
- **Lim 18.2b.** For a constant density of states the ratio is $A/(x-\Eg)$, so $A$ carries eV, not eV$^3$. Reusing $\lambda_{\mathrm{AB}} = A_{\mathrm{AB}}/\Eg^3$ there is dimensionally loose. Define $\lambda$ for that kernel as $A/\Eg$, or say so.
- **Pace.** The random-parking worked example is dense but complete. Good.
- **Outcomes.** (1) Get $\varepsilon_{\mathrm{eh}}$, $F_{\mathrm{eh}}$ from the energy identity: yes. (2) Explain why $F$ is a small difference of large terms: yes. (3) Compute the parking constants: yes. (4) Compute the three terms myself: no (recursion not shown). (5) Say why the renewal estimate is low: yes, qualitatively.

### 18.3 Seeding and the phenomenological models
- **Lost points.** None blocking.
- **Steps reproduced.** Step model at 5 eV: $1 + \lfloor1.024\rfloor = 2$. $p_{\mathrm{ii}}$ at 2/2.5/3/3.5/3.84 eV: 0.0041/0.0185/0.049/0.100/0.146, exactly. $P_{\mathrm{no}}$ over 43 steps is 0.1747, and the integral form gives $-1.744$, i.e. 0.175. Equal split at 1.92 eV: 0.990. Fig. 18.pn10 mean and variance from the rounded bins: 2.63 and 0.314 (after rounding). Step-model mean $\omega/\varepsilon + 0.19$. $\sigma_N(20.2\,\mathrm{eV}) = 0.78$. The 5.9x ratio and the 12% photon excess. Law of total variance (18.3-moments). All correct.
- **Could not reproduce.** The dark-matter seed numbers (0.830/0.170, the 26% one-sided weight) need the Ch. 8 band seed. That is expected and stated.
- **Overstatement.** "The second term of the variance ... vanishes only for a seed with a single split." It also vanishes whenever $m_e + m_h$ is constant on the seed's support, for instance in the forced region, where both are zero. Write "vanishes for a single split".
- **Used before defined.** "Valleys" in "the valleys and crystal momenta of the first generation" (Ch. 3 defines them, so this is fine). The forward reference to Sec. 19.5 for "the phonon energy goes to heat once" points to a chapter I have not read, but 8.7 already said it.
- **Outcomes.** (1) Build $P(N)$ from seed and cascade tables: yes. (2) Show the step model failing at a few pairs: yes (redid the 5 eV single-carrier case). (3) Place the R-K model as a limit: yes.

### 18.4 Pair energies in Si, Ge and GaAs
- **Steps reproduced.** $\lambda$, $w$ for Si, Ge, GaAs; $2.5\sigma$ and $1.0\sigma$. Shockley sum $1.160+1.661+0.928$; $\bar E_{\mathrm{res}} = 0.716\Eg$; 14.7 phonons. The uniform mean $\frac35\theta\Eg$; 39% and 36%; $\bar E_{\mathrm{res}} = 0.293, 0.528$. Diamond: $\lambda = 0.035$, Klein 15.9 eV. Exponent 0.046, $k_2 \propto \omega^{0.232}$. $k_2(\mathrm{Si}) = 1.87$. GaAs worked example: 0.04377, 0.4713, 4.13 eV, $k_2 = 1.67$, 4.23 and 4.76 eV, and 3.96 eV at 1.42 eV. All reproduced. Tab. 18.valid residuals reproduced. The RMS is 12.2%.
- **Could not reproduce (last digit).** The mean residual from the tabulated values is +8.0%, not +8.1%. Ge from the table, 2.96/2.81, is +5.3%, not +5.2%. Presumably unrounded model values. Either quote those or recompute from the table.
- **Minor confusion.** The Klein box uses $\theta_{\mathrm{ii}} = 3/2$ and no hole cutoff, and "silicon, at 3.64, sits almost on that point". But the calibrated silicon model is $\theta = 1$, with $\bar E_{\mathrm{res}} = 0.716\Eg$, far from 0.9. Say explicitly that the 0.2% agreement is in the $\theta = 3/2$ variant (whose silicon constant, 5.604, gives $\lambda = 3.59$).
- **Inconsistency.** The lead-in to Tab. 18.valid says "highest longitudinal optical phonon energy"; the caption says "highest optical phonon energy" for diamond, GaN and quartz.
- **Pace.** Good. The "what this agreement shows is limited" paragraph is exactly what I want.
- **Outcomes.** (1) Estimate $\varepsilon_{\mathrm{eh}}$ for a new crystal from $\Eg$, $\omega_{\mathrm{AB}}$: yes (GaAs redone). (2) Derive Klein as a truncation: yes. (3) State the validated range: yes.

### 18.5 The end of the cascade
- **Lost points.** The capture bookkeeping relative to the electrodes' Fermi level $\mu_F$ took two reads: why the unpaired hole "holds $\mu_F - E_v$" when nothing is connected to an electrode yet. One sentence would fix it: energies are the work the charge does when it finally reaches an electrode, so they are measured from $\mu_F$.
- **Steps reproduced.** (18.5-thin) from (18.5-thingen); $f_{\mathrm{cap}} = 0.56\%$ (range 0.34-0.79%) and the +0.57% shift. $r_C$, cross-sections, the 20 cm path, 29 $\mu$m. Worked example: 25.80, 26.97, 4.17 eV, 11.1%, $F' = 0.207$, 1.09 to 1.37, and $0.96 + 0.90$. $F_{\mathrm{heat}}$ and $(1-E_x^b/\Eg)^2$: 2.5% and 1.3%. $r_{\mathcal E}$: 0.56 and 0.11 $\mu$m. Exciton ionizing field $3.5\times10^4$ V/cm. Poole-Frenkel 2.25 meV and exponent $1.0\times10^4$. Direct bound pairs: 25 and 8.5 meV. Rate equations with the Fig. 18.end rates: weights +1.28/-0.33/+0.05, bound peak 0.145 at 0.45 $\mu$s, half at 0.83 $\mu$s, 1% at 4.41 $\mu$s, 42% missed at 1 $\mu$s, split 0.050/0.009/0.941. All reproduced exactly.
- **Used before defined.** "Electron-hole droplets" (open problems only, undefined), and "metastable state with low trapping" (fine as a citation).
- **Own field (units).** $\alpha/(\varepsilon_0 r)$ in natural units sits next to $e\mathcal E$ in V/cm. The numbers are right ($\alpha = 1.44$ eV nm with $\hbar c$ restored), but a reminder at first use that $\alpha \to \alpha\hbar c = 1.44$ eV nm would help a reader from either side.
- **Outcomes.** (1) Book a capture or exciton in energy and pair number: yes. (2) Propagate random capture to $\varepsilon'$, $F'$: yes. (3) Solve the linear rate equations for the branching fractions: yes.

### Verdict (b): MINOR GAPS
I would keep reading. Every derivation in the chapter checks numerically. The gaps are the ambiguous sum in (18.2-tagged), the unprinted second-moment recursion and a handful of last-digit or labelling inconsistencies. None blocks later material.

## Persona (c): condensed-matter theorist, DFT and many-body yes, dark matter no

### 18.1
- **Lost points.** None. The dark-matter vocabulary ($q_0 = \alpha m_e$, the class $\Lambda$, sectors $\mathcal P_0$/$\mathcal P_+$, the hand-off, coupling rows) all comes from Ch. 8 and is used consistently. Fine, since I have read Ch. 8.
- **Own field: correct.** Screened-interaction kernel, the plasmon inside the loss function for Si (overdamped, so no separate channel), the Fröhlich double counting and its three matching conditions (Born charges and $\varepsilon_\infty$, multipole order, the Gaussian cutoff), the inversion-centre remark on $W_{GG'} = W_{G'G}$ (needs inversion plus time reversal, as stated), and $z_{\mathrm{qp}} \approx 0.8$. This is a careful treatment, better than most semiconductor texts.
- **Own field: quibble.** The Pauli-blocking estimate compares the pair density with the *average valence* density of states over 12 eV. The relevant states are the final states of the hot carriers, at a few eV in the conduction and valence bands, where a parabolic estimate gives a few $10^{21}$ cm$^{-3}$ eV$^{-1}$. The conclusion (blocking negligible) survives, but the comparison should be with the density of states at the carriers' energies.
- **Pace.** The FDT and $W - v$ step is fast but correct for me. For persona (a) it relies wholly on Sec. 4.8.
- **Notation.** $x$ is both the "state" of a cascade particle (18.1-branching) and its kinetic energy (everywhere after). $p$ is the momentum transfer, the probabilities $p_a, p_b$, the Beta density $p(f)$, the occupations $p_F$ and $p_{\mathrm{ns}}$. Readable, but $x$ in particular should be split.

### 18.2
- **Lost points.** Same as (b): the tagged-unit sum and the meaning of $\lambda_{\mathrm{AB}}$.
- **Own field.** The decomposition and its interpretation (anticorrelation along one line of descent, not between siblings) are correct and insightful. The random-parking comparison with Subashiev-Luryi is correct: I confirm $\rho_\infty = 0.7475979203$ (Rényi's constant), so their printed 0.7475987 is indeed off in the seventh digit.
- **Outcomes.** As for (b). Without the printed second-moment recursion I could not reproduce the silicon terms. As a DFT user I would want it in the text, since the claim "computes exactly" is the selling point.

### 18.3
- **Lost points.** None. The DFT-on-roots-of-unity aliasing statement is right ($N_z = 32$ against means below 6).
- **Dark-matter side.** That the seed is model-independent for one coupling row, and that dark-photon absorption shares the photon seed, are both clear from Ch. 8. The key physics claim (DM at $q_0$ shifts about 0.9 eV to the hole relative to a photon) is cited, not rederived. Acceptable.
- **Outcomes.** Yes, as for (b).

### 18.4
- **Own field: correct.** The gaps (Si 1.160/1.17, Ge 0.735/0.744, GaAs 1.42/1.52), the phonons (Si 63, Ge 37.6, GaAs LO 36.35 meV), the Si valence width of 12 eV, $\varepsilon_{\mathrm{eh}}$(Ge, 77 K) = 2.96 eV, Rodrigues et al. 3.749 eV and 0.119, the Klein and Shockley forms, and diamond near 13 eV. The statement that a constant matrix element cannot tell Fröhlich from deformation-potential coupling is right. The honesty about two implementations of one model agreeing is welcome.
- **Own field: quibble.** GaAs: besides Fröhlich, the strongly unequal masses and the $\Gamma$-$L$-$X$ conduction structure make a single parabolic random-k kernel especially crude. A clause would sharpen "the polar contrast".
- **Inconsistencies.** As in (b): mean residual 8.0 vs 8.1%, Ge 5.3 vs 5.2%, LO vs "highest optical" in Tab. 18.valid, grid $\Eg/73$ vs $/74$.
- **Outcomes.** Yes.

### 18.5
- **Own field: mostly correct.** P donor 45.6 meV, $\varepsilon_0 = 11.4$ at LHe, Si exciton 14.7 meV and 4.2 nm, the Auger-dominated bound-exciton decay at the P donor (200-300 ns), Poole-Frenkel lowering, frozen thermal emission. The capture bound $\pi r_C^2$ is a reasonable geometric ceiling for hot carriers, and the text rightly says that cold carriers (giant-trap or cascade capture) are a different regime.
- **Own field: small error.** The Ge free (indirect) exciton binding energy is about 4.2 meV. "About 5 meV" is high by about 20%. The derived 1.3% becomes about 1.1%, and 8.5 meV becomes about 7 meV. Not consequential, but in a table of sizes it should be the measured value.
- **Lost points.** "Electron-hole droplets" is unexplained (I know it, but persona (a) will not). For persona (c) the electrode-$\mu_F$ bookkeeping is natural.
- **Outcomes.** Yes, all three (redone as in (b)).

### Verdict (c): MINOR GAPS
I would keep reading. The many-body content is correct and unusually careful about double counting. My flags are a crude Pauli-blocking comparison, the Ge exciton binding energy, notation overloading ($x$, $p$) and the same reproducibility gap in 18.2 as persona (b).

## Priority fixes (both personas)
1. Reword (18.2-tagged): sum over ionization events at the ionizing energy; drop or qualify $x_1 = E$.
2. Print the energy-only second-moment recursion in 18.2 (one display).
3. "$\lambda_{\mathrm{AB}}$ ... relative to ionization a gap above threshold" should say "proportional to" (the factor is about 23.6). Define $\lambda$ separately for the constant-DOS kernel of Lim. 18.2b.
4. Grid $\Eg/73$ vs $\Eg/74$; mean residual 8.0 vs 8.1%; Ge 5.2 vs 5.3%; LO vs "highest optical".
5. 18.3: "vanishes only for a single split" is too strong.
6. 18.1: flag early that the $A = 5.2$, $\Eg = 1.17$ model of Fig. 18.1 is not the calibrated one. 18.4: say that the Klein match at silicon is in the $\theta = 3/2$ variant.
7. Ge exciton binding about 4.2 meV; Pauli comparison against the DOS at the carriers' energies; define electron-hole droplets or drop the term.
