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
import random

N = 150    #
#N = 10000    #
#N = 100000   #
#N = 1000000  #
#N = 50000000
#N = 9  # Answer should be 6

def fermat_primality_test(p):
    # True  = p might be prime
    # False = p is definitely not prime
    #
    # http://en.wikipedia.org/wiki/Fermat_primality_test
    # (a^(p-1) mod p) = 1 if p is prime
    a = random.randint(1,p-1)
    n = (a**(p-1) % p)
    if (n == 1):  return True
    else:         return False

def is_prime(n):
    for i in xrange(4):
        if (fermat_primality_test(n) == False):
            return False
    return True

def t(n):
    return 2*n*n-1

start_time = time.clock()

answer = 0
prev_time = time.clock()
for i in range(2,N+1):
    n = t(i)
    #print "trying i =", i, "n =", n, "answer =", answer
    if (is_prime(n)):
        print "i =", i, "n =", n, "is prime, answer =", answer
        answer += 1
    if ((i % 10000) == 0):
        curr_time = time.clock()
        print "Calculating {0}, last 10,000 numbers took {1} seconds.".format(i, curr_time-prev_time)
        prev_time = curr_time

print "Answer = {0} out of {1}, total time taken = {2} seconds".format(answer, i, time.clock() - start_time)
