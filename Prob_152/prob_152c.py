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
i_num = [0]*81
denom = 2*2*2*2*2*2 * 3*3*3 * 5*5 * 7*7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47 * 53 * 59 * 61 * 67* 71 * 73 * 79
denom = denom ** 2
for i in xrange(2,81):
    i_num[i] = (denom / i**2)

t_num = [0]*81
tot = 0
for i in xrange(80,1,-1):
    tot += i_num[i]
    t_num[i] = tot

target = denom/4
print "target =", target
print "i_num[2]/target =", i_num[2]/target

for i in xrange(3,81):
    print "i_num[{0}] = {1}, t_num[{0}] = {2}".format(i,i_num[i],t_num[i])
for i in xrange(3,81):
    print "i_num[{0}] = {1:2.4f}%, t_num[{0}] = {2:2.4f}%".format(i,100.0*i_num[i]/target,100.0*t_num[i]/target)

print "Time taken = {0} seconds".format(time.clock() - start_time)
