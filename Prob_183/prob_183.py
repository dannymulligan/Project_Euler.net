#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 183
#
# Maximum product of parts
#
# Let N be a positive integer and let N be split into k equal parts, r
# = N/k, so that N = r + r + ... + r.
#
# Let P be the product of these parts, P = r * r * ... * r = rk.
#
# For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 +
# 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.
#
# Let M(N) = Pmax for a given value of N.
#
# It turns out that the maximum for N = 11 is found by splitting
# eleven into four equal parts which leads to Pmax = (11/4)^4; that
# is, M(11) = 14641/256 = 57.19140625, which is a terminating decimal.
#
# However, for N = 8 the maximum is achieved by splitting it into
# three equal parts, so M(8) = 512/27, which is a non-terminating
# decimal.
#
# Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if
# M(N) is a terminating decimal.
# 
# For example, sum(D(N)) for 5 <= N <= 100 is 2438.
#
# Find sum(D(N)) for 5 <= N <= 10000.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import cProfile
import time
import fractions

start_time = time.clock()

def is_terminating(n):
    d = n.denominator
    while ((d % 2) == 0):  d /= 2
    while ((d % 5) == 0):  d /= 5
    if (d == 1):  return True
    else:         return False

def Pmax(n):
    #print "Pmax({0})".format(n)
    found = False
    bestP = fractions.Fraction(0)
    bestK = 0
    k = n * 32 / 100
    #k = 1
    while not found:
        g = fractions.gcd(n,k)
        n1 = n/g
        k1 = k/g
        P = fractions.Fraction(n1**k,k1**k)
        #print "Pmax({0}) = ({0}/{1})^{1} = {2} = {3}".format(n,k,float(P),P)
        if (P >= bestP):
            bestP = P
            bestK = k
        elif (P < bestP):
            #print "bestK = {0} which is {1:5.2f}% of {2}".format(bestK, 100.0*bestK/n, n)
            return bestP
        k += 1

def main():
    ans = 0
    #ans = 452936  # Answer with n = 1000
    #ans = 9692530  # Answer with n = 4500
    ans = 25004666  # Answer with n = 7200
    now_time = start_time
    prev_time = start_time
    #for n in range(5,101):
    #for n in range(5,10001):
    #for n in range(4501,10001):
    for n in range(7201,10001):
        Pm = Pmax(n)
        print "Pmax({0}) =".format(n),
        if is_terminating(Pm):
            print "terminating"
            ans -= n
        else:
            print "non-terminating"
            ans += n
        if ((n % 100) == 0):
            prev_time = now_time
            now_time = time.clock()
            print "========================================"
            print "N =", n
            print "    Answer so far =", ans
            print "    Time =", now_time - start_time, "seconds"
            print "    Incremental =", now_time - prev_time, "seconds"

    print "Answer =", ans
    print "Time taken =", time.clock() - start_time, "seconds"

cProfile.run('main()')
