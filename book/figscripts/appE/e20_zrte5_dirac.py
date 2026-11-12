"""App. E.20: Dirac numbers of ZrTe5 for the measured-structure row of Sect. 16.1.

Inputs (Sect. 16.1, sec:16.1-zrte5): half-gap 11.8 meV, principal velocities 1.1e-3, 4.5e-4, 1.0e-3 (units of c),
background tensor 308.4, 20.75, 126.1, g_deg = 2. The relaxed-cell row (15.6 meV; 11, 4.4, 9.1 x 1e-4) is evaluated
beside it for comparison with the earlier text. Grid spacing of a 24^3 zone grid: 1.9e-2 1/Angstrom (E.20 text).
Writes e20_zrte5_dirac.log next to this file.
"""
import math, os
alpha = 1/137.035999
hbarc = 1973.2698  # eV Angstrom
eps = (308.4, 20.75, 126.1)
eps_h = 3/sum(1/e for e in eps)
rows = {"measured structure (central)": (11.8e-3, (1.1e-3, 4.5e-4, 1.0e-3)),
        "relaxed cell (implemented)": (15.6e-3, (11e-4, 4.4e-4, 9.1e-4))}
dk = 1.9e-2
out = [f"harmonic-mean background eps_bg = {eps_h:.2f}"]
for name, (D, v) in rows.items():
    vg = (v[0]*v[1]*v[2])**(1/3)
    at = alpha/(eps_h*vg)
    Ry = D*at**2/4
    aD = 2*vg/(at*D)*hbarc  # Angstrom
    out.append(f"{name}: Delta_D = {D*1e3:.1f} meV, v_D(geo) = {vg:.3e}, alpha_tilde = {at:.4f}, "
               f"Ry_D = {Ry*1e3:.4f} meV, a_D = {aD:.4g} A, 1/a_D = {1/aD:.3e} 1/A, grid/(1/a_D) = {dk*aD:.1f}")
txt = "\n".join(out)
print(txt)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "e20_zrte5_dirac.log"), "w").write(txt + "\n")
