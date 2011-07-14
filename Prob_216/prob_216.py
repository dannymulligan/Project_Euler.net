#!/usr/bin/python
#
# Project Euler.net Problem 216
#
# Investigating the primality of numbers of the form 2n^2-1
#
# Consider numbers t(n) of the form t(n) = 2n^(2)-1 with n > 1.
# The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
# It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
# For n <= 10000 there are 2202 numbers t(n) that are prime.
# 
# How many numbers t(n) are prime for n <= 50,000,000 ?
#
# Solved ??/??/09
# ?? problems solved
# Position #??? on level ?

import sys
import time

N = 100      # Answer = 45 out of 100, total time taken = 0.000621 seconds
#N = 10000    # Answer = 2202 out of 10000, total time taken = 0.628397 seconds
#N = 100000   # Answer = 17185 out of 100000, total time taken = 35.386885 seconds
#N = 1000000  # Answer = 141444 out of 1000000, total time taken = 2323.737389 seconds
#N = 50000000
#N = 9  # Answer should be 6

MAX = 2*N*N-1
LIMIT_PRIME = 1+int(MAX**.5)
prime_table = [1]*LIMIT_PRIME  # table of largest factor
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

def t(n):
    return 2*n*n-1

start_time = time.clock()
calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "They are", primes
print "The highest prime is", primes[-1]
print "Time taken to calculate primes =", time.clock() - start_time, "seconds"

answer = 0
prev_time = time.clock()
for i in range(2,N+1):
    n = t(i)
    if (is_prime(n)):
        #print "i =", i, "n =", n, "is prime, answer =", answer
        answer += 1
    if ((i % 10000) == 0):
        curr_time = time.clock()
        print "Calculating {0}, last 10,000 numbers took {1} seconds.".format(i, curr_time-prev_time)
        prev_time = curr_time

print "Answer = {0} out of {1}, total time taken = {2} seconds".format(answer, i, time.clock() - start_time)
