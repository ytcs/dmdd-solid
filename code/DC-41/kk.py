"""DC-41 log-grid Kramers-Kronig and sum rules at fixed Q (Delta = 1).  Im P on Gauss panels in omega' from 2 to OM = fac*max(Q, 2), graded at omega' = 2 and at the
pair edge sqrt(Q^2 + 4); KK by subtraction of I(y): Re P(y) = (2/pi){Int w'[I(w') - I(y)]/(w'^2 - y^2) dw' + I(y) (1/2) ln|(OM^2 - y^2)/(4 - y^2)|} + AB pole term.
GRPA carries a delta function at omega_AB < 2: P~ ~ Z/(w - w_AB) - Z/(w + w_AB) (Im P~ = -pi Z delta(w - w_AB)); the bare bubble has none."""
import numpy as np
import bcs1d as b

def wgrid(Q, fac=1e3, n=12, per_oct=4):
    top = fac * max(Q, 2.0)
    e = np.sqrt(Q * Q + 4)
    pts = [2.0, top, e]
    pts += [2.0 + 2.0 ** (-j) * 2.0 for j in range(0, 40)]
    pts += [e + sg * (e - 2.0) * 2.0 ** (-j) for sg in (-1, 1) for j in range(1, 40)]
    pts += list(2.0 * 2.0 ** (np.arange(0, 34 * per_oct) / per_oct))
    bb = np.array(sorted(x for x in set(pts) if 2.0 <= x <= top))
    xg, wg = b.gl(n)
    a, c = bb[:-1, None], bb[1:, None]
    return (0.5 * (c - a) * xg + 0.5 * (c + a)).ravel(), (0.5 * (c - a) * wg).ravel(), top

class Spec:
    def __init__(self, Q, fac=1e3, n=12, per_oct=4, nq=12, refine=1):
        self.Q = Q; self.kw = dict(n=nq, refine=refine)
        self.w, self.wt, self.top = wgrid(Q, fac, n, per_oct)
        ib = np.empty(self.w.size); ig = np.empty(self.w.size)
        for i, y in enumerate(self.w):
            p, g = b.Pg(y, Q, **self.kw)
            ib[i], ig[i] = p.imag, g.imag
        self.I = dict(bare=ib, grpa=ig)
        ab = b.ab_pole(Q, **self.kw)
        self.wab, self.Z = (ab[0], ab[1]) if ab[0] is not None else (None, 0.0)
        self.dab = ab[2] if ab[0] is not None else None

    def kk(self, y, kind="grpa"):
        I = self.I[kind]; Iy = (b.Pg(y, self.Q, **self.kw)[0 if kind == "bare" else 1]).imag if y > 2 else 0.0
        w = self.w
        d = w * w - y * y
        r = (2 / np.pi) * (self.wt @ (w * (I - Iy) / d) + Iy * 0.5 * np.log(abs((self.top ** 2 - y * y) / (4 - y * y))))
        if kind == "grpa" and self.Z:
            r += 2 * self.Z * self.wab / (y * y - self.wab ** 2)
        return r

    def sums(self, kind="grpa"):
        """f-sum ratio  Int w(-Im P)dw / (pi Q^2/6);  compressibility (2/pi) Int (-Im P)/w dw  (normal = 1), pole included."""
        I = self.I[kind]; w = self.w
        f = self.wt @ (w * (-I)) + (np.pi * self.Z * self.wab if kind == "grpa" and self.Z else 0.0)
        c = (2 / np.pi) * (self.wt @ (-I / w)) + (2 * self.Z / self.wab if kind == "grpa" and self.Z else 0.0)
        return f / (np.pi * self.Q ** 2 / 6), c
