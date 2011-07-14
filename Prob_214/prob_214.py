#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 214
#
# Totient Chains
#
# Let phi be Euler's totient function, i.e. for a natural number n,
# phi(n) is the number of k, 1 <= k <= n, for which gcd(k,n) = 1.
#
# By iterating φ, each positive integer generates a decreasing chain
# of numbers ending in 1.
#
# E.g. if we start with 5 the sequence 5,4,2,1 is generated.
#
# Here is a listing of all chains with length 4:
#     5,4,2,1
#     7,6,2,1
#     8,4,2,1
#     9,6,2,1
#     10,4,2,1
#     12,4,2,1
#     14,6,2,1
#     18,6,2,1
#
# Only two of these chains start with a prime, their sum is 12.
# 
# What is the sum of all primes less than 40000000 which generate a
# chain of length 25?
#
# Solved 07/10/10
# 148 problems solved
# Position #39 on level 3

import sys

import time
start_time = time.clock()

LIMIT_PRIME = 40000000
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
LENGTH = 25

def calculate_primes():
    i = 2
    while (i < (LIMIT_PRIME/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i*2
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += i
        i += 1
    while (i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 1

totient_cache = [0]*(LIMIT_PRIME+1)
def totient(n):
    if (totient_cache[n] != 0):
        return totient_cache[n]

    nn = n
    factors = []
    while (prime_table[nn] != 1):
        if not (prime_table[nn] in factors):
            factors.append(prime_table[nn])
        nn /= prime_table[nn]

    if not (nn in factors):
        factors.append(nn)
    nn /= nn

    ans_num = n
    ans_dem = 1
    for x in factors:
        ans_num *= (x-1)
        ans_dem *= x

    totient_cache[n] = ans_num/ans_dem
    return ans_num/ans_dem


calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME

ans = 0
max_len = 0
for p in primes:
    len = 1
    pp = p
    while (pp != 1):
        len += 1
        pp = totient(pp)
    if (len > max_len):
        max_len = len
        print "Found a totient chain starting with {0} with a length of {1}".format(p, len)
    if (len == LENGTH):
        print "The totient chain starting with {0} with a length of {1}".format(p, len)
        ans += p

print "Answer =", ans
print "Time taken =", time.clock() - start_time, "seconds"
