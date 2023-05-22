import sys, json
from state_data import fips_dict
fips_dict[''] = '*'

d = '/Users/telliott/Library/CloudStorage/Dropbox/Github/maps2/data/'
fn = 'gz_2010_us_outline_20m.json'
fh = open(d + fn,'r')

obj = json.load(fh)
fL = obj['features']

# nothing but LineStrings
for e in fL:
    kind = e['properties']['TYPE']
    right = e['properties']['R_STATEFP']
    left = e['properties']['L_STATEFP']
    
    r = fips_dict[right]
    l = fips_dict[left]
    if r in ['AK','HI','PR']:
        continue
    
    print(','.join([kind,r,l]))

    cL = e['geometry']['coordinates']
    for long,lat in cL:
        print('%.10f, %.10f' % (long,lat))
    print('')


 