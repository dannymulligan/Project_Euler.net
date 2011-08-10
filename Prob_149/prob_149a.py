#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 149
#
# Searching for a maximum-sum subsequence.
#
# Looking at the table below, it is easy to verify that the maximum
# possible sum of adjacent numbers in any direction (horizontal,
# vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).
#
#     -2   5   3   2
#      9  -6   5   1
#      3   2   7   3
#     -1   8  -4   8
# 
# Now, let us repeat the search, but on a much larger scale:
# 
# First, generate four million pseudo-random numbers using a specific
# form of what is known as a "Lagged Fibonacci Generator":
#
# For 1 <= k <= 55,
#     s(k) = [100003 − 200003k + 300007k^3] (modulo 1000000) − 500000.
# For 56 <= k <= 4000000,
#     s(k) = [s(k−24) + s(k−55) + 1000000] (modulo 1000000) − 500000.
#
# Thus, s(10) = −393027 and s(100) = 86613.
#
# The terms of s are then arranged in a 2000×2000 table, using the
# first 2000 numbers to fill the first row (sequentially), the next
# 2000 numbers to fill the second row, and so on.
#
# Finally, find the greatest sum of (any number of) adjacent entries
# in any direction (horizontal, vertical, diagonal or anti-diagonal).
#
# Solved 07/18/11
# 151 problems solved
# Position #756 on level 4

SIZEX = 2000
SIZEY = 2000

print "Running with SIZEX = {0} & SIZEY = {1}".format(SIZEX, SIZEY)

#SIZEX = 4
#SIZEY = 4
#s = [-1,  8, -4,  8,
#      3,  2,  7,  3,
#      9, -6,  5,  1,
#     -2,  5,  3,  2 ]

import sys

import time
overall_start_time = time.clock()
start_time = overall_start_time
end_time = 0.0


########################################
def check_list(l):
    #print "check_list: {0}".format(l)
    improved = True
    while improved:
        improved = False
        for x in range(len(l)-2):
            if (l[x] > 0):
                if ((l[x]+l[x+1] > 0) & (l[x+1]+l[x+2] > 0)):
                    #print "shortening", l,
                    improved = True
                    l[x] += (l[x+1] + l[x+2])
                    l[x+1] = 0
                    l[x+2] = 0
                    #print "to", l

        for x in range(len(l)-4):
            if (l[x] > 0):
                if ((l[x  ]+l[x+1]+l[x+2]+l[x+3]        > 0)
                  & (l[x  ]+l[x+1]                      > 0)
                  & (                     l[x+3]+l[x+4] > 0)
                  & (       l[x+1]+l[x+2]+l[x+3]+l[x+4] > 0)):
                    #print "shortening", l,
                    improved = True
                    l[x] += (l[x+1] + l[x+2] + l[x+3] + l[x+4])
                    l[x+1] = 0
                    l[x+2] = 0
                    l[x+3] = 0
                    l[x+4] = 0
                    #print "to", l

        if (len(l) >= 2):
            if ((l[0] < 0) & (l[1] > 0)):
                improved = True
                l[0] = 0
            if ((l[-1] < 0) & (l[-2] > 0)):
                improved = True
                l[-1] = 0

        if (len(l) >= 3):
            if ((l[0] > 0) & (l[0]+l[1] < 0) & (l[0] < l[2])):
                improved = True
                l[0] = 0
            if ((l[-1] > 0) & (l[-1]+l[-2] < 0) & (l[-1] < l[-3])):
                improved = True
                l[-1] = 0

        #print "check_list:. {0}".format(l)

        ll = []
        for x in range(len(l)):
            if (l[x] != 0):
                ll.append(l[x])
        del l
        l = ll
        #print "check_list:.. {0}".format(l)

    best = l[0]
    for xl in range(0,1+len(l),2):
        for xr in range(1+xl,1+len(l),2):
            b = sum(l[xl:xr])
            #print "sum([{0}:{1}]) = sum({2}) = {3}".format(xl,xr,l[xl:xr],b)
            if (b>best):  best = b
    #print "check_list: max = {0}, l = {1}".format(max(l), l)
    return best

# The simplistic algoritm of picking the maximum value in l fails for this data sequence
# 439, -452041, 275029, 323399, 52962, -138838, -80081, 46962, -156475, 220312, 406181
# The simple algorithm picks 275029 + 323399 + 52962 = 651390
# The correct result is 275029, 323399, 52962, -138838, -80081, 46962, -156475, 220312, 406181 = 949451

# 439, -452041, 275029, 323399, 52962, -138838, -80081, 46962, -156475, 220312, 406181
# 439, -452041, 651390, -218919, 46962, -156475, 626493

#l = [-1, 439, -452041, 651390, -218919, 46962, -156475, 626493, -100, 10]
#print check_list(l)  # Answer should be 949451
#l = [-759174, 1077662, -1079585, 787016, -333564]
#print check_list(l)  # Answer should be 1077662
#sys.exit()


########################################
# Build the array that we will search
print "Creating array at", start_time, "seconds"
s = []
for k in xrange(1,SIZEX*SIZEY+1):
    if (k <= 55):
        t = (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
    else:
        t = (s[k-25] + s[k-56] +  1000000) % 1000000 - 500000
    s.append(t)
end_time = time.clock()
print "Finished creating array at", end_time - start_time, "seconds"


########################################
# X search
start_time = end_time
print "Starting X search at", start_time, "seconds"
bestX = s[0]
for y in range(SIZEY):
    rep = 1
    val = s[y*SIZEX]
    vmin = s[y*SIZEX]
    ss = []
    #print "    ({0},{1}) = {2}".format(0,y,val)
    for x in range(1,SIZEX):
        t = s[y*SIZEX+x]
        #print "    ({0},{1}) = {2}".format(x,y,t)
        if (t>vmin):  vmin = t
        if ((val * t) < 0):
            # change in sign, add to list and start a new combination
            ss.append(val)
            rep = 1
            val = t
        else:
            # sign is the same, combine
            val += t
            rep += 1
    ss.append(val)
    #print ss
    b = check_list(ss)
    if (b < 0):
        b = vmin
    if (b > bestX):
        bestX = b
    #print "XLine ({0},{1}): best = {2}".format(0,y,b)
end_time = time.clock()
print "Finished X search, best found = {0}, time taken = {1} seconds".format(bestX, end_time - start_time)


########################################
# Y search
start_time = end_time
print "Starting Y search at", start_time, "seconds"
bestY = s[0]
for x in range(SIZEX):
    rep = 1
    val = s[x]
    vmin = s[x]
    ss = []
    #print "    ({0},{1}) = {2}".format(x,0,val)
    for y in range(1,SIZEY):
        t = s[y*SIZEX+x]
        #print "    ({0},{1}) = {2}".format(x,y,t)
        if (t>vmin):  vmin = t
        if ((val * t) < 0):
            # change in sign, add to list and start a new combination
            ss.append(val)
            rep = 1
            val = t
        else:
            # sign is the same, combine
            val += t
            rep += 1
    ss.append(val)
    b = check_list(ss)
    if (b < 0):
        b = vmin
    if (b > bestY):
        bestY = b
    #print "YLine ({0},{1}): best = {2}".format(x,0,b)
end_time = time.clock()
print "Finished Y search, best found = {0}, time taken = {1} seconds".format(bestY, end_time - start_time)


########################################
# A search /
start_time = end_time
print "Starting A search (/) at", start_time, "seconds"
bestA = s[0]
for y in range(SIZEY-1,0,-1):
    rep = 1
    val = s[y*SIZEX]
    vmin = s[y*SIZEX]
    ss = []
    #print "    ({0},{1}) = {2}".format(0,y,val)
    for l in range(1,min(SIZEY-y,SIZEX)):
        (xl,yl) = (l,y+l)
        t = s[yl*SIZEX+xl]
        if (t>vmin):  vmin = t
        #print "    ({0},{1}) = {2}".format(xl,yl,t)
        if ((val * t) < 0):
            # change in sign, add to list and start a new combination
            ss.append(val)
            rep = 1
            val = t
        else:
            # sign is the same, combine
            val += t
            rep += 1
    ss.append(val)
    b = check_list(ss)
    if (b < 0):
        b = vmin
    if (b > bestA):
        bestA = b
    #print "ALine ({0},{1}): best = {2}".format(0,y,b)

for x in range(SIZEX):
    rep = 1
    val = s[x]
    vmin = s[x]
    ss = []
    #print "    ({0},{1}) = {2}".format(x,0,val)
    for l in range(1,min(SIZEY,SIZEX-x)):
        (xl,yl) = (x+l,l)
        t = s[yl*SIZEX+xl]
        if (t>vmin):  vmin = t
        #print "    ({0},{1}) = {2}".format(xl,yl,t)
        if ((val * t) < 0):
            # change in sign, add to list and start a new combination
            ss.append(val)
            rep = 1
            val = t
        else:
            # sign is the same, combine
            val += t
            rep += 1
    ss.append(val)
    #print ss
    b = check_list(ss)
    if (b < 0):
        b = vmin
    if (b > bestA):
        bestA = b
    #print "ALine ({0},{1}): best = {2}".format(x,0,b)

end_time = time.clock()
print "Finished A search (/), best found = {0}, time taken = {1} seconds".format(bestA, end_time - start_time)


########################################
# B search \
start_time = end_time
print "Starting B search (\) at", start_time, "seconds"
bestB = s[0]
for y in range(SIZEY):
    rep = 1
    val = s[y*SIZEX]
    vmin = s[y*SIZEX]
    ss = []
    #import pdb; pdb.set_trace()
    #print "    ({0},{1}) = {2}".format(0,y,val)
    for l in range(0,min(y,SIZEX)):
        (xl,yl) = (l+1,y-l-1)
        t = s[yl*SIZEX+xl]
        if (t>vmin):  vmin = t
        #print "    ({0},{1}) = {2}".format(xl,yl,t)
        if ((val * t) < 0):
            # change in sign, add to list and start a new combination
            ss.append(val)
            rep = 1
            val = t
        else:
            # sign is the same, combine
            val += t
            rep += 1
    ss.append(val)
    b = check_list(ss)
    if (b < 0):
        b = vmin
    if (b > bestB):
        bestB = b
    #print "BLine ({0},{1}): best = {2}".format(0,y,b)

for x in range(1,SIZEX):
    rep = 1
    val = s[(SIZEY-1)*SIZEX+x]
    vmin = s[(SIZEY-1)*SIZEX+x]
    ss = []
    #print "    ({0},{1}) = {2}".format(x,SIZEY-1,val)
    for l in range(0,min(SIZEY-1,SIZEX-1-x)):
        (xl,yl) = (x+l+1,SIZEY-1-l-1)
        t = s[yl*SIZEX+xl]
        if (t>vmin):  vmin = t
        #print "    ({0},{1}) = {2}".format(xl,yl,t)
        if ((val * t) < 0):
            # change in sign, add to list and start a new combination
            ss.append(val)
            rep = 1
            val = t
        else:
            # sign is the same, combine
            val += t
            rep += 1
    ss.append(val)
    b = check_list(ss)
    if (b < 0):
        b = vmin
    if (b > bestB):
        bestB = b
    #print "BLine ({0},{1}): best = {2}".format(x,SIZEY-1,b)

end_time = time.clock()
print "Finished B search (/), best found = {0}, time taken = {1} seconds".format(bestB, end_time - start_time)


########################################
print "Answer =", max(bestX, bestY, bestA, bestB)
print "Total time taken =", end_time - overall_start_time, "seconds"
