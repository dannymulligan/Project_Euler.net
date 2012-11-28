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

LIMIT_PRIME = 10**7 # ~4 seconds
#LIMIT_PRIME = 10**6 # ~0.35 seconds
prime_table = [1]*LIMIT_PRIME  # table of largest factor

def calculate_primes():
    pcnt = 1
    prime_table[0] = 0  # 0 is not a prime number
    prime_table[1] = 0  # 1 is not a prime number
    i = 2
    j = i*2
    while (j < LIMIT_PRIME):
        prime_table[j] = i
        j += i

    i = 3
    while (i*i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            pcnt += 1
            j = i*3
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += 2*i
        i += 2
    while (i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            pcnt += 1
        i += 2
    return pcnt

def is_prime(x):
    if (x < LIMIT_PRIME):
        return (prime_table[x] == 1)
    for i in range(2,LIMIT_PRIME):
        if (prime_table[i] == 1):
            if ((x % i) == 0):
                return False
        if (i*i > x):
            return True
    return True

def set_to_int(nums):
    res = 0
    for i in nums:
        res = 10*res + int(i)
    return res

def count_poss(nums):
    import itertools

    res = 0
    for llen in range(1,len(nums)):
        for lnum in itertools.combinations(nums,llen):
            lnum = set(lnum)
            rnum = (nums - lnum)
            lcnt = 0
            for l in itertools.permutations(lnum):
                if (is_prime(set_to_int(l))):
                    print "    {0}".format(set_to_int(l))
                    lcnt += 1
            if (lcnt != 0):
                rcnt = count_poss(rnum)
            else:
                rcnt = 0

            res = res + lcnt * rcnt
            print "{0} * {1}".format(lcnt, rcnt), "{0} * {1}".format(lnum, rnum)
    return res

prime_count = calculate_primes()
print "There are", prime_count, "primes less than", LIMIT_PRIME
#print "Primes are..."
#for i in range(2,LIMIT_PRIME):
#    if (prime_table[i] == 1):
#        print i

#for i in range(LIMIT_PRIME, 2*LIMIT_PRIME):
#    if (is_prime(i)):
#        print i

nums = set(range(1,10))
nums = set([3, 5])
answer = count_poss(nums)

print "Answer =", answer

print "Time taken = {0} seconds".format(time.clock() - start_time)


