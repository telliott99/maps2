import json

fn = '../data_Celeste/counties.sm.json'

try:
    fh = open(fn,'r')
    counties = json.load(fh)
  
except UnicodeDecodeError:
    print('handling UnicodeDecodeError')
    fh = open(fn,'rb')
    s = fh.read()
    
    data = s.decode('ISO-8859-1')
    tmp = open('.tmp','w')
    tmp.write(data)
    tmp.close()
    
    fh = open('.tmp','r')
    counties = json.load(fh)

print(counties['type'])
features = counties['features']
print()

autauga = features[0]
# print(autauga)

D = autauga['properties']
for k in D:
    print(k, D[k])

# geometry is a top-level key
D2 = autauga['geometry']
print(D2['type'])
L = D2['coordinates']

# nested-two deep
for point in L[0]:
    print(point)

# delete all but the first two features

counties['features'] = counties['features'][:2]

fn = 'two-counties.json'
json_object = json.dumps(counties, indent=2)
with open(fn, 'w') as of:
    of.write(json_object)




