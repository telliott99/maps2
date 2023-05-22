import matplotlib.pyplot as plt
import numpy as np
# plots the endpoints and shows direction

fn = 'I-10-ends.txt'
fh = open(fn)
data = fh.read().strip().split('\n\n')

#data = sorted(data,reverse=True,
    #key=lambda x: x.split()[-1])

L = list()
i = 0  # can't use n b/c filtering

for group in data:
    t = group.strip().split('\n')
    n = t.pop(0)
    
    p1 = t[0][1:-1].split(',')    
    x1 = float(p1[0])

    p2 = t[1][1:-1].split(',')    
    x2 = float(p2[0])

    #filter
    dx = x2 - x1
    if dx < 0:
        dx *= -1
    if dx < 0.5:
        continue

    X = [x1,x2]
    Y = [i,i]
    i += 1
            
    # make going E darker
    if x2 > x1:
        col = '0.7'
    else:
        col = '0.3'
    plt.plot(X,Y,
        markersize=5,marker='o',color=col)
    
ax = plt.gca()
start, end = ax.get_ylim()
ax.yaxis.set_ticks(np.arange(0, 50, 5))

plt.savefig('I10-first-50.png',dpi=500)