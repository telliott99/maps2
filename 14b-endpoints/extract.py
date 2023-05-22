# python3 extract.py target
# writes to 'target.txt'

import sys

d = sys.path[0]
parent = '/'.join(d.split('/')[:-1])
sys.path.insert(0,parent + '/scripts')
import utils

target = sys.argv[1]
d = '/Users/telliott/Desktop/'
fn = d + 'all_roads.txt'

with open(fn) as fh:
    data = fh.read().strip().split('\n\n')

'''
filter

for interstates like
NUM I-520
LINEARID 1104977792355
FULLNAME I- 520
RTTYP I

FULLNAME may have something like Hov
and for some reason there's a space
that's why I extracted the NUM, which isn't in original data
  
for US highways like:
NUM 101
LINEARID 1108311491594
FULLNAME US Hwy 101
RTTYP U
'''

# we want these segments to be in the same order
# as those in endpoints
# therefore we need to compute 
# seg_length = utils.dist((x1,y1),(x2,y2))

def calculate_length(seg):
    def fmt(f,precision=3):   
        return str(round(f,precision))
    sL = seg.strip().split('\n')
    # the first point is on line 7, i.e. sL[6]
    p = sL[6]
    q = sL[-1]
    seg_length = utils.dist_string_pts(p,q)
    return fmt(seg_length)
    
L = list()

if target.startswith('I'):  # it's an interstate
    for item in data:
        if item.startswith('NUM ' + target):
            length = calculate_length(item)
            L.append(item + '\n' + length)

elif target.startswith('U'):  # it's a US Hwy
    fullname = 'FULLNAME US Hwy ' + target[2:]
    for item in data:
        if item.strip().split('\n',3)[2] == fullname:
            length = calculate_length(item)
            L.append(item + '\n' + length)

def f(s):
    return float(s.strip().split()[-1])

L = sorted(L, reverse=True, key=f)

with open(target + '.txt','w') as fh:
    fh.write('\n\n'.join(L))