import json
r=json.load(open('/home/ytc/Projects/bm-paer/campaign/paer/code/DC-54/results/recast.json'))
EX={'3':57.71,'4':63.03,'5':65.56,'6':67.73}
for k,v in r.items():
    if k.startswith('Si'):
        Z=v.get('Z',{})
        ev=lambda row: sum(Z[row][z]*EX[z]*1e-3/365.25 for z in '456') if Z else 0
        print(k,'I src %.3g den %.3g | Z456 ev src %.3g den/src %.4f tr/den %.4f trc/den %.4f'%(v['I']['src'],v['I']['den'],ev('src'),ev('den')/ev('src') if ev('src') else 0,ev('tr')/ev('den') if ev('den') else 0,ev('trc')/ev('den') if ev('den') else 0))
    if 'src_T' in v and k.startswith('Si') and 'light' in k: print('   cum src vs T:',[('%.0e'%a,round(b,3)) for a,b in v['src_T']][::2])
