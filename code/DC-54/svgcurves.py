"""Parse vector curves out of pdftocairo SVGs of published figures (no pixel digitisation)."""
import re, numpy as np

def _nums(s): return [float(x) for x in re.findall(r'-?\d+\.?\d*(?:e-?\d+)?', s)]

def paths(svg):
    s = open(svg).read()
    out = []
    for p in re.findall(r'<path ([^>]*?)/?>', s):
        st = re.search(r'stroke="([^"]*)"', p); d = re.search(r'(?:^| )d="([^"]*)"', p)
        if not st or st.group(1) == 'none' or not d: continue
        da = re.search(r'stroke-dasharray="([^"]*)"', p)
        tr = re.search(r'transform="matrix\(([^)]*)\)"', p)
        sw = re.search(r'stroke-width="([^"]*)"', p)
        pts = []; subs = []
        for cmd, arg in re.findall(r'([MLCZ])([^MLCZ]*)', d.group(1)):
            a = _nums(arg)
            if cmd == 'M':
                if pts: subs.append(np.array(pts)); pts = []
                pts.append(a[:2])
            elif cmd == 'L': pts.append(a[:2])
            elif cmd == 'C': pts.append(a[4:6])
        if pts: subs.append(np.array(pts))
        M = np.array(_nums(tr.group(1))) if tr else None
        for q in subs:
            if M is not None:
                x = M[0]*q[:, 0]+M[2]*q[:, 1]+M[4]; y = M[1]*q[:, 0]+M[3]*q[:, 1]+M[5]
                q = np.c_[x, y]
            out.append(dict(color=st.group(1), dash=da.group(1) if da else None,
                            sw=float(sw.group(1)) if sw else 1., pts=q))
    return out

def ticks(ps, color='rgb(0%, 0%, 0%)'):
    """Return short straight black segments as (x0,y0,x1,y1)."""
    t = []
    for p in ps:
        if p['color'] == color and len(p['pts']) == 2:
            t.append(p['pts'].ravel())
    return np.array(t)
