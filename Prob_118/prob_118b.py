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
# Solved 11/27/12
# 175 problems solved
# Position #392 on level 7

import sys
import time
start_time = time.clock()

LIMIT_PRIME = 10**9 # ~? seconds
LIMIT_PRIME = 5*10**8 # ~216 seconds
LIMIT_PRIME = 2*10**8 # ~84.1 seconds
LIMIT_PRIME = 10**8 # ~40.9 seconds
#LIMIT_PRIME = 2*10**7 # ~7.9 seconds
#LIMIT_PRIME = 10**7 # ~3.9 seconds
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

def to_int(nums):
    res = 0
    for i in nums:
        res = 10*res + int(i)
    return res

def count_poss(llist, nums):
    #print "count_poss({0}, {1})".format(llist, nums)

    # split rset into 2 parts
    # the left part must convert to an integer greater than the largest number in llist
    # the right part must be capable of being larger then the left, this limits the left to half of the digits
    # if no right part is possible, because all of the digits are required for the left, then yield the answer
    import itertools

    # The next number in the list must be larger than lnum_min
    if (llist == []):  lnum_min = 0
    else:              lnum_min = llist[-1]

    # Given the size of lnum_min, we must take at least a minimum number of digits in next number
    if   (lnum_min < 10)    :  llen_min = 1
    elif (lnum_min < 100)   :  llen_min = 2
    elif (lnum_min < 1000)  :  llen_min = 3
    elif (lnum_min < 10000) :  llen_min = 4
    elif (lnum_min < 100000):  llen_min = 5
    else                    :  raise RunTimeError("Error: lnum_min of {0} is too large".format(lnum_min))

    # We can't take too many digits, otherwise the numbers to the right can never be big enough
    llen_max = len(nums)/2

    # Take some digits from nums, and recurse when they form a valid prime
    for llen in range(llen_min, llen_max+1):
        for lset in itertools.combinations(nums, llen):
            rset = (nums - set(lset))
            for l in itertools.permutations(lset):
                lnum = to_int(l)
                if (lnum < lnum_min):
                    continue
                if not(is_prime(lnum)):
                    continue
                for result in count_poss((llist + list([lnum])), rset):
                    yield result

    # Take all of the digits from nums, and yield results when they form a valid prime
    if ((sum(nums) % 3) == 0):
        # if the digits add up to a multiple of 3, then every possible number is divisible by 3
        pass
    else:
        for l in itertools.permutations(nums):
            lnum = to_int(l)
            if (lnum < lnum_min):
                continue
            if (is_prime(lnum)):
                yield (llist + list([lnum]))


prime_count = calculate_primes()
print "There are", prime_count, "primes less than", LIMIT_PRIME
print "Prime search took {0} seconds".format(time.clock() - start_time)
#print "Primes are..."
#for i in range(2,LIMIT_PRIME):
#    if (prime_table[i] == 1):
#        print i

nums = set(range(1,10))

answer = 0
for i in count_poss([], nums):
    print i
    answer += 1

print "Answer =", answer

print "Time taken = {0} seconds".format(time.clock() - start_time)


