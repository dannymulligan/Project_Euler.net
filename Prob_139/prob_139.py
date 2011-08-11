#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 139
#
# Finding Pythagorean triangles which allow the square on the
# hypotenuse to be tiled.
#
# Let (a, b, c) represent the three sides of a right angle triangle
# with integral length sides. It is possible to place four such
# triangles together to form a square with length c.
#
# For example, (3, 4, 5) triangles can be placed together to form a 5
# by 5 square with a 1 by 1 hole in the middle and it can be seen that
# the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.
#
# However, if (5, 12, 13) triangles were used then the hole would
# measure 7 by 7 and these could not be used to tile the 13 by 13
# square.
#
# Given that the perimeter of the right triangle is less than
# one-hundred million, how many Pythagorean triangles would allow such
# a tiling to take place?
#
# Solved 08/11/11
# 161 problems solved
# Position #494 on level 4

import sys
import time
import fractions

MAX = 100000000
#MAX = 100

print "Running with MAX={0}".format(MAX)
start_time = time.clock()

# Euclid's formula from http://en.wikipedia.org/wiki/Pythagorean_triple
def pythagorean_triple(m,n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    # a + b + c = 2*m**2 + 2*m*n

    if (a>b):
        a,b = b,a
    #print "m={0}, n={1}, (a,b,c) = ({2},{3},{4})".format(m,n,a,b,c)
    return a, b, c

def odd(x):
    if ((x % 2) == 1):  return True
    else:               return False

answer = 0
m = 2
#while ((2*m**2 + 2*m) < MAX):
while ((2*m**2) < MAX):

    # m-n must be odd
    if odd(m):
        n = 2
    else:
        n = 1

    while (((2*m**2 + 2*m*n) < MAX) & (n < m)):
        # m and n must be coprime
        if (fractions.gcd(m,n) != 1):
            n += 2
            continue

        a,b,c = pythagorean_triple(m,n)

        if ((a+b+c) < MAX):
            h = (b - a)
            max_k = (MAX-1)/(a+b+c)
            if ((c % h) == 0):
                answer += max_k
#                for k in range(1,max_k+1):
#                    print "++ (m,n,k) = ({0},{1},{2}), (a,b,c) = ({3},{4},{5}) h={6} p={7}".format(m,n,k,k*a,k*b,k*c,k*h,k*(a+b+c))
#            else:
#                for k in range(1,max_k+1):
#                    print "-- (m,n,k) = ({0},{1},{2}), (a,b,c) = ({3},{4},{5}) h={6} p={7} not divisible".format(m,n,k,k*a,k*b,k*c,k*h,k*(a+b+c))
#        else:
#            print "-- (m,n,k) = ({0},{1},{2}), (a,b,c) = ({3},{4},{5}) h={6} p={7} too big".format(m,n,k,k*a,k*b,k*c,k*h,k*(a+b+c))

        n += 2
    m += 1

print "Answer = {0}".format(answer)
print "Time taken = {0} seconds".format(time.clock() - start_time)
