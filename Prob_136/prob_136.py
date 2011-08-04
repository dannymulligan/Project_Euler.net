#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 136
#
# Discover when the equation x^2 − y^2 − z^2 = n has a unique
# solution.
#
# The positive integers, x, y, and z, are consecutive terms of an
# arithmetic progression. Given that n is a positive integer, the
# equation, x^2 − y^2 − z^2 = n, has exactly one solution when n = 20:
#
#     13^2 − 10^2 − 7^2 = 20
#
# In fact there are twenty-five values of n below one hundred for
# which the equation has a unique solution.
#
# How many values of n less than fifty million have exactly one
# solution?
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

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
#     z = 7, s = 3, so n = (3*3 - 7) * (3 + 7) = 2 * 10 = 20

import sys 
import time
import itertools

start_time = time.clock()

SIZE  = 50000000
#SIZE  = 5000000
#SIZE  = 500000
#SIZE  = 50000
#SIZE  = 100
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
print "Finished calculating primes up to {0} at time = {1} seconds".format(SIZE, (time.clock() - start_time))

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
for n in range(1,SIZE):
    solns = 0
    for d1 in divisors(n):
        d2 = n / d1
        if (((d1+d2) % 4) == 0):
            s = (d1 + d2)/4
            z = d2 - s
            if ((z > 0) & (s > 0)):
                solns += 1
        if (solns > 1):
            break
    if (solns == 1):
        ans += 1
        if ((ans % 1000) == 0):
            print "Found {0} solutions at n = {1}, time = {2}".format(ans, n, (time.clock() - start_time))
print "Answer = {0} values of n below {1} with exactly one solution".format(ans, SIZE)
print "Time taken =", time.clock() - start_time, "seconds"
