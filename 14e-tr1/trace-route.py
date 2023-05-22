import sys

target = sys.argv[1]

v = len(sys.argv) > 2
# yes, globals are bad, v for verbose output

with open(target + '-ends.txt') as fh:
    L = fh.read().strip().split('\n\n')

# alter path to find utils
d = sys.path[0]
parent = '/'.join(d.split('/')[:-1])
sys.path.insert(0,parent + '/scripts')
import utils

# ----------------------------

def preprocess(L):
    rL = list()
    for e in L:
        sL  = e.split('\n',3)   
        rL.append(sL[:3])
    return rL

# contains index, p1, p2

L = preprocess(L)

# ----------------------------

# list of segments found
# points are all in forward order

# a global var
results = list()

# distance function for string versions of points

# dist_string_pts returns miles
def close_enough(p1,p2,proximity=1):
    return utils.dist_string_pts(p1,p2) < proximity
    
# make bbox around p1,p2, is p inside?

def is_in_bbox(p,bbox):
    x,y = utils.get_floats(p)
    (x1,y1),(x2,y2) = bbox
    if v:  print('is_in_bbox', p, bbox)
    if x1 < x < x2:
        if v:  print('x is in')
        return True
    if y1 < y < y2:
        if v:  print('y is in')
        return True
    return False
    
def reverse_segment(segment):
    i,p,q = segment
    return i + 'r', q, p

# ============================

# decided to split things into round 1 and rest

# choose the starting segment by hand

if target == 'I-5':
    first = ['4',
             '-117.0297, 32.5424',	
             '-117.5937, 33.3965']

    first_rev = ['54',
             '-122.757, 49.0021',
             '-122.3648, 48.6451']

if target == 'I-10':
    first = ['112r',
             '-118.4905, 34.0125', 
             '-118.214, 34.0551']
             
# changing things
if target == 'I-80':
    first = ['229',
             '-122.4058, 37.7703',	
             '-122.3902, 37.7867' ]

if target == 'I-84':
    first = ['11',
             '-122.6607, 45.5255',	
             '-121.9221, 45.6451']

# ============================

results = [first]

skip_list = { }
#'I-5': ['340','341'],
#'I-84': ['262'] }

# we use target to get the data
# and a particular segment to start and orient also

def find_first_segment(t,v=v):
    # we search from largest to smallest
    # return the first match
    
    for segment in L:
        i,p,q = segment
        if p == t or close_enough(p,t):
            results.append(segment)
            return
            
        elif q == t or close_enough(q,t):
            results.append(
                reverse_segment(segment))    
            return
            
    return 'failure'
        
# ============================

# when a "wrong" choice is made,
# see what other choices available

def print_state_and_exit(seen_before):
    print('print_state')
    pL = list()
    # filter out ineligible segments
    for e in L:
        idx = e[0]
        if idx.endswith('r'):
            idx = idx[:-1]
        if not idx in seen_before:
            pL.append(e)
    print('actives:')
    print('\n\n'.join(pL))
    sys.exit()

# ============================

# extension phase

def search(v=False):
    if v:  print('search started')

    # previous segment guaranteed in fwd order
    prev = results[-1]
    i,s,t = prev

    if v:  print('previous segment:')
    if v:  
        print(str(i))
        print('s:  ' + s)
        print('t:  ' + t)
    
    seen_before = [e[0] for e in results]
        
    # we search from largest to smallest
    # so return the first match
    
    for segment in L:
    
        # print('segment no.', i)
        j, p, q = segment
        
        if target in skip_list:
            if j in skip_list[target]:
                continue

        # note:  this should eliminate prev
        if j in seen_before:
            continue
        elif j + 'r' in seen_before:
            continue
                      
        # so the points we are thinking about are
        # in the candidate segment:  p and q
        
        # and in the prev accepted segment s and t
        # t is the same as prev[2]
        
        # test for close matches
        t_eq_p = p == t or close_enough(p,t)
        t_eq_q = q == t or close_enough(q,t)

       # neither of the points is a close match
        if not (t_eq_p or t_eq_q):
            continue
                        
        # if this is precisely the same segment, skip
        # i should already be in seen_before
        # so we should not get here
        if prev == segment:
            if v:  print('duplicate')
            seen_before.append(j)
            continue
                
        # or reversed
        if s == q and t == p:
            if v:  print('reverse')
            seen_before.append(j)
            continue

        # perhaps just a real close match
        if t_eq_q and close_enough(p,s):
            if v:  print('close forward match')
            seen_before.append(j)
            continue
            
        # close match but exactly reversed
        if t_eq_p and close_enough(q,s):
            if v:  print('close reverse match')
            seen_before.append(j)
            continue
        
        # Looks like we found an extension:
        if v:  print('found')
        if v:  print('\n'.join(segment))
        if v:  print()
        
        # stop at wrong choice
        bad = 'xyz'
        if j == bad:
            print_state_and_exit(seen_before)

        if t_eq_q:
            # reverse the orientation of the saved piece
            segment = [j + 'r', q, p]
                
        results.append(segment)
        
        if v:  print('-' * 20)
        seen_before.append(j)        
        return
        
    if v:  print('search completed')
    return 'stop'
            
def get_next(v=False):
    result_code = search(v=v)
    return result_code
    
# -------------------------------


# we also want to terminate gracefully when end isn't found
# while not close_enough(results[-1][2], end):

counter = 0
while True:
    result_code = get_next(v=v)
    if result_code == 'stop':
        break
    
    counter += 1
    if counter > 100:
        print('runaway process')
        break

print()
pL = ['\t'.join(item) for item in results]
print('\n'.join(pL))
