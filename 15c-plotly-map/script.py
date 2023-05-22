import geopandas as gpd
import plotly.graph_objects as go

# must unzip first
fn = '../data/gz_2010_us_040_00_5m'
df = gpd.read_file(fn)
N = len(df)

skip = ['Alaska','Hawaii','Puerto Rico']
west = ['California', 'Oregon','Washington',
        'Arizona','Nevada','Idaho','Utah',
        'New Mexico','Colorado','Montana',
        'Colorado','Wyoming']
        

L = list()
for i in range(1,N):
    item = df.loc[i]
    name = item['NAME']
    
    if not name in west:
        continue
    geo = item['geometry']
        
    if geo.geom_type == 'Polygon':
        coords = list(
            geo.exterior.coords)
    
    # in contrast to the docs
    # correct polygon is the *last* one
    if geo.geom_type == 'MultiPolygon':
        coords = list(
            geo.geoms[-1].exterior.coords)  
             
    L.append(coords)

#---------

def poly_for_coords(cL):
    X = list()
    Y = list()
    for point in cL:
        X.append(point[0])
        Y.append(point[1])
    poly = go.Scatter(
        x=X,y=Y,   
        line={'color':'gray', 
              'width':1.5},
        mode='lines',
        fill='none')        
    return poly

routes = list()
for s in ['I-5','I-10']:
    X = list()
    Y = list()
    fn = s + '.txt'
    
    with open(fn) as fh:
        data = fh.read().strip().split('\n')
        for line in data:
            x,y = line.strip().split(',')
            x,y = float(x),float(y)
            X.append(x)
            Y.append(y)
    routes.append((X,Y))

#---------

fig = go.Figure()

for X,Y in routes:
    route = go.Scatter(
        #x=X,y=Y,line=
            #{'width':4,'color':'red'})
         x=X,y=Y,
         mode='markers')
         #marker_color='red')
    fig.add_trace(route)

for f in L:
    p = poly_for_coords(f)
    fig.add_trace(p)
    
fig.update_layout(
    width = 1500,height = 1500,
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1.2,
    ),
    showlegend=False
)

fig.show()
