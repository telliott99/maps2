# python3 filter.py I-10

import sys

target = sys.argv[1]

desktop = '/Users/telliott/Desktop/'
fn = desktop + 'all_roads.txt'

fh = open(fn)
data = fh.read().strip().split('\n\n')
pL = list()

for segment in data:
    line1,rest = segment.split('\n',1)
    name = line1.split()[-1]
    if name == target:
        pL.append(segment)

with open(desktop + target + '.txt', 'w') as fh:
    fh.write('\n\n'.join(pL))