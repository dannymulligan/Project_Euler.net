#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 517
#
# A real recursion
# 
# For every real number a>1 is given the sequence ga by:
#
#    g_a(x) = 1 for x < a
#    g_a(x) = g_a(x−1) + g_a(x−a) for x >= a
#    G(n) = g_rootN(n)
#    G(90) = 7564511
#
# Find sum(G(p)) for p prime and 10000000<p<10010000
#
# Give your answer modulo 1000000007.

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
