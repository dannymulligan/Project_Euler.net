#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 347
#
# Largest integer divisible by two primes
#
# The largest integer <= 100 that is only divisible by both the primes
# 2 and 3 is 96, as 96=32*3=25*3. For two distinct primes p and q let
# M(p,q,N) be the largest positive integer <=N only divisible by both
# p and q and M(p,q,N)=0 if such a positive integer does not exist.
#
# E.g. M(2,3,100)=96.
#
# M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
#
# Also M(2,73,100)=0 because there does not exist a positive integer
# <= 100 that is divisible by both 2 and 73.
#
# Let S(N) be the sum of all M(p,q,N). S(100)=2262.
#
# Find S(10 000 000).
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()
SIZE = 10000000

########################################
def M(p,q,n):
    a = p*q
    if (a > n):  return 0
    qp = 1
    pp = 1
    while (a <= n):
        a *= q
        qp += 1
    a /= q
    qp -= 1

    while (a <= n):
        a *= p
        pp += 1
    a /= p
    pp -= 1

    #print "a = {0} = {1}^{2} * {3}^{4}".format(a,p,pp,q,qp)

    best = a
    bestp = 1
    bestq = qp
    while (qp > 1):
        qp -= 1
        a /= q
        while (a <= n):
            a *= p
            pp += 1
        a /= p
        pp -= 1

        #print "a = {0} = {1}^{2} * {3}^{4}".format(a,p,pp,q,qp)

        if (a > best):
            best = a
            bestp = pp
            bestq = qp

    #print "    M({0},{1},{2}) = {3} = {0}^{4} * {1}^{5}".format(p,q,n,best,bestp,bestq)
    return best

########################################
LIMIT_PRIME = SIZE
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

calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "They are", primes

########################################
#print "M(2,3,100)={0}".format(M(2,3,100))
#print "M(3,5,100)={0}".format(M(3,5,100))
#print "M(2,73,100)={0}".format(M(2,73,100))

answer = 0
for q in xrange(len(primes)):
    if ((q % 1000) == 0):
        print "Testing M(p,{0},{1})".format(primes[q],SIZE)
    for p in xrange(q):
        if (p*q > SIZE):  break
        a = M(primes[p],primes[q],SIZE)
#        if (a > 0):
#            print "M({0},{1},{2}) = {3}".format(primes[p],primes[q],SIZE,a)
        answer += a

print "Answer =", answer

print "Time taken = {0} seconds".format(time.clock() - start_time)

