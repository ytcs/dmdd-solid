"""O4 symbolic checks (theory only, < 10 s). Run: python3 -I sympy_checks.py
S1  Gamma/(x^2+Gamma^2/4) = 2 pi delta(x) + Gamma fp(1/x^2) + O(Gamma^2)   (Gaussian test function, exact)
S2  Lorentzian kernel L_Gamma = delta + (Gamma/2pi) fp(1/x^2) + O(Gamma^2)  (the tail that T3a double counts)
S3  Re (x+i s)^-2 -> fp(1/x^2) as s->0 (implementable X+ regulator, s independent of Gamma)
S4  semicircle KK: d ReSigma/dw = -(1/2pi) fp int Gamma(w')/(w'-w)^2  (Ward identity behind Z)"""
import sympy as sp
x, a, s, w = sp.symbols('x a s w', real=True)
G = sp.symbols('Gamma', positive=True)
def rep(n, ok, r=""): print(f"{'PASS' if ok else 'FAIL'}  {n:70s} {r}")

# S1: int e^{-x^2} Gamma/(x^2+Gamma^2/4) dx = 2 pi e^{a^2} erfc(a), a = Gamma/2 (closed form, verified numerically)
closed = 2*sp.pi*sp.exp(G**2/4)*sp.erfc(G/2)
num = sp.Integral(sp.exp(-x**2)*G/(x**2+G**2/4), (x, -sp.oo, sp.oo)).subs(G, sp.Rational(3, 10)).evalf(20)
rep("S1a closed form of Lorentzian x Gaussian", abs(num-closed.subs(G, sp.Rational(3, 10)).evalf(20)) < 1e-15)
ser = sp.series(closed, G, 0, 3).removeO()
fp_gauss = -2*sp.sqrt(sp.pi)                       # fp int e^{-x^2}/x^2 = -2 sqrt(pi)
fp_check = sp.integrate((sp.exp(-x**2)-1)/x**2, (x, -sp.oo, sp.oo))   # fp of 1/x^2 over R kills the constant
rep("S1b fp int e^{-x^2}/x^2 dx = -2 sqrt(pi)", sp.simplify(fp_check-fp_gauss) == 0)
rep("S1c order-Gamma coefficient = fp term", sp.simplify(ser.coeff(G, 1)-fp_gauss) == 0, f"series={sp.expand(ser)}")
rep("S1d remainder is O(Gamma^2) (coefficient pi/2 * phi-curvature)", sp.simplify(ser.coeff(G, 2)-sp.pi/2) == 0)
# S2: same with weight 1/(2pi)
rep("S2  L_Gamma = delta + (Gamma/2pi) fp 1/x^2 + O(Gamma^2)", sp.simplify(sp.expand(ser/(2*sp.pi)).coeff(G, 1)-fp_gauss/(2*sp.pi)) == 0)
# S3: int e^{-x^2} Re (x+is)^-2 dx -> -2 sqrt(pi)
f3 = sp.re(1/(x+sp.I*s)**2).simplify()
val = [sp.Integral(sp.exp(-x**2)*f3.subs(s, sv), (x, -sp.oo, sp.oo)).evalf(15) for sv in (sp.Rational(1, 10), sp.Rational(1, 100))]
rep("S3  Re(x+is)^-2 -> fp(1/x^2), error O(s)", abs(val[0]-fp_gauss.evalf()) > 5*abs(val[1]-fp_gauss.evalf()),
    f"s=0.1:{float(val[0]):.4f} s=0.01:{float(val[1]):.4f} target {float(fp_gauss):.4f}")
# S4: semicircle, W=1, g=1: Gamma(w) = 4 sqrt(1-w^2), ReSigma = 2 w inside band -> d/dw = 2
wp = sp.symbols('wp', real=True); w0 = sp.Rational(1, 5)
Gam = 4*sp.sqrt(1-wp**2)
F0, F1 = Gam.subs(wp, w0), sp.diff(Gam, wp).subs(wp, w0)
reg = sp.Integral((Gam-F0-F1*(wp-w0))/(wp-w0)**2, (wp, -1, 1)).evalf(25)
fp = reg + F0*(-1/(1-w0)-1/(w0+1)) + F1*sp.log((1-w0)/(w0+1))
rep("S4  dReSigma/dw = -(1/2pi) fp int Gamma/(w'-w)^2  (= 2)", abs(sp.N(-fp/(2*sp.pi))-2) < 1e-12, f"{sp.N(-fp/(2*sp.pi), 15)}")
