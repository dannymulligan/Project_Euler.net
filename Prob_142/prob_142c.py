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
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

# Tried 638500000 solutions, sum = 182146, max_sq = 1048576, sum = 182146, x = 97465, y = 78096, z = 6585
#   C-c C-cTraceback (most recent call last):
#   File "./prob_142c.py", line 53, in <module>
#     if ((x+z) not in squares):  continue
# KeyboardInterrupt
# 
# real	526m41.276s
# user	525m29.129s
# sys	0m31.287s

import sys

MAX    = 112
MAX_SQ = MAX*MAX

print "Running with max = {0}, max_sq = {1}".format(MAX, MAX_SQ)

squares = []
for i in range(1,MAX+1):
    squares.append(i*i)

print squares

cnt = 0
for sum in range (6,MAX_SQ):
    for yz in squares:
        #if ((y+z) not in squares):  continue
        if (yz >= sum): break

        x = sum - yz
        if (x*2 <= yz): break

        for xy in squares:
            if (xy >= sum): break
            #if ((x+y) not in squares):  continue
            y = xy - x
            if (y >= x): break

            z = sum - xy
            if (z <= 0): break
            if (z >= y): continue
            cnt += 1
            if ((cnt % 500000) == 0):
                print "Tried {0} solutions, sum = {1}, max_sq = {2},".format(cnt, sum, MAX_SQ),
                print "sum = {0}, x = {1}, y = {2}, z = {3}".format(sum, x, y, z)

            if ((x+z) not in squares):  continue
            if ((x-y) not in squares):  continue
            if ((x-z) not in squares):  continue
            if ((y-z) not in squares):  continue

            # If x+z is a square1, and y-z is a square2, then x+z+y-z = square1+square2
            # Thus x+y = square1+square2, and x+y = square => investigate pythagoran squares

            print "Solution found sum = {0}, x = {1}, y = {2}, z = {3}".format(sum, x, y, z)
            print "Tried {0} solutions, sum = {1}, max_sq = {2}".format(cnt, sum, MAX_SQ)
            print cnt
            print "Answer =", sum
            sys.exit()

print "Done: Tried", cnt, "solutions, sum =", sum, "max =", MAX, "max_sq =", MAX_SQ
