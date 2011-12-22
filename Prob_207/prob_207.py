#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 207
#
# Integer partition equations
#
# For some positive integers k, there exists an integer partition of
# the form
#
#     4^t = 2^t + k
#
# where 4t, 2t, and k are all positive integers and t is a real
# number.
#
# The first two such partitions are 4^1 = 2^1 + 2 and 4^1.5849625... =
# 2^1.5849625... + 6.
#
# Partitions where t is also an integer are called perfect.
#
# For any m>= 1 let P(m) be the proportion of such partitions that are
# perfect with k <= m.  Thus P(6) = 1/2.
#
# In the following table are listed some values of P(m)
#
#     P(5) = 1/1
#     P(10) = 1/2
#     P(15) = 2/3
#     P(20) = 1/2
#     P(25) = 1/2
#     P(30) = 2/5
#     ...
#     P(180) = 1/4
#     P(185) = 3/13
#
# Find the smallest m for which P(m) < 1/12345
#
# Solved 12/21/11
# 173 problems solved
# Position #29 on level 6

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

import math

import sys
import time
start_time = time.clock()

########################################
def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a


########################################
def log2(n):
    return math.log(1.0*n)/math.log(2.0)


########################################
# 4^1 = 2^1 + 2  =>  4 = 2 + 2
# 4^? = 2^? + 6  =>  9 = 3 + 6
# 4^2 = 2^2 + 12 =>  16 = 4 + 12
# 4^? = 2^? + 20 =>  25 = 5 + 20
# 4^? = 2^? + 30 =>  36 = 6 + 30

# Rearranging the formula...
#
#     4^t = 2^t + k
#     (2^t)*(2^t) = 2^t + k
#     n*n = n + k
#     k = n*(n-1)
#
# The partition is prefect if n is an integer power of 2, or 2^i = n

# We're going to iterate through n
MAX = 1000000
p_total   = 0
p_perfect = 0
next_power_2 = 2
found = False
for n in xrange(2,MAX):
    k = n*(n-1)
    p_total += 1

    if (n == next_power_2):
        p_perfect += 1
        next_power_2 *= 2
        print "    4^{0} = 2^{0} + {1} (perfect)".format(int(log2(n)), k)

        det = gcd(p_perfect,p_total)
        print "P({0}) = {1}/{2} ({3} perfect out of {4} total)".format(k,p_perfect/det,p_total/det,p_perfect,p_total)
    #else:
        #print "    4^{0} = 2^{0} + {1}".format(log2(n), k)


    if ((p_perfect*12345) < p_total):
        found = True
        break

if (found):
    print "Answer =", k
else:
    print "Answer not found, try rerunning with MAX >", MAX

print "Time taken = {0} seconds".format(time.clock() - start_time)

