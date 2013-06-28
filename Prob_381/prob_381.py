#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 381
#
# (prime-k) factorial
#
# For a prime p let S(p) = ((p-k)!) mod(p) for 1<=k<=5.
#
# For example, if p=7,
#     (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)!
#   = 6! + 5! + 4! + 3! + 2!
#   = 720+120+24+6+2
#   = 872.
# As 872 mod(7) = 4, S(7) = 4.
#
# It can be verified that S(p) = 480 for 5<=p<=100.
#
# Find S(p) for 5<=p<=10^8.
#
# Solved ??/??/12
# ?? problems solved
# Position #??? on level ?

#import numpy as np
#import scipy as sp
#import matplotlib as mpl

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

import sys
import time
start_time = time.clock()

########################################
########################################
LIMIT_PRIME = 20
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
#prime_table = [1,2]*(LIMIT_PRIME/2)  # table of largest factor
#primes = [2]

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
print prime_table

print "Time taken = {0} seconds".format(time.clock() - start_time)

