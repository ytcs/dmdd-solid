"""Assemble properties.csv (WP8-U-table column format) from values.json (written by hand from the logged outputs)."""
import json, csv
V=json.load(open('values.json'))
hdr=['material','label','group','verdict','property','value','unit','tag','source','locator','note']
LAB={'Si':('Si (diamond)','elemental','SURVIVOR'),'Ge':('Ge (diamond)','elemental','SURVIVOR')}
with open('properties.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(hdr)
    for r in V:
        l=LAB[r['material']]
        w.writerow([r['material'],l[0],l[1],l[2],r['property'],r['value'],r['unit'],'CALC',
                    'COMP-PH: QE 7.6 PBE, SG15 ONCV '+r.get('pp','1.2'),r['locator'],r['note']])
print(len(V),'rows')
