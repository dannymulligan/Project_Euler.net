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
# Solved 11/21/16

import time
start_time = time.clock()

SIZE = 12345

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
if False:
    FitSize = dict()
    FitHex = dict()
    for x in range(1, SIZE+1):
        for y in range(x+1):
            TSize = HexagonXRange(x, y)
            if TSize > SIZE:
                continue

            Symmetric = (x == y) or (y == 0)
            if Symmetric:
                # Symmetric hexagons can not be reflected horizontally
                Count = 1
            else:
                # Asymmetric hexagons can be reflected horizontally
                Count = 2

            if TSize not in FitSize.keys():
                # First bounding triangle of this size
                FitSize[TSize] = Count
                FitHex[TSize] = [(x, y, Count)]
            else:
                FitSize[TSize] += Count
                FitHex[TSize].append((x, y, Count))

    if False:
        for TSize in sorted(FitSize.keys()):
            if TSize > 100:
                break
            print("Fits[{}] = {}, {}".format(TSize, FitSize[TSize], FitHex[TSize]))

else:
    # Much faster, and known from observation to be the same result
    FitSize = [n//3 if ((n % 3) == 0) else 0 for n in range(SIZE+1)]

    if False:
        # Test code
        for TSize in range(3, SIZE+1, 3):
            if TSize > 100:
                break
            print("Fits[{}] = {}".format(TSize, FitSize[TSize]))


########################################
def TFitT(n, m):
    '''How many triangles of size m fit inside
    a triangle of size n'''
    return (n-m+1)*(n-m+2)//2

if False:
    # Test code for the TFitT(n, m) function
    assert TFitT(6, 3) == 10
    assert TFitT(7, 3) == 15
    assert TFitT(7, 4) == 10


########################################
def Hquick(n):
    '''Quicker way of calculating H(n)'''
    Debug = False

    Answer = 0
    for m in range(3, n+1, 3):
        Triangles = TFitT(n, m)
        Fits = FitSize[m]
        Answer += Triangles * Fits
        if Debug:
            print(" + {} * {} = {} = {} * {}".format(
                    Triangles, Fits, Triangles*Fits, Triangles, FitHex[m]))

    return Answer

Answer = 0
for n in range(3, SIZE+1):
    H = Hquick(n)
    Answer += H

print("Answer: sum(H({})) = {}".format(n, Answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
