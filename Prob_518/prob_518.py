#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 518
#
# Prime triples and geometric sequences
#
# Let S(n) = sum( a+b+c ) over all triples (a,b,c) such that:
#
#    a, b, and c are prime numbers.
#    a < b < c < n.
#    a+1, b+1, and c+1 form a geometric sequence.
#
# For example, S(100) = 1035 with the following triples:
#
#    ( 2,  5, 11),
#    ( 2, 11, 47),
#    ( 5, 11, 23),
#    ( 5, 17, 53),
#    ( 7, 11, 17),
#    ( 7, 23, 71),
#    (11, 23, 47),
#    (17, 23, 31),
#    (17, 41, 97),
#    (31, 47, 71),
#    (71, 83, 97)
#
#Find S(10^8).

                

import sys
import time
start_time = time.clock()

########################################
#examples = [(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71), (11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)]
#
#for example in examples:
#    (a, b, c) = example
#    print(a+1, b+1, c+1, (c+1)/(b+1), (b+1)/(a+1))

SIZE = 100    # Answer = 1035
#SIZE = 10**3  # Answer = 75019
#SIZE = 10**4  # Answer = 4225228 in 0.27 seconds
#SIZE = 4*10**4  # Answer = 48159907 in 3.05 seconds
#SIZE = 5*10**4  # Answer = 72290551 in 4.5 seconds
SIZE = 10**5  # Answer = 249551109 in 16.17 seconds
SIZE = 10**6  # Answer = 
#SIZE = 10**6
#SIZE = 10**8

LIMIT_PRIME = SIZE+1
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

############################################################
def calculate_primes(limit=LIMIT_PRIME):
    start_time = time.clock()
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
    print("There are {:,} primes less than {:,}, calculated in {:.2f} seconds".format(len(primes), limit, (time.clock() - start_time)))

calculate_primes(LIMIT_PRIME)


############################################################

Answer = 0
for ci in range(3, len(primes)):
    c = primes[ci]
    #print(c, end=':')
    for bi in range(ci-1, 0, -1):
        b = primes[bi]
        #print(b, end=', ')

        #if (b+1)*(b+1) < (c+1):
        #    break

        if (((b+1)*(b+1) % (c+1)) == 0):
            a = (b+1)*(b+1) // (c+1) - 1
            if (prime_table[a] == 1) & (a > 1):
                #print((a, b, c))
                Answer += a + b + c
    #print()

print("Answer = {}".format(Answer))
    
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
