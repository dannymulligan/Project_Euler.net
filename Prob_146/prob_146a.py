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

# We only have to check even values of N.  Odd values of N will yield
# odd numbers when squared.  Adding one to an odd number will produce
# an even number so n^2+1 will not be a prime.


# This program is able to search to 9 million in 62 seconds. I need to
# make it about 15-16x faster.
#
# bash-3.2$ ./prob_146a.py 
# There are 602489 primes less than 9000000
# The highest prime is 8999993
# Time taken to calculate primes = 8.095391 seconds
# n = 10: n^2+1=101, n^2+3=103, n^2+7=107, n^2+9=109, n^2+13=113, n^2+27=127
# n = 315410: n^2+1=99483468101, n^2+3=99483468103, n^2+7=99483468107, n^2+9=99483468109, n^2+13=99483468113, n^2+27=99483468127
# n = 927070: n^2+1=859458784901, n^2+3=859458784903, n^2+7=859458784907, n^2+9=859458784909, n^2+13=859458784913, n^2+27=859458784927
# Calculating 1000000, last 1,000,000 numbers took 6.529287 seconds.
# Calculating 2000000, last 1,000,000 numbers took 5.812202 seconds.
# n = 2525870: n^2+1=6380019256901, n^2+3=6380019256903, n^2+7=6380019256907, n^2+9=6380019256909, n^2+13=6380019256913, n^2+27=6380019256927
# Calculating 3000000, last 1,000,000 numbers took 6.298078 seconds.
# Calculating 4000000, last 1,000,000 numbers took 5.929381 seconds.
# Calculating 5000000, last 1,000,000 numbers took 5.714539 seconds.
# Calculating 6000000, last 1,000,000 numbers took 5.689378 seconds.
# Calculating 7000000, last 1,000,000 numbers took 5.728071 seconds.
# Calculating 8000000, last 1,000,000 numbers took 5.770876 seconds.
# n = 8146100: n^2+1=66358945210001, n^2+3=66358945210003, n^2+7=66358945210007, n^2+9=66358945210009, n^2+13=66358945210013, n^2+27=66358945210027
# Answer =  11914460
# Time taken = 62.332171 seconds


import sys
import time

LIMIT_PRIME = 9000000
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
for n in xrange(2,9000000,2):
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
