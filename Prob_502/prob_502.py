#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 502
#
#
#
#
#
#
#
#
#
#
#
#
#
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

############################################################

############################################################

print("Answer = {}".format(answer))
print "Time taken = {0} seconds".format(time.clock() - start_time)
