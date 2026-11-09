"""Check of Worked example 8.6 (nucleon-number coupling of GaAs) against the full DFPT phonons (gaas11_2.py).
WE 8.6 uses zone-center eigenvectors with site phases exp(i q.tau); here the eigenvectors at the actual q are used.
a_N(q) = sqrt(mu) x sum_kappa A_kappa exp(i q.tau) qhat.e*_{kappa LO}(q)/sqrt(M_kappa), so that
S_NN = pi q^2 |a_N|^2/(mu Omega omega_LO) delta(omega - omega_LO) as in WE 8.6. Mean nucleon numbers per atom: natural mass
times the A/M of WE 8.6 (1.001072 per u for Ga, 1.001046 per u for As). [111] of WE 8.6 (As at +a(1,1,1)/4) is [-1,1,1] in the
axes of the force-constant file (As at a(-1,1,1)/4); [100] is the same in both.
Energy-weighted optical share: |a_N|^2 M_cell/(mu |A-amplitude of LA|^2), LA amplitude sum_kappa A_kappa e^{iq.tau} qhat.e*/sqrt(M)
times sqrt(M_cell). Mass-density coupling (A_kappa = M_kappa): isolates the center-of-mass motion of the LO mode, nonzero along
[111] (longitudinal strain with shear, internal strain) and ~0 along [100].
"""
import numpy as np
import gaas11_2 as G
import pol11_2 as P

mu = G.M_GA * G.M_AS / (G.M_GA + G.M_AS)
Mc = G.M_GA + G.M_AS
QUNIT = 2 * np.pi / G.A_ANG * P.HBARC
for name, d in (("[111] (bond)", [-1, 1, 1]), ("[100]", [1, 0, 0])):
    d = np.array(d, float) / np.linalg.norm(d)
    ql = np.array([0.02, 1.0, 13.7, 100.0])
    qs = ql[:, None] * d / QUNIT
    w, e = G.run_matdyn(qs, "we86_" + ("111" if "111" in name else "100"))
    amp = G.nucleon_amplitude(qs, w, e)
    for i, q in enumerate(ql):
        aN = abs(np.sqrt(mu) * amp[i, 5])
        aLA = abs(amp[i, 2]) * np.sqrt(Mc)
        # WE 8.6 form: zone-center eigenvectors, tau_As - tau_Ga = a(1,1,1)/4 in its axes ([111] -> (1,1,1)/sqrt3 there)
        dtau = np.array([1, 1, 1]) * G.A_ANG / 4
        qdir = np.array([1, 1, 1]) / np.sqrt(3) if "111" in name else np.array([1, 0, 0])
        qv = qdir * q / P.HBARC
        aG = abs(mu * (1.001072 - 1.001046 * np.exp(1j * qv @ dtau)))
        aM = abs(np.sqrt(mu) * G.nucleon_amplitude(qs[i:i+1], w[i:i+1], e[i:i+1], A=(G.M_GA, G.M_AS))[0, 5])
        print(f"{name:13s} q = {q:6.2f} eV: |a_N| full {aN:.4g} (zone-center eigenvectors {aG:.4g}); LA vertex {aLA:.2f};"
              f" optical share {aN**2*Mc/(mu*aLA**2):.2e}; mass-density coupling {aM:.4g}")
