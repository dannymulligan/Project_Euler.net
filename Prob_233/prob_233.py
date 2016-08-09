#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 233
#
# Lattice points on a circle
#
# Let f(N) be the number of points with integer coordinates that are
# on a circle passing through (0,0), (N,0),(0,N), and (N,N).
#
# It can be shown that f(10000) = 36.
#
# What is the sum of all positive integers N <=10**11 such that f(N) = 420 ?
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

#
#              |
#              |          ***************
#              |     *****               *****
#              | ****                         ****
#             *+*                                 *+*
#           ** |                                     **
#         **   |                                       **
#        *     |                                         *
#       *      |                                          *
#      *       |                                           *
#     *        |                                            *
#    *         |                                             *
#    *         |                                             *
#    *         |                 +                           *
#    *         |                                             *
#    *         |                                             *
#     *        |                                            *
#      *       |                                           *
#       *      |                                          *
#        *     |                                         *
#         **   |                                       **
#           ** |                                     **
#  -----------*+*---------------------------------*+*-----------
#              | ****                         ****
#              |     *****               *****
#              |          ***************
#              |
#

import sys
from fractions import gcd
import time
start_time = time.clock()

########################################


def even(n):
    return (n % 2) == 0


def odd(n):
    return (n % 2) == 1


########################################

def pythagorean_triple(limit):
    '''Return pythagorean triples (a, b, c)
    where a**2 + b**2 = c**3
    with a < b
    and c < limit'''
    p = 1
    while True:
        p += 1
        if (p**2 + 1) >= limit:
            break

        for q in range(1, p):
            a = 2*p*q
            b = (p*p - q*q)
            c = (p*p + q*q)

            if gcd(a, b) != 1:
                continue
            if a > b:
                b, a = a, b

            if c > limit:
                break

            yield (a, b, c)
            n = 2
            while n*c < limit:
                yield (n*a, n*b, n*c)
                n += 1
    return

if False:
    # Test code
    expected_answer_count = 20  # 20 pythagorean triples with c < 51
    answer_count = 0
    for (a, b, c) in pythagorean_triple(51):
        if a**2 + b**2 - c**2 == 0:
            answer_count += 1
            print("({:2}, {:2}, {:2})".format(a, b, c), end='')
            if gcd(a, b) == 1:
                print()
            else:
                print(" = {:2} * ({:2}, {:2}, {:2})"
                      .format(gcd(a, b),
                              a//gcd(a, b),
                              b//gcd(a, b),
                              c//gcd(a, b)))
        else:
            print("ERROR (a, b, c) = ({}, {}, {})".format(a, b, c))
    assert answer_count == expected_answer_count
    sys.exit()

########################################

# 2016-08-08 searched to N = 110,000 and found 0 cases with 420 lattice points
# 2016-08-08 searched to N = 10,000 and found 60 cases with 108 lattice points
# 2016-08-08 searched to N = 1,000 and found 8 cases with 60 lattice points
# 2016-08-08 searched to N = 100 and found 2 cases with 36 lattice points
# 2016-08-08 searched to N = 30 and found 1 cases with 20 lattice points

MatchCount = 0
Now = time.clock()
for n in range(1, 30):
    if (n % 10**3) == 0:
        PrevNow = Now
        Now = time.clock()
        TotalTime = Now - start_time
        DeltaTime = Now - PrevNow
        print("N = {:,} after {:,.1f} seconds, delta {:,.1f} seconds"
              .format(n, TotalTime, DeltaTime))

    ncnt = 4  # the 4 given points
    for x in range(1, n//2):
        y = ((n**2)/2 - (x-n/2)**2)**0.5 + n/2
        yint, yfrac = divmod(y, 1)
        yint = int(yint)
        check = (n**2)/2 - (x-n/2)**2 - (yint-n/2)**2
        if check < 0.00001:
            ncnt += 8  # because of symmetry
            print("N = {:,}: x = {:6,}, y = {:6,}".format(n, x, yint))

    if ncnt >= 10:
        if ncnt == 20:
            MatchCount += 1
            print("F({:,}) = {:,} = Match {}".format(n, ncnt, MatchCount))
        else:
            print("F({:,}) = {:,}".format(n, ncnt))


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
