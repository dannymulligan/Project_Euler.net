#!/usr/bin/python
#
# Project Euler.net Problem 63
#
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
# 9-digit number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?
#

#
# 10^N will be an (N+1) digit number, '1' followed by N '0's.
# Therefore, solutions will be from some variation of X^N where X < 10

found = 0
for N in range(1,30):
    for X in range(1,10):
        result = X ** N
        length = len(str(result))
        if (length == N):
            found += 1
            print "{0}^{1} = {2}, length = {3}".format(X, N, result, length)

print "Found {0} solutions".format(found)
