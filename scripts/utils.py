from math import cos, radians

def preprocess(L):
    rL = list()
    for e in L:
        sL  = e.split('\n',3)   
        rL.append(sL[:3])
    return rL

def euclidean_dist(dx,dy):
    return (dx**2 + dy**2)**0.5

def dist(p1,p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx < 0:  dx = -dx
    if dy < 0:  dy = -dy
    
    # 1 deg of LAT is 69 miles
    # 1 deg of LON depends on LAT
    # for LAT = 38, cos 38 = 0.788
    
    dy = dy * 69
    dx = dx * 69 * (cos(radians(p1[1])))
    
    # miles
    return euclidean_dist(dx,dy)

def get_floats(s):
    # coords, each a tuple of x,y
    x,y = s.split(',')
    x,y = float(x),float(y)
    return (x,y)
    
def dist_string_pts(p1,p2):
    x1,y1 = get_floats(p1)
    x2,y2 = get_floats(p2)
    return dist((x1,y1),(x2,y2))

def close_enough(p1,p2,proximity=1):
    return dist_string_pts(p1,p2) < proximity

def reverse_segment(segment):
    i,p,q = segment
    if i. endswith('r'): 
        i = i[:-1]
    else:  
        i += 'r'
    return [i,q,p]

def bbox(p1,p2):
    x1,y1 = get_floats(p1)
    x2,y2 = get_floats(p2)
    if x1 > x2:
        x1,x2 = x2,x1
    if y1 > y2:
        y1,y2 = y2,y1
    return ((x1,y1),(x2,y2))
