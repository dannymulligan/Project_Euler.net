#!/usr/bin/python
#
# Project Euler.net Problem 69
# 
# Euler's Totient function, phi(n) [sometimes called the phi function],
# is used to determine the number of numbers less than n which are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
# less than nine and relatively prime to nine, phi(9)=6.
# 
#     n    Relatively Prime    phi(n)    n/phi(n)
#     2    1                   1         2
#     3    1,2                 2         1.5
#     4    1,3                 2         2
#     5    1,2,3,4             4         1.25
#     6    1,5                 2         3
#     7    1,2,3,4,5,6         6         1.1666...
#     8    1,3,5,7             4         2
#     9    1,2,4,5,7,8         6         1.5
#     10   1,3,7,9             4         2.5
# 
# It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.
# 
# Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
# 

import sys

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

def phi(n):
    ans = 0
    for i in range(n):
        if (gcd(i,n) == 1):
            ans += 1
    return ans

# # Testing code
# for i in range(2,11):
#     print i, phi(i)

max_nphi = 0.0

for n in range(1,1000001):
    if ((n % 1000) == 0):
        print "Trying n = %d, phi(%d) = %d, n/phi(n) = %f" % (n, n, phi(n), float(n)/phi(n))
    tmp = float(n)/phi(n)
    if (tmp > max_nphi):
        max_n = n
        max_nphi = tmp
        print "n = %d gives phi(n) = %d, n/phi(n) = %f" % (n, phi(n), tmp)

