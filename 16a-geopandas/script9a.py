# scrape data for US Hwy 101 in CA-NV-WA
# CA fips = 06, OR = 41, WA = 53

import geopandas as gpd
import pandas as pd

fipsD = {'CA':'06', 'OR':'41', 'WA':'53'}

template = 'data-us_highways/tl_2020_%s_prisecroads.zip'

# --------------------------------

alt_names =  ['US Hwy 101'
              'US Hwy 101 Bus',
              'US Hwy 101 N',
              'US Hwy 101N']

def get_highway(state, hwy):
    fn = template % fipsD[state]
    df = gpd.read_file(fn)
    
    L = list()
    # note: would not allow a list of boolean as selector
    # why different this time?
    for name in alt_names:
        sub = df[df['FULLNAME'] == name]
        L.append(sub)
    us101 = pd.concat(L)    
    return us101

us101ca = get_highway(state='CA', hwy='US Hwy 101')
us101or = get_highway(state='OR', hwy='US Hwy 101')
us101wa = get_highway(state='WA', hwy='US Hwy 101')

us101 = pd.concat([us101ca,us101or,us101wa])

ofn = 'us101.shp.zip'
us101.to_file(
    filename=ofn,
    driver='ESRI Shapefile')

