#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 127
#
# Investigating the number of abc-hits below a given limit.
#
# The radical of n, rad(n), is the product of distinct prime factors
# of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
#
# We shall define the triplet of positive integers (a, b, c) to be an
# abc-hit if:
#
#    1. GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
#    2. a < b
#    3. a + b = c
#    4. rad(abc) < c
#
# For example, (5, 27, 32) is an abc-hit, because:
#
#    GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
#    5 < 27
#    5 + 27 = 32
#    rad(4320) = 30 < 32
#
# It turns out that abc-hits are quite rare and there are only
# thirty-one abc-hits for c < 1000, with sum(c) = 12523.
#
# Find sum(c) for c < 120000.
#
# Note: This problem has been changed recently, please check that you
# are using the right parameters.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

# a = 5; b = 27 = 3^3; c = 32 = 2^5
# 1. Since all three numbers are based on different primes, GCD will be 1
# 2. a < b; 5 < 27
# 3. a + b = c; 5 + 27 = 32
# 4. rad(5*27*32) = 5 * 3 * 2 = 30 < 32

import sys
import pdb
import cProfile
import time

start_time = time.clock()


MAX = 1000   # 31: (a,b,c) = (343,625,968), answer so far = 12523, time = 0.916671 seconds
MAX = 2000   # 40: (a,b,c) = (81,1600,1681), answer so far = 24423, time = 2.77918 seconds
MAX = 5000   # 80: (a,b,c) = (49,4864,4913), answer so far = 150401, time = 24.647695 seconds
MAX = 10000  # 120: (a,b,c) = (3125,6859,9984), answer so far = 441085, time = 105.277711 seconds
MAX = 120000
LIMIT_PRIME = 1+MAX
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
radicals = []


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


def calculate_radicals():
    radicals.append([])  # 0 has no factors
    for n in range(1,LIMIT_PRIME):
        factors = []
        while (prime_table[n] != 1):
            if prime_table[n] not in factors:
                factors.append(prime_table[n])
            n /= prime_table[n]
        if n not in factors:
            factors.append(n)

        radicals.append(factors)


def main():
    calculate_primes()
    calculate_radicals()

    ans = 0
    cnt = 0
    for c in range(1,MAX):
        for b in range(c/2,c):
            a = c - b
            if (a >= b): continue

            next = False
            factors_a = radicals[a]
            factors_b = radicals[b]
            factors_abc = list(factors_a)
            for i in factors_b:
                if i in factors_abc:
                    next = True
                    continue
                factors_abc.append(i)
            if (next):  continue

            factors_c = radicals[c]
            for i in factors_c:
                if i in factors_abc:
                    next = True
                    continue
                factors_abc.append(i)
            if (next):  continue

            rad_abc = 1
            for i in factors_abc:
                rad_abc *= i
            if (rad_abc > c):  continue

            ans += c
            cnt += 1
            now_time = time.clock()
            print "{0}: (a,b,c) = ({1},{2},{3}), answer so far = {4}, time = {5} seconds".format(cnt, a,b,c, ans, now_time - start_time)

    print "MAX =", MAX
    print "Answer =", ans, "Count =", cnt
    print "Time taken =", time.clock() - start_time, "seconds"

main()
#cProfile.run('main()')
