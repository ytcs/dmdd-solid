import numpy as np, svgtools as t, collections
S='/tmp/claude-1000/-home-ytc-Projects-breakthrough-maths/42e1e9d0-2a1c-462d-8f88-358ed2914b1d/scratchpad/f/'
ps=t.load(S+'Summary_scattering.svg')
ys=collections.Counter();xs=collections.Counter()
for p in ps:
    q=p['pts']
    if len(q)==2:
        dx,dy=np.abs(q[1]-q[0])
        if dy<1e-3 and .5<dx<15: ys[(round(q[0,1],2),round(dx,1))]+=1
        if dx<1e-3 and .5<dy<15: xs[(round(q[0,0],2),round(dy,1))]+=1
print('x',sorted(k for k in xs)[:30]);print('y',sorted(k for k in ys)[:24])
print([(p['stroke'],p['dash'],len(p['pts'])) for p in ps if p['stroke'] and len(p['pts'])>15])
