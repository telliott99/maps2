import sys
import matplotlib.pyplot as plt

# arg is like '10'
target = sys.argv[1]
target = 'I-' + target

fn = '/Users/telliott/Desktop/interstates.txt'
fh = open(fn)
data = fh.read().strip().split('\n\n')

pL = list()
for item in data:
    first,rest = item.strip().split('\n',1)
    name = first.split()[-1]
    if name == target:
        pL.append(item)

# -----

# rename
data = pL

L = list()
precision = 2

for group in data:
    for item in group.strip().split('\n'):
        if item[0] == '-':
            x,y = item.strip().split(',')
            x,y = float(x),float(y)
            x = round(x,precision)
            y = round(y,precision)
            L.append((x,y))

# look for dupe points
L = list(set(L))
L = sorted(L)

print(len(L))
    
fh = open(target + '.txt', 'w')
pL = [str(t[0]) + ',' + str(t[1]) for t in L]
fh.write('\n'.join(pL))

# -----

X = [x for (x,y) in L]
Y = [y for (x,y) in L]


plt.scatter(X,Y,
    s=1,marker='o',color='red')
ax = plt.gca()
ax.set_aspect('equal')

plt.savefig(target + '.png',dpi=500)

