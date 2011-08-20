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

import sys
import time
start_time = time.clock()

########################################
def odd(n):
    if (n % 2):  return True
    else:        return False

########################################
# a = factorial 1..XXY
# where X = 0...9, and Y = 1..9
a = 1
a2 = 0
a5 = 0
at = 999
for i in xrange(1,at+1):
    if ((i%10) == 0):  continue

    ii = i
    while ((ii%2) == 0):
        ii /= 2
        a2 += 1
    while ((ii%5) == 0):
        ii /= 5
        a5 += 1

    a = a * ii
    a = a % 100000


print "a={0} * 2^{1} * 5^{2}".format(a,a2,a5)
m = min(a2,a5)
(a2,a5) = (a2-m,a5-m)
print "a={0} * 2^{1} * 5^{2}".format(a,a2,a5)

ap = 2
while a2:
    if odd(a2):
        a2 -= 1
        a = (a*ap) % 100000
    else:
        ap = ap**2 % 100000
        a2 /= 2
    print "    ap={0}, a2={1}, a={2} * {0}^{1}".format(ap,a2,a)
print "a={0} * 2^{1} * 5^{2}".format(a,a2,a5)
print "f({0})={1}".format(at,a)
print


#print "########################################"
#print "simple calculation method"
#a = 1
#tt = at
#for i in xrange(2,tt+1):
#    ii = i
#    while ((ii%10) == 0):
#        ii /= 10
#    a = a*ii
#    while ((a%10) == 0):
#        a /= 10
#    a = a % 100000000
#a = a % 100000
#print "simple calculation f({0})={1}".format(tt, a)


########################################
# c = a^1,000,000
c = 1
ct = 2
for i in xrange(ct):
    c = c * a
    c = c % 100000

print "c={0}".format(c)
print "f({0})={1}".format(at*ct,c)

print "Answer =", c
print "Time taken = {0} seconds".format(time.clock() - start_time)
