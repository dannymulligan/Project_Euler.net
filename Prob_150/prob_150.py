#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 150
#
# Searching a triangular array for a sub-triangle having minimum-sum.
#
# In a triangular array of positive and negative integers, we wish to
# find a sub-triangle such that the sum of the numbers it contains is
# the smallest possible.
#
# In the example below, it can be easily verified that the marked
# triangle satisfies this condition having a sum of −42.
#
# We wish to make such a triangular array with one thousand rows, so
# we generate 500500 pseudo-random numbers s(k) in the range +/-2^19,
# using a type of random number generator (known as a Linear
# Congruential Generator) as follows:
#
#     t := 0
#     for k = 1 up to k = 500500:
#         t := (615949*t + 797807) modulo 2^20
#         s(k) := t-2^19
# 
# Thus: s(1) = 273519, s(2) = −153582, s(3) = 450905 etc
# 
# Our triangular array is then formed using the pseudo-random numbers thus:
#             s1
#           s2  s3
#         s4  s5  s6 
#       s7  s8  s9  s10
#            ....
#
# Sub-triangles can start at any element of the array and extend down
# as far as we like (taking-in the two elements directly below it from
# the next row, the three elements directly below from the row after
# that, and so on).
#
# The "sum of a sub-triangle" is defined as the sum of all the
# elements it contains.
#
# Find the smallest possible sub-triangle sum.
# 
# Solved 07/10/10
# 140 problems solved
# Position #789 on level 4


# SIZE =  50 gives search time = 0.215414 seconds
# SIZE = 100 gives search time = 3.093088 seconds
# SIZE = 200 gives search time = 46.921239 seconds
# Doubling the size of the problem gives ~16x larger run time
# Algorithm is O(n^4)
SIZE = 1000

import sys

import time
start_time = time.clock()

s = []

def grid(x,y):
    #print "grid({0},{1})".format(x,y)
    offset = x*(x+1)/2
    return s[offset+y]
# (x,y)       (0,0)
#          (1,0) (1,1)
#       (2,0) (2,1) (2,2)
#    (3,0) (3,1) (3,2) (3,3)
# (4,0) (4,1) (4,2) (4,3) (4,4)

t = 0
for k in xrange(SIZE*(SIZE+1)/2):
    t = (615949*t + 797807) % 2**20
    s.append(t - 2**19)

print "Finished creating grid at", time.clock() - start_time, "seconds"

#SIZE = 6
#s = [      15,
#        -14,  -7, 
#       20, -13,  -5,
#     -3,   8,  23, -26,
#    1,  -4,  -5, -18,   5,
#-13,  31,   2,   9,  28,   3]
#for x in xrange(10):
#    for y in xrange(x+1):
#        print "{0:8}".format(grid(x,y)),
#    print

print "Starting search at", time.clock() - start_time, "seconds"
search_start_time = time.clock()

best_x = 0
best_y = 0
best_d = 0
best_t = 2**20
for x in xrange(SIZE):
    print ">  x = {0}".format(x)
    for y in xrange(x+1):
        #print ">  x = {0}, y = {1}".format(x,y)
        t = 0
        for d in xrange(SIZE-x):
            for a in xrange(d+1):
                t += grid(x+d,y+a)
            if (t < best_t):
                best_x = x
                best_y = y
                best_d = d
                best_t = t
                print "x = {0}, y = {1}, d = {2}, t = {3}".format(x,y,d,t)

print "Answer =", best_t
print "(x,y) = ({0},{1}), depth={2}".format(best_x,best_y, best_d)
print "Search time taken =", time.clock() - search_start_time, "seconds"
print "Time taken =", time.clock() - start_time, "seconds"
