# App B editor notes
## Rulings after the accuracy review (accuracy.md)
- **B1:** fix every generator bug in gen_B1.py and rerun. Do not hand-edit B-1.tex. The bugs:
  - the decimal-vs-section filter;
  - section numbers left in symbol cells;
  - clash notes left in meanings;
  - primes, \sum, bold vectors, upright i, upright Si/PV/fp/ZPR, text/math splits, K_η units, φ→\varphi for the CDW phase;
  - the h row (drop H_Hub,0) and the v_min "≥ 0".
  
  Correct the five first uses in NOTATION.md (Φ^(n) 5.1, ℓ₀ 5.6, T_d 5.4, r_cl 14.4, Γ₀ 16.8). Shorten the "First use" header so it does not wrap (e.g. "Sect.").
- **B2:** two renames in the tex, with the NOTATION rows updated:
  - kink width → d_kink (wherever the kink width is used; it meets d_k in C.20);
  - the Lindhard bracket f₁+if₂ in 10.3 → f^L₁ + i f^L₂, or a single f^L as accuracy.md proposes. Grep every use in Ch10, App C and App E.
- **B3:** the nine NOTATION errors (θ_s, Γ₀, σ_ω, Θ_D, ℓ₀, z_p, 𝗍, CDW φ, the missing E.16 v₀ row) and the duplicates (keep the rows accuracy.md names; ω_max l.1204/1484). Remove E_el from the duplicate list. The remaining clashes are acceptable local reuse: gen_B1.py prints both meanings with a scope note ("in Ch. N").
- **B4:** in B.2, make σ_F italic F as in 10.9; reword the spin-factor sentence to agree with eq:A.7-spin. In B.3, PT = parity (inversion) × time reversal; HSE and PBE name the functional (Heyd–Scuseria–Ernzerhof hybrid; Perdew–Burke–Ernzerhof GGA). SOC is not a defect.
- **Sequencing:** run after the Ch9 ledger merge has finished editing NOTATION.md.
