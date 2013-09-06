#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 130
#
# Finding composite values, n, for which n−1 is divisible by the
# length of the smallest repunits that divide it.
#
# A number consisting entirely of ones is called a repunit. We shall
# define R(k) to be a repunit of length k; for example, R(6) = 111111.
#
# Given that n is a positive integer and GCD(n, 10) = 1, it can be
# shown that there always exists a value, k, for which R(k) is
# divisible by n, and let A(n) be the least such value of k; for
# example, A(7) = 6 and A(41) = 5.
#
# You are given that for all primes, p > 5, that p − 1 is divisible by
# A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.
#
# However, there are rare composite values for which this is also
# true; the first five examples being 91, 259, 451, 481, and 703.
#
# Find the sum of the first twenty-five composite values of n for
# which GCD(n, 10) = 1 and n − 1 is divisible by A(n).
#
# Solved 09/06/13
# 185 problems solved
# Position #233 on level 7

import sys
import time

########################################

LIMIT_PRIME = 100000
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

start_time = time.clock()
calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "They are", primes
print "The highest prime is", primes[-1]
print "Time taken to calculate primes =", time.clock() - start_time, "seconds"

########################################

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

########################################

def A(n):
    res = 1
    num = 1
    iter = 1
    while True:
        if (num < n):
            num = num*10 + 1
            res += 1
        num = num % n
        if (num == 0):
            return res
        iter += 1
        if (iter > n):
            return -1  # no solution found

########################################

print "########################################"

answers = []
p = 25
while (len(answers) < 25):
    #print "Testing p = {}".format(p)

    assert (p < LIMIT_PRIME)

    if (prime_table[p] == 1):
        # This number is prime, so skip
        p += 1
        continue

    ap = A(p)
    if ((ap > 0) and (((p-1) % ap) == 0)):
        print "when p = {}, A({}) = {}, and {} is divisible by {}".format(p, p, ap, p-1, ap)
        answers.append(p)

    p += 1

print "Answer = {}".format(sum(answers))
print "Time taken =", time.clock() - start_time, "seconds"
