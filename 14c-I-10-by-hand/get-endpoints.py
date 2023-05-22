# python3 get-endpoints.py I-10

import sys

d = sys.path[0]
parent = '/'.join(d.split('/')[:-1])
sys.path.insert(0,parent + '/scripts')
from utils import dist, get_floats

target = sys.argv[1]
desktop = '/Users/telliott/Desktop/'
fn = desktop + target + '.txt'
fh = open(fn)

data = fh.read().strip().split('\n\n')
pL = list()

def fmt(f,precision=3):
    return str(round(f,precision))

for i,segment in enumerate(data):
    lines = segment.split('\n')
    points = lines[6:]
    first = points[0]
    last = points[-1]
    N = str(len(points))
    
    x1,y1 = get_floats(first)
    x2,y2 = get_floats(last)
    delta = fmt(dist((x1,y1),(x2,y2)))

    x1 = fmt(x1)
    y1 = fmt(y1)
    x2 = fmt(x2)
    y2 = fmt(y2)
    sL = [str(i),x1 + ', ' + y1,
          x2 + ', ' + y2, N, delta]
    pL.append('\n'.join(sL))

with open(desktop + target + '-endpoints.txt', 'w') as fh:
    fh.write('\n\n'.join(pL))