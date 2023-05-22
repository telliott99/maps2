import sys, os
fn = sys.argv[1]

base = os.environ.get('covid_base')
sys.path.insert(0,base)

import myutil.ugeo as ugeo
import myutil.ustrings as ustrings

abbrev = sys.argv[2]
requested_state = ustrings.abbrev_to_state[abbrev]

import plotly.graph_objects as go
from ellipsoid import project

# center of projection:
proj = project(33,-86)

with open(fn) as fh:
    data = fh.read().strip().split('\n\n')

fig = go.Figure()

for e in data:
    county, state, fips, rest = e.strip().split('\n',3)
    
    if requested_state != state:
        continue
              
    rest = rest.strip().split('\n')
    X = []
    Y = []
    
    for line in rest:
        print(line)
        lon, lat = line.strip().split('\t')
        lat = float(lat)
        lon = float(lon)
        x,y = proj(lat,lon)
        X.append(x)
        Y.append(y)
    
    col = 'salmon'
    if county == 'Mobile':
        col = 'red'
        
    poly = go.Scatter(
        name = county,
        x=X,y=Y,
        line={'color':'black', 'width':3},
        mode='lines',
        fill='toself', 
        fillcolor='salmon',
        showlegend=False)
        
    fig.add_trace(poly)

print(len(fig['data']))
print(fig)

fig.update_layout(
    width = 1200,
    height = 1200,
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1.0,
    )
)


fig.show()


