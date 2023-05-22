import sys

def find_util():
    d = sys.path[0]
    parent = '/'.join(d.split('/')[:-1])
    sys.path.insert(0,parent + '/scripts')

find_util()

import os, json
import plotly.graph_objects as go

home = '/Users/telliott'
base = home + '/Dropbox/Github/maps'
sys.path.insert(0, base + '/data_geo')

from ellipsoid import project

p0 = 23
l0 = -96
#print('p0: %.1f' % p0)
#print('l0: %.1f' % l0)
f = project(p0,l0)

#--------------------------------

fn = 'x.txt'
with open(fn) as fh:
    data = fh.read().strip().split('\n\n')
    
pL = list()
for item in data:
    sL = item.strip().split('\n')
    title = sL[0]
    rest = sL[1:]
    X = []
    Y = []
    for line in rest:
        values = line.strip().split(',')
        long = float(values[0])
        lat = float(values[1])
        x,y = f(lat,long)
        X.append(x)
        Y.append(y)
    pL.append((title, X, Y))
    

fig = go.Figure()

for title,X,Y in pL:
    poly = go.Scatter(
        x=X,y=Y,
        line={'color':'black', 'width':2},
        #marker={'size':5, 'color':'blue'},
        #mode='lines+markers')
        mode = 'lines')
            
    fig.add_trace(poly)
    
fig.update_layout(
    width = 1500,
    height = 1500,
    yaxis = dict(
        scaleanchor = "x",
        scaleratio = 1.0),
    showlegend = False
    )

fig.show()



'''



multi = route["features"][0]
vL = multi['geometry']['coordinates'][0]
# vL = [f(t) for t in vL]

X = [t[0] for t in vL]
Y = [t[1] for t in vL]

'''