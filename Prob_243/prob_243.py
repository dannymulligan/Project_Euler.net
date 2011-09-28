#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 243
#
# Resilience
#
# A positive fraction whose numerator is less than its denominator is
# called a proper fraction.
#
# For any denominator, d, there will be d−1 proper fractions; for
# example, with d = 12:
#     1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.
#
# We shall call a fraction that cannot be cancelled down a resilient
# fraction.
#
# Furthermore we shall define the resilience of a denominator, R(d),
# to be the ratio of its proper fractions that are resilient; for
# example, R(12) = 4/11.
#
# In fact, d = 12 is the smallest denominator having a resilience R(d)
# < 4/10.
#
# Find the smallest denominator d, having a resilience R(d) <
# 15499/94744.
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

import fractions


########################################
#def totient(n):  
#    "short and sweet, but a bit slow"
#    return len([i for i in range(1,n) if fractions.gcd(i,n)==1]) 
def totient(n):
    """
    Compute the number of positives < n that are
    relatively prime to n -- good solution!
    """
    tot, pos = 0, n-1
    while pos>0:
       if fractions.gcd(pos,n)==1: tot += 1
       pos -= 1
    return tot 


########################################
STEP  = 2*3*5*7
START = STEP
MAX   = 35000
#STEP  = 1
#START = 2
#MAX   = 211

target = fractions.Fraction(15499,94744)
print "target = {0} = {1}".format(target, float(target))

min_found = fractions.Fraction(2,1)
for i in xrange(START, MAX, STEP):
    ans = totient(i)
    ansf = fractions.Fraction(ans,i-1)
    #print "R({0}) = {1}/{2} = {3}".format(i,ans,i-1, float(ansf))
    if (ansf < min_found):
        min_found = ansf
        print "    R({0}) = {1}/{2} = {3} ({4} = {5}*{6})".format(i,ans,i-1, float(ansf), i,i/STEP,STEP)
        if (ansf < target):
            print "Answer found = {0}".format(i)
            print "Time taken = {0} seconds".format(time.clock() - start_time)
            sys.exit(0)
    elif ((i % 1000) == 0):
        print "R({0}) = {1}/{2} = {3}".format(i,ans,i-1, float(ansf)), 
        print "Time taken = {0} seconds".format(time.clock() - start_time)

print "Time taken = {0} seconds".format(time.clock() - start_time)

# R(2310) = 480/2309 = 0.207882200087
# R(60060) = 11520/60059 = 0.191811385471
# R(90090) = 17280/90089 = 0.191810320905
# R(106260) = 21120/106259 = 0.198759634478
# R(120120) = 23040/120119 = 0.191809788626
# R(150150) = 28800/150149 = 0.191809469261
# R(180180) = 34560/180179 = 0.191809256351
# R(300300) = 57600/300299 = 0.191808830532
# R(1021020) = 184320/1021019 = 0.180525533805
# R(1531530) = 276480/1531529 = 0.180525474869


# This is Euler's Totient function: http://en.wikipedia.org/wiki/Euler%27s_totient_function

# If N = p1^k1 * p2^k2 * ... * pn^kn
# Then, totient(n) = totient(p1^k1) * totient(p2^k2) * ... * totient(pn^kn)
#     = p1^k1*(1-1/p1) * p2^k2*(1-1/p2) * ... * pn^kn*(1-1/pn)
#     = n * (1-1/p1) * (1-1/p2) * ... * (1-1/pn)
#
# Since we are trying to minimize totient(n)/(n-1), we are trying to minimize...
#     = (n/(n-1)) * (1-1/p1) * (1-1/p2) * ... * (1-1/pn)
# which is approximately equal to
#     = (1-1/p1) * (1-1/p2) * ... * (1-1/pn)
# which means that we'll get there by building N from primes to the power of 1 only


