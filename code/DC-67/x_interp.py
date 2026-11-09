"""DC-67: error of the reader's linear x interpolation against the solver's fine grid, m1, all x of the table away from the ends.  data/x_interp_error.json"""
import json, os, sys
sys.argv = ["x"]
import numpy as np, build_library as BL
from P_casc_lib import Lib
out = {}
for mat in ("Si", "GaAs", "Al2O3", "LiF", "C", "PbSe"):
    m = BL.materials()[mat]; cfg = dict(BL.configs(m))["m1"]; r = BL.solve_cfg(m, cfg); L = Lib(mat)
    x = r["x"]; sel = np.where((x > 0.3) & (x < min(r["X"], 24) - .3))[0][::2]; d = []
    for i in sel:
        P = L.carrier("m1", x[i], "e"); n = min(P.size, r["Pe"].shape[1]); d.append(np.abs(P[:n] - r["Pe"][i, :n]).max())
    d = np.array(d); j = d.argmax()
    out[mat] = dict(max=float(d.max()), at_x=float(x[sel[j]]), median=float(np.median(d)), max_above_5=float(d[x[sel] > 5.1].max()))
print(out); json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "x_interp_error.json"), "w"), indent=1)
