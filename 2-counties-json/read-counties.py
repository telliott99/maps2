import sys, json

fn = 'geojson-counties-fips.json'
fn = '../data/' + fn

with open(d+fn,'r') as fh:
    counties = json.load(fh)
    
#----

from state_data import fips_dict

#----

def extract_poly_coord(L):
    rL = list()
    for polygon in L:
        sL = list()
        # [[x,y],[x,y] ...
        for (x,y) in polygon:
            string = (str(x) + ' ' + str(y))
            sL.append(string)
        rL.append('\n'.join(sL))
    return rL

#----

features = counties['features']
for f in features:
    properties = f['properties']
    name = properties['NAME']
    fips = properties['GEO_ID'][-5:] 
    state_code = properties['STATE']
    state = fips_dict[state_code]
    print(name)
    print(state)
    print(fips)
       
    geometry = f['geometry']
    geojson_type = geometry['type']
    coord = geometry['coordinates']
    
    if geojson_type == 'MultiPolygon':
        for element in coord:
            poly_list = extract_poly_coord(element)
            for poly in poly_list:
                print(poly)
                print()
    
    elif geojson_type == 'Polygon':
        poly_list = extract_poly_coord(coord)
        for poly in poly_list:
            print(poly)
        print()
    
    else:
        print('error:  ' + geojson_type)
        1/0
        
    print()
