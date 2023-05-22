import geopandas as gpd

fn = '../1b-json-ex/two-counties.json'
df = gpd.read_file(fn)

item = df.loc[1]
print(item)
print()

print(df.columns)
print()

SEL = df['NAME'] == 'Autauga'
sub = df[SEL]

geo = sub.loc[0]['geometry']

# geo is a 'Polygon' object
# print(help(geo))

# access to coords
# exterior is the first linear ring in a polygon
print(list(geo.exterior.coords))

print()
# can give svg object
print(geo.svg())


'''
> python3 geopandas-example.py
GEO_ID                                           0500000US01009
STATE                                                        01
COUNTY                                                      009
NAME                                                     Blount
LSAD                                                     County
CENSUSAREA                                              644.776
geometry      POLYGON ((-86.577799 33.765316, -86.759144 33....
Name: 1, dtype: object

Index(['GEO_ID', 'STATE', 'COUNTY', 'NAME', 'LSAD', 'CENSUSAREA', 'geometry'], dtype='object')

[(-86.496774, 32.344437), (-86.717897, 32.402814), (-86.814912, 32.340803), (-86.890581, 32.502974), (-86.917595, 32.664169), (-86.71339, 32.661732), (-86.714219, 32.705694), (-86.413116, 32.707386), (-86.411172, 32.409937), (-86.496774, 32.344437)]

<path fill-rule="evenodd" fill="#66cc99" stroke="#555555" stroke-width="2.0" opacity="0.6" d="M -86.496774,32.344437 L -86.717897,32.402814 L -86.814912,32.340803 L -86.890581,32.502974 L -86.917595,32.664169 L -86.71339,32.661732 L -86.714219,32.705694 L -86.413116,32.707386 L -86.411172,32.409937 L -86.496774,32.344437 z" />
>
'''