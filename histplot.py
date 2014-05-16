#!/usr/lib/python
import matplotlib.pyplot as plt
import freebayes_pipeline as fp
import matplotlib.patches as patches

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
    print 'snp_total_dep: ' + str(sum(snp_dep))
    print 'snp_sites: ' + str(len(snp_qual))
    print 'snp_site_depth: ' + str(snp_cov)

    fit = 0
    total = 0
    for x, y in zip(snp_dep, snp_qual):
        total += 1
        if x > 10 and y > 30 :
            fit += 1
    fitality = '%.2f'%(float(fit)/total)

    plt.figure(1)
    plt.hist(snp_qual, 600, (1, 600), normed=1)
    plt.title(fn.split('.')[0] + ' SNP quality')
    plt.xlabel('Quality')
    plt.ylabel('Probability')
    plt.grid()
    plt.savefig(fn.split('.')[0] + '.snp_qual.png')

    plt.figure(2)
    plt.hist(snp_dep, 60, (1, 60), normed=1)
    plt.title(fn.split('.')[0] + ' snp depth')
    plt.xlabel('Depth')
    plt.ylabel('Probability')
    plt.savefig(fn.split('.')[0] + '.snp_dep.png')
    plt.grid()

    fig = plt.figure(3)
    ax = fig.add_subplot(111)
    plt.plot(snp_dep, snp_qual, '.')
    plt.axis([0, 60, 0, 1000])
    plt.title(fn.split('.')[0] + ' Dep-Qual')
    rect = patches.Rectangle((10,30),width=590, height=970,
                             color='green', alpha=0.5)
    ax.add_patch(rect)
    plt.xlabel('Depth')
    plt.text(40, 600, 'Total: ' + str(total)+'\n' + 'Filtered:' + \
str(fit) + '\n' + fitality, fontsize=20, bbox=dict(facecolor='green') )
    plt.ylabel('Quality')

    plt.savefig(fn.split('.')[0] + '.dep-qual.png')

    plt.show()





