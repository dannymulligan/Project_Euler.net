#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 146
#
# Investigating a Prime Pattern
#
# The smallest positive integer n for which the numbers n^2+1, n^2+3,
# n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The
# sum of all such integers n below one-million is 1242490.
#
# What is the sum of all such integers n below 150 million?
#
#
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

# We only have to check even values of n.  Odd values of N will yield
# odd numbers when squared.  Adding one to an odd number will produce
# an even number so n^2+1 will not be a prime.
#
# We only have to check multiples of 10 for n.  Any other values of n
# will produce an n^2 that is not a multiple of 10.  Any n^2 that is
# not a multiple of 10 will cause one of n^2+1, n^2+3, n^2+7 or n^2+9
# to equal a number ending in 5, which will not be a prime.  The only
# way that all of n^2+1, n^2+3, n^2+7 and n^2+9 can be prime is if n^2
# is a multiple of 10.

# This program is able to search to 22 million in 62 seconds. This is
# about 2.4x faster than the previous version.  I need to make it
# about 6-7x faster.
#
# bash-3.2$ ./prob_146b.py
# There are 1389261 primes less than 22000000
# The highest prime is 21999977
# Time taken to calculate primes = 19.972296 seconds
# n = 10: n^2+1=101, n^2+3=103, n^2+7=107, n^2+9=109, n^2+13=113, n^2+27=127
# n = 315410: n^2+1=99483468101, n^2+3=99483468103, n^2+7=99483468107, n^2+9=99483468109, n^2+13=99483468113, n^2+27=99483468127
# n = 927070: n^2+1=859458784901, n^2+3=859458784903, n^2+7=859458784907, n^2+9=859458784909, n^2+13=859458784913, n^2+27=859458784927
# Calculating 1000000, last 1,000,000 numbers took 2.099911 seconds.
# Calculating 2000000, last 1,000,000 numbers took 1.490861 seconds.
# n = 2525870: n^2+1=6380019256901, n^2+3=6380019256903, n^2+7=6380019256907, n^2+9=6380019256909, n^2+13=6380019256913, n^2+27=6380019256927
# Calculating 3000000, last 1,000,000 numbers took 1.940095 seconds.
# Calculating 4000000, last 1,000,000 numbers took 1.595942 seconds.
# Calculating 5000000, last 1,000,000 numbers took 1.388836 seconds.
# Calculating 6000000, last 1,000,000 numbers took 1.379084 seconds.
# Calculating 7000000, last 1,000,000 numbers took 1.415199 seconds.
# Calculating 8000000, last 1,000,000 numbers took 1.461728 seconds.
# n = 8146100: n^2+1=66358945210001, n^2+3=66358945210003, n^2+7=66358945210007, n^2+9=66358945210009, n^2+13=66358945210013, n^2+27=66358945210027
# Calculating 9000000, last 1,000,000 numbers took 2.413751 seconds.
# Calculating 10000000, last 1,000,000 numbers took 2.4782 seconds.
# Calculating 11000000, last 1,000,000 numbers took 2.431019 seconds.
# Calculating 12000000, last 1,000,000 numbers took 1.375987 seconds.
# Calculating 13000000, last 1,000,000 numbers took 1.556432 seconds.
# Calculating 14000000, last 1,000,000 numbers took 2.816427 seconds.
# Calculating 15000000, last 1,000,000 numbers took 1.469967 seconds.
# Calculating 16000000, last 1,000,000 numbers took 1.611538 seconds.
# n = 16755190: n^2+1=280736391936101, n^2+3=280736391936103, n^2+7=280736391936107, n^2+9=280736391936109, n^2+13=280736391936113, n^2+27=280736391936127
# Calculating 17000000, last 1,000,000 numbers took 3.17826 seconds.
# Calculating 18000000, last 1,000,000 numbers took 1.608938 seconds.
# Calculating 19000000, last 1,000,000 numbers took 1.370456 seconds.
# Calculating 20000000, last 1,000,000 numbers took 1.414993 seconds.
# Calculating 21000000, last 1,000,000 numbers took 3.268665 seconds.
# Answer =  28669650
# Time taken = 61.238925 seconds



import sys
import time

LIMIT_PRIME = 150000000
prime_table = [1]*LIMIT_PRIME  # table of smallest factor
primes = []

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

def is_prime(n):
    if (n > LIMIT_PRIME*LIMIT_PRIME):
        print "Error: checking n = {0}, which is larger than LIMIT_PRIME^2 (LIMIT_PRIME = {1})".format(n, LIMIT_PRIME)
        sys.exit()
    elif (n < LIMIT_PRIME):
        return (prime_table[n] == 1)
    else:
        for i in primes:
            if ((n % i) == 0):
                return False
            if (i*i > n):
                return True
        return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q0_prime(n):
    # Test for divisibility by first 10 primes
    for p in primes[0:10]:
        if (n == p): return True
        if (n%p == 0): return False
    return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q1_prime(n):
    # Test for divisibility by first 100 primes
    for p in primes[10:100]:
        if (n == p): return True
        if (n%p == 0): return False
    return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q2_prime(n):
    # Test for divisibility by first 1,000 primes
    for p in primes[100:1000]:
        if (n == p): return True
        if (n%p == 0): return False
    return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q3_prime(n):
    # Test for divisibility by first 10,000 primes
    for p in primes[1000:10000]:
        if (n == p): return True
        if (n%p == 0): return False
    return True

# Quick but not 100% accurate test for primeness
# If this test returns False, definitely not a prime
# If this test returns True, might be a prime
def q4_prime(n):
    # Test for divisibility by first 100,000 primes
    for p in primes[10000:100000]:
        if (n == p): return True
        if (n%p == 0): return False
    return True


start_time = time.clock()
calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "They are", primes
print "The highest prime is", primes[-1]
print "Time taken to calculate primes =", time.clock() - start_time, "seconds"

answer = 0
#answer = 10 + 315410 + 927070 + 2525870 + 8146100 # All solutions below n = 10 million

prev_time = time.clock()
#for n in xrange(10,22000000,10):
for n in xrange(10,150000000,10):
    if ((n % 1000000) == 0):
        curr_time = time.clock()
        print "Calculating {0}, last 1,000,000 numbers took {1} seconds.".format(n, curr_time-prev_time)
        prev_time = curr_time

    nn = n*n

    # Quick tests to disallow many numbers before we do the expensive primaility test
    if not(q0_prime(nn+1) & q0_prime(nn+3) & q0_prime(nn+7) & q0_prime(nn+9) & q0_prime(nn+13) & q0_prime(nn+27)):
        continue
    if not(q1_prime(nn+1) & q1_prime(nn+3) & q1_prime(nn+7) & q1_prime(nn+9) & q1_prime(nn+13) & q1_prime(nn+27)):
        continue
    if not(q2_prime(nn+1) & q2_prime(nn+3) & q2_prime(nn+7) & q2_prime(nn+9) & q2_prime(nn+13) & q2_prime(nn+27)):
        continue
    if not(q3_prime(nn+1) & q3_prime(nn+3) & q3_prime(nn+7) & q3_prime(nn+9) & q3_prime(nn+13) & q3_prime(nn+27)):
        continue
    if not(q4_prime(nn+1) & q4_prime(nn+3) & q4_prime(nn+7) & q4_prime(nn+9) & q4_prime(nn+13) & q4_prime(nn+27)):
        continue

    # Accurate but slow primaility test
    if not(is_prime(nn+1) & is_prime(nn+3) & is_prime(nn+7) & is_prime(nn+9) & is_prime(nn+13) & is_prime(nn+27)):
        continue

    # Make sure that the prime numbers are consecutive 
    if (is_prime(nn+5) | is_prime(nn+11) | is_prime(nn+15) | is_prime(nn+17) | is_prime(nn+19) | is_prime(nn+21) | is_prime(nn+23) | is_prime(nn+25)):
        continue

    print "n = {0}: n^2+1={1}, n^2+3={2}, n^2+7={3}, n^2+9={4}, n^2+13={5}, n^2+27={6}".format(n, (nn+1), (nn+3), (nn+7), (nn+9), (nn+13), (nn+27))
    answer += n



print "Answer = ", answer
print "Time taken =", time.clock() - start_time, "seconds"
sys.exit()


# bash-3.2$ time ./prob_146b.py
# There are 8444396 primes less than 150000000
# The highest prime is 149999957
# Time taken to calculate primes = 144.698415 seconds
# n = 10: n^2+1=101, n^2+3=103, n^2+7=107, n^2+9=109, n^2+13=113, n^2+27=127
# n = 315410: n^2+1=99483468101, n^2+3=99483468103, n^2+7=99483468107, n^2+9=99483468109, n^2+13=99483468113, n^2+27=99483468127
# n = 927070: n^2+1=859458784901, n^2+3=859458784903, n^2+7=859458784907, n^2+9=859458784909, n^2+13=859458784913, n^2+27=859458784927
# n = 2525870: n^2+1=6380019256901, n^2+3=6380019256903, n^2+7=6380019256907, n^2+9=6380019256909, n^2+13=6380019256913, n^2+27=6380019256927
# n = 8146100: n^2+1=66358945210001, n^2+3=66358945210003, n^2+7=66358945210007, n^2+9=66358945210009, n^2+13=66358945210013, n^2+27=66358945210027
# n = 16755190: n^2+1=280736391936101, n^2+3=280736391936103, n^2+7=280736391936107, n^2+9=280736391936109, n^2+13=280736391936113, n^2+27=280736391936127
# n = 39313460: n^2+1=1545548137171601, n^2+3=1545548137171603, n^2+7=1545548137171607, n^2+9=1545548137171609, n^2+13=1545548137171613, n^2+27=1545548137171627
# n = 97387280: n^2+1=9484282305798401, n^2+3=9484282305798403, n^2+7=9484282305798407, n^2+9=9484282305798409, n^2+13=9484282305798413, n^2+27=9484282305798427
# n = 119571820: n^2+1=14297420138112401, n^2+3=14297420138112403, n^2+7=14297420138112407, n^2+9=14297420138112409, n^2+13=14297420138112413, n^2+27=14297420138112427
# n = 121288430: n^2+1=14710883251864901, n^2+3=14710883251864903, n^2+7=14710883251864907, n^2+9=14710883251864909, n^2+13=14710883251864913, n^2+27=14710883251864927
# n = 130116970: n^2+1=16930425881980901, n^2+3=16930425881980903, n^2+7=16930425881980907, n^2+9=16930425881980909, n^2+13=16930425881980913, n^2+27=16930425881980927
# n = 139985660: n^2+1=19595985005635601, n^2+3=19595985005635603, n^2+7=19595985005635607, n^2+9=19595985005635609, n^2+13=19595985005635613, n^2+27=19595985005635627
# Answer =  676333270
# Time taken = 721.18391 seconds
# 
# real	12m12.150s
# user	12m7.382s
# sys	0m1.719s
# bash-3.2$ 
