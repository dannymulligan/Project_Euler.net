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
s = 1
for i in xrange(1,4999999+1):
    if ((i % 10) == 0):  continue

    ii = i
    while ((ii % 10) == 0):
        ii /= 10

    s = s*ii
    while ((s % 10) == 0):
        s /= 10

    s = s % 1000000000
s = s % 100000
print "f(XXX,XXY)={0}".format(s)
# f(Y)=36288
# f(XY)=44128
# f(XXY)=46048
# f(X,XXY)=94464
# f(XXX,XXY)=96864

print "########################################"
print "Fancy calculation method"
(a, a2, a5) = (1, 0, 0)
for i in xrange(1,4999999+1):
    if ((i % 10) == 0):  continue

    ii = i
    while ((ii % 2) == 0):
        ii /= 2
        a2 += 1
    while ((ii % 5) == 0):
        ii /= 5
        a5 += 1

    a = a * ii
    a = a % 100000

print "a={0} * 2^{1} * 5^{2}".format(a,a2,a5)
m = min(a2,a5)
(a2,a5) = (a2-m,a5-m)
print "a={0} * 2^{1} * 5^{2}".format(a,a2,a5)
print "a=", expand(a,a2,a5)

sys.exit()




(b, b2, b5) = (1, 0, 0)
for i in xrange(2):
    b = (a*b) % 100000
    b2 += a2
    b5 += a5
    print "    b={0} * 2^{1} * 5^{2}".format(b,b2,b5)
    print "    b =", expand(b,b2,b5)

(b,b2,b5) = expand(b,b2,b5)
print "b={0} * 2^{1} * 5^{2}".format(b,b2,b5)





bp = 2
while b2:
    if odd(b2):
        b2 -= 1
        b = (b*bp) % 100000
    else:
        bp = bp**2 % 100000
        b2 /= 2
    #print "    ap={0}, a2={1}, a={2} * {0}^{1}".format(ap,a2,a)
print "b={0} * 2^{1} * 5^{2}".format(b,b2,b5)

print "f(XXX,XXY)={0}".format(b)
if (s != b):  print "Error"




print "########################################"
# c = a^1,000,000
c = 1
ct = 2
for i in xrange(ct):
    c = c * a
    c = c % 100000

print "c={0}".format(c)
print "f({0})={1}".format(a*ct,c)

print "Answer =", c
print "Time taken = {0} seconds".format(time.clock() - start_time)
