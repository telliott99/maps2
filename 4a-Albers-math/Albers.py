import sys

def find_scripts():
    d = sys.path[0]
    parent = '/'.join(d.split('/')[:-1])
    sys.path.insert(0,parent + '/scripts')

find_scripts()

from math import sin, cos, radians, log

# reference latitudes
LAT1 = 29.5 # phi_1
LAT2 = 45.5 # phi_2

# map center
LON0 = -96.0 # lambda_0
LAT0 =  23.0 # phi_0

# sphericity
R = 1.0

# ellipticity
a = 6378206.4
e = 0.0822719
e_sq = e**2

#-----------------

def sine(theta):
    return sin(radians(theta))

def cosine(theta):
    return cos(radians(theta))
    
#-----------------

def get_spherical_constants():
    n = (sine(LAT1) + sine(LAT2))/2
    C = (cosine(LAT1))**2
    C += 2 * n * sine(LAT1)
    RHO0 = (C - 2 * n * sine(LAT0))**0.5
    RHO0 = (R/n)*RHO0
    return n,C,RHO0
    
def getM(lat):
    num = cosine(lat)
    den = 1 - (e**2)*(sine(lat)**2)
    den = den**0.5
    return num/den
    
def getQ(lat):
    S = sine(lat)
    eS = e*S  
    g1 = (1-e_sq)
    g2 = S/(1-eS**2)
    g3 = 1.0/(2*e)
    g4 = log((1 - eS)/(1 + eS))
    return g1 * (g2 - (g3 * g4))

# broken out separately only so that we can print them in test()
def get_ellipsoid_constants1():
    m1 = getM(LAT1)
    m2 = getM(LAT2)
    q0 = getQ(LAT0)
    q1 = getQ(LAT1)
    q2 = getQ(LAT2)
    return m1,m2,q0,q1,q2

def get_ellipsoid_constants2():
    m1,m2,q0,q1,q2 = get_ellipsoid_constants1()
    n = (m1**2 - m2**2)/(q2-q1)
    C = m1**2 + n*q1
    RHO0 = a * (C - n*q0)**0.5
    RHO0 /= n
    return n,C,RHO0

def test():
    print('spherical constants')
    n,C,RHO0 = get_spherical_constants()
    print('n',n)
    print('C',C)
    print('RHO0',RHO0)
    print()
    
    print('ellipsoid constants')
    m1,m2,q0,q1,q2 = get_ellipsoid_constants1()
    print('m1',m1)
    print('m2',m2)
    print('q0',q0)
    print('q1',q1)
    print('q2',q2)
    
    n,C,RHO0 = get_ellipsoid_constants2()
    print()
    print('n',n)
    print('C',C)
    print('RHO0',RHO0)
    print()

test()

#-----------------

def convert_spherical(lon,lat):
    n,C,RHO0 = get_spherical_constants()
    
    RHO = (C - 2 * n * sine(lat))**0.5
    RHO = (R/n)*RHO
    print('RHO', RHO)
    
    THETA = n * (lon - LON0)
    print('THETA', THETA)
    
    x = RHO * sine(THETA)
    y = RHO0 - RHO * cosine(THETA)
    return (x,y)
    
def convert_ellipsoid(lon,lat):
    n,C,RHO0 = get_ellipsoid_constants2()
    
    # we need q for each latitude
    q = getQ(lat)
    print('q',q)
    
    RHO = a * (C - n*q)**0.5
    RHO /= n
    print('RHO', RHO)

    THETA = n * (lon - LON0)
    print('THETA', THETA)
    
    x = RHO * sine(THETA)
    y = RHO0 - RHO * cosine(THETA)
    return (x,y)
   
if __name__ == "__main__":
    
    try:
        LON = float(sys.argv[1])
        LAT = float(sys.argv[2])
    except:
        print('using default longitude latitude')
        LON = LON0
        LAT = LAT0

    print('LON LAT')
    print(LON,LAT)
    
    print()
    print('spherical')
    x,y = convert_spherical(LON,LAT)
    print('x',x)
    print('y',y)
    print()
    
    print('ellipsoid')
    x,y = convert_ellipsoid(LON,LAT)
    print('x',x)
    print('y',y)  

'''
> p3 Albers_spherical.py           
n 0.6028370046288244
C 1.351221325417899
RHO0 1.5562263294996075

using default longitude latitude
-96.0 23.0
RHO 1.5562263294996075
THETA 0.0
x 0.0
y 0.0
> p3 Albers_spherical.py -75.0 35.0
n 0.6028370046288244
C 1.351221325417899
RHO0 1.5562263294996075

-75.0 35.0
RHO 1.3473026077172072
THETA 12.659577097205313
x 0.2952720069922353
y 0.24167744921848078
>
'''