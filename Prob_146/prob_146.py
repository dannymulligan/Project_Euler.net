#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 146
#
# Investigating a Prime Pattern
#
# The smallest positive integer n for which the numbers n^2+1, n^2+3,
# n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The
# sum of all such integers n below one-million is 1242490.
#
# What is the sum of all such integers n below 150 million?
#
#
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import time

MAX = 10000000
LIMIT_PRIME = MAX/2
prime_table = [1]*LIMIT_PRIME  # table of smallest factor
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

def is_prime(n):
    if (n < LIMIT_PRIME):
        return (prime_table[n] == 1)
    else:
        for i in range(2,LIMIT_PRIME):
            if (prime_table[i] == 1):
                if ((n % i) == 0):
                    return False
        return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q0_prime(n):
    # Test for divisibility by first 10 primes
    for p in primes[0:10]:
        if (n == p): return True
        if (n%p == 0): return False
    return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q1_prime(n):
    # Test for divisibility by first 100 primes
    for p in primes[10:100]:
        if (n == p): return True
        if (n%p == 0): return False
    return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q2_prime(n):
    # Test for divisibility by first 1,000 primes
    for p in primes[100:1000]:
        if (n == p): return True
        if (n%p == 0): return False
    return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q3_prime(n):
    # Test for divisibility by first 10,000 primes
    for p in primes[1000:10000]:
        if (n == p): return True
        if (n%p == 0): return False
    return True


start_time = time.clock()
calculate_primes()
print "MAX =", MAX
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "They are", primes
print "The highest prime is", primes[-1]
print "Time taken to calculate primes =", time.clock() - start_time, "seconds"

answer = 0
for n in xrange(2,1000000,2):
    if ((n % 100000) == 0):  print n

    nn = n*n

    # Quick tests to disallow many numbers before we do the expensive primaility test
    if not(q0_prime(nn+1) & q0_prime(nn+3) & q0_prime(nn+7) & q0_prime(nn+9) & q0_prime(nn+13) & q0_prime(nn+27)):
        continue
    if not(q1_prime(nn+1) & q1_prime(nn+3) & q1_prime(nn+7) & q1_prime(nn+9) & q1_prime(nn+13) & q1_prime(nn+27)):
        continue
    if not(q2_prime(nn+1) & q2_prime(nn+3) & q2_prime(nn+7) & q2_prime(nn+9) & q2_prime(nn+13) & q2_prime(nn+27)):
        continue
    if not(q3_prime(nn+1) & q3_prime(nn+3) & q3_prime(nn+7) & q3_prime(nn+9) & q3_prime(nn+13) & q3_prime(nn+27)):
        continue

    # Accurate but slow primaility test
    if not(is_prime(nn+1) & is_prime(nn+3) & is_prime(nn+7) & is_prime(nn+9) & is_prime(nn+13) & is_prime(nn+27)):
        continue

    # Make sure that they prime numbers are consecutive 
    if (is_prime(nn+5) | is_prime(nn+11) | is_prime(nn+15) | is_prime(nn+17) | is_prime(nn+19) | is_prime(nn+21) | is_prime(nn+23) | is_prime(nn+25)):
        continue

    print "n = {0}: n^2+1={1}, n^2+3={2}, n^2+7={3}, n^2+9={4}, n^2+13={5}, n^2+27={6}".format(n, (nn+1), (nn+3), (nn+7), (nn+9), (nn+13), (nn+27))
    answer += n



print "Answer = ", answer
print "Time taken =", time.clock() - start_time, "seconds"
sys.exit()
