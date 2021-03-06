#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 138
#
# Investigating isosceles triangle for which the height and base
# length differ by one.
#
# Consider the isosceles triangle with base length, b = 16, and legs,
# L = 17.
#
#               .
#              /|\
#             / | \
#            /  |  \
#           /   |   \
#        L /    |    \  L
#         /    h|     \
#        /      |      \
#       /       |       \
#      /        |        \
#     ---------------------
#               b
#  
# By using the Pythagorean theorem it can be seen that the height of
# the triangle, h = sqrt(17^2 − 8^2) = 15, which is one less than the
# base length.
#
# With b = 272 and L = 305, we get h = 273, which is one more than the
# base length, and this is the second smallest isosceles triangle with
# the property that h = b +/- 1.
#
# Find sum(L) for the twelve smallest isosceles triangles for which h
# = b +/- 1 and b, L are positive integers.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

# L, b & h are all integer
# b/2 is also integer, therefore b must be even
# h = b +/-1, therefore h must be odd

import sys
import pdb
import cProfile
import time

start_time = time.clock()
now_time = start_time

ans = 0
soln_cnt = 0
b = 10
while (soln_cnt < 12):
    hp = b + 1
    hm = b - 1
    Lp2 = hp**2 + (b/2)**2
    Lm2 = hm**2 + (b/2)**2
    fLp = float(Lp2)**0.5
    fLm = float(Lm2)**0.5
    Lp = int(fLp)
    Lm = int(fLm)

    if ((Lp  )**2 == Lp2):
        soln_cnt += 1
        ans += (Lp  )
        print "Found solution #{0}: b = {1}, h = {2}, L = {3}, ans = {4}  (Lp  )".format(soln_cnt, b, hp, (Lp  ), ans)
    if ((Lm  )**2 == Lm2):
        soln_cnt += 1
        ans += (Lm  )
        print "Found solution #{0}: b = {1}, h = {2}, L = {3}, ans = {4}  (Lm  )".format(soln_cnt, b, hm, (Lm  ), ans)

    if ((Lp-1)**2 == Lp2):
        soln_cnt += 1
        ans += (Lp-1)
        print "Found solution #{0}: b = {1}, h = {2}, L = {3}, ans = {4}  (Lp-1)".format(soln_cnt, b, hp, (Lp-1), ans)
    if ((Lp+1)**2 == Lp2):
        soln_cnt += 1
        ans += (Lp+1)
        print "Found solution #{0}: b = {1}, h = {2}, L = {3}, ans = {4}  (Lp+1)".format(soln_cnt, b, hp, (Lp+1), ans)
    if ((Lm-1)**2 == Lm2):
        soln_cnt += 1
        ans += (Lm-1)
        print "Found solution #{0}: b = {1}, h = {2}, L = {3}, ans = {4}  (Lm-1)".format(soln_cnt, b, hm, (Lm-1), ans)
    if ((Lm+1)**2 == Lm2):
        soln_cnt += 1
        ans += (Lm+1)
        print "Found solution #{0}: b = {1}, h = {2}, L = {3}, ans = {4}  (Lm+1)".format(soln_cnt, b, hm, (Lm+1), ans)

    if ((b % 20000000) == 0):
        prev_time = now_time
        now_time = time.clock()
        print "    b = {0}, soln_cnt = {1}, time = {2}, delta = {3}".format(b, soln_cnt, now_time, now_time-prev_time)
    b += 2

print "Answer =", ans
print "Time taken =", time.clock() - start_time, "seconds"
