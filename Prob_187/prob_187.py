#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 187
#
# Semiprimes
#
# A composite is a number containing at least two prime factors. For
# example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
#
# There are ten composites below thirty containing precisely two, not
# necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22,
# 25, 26.
#
# How many composite integers, n < 10^(8), have precisely two, not
# necessarily distinct, prime factors?
#
# Solved 08/04/10
# 114 problems solved
# Position #900 on level 3


# MAX = 30
# There are 6 primes less than 15
# The highest prime is 13
# Answer = 10
# real	0m0.026s
# 
# MAX = 10000
# There are 669 primes less than 5000
# The highest prime is 4999
# Answer = 2625
# real	0m0.034s
# 
# MAX = 100000
# There are 5133 primes less than 50000
# The highest prime is 49999
# Answer = 23378
# real	0m0.112s
# 
# MAX = 1000000
# There are 41538 primes less than 500000
# The highest prime is 499979
# Answer = 210035
# real	0m0.931s
# 
# MAX = 10000000
# There are 348513 primes less than 5000000
# The highest prime is 4999999
# Answer = 1904324
# real	0m9.961s
# 
# MAX = 100000000
# There are 3001134 primes less than 50000000
# The highest prime is 49999991
# Answer = 17427258
# real	1m44.653s

MAX = 10**8
LIMIT_PRIME = MAX/2
prime_table = [1]*LIMIT_PRIME  # table of smallest factor
primes = []
tried = []

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
print "MAX =", MAX
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "They are", primes
print "The highest prime is", primes[-1]

answer = 0
for i in range(len(primes)):
    if ((primes[i]*primes[i]) <= MAX):
        answer += (i+1)
#        for j in range(i+1):
#            print primes[j], "*", primes[i], "=", primes[j]*primes[i]
    else:
        # find the maximum j, such that primes[j] * primes[i] < MAX
        j = 0
        k = i
        while ((k - j) > 1):
            p = (j + k)/2
            if (primes[p]*primes[i] < MAX):
                j = p
            else:
                k = p
        answer += (j+1)
#        for k in range(j+1):
#            print primes[i], "*", primes[k], "=", primes[i]*primes[k]

print "Answer =", answer
