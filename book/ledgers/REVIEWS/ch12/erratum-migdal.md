# Ch12 erratum check: the coherent small-q Migdal response against eq:8.3-boostward

Reviewer: Ch12 erratum verifier (isolated). Date 2026-11-06. Trigger: ch17/derivation-2.md §A, ch17/editor-notes.md (17.4 entry).
No tex edited, nothing committed. Scripts and logs: `ledgers/REVIEWS/ch12/erratum-migdal-scripts/` (light numpy and scipy only, no QE).
Every number below is in one of those logs (file named in brackets).

## Verdict: PARTLY

What is right in the Ch17 claim:
- eq:8.3-boostward binds the coherent response at q ≪ q_BZ. With Debye–Waller ≈ 1 (2W(2 keV) ≈ 2.5e-3), the Migdal process at these q is
  the coherent zero-phonon process of the whole lattice. Its exact limit is
  dP/dω_e → (m_e/M)² (2q²/e²) L(q,ω_e) / (2π n_at), where L is the head of ε⁻¹ (the screened, measured loss function).
- eq:12.3-soft / eq:12.4-harm / eq:D.33-diag (diagonal G = G′, self part of the lattice factor) do not obey this limit. As q → 0 they are
  high by 14.9 (Si, KKL RPA+LF table), and the ratio stays finite as q → 0 because both forms scale as q². The spectral shape is wrong too:
  the exact spectrum has median 17.4 eV (plasmon), the diagonal one has median 4.5 eV [ratio_tab.log]. The Ch17 table (14.9, 15.3, 16.1, 16.8,
  17.7) is reproduced: 14.88 at 0.49 keV, 15.33 at 0.97, 16.05 at 1.48, 16.80 at 1.85, 17.30 at 1.97 keV.
- The 12.4 Bragg check (1.08/1.04/1.03) uses the diagonal, direction-averaged L(|p|). It averages the coherent sum over the zone, so it cannot
  test the identity.

What is wrong or overstated:
1. **Range in q.** The identity is a q → 0 statement: ⟨f|Σn_κ|0⟩ = −(m_e/M)⟨f|n_e|0⟩ + O(q²). Relative to the leading term the remainder is of
   order q·v_band/ω_e, plus the zone scale q/q_BZ (derivation below). The 15–18 for 1.0–2.3 keV comes from applying the q → 0 formula at the zone
   boundary, where it does not hold. In a model where the identity is exact (non-interacting electrons, the same local pseudopotential as
   Hamiltonian and vertex), the coherent result divided by the identity is 0.996, 0.989, 1.034, 1.181, 1.449, 1.79, 2.13, 2.75 at q = 0.1, 0.25,
   0.5, 0.75, 1.0, 1.25, 1.5, 2.0 keV [run_coh.log]. So the identity is quantitative only for q ≲ 0.75 keV (≈ 0.33 q_BZ). Kinematics allow
   q ≥ E_g/v_max = 0.42 keV, so its range of use is a narrow strip.
2. **Mechanism.** "The large Umklapp terms cancel among themselves in the G ≠ G′ products" is not the whole story. In the non-interacting model the
   coherent sum is *larger* than its Bragg-diagonal part (×2.84 at 0.1 keV) [run_coh.log], yet the identity still holds. The suppression by about 15
   in Si comes from screening. The coherent kick of the lattice at q ≪ q_BZ is a long-wavelength longitudinal perturbation (the G = 0 term,
   with the bare Coulomb tail Z e²/p²). The valence electrons screen it with the macroscopic ε⁻¹ (head ≈ 1/11.7 away from the plasmon). The
   diagonal form samples ε⁻¹_GG at p ≈ 2.5 q_BZ, where ε_GG ≈ 1. The terms the diagonal/incoherent form drops are the **inter-site
   (I ≠ I′) coherence** of the zero-phonon lattice factor, which keeps k ≡ q and the full G ≠ G′ matrix at that k. The single-site G ≠ G′ terms
   are kept by offdiag12 and are a different object.
3. **Downstream reach** (rates, below). Applying the identity where it holds changes no printed rate by more than 0.2 %, except near the Migdal
   threshold (0.42–0.5 MeV in Si). "The 17.1 crossovers at 1–3 MeV" are affected only through the unsized band 0.75 keV ≲ q ≲ 2–3 q_BZ, and at
   3 MeV that band holds 0.2 % of the rate.

## Derivation (independent)

Crystal-frame amplitude of the kick on all nuclei, eq:12.1-amp summed over I, zero-phonon (Debye–Waller ≈ 1). Σ_I e^{i(q−p)·X_I} forces
p = q + G and gives the phase S(G) = Σ_s e^{iG·τ_s}:
  A_j(q) = Σ_G (q·(q+G)) v(|q+G|) S(G) ⟨j|n_e(q+G)|0⟩ / (Ω M ΔE_j²) = (i/(M ΔE_j²)) ⟨j| q·Σ_I e^{iq·X_I} ∇_{X_I}V_eN |0⟩.
At q → 0, e^{iq·X_I} → e^{iq·r_e} + O(q·(r_e − X_I)). Total momentum is conserved, so the electron–electron forces cancel in [H, P_e], and
Σ_I∇_{X_I}V_eN = −Σ_e∇_eV_eN = i[H, P_e]. Hence ⟨j|q·F|0⟩ = m_e ΔE_j² q·⟨j|r|0⟩ = −i m_e ΔE_j² ⟨j|n_e(q)|0⟩ + O(q²), and
  A_j = −(m_e/M)⟨j|n_e(q)|0⟩ + O(q²)   (eq:8.3-boostward at n_B = 2).
The remainder comes from the electron stress (kinetic flux, e–e stress) and from the electron–ion stress e^{iqX}−e^{iqr}. Relative to the leading
term it is ~ q⟨T_e⟩/(ΔE⟨p⟩) ~ q v_band/ΔE: with v_F ≈ 7e-3, about 1 at q = 1 keV near the gap, and about 0.4 at the plasmon.
The diagonal form keeps Σ_G|A_G|² with the momentum k of the pair free in the zone (self lattice factor). It has no reason to satisfy the identity.
Check in the model where the identity is exact: non-interacting Si in a local Cohen–Bergstresser-type pseudopotential (PCHIP in p², V3/V8/V11 =
−0.21/0.04/0.08 Ry). Indirect gap 0.86 eV, direct Γ gap 3.46 eV [bands.log]. Coherent/identity = 0.996 at 0.1 keV [run_coh.log], so both the
algebra and the normalization are confirmed.

## Reconciliation with the EPM-RPA ×1.2–1.4 (offdiag12)

The two numbers answer different questions and do not contradict each other.
- offdiag12 (i) is the **incoherent, single-site** form. It takes the structure phase of one struck atom, the closure lattice factor and k
  integrated over the zone. It is the impulse/incoherent object of eq:12.1-Skk with the self part of S^ad, and it knows nothing about I ≠ I′ coherence.
- For |q| ≳ (1–2) q_BZ, averaging the coherent zero-phonon response over directions of q is the same as averaging over the zone. Averaging over the
  shell's G₀ removes the cross-site phases e^{iG₀·(τ_s−τ_s′)}, and what is left is offdiag12's form (i). Checks:
  - RPA model, offdiag12 machinery, NK = 4, |G|² ≤ 11: coherent/(i) = 1.06, 1.03, 1.16, 0.90, 0.90, 1.08, 1.01, 1.01, 0.93, 1.10 in Q bins from
    2.4 to 9.5 keV, with (i)/(ii) = 1.56 at this truncation [cohrpa.log].
  - Non-interacting model: coherent/(zone-averaged full) = 1.03 (2 keV), 1.17 (2.5), 0.92 (4), 0.95 (5), 1.25 (7), with 3 directions and NK = 4
    (zone averages: diagonal 0.265, full 0.427 per keV²) [run_coh.log, inc_ni.log].
- At q ≪ q_BZ only the coherent form is right. The offdiag12 model cannot be used there: EPM eigenstates with the bare vertex Z_ion(p)e²/p² are not a
  conserving pair, and its coherent result at |Q| = 68 eV is 16.5× the identity [cohrpa.log]. The ×1.2–1.4 therefore stays valid in the regime it
  was computed for: the rates of 12.3 (q ≥ 92.5 keV) and the impulse-regime figures of merit of 17.5.
- The KKL-table identity value uses only L(q,ω) at q < q_BZ, which is robust (measured-equivalent head). The ×15 at q → 0 therefore stands.

## Which Ch12 statements change (wording, not numbers)

No printed Ch12 number changes by more than 0.2 %. The fraction of each rate that comes from q < 0.75 keV is ≤ 0.002 at every mass [rates.log].
The defect is one of domain. Recommended qualifiers for the Ch12 reviser (not applied here, per the PARTLY rule):
- s12-4 key result, l.~65 "dP_Mig/dω_e is eq:12.3-soft at every q" → "…at every q in the incoherent (self) lattice form. For the coherent
  zero-phonon process this holds for q ≳ 2 q_BZ on direction average. For q ≪ q_BZ the electronic spectrum is fixed by eq:8.3-boostward,
  (m_e/M)²(2q²/e²)L(q,ω_e)/(2πn_at), 1/15 of eq:12.3-soft in Si, with the plasmon shape. Between the two it is not computed." The same qualifier
  applies to s12-4 l.~3 and l.~8 ("Does the leading entry … hold … ? It does") and to WE 12.4's "By the sum rule … the electronic spectrum is eq:12.3-soft".
  At 5 keV (2.2 q_BZ) the zone-average statement holds within the G ≠ G′ nuisance.
- s12-4 l.~92 and l.~157 (Bragg sum 1.08/1.04/1.03; "zero-phonon line … within 8 %") → "within the diagonal, direction-averaged
  approximation; the cross-site G ≠ G′ terms of the coherent sum are not tested".
- s12-3 opening "At low mass … the formula holds unchanged" → add "for q ≳ 2 q_BZ".
- D-33 app:D.33-soft: after "Keep only G = G′ and the self part of the lattice factor", add that the self part is exact for the phonon-emitting
  incoherent terms and, on zone average, for q ≳ 2 q_BZ. The coherent zero-phonon part at q ≪ q_BZ obeys eq:8.3-boostward instead.
  D-34: its Migdal marginal uses "the incoherent lattice factor, whose weight is 2πn_κ at every momentum". Same qualifier.
- s12-1 (eq:12.1-Skk text): one sentence saying that eq:12.1-Skk with the full coherent S^ad satisfies eq:8.3-boostward at q → 0, and that
  its diagonal/self truncations do not.
- tab:12-nuisances, new row (or extend "Incoherent lattice factor below the zone"): "Coherent zero-phonon response at q < q_BZ | normalization;
  ω_e shape | exact limit q ≪ q_BZ: 1/14.9 of the diagonal form, median ω_e 17.4 eV against 4.5 eV (eq:8.3-boostward); quantitative to ≲ 20 % only
  for q ≲ 0.75 keV (model); 0.75 keV–2 q_BZ unsized; rate effect ≤ 0.2 % above 0.5 MeV for the part where it is exact | computed (limit); model |
  sec:12.4". Keep the G ≠ G′ row (×1.2–1.4) and add "incoherent/zone-averaged form; not applicable at q ≪ q_BZ".
- F rows (appF/F-rows.tex l.335–367, lim:12.3a/12.4a): add to the 12.4a row "valid for q ≳ 2 q_BZ (zone average); q ≪ q_BZ: eq:8.3-boostward".
- Figures fig12_1 (50 keV), fig12_3 and fig12_4: unchanged. Fig12_4's zero-phonon fractions are lattice-spectrum statements. Its points below
  ≈ 2 q_BZ inherit the unsized coherent factor in the absolute probability, not in the fractions plotted.
- Limit checks 12.3a/b/c and 12.4a/b: ratios between truncations that share the same electronic factor, or rates at q ≥ 92.5 keV. Unchanged.

## Changed numbers (old → new)

None of the printed Ch12/Ch17 numbers is replaced. New numbers for the qualifiers, each from the logs:
- small-q exact/diagonal: new 1/14.9 (q = 0.49 keV) … 1/17.3 (1.97 keV, outside the domain) [ratio_tab.log]
- exact spectrum median 17.4–20.4 eV, against 4.5 eV for the diagonal [ratio_tab.log]
- domain of the identity (model): ≤ 3 % to 0.5 keV, 18 % at 0.75, 45 % at 1.0, ×2.1 at 1.5 keV [run_coh.log]
- share of the Si heavy-mediator Migdal rate (ω_e ≥ 1.11 eV) from q < 0.75 / 1 keV / q_BZ [rates.log]:
  0.42 MeV 0.002/0.217/1.000; 0.5 MeV 0.002/0.079/1.000; 0.7 MeV 0/0.012/0.810; 1 MeV 0/0.002/0.287; 2 MeV 0/0/0.013; 3 MeV 0/0/0.002;
  ≥ 6.3 MeV 0.
- rate with the identity in place of the diagonal form below a cut, over the diagonal rate [rates.log]:
  - cut 0.75 keV: ≥ 0.998 at every mass;
  - cut 1 keV: 0.783 (0.42 MeV), 0.921 (0.5), 0.988 (0.7), 0.998 (1 MeV);
  - cut q_BZ, a lower edge beyond the domain: 0 (≤ 0.5 MeV; the plasmon is out of reach), 0.19 (0.7), 0.71 (1), 0.987 (2), 0.998 (3 MeV).

## Downstream items for Ch17 and the campaign ledgers

- **17.1, tab:17-crossover.** 1 MeV column: Migdal rate 1.9e-3 carries an unsized factor from q = 1–2.25 keV (28.7 % of it), bracket ≈ 0.7–1
  (could exceed 1 near the zone boundary). From 3 MeV on: ≤ 0.2 %, no change. The crossover thresholds move negligibly, since the lattice side falls
  by ×65 per 0.1 eV. Fig. 17.sectors: the Migdal band at 0.32–0.7 MeV is unsized. Near threshold it can be suppressed by a large factor, because
  the exact small-q spectrum sits at the plasmon, beyond the 1.2–1.8 eV that is kinematically open. State this, and do not plot it as computed.
- **17.4.** eq:17.4-lock is eq:8.3-boostward applied to the one-phonon sector and is consistent with this finding. Its O(qa) → O(q/q_BZ) wording fix
  (derivation-2) is supported. The domain found here (≲ 0.33 q_BZ for 20 % accuracy) is the quantitative form of that remainder, and the Si
  window at q = 0.9–1.3 keV lies outside it. Keep "order of magnitude only" in the window nuisance row.
- **17.5 Migdal pole factor and tab:17-fom.** Impulse regime (Si above 17.5 MeV): unaffected. The ×1.2–1.4 applies there.
- **17.6 rankings.** Built on the 17.5 pole factor: unaffected.
- **tab:17-nuisances.** Add the row "coherent Migdal at q < q_BZ: diagonal form 15× high as q → 0 (eq:8.3-boostward); quantitative only below
  ≈ 0.75 keV; affects m_χ ≲ 1 MeV".
- **Ch13.** No Migdal rate is used. Nothing to change.
- **Campaign ledgers.** Record the result: the diagonal/incoherent Migdal form is the zone-averaged (q ≳ 2 q_BZ) object. The coherent q → 0
  limit is (m_e/M)²S_ee, 1/15 in Si. The 15–18 at 1–2.3 keV in derivation-2 §A.3 is outside the identity's domain and should not be quoted
  as computed. Close the Ch17 "PRIORITY 1" item as PARTLY: qualifiers in Ch12, no number changes.

## Applied (2026-11-06)
Qualifiers applied as small exact edits; no printed number changed. Scripts copied to figscripts/ch12 and rerun there:
migdal_ratio12.py (= ratio_tab.py, log identical), migdal_rates12.py (= rates.py, log identical, plus a block for the shares of
0.75 keV ≤ q < q_BZ and < 2 q_BZ), migdal_coh12.py with migcoh12/migmodel12/migwcb12.py (= run_coh.py/coh.py/model.py/wcb.py).
- tex/ch12/s12-4.tex: l.5 opening question ("It does … for the incoherent lattice factor … q ≳ 2 q_BZ; q ≪ q_BZ obeys eq:8.3-boostward");
  key result after eq:12.4-harm (incoherent form; coherent = same for q ≳ 2 q_BZ; q ≪ q_BZ: (m_e/M)²(2q²/e²)L/(2πn_κ), 1/14.9, median 17.4
  vs 4.5 eV; between not computed); Bragg-check sentence (diagonal, direction-averaged; cross-site G ≠ G′ terms not tested); open-items
  paragraph ("diagonal, direction-averaged Bragg sum within 8 %"); WE 12.4 probability (2.2 q_BZ: direction-averaged coherent process within
  the G ≠ G′ row).
- tex/ch12/s12-3.tex opening: "holds unchanged for q ≳ 2 q_BZ (sec:12.4)".
- tex/appD/D-33.tex app:D.33-soft and tex/appD/D-34.tex: domain of the self part / incoherent lattice factor.
- tex/ch12/s12-6.tex tab:12-nuisances: new row "Coherent zero-phonon response at q < 2 q_BZ"; G ≠ G′ row: "incoherent, zone-averaged form,
  not applicable at q ≪ q_BZ".
- tex/appF/F-rows.tex 12.4a row: validity q ≳ 2 q_BZ (zone average), q ≪ q_BZ eq:8.3-boostward.
- tex/ch17/s17-1.tex (Migdal band qualifier, fig:17-sectors caption) and s17-summary.tex (tab:17-nuisances row); see ch17/revision.md.
- Not applied: the optional s12-1 sentence on eq:12.1-Skk (not in the task list).
- Finding from the added rates block: the band 0.75 keV–2 q_BZ carries 0.998–1.000 of the Si rate at 0.42–1 MeV, 0.327 at 2 MeV,
  0.074 at 3 MeV, 0.003 at 6.3 MeV (the 28.7 % above is the part below q_BZ).
- migdal_coh12.log (defaults ECUT 6, NK 6, 8 directions) differs slightly from run_coh.log, whose arguments are not recorded:
  coherent/identity 1.000, 1.001, 1.029, 1.152, 1.381, 1.723, 2.180, 3.310 at q = 0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0 keV. The printed
  domain uses this log: "within 15 % only for q ≤ 0.75 keV" (the 18 % above is from run_coh.log).
