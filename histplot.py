#!/usr/lib/python
import matplotlib.pyplot as plt
import freebayes_pipeline as fp

x = fp.FreebayesPipe('.')
x.getvcffilelist()
for fn in x.namelist:
    f0 = open(fn, 'r')
    snp_dep = []
    snp_qual = []
#mnp_dep = []
#mnp_qual = []
#ins_dep = []
#ins_qual = []
#del_dep = []
#del_qual = []
#complex_dep = []
#complex_qual = []
#others = []
#total_dep = []
#total_qual = []
    for i in f0:
        if not i.startswith('#'):
            j=i.split()
            if j[7].split('=')[-1] == 'snp':
                snp_qual.append(float(j[5]))
                snp_dep.append(int(j[9].split(':')[1]))
#        elif j[7].split('=')[-1] == 'ins':
#            ins_qual.append(float(j[5]))
#            ins_dep.append(int(j[9].split(':')[1]))
#        elif j[7].split('=')[-1] == 'del':
#            del_qual.append(float(j[5]))
#            del_dep.append(int(j[9].split(':')[1]))
#        elif j[7].split('=')[-1] == 'complex':
#            complex_qual.append(float(j[5]))
#            complex_dep.append(int(j[9].split(':')[1]))
#       elif j[7].split('=')[-1] == 'mnp':
#            mnp_qual.append(float(j[5]))
#            mnp_dep.append(int(j[9].split(':')[1]))
#        else:
#            others.append(j[7].split('=')[-1])
    f0.close()
#total_dep.extend(snp_dep)
#total_dep.extend(mnp_dep)
#total_dep.extend(ins_dep)
#total_dep.extend(del_dep)
#total_dep.extend(complex_dep)

#total_qual.extend(snp_qual)
#total_qual.extend(mnp_qual)
#total_qual.extend(ins_qual)
#total_qual.extend(del_qual)
#total_qual.extend(complex_qual)
#total_cov=sum(total_dep)/float(len(total_dep))
#print 'total_dep: ' +str(sum(total_dep))
#print 'total_counts: ' + str(len(total_qual))
#print 'coverage: ' + str(total_cov)

    snp_cov = sum(snp_dep)/float(len(snp_dep))
    print 'snp_total_dep: ' +str(sum(snp_dep))
    print 'snp_sites: ' + str(len(snp_qual))
    print 'snp_site_depth: ' + str(snp_cov)

    plt.figure(1)
    plt.hist(snp_qual, 600, (1, 600))
    plt.title('SNP quality')
    plt.xlabel('Quality')
    plt.ylabel('Probability')
    plt.grid()
    plt.savefig(fn.split('.')[0] + '.snp_qual.png')

    plt.figure(2)
    plt.hist(snp_dep, 100, (1, 100))
    plt.title('snp depth')
    plt.xlabel('Depth')
    plt.ylabel('Probability')
    plt.savefig(fn.split('.')[0] + '.snp_dep.png')
    plt.grid()
#    plt.show()
