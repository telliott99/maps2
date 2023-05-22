import sys

target = sys.argv[1]

# give the number of the first segment to use
first = sys.argv[2]

# yes, globals are bad, v for verbose output
v = False

with open('../data-interstates/' + target + '-ends.txt') as fh:
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

# find the first segment based on index passed in

# global var
# results = list()

# locate the first segment based on CL arg first
results = list()

# segments in L don't have r and not orientated
rev = first.endswith('r')

if rev:
    j = first[:-1]
else:
    j = first

for segment in L:
    i,p,q = segment
    if i == j:
        if rev:
            segment = utils.reverse_segment(segment) 
        results.append(segment)
        break
        
# ----------------------------
    
# extension

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
        t_eq_p = p == t or utils.close_enough(p,t)
        t_eq_q = q == t or utils.close_enough(q,t)

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
        if t_eq_q and utils.close_enough(p,s):
            if v:  print('close forward match')
            seen_before.append(j)
            continue
            
        # close match but exactly reversed
        if t_eq_p and utils.close_enough(q,s):
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
            # reverse the orientation of the piece to save
            segment = utils.reverse_segment(segment)
                
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

# we want to terminate gracefully when end isn't found
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

pL = ['\t'.join(item) for item in results]
print('\n'.join(pL))