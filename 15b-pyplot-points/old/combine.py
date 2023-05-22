import sys
import matplotlib.pyplot as plt

fn = '../data/I-10-full.txt'
fh = open(fn)
data = fh.read().strip().split('\n\n')

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
for t in L[:10] + L[-10:]:
    print(str(t[0]) + ',' + str(t[1]))

X = [x for (x,y) in L]
Y = [y for (x,y) in L]

plt.scatter(X,Y,
    s=1,marker='o',color='red')
ax = plt.gca()
ax.set_aspect('equal')

plt.savefig('I10.png',dpi=500)