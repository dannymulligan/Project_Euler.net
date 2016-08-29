#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 549
#
# Divisibility of factorials
#
# The smallest number m such that 10 divides m! is m=5.
# The smallest number m such that 25 divides m! is m=10.
#
# Let s(n) be the smallest number m such that n divides m!.
# So s(10)=5 and s(25)=10.
#
# Let S(n) be Sum(s(i)) for 2 <= i <= n.
#
# S(100)=2012.
#
# Find S(10^8).
#
# Solved ??/??/15
# ?? problems solved
# Position #??? on level ?

#import numpy as np
#import matplotlib as mpl

import sys
import time
start_time = time.clock()
print("Running with python version {}".format(sys.version))


########################################
# Calculate a table of primes

LIMIT = 1 + 10**8
PrimeStartTime = time.clock()
prime_table = [1]*(LIMIT)  # table of largest factor
primes = []

def calculate_primes(limit=LIMIT):
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
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
    print("There are {:,} primes <= {:,}, calculated in {:.2f} seconds".format(len(primes), limit-1, (time.clock() - PrimeStartTime)))

calculate_primes(LIMIT)


############################################################
# Calculate factors

def factors_of(n):
    n_factors = dict()
    while n > 1:
        if prime_table[n] == 1:
            factor = n
        else:
            factor = prime_table[n]

        if factor in n_factors.keys():
            n_factors[factor] += 1
        else:
            n_factors[factor] = 1
        n //= factor

    return n_factors


############################################################
# Calculate s(i)

def factorial(n):
    answer = 1
    for i in range(2,n+1):
        answer *= i
    return answer

def s_slow(n):
    for j in range(2,n+1):
        if (factorial(j) % n) == 0:
            return j

def s_fast(n):
    if prime_table[n] == 1:
        return n
    else:
        best_answer = 1
        factors = factors_of(n)
        for prime in sorted(factors.keys()):
            power = factors[prime]

            mult = 1
            count = 1
            while count < power:
                mult += 1
                count += 1
                if mult % prime == 0:
                    m = mult
                    while m % prime == 0:
                        m //= prime
                        count += 1

            if prime*mult > best_answer:
                best_answer = prime*mult
            #print("    {n} has factor {p}^{pp} which means s({n}) >= {m}".format(n=n, p=prime, pp=power, m=prime*mult))

        return best_answer


############################################################
# Calculate the answer

Answer = 0
for i in range(2,LIMIT):
    s_result = s_fast(i)
    Answer += s_result
    #print("s({i}) = {s}".format(i=i, s=s_result))

print("Answer = {:,}".format(Answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))


# if i is a prime, then c(i) = i
# if i is not a prime, then iterate through each of the prime factors
# and find the smallest multiple of that prime factor needed to have
# more than the power number of that prime factor in the factorial,
# then take the largest of these results as the answer
