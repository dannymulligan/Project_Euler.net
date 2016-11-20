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
SIZE = 1000

########################################
def HexagonXRange(dx, dy):
    if False:
        print("H({}, {})".format(x, y))

    x1, y1 = dx, dy
    x2, y2 = (x1      - dy), (y1 + dx + dy)
    x3, y3 = (x2 - dx - dy), (y2 + dx     )
    x4, y4 = (x3 - dx     ), (y3      - dy)
    x5, y5 = (x4      + dy), (y4 - dx - dy)
    x6, y6 = (x5 + dx + dy), (y5 - dx     )
    assert x6 == 0
    assert y6 == 0

    MaxX = max((x1+y1), (x2+y2), (x3+y3), (x4+y4), (x5+y5), (x6+y6))
    MinX = min(x1, x2, x3, x4, x5, x6)

    if False:
        print("   p1 ({},{})".format(x1, y1))
        print("   p2 ({},{})".format(x2, y2))
        print("   p3 ({},{})".format(x3, y3))
        print("   p4 ({},{})".format(x4, y4))
        print("   p5 ({},{})".format(x5, y5))
        print("   p6 ({},{})".format(x6, y6))
        print("   range = ({} ... {})".format(MinX, MaxX))

    return MaxX - MinX


########################################
Ranges = dict()
for x in range(1, SIZE+1):
    for y in range(x+1):
        Ranges[(x, y)] = HexagonXRange(x, y)

#for (x, y) in sorted(Ranges.keys()):
#    if (x == y):
#        print("Range({}, {}) = {} (symmetric)".format(x, y, Ranges[(x, y)]))
#    else:
#        print("Range({}, {}) = {}".format(x, y, Ranges[(x, y)]))


########################################
H = 0
Hlist = list()
Hlist.append(H)  # H(0)
Hlist.append(H)  # H(1)
Hlist.append(H)  # H(2)
Debug = False

for n in range(3, SIZE+1):
#    if (n == 80) or (n == 180):
#        Debug = True
#    else:
#        Debug = False

    H = Hlist[n-3]
    if Debug:
        print("----------------------------------------")
        print("Calculating H({})".format(n))
        print("    Starting with H({}) = {}".format(n-3, H))

    for x in range(1, n+1):
        for y in range(x+1):
            Range = Ranges[(x, y)]
            if (Range <= n) and Debug:
                print("    Range[({}, {})] is {}".format(x, y, Range))

            if (x == y) or (y == 0):
                # Symmetric cases
                if Range == n:
                    H += 1
                    if Debug:
                        print("    H = H + 1 = {}".format(H))

                elif Range < n:
                    H += (n-Range)*3
                    if Debug:
                        print("    H = H + ({})*3 = H + {} = {}".format(n-Range, (n-Range)*3, H))
            else:
                # Not-symmetric cases
                if Range == n:
                    H += 2
                    if Debug:
                        print("    H = H + 1*2 = {} symmetry".format(H))

                elif Range < n:
                    H += (n-Range)*3*2
                    if Debug:
                        print("    H = H + ({})*3*2 = H + {} = {} symmetry".format(n-Range, (n-Range)*3*2, H))

    Hlist.append(H)

    if ((n % 10) == 0) or Debug:
        print("H({}) = {}".format(n, H))

print("Answer = H({}) = {}".format(n, H))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
