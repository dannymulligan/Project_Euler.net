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

import sys

MAX    = 32
MAX_SQ = MAX*MAX

squares = []
for i in range(1,MAX+1):
    squares.append(i*i)

print squares

cnt = 0
for sum in range (6,MAX_SQ):
    for x in range(3, sum):
        for y in range(1+(sum-x)/2,sum-1-x):
            z = sum - x - y
            if (x > y > z):
                cnt += 1
                if ((cnt % 1000000) == 0):  print "Tried", cnt, "solutions, sum =", sum, "max =", MAX_SQ

                # print "sum = {0}, x = {1}, y = {2}, z = {3}".format(sum, x, y, z)
                if ((x+y) not in squares):  continue
                if ((x-y) not in squares):  continue
                if ((x+z) not in squares):  continue
                if ((x-z) not in squares):  continue
                if ((y+z) not in squares):  continue
                if ((y-z) not in squares):  continue

                print "Solution found sum = {0}, x = {1}, y = {2}, z = {3}".format(sum, x, y, z)
                print cnt
                print "Answer =", sum
                sys.exit()

print "Done: Tried", cnt, "solutions, sum =", sum, "max =", MAX_SQ
