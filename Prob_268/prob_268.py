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

# When primes < 100 & NUM = 1000, the answer should be 23
# When primes < 100 & NUM = 10**4, the answer should be unique 811, duplicates 132, total 943
# When primes < 100 & NUM = 10**5, the answer should be unique 9,280, duplicates 6,346, total 15,626
# When primes < 100 & NUM = 10**6, the answer should be unique 77,579, duplicates 102,372, total 179,951
# When primes < 100 & NUM = 10**7, the answer should be unique 768,778, duplicates 1,077,659, total 1,846,437

# There are 8 primes less than 20
# They are [2, 3, 5, 7, 11, 13, 17, 19]

# When primes < 20 & NUM = 1000, the answer should be 
# When primes < 20 & NUM = 10**4, the answer should be unique , duplicates , total 
# When primes < 20 & NUM = 10**5, the answer should be unique , duplicates , total 
# When primes < 20 & NUM = 10**6, the answer should be unique , duplicates , total 
# When primes < 20 & NUM = 10**7, the answer should be unique , duplicates , total 

import itertools

#NUM = 10**16
NUM = 10**4
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
total_dup = 0
for i in itertools.combinations(primes,4):
    base = (i[0] * i[1] * i[2] * i[3])
    if (base > NUM):  continue

    print
    print "Evaluating i =", i
    divisors = NUM / base
    print "  total divisors =", divisors

    overlaps = 0
    for j in tried:
        print "  Looking for overlaps between i =", i, "and j =", j
        common = []
        i_only = []
        j_only = list(j)
        for ii in i:
            if ii in j:
                common.append(ii)
                j_only.remove(ii)
            else:
                i_only.append(ii)
        print "    common = ", common
        print "    i_only = ", i_only
        print "    j_only = ", j_only
        product = 1
        for n in common + i_only + j_only:
            product *= n
        print "    overlaps found =", NUM/product
        overlaps += NUM/product
    tried.append(i)
    print "  total overlaps =", overlaps
    total_all += divisors
    total_dup += overlaps

print "All =", total_all
print "duplicates =", total_dup

print "Unique =", total_all - total_dup
