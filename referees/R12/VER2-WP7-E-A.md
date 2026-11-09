# R12 re-verification VER2-WP7-E-A: returns/R12/WP7-E-v3.md against referees/R12/VER-WP7-E-A.md

Read: WP7-E-v3 §0–§7, §5 (A-1…A-16), §6 and its closing table; code/WP7-E-v3/checks.py, run 47/47 PASS; WP7-T-v2 updated Theorem T-1 (conditions (i)–(v),
time-dependent rates, naming of E_st^{unrel}). I re-derived the algebra of the corrected items by hand (below).

## 1. VER-WP7-E-A items
| VER item | Verdict | Check |
|---|---|---|
| §1 row 1 / §3.1: exciton E_g unbooked | RESOLVED | E_X = Σ(E_g − E_x^b) is now an explicit reservoir and E_pairs counts unbound carriers only. Formation moves E_g → E_X + ℋ_ph(E_x^b), which conserves (E1) (C13c). From (E1-pr), with N_eh ≡ N_e^f + N_X and E_X = N_XE_g + E_x, I recover (E1-W4) exactly |
| §1 row 3 / §2: ΔZPE vs E^conf | RESOLVED (minor omission, §3.1 below) | E_st is configurational and ΔZPE sits in ℋ_ph, matching T-1 (v) and WP5 (W12). A ZPE sum rule telescopes separately (C16) |
| §1 row 8 / §3.2: (1−κ) term; central values as bounds | RESOLVED | (E13): d′_NR − κd′_ER = [E_st + ΔX + (1−κ)X_ER]/ω. Bounds are now 95% C.L.: 0.055/(0.4·0.65) = 0.21 and p_surv ≲ 0.47 (Si); Ge 0.064 → 0.20 and 0.66. Conditions (B-a)–(B-c) are stated; under them 1 − η ≥ E_st/ω, since the r-term g(r−1)(1−y)/(1+rg) ≥ 0 for r ≥ 1. The degeneracy r = 1.144 → η = 0.952 checks: g = 1.047, y = 0.3 gives −0.048 |
| §1 row 13 / §3.3: 1803.02903 collection efficiency misread | RESOLVED | now a field- and model-dependent ratio used only as a one-sided, flagged constraint. θ_tr's central value no longer comes from it (σ_ln 0.5) |
| §1 row 15 / §3.4: θ_tr^{pr} with f₀ = 0 | RESOLVED | f₀ = 10⁻³, ψ = ln 10.09 gives f(1) = 0.01 (C14a). The f₀ > 0 requirement is stated for every two-point type T, θ_X included |
| §1 row 16: excitons absent from §7 | RESOLVED | exciton/EHD rate equations, field suppression, inputs (WP1 BSE), and "G4CMP does not model excitons" |
| §2 (E6) wording "constraint" | RESOLVED | "(E6) is an identity, Theorem T-1"; G-E3 narrowed to condition (ii) |
| §2 normalisation | RESOLVED | ∫∫𝒦^{rel} = ⟨N_hop⟩ in §1.5 and in the θ_𝒦 constraint |
| §2 mean versus event | RESOLVED | (E5) gives ⟨E_st(t)⟩; event by event, E_st(t) is a sampled hop sequence; Theorem E-0 is restated for the expectation and per realisation |
| §2 time-dependent rates | RESOLVED | WP7-T-v2 now states that T-1 holds for Γ_ij(t) (C16b). WP7-E-v3 IF-E2 still asks for it, so close that sub-item |
| §3.5 / A-12 pre-t_pr bias work | RESOLVED | eℰ_b v_d t_pr: 250 V/cm × 10⁷ cm/s × 100 ps = 0.25 eV; booked in 𝒲_bias and ℋ (C15). A-10 includes −𝒲_bias(t_pr) |
| §4 A-1 non-additive N_eh | RESOLVED (minor wording) | per-carrier deposits, and N_eh = N_e^f = N_h^f only without capture. Wording: "trapped electron (N_e^{tr} += 1, N_e^f −= 1 …)" double-books if an edge carrier is already absorbing and has deposited N_e^f. Either make "free at edge" a non-absorbing type until t_pr, or deposit N_e^{tr} instead of N_e^f |
| §4 A-3 | RESOLVED | E_st configurational; ΔZPE in ℋ_ph; ⟨N_hop⟩ |
| §4 A-10 sign and missing terms | RESOLVED | ℋ_eff = ℋ + E_trap^{pr} + E_es + E_pairs^{unp} + E_x − 𝒲_bias(t_pr), with E_x ≤ 0. Matches (E1-W4) and C13a |
| §4 A-11 | RESOLVED | f₀ = 10⁻³ |
| A-2, A-4–A-9, A-13–A-16 | RESOLVED (no regression) | A-4 and A-9 rewritten consistently with the multiplicative collection (E7); A-16 keeps dℛ/d𝐍 as the t_pr marginal |

## 2. (E6) against the updated T-1
- **Form and conditions (i)–(iii), (v): consistent.** Same t_obs cut, ⟨N_hop⟩ normalisation and configurational energies. ΔZPE is outside E_st and
  𝒦^{rel}, as T-1 (v) requires.
- **Condition (iv) is not cited (NOT RESOLVED, minor).** WP7-E-v3 §1.5 lists only T-1 (i)–(iii). (iv) requires a closed, linear, single-seed chain
  (Σ_iN_i = 1). Consequences to state in §1.5 and IF-E2:
  - the 3D correlated case escapes to a separated-pair state with probability 1 − r_c/d; that state must be listed in the chain;
  - uncorrelated (bimolecular) recombination and inter-seed reactions of the cooldown/stress reservoirs, E14 sources (ii)–(iii), are outside the per-seed (E6);
  - v3 rightly dropped (1+t/t₀)⁻² from θ_law, and should say why: it follows from (iv).
- **Naming mismatch (NOT RESOLVED, minor).** T-1 now calls the finite-t_obs quantity E_st^{unrel}(t_obs) and reserves E_st^{frz} for t_obs → ∞. WP7-E-v3 uses
  ⟨E_st^{frz}(t_obs)⟩ in (E5)–(E6), (E8), A-3, A-4 and θ_frz. Rename to E_st^{unrel}(t_obs); the physics is unchanged.

## 3. New errors
1. **ΔZPE missing from the sensor deficit (minor).** §1.1 puts ΔZPE inside ℋ_ph and says "only ℋ_ph^{avail} can reach a sensor". But
   D′ ≡ E_stored(t_win) + E_esc in (E7), (E8), (E13), A-4 and A-9 has no ⟨ΔZPE(t_win)⟩. The NR heat deficit therefore misses ~0.1 eV per surviving defect (~1% of
   E_st). **Fix:** D′ → D′ + ΔZPE(t_win), with ΔZPE^{ER} = 0, and carry it in (B-c) (sign either way, size ≲ 0.01E_st).
2. No other new errors found. The multiplicative collection (E7) is correct (absolute ϵ cancels in every NR/ER ratio). The Ge κ ≈ 0.6 checks
   (g = 4/3.0, y ≈ 0.3). The 2007.14289 "16.3 eV" is the source's own number.

## 4. Summary
Every VER-WP7-E-A item is RESOLVED, with a minor A-1 wording point. (E6) agrees with T-1 under (i)–(iii) and (v). Two minor items remain open:
- cite T-1 (iv) (closed single-seed chain) and its consequences;
- rename E_st^{frz}(t_obs) to E_st^{unrel}(t_obs).
One minor new omission: ΔZPE belongs in the pre-sensor deficit D′. None of these changes a stated number or bound beyond ~1% of E_st.
