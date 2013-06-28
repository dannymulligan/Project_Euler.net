#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 293
#
# Pseudo-Fortunate Numbers
#
# An even positive integer N will be called admissible, if it is a
# power of 2 or its distinct prime factors are consecutive primes.
#
# The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.
#
# If N is admissible, the smallest integer M > 1 such that N+M is
# prime, will be called the pseudo-Fortunate number for N.
#
# For example, N=630 is admissible since it is even and its distinct
# prime factors are the consecutive primes 2,3,5 and 7.
#
# The next prime number after 631 is 641; hence, the pseudo-Fortunate
# number for 630 is M=11.
#
# It can also be seen that the pseudo-Fortunate number for 16 is 3.
#
# Find the sum of all distinct pseudo-Fortunate numbers for admissible
# numbers N less than 10^9.
#
# Solved 06/28/13
# 177 problems solved
# Position #395 on level 7

#import numpy as np
#import scipy as sp
#import matplotlib as mpl

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

import sys
import time
start_time = time.clock()

########################################

#LIMIT_PRIME = 100      # There are 25 primes less than 100
#LIMIT_PRIME = 1000     # There are 168 primes less than 1,000
#LIMIT_PRIME = 10000    # There are 1,229 primes less than 10,000
#LIMIT_PRIME = 100000   # There are 9,592 primes less than 100,000
LIMIT_PRIME = 1000000  # There are 78,498 primes less than 1,000,000
#LIMIT_PRIME = 10000000  # There are 664,579 primes less than 10,000,000
#LIMIT_PRIME = 100000000  # There are 5,761,455 primes less than 100,000,000
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

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


calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME
print "The first 20 primes are", primes[:20]

########################################

#LIMIT_ADMISSABLE = 49  # There are 12 admissable numbers below 49
#LIMIT_ADMISSABLE = 100  # There are 18 admissable numbers below 100
#LIMIT_ADMISSABLE = 10**3  # There are 56 admissable numbers below 1000
#LIMIT_ADMISSABLE = 10**4  # There are 147 admissable numbers below 10000
#LIMIT_ADMISSABLE = 10**5  # There are 350 admissable numbers below 100000
#LIMIT_ADMISSABLE = 10**6  # There are 784 admissable numbers below 1000000
#LIMIT_ADMISSABLE = 10**7  # There are 1660 admissable numbers below 10000000
#LIMIT_ADMISSABLE = 10**8  # There are 3377 admissable numbers below 100000000
LIMIT_ADMISSABLE = 10**9  # There are 6656 admissable numbers below 1000 000 000

# There are 6509 admissable numbers above 10000 and below 1000000000
# There are 6306 admissable numbers above 100000 and below 1000000000
# There are 5872 admissable numbers above 1000000 and below 1000000000
# There are 4996 admissable numbers above 10000000 and below 1000000000
# There are 3279 admissable numbers above 100000000 and below 1000000000

a_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# We only need to use the first 10 primes, because any admissable number
# using the first 11 primes would have to be at least...
#     2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 = 200560490130 > 10^9

def admissable(limit, divisor_so_far, zeros_allowed, primes):
    #print "admissable({}, {}, {}, {})".format(limit, divisor_so_far, zeros_allowed, primes)

    # Recurse to shorter versions not using the last prime
    if (zeros_allowed & (len(primes) > 1)):
        for m in admissable(limit, divisor_so_far, True, primes[:-1]):
            yield m

    # Recurse to shorter versions with the last prime forced to be used
    if (len(primes) == 1):
        m = 1
        while ((divisor_so_far * (primes[-1]**m)) < limit):
            yield primes[-1]**m
            m += 1
    else:
        m = 1
        while ((divisor_so_far * (primes[-1]**m)) < limit):
            for x in admissable(limit, divisor_so_far*(primes[-1]**m), False, primes[:-1]):
                yield primes[-1]**m * x
            m += 1

admissable_numbers = []
for i in admissable(LIMIT_ADMISSABLE, 1, True, a_primes):
    admissable_numbers.append(i)

print "There are {} admissable numbers below {}".format(len(admissable_numbers), LIMIT_ADMISSABLE)
admissable_numbers.sort()
if (len(admissable_numbers) < 50):
    print admissable_numbers

big_admissable_numbers = []
for n in admissable_numbers:
    if (n > LIMIT_PRIME):
        big_admissable_numbers.append(n)
print "There are {} admissable numbers above {} and below {}".format(len(big_admissable_numbers), LIMIT_PRIME, LIMIT_ADMISSABLE)



########################################

def slow_test_prime(n):
    for p in primes:
        if ((n % p) == 0):
            return False
        if ((p * p) > n):
            return True


def test_prime(n):
    assert ((n % 2) == 1)
    if ((n != 3) & ((n % 3) == 0)):
        return False
    if ((n != 5) & ((n % 5) == 0)):
        return False
    if ((n != 7) & ((n % 7) == 0)):
        return False
    return slow_test_prime(n)


def pseudo_fortunate(n):
    assert ((n % 2) == 0)
    i = 3
    while not(test_prime(n+i)):
        i += 2
    return i


pseudo_fortunate_set = set()
for n in admissable_numbers:
    a = pseudo_fortunate(n)
    print "psuedo_fortunate({}) = {}".format(n, a)
    pseudo_fortunate_set.add(a)

print "pseudo_fortunate_set =", pseudo_fortunate_set
print "Answer = sum(pseudo_fortunate_set) =", sum(pseudo_fortunate_set)
print "Time taken = {0} seconds".format(time.clock() - start_time)
