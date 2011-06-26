#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 134
#
# Finding the smallest positive integer related to any pair of
# consecutive primes.
#
# Consider the consecutive primes p1 = 19 and p2 = 23. It can be
# verified that 1219 is the smallest number such that the last digits
# are formed by p1 whilst also being divisible by p2.
#
# In fact, with the exception of p1 = 3 and p2 = 5, for every pair of
# consecutive primes, p2 > p1, there exist values of n for which the
# last digits are formed by p1 and n is divisible by p2. Let S be the
# smallest of these values of n.
#
# Find sum(S) for every pair of consecutive primes with 5 <= p1 <=
# 1000000.
#
# Answer: 18613426663617118
# Solved 06/18/11
# 141 problems solved
# Position #202 on level 3

import time
import sys

start_time = time.clock()

#LIMIT_PRIME = 100
#LIMIT_PRIME = 1000
#LIMIT_PRIME = 10000
#LIMIT_PRIME = 100000
LIMIT_PRIME = 1000004
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
print "4 largest primes =", primes[-4:]


def step_size(n):
    if   (n < 10         ):  return 10
    elif (n < 100        ):  return 100
    elif (n < 1000       ):  return 1000
    elif (n < 10000      ):  return 10000
    elif (n < 100000     ):  return 100000
    elif (n < 1000000    ):  return 1000000
    elif (n < 10000000   ):  return 10000000
    elif (n < 100000000  ):  return 100000000
    elif (n < 1000000000 ):  return 1000000000
    elif (n < 10000000000):  return 10000000000


def mod_inv(x, y):
    if (y >= x):
        print "Error in mod_inv function"
        sys.exit()

    #print "     a      b      d      k"
    (a1, b1, d1) = (1, 0, x)
    (a0, b0, d0) = (0, 1, y)
    k0 = d1 / d0
    #print "{0:6} {1:6} {2:6}".format(a1, b1, d1)
    #print "{0:6} {1:6} {2:6} {3:6}".format(a0, b0, d0, k0)

    while (d0 != 1):
        (a2, b2, d2) = (a1, b1, d1)
        (a1, b1, d1, k1) = (a0, b0, d0, k0)
        (a0, b0, d0) = (a2-k1*a1, b2-k1*b1, d2-k1*d1)
        k0 = d1 / d0
        #print "{0:6} {1:6} {2:6} {3:6}".format(a0, b0, d0, k0)
    if (a0 < 0):  a0 += y
    if (b0 < 0):  b0 += x
    #print a0, b0
    return (a0, b0)


def try_out_euler(p1, p2):
    #print "testing p1 = {0}, p2 = {1}.  ".format(p1, p2), 
    step = step_size(p1)
    if (step > p2):
        (a, b) = mod_inv(step,p2)
    else:
        (b, a) = mod_inv(p2,step)

    n = p1 * b * p2
    n = n % (p2 * step)
    #print "...n = {0}".format(n)
    return n


answer = 0
pcount = 0
prev_time = time.clock()

for i in range(2,len(primes)-1):
    pcount += 1
    p1 = primes[i]
    p2 = primes[i+1]
    n = try_out_euler(p1, p2)
    answer += n
    if ((pcount % 1000) == 0):
        now_time = time.clock()
        print "{0}: p1 = {1}, p2 = {2}.  n = {3}.  answer = {4}.  Time taken = {5}.  Total time = {6}".format(pcount, p1, p2, n, answer, now_time - prev_time, now_time - start_time)
        prev_time = now_time

print "Answer =", answer
print "Time taken =", time.clock() - start_time, "seconds"


# Worked example for 181 and 191
# 
# From the Chinese Remainder Theorem, we need to find n such that
#     n = 181 (mod 1,000)
#     n = 0 (mod 191)
# 
# Use the Extended Euclidean algorithm to find inverses in modular arithmetic
# a      b      d      k
# 1      0      1,000
# 0      1      191    5
# 1      -5     45     4
# -4     21     11     4
# 17     -89    1      1
# 
# 17 = inverse 1,000 in modulus 191
# -89 = 911 = inverse 191 in modulus 1,000
# 
# Now we can find n such that
#     n = 1 (mod 1,000)
#     n = 0 (mod 191)
# as follows
#     911 * 191 = 174,001 = 1 (mod 1,000)
# so multiply by 181 to find our answer
#     n = 181 (mod 1,000)
#     n = 0 (mod 191)
# as follows
#     181 * 911 * 191 = 31,494,181 = 181 (mod 1,000)
# reduce to the smallest value that satisifies the constraint
#     31,494,181 = 170,181 (mod 1,000 * 191)
# which gives our answer
#     n = 170,181
