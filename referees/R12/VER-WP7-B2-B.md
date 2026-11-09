# R12 verification VER-WP7-B2-B (referee B of R11) on returns/R12/WP7-B2-v2.md

Scope: the R12 revision checked against my R11 report (referees/R11/REF-WP7-B2-B.md). Same isolation: I read no other referee, state/ or R12 returns.
Checks: code/WP7-B2-v2/checks.py re-run, 39/39 PASS (≈ 6 s). I also ran my own sympy checks: the one-mode LO residue (C21) and the SMM S⁺ branch.
No papers were re-fetched: none of the revised claims depends on a full-text quotation that I had not already verified in R11.

## Verdict per R11 item
| R11 item | Verdict | Evidence |
|---|---|---|
| 1 / R1: A4 source-defect wording, acoustic condition, R̃ zero-field | RESOLVED | §1: condition is c_νv ≪ 1; R̃ is stated at zero macroscopic field; footnote 2 is credited. ×0.47 is dropped and replaced by the LO residue Z_κ − Z*_κ/ε_∞ (B2.1.4). My own symbolic check confirms Res_LO R_OO = [a + b(1 − 1/ε_∞)]² and Res_TO = 0 in the one-mode model. GaAs d = −0.00117 vs −0.00346 gives a ratio ≈ 0.115. The 46% sensitivity per 10% of Z*/ε_∞ reproduces. "Fig. 2 UNRESOLVED" is honest |
| 2 / R2: scope of (R3) | RESOLVED | §2.1: exact for mass-independent vertices, leading order in σ_M/M̄ otherwise; isotope-class D_κ named as the cure |
| 2a / R3: isotope B−L channel | RESOLVED | (a) Novelty UNRESOLVED, "[E for novelty]". (b) EM-like decomposition (B2.4.1); additivity argued from distinct final states. (c) Mass-weighted 1.88×10⁻⁴ (C4a). I re-derived (B2.4.2) from (B2.2.1): Γ = πg²σ_wD/(2Ω_at). I recomputed the C27 ratio as ≈ 5×10² from the stated inputs. That ratio rests on a room-T 76 meV two-phonon α applied at 50 meV [UNVERIFIED], which the return declares in gap 2. Acceptable as [E] |
| 2b / R4: C^{IR} ∝ ω² | RESOLVED | Withdrawn. A + Bω² with cond-mat/0604205 [ABS]; the incoherent estimate is identified as the A term; the spec now asks for a charge model that reproduces A |
| 3: disordered-solid S, gap 6 | RESOLVED (stood) | Wording narrowed to S_self plus S_dist at n_ph = 1; n_ph ≥ 2 stays [D, sketch] |
| 4 / R5: §10(iii) | RESOLVED | Eq. (12) derived (C22, matches my R11 derivation). 2W ≈ 1.3×10⁻¹¹ (C25). B2-L4 now matches §3 (DWBA phase drops out below σ_crit; reflection above). The f(v) caveat is added (C26: 1.29 at v = 1.2×10⁻³) |
| 5: solid He | RESOLVED (stood) | Unchanged apart from the τ string |
| 6 / R6: Larmor citation, ω_L, m_s | RESOLVED | Cited as standard ESR (citations [UNVERIFIED], acceptable). ω_Lar and 𝔰_net used throughout; m_s kept only as species mass. Grep finds no stray ω_L or m_s use |
| 7 / R7: Ni²⁺ λ_S | RESOLVED | λ_S ≈ 1 for quenched 3d, bracket 0.83 (C24); g_J − 1 restricted to J multiplets in §5 and §6 |
| 8 / R8: SMM S⁺ branch | RESOLVED | (B2.7.2) now has both branches. I checked the S⁺ term δ(ω + D(2m+1) + ω_Z) with weight S(S+1) − m(m+1). Metastable line D(2S−1) − ω_Z, weight 2S (C16 extended) |
| 9 / R9: X10 medium factor | RESOLVED | 1 + (3/2)ω_p²/ω². Using 12 bound-below-ω electrons (ω_p ≈ 29 eV) gives +1.2×10⁻³; my R11 valence-only figure was +4×10⁻⁴. Both are [E]; the choice is stated |
| 10 / R10: D2 source caveats | RESOLVED | Footnote 2 (≲ 15%), "dislocated nucleus" and "spontaneous and immediate" are all credited |
| 11: D5 | RESOLVED (stood) | Orientation independence made explicit in (M) |
| 12: source-defect list | RESOLVED | Rigid-ion vertex and κ retracted as defects; the Eq. (49) residual ×3 is stated; IF-B2-9 updated |
| R11 notation (λ mode label, γ_I/γ_λ) | RESOLVED | Modes ν, λ^I_κ, ϑ^{BL}_I, Γ^{ph}_ν; grep finds no leftover γ_λ, e_Iλ or ω_λ |
| R12 τ strings | RESOLVED (with a new minor item N1) | `src=data` replaces `X=data`; `ref=exact(Larmor)` dropped; T in every τ; IF-B2-10 and -11 added |
| §B LIMITS rows (B2-L1, -L3, -L4, -L7, -L8, -L9, -L10) | RESOLVED | Each row carries the requested wording |
| §G check-script points (C4a, C15, C16, C10 identity) | RESOLVED | C4a mass-weighted; C15 checks sign and size; C16 covers both wells; C23 states uᵀ[J,D]u in general |

## New issues in changed sections
- **N1 (minor, NEW ERROR, wording).** The §3 τ uses `K=1ph-coh` for the elastic n_ph = 0 term. CONVENTIONS §11 has no elastic K value; "1ph-coh" mislabels a zero-phonon coherent term. Use `K=-` with a note `n_ph=0`, or propose an `el` value in the IF table.
  The §8 τ uses `nB=-` for an X-sector nuclear-coupling channel. That needs a one-line justification: the acceleration form is BO-order-free, (B2.8.1), so `-` is defensible but should be said.
- **N2 (cosmetic).** The checks.py docstring says "C21–C30 new", but the header and the count (39 = 31 + 8) mean C21–C28.
- **No new physics error found.** I checked (B2.1.4) (LO residue), (B2.4.1)–(B2.4.2), (B2.7.0) (one-phonon j_T vertex; the prefactor i√N(eZ*/M)√(Mω/2) agrees with CONVENTIONS §5 up to the stated phase) and (B2.7.2).
  The statement that u × P is the antisymmetric O(q·u) part of the current is correct. The claim that magnetic-dipole DM makes single phonons through j_T is consistent with WP2-v3 (7.2).
- **Caveat (not an error).** The 0.11 GaAs ratio compares with "the source's structure" reconstructed as Z − Q/ε_∞ from its Eqs. (40)–(41). The return rightly makes it an order-of-magnitude statement with type-M nuisances on Z*/ε_∞, and lists gap 11.

## Summary
All 12 verdict rows, R1–R12 and the LIMITS and check-script points: RESOLVED. One minor new wording/τ error (N1) and one cosmetic docstring mismatch (N2). No new physics error.
