#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 630
#
# Crossed lines
#
# Given a set, L, of unique lines, let M(L) be the number of lines in
# the set and let S(L) be the sum over every line of the number of
# times that line is crossed by another line in the set. For example,
# two sets of three lines are shown below:
#
# crossed lines
#
# In both cases M(L) is 3 and S(L) is 6: each of the three lines is
# crossed by two other lines. Note that even if the lines cross at a
# single point, all of the separate crossings of lines are counted.
#
# Consider points (T[2k−1], T[2k]), for integer k >= 1, generated in
# the following way:
#
#  S[0]   = 290797
#  S[n+1] = S[n]^2 mod 50515093
#  T[n]   = (S[n] mod 2000) − 1000
#
# For example, the first three points are: (527, 144), (−488, 732),
# (−454, −947). Given the first n points generated in this manner, let
# Ln be the set of unique lines that can be formed by joining each
# point with every other point, the lines being extended indefinitely
# in both directions. We can then define M(Ln) and S(Ln) as described
# above.
#
# For example, M(L[3])=3 and S(L[3])=6. Also M(L[100])=4948 and
# S(L[100])=24477690.
#
# Find S(L[2500]).

SIZE = 55   # Smallest problem with at least 1 duplicate in the x value
            # T[47] and T[55] have the same x value (43)
SIZE = 100
SIZE = 500
SIZE = 750
SIZE = 1000
SIZE = 2500

import sys
import time
start_time = time.clock()

import math
from fractions import Fraction


print("Running with SIZE = {}".format(SIZE))


########################################
# Algorithm to generate points
def S():
    S = 290797
    yield S
    while True:
        S = (S*S % 50515093)
        yield S

def map(s):
    return (s % 2000) - 1000

def genT():
    x, y = 0, 0
    odd = False
    for s in S():
        if odd:
            x = map(s)
            odd = False
        else:
            y = map(s)
            odd = True
            yield (x, y)


########################################
# Calculate the points
T = []
duplicate_spotter = [0] * 1999
for n, (x, y) in enumerate(genT()):
    T.append((x, y))

    if n >= SIZE:
        break


########################################
# Calculate the slopes & intercepts for the lines
Lines = {}
duplicates = 0
for a in range(2, SIZE+1):
    for b in range(1, a):
        line_id = "{}-{}".format(a, b)
        #print("{}: ".format(line_id), end='')

        (ax, ay) = T[a]
        (bx, by) = T[b]
        if (ax == bx):
            slope = (1, 0)
            intercept = ax
        else:
            dx = bx - ax
            dy = by - ay
            g = math.gcd(dx, dy)
            if dx < 0:
                g = -g
            slope = (dy//g, dx//g)
            intercept = ay - ax * Fraction(dy, dx)

        if slope in Lines:
            if intercept in Lines[slope]:
                duplicates += 1
                #print("line {} is a duplicate of {}".format(line_id, Lines[slope][intercept]))
            else:
                Lines[slope][intercept] = line_id
            pass
        else:
            Lines[slope] = {intercept: line_id}

        #print("slope = {}, intercept = {}".format(slope, intercept))



print("{} duplicate lines found".format(duplicates))
num_lines = SIZE * (SIZE-1) // 2
num_lines -= duplicates
print("M({}) = {} lines".format(SIZE, num_lines))
print()

num_intersections = num_lines * (num_lines - 1)
for slope in Lines:
    parallel_lines = len(Lines[slope])
    if parallel_lines > 1:
        #print("{} parallel lines with slope {}".format(parallel_lines, slope))
        num_intersections -= parallel_lines * (parallel_lines - 1)
print("L({}) = {} lines".format(SIZE, num_intersections))
print()

print("Answer = {:,}".format(num_intersections))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
