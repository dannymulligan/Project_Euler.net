#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 321
#
# Swapping Counters
#
# A horizontal row comprising of 2n + 1 squares has n red counters
# placed at one end and n blue counters at the other end, being
# separated by a single empty square in the centre. For example, when
# n = 3.
#
#     +---+---+---+---+---+---+---+
#     | R | R | R |   | B | B | B |
#     +---+---+---+---+---+---+---+
#
# A counter can move from one square to the next (slide) or can jump
# over another counter (hop) as long as the square next to that
# counter is unoccupied.
#
#     +---+---+        +---+---+---+
#     | R |   |        | R | B |   |
#     +---+---+        +---+---+---+
#        -->              ------>
#     +---+---+        +---+---+---+
#     |   | R |        |   | B | R |
#     +---+---+        +---+---+---+
#
# Let M(n) represent the minimum number of moves/actions to completely
# reverse the positions of the coloured counters; that is, move all
# the red counters to the right and all the blue counters to the left.
#
# It can be verified M(3) = 15, which also happens to be a triangle
# number.
#
# If we create a sequence based on the values of n for which M(n) is a
# triangle number then the first five terms would be:
#    1, 3, 10, 22, and 63, and their sum would be 99.
#
# Find the sum of the first forty terms of this sequence.


import sys
#print(sys.version)
import time
start_time = time.clock()

SIZE = 20

########################################

def triangle(n):
    return n*(n+1)//2

def is_triangle(n):
    """ is_triangle(n) returns 0 if n is not a triangle number
                       returns x if n is a triangle number
                       where n = x * (x + 1) / 2"""
    if not (((n % 3) == 0) or ((n % 9) == 1)):
        # Every triangle number is divisible by 3 or has
        # remainder 1 when divided by 9
        return 0

    # These cases are too small to be handled properly by the code below
    if n == 1:
        return 1
    elif n == 3:
        return 2
    elif n == 6:
        return 3

    bot, top = 1, 2
    while triangle(top) < n:
        bot = top
        top *= 2
        #print("    bot = {}, top = {}, triangle({}) = {}".format(bot, top, top, top*(top+1)//2))

        if triangle(top) == n:
            return top

    while (top - bot) > 1:
        mid = (top + bot) // 2
        t = triangle(mid)
        #print("    bot = {}, mid = {} top = {}, triangle({}) = {}".format(bot, mid, top, mid, t))
        if t == n:
            #print("triangle({}) == {}, returning True".format(mid, n))
            return mid
        elif t > n:
            top = mid
        else:
            bot = mid
    #print("finished iterating, returning False")
    return 0


if False:  # debug code
    triangle_nums = [triangle(x+1) for x in range(25)]
    print(triangle_nums)
    for n in range(1, 300):
        print("Testing is_triangle({})".format(n))
        t = is_triangle(n)
        if n in triangle_nums:
            assert triangle_nums[t-1] == n, "is_triangle({}) returned False, should be True".format(n)
        else:
            assert t == 0, "is_triangle({}) returned True, should be False".format(n)


########################################

# We need to find values of n for which there are integer solutions to
#
# M(n) = n*(n+2) = T(x) = x*(x+1)/2
#
# for the first 10 solutions we have...
#
#  1: M(   1) =    1 *    3 =        3 =     2 *    3 / 2 = triangle(   2)
#  2: M(   3) =    3 *    5 =       15 =     5 *    6 / 2 = triangle(   5)
#  3: M(  10) =   10 *   12 =      120 =    15 *   16 / 2 = triangle(  15)
#  4: M(  22) =   22 *   24 =      528 =    32 *   33 / 2 = triangle(  32)
#  5: M(  63) =   63 *   65 =     4095 =    90 *   91 / 2 = triangle(  90)
#  6: M( 133) =  133 *  135 =    17955 =   189 *  190 / 2 = triangle( 189)
#  7: M( 372) =  372 *  374 =   139128 =   527 *  528 / 2 = triangle( 527)
#  8: M( 780) =  780 *  782 =   609960 =  1104 * 1105 / 2 = triangle(1104)
#  9: M(2173) = 2173 * 2175 =  4726275 =  3074 * 3075 / 2 = triangle(3074)
# 10: M(4551) = 4551 * 4553 = 20720703 =  6437 * 6438 / 2 = triangle(6437)


def M(n):
    return n * (n+2)

answer = 0
count = 0
n = 1
t = 1
x = 2
while count < SIZE:
    m = M(n)
    while (t < m):
        t, x = t+x, x+1
    if t == m:
        answer += n
        count += 1
        print("{}: M({:,}) = {:,} = triangle({:,})".format(count, n, m, x-1), end='')
        #print("With SIZE = {:,}, answer = {:,}".format(count, answer), end='')
        print(".  Time taken = {:.2f} seconds".format(time.clock() - start_time))
    n += 1


########################################

print("With SIZE = {:,}, answer = {:,}".format(SIZE, answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))

# First working version of the code, too slow...
# With SIZE = 5, answer = 99.  Time taken = 0.01 seconds
# With SIZE = 10, answer = 8,108.  Time taken = 0.06 seconds
# With SIZE = 15, answer = 706,232.  Time taken = 6.86 seconds
# With SIZE = 16, answer = 1,607,504.  Time taken = 15.14 seconds
# With SIZE = 17, answer = 4,116,297.  Time taken = 45.64 seconds
# With SIZE = 18, answer = 9,369,300.  Time taken = 100.24 seconds

# Added a quick test to start of is_triangle()...
# With SIZE = 5, answer = 99.  Time taken = 0.00 seconds
# With SIZE = 10, answer = 8,108.  Time taken = 0.04 seconds
# With SIZE = 15, answer = 706,232.  Time taken = 4.70 seconds
# With SIZE = 16, answer = 1,607,504.  Time taken = 10.40 seconds
# With SIZE = 17, answer = 4,116,297.  Time taken = 31.01 seconds
# With SIZE = 18, answer = 9,369,300.  Time taken = 67.83 seconds

# Calculate triangle numbers as we go...
# With SIZE = 5, answer = 99.  Time taken = 0.00 seconds
# With SIZE = 10, answer = 8,108.  Time taken = 0.00 seconds
# With SIZE = 15, answer = 706,232.  Time taken = 0.30 seconds
# With SIZE = 16, answer = 1,607,504.  Time taken = 0.63 seconds
# With SIZE = 17, answer = 4,116,297.  Time taken = 1.74 seconds
# With SIZE = 18, answer = 9,369,300.  Time taken = 3.62 seconds
# With SIZE = 19, answer = 23,991,622.  Time taken = 10.13 seconds
# With SIZE = 20, answer = 54,608,372.  Time taken = 21.22 seconds
# With SIZE = 21, answer = 139,833,515.  Time taken = 59.06 seconds
# With SIZE = 22, answer = 318,281,016.  Time taken = 124.00 seconds
#
# 5: M(63) = 4,095 = triangle(90).  Time taken = 0.00 seconds
# 10: M(4,551) = 20,720,703 = triangle(6,437).  Time taken = 0.00 seconds
# 15: M(430,440) = 185,279,454,480 = triangle(608,735).  Time taken = 0.28 seconds
# 16: M(901,272) = 812,293,020,528 = triangle(1,274,592).  Time taken = 0.58 seconds
# 17: M(2,508,793) = 6,294,047,334,435 = triangle(3,547,970).  Time taken = 1.61 seconds
# 18: M(5,253,003) = 27,594,051,024,015 = triangle(7,428,869).  Time taken = 3.38 seconds
# 19: M(14,622,322) = 213,812,329,916,328 = triangle(20,679,087).  Time taken = 9.40 seconds
# 20: M(30,616,750) = 937,385,441,796,000 = triangle(43,298,624).  Time taken = 19.69 seconds
# With SIZE = 20, answer = 54,608,372
#
# This is much faster than the previous attempts, but still MUCH too slow to
# solve this problem.  :-(

# How to rearrange the squares...
#
#   0 rrr.bbb
#   1 rr.Rbbb  Move  init-step
#   2 rrBr.bb  Jump
#   3 rrbrB.b  Move
#   4 rrb.bRb  Jump
#   5 r.bRbrb  Jump
#   6 .Rbrbrb  Move
#   7 Br.rbrb  Jump
#   8 brBr.rb  Jump
#   9 brbrBr.  Jump
#  10 brbrb.R  Move
#  11 brb.bRr  Jump
#  12 b.bRbrr  Jump
#  13 bB.rbrr  Move
#  14 bbBr.rr  Jump
#  15 bbb.Rrr  Move  end-step
#
# n = 3:
# 1 M
# 2 JM
# 3 JJM
# 4 JJJM
# 3 JJM
# 2 JM
# M(3) = 15
#
# By pattern matching, it looks like the M(10) case will be...
#
# n = 10:
#  1 M
#  2 JM
#  3 JJM
#  4 JJJM
#  5 JJJJM
#  6 JJJJJ M
#  7 JJJJJ JM
#  8 JJJJJ JJM
#  9 JJJJJ JJJM
# 10 JJJJJ JJJJM
# 11 JJJJJ JJJJJ M
# 10 JJJJJ JJJJM
#  9 JJJJJ JJJM
#  8 JJJJJ JJM
#  7 JJJJJ JM
#  6 JJJJJ M
#  5 JJJJM
#  4 JJJM
#  3 JJM
#  2 JM
# M(10) = 120
#
# The formula seems to be... M(n) = n*(n+2)
#
# M(3) = 15
# M(4) = 24
# M(10) = 120
# M(22) = 528
