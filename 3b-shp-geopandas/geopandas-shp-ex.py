import geopandas as gpd

d = '../data/gz_2010_us_040_00_20m'
fn = d + '/gz_2010_us_040_00_20m.shp'
df = gpd.read_file(fn)

print(df.columns)

# notice no quotes
print(df.NAME.head())
print()

SEL = df['NAME'] == 'Colorado'
sub = df[SEL]

print(sub.NAME)
print()

# geo is a GeoSeries object
geo = sub['geometry']
# with a coordinate reference system
print(geo.crs)
print()

from shapely.geometry import mapping
D = mapping(geo)

first = D['features'][0]
# fips:  prints 3 for Colorado
print(first['id'])
print(first['geometry']['coordinates'][0][:2])

'''
> python3 geopandas-shp-ex.py
Index(['GEO_ID', 'STATE', 'NAME', 'LSAD', 'CENSUSAREA', 'geometry'], dtype='object')
0        Arizona
1       Arkansas
2     California
3       Colorado
4    Connecticut
Name: NAME, dtype: object

3    Colorado
Name: NAME, dtype: object

EPSG:4269

3
((-107.317794057388, 41.00295740871), (-107.000606, 41.003443999999995))
> 
'''