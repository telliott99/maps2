# python3 filter.py I-10 > I-10-full.txt

import sys

target = sys.argv[1]

fn = '../data/interstates.txt'
fh = open(fn)
data = fh.read().strip().split('\n\n')

pL = list()
for item in data:
    first,rest = item.strip().split('\n',1)
    name = first.split()[-1]
    if name == target:
        pL.append(item)
    
print('\n\n'.join(pL))