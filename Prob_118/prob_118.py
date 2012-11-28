#!/usr/bin/python
#
# Project Euler.net Problem 118
#
# Exploring the number of ways in which sets containing prime elements
# can be made.
# 
# Using all of the digits 1 through 9 and concatenating them freely to
# form decimal integers, different sets can be formed. Interestingly
# with the set {2,5,47,89,631}, all of the elements belonging to it
# are prime.
# 
# How many distinct sets containing each of the digits one through
# nine exactly once contain only prime elements?
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

LIMIT_PRIME = 10**7
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

def calculate_primes():
    i = 2
    #primes.append(i)
    j = i*2
    while (j < LIMIT_PRIME):
        prime_table[j] = i
        j += i

    i = 3
    while (i*i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            #primes.append(i)
            j = i*3
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += 2*i
        i += 2
    #while (i < LIMIT_PRIME):
    #    if (prime_table[i] == 1):
    #        primes.append(i)
    #    i += 1

def valid_prime(x):
    digits = list("{0:d}".format(x))
    dedupd = list(set(digits))
    digits.sort()
    dedupd.sort()
    return (digits == dedupd)

def build_valid_list():
    i = 2
    while (i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            if valid_prime(i):
                primes.append(i)
        i += 1
    

calculate_primes()
build_valid_list()
print "There are", len(primes), "primes less than", LIMIT_PRIME
print "They are primes =",
for p in primes:
    print p
print

print "Time taken = {0} seconds".format(time.clock() - start_time)


