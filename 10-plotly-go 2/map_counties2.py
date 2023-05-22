import sys

def find_util():
    d = sys.path[0]
    parent = '/'.join(d.split('/')[:-1])
    sys.path.insert(0,parent + '/scripts')

find_util()

import plotly.graph_objects as go
from ellipsoid import project
from state_data import fips_dict, abbrev_dict

abbrev = 'CA'
requested_state = abbrev_dict[abbrev]

# center of projection:
proj = project(33,-86)

fn = '../Celeste/counties.lg.geo.txt'
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

fig.update_layout(
    width = 1200,
    height = 1200,
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1.0,
    )
)

fig.show()


