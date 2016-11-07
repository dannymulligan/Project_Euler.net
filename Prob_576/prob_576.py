#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 576
#
# Irrational jumps
#
# A bouncing point moves counterclockwise along a circle with
# circumference 1 with jumps of constant length l < 1, until it hits a
# gap of length g < 1, that is placed in a distance d counterclockwise
# from the starting point. The gap does not include the starting
# point, that is g + d < 1.
#
# Let S(l,g,d) be the sum of the length of all jumps, until the point
# falls into the gap. It can be shown that S(l,g,d) is finite for any
# irrational jump size l, regardless of the values of g and d.
#
# Examples:
#    S(sqrt(1/2), 0.06, 0.7   ) =  0.7071...,
#    S(sqrt(1/2), 0.06, 0.3543) =  1.4142... and
#    S(sqrt(1/2), 0.06, 0.2427) = 16.2634...
#
# Let M(n,g) be the maximum of Sum(S(sqrt(1/p),g,d)) for all primes p
# <= n and any valid value of d.
#
# Examples:
#    M(3, 0.06) = 29.5425...,
# since
#    S(sqrt(1/2), 0.06, 0.2427) + S(sqrt(1/3), 0.06, 0.2427) = 29.5425...
# is the maximal reachable sum for g=0.06.
#
#    M(10, 0.01) = 266.9010...
#
# Find M(100, 0.00002), rounded to 4 decimal places.
#
# Solved ??/??/16

import sys
#print(sys.version)
import time
start_time = time.clock()

########################################


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
