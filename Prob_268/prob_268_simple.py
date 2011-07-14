#!/usr/bin/python
#
# Project Euler.net Problem 268
#
# Counting numbers with at least four distinct prime factors less than
# 100
#
# It can be verified that there are 23 positive integers less than
# 1000 that are divisible by at least four distinct primes less than
# 100.
#
# Find how many positive integers less than 10^(16) are divisible by
# at least four distinct primes less than 100.
#
# Solved ??/??/09
# ?? problems solved
# Position #??? on level ?

# There are 25 primes less than 100
# They are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# Selecting groups of 4 primes
# When primes < 100 & NUM = 1000, the answer should be 23
# When primes < 100 & NUM = 10**4, the answer should be unique 811, duplicates 132, total 943
# When primes < 100 & NUM = 10**5, the answer should be unique 9,280, duplicates 6,346, total 15,626
# When primes < 100 & NUM = 10**6, the answer should be unique 77,579, duplicates 102,372, total 179,951
# When primes < 100 & NUM = 10**7, the answer should be unique 768,778, duplicates 1,077,659, total 1,846,437

# There are 8 primes less than 20
# They are [2, 3, 5, 7, 11, 13, 17, 19]
# Selecting groups of 4 primes
# When primes < 20 & NUM = 10**3, the answer should be unique      19, total      19
# When primes < 20 & NUM = 10**4, the answer should be unique     304, total     392
# When primes < 20 & NUM = 10**5, the answer should be unique   2,769, total   4,243
# When primes < 20 & NUM = 10**6, the answer should be unique  27,901, total  42,733
# When primes < 20 & NUM = 10**7, the answer should be unique 278,941, total 427,662

# There are 8 primes less than 20
# They are [2, 3, 5, 7, 11, 13, 17, 19]
# Selecting groups of 6 primes
# When primes < 20 & NUM = 10**4, the answer should be unique       0, total       0
# When primes < 20 & NUM = 10**5, the answer should be unique      13, total      13
# When primes < 20 & NUM = 10**6, the answer should be unique     214, total     238
# When primes < 20 & NUM = 10**7, the answer should be unique   2,073, total   2,514
# When primes < 20 & NUM = 10**8, the answer should be unique  20,726, total  25,256
# When primes < 20 & NUM = 10**9, the answer should be unique 207,229, total 252,676

import itertools
import operator

#NUM = 10**16
NUM = 10**7
LIMIT_PRIME = 20
prime_table = [1]*LIMIT_PRIME  # table of largest factor
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
print "There are", len(primes), "primes less than", LIMIT_PRIME
print "They are", primes
total_all = 0
for i in itertools.combinations(primes,6):
    base = reduce(operator.mul, i)
    if (base > NUM):  continue

    divisors = NUM / base
    for x in range(divisors):
        print "    ", (x+1)*base, i, x+1

    total_all += divisors

print "All =", total_all

# Run with...
#     python prob_268_simple.py > xxx; grep "^    " xxx | sort -n > yyy; grep "^    " xxx | awk '{print $1}' | sort -n | uniq -c > zzz; wc yyy zzz
