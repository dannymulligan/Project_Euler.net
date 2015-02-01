#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 501
#
# Eight Divisors
#
# The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24.
#
# The ten numbers not exceeding 100 having exactly eight divisors are
# 24, 30, 40, 42, 54, 56, 66, 70, 78 and 88.
#
# Let f(n) be the count of numbers not exceeding n with exactly eight
# divisors.
#
# You are given f(100) = 10, f(1000) = 180 and f(10^6) = 224427.
#
# Find f(10^12).
#
# Solved ??/??/14
# ??? problems solved
# Position #??? on level ?

import time

LIMIT_PRIME = 10**6
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

############################################################
def calculate_primes(limit=LIMIT_PRIME):
    start_time = time.clock()
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    prime_table[i] = i
    primes.append(i)
    j = i**2
    while (j < limit):
        prime_table[j] = i
        j += i

    i = 3
    while (i < (limit/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i**2
            while (j < limit):
                prime_table[j] = i
                j += i
        i += 2
    while (i < limit):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 2
    print("There are {} primes less than {}, calculated in {} seconds".format(len(primes), limit, (time.clock() - start_time)))

calculate_primes(limit = 10**6)

import itertools

def pi(n):
    """Calculate the number of prime numbers less than n"""
    # First we need to find a list of the primes <= sqrt(n)
    # (We assume that calculate_primes() was already run)
    x = 1
    while (primes[x]**2 <= n):
        x += 1
    # Now, primes[x-1]^2 is the largest squared prime <= n
    print("Working with primes[:{}], primes[{}]^2 = {}".format(x, x-1, primes[x-1]**2))

    # Then we iterate through combinations of 1..x primes
    result = n-1+x
    for xn in range(0,x):
        print("result = {}, adjusting for combinations of {} primes".format(result, xn+1))
        iresult = 0
        looked_at = 0
        for pn in itertools.combinations(primes[:x], xn+1):
            looked_at += 1
            product = 1
            for ipn in pn:
                product *= ipn
                if product > n:
                    break
            if product > n:
                continue
            if n/product < 1:
                break
            iresult += n/product
        if iresult < 1:
            break
        if (xn % 2) == 0:
            result -= iresult
        else:
            result += iresult
        print("Looked at {} combinations".format(looked_at))
    return result

#for i in [1, 2, 3, 4, 5, 6, 7]:
for i in [1, 2, 3, 4, 5, ]:
    print("pi(10**{i}) = {pi}".format(i=i, pi=pi(10**i)))
