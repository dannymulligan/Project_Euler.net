#!/usr/bin/python
#
# Project Euler.net Problem 53
#
# There are exactly ten ways of selecting three from five, 12345:
# 
#     123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# 
# In combinatorics, we use the notation,
#
#    5
#     C = 10
#      3
#
# In general,
#   
#    n        n!
#     C =   -----
#      r    r!(n-r)!
# where r <= n, n! = n x (n-1) ... x 3 x 2 x 1, and 0! = 1.
# 
# It is not until n = 23, that a value exceeds one-million:
#     23
#       C = 1,144,066.
#        10
# 
# How many, not necessarily distinct, values of
#    n
#     C
#      r
# for 1 <= n <= 100, are greater than one-million?
#
# Answer: 4075

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

def combinations(n,r):
    r = min(r, n-r)
    m = 1  # numerator
    d = 1  # denominator

    for i in range(r):
        m *= (n-i)
        d *= (r-i)
        g = gcd(m,d)
        if (g>1):
            m = m/g
            d = d/g

    if (d == 1):
        # print "combinations({0},{1}) = {2}".format(n, r, m)
        return m
    else:
        print "Error, denominator != 1"


answer = 0
for n in range(1,101):
    for r in range(1,n+1):
        c = combinations(n,r)
        if (c > 1000000):
            answer += 1
            print "    c({0},{1}) is {2}".format(n,r,c)
    if ((n % 10) == 0):
        print "{0}: found {1} combinations > 1,000,000 so far".format(n, answer)

print "Done - found {0} combinations > 1,000,000".format(answer)
