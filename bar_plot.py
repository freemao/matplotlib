#!/usr/lib/python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

n = 3
L_variant = (42356, 46004, 274582)
R_variant = (31060, 52114, 246004)
L_datasize = (7.4, 9.4, 9.2)
R_datasize = (8.2, 7, 7.2)

plt.figure(1)
index = np.arange(n)
width = 0.35
bar1 = plt.bar(index+0.15, L_variant, width=0.35, color='g', label='Leaf')
bar2 = plt.bar(index+0.15+width, R_variant,width=0.35, color='r', label='Root')
plt.title('Variants result')
plt.text(1,200000, 'this is text i added')
plt.annotate('local max', xy=(2, 150000), xytext=(2, 180000),
             arrowprops=dict(facecolor='red', shrink=0.1))
plt.xlabel('Species')
plt.ylabel('Number of variants')

plt.xticks(index+width, ('C17', 'C18', 'CS173'))
plt.legend(loc='best')
plt.savefig('first.png')

plt.figure(2)
index = np.arange(n)
width = 0.35
bar1 = plt.bar(index+0.15, L_datasize, width=0.35, color='g', label='Leaf')
bar2 = plt.bar(index+0.15+width, R_datasize,
               width=0.35, color='r', label='Root')
plt.annotate('annotation test', xy=(2, 5),
             xytext=(2, 6), arrowprops=dict(facecolor='red', shrink=0.05))
plt.title('Data_size result')
plt.xlabel('Species')
plt.ylabel('data_size(G)')

plt.xticks(index+width, ('C17', 'C18', 'CS173'))
plt.legend(loc='best')
plt.savefig('second.pdf')

plt.figure(3)
bar1 = plt.bar(index+0.15, L_variant, width=0.7, color='g',label='Leaf')
bar2 = plt.bar(index+0.15, R_variant, width=0.7, color='r', bottom=L_variant,
label='Root')
plt.title('Variants result')
plt.xlabel('species')
plt.ylabel('Number of variants')

plt.xticks(index+0.5, ('C17', 'C18', 'CS173'))
plt.legend(loc='best')
plt.savefig('third.png')

plt.grid(True)
#plt.show()

