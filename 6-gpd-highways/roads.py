import geopandas as gpd

d = '/Users/telliott/Library/CloudStorage/Dropbox/Github/maps2/data/'
fn = 'tl_2016_us_primaryroads.zip'

df = gpd.read_file(d+fn)

item = df.loc[3]
print(item)
print()

geo = item['geometry']
X,Y = geo.xy
print(list(X)[:3])
print()

SEL = df['RTTYP'] == 'I'
sub = df[SEL]
print(sub[['RTTYP','FULLNAME']])  # double brackets