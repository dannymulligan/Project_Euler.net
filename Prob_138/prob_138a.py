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
import fractions

start_time = time.clock()
now_time = start_time

def test(b,h,L):
    if ((b % 2) != 0):  return False
    if ((b - h)**2 != 1):  return False
    if (((b/2)**2 + h**2) != L**2):  return False
    return True


def pythagorean_triple(m,n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    if (a>b):
        a,b = b,a
    #print "m={0}, n={1}, (a,b,c) = ({2},{3},{4})".format(m,n,a,b,c)
    return a, b, c


ans = 0
cnt = 0
soln_cnt = 0
m,n = 2,1
while (soln_cnt < 12):
    b,h,L = pythagorean_triple(m,n)
    b *= 2

    if test(b,h,L):
        soln_cnt += 1
        ans += L
        print "Found solution #{0}: b={1}, h={2}, L={3}, ans={4}, (m,n)=({5},{6})".format(soln_cnt, b, h, L, ans, m, n)
        m,n = m+1,m
    m += 2

    cnt += 1
    if ((cnt % 1000000) == 0):
        prev_time = now_time
        now_time = time.clock()
        print "    cnt={0}, soln_cnt={1}, (m,n)=({2},{3}), time={4}, delta={5}".format(cnt, soln_cnt, m, n, now_time, now_time-prev_time)

print "Answer =", ans
print "Time taken =", time.clock() - start_time, "seconds"


# There's a pattern here...
# Found solution #1: b=16, h=15, L=17, ans=17, (m,n)=(4,1)
# Found solution #2: b=272, h=273, L=305, ans=322, (m,n)=(17,4)
# Found solution #3: b=4896, h=4895, L=5473, ans=5795, (m,n)=(72,17)
# Found solution #4: b=87840, h=87841, L=98209, ans=104004, (m,n)=(305,72)
# When a solution is found, the next n is the same as the previous solution m
