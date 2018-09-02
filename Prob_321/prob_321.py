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

SIZE = 15

########################################

def triangle(n):
    return n*(n+1)//2

def is_triangle(n):
    #print("is_triangle({})".format(n))
    if not (((n % 3) == 0) or ((n % 9) == 1)):
        # Every triangle number is divisible by 3 or has
        # remainder 1 when divided by 9
        return False

    if n in [1, 3, 6]:
        return True
        # These cases are too small to be handled properly by the code below

    bot, top = 1, 2

    while triangle(top) < n:
        bot = top
        top *= 2
        #print("    bot = {}, top = {}, triangle({}) = {}".format(bot, top, top, top*(top+1)//2))

        if triangle(top) == n:
            return True

    while (top - bot) > 1:
        mid = (top + bot) // 2
        t = triangle(mid)
        #print("    bot = {}, mid = {} top = {}, triangle({}) = {}".format(bot, mid, top, mid, t))
        if t == n:
            #print("triangle({}) == {}, returning True".format(mid, n))
            return True
        elif t > n:
            top = mid
        else:
            bot = mid
    #print("finished iterating, returning False")
    return False


if True:  # debug code
    triangle_nums = [triangle(x+1) for x in range(25)]
    print(triangle_nums)
    for n in range(1, 300):
        print("Testing is_triangle({})".format(n))
        t = is_triangle(n)
        if n in triangle_nums:
            assert t == True, "is_triangle({}) returned False, should be True".format(n)
        else:
            assert t == False, "is_triangle({}) returned True, should be False".format(n)


########################################

def M(n):
    return n * (n+2)

answer = 0
count = 0
i = 1
while count < SIZE:
    n = M(i)
    if is_triangle(n):
        answer += i
        count += 1
        print("{}: M({:,}) = {:,} is a triangle number".format(count, i, n))
        print("With SIZE = {:,}, answer = {:,}.  ".format(count, answer), end='')
        print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
    i += 1


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
# n = 4:
# 1 M
# 2 JM
# 3 JJM
# 4 JJJM
# 5 JJJJM
# 4 JJJM
# 3 JJM
# 2 JM
# M(4) = 24
#
# n = 5:
# 1 M
# 2 JM
# 3 JJM
# 4 JJJM
# 5 JJJJM
# 6 JJJJJ M
# 5 JJJJM
# 4 JJJM
# 3 JJM
# 2 JM
# M(5) = 35
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
# M(n) = n*(n+2)
# M(3) = 15
# M(4) = 24
# M(10) = 120
