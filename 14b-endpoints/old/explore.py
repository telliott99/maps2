# python3 explore.py > I-10-segments.txt

import sys

def find_script_path():
    d = sys.path[0]
    parent = '/'.join(d.split('/')[:-1])
    sys.path.insert(0,parent + '/scripts')

find_script_path()
from utils import dist

d = '/Users/telliott/Library/CloudStorage/'
d += 'Dropbox/Github/maps2/14a-highways/'
fn = 'endpoints.txt'
fh = open(d + fn)
data = fh.read().strip().split('\n\n')

#-----

# print(len(data))
# 9414

def fmt(n):
    return round(n,4)
    
def gather_coords(target):
    rL = list()
    for item in data:
        lines = item.strip().split('\n')
        name = lines[0].split()[-1]
                
        if name == target:
        
            # number of original points last line
            count = lines.pop()

            # coords, each a tuple of x,y
            x1,y1 = lines[-2].strip().split(',')
            x1,y1 = float(x1),float(y1)
            x2,y2 = lines[-1].strip().split(',')
            x2,y2 = float(x2),float(y2)
            t = [x1,y1,x2,y2,count]
            rL.append(t)
    return rL

L = gather_coords('I-10')

for i,(x1,y1,x2,y2,count) in enumerate(L):
    print(i)    
    print([fmt(n) for n in (x1,y1)])
    print([fmt(n) for n in (x2,y2)])
    print(count)    
    print(fmt(dist((x1,y1),(x2,y2))))
    print()