#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 200
#
# Find the 200th prime-proof sqube containing the contiguous sub-string "200"
#
# We shall define a sqube to be a number of the form, p^2*q^3, where p
# and q are distinct primes.
#
# For example, 200 = 5^2*2^3 or 120072949 = 23^2*61^3.
#
# The first five squbes are 72, 108, 200, 392, and 500.
#
# Interestingly, 200 is also the first number for which you cannot
# change any single digit to make a prime; we shall call such numbers,
# prime-proof. The next prime-proof sqube which contains the
# contiguous sub-string "200" is 1992008.
#
# Find the 200th prime-proof sqube containing the contiguous sub-string "200".
#
# Solved ??/??/15
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


print "Time taken = {0} seconds".format(time.clock() - start_time)
