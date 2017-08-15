#!/usr/lib/python
import numpy as np
import matplotlib.pyplot as plt

f = open('miss.txt')
sensitivity = []
specificity = []
accuracy = []
for i in f:
    j = i.split()
    sensitivity.append(float(j[1]))
    specificity.append(float(j[2]))
    accuracy.append(float(j[3]))

x = np.arange(0, 1.0, 0.025)
print len(x)

x_label = [str(i) for i in np.arange(0,101,10)]
y_label = [str(i)+'%' for i in np.arange(0,101,20)]
#x_label[0]='0'
y_label.insert(-2, '95%')

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_xlabel('Missing Rate (%)')
#ax.set_ylabel('(%)', labelpad=2)
#ax.xaxis.set_major_locator(plt.MultipleLocator(4))
#ax.xaxis.set_minor_locator(plt.MultipleLocator(2))
#ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
#xtickNames = plt.setp(ax, xticklabels=x_label)
#ytickNames = plt.setp(ax, yticklabels=y_label)
#plt.setp(xtickNames, rotation=45, fontsize=8)
#plt.setp(xtickNames)


ax.set_xticks(np.arange(0,1.01,0.1))
yticks = list(np.arange(0,1.01,0.2))
yticks.insert(-2,0.95)
ax.set_yticks(yticks)
ax.set_xticklabels(x_label)
ax.set_yticklabels(y_label)

sen_line = ax.plot(x, sensitivity, color='#1b9e77', marker='p', alpha=1,markeredgecolor='#1b9e77',mew=1,markerfacecolor='#1b9e77',linestyle=':',markersize =8,label='Sensitivity', linewidth=2)
spe_line = ax.plot(x, specificity, color='#d95f02', marker ='s',alpha=0.9,markeredgecolor ='#d95f02',mew=1,markerfacecolor='#d95f02', linestyle='-',markersize =7,label='Specificity', linewidth=2)

acc_line = ax.plot(x, accuracy, color='#e7298a', marker='o',alpha=0.9,markeredgecolor ='#e7298a',mew=1,markerfacecolor='#e7298a', linestyle='--',markersize =8,label='Accuracy', linewidth=2)
ninefive_line = ax.plot([0,1],[0.95,0.95] ,color='k', linestyle=':', linewidth=1)
#ax.set_xlim(0,0.95)
ax.set_ylim(0,1.02)
ax.legend()
fig.savefig('only_miss.pdf')
