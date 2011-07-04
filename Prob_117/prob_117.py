#!/usr/bin/python
#
# Project Euler.net Problem 117
# 
# Using a combination of black square tiles and oblong tiles chosen
# from: red tiles measuring two units, green tiles measuring three
# units, and blue tiles measuring four units, it is possible to tile a
# row measuring five units in length in exactly fifteen different
# ways.
#                                 
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# | | | | | |  |R-R| | | |  | |R-R| | |  | | |R-R| |
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
#
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# | | | |R-R|  |R-R|R-R| |  |R-R| |R-R|  | |R-R|R-R|
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
#
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# |G-G-G| | |  | |G-G-G| |  | | |G-G-G|  |R-R|G-G-G|
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# 
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# |G-G-G|R-R|  |B-B-B-B| |  | |B-B-B-B|
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# 
# How many ways can a row measuring fifty units in length be tiled?
# 
# NOTE: This is related to problem 116.
#
# Answer: 100808458960497
# Solved 07/04/11
# 144 problems solved
# Position #176 on level 3


import sys
import math

SIZE = 50
print "Running with SIZE = {0}".format(SIZE)

RSIZE = 2
GSIZE = 3
BSIZE = 4
ways_cache = [[0]*SIZE for _ in range(SIZE)]  # This is how you create a 2D array in python!

def ways_to_fit(b,i):
    if (i==0):
        #print "ways_to_fit({0},{1})".format(b,i), "= 1 (i==0)"
        return 1

    if (b==1):
        #print "ways_to_fit({0},{1})".format(b,i), "= 1 (b==1)"
        return 1

    if (i==1):
        #print "ways_to_fit({0},{1})".format(b,i), "= {0} (i==1)".format(b)
        return b

    if (b==2):
        #print "ways_to_fit({0},{1})".format(b,i), "= {0} (b==2)".format(i+1)
        return (i+1)

    if (ways_cache[b][i] == 0):
        a = 0
        for x in range(i+1):
            a += ways_to_fit(b-1,i-x)
        ways_cache[b][i] = a
        #print "ways_to_fit({0},{1})".format(b,i), "= {0} (recursion)".format(a)
    #else:
        #print "ways_to_fit({0},{1})".format(b,i), "= {0} (cache)".format(ways_cache[b][i])
    return ways_cache[b][i]

def ways_to_perm(r,g,b):
    ans = math.factorial(r+g+b) / (math.factorial(r) * math.factorial(g) * math.factorial(b))
    return ans

answer = 0

print SIZE/RSIZE
for r in range(1+SIZE/RSIZE):
    for g in range(1+(SIZE-r*RSIZE)/GSIZE):
        for b in range(1+(SIZE-r*RSIZE-g*GSIZE)/BSIZE):
            #print "(r,g,b) = ({0},{1},{2})".format(r,g,b)

            bins = r + g + b + 1
            items = SIZE - r*RSIZE - g*GSIZE - b*BSIZE
            wcnt = ways_to_fit(bins, items)
            ocnt = ways_to_perm(r,g,b)
            answer += wcnt * ocnt

            print "(r,g,b) = ({0},{1},{2}), wcnt = {3}, ocnt = {4}".format(r,g,b, wcnt, ocnt)
            
print "Answer =", answer
sys.exit()
