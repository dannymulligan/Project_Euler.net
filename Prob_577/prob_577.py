#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 577
#
# Counting hexagons
#
# An equilateral triangle with integer side length n >= 3 is divided
# into n^2 equilateral triangles with side length 1 as shown in the
# diagram below.
#
# The vertices of these triangles constitute a triangular lattice with
# (n+1)(n+2)/2 lattice points.
#
# Let H(n) be the number of all regular hexagons that can be found by
# connecting 6 of these points accordingly.
#
# For example, H(3)=1, H(6)=12 and H(20)=966.
#
# Find sum(n=1..12345) H(n).
#
# Solved ??/??/16

#import numpy as np
#import scipy as sp
#import matplotlib as mpl

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

import sys
#print(sys.version)
import time
start_time = time.clock()
SIZE = 6

########################################
def H(n):
    if n < 3:
        return 0
    elif n == 3:
        return 1
    elif n == 4:
        return 3
    else:
        Answer = H(n-3)

        for x in range(1, n//3+1):
            NormalHexagons = 0
            if n == 3*x:
                NormalHexagons = 1
            elif n > 3*x:
                NormalHexagons = 3*(n-2*x-1)
            print("{} normal hexagons of size {} fix into a triangle of size {}"
                  .format(NormalHexagons, x, n))
            Answer += NormalHexagons

        for x in range(1, n//6+1):
            VerticalHexagons = 0
            if n == 6*x:
                VerticalHexagons = 1
            elif n > 6*x:
                VerticalHexagons = 3*(n-6*x-1)
            print("{} vertical hexigons of size {} fix into a triangle of size {}"
                  .format(VerticalHexagons, x, n))
            Answer += VerticalHexagons

        return Answer




print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
