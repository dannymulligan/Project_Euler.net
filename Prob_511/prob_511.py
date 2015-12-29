#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 511
#
# Sequences with nice divisibility properties
#
# Let Seq(n,k) be the number of positive-integer sequences {ai}1≤i≤n
# of length n such that:
#
#     n is divisible by ai for 1 ≤ i ≤ n, and
#     n + a1 + a2 + ... + an is divisible by k.
#
# Examples:
#
# Seq(3,4) = 4, and the 4 sequences are:
#    {1, 1, 3}
#    {1, 3, 1}
#    {3, 1, 1}
#    {3, 3, 3}
#
# Seq(4,11) = 8, and the 8 sequences are:
#    {1, 1, 1, 4}
#    {1, 1, 4, 1}
#    {1, 4, 1, 1}
#    {4, 1, 1, 1}
#    {2, 2, 2, 1}
#    {2, 2, 1, 2}
#    {2, 1, 2, 2}
#    {1, 2, 2, 2}
#
# The last nine digits of Seq(1111,24) are 840643584.
#
# Find the last nine digits of Seq(1234567898765,4321).
#
# Solved ??/??/15
# ?? problems solved
# Position #??? on level ?


# Factors of 1234567898765 are 5, 41, 25343, 237631
# Factors of 4321 are 29, 149

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


print "Time taken = {0} seconds".format(time.clock() - start_time)
