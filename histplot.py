#!/usr/lib/python
#import matplotlib.pyplot as plt

f0 = open('LC17-1.vcf','r')
snp_dep = []
snp_qual = []
mnp_dep = []
mnp_qual = []
ins_dep = []
ins_qual = []
del_dep = []
del_qual = []
complex_dep = []
complex_qual = []
others = []
total_dep = []
total_qual = []

for i in f0:
    if not i.startswith('#'):
        j=i.split()
        if j[7].split('=')[-1] == 'snp':
            snp_qual.append(float(j[5]))
            snp_dep.append(int(j[9].split(':')[1]))
        elif j[7].split('=')[-1] == 'ins':
            ins_qual.append(float(j[5]))
            ins_dep.append(int(j[9].split(':')[1]))
        elif j[7].split('=')[-1] == 'del':
            del_qual.append(float(j[5]))
            del_dep.append(int(j[9].split(':')[1]))
        elif j[7].split('=')[-1] == 'complex':
            complex_qual.append(float(j[5]))
            complex_dep.append(int(j[9].split(':')[1]))
        elif j[7].split('=')[-1] == 'mnp':
            mnp_qual.append(float(j[5]))
            mnp_dep.append(int(j[9].split(':')[1]))
        else:
            others.append(j[7].split('=')[-1])
f0.close()
total_dep.extend(snp_dep)
total_dep.extend(mnp_dep)
total_dep.extend(ins_dep)
total_dep.extend(del_dep)
total_dep.extend(complex_dep)

total_qual.extend(snp_qual)
total_qual.extend(mnp_qual)
total_qual.extend(ins_qual)
total_qual.extend(del_qual)
total_qual.extend(complex_qual)
total_cov=sum(total_dep)/float(len(total_dep))
print 'total_dep: ' +str(sum(total_dep))
print 'total_counts: ' + str(len(total_qual))
print 'coverage: ' + str(total_cov)

snp_cov=sum(snp_dep)/float(len(snp_dep))
print 'snp_dep: ' +str(sum(snp_dep))
print 'snp_counts: ' + str(len(snp_qual))
print 'coverage: ' + str(snp_cov)

plt.figure(1)
plt.hist(total_qual,normed=1)
plt.title('Variants sites quality')
plt.xlabel('Quality')
plt.ylabel('Probability')

plt.figure(2)
plt.hist(total_dep,normed=1)
plt.title('Variants sites depth')
plt.xlabel('Depth')
plt.ylabel('Probability')
plt.show()
