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

# x+y + x-y = a hypo square
# => 2x = a hypo square
#
# y+z + y-z = a hypo square
# => 2y = a hypo square
#
# x+z + y-z = a hypo square
# => x+y = a hypo square
#
# x-y + y+z = a hypo square
# => x+z = a hypo square

# Tried 4821000000 solutions, sum = 1006132, max_sq = 1048576, sum = 1006132, x = 663054, y = 229971, z = 113107
# Tried 4821500000 solutions, sum = 1006185, max_sq = 1048576, sum = 1006185, x = 531128, y = 346841, z = 128216
# Solution found sum = 1006193, x = 434657, y = 420968, z = 150568
# Tried 4821574776 solutions, sum = 1006193, max_sq = 1048576
# 4821574776
# Answer = 1006193
# 
# real	327m55.969s
# user	322m35.830s
# sys	0m37.964s

import sys

#MAX    = 250  # Takes ~1 minute to run
#MAX    = 180  # Takes ~15 seconds to run
MAX    = 1024  # Takes ? to run
MAX_SQ = MAX*MAX

print "Running with max = {0}, max_sq = {1}".format(MAX, MAX_SQ)

psqr = []
for i in range(1,MAX+1):
    psqr.append(i*i)

hsqr = []
for i in psqr:
    for j in psqr:
        if (j >= i): break
        if ((i-j) in psqr):
            hsqr.append(i)
            break

print len(psqr), psqr
print len(hsqr), hsqr

dpsqr = {}
for i in psqr:
    dpsqr[i] = True

print len(dpsqr), dpsqr

cnt = 0
#for sum in range (6,MAX_SQ):
for sum in range (1006190,MAX_SQ):
    for xy in hsqr:
        # xy gets larger as we go through this loop
        # z gets smaller as we go through this loop
        z = sum - xy
        if (3*z >= sum): continue
        if (z <= 0): break

        for xz in hsqr:
            # xz gets larger as we go through this loop
            # x gets larger as we go through this loop
            # y gets smaller as we go through this loop
            x = xz - z
            y = xy - x
            if (z >= y): break
            if (y >= x): continue

            cnt += 1
            if ((cnt % 500000) == 0):
                print "Tried {0} solutions, sum = {1}, max_sq = {2},".format(cnt, sum, MAX_SQ),
                print "sum = {0}, x = {1}, y = {2}, z = {3}".format(sum, x, y, z)

            #if ((x+y) not in psqr):  continue
            #if ((x+z) not in psqr):  continue
            if ((x-y) not in dpsqr):  continue
            if ((x-z) not in dpsqr):  continue
            if ((y+z) not in dpsqr):  continue
            if ((y-z) not in dpsqr):  continue

            print "Solution found sum = {0}, x = {1}, y = {2}, z = {3}".format(sum, x, y, z)
            print "Tried {0} solutions, sum = {1}, max_sq = {2}".format(cnt, sum, MAX_SQ)
            print cnt
            print "Answer =", sum
            sys.exit()

print "Done: Tried", cnt, "solutions, sum =", sum, "max =", MAX, "max_sq =", MAX_SQ
