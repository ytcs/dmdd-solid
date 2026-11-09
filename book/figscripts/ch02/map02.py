"""Chapter map of Chap. 2 (fig:2-map): from Fermi's golden rule to the thermal golden rule and the dynamic
structure factor, with the absorption of a bosonic field and the second-order rule as branches.
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. Output: tex/figures/ch02/map02.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 5.2
XR, WR = 6.4, 3.55
P = 1.45
y = lambda i: 0.15 + (5 - i) * P
N = {
    "fgr": dict(x=X, y=y(0), w=W, title="Fermi's golden rule",
                body=r"$2\pi|\langle f|H'|i\rangle|^2\delta(E_f - E_i)$ into a continuum", tag="Sect. 2.1"),
    "born": dict(x=X, y=y(1), w=W, title="Born cross-section",
                 body=r"free electron or nucleus; heavy and light mediators", tag="Sect. 2.2"),
    "bound": dict(x=X, y=y(2), w=W, title="Rate off a bound target",
                  body=r"form factor $f_{i\to f}(\mathbf{q})$; hydrogen; Helm form factor",
                  tag="Sect. 2.2; Limit Check 2.1"),
    "sq": dict(x=X, y=y(3), w=W, title="Second quantization",
               body=r"density operator $n_e(\mathbf{q})$; Coulomb Hamiltonian of a solid", tag="Sect. 2.3"),
    "th": dict(x=X, y=y(4), w=W, title="Thermal golden rule",
               body=r"Gibbs state; $S(\mathbf{q},\omega)$; detailed balance; electron gas", tag="Sect. 2.5"),
    "crys": dict(x=X, y=y(5), w=W, shade="ext", title="Electrons and nuclei of a crystal",
                 body=r"the states inside $S(\mathbf{q},\omega)$", tag="Chaps. 3-5"),
    "abs": dict(x=XR, y=y(1) - 0.1, w=WR, shade="light", title="Absorption",
                body="rate of a bosonic field fixed" "\n" "by its energy density", tag="Sect. 2.1", h=1.15),
    "so": dict(x=XR, y=y(2) - 0.1, w=WR, shade="light", title="Second-order golden rule",
               body="intermediate states; time" "\n" "orderings; finite width", tag="Sect. 2.4", h=1.15),
}
E = [
    ("fgr", "born", "first Born approximation"),
    ("born", "bound", "bind the target: add the form factor"),
    ("bound", "sq", "many identical electrons"),
    ("sq", "th", "thermal initial states"),
    ("th", "crys", "periodic potential, moving nuclei", dict(ls="--")),
    ("fgr", "abs", "harmonic\nperturbation", dict(start="right", end="top", conn="arc3,rad=-0.3", side="end")),
    ("bound", "so", "first order\nforbidden", dict(start="right", end="left", side="above", dy=0.0)),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch02"), size=(5.4, 5.0), height=y(0) + 1.05)
