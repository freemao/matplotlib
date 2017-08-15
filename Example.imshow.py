import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator


f= open('miss_X_accuracy.txt')
xlabel = [str(int(i*100)) for i in np.arange(0, 1.01, 0.1)]
ylabel = [str(int(i*100)) for i in np.arange(0, 1.01, 0.1)[::-1]]
my_matrix = []
f.readline()
for i in f:
    j = i.split()[1:]
    k = [float(m) for m in j]
    my_matrix.append(k)
my_matrix.append([0.0]*41)
my_mrx = map(list, zip(*my_matrix))
my_mrx.reverse()
mrx = np.array(my_mrx)

fig = plt.figure(1)
ax = fig.add_subplot(111)

x = np.arange(0, 40.1, 4)

ax.set_xlabel('Missing Rate (%)')
ax.set_ylabel('Heterozygous Error Rate (%)', labelpad=0)
ax.set_xticks(x)
ax.set_yticks(x)
ax.set_xticklabels(xlabel)
ax.set_yticklabels(ylabel)

levels = MaxNLocator(nbins=15).tick_values(mrx.min(), mrx.max())
#colors_set = ['Blues', 'BuGn', 'BuPu','GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd','PuBu', 'PuBuGn','PuRd', 'Purples','RdPu','Reds','YlGn','YlGnBu','YlOrBr','YlOrRd']
cmap = plt.get_cmap('GnBu')
#cmap = plt.get_cmap('autumn')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
myheat = ax.imshow(mrx, cmap=cmap, norm=norm)
fig.colorbar(myheat)

fig.savefig('miss_X_accuracy.pdf')
