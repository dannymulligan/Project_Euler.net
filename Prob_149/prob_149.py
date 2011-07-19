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
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

SIZEX = 100
SIZEY = 100

#SIZEX = 4
#SIZEY = 4
#s = [-1,  8, -4,  8,
#      3,  2,  7,  3,
#      9, -6,  5,  1,
#     -2,  5,  3,  2 ]

import sys

import time
#start_time = time.clock()
overall_start_time = 0.0
start_time = overall_start_time
end_time = 0.0


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
#end_time = time.clock()
print "Finished creating array at", end_time - start_time, "seconds"


########################################
# Search along X axis
start_time = end_time
print "Starting X search at", start_time, "seconds"
bestX = 0
for y in range(SIZEY):
    best = 0
    #print "line = {0}".format(s[y*SIZEX:(y+1)*SIZEX])
    #import pdb; pdb.set_trace()
    for xl in range(0,SIZEX):
        for xr in range(xl,SIZEX):
            b = s[y*SIZEX+xl]
            #print "    ({0},{1}) = {2}".format(xl,y,b)
            for l in range(0,xr-xl):
                b += s[y*SIZEX+xl+l+1]
                #print "    ({0},{1}) = {2}".format(xl+l+1,y,s[y*SIZEX+xl+l+1])
            if (b > bestX):
                bestX = b
            if (b > best):
                best = b
            #print "b=",b, "bestX=", bestX
    print "XLine ({0},{1}): best = {2}".format(0,y,best)
#end_time = time.clock()
print "Finished X search, best found = {0}, time taken = {1} seconds".format(bestX, end_time - start_time)


########################################
# Search along Y axis
start_time = end_time
print "Starting Y search at", start_time, "seconds"
bestY = 0
for x in range(SIZEX):
    best = 0
    for yl in range(0,SIZEY):
        for yr in range(yl,SIZEY):
            b = s[yl*SIZEX+x]
            #print "    ({0},{1}) = {2}".format(x,yl,b)
            for l in range(0,yr-yl):
                b += s[(yl+l+1)*SIZEX+x]
                #print "    ({0},{1}) = {2}".format(x,yl+l+1,s[(yl+l+1)*SIZEX+x])
            if (b > bestY):
                bestY = b
            if (b > best):
                best = b
            #print "--", b, best
    print "YLine ({0},{1}): best = {2}".format(x,0,best)
#end_time = time.clock()
print "Finished Y search, best found = {0}, time taken = {1} seconds".format(bestY, end_time - start_time)


########################################
# Search along A (/) axis
start_time = end_time
print "Starting A search (/) at", start_time, "seconds"
bestA = s[0]
for y in range(SIZEY-1,0,-1):
    best = s[y*SIZEX]  # (0,y)
    l = min(SIZEY-y,SIZEX)
    for ll in range(0,l):
        for lr in range(ll,l):
            b = 0
            for a in range(ll,lr+1):
                b += s[(y+a)*SIZEX+a]
                #print "    ({0},{1}) = {2}".format(a,y+a,s[(y+a)*SIZEX+a])
            #print "--"
            if (b > bestA):
                bestA = b
            if (b > best):
                best = b
    print "ALine ({0},{1}): best = {2}".format(0,y,best)

for x in range(SIZEX):
    best = s[x]  # (x,0)
    l = min(SIZEX-x,SIZEY)
    for ll in range(0,l):
        for lr in range(ll,l):
            b = 0
            for a in range(ll,lr+1):
                b += s[a*SIZEX+x+a]
                #print "    ({0},{1}) = {2}".format(x+a,a,s[a*SIZEX+x+a])
                #print "x =", x, "ll =", ll, "lr =", lr
            #print "--"
            if (b > bestA):
                bestA = b
            if (b > best):
                best = b
    print "ALine ({0},{1}): best = {2}".format(x,0,best)
#end_time = time.clock()
print "Finished A search (/), best found = {0}, time taken = {1} seconds".format(bestA, end_time - start_time)


########################################
# Search along B (\) axis
start_time = end_time
print "Starting B search (\) at", start_time, "seconds"
bestB = s[0]
for y in range(SIZEY):
    best = s[y*SIZEX]  # (0,y)
    l = min(y+1,SIZEX)
    for ll in range(0,l):
        for lr in range(ll,l):
            b = 0
            for a in range(ll,lr+1):
                b += s[(y-a)*SIZEX+a]
                #print "    ({0},{1}) = {2}".format(a,y-a,s[(y-a)*SIZEX+a])
            #print "--"
            if (b > bestB):
                bestB = b
            if (b > best):
                best = b
    print "BLine ({0},{1}): best = {2}".format(0,y,best)

for x in range(1,SIZEX):
    best = s[(SIZEY-1)*SIZEX+x]  # (x,SIZEY-1)
    l = min(SIZEX-x,SIZEY)
    for ll in range(0,l):
        for lr in range(ll,l):
            b = 0
            for a in range(ll,lr+1):
                b += s[(SIZEY-a-1)*SIZEX+x+a]
                #print "    ({0},{1}) = {2}".format(x+a,SIZEY-a-1,s[(SIZEY-a-1)*SIZEX+x+a])
            #print "--"
            if (b > bestB):
                bestB = b
            if (b > best):
                best = b
    print "BLine ({0},{1}): best = {2}".format(x,SIZEY-1,best)
#end_time = time.clock()
print "Finished B search (/), best found = {0}, time taken = {1} seconds".format(bestB, end_time - start_time)


print "Answer =", max(bestX, bestY, bestA, bestB)
print "Total time taken =", end_time - overall_start_time, "seconds"
