#!/usr/bin/python
#
# Project Euler.net Problem 108
#
# In the following equation x, y, and n are positive integers.
#
#     1     1     1
#    --- + --- = ---
#     x     y     n
#
# For n = 4 there are exactly three distinct solutions:
#
#     1      1     1
#    --- + ---- = ---
#     5     20     4
#
#     1      1     1
#    --- + ---- = ---
#     6     12     4
#
#     1     1     1
#    --- + --- = ---
#     8     8     4
#
# What is the least value of n for which the number of distinct
# solutions exceeds one-thousand?
#
# NOTE: This problem is an easier version of problem 110; it is
# strongly advised that you solve this one first.
#
# Solved: 07/03/11
# 143 problems solved
# Position #139 on level 3

# Prime factors of 180180 are
# 2^2, 3^2, 5, 7, 11, 13
#

#
#     1     1     1
#    --- + --- = ---
#     x     y     n
#
# Restate as
#
#     1     1     1
#    --- + --- = ---
#    n+a   n+b    n
#
# for a > 0 and b > a
#
# Therefore
#
#    (n+b) + (n+a)    1
#    ------------- = ---
#     (n+a)*(n+b)     n
#
#        2n + a + b        1
#    ------------------ = ---
#    n^2 + na + nb + ab    n
#
#    2n^2 + an + bn = n^2 + na + nb + ab
#
#    n^2 = ab
#
# Thus the number of solutions for the original equation is equal to
# the number of factors of n^2.  Our goal is to find n such that
# number n^2 has a lot of divisors - the first n where n^2 has > 1000
# divisors is our answer.
#
# We will search highly composite numbers to find the first M which
# >1000 factors, and then backtrack to see if there is an integer n
# where n^2 = M
#
# From: http://mathworld.wolfram.com/HighlyCompositeNumber.html
#
# If
#     N=2^(a_2) 3^(a_3) ... p^(a_p) 	(1)
# is the prime factorization of a highly composite number, then
#
# 1. The primes 2, 3, ..., p form a string of consecutive primes,
#
# 2. The exponents are nonincreasing, so a_2>=a_3>=...>=a_p, and
#
# 3. The final exponent a_p is always 1, except for the two cases
# N=4=2^2 and N=36=2^2 * 3^2, where it is 2.


import sys

# 25 primes < 100
#pr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 8 primes < 20
pr = [2, 3, 5, 7, 11, 13, 17, 19]

def hcn(pow):
    ans = 1
    for p in range(len(pow)):
        ans *= (pr[p]**pow[p])
    return ans

nums = []
nums.append(hcn([0,0,0,0, 0,0]))

nums.append(hcn([1,0,0,0, 0,0]))
nums.append(hcn([1,1,0,0, 0,0]))
nums.append(hcn([1,1,1,0, 0,0]))
nums.append(hcn([1,1,1,1, 0,0]))
nums.append(hcn([1,1,1,1, 1,0]))
nums.append(hcn([1,1,1,1, 1,1]))

nums.append(hcn([2,0,0,0, 0,0]))
nums.append(hcn([2,1,0,0, 0,0]))
nums.append(hcn([2,1,1,0, 0,0]))
nums.append(hcn([2,1,1,1, 0,0]))
nums.append(hcn([2,1,1,1, 1,0]))
nums.append(hcn([2,1,1,1, 1,1]))

nums.append(hcn([2,2,0,0, 0,0]))
nums.append(hcn([2,2,1,0, 0,0]))
nums.append(hcn([2,2,1,1, 0,0]))
nums.append(hcn([2,2,1,1, 1,0]))
nums.append(hcn([2,2,1,1, 1,1]))

nums.append(hcn([2,2,2,0, 0,0]))
nums.append(hcn([2,2,2,1, 0,0]))
nums.append(hcn([2,2,2,1, 1,0]))
nums.append(hcn([2,2,2,1, 1,1]))

nums.append(hcn([2,2,2,2, 0,0]))
nums.append(hcn([2,2,2,2, 1,0]))
nums.append(hcn([2,2,2,2, 1,1]))

nums.append(hcn([2,2,2,2, 2,0]))
nums.append(hcn([2,2,2,2, 2,1]))

nums.append(hcn([2,2,2,2, 2,2]))

nums.sort()

print nums

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

mcnt = 0
for n in nums:
    x = n + 1
    done = False
    acnt = 0
    while not done:
        #num = (n*x)/gcd(n*x, x-n)
        div = (x-n)/gcd(n*x, x-n)
        if (div == 1):
            acnt += 1
            #y = n*x/(x-n)
            #print "    1/{0} + 1/{1} = 1/{2}".format(x, y, n)
            if (x >= n*2):
                done = True
        x += 1

    print "{0} answers found with n = {1}".format(acnt, n)
    if (acnt > mcnt):
        mcnt = acnt

    if (acnt > 1000):
        print "Answer =", n
        sys.exit()

