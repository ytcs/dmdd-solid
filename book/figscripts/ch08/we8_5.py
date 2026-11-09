"""Numbers of Sect. 8.3, Worked example 8.5 (Ward identity of a harmonic chain) and the boost factor of the
Ward subsection. Natural units, energies in eV.
Inputs: longitudinal [100] chain of silicon planes of Sect. 5.2 (plane spacing d = a/4 = 1.358 A, nearest-plane
model maximum frequency 2 sqrt(K/M) = omega_{0+} = 64.1 meV, sound speed 6.61 km/s there); M = 26.16 GeV (natural
Si mass, Sect. 5.6); hbar c = 1973.27 eV A; hbar = 6.582119569e-16 eV s; m_e = 510998.95 eV.
Checks the chain amplitudes of the worked example symbolically at random k, q (one- and two-phonon Ward identity).
"""
import numpy as np

hbarc, hbar, M, me = 1973.27, 6.582119569e-16, 26.16e9, 510998.95
d, wmax = 1.358, 0.0641
q = 1000.0 / hbarc                      # 1 keV in 1/A
wq = wmax * abs(np.sin(q * d / 2))
print(f"q = 1 keV = {q:.3f} 1/A, qd = {q*d:.3f}, omega_q = {wq*1e3:.1f} meV")
print(f"sound speed c = d sqrt(K/M) = {d*1e-10*(wmax/2)/hbar/1e3:.2f} km/s")
print(f"q^2/(2 M omega_q) = {1e6/(2*M)/wq:.2e}  (q = 1 keV in eV)")
print(f"(m_e/M_Si)^2 = {(me/M)**2:.2e}")

# Ward identity checks in units M = 1, d = 1, K = 1 (amplitudes per the worked example, N = 1 normalization)
rng = np.random.default_rng(1)
w = lambda k: 2 * abs(np.sin(k / 2))
for _ in range(3):
    qq, k = rng.uniform(0.05, 1.0), rng.uniform(0.3, 2.5)
    w1, w2, w0 = w(k), w(qq - k), w(qq)
    n1, g1 = 1j * qq * (1 / (2 * w0))**0.5, 1j * (w0 / 2)**0.5
    n2 = -qq**2 / (2 * (w1 * w2)**0.5)
    g2 = -qq * (w1 + w2) / (2 * (w1 * w2)**0.5)
    flux1 = 4j * np.sin(qq / 2)**2 * (1 / (2 * w0))**0.5
    print(f"q={qq:.3f}: one-phonon M w n - q g = {abs(w0*n1 - qq*g1):.1e}; two-phonon {abs((w1+w2)*n2 - qq*g2):.1e}; "
          f"w g - flux = {abs(w0*g1 - flux1):.1e}")
