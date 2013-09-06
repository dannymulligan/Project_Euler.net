#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 133
#
# Repunit nonfactors
#
# A number consisting entirely of ones is called a repunit. We shall
# define R(k) to be a repunit of length k; for example, R(6) = 111111.
#
# Let us consider repunits of the form R(10^n).
#
# Although R(10), R(100), or R(1000) are not divisible by 17, R(10000)
# is divisible by 17. Yet there is no value of n for which R(10^n)
# will divide by 19. In fact, it is remarkable that 11, 17, 41, and 73
# are the only four primes below one-hundred that can be a factor of
# R(10^n).
#
# Find the sum of all the primes below one-hundred thousand that will
# never be a factor of R(10^n).
#
# Solved 09/06/13
# 184 problems solved
# Position #244 on level 7

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

def A(n):
    res = 1
    num = 1
    while True:
        if (num < n):
            num = num*10 + 1
            res += 1
        num = num % n
        if (num == 0):
            return res

########################################

def factor_of_10_pow_n(x):
    while ((x % 5) == 0):
        x = x / 5
    while ((x % 2) == 0):
        x = x / 2
    return (x == 1)

########################################

print "########################################"

answer = 0
for p in primes:
    if ((p == 2) or (p == 5)):
        #print "A({}) = <undefined>".format(p),
        #print "can never be a factor of R(10^n)"
        answer += p
        continue

    a = A(p)
    if factor_of_10_pow_n(a):
        print "A({}) = {}".format(p, a),
        print "can be a factor of R(10^n)"
    else:
        #print "A({}) = {}".format(p, a),
        #print "can never be a factor of R(10^n)"
        answer += p

print "Answer = {}".format(answer)
print "Time taken =", time.clock() - start_time, "seconds"
