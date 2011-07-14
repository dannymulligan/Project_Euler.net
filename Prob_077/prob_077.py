#!/usr/bin/python
#
# Project Euler.net Problem 77
#
# It is possible to write ten as the sum of primes in exactly five different ways:
# 
#     7 + 3
#     5 + 5
#     5 + 3 + 2
#     3 + 3 + 2 + 2
#     2 + 2 + 2 + 2 + 2
# 
# What is the first value which can be written as the sum of primes in over five thousand different ways?
# 

import sys

def primes(n): 
    if (n == 2):
        return [2]
    elif (n < 2):
        return []

    s = range(3, n+1, 2)
    mroot = n ** 0.5
    half = (n+1)/2-1
    i = 0
    m = 3
    while (m <= mroot):
        if s[i]:
            j = (m*m - 3)/2
            s[j] = 0
            while (j < half):
                s[j] = 0
                j += m
        i = i + 1
        m = 2*i + 3
    return [2] + [x for x in s if x]


def ways_p(d, n, m, l):
#     print "ways(%d, %d, %d, %s)" % (d, n, m, l)

    if (n < 2):
        return 0  # no solution possible

    ans = 0
    for i in range(1, min(m,n)+1):
#         if i in prime_list:
#             print "trying %d, prime" % (i)
#         else:
#             print "trying %d, not prime" % (i)
        if i in prime_list:
            if (i == n):
                ans += 1
                ltmp = l + [i]
#                print "solution = %s" % ltmp
            if ((n-i) != 0):
                tmp = ways_p(d+1, n-i, min(i,m), l + [i])
                ans += tmp

#     print "ways(%d, %d, %d, %s) = %d" % (d, n, m, l, ans)
    return ans


prime_list = primes(2000)

# i = 12
# c = ways_p(0, i, i, [])
# print "ways_p(0, %d, %d) = %d" % (i, i, c)

max_c = 0
for i in range (2,100):
    c = ways_p(0, i, i, [])
    if (c > max_c):
        max_c = c
        print "%d can be written in %d different ways." % (i, c)
    if (c > 5000):
        print "Solution found = %d\n" % i
        sys.exit()
