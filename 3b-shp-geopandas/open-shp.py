# opening a shapefile with geopandas

import sys
import geopandas as gpd

# US state outlines

d = '/Users/telliott/Library/CloudStorage/Dropbox/Github/maps2/data/'
fn = 'gz_2010_us_040_00_20m'
df = gpd.read_file(d+fn)

print(df.loc[0:5,'NAME'])
print()

#-----

SEL = df['NAME'] == 'Colorado'
colorado = df.loc[SEL]
print(colorado.columns)
print()

#-----

from shapely.geometry import mapping

D = mapping(colorado['geometry'])

'''
`D['features']` gives

```
[{'id': '42', 
  'type': 'Feature', 
  'properties': {}, 
  'geometry': {'type': 'Polygon', 
               'coordinates': (((-109.059962, 38.499987),
                                (-109.05122383101701, 39.36667754958629),
                                ...
                                (-109.059962, 38.499987)),)
              }
  'bbox': (-109.060062, 36.992426, -102.041876, 41.003073)
 }
]
'''

for feature in D['features']:
    L = feature['geometry']['coordinates']
    for poly in L[:5]:
        for t in poly[:5]:
            print(t)
        print()

'''
> python3 open-shp.py
0                 Arizona
1                Arkansas
2              California
3                Colorado
4             Connecticut
5    District of Columbia
Name: NAME, dtype: object

Index(['GEO_ID', 'STATE', 'NAME', 'LSAD', 'CENSUSAREA', 'geometry'], dtype='object')

(-107.317794057388, 41.00295740871)
(-107.000606, 41.003443999999995)
(-106.85777193794601, 41.0030816553615)
(-106.453859, 41.002057)
(-106.43956299999999, 41.001978)

>
'''