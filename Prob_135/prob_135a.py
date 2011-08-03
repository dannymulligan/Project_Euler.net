#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 135
#
# Determining the number of solutions of the equation
#     x^2 − y^2 − z^2 = n.
#
# Given the positive integers, x, y, and z, are consecutive terms of
# an arithmetic progression, the least value of the positive integer,
# n, for which the equation, x^2 − y^2 − z^2 = n, has exactly two
# solutions is n = 27:
# 
#     34^2 − 27^2 − 20^2 = 27
#     12^2 − 9^2 − 6^2 = 27
# 
# It turns out that n = 1155 is the least value which has exactly ten
# solutions.
# 
# How many values of n less than one million have exactly ten distinct
# solutions?
#
# Solved 08/03/11
# 153 problems solved
# Position #688 on level 4

# If we assume
#     x = z + 2*s
#     y = z + 1*s
#     z = z + 0*s
# Then...
#     n = x^2 - y^2 - z^2
#     n = (z+2s)^2 - (z+s)^2 - z^2
#     n = (z^2 + 4zs + 4s^2) - (z^2 + 2zs + s^2) - z^2
#     n = -z^2 + 2zs + 3s^2
#     n = -1 * (z^s - 2zs - 3s^2)
#     n = -1 * (z - 3s) * (z + s)
#     n = (3s - z) * (s + z)
#
# For the example above,
#     z = 6, s = 3, so n = (3*3 - 6) * (3 + 6) = 3 * 9 = 27
#     z = 20, s = 7, so n = (3*7 - 20) * (7 + 20) = 1 * 27 = 27

import sys 
import time
import itertools

start_time = time.clock()

SIZE  = 1000000
LIMIT_PRIME = SIZE
prime_table = [1]*LIMIT_PRIME  # table of largest factor

def calculate_primes():
    i = 2
    while (i < (LIMIT_PRIME/2)):
        if (prime_table[i] == 1):
            j = i*2
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += i
        i += 1

calculate_primes()

def divisors(n):
    powers = []
    factors = []
    nn = n
    prev_factor = 0
    prev_count = 0
    while (prime_table[nn] != 1):
        if (prev_factor == prime_table[nn]):
            prev_count += 1
        else:
            if (prev_count > 0):
                powers.append(range(prev_count+1))
                factors.append(prev_factor)
            prev_factor = prime_table[nn]
            prev_count = 1
        nn /= prime_table[nn]

    if (prev_factor == nn):
        prev_count += 1
        powers.append(range(prev_count+1))
        factors.append(prev_factor)
    else:
        if (prev_count > 0):
            powers.append(range(prev_count+1))
            factors.append(prev_factor)
        prev_factor = nn
        prev_count = 1
        powers.append(range(prev_count+1))
        factors.append(prev_factor)

    for i in itertools.product(*powers):
        result = 1
        for x in range(len(i)):
            result *= factors[x]**i[x]
        yield result


#print "divisors(27) =",
#for n in divisors(27):
#    print n,
#print
#
#print "divisors(28) =",
#for n in divisors(28):
#    print n,
#print
#
#print "divisors(281) =",
#for n in divisors(281):
#    print n,
#print
#
#print "divisors(2811) =",
#for n in divisors(2811):
#    print n,
#print
#
#print "divisors(12811) =",
#for n in divisors(12811):
#    print n,
#print
#
#print "divisors(3810) =",
#for n in divisors(3810):
#    print n,
#print
#
#print "divisors(99) =",
#for n in divisors(99):
#    print n,
#print
#
#print "divisors(297) =",
#for n in divisors(297):
#    print n,
#print

# n = d1 * d2 = (3s - z) * (s + z)
# d1 = 3s - z
# d2 = s + z
ans = 0
for n in range(1000,SIZE):
    solns = 0
    for d1 in divisors(n):
        d2 = n / d1
        if (((d1+d2) % 4) == 0):
            s = (d1 + d2)/4
            z = d2 - s
            if ((z > 0) & (s > 0)):
                solns += 1
                #print "{0}^2 - {1}^2 - {2}^2 = {3}".format((z+2*s), (z+s), z, n)
    if (solns == 10):
        print "Found {0} soluntions for n = {1}".format(solns,n)
        ans += 1
print "Answer =", ans
print "Time taken =", time.clock() - start_time, "seconds"
