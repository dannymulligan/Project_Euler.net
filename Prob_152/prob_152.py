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

MAX = 35
print "Running with MAX={0}".format(MAX)
import sys
import time
start_time = time.clock()
import pdb

import fractions

########################################



def search(nlist, nmin, nmax, remain):
    global n2
    if (len(nlist) <= 3):
        print "search({0}, {1}, {2}, {3})".format(nlist, nmin, nmax, remain)
    for n in xrange(nmin+1, nmax+1):
        if (n2[n] < remain):
            if (remain < mremain[n]):
                nlist.append(n)
                search(nlist,n,nmax,remain-n2[n])
                del nlist[-1]
            else:
                break
        elif (n2[n] == remain):
            nlist.append(n)
            print "Found {0}, remain={1}, time={2}".format(nlist,remain-n2[n],time.clock() - start_time)
            return
    return


#pdb.set_trace()

n2 = [0]
for n in xrange(1,MAX+1):
    temp = fractions.Fraction(1,n**2)
    n2.append(temp)

mremain = [0]*(MAX+1)
temp = fractions.Fraction(0,1)
for n in xrange(MAX,1,-1):
    temp += n2[n]
    mremain[n] = temp

search([], 1, MAX, fractions.Fraction(1,2))

print "Time taken = {0} seconds".format(time.clock() - start_time)

