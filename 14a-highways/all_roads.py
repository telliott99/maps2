import sys
import geopandas as gpd

d = sys.path[0]
parent = '/'.join(d.split('/')[:-1])
sys.path.insert(0,parent + '/scripts')
import utils

# must be run from maps2 for this to work
fn = '../data/tl_2019_us_primaryroads.zip'
df = gpd.read_file(fn)

# print(df.shape)
# (17495,5)

# a surprising variety of 'FULLNAME' 
# even for interstates

# this works for interstates but not some highways

def get_name(fullname):
    def get_digits(s):
        return [c for c in s if c in '0123456789']
    rL = reversed(fullname.split())
    for s in rL:
        sL = get_digits(s)
        if sL != []:
            return ''.join(sL)
    return 'parse error'


columns = ['LINEARID', 'FULLNAME', 'RTTYP', 
           'MTFCC', 'geometry']

def fmt(f,precision=4):   
    return str(round(f,precision))

#-----------------------------
          
def parse(df):
    row_count = df.shape[0]
    results = list()
    
    for i in range(row_count):
        item = df.loc[i]
        D = dict()
        for col in columns[:-1]:
            D[col] = item[col]
            
        # some are marked as '(Hov)'
        fullname = item['FULLNAME']
        
        if D['RTTYP'] == 'I':
            name = get_name(fullname)
            D['NUM'] = 'I-' + name   
        else:
            try:
                num = int(fullname.split()[-1])
                D['NUM'] = num       
            except:
                D['NUM'] = fullname
        
        g = item['geometry']
        D['GEOM_TYPE'] = g.geom_type
        X,Y = g.xy
        X = list(X)
        Y = list(Y)

        x1 = X[0]
        x2 = X[-1]
        y1 = Y[0]
        y2 = Y[-1]
        
        # leave this out for now
        # seg_length = utils.dist((x1,y1),(x2,y2))
        # D['LEN'] = fmt(seg_length)
             
        # here we round the values to 'precision' (4)
        
        D['X'] = [fmt(x) for x in X]
        D['Y'] = [fmt(y) for y in Y]              
        results.append(D)
    return results

L = parse(df)

def show(L):
    for D in L:
        for col in ['NUM'] + columns[:-1]:
            print(col, D[col])
        print('GEOM_TYPE',D['GEOM_TYPE'])
        pL = list()
        for x,y in zip(D['X'],D['Y']):
            pL.append(str(x) + ', ' + str(y))
        print('\n'.join(pL))
        print()

show(L)