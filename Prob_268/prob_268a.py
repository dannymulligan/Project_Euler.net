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
# Answer: 
# Solved 12/16/09
# 108 problems solved
# Position #927 on level 3


# bash-3.2$ time python prob_268a.py 
# There are 25 primes less than 100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# NUM = 10000000000000000
# div_excl_overlap(primes[0:8],4,NUM) = 785478606870985
# 
# real	376m0.836s
# user	373m45.577s
# sys	0m33.899s
# bash-3.2$ 


# Solutions from prob_268_simple.py...

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
import math

NUM = 10**16
LIMIT_PRIME = 100
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
# There are 25 primes less than 100
# They are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def selftest():
    print "Running selftest()"

    print "Testing div_incl_overlap with combinations of 4 primes"

    a = div_incl_overlap(primes[0:8],4,10**3)
    print "div_incl_overlap(primes[0:8],4,10**3) =", a
    if (a != 19):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],4,10**4)
    print "div_incl_overlap(primes[0:8],4,10**4) =", a
    if (a != 392):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],4,10**5)
    print "div_incl_overlap(primes[0:8],4,10**5) =", a
    if (a != 4243):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],4,10**6)
    print "div_incl_overlap(primes[0:8],4,10**6) =", a
    if (a != 42733):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],4,10**7)
    print "div_incl_overlap(primes[0:8],4,10**7) =", a
    if (a != 427662):  print "ERROR!"

    print "===="

    print "Testing div_incl_overlap with combinations of 6 primes"

    a = div_incl_overlap(primes[0:8],6,10**4)
    print "div_incl_overlap(primes[0:8],6,10**4) =", a
    if (a != 0):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],6,10**5)
    print "div_incl_overlap(primes[0:8],6,10**5) =", a
    if (a != 13):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],6,10**6)
    print "div_incl_overlap(primes[0:8],6,10**6) =", a
    if (a != 238):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],6,10**7)
    print "div_incl_overlap(primes[0:8],6,10**7) =", a
    if (a != 2514):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],6,10**8)
    print "div_incl_overlap(primes[0:8],6,10**8) =", a
    if (a != 25256):  print "ERROR!"

    a = div_incl_overlap(primes[0:8],6,10**9)
    print "div_incl_overlap(primes[0:8],6,10**9) =", a
    if (a != 252676):  print "ERROR!"

    print "===="

    print "Testing div_excl_overlap with combinations of 4 primes"

    a = div_excl_overlap(primes[0:8],4,10**3)
    print "div_excl_overlap(primes[0:8],4,10**3) =", a
    if (a != 19):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],4,10**4)
    print "div_excl_overlap(primes[0:8],4,10**4) =", a
    if (a != 304):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],4,10**5)
    print "div_excl_overlap(primes[0:8],4,10**5) =", a
    if (a != 2769):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],4,10**6)
    print "div_excl_overlap(primes[0:8],4,10**6) =", a
    if (a != 27901):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],4,10**7)
    print "div_excl_overlap(primes[0:8],4,10**7) =", a
    if (a != 278941):  print "ERROR!"

    print "===="

    print "Testing div_excl_overlap with combinations of 6 primes"

    a = div_excl_overlap(primes[0:8],6,10**4)
    print "div_excl_overlap(primes[0:8],6,10**4) =", a
    if (a != 0):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],6,10**5)
    print "div_excl_overlap(primes[0:8],6,10**5) =", a
    if (a != 13):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],6,10**6)
    print "div_excl_overlap(primes[0:8],6,10**6) =", a
    if (a != 214):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],6,10**7)
    print "div_excl_overlap(primes[0:8],6,10**7) =", a
    if (a != 2073):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],6,10**8)
    print "div_excl_overlap(primes[0:8],6,10**8) =", a
    if (a != 20726):  print "ERROR!"

    a = div_excl_overlap(primes[0:8],6,10**9)
    print "div_excl_overlap(primes[0:8],6,10**9) =", a
    if (a != 207229):  print "ERROR!"

    print "Finished selftest()"

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
print "There are", len(primes), "primes less than", LIMIT_PRIME, "=", primes
print "primes =", primes
print "NUM =", NUM

div_incl_overlap_cache = [0]*(len(primes)+1)

def div_incl_overlap (factors, fcnt, N):
    #print "=> div_incl_overlap(factors, {0}, N)".format(fcnt)
    result = 0
    product = reduce(operator.mul, factors[0:fcnt])  # calculate the smallest possible product
    if (product < N):                                # skip the calculations if this is > N
        for perm in itertools.combinations(factors, fcnt):
            product = reduce(operator.mul, perm)
            divs = N/product
            #print perm, product, divs
            result += divs
    #print "<- div_incl_overlap(factors, {0}, N) = {1}".format(fcnt, result)
    return result

div_excl_overlap_cache = [0]*(len(primes)+1)

def div_excl_overlap (factors, fcnt, N):
    #print "=> div_EXCL_overlap(factors, {0}, N)".format(fcnt)
    if (fcnt > len(factors)):
        result = 0
    else:
        result = div_incl_overlap(factors, fcnt, N)
        for x in range(fcnt+1,len(factors)+1):
            combinations = (math.factorial(x)/(math.factorial(x-fcnt)*math.factorial(fcnt)))
            result -= (combinations-1)*(div_excl_overlap(factors, x, N) - div_excl_overlap(factors, x+1, N))
    #print "<- div_EXCL_overlap(factors, {0}, N) = {1}".format(fcnt, result)
    return result

#answer = div_excl_overlap(primes, 4, NUM)
#print answer



#selftest()
#print "div_excl_overlap(primes,6,10**3) =", div_excl_overlap(primes,6,10**3)
#print "div_excl_overlap(primes,4,10**4) =", div_excl_overlap(primes,4,10**4)
#print "div_excl_overlap(primes[0:8],6,10**6) =", div_excl_overlap(primes[0:8],6,10**6), "(Expected answer is 214)"
#a = div_excl_overlap(primes[0:8],6,10**7)
#print "div_excl_overlap(primes[0:8],6,10**7) =", a, "(Expected answer is 2073)"

a = div_excl_overlap(primes,4,NUM)
print "div_excl_overlap(primes[0:8],4,NUM) =", a
