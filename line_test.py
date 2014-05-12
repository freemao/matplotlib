#!/usr/lib/python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

f0 = open('test.txt', 'r')
mo_list = []
so_list = []
for i in f0:
    m = i.split()[1]
    mo_list.append(m)
    s = i.split()[2]
    so_list.append(s)
print mo_list, len(mo_list)
print so_list, len(so_list)

plt.figure(1)
plt.plot(mo_list, so_list, 'ro')
plt.title('Chr1.group1')
plt.xlabel('Molokai')
plt.ylabel('Sorghum')
plt.savefig('test.pdf')
plt.show()
