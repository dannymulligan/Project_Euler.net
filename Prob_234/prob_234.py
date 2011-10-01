#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 234
#
# Semidivisible numbers
#
# For an integer n >= 4, we define the lower prime square root of n,
# denoted by lps(n), as the largest prime <= sqrt(n) and the upper
# prime square root of n, ups(n), as the smallest prime >= sqrt(n).
#
# So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) =
# 37.
#
# Let us call an integer n >= 4 semidivisible, if one of lps(n) and
# ups(n) divides n, but not both.
#
# The sum of the semidivisible numbers not exceeding 15 is 30, the
# numbers are 8, 10 and 12.
#
# 15 is not semidivisible because it is a multiple of both lps(15) = 3
# and ups(15) = 5.
#
# As a further example, the sum of the 92 semidivisible numbers up to
# 1000 is 34825.
#
# What is the sum of all semidivisible numbers not exceeding
# 999966663333?
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

########################################
PROB_MAX = 999966663333
LIMIT_PRIME = 1000004

PROB_MAX = 1000
LIMIT_PRIME = 38

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
#print "primes =", primes
print "PROB_MAX={0}, MAX_PRIME={1}, LIMIT_PRIME^2-PROB_MAX={2}".format(PROB_MAX, primes[-1], primes[-1]**2-PROB_MAX)

########################################
answer = 0
count = 0
for i in xrange(len(primes)-1):
    (l_prime, u_prime) = (primes[i], primes[i+1])
    (l_limit, u_limit) = (l_prime**2 + 1, u_prime**2 -1)
    u_limit = min(PROB_MAX,u_limit)
    print "  Answer =", answer
    print "Checking from {0} to {1} ({2} numbers, covered by primes {3} & {4})".format(l_limit, u_limit, u_limit-l_limit+1, l_prime, u_prime)

    for i in xrange(l_limit, u_limit+1):
        (l_match, u_match) = ((i % l_prime) == 0, (i % u_prime) == 0)
        if ((l_match and not u_match) or (not l_match and u_match)):
            print "    {0} is semi-prime".format(i)
            answer += i
            count += 1

print "Anwer =", answer
print "There are {0} semi-divisible numbers".format(count)
print "Time taken = {0} seconds".format(time.clock() - start_time)

# sqrt(999966663333) ~= 999983^2
# 999983^2 = 999966000289

