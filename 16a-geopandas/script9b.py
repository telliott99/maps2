import matplotlib.pyplot as plt
import geopandas as gpd

us_data = gpd.read_file('data/gz_2010_us_040_00_5m')
us101 = gpd.read_file('data-us_highways/us101.shp.zip')

xmin,ymin,xmax,ymax = -125,32,-120,49
CA_OR_WA = us_data.cx[xmin:xmax, ymin:ymax]

# --------------------------------

fig, ax = plt.subplots(figsize=(5,5))

def albers(df):
    return df.to_crs("ESRI:102003")
    
def plot_outline(df):
    df = albers(df)
    df.boundary.plot(
        ax=ax, color='gray', linewidth=1)

plot_outline(CA_OR_WA)

# --------------------------------

albers(us101).plot(
    ax=ax, color='red', linewidth=1.5)

plt.savefig('example9.png', dpi=600)