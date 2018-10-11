#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 351
#
# Hexagon orchards
#
# A hexagonal orchard of order n is a triangular lattice made up of
# points within a regular hexagon with side n. The following is an
# example of a hexagonal orchard of order 5:
#
#               X   .   .   .   .   X
#             .   X   .   X   .   X   .
#           .   .   X   .   .   X   .   .
#         .   X   .   X   .   X   .   X   .
#       .   .   .   .   .   .   .   .   .   .
#     X   X   X   X   .   O   .   X   X   X   X
#       .   .   .   .   .   .   .   .   .   .
#         .   X   .   X   .   X   .   X   .
#           .   .   X   .   .   X   .   .
#             .   X   .   X   .   X   .
#               X   .   .   .   .   X
#
# Highlighted in green are the points which are hidden from the center
# by a point closer to it. It can be seen that for a hexagonal orchard
# of order 5, 30 points are hidden from the center.
#
# Let H(n) be the number of points hidden from the center in a
# hexagonal orchard of order n.
#
# H(5) = 30. H(10) = 138. H(1,000) = 1177848.
#
# Find H(100,000,000).


import sys
#print(sys.version)
import time
start_time = time.clock()

###############################################################################
SIZE = 100000000

import primes
prime_table = primes.calculate_primes(SIZE+1, make_prime_list=False)
phi_table = primes.calculate_phi(prime_table)

def Hfast(n):
    ans = 0
    for i in range(2,n+1):
        ans += i - phi_table[i]
    return ans * 6



###############################################################################

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

def H(n, debug=False):
    max_x = 0
    max_y = 0
    max_xy = 0
    points = 0
    answer = 0
    # Calculate points hidden by (1,0)
    x, y = 1, 0
    a = (n // (x+y)) - 1
    answer += a
    if a > 0:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_xy = max(max_xy, x+y)
        points += 1
    if debug:
        print("({},{}) hides {} points in the form (a,0)".format(x, y, a))
        result = "    " + ', '.join(['({},{})'.format(x*_a, y*_a) for _a in range(2, a+2)])
        print(result)

    # Calculate points hidden by (1,1)
    x, y = 1, 1
    a = (n // (x+y)) - 1
    answer += a
    if a > 0:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_xy = max(max_xy, x+y)
        points += 1
    if debug:
        print("({},{}) hides {} points in the form (a,a)".format(x, y, a))
        result = "    " + ', '.join(['({},{})'.format(x*_a, y*_a) for _a in range(2, a+2)])
        print(result)

    # Calculate points hidden by (x, y) other than the above
    for y in range(1, n//4+1):
        for x in range(y+1, n//2 - y + 1):
            if gcd(x, y) != 1:
                continue
            if (x+y) > n:
                continue
            #print("========\nTrying ({},{})\n========".format(x, y))
            a = (n // (x+y)) - 1
            answer += 2*a
            if a > 0:
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                max_xy = max(max_xy, x+y)
                points += 1

            if debug and (a > 0):
                if (x == y):
                    print("({x},{y}) hides {a} points in the form ({x}a,{y}a)".format(x=x, y=y, a=a))
                    result = "    "
                    result += ', '.join(['({},{})'.format(x*_a, y*_a) for _a in range(2, a+2)])
                    print(result)
                else:
                    print("({x},{y}) hides {a} points in the form ({x}a,{y}a) & ({y}a,{x}a)".format(x=x, y=y, a=2*a))
                    result = "    "
                    result += ', '.join(['({},{})'.format(x*_a, y*_a) for _a in range(2, a+2)])
                    result += ', '
                    result += ', '.join(['({},{})'.format(y*_a, x*_a) for _a in range(2, a+2)])
                    print(result)

    print("max_x = {}, max_y = {}, max_xy = {}, points = {}/{:.2f}%".format(max_x, max_y, max_xy, points, 100*points/n/n))
    return answer*6


###############################################################################

debug = False
if debug == True:
    solutions = [
        (   10,       138),
        (   11,       144),
        (   12,       192),
        (   15,       288),
        (   16,       336),
        (   17,       342),
        (   18,       414),
        (   19,       420),
        (   20,       492),
        (   25,       750),
        (   26,       834),
        (   27,       888),
        (   28,       984),
        (   29,       990),
        (   30,      1122),
        (   40,      1980),
        (   49,      2826),
        (   50,      3006),
        (  100,     12036),
        ( 1000,   1177848),
        ( 2000,   4706472),
        ( 3000,  10591872),
        ( 4000,  18830388),
        ( 5000,  29412252),
        (10000, 117645084),
        (15000, 264679104),
        (20000, 470517624),
        (25000, 735194460),
    ]
    for n, h in solutions:
        #if n > 20:  break
        start_time = time.clock()
        print()
        s = Hfast(n)
    #    s = H(n, False)
    #    s = H(n, True)
        if (s == h):
            print("H({:,}) = {:,} (calculated in {:.2f} seconds)".format(n, s, time.clock() - start_time))
        else:
            print("H({:,}) = {:,} incorrect, expecting {},  (calculated in {:.2f} seconds)".format(n, s, h, time.clock() - start_time))
        assert s == h

n = SIZE
print("Answer = H({:,}) = {:,}".format(n, Hfast(n)))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))


#
#               X   .   .   .   .   X
#             .   X   .   X   .   X   .
#           .   .   X   .   .   X   .   .
#         .   X   .   X   .   X   .   X   .
#       .   .   .   .   .   .   .   .   .   .
#     X   X   X   X   .   O   .   X   X   X   X
#       .   .   .   .   .   .   .   .   .   .
#         .   X   .   X   .   X   .   X   .
#           .   .   X   .   .   X   .   .
#             .   X   .   X   .   X   .
#               X   .   .   .   .   X
#
# This is the same as the following repeated 6 times
#
#                                     .
#                                   .   .
#                                 .   X   .
#                               .   .   .   .
#                             .   X   X   X   X
#
# Adding numbering
#
#               .
#             (1,4)
#            .     .
#          (1,3) (2,3)
#         .     X     .
#       (1,2) (2,2) (3,2)
#      .     .     .     .
#    (1,1) (2,1) (3,1) (4,1)
#   .     X     X     X     X
# (1,0) (2,0) (3,0) (4,0) (5,0)
#
# points (1,0) lead to p hidden points of the form (a,0)
# p = maximum value of a minus 1
# maximum value of a = n
#
# points (x,y) lead to p hidden points of the form (ax,ay)
# p = maximum value of a minus 1
# maximum value of a is when ax+ay <= n, a = n // (x + y)
#
# when x = non-prime and y = non-prime, then this point is hidden
# the only solutions are for (x, y) points with
#     x = prime, and y = non-prime
#     x = non-prime, and y = prime
#     x = prime, and y = prime
#
# we will cut our work in half by only considering points with y = prime
# and adjust for the x = prime, and y = non-prime points by multiplying any
# x = prime, and y = non-prime points by 12 instead of 6, but multiplying the
# x = prime, and y = prime points by 6
#
# when x = prime and y = non-prime, then this point appears 6 times
# but we can include the (y, x) equivalent point by multiplying by 12
