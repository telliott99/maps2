import sys

def find_script_path():
    d = sys.path[0]
    parent = '/'.join(d.split('/')[:-1])
    sys.path.insert(0,parent + '/scripts')

find_script_path()

# method 1

from ellipsoid import project

# note LAT first
proj = project(23,-96,v=True)
print(proj(35,-75))

'''
> python3 projection.py
p1: 29.5
p2: 45.5
q0: 0.7767080
q1: 0.9792529
q2: 1.4201080
m1: 0.8710708
m2: 0.7021191
n:  0.6029035
C:  1.3491594
R0: 9929079.6
q:  1.1410831
R:  8602328.3
t:  12.6609735
(1885472.726709384, 1535925.006017996)
>'''

# method 2

from Albers import convert_ellipsoid
print(convert_ellipsoid(-75,35))

'''
..
ellipsoid constants
m1 0.871070821796458
m2 0.7021191443812667
q0 0.7767080179035076
q1 0.9792529106872788
q2 1.420108011659379

n 0.6029035007021405
C 1.3491593845112777
RHO0 9929079.56149474

q 1.1410830527980151
RHO 8602328.226835338
THETA 12.660973514744951
(1885472.7282290398, 1535924.9987982716)
'''

# note a slight difference 
# I suspect this is due to rounding
# but then why don't my two scripts match?