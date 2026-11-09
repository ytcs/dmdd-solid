"""Sect. 16.5: momenta and thresholds of the valley-orbit transitions 1s(A1) -> 1s(E), 1s(T2) of Si:P, and the
intravalley amplitude of 1s(A1) -> 1s(E) from the anisotropic envelope.  Prints every number of the text.

Inputs: a = 5.431 A (Sect. 3.1); conduction minima at k0 = 0.85 (2 pi/a) on the <100> axes (Sect. 3.3);
  valley-orbit lines of Si:P: A1 -> T2 11.70 meV, A1 -> E 13.01 meV (Sect. 7.4, from the levels 45.59, 33.89, 32.58 meV
  of Vinh et al., arXiv:0812.0148, Fig. 1); v_max = 2.650e-3 (Sect. 1.3);
  Kohn-Luttinger variational envelope (App. D.23) with radii r_perp = 24.3 A, r_par = 14.0 A (Sect. 7.4).
Envelope density transform: |F_j|^2 of the variational envelope is the hydrogen 1s density in the coordinates scaled by
  r_perp, r_perp, r_par, so  int |F_j|^2 e^{i q.r} = [1 + (r_perp^2 q_perp^2 + r_par^2 q_par^2)/4]^{-2},  with q_par the
  component along the axis of valley j.
Valley combinations (eq:D.23-vo, order +x, -x, +y, -y, +z, -z): A1 (1,1,1,1,1,1)/sqrt6; E (1,1,-1,-1,0,0)/2 and
  (1,1,1,1,-2,-2)/sqrt12; T2 (1,-1,0,0,0,0)/sqrt2 and partners.
"""
import itertools
import numpy as np

HBARC = 1973.2698
a = 5.431
b = 2 * np.pi * HBARC / a           # eV, 2 pi/a
k0 = 0.85
VMAX = 2.650e-3
W_T2, W_E = 11.70e-3, 13.01e-3      # eV
RP, RZ = 24.3, 14.0

print(f"2 pi/a = {b:.1f} eV; k0 = 0.85 (2 pi/a) = {k0*b:.1f} eV")
Gs = [np.array(g) for g in itertools.product(range(-3, 4), repeat=3)
      if (all(x % 2 == 0 for x in g) or all(x % 2 == 1 for x in g))]      # bcc reciprocal lattice in units 2pi/a
for name, d in (("g (opposite valleys)", np.array([2 * k0, 0, 0])), ("f (perpendicular valleys)", np.array([k0, -k0, 0]))):
    qs = sorted({round(np.linalg.norm(d + G) * b, 1) for G in Gs})
    print(f"  {name}: |k_j - k_j' + G| = " + ", ".join(f"{q/1e3:.3f}" for q in qs[:3]) + " keV (three smallest)")
    for q in qs[:2]:
        for lab, w in (("T2", W_T2), ("E", W_E)):
            m = q**2 / (2 * (q * VMAX - w))
            print(f"     q = {q/1e3:.3f} keV, A1 -> {lab} ({w*1e3:.2f} meV): lightest mass q^2/[2(q v_max - omega)] = {m/1e3:.0f} keV")


def FT(qpar, qperp):
    return (1 + (RP**2 * qperp**2 + RZ**2 * qpar**2) / (4 * HBARC**2)) ** -2


A1 = np.ones(6) / np.sqrt(6)
E1 = np.array([1, 1, -1, -1, 0, 0]) / 2
E2 = np.array([1, 1, 1, 1, -2, -2]) / np.sqrt(12)
T2 = np.array([1, -1, 0, 0, 0, 0]) / np.sqrt(2)
axes = [np.array(v) for v in ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1])]


def amps(qvec):
    q = np.linalg.norm(qvec)
    f = np.array([FT(abs(qvec @ ax), np.sqrt(max(q**2 - (qvec @ ax) ** 2, 0))) for ax in axes])
    return {"E": (E1 @ (f * A1))**2 + (E2 @ (f * A1))**2, "T2": (T2 @ (f * A1))**2, "A1": (A1 @ (f * A1))**2}


print("\nIntravalley 1s(A1) -> 1s(E), summed over the two E states, |<E|e^{iq.r}|A1>|^2:")
for dname, dirv in (("[100]", np.array([1, 0, 0])), ("[110]", np.array([1, 1, 0]) / np.sqrt(2)),
                    ("[111]", np.array([1, 1, 1]) / np.sqrt(3))):
    qs = np.linspace(1, 600, 6000)
    vals = np.array([amps(q * dirv)["E"] for q in qs])
    t2 = max(amps(q * dirv)["T2"] for q in qs[::50])
    i = np.argmax(vals)
    print(f"  q along {dname}: maximum {vals[i]:.4f} at q = {qs[i]:.0f} eV; at q = 100 eV {amps(100*dirv)['E']:.4f}; "
          f"T2 (max over q) {t2:.1e}")
qv = 100 * np.array([1, 0, 0])
print(f"  check, q = 100 eV along [100]: (2/9)(F_par - F_perp)^2 = {2/9*(FT(100,0)-FT(0,100))**2:.4f}")
print(f"  elastic |<A1|e^iqr|A1>|^2 at 100 eV [100]: {amps(qv)['A1']:.4f}")
print(f"  small q: (F_par - F_perp) ~ -(r_par^2 - r_perp^2) q^2/2 -> amplitude^2 ~ q^4; at q = 13 meV (optical) "
      f"{amps(0.013*np.array([1,0,0]))['E']:.1e}")
for qq in (100.0, 150.0):
    print(f"  lightest mass that reaches q = {qq:.0f} eV with omega = 13.01 meV: {qq**2/(2*(qq*VMAX - W_E))/1e3:.1f} keV")
