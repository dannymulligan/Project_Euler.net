#!/usr/bin/python
#
# Project Euler.net Problem 111
# 
# Considering 4-digit primes containing repeated digits it is clear
# that they cannot all be the same: 1111 is divisible by 11, 2222 is
# divisible by 22, and so on. But there are nine 4-digit primes
# containing three ones:
# 
#     1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
# 
# We shall say that M(n, d) represents the maximum number of repeated
# digits for an n-digit prime where d is the repeated digit, N(n, d)
# represents the number of such primes, and S(n, d) represents the sum
# of these primes.
# 
# So M(4, 1) = 3 is the maximum number of repeated digits for a
# 4-digit prime where one is the repeated digit, there are N(4, 1) = 9
# such primes, and the sum of these primes is S(4, 1) = 22275. It
# turns out that for d = 0, it is only possible to have M(4, 0) = 2
# repeated digits, but there are N(4, 0) = 13 such cases.
# 
# In the same way we obtain the following results for 4-digit primes.
#     Digit,d   M(4,d)   N(4,d)    S(4,d)
#       0         2        13      67061
#       1         3        9       22275
#       2         3        1       2221
#       3         3        12      46214
#       4         3        2       8888
#       5         3        1       5557
#       6         3        1       6661
#       7         3        9       57863
#       8         3        1       8887
#       9         3        7       48073
# 
# For d = 0 to 9, the sum of all S(4, d) is 273700.
# 
# Find the sum of all S(10, d).
#
# Solved ??/??/10
# ??? problems solved
# Position #??? on level 3

import sys
import time
start_time = time.clock()

LIMIT_PRIME = 10**9 # ~? seconds
LIMIT_PRIME = 5*10**8 # ~216 seconds
LIMIT_PRIME = 2*10**8 # ~84.1 seconds
LIMIT_PRIME = 10**8 # ~40.9 seconds
LIMIT_PRIME = 5*10**7 # ~19.9 seconds
#LIMIT_PRIME = 2*10**7 # ~7.9 seconds
#LIMIT_PRIME = 10**7 # ~3.9 seconds
#LIMIT_PRIME = 10**6 # ~0.35 seconds
prime_table = [1]*LIMIT_PRIME  # table of largest factor

def calculate_primes():
    prime_table[0] = 0  # 0 is not a prime number
    prime_table[1] = 0  # 1 is not a prime number

    # Special case 2 = the only even prime
    pcnt = 1
    j = 4
    while (j < LIMIT_PRIME):
        prime_table[j] = 2
        j += 2

    # Deal with all the odd primes starting with 3
    i = 3
    while (i*i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            pcnt += 1
            j = i*3  # can skip i*2, already covered
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += 2*i
        i += 2

    # Keep counting if we want an accurate count
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

def rep_digit_primes(n, r, x):
    # n = number of digits in the number
    # r = repeating digit, x = number of repetitions
    import itertools

    poss_dig = set([range(1,10)])
    a = set([r])
    poss_dig = poss_dig - a
    for b in itertools.permutations(poss_dig, 

answer = 0
for a in rep_digit_primes(4, 1, 3):
    print a
    answer += 1

print "Answer =", answer
print "Time taken = {0} seconds".format(time.clock() - start_time)


