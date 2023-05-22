# takes a target that's already been extracted

# python3 endpoints.py target
# writes to 'target.txt'

import sys
target = sys.argv[1]


fn = target + '.txt'

with open(fn) as fh:
    data = fh.read().strip().split('\n\n')

pL = list()
for i,item in enumerate(data):
    rows = item.strip().split('\n')
    
    # LEN is last line
    points = rows[6:-1]
    
    sL = [str(i),points[0],points[-1],
        str(len(points)), rows[-1]]
    pL.append('\n'.join(sL))

with open (target + '-ends.txt', 'w') as fh:
    fh.write('\n\n'.join(pL))

    