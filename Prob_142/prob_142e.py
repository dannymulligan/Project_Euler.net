#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 142
#
# Perfect Square Collection
#
# Find the smallest x + y + z with integers x > y > z > 0 such that
# x + y, x - y, x + z, x - z, y + z, y - z are all perfect squares.
#
# Solved 08/28/10
# 121 problems solved
# Position #692 on level 3

# x+y is a perfect square
# x-y is a perfect square
# x+z is a perfect square
# x-z is a perfect square
# y+z is a perfect square
# y-z is a perfect square
#
# A perfect square + a perfect square = a hypo square

# x+y + x-y = sum of squares
# => 2x = sum of squares
#
# y+z + y-z = sum of squares
# => 2y = sum of squares
#
# x+z + y-z = sum of squares
# => x+y = sum of squares
#
# x-y + y+z = sum of squares
# => x+z = sum of squares


import sys

#MAX    = 60  # Takes ~1 second to run
#MAX    = 120  # Takes ~15 seconds to run
#MAX    = 180  # Takes ~75 seconds to run
#MAX    = 200  # Takes ~110 seconds to run
#MAX    = 250  # Takes ~280 seconds to run
#MAX    = 500  # Takes ? seconds to run
MAX    = 1024  # Takes ~19 mins to run
MAX_SQ = MAX*MAX

print "Running with max = {0}, max_sq = {1}".format(MAX, MAX_SQ)

psqr = []
for i in range(1,MAX+1):
    psqr.append(i*i)
print "len(psqr) =", len(psqr)
#print "psqr =", psqr


dpsqr = {}
for i in psqr:
    dpsqr[i] = True
print "len(dpsqr) =", len(dpsqr)
#print "dpsqr =", dpsqr

# x+y = a = a perfect square
# x-y = b = a perfect square
# 2x = a + b = a sum of perfect squares
# 2y = a - b = a difference of perfect squares
# x = (a + b)/2
# y = (a - b)/2

poss_xy = []
for a in psqr:
    for b in psqr:
        if (b >= a): continue
        if ((a+b) % 2 == 1): continue
        if ((a-b) % 2 == 1): continue
        x = (a + b)/2
        y = (a - b)/2
        if ((x > 3) & (y > 2)):
            poss_xy.append((x+y, x,y))

poss_xy.sort()

print "len(poss_xy) =", len(poss_xy)
#print "poss_xy =", poss_xy
#sys.exit()

cnt = 0
for sum in range (6,MAX_SQ):
    for (xy, x, y) in poss_xy:
        z = sum - xy

        if (z >= y): continue
        if (z <= 0): break

        cnt += 1
        if ((cnt % 1000000) == 0):
            print "Trying sum = {0} (out of {5}, {6:4.2}% complete), x = {1}, y = {2}, z = {3}, cnt={4}".format(sum, x, y, z, cnt, MAX_SQ, 100.0*sum/1006193)

        #if ((x+y) not in dpsqr):  continue
        #if ((x-y) not in dpsqr):  continue
        if ((x+z) not in dpsqr):  continue
        if ((x-z) not in dpsqr):  continue
        if ((y+z) not in dpsqr):  continue
        if ((y-z) not in dpsqr):  continue

        print "Solution found sum = {0}, x = {1}, y = {2}, z = {3}".format(sum, x, y, z)
        print "    x+y = {0}, x-y = {1}".format(x+y, x-y)
        print "    x+z = {0}, x-z = {1}".format(x+z, x-z)
        print "    y+z = {0}, y-z = {1}".format(y+z, y-z)
        print "Tried {0} solutions, sum = {1}, max_sq = {2}".format(cnt, sum, MAX_SQ)
        print "Answer =", sum
        sys.exit()

print "Done: Tried", cnt, "solutions, sum =", sum, "max =", MAX, "max_sq =", MAX_SQ
