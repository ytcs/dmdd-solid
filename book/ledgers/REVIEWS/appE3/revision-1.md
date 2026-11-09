# App. E second pass, part 1: revision of E.14–E.20 (plus E.1 l.147, 8.4)

Brief: briefs/reviews/appE3-revise-1.md. Inputs: consistency-1.md (items 1–26), ../appCE/prose.md (E.14–E.20 parts), editor-notes.md (rulings E1–E6).
Files edited: tex/appE/E-14.tex … E-20.tex, tex/appE/E-1.tex (l.147 only), tex/ch08/s8-4.tex (one pointer), NOTATION.md (appended entry 98).
New script: figscripts/appE/e20_zrte5_dirac.py with its log e20_zrte5_dirac.log (ZrTe₅ numbers of ruling E3).
Lint (`lint.py --banned BANNED-TERMS.txt` on E-1, E-14…E-20, s8-4): 0 blocking (warnings only: LONG-SENT, two EQ-PUNCT false positives on `gathered`).
Build (`latexmk -pdf -outdir=/tmp/claude-0/build-appE3-1 main.tex`): 0 errors, no undefined references or citations. Not committed.

## consistency-1 items

| # | Done | How |
|---|---|---|
| 1 | done | E.15 "Spin–orbit mixing": HSE06 reuse and the hybrid Fock-cutoff/exchange-grid clause removed; runs on Ge bands with SOC that pass the E.14 check (order, both gaps, masses at L and Γ), GW named as next route without verdict; convergence on the bands (number of bands, screening cutoff); "once bands that pass exist, less than a core-hour" (ruling E1). |
| 2 | done | E.1 l.147: "needs bands that pass the check of app:E.14 … with SOC"; hybrid at standard fraction inverts Γ and L even with SOC; 4s shift fitted to both gaps gets the masses wrong; quasiparticle route is next under that check. Broken clause on the SO splitting repaired. |
| 3 | done | E.16 library: scissor on PBE for Si only; Ge library built only on bands passing the E.14 check, no Ge version released until then. Candidate-target loss functions: scissor only where PBE band order is right, else the E.14 check. |
| 4 | done | E.18 drag masses: Ge sentence added (PBE Γ at 0.047 eV, I₃, I₄ inflated far more than GaAs, scissor keeps wrong order); Ge drag masses and electronic piece of the Ge Migdal rate on bands that pass the E.14 check. |
| 5 | done | E.15 BSE: Ge quasiparticle bands must pass the E.14 check before the BSE and the Γ–L exciton dispersion are run (also in the dispersion subsection). |
| 6 | done | E.18 new subsection "Coherent zero-phonon Migdal response" (ruling E2): Bragg picture, cross-site S_κκ′ with full S^ee_{q−G,q−G′}, q from 0.75 keV to 2q_BZ, carries nearly all of the Si Migdal rate to 1 MeV, 33 % at 2, 7 % at 3 MeV; method (matrices of the crystal rate, extra reduced p on three lines toward Γ for head/wings, AE/PAW ion vertex, Bragg weights e^{−2W(G)}), tests (boost limit 1/14.9 and plasmon median 17.4 vs 4.5 eV; diagonal form above 2q_BZ; eq:8.6-fsum-k), cost (per added p as the crystal rate), output replaces the unsized entry of tab:12-nuisances and the 17.1 band. Table row added. |
| 7 | done | E.20 ZrTe₅: central row = measured structure (Δ_D 11.8 meV; v 1.1e-3, 4.5e-4, 1.0e-3; geometric mean 7.9e-4; Λ̃ 0.191 eV; g_deg 2; ε_bg 50.5) → α̃ ≈ 0.18, Ry_D ≈ 0.10 meV, a_D ≈ 1.4e3 Å, grid ratio 27 (script log). Relaxed row (15.6 meV, α̃ 0.19) kept as the row Geilhufe et al. use, for reproducing their curve. tab:E20-dirac has both rows. |
| 8 | done | "0.55–0.62" → "0.54 to 0.61", rephrased as a fact (the factor is already in their curves; we:16-factor). |
| 9 | done | E.20 Al: film diffusive (q = 0.15 eV at y = 2.2, q𝔩_e = 0.023 at 30 nm); clean table valid at y ≤ 2.5 only for 𝔩_e ≳ 10 µm, not films (DC-41 scope in the same paragraph); Born impurity ladder in Nambu space (η G η), same ladder on density and two pair vertices, Mermin normal state at γ_rel = v_F/𝔩_e; grid clean, 1 µm, 300 nm, 30 nm; acceptance 1.008–1.091 at y ≥ 3 and 0.87/0.60/0.38/0.19 at y = 2.2 (15.3 values; DC-41's 1.01–1.09 rounded), L vanishes at 2Δ. The "small-q region not needed" sentence now holds explicitly in the clean limit only. |
| 10 | done | E.20 Holstein: refined small-Q grid for α²F_tr below a few meV (ω′⁴ law; free-electron model 1.25e4× too much weight), acoustic sum rule eq:6.2-asr checked on the interpolated vertex, λ_tr vs 0.39 (free-electron 0.32), normal-metal factor (1+λ_tr)⁻² = 0.52 quoted. Display removed in favour of eq:15.4-holstein (no notation clash ω_p² vs (ω_p^intra)² left). |
| 11 | done | E.17: CsI enters with measured 4.2 K constants (27.37, 7.93, 8.25 GPa); missing input is the cold-cell density, from the thermal-contraction calculation. PBE/PBEsol CsI tensor removed. |
| 12 | done | E.16: library f-sum held to 2 % below the band cutoff (21.6 release tolerance, we:22-fsum transfer rule), fraction stored per |q| where the spectrum ends early. The 95 % in E.14's own f-sum check (a code test, not the library) is kept. |
| 13 | done | E.16: 𝒪₂ adds four functions per version (20 in all) in the library paragraph; "Kinetic-energy response" gains the finite-q 𝒯_e rows as external rows of the Dyson solve, vertex from plane waves with (k+k′)²/8m_e of eq:8.1-rows plus PAW one-center term, q→0 limit eq:E.16-TT. |
| 14 | done | E.16 anisotropy: minima 0.13–0.22 rad in {001}, 14–107 meV below the axis, at |q| = 1.2–1.48 keV, shallower in {011}. |
| 15 | done | E.16 recast: heavy mediator unchanged (10⁻⁴, transverse ≤ 10⁻⁴), R^{−1/2} scaling, light mediator below ~3 keV undetermined, density-row ratio 0.05–0.93 at 1 keV depending on the low-energy flux treatment, which the recast must state (REF §4 / 21.5 wording). No withdrawn number. |
| 16 | done | E.14 new subsection "The phonon-assisted kinetic-energy row": S^PA_𝒯𝒯(0, m_φ) of eq:13.8-scalar via eq:13.8-MT, same gauge, vertices, Sternheimer remainder and pocket grids; PAW/AE kinetic elements (≥ 80 Ry, as E.16); control by evaluating eq:13.8-MT with the kinetic and with the crystal-potential vertex (⟨c|p²/2m|v⟩ = −⟨c|V|v⟩) to the 5 %/bin of tab:E14-params; density row at q→0 reproduces ε₂^PA; exciton envelope of E.15; enters 10.7, 13.8, 21.7. |
| 17 | done | ch08/s8-4.tex: supercell pointer app:E.14 → app:E.16 (ruling E4). |
| 18 | done | E.20-magnet: B₁, B₂ from the strain derivative of the anisotropy energy with SOC, ±0.5 % strains (as E.17), checked against ultrasonic data where they exist. |
| 19 | done | E.20-magnet: Dzyaloshinskii–Moriya constants of Cr₂O₃ by four-state mapping with SOC, for the 14.5 spin model at T ≪ T_CM. |
| 20 | done | Uniform modes with demagnetization moved into E.20-magnet, with sample shape and dipolar lattice sums as inputs (so the 14.3 pointer now resolves); Larmor and two-sublattice tests moved with them. |
| 21 | done | E.17 PIMD: error on the kinetic energy, statistical plus harmonic-difference correction, at most 0.2 % (ruling E4), tied to the ±0.2 % of 11.5 and the E.19 anchor; E.19 states the same. |
| 22 | done | E.17: TeO₂ vs CaWO₄ sentence; measured tensor is the requirement, the 4.8 % computed-tensor offset (17.6) the nuisance. |
| 23 | done | E.18 crystal rate: the same code reports the rate at each truncation of tab:12-truncations from one set of inputs. |
| 24 | done | E.14 GaAs: "PBE puts the direct gap at about 0.5 eV (app:E.18-drag)". |
| 25 | done | E.14 Fano: "a few meV from just above the conduction minimum to the Γ–L onset (about 3 meV at the onset, 0.3 eV above the minimum), 20–60 meV above the onset". |
| 26 | done | E.14 optical-limit control: measured edge at the temperature of each measurement (Si 20 K, Ge 77–80 K, GaAs at its data temperature), branch by branch with ε₂^PA resolved by branch (13.5). |
| Minor L items | done | E.16 static step: unreduced q = q_r + G to several zone momenta (ch17/ch22 promise). E.17 Ge TA "11.6 to 13.5 %" (matches E.14). E.20 optional orientation-averaged factor 5200–6400 (central) and 4800–6600 quoted from 16.1. |

## Prose items (appCE/prose.md, E.14–E.20)

- Recipe template (ruling E5): slot openers ("The quantity is / The method is / The acceptance test is / Convergence is / The cost is / The result enters / The trap is") removed or folded into causal prose throughout E.15 and E.20 (rewritten specification paragraphs) and E.16–E.19; residual "The cost is"/"The results enter" about one per section, below the E.1–E.13 rate.
- Count-teasers removed: E.14 l.3 (list in one sentence), l.40, l.46; E.16 "The cost forces two choices", "Two calculations ride…", "Three calculations would…", "Three runs…", "Three couplings have known limits"; E.17 "Two pieces remain"; E.18 "We specify four calculations" (now a list without a count, five calculations incl. the coherent one).
- E.14: gauge sentence de-figured; l.13 split; Ge paragraph split at the HSE06 failure and at "On bands that pass"; "confident and wrong" → "wrong by the inversion of Γ and L"; cite to [Fig. 1(a)]; Ge phonon past tense → present; GaAs justification sentence cut; "It" → "The Fano term"; consistency assurance on scissor/valley offsets cut.
- E.15: "how it is treated matters" cut; "The trap is near Γ" → causal sentence; 90-word model-chain sentence split; truncation-label phrasing.
- E.16: l.9 paragraph split ("Storing the full matrix is impossible"); "free diagnostic" → "check that costs nothing"; fragment "Directions: …" rewritten; pitfall list in the relativistic subsection rewritten as cause and consequence; titles "Static screening with lattice relaxation", "Kinetic-energy response", "Cosmic-ray-boosted dark matter"; "evaluates it differently" → names the dropped factor and row.
- E.17: GaAs lattice-constant bookkeeping folded into one clause; "The run takes minutes. The magnitude…" → "its size decides which terms dominate the soft limit"; "later specifications state which they tabulate" cut; slots in charge vertex, PIMD (rewritten in the register of prose.md §5), two-phonon, dynamical Born charges; "one value of Z*" assurance cut; "The recipe is uniform" / "oxide recipe" rewritten; "They enter" → "the lifetimes enter"; "Last," cut; closing generic sentence cut; Ref. citation now names Deinzer and Strauch.
- E.18: l.3 semicolon split; "bookkeeping pitfall" frame removed and 70-word sentence split; broken parallel l.46 fixed (ph.x sentence separated); "two pitfalls err in opposite directions" removed, the two errors stated where they act; "It is accepted" → "The calculation is accepted".
- E.19: C.10 band restatement cut to one sentence with pointer; slots in l.9, 35, 44, 46, 57, 59 folded.
- E.20: rewritten specification paragraphs (problem → method → checks → cost); "Finally" dropped; Padé sentence given its consequence (real axis); "for the shells that matter" → convergence criterion shell by shell against the U spread; "implemented row" jargon → "the relaxed cell that Geilhufe et al. use in their rate"; "used for nothing else" cut; source equation → "a misprint in \cite[Eq. (3.14)]"; "re-plot" → "recalculation"; trailing spaces removed.
- Table headers harmonized (lower case; "grids and parameters", "acceptance test") in tab:E14-params and tab:E20-params; labels already in tab:E14-… form.

## Notation

NOTATION.md entry 98 appended (after 99, which the parallel reviser had appended): spellings aligned with the chapters in E.20 (upright F, D subscripts; 𝔤_I, σ_1^S, σ_n, 𝔳 in its 15.1 form, g_ion), 𝒬 in the E.16 recast, no new symbols; pre-existing E.14–E.20 gaps of check_notation listed for the App. E ledger merge.

## Numbers added or changed and their sources

- ZrTe₅ α̃ 0.1825, Ry_D 0.098 meV, a_D 1449 Å, v_D(geo) 7.91e-4, ε_bg 50.53, grid ratio 27.5 (central) and 0.19/0.14 meV/1014 Å/19.3 (relaxed): figscripts/appE/e20_zrte5_dirac.log. All other added numbers are quoted from the accepted chapters or DC-RESULTS as cited in the table above (13.5, 13.6, 13.9, 15.3, 15.4, 16.1, 12.4, 12.6 tab:12-nuisances, 17.6, 21.5, 21.6, 21.7, 11.5).

## Chapter fixes found

None needed for this pass. The pointers of 13.5 (branch-resolved ε₂^PA, Ge/GaAs edge temperatures), 14.2 (B₁, B₂), 14.3 (shape and dipolar sums in E.20-magnet), 14.5 (DM constants), 12.3 (truncations), 10.7/13.8/17.2/21.7 (phonon-assisted kinetic row), 15.1/15.3 (impurity ladder) and tab:22-calc (coherent Migdal row, Al transport tests) now resolve in the specifications. Observation for a later light pass, not a fix: 7.3/we:7-zrte5 use the relaxed ZrTe₅ row (15.6 meV) as a "ZrTe₅-like cone"; it is labelled as such and agrees with E.20's relaxed row.
