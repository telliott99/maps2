def albers(df):
    return df.to_crs("ESRI:102003")

def process(e):
    def get_digits(s):
        return [c for c in s if c in '0123456789']
    rL = reversed(e.split())
    for s in rL:
        sL = get_digits(s)
        if s != []:
            num = ''.join(sL)
            return len(num) <= 2
    return False

import geopandas as gpd
import matplotlib.pyplot as plt

fn = 'data/tl_2019_us_primaryroads'
df = gpd.read_file(fn)

states = gpd.read_file('data/gz_2010_us_040_00_5m')

xmin,ymin,xmax,ymax = -124.9,25.02,-66.74,49.1
df = df.cx[xmin:xmax, ymin:ymax]
us48 = states.cx[xmin:xmax, ymin:ymax]

df = df[df['RTTYP'] == 'I']
SEL = [process(e) for e in list(df['FULLNAME'])]
majors = df[SEL]
    
fig, ax = plt.subplots(figsize=(7,7))
albers(us48).boundary.plot(
    ax=ax, color='gray', linewidth=0.5)
albers(majors).plot(
    ax=ax, color='green', linewidth=0.75)

plt.savefig('example6.png', dpi=300)

