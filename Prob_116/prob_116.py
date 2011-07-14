#!/usr/bin/python
#
# Project Euler.net Problem 116
# 
# A row of five black square tiles is to have a number of its tiles
# replaced with coloured oblong tiles chosen from red (length two),
# green (length three), or blue (length four).
# 
# If red tiles are chosen there are exactly seven ways this can be
# done.
#                         
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# |R-R| | | |  | |R-R| | |  | | |R-R| |  | | | |R-R|
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
#         
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# |R-R|R-R| |  |R-R| |R-R|  | |R-R|R-R|
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# 
# If green tiles are chosen there are three ways.
#                 
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# |G-G-G| | |  | |G-G-G| |  | | |G-G-G|
# +-+-+-+-+-+  +-+-+-+-+-+  +-+-+-+-+-+
# 
# And if blue tiles are chosen there are two ways.
#         
# +-+-+-+-+-+  +-+-+-+-+-+
# |B-B-B-B| |  | |B-B-B-B|
# +-+-+-+-+-+  +-+-+-+-+-+
# 
# Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways
# of replacing the black tiles in a row measuring five units in
# length.
# 
# How many different ways can the black tiles in a row measuring fifty
# units in length be replaced if colours cannot be mixed and at least
# one coloured tile must be used?
# 
# NOTE: This is related to problem 117.
#
# Solved 07/03/11
# 142 problems solved
# Position #176 on level 3


import sys

size = 50
print "Running with size = {0}".format(size)

rsize = 2
gsize = 3
bsize = 4
ways_cache = [[0]*size for _ in range(size)]  # This is how you create a 2D array in python!

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

answer = 0

for r in range(1, 1+size/rsize):
    rcnt = ways_to_fit(r+1,size-r*rsize)
    print "{0} red blocks = {1}".format(r, rcnt)
    answer += rcnt

for g in range(1, 1+size/gsize):
    gcnt = ways_to_fit(g+1,size-g*gsize)
    print "{0} green blocks = {1}".format(g, gcnt)
    answer += gcnt

for b in range(1, 1+size/bsize):
    bcnt = ways_to_fit(b+1,size-b*bsize)
    print "{0} blue blocks = {1}".format(b, bcnt)
    answer += bcnt

print "Answer =", answer
