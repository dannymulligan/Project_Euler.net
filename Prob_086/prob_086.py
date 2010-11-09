#!/usr/bin/python
#
# Project Euler.net Problem 86
#
# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5
# by 3, and a fly, F, sits in the opposite corner. By travelling on
# the surfaces of the room the shortest "straight line" distance from
# S to F is 10 and the path is shown on the diagram.
# 
#          +----------------+ F 
#         /                /|
#        /                / |
#       /                /  |
#      +----------------+   +
#      |                |  /
#      |                | /
#      |                |/
#   S  +----------------+
#
# However, there are up to three "shortest" path candidates for any
# given cuboid and the shortest route is not always integer.
# 
# By considering all cuboid rooms up to a maximum size of M by M by M,
# there are exactly 2060 cuboids for which the shortest distance is
# integer when M=100, and this is the least value of M for which the
# number of solutions first exceeds two thousand; the number of
# solutions is 1975 when M=99.
# 
# Find the least value of M such that the number of solutions first
# exceeds one million.
#
# Answer:
# Solved
# ?? problems solved
# Position #?? on level 2

# The three paths can be found by flattening the cuboid in 3 ways.
# Then the shortest distance will be given by the hypotenuse of the
# right angle triangle that is formed.
#
# Example: Given a cuboid of dimensions 3, 5, 6, we can flatten in the
# following ways
#
# 6x5 + 6x3 surfaces
#
#     +-----+-----+-----+-----+-----+-----+ F
#     |                                   |
#     +     +     +     +     +     +     +
#     |               6 x 3               |
#     +     +     +     +     +     +     +
#     |                                   |
#     +-----+-----+-----+-----+-----+-----+
#     |                                   |
#     +     +     +     +     +     +     +
#     |                                   |
#     +     +     +     +     +     +     +
#     |               6 x 5               |
#     +     +     +     +     +     +     +
#     |                                   |
#     +     +     +     +     +     +     +
#     |                                   |
#   S +-----+-----+-----+-----+-----+-----+
#
# Shortest path is given by
#     P^2 = (5+3)^2 + 6^2 = 8^2 + 6^2 = 64 + 36 = 100
#     P = sqrt(100) = 10
#
# 6x5 + 5x3 surfaces
#
#     +-----+-----+-----+-----+-----+-----+-----+-----+-----+ F
#     |                                   |                 |
#     +     +     +     +     +     +     +     +     +     +
#     |                                   |                 |
#     +     +     +     +     +     +     +     +     +     +
#     |               6 x 5               |      5 x 3      |
#     +     +     +     +     +     +     +     +     +     +
#     |                                   |                 |
#     +     +     +     +     +     +     +     +     +     +
#     |                                   |                 |
#   S +-----+-----+-----+-----+-----+-----+-----+-----+-----+
#
# Shortest path is given by
#     P^2 = (6+3)^2 + 5^2 = 9^2 + 5^2 = 81 + 25 = 106
#     P = sqrt(106)
#
# 5x3 + 6x3 surfaces
#
#     +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+ F
#     |                                   |                             |
#     +     +     +     +     +     +     +     +     +     +     +     +
#     |               6 x 3               |            5 x 3            |
#     +     +     +     +     +     +     +     +     +     +     +     +
#     |                                   |                             |
#   S +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
#
# Shortest path is given by
#     P^2 = (6+5)^2 + 3^2 = 11^2 + 3^2 =121 + 9 = 130
#     P = sqrt(130)
#
# If A <= B <= C, the solution that will give the shortest path will be
# on the triangle with sides A+B & C.
#
# We restrict our search to A <= B <= C.  This means that we will
# search about 1/6 as much space, but we need to count some items more
# than once to compensate.
#
#     For items with A=B=C: we count them once
#         (A, A, A)  <-- we iterate this one
#     For items with A<B=C: we count them three times
#         (A, C, C)  <-- we iterate this one
#         (C, A, C)  <-- skip this one
#         (A, C, C)  <-- skip this one
#     For items with A=B<C: we count them 3 times
#         (A, A, C)  <-- we iterate this one
#         (A, C, A)  <-- skip this one
#         (C, A, A)  <-- skip this one
#     For items with A<B<C: we count them 6 times
#         (A, B, C)  <-- we iterate this one
#         (A, C, B)  <-- skip this one
#         (B, A, C)  <-- skip this one
#         (B, C, A)  <-- skip this one
#         (C, A, B)  <-- skip this one
#         (C, B, A)  <-- skip this one
#
# Oops, the reference solution only counts (A,B,C) for A<=B<=C

# If we've found all the solutions up to M, and given A<=B<=C, then
# going to M+1 requires us to search the following range...
#     A = 1..M+1, B = 1..M+1, C = M+1
#

# Solution given various values of M
# M  solutions
# M=10, answer=14
# M=99, answer=1975
# M=100, answer=2060
# M=150, answer=4918
# M=200, answer=9034
# M=250, answer=14376
# M=300, answer=21928
# M=350, answer=29906
# M=400, answer=40432
# M=450, answer=51590
# M=500, answer=64210
# M=550, answer=78752
# M=600, answer=95506
# M=700, answer=132288
# M=750, answer=152547


MAX = 250
START = 10

squares = []
for A in range(1,3*MAX):
    squares.append(A*A)

def do_it():
    cnt0 = 0
    for C in range(1,START+1):
        for B in range(1,C+1):
            for A in range(1,B+1):
                hyposq = (A+B)**2 + C**2
                if (hyposq in squares):
                    #print "({0},{1},{2})".format(A, B, C)
                    cnt0 += 1
                    #if (A==B==C):  # Counts 1x
                    #    continue
                    #if (A==B<C):  # Counts 3x
                    #    #print "({0},{1},{2})".format(B, C, B)
                    #    #print "({0},{1},{2})".format(C, B, B)
                    #    cnt0 += 2
                    #if (A<B==C):  # Counts 3x
                    #    #print "({0},{1},{2})".format(B, A, C)
                    #    #print "({0},{1},{2})".format(B, C, A)
                    #    cnt0 += 2
                    #if (A<B<C):  # Counts 6x
                    #    #print "({0},{1},{2})".format(A, C, B)
                    #    #print "({0},{1},{2})".format(B, A, C)
                    #    #print "({0},{1},{2})".format(B, C, A)
                    #    #print "({0},{1},{2})".format(C, A, B)
                    #    #print "({0},{1},{2})".format(C, B, A)
                    #   cnt0 += 5

    print "M={0}, answer={1}".format(START, cnt0)

    for C in range(START+1,MAX+1):
        for B in range(1,C+1):
            for A in range(1,B+1):
                hyposq = (A+B)**2 + C**2
                if (hyposq in squares):
                    #print "({0},{1},{2})".format(A, B, C)
                    cnt0 += 1
                    #if (A==B==C):  # Counts 1x
                    #    continue
                    #if (A==B<C):  # Counts 3x
                    #    #print "({0},{1},{2})".format(B, C, B)
                    #    #print "({0},{1},{2})".format(C, B, B)
                    #    cnt0 += 2
                    #if (A<B==C):  # Counts 3x
                    #    #print "({0},{1},{2})".format(B, A, C)
                    #    #print "({0},{1},{2})".format(B, C, A)
                    #    cnt0 += 2
                    #if (A<B<C):  # Counts 6x
                    #    #print "({0},{1},{2})".format(A, C, B)
                    #    #print "({0},{1},{2})".format(B, A, C)
                    #    #print "({0},{1},{2})".format(B, C, A)
                    #    #print "({0},{1},{2})".format(C, A, B)
                    #    #print "({0},{1},{2})".format(C, B, A)
                    #   cnt0 += 5
        if ((C % 5) == 0):
            print "M={0}, answer={1}".format(C, cnt0)


do_it()
