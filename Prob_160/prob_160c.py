#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 160
#
# Problem summary
#
# For any N, let f(N) be the last five digits before the trailing
# zeroes in N!. For example,
#
#     9! = 362880 so f(9)=36288
#     10! = 3628800 so f(10)=36288
#     20! = 2432902008176640000 so f(20)=17664
#
# Find f(1,000,000,000,000)
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level 4


# X = 0..9
# Y = 1..9

import sys
import time
start_time = time.clock()

########################################
def odd(n):
    if (n % 2):  return True
    else:        return False


########################################
def expand(n,n2,n5):
    np = 2
    while n2:
        if odd(n2):
            n2 -= 1
            n = (n*np) % 100000
        else:
            np = np**2 % 100000
            n2 /= 2
    np = 5
    while n5:
        if odd(n5):
            n5 -= 1
            n = (n*np) % 100000
        else:
            np = np**2 % 100000
            n5 /= 2
    return (n, n2, n5)


print "########################################"
print "Simple calculation method"
N = 6
LIMIT = 10**N
(s,s2,s5) = (1,0,0)
for i in xrange(1,10**N):
    s = s*i
    while ((s % 10) == 0):
        s /= 10
    s = s % 10**12

    if ((i % 10**7) == 0):
        print "    Answer: f({0}) = {1} ({2}) {3} seconds".format(i,s%100000,s, time.clock() - start_time)

s = s % 100000

print "s={0} * 2^{1} * 5^{2}".format(s,s2,s5)

m = min(s2,s5)
(s2,s5) = (s2-m,s5-m)

print "s={0} * 2^{1} * 5^{2}".format(s,s2,s5)

(s,s2,s5) = expand(s,s2,s5)

print "s={0} * 2^{1} * 5^{2}".format(s,s2,s5)

s = s % 100000

print "s={0} * 2^{1} * 5^{2}".format(s,s2,s5)

print "Answer: f(10^{0}) = {1}".format(N,s)
print "Time taken = {0} seconds".format(time.clock() - start_time)

# f(10^1) = 36288
# f(10^2) = 16864
# f(10^3) = 53472
# f(10^4) = 79008
# f(10^5) = 62496
# f(10^6) = 12544
# f(10^7) = 94688

