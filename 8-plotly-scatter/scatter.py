import json
import plotly.graph_objects as go

fn = '../data/geojson-counties-fips.json'
with open(fn,'r') as fh:
    counties = json.load(fh)

cL = ['salmon','blue']

def poly_for_feature(f):
    vL = f['geometry']['coordinates'][0]
    X = list()
    Y = list()
    for t in vL:
        X.append(t[0])
        Y.append(t[1])

    poly = go.Scatter(
        x=X,y=Y,
        line={'color':'black', 'width':2},
        #marker={'size':10, 'color':'red'},
        mode='lines',
        #mode='lines+markers',
        fill='toself', 
        fillcolor='blue')
        
    return poly

#-----

fig = go.Figure()

# 01 is the state code for Alabama
# 12 is the state code for Alabama
fL = [f for f in counties['features'] if f['id'].startswith('12')]

for f in fL:
    p = poly_for_feature(f)
    fig.add_trace(p)
    
fig.update_layout(
    width = 500,
    height = 500,
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1.2,
    )
)

fig.show()
