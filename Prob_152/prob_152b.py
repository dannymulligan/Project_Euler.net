#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 152
#
# Writing 1/2 as a sum of inverse squares
#
# There are several ways to write the number 1/2 as a sum of inverse
# squares using distinct integers.
#
# For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:
#
# In fact, only using integers between 2 and 45 inclusive, there are
# exactly three ways to do it, the remaining two being:
# {2,3,4,6,7,9,10,20,28,35,36,45} and
# {2,3,4,6,7,9,12,15,28,30,35,36,45}.
#
# How many ways are there to write the number 1/2 as a sum of inverse
# squares using distinct integers between 2 and 80 inclusive?
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
#import pdb
#pdb.set_trace()

import time
start_time = time.clock()
prev_time = start_time

import fractions
import itertools
import bisect


########################################
def possibilities(nlist):
    for e in itertools.product('01',repeat=len(nlist)):
        f = list(e)
        poss = []
        for i in xrange(len(f)):
            if (f[i] == '1'):
                poss.append(nlist[i])
        yield poss
    return


########################################
MAX0 = 2    + 10
MAX1 = MAX0 + 14
MAX2 = MAX1 + 10
MAX3 = MAX2 + 11
MAX4 = MAX3 + 2
MAX5 = MAX4 + 2
#MAX0 = 2    + 13
#MAX1 = MAX0 + 13
#MAX2 = MAX1 + 13
#MAX3 = MAX2 + 13
#MAX4 = MAX3 + 13
#MAX5 = MAX4 + 13
print "MAX0={0}, MAX1={1}, MAX2={2}, MAX3={3}, MAX4={4}, MAX5={5}".format(MAX0, MAX1, MAX2, MAX3, MAX4, MAX5)


########################################
n2 = [0]
for n in xrange(1,MAX5+1):
    temp = fractions.Fraction(1,n**2)
    n2.append(temp)

max_remaining = [0]*(MAX5+1)
temp = fractions.Fraction(0,1)
for n in xrange(MAX5,1,-1):
    temp += n2[n]
    max_remaining[n] = temp
#for n in xrange(MAX5):
#    print "max_remaining[{0}] = {1:5e} = {2}".format(n,float(max_remaining[n]),max_remaining[n])


########################################
n_poss0 = []
l_poss0 = []
for p in possibilities(xrange(2,MAX0)):
    temp = fractions.Fraction(0,1)
    for n in p:
        temp += n2[n]

    # insert into the l_poss? & n_poss? lists in a sorted manner
    i_poss0 = bisect.bisect_left(n_poss0,temp)
    n_poss0.insert(i_poss0,temp)
    l_poss0.insert(i_poss0,p)

#print "len(n_poss0)=", len(n_poss0)
#for i in xrange(len(n_poss0)):
#    print n_poss0[i], l_poss0[i]
new_time = time.clock()
print "Generated n_poss0/l_poss0 table in {0} seconds, length = {1}".format(new_time - prev_time, len(l_poss0))
prev_time = new_time

########################################
n_poss1 = []
l_poss1 = []
for p in possibilities(xrange(MAX0,MAX1)):
    temp = fractions.Fraction(0,1)
    for n in p:
        temp += n2[n]

    # insert into the l_poss? & n_poss? lists in a sorted manner
    i_poss1 = bisect.bisect_left(n_poss1,temp)
    n_poss1.insert(i_poss1,temp)
    l_poss1.insert(i_poss1,p)

#print "len(n_poss1)=", len(n_poss1)
#for i in xrange(len(n_poss1)):
#    print n_poss1[i], l_poss1[i]
new_time = time.clock()
print "Generated n_poss1/l_poss1 table in {0} seconds, length = {1}".format(new_time - prev_time, len(l_poss1))
prev_time = new_time

########################################
n_poss2 = []
l_poss2 = []
for p in possibilities(xrange(MAX1,MAX2)):
    temp = fractions.Fraction(0,1)
    for n in p:
        temp += n2[n]

    # insert into the l_poss? & n_poss? lists in a sorted manner
    i_poss2 = bisect.bisect_left(n_poss2,temp)
    n_poss2.insert(i_poss2,temp)
    l_poss2.insert(i_poss2,p)

#print "len(n_poss2)=", len(n_poss2)
#for i in xrange(len(n_poss2)):
#    print n_poss2[i], l_poss2[i]
new_time = time.clock()
print "Generated n_poss2/l_poss2 table in {0} seconds, length = {1}".format(new_time - prev_time, len(l_poss2))
prev_time = new_time

########################################
n_poss3 = []
l_poss3 = []
for p in possibilities(xrange(MAX2,MAX3)):
    temp = fractions.Fraction(0,1)
    for n in p:
        temp += n2[n]

    # insert into the l_poss? & n_poss? lists in a sorted manner
    i_poss3 = bisect.bisect_left(n_poss3,temp)
    n_poss3.insert(i_poss3,temp)
    l_poss3.insert(i_poss3,p)

#print "len(n_poss3)=", len(n_poss3)
#for i in xrange(len(n_poss3)):
#    print n_poss3[i], l_poss3[i]
new_time = time.clock()
print "Generated n_poss3/l_poss3 table in {0} seconds, length = {1}".format(new_time - prev_time, len(l_poss3))
prev_time = new_time

########################################
n_poss4 = []
l_poss4 = []
for p in possibilities(xrange(MAX3,MAX4)):
    temp = fractions.Fraction(0,1)
    for n in p:
        temp += n2[n]

    # insert into the l_poss? & n_poss? lists in a sorted manner
    i_poss4 = bisect.bisect_left(n_poss4,temp)
    n_poss4.insert(i_poss4,temp)
    l_poss4.insert(i_poss4,p)

#print "len(n_poss4)=", len(n_poss4)
#for i in xrange(len(n_poss4)):
#    print n_poss4[i], l_poss4[i]
new_time = time.clock()
print "Generated n_poss4/l_poss4 table in {0} seconds, length = {1}".format(new_time - prev_time, len(l_poss4))
prev_time = new_time


########################################
n_poss5 = []
l_poss5 = []
for p in possibilities(xrange(MAX4,MAX5)):
    temp = fractions.Fraction(0,1)
    for n in p:
        temp += n2[n]

    # insert into the l_poss? & n_poss? lists in a sorted manner
    i_poss5 = bisect.bisect_left(n_poss5,temp)
    n_poss5.insert(i_poss5,temp)
    l_poss5.insert(i_poss5,p)

#print "len(n_poss5)=", len(n_poss5)
#for i in xrange(len(n_poss5)):
#    print n_poss5[i], l_poss5[i]
new_time = time.clock()
print "Generated n_poss5/l_poss5 table in {0} seconds, length = {1}".format(new_time - prev_time, len(l_poss5))
prev_time = new_time


########################################
prev = fractions.Fraction(0,1)
total = fractions.Fraction(0,1)
min_diff = fractions.Fraction(1,1)
max_diff = fractions.Fraction(0,1)
print "####################"
for i in xrange(len(n_poss0)):
    if (i > 0):
        diff = n_poss0[i] - n_poss0[i-1]
        total += diff
        if (diff < min_diff):  min_diff = diff
        if (diff > max_diff):  max_diff = diff
avg_diff = total/(len(n_poss2)-1)
print "poss0 minimum delta = {0:12g} = {1}".format(float(min_diff), min_diff)
print "poss0 maximum delta = {0:12g} = {1}".format(float(max_diff), max_diff)
print "poss0 average delta = {0:12g} = {1}".format(float(avg_diff), avg_diff)

prev = fractions.Fraction(0,1)
total = fractions.Fraction(0,1)
min_diff = fractions.Fraction(1,1)
max_diff = fractions.Fraction(0,1)
print "####################"
for i in xrange(len(n_poss1)):
    if (i > 0):
        diff = n_poss1[i] - n_poss1[i-1]
        total += diff
        if (diff < min_diff):  min_diff = diff
        if (diff > max_diff):  max_diff = diff
avg_diff = total/(len(n_poss2)-1)
print "poss1 minimum delta = {0:12g} = {1}".format(float(min_diff), min_diff)
print "poss1 maximum delta = {0:12g} = {1}".format(float(max_diff), max_diff)
print "poss1 average delta = {0:12g} = {1}".format(float(avg_diff), avg_diff)

prev = fractions.Fraction(0,1)
total = fractions.Fraction(0,1)
min_diff = fractions.Fraction(1,1)
max_diff = fractions.Fraction(0,1)
print "####################"
for i in xrange(len(n_poss2)):
    if (i > 0):
        diff = n_poss2[i] - n_poss2[i-1]
        total += diff
        if (diff < min_diff):  min_diff = diff
        if (diff > max_diff):  max_diff = diff
avg_diff = total/(len(n_poss2)-1)
print "poss2 minimum delta = {0:12g} = {1}".format(float(min_diff), min_diff)
print "poss2 maximum delta = {0:12g} = {1}".format(float(max_diff), max_diff)
print "poss2 average delta = {0:12g} = {1}".format(float(avg_diff), avg_diff)

prev = fractions.Fraction(0,1)
total = fractions.Fraction(0,1)
min_diff = fractions.Fraction(1,1)
max_diff = fractions.Fraction(0,1)
print "####################"
for i in xrange(len(n_poss3)):
    if (i > 0):
        diff = n_poss3[i] - n_poss3[i-1]
        total += diff
        if (diff < min_diff):  min_diff = diff
        if (diff > max_diff):  max_diff = diff
avg_diff = total/(len(n_poss3)-1)
print "poss3 minimum delta = {0:12g} = {1}".format(float(min_diff), min_diff)
print "poss3 maximum delta = {0:12g} = {1}".format(float(max_diff), max_diff)
print "poss3 average delta = {0:12g} = {1}".format(float(avg_diff), avg_diff)

#prev = fractions.Fraction(0,1)
#for i in xrange(len(n_poss0)):
#    print "poss0[{0}] = {1} {2} (delta = {3})".format(i, n_poss0[i], l_poss0[i], n_poss0[i] - prev)
#    prev = n_poss0[i]
#prev = fractions.Fraction(0,1)
#for i in xrange(len(n_poss1)):
#    print "poss2[{0}] = {1} {2} (delta = {3})".format(i, n_poss1[i], l_poss1[i], n_poss1[i] - prev)
#    prev = n_poss1[i]
#prev = fractions.Fraction(0,1)
#for i in xrange(len(n_poss1)):
#    print "poss2[{0}] = {1} {2} (delta = {4})".format(i, n_poss2[i], l_poss2[i], n_poss2[i] - prev)
#    prev = n_poss2[i]
#prev = fractions.Fraction(0,1)
#for i in xrange(len(n_poss2)):
#    print "poss3[{0}] = {1} {2} (delta = {3})".format(i, n_poss3[i], l_poss3[i], n_poss3[i] - prev)
#    prev = n_poss3[i]

sys.exit(0)

# MAX0=13, MAX1=24, MAX2=35, MAX3=46, MAX4=48, MAX5=50

# {2,3,4,5,7,12,15,20,28,35}
#poss0[1904] = 43303/88200 [2, 3, 4, 5, 7, 12]
#poss1[47] = 1/144 [15, 20]
#poss2[7] = 1/784 [28]
#poss3[11] = 1/1225 [35]
#print n_poss0[1904] + n_poss1[47] + n_poss2[7] + n_poss3[11]

# {2,3,4,6,7,9,10,20,28,35,36,45}
#poss0[1915] = 784501/1587600 [2, 3, 4, 6, 7, 9, 10]
#poss1[4] = 1/400 [20]
#poss2[7] = 1/784 [28]
#poss3[207] = 661/317520 [35, 36, 45]
#print n_poss0[1915] + n_poss1[4] + n_poss2[7] + n_poss3[207]

# {2,3,4,6,7,9,12,15,28,30,35,36,45}.
#poss0[1905] = 15593/31752 [2, 3, 4, 6, 7, 9, 12]
#poss1[13] = 1/225 [15]
#poss2[35] = 421/176400 [28, 30]
#poss3[207] = 661/317520 [35, 36, 45]
#print n_poss0[1905] + n_poss1[13] + n_poss2[35] + n_poss3[207]

#sys.exit()


########################################
remain0 = fractions.Fraction(1,2)
n0_min = bisect.bisect_left(n_poss0,remain0-max_remaining[MAX0])
n0_max = bisect.bisect_right(n_poss0,remain0)
print "n0_min =", n0_min
print "n0_max =", n0_max
for n0 in xrange(n0_min,n0_max):
    remain1 = remain0 - n_poss0[n0]
    n1_min = bisect.bisect_left(n_poss1,remain1-max_remaining[MAX1])
    n1_max = bisect.bisect_right(n_poss1,remain1)
    print "l_poss0[{0}] = {1:32}, remainder = {2:8e}, n1={3:4}-{4:4}".format(n0,l_poss0[n0],float(remain1), n1_min, n1_max)

    if (remain1 == 0):
        print "Solution found, n0={0}".format(n0)
        print "    answer={0}".format(l_poss0[n0])
        continue

    for n1 in xrange(n1_min,n1_max):
        remain2 = remain1 - n_poss1[n1]
        n2_min = bisect.bisect_left(n_poss2,remain2-max_remaining[MAX2])
        n2_max = bisect.bisect_right(n_poss2,remain2)
        print "    l_poss1[{0}] = {1:32}, remainder = {2:8e}, n2={3:4}-{4:4}".format(n1,l_poss1[n1],float(remain2), n2_min, n2_max)

        if (remain2 == 0):
            print "Solution found, n0={0}, n1={1}".format(n0,n1)
            print "    answer={0}".format(l_poss0[n0]+l_poss1[n1])
            continue

        for n2 in xrange(n2_min,n2_max):
            remain3 = remain2 - n_poss2[n2]
            n3_min = bisect.bisect_left(n_poss3,remain3-max_remaining[MAX3])
            n3_max = bisect.bisect_right(n_poss3,remain3)
            print "        l_poss2[{0}] = {1:32}, remainder = {2:8e}, n3={3:4}-{4:4}".format(n2,l_poss2[n2],float(remain3), n3_min, n3_max)

            if (remain3 == 0):
                print "Solution found, n0={0}, n1={1}, n2={2}".format(n0,n1,n2)
                print "    answer={0}".format(l_poss0[n0]+l_poss1[n1]+l_poss2[n2])
                continue

            for n3 in xrange(n3_min,n3_max):
                remain4 = remain3 - n_poss3[n3]
                n4_min = bisect.bisect_left(n_poss4,remain4-max_remaining[MAX4])
                n4_max = bisect.bisect_right(n_poss4,remain4)
                #print "            l_poss3[{0}] = {1}, n_poss3[{0}] = {2}, remainder = {3}".format(n3,l_poss3[n3],n_poss3[n3],float(remain4))

                if (remain4 == 0):
                    print "Solution found, n0={0}, n1={1}, n2={2}, n3={3}".format(n0,n1,n2, n3)
                    print "    answer={0}".format(l_poss0[n0]+l_poss1[n1]+l_poss2[n2]+l_poss3[n3])
                    continue

print "Time taken = {0} seconds".format(time.clock() - start_time)
