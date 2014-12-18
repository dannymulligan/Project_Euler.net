#!/usr/bin/python

import time

start_time = time.clock()

LIMIT_PRIME = 10000000
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

def calculate_primes(limit=LIMIT_PRIME):
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
    print "There are", len(primes), "primes less than", LIMIT_PRIME
    #print "primes =", primes

calculate_primes(LIMIT_PRIME)
print "Run time =", (time.clock() - start_time), "seconds"
