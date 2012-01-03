#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 365
#
# A huge binomial coefficient
#
# The binomial coeffient C(10^18,10^9) is a number with more than 9
# billion (9x10^9) digits.
#
# Let M(n,k,m) denote the binomial coefficient C(n,k) modulo m.
#
# Calculate M(10^18,10^9,p*q*r) for 1000<p<q<r<5000 and p,q,r prime.
#
# Solved ??/??/11
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
TOP = 5000
BOT = 1000
LIMIT_PRIME = TOP
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
pqr = []

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
            if ((i > BOT) & (i < TOP)):
                pqr.append(i)
        i += 1

calculate_primes()
print "There are", len(pqr), "primes greater than", BOT, "and less than", TOP
#print "They are", pqr

print "We will have {0} different cases to consider".format(len(pqr)*(len(pqr)-1)*(len(pqr)-2)/(3*2*1))

sys.exit()

########################################
poss = 0
for pi in range(2,len(pqr)):
    for qi in range(1,pi):
        for ri in range(0,qi):
            poss += 1
            print "{0}-{1}-{2} = {3} * {4} * {5} = {6}".format(pi,qi,ri, pqr[pi],pqr[qi],pqr[ri], pqr[pi]*pqr[qi]*pqr[ri])

print "Considered {0} possibilities".format(poss)
print "Time taken = {0} seconds".format(time.clock() - start_time)

